"""Goldman Sachs - HCM Strategy, Data Program Product Management, Vice President.

Built at the owner's explicit request (18 Sep 2026) after the fit was argued
against. The record does not meet the central basic qualification - "minimum of
7+ years of progressive experience in product management" - and there is no
Snowflake, no Oracle HCM Cloud, and no HR domain anywhere on it. Those are named
in the cover letter rather than papered over, because the alternative is a
document that misleads a screener.

What the record DOES support is the half of the posting that is about data
products rather than product management: end-to-end lineage ownership, data
quality and certification, ETL and master data at scale, and governance that had
to survive a regulator. The Citi Global Legal Entity Management programme is a
data product by any working definition - 500+ sources consolidated into governed
master data with ownership and lineage, serving downstream consumers (FR 2900
and TIC regulatory filings) at 99.8% accuracy, where the cost of bad data was a
misfiled return. That is the spine of this resume.

Registered Scrum Master is surfaced prominently: the posting names "Agile
Product Owner/Scrum Master, or other relevant product management certifications"
as highly desirable, and it is the one credential on the list he holds.

Branded through builders/brand.py, per the owner's standing choice.

Run from repo root:
    python3 applications/resume/builders/build_gs_hcm_data_product_branded.py [scale]

Standing rules: never "OCC"; examiner history is the Florida Office of
Financial Regulation; DBA in progress; CIA in progress; never a
career-length number. Never claim Snowflake, Oracle HCM, data mesh, or Jira.
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
OUT = ROOT / "applications" / "resume" / "Yasir_Malik_Resume_GS_HCM_DataProduct_VP_Branded.pdf"
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
flow.append(Paragraph("Data Products &amp; Governance | End-to-End Lineage &bull; Data Quality &amp; Certification "
                      "&bull; ETL and Master Data at Scale | Built for Regulatory Scrutiny", tag))
flow.append(Paragraph("Newark, NJ &bull; YasirAMalik@gmail.com &bull; +1 (786) 704-8536 &bull; "
                      "linkedin.com/in/yasiramalik &bull; github.com/MalikAI-786", contact))

# ---- Summary -----------------------------------------------------------------
flow += section("SUMMARY")
flow.append(Paragraph(
    "Builds and governs data products where the cost of bad data is a misfiled regulatory return. At Citi, "
    "consolidated <b>500+ legal-entity data sources</b> into governed master data &mdash; data modeling, ETL, "
    "ownership and <b>end-to-end lineage</b>, and the data-quality controls that made the output certifiable "
    "&mdash; serving downstream <b>FR 2900</b> and <b>TIC</b> regulatory filings at <b>99.8% accuracy</b>. Ships "
    "as well as governs: elicited requirements from the teams who needed it, wrote the code, and put a "
    "retrieval-augmented assistant into production (Python, LangChain) that cut review cycle time <b>~35%</b>; "
    "automated capital and liquidity reconciliations for <b>~40%</b> less manual review. Quantifies the case "
    "before building it &mdash; analysis of Basel III RWA treatment on a $50B book surfaced <b>$180M</b> in "
    "capital optimisation for CFO decision support. Partners across Data, Engineering, Legal, Treasury, and "
    "Operations at scale (50+ stakeholders on a single regulatory programme) and reports outcomes to executive "
    "management and the Board Audit Committee. <b>Registered Scrum Master.</b> MBA in Financial Mathematics; DBA "
    "candidate at FIU.", body))

# ---- Mapping ---------------------------------------------------------------------
flow += section("THE DATA-PRODUCT REQUIREMENTS, AGAINST THE RECORD")
rows = [
    [Paragraph("The posting asks for", cellh), Paragraph("Where it has been done", cellh)],
    [Paragraph("<b>Ownership and ongoing maintenance of end-to-end data lineage for data products</b>", cell),
     Paragraph("Citi Global Legal Entity Management: owned 500+ consolidated sources with defined ownership, "
               "lineage, and access control through to the downstream consumers &mdash; and kept it running, not "
               "just delivered.", cell)],
    [Paragraph("Data architecture: data structures, data modeling, ETL/ELT pipelines, warehousing, semantic layers", cell),
     Paragraph("Data modeling and ETL across the GLEM consolidation; automated capital and liquidity "
               "reconciliation pipelines at JPMorgan; reporting and semantic layers delivered in Tableau and "
               "Power BI for downstream analytics consumers.", cell)],
    [Paragraph("Governance, data privacy, and regulatory compliance across all products", cell),
     Paragraph("The whole career. Data-quality certification under regulatory examination; consent-order issue "
               "closure with evidence accepted by external regulators; an AI governance framework referencing "
               "NIST AI RMF and SR 11-7.", cell)],
    [Paragraph("Business cases with financial justification (ROI) and KPIs", cell),
     Paragraph("$180M in capital optimisation quantified for CFO decision support; ~40% and ~35% efficiency "
               "programmes measured and reported.", cell)],
    [Paragraph("User research, stakeholder interviews, continuous feedback loops", cell),
     Paragraph("Requirements for the workpaper assistant were elicited from the audit teams who would use it, "
               "then iterated against their feedback until it went to production.", cell)],
    [Paragraph("Partnerships with Data, Engineering, PMO, and HRIS teams; matrixed delivery", cell),
     Paragraph("Resolution &amp; Recovery Planning across 50+ stakeholders in Legal, Treasury, Operations, "
               "Controllers, and Model Risk, to statutory deadlines, none of whom reported to him.", cell)],
    [Paragraph("Executive-level communication; translate data architecture into business value", cell),
     Paragraph("Executive and Board Audit Committee reporting; regulator-facing submissions to the Federal "
               "Reserve and FDIC.", cell)],
]
t = Table(rows, colWidths=[usable * 0.37, usable * 0.63])
t.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 0.5, colors.black), ("LINEBELOW", (0, 0), (-1, 0), 0.9, GOLD),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 1.3), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.3),
]))
flow.append(t)

# ---- Technical ------------------------------------------------------------------
flow += section("TECHNICAL SKILLS")
flow.append(Paragraph(
    "<b>Data:</b> SQL / RDBMS &bull; data modeling &bull; master data management &bull; ETL pipelines "
    "(structured and unstructured) &bull; data lineage &bull; data quality and certification &bull; data "
    "governance &bull; regulatory data (FR 2900, TIC)<br/>"
    "<b>Analytics &amp; reporting:</b> Tableau &bull; Power BI &bull; Alteryx &bull; Excel/VBA &bull; SPSS "
    "&bull; SAS &bull; scikit-learn &bull; descriptive statistics, regression, clustering<br/>"
    "<b>Build:</b> Python &bull; LangChain / retrieval-augmented generation &bull; vector databases &bull; "
    "SHAP / LIME explainability &bull; GitHub Actions<br/>"
    "<b>Governance frameworks:</b> NIST AI RMF &bull; SR 11-7 model risk &bull; COSO &bull; Three Lines of "
    "Defense &bull; SOX ITGC", body))

# ---- Experience ----------------------------------------------------------------
flow += section("PROFESSIONAL EXPERIENCE")
flow.append(job("Assistant Vice President, Global Legal Entity Management &mdash; Citi", "2012 &ndash; 2015"))
flow.append(Paragraph("Tampa, FL &bull; the data-product programme", sub))
flow.append(Paragraph("<b>Consolidated 500+ legal-entity data sources into governed master data</b> &mdash; data "
                      "modeling, ETL, ownership and end-to-end lineage, and the data-quality controls that made "
                      "the output certifiable. Enabled automated <b>FR 2900</b> and <b>TIC</b> regulatory filings "
                      "at <b>99.8% accuracy</b>, with regulators as the downstream consumer.",
                      bullet, bulletText="•"))

flow.append(job("Vice President, Audit Manager &mdash; Citi", "Jul 2021 &ndash; Apr 2026"))
flow.append(Paragraph("Internal Audit, Cross-Enterprise Program &amp; Change Management | New York, NY", sub))
for b in [
    "<b>Took a tool from requirement to production:</b> elicited needs from audit teams, built a "
    "retrieval-augmented workpaper assistant (Python, LangChain, vector search, SHAP/LIME), integrated it with "
    "Alteryx workflows, and iterated on feedback &mdash; <b>~35%</b> faster review cycle.",
    "Defined the governance target state for AI adoption: use-case intake, risk tiering, a control library, and "
    "post-deployment monitoring KPIs, referenced to NIST AI RMF and SR 11-7.",
    "Led risk-based audits across <b>15+ business units</b> &mdash; including judging whether a data population "
    "was complete and trustworthy enough to test against. Consent-order issue closure accepted by quality "
    "assurance and external regulators. Executive and Board Audit Committee reporting.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Risk Control Manager, Treasury &amp; CIO &mdash; JPMorgan Chase", "Mar 2019 &ndash; Jun 2021"))
flow.append(Paragraph("Capital Controls &amp; Resolution and Recovery Planning | Jersey City, NJ", sub))
for b in [
    "<b>Automated capital and liquidity reconciliation pipelines</b>: <b>~40%</b> less manual review and a "
    "recurring source of reporting error removed.",
    "Ran Resolution &amp; Recovery Planning across <b>50+ stakeholders</b> in Legal, Treasury, and Operations "
    "into Federal Reserve and FDIC submissions; led CCAR validation over a $2.6T balance sheet under SR 15-18.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Capital Controller, Basel Measurement &amp; Analytics &mdash; JPMorgan Chase",
                "Sep 2017 &ndash; Feb 2019"))
flow.append(Paragraph("Brooklyn, NY &bull; preceded by Program Manager, CIB Resolution &amp; Recovery Planning "
                      "(2015&ndash;2017)", sub))
flow.append(Paragraph("Owned Basel III RWA and capital adequacy reporting for a $50B book; analysis of RWA "
                      "treatment identified <b>$180M</b> in capital optimisation for CFO decision support.",
                      bullet, bulletText="•"))

flow.append(job("Bank Examiner &mdash; Florida Office of Financial Regulation", "Apr 2011 &ndash; Mar 2012"))
flow.append(Paragraph("West Palm Beach, FL &bull; earlier: Senior Business Analyst, Retail Credit Risk &mdash; "
                      "Royal Bank of Scotland, Dubai (2008&ndash;2009)", sub))
flow.append(Paragraph("CAMELS safety-and-soundness examinations alongside federal banking regulators. At RBS, "
                      "built credit-risk MIS over a $500M+ retail portfolio in SAS, SQL, and Excel/VBA.",
                      bullet, bulletText="•"))

# ---- Education & certifications -------------------------------------------------
flow += section("EDUCATION &amp; CERTIFICATIONS")
flow.append(Paragraph(
    "<b>Doctor of Business Administration (DBA), Florida International University</b> &mdash; in progress, "
    "&bull; <b>MBA, Financial Mathematics, Florida International University</b> &mdash; "
    "2011 &bull; <b>B.Sc., Banking &amp; Finance, London School of Economics</b> &mdash; 2005 &bull; "
    "<b>Columbia Engineering FinTech Boot Camp</b> &mdash; 2021<br/>"
    "<b>Certifications:</b> <b>Registered Scrum Master</b> &bull; FDIC Bank Examiner I &bull; GCP "
    "Social/Behavioral Human Research. <i>In progress:</i> CIA Part 1, IAPP AIGP.", body))

doc = SimpleDocTemplate(str(OUT), pagesize=LETTER,
                        leftMargin=0.55 * inch, rightMargin=0.55 * inch,
                        topMargin=0.36 * inch, bottomMargin=0.36 * inch,
                        title="Yasir A. Malik - Resume - HCM Data Program Product Management VP",
                        author="Yasir A. Malik", subject="Data products, lineage & governance")
doc.build(flow)
print(f"built {OUT} at S={S} | header: {header_mode()}")
