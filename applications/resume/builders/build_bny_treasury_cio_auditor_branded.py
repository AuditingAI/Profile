"""BNY - Vice President, Auditor, Corporate Treasury, Chief Investment Office
and Risk (New York).

The single best-matched role on the board, and the pitch is one sentence: he
audits the function he used to run. At JPMorgan Chase his title was Risk
Control Manager, Treasury & CIO - he owned the first-line control framework for
exactly the activities this seat audits. Add the capital side (Basel III RWA on
a $50B book, CCAR over $2.6T), the liquidity and resolution side (RRP into
Federal Reserve and FDIC submissions), five years of the audit craft itself at
Citi, and CAMELS examinations at the Florida OFR, and every column of the audit
universe named in the title is covered from both sides.

The resume is built around that: a table mapping each function under audit to
the seat he held in it.

Branded through builders/brand.py, per the owner's standing choice (14 Sep).

Run from repo root:
    python3 applications/resume/builders/build_bny_treasury_cio_auditor_branded.py [scale]

Standing rules: never "OCC"; examiner history is the Florida Office of
Financial Regulation; DBA in progress; CIA in progress; never a
career-length number.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brand import GOLD, MUTED, brand_header, header_mode  # noqa: E402

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "applications" / "resume" / "Yasir_Malik_Resume_BNY_Treasury_CIO_Auditor_VP_Branded.pdf"
S = float(sys.argv[1]) if len(sys.argv) > 1 else 0.86

body = ParagraphStyle("body", fontName="Times-Roman", fontSize=8.9 * S,
                      leading=11.0 * S, alignment=TA_JUSTIFY, spaceAfter=2.0 * S)
name = ParagraphStyle("name", parent=body, alignment=TA_CENTER, fontName="Times-Bold",
                      fontSize=15.5 * S, leading=18 * S, spaceAfter=1.5)
tag = ParagraphStyle("tag", parent=body, alignment=TA_CENTER, fontSize=8.9 * S,
                     leading=11 * S, spaceAfter=1)
contact = ParagraphStyle("contact", parent=tag, fontSize=8.5 * S, spaceAfter=4 * S)
h2 = ParagraphStyle("h2", parent=body, fontName="Times-Bold", fontSize=9.4 * S,
                    leading=11 * S, spaceBefore=4.5 * S, spaceAfter=1.5,
                    textColor=HexColor("#000000"))
bullet = ParagraphStyle("bullet", parent=body, leftIndent=11, bulletIndent=1,
                        spaceAfter=1.2 * S)
sub = ParagraphStyle("sub", parent=body, fontName="Times-Italic",
                     fontSize=8.5 * S, textColor=MUTED, spaceAfter=1)
cell = ParagraphStyle("cell", parent=body, fontSize=8.1 * S, leading=9.8 * S,
                      alignment=TA_LEFT, spaceAfter=0)
cellh = ParagraphStyle("cellh", parent=cell, fontName="Times-Bold")

RULE = ('<para><font size="1" color="#000000"><u>' + "&nbsp;" * 300 + "</u></font></para>")


def rule():
    return Paragraph(RULE, ParagraphStyle("r", parent=body, spaceAfter=2, leading=2))


def job(title, dates):
    return Paragraph(f'<b>{title}</b><font color="#000000"> &nbsp;&nbsp;&mdash;&nbsp;&nbsp; </font><b>{dates}</b>',
                     body)


def section(title):
    return [Paragraph(title, h2), rule()]


usable = LETTER[0] - 1.1 * inch
flow = []

# ---- Letterhead + identity -----------------------------------------------------
flow += brand_header(body, scale=S)
flow.append(Paragraph("YASIR A. MALIK", name))
flow.append(Paragraph("Internal Audit &mdash; Corporate Treasury, Chief Investment Office &amp; Risk | "
                      "Capital, Liquidity &amp; Stress Testing &bull; First-Line Control Frameworks &bull; "
                      "Former Bank Examiner", tag))
flow.append(Paragraph("Newark, NJ &bull; YasirAMalik@gmail.com &bull; +1 (786) 704-8536 &bull; "
                      "linkedin.com/in/yasiramalik &bull; auditingai.github.io", contact))

# ---- Summary -----------------------------------------------------------------
flow += section("SUMMARY")
flow.append(Paragraph(
    "Audits the function he used to run. At JPMorgan Chase his title was <b>Risk Control Manager, Treasury &amp; "
    "CIO</b> &mdash; he owned the first-line control framework for the capital and liquidity activities this seat "
    "examines, defined the supervisor expectations and escalation paths, and automated the reconciliations behind "
    "them (~40% less manual review). He also led <b>CCAR</b> forecast validation and quantitative model challenge "
    "over a <b>$2.6T</b> balance sheet under SR 15-18, owned Basel III RWA and capital adequacy reporting for a "
    "<b>$50B</b> book, and ran Resolution &amp; Recovery Planning into Federal Reserve and FDIC submissions. The "
    "audit craft is the other half: five years as VP, Audit Manager at Citi Internal Audit leading risk-based "
    "audits across <b>15+ business units</b>, with consent-order issue-closure evidence accepted by quality "
    "assurance and external regulators &mdash; and, before all of it, CAMELS safety-and-soundness examinations as "
    "a bank examiner with the Florida Office of Financial Regulation. Every column of this audit universe has been "
    "seen from both sides of the control.", body))

# ---- The audit universe ----------------------------------------------------------
flow += section("THE AUDIT UNIVERSE, AND THE SEAT HELD IN EACH")
rows = [
    [Paragraph("Function under audit", cellh), Paragraph("Where it was done &mdash; from the inside", cellh)],
    [Paragraph("<b>Corporate Treasury</b>", cell),
     Paragraph("Risk Control Manager, <b>Treasury &amp; CIO</b>, JPMorgan Chase (2019&ndash;21): owned the "
               "first-line control framework &mdash; controls, supervisor expectations, escalation &mdash; and "
               "automated capital and liquidity reconciliations, cutting manual review ~40% and removing a "
               "recurring source of reporting error.", cell)],
    [Paragraph("<b>Chief Investment Office</b>", cell),
     Paragraph("Same seat. CIO capital activities sat inside that mandate, alongside Finance, Treasury, and "
               "Model Risk on capital-planning submissions.", cell)],
    [Paragraph("<b>Capital &amp; stress testing</b>", cell),
     Paragraph("CCAR forecast validation and qualitative model challenge over a $2.6T balance sheet under "
               "SR 15-18. Earlier, as Capital Controller, Basel Measurement &amp; Analytics: Basel III RWA and "
               "capital adequacy reporting for a $50B book of equities, fixed income, and OTC derivatives, with "
               "$180M in capital optimisation identified for CFO decision support.", cell)],
    [Paragraph("<b>Liquidity &amp; resolution</b>", cell),
     Paragraph("Resolution &amp; Recovery Planning across 50+ stakeholders in Legal, Treasury, and Operations, "
               "delivering regulator-ready submissions to the Federal Reserve and FDIC against statutory "
               "deadlines. Earlier: Program Manager, CIB Resolution &amp; Recovery Planning.", cell)],
    [Paragraph("<b>Risk &amp; the audit craft</b>", cell),
     Paragraph("VP, Audit Manager, Citi Internal Audit: risk-based audits end to end across 15+ business units "
               "&mdash; control design and operating effectiveness, opinions on the control environment, "
               "consent-order issue closure accepted by QA and external regulators, Board Audit Committee "
               "reporting.", cell)],
    [Paragraph("<b>The regulator's standard</b>", cell),
     Paragraph("Bank Examiner, Florida Office of Financial Regulation: CAMELS safety-and-soundness examinations "
               "&mdash; capital, asset quality, earnings, liquidity, market risk &mdash; alongside federal "
               "banking regulators. <b>FDIC Bank Examiner I.</b>", cell)],
]
t = Table(rows, colWidths=[usable * 0.24, usable * 0.76])
t.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.5, colors.black), ("LINEBELOW", (0, 0), (-1, 0), 0.9, GOLD),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 1.3), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.3),
]))
flow.append(t)

# ---- Competencies --------------------------------------------------------------
flow += section("CORE COMPETENCIES")
flow.append(Paragraph(
    "Internal Audit &amp; Controls (IIA Standards, COSO, Three Lines of Defense, SOX ITGC) | Treasury &amp; CIO "
    "Control Frameworks | Capital Adequacy &amp; Basel III RWA | CCAR / SR 15-18 Stress Testing &amp; Model "
    "Challenge | Liquidity Risk &amp; Regulatory Reporting (FR 2900, TIC) | Resolution &amp; Recovery Planning | "
    "Consent-Order Remediation &amp; Sustainable Closure | Regulatory Examination (Federal Reserve, FDIC, state "
    "supervision) | Model Risk (SR 11-7) &amp; AI Governance (NIST AI RMF) | Audit Analytics &amp; Automation "
    "(Python, SQL, Alteryx, Tableau, Power BI) | Board Audit Committee Reporting", body))

# ---- Experience ----------------------------------------------------------------
flow += section("PROFESSIONAL EXPERIENCE")
flow.append(job("Vice President, Audit Manager &mdash; Citi", "Jul 2021 &ndash; Apr 2026"))
flow.append(Paragraph("Internal Audit, Cross-Enterprise Program &amp; Change Management | New York, NY", sub))
for b in [
    "Led risk-based audits end to end across <b>15+ business units</b> &mdash; planning, population and sample "
    "definition, control design and operating-effectiveness testing, issue dimensioning, and the overall opinion "
    "on the control environment.",
    "Drove <b>consent-order</b> audit execution: issue-closure packages and sustainable-closure evidence accepted "
    "by quality assurance and by external regulators; escalated where remediation was not credible.",
    "Delivered executive and <b>Board Audit Committee</b> reporting; coached 8+ auditors. Built and shipped a "
    "RAG-based workpaper assistant (Python, LangChain) that cut review cycle time ~35% and created continuous "
    "coverage where sampling had been the only option. Citi <i>Delivers with Pride</i> recognition.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Risk Control Manager, Treasury &amp; CIO &mdash; JPMorgan Chase", "Mar 2019 &ndash; Jun 2021"))
flow.append(Paragraph("First-Line Capital Controls &amp; Resolution and Recovery Planning | Jersey City, NJ", sub))
for b in [
    "<b>Owned the first-line control framework for Treasury &amp; CIO capital activities</b>: defined the "
    "controls, the supervisor's expectations, and the escalation path, then built the monitoring.",
    "Led <b>CCAR</b> forecast validation and quantitative model challenge over a <b>$2.6T</b> balance sheet under "
    "SR 15-18, partnering with Finance, Treasury, and Model Risk on capital-planning submissions.",
    "Ran <b>Resolution &amp; Recovery Planning</b> across 50+ stakeholders in Legal, Treasury, and Operations, "
    "delivering to the Federal Reserve and FDIC. Automated capital and liquidity reconciliations: ~40% less "
    "manual review.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Capital Controller, Basel Measurement &amp; Analytics &mdash; JPMorgan Chase",
                "Sep 2017 &ndash; Feb 2019"))
flow.append(Paragraph("Brooklyn, NY &bull; preceded by Program Manager, CIB Resolution &amp; Recovery Planning "
                      "(2015&ndash;2017)", sub))
flow.append(Paragraph("Owned <b>Basel III RWA and capital adequacy reporting</b> for a <b>$50B</b> book of "
                      "equities, fixed income, and OTC derivatives; analysis of RWA treatment identified "
                      "<b>$180M</b> in capital optimisation for CFO decision support.", bullet, bulletText="•"))

flow.append(job("Assistant Vice President, Global Legal Entity Management &mdash; Citi", "2012 &ndash; 2015"))
flow.append(Paragraph("Tampa, FL", sub))
flow.append(Paragraph("Consolidated 500+ legal-entity data sources into governed master data, enabling automated "
                      "<b>FR 2900</b> and <b>TIC</b> regulatory filings at <b>99.8% accuracy</b>.",
                      bullet, bulletText="•"))

flow.append(job("Bank Examiner, Bureau of Bank Regulation &mdash; Florida Office of Financial Regulation",
                "Apr 2011 &ndash; Mar 2012"))
flow.append(Paragraph("West Palm Beach, FL &bull; earlier: Senior Business Analyst, Retail Credit Risk &mdash; "
                      "Royal Bank of Scotland, Dubai (2008&ndash;2009)", sub))
flow.append(Paragraph("Conducted <b>CAMELS</b> safety-and-soundness examinations of state and national banks "
                      "alongside federal banking regulators; authored workpapers supporting formal enforcement "
                      "actions.", bullet, bulletText="•"))

# ---- Education & certifications -------------------------------------------------
flow += section("EDUCATION &amp; CERTIFICATIONS")
flow.append(Paragraph(
    "<b>Doctor of Business Administration (DBA), Florida International University</b> &mdash; in progress, "
    "&bull; <b>MBA, Financial Mathematics, Florida International University</b> &mdash; "
    "2011 &bull; <b>B.Sc., Banking &amp; Finance, London School of Economics</b> &mdash; 2005 &bull; "
    "<b>Columbia Engineering FinTech Boot Camp</b> &mdash; 2021<br/>"
    "<b>Certifications:</b> <b>FDIC Bank Examiner I</b> &bull; Registered Scrum Master &bull; GCP "
    "Social/Behavioral Human Research. <i>In progress:</i> <b>CIA Part 1</b>, IAPP AIGP.", body))

doc = SimpleDocTemplate(str(OUT), pagesize=LETTER,
                        leftMargin=0.55 * inch, rightMargin=0.55 * inch,
                        topMargin=0.36 * inch, bottomMargin=0.36 * inch,
                        title="Yasir A. Malik - Resume - VP Auditor, Corporate Treasury, CIO & Risk (BNY)",
                        author="Yasir A. Malik", subject="Internal Audit - Treasury, CIO & Risk")
doc.build(flow)
print(f"built {OUT} at S={S} | header: {header_mode()}")
