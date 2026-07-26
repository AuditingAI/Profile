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

    p.extend(["", "Resume + seed cover letters attached.", ""])
    h.append("<p>Resume + seed cover letters attached.</p>")
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


def send_email(corporate: list[dict], teaching: list[dict], report: SourceReport) -> None:
    sender = os.environ["GMAIL_ADDRESS"]
    password = os.environ["GMAIL_APP_PASS"]
    extra = [a.strip() for a in os.environ.get("EXTRA_RECIPIENTS", "").split(",") if a.strip()]
    recipients = [sender, *extra]

    plain, html = build_email_body(corporate, teaching, report)
    flag = " [SOURCE ISSUES]" if report.failures else ""
    msg = EmailMessage()
    msg["Subject"] = (f"Daily jobs digest - {date.today().isoformat()} "
                      f"({len(corporate)} corporate / {len(teaching)} teaching){flag}")
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg.set_content(plain)
    msg.add_alternative(html, subtype="html")

    attach_pdfs(msg, [
        REPO_ROOT / "applications/resume/Yasir_Malik_Resume_Master.pdf",
        REPO_ROOT / "applications/cover_letters/google_content_ai_compliance_spm.pdf",
        REPO_ROOT / "applications/cover_letters/anthropic_generic.pdf",
    ])

    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
    print(f"sent digest to {recipients}: "
          f"{len(corporate)} corporate, {len(teaching)} teaching, "
          f"{len(report.failures)} source failure(s)")


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

    corporate, teaching, report = collect()
    print(f"corporate={len(corporate)} teaching={len(teaching)} "
          f"failures={len(report.failures)}")

    if "--dry-run" in sys.argv:
        plain, _ = build_email_body(corporate, teaching, report)
        print("\n" + plain)
        return

    send_email(corporate, teaching, report)


if __name__ == "__main__":
    main()
