#!/usr/bin/env python3
"""GEB 7911 one-page proposal poster. One slide, 16:9, editable PowerPoint.

Built to the Week 6 class requirement: problem, purpose, research questions,
assumptions highlights, methodology, contributions, potential limitations and
references, all on one page, ten minutes maximum.

Three corrections from the 13 and 14 September feedback are already applied:
the gap is framed as what the literature has focused on rather than what nobody
has done, eligibility is the phenomenon rather than the job title, and the
research question is never called a process question.

Content and argument are Yasir A. Malik's. References are taken from the
reference list of his own submitted quantitative paper, where each carries a DOI.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pptx_shim import Deck, rgb, W, H, DISP, DISPI, BODY, MONO, MONOB

BLUE=rgb("#081E3F"); GOLD=rgb("#B6862C"); INK=rgb("#14171C")
PAPER=rgb("#FCFBF8"); MUTE=rgb("#767D86"); RULE=rgb("#D8D4CB")
SOFT=rgb("#E8EDF4"); WARM=rgb("#FAF3E4"); WHITE=rgb("#FFFFFF")
BODYC=rgb("#3A4048"); TEAL=rgb("#1C6B63"); RUST=rgb("#8C3A1B")
DKTXT=rgb("#B9C7D8"); DKSUB=rgb("#8FA3BC"); AMBER=rgb("#8A6A1F")

M = 34
SEAL = "/home/user/Profile/assets/images/fiu-seal.png"

d = Deck("Receiving Confirmation - GEB 7911 qualitative research proposal",
         "Yasir A. Malik - FIU DBA Cohort 8.14")
box, txt, para, rule = d.box, d.txt, d.para, d.rule
d.page(PAPER)

# ---------------- header ----------------
box(0, 0, W, 74, fill=BLUE)
try:
    d.image(SEAL, M, 14, 44, 44)
    ox = M + 56
except Exception:
    box(M, 16, 4, 40, fill=GOLD); ox = M + 16
txt("FLORIDA INTERNATIONAL UNIVERSITY  ·  CHAPMAN GRADUATE SCHOOL OF BUSINESS",
    ox, 14, MONOB, 7.5, GOLD, track=1.6)
txt("Receiving Confirmation", ox, 26, DISP, 25, WHITE)
txt("How experienced auditors make sense of AI-generated agreement with a judgment they had already formed",
    ox, 55, DISPI, 11.5, DKTXT)
txt("YASIR A. MALIK", W - M, 20, MONOB, 9.5, GOLD, track=1.6, align="r")
txt("DBA Cohort 8.14  ·  GEB 7911  ·  Dr. Cristina Gonzalez", W - M, 36, BODY, 10, DKSUB, align="r")
txt("WEEK 8 PRESENTATION  ·  6 OCT 2026", W - M, 54, MONOB, 7.6, GOLD, track=1.0, align="r")

# ---------------- research question strip ----------------
box(M, 84, W - 2 * M, 44, fill=WARM, stroke=GOLD, r=3)
box(M, 84, 5, 44, fill=GOLD)
txt("RESEARCH QUESTION", M + 18, 94, MONOB, 7.5, AMBER, track=1.5)
txt("How do experienced auditors experience and make sense of receiving an AI-generated conclusion "
    "that confirms a judgment they had already formed?", M + 18, 108, DISPI, 13.5, INK)

# ---------------- four columns ----------------
COLS = 4
CW = (W - 2 * M - 3 * 11) / COLS
TOP = 138
BODYSZ, LEAD = 8.0, 10.1

def head(x, y, label, color):
    box(x, y, CW, 14, fill=color, r=2)
    txt(label, x + 8, y + 3, MONOB, 7.2, WHITE, track=1.2)
    return y + 19

def blk(x, y, s, size=BODYSZ, color=BODYC, font=BODY, w=None):
    return y + para(s, x, y, w or CW, font, size, color, lead=LEAD) + 4

def bullets(x, y, items, dot=TEAL, size=BODYSZ):
    for it in items:
        box(x + 1, y + 3.0, 3.2, 3.2, fill=dot, r=2)
        y = y + para(it, x + 9, y, CW - 9, BODY, size, BODYC, lead=LEAD) + 3
    return y + 2

X = [M + i * (CW + 11) for i in range(COLS)]

# ---- column 1 ----
y = head(X[0], TOP, "1 · PROBLEM STATEMENT", BLUE)
y = blk(X[0], y,
    "An auditor on a recurring engagement has always carried a prior conclusion forward. What is new "
    "is that an AI system now produces a conclusion of its own, and sometimes it agrees.")
y = blk(X[0], y,
    "Research on AI and auditor judgment has focused primarily on the extent of reliance, which a "
    "survey can measure. The lived experience of receiving machine agreement with a judgment already "
    "formed remains unexplored.", color=INK)
y = blk(X[0], y,
    "Firms and regulators are writing AI-use policy on the assumption that a human reviewer still "
    "exercises independent judgment.")
y = head(X[0], y + 2, "2 · PURPOSE STATEMENT", BLUE)
bt = y - 2
yy = blk(X[0] + 8, y + 5,
    "The purpose of this phenomenological study is to understand how experienced auditors experience "
    "and make sense of receiving an AI-generated conclusion that confirms a judgment they had already "
    "formed.", color=INK, w=CW - 16)
box(X[0], bt, CW, yy - bt + 2, fill=SOFT, r=3)
blk(X[0] + 8, y + 5,
    "The purpose of this phenomenological study is to understand how experienced auditors experience "
    "and make sense of receiving an AI-generated conclusion that confirms a judgment they had already "
    "formed.", color=INK, w=CW - 16)

# ---- column 2 ----
y = head(X[1], TOP, "3 · PHILOSOPHICAL ASSUMPTIONS", BLUE)
txt("SOCIAL CONSTRUCTIVIST  ·  INDUCTIVE", X[1], y - 2, MONOB, 7.5, TEAL, track=1.1)
y += 11
for lab, bd in [
  ("ONTOLOGICAL", "Multiple realities. Auditors' accounts of the experience are the data, not a proxy for one correct account."),
  ("EPISTEMOLOGICAL", "Knowledge comes from first-person accounts in semi-structured interviews."),
  ("AXIOLOGICAL", "The researcher is a career auditor who built an AI review tool: insider access and insider bias, managed through reflexive memos and a confirmation hazard log."),
  ("METHODOLOGICAL", "Inductive phenomenology across individuals at different firms."),
]:
    txt(lab, X[1], y, MONOB, 7.0, AMBER, track=1.0)
    y = y + 9 + para(bd, X[1], y + 9, CW, BODY, 7.9, BODYC, lead=9.9) + 4
y = head(X[1], y + 1, "4 · METHODOLOGY: APPROACH", BLUE)
y = blk(X[1], y,
    "Phenomenology (Creswell & Poth, 2024). The question asks about experience and meaning making "
    "across individuals, which is what phenomenology is for.", color=INK)
y = bullets(X[1], y, [
  "Not case study: the phenomenon crosses firms, with no bounded site",
  "Not grounded theory: the question is about experience, not process",
], dot=RUST)

# ---- column 3 ----
y = head(X[2], TOP, "5 · METHODOLOGY: DATA COLLECTION", BLUE)
txt("ELIGIBILITY IS THE PHENOMENON", X[2], y - 2, MONOB, 7.2, RUST, track=1.0)
y += 10
y = blk(X[2], y,
    "Participants can recall a specific time AI output agreed with a judgment they had already formed. "
    "They do not need to have interpreted it in any particular way.", color=INK)
y = bullets(X[2], y, [
  "Five or more years in audit or risk assurance, recurring engagements",
  "Criterion sampling plus referrals, all screened the same way; a short screening question tested first",
  "About 10 to 15, guided by the depth and richness of accounts",
  "Semi-structured, recorded interviews; protocol piloted first",
])
y = head(X[2], y, "6 · METHODOLOGY: DATA ANALYSIS", BLUE)
txt("FIVE ACTIVITIES  ·  NVIVO", X[2], y - 2, MONOB, 7.0, TEAL, track=0.9)
y += 10
for n, s2 in [
  ("1", "Managing and organising. NVivo, named file plan, secure storage."),
  ("2", "Reading and memoing. A dated reflexive journal, kept as evidence."),
  ("3", "Describing and classifying. Horizontalisation, meaning units, clusters."),
  ("4", "Developing interpretations. Textural and structural, then a composite."),
  ("5", "Representing. A thematic map and a composite narrative."),
]:
    txt(n, X[2] + 2, y, MONOB, 8.0, GOLD)
    y = y + para(s2, X[2] + 11, y, CW - 11, BODY, 7.9, BODYC, lead=9.9) + 2

# ---- column 4 ----
y = head(X[3], TOP, "7 · ETHICS AND VALIDATION", BLUE)
y = bullets(X[3], y, [
  "Informed consent and IRB determination before any contact; pseudonyms, no firm detail",
  "Member checking of each participant's own textural description",
  "External reviewer reads purposefully chosen transcripts, including a disconfirming one, with the analytic memos",
  "Confirmation hazard log entries tied to specific analytic decisions in the audit trail",
], dot=RUST)
y = head(X[3], y, "8 · DESIRED CONTRIBUTIONS", BLUE)
txt("TO PRACTICE", X[3], y - 2, MONOB, 7.0, AMBER, track=1.0)
y = blk(X[3], y + 9,
    "Shows what human review of AI output is actually like, for firms and regulators relying on it.")
txt("TO ACADEMIA", X[3], y - 2, MONOB, 7.0, AMBER, track=1.0)
y = blk(X[3], y + 9,
    "Distinguishes the auditor's experience of agreement from measures of reliance.")
y = head(X[3], y, "9 · POTENTIAL LIMITATIONS", BLUE)
y = bullets(X[3], y, [
  "Retrospective accounts of a past experience",
  "Insider researcher: bias managed, not eliminated",
  "Small purposive sample; not intended to generalise",
], dot=RUST)

# ---------------- AI disclosure (replaces the timeline, per Dr. Gonzalez, 1 Oct) ----------------
TY = 452
box(M, TY, W - 2 * M, 26, fill=SOFT, r=3)
txt("AI DISCLOSURE", M + 10, TY + 8, MONOB, 7.2, BLUE, track=1.2)
para("Generative AI (Claude, Anthropic) helped draft and lay out this poster from the author's proposal and protocol, and checked clarity. "
     "The research question, design decisions and interpretations are the author's (FIU Graduate School AI policy).",
     M + 92, TY + 5, W - 2 * M - 120, BODY, 7.2, BODYC, lead=8.8)

# ---------------- references ----------------
RY = 486
rule(RY, color=RULE)
txt("REFERENCES", M, RY + 5, MONOB, 7.2, BLUE, track=1.2)
txt("Full list in the paper", M, RY + 15, BODY, 6.6, MUTE)
REFS = [
 "Commerford, B. P., Dennis, S. A., Joe, J. R., & Ulla, J. W. (2022). Man versus machine: Complex estimates and auditor reliance on artificial intelligence. Journal of Accounting Research, 60(1), 171-201.",
 "Creswell, J. W., & Poth, C. N. (2024). Qualitative inquiry and research design: Choosing among five approaches (5th ed.). SAGE.",
 "Fotoh, L. E., & Mugwira, T. (2025). Exploring the impact of generative AI on professional skepticism in auditing.",
 "Glickman, M., & Sharot, T. (2025). How human-AI feedback loops alter human perceptual, emotional and social judgements.",
 "Kokina, J., Blanchette, S., Davenport, T. H., & Pachamanova, D. (2025). Challenges and opportunities for artificial intelligence in auditing. International Journal of Accounting Information Systems, 56, 100734.",
 "Murikah, W., Nthenge, J. K., & Musyoka, F. M. (2024). Bias and ethics of AI systems applied in auditing: A systematic review.",
 "Parasuraman, R., & Manzey, D. H. (2010). Complacency and bias in human use of automation. Human Factors, 52(3), 381-410.",
 "Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science, 185(4157), 1124-1131.",
]
cw = (W - 2 * M - 80) / 4
for i, r in enumerate(REFS):
    cx = M + 80 + (i % 4) * cw
    cy = RY + 4 + (i // 4) * 24
    para(r, cx, cy, cw - 8, BODY, 6.0, MUTE, lead=6.3)

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if "--appendix" in sys.argv:
    from poster_appendix import add as add_appendix
    add_appendix(d)
out = args[0] if args else "poster.pptx"
d.save(out)
print("wrote", out)
