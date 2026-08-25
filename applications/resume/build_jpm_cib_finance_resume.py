"""Build the JPMorgan Audit Manager (Asset & Wealth Management) resume as a
single-page, ATS-clean PDF. Tighter than build_google_tpm_resume.py because
the JPM variant has one more experience block (JPMC tenure spans two roles).

Run from repo root: python3 applications/resume/build_jpm_audit_mgr_resume.py
"""
from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

HERE = Path(__file__).resolve().parent
MD = HERE / "resume_jpm_cib_finance_audit.md"
PDF = HERE / "Yasir_Malik_Resume_JPM_CIB_Finance_Audit.pdf"


def _inline(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(?!\s)([^*]+?)\*(?!\*)", r"<i>\1</i>", text)
    return text


def build() -> Path:
    base = getSampleStyleSheet()
    body = ParagraphStyle("Body", parent=base["BodyText"], fontName="Helvetica",
                          fontSize=7.9, leading=9.5, spaceAfter=1.5)
    h1 = ParagraphStyle("H1", parent=base["Heading1"], fontName="Helvetica-Bold",
                        fontSize=14.5, leading=16, spaceAfter=1.5, textColor="#222222")
    h2 = ParagraphStyle("H2", parent=base["Heading2"], fontName="Helvetica-Bold",
                        fontSize=9.5, leading=11, spaceBefore=4.5, spaceAfter=1.5,
                        textColor="#1a1a1a")
    bullet = ParagraphStyle("Bullet", parent=body, leftIndent=11, bulletIndent=2,
                            spaceAfter=1.5)
    italic = ParagraphStyle("Italic", parent=body, fontName="Helvetica-Oblique",
                            textColor="#555555", spaceAfter=1.5)

    flow = []
    for line in MD.read_text(encoding="utf-8").splitlines():
        s = line.rstrip()
        if not s.strip():
            flow.append(Spacer(1, 1.5))
        elif s.startswith("## "):
            flow.append(Paragraph(_inline(s[3:]), h2))
        elif s.startswith("# "):
            flow.append(Paragraph(_inline(s[2:]), h1))
        elif s.startswith("- "):
            flow.append(Paragraph(_inline(s[2:]), bullet, bulletText="•"))
        elif s.startswith("*") and s.endswith("*") and not s.startswith("**"):
            flow.append(Paragraph(_inline(s.strip("*")), italic))
        else:
            flow.append(Paragraph(_inline(s), body))

    doc = SimpleDocTemplate(
        str(PDF),
        pagesize=LETTER,
        leftMargin=0.42 * inch,
        rightMargin=0.42 * inch,
        topMargin=0.34 * inch,
        bottomMargin=0.34 * inch,
        title="Yasir A. Malik - Resume - Internal Audit Manager VP, CIB Finance (210759059)",
        author="Yasir A. Malik",
    )
    doc.build(flow)
    return PDF


if __name__ == "__main__":
    p = build()
    print(f"wrote {p}")
