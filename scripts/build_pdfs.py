"""Build PDFs for the resume and cover letters from markdown sources.

Used both interactively and by the daily GitHub Actions workflow.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

REPO_ROOT = Path(__file__).resolve().parent.parent


def _styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    body = ParagraphStyle(
        "Body",
        parent=base["BodyText"],
        fontName="Helvetica",
        fontSize=10.2,
        leading=14,
        spaceAfter=6,
    )
    h1 = ParagraphStyle(
        "H1",
        parent=base["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        spaceAfter=4,
        textColor="#222222",
    )
    h2 = ParagraphStyle(
        "H2",
        parent=base["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=15,
        spaceBefore=10,
        spaceAfter=4,
        textColor="#1a1a1a",
    )
    h3 = ParagraphStyle(
        "H3",
        parent=base["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=10.8,
        leading=14,
        spaceBefore=8,
        spaceAfter=2,
    )
    bullet = ParagraphStyle(
        "Bullet",
        parent=body,
        leftIndent=14,
        bulletIndent=2,
        spaceAfter=3,
    )
    italic = ParagraphStyle(
        "Italic",
        parent=body,
        fontName="Helvetica-Oblique",
        textColor="#555555",
        spaceAfter=4,
    )
    quote = ParagraphStyle(
        "Quote",
        parent=italic,
        leftIndent=12,
        textColor="#444444",
    )
    return {
        "body": body,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "bullet": bullet,
        "italic": italic,
        "quote": quote,
    }


def _inline(text: str) -> str:
    """Convert minimal markdown inline syntax to ReportLab markup."""
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(?!\s)([^*]+?)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    return text


def _md_to_flowables(md_text: str) -> list:
    styles = _styles()
    flow: list = []
    for raw_line in md_text.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            flow.append(Spacer(1, 4))
            continue
        if line.startswith("### "):
            flow.append(Paragraph(_inline(line[4:]), styles["h3"]))
        elif line.startswith("## "):
            flow.append(Paragraph(_inline(line[3:]), styles["h2"]))
        elif line.startswith("# "):
            flow.append(Paragraph(_inline(line[2:]), styles["h1"]))
        elif line.startswith("> "):
            flow.append(Paragraph(_inline(line[2:]), styles["quote"]))
        elif line.startswith("- "):
            flow.append(
                Paragraph(_inline(line[2:]), styles["bullet"], bulletText="•")
            )
        elif line.startswith("---"):
            flow.append(Spacer(1, 6))
        elif line.startswith("*") and line.endswith("*") and not line.startswith("**"):
            flow.append(Paragraph(_inline(line.strip("*")), styles["italic"]))
        else:
            flow.append(Paragraph(_inline(line), styles["body"]))
    return flow


def build_pdf(md_path: Path, out_path: Path, title: str | None = None) -> Path:
    md_text = md_path.read_text(encoding="utf-8")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=LETTER,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        title=title or out_path.stem,
        author="Yasir A. Malik",
    )
    doc.build(_md_to_flowables(md_text))
    return out_path


def build_all() -> list[Path]:
    outputs: list[Path] = []
    pairs = [
        (
            REPO_ROOT / "applications/resume/resume.md",
            REPO_ROOT / "applications/resume/Yasir_Malik_Resume.pdf",
            "Yasir A. Malik - Resume",
        ),
        (
            REPO_ROOT / "applications/cover_letters/google_content_ai_compliance_spm.md",
            REPO_ROOT / "applications/cover_letters/google_content_ai_compliance_spm.pdf",
            "Cover Letter - Google Content & AI Compliance Sr PM",
        ),
        (
            REPO_ROOT / "applications/cover_letters/anthropic_generic.md",
            REPO_ROOT / "applications/cover_letters/anthropic_generic.pdf",
            "Cover Letter - Anthropic",
        ),
        (
            REPO_ROOT / "applications/resume/resume_citi_chief_auditor_ai.md",
            REPO_ROOT / "applications/resume/Yasir_Malik_Resume_Citi_ChiefAuditorAI.pdf",
            "Yasir A. Malik - Resume (Citi Chief Auditor AI MD)",
        ),
        (
            REPO_ROOT / "applications/cover_letters/citi_chief_auditor_ai_md.md",
            REPO_ROOT / "applications/cover_letters/citi_chief_auditor_ai_md.pdf",
            "Cover Letter - Citi Chief Auditor AI MD",
        ),
    ]
    for src, dst, title in pairs:
        if src.exists():
            outputs.append(build_pdf(src, dst, title))
    return outputs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--md", type=Path, help="Single markdown source to convert")
    parser.add_argument("--out", type=Path, help="Output PDF path")
    parser.add_argument("--title", type=str, default=None)
    args = parser.parse_args()

    if args.md and args.out:
        path = build_pdf(args.md, args.out, args.title)
        print(f"wrote {path}")
        return

    for path in build_all():
        print(f"wrote {path}")


if __name__ == "__main__":
    main()
