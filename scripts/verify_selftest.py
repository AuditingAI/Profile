"""Prove the harness still catches what it claims to catch.

A verification script that passes is only reassuring if it would have failed.
This injects each known failure mode into a throwaway copy of the repository,
runs scripts/verify_documents.py against it, and asserts the right check
fires. If someone loosens a rule, a case here goes red.

    python3 scripts/verify_selftest.py
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY_DIRS = ("applications", "automation", "scripts", "agent-kit", "assets")


def sandbox(tmp: Path) -> Path:
    repo = tmp / "repo"
    repo.mkdir()
    for name in COPY_DIRS:
        src = ROOT / name
        if src.exists():
            shutil.copytree(src, repo / name)
    return repo


def run(repo: Path) -> tuple[int, list[dict]]:
    proc = subprocess.run(
        [sys.executable, str(repo / "scripts" / "verify_documents.py"), "--json"],
        capture_output=True, text=True, cwd=repo)
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        print(proc.stdout[-2000:], proc.stderr[-2000:], sep="\n")
        raise
    return proc.returncode, data["findings"]


# --- the injections -------------------------------------------------------

def inject_occ(repo: Path) -> None:
    md = repo / "applications/cover_letters/bny_vp_auditor_treasury_cio_risk.md"
    md.write_text(md.read_text().replace(
        "Florida Office of Financial Regulation", "OCC", 1))


def inject_career_length(repo: Path) -> None:
    md = repo / "applications/cover_letters/bny_vp_auditor_treasury_cio_risk.md"
    md.write_text("Over 20 years of experience in banking.\n" + md.read_text())


def inject_dr_malik(repo: Path) -> None:
    md = repo / "applications/cover_letters/bny_vp_auditor_treasury_cio_risk.md"
    md.write_text(md.read_text() + "\n\nRegards, Dr. Malik\n")


def inject_unheld_tool(repo: Path) -> None:
    md = repo / "applications/cover_letters/bny_vp_auditor_treasury_cio_risk.md"
    md.write_text(md.read_text() + "\n\nI build pipelines in Snowflake and track them in Jira.\n")


def inject_missing_resume(repo: Path) -> None:
    (repo / "applications/resume/Yasir_Malik_Resume_GenAI_Risk_Master_Branded.pdf").unlink()


def inject_archived_wiring(repo: Path) -> None:
    src = repo / "scripts/discover_jobs.py"
    src.write_text(src.read_text().replace(
        'DEFAULT_RESUME = "applications/resume/Yasir_Malik_Resume_GenAI_Risk_Master_Branded.pdf"',
        'DEFAULT_RESUME = "applications/resume/Yasir_Malik_Resume.pdf"'))


def inject_unstamped_queue(repo: Path) -> None:
    entry = sorted((repo / "automation/queue/pending").glob("*.json"))[0]
    data = json.loads(entry.read_text())
    data.pop("_rules", None)
    entry.write_text(json.dumps(data, indent=2) + "\n")


def inject_placeholder(repo: Path) -> None:
    md = repo / "applications/cover_letters/bny_vp_auditor_treasury_cio_risk.md"
    md.write_text(md.read_text() + "\n\n[TO CONFIRM: the req number.]\n")


def inject_retired_phone(repo: Path) -> None:
    md = repo / "applications/cover_letters/bny_vp_auditor_treasury_cio_risk.md"
    md.write_text(md.read_text().replace("+1 (786) 704-8536", "(305) 555-0134", 1))


def inject_letter_spacing(repo: Path) -> None:
    """The failure this whole harness exists for: the name stops extracting."""
    html = repo / "applications/resume/builders/gs-gbm-src-vp.html"
    if html.exists():
        html.write_text(re.sub(r"letter-spacing:\s*[\d.]+px", "letter-spacing: 4px",
                               html.read_text()))


CASES = [
    ("OCC reintroduced", inject_occ, "OCC", False),
    ("career-length number", inject_career_length, "career-length number", False),
    ("Dr. Malik", inject_dr_malik, "Dr. Malik", False),
    ("claims an unheld tool", inject_unheld_tool, "unheld tool", False),
    ("Jira claimed", inject_unheld_tool, "Jira", False),
    ("default resume deleted", inject_missing_resume, "named but missing", False),
    ("pipeline points at an archived resume", inject_archived_wiring,
     "archived file is wired in", False),
    ("queue entry loses its rules", inject_unstamped_queue, "rules not stamped", False),
    ("placeholder left in a letter", inject_placeholder, "unfilled placeholder", False),
    ("retired 305 number", inject_retired_phone, "retired phone", False),
]

# Cases whose fault only shows up after a rebuild.
REBUILD_CASES = [
    ("a source changes and the PDF does not", inject_occ, "stale"),
]


def main() -> int:
    failures = 0

    with tempfile.TemporaryDirectory() as tmp:
        repo = sandbox(Path(tmp))
        code, findings = run(repo)
        if code != 0:
            print("control  FAIL - a clean copy does not pass")
            for f in findings:
                if f["level"] == "FAIL":
                    print(f"           {f['where']}: {f['check']}")
            failures += 1
        else:
            print("control  ok   - a clean copy passes")

    for name, inject, expect, _ in CASES:
        with tempfile.TemporaryDirectory() as tmp:
            repo = sandbox(Path(tmp))
            inject(repo)
            code, findings = run(repo)
            caught = any(f["level"] == "FAIL" and f["check"] == expect
                         for f in findings)
            # Injections into markdown only reach a PDF after a rebuild, so the
            # source check is what has to catch them. Either is a pass.
            if caught and code != 0:
                print(f"caught   ok   - {name}")
            else:
                print(f"MISSED   FAIL - {name}: no {expect!r} finding")
                failures += 1

    for name, inject, expect in REBUILD_CASES:
        with tempfile.TemporaryDirectory() as tmp:
            repo = sandbox(Path(tmp))
            subprocess.run(["git", "init", "-q"], cwd=repo, check=False)
            subprocess.run(["git", "add", "-A"], cwd=repo, check=False)
            subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t",
                            "commit", "-qm", "base"], cwd=repo, check=False)
            inject(repo)
            proc = subprocess.run(
                [sys.executable, str(repo / "scripts/verify_documents.py"),
                 "--rebuild", "--json"],
                capture_output=True, text=True, cwd=repo)
            data = json.loads(proc.stdout)
            caught = any(f["level"] == "FAIL" and f["check"].startswith(expect)
                         for f in data["findings"])
            if caught:
                print(f"caught   ok   - {name}")
            else:
                print(f"MISSED   FAIL - {name}: no {expect!r} finding")
                failures += 1

    print(f"\n{len(CASES) + len(REBUILD_CASES) + 1} case(s), {failures} failure(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
