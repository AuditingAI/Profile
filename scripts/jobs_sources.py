"""Job sources, scoring, and sponsor policy for the daily agent.

Kept separate from daily_jobs_email.py so the search/scoring logic can be
tested and tuned without touching the email plumbing.

Two streams run every morning:

  CORPORATE - VP/Director AI governance, audit, and risk roles, weighted
              toward employers with a real green-card sponsorship record.
  TEACHING  - adjunct / lecturer / professor-of-practice roles. Universities
              are H-1B cap-exempt, which is why this stream is worth its own
              pass rather than being folded into the corporate keywords.

Every fetch reports success or failure so a dead source shows up in the
digest instead of quietly returning nothing. A source that breaks and says
nothing is worse than no source at all.
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; YasirJobBot/2.0)"
TIMEOUT = 30

# --------------------------------------------------------------------------
# Policy
# --------------------------------------------------------------------------

# Employers with a well-established record of sponsoring employment-based
# permanent residence. Used to flag rows, never to invent a guarantee -
# sponsorship is always confirmed with the employer before applying.
SPONSOR_EMPLOYERS = {
    "jpmorgan", "jpmorgan chase", "jpmorganchase", "j.p. morgan",
    "bank of america", "bofa", "goldman sachs", "morgan stanley",
    "bny", "bny mellon", "state street", "wells fargo",
    "prudential", "pgim", "metlife", "blackrock", "barclays", "hsbc", "rbc",
    "google", "microsoft", "apple", "amazon", "meta", "anthropic", "openai",
}

# Past employer - rehire is not the plan. Ranked but never promoted.
EXCLUDED_EMPLOYERS = {"citi", "citigroup", "citibank"}

# Geography that counts as in-market. Newark and Jersey City matter as much
# as Manhattan; several target employers are headquartered in New Jersey.
IN_MARKET = [
    "new york", "nyc", "manhattan", "newark", "jersey city", "new jersey",
    "nj", "ny", "remote", "hybrid",
]

# Title scoring. Higher wins. The rubric mirrors how Yasir actually triages:
# a bullseye title at any sponsor beats a vague "risk" title anywhere.
SCORE_5 = [
    "ai governance", "ai risk", "responsible ai", "model risk",
    "ai audit", "ai assurance", "algorithmic risk",
]
SCORE_4 = [
    "technology audit", "tech audit", "third party risk", "vendor risk",
    "data governance", "internal audit", "audit director", "audit manager",
    "controls", "regulatory", "compliance",
]
SCORE_3 = ["risk", "audit", "governance", "assurance", "policy", "trust and safety"]

SENIORITY = ["vice president", "vp", "director", "head", "executive", "principal",
             "senior manager", "lead", "svp", "managing director", "md"]

TEACHING_TITLES = [
    "adjunct", "lecturer", "professor of practice", "instructor",
    "teaching faculty", "executive in residence", "clinical faculty",
]


def score_role(title: str, company: str, location: str) -> tuple[int, list[str]]:
    """Return (score, tags). Score 0 means drop it."""
    t, c, loc = title.lower(), company.lower(), (location or "").lower()
    tags: list[str] = []

    if any(x in c for x in EXCLUDED_EMPLOYERS):
        tags.append("past-employer")
        return 1, tags  # ranked last, never promoted

    score = 0
    if any(k in t for k in SCORE_5):
        score = 5
    elif any(k in t for k in SCORE_4):
        score = 4
    elif any(k in t for k in SCORE_3):
        score = 3

    if score and any(s in t for s in SENIORITY):
        score = min(5, score + 1)

    if any(x in c for x in SPONSOR_EMPLOYERS):
        tags.append("sponsor")

    if loc and not any(m in loc for m in IN_MARKET):
        score = max(0, score - 1)
        tags.append("out-of-market")

    return score, tags


def score_teaching(title: str) -> int:
    t = title.lower()
    if any(k in t for k in TEACHING_TITLES):
        return 5 if any(k in t for k in ("adjunct", "professor of practice", "lecturer")) else 4
    return 0


# --------------------------------------------------------------------------
# Fetching
# --------------------------------------------------------------------------


class SourceReport:
    """Records what each source did, so failures surface in the digest."""

    def __init__(self) -> None:
        self.rows: list[tuple[str, str, int]] = []

    def ok(self, name: str, count: int) -> None:
        self.rows.append((name, "ok", count))

    def fail(self, name: str, detail: str) -> None:
        self.rows.append((name, f"FAILED - {detail}", 0))

    @property
    def failures(self) -> list[tuple[str, str, int]]:
        return [r for r in self.rows if r[1] != "ok"]


def _get_json(url: str, data: dict | None = None) -> dict | None:
    body = json.dumps(data).encode() if data is not None else None
    headers = {"User-Agent": UA, "Accept": "application/json"}
    if body:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001 - any failure is just a dead source
        print(f"[warn] {url}: {exc}", file=sys.stderr)
        return None


def fetch_greenhouse(board: str, company: str, report: SourceReport) -> list[dict]:
    """Greenhouse boards expose a stable public JSON API."""
    url = f"https://boards-api.greenhouse.io/v1/boards/{board}/jobs?content=true"
    data = _get_json(url)
    if not data or "jobs" not in data:
        report.fail(f"{company} (Greenhouse)", "no response")
        return []
    out = []
    for job in data["jobs"]:
        title = job.get("title") or ""
        loc = (job.get("location") or {}).get("name") or ""
        out.append({"company": company, "title": title, "location": loc,
                    "url": job.get("absolute_url")})
    report.ok(f"{company} (Greenhouse)", len(out))
    return out


def fetch_workday(tenant: str, site: str, company: str, report: SourceReport,
                  search: str = "", host: str = "wd1") -> list[dict]:
    """Workday's careers JSON endpoint. Most large banks run on Workday.

    If a tenant/site pair is wrong the source reports FAILED in the digest,
    which is the signal to correct the two strings below - not to guess.
    """
    url = (f"https://{tenant}.{host}.myworkdayjobs.com/wday/cxs/"
           f"{tenant}/{site}/jobs")
    data = _get_json(url, {"appliedFacets": {}, "limit": 20, "offset": 0,
                           "searchText": search})
    if not data or "jobPostings" not in data:
        report.fail(f"{company} (Workday)", "no response / wrong tenant")
        return []
    out = []
    for job in data["jobPostings"]:
        path = job.get("externalPath") or ""
        out.append({
            "company": company,
            "title": job.get("title") or "",
            "location": job.get("locationsText") or "",
            "url": f"https://{tenant}.{host}.myworkdayjobs.com/{site}{path}",
        })
    report.ok(f"{company} (Workday)", len(out))
    return out


def fetch_google(queries: list[str], report: SourceReport) -> list[dict]:
    api = ("https://careers.google.com/api/v3/search/"
           "?location=New%20York%2C%20NY%2C%20USA&q={q}&page_size=20")
    seen, out = set(), []
    any_ok = False
    for q in queries:
        data = _get_json(api.format(q=urllib.parse.quote_plus(q)))
        if data is None:
            continue
        any_ok = True
        for job in data.get("jobs", []):
            url = job.get("apply_url") or (
                "https://www.google.com/about/careers/applications/jobs/results/"
                f"{job.get('id')}" if job.get("id") else None)
            if not url or url in seen:
                continue
            seen.add(url)
            out.append({"company": "Google", "title": job.get("title") or "",
                        "location": ", ".join(job.get("locations") or []) or "New York, NY",
                        "url": url})
    report.ok("Google Careers", len(out)) if any_ok else report.fail("Google Careers", "no response")
    return out
