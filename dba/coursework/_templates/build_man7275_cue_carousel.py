#!/usr/bin/env python3
"""Phone cue carousel for the MAN 7275 Sherf discussion lead — 9:16, 1080 x 1920.
Yasir A. Malik, FIU DBA Cohort 8.14. One card per slide: the one line to say, big enough to read
at arm's length, plus a small cue. Open the PDF on the phone and swipe.

House palette for coursework: FIU Blue #081E3F, FIU Gold #B6862C, Times.
Usage: python3 build_man7275_cue_carousel.py <out.pdf>
"""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

W, H = 1080, 1920
BLUE = HexColor("#081E3F"); GOLD = HexColor("#B6862C"); PAPER = HexColor("#FCFBF8")
INK = HexColor("#14171C"); MUTE = HexColor("#767D86"); DKTXT = HexColor("#B9C7D8")
TEAL = HexColor("#1C6B63"); RUST = HexColor("#8C3A1B")
DISP, DISPI, BODY, MONOB = "Times-Bold", "Times-Italic", "Times-Roman", "Courier-Bold"
M = 90
SEAL = "/home/user/Profile/assets/images/fiu-seal.png"
out = sys.argv[1] if len(sys.argv) > 1 else "cue_carousel.pdf"
c = canvas.Canvas(out, pagesize=(W, H))
c.setTitle("Sherf et al. (2019) - phone cue cards")
c.setAuthor("Yasir A. Malik")


def y(v): return H - v


def para(s, x, t, w, font, size, color, lead=None):
    lead = lead or size * 1.22
    c.setFont(font, size); c.setFillColor(color)
    lines, line = [], ""
    for wd in s.split():
        cand = (line + " " + wd).strip()
        if c.stringWidth(cand, font, size) <= w: line = cand
        else: lines.append(line); line = wd
    if line: lines.append(line)
    yy = y(t) - size * 0.84
    for ln in lines:
        c.drawString(x, yy, ln); yy -= lead
    return len(lines) * lead


CARDS = [
    ("1", "Title", "0:20", "This paper says unfairness comes from the job, not just the manager.", "Say the paper's name, then this line."),
    ("2", "The question", "0:45", "Busy managers drop fairness first.", "Earlier work blamed traits. This paper says workload and rewards."),
    ("3", "Theory", "2:00", "More work → technical tasks first → less fairness. Unless fairness is rewarded.", "Point: navy box, teal box, red box, then the gold box. Slow down."),
    ("4", "Method", "0:45", "Three studies: a diary, a field survey, a lab experiment.", "Point at the gold row: who rated fairness."),
    ("5", "Findings", "0:45", "Reward fairness and it stays, with no loss in performance.", "Point at the two lines: red climbs, teal stays flat."),
    ("6", "Authors' advice", "0:30", "Manage workload. Reward fairness. Protect time.", "Three circles, left to right."),
    ("7", "My critique", "1:45", "My main question: who rated the fairness?", "Ask, don't accuse. He co-wrote the paper."),
    ("8", "My research", "1:00", "In audits, an AI that agrees makes skipping review easier.", "Same shape as Sherf's model."),
    ("9", "Questions", "0:30", "Why don't more firms reward fairness?", "Ask it, then stop talking and let the room answer."),
    ("10", "References", "—", "Leave it on screen.", "Say nothing. Take questions."),
]

# cover
c.setFillColor(BLUE); c.rect(0, 0, W, H, fill=1, stroke=0)
try: c.drawImage(SEAL, M, y(200), width=110, height=110, mask="auto")
except Exception: pass
c.setFont(MONOB, 26); c.setFillColor(GOLD); c.drawString(M, y(300), "MAN 7275  ·  SAT 14 NOV  ·  MANGO 220")
para("Too Busy to Be Fair?", M, 380, W - 2 * M, DISP, 96, HexColor("#FFFFFF"))
para("Your 10 lines. One per slide. Swipe as you click.", M, 640, W - 2 * M, DISPI, 50, DKTXT)
para("7–8 minutes. Slow down on slide 3. Ask, don't accuse on slide 7.", M, 860, W - 2 * M, BODY, 42, DKTXT)
c.setFont(MONOB, 26); c.setFillColor(GOLD); c.drawString(M, y(H - 120), "SWIPE →")
c.showPage()

for num, name, t, line, cue in CARDS:
    c.setFillColor(PAPER); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(BLUE); c.rect(0, y(260), W, 260, fill=1, stroke=0)
    c.setFont(DISP, 150); c.setFillColor(GOLD); c.drawString(M, y(200), num)
    c.setFont(MONOB, 34); c.setFillColor(HexColor("#FFFFFF"))
    c.drawString(M + c.stringWidth(num, DISP, 150) + 40, y(120), name.upper())
    c.setFont(MONOB, 30); c.setFillColor(DKTXT)
    c.drawString(M + c.stringWidth(num, DISP, 150) + 40, y(175), "TIME " + t)
    c.setFont(MONOB, 28); c.setFillColor(MUTE); c.drawString(M, y(370), "SAY")
    h = para(line, M, 420, W - 2 * M, DISP, 78, INK, lead=94)
    c.setStrokeColor(GOLD); c.setLineWidth(4); c.line(M, y(470 + h), M + 160, y(470 + h))
    c.setFont(MONOB, 28); c.setFillColor(MUTE); c.drawString(M, y(530 + h), "DO")
    para(cue, M, 580 + h, W - 2 * M, DISPI, 48, TEAL if num != "7" else RUST, lead=60)
    c.setFont(MONOB, 24); c.setFillColor(MUTE)
    c.drawString(M, y(H - 80), "Yasir A. Malik  ·  Sherf et al. (2019)")
    c.drawRightString(W - M, y(H - 80), f"{num} / 10")
    c.showPage()

c.save()
print("wrote", out)
