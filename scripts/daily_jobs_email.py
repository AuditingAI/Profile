"""Daily job search + email digest.

Runs from GitHub Actions. Searches Google careers and Anthropic's Greenhouse
board for roles matching the configured filters, attaches the resume + the
two seed cover letters, and emails the digest via Gmail SMTP.

Required environment variables:
    GMAIL_ADDRESS   - the From / To address (e.g. YasirAMalik@gmail.com)
    GMAIL_APP_PASS  - a Gmail App Password (not the account password). Create at
                      https://myaccount.google.com/apppasswords - requires 2FA.

Optional:
    EXTRA_RECIPIENTS - comma-separated additional To addresses.
"""

from __future__ import annotations

import json
import mimetypes
import os
import smtplib
import ssl
import sys
import urllib.error
import urllib.request
from datetime import date
from email.message import EmailMessage
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

ANTHROPIC_API = "https://boards-api.greenhouse.io/v1/boards/anthropic/jobs?content=true"
GOOGLE_CAREERS_API = (
    "https://careers.google.com/api/v3/search/?location=New%20York%2C%20NY%2C%20USA"
    "&q={query}&page_size=20"
)

ANTHROPIC_KEYWORDS = [
    "policy",
    "trust",
    "safety",
    "responsible",
    "alignment",
    "risk",
    "audit",
    "governance",
    "assurance",
    "model evaluation",
    "model risk",
    "compliance",
]

GOOGLE_QUERIES = [
    "AI compliance",
    "AI governance",
    "responsible AI",
    "model risk",
    "internal audit",
    "AI policy",
    "trust and safety program manager",
]


def _http_get_json(url: str) -> dict | None:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; YasirJobBot/1.0)",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as exc:
        print(f"[warn] fetch failed for {url}: {exc}", file=sys.stderr)
        return None


def fetch_anthropic_jobs() -> list[dict]:
    data = _http_get_json(ANTHROPIC_API)
    if not data or "jobs" not in data:
        return []
    matches = []
    for job in data["jobs"]:
        title = (job.get("title") or "").lower()
        content = (job.get("content") or "").lower()
        if any(kw in title or kw in content for kw in ANTHROPIC_KEYWORDS):
            matches.append(
                {
                    "company": "Anthropic",
                    "title": job.get("title"),
                    "location": (job.get("location") or {}).get("name"),
                    "url": job.get("absolute_url"),
                }
            )
    return matches


def fetch_google_jobs() -> list[dict]:
    seen: set[str] = set()
    matches: list[dict] = []
    for query in GOOGLE_QUERIES:
        url = GOOGLE_CAREERS_API.format(query=urllib.parse.quote_plus(query))
        data = _http_get_json(url)
        if not data:
            continue
        for job in data.get("jobs", []):
            apply_url = job.get("apply_url") or (
                f"https://www.google.com/about/careers/applications/jobs/results/"
                f"{job.get('id')}"
                if job.get("id")
                else None
            )
            if not apply_url or apply_url in seen:
                continue
            seen.add(apply_url)
            matches.append(
                {
                    "company": "Google",
                    "title": job.get("title"),
                    "location": ", ".join(job.get("locations") or []) or "New York, NY",
                    "url": apply_url,
                }
            )
    return matches


def build_email_body(jobs: list[dict]) -> tuple[str, str]:
    today = date.today().isoformat()
    if not jobs:
        plain = (
            f"Daily job digest - {today}\n\n"
            "No new matching roles surfaced today at Google NY or Anthropic.\n"
            "Resume and seed cover letters are attached so you have them ready.\n"
        )
        html = f"<p><b>Daily job digest - {today}</b></p><p>No new matching roles today.</p>"
        return plain, html

    plain_lines = [f"Daily job digest - {today}", "", f"{len(jobs)} matching role(s):", ""]
    html_lines = [f"<h2>Daily job digest - {today}</h2>", f"<p>{len(jobs)} matching role(s):</p>", "<ul>"]
    for job in jobs:
        plain_lines.append(f"- [{job['company']}] {job['title']} ({job['location']})")
        plain_lines.append(f"    {job['url']}")
        html_lines.append(
            f"<li><b>[{job['company']}]</b> "
            f"<a href='{job['url']}'>{job['title']}</a> "
            f"<span style='color:#666'>- {job['location']}</span></li>"
        )
    html_lines.append("</ul>")
    plain_lines.extend(["", "Resume + seed cover letters attached.", ""])
    html_lines.append("<p>Resume + seed cover letters attached.</p>")
    return "\n".join(plain_lines), "".join(html_lines)


def attach_pdfs(msg: EmailMessage, paths: list[Path]) -> None:
    for path in paths:
        if not path.exists():
            print(f"[warn] missing attachment {path}", file=sys.stderr)
            continue
        ctype, _ = mimetypes.guess_type(path.name)
        maintype, subtype = (ctype or "application/pdf").split("/", 1)
        msg.add_attachment(
            path.read_bytes(),
            maintype=maintype,
            subtype=subtype,
            filename=path.name,
        )


def send_email(jobs: list[dict]) -> None:
    sender = os.environ["GMAIL_ADDRESS"]
    password = os.environ["GMAIL_APP_PASS"]
    extra = [a.strip() for a in os.environ.get("EXTRA_RECIPIENTS", "").split(",") if a.strip()]
    recipients = [sender, *extra]

    plain, html = build_email_body(jobs)
    msg = EmailMessage()
    msg["Subject"] = f"Daily jobs digest - {date.today().isoformat()} ({len(jobs)} roles)"
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg.set_content(plain)
    msg.add_alternative(html, subtype="html")

    attach_pdfs(
        msg,
        [
            REPO_ROOT / "applications/resume/Yasir_Malik_Resume.pdf",
            REPO_ROOT / "applications/cover_letters/google_content_ai_compliance_spm.pdf",
            REPO_ROOT / "applications/cover_letters/anthropic_generic.pdf",
        ],
    )

    ctx = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ctx) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
    print(f"sent digest to {recipients} with {len(jobs)} role(s)")


def main() -> None:
    # Rebuild PDFs every run so any markdown edits go out the same morning.
    from build_pdfs import build_all

    build_all()

    jobs = fetch_anthropic_jobs() + fetch_google_jobs()
    print(f"matched {len(jobs)} roles")
    send_email(jobs)


if __name__ == "__main__":
    main()
