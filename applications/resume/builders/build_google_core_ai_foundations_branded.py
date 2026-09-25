"""Google - Vice President, Product Management, Core AI Foundations.

Built at the owner's explicit request, 19 Sep 2026, with the gap stated rather
than papered over. The posting's stated minimum is "20 years of experience in
the full scope of product management" plus a Bachelor's in Computer Science.
He has never held a product-manager title and his degree is Banking & Finance.
Those facts are not arguable and the cover letter opens with them.

What the record DOES support is the half of a foundation-model product
organisation that is about trust: whether a model can be deployed into a
regulated market and defended afterwards. He authored an AI governance
framework at Citi against NIST AI RMF and SR 11-7, defined the AI tooling
roadmap for Internal Audit (use-case intake, risk tiering, control library,
post-deployment monitoring KPIs), and then built and shipped the retrieval
system that roadmap governed - requirements elicited from users, written in
Python and LangChain, iterated to production. Builder and governor in one
person is rare, and it is the spine of this resume.

The doctoral research is load-bearing here rather than decorative: automation
bias and judgment drift under AI assistance is a foundation-model product
problem (sycophancy, over-reliance, degraded human oversight), not an academic
footnote.

Branded through builders/brand.py, per the owner's standing choice - Google is
the one employer where the Audit the Algorithm mark reads as an asset rather
than an outside-business-activity question.

Run from repo root:
    python3 applications/resume/builders/build_google_core_ai_foundations_branded.py [scale]

Standing rules: never "OCC"; examiner history is the Florida Office of
Financial Regulation; DBA in progress; CIA in progress; never a
career-length number. Never claim a product-manager title, a CS degree, or
experience running a PM organisation.
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
OUT = ROOT / "applications" / "resume" / "Yasir_Malik_Resume_Google_CoreAIFoundations_VP_Branded.pdf"
S = float(sys.argv[1]) if len(sys.argv) > 1 else 0.82

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
flow.append(Paragraph("AI Governance &amp; Model Risk | Responsible AI at Enterprise Scale | Ships the Systems "
                      "as Well as the Policy | Doctoral Researcher in Human&ndash;AI Judgment", tag))
flow.append(Paragraph("Newark, NJ &bull; Preferred working location: New York, NY &bull; YasirAMalik@gmail.com "
                      "&bull; +1 (786) 704-8536 &bull; linkedin.com/in/yasiramalik &bull; github.com/MalikAI-786",
                      contact))

# ---- Summary -----------------------------------------------------------------
flow += section("SUMMARY")
flow.append(Paragraph(
    "Works on the half of an AI platform that decides whether a model can be deployed into a regulated market "
    "and defended afterwards. Authored an <b>AI governance framework</b> at Citi referencing <b>NIST AI RMF</b> "
    "and <b>SR 11-7</b> &mdash; use-case intake, risk tiering, control library, explainability and "
    "human-in-the-loop requirements, post-deployment monitoring KPIs &mdash; and defined the AI tooling roadmap "
    "it governed. Then built what it governed: requirements elicited from the teams who needed it, a "
    "retrieval-augmented assistant written in <b>Python and LangChain</b> with vector search, SHAP/LIME "
    "explainability and prompt-injection guardrails, iterated to production &mdash; <b>~35%</b> faster review "
    "cycles. The career before AI was capital and regulatory: <b>CCAR</b> validation over a <b>$2.6T</b> balance "
    "sheet, Basel III RWA analysis surfacing <b>$180M</b> in capital optimisation, and Resolution &amp; Recovery "
    "Planning across <b>50+ stakeholders</b> into Federal Reserve and FDIC submissions. A former bank examiner, "
    "so the regulator's read on a launch decision is a learned instinct. <b>DBA candidate at FIU</b> researching "
    "automation bias in AI-assisted judgment &mdash; the over-reliance problem, measured rather than asserted.", body))

# ---- What the role needs, against the record ---------------------------------
flow += section("WHAT A FOUNDATION-MODEL PRODUCT ORGANISATION NEEDS, AGAINST THE RECORD")
rows = [
    [Paragraph("What the work requires", cellh), Paragraph("Where it has been done", cellh)],
    [Paragraph("Product roadmap ownership and prioritisation", cell),
     Paragraph("Defined the <b>AI tooling roadmap</b> for Citi Internal Audit: use-case intake, risk tiering by "
               "criticality, control library, and post-deployment monitoring KPIs &mdash; what gets built, in "
               "what order, and what has to be true before it ships.", cell)],
    [Paragraph("Requirements to shipped product, with users in the loop", cell),
     Paragraph("RAG Workpaper Quality Assistant: requirements elicited from the auditors who needed it, written "
               "in Python and LangChain with vector search, SHAP/LIME explainability and prompt-injection "
               "guardrails, integrated with Alteryx, iterated on feedback, and put into production. <b>~35%</b> "
               "faster review cycle.", cell)],
    [Paragraph("Launch gating, evaluation and model risk", cell),
     Paragraph("Independent assurance over enterprise AI adoption &mdash; governance, model risk, bias and "
               "fairness, hallucination, adversarial robustness, third-party AI; SR 11-7; SHAP/LIME; evaluation "
               "and red-teaming scripts. Consent-order remediation with evidence accepted by external "
               "regulators: pre-launch review under the least forgiving reviewer there is.", cell)],
    [Paragraph("Deploying into regulated markets &mdash; EU AI Act and after", cell),
     Paragraph("NIST AI RMF, EU AI Act, ISO/IEC 42001. Former <b>bank examiner</b> (Florida Office of Financial "
               "Regulation), CAMELS examinations alongside federal banking regulators &mdash; the supervisory "
               "view of a product decision, from inside the supervisor.", cell)],
    [Paragraph("The human side of model quality", cell),
     Paragraph("DBA research at FIU on <b>automation bias in AI-assisted judgment</b>: how expert judgment "
               "degrades when a model is confidently wrong. Qualifying study completed Jul 2026 (IRB-25-0462), "
               "a 55-item instrument designed and fielded under IRB approval. The sycophancy and over-reliance problem, measured.", cell)],
]
t = Table(rows, colWidths=[usable * 0.30, usable * 0.70])
t.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (-1, -1), "Times-Roman"),
    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#000000")),
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F2EFE6")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 3),
    ("RIGHTPADDING", (0, 0), (-1, -1), 3),
    ("TOPPADDING", (0, 0), (-1, -1), 1.5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
]))
flow.append(t)

# ---- Technical ---------------------------------------------------------------
flow += section("TECHNICAL")
flow.append(Paragraph(
    "<b>Build:</b> Python &bull; LangChain / LangGraph &bull; retrieval-augmented generation and agentic RAG "
    "&bull; vector databases (Pinecone, ChromaDB) &bull; Hugging Face &bull; scikit-learn &bull; SHAP / LIME "
    "&bull; evaluation and red-teaming scripts &bull; prompt engineering and injection guardrails &bull; SQL "
    "&bull; GitHub Actions<br/>"
    "<b>Govern:</b> NIST AI RMF &bull; EU AI Act &bull; ISO/IEC 42001 &bull; SR 11-7 model risk &bull; "
    "Global Internal Audit Standards &bull; COSO &bull; Three Lines of Defense<br/>"
    "<b>Analyse:</b> SPSS (experiment design and statistical testing) &bull; SAS &bull; Alteryx &bull; Tableau "
    "&bull; Power BI &bull; Excel/VBA. <b>Delivery:</b> Registered Scrum Master.", body))

# ---- Experience --------------------------------------------------------------
flow += section("PROFESSIONAL EXPERIENCE")
flow.append(job("Vice President, Audit Manager &mdash; Citi", "Jul 2021 &ndash; Apr 2026"))
flow.append(Paragraph("Internal Audit, Cross-Enterprise Program &amp; Change Management | New York, NY", sub))
for b in [
    "<b>Authored the AI governance framework</b> referencing NIST AI RMF and SR 11-7, and defined the AI tooling "
    "roadmap it governed &mdash; use-case intake, risk tiering, control library, explainability and "
    "human-in-the-loop requirements, post-deployment monitoring KPIs.",
    "<b>Designed and shipped the RAG Workpaper Quality Assistant</b> &mdash; Python, LangChain, vector search "
    "over unstructured workpapers, SHAP/LIME explainability, prompt-injection guardrails, Alteryx integration. "
    "Specified with its users, iterated on their feedback, put into production: <b>~35%</b> less review cycle "
    "time, and continuous coverage where sampling had been the only option.",
    "Built independent assurance over enterprise AI adoption across governance, model risk, bias and fairness, "
    "hallucination, adversarial robustness, and third-party AI; led risk-based audits across <b>15+ business "
    "units</b>; drove consent-order remediation with evidence accepted by external regulators. Executive and "
    "Board Audit Committee reporting; coached <b>8+ auditors</b>.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Risk Control Manager, Treasury &amp; CIO &mdash; JPMorgan Chase", "Mar 2019 &ndash; Jun 2021"))
flow.append(Paragraph("First-Line Capital Controls &amp; Resolution and Recovery Planning | Jersey City, NJ", sub))
for b in [
    "Owned the first-line control framework for Treasury and CIO capital activities; <b>automated capital and "
    "liquidity reconciliations</b>, cutting manual review <b>~40%</b> and removing a recurring source of "
    "reporting error. Led <b>CCAR</b> forecast validation and quantitative model challenge over a <b>$2.6T</b> "
    "balance sheet under SR 15-18.",
    "Ran <b>Resolution &amp; Recovery Planning</b> across <b>50+ stakeholders</b> in five functions &mdash; none "
    "reporting to him &mdash; into Federal Reserve and FDIC submissions against statutory deadlines.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Capital Controller, Basel Measurement &amp; Analytics &mdash; JPMorgan Chase",
                "Sep 2017 &ndash; Feb 2019"))
flow.append(Paragraph("Brooklyn, NY &bull; preceded by Program Manager, CIB Resolution &amp; Recovery Planning "
                      "(2015&ndash;2017)", sub))
flow.append(Paragraph(
    "Owned Basel III RWA and capital adequacy reporting across a <b>$50B</b> book of equities, fixed income and "
    "OTC derivatives; analysis of RWA treatment surfaced <b>$180M</b> in capital optimisation for CFO decision "
    "support.", bullet, bulletText="•"))

flow.append(job("Assistant Vice President, Global Legal Entity Management &mdash; Citi", "2012 &ndash; 2015"))
flow.append(Paragraph("Tampa, FL", sub))
flow.append(Paragraph(
    "Consolidated <b>500+ legal-entity data sources</b> into governed master data with ownership, lineage and "
    "data-quality controls &mdash; enabling automated <b>FR 2900</b> and <b>TIC</b> filings at <b>99.8% "
    "accuracy</b> under regulatory examination.", bullet, bulletText="•"))

flow.append(job("Bank Examiner, Bureau of Bank Regulation &mdash; Florida Office of Financial Regulation",
                "Apr 2011 &ndash; Mar 2012"))
flow.append(Paragraph("West Palm Beach, FL &bull; earlier: Senior Business Analyst, Retail Credit Risk &mdash; "
                      "Royal Bank of Scotland, Dubai (2008&ndash;2009)", sub))
flow.append(Paragraph(
    "Conducted CAMELS safety-and-soundness examinations of state and national banks alongside federal banking "
    "regulators; authored workpapers supporting formal enforcement actions.", bullet, bulletText="•"))

# ---- Education + advisory ----------------------------------------------------
flow += section("EDUCATION, RESEARCH &amp; ADVISORY")
flow.append(Paragraph(
    "<b>Doctor of Business Administration (DBA), Florida International University</b> &mdash; in progress. "
    "Qualifying examination passed Jul 2026 (IRB-25-0462): a 55-item instrument on anchoring in audit "
    "judgment, designed and fielded under institutional ethics approval. "
    "Dissertation in development: <i>Anchoring Bias in LLM-Assisted Audit Judgment</i>.<br/>"
    "<b>MBA, Financial Mathematics, Florida International University</b> &mdash; 2011 | GPA 3.8 &bull; "
    "<b>B.Sc., Banking &amp; Finance, London School of Economics</b> &mdash; 2005 &bull; "
    "<b>Columbia Engineering FinTech Boot Camp</b> &mdash; 2021<br/>"
    "<b>Founder, Audit the Algorithm</b> (auditingai.github.io, 2024&ndash;): AI governance advisory for "
    "regulated financial services. <b>Certifications:</b> FDIC Bank Examiner I &bull; Registered Scrum Master "
    "&bull; GCP Social/Behavioral Human Research. <i>In progress:</i> CIA Part 1, IAPP AIGP.", body))

doc = SimpleDocTemplate(str(OUT), pagesize=LETTER,
                        leftMargin=0.55 * inch, rightMargin=0.55 * inch,
                        topMargin=0.36 * inch, bottomMargin=0.36 * inch,
                        title="Yasir A. Malik - Resume", author="Yasir A. Malik",
                        subject="AI Governance, Model Risk, Responsible AI")
doc.build(flow)
print(f"built {OUT} at S={S} | header: {header_mode()}")
