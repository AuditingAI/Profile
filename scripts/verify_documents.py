"""Verify every shipped document before anything is sent to an employer.

This is the harness. It replaces the checks that used to be run by hand after
each build and were therefore run inconsistently. It answers one question:

    can this repository's documents be attached to a real application today?

Four groups of checks:

  FORMAT    page count, extractable text, the name extracting as one
            contiguous string (the letter-spacing trap - see
            applications/resume/builders/README.md), phone, email.
  CONTENT   the standing content rules: no "OCC", no career-length number, no
            "Dr. Malik", no unqualified CIA claim, no unfilled placeholder, no
            tool he does not use. Applied to the PDFs *and* to the sources
            that generate them, so a violation is caught before it ships.
  WIRING    every resume named by the discovery rules, by a queued role, or by
            the daily digest exists, is shippable, and is one page.
  FRESHNESS (--rebuild) regenerate every PDF from its source and compare the
            extracted text. A PDF whose text no longer matches its builder is
            stale, which is the failure mode nobody notices.

Run:
    python3 scripts/verify_documents.py              # checks only
    python3 scripts/verify_documents.py --rebuild    # also rebuild and compare
    python3 scripts/verify_documents.py --json       # machine-readable

Exit code is 0 only when there are no failures. Warnings do not fail the run.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

# The system `cryptography` package in the cloud image is broken, and it takes
# pypdf's import down with it. pypdf falls back to a pure-Python provider when
# the module is explicitly absent. See builders/README.md.
sys.modules.setdefault("cryptography", None)  # type: ignore[arg-type]

from pypdf import PdfReader  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RESUMES = ROOT / "applications" / "resume"
LETTERS = ROOT / "applications" / "cover_letters"
BUILDERS = RESUMES / "builders"
QUEUE_PENDING = ROOT / "automation" / "queue" / "pending"

# ---------------------------------------------------------------------------
# What each document is for
# ---------------------------------------------------------------------------

# Superseded documents. They stay in the repository as a record of what was
# sent, they still have to obey the content rules, but they are not one page
# and must never be attached to anything. Nothing in the pipeline may name one.
ARCHIVE = {
    "applications/resume/Yasir_Malik_Resume.pdf",
    "applications/resume/Yasir_Malik_Resume_Citi_ChiefAuditorAI.pdf",
    "applications/resume/Yasir_Malik_Resume_Google_TPM_RegAudit.pdf",
    "applications/cover_letters/anthropic_generic.pdf",
    "applications/cover_letters/citi_chief_auditor_ai_md.pdf",
    "applications/cover_letters/google_content_ai_compliance_spm.pdf",
}

# Documents that are finished as far as this repository can take them but are
# not sendable yet, and why. A blocked document is reported every run so it
# cannot quietly become normal, and wiring one into the pipeline is a failure.
BLOCKED = {
    "applications/resume/Yasir_Malik_CV_Academic_Branded.pdf":
        "carries [TO CONFIRM] placeholders - the graduate TA post, the SAAC "
        "tutoring, the FIU guest lectures and the Rutgers class visit are "
        "facts only the owner has",
}

# Letters kept as a record or as a template, which must not be built into a
# sendable PDF. The harness would otherwise nag about them every run, and a
# warning nobody can clear is a warning nobody reads.
DRAFT_ONLY = {
    "applications/cover_letters/jpm_cib_finance_audit_vp_210759059.md":
        "req 210759059 was rejected 25 Aug 2026 - the letter is kept as the "
        "argument to reuse for a sibling CIB Audit VP req, not to send",
}

# The academic CV is deliberately multi-page: it is a CV, not a resume.
MULTIPAGE_OK = {
    "applications/resume/Yasir_Malik_CV_Academic_Branded.pdf": 4,
}

# ---------------------------------------------------------------------------
# The standing content rules
# ---------------------------------------------------------------------------

# Career-length numbers. Employer-specific spans ("five years at JPMorgan") are
# explicitly allowed by the owner's rule; what is banned is the total-career
# number that dates him. Spelled numbers below ten are therefore permitted and
# anything from ten up, any numeric "N years" from eight up, any "over/more
# than N years", and any use of "decade" is not.
CAREER_LENGTH = [
    r"\b(?:1\d|[2-9]\d)\s*\+?\s*(?:years|yrs)\b",
    r"\b[89]\s*\+?\s*(?:years|yrs)\b",
    r"\b(?:over|more than|nearly|almost|upwards of)\s+\d{1,2}\s*\+?\s*(?:years|yrs)\b",
    r"\b(?:ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|"
    r"eighteen|nineteen|twenty|twenty[- ]five|thirty)(?:[- ]plus)?[- ]years?\b",
    r"\bdecades?\b",
    r"\bcareer spanning\b",
]

PHONE_DIGITS = "7867048536"
RETIRED_AREA_CODE = r"\(?305\)?[\s.-]?\d{3}[\s.-]?\d{4}"
EMAIL = "yasiramalik@gmail.com"

FORBIDDEN = [
    ("OCC", r"\bOCC\b",
     "the examiner history is the Florida Office of Financial Regulation"),
    ("career-length number", "(?i)" + "|".join(CAREER_LENGTH),
     "name the institutions; the dates on the entries carry the tenure"),
    ("retired phone", RETIRED_AREA_CODE,
     "the 305 line is dead; the number is +1 (786) 704-8536"),
    # A raw entity in the TEXT LAYER means the markup did not render - "&mdash;"
    # or a mangled ".mdash;" printed where an em dash belonged. Found on a
    # shipped page once, from a sed replacement whose "&" re-inserted the match.
    # No content rule catches it, so it gets its own.
    ("unrendered markup", r"&(?:amp|bull|mdash|ndash|nbsp|lt|gt|quot|#\d+);|\.(?:mdash|bull|ndash|amp);",
     "the markup did not render - check the builder's escaping"),
    ("Dr. Malik", r"(?i)\bDr\.?\s+Malik\b",
     "the DBA is in progress, expected 2028"),
    ("CIA certified", r"(?i)\bCIA[\s-]certified\b",
     "CIA Part 1 is in progress"),
    ("unfilled placeholder", r"\[TO CONFIRM",
     "fill it or cut the line; never send a document with a placeholder"),
    ("unheld tool", r"(?i)\b(?:snowflake|oracle hcm|data mesh|data lake)\b",
     "not on the record - do not claim it"),
    ("Jira", r"(?i)\bjira\b", "not on the record - do not claim it"),
    ("R (statistics)", r"(?i)\b(?:python|sas|sql|spss|stata)\s*[,/]\s*r\b"
                       r"|\br\s*[,/]\s*(?:python|sas|sql|spss|stata)\b",
     "the statistical tool is SPSS, plus SAS and SQL. Never R."),
    ("dissertation claimed IRB-approved",
     r"(?i)\bIRB[- ]approved\s+(?:\w+[- ]){0,3}dissertation\b"
     r"|\bdissertation\b(?:(?!\.).){0,70}?\bIRB[- ]approved\b",
     "IRB-25-0462 covers the completed anchoring-bias qualifying study, "
     "not the automation-bias dissertation"),
]

# "Certified Internal Auditor" is legitimate when qualified. Anything else is a
# claim to hold it.
CIA_QUALIFIERS = r"(?i)(in progress|part 1|part i\b|candidate|pursuing|sitting)"

# ---------------------------------------------------------------------------
# Sources, so freshness can be checked
# ---------------------------------------------------------------------------

# builder script -> output PDF. Parsed from the builders where they declare it;
# build_branded_resume.py writes to its working directory, so it is pinned.
BUILDER_OUTPUTS: dict[str, str] = {
    "build_branded_resume.py": "Yasir_Malik_Resume_Google_CloudRAI_Branded.pdf",
}

HTML_OUTPUTS: dict[str, str] = {
    "master-resume-no-url.html": "Yasir_Malik_Resume_Master.pdf",
    "genai-risk-master.html": "Yasir_Malik_Resume_GenAI_Risk_Master.pdf",
    "gs-gbm-src-vp.html": "Yasir_Malik_Resume_GS_GBM_SRC_VP.pdf",
    "gs-ia-data-analytics-vp.html": "Yasir_Malik_Resume_GS_IA_DataAnalytics_VP.pdf",
    "blackstone-tprm-miami.html": "Yasir_Malik_Resume_Blackstone_TPRM_Miami.pdf",
    "google-core-ai-foundations-vp.html": "Yasir_Malik_Resume_Google_CoreAIFoundations_VP.pdf",
}

LEVELS = ("FAIL", "WARN")


@dataclass
class Report:
    findings: list[tuple[str, str, str, str]] = field(default_factory=list)
    checked: int = 0

    def fail(self, where: str, check: str, detail: str) -> None:
        self.findings.append(("FAIL", where, check, detail))

    def warn(self, where: str, check: str, detail: str) -> None:
        self.findings.append(("WARN", where, check, detail))

    @property
    def failures(self) -> list[tuple[str, str, str, str]]:
        return [f for f in self.findings if f[0] == "FAIL"]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def pdf_text(path: Path) -> tuple[str, int]:
    reader = PdfReader(str(path))
    pages = [(page.extract_text() or "") for page in reader.pages]
    return "\n".join(pages), len(reader.pages)


def normalise(text: str) -> str:
    """Collapse whitespace so wrapping differences do not read as changes."""
    return re.sub(r"\s+", " ", text).strip()


def fingerprint(path: Path) -> str:
    """What a rebuild must reproduce: the text AND the embedded images.

    Text alone is not enough. Adding the brand mark to every letterhead changes
    no text at all, so a text-only comparison reported "unchanged" and the
    restore step then reverted every rebuilt PDF - silently undoing the change
    it was meant to verify. The image digest closes that hole.
    """
    reader = PdfReader(str(path))
    text = normalise("\n".join((page.extract_text() or "") for page in reader.pages))
    images = []
    for page in reader.pages:
        try:
            for img in page.images:
                images.append(f"{img.name}:{len(img.data)}")
        except Exception:
            images.append("unreadable-image")
    return text + "\x00IMAGES\x00" + "|".join(sorted(images))


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

NEGATIONS = r"(?i)\b(?:not|no|never|don't|do not|does not|nothing|without|lack|"
NEGATIONS += r"absent|unfamiliar|cannot|can't|neither|nor)\b"


def _sentence_around(text: str, start: int, end: int) -> str:
    left = max(text.rfind(".", 0, start), text.rfind("\n", 0, start))
    right = text.find(".", end)
    return text[left + 1: right if right != -1 else end + 120]


def check_content_rules(where: str, text: str, rep: Report,
                        blocked_checks: set[str] | None = None) -> None:
    """Flag a rule break once per document per rule.

    A tool the owner does not use is only a violation when he claims it.
    Saying "I do not know Snowflake" in a cover letter is the opposite of a
    false claim, so a negated sentence does not count - otherwise the harness
    punishes the honesty it exists to protect.
    """
    seen: set[tuple[str, str]] = set()
    for name, pattern, remedy in FORBIDDEN:
        if blocked_checks and name in blocked_checks:
            continue
        for m in re.finditer(pattern, text):
            hit = m.group(0)
            if name in ("unheld tool", "Jira", "R (statistics)"):
                if re.search(NEGATIONS, _sentence_around(text, m.start(), m.end())):
                    continue
            key = (name, hit.lower())
            if key in seen:
                continue
            seen.add(key)
            rep.fail(where, name, f"{hit!r} - {remedy}")

    for m in re.finditer(r"(?i)certified internal auditor", text):
        window = text[max(0, m.start() - 100): m.end() + 100]
        if not re.search(CIA_QUALIFIERS, window):
            rep.fail(where, "CIA claimed as held",
                     "'Certified Internal Auditor' with no 'in progress' nearby")


def check_pdf(path: Path, rep: Report) -> str:
    where = rel(path)
    try:
        text, pages = pdf_text(path)
    except Exception as exc:  # a PDF nobody can read is worse than a bad one
        rep.fail(where, "unreadable", str(exc))
        return ""

    rep.checked += 1
    archived = where in ARCHIVE
    blocked = where in BLOCKED
    if blocked:
        rep.warn(where, "blocked from sending", BLOCKED[where])

    if len(normalise(text)) < 400:
        rep.fail(where, "no text layer",
                 f"only {len(normalise(text))} characters extract - an ATS reads nothing")

    limit = MULTIPAGE_OK.get(where, 1)
    if archived:
        if pages > 1:
            rep.warn(where, "archived", f"{pages} pages - superseded, never attach it")
    elif pages > limit:
        rep.fail(where, "page count", f"{pages} pages, expected at most {limit}")

    flat = normalise(text)
    if path.parent == RESUMES:
        if "YASIR A. MALIK" not in flat.upper().replace(" A . ", " A. "):
            rep.fail(where, "name not contiguous",
                     "'YASIR A. MALIK' does not extract as one string - "
                     "check h1 letter-spacing (builders/README.md)")
    elif "Yasir A. Malik" not in flat:
        rep.fail(where, "name missing", "the signature block did not extract")

    digits = re.sub(r"\D", "", flat)
    if PHONE_DIGITS not in digits:
        rep.fail(where, "phone missing", "+1 (786) 704-8536 is not in the text")
    if EMAIL not in flat.lower():
        rep.fail(where, "email missing", EMAIL)

    check_content_rules(where, text, rep,
                        {"unfilled placeholder"} if blocked else None)
    return text


def check_sources(rep: Report) -> None:
    """The same content rules, applied to what generates the PDFs."""
    sources = [
        *sorted(BUILDERS.glob("*.py")),
        *sorted(BUILDERS.glob("*.html")),
        *sorted(LETTERS.glob("*.md")),
        *sorted(RESUMES.glob("*.md")),
    ]
    for src in sources:
        text = src.read_text(encoding="utf-8", errors="replace")
        # A builder's docstring names the rules it must not break; reading them
        # as violations would make the harness fight its own documentation.
        body = re.sub(r'(?s)^\s*"""(?:.*?)"""', "", text, count=1)
        body = re.sub(r"(?m)^\s*#.*$", "", body)
        blocked_out = {out for out, _ in _blocked_outputs()}
        # "unrendered markup" is a rendered-output rule: an entity in a builder
        # is how you write an em dash, and only a leak into the PDF text layer
        # is a defect.
        skip = {"unrendered markup"}
        if _builder_output(src) in blocked_out:
            skip.add("unfilled placeholder")
        check_content_rules(rel(src), body, rep, skip)


def _builder_output(src: Path) -> str:
    m = re.search(r'(?m)^OUT\s*=\s*.*?"([^"]+\.pdf)"', src.read_text())
    return f"applications/resume/{m.group(1)}" if m else ""


def _blocked_outputs() -> list[tuple[str, str]]:
    return sorted(BLOCKED.items())


def shippable_set() -> dict[str, list[str]]:
    """Every resume the pipeline can actually name, and who names it."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import discover_jobs  # noqa: E402  (import here: needs the path above)

    named: dict[str, list[str]] = {}

    def note(path: str, source: str) -> None:
        named.setdefault(path, []).append(source)

    for pattern, path in discover_jobs.RESUME_RULES:
        note(path, f"discovery rule /{pattern[:28]}.../")
    note(discover_jobs.DEFAULT_RESUME, "discovery default")

    for entry in sorted(QUEUE_PENDING.glob("*.json")):
        try:
            data = json.loads(entry.read_text())
        except json.JSONDecodeError:
            continue
        resume = (data.get("package") or {}).get("resume")
        if resume:
            note(resume, f"queue/{entry.name}")

    digest = (ROOT / "scripts" / "daily_jobs_email.py").read_text()
    for m in re.finditer(r'REPO_ROOT / "(applications/[^"]+\.pdf)"', digest):
        note(m.group(1), "daily digest attachment")

    return named


def check_wiring(rep: Report) -> None:
    for path, sources in sorted(shippable_set().items()):
        full = ROOT / path
        who = ", ".join(sorted(set(sources))[:3])
        if not full.exists():
            rep.fail(path, "named but missing", f"named by {who}")
            continue
        if path in ARCHIVE:
            rep.fail(path, "archived file is wired in",
                     f"{who} points at a superseded document")
            continue
        if path in BLOCKED:
            rep.fail(path, "blocked file is wired in",
                     f"{who} attaches it, but it {BLOCKED[path]}")
            continue
        try:
            _, pages = pdf_text(full)
        except Exception as exc:
            rep.fail(path, "unreadable", str(exc))
            continue
        if pages > MULTIPAGE_OK.get(path, 1):
            rep.fail(path, "not shippable", f"{pages} pages but {who} attaches it")

    for entry in sorted(QUEUE_PENDING.glob("*.json")):
        where = rel(entry)
        try:
            raw = entry.read_text()
            data = json.loads(raw)
        except json.JSONDecodeError as exc:
            rep.fail(where, "invalid JSON", str(exc))
            continue
        keys = list(data)
        if not keys or keys[0] != "_rules":
            rep.fail(where, "rules not stamped",
                     "'_rules' must be the first key so an agent that opens "
                     "one file in isolation still sees them")
        if not (data.get("package") or {}).get("resume"):
            rep.fail(where, "no resume", "package.resume is empty")

    for builder, output in BUILDER_OUTPUTS.items():
        if not (BUILDERS / builder).exists():
            rep.warn(builder, "builder missing", "named in verify_documents.py")
        elif not (RESUMES / output).exists():
            rep.fail(output, "builder output missing", f"{builder} produces it")

    for letter in sorted(LETTERS.glob("*.md")):
        if rel(letter) in DRAFT_ONLY:
            if letter.with_suffix(".pdf").exists():
                rep.fail(rel(letter), "draft built into a PDF",
                         DRAFT_ONLY[rel(letter)])
            continue
        if not letter.with_suffix(".pdf").exists():
            rep.warn(rel(letter), "no PDF",
                     "markdown letter with no built PDF - register it in "
                     "scripts/build_pdfs.py build_all()")


# ---------------------------------------------------------------------------
# Freshness
# ---------------------------------------------------------------------------

def discover_builders() -> dict[Path, Path]:
    """builder script -> output PDF, read from each builder's own OUT line."""
    out: dict[Path, Path] = {}
    for script in sorted(BUILDERS.glob("build_*.py")):
        if script.name in BUILDER_OUTPUTS:
            out[script] = RESUMES / BUILDER_OUTPUTS[script.name]
            continue
        m = re.search(r'(?m)^OUT\s*=\s*.*?"([^"]+\.pdf)"', script.read_text())
        if m:
            out[script] = RESUMES / m.group(1)
    return out


def restore(originals: dict[Path, bytes]) -> None:
    """Put back the exact bytes that were on disk before the rebuild.

    Every PDF stamps its build time into /CreationDate, so a rebuild that
    changes nothing still rewrites the file. Writing the original bytes back
    keeps `git status` meaningful: what is left modified after a verify run is
    what actually changed.

    This restores the PRE-RUN bytes, not the last commit. An earlier version
    ran `git checkout --` here, which reverted uncommitted work - a verify run
    could silently undo the change it was being run to check.
    """
    for path, data in originals.items():
        try:
            if path.read_bytes() != data:
                path.write_bytes(data)
        except OSError:
            pass


def check_freshness(rep: Report, include_html: bool) -> None:
    before: dict[Path, str] = {}
    original_bytes: dict[Path, bytes] = {}
    targets: list[Path] = []

    builders = discover_builders()
    for script, output in builders.items():
        if output.exists():
            before[output] = fingerprint(output)
            original_bytes[output] = output.read_bytes()
        targets.append(output)

    sys.path.insert(0, str(ROOT / "scripts"))
    import build_pdfs  # noqa: E402

    for src, dst, *_ in _build_all_pairs(build_pdfs):
        if dst.exists():
            before[dst] = fingerprint(dst)
            original_bytes[dst] = dst.read_bytes()

    for script, output in builders.items():
        result = subprocess.run([sys.executable, str(script)], cwd=RESUMES,
                                capture_output=True, text=True)
        if result.returncode != 0:
            rep.fail(rel(script), "builder failed",
                     result.stderr.strip().splitlines()[-1] if result.stderr else "")

    try:
        build_pdfs.build_all()
    except Exception as exc:
        rep.fail("scripts/build_pdfs.py", "build_all failed", str(exc))

    if include_html:
        _rebuild_html(rep, before)

    unchanged: dict[Path, bytes] = {}
    for path, old in before.items():
        if not path.exists():
            rep.fail(rel(path), "disappeared", "the rebuild did not produce it")
            continue
        new = fingerprint(path)
        if new == old:
            unchanged[path] = original_bytes[path]
        else:
            rep.fail(rel(path), "stale",
                     "the committed PDF does not match what its source builds "
                     "today - the rebuilt file is now in place; review and commit it")
    restore(unchanged)

    for path in targets:
        if not path.exists():
            rep.fail(rel(path), "never built", "its builder produced no output")


def _build_all_pairs(build_pdfs) -> list[tuple]:
    """Read build_all's table without running it."""
    pairs = []
    text = (ROOT / "scripts" / "build_pdfs.py").read_text()
    for m in re.finditer(r'REPO_ROOT / "(applications/[^"]+\.md)",\s*\n\s*'
                         r'REPO_ROOT / "(applications/[^"]+\.pdf)"', text):
        pairs.append((ROOT / m.group(1), ROOT / m.group(2)))
    return pairs


def _rebuild_html(rep: Report, before: dict[Path, str]) -> None:
    chrome = None
    for candidate in sorted(Path("/opt/pw-browsers").glob("chromium*/chrome-linux/chrome")):
        chrome = candidate
        break
    if chrome is None or not shutil.which(str(chrome)):
        rep.warn("html resumes", "chromium unavailable",
                 "skipped the HTML freshness check in this environment")
        return
    tmp = ROOT / ".verify-tmp"
    tmp.mkdir(exist_ok=True)
    try:
        for source, output in HTML_OUTPUTS.items():
            src = BUILDERS / source
            dst = RESUMES / output
            if not src.exists() or not dst.exists():
                continue
            built = tmp / output
            subprocess.run([str(chrome), "--headless", "--no-sandbox",
                            "--disable-gpu", "--no-pdf-header-footer",
                            f"--print-to-pdf={built}", f"file://{src}"],
                           capture_output=True, check=False)
            if not built.exists():
                rep.warn(rel(src), "chromium produced nothing", "")
                continue
            if fingerprint(built) != fingerprint(dst):
                rep.fail(rel(dst), "stale (HTML)",
                         f"{source} renders different text than the committed PDF")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rebuild", action="store_true",
                    help="regenerate every PDF and compare the text")
    ap.add_argument("--html", action="store_true",
                    help="with --rebuild, also re-render the Chromium resumes")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rep = Report()

    if args.rebuild:
        check_freshness(rep, include_html=args.html)

    for folder in (RESUMES, LETTERS):
        for pdf in sorted(folder.glob("*.pdf")):
            check_pdf(pdf, rep)

    check_sources(rep)
    check_wiring(rep)

    if args.json:
        print(json.dumps({
            "checked": rep.checked,
            "failures": len(rep.failures),
            "findings": [dict(zip(("level", "where", "check", "detail"), f))
                         for f in rep.findings],
        }, indent=2))
        return 1 if rep.failures else 0

    width = max((len(f[1]) for f in rep.findings), default=0)
    for level in LEVELS:
        rows = [f for f in rep.findings if f[0] == level]
        if not rows:
            continue
        print(f"\n{level}  ({len(rows)})")
        for _, where, check, detail in rows:
            print(f"  {where:<{width}}  {check}")
            if detail:
                print(f"  {'':<{width}}    {detail}")

    print(f"\n{rep.checked} document(s) checked, "
          f"{len(rep.failures)} failure(s), "
          f"{len(rep.findings) - len(rep.failures)} warning(s).")
    if not rep.failures:
        print("READY - every document passes.")
    return 1 if rep.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
