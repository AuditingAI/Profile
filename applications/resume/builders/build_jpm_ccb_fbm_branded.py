"""JPMorgan CCB Finance & Business Management resume, Audit the Algorithm brand.

Built for req 210776418 (Business Management / Finance / Consumer & Community
Banking, Jersey City + Columbus, $128,250-$210,000).

Positioning differs deliberately from the CIB Finance AUDIT variant. That one
headlines audit opinions and consent-order closure. A Finance & Business
Management role is not an assurance role: it owns the numbers rather than
opining on them. So the same evidence is re-pointed at financial control,
capital and liquidity reporting, CFO decision support, and reporting
automation - and the audit tenure is framed as control fluency rather than as
the main event.

The honest gap is named in the summary rather than hidden: twenty years of this
record is corporate and investment bank, not consumer. Pretending otherwise
fails at the first interview question.

Run from repo root:
    python3 applications/resume/builders/build_jpm_ccb_fbm_branded.py

Standing rules: never "OCC"; examiner history is the Florida Office of
Financial Regulation; DBA is in progress (expected 2028); CIA is in progress.
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "applications" / "resume" / "Yasir_Malik_Resume_JPM_CCB_FBM_Branded.pdf"

GOLD = HexColor("#B8860B")
MUTED = HexColor("#6F6754")

S = 0.86  # global scale; nudge down if content grows past one page

body = ParagraphStyle("body", fontName="Times-Roman", fontSize=8.9 * S,
                      leading=11.1 * S, alignment=TA_JUSTIFY, spaceAfter=2.2 * S)
mark = ParagraphStyle("mark", parent=body, alignment=TA_CENTER, fontSize=15 * S,
                      leading=17 * S, spaceAfter=1)
name = ParagraphStyle("name", parent=body, alignment=TA_CENTER, fontName="Times-Bold",
                      fontSize=15.5 * S, leading=18 * S, spaceAfter=1.5)
tag = ParagraphStyle("tag", parent=body, alignment=TA_CENTER, fontSize=8.9 * S,
                     leading=11 * S, spaceAfter=1)
contact = ParagraphStyle("contact", parent=tag, fontSize=8.5 * S, spaceAfter=4.5 * S)
h2 = ParagraphStyle("h2", parent=body, fontName="Times-Bold", fontSize=9.4 * S,
                    leading=11 * S, spaceBefore=5 * S, spaceAfter=1.5,
                    textColor=HexColor("#000000"))
bullet = ParagraphStyle("bullet", parent=body, leftIndent=11, bulletIndent=1,
                        spaceAfter=1.3 * S)
sub = ParagraphStyle("sub", parent=body, fontName="Times-Italic",
                     fontSize=8.5 * S, textColor=MUTED, spaceAfter=1)
cell = ParagraphStyle("cell", parent=body, fontSize=8.1 * S, leading=9.9 * S,
                      alignment=TA_LEFT, spaceAfter=0)
cellh = ParagraphStyle("cellh", parent=cell, fontName="Times-Bold")

RULE = ('<para><font size="1" color="#000000">'
        '<u>' + "&nbsp;" * 300 + "</u></font></para>")


def rule():
    return Paragraph(RULE, ParagraphStyle("r", parent=body, spaceAfter=2, leading=2))


def job(title, dates):
    return Paragraph(
        f'<b>{title}</b><font color="#000000"> &nbsp;&nbsp;&mdash;&nbsp;&nbsp; </font>'
        f'<b>{dates}</b>', body)


def section(title):
    return [Paragraph(title, h2), rule()]


flow = []

# ---- Brand + identity --------------------------------------------------------
flow.append(Paragraph(
    '<font color="#B8860B"><b>Audit</b></font> '
    '<font color="#6F6754"><i>the</i></font> '
    '<font color="#B8860B"><b>Algorithm</b></font>', mark))
flow.append(Paragraph("YASIR A. MALIK", name))
flow.append(Paragraph("AI Valuation Chief of Staff, Vice President &mdash; Finance &amp; Business Management | Financial Control "
                      "&bull; Capital &amp; Liquidity Reporting &bull; AI Governance &bull; Reporting Automation", tag))
flow.append(Paragraph("Newark, NJ &bull; YasirAMalik@gmail.com &bull; +1 (786) 704-8536 &bull; "
                      "linkedin.com/in/yasiramalik &bull; github.com/MalikAI-786 &bull; auditingai.github.io",
                      contact))

# ---- Summary -----------------------------------------------------------------
flow += section("SUMMARY")
flow.append(Paragraph(
    "Twenty years in financial control, capital reporting, and business management across JPMorgan Chase and Citi. "
    "Six of those years were inside JPMorgan &mdash; owning Basel III RWA and capital adequacy reporting on a $50B "
    "book and surfacing $180M in capital optimization for CFO decision support, running CCAR forecast validation "
    "over a $2.6T balance sheet, and coordinating CIB regulatory deliverables across legal entities, controllers, "
    "and Treasury. Consistent pattern across every role: take a reporting process that is manual, slow, and "
    "error-prone, and make it governed, automated, and defensible &mdash; reconciliations down ~40%, review cycle "
    "down ~35%, 500+ legal-entity data sources consolidated to 99.8% filing accuracy. Began as a bank examiner "
    "with the Florida Office of Financial Regulation, so the control standard was learned from the examiner's side "
    "of the table. <b>Honest framing:</b> this record is Corporate &amp; Investment Bank and enterprise Finance, not "
    "Consumer &amp; Community Banking &mdash; the consumer product set is ramp, the financial-control discipline "
    "transfers intact. Newark resident; Jersey City is a 25-minute commute.", body))

# ---- Results table ------------------------------------------------------------
flow += section("SELECTED RESULTS")
rows = [
    [Paragraph("Result", cellh), Paragraph("What it was", cellh), Paragraph("Where", cellh)],
    [Paragraph("$180M", cell),
     Paragraph("Capital optimization opportunities identified and quantified for CFO decision support, from Basel III "
               "RWA and capital adequacy reporting across a $50B portfolio", cell),
     Paragraph("JPMorgan Chase", cell)],
    [Paragraph("~40% less", cell),
     Paragraph("Manual review effort on capital and liquidity reconciliations, by automating them &mdash; and removing "
               "a recurring source of reporting error", cell),
     Paragraph("JPMorgan Chase", cell)],
    [Paragraph("99.8%", cell),
     Paragraph("Filing accuracy on automated FR 2900 and TIC regulatory reporting, after consolidating 500+ "
               "legal-entity data sources into governed master data", cell),
     Paragraph("Citi", cell)],
    [Paragraph("~35% faster", cell),
     Paragraph("Review cycle time, by building and shipping a retrieval-augmented reporting assistant (Python, "
               "LangChain, Alteryx integration) &mdash; built it, did not commission it", cell),
     Paragraph("Citi", cell)],
]
usable = LETTER[0] - 1.1 * inch
table = Table(rows, colWidths=[usable * 0.14, usable * 0.68, usable * 0.18])
table.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ("LINEBELOW", (0, 0), (-1, 0), 0.9, GOLD),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
]))
flow.append(table)

# ---- Competencies --------------------------------------------------------------
flow += section("CORE COMPETENCIES")
flow.append(Paragraph(
    "Financial Control &amp; Close Governance | Capital Adequacy &amp; Basel III RWA Reporting | CCAR and SR 15-18 "
    "Capital Planning | Liquidity and Treasury Reporting | Legal-Entity and Management Reporting | Regulatory "
    "Reporting (FR 2900, TIC) | Reporting Automation and Process Re-engineering | Data Governance for Financial "
    "Reporting | Executive and Board-Level Reporting | Cross-Functional Program Delivery (50+ stakeholders) | "
    "Control Design and Operating-Effectiveness Assessment | Python &bull; SQL &bull; Alteryx &bull; Tableau &bull; "
    "Power BI &bull; Excel/VBA", body))

# ---- Experience ----------------------------------------------------------------
flow += section("PROFESSIONAL EXPERIENCE")

flow.append(job("Capital Controller, Basel Measurement &amp; Analytics &mdash; JPMorgan Chase",
                "Sep 2017 &ndash; Feb 2019"))
flow.append(Paragraph("Brooklyn, NY &bull; preceded by Program Manager, CIB Resolution &amp; Recovery Planning "
                      "(2015&ndash;2017)", sub))
for b in [
    "Owned <b>Basel III RWA and capital adequacy reporting</b> across a $50B portfolio of equities, fixed income, and "
    "OTC derivatives &mdash; the monthly and quarterly numbers, their substantiation, and their defence to Finance "
    "leadership.",
    "Identified and quantified <b>$180M in capital optimization</b> for CFO decision support, by analysing where "
    "RWA treatment and booking structure were costing capital unnecessarily.",
    "As Program Manager, CIB RRP: coordinated regulatory deliverables across legal entities, controllers, and "
    "Treasury &mdash; business management in practice, against deadlines that do not move.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Risk Control Manager, Treasury &amp; CIO &mdash; JPMorgan Chase", "Mar 2019 &ndash; Jun 2021"))
flow.append(Paragraph("Capital Controls &amp; Resolution and Recovery Planning | Jersey City, NJ", sub))
for b in [
    "Led <b>CCAR forecast validation</b> and qualitative model challenge over a <b>$2.6T balance sheet</b> under "
    "SR 15-18, partnering with Finance, Treasury, and Model Risk on capital-planning submissions.",
    "<b>Automated capital and liquidity reconciliations, cutting manual review effort ~40%</b> and eliminating a "
    "recurring source of reporting error &mdash; the reporting-efficiency work this function lives on.",
    "Ran Resolution &amp; Recovery Planning across <b>50+ stakeholders</b> in Legal, Treasury, and Operations, "
    "delivering to the Federal Reserve and FDIC against statutory deadlines.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Vice President, Audit Manager &mdash; Citi", "Jul 2021 &ndash; Apr 2026"))
flow.append(Paragraph("Internal Audit, Cross-Enterprise Program &amp; Change Management | New York, NY", sub))
for b in [
    "Assessed control design and operating effectiveness over <b>financial, business, and technology processes "
    "across 15+ business units</b> &mdash; four years spent judging whether a reporting control actually works, "
    "which is the fastest way to learn how to build one that does.",
    "Built and shipped a <b>retrieval-augmented reporting assistant</b> (Python, LangChain, vector search, Alteryx "
    "integration) that cut review cycle time <b>~35%</b>.",
    "Delivered executive and <b>Board-level reporting</b>; coached 8+ staff. Citi <i>Delivers with Pride</i> "
    "recognition.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Assistant Vice President, Global Legal Entity Management &mdash; Citi", "2012 &ndash; 2015"))
flow.append(Paragraph("Tampa, FL", sub))
flow.append(Paragraph(
    "Consolidated <b>500+ legal-entity data sources</b> into governed master data, enabling automated <b>FR 2900 and "
    "TIC</b> regulatory filings at <b>99.8% accuracy</b> &mdash; legal-entity and management reporting at source.",
    bullet, bulletText="•"))

flow.append(job("Bank Examiner, Bureau of Bank Regulation &mdash; Florida Office of Financial Regulation",
                "Apr 2011 &ndash; Mar 2012"))
flow.append(Paragraph("West Palm Beach, FL", sub))
flow.append(Paragraph(
    "Safety-and-soundness examinations across credit, liquidity, and operational risk alongside federal banking "
    "regulators. <b>FDIC Bank Examiner I.</b>", bullet, bulletText="•"))

# ---- Education -------------------------------------------------------------------
flow += section("EDUCATION &amp; CERTIFICATIONS")
flow.append(Paragraph(
    "<b>Doctor of Business Administration, Florida International University</b> &mdash; in progress, expected 2028 | "
    "GPA 3.81. <b>MBA, Financial Mathematics, Florida International University</b> &mdash; 2011 &bull; "
    "<b>B.Sc., Banking &amp; Finance, London School of Economics</b> &mdash; 2005 &bull; "
    "<b>Columbia Engineering FinTech Boot Camp</b> &mdash; 2021<br/>"
    "<b>Certifications:</b> FDIC Bank Examiner I &bull; Registered Scrum Master &bull; GCP Human Subjects Research. "
    "<i>In progress:</i> CIA Part 1, CISA, IAPP AIGP.", body))

doc = SimpleDocTemplate(str(OUT), pagesize=LETTER,
                        leftMargin=0.55 * inch, rightMargin=0.55 * inch,
                        topMargin=0.36 * inch, bottomMargin=0.36 * inch,
                        title="Yasir A. Malik - Resume - AI Valuation Chief of Staff VP, F&BM (210776418)",
                        author="Yasir A. Malik",
                        subject="Finance & Business Management")
doc.build(flow)
print(f"built {OUT}")
