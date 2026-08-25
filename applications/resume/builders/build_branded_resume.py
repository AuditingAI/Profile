"""Harvard-style ATS resume with the Audit the Algorithm wordmark.

The wordmark is drawn as real text rather than an embedded image: it keeps the
file small enough to attach reliably, and an ATS reading the text layer sees
the brand rather than skipping over an opaque graphic.
"""
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

GOLD = HexColor("#B8860B")
MUTED = HexColor("#6F6754")

S = 0.97  # global scale; nudge down if content grows past one page

body = ParagraphStyle("body", fontName="Times-Roman", fontSize=8.9 * S,
                      leading=11.3 * S, alignment=TA_JUSTIFY, spaceAfter=2.5 * S)
mark = ParagraphStyle("mark", parent=body, alignment=TA_CENTER, fontSize=15 * S,
                      leading=17 * S, spaceAfter=1)
name = ParagraphStyle("name", parent=body, alignment=TA_CENTER, fontName="Times-Bold",
                      fontSize=15.5 * S, leading=18 * S, spaceAfter=1.5)
tag = ParagraphStyle("tag", parent=body, alignment=TA_CENTER, fontSize=8.9 * S,
                     leading=11 * S, spaceAfter=1)
contact = ParagraphStyle("contact", parent=tag, fontSize=8.5 * S, spaceAfter=5 * S)
h2 = ParagraphStyle("h2", parent=body, fontName="Times-Bold", fontSize=9.4 * S,
                    leading=11 * S, spaceBefore=5.5 * S, spaceAfter=1.5,
                    borderWidth=0, textColor=HexColor("#000000"))
bullet = ParagraphStyle("bullet", parent=body, leftIndent=11, bulletIndent=1,
                        spaceAfter=1.5 * S)
sub = ParagraphStyle("sub", parent=body, fontName="Times-Italic",
                     fontSize=8.5 * S, textColor=MUTED, spaceAfter=1)

RULE = ('<para><font size="1" color="#000000">'
        '<u>' + "&nbsp;" * 300 + "</u></font></para>")


def rule():
    return Paragraph(RULE, ParagraphStyle("r", parent=body, spaceAfter=2, leading=2))


def job(title, dates):
    return Paragraph(
        f'<b>{title}</b><font color="#000000"> &nbsp;&nbsp;&mdash;&nbsp;&nbsp; </font>'
        f'<b>{dates}</b>', body)


flow = []
flow.append(Paragraph(
    f'<font color="#B8860B"><b>Audit</b></font> '
    f'<font color="#6F6754"><i>the</i></font> '
    f'<font color="#B8860B"><b>Algorithm</b></font>', mark))
flow.append(Paragraph("YASIR A. MALIK", name))
flow.append(Paragraph("Responsible AI Program Manager &mdash; Governance, Safety Standards &amp; Enterprise Trust", tag))
flow.append(Paragraph("Newark, NJ &bull; YasirAMalik@gmail.com &bull; +1 (786) 704-8536 &bull; "
                      "linkedin.com/in/yasiramalik &bull; github.com/MalikAI-786", contact))

flow.append(Paragraph("SUMMARY", h2)); flow.append(rule())
flow.append(Paragraph(
    "Twenty years running risk and safety programs where a bad launch is a federal matter. Authored an "
    "AI governance framework referencing NIST AI RMF and SR 11-7 &mdash; model inventory, risk tiering, "
    "explainability, human-in-the-loop controls &mdash; and built the AI tooling it governs. Former OCC bank "
    "examiner; led consent-order remediation with evidence accepted by federal regulators, which is pre-launch "
    "safety review under the harshest possible audience. DBA candidate (FIU, expected 2028) researching "
    "over-reliance on AI-assisted tools &mdash; the human-factors half of Responsible AI.", body))

flow.append(Paragraph("PROFESSIONAL EXPERIENCE", h2)); flow.append(rule())
flow.append(job("Vice President, Audit Manager &mdash; Citi", "Jul 2021 &ndash; Apr 2026"))
flow.append(Paragraph("Cross-Enterprise Program &amp; Change Management | New York, NY", sub))
for b in [
    "Authored the AI governance framework for the internal governance team: use-case inventory, risk tiering to "
    "prioritize higher-risk offerings, explainability requirements, and human-in-the-loop control design &mdash; "
    "referenced to NIST AI RMF and SR 11-7.",
    "Ran risk-based review across 15+ business units, setting the standard for what had to be true before a change "
    "shipped, and escalating where it was not.",
    "Drove consent-order remediation: issue-closure packages and evidence submitted to quality assurance and external "
    "regulators &mdash; safety claims that had to survive adversarial review.",
    "Built and shipped a prompt-engineered RAG document assistant for workpaper Q&amp;A (~35% faster review), so the "
    "governance frameworks were written by someone who has also shipped the product being governed.",
    "Delivered executive and Board Audit Committee reporting; mentored 8+ staff on responsible AI adoption and bias "
    "awareness. Citi <i>Delivers with Pride</i> recognition.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Risk Control Manager, Treasury &amp; CIO &mdash; JPMorgan Chase", "Mar 2019 &ndash; Jun 2021"))
flow.append(Paragraph("Capital Controls &amp; Resolution and Recovery Planning | Jersey City, NJ", sub))
for b in [
    "Led the firm's Resolution &amp; Recovery Planning program across 50+ stakeholders in Legal, Treasury, and "
    "Operations &mdash; cross-functional program management against immovable regulatory deadlines, delivering to the "
    "Federal Reserve and FDIC.",
    "Built automated reconciliation dashboards that cut manual review time ~40%.",
]:
    flow.append(Paragraph(b, bullet, bulletText="•"))

flow.append(job("Capital Controller, Basel Measurement &amp; Analytics &mdash; JPMorgan Chase", "Sep 2017 &ndash; Feb 2019"))
flow.append(Paragraph("Brooklyn, NY (preceded by Program Manager, CIB Resolution &amp; Recovery Planning, 2015&ndash;2017)", sub))
flow.append(Paragraph("Owned Basel III RWA and capital adequacy reporting; identified $180M in capital optimization "
                      "opportunities for CFO decision support.", bullet, bulletText="•"))

flow.append(job("Bank Examiner &mdash; OCC / FL Office of Financial Regulation", "Apr 2011 &ndash; Mar 2012"))
flow.append(Paragraph("Bureau of Bank Regulation | West Palm Beach, FL", sub))
flow.append(Paragraph("Conducted safety-and-soundness examinations across credit, liquidity, and operational risk; "
                      "contributed to enforcement actions and remediation monitoring. FDIC Bank Examiner I.",
                      bullet, bulletText="•"))

flow.append(Paragraph("EARLIER EXPERIENCE", h2)); flow.append(rule())
flow.append(Paragraph("<b>Assistant Vice President, Global Legal Entity Management &mdash; Citi,</b> Tampa, FL "
                      "(2012&ndash;2015): Centralized 500+ legal-entity data sources into governed master data, "
                      "enabling automated FR2900 and TIC regulatory filings at 99.8% accuracy.", body))

flow.append(Paragraph("EDUCATION", h2)); flow.append(rule())
flow.append(Paragraph(
    "<b>Doctor of Business Administration (DBA), Florida International University</b> &mdash; in progress, expected "
    "2028 | GPA 3.81. Qualifying research completed Jul 2026: <i>Mitigating Anchoring Bias in Long-Term Auditor "
    "Engagements</i> (IRB-25-0462). Dissertation in development: automation bias in AI-assisted judgment.<br/>"
    "<b>Master of Business Administration (MBA), Florida International University</b> &mdash; 2011<br/>"
    "<b>B.Sc., Banking &amp; Finance, London School of Economics (LSE)</b> &mdash; 2005<br/>"
    "<b>Columbia Engineering FinTech Boot Camp, Columbia University</b> &mdash; 2021", body))

flow.append(Paragraph("SKILLS &amp; CERTIFICATIONS", h2)); flow.append(rule())
flow.append(Paragraph(
    "<b>Responsible AI:</b> NIST AI RMF &bull; SR 11-7 model risk &bull; EU AI Act and ISO/IEC 42001 readiness &bull; "
    "risk tiering &bull; explainability &bull; human-in-the-loop control design &bull; pre-launch review &bull; "
    "responsible-AI policy and training<br/>"
    "<b>Program management:</b> Cross-functional programs (50+ stakeholders) &bull; regulatory deadline delivery &bull; "
    "roadmap and milestone ownership &bull; escalation management &bull; executive and Board reporting<br/>"
    "<b>Technical:</b> Python (applied) &bull; RAG and prompt engineering &bull; SQL &bull; Tableau &bull; Excel/VBA "
    "&bull; GitHub<br/>"
    "<b>Certifications:</b> FDIC Bank Examiner I &bull; Registered Scrum Master &bull; GCP Social/Behavioral Human "
    "Research (AI Ethics)", body))

doc = SimpleDocTemplate("Yasir_Malik_Resume_Google_CloudRAI_Branded.pdf", pagesize=LETTER,
                        leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                        topMargin=0.45 * inch, bottomMargin=0.45 * inch,
                        title="Yasir A. Malik - Resume", author="Yasir A. Malik",
                        subject="Responsible AI Program Manager")
doc.build(flow)
print("built")
