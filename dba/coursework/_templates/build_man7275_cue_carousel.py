#!/usr/bin/env python3
"""Phone speaker notes for the MAN 7275 Sherf discussion lead — 9:16, 1080 x 1920.
Yasir A. Malik, FIU DBA Cohort 8.14. One card per slide (continued onto a second card when long):
the headline to say, then the talking points with the paper's numbers. Swipe on the phone.

House palette for coursework: FIU Blue #081E3F, FIU Gold #B6862C, Times.
Every number was read in the paper (see ../MAN7275_Organizational_Behavior/LEAD_Sherf_2019_PREP.md).
Usage: python3 build_man7275_cue_carousel.py <out.pdf>
"""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

W, H = 1080, 1920
BLUE = HexColor("#081E3F"); GOLD = HexColor("#B6862C"); PAPER = HexColor("#FCFBF8")
INK = HexColor("#14171C"); MUTE = HexColor("#767D86"); DKTXT = HexColor("#B9C7D8")
TEAL = HexColor("#1C6B63"); RUST = HexColor("#8C3A1B"); BODYC = HexColor("#2E333A")
DISP, DISPI, BODY, MONOB = "Times-Bold", "Times-Italic", "Times-Roman", "Courier-Bold"
M = 80
SEAL = "/home/user/Profile/assets/images/fiu-seal.png"
out = sys.argv[1] if len(sys.argv) > 1 else "cue_carousel.pdf"
c = canvas.Canvas(out, pagesize=(W, H))
c.setTitle("Sherf et al. (2019) - phone speaker notes")
c.setAuthor("Yasir A. Malik")
BOTTOM = H - 140


def y(v): return H - v


def lines_of(s, w, font, size):
    out_, line = [], ""
    for wd in s.split():
        cand = (line + " " + wd).strip()
        if c.stringWidth(cand, font, size) <= w: line = cand
        else: out_.append(line); line = wd
    if line: out_.append(line)
    return out_


def draw_lines(ls, x, t, font, size, color, lead):
    c.setFont(font, size); c.setFillColor(color)
    yy = y(t) - size * 0.84
    for ln in ls:
        c.drawString(x, yy, ln); yy -= lead
    return len(ls) * lead


SLIDES = [
 ("1", "Title", "0:20",
  "This paper says unfairness comes from the job, not just the manager.",
  ["Sherf, Venkataramani & Gajendran, Academy of Management Journal, 2019.",
   "Three studies, one model: a two-week diary study, a field survey and a lab experiment.",
   "The puzzle: managers know fairness pays off, yet they still act unfairly. Why?"]),
 ("2", "The question", "0:45",
  "Busy managers drop fairness first.",
  ["Earlier work is actor-centric: unfairness comes from the manager's traits, empathy and motives.",
   "This paper is context-centric: workload and what the organisation rewards.",
   "Contribution: fairness is one task competing with others for time and effort.",
   "Their line: putting the onus entirely on managers “might, ironically, be unfair.”"]),
 ("3", "Theory and model", "2:00",
  "More work → technical tasks first → less fairness. Unless fairness is rewarded.",
  ["Theory: multiple-task pursuit (Neal et al., 2017). Under scarce time, effort goes to the task that looks most important and most rewarded.",
   "Why technical tasks win: clear metrics (sales, productivity), more feedback from above, and Kerr (1975): we reward A while hoping for B.",
   "H1: workload → prioritising technical tasks → lower justice rule adherence.",
   "H2: rewards for justice weaken workload → prioritising.",
   "H3: so the whole indirect effect is weaker when justice is rewarded.",
   "Justice = all four rules (distributive, procedural, interpersonal, informational), treated as one construct.",
   "A pilot study (Appendix A) built the reward and prioritisation scales."]),
 ("4", "Method", "0:45",
  "Three studies: a diary, a field survey, a lab experiment.",
  ["Study 1: 107 U.S. managers on MTurk, two weeks, two surveys a day: 862 day-level records. Justice is self-rated.",
   "Study 2: 166 manager trios in India. One employee rated the manager's justice, another rated technical performance.",
   "Study 3: 239 students in an inbox simulation. Workload = 20 vs 30 minutes. Rewards = scorecard 70/20/10 vs 45/45/10. Blind coders scored the justice message.",
   "Fun fact: Study 3's scenario sends you off to a week-long residential leadership training. Like today."]),
 ("5", "Findings", "0:45",
  "Reward fairness and it stays, with no loss in performance.",
  ["Study 1: workload → prioritising, γ = .13. With low rewards the slope is .21; with high rewards .05, not significant.",
   "Prioritising → justice adherence, γ = −.16.",
   "Study 2 replicates the interaction (B = −.09, p = .03). Prioritising does not hurt technical performance (B = −.04, n.s.).",
   "Study 3 (causal): interaction F = 4.14, p = .04. Justice is lowest under high workload + low rewards.",
   "Rewards changed justice, not technical performance: the trade-off “is not always zero-sum.”"]),
 ("6", "Authors' advice", "0:30",
  "Manage workload. Reward fairness. Protect time.",
  ["Workload: job design, flexibility, job crafting (they cite Gajendran et al., 2015).",
   "Rewards: put fair treatment into evaluations and 360-degree feedback. Example: Google evaluating managers on explaining decisions.",
   "Time: pre-commit to meetings, town halls, walking around.",
   "They do not say fairness should always beat technical work. Context decides.",
   "Their limits: same-time measures (S1), cross-sectional (S2), students (S3), no top-management ratings."]),
 ("7", "My critique", "1:45",
  "My main question: who rated the fairness?",
  ["1. Who rated? S1 managers rated themselves; in S2 managers chose the raters; in S3 prioritising was self-reported afterwards. Ties to my 5 Nov point: ratings are weak evidence.",
   "2. Is the moderator robust? In S2 the interaction was not significant without controls (B = −.04, p = .44). The authors report it openly (Becker, 2005).",
   "3. How big? Study 3 interaction η²p = .02: meaningful daily drift, or fragile?",
   "4. Is explaining protected? Informational justice was not significant in S2 (footnote 7), yet S3's task was mostly an explanation.",
   "Ask, don't accuse. He co-wrote the paper."]),
 ("8", "My research", "1:00",
  "In audits, an AI that agrees makes skipping review easier.",
  ["The manager's challenge (“How do you know? What else could explain this?”) is the justice-like task: effortful, rarely measured, first to go under load.",
   "An AI summary that agrees makes skipping it cheaper: the AI anchors, the busy reviewer confirms, judgments converge on the tool.",
   "Same shape as Sherf: workload → accepting the AI → less challenge; rewards for challenge as the moderator.",
   "Test: a survey of reviewers who use AI tools, later a Study 3-style experiment."]),
 ("9", "Questions", "0:30",
  "Why don't more firms reward fairness?",
  ["Links: Judge & Piccolo (contingent reward), Lin, Scott & Matta (good leadership costs resources), Colquitt & Zipay (rules vs. fairness), Avery et al. (uneven rewards, uneven fairness).",
   "Dr. Buckman's point: contribution comes from moderators that change a known effect. Rewards for justice is exactly that.",
   "Backup question: “Which task of yours would be cut first in a 20-minute version of your week?”",
   "Ask, then stop talking and let the room answer."]),
 ("10", "If he asks", "Q&A",
  "Short answers. You know this paper.",
  ["Why does S2's interaction drop without controls? A varied sample adds omitted differences; the controls expose the moderator. They reported both.",
   "Is self-report fatal? No: S2 used employee ratings, S3 blind coders. My point is the moderator and prioritising stay self-reported.",
   "Informational justice? “I don't know. How do you read it?”",
   "Always reward justice? The authors say context decides; the 45/45 scorecard is one model."]),
]

# cover
c.setFillColor(BLUE); c.rect(0, 0, W, H, fill=1, stroke=0)
c.drawImage(SEAL, M, y(200), width=110, height=110, mask="auto")
c.setFont(MONOB, 26); c.setFillColor(GOLD); c.drawString(M, y(300), "MAN 7275  ·  SAT 14 NOV  ·  MANGO 220")
draw_lines(lines_of("Too Busy to Be Fair?", W - 2 * M, DISP, 96), M, 380, DISP, 96, HexColor("#FFFFFF"), 110)
draw_lines(lines_of("Your speaker notes. One card per slide. Swipe as you click.", W - 2 * M, DISPI, 50),
           M, 640, DISPI, 50, DKTXT, 62)
draw_lines(lines_of("Big line = what to say. Points = what to add. Slow down on slide 3. Ask, don't accuse on slide 7.",
                    W - 2 * M, BODY, 42), M, 860, BODY, 42, DKTXT, 54)
c.setFont(MONOB, 26); c.setFillColor(GOLD); c.drawString(M, y(H - 120), "SWIPE →")
c.showPage()


def header(num, name, t, cont=False):
    c.setFillColor(PAPER); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(BLUE); c.rect(0, y(230), W, 230, fill=1, stroke=0)
    c.setFont(DISP, 140); c.setFillColor(GOLD); c.drawString(M, y(185), num)
    x = M + c.stringWidth(num, DISP, 140) + 40
    c.setFont(MONOB, 34); c.setFillColor(HexColor("#FFFFFF")); c.drawString(x, y(110), (name + (" (cont.)" if cont else "")).upper())
    c.setFont(MONOB, 30); c.setFillColor(DKTXT); c.drawString(x, y(160), "TIME " + t)


def footer(num):
    c.setFont(MONOB, 24); c.setFillColor(MUTE)
    c.drawString(M, y(H - 70), "Yasir A. Malik  ·  Sherf et al. (2019)")
    c.drawRightString(W - M, y(H - 70), f"{num} / 10")
    c.showPage()


PT, PL = 40, 50          # point size and leading
for num, name, t, say, points in SLIDES:
    header(num, name, t)
    c.setFont(MONOB, 26); c.setFillColor(MUTE); c.drawString(M, y(300), "SAY")
    top = 340
    top += draw_lines(lines_of(say, W - 2 * M, DISP, 64), M, top, DISP, 64, INK, 76)
    c.setStrokeColor(GOLD); c.setLineWidth(4); c.line(M, y(top + 30), M + 160, y(top + 30))
    c.setFont(MONOB, 26); c.setFillColor(MUTE); c.drawString(M, y(top + 70), "POINTS")
    top += 110
    for p in points:
        ls = lines_of(p, W - 2 * M - 40, BODY, PT)
        need = len(ls) * PL + 26
        if top + need > BOTTOM:
            footer(num); header(num, name, t, cont=True); top = 300
        c.setFillColor(RUST if num == "7" else TEAL); c.circle(M + 10, y(top + 22), 8, fill=1, stroke=0)
        draw_lines(ls, M + 40, top, BODY, PT, BODYC, PL)
        top += need
    footer(num)

c.save()
print("wrote", out)
