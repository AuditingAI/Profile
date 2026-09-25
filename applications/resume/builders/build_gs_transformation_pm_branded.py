"""Goldman Sachs - Office of Transformation, Digital Transformation Project
Manager, AI-Driven Strategic Initiatives, Vice President.

The posting's own overview promises "revenue, risk and control, and efficiency
outcomes" from cross-divisional programs. That triad is the spine of this
resume, because he has delivered all three and can price each one: $180M in
capital optimization, consent-order closure accepted by external regulators,
and two automation programs at ~40% and ~35%.

The differentiator is stated plainly rather than implied. Most project managers
on an AI transformation program have to learn the risk-and-control half of it;
he authored an AI governance framework - use-case intake, risk tiering, control
library, post-deployment monitoring KPIs - which is a target-state operating
model for an AI-enabled function, and then built and shipped the tooling that
ran inside it.

Branded through builders/brand.py, per the owner's standing choice (14 Sep).

Run from repo root:
    python3 applications/resume/builders/build_gs_transformation_pm_branded.py [scale]

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
OUT = ROOT / "applications" / "resume" / "Yasir_Malik_Resume_GS_Transformation_PM_VP_Branded.pdf"
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
flow.append(Paragraph("Program &amp; Project Delivery | AI-Enabled Target-State Operating Models &bull; "
                      "Cross-Divisional Transformation &bull; Risk, Control &amp; Efficiency Outcomes", tag))
flow.append(Paragraph("Newark, NJ &bull; YasirAMalik@gmail.com &bull; +1 (786) 704-8536 &bull; "
                      "linkedin.com/in/yasiramalik &bull; auditingai.github.io", contact))

# ---- Summary -----------------------------------------------------------------
flow += section("SUMMARY")
flow.append(Paragraph(
    "Delivers complex cross-divisional programs in banking, against deadlines that do not move and audiences that "
    "do not accept hand-waving. Ran <b>Resolution &amp; Recovery Planning</b> at JPMorgan Chase across <b>50+ "
    "stakeholders</b> in Legal, Treasury, and Operations into Federal Reserve and FDIC submissions, after serving "
    "as <b>Program Manager for CIB Resolution &amp; Recovery Planning</b> coordinating deliverables across legal "
    "entities, controllers, and Treasury. Led consent-order remediation across <b>15+ business units</b> at Citi, "
    "tracking every action and issue to closure with evidence external regulators accepted. The AI half is not "
    "aspiration: authored an AI governance framework &mdash; use-case intake, risk tiering, control library, "
    "post-deployment monitoring KPIs &mdash; which is a target-state operating model for an AI-enabled function, "
    "then gathered requirements, wrote the code, and put the tooling into production. Most project managers on an "
    "AI transformation have to learn the risk-and-control half; that half is the career.", body))

# ---- The triad -------------------------------------------------------------------
flow += section("REVENUE, RISK AND CONTROL, EFFICIENCY &mdash; THE POSTING'S OWN TRIAD, PRICED")
rows = [
    [Paragraph("Outcome", cellh), Paragraph("Programme", cellh), Paragraph("Result", cellh)],
    [Paragraph("Revenue / capital", cell),
     Paragraph("Basel III RWA and capital adequacy reporting across a $50B book of equities, fixed income, and "
               "OTC derivatives; analysis of RWA treatment surfaced optimisation for CFO decision support", cell),
     Paragraph("<b>$180M</b> identified", cell)],
    [Paragraph("Risk and control", cell),
     Paragraph("Consent-order remediation across 15+ business units &mdash; actions and issues tracked to "
               "deadline, issue-closure packages and sustainable-closure evidence authored", cell),
     Paragraph("Accepted by QA and <b>external regulators</b>", cell)],
    [Paragraph("Risk and control", cell),
     Paragraph("Resolution &amp; Recovery Planning across 50+ stakeholders in Legal, Treasury, and Operations, to "
               "statutory deadlines", cell),
     Paragraph("<b>Federal Reserve and FDIC</b> submissions delivered", cell)],
    [Paragraph("Efficiency", cell),
     Paragraph("Automated capital and liquidity reconciliations, removing a recurring source of reporting error", cell),
     Paragraph("<b>~40%</b> less manual review", cell)],
    [Paragraph("Efficiency", cell),
     Paragraph("RAG workpaper assistant &mdash; requirements from the teams who needed it, built in Python and "
               "LangChain, put into production", cell),
     Paragraph("<b>~35%</b> faster review cycle", cell)],
]
t = Table(rows, colWidths=[usable * 0.16, usable * 0.62, usable * 0.22])
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
    "Programme &amp; Project Delivery (scope, timelines, resources, deliverables) | Cross-Divisional Stakeholder "
    "Management (50+ across Legal, Treasury, Operations, Controllers, Model Risk) | Requirements Elicitation &amp; "
    "Target-State Operating Model Design | AI-Enabled Operating Models (use-case intake, risk tiering, control "
    "library, post-deployment monitoring KPIs) | Risk &amp; Issue Management, Tracking and Escalation | Working "
    "Groups &amp; Steering Committees | Senior Management and Board Audit Committee Reporting | Business Cases "
    "&amp; Benefits Realisation | Process Re-engineering &amp; Automation | Regulatory Programme Delivery "
    "(Federal Reserve, FDIC, consent orders) | Excel/VBA &bull; SQL &bull; Python &bull; Tableau &bull; Power BI "
    "&bull; Alteryx &bull; SharePoint", body))

# ---- Experience ----------------------------------------------------------------
flow += section("PROFESSIONAL EXPERIENCE")
flow.append(job("Vice President, Audit Manager &mdash; Citi", "Jul 2021 &ndash; Apr 2026"))
flow.append(Paragraph("Internal Audit, Cross-Enterprise <b>Program &amp; Change Management</b> | New York, NY", sub))
for b in [
    "Ran consent-order remediation across <b>15+ business units</b> as a programme: actions and issues tracked, "
    "escalated, and driven to resolution by their deadlines; issue-closure and sustainable-closure evidence "
    "accepted by quality assurance and by external regulators.",
    "<b>Designed the AI-enabled target state for the audit function</b> &mdash; use-case intake, risk tiering, a "
    "control library, and post-deployment monitoring KPIs, referenced to NIST AI RMF and SR 11-7 &mdash; then "
    "elicited the requirements, built the RAG workpaper assistant (Python, LangChain), and put it into "
    "production: <b>~35%</b> faster review cycle.",
    "Chaired and prepared materials for governance forums; delivered status and escalation reporting to executive "
    "management and the <b>Board Audit Committee</b>. Coached 8+ staff. Citi <i>Delivers with Pride</i> recognition.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Risk Control Manager, Treasury &amp; CIO &mdash; JPMorgan Chase", "Mar 2019 &ndash; Jun 2021"))
flow.append(Paragraph("Capital Controls &amp; Resolution and Recovery Planning | Jersey City, NJ", sub))
for b in [
    "Delivered the <b>Resolution &amp; Recovery Planning</b> programme across <b>50+ stakeholders</b> in Legal, "
    "Treasury, and Operations &mdash; plan, scope, dependencies, and issue management into Federal Reserve and "
    "FDIC submissions against statutory deadlines.",
    "Led CCAR forecast validation and quantitative model challenge over a <b>$2.6T</b> balance sheet under "
    "SR 15-18, coordinating Finance, Treasury, and Model Risk.",
    "Automated capital and liquidity reconciliations: <b>~40%</b> less manual review and a recurring source of "
    "reporting error removed.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Program Manager, CIB Resolution &amp; Recovery Planning &mdash; JPMorgan Chase",
                "2015 &ndash; 2017"))
flow.append(Paragraph("followed by Capital Controller, Basel Measurement &amp; Analytics (Sep 2017 &ndash; Feb 2019) "
                      "| Brooklyn, NY", sub))
for b in [
    "Coordinated CIB regulatory deliverables across legal entities, controllers, and Treasury &mdash; multiple "
    "interdependent workstreams, one immovable date.",
    "As Capital Controller: owned Basel III RWA and capital adequacy reporting for a <b>$50B</b> book; identified "
    "<b>$180M</b> in capital optimisation for CFO decision support.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Assistant Vice President, Global Legal Entity Management &mdash; Citi", "2012 &ndash; 2015"))
flow.append(Paragraph("Tampa, FL", sub))
flow.append(Paragraph("Consolidated <b>500+ legal-entity data sources</b> into governed master data, enabling "
                      "automated FR 2900 and TIC regulatory filings at <b>99.8% accuracy</b> &mdash; a data "
                      "transformation delivered end to end.", bullet, bulletText="•"))

flow.append(job("Bank Examiner, Bureau of Bank Regulation &mdash; Florida Office of Financial Regulation",
                "Apr 2011 &ndash; Mar 2012"))
flow.append(Paragraph("West Palm Beach, FL &bull; earlier: Senior Business Analyst, Retail Credit Risk &mdash; "
                      "Royal Bank of Scotland, Dubai (2008&ndash;2009)", sub))
flow.append(Paragraph("Conducted CAMELS safety-and-soundness examinations alongside federal banking regulators. "
                      "At RBS, built credit-risk MIS over a $500M+ retail portfolio in SAS, SQL, and Excel/VBA.",
                      bullet, bulletText="•"))

# ---- Education & certifications -------------------------------------------------
flow += section("EDUCATION &amp; CERTIFICATIONS")
flow.append(Paragraph(
    "<b>Doctor of Business Administration (DBA), Florida International University</b> &mdash; in progress; "
    "research on how expert judgment behaves under AI assistance &bull; "
    "<b>MBA, Financial Mathematics, Florida International University</b> &mdash; 2011 &bull; "
    "<b>B.Sc., Banking &amp; Finance, London School of Economics</b> &mdash; 2005 &bull; "
    "<b>Columbia Engineering FinTech Boot Camp</b> &mdash; 2021<br/>"
    "<b>Certifications:</b> <b>Registered Scrum Master</b> &bull; FDIC Bank Examiner I &bull; GCP "
    "Social/Behavioral Human Research. <i>In progress:</i> CIA Part 1, IAPP AIGP.", body))

doc = SimpleDocTemplate(str(OUT), pagesize=LETTER,
                        leftMargin=0.55 * inch, rightMargin=0.55 * inch,
                        topMargin=0.36 * inch, bottomMargin=0.36 * inch,
                        title="Yasir A. Malik - Resume - Digital Transformation PM VP, Goldman Sachs",
                        author="Yasir A. Malik", subject="Programme delivery & AI-enabled transformation")
doc.build(flow)
print(f"built {OUT} at S={S} | header: {header_mode()}")
