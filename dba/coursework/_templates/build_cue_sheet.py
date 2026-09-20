#!/usr/bin/env python3
"""One page. Sixteen cues. The sheet Yasir holds while he talks.

Not a script. A script gets read out loud, and reading out loud is what the
evaluation form marks down. This is the trigger for each slide and nothing
else, laid out so the eye finds slide seven without hunting for it.
Landscape letter so it prints on one sheet.
"""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

W, H = 792, 612
BLUE=HexColor("#081E3F"); GOLD=HexColor("#B6862C"); INK=HexColor("#14171C")
PAPER=HexColor("#FFFFFF"); MUTE=HexColor("#767D86"); RULE=HexColor("#D8D4CB")
SOFT=HexColor("#E8EDF4"); WARM=HexColor("#FAF3E4"); RUST=HexColor("#8C3A1B")
TEAL=HexColor("#1C6B63"); BODYC=HexColor("#3A4048")
DISP="Times-Bold"; DISPI="Times-Italic"; BODY="Times-Roman"
MONO="Courier"; MONOB="Courier-Bold"

out = sys.argv[1] if len(sys.argv) > 1 else "cue.pdf"
c = canvas.Canvas(out, pagesize=(W, H))
c.setTitle("One-page cue sheet - GEB 7365 project presentation")
c.setAuthor("Yasir A. Malik - FIU DBA Cohort 8.14")

def y(v): return H - v
def box(x,t,w,h,fill=None,stroke=None,lw=0.8,r=None):
    if fill: c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke); c.setLineWidth(lw)
    if r: c.roundRect(x,y(t+h),w,h,r,fill=1 if fill else 0,stroke=1 if stroke else 0)
    else: c.rect(x,y(t+h),w,h,fill=1 if fill else 0,stroke=1 if stroke else 0)
def txt(s,x,t,font=BODY,size=9,color=INK,align="l",track=0):
    c.setFont(font,size); c.setFillColor(color)
    if track: c._charSpace=track
    if align=="c": c.drawCentredString(x,y(t)-size*0.84,s)
    elif align=="r": c.drawRightString(x,y(t)-size*0.84,s)
    else: c.drawString(x,y(t)-size*0.84,s)
    c._charSpace=0
def para(s,x,t,w,font=BODY,size=9,color=BODYC,lead=None):
    lead=lead or size*1.25
    c.setFont(font,size); c.setFillColor(color)
    lines=[]; line=""
    for wd in s.split():
        cand=(line+" "+wd).strip()
        if c.stringWidth(cand,font,size)<=w: line=cand
        else: lines.append(line); line=wd
    if line: lines.append(line)
    yy=y(t)-size*0.84
    for ln in lines:
        c.drawString(x,yy,ln); yy-=lead
    return len(lines)*lead

M = 32
c.setFillColor(PAPER); c.rect(0,0,W,H,fill=1,stroke=0)

# ---- header ----
box(0,0,W,58,fill=BLUE)
txt("ONE PAGE  ·  GEB 7365 PROJECT PRESENTATION  ·  REVISED 20 SEPTEMBER 2026",
    M,14,MONOB,8,GOLD,track=1.6)
txt("The average hides the answer. The worst country decides it.",M,28,DISP,19,HexColor("#FFFFFF"))
txt("YASIR A. MALIK  ·  COHORT 8.14",W-M,16,MONOB,7.5,HexColor("#8FA3BC"),track=1.2,align="r")
txt("10 to 15 minutes  ·  opening 10%, body 80%, close 10%",W-M,32,BODY,9.5,
    HexColor("#8FA3BC"),align="r")

# ---- the sixteen cues ----
CUES = [
 (1,"0:00","TITLE","\"I screened 334,976 people.\"  PAUSE TWO SECONDS.  \"I got four.\"","hook",RUST),
 (2,"0:25","THE TOPIC","General population = fieldwork problem. Rare population = arithmetic.","",None),
 (3,"1:10","GAP + QUESTION","Read the question off the slide. Land: parameter, not limitation.","signpost",None),
 (4,"1:50","THE MODEL","Four terms, four levels. THEN SAY THE THREE LEVELS OF ANALYSIS.","say it",RUST),
 (5,"2:50","FIVE HYPOTHESES","Signs, then: H1 is structural, H2 IS THE CONTRIBUTION. Two unsigned.","signs",None),
 (6,"3:40","H1","Spain AND China. A conjunction. Breadth is fragility, not ambition.","",None),
 (7,"4:30","H2 AND H3","320 of 380. A panel is a firm and its product is entirely downstream.","",None),
 (8,"5:40","H4 AND H5","Harzing 47% by phone. Zeng is mine-vs-theirs: say which is which.","",None),
 (9,"6:30","DATA SOURCES","Three levels. Region is a VARIABLE, not a setting. Spell out every acronym.","say it",RUST),
 (10,"7:20","MEASURES","Walk the table. DV, then H2 to H5, then controls. Do not wave.","scored",None),
 (11,"8:10","METHOD","Analytic vs inferential. No p-value on H1, and say why not.","",None),
 (12,"8:55","TIMEFRAME","Nine months. Notice what is missing: there is no recruitment step.","signpost",None),
 (13,"9:25","PRELIM ANALYSIS","ASK THE ROOM: who has read a paper with one overall response rate?","ask",RUST),
 (14,"10:40","MY EVIDENCE","334,976 to 20 to 4. Then say what it CANNOT do. H1 yes, H2 no, H4 weak.","slow",RUST),
 (15,"11:40","LIMITS","\"I would rather state the limits than be handed them.\" Four of them.","",None),
 (16,"12:20","CLOSE","Parameter before. Limitation after. Then STOP. \"Thank you. Questions.\"","stop",RUST),
]
COLS = 2
CW = (W - 2*M - 16) / COLS
top = 76
rh = 34
for i,(n,tm,head,line,tag,accent) in enumerate(CUES):
    col = i // 8
    row = i % 8
    x = M + col*(CW+16)
    t = top + row*(rh+4)
    fill = WARM if accent else HexColor("#F7F8FA")
    box(x,t,CW,rh,fill=fill,r=2)
    box(x,t,3,rh,fill=accent or BLUE)
    txt(str(n),x+12,t+7,MONOB,10,accent or BLUE)
    txt(tm,x+12,t+21,MONO,7,MUTE)
    txt(head,x+42,t+7,MONOB,7.5,accent or BLUE,track=1.1)
    txt(line,x+42,t+20,BODY,9.2,INK)
    if tag:
        txt(tag.upper(),x+CW-8,t+7,MONOB,6.5,accent or TEAL,track=1.0,align="r")

# ---- bottom strip ----
bt = top + 8*(rh+4) + 10
box(M,bt,W-2*M,1,fill=RULE)
bt += 10

colw = (W-2*M-24)/3
txt("THE FOUR PHRASES",M,bt,MONOB,7.5,BLUE,track=1.4)
ph = ["Parameter before a design. Limitation after it fails.",
      "A comparison is a conjunction, not an average.",
      "Priced by the weakest frame, not the average one.",
      "A panel's whole product is a downstream asset."]
tt = bt+14
for p in ph:
    txt("·  "+p,M,tt,BODY,9,BODYC); tt += 11

x2 = M+colw+12
txt("THE NUMBERS, IN ORDER",x2,bt,MONOB,7.5,BLUE,track=1.4)
nums = ["334,976 screened  ·  20 eligible  ·  4 usable",
        "6 per hundred thousand",
        "320 of 380 home-region  ·  80.3% of sales  ·  9 global",
        "18.8M to 72.2M panel  ·  mean only 15.4 to 9.2%"]
tt = bt+14
for p in nums:
    txt("·  "+p,x2,tt,BODY,9,BODYC); tt += 11

x3 = M+2*(colw+12)
txt("DO NOT",x3,bt,MONOB,7.5,RUST,track=1.4)
dn = ["Read the slides.",
      "Apologise for being nervous.",
      "Rush the numbers. Pause after 334,976.",
      "Trail off. End on the sentence, then stop.",
      "Use an acronym you have not spelled out."]
tt = bt+14
for p in dn:
    txt("·  "+p,x3,tt,BODY,9,BODYC); tt += 11

# ---- the three that hurt ----
qb = bt + 80
box(M,qb-8,W-2*M,1,fill=RULE)
txt("THE THREE THAT HURT, AND THE ANSWER",M,qb,MONOB,7.5,RUST,track=1.4)
hard = [("\"You failed to collect data. Why trust a design from you?\"",
         "Because the failure is the finding. I had a complete protocol and nothing to run it on, "
         "and the reason was visible before I fielded. This project exists so the next person sees it too."),
        ("\"Isn't this just a methods paper?\"",
         "The dependent variable is cross-national. Which countries can be reached, and why coverage "
         "differs. H2 is what makes it international business."),
        ("\"Is the triad the right way to cut region?\"",
         "That is what I am least sure about. Fainshmidt's seven institutional types may predict "
         "coverage better. I would rather raise the doubt than quietly revise after the deadline.")]
qw = (W-2*M-24)/3
for i,(q,a) in enumerate(hard):
    qx = M + i*(qw+12)
    box(qx,qb+14,qw,70,fill=HexColor("#FBEFE9"),r=3)
    n = para(q,qx+10,qb+24,qw-20,DISP,8.5,RUST,lead=11)
    para(a,qx+10,qb+26+n,qw-20,BODY,8.3,BODYC,lead=10.5)

# ---- footer ----
box(M,H-46,W-2*M,1,fill=RULE)
txt("If a question goes somewhere you have not been: \"That is the part I am least sure about\" "
    "is a real answer, and it scores better than a guess.",
    M,H-36,DISPI,9.5,INK)
txt("Full script in the notes pane of Malik_GEB7365_ProjectPresentation_19SEP.pptx  ·  "
    "FAQ in SPEAK_AND_FAQ_19SEP.md",M,H-22,MONO,7,MUTE)

c.save()
print("wrote",out)
