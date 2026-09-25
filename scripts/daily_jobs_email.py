"""Daily job search + email digest.

Runs from GitHub Actions every weekday morning. Two streams:

  CORPORATE - VP/Director AI governance, audit, and risk roles, ranked with
              sponsor employers weighted up and the past employer ranked down.
  TEACHING  - adjunct / lecturer roles. Universities are H-1B cap-exempt, so
              this stream is worth its own pass.

Sources that fail are named in the digest under "Source health" rather than
silently contributing nothing - a quiet source looks identical to a quiet
job market, and those need to be told apart.

Required environment variables:
    GMAIL_ADDRESS   - the From / To address (e.g. YasirAMalik@gmail.com)
    GMAIL_APP_PASS  - a Gmail App Password (not the account password). Create at
                      https://myaccount.google.com/apppasswords - requires 2FA.

Optional:
    EXTRA_RECIPIENTS - comma-separated additional To addresses.
"""

from __future__ import annotations

import mimetypes
import os
import smtplib
import ssl
import sys
from datetime import date
from email.message import EmailMessage
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from jobs_sources import (  # noqa: E402
    SourceReport,
    fetch_google,
    fetch_greenhouse,
    fetch_workday,
    score_role,
    score_teaching,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
QUEUE = REPO_ROOT / "automation" / "queue"

GOOGLE_QUERIES = [
    "AI governance", "responsible AI", "model risk", "internal audit",
    "AI compliance", "AI policy", "regulatory audit",
]

# Corporate employers. Workday tenants are best-effort: any that are wrong
# announce themselves in the digest's source-health block on the first run.
WORKDAY_CORPORATE = [
    # (tenant, site, company, search, host)
    ("prudential", "PRUDENTIAL_CAREERS", "Prudential / PGIM", "audit", "wd5"),
    ("metlife", "MetLife_Careers", "MetLife", "risk", "wd5"),
    ("bnymellon", "BNY_Careers", "BNY", "audit", "wd1"),
    ("statestreet", "Global", "State Street", "audit", "wd1"),
    ("wellsfargojobs", "Wells_Fargo_Jobs", "Wells Fargo", "audit", "wd1"),
]

GREENHOUSE_CORPORATE = [("anthropic", "Anthropic")]

# Teaching stream. NJ-first: Newark is home.
WORKDAY_TEACHING = [
    ("rutgers", "Rutgers_Careers", "Rutgers University", "adjunct", "wd1"),
    ("njit", "NJIT_Careers", "NJIT", "adjunct", "wd1"),
]


def rank_corporate(jobs: list[dict]) -> list[dict]:
    ranked = []
    seen = set()
    for job in jobs:
        key = (job["company"].lower(), (job["title"] or "").lower())
        if key in seen:
            continue
        seen.add(key)
        score, tags = score_role(job["title"], job["company"], job.get("location", ""))
        if score < 3:
            continue
        job["score"], job["tags"] = score, tags
        ranked.append(job)
    ranked.sort(key=lambda j: (-j["score"], "sponsor" not in j["tags"], j["company"]))
    return ranked


def rank_teaching(jobs: list[dict]) -> list[dict]:
    out = []
    for job in jobs:
        score = score_teaching(job["title"])
        if score:
            job["score"] = score
            out.append(job)
    out.sort(key=lambda j: -j["score"])
    return out


def _row_html(job: dict) -> str:
    badges = ""
    if "sponsor" in job.get("tags", []):
        badges += " <span style='background:#e8f0e4;color:#3d5636;padding:1px 6px;border-radius:3px;font-size:11px'>sponsor</span>"
    if "past-employer" in job.get("tags", []):
        badges += " <span style='background:#f0ece4;color:#7a6a4a;padding:1px 6px;border-radius:3px;font-size:11px'>past employer</span>"
    return (f"<li><b>[{job['score']}] {job['company']}</b> - "
            f"<a href='{job['url']}'>{job['title']}</a>"
            f" <span style='color:#666'>{job.get('location','')}</span>{badges}</li>")


def queue_counts() -> dict[str, int]:
    """Counts from automation/queue/ - the discover_jobs.py pipeline.

    This digest's own corporate/teaching lists come from a separate,
    older scoring pass (see module docstring). The queue is the one an
    external agent actually works from, so its backlog has to be visible
    here or it silently grows unseen.
    """
    counts = {}
    for name in ("pending", "submitted", "skipped"):
        d = QUEUE / name
        counts[name] = len(list(d.glob("*.json"))) if d.exists() else 0
    return counts


def build_email_body(corporate: list[dict], teaching: list[dict],
                     report: SourceReport) -> tuple[str, str]:
    today = date.today().isoformat()
    p: list[str] = [f"Daily jobs digest - {today}", ""]
    h: list[str] = [f"<h2>Daily jobs digest - {today}</h2>"]

    top = corporate[:8]
    p.append(f"CORPORATE - {len(corporate)} role(s) scored, top {len(top)}:")
    h.append(f"<h3>Corporate ({len(corporate)} scored)</h3><ul>")
    for job in top:
        tag = " [sponsor]" if "sponsor" in job.get("tags", []) else ""
        p.append(f"  [{job['score']}] {job['company']} - {job['title']}{tag}")
        p.append(f"      {job['url']}")
        h.append(_row_html(job))
    if not top:
        p.append("  (nothing cleared the bar today)")
        h.append("<li>(nothing cleared the bar today)</li>")
    h.append("</ul>")

    p.extend(["", f"TEACHING - {len(teaching)} role(s):"])
    h.append(f"<h3>Teaching ({len(teaching)})</h3><ul>")
    for job in teaching[:6]:
        p.append(f"  [{job['score']}] {job['company']} - {job['title']}")
        p.append(f"      {job['url']}")
        h.append(_row_html(job))
    if not teaching:
        p.append("  (none today)")
        h.append("<li>(none today)</li>")
    h.append("</ul>")

    # Source health: never let a broken source look like a quiet market.
    p.extend(["", "SOURCE HEALTH:"])
    h.append("<h3>Source health</h3><ul>")
    for name, status, count in report.rows:
        line = f"  {name}: {status}" + (f" ({count})" if status == "ok" else "")
        p.append(line)
        colour = "#3d5636" if status == "ok" else "#a33"
        h.append(f"<li style='color:{colour}'>{name}: {status}"
                 f"{f' ({count})' if status == 'ok' else ''}</li>")
    h.append("</ul>")
    if report.failures:
        note = ("Some sources failed - the counts above are incomplete. "
                "Fix the tenant/site strings in scripts/jobs_sources.py.")
        p.extend(["", note])
        h.append(f"<p style='color:#a33'><b>{note}</b></p>")

    q = queue_counts()
    backlog_line = (
        f"QUEUE (automation/queue/, separate from the lists above): "
        f"{q['pending']} pending, {q['submitted']} submitted, {q['skipped']} skipped."
    )
    p.extend(["", backlog_line])
    if q["pending"] and not q["submitted"]:
        note = (f"{q['pending']} roles are queued and NONE have been submitted - "
                f"run the local runner (automation/runner/) or work "
                f"automation/queue/pending/ directly.")
        p.append(note)
        h.append(f"<h3>Queue backlog</h3><p style='color:#a33'><b>{note}</b></p>")
    else:
        h.append(f"<h3>Queue backlog</h3><p>{backlog_line}</p>")

    start = "Start any session - yours or an agent's - with:  ./agent-kit/run.sh"
    p.extend(["", start])
    h.append("<p>Start any session - yours or an agent's - with "
             "<code>./agent-kit/run.sh</code> "
             "(rules, all three streams, and the queue).</p>")

    p.extend(["", "Resume (GenAI-risk default + broad master) attached.", ""])
    h.append("<p>Resume (GenAI-risk default + broad master) attached.</p>")
    return "\n".join(p), "".join(h)


def attach_pdfs(msg: EmailMessage, paths: list[Path]) -> None:
    for path in paths:
        if not path.exists():
            print(f"[warn] missing attachment {path}", file=sys.stderr)
            continue
        ctype, _ = mimetypes.guess_type(path.name)
        maintype, subtype = (ctype or "application/pdf").split("/", 1)
        msg.add_attachment(path.read_bytes(), maintype=maintype,
                           subtype=subtype, filename=path.name)


def verify_documents() -> list[str]:
    """Run the document harness. Returns the failures, most important first.

    The digest attaches resumes. Attaching one that breaks a standing content
    rule is worse than sending no digest at all, so the failures ride in the
    email and the attachments are dropped when there are any.
    """
    import verify_documents as vd

    rep = vd.Report()
    for folder in (vd.RESUMES, vd.LETTERS):
        for pdf in sorted(folder.glob("*.pdf")):
            vd.check_pdf(pdf, rep)
    vd.check_sources(rep)
    vd.check_wiring(rep)
    return [f"{where}: {check} - {detail}" for _, where, check, detail
            in rep.failures]


def send_email(corporate: list[dict], teaching: list[dict],
               report: SourceReport, doc_failures: list[str]) -> None:
    sender = os.environ["GMAIL_ADDRESS"]
    password = os.environ["GMAIL_APP_PASS"]
    extra = [a.strip() for a in os.environ.get("EXTRA_RECIPIENTS", "").split(",") if a.strip()]
    recipients = [sender, *extra]

    plain, html = build_email_body(corporate, teaching, report)
    flag = " [SOURCE ISSUES]" if report.failures else ""
    if doc_failures:
        flag += " [DOCUMENTS FAILED VERIFICATION]"
        banner = ("DOCUMENT VERIFICATION FAILED - nothing is attached to this "
                  "digest. Do not apply until these are fixed "
                  "(./agent-kit/run.sh verify):")
        plain = banner + "\n  " + "\n  ".join(doc_failures) + "\n\n" + plain
        html = (f"<p style='color:#a33'><b>{banner}</b></p><ul>"
                + "".join(f"<li style='color:#a33'>{f}</li>" for f in doc_failures)
                + "</ul>" + html)
    msg = EmailMessage()
    msg["Subject"] = (f"Daily jobs digest - {date.today().isoformat()} "
                      f"({len(corporate)} corporate / {len(teaching)} teaching){flag}")
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg.set_content(plain)
    msg.add_alternative(html, subtype="html")

    attachments = [] if doc_failures else [
        # The two resumes that cover almost everything in the queue: the
        # GenAI-risk default and the broad master. Both one page, both
        # branded, both verified by scripts/verify_documents.py before the
        # digest goes out. Seed cover letters are no longer attached - the
        # two that used to be here were superseded and went out stale for
        # weeks without anyone noticing.
        REPO_ROOT / "applications/resume/Yasir_Malik_Resume_GenAI_Risk_Master_Branded.pdf",
        REPO_ROOT / "applications/resume/Yasir_Malik_Resume_Master_Branded.pdf",
    ]
    attach_pdfs(msg, attachments)

    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
    print(f"sent digest to {recipients}: "
          f"{len(corporate)} corporate, {len(teaching)} teaching, "
          f"{len(report.failures)} source failure(s), "
          f"{len(doc_failures)} document failure(s), "
          f"{len(attachments)} attachment(s)")


def collect() -> tuple[list[dict], list[dict], SourceReport]:
    report = SourceReport()

    raw_corporate: list[dict] = []
    raw_corporate += fetch_google(GOOGLE_QUERIES, report)
    for board, company in GREENHOUSE_CORPORATE:
        raw_corporate += fetch_greenhouse(board, company, report)
    for tenant, site, company, search, host in WORKDAY_CORPORATE:
        raw_corporate += fetch_workday(tenant, site, company, report, search, host)

    raw_teaching: list[dict] = []
    for tenant, site, company, search, host in WORKDAY_TEACHING:
        raw_teaching += fetch_workday(tenant, site, company, report, search, host)

    return rank_corporate(raw_corporate), rank_teaching(raw_teaching), report


def main() -> None:
    # Rebuild PDFs every run so any markdown edits go out the same morning.
    from build_pdfs import build_all

    build_all()

    doc_failures = verify_documents()
    if doc_failures:
        print(f"[stop] {len(doc_failures)} document failure(s); "
              f"the digest will go out with no attachments", file=sys.stderr)
        for line in doc_failures:
            print(f"  {line}", file=sys.stderr)

    corporate, teaching, report = collect()
    print(f"corporate={len(corporate)} teaching={len(teaching)} "
          f"failures={len(report.failures)}")

    if "--dry-run" in sys.argv:
        plain, _ = build_email_body(corporate, teaching, report)
        print("\n" + plain)
        return

    send_email(corporate, teaching, report, doc_failures)


if __name__ == "__main__":
    main()
