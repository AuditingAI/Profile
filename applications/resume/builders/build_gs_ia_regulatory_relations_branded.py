"""Goldman Sachs - Internal Audit, Regulatory Relations Team, Vice President.

The posting is the liaison seat between Internal Audit and the regulators:
oversee the examination process, coordinate information requests and
responses, monitor undertakings made to regulators, report to senior
management, own the document warehouse. He has sat in every chair that seat
faces - the examiner who ran the exams, the first-line manager who made the
submissions, the auditor who tracked the undertakings to closure. That is the
whole argument, and the resume is built around it.

Branded at the owner's request (13 Sep 2026), through builders/brand.py.

Run from repo root:
    python3 applications/resume/builders/build_gs_ia_regulatory_relations_branded.py [scale]

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
OUT = ROOT / "applications" / "resume" / "Yasir_Malik_Resume_GS_IA_RegRelations_VP_Branded.pdf"
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
flow.append(Paragraph("Regulatory Relations &amp; Internal Audit | Former Bank Examiner &bull; Regulatory "
                      "Examinations, Submissions &amp; Undertakings &bull; Senior Management Reporting", tag))
flow.append(Paragraph("Newark, NJ &bull; YasirAMalik@gmail.com &bull; +1 (786) 704-8536 &bull; "
                      "linkedin.com/in/yasiramalik &bull; auditingai.github.io", contact))

# ---- Summary -----------------------------------------------------------------
flow += section("SUMMARY")
flow.append(Paragraph(
    "Has sat in every chair a Regulatory Relations seat faces. As a <b>bank examiner</b> with the Florida Office of "
    "Financial Regulation, ran safety-and-soundness examinations alongside federal banking regulators and wrote "
    "the workpapers behind enforcement actions &mdash; the regulator's side of the request. At JPMorgan Chase, "
    "made the submissions: ran <b>Resolution &amp; Recovery Planning</b> across 50+ stakeholders in Legal, "
    "Treasury, and Operations into Federal Reserve and FDIC filings against statutory deadlines, and led CCAR "
    "validation over a $2.6T balance sheet. At Citi Internal Audit, tracked the undertakings: led "
    "<b>consent-order</b> issue closure across 15+ business units, authoring the evidence that quality assurance "
    "and external regulators accepted. Runs the process as well as the relationship &mdash; consolidated 500+ "
    "legal-entity data sources into a governed repository at 99.8% filing accuracy, automated reconciliations "
    "(~40% less manual review), and built a workpaper assistant (~35% faster review). Reports to executive "
    "management and the Board Audit Committee. DBA candidate at FIU.", body))

# ---- Mapping ---------------------------------------------------------------------
flow += section("THE ROLE'S RESPONSIBILITIES, AGAINST THE RECORD")
rows = [
    [Paragraph("The posting asks for", cellh), Paragraph("Where it has been done", cellh)],
    [Paragraph("Liaison between Internal Audit and the regulators; oversee the examination process", cell),
     Paragraph("Ran examinations as a state bank examiner alongside federal regulators (Florida OFR); managed "
               "the regulated side of Federal Reserve and FDIC submissions at JPMorgan; worked consent-order "
               "interactions with external regulators at Citi.", cell)],
    [Paragraph("Track incoming regulatory matters; coordinate information requests and responses across "
               "functional teams", cell),
     Paragraph("Resolution &amp; Recovery Planning program: 50+ stakeholders across Legal, Treasury, Operations, "
               "Controllers, and Model Risk delivering regulator-ready submissions to non-negotiable deadlines; "
               "CIB RRP Program Manager coordinating deliverables across legal entities.", cell)],
    [Paragraph("Monitor teams' progress in completing undertakings made to regulators", cell),
     Paragraph("Consent-order remediation at Citi: issue-closure packages and sustainable-closure evidence across "
               "15+ business units, accepted by quality assurance and by external regulators; escalated where "
               "remediation was not credible.", cell)],
    [Paragraph("Best practices for regulatory interactions; senior management reporting; escalation", cell),
     Paragraph("Executive and Board Audit Committee reporting at Citi; supervisory-expectation and escalation "
               "design as first-line Risk Control Manager at JPMorgan; examiner-side view of what a credible "
               "response looks like.", cell)],
    [Paragraph("Own and re-engineer the team's processes and controls; maintain a centralized warehouse of "
               "requests, responses and commitments", cell),
     Paragraph("500+ legal-entity data sources consolidated into governed master data with ownership and lineage "
               "(99.8% filing accuracy); automated reconciliations, ~40% less manual review; RAG workpaper "
               "assistant, ~35% faster review &mdash; built, not commissioned.", cell)],
]
t = Table(rows, colWidths=[usable * 0.36, usable * 0.64])
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
    "Regulatory Examination Management | Regulatory Submissions &amp; Information Requests (Federal Reserve, "
    "FDIC, state supervision) | Undertakings &amp; Consent-Order Remediation Tracking | Internal Audit &amp; "
    "Controls (IIA Standards, COSO, Three Lines of Defense) | Senior Management &amp; Audit Committee Reporting | "
    "Stakeholder Management across Legal, Compliance, Finance, Treasury, Operations | Process Re-engineering "
    "&amp; Automation | Document Governance &amp; Centralized Repositories | Capital &amp; Liquidity (CCAR, Basel "
    "III, RRP) | Excel/VBA &bull; PowerPoint &bull; SharePoint &bull; Tableau &bull; Power BI &bull; Alteryx "
    "&bull; Python &bull; SQL", body))

# ---- Experience ----------------------------------------------------------------
flow += section("PROFESSIONAL EXPERIENCE")
flow.append(job("Vice President, Audit Manager &mdash; Citi", "Jul 2021 &ndash; Apr 2026"))
flow.append(Paragraph("Internal Audit, Cross-Enterprise Program &amp; Change Management | New York, NY", sub))
for b in [
    "Led consent-order audit execution across 15+ business units: tracked undertakings to closure, authored "
    "issue-closure packages and sustainable-closure evidence accepted by quality assurance and external regulators.",
    "Led risk-based audits end to end &mdash; control design and operating effectiveness across business, "
    "finance, and technology risk; opinions on the control environment; escalation where remediation was not credible.",
    "Delivered executive and Board Audit Committee reporting; coached 8+ auditors. Built and shipped a RAG "
    "workpaper assistant (Python, LangChain) that cut review cycle time ~35%. Citi <i>Delivers with Pride</i> recognition.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))
flow.append(job("Risk Control Manager, Treasury &amp; CIO &mdash; JPMorgan Chase", "Mar 2019 &ndash; Jun 2021"))
flow.append(Paragraph("First-Line Capital Controls &amp; Resolution and Recovery Planning | Jersey City, NJ", sub))
for b in [
    "Ran Resolution &amp; Recovery Planning across 50+ stakeholders in Legal, Treasury, and Operations, "
    "delivering regulator-ready submissions to the Federal Reserve and FDIC against statutory deadlines.",
    "Led CCAR forecast validation and qualitative model challenge over a $2.6T balance sheet under SR 15-18; "
    "automated capital and liquidity reconciliations, cutting manual review ~40%.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))
flow.append(job("Capital Controller, Basel Measurement &amp; Analytics &mdash; JPMorgan Chase",
                "Sep 2017 &ndash; Feb 2019"))
flow.append(Paragraph("Brooklyn, NY &bull; preceded by Program Manager, CIB Resolution &amp; Recovery Planning "
                      "(2015&ndash;2017), coordinating regulatory deliverables across legal entities, controllers, "
                      "and Treasury", sub))
flow.append(Paragraph("Owned Basel III RWA and capital adequacy reporting for a $50B book; identified $180M in "
                      "capital optimization for CFO decision support.", bullet, bulletText="•"))
flow.append(job("Assistant Vice President, Global Legal Entity Management &mdash; Citi", "2012 &ndash; 2015"))
flow.append(Paragraph("Tampa, FL", sub))
flow.append(Paragraph("Consolidated 500+ legal-entity data sources into governed master data, enabling automated "
                      "FR 2900 and TIC regulatory filings at 99.8% accuracy.", bullet, bulletText="•"))
flow.append(job("Bank Examiner, Bureau of Bank Regulation &mdash; Florida Office of Financial Regulation",
                "Apr 2011 &ndash; Mar 2012"))
flow.append(Paragraph("West Palm Beach, FL &bull; earlier: Senior Business Analyst, Retail Credit Risk &mdash; Royal "
                      "Bank of Scotland, Dubai (2008&ndash;2009)", sub))
flow.append(Paragraph("Conducted CAMELS safety-and-soundness examinations of state and national banks alongside "
                      "federal banking regulators; authored workpapers supporting formal enforcement actions.",
                      bullet, bulletText="•"))

# ---- Education & certifications -------------------------------------------------
flow += section("EDUCATION &amp; CERTIFICATIONS")
flow.append(Paragraph(
    "<b>Doctor of Business Administration (DBA), Florida International University</b> &mdash; in progress "
    "&bull; <b>MBA, Financial Mathematics, Florida International University</b> &mdash; 2011 &bull; "
    "<b>B.Sc., Banking &amp; Finance, London School of Economics</b> &mdash; 2005 &bull; "
    "<b>Columbia Engineering FinTech Boot Camp</b> &mdash; 2021<br/>"
    "<b>Certifications:</b> FDIC Bank Examiner I &bull; Registered Scrum Master &bull; GCP Social/Behavioral Human "
    "Research. <i>In progress:</i> CIA Part 1, IAPP AIGP.", body))

doc = SimpleDocTemplate(str(OUT), pagesize=LETTER,
                        leftMargin=0.55 * inch, rightMargin=0.55 * inch,
                        topMargin=0.36 * inch, bottomMargin=0.36 * inch,
                        title="Yasir A. Malik - Resume - Internal Audit Regulatory Relations VP, Goldman Sachs",
                        author="Yasir A. Malik", subject="Regulatory Relations & Internal Audit")
doc.build(flow)
print(f"built {OUT} at S={S} | header: {header_mode()}")
