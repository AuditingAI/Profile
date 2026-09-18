"""The broad master resume in the Audit the Algorithm brand.

The one to send when no tailored variant fits: internal audit, first-line risk
and controls, capital and financial control, data governance, and AI governance
on one page, under the wordmark. Same design system as build_branded_resume.py
and build_genai_risk_branded.py - Times faces, hairline rules, the wordmark as
real text so an ATS reads it and the file stays small.

Deliberately broad. The tailored variants narrow the story for one reader;
this one keeps every lane open so a recruiter scanning for any of them finds it.

Run from repo root:
    python3 applications/resume/builders/build_master_branded.py

Standing rules: never "OCC"; examiner history is the Florida Office of
Financial Regulation; DBA in progress (expected 2028); CIA in progress; never a
career-length number - the dates on the entries speak.
"""
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brand import brand_block  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "applications" / "resume" / "Yasir_Malik_Resume_Master_Branded.pdf"

GOLD = HexColor("#B8860B")
MUTED = HexColor("#6F6754")

S = float(sys.argv[1]) if len(sys.argv) > 1 else 0.86  # global scale

body = ParagraphStyle("body", fontName="Times-Roman", fontSize=8.9 * S,
                      leading=11.0 * S, alignment=TA_JUSTIFY, spaceAfter=2.0 * S)
mark = ParagraphStyle("mark", parent=body, alignment=TA_CENTER, fontSize=15 * S,
                      leading=17 * S, spaceAfter=1)
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
flow += brand_block(mark)
flow.append(Paragraph("YASIR A. MALIK", name))
flow.append(Paragraph(
    "Internal Audit &bull; Risk &amp; Controls &bull; Capital &amp; Financial Control &bull; Data Governance "
    "&bull; AI Governance | Former Bank Examiner | Doctoral Researcher in AI-Assisted Judgment", tag))
flow.append(Paragraph("Newark, NJ &bull; YasirAMalik@gmail.com &bull; +1 (786) 704-8536 &bull; "
                      "linkedin.com/in/yasiramalik &bull; github.com/MalikAI-786 &bull; auditingai.github.io",
                      contact))

# ---- Summary -----------------------------------------------------------------
flow += section("SUMMARY")
flow.append(Paragraph(
    "Audit and risk executive across Citi, JPMorgan Chase, and the Florida Office of Financial Regulation who has "
    "held every seat around a control: the examiner who tested it, the first-line manager who built and ran it, "
    "and the auditor who opined on it. At JPMorgan, owned the control framework for Treasury &amp; CIO capital "
    "activities, led CCAR validation over a $2.6T balance sheet, and ran Resolution &amp; Recovery Planning into "
    "Federal Reserve and FDIC submissions. At Citi, led risk-based audits across 15+ business units with "
    "consent-order closure evidence accepted by external regulators. Builds the tooling as well as the framework: "
    "a production RAG workpaper assistant (~35% faster review), automated reconciliations (~40% less manual "
    "review), 500+ legal-entity data sources into governed master data at 99.8% filing accuracy. Authored an AI "
    "governance framework referencing NIST AI RMF and SR 11-7. DBA candidate at FIU (expected 2028, GPA 3.81) "
    "researching how expert judgment degrades under AI assistance.", body))

# ---- Selected results --------------------------------------------------------
flow += section("SELECTED RESULTS")
rows = [
    [Paragraph("Result", cellh), Paragraph("What it was", cellh), Paragraph("Where", cellh)],
    [Paragraph("$2.6T", cell),
     Paragraph("CCAR forecast validation and qualitative model challenge under SR 15-18, with Finance, Treasury, "
               "and Model Risk", cell), Paragraph("JPMorgan Chase", cell)],
    [Paragraph("$180M", cell),
     Paragraph("Capital optimization identified for CFO decision support from Basel III RWA reporting on a $50B "
               "book", cell), Paragraph("JPMorgan Chase", cell)],
    [Paragraph("99.8%", cell),
     Paragraph("Filing accuracy on automated FR 2900 and TIC regulatory reporting after consolidating 500+ "
               "legal-entity data sources into governed master data", cell), Paragraph("Citi", cell)],
    [Paragraph("~40% less", cell),
     Paragraph("Manual review on capital and liquidity reconciliations, by automating them and removing a "
               "recurring source of reporting error", cell), Paragraph("JPMorgan Chase", cell)],
    [Paragraph("~35% faster", cell),
     Paragraph("Audit review cycle time from a RAG workpaper assistant built in Python and LangChain &mdash; "
               "designed so the tool was itself auditable", cell), Paragraph("Citi", cell)],
]
usable = LETTER[0] - 1.1 * inch
table = Table(rows, colWidths=[usable * 0.13, usable * 0.69, usable * 0.18])
table.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    ("LINEBELOW", (0, 0), (-1, 0), 0.9, GOLD),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 1.3), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.3),
]))
flow.append(table)

# ---- Competencies --------------------------------------------------------------
flow += section("CORE COMPETENCIES")
flow.append(Paragraph(
    "Internal Audit &amp; Controls (IIA Standards, COSO, Three Lines of Defense, SOX ITGC) | First-Line Risk &amp; "
    "Control Frameworks | Regulatory Examination &amp; Remediation (consent orders, Federal Reserve, FDIC, state "
    "supervision) | Capital &amp; Liquidity (CCAR / SR 15-18, Basel III RWA, Resolution &amp; Recovery Planning) | "
    "Financial &amp; Regulatory Reporting Control (FR 2900, TIC, legal entity) | Data Governance &amp; Data Quality | "
    "AI Governance &amp; Model Risk (NIST AI RMF, SR 11-7, EU AI Act, ISO/IEC 42001) | Audit Analytics &amp; "
    "Automation (Python, SQL, LangChain / RAG, Alteryx, Tableau) | Executive &amp; Board Audit Committee Reporting",
    body))

# ---- Experience ----------------------------------------------------------------
flow += section("PROFESSIONAL EXPERIENCE")
flow.append(job("Vice President, Audit Manager &mdash; Citi", "Jul 2021 &ndash; Apr 2026"))
flow.append(Paragraph("Internal Audit, Cross-Enterprise Program &amp; Change Management | New York, NY", sub))
for b in [
    "Led risk-based audits end to end across 15+ business units &mdash; control design and operating "
    "effectiveness across business, finance, and technology risk; opinions on the control environment; "
    "escalation where remediation was not credible.",
    "Drove consent-order remediation: issue-closure packages and sustainable-closure evidence accepted by "
    "quality assurance and by external regulators.",
    "Built independent assurance over enterprise AI adoption &mdash; governance, model risk, bias, hallucination, "
    "third-party AI &mdash; and designed and shipped a RAG-based Workpaper Quality Assistant (Python, LangChain, "
    "SHAP/LIME) that cut review cycle time ~35%.",
    "Delivered executive and Board Audit Committee reporting; coached 8+ auditors. Citi <i>Delivers with Pride</i> "
    "recognition.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Risk Control Manager, Treasury &amp; CIO &mdash; JPMorgan Chase", "Mar 2019 &ndash; Jun 2021"))
flow.append(Paragraph("First-Line Capital Controls &amp; Resolution and Recovery Planning | Jersey City, NJ", sub))
for b in [
    "Owned the first-line control framework for Treasury &amp; CIO capital activities; automated capital and "
    "liquidity reconciliations, cutting manual review ~40%.",
    "Led CCAR forecast validation and qualitative model challenge over a $2.6T balance sheet under SR 15-18.",
    "Ran Resolution &amp; Recovery Planning across 50+ stakeholders in Legal, Treasury, and Operations, delivering "
    "to the Federal Reserve and FDIC against statutory deadlines.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Capital Controller, Basel Measurement &amp; Analytics &mdash; JPMorgan Chase",
                "Sep 2017 &ndash; Feb 2019"))
flow.append(Paragraph("Brooklyn, NY &bull; preceded by Program Manager, CIB Resolution &amp; Recovery Planning "
                      "(2015&ndash;2017)", sub))
flow.append(Paragraph("Owned Basel III RWA and capital adequacy reporting for a $50B book of equities, fixed income, "
                      "and OTC derivatives; identified $180M in capital optimization for CFO decision support.",
                      bullet, bulletText="•"))

flow.append(job("Assistant Vice President, Global Legal Entity Management &mdash; Citi", "2012 &ndash; 2015"))
flow.append(Paragraph("Tampa, FL", sub))
flow.append(Paragraph("Consolidated 500+ legal-entity data sources into governed master data, enabling automated "
                      "FR 2900 and TIC regulatory filings at 99.8% accuracy.", bullet, bulletText="•"))

flow.append(job("Bank Examiner, Bureau of Bank Regulation &mdash; Florida Office of Financial Regulation",
                "Apr 2011 &ndash; Mar 2012"))
flow.append(Paragraph("West Palm Beach, FL &bull; earlier: Senior Business Analyst, Retail Credit Risk &mdash; Royal "
                      "Bank of Scotland, Dubai (2008&ndash;2009), credit-risk MIS over a $500M+ portfolio in SAS "
                      "and SQL", sub))
flow.append(Paragraph("Conducted CAMELS safety-and-soundness examinations of state and national banks alongside "
                      "federal banking regulators; authored workpapers supporting formal enforcement actions.",
                      bullet, bulletText="•"))

# ---- Education -------------------------------------------------------------------
flow += section("EDUCATION")
flow.append(Paragraph(
    "<b>Doctor of Business Administration (DBA), Florida International University</b> &mdash; in progress, expected "
    "2028 | GPA 3.81. Qualifying research completed Jul 2026 (IRB-25-0462): a designed experiment on anchoring "
    "in auditor judgment, analysed in SPSS. Dissertation in development: automation bias in AI-assisted judgment.<br/>"
    "<b>MBA, Financial Mathematics, Florida International University</b> &mdash; 2011 | GPA 3.8 &bull; "
    "<b>B.Sc., Banking &amp; Finance, London School of Economics</b> &mdash; 2005 &bull; "
    "<b>Columbia Engineering FinTech Boot Camp</b> &mdash; 2021", body))

# ---- Advisory, certs, technical ----------------------------------------------------
flow += section("ADVISORY, CERTIFICATIONS &amp; TECHNICAL SKILLS")
flow.append(Paragraph(
    "<b>Founder, Audit the Algorithm</b> (auditingai.github.io, 2024&ndash;): AI governance advisory for regulated "
    "financial services.<br/>"
    "<b>Certifications:</b> FDIC Bank Examiner I &bull; Registered Scrum Master &bull; GCP Social/Behavioral Human "
    "Research. <i>In progress:</i> CIA Part 1, IAPP AIGP.<br/>"
    "<b>Technical:</b> Python &bull; SQL &bull; SAS &bull; SPSS &bull; LangChain / RAG &bull; scikit-learn &bull; "
    "SHAP / LIME &bull; Alteryx &bull; Tableau &bull; Power BI &bull; Excel/VBA &bull; GitHub Actions.", body))

doc = SimpleDocTemplate(str(OUT), pagesize=LETTER,
                        leftMargin=0.55 * inch, rightMargin=0.55 * inch,
                        topMargin=0.36 * inch, bottomMargin=0.36 * inch,
                        title="Yasir A. Malik - Resume", author="Yasir A. Malik",
                        subject="Internal Audit, Risk & Controls, AI Governance")
doc.build(flow)
print(f"built {OUT} at S={S}")
