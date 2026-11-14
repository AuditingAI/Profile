#!/usr/bin/env python3
"""MAN 7275 Week 5 discussion lead + research-topic approval — editable PowerPoint, 16:9.
Yasir A. Malik, FIU DBA Cohort 8.14. Residency, Sat 14 Nov 2026.

House protocol (see build_w5_deck.py, build_project_deck_pptx.py):
FIU Blue #081E3F, FIU Gold #B6862C; Times / Consolas; seal lockup; name on every slide;
every slide carries a figure; no slide is a list of sentences; speaker script in the notes.

Paper: Sherf, E. N., Venkataramani, V., & Gajendran, R. S. (2019). Too busy to be fair?
Academy of Management Journal, 62(2), 469-502. Every number on these slides was read in
the paper (lead prep: ../MAN7275_Organizational_Behavior/LEAD_Sherf_2019_PREP.md).

Usage: python3 build_man7275_sherf_deck.py <out_dir>
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pptx_shim import Deck, rgb, W, H, DISP, DISPI, BODY, MONO, MONOB

BLUE=rgb("#081E3F"); GOLD=rgb("#B6862C"); INK=rgb("#14171C")
PAPER=rgb("#FCFBF8"); MUTE=rgb("#767D86"); RULE=rgb("#D8D4CB")
SOFT=rgb("#E8EDF4"); WARM=rgb("#FAF3E4"); WHITE=rgb("#FFFFFF")
BODYC=rgb("#454B54"); TEAL=rgb("#1C6B63"); RUST=rgb("#8C3A1B")
STEEL=rgb("#9AA4AE"); PALE=rgb("#EFF2F6")
DKCARD=rgb("#0E2949"); DKRULE=rgb("#1B3252"); DKTXT=rgb("#B9C7D8")
DKSUB=rgb("#8FA3BC"); DKFOOT=rgb("#7E93A8"); AMBER=rgb("#8A6A1F")
RUSTBG=rgb("#FBEFE9"); TEALBG=rgb("#E8F1F0")
M = 54
SEAL = "/home/user/Profile/assets/images/fiu-seal.png"
OUT = sys.argv[1] if len(sys.argv) > 1 else "."


def make(title_meta, footer):
    d = Deck(title_meta, "Yasir A. Malik - FIU DBA Cohort 8.14")
    n = [0]

    def ground(dark=False): d.page(BLUE if dark else PAPER)

    def crest(t=40, light=False):
        fg = WHITE if light else BLUE
        sub = DKSUB if light else MUTE
        d.image(SEAL, M, t, 34, 34)
        d.txt("FLORIDA INTERNATIONAL UNIVERSITY", M + 46, t, MONOB, 10, fg, track=1.9)
        d.txt("Chapman Graduate School of Business  ·  Doctor of Business Administration",
              M + 46, t + 15, BODY, 10.5, sub)

    def chrome(notes, light=False):
        n[0] += 1
        fg = DKFOOT if light else MUTE
        d.rule(H - 32, color=DKRULE if light else RULE)
        d.txt("Yasir A. Malik  ·  Cohort 8.14", M, H - 24, MONOB, 8.5, fg, track=1.1)
        d.txt(footer, W / 2, H - 24, MONO, 8.5, fg, align="c")
        d.txt(str(n[0]), W - M, H - 24, MONOB, 8.5, GOLD, align="r")
        d.notes(notes)

    def eyebrow(s, t, color=GOLD): d.txt(s.upper(), M, t, MONOB, 9.5, color, track=2.0)

    def title(s, t, size=29, color=INK, w=None):
        return d.para(s, M, t, w or (W - 2 * M), DISP, size, color, lead=size * 1.14)

    def node(x, t, w, h, label, fill, color=WHITE, size=15, sub=None):
        d.box(x, t, w, h, fill=fill, r=5)
        if sub:
            d.para(label, x + 12, t + 14, w - 24, DISP, size, color, lead=size * 1.15, align="c")
            d.para(sub, x + 12, t + h - 30, w - 24, DISPI, 11.5, color, lead=14, align="c")
        else:
            lines = len(d.wrap(label, w - 24, DISP, size))
            d.para(label, x + 12, t + (h - lines * size * 1.15) / 2, w - 24, DISP, size, color,
                   lead=size * 1.15, align="c")

    return d, ground, crest, chrome, eyebrow, title, node


# =================================================================== SHERF LEAD
d, ground, crest, chrome, eyebrow, title, node = make(
    "Too Busy to Be Fair? - MAN 7275 Week 5 Discussion Lead",
    "MAN 7275  ·  Week 5  ·  Organizational Behavior  ·  14 November 2026")
box, txt, para, rule, arrow = d.box, d.txt, d.para, d.rule, d.arrow

# 1 TITLE
ground(dark=True); crest(40, light=True)
eyebrow("MAN 7275  ·  Week 5  ·  Justice and fairness  ·  Discussion lead", 150, GOLD)
title("Too Busy to Be Fair?", 190, size=44, color=WHITE)
title("Sherf, Venkataramani & Gajendran (2019)", 244, size=22, color=DKTXT)
title("Academy of Management Journal, 62(2), 469–502", 272, size=22, color=DKTXT)
rule(330, color=DKRULE)
txt("YASIR A. MALIK", M, 352, MONOB, 11, GOLD, track=2.0)
txt("Doctor of Business Administration  ·  Cohort 8.14", M, 372, BODY, 13, DKSUB)
txt("Instructor: Dr. Ravi S. Gajendran  ·  14 November 2026", M, 392, BODY, 13, DKSUB)
box(W - M - 300, 150, 300, 258, fill=DKCARD, r=4)
txt("THE ARGUMENT IN ONE LINE", W - M - 276, 176, MONOB, 8.5, GOLD, track=1.4)
para("Unfair treatment is not only about who the manager is. It is also about how much work they carry "
     "and what the firm rewards.", W - M - 276, 202, 252, BODY, 14, DKTXT, lead=19)
rule(300, x=W - M - 276, w=252, color=DKRULE)
for i, (num, lab) in enumerate([("107", "managers, daily"), ("166", "manager trios"), ("239", "lab participants")]):
    x = W - M - 276 + i * 86
    txt(num, x, 316, DISP, 26, WHITE)
    txt(lab, x, 350, BODY, 10.5, DKSUB)
para("Three designs, one model.", W - M - 276, 378, 252, DISPI, 12, DKTXT)
chrome(">> 20 seconds.\nThis paper moves the cause of unfair management from the manager to the job.\n"
       ">> Go straight to slide 2.", light=True)

# 2 THE PUZZLE
ground(); crest()
eyebrow("The question", 112, BLUE)
title("Why do managers who value fairness still act unfairly?", 140, size=27)
COLW = (W - 2 * M - 80) / 2
box(M, 210, COLW, 170, fill=WHITE, stroke=RULE, r=4)
txt("PRIOR WORK  ·  ACTOR-CENTRIC", M + 18, 230, MONOB, 8.5, MUTE, track=1.4)
para("Unfairness comes from the manager: traits, empathy, motives. The fix is to select and train better managers.",
     M + 18, 256, COLW - 36, BODY, 15, BODYC, lead=21)
arrow(M + COLW + 12, 295, M + COLW + 68, 295, color=GOLD, lw=2.4, head=8)
box(M + COLW + 80, 210, COLW, 170, fill=WARM, stroke=GOLD, r=4)
txt("THIS PAPER  ·  CONTEXT-CENTRIC", M + COLW + 98, 230, MONOB, 8.5, AMBER, track=1.4)
para("Unfairness also comes from the job: how much work there is, and what the organisation rewards.",
     M + COLW + 98, 256, COLW - 36, BODY, 15, BODYC, lead=21)
para("Fair treatment becomes one task competing with others for time and effort. Putting the onus entirely on "
     "managers “might, ironically, be unfair.”", M, 408, W - 2 * M, DISPI, 15, INK, lead=21)
chrome(">> 45 seconds. Classmates have read it: frame the shift, don't summarise.\n"
       "Prior work blamed traits. This paper says workload and rewards.")

# 3 THEORY AND MODEL
ground(); crest()
eyebrow("Theory and model  ·  multiple-task pursuit (Neal et al., 2017)", 112, BLUE)
title("Under scarce time, effort goes to what is measured and rewarded", 140, size=26)
nw, nh, ty = 230, 92, 300
xs = [M, (W - nw) / 2, W - M - nw]
node(xs[0], ty, nw, nh, "Workload", BLUE, sub="amount of work + time pressure")
node(xs[1], ty, nw, nh, "Prioritising technical tasks", TEAL)
node(xs[2], ty, nw, nh, "Justice rule adherence", RUST, sub="all four justice rules")
arrow(xs[0] + nw + 6, ty + nh / 2, xs[1] - 6, ty + nh / 2, color=INK, lw=2, head=7)
arrow(xs[1] + nw + 6, ty + nh / 2, xs[2] - 6, ty + nh / 2, color=INK, lw=2, head=7)
txt("+", (xs[0] + nw + xs[1]) / 2, ty + nh / 2 + 6, DISP, 20, INK, align="c")
txt("−", (xs[1] + nw + xs[2]) / 2, ty + nh / 2 + 6, DISP, 20, INK, align="c")
mx = (xs[0] + nw + xs[1]) / 2
box(mx - 105, 206, 210, 48, fill=GOLD, r=5)
txt("Rewards for justice", mx, 220, DISP, 15, WHITE, align="c")
arrow(mx, 254, mx, ty + nh / 2 - 4, color=GOLD, lw=2, head=7)
for i, (h, s) in enumerate([("H1", "Workload lowers justice through prioritising technical tasks."),
                            ("H2", "Rewards for justice weaken workload → prioritising."),
                            ("H3", "So the indirect effect is weaker when justice is rewarded.")]):
    x = M + i * (W - 2 * M) / 3
    txt(h, x, 416, MONOB, 11, GOLD, track=1.4)
    para(s, x + 30, 414, (W - 2 * M) / 3 - 44, BODY, 13, BODYC, lead=17)
chrome(">> Spend 2 minutes here. Walk the boxes left to right, then the gold box.\n"
       "Technical tasks have clear metrics and get rewarded; fairness rarely does (Kerr, 1975).\n"
       "Rewards for justice weaken the first arrow, so under load the manager keeps doing justice.")

# 4 METHOD
ground(); crest()
eyebrow("Method  ·  three designs, each covering another's weakness", 112, BLUE)
title("Field realism from two studies, causality from the third", 140, size=26)
cols = [("107", "managers", "Study 1  ·  Experience sampling", "2 weeks, two surveys a day, 862 day-level records (MTurk, U.S.)", "Manager self-report"),
        ("166", "manager trios", "Study 2  ·  Field survey, India", "Manager plus two employees; workload and rewards perceived", "Rated by an employee"),
        ("239", "participants", "Study 3  ·  Lab experiment, 2 × 2", "Workload 20 vs 30 min; scorecard 70/20/10 vs 45/45/10", "Coded by blind raters")]
cw = (W - 2 * M - 40) / 3
for i, (num, unit, des, det, rated) in enumerate(cols):
    x = M + i * (cw + 20)
    box(x, 196, cw, 230, fill=WHITE, stroke=RULE, r=4)
    txt(num, x + 18, 210, DISP, 34, RUST if i == 2 else TEAL)
    txt(unit, x + 18 + d.width(num, DISP, 34) + 8, 228, BODY, 13, MUTE)
    txt(des, x + 18, 262, DISP, 14, INK)
    para(det, x + 18, 288, cw - 36, BODY, 13, BODYC, lead=17)
    box(x, 380, cw, 46, fill=WARM, stroke=GOLD, r=4)
    txt("JUSTICE: " + rated.upper(), x + 18, 397, MONOB, 8.5, AMBER, track=1.1)
para("The gold row is who measured fairness. Hold on to it for my critique.", M, 444, W - 2 * M, DISPI, 14, INK)
chrome(">> 45 seconds.\nDiary study, field trios, lab experiment: realism plus causality.\n"
       "Point at the gold row: who rated fairness changes by study.")

# 5 FINDINGS — simple-slopes figure
ground(); crest()
eyebrow("Findings  ·  Study 1 simple slopes", 112, BLUE)
title("When justice is rewarded, workload stops crowding it out", 140, size=26)
gx, gt, gw, gh = M + 40, 200, 420, 210
rule(gt + gh, x=gx, w=gw, color=INK)
d.box(gx, gt, 1.2, gh, fill=INK)
txt("Workload  →", gx + gw, gt + gh + 10, MONO, 9.5, MUTE, align="r")
txt("low", gx + 10, gt + gh + 10, MONO, 9.5, MUTE)
para("Prioritising technical tasks", gx - 44, gt - 30, 200, MONO, 9.5, MUTE)
arrow(gx + 20, gt + 150, gx + gw - 20, gt + 40, color=RUST, lw=3, head=0.1)
arrow(gx + 20, gt + 140, gx + gw - 20, gt + 112, color=TEAL, lw=3, head=0.1)
txt("Low justice rewards   slope .21", gx + gw - 18, gt + 22, MONOB, 10, RUST, align="r")
txt("High justice rewards   slope .05, n.s.", gx + gw - 18, gt + 158, MONOB, 10, TEAL, align="r")
rx = gx + gw + 50; rw = W - M - rx
for i, (val, lab, col) in enumerate([("−.16", "Prioritising → justice adherence (Study 1)", RUST),
                                     ("−.04", "Prioritising → technical performance (Study 2), not significant", TEAL)]):
    t = 200 + i * 110
    box(rx, t, rw, 96, fill=WHITE, stroke=RULE, r=4)
    txt(val, rx + 18, t + 14, DISP, 32, col)
    para(lab, rx + 18, t + 58, rw - 36, BODY, 12.5, BODYC, lead=16)
para("Rewarding fairness raised fair treatment with no measurable loss in technical performance (Studies 2 and 3). "
     "The authors call this a hint that the trade-off “is not always zero-sum.”",
     M, 432, W - 2 * M, DISPI, 14, INK, lead=19)
chrome(">> 45 seconds. Point at the two lines, not the numbers.\n"
       "Red line: low rewards, workload pushes technical tasks first. Teal line: high rewards, almost flat.\n"
       "Study 3 interaction on prioritising: F = 4.14, p = .04.")

# 6 AUTHORS' LEVERS
ground(); crest()
eyebrow("The authors' discussion", 112, BLUE)
title("Three levers for organisations", 140, size=27)
levers = [("1", "Manage workload", "Job design and flexibility (they cite Gajendran et al., 2015)", TEAL),
          ("2", "Reward justice", "Put fair treatment into evaluations and 360-degree feedback", GOLD),
          ("3", "Pre-commit time", "Fixed meetings, town halls, walking around: protected from the inbox", TEAL)]
for i, (num, h, s, col) in enumerate(levers):
    x = M + i * (cw + 20)
    box(x + cw / 2 - 30, 196, 60, 60, fill=col, r=30)
    txt(num, x + cw / 2, 211, DISP, 24, WHITE, align="c")
    txt(h, x + cw / 2, 270, DISP, 17, INK, align="c")
    para(s, x + 14, 296, cw - 28, BODY, 13.5, BODYC, lead=18, align="c")
box(M, 372, W - 2 * M, 70, fill=PALE, stroke=RULE, r=4)
txt("THEIR OWN LIMITS", M + 18, 384, MONOB, 8.5, MUTE, track=1.4)
para("Same-time measures in Study 1  ·  cross-sectional Study 2  ·  student simulation in Study 3  ·  "
     "technical performance never rated by top management", M + 18, 404, W - 2 * M - 36, BODY, 13, BODYC, lead=17)
chrome(">> 30 seconds.\nThey do not argue fairness should always outrank technical work: context decides.")

# 7 CRITIQUE
ground(); crest()
eyebrow("My critique  ·  four questions the evidence leaves open", 112, RUST)
title("Asked as questions, not verdicts", 140, size=27)
crit = [("Who rated fairness?", "Study 1: managers rated themselves. Study 2: managers chose the employees who rated them. Study 3: prioritising was self-reported afterwards."),
        ("Is the moderator robust?", "In Study 2 the workload × rewards interaction was not significant without controls (B = −.04, p = .44). The authors report this openly."),
        ("How large is the effect?", "Study 3 interaction: η²p = .02. Meaningful daily drift, or a fragile effect?"),
        ("Is explaining protected?", "Study 2: no significant effect for informational justice, yet Study 3's justice task was mostly writing an explanation.")]
qw, qh = (W - 2 * M - 20) / 2, 118
for i, (h, s) in enumerate(crit):
    x = M + (i % 2) * (qw + 20); t = 192 + (i // 2) * (qh + 14)
    box(x, t, qw, qh, fill=WHITE, stroke=RULE, r=4)
    box(x + 16, t + 14, 26, 26, fill=RUST, r=13)
    txt(str(i + 1), x + 29, t + 19, MONOB, 12, WHITE, align="c")
    txt(h, x + 54, t + 17, DISP, 16, INK)
    para(s, x + 16, t + 50, qw - 32, BODY, 12.5, BODYC, lead=16)
chrome(">> About 1 minute 45. Lead with question 1: it ties to my 5 Nov class point that ratings are weak evidence.\n"
       "Then question 2. Dr. Gajendran co-wrote this paper: ask, don't accuse.\n"
       "If asked about question 4: 'I don't know. How do you read it?'")

# 8 EXTENSION
ground(); crest()
eyebrow("Extension  ·  my research on AI in audit review", 112, BLUE)
title("When a tool does part of the job", 140, size=27)
para("In audit review, the manager's challenge works like a justice task: effortful, rarely measured, first to go "
     "under load. An AI summary that agrees makes skipping it cheaper.", M, 184, W - 2 * M, BODY, 15, BODYC, lead=21)
ty = 318
node(xs[0], ty, nw, 84, "Reviewer workload", BLUE)
node(xs[1], ty, nw, 84, "Accepting the AI's agreement", TEAL)
node(xs[2], ty, nw, 84, "Challenge of the work", RUST)
arrow(xs[0] + nw + 6, ty + 42, xs[1] - 6, ty + 42, color=INK, lw=2, head=7)
arrow(xs[1] + nw + 6, ty + 42, xs[2] - 6, ty + 42, color=INK, lw=2, head=7)
box(mx - 105, 250, 210, 44, fill=GOLD, r=5)
txt("Rewards for challenge", mx, 263, DISP, 15, WHITE, align="c")
arrow(mx, 294, mx, ty + 38, color=GOLD, lw=2, head=7)
para("Same shape as Sherf's model: the reviewer's challenge is what gets cut, and rewards decide whether it survives.",
     M, 424, W - 2 * M, DISPI, 14, INK, lead=19)
chrome(">> 1 minute.\nIn audit review, the manager's challenge is the justice-like task. An AI that agrees makes skipping it cheaper.\n"
       "Study idea: survey reviewers who use AI tools; workload, rewards for challenge, reliance on AI agreement, professional skepticism.")

# 9 CONNECTIONS + QUESTIONS — hub figure
ground(); crest()
eyebrow("Connections and two questions for the room", 112, BLUE)
title("Where this paper sits in the course", 140, size=27)
hx, ht = M + 200, 300
box(hx - 70, ht - 26, 140, 52, fill=BLUE, r=5)
txt("Sherf et al.", hx, ht - 10, DISP, 16, WHITE, align="c")
spokes = [("Judge & Piccolo (2004)", "the moderator is a contingent reward", M, 196),
          ("Lin, Scott & Matta (2019)", "good leader behaviour costs resources", M + 230, 196),
          ("Colquitt & Zipay (2015)", "justice rules vs. overall fairness", M, 360),
          ("Avery et al. (2023)", "uneven rewards, uneven fairness", M + 230, 360)]
for name, s, x, t in spokes:
    box(x, t, 170, 62, fill=WHITE, stroke=RULE, r=4)
    txt(name, x + 10, t + 10, DISP, 12, INK)
    para(s, x + 10, t + 30, 150, BODY, 11.5, BODYC, lead=14)
    arrow(hx, ht + (-26 if t < ht else 26), x + 85, t + (62 if t < ht else 0), color=STEEL, lw=1.2, head=0.1)
qx = M + 450; qw2 = W - M - qx
for i, (q, col, bg) in enumerate([("If rewarding fairness cost nothing in performance, why don't more firms do it?", RUST, RUSTBG),
                                  ("Which task of yours would be cut first in a 20-minute version of your week?", TEAL, TEALBG)]):
    t = 196 + i * 116
    box(qx, t, qw2, 104, fill=bg, stroke=col, r=4)
    txt("QUESTION %d" % (i + 1), qx + 18, t + 14, MONOB, 9, col, track=1.4)
    para(q, qx + 18, t + 38, qw2 - 36, DISP, 15, INK, lead=19)
chrome(">> 30 seconds, then open the floor with Question 1.")

# 10 REFERENCES
ground(); crest()
eyebrow("References", 112, BLUE)
refs = ["Avery, D. R., Hall, A. V., Preston, M., Ruggs, E. N., & Washington, E. (2023). Is justice colorblind? Annual Review of Organizational Psychology and Organizational Behavior, 10, 389–412.",
        "Colquitt, J. A., & Zipay, K. P. (2015). Justice, fairness, and employee reactions. Annual Review of Organizational Psychology and Organizational Behavior, 2, 75–99.",
        "Judge, T. A., & Piccolo, R. F. (2004). Transformational and transactional leadership. Journal of Applied Psychology, 89(5), 755–768.",
        "Kerr, S. (1975). On the folly of rewarding A, while hoping for B. Academy of Management Journal, 18(4), 769–783.",
        "Lin, S.-H., Scott, B. A., & Matta, F. K. (2019). The dark side of transformational leader behaviors for leaders themselves. Academy of Management Journal, 62(5), 1556–1582.",
        "Neal, A., Ballard, T., & Vancouver, J. B. (2017). Dynamic self-regulation and multiple-goal pursuit. Annual Review of Organizational Psychology and Organizational Behavior, 4, 401–423.",
        "Sherf, E. N., Venkataramani, V., & Gajendran, R. S. (2019). Too busy to be fair? Academy of Management Journal, 62(2), 469–502."]
t = 140
for r_ in refs:
    t += para(r_, M, t, W - 2 * M, BODY, 12, BODYC, lead=15.5) + 6
para("AI use (FIU policy): Claude (Anthropic) helped organise the slide structure from my reading notes; "
     "the critique, extension and questions are my own.", M, 452, W - 2 * M, DISPI, 11.5, MUTE, lead=15)
chrome(">> Leave on screen during the discussion.")
d.save(os.path.join(OUT, "MAN7275_Sherf2019_DiscussionLead_Malik.pptx"))

# =================================================================== TOPIC APPROVAL
d, ground, crest, chrome, eyebrow, title, node = make(
    "When the AI Agrees - MAN 7275 Research Topic for Approval",
    "MAN 7275  ·  Research topic for approval  ·  14 November 2026")
box, txt, para, rule, arrow = d.box, d.txt, d.para, d.rule, d.arrow

ground(dark=True); crest(40, light=True)
eyebrow("MAN 7275  ·  Research proposal  ·  Topic for approval", 150, GOLD)
title("When the AI Agrees", 190, size=44, color=WHITE)
title("Workload, rewards and how auditors challenge AI output", 244, size=22, color=DKTXT)
rule(330, color=DKRULE)
txt("YASIR A. MALIK", M, 352, MONOB, 11, GOLD, track=2.0)
txt("Doctor of Business Administration  ·  Cohort 8.14", M, 372, BODY, 13, DKSUB)
txt("Instructor: Dr. Ravi S. Gajendran  ·  14 November 2026", M, 392, BODY, 13, DKSUB)
box(W - M - 300, 150, 300, 258, fill=DKCARD, r=4)
txt("RESEARCH QUESTION", W - M - 276, 176, MONOB, 8.5, GOLD, track=1.4)
para("When an AI tool agrees with a reviewer's first view, does the reviewer challenge the work less, more so "
     "under high workload, and less so when challenge is rewarded?", W - M - 276, 202, 252, DISP, 15, WHITE, lead=20)
rule(348, x=W - M - 276, w=252, color=DKRULE)
para("Firms assume a human reviewer challenges AI output. Under load, agreement may become the default.",
     W - M - 276, 362, 252, DISPI, 12, DKTXT, lead=16)
chrome(">> 20 seconds. Read the question once, slowly.", light=True)

ground(); crest()
eyebrow("Model  ·  anchor, confirm, converge", 112, BLUE)
title("X, mediator, outcome and two moderators", 140, size=27)
nw, ty = 230, 312
xs = [M, (W - nw) / 2, W - M - nw]
node(xs[0], ty, nw, 92, "AI agreement", BLUE, sub="X  ·  with the reviewer's first view")
node(xs[1], ty, nw, 92, "Confirmation", TEAL, sub="M  ·  less independent testing")
node(xs[2], ty, nw, 92, "Convergence on the AI", RUST, sub="Y  ·  not on the evidence")
arrow(xs[0] + nw + 6, ty + 46, xs[1] - 6, ty + 46, color=INK, lw=2, head=7)
arrow(xs[1] + nw + 6, ty + 46, xs[2] - 6, ty + 46, color=INK, lw=2, head=7)
mx = (xs[0] + nw + xs[1]) / 2
box(mx - 230, 206, 210, 46, fill=GOLD, r=5); txt("W1  Workload (+)", mx - 125, 220, DISP, 15, WHITE, align="c")
box(mx + 20, 206, 210, 46, fill=GOLD, r=5); txt("W2  Rewards for challenge (−)", mx + 125, 220, DISP, 15, WHITE, align="c")
arrow(mx - 125, 252, mx - 4, ty + 42, color=GOLD, lw=2, head=7)
arrow(mx + 125, 252, mx + 4, ty + 42, color=GOLD, lw=2, head=7)
para("Theory: anchoring and confirmation (Tversky & Kahneman, 1974; Nickerson, 1998) explain X → M → Y. "
     "Multiple-task pursuit (Neal et al., 2017; Sherf et al., 2019) explains why workload and rewards change X → M.",
     M, 424, W - 2 * M, BODY, 14, BODYC, lead=19)
chrome(">> 1 minute. X, M, Y, then the two gold moderators.\nOpen choice to raise: workload as X or as a moderator.")

ground(); crest()
eyebrow("Design and the question for Dr. Gajendran", 112, BLUE)
title("A one-time survey, sized for the analysis", 140, size=27)
box(M, 196, 250, 230, fill=WHITE, stroke=RULE, r=4)
txt("SAMPLE", M + 18, 212, MONOB, 8.5, MUTE, track=1.4)
txt("100", M + 18, 236, DISP, 34, TEAL); txt("pilot", M + 100, 254, BODY, 13, MUTE)
arrow(M + 40, 290, M + 40, 318, color=GOLD, lw=2, head=6)
txt("300", M + 18, 326, DISP, 34, RUST); txt("full study", M + 100, 344, BODY, 13, MUTE)
para("Auditors and reviewers who use AI tools; individual level.", M + 18, 384, 214, BODY, 12, BODYC, lead=15)
mw = W - 2 * M - 270
box(M + 270, 196, mw, 230, fill=WHITE, stroke=RULE, r=4)
txt("MEASURES TO CONFIRM", M + 288, 212, MONOB, 8.5, MUTE, track=1.4)
for i, (h, s) in enumerate([("Workload", "Janssen (2001), as used by Sherf et al."),
                            ("Rewards for challenge", "adapted from Sherf et al.'s reward scale"),
                            ("Professional skepticism", "Hurtt (2010)"),
                            ("AI agreement", "scale to find or build")]):
    t = 238 + i * 44
    box(M + 288, t + 4, 10, 10, fill=GOLD if i < 3 else RUST, r=5)
    txt(h, M + 308, t, DISP, 15, INK)
    txt(s, M + 308, t + 19, BODY, 12, BODYC)
box(M, 440, W - 2 * M, 50, fill=WARM, stroke=GOLD, r=4)
para("Ask: “Is AI agreement a strong enough focal construct, or should the AI tool be framed as a teammate?”",
     M + 18, 455, W - 2 * M - 36, DISPI, 14.5, INK, lead=18)
chrome(">> 1 minute, then ask the question at the bottom and write down every suggestion.")
d.save(os.path.join(OUT, "MAN7275_Topic_Approval_Malik.pptx"))
print("wrote both decks to", OUT)
