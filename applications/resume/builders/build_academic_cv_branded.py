"""Academic CV in the Audit the Algorithm brand - for adjunct, lecturer, and
doctoral-adjacent applications.

Education and research lead. Two pages is normal for a CV and is the target.
Same design system as the branded resumes: wordmark as real text, Times faces,
hairline rules. The research section is written to the standard the public
research page sets for itself: what has been done is stated plainly, what has
not been done is stated just as plainly. No hypotheses have been tested, there
are no peer-reviewed publications to date, and the AI extension is argued, not
tested. Overstating any of that on a CV to a hiring committee would be worse
than saying so.

Placeholders marked [TO CONFIRM: ...] are facts the owner supplied verbally
(SAAC tutoring, graduate teaching assistantship) without the details a CV
needs. The build reports how many remain. Do not ship the PDF while any do.

Run from repo root:
    python3 applications/resume/builders/build_academic_cv_branded.py
"""
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Table, TableStyle

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brand import brand_block  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "applications" / "resume" / "Yasir_Malik_CV_Academic_Branded.pdf"

GOLD = HexColor("#B8860B")
MUTED = HexColor("#6F6754")
S = float(sys.argv[1]) if len(sys.argv) > 1 else 0.90  # 0.90 holds two pages with the mark in the header

body = ParagraphStyle("body", fontName="Times-Roman", fontSize=9.2 * S,
                      leading=11.6 * S, alignment=TA_JUSTIFY, spaceAfter=2.4 * S)
mark = ParagraphStyle("mark", parent=body, alignment=TA_CENTER, fontSize=15 * S,
                      leading=17 * S, spaceAfter=1)
name = ParagraphStyle("name", parent=body, alignment=TA_CENTER, fontName="Times-Bold",
                      fontSize=16 * S, leading=18.5 * S, spaceAfter=1)
cvline = ParagraphStyle("cvline", parent=body, alignment=TA_CENTER, fontName="Times-Italic",
                        fontSize=9 * S, textColor=MUTED, spaceAfter=1)
contact = ParagraphStyle("contact", parent=body, alignment=TA_CENTER, fontSize=8.6 * S,
                         spaceAfter=5 * S)
h2 = ParagraphStyle("h2", parent=body, fontName="Times-Bold", fontSize=9.8 * S,
                    leading=11.5 * S, spaceBefore=6 * S, spaceAfter=1.5,
                    textColor=HexColor("#000000"))
h3 = ParagraphStyle("h3", parent=body, fontName="Times-Bold", fontSize=9.2 * S,
                    leading=11.4 * S, spaceBefore=3 * S, spaceAfter=1)
bullet = ParagraphStyle("bullet", parent=body, leftIndent=11, bulletIndent=1,
                        spaceAfter=1.4 * S)
sub = ParagraphStyle("sub", parent=body, fontName="Times-Italic",
                     fontSize=8.8 * S, textColor=MUTED, spaceAfter=1)
cell = ParagraphStyle("cell", parent=body, fontSize=8.4 * S, leading=10.2 * S,
                      alignment=TA_LEFT, spaceAfter=0)
cellh = ParagraphStyle("cellh", parent=cell, fontName="Times-Bold")
todo = ParagraphStyle("todo", parent=body, textColor=HexColor("#A33A2E"), fontName="Times-Bold")

RULE = ('<para><font size="1" color="#000000">'
        '<u>' + "&nbsp;" * 300 + "</u></font></para>")


def rule():
    return Paragraph(RULE, ParagraphStyle("r", parent=body, spaceAfter=2, leading=2))


def section(title):
    return [Paragraph(title, h2), rule()]


def entry(title, dates):
    return Paragraph(
        f'<b>{title}</b><font color="#000000"> &nbsp;&nbsp;&mdash;&nbsp;&nbsp; </font><b>{dates}</b>', body)


def grid(rows, widths):
    t = Table(rows, colWidths=widths)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("LINEBELOW", (0, 0), (-1, 0), 0.9, GOLD),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 1.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
    ]))
    return t


usable = LETTER[0] - 1.1 * inch
flow = []

# ---- Header --------------------------------------------------------------------
flow += brand_block(mark)
flow.append(Paragraph("YASIR A. MALIK", name))
flow.append(Paragraph("Curriculum Vitae", cvline))
flow.append(Paragraph("Newark, NJ &bull; YasirAMalik@gmail.com &bull; +1 (786) 704-8536 &bull; "
                      "linkedin.com/in/yasiramalik &bull; github.com/MalikAI-786 &bull; "
                      "auditingai.github.io/research.html", contact))

# ---- Education -------------------------------------------------------------------
flow += section("EDUCATION")
flow.append(entry("Doctor of Business Administration (DBA), Florida International University",
                  "in progress"))
flow.append(Paragraph("Chapman Graduate School of Business, Miami, FL &bull; in progress", sub))
for b in [
    "Qualifying examination passed July 2026. Qualifying research: <i>Mitigating Anchoring Bias in Long-Term "
    "Auditor Engagements</i> &mdash; IRB-approved instrument (IRB-25-0462) built and fielded.",
    "Dissertation in development: automation bias and judgment drift when auditors work with AI assistants. "
    "Not yet under ethics review; no participants approached.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))
flow.append(entry("MBA, Financial Mathematics, Florida International University", "2011"))
flow.append(Paragraph("GPA 3.8 &bull; preceded by the Pre-MBA program in International Banking, FIU, 2007", sub))
flow.append(entry("B.Sc., Banking &amp; Finance, London School of Economics and Political Science", "2005"))
flow.append(entry("Columbia Engineering FinTech Boot Camp, Columbia University", "2021"))

# ---- Research programme ----------------------------------------------------------
flow += section("DOCTORAL RESEARCH PROGRAMME &mdash; <i>Auditing the Auditor</i>")
flow.append(Paragraph(
    "What happens to professional judgment when the machine answers first &mdash; and agrees with you. Every "
    "framework now governing AI (SR 11-7, the NIST AI Risk Management Framework, the EU AI Act) assumes a "
    "competent human reviewer sits above the model; none measures whether that reviewer's judgment survives "
    "contact with it. The programme separates three links that are usually conflated, of which only the first "
    "is a cognitive bias:", body))
flow.append(grid([
    [Paragraph("Link", cellh), Paragraph("Claim", cellh), Paragraph("Construct", cellh),
     Paragraph("Question &middot; method", cellh)],
    [Paragraph("L1 &middot; Automated anchoring", cell),
     Paragraph("System output functions as an anchor &mdash; automated, continuous, arriving before the reviewer "
               "has formed a view", cell),
     Paragraph("Automation bias &mdash; a human cognitive bias", cell), Paragraph("How much &middot; survey", cell)],
    [Paragraph("L2 &middot; Sycophantic confirmation", cell),
     Paragraph("The model agrees with a stated position rather than challenging it", cell),
     Paragraph("Sycophancy &mdash; model behaviour, not a bias", cell), Paragraph("How &middot; interviews", cell)],
    [Paragraph("L3 &middot; Recursive epistemic drift", cell),
     Paragraph("Successive systems reprocess earlier machine-influenced work and converge on each other rather "
               "than on evidence", cell),
     Paragraph("Model collapse &mdash; a property of a system of models", cell),
     Paragraph("How, over time &middot; longitudinal", cell)],
], [usable * 0.19, usable * 0.42, usable * 0.22, usable * 0.17]))

flow.append(Paragraph("Status, stated plainly", h3))
flow.append(grid([
    [Paragraph("Element", cellh), Paragraph("State", cellh)],
    [Paragraph("Qualifying examination", cell), Paragraph("Passed, July 2026", cell)],
    [Paragraph("Model &mdash; eleven constructs, fifty-five items, sixteen hypotheses", cell), Paragraph("Built", cell)],
    [Paragraph("Instrument &mdash; IRB-approved (IRB-25-0462), fielded", cell), Paragraph("Built and fielded", cell)],
    [Paragraph("Hypotheses tested", cell), Paragraph("None &mdash; the sample did not support it (below)", cell)],
    [Paragraph("Peer-reviewed publications", cell), Paragraph("None to date", cell)],
    [Paragraph("The AI extension (L1&ndash;L3)", cell), Paragraph("Argued, not tested &mdash; no findings exist", cell)],
], [usable * 0.55, usable * 0.45]))

flow.append(Paragraph("The finding that came out of the failure", h3))
flow.append(Paragraph(
    "The instrument worked; the population did not exist. Applying the study's eligibility criteria to a "
    "commercial research panel in July 2026: <b>334,976</b> panel members screened, <b>~20</b> matched the "
    "eligibility criteria (a prevalence near six per hundred thousand), <b>23</b> raw responses recorded, "
    "<b>4</b> survived screening. A survey at that prevalence needed a sampling frame of roughly 9.6 million; "
    "the panel held about three and a half percent of it. This is a structural property of studying a narrow "
    "specialist population, measurable in advance, which the profession's methods literature treats as a "
    "limitation to apologise for rather than a parameter to design around. It is now a research question in "
    "its own right: under what conditions is a cross-national study of a rare professional population "
    "feasible at all?", body))

flow.append(Paragraph("Open gaps, including the uncomfortable ones", h3))
for b in [
    "<b>Measurement.</b> The outcome construct is self-reported &mdash; it asks auditors to report how far a "
    "reference point drove their judgment, which is precisely what anchoring prevents them from noticing. "
    "Needs an honest rename to <i>perceived judgment discipline</i>, or a behavioural measure: a planted "
    "anchor and an observable adjustment.",
    "<b>Theory.</b> Automation bias and algorithm aversion both have support; L1 assumes over-trust and has no "
    "account of when the reverse occurs. The moderators need specifying &mdash; task type, expertise, stakes, "
    "and whether output arrives before or after the human forms a view.",
    "<b>Access.</b> L3 has no design, deliberately: it needs multi-year engagement files or repeated access to "
    "the same auditors. Writing a protocol for a study that cannot be run would repeat the error already made.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(Paragraph("Current work", h3))
for b in [
    "<b>Feasibility manuscript &mdash; drafted, not submitted.</b> The prevalence finding written as a "
    "methodological contribution for cross-national research on hard-to-reach professional populations.",
    "<b>Feasibility calculator &mdash; working.</b> Takes panel size, prevalence, eligibility and completion "
    "rates; returns reachable sample and cost per usable response; validated by reproducing the study that "
    "produced it. Its useful output is the threshold where a survey design stops being viable and an interview "
    "design becomes the honest choice.",
    "<b>The qualitative arm (L2) &mdash; blocked on ethics review.</b> Phenomenological design: protocol, "
    "sampling plan, coding scheme, trustworthiness criteria and an append-only audit trail written. "
    "Falsification conditions committed and timestamped <i>before</i> any data exists. Zero participants.",
    "<b>A research pipeline built against its own subject.</b> Model-agnostic runbooks: every claim carries a "
    "resolving source, a null search is reported as null, and an adversarial pass runs against the programme's "
    "own conclusions &mdash; because a researcher who lets a model confirm his topic is running his own "
    "dissertation's failure mode on himself.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

# ---- Teaching --------------------------------------------------------------------
flow += section("TEACHING, TUTORING &amp; MENTORING")
flow.append(Paragraph(
    "[TO CONFIRM: Graduate Teaching Assistant &mdash; institution, department, course title(s) and number(s), "
    "term(s), supervising faculty member, and duties (sections led, grading, office hours).]", todo))
flow.append(Paragraph(
    "[TO CONFIRM: SAAC Tutor &mdash; spell out the acronym, institution, subjects tutored, dates, and whether "
    "one-to-one or group.]", todo))
flow.append(entry("Guest lecturer, Florida International University", "ongoing"))
flow.append(Paragraph("[TO CONFIRM: course(s), host faculty, topic(s) and date(s) of guest lectures.]", todo))
flow.append(entry("Class visit, Rutgers University", "15 Sep 2026"))
flow.append(Paragraph("[TO CONFIRM: campus, course, host, and whether this is a talk or an observation.]", todo))
flow.append(entry("Mentor to 8+ internal auditors, Citi Internal Audit", "2021 &ndash; 2026"))
flow.append(Paragraph("Responsible AI adoption, prompt engineering, and ethical decision-making in human&ndash;AI "
                      "workflows; recognised with Citi's <i>Delivers with Pride</i> award.", bullet, bulletText="•"))
flow.append(Paragraph("Teaching interests", h3))
flow.append(Paragraph(
    "Auditing and assurance &bull; internal audit and controls &bull; enterprise and operational risk &bull; "
    "bank regulation and supervision &bull; AI governance and AI ethics &bull; business analytics and data "
    "governance &bull; fintech &bull; judgment and decision-making in professional practice", body))

# ---- Professional experience -----------------------------------------------------
flow += section("PROFESSIONAL EXPERIENCE")
for title, dates, where, line in [
    ("Vice President, Audit Manager &mdash; Citi", "Jul 2021 &ndash; Apr 2026",
     "Internal Audit, Cross-Enterprise Program &amp; Change Management, New York",
     "Led risk-based audits across 15+ business units; consent-order issue-closure evidence accepted by external "
     "regulators; built independent assurance over enterprise AI adoption; designed and shipped a RAG workpaper "
     "assistant (Python, LangChain) that cut review cycle time ~35%; executive and Board Audit Committee reporting."),
    ("Risk Control Manager, Treasury &amp; CIO &mdash; JPMorgan Chase", "Mar 2019 &ndash; Jun 2021",
     "First-line capital controls and Resolution &amp; Recovery Planning, Jersey City",
     "Owned the first-line control framework for capital activities; CCAR forecast validation over a $2.6T balance "
     "sheet under SR 15-18; Resolution &amp; Recovery Planning across 50+ stakeholders into Federal Reserve and "
     "FDIC submissions; automated reconciliations, ~40% less manual review."),
    ("Capital Controller, Basel Measurement &amp; Analytics &mdash; JPMorgan Chase", "Sep 2017 &ndash; Feb 2019",
     "Brooklyn; preceded by Program Manager, CIB Resolution &amp; Recovery Planning, 2015&ndash;2017",
     "Basel III RWA and capital adequacy reporting for a $50B book; $180M in capital optimization identified."),
    ("Assistant Vice President, Global Legal Entity Management &mdash; Citi", "2012 &ndash; 2015", "Tampa",
     "Consolidated 500+ legal-entity data sources into governed master data; automated FR 2900 and TIC "
     "regulatory filings at 99.8% accuracy."),
    ("Bank Examiner, Bureau of Bank Regulation &mdash; Florida Office of Financial Regulation",
     "Apr 2011 &ndash; Mar 2012", "West Palm Beach",
     "CAMELS safety-and-soundness examinations of state and national banks alongside federal banking "
     "regulators; workpapers supporting formal enforcement actions."),
    ("Senior Business Analyst, Retail Credit Risk &mdash; Royal Bank of Scotland", "2008 &ndash; 2009", "Dubai",
     "Credit-risk MIS over a $500M+ retail portfolio in SAS, SQL, and Excel/VBA."),
]:
    flow.append(entry(title, dates))
    flow.append(Paragraph(where, sub))
    flow.append(Paragraph(line, bullet, bulletText="•"))

# ---- Industry practice -----------------------------------------------------------
flow += section("INDUSTRY PRACTICE")
flow.append(entry("Founder, Audit the Algorithm", "2024 &ndash; present"))
flow.append(Paragraph("AI governance advisory for regulated financial services (auditingai.github.io): bias and "
                      "drift testing, regulator-defensible control frameworks, human&ndash;AI workflow design. "
                      "Authored an AI governance framework referencing NIST AI RMF and SR 11-7.", bullet, bulletText="•"))

# ---- Research skills -------------------------------------------------------------
flow += section("RESEARCH METHODS &amp; SKILLS")
flow.append(Paragraph(
    "<b>Methods:</b> survey instrument development and validation &bull; experimental design &bull; IRB protocol "
    "authorship &bull; feasibility and prevalence analysis for hard-to-reach populations &bull; phenomenological "
    "interview design and coding &bull; pre-registered falsification conditions &bull; adversarial review of "
    "one's own conclusions<br/>"
    "<b>Statistical and analytical software:</b> SPSS &bull; SAS &bull; Python (scikit-learn, pandas) &bull; SQL "
    "&bull; Excel/VBA<br/>"
    "<b>AI and NLP:</b> LangChain / LangGraph &bull; retrieval-augmented generation &bull; vector databases &bull; "
    "SHAP / LIME explainability &bull; evaluation and red-teaming<br/>"
    "<b>Visualisation and workflow:</b> Tableau &bull; Power BI &bull; Alteryx &bull; GitHub Actions", body))

# ---- Certifications ---------------------------------------------------------------
flow += section("CERTIFICATIONS &amp; TRAINING")
flow.append(Paragraph(
    "FDIC Bank Examiner I &bull; GCP Social/Behavioral Human Subjects Research &bull; Registered Scrum Master. "
    "<i>In progress:</i> Certified Internal Auditor (Part 1) &bull; IAPP Artificial Intelligence Governance "
    "Professional (AIGP).", body))

# ---- Recognition & references ----------------------------------------------------
flow += section("RECOGNITION")
flow.append(Paragraph("Citi <i>Delivers with Pride</i> award for AI-powered audit quality and mentoring.", body))
flow += section("REFERENCES")
flow.append(Paragraph("Available on request.", body))

doc = SimpleDocTemplate(str(OUT), pagesize=LETTER,
                        leftMargin=0.55 * inch, rightMargin=0.55 * inch,
                        topMargin=0.4 * inch, bottomMargin=0.4 * inch,
                        title="Yasir A. Malik - Curriculum Vitae", author="Yasir A. Malik",
                        subject="Academic CV - auditing, risk, AI governance")
doc.build(flow)

src = Path(__file__).read_text(encoding="utf-8")
n_todo = len(re.findall(r"\[TO CONFIRM:", src))
print(f"built {OUT} at S={S}  |  placeholders remaining: {n_todo}")
