#!/usr/bin/env python3
"""Render every application cover letter to a clearly-named PDF.

Reads the "## Cover letter — paste-ready" blockquote out of each role folder
(PACKAGE.md, or COVER_LETTER.md for the older multi-file layout) and writes
COVER-LETTER_<Company>_<Role>.pdf next to it.

Contact details live in Notion, not this repo, so {{PHONE}} / {{EMAIL}}
placeholders are rendered as a fill-in line rather than being silently dropped.

Usage: python3 career/applications/make_pdfs.py
"""
import re
import pathlib

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

ROOT = pathlib.Path(__file__).resolve().parent
INK = HexColor("#14171C")
GREY = HexColor("#5A6068")
RULE = HexColor("#C9C4BA")

BODY = ParagraphStyle("body", fontName="Times-Roman", fontSize=11, leading=15.5,
                      textColor=INK, spaceAfter=11)
NAME = ParagraphStyle("name", fontName="Times-Bold", fontSize=16, leading=19,
                      textColor=INK, spaceAfter=2)
META = ParagraphStyle("meta", fontName="Helvetica", fontSize=8.5, leading=12,
                      textColor=GREY, spaceAfter=2)
ROLE = ParagraphStyle("role", fontName="Times-Bold", fontSize=11, leading=15,
                      textColor=INK, spaceAfter=12)


def extract_letter(folder: pathlib.Path):
    """Return (title_line, [paragraphs]) or None if no letter is present."""
    for candidate in ("PACKAGE.md", "COVER_LETTER.md"):
        path = folder / candidate
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")

        title = ""
        m = re.search(r"^#\s+(.*)$", text, re.M)
        if m:
            title = m.group(1).strip()

        # the letter is the blockquote following the cover-letter heading
        m = re.search(r"^##\s+Cover letter.*?$(.*?)(?=^##\s|\Z)", text, re.M | re.S)
        if not m:
            continue
        quoted = [ln[1:].strip() if ln.startswith(">") else ""
                  for ln in m.group(1).splitlines() if ln.startswith(">") or not ln.strip()]

        paras, buf = [], []
        for line in quoted:
            if line:
                buf.append(line)
            elif buf:
                paras.append(" ".join(buf))
                buf = []
        if buf:
            paras.append(" ".join(buf))
        if paras:
            return title, paras
    return None


def slug(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9 &-]", "", text)
    return re.sub(r"[\s&]+", "-", text.strip())[:60].strip("-")


def render(folder: pathlib.Path, title: str, paras: list) -> pathlib.Path:
    company, _, role = title.partition("—")
    company, role = company.strip() or folder.name, role.strip() or "Application"
    out = folder / f"COVER-LETTER_{slug(company)}_{slug(role)}.pdf"

    doc = SimpleDocTemplate(
        str(out), pagesize=LETTER,
        leftMargin=1.1 * inch, rightMargin=1.1 * inch,
        topMargin=0.9 * inch, bottomMargin=0.9 * inch,
        title=f"Cover letter — {company}", author="Yasir A. Malik",
        subject=role,
    )

    flow = [
        Paragraph("Yasir A. Malik", NAME),
        Paragraph("Newark, New Jersey &nbsp;·&nbsp; ____________________ &nbsp;·&nbsp; ____________________", META),
        Spacer(1, 8),
        HRFlowable(width="100%", thickness=0.6, color=RULE, spaceAfter=14),
        Paragraph(f"{company} — {role}", ROLE),
    ]

    for para in paras:
        if para.lower().startswith(("sincerely", "regards")):
            flow.append(Spacer(1, 4))
        # placeholders become a signature fill-in line, never a literal {{TOKEN}}
        para = para.replace("{{PHONE}}", "____________________")
        para = para.replace("{{EMAIL}}", "____________________")
        para = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", para)
        flow.append(Paragraph(para, BODY))

    doc.build(flow)
    return out


def main():
    made = []
    for folder in sorted(p for p in ROOT.iterdir() if p.is_dir()):
        found = extract_letter(folder)
        if not found:
            print(f"  skip  {folder.name} — no cover letter found")
            continue
        out = render(folder, *found)
        made.append(out)
        print(f"  ok    {out.relative_to(ROOT.parent.parent)}")
    print(f"\n{len(made)} cover letter PDF(s) written.")
    return made


if __name__ == "__main__":
    main()
