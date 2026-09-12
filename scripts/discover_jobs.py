"""Discover roles and write them to the application queue as JSON.

This is the first half of the pipeline. It finds roles, scores them, drops
duplicates, picks a resume, and writes one JSON file per role into
`automation/queue/pending/`.

It deliberately stops there. The second half - actually submitting the
application - is done by an external agent that reads the queue. See
`automation/AGENT_CONTRACT.md` for the interface. Nothing in this file
touches an employer's careers portal, and nothing here sends mail.

Run:
    python scripts/discover_jobs.py            # write new queue entries
    python scripts/discover_jobs.py --dry-run  # print, write nothing
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import jobs_sources as js  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
QUEUE = ROOT / "automation" / "queue"
PENDING = QUEUE / "pending"
SUBMITTED = QUEUE / "submitted"
SKIPPED = QUEUE / "skipped"
LEDGER = QUEUE / "seen.json"

KIT = ROOT / "agent-kit"
STRATEGY = KIT / "strategy.json"
RULES = KIT / "rules.json"

# Stamped as the first key of every queue file so an agent that opens one JSON
# in isolation still sees the rules. Kept short on purpose - the full set is in
# agent-kit/rules.json and the interface spec is automation/AGENT_CONTRACT.md.
QUEUE_RULES = {
    "read_first": "agent-kit/START_HERE.md",
    "full_rules": "agent-kit/rules.json",
    "contract": "automation/AGENT_CONTRACT.md",
    "must": [
        "Claim this role (status: claimed, agent.claimed_by, agent.claimed_at) and commit before touching the portal.",
        "Attach package.resume verbatim. Do not substitute a different resume.",
        "Move this file to submitted/ with a confirmation_ref, or to skipped/ with a reason. Commit the move.",
    ],
    "never": [
        "Never store credentials, cookies, or tokens in this repository - it is public and git history is permanent.",
        "Never answer immigration, work-authorization, salary-history, EEO, or attestation fields. Stop and skip instead.",
        "Never send email as Yasir. Draft only.",
        "Never write 'OCC' - the examiner history is the Florida Office of Financial Regulation.",
        "Never write 'Dr. Malik' or 'CIA certified' - the DBA and the CIA are both in progress.",
    ],
    "facts": {
        "name": "Yasir A. Malik",
        "email": "YasirAMalik@gmail.com",
        "phone": "+1 (786) 704-8536",
        "location": "Newark, NJ",
        "current_employer": "None - Citi role ended April 2026",
    },
}

# Resume selection. First pattern that matches the title wins; the master
# resume is the fallback. These are the files that actually exist in the repo -
# a package that names a missing file is worse than one that names the generic.
RESUME_RULES: list[tuple[str, str]] = [
    (r"\b(supervisory risk|supervisory control|business control|first.line control|risk governance)",
     "applications/resume/Yasir_Malik_Resume_GS_GBM_SRC_VP.pdf"),
    (r"\b(cib|commercial.*investment|capital|basel|treasury|liquidity|"
     r"regulatory report|financial control)\b",
     "applications/resume/Yasir_Malik_Resume_JPM_CIB_Finance_Audit.pdf"),
    (r"\b(responsible ai|ai governance|ai risk|model risk|ai polic)\b",
     "applications/resume/Yasir_Malik_Resume_Google_CloudRAI_Branded.pdf"),
    # No trailing \b on stems: "program manag" must match "Program Management",
    # and \b after "manag" requires a non-word character that never comes.
    (r"\b(program manag|portfolio|pmo|transformation)",
     "applications/resume/Yasir_Malik_Resume_PGIM_AI_Director.pdf"),
    (r"\b(data governance|chief data|data strateg)",
     "applications/resume/Yasir_Malik_Resume_CUNY_DataGovernance.pdf"),
    (r"\b(inspector general|public sector|integrity|compliance officer)",
     "applications/resume/Yasir_Malik_Resume_NYC_InspectorGeneral.pdf"),
]
# The branded GenAI-risk master (builders/build_genai_risk_branded.py) is the
# default for every role that no tailored rule claims. Owner's decision, 3 Sep
# 2026: the Audit the Algorithm wordmark goes on every application. It carries
# the research-trajectory table and the corrected examiner history, and at
# ~7 KB attaches anywhere. The unbranded twin (same content, Chromium build)
# remains at Yasir_Malik_Resume_GenAI_Risk_Master.pdf if a form rejects it.
DEFAULT_RESUME = "applications/resume/Yasir_Malik_Resume_GenAI_Risk_Master_Branded.pdf"

MIN_SCORE = 3  # anything below this is noise; it never reaches the queue


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def job_id(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


def pick_resume(title: str) -> str:
    low = title.lower()
    for pattern, path in RESUME_RULES:
        if re.search(pattern, low):
            return path
    return DEFAULT_RESUME


def load_seen() -> dict:
    if LEDGER.exists():
        return json.loads(LEDGER.read_text())
    return {}


def is_sponsor(company: str) -> bool:
    low = company.lower()
    return any(s in low for s in js.SPONSOR_EMPLOYERS)


def is_excluded(company: str) -> bool:
    low = company.lower()
    return any(x in low for x in js.EXCLUDED_EMPLOYERS)


def load_strategy() -> dict:
    """The three streams. Owner-editable config, not code.

    agent-kit/strategy.json is the single place target employers are added or
    removed, so a non-programmer (or another agent) can change who gets
    searched without touching this file.
    """
    return json.loads(STRATEGY.read_text(encoding="utf-8"))


def collect(report: js.SourceReport) -> list[dict]:
    """Run every verified source in every stream.

    A dead source reports and the run continues - a source that breaks and says
    nothing is worse than no source at all. Targets marked verified: false have
    no working endpoint yet and are skipped rather than guessed at; they surface
    in the briefing as "needs an endpoint" so they get looked up rather than
    invented.
    """
    rows: list[dict] = []
    google_queries: list[str] = []

    for stream in load_strategy()["streams"]:
        sid = stream["id"]
        search_hint = stream["keywords"][0] if stream.get("keywords") else ""

        for target in stream["targets"]:
            if target.get("excluded") or not target.get("verified"):
                continue
            company, board = target["company"], target.get("board")

            if board == "workday":
                found = js.fetch_workday(
                    target["tenant"], target["site"], company, report,
                    search=search_hint, host=target.get("host", "wd1"),
                )
            elif board == "greenhouse":
                found = js.fetch_greenhouse(target["slug"], company, report)
            elif board == "google-careers":
                # Batched into one pass after the loop; the Google endpoint is
                # queried by keyword, not by employer.
                google_queries += stream["keywords"][:4]
                continue
            else:
                continue

            for row in found:
                row["stream"] = sid
            rows += found

    if google_queries:
        found = js.fetch_google(sorted(set(google_queries)), report)
        for row in found:
            row["stream"] = "ai"
        rows += found

    return rows


def build_entry(row: dict, score: int, reasons: list[str], stream: str) -> dict:
    return {
        # First key on purpose. An agent reading one file out of context still
        # gets the rules before it gets the role.
        "_rules": QUEUE_RULES,
        "id": job_id(row["url"]),
        "discovered_at": now(),
        "stream": stream,
        "company": row["company"],
        "title": row["title"],
        "location": row.get("location") or "",
        "url": row["url"],
        "score": score,
        "score_reasons": reasons,
        "sponsor_employer": is_sponsor(row["company"]),
        "status": "pending",
        "package": {
            "resume": pick_resume(row["title"]),
            "cover_letter": None,
        },
        # Everything below is written by the submitting agent, not by this
        # script. See automation/AGENT_CONTRACT.md.
        "agent": {
            "claimed_by": None,
            "claimed_at": None,
            "submitted_at": None,
            "confirmation_ref": None,
            "notes": None,
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    for d in (PENDING, SUBMITTED, SKIPPED):
        d.mkdir(parents=True, exist_ok=True)

    report = js.SourceReport()
    rows = collect(report)
    seen = load_seen()

    written, skipped_dupe, skipped_low, skipped_excl = 0, 0, 0, 0
    fresh: list[dict] = []

    for row in rows:
        if not row.get("url") or not row.get("title"):
            continue
        if is_excluded(row["company"]):
            skipped_excl += 1
            continue

        jid = job_id(row["url"])
        if jid in seen:
            skipped_dupe += 1
            continue

        stream = row.get("stream", "gsib")

        if stream == "adjunct":
            # Universities post plenty of non-teaching roles. Score the
            # teaching titles first here, and only fall back to the corporate
            # rubric for things like a university's own internal-audit opening.
            score = js.score_teaching(row["title"])
            reasons = ["teaching title"]
            if score < MIN_SCORE:
                score, reasons = js.score_role(
                    row["title"], row["company"], row.get("location") or ""
                )
        else:
            score, reasons = js.score_role(
                row["title"], row["company"], row.get("location") or ""
            )
            if score < MIN_SCORE:
                teach = js.score_teaching(row["title"])
                if teach >= MIN_SCORE:
                    score, reasons, stream = teach, ["teaching title"], "adjunct"

        if score < MIN_SCORE:
            skipped_low += 1
            continue

        entry = build_entry(row, score, reasons, stream)
        fresh.append(entry)
        seen[jid] = {"url": row["url"], "first_seen": entry["discovered_at"]}
        written += 1

    fresh.sort(key=lambda e: (-e["score"], not e["sponsor_employer"]))

    if args.dry_run:
        for e in fresh:
            flag = "sponsor" if e["sponsor_employer"] else "-"
            print(f"{e['score']}  {flag:8}  {e['company']:22}  {e['title'][:60]}")
    else:
        for e in fresh:
            (PENDING / f"{e['id']}.json").write_text(
                json.dumps(e, indent=2) + "\n"
            )
        LEDGER.write_text(json.dumps(seen, indent=2, sort_keys=True) + "\n")

    print(
        f"\nqueued {written}  |  duplicate {skipped_dupe}  "
        f"|  below score {skipped_low}  |  excluded employer {skipped_excl}",
        file=sys.stderr,
    )
    if report.failures:
        print("\nDEAD SOURCES (fix these, do not ignore them):", file=sys.stderr)
        for name, state, _ in report.failures:
            print(f"  {name}: {state}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
