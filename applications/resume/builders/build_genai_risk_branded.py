"""GenAI-risk master resume in the Audit the Algorithm brand.

Same design system as build_branded_resume.py: the wordmark is drawn as real
text in the brand gold (#B8860B) with the muted "the" (#6F6754), Times faces,
hairline section rules. That keeps the file small enough to attach anywhere
and lets an ATS read the brand instead of skipping an opaque image.

Content is the GenAI-risk positioning from builders/genai-risk-master.html,
including the three-row "Where the Research Is Going" table, rendered here as
a reportlab Table so the text layer carries every cell.

Run from repo root:
    python3 applications/resume/builders/build_genai_risk_branded.py

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
OUT = ROOT / "applications" / "resume" / "Yasir_Malik_Resume_GenAI_Risk_Master_Branded.pdf"

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
    f'<font color="#B8860B"><b>Audit</b></font> '
    f'<font color="#6F6754"><i>the</i></font> '
    f'<font color="#B8860B"><b>Algorithm</b></font>', mark))
flow.append(Paragraph("YASIR A. MALIK", name))
flow.append(Paragraph("GenAI Risk &amp; Assurance Executive &mdash; Internal Audit &bull; Model Risk (SR 11-7) "
                      "&bull; Responsible AI Governance | Doctoral Researcher in AI-Assisted Judgment", tag))
flow.append(Paragraph("Newark, NJ &bull; YasirAMalik@gmail.com &bull; +1 (786) 704-8536 &bull; "
                      "linkedin.com/in/yasiramalik &bull; github.com/MalikAI-786 &bull; auditingai.github.io",
                      contact))

# ---- Summary -----------------------------------------------------------------
flow += section("EXECUTIVE SUMMARY")
flow.append(Paragraph(
    "Audit and risk executive with 20 years across Citi, JPMorgan Chase, and the Florida Office of Financial "
    "Regulation, now focused on the risks generative AI introduces that legacy control frameworks do not see: "
    "sycophancy and judgment drift in AI-assisted decisions, automation bias, hallucination, adversarial input, "
    "and unmanaged third-party AI. A builder-auditor &mdash; authored an AI governance framework referencing NIST "
    "AI RMF and SR 11-7, and shipped the RAG assistant it governs (~35% faster audit review). Led consent-order "
    "remediation accepted by federal regulators, CCAR forecast validation over a $2.6T balance sheet, and "
    "Resolution &amp; Recovery Planning that earned the Federal Reserve&rsquo;s &ldquo;not not-credible&rdquo; "
    "rating. DBA candidate at FIU (GPA 3.81, expected 2028) whose research measures how expert judgment degrades "
    "under AI assistance &mdash; the human-factors half of AI risk that model validation alone cannot cover.",
    body))

# ---- Research trajectory table ----------------------------------------------
flow += section("WHERE THE RESEARCH IS GOING")
rows = [
    [Paragraph("Stage", cellh), Paragraph("Work", cellh), Paragraph("Why it matters to an employer", cellh)],
    [Paragraph("Completed &middot; Jul 2026", cell),
     Paragraph("Empirical study of anchoring bias in long-term auditor engagements (IRB-25-0462, FIU)", cell),
     Paragraph("Evidence on how expert judgment drifts under a persistent reference point &mdash; the same "
               "mechanism an AI recommendation creates.", cell)],
    [Paragraph("In development", cell),
     Paragraph("Dissertation: automation bias and judgment drift when auditors work with LLM assistants; "
               "controls aligned to SR 11-7 and NIST AI RMF", cell),
     Paragraph("Turns &ldquo;human in the loop&rdquo; from a slogan into a measurable control with a test "
               "procedure.", cell)],
    [Paragraph("Planned", cell),
     Paragraph("Audit Judgment Drift benchmark; three-layer LLM audit model (governance / model / application) "
               "for bank supervision; open-source AI Audit Playbook", cell),
     Paragraph("Reusable test assets a second line or Internal Audit can adopt directly, in regulator-legible "
               "vocabulary.", cell)],
]
usable = LETTER[0] - 1.1 * inch
table = Table(rows, colWidths=[usable * 0.17, usable * 0.43, usable * 0.40])
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
    "GenAI &amp; AI Risk Identification (sycophancy, judgment drift, automation bias, hallucination, prompt "
    "injection, model drift, third-party AI) | AI Governance &amp; Responsible AI (NIST AI RMF, EU AI Act, ISO/IEC "
    "42001) | Model Risk Management (SR 11-7) | Internal Audit &amp; Controls (Global Internal Audit Standards, "
    "3LOD, COSO) | Consent-Order Remediation &amp; Issue Closure | Regulatory Examination &amp; Supervisory "
    "Engagement | CCAR / SR 15-18 &bull; Basel III RWA &bull; Resolution &amp; Recovery Planning | Applied AI Build "
    "(RAG, LangChain, evaluation scripts, XAI &mdash; SHAP/LIME) | Executive &amp; Audit Committee Reporting", body))

# ---- Experience ----------------------------------------------------------------
flow += section("PROFESSIONAL EXPERIENCE")
flow.append(job("Vice President, Audit Manager &mdash; Citi", "Jul 2021 &ndash; Apr 2026"))
flow.append(Paragraph("Cross-Enterprise Program &amp; Change Management, Internal Audit | New York, NY", sub))
for b in [
    "Built independent assurance over enterprise AI/GenAI adoption &mdash; governance, model risk, bias and "
    "fairness, hallucination, adversarial robustness, and third-party AI &mdash; and defined the AI tooling roadmap "
    "for Internal Audit: use-case intake, risk tiering, control library, and post-deployment monitoring KPIs.",
    "Designed and shipped a RAG-based Workpaper Quality Assistant (Python, LangChain, SHAP/LIME explainability, "
    "prompt-injection guardrails) that cut audit cycle time ~35% &mdash; built so the AI tool was itself auditable.",
    "Led consent-order audit execution across 15+ business units; authored issue-closure packages and "
    "sustainable-closure evidence accepted by quality assurance and external regulators.",
    "Delivered executive and Board Audit Committee risk reporting; mentored 8+ auditors on responsible AI "
    "adoption and bias awareness. Citi <i>Delivers with Pride</i> recognition.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Risk Control Manager, Treasury &amp; CIO &mdash; JPMorgan Chase", "Mar 2019 &ndash; Jun 2021"))
flow.append(Paragraph("Capital Controls &amp; Resolution and Recovery Planning | Jersey City, NJ", sub))
for b in [
    "Led CCAR forecast validation and qualitative model challenge over a $2.6T balance sheet under SR 15-18; "
    "automated reconciliations cut manual review ~40%.",
    "Directed Resolution &amp; Recovery Planning across 50+ stakeholders in Legal, Treasury, and Operations, "
    "delivering regulator-ready submissions to the Federal Reserve and FDIC.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Capital Controller, Basel Measurement &amp; Analytics &mdash; JPMorgan Chase",
                "Sep 2017 &ndash; Feb 2019"))
flow.append(Paragraph("Brooklyn, NY (preceded by Program Manager, CIB Resolution &amp; Recovery Planning, "
                      "2015&ndash;2017)", sub))
flow.append(Paragraph("Owned Basel III RWA and capital adequacy reporting for a $50B book; identified $180M in "
                      "capital optimization for CFO decision support.", bullet, bulletText="•"))

flow.append(job("Bank Examiner, Bureau of Bank Regulation &mdash; Florida Office of Financial Regulation",
                "Apr 2011 &ndash; Mar 2012"))
flow.append(Paragraph("West Palm Beach, FL", sub))
flow.append(Paragraph("Conducted CAMELS safety-and-soundness examinations of state and national banks alongside "
                      "federal banking regulators; authored workpapers supporting formal enforcement actions.",
                      bullet, bulletText="•"))

# ---- Earlier -------------------------------------------------------------------
flow += section("EARLIER EXPERIENCE")
flow.append(Paragraph(
    "<b>Assistant Vice President, Global Legal Entity Management &mdash; Citi,</b> Tampa, FL (2012&ndash;2015): "
    "Centralized 500+ legal-entity data sources into governed master data, enabling automated FR 2900 and TIC "
    "regulatory filings at 99.8% accuracy. Earlier: Senior Business Analyst, Retail Credit Risk &mdash; Royal Bank "
    "of Scotland, Dubai (2008&ndash;2009).", body))

# ---- Education -------------------------------------------------------------------
flow += section("EDUCATION")
flow.append(Paragraph(
    "<b>Doctor of Business Administration (DBA), Florida International University</b> &mdash; Expected 2028 | "
    "GPA 3.81 &mdash; research above.<br/>"
    "<b>Master of Business Administration (MBA), Florida International University</b> &mdash; 2011 | GPA 3.8 &bull; "
    "<b>B.Sc., Banking &amp; Finance, London School of Economics</b> &mdash; 2005 &bull; "
    "<b>Columbia Engineering FinTech Boot Camp</b> &mdash; 2021", body))

# ---- Advisory, certs, technical ----------------------------------------------------
flow += section("ADVISORY, CERTIFICATIONS &amp; TECHNICAL SKILLS")
flow.append(Paragraph(
    "<b>Founder, Audit the Algorithm</b> (auditingai.github.io, 2024&ndash;): AI governance advisory for regulated "
    "financial services &mdash; bias and drift testing, regulator-defensible control frameworks, human&ndash;AI "
    "workflow design.<br/>"
    "<b>Certifications:</b> FDIC Bank Examiner I &bull; Registered Scrum Master &bull; GCP Social/Behavioral Human "
    "Research (AI Ethics). <i>In progress:</i> CIA Part 1, IAPP AIGP.<br/>"
    "<b>Technical:</b> Python &bull; LangChain / LangGraph &bull; RAG and agentic RAG &bull; vector databases &bull; "
    "prompt engineering &bull; evaluation and red-teaming scripts &bull; SHAP / LIME &bull; SQL &bull; Alteryx &bull; "
    "Tableau &bull; Excel/VBA &bull; GitHub Actions.", body))

doc = SimpleDocTemplate(str(OUT), pagesize=LETTER,
                        leftMargin=0.55 * inch, rightMargin=0.55 * inch,
                        topMargin=0.36 * inch, bottomMargin=0.36 * inch,
                        title="Yasir A. Malik - Resume", author="Yasir A. Malik",
                        subject="GenAI Risk & Assurance Executive")
doc.build(flow)
print(f"built {OUT}")
