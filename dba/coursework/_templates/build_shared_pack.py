#!/usr/bin/env python3
"""FIU DBA presentation deck — 16:9. Yasir A. Malik, Cohort 8.14.

Institutional identity, not the consulting brand: this is coursework presented
to a professor and a cohort. FIU Blue #081E3F, FIU Gold #B6862C.
Every slide carries a figure. No slide is a list of sentences.
"""
import sys, math
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

W, H = 960, 540
BLUE=HexColor("#081E3F"); GOLD=HexColor("#B6862C"); INK=HexColor("#14171C")
PAPER=HexColor("#FCFBF8"); MUTE=HexColor("#767D86"); RULE=HexColor("#D8D4CB")
SOFT=HexColor("#E8EDF4"); WARM=HexColor("#FAF3E4"); WHITE=HexColor("#FFFFFF")
BODYC=HexColor("#454B54"); TEAL=HexColor("#1C6B63"); RUST=HexColor("#8C3A1B")
STEEL=HexColor("#9AA4AE"); PALE=HexColor("#EFF2F6")
DISP="Times-Bold"; DISPI="Times-Italic"; BODY="Times-Roman"
MONO="Courier"; MONOB="Courier-Bold"
M=54
out=sys.argv[1] if len(sys.argv)>1 else "deck.pdf"
c=canvas.Canvas(out,pagesize=(W,H))
c.setTitle("Internationalization and Performance — GEB 7365 Module 2")
c.setAuthor("Yasir A. Malik · FIU DBA Cohort 8.14")
_n=[0]

def y(v): return H-v
def box(x,t,w,h,fill=None,stroke=None,lw=1,r=None,dash=None):
    c.setDash(dash) if dash else c.setDash()
    if fill: c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke); c.setLineWidth(lw)
    if r: c.roundRect(x,y(t+h),w,h,r,fill=1 if fill else 0,stroke=1 if stroke else 0)
    else: c.rect(x,y(t+h),w,h,fill=1 if fill else 0,stroke=1 if stroke else 0)
    c.setDash()
def txt(s,x,t,font=BODY,size=15,color=INK,align="l",track=0):
    c.setFont(font,size); c.setFillColor(color)
    if track: c._charSpace=track
    if align=="c": c.drawCentredString(x,y(t)-size*0.84,s)
    elif align=="r": c.drawRightString(x,y(t)-size*0.84,s)
    else: c.drawString(x,y(t)-size*0.84,s)
    c._charSpace=0
def para(s,x,t,w,font=BODY,size=15,color=BODYC,lead=None,align="l"):
    lead=lead or size*1.4
    c.setFont(font,size); c.setFillColor(color)
    lines=[]; line=""
    for wd in s.split():
        cand=(line+" "+wd).strip()
        if c.stringWidth(cand,font,size)<=w: line=cand
        else: lines.append(line); line=wd
    if line: lines.append(line)
    yy=y(t)-size*0.84
    for ln in lines:
        if align=="c": c.drawCentredString(x,yy,ln)
        else: c.drawString(x,yy,ln)
        yy-=lead
    return len(lines)*lead
def rule(t,x=M,w=W-2*M,color=RULE,lw=1):
    c.setStrokeColor(color); c.setLineWidth(lw); c.setDash(); c.line(x,y(t),x+w,y(t))
def arrow(x1,t1,x2,t2,color=STEEL,lw=1.4,dash=None,head=5):
    c.setStrokeColor(color); c.setLineWidth(lw)
    c.setDash(dash) if dash else c.setDash()
    c.line(x1,y(t1),x2,y(t2)); c.setDash()
    a=math.atan2(y(t2)-y(t1),x2-x1)
    c.setFillColor(color)
    p=c.beginPath(); p.moveTo(x2,y(t2))
    p.lineTo(x2-head*math.cos(a-0.4),y(t2)-head*math.sin(a-0.4))
    p.lineTo(x2-head*math.cos(a+0.4),y(t2)-head*math.sin(a+0.4)); p.close()
    c.drawPath(p,fill=1,stroke=0)

def crest(t=40, light=False):
    """FIU DBA institutional lockup — not the consulting brand."""
    fg = WHITE if light else BLUE
    sub = HexColor("#8FA3BC") if light else MUTE
    box(M,t-2,3,30,fill=GOLD)
    txt("FLORIDA INTERNATIONAL UNIVERSITY",M+14,t,MONOB,10,fg,track=1.9)
    txt("Chapman Graduate School of Business  ·  Doctor of Business Administration",
        M+14,t+15,BODY,10.5,sub)
def chrome(light=False):
    _n[0]+=1
    fg = HexColor("#7E93A8") if light else MUTE
    rule(H-32,color=HexColor("#1B3252") if light else RULE)
    txt("Yasir A. Malik  ·  Cohort 8.14",M,H-24,MONOB,8.5,fg,track=1.1)
    txt("GEB 7365  ·  Module 2  ·  27 August 2026",W/2,H-24,MONO,8.5,fg,align="c")
    txt(f"{_n[0]}",W-M,H-24,MONOB,8.5,GOLD,align="r")
def ground(dark=False):
    c.setFillColor(BLUE if dark else PAPER); c.rect(0,0,W,H,fill=1,stroke=0)
def eyebrow(s,t,color=GOLD):
    txt(s.upper(),M,t,MONOB,9.5,color,track=2.0)
def title(s,t,size=31,color=INK,w=None):
    return para(s,M,t,w or (W-2*M),DISP,size,color,lead=size*1.14)


# ══════════ COVER ══════════
ground(dark=True); crest(40,light=True)
box(M,150,72,4,fill=GOLD)
eyebrow("For Daniela Garcia Aguirre  ·  shared working pack",184,GOLD)
para("Module 2 — how we split it, and everything behind my half.",M,214,W-2*M-30,DISP,34,WHITE,lead=42)
para("Thursday 27 August, 7:00 PM · Internationalization and Performance · five minutes each",
     M,304,W-2*M,BODY,15,HexColor("#8FA3BC"),lead=20)
box(M,346,W-2*M,84,fill=HexColor("#0C2547"),stroke=HexColor("#1B3252"),r=4)
para("Everything here follows the split you proposed on 23 August. You open with the introduction and your two papers; I follow with mine and take the conclusion. Nothing in my half repeats yours — I reference your two in one line each at the close, and that is all.",
     M+20,362,W-2*M-40,DISPI,14.5,WHITE,lead=19)
txt("PREPARED BY YASIR A. MALIK  ·  COHORT 8.14  ·  26 AUGUST 2026",M,452,MONOB,9,GOLD,track=1.6)
chrome(light=True); c.showPage()

# ══════════ RUNNING ORDER ══════════
ground(); crest()
eyebrow("The ten minutes, minute by minute",104)
title("Running order.",128)

rows=[("0:00","1:00","DANIELA","Introduction — what the module is about",TEAL,True),
      ("1:00","3:00","DANIELA","Arregle et al. (2021) — 220 studies, seven themes",TEAL,True),
      ("3:00","5:00","DANIELA","Ghemawat (2001) — CAGE, Star TV",TEAL,True),
      ("5:00","5:30","HANDOFF","“…over to Yasir”",GOLD,False),
      ("5:30","7:20","YASIR","Contractor, Kundu & Hsu (2003) — the sigmoid",BLUE,True),
      ("7:20","8:30","YASIR","Mezias (2002) — replacing the measure",BLUE,True),
      ("8:30","10:00","YASIR","Conclusion — all four, and the close",BLUE,True)]
t=168
for a,b,who,what,col,solid in rows:
    if solid: box(M,t,3.5,30,fill=col)
    else:
        box(M,t,3.5,30,fill=None,stroke=col,lw=1.4,dash=(2,2))
    txt(f"{a}–{b}",M+14,t+6,MONOB,9.5,MUTE,track=1.0)
    txt(who,M+92,t+6,MONOB,9.5,col,track=1.3)
    txt(what,M+186,t+5,BODY,14,INK if solid else MUTE)
    t+=38

box(M,450,W-2*M,52,fill=SOFT,r=4)
para("If you run long, take it out of my time not yours — tell me on the night and I will cut the Mezias backup numbers. My conclusion is the only part that must survive intact, because it carries all four papers.",
     M+18,462,W-2*M-36,DISPI,14,INK,lead=18)
chrome(); c.showPage()

# ══════════ DEPENDENCIES ══════════
ground(); crest()
eyebrow("What I need from you, and what you can rely on from me",104)
title("Dependencies.",128)

# my half → depends on
box(M,170,(W-2*M-24)/2,196,fill=WHITE,stroke=RULE,r=5)
box(M,170,(W-2*M-24)/2,5,fill=TEAL)
txt("WHAT I NEED FROM YOU",M+20,190,MONOB,9.5,TEAL,track=1.3)
needs=[("Your deck","so our styling does not clash and I know your last slide"),
       ("Your closing line","I will echo it into my opening so the handoff is clean"),
       ("Whether you use Star TV's numbers","$825m paid, ~$500m lost — if you skip them I may use one"),
       ("One 20-min run-through","with a timer, any time before 6:00 PM")]
t=214
for k,v in needs:
    c.setFillColor(TEAL); c.circle(M+26,y(t+6),3,fill=1,stroke=0)
    txt(k,M+38,t,MONOB,9,INK,track=0.9)
    h=para(v,M+38,t+13,(W-2*M-24)/2-58,BODY,12,BODYC,lead=15); t+=h+18

x2=M+(W-2*M-24)/2+24
box(x2,170,(W-2*M-24)/2,196,fill=WHITE,stroke=BLUE,lw=1.5,r=5)
box(x2,170,(W-2*M-24)/2,5,fill=BLUE)
txt("WHAT YOU CAN RELY ON",x2+20,190,MONOB,9.5,BLUE,track=1.3)
gives=[("I will not touch Arregle or Ghemawat","except one line each in the conclusion"),
       ("I take the conclusion","so you do not need a wrap-up — end on your paper"),
       ("My half is timed at 4:30","leaving slack for the handoff"),
       ("Every quote is verified","checked against the PDFs, page numbers on the next page")]
t=214
for k,v in gives:
    c.setFillColor(BLUE); c.circle(x2+26,y(t+6),3,fill=1,stroke=0)
    txt(k,x2+38,t,MONOB,9,INK,track=0.9)
    h=para(v,x2+38,t+13,(W-2*M-24)/2-58,BODY,12,BODYC,lead=15); t+=h+18

box(M,386,W-2*M,50,fill=WARM,stroke=HexColor("#E4D3A8"),r=4)
para("One thing worth flagging: the split is for the presentation only. Bill was explicit that the write-ups are individual and still analyse all four papers.",
     M+18,398,W-2*M-36,DISPI,14.5,INK,lead=19)
txt("→ THE ONE LINE THAT CONNECTS US: EVERY PAPER HERE MADE PROGRESS BY CHANGING WHAT WAS MEASURED.",
    M,456,MONOB,8.5,BLUE,track=1.0)
chrome(); c.showPage()

# ══════════ EVIDENCE BEHIND MY CHARTS ══════════
ground(); crest()
eyebrow("Every figure and quote in my half, with its page",104)
title("The evidence behind the charts.",128)

hdr=["SLIDE","CLAIM ON IT","SOURCE","CHECKED"]
xs=[M, M+80, M+520, M+742]
for i,h in enumerate(hdr): txt(h,xs[i],168,MONOB,8.5,MUTE,track=1.2)
rule(184)
ev=[("2","Sigmoid, three stages; four findings are segments of one curve","Contractor p.7, Fig. 1"),
    ("2","“Depending on which part of Figure 1 we examined…”","Contractor p.7"),
    ("3","Knowledge-based vs capital-intensive; lower fixed capital burden","Contractor p.9"),
    ("3","“Few companies possess the managerial tools…”","Contractor p.11"),
    ("4","486 foreign subsidiaries vs 486 US, same industries and cities","Mezias p.229–231"),
    ("4","“labor lawsuits only measure labor-related disadvantage”","Mezias p.231"),
    ("4","78.9% / 70.0% / 58.4%; award > $600,000; fees ~$100,000","Mezias p.232"),
    ("5","“varied and at times incompatible findings”","Arregle, abstract"),
    ("6","Performance is 12% of the 220 studies","Arregle p.6"),
    ("6","Kundu authored both 2003 and 2021 papers","Both title pages")]
t=196
for n,claim,src in ev:
    txt(n,xs[0]+6,t,MONOB,9.5,BLUE)
    txt(claim,xs[1],t,BODY,12.5,INK)
    txt(src,xs[2],t,BODY,11.5,MUTE)
    txt("EXACT",xs[3],t,MONOB,8,TEAL,track=1.0)
    rule(t+18,color=HexColor("#EFEBE3")); t+=25

box(M,452,W-2*M,40,fill=SOFT,r=4)
para("All ten verified against the source PDFs on 26 August. Nothing on my slides is paraphrased and presented as a quote.",
     M+18,463,W-2*M-36,DISPI,13.5,INK,lead=17)
chrome(); c.showPage()

# ══════════ WHAT I WILL SAY ══════════
ground(); crest()
eyebrow("So you know exactly where I go — and can hand off into it",104)
title("What I will actually say.",128)

say=[("CONTRACTOR","For thirty years this literature reported four different answers — positive, negative, U, inverted-U — all with real data. They say it was one sigmoid curve all along, and the field was sampling different segments of it.",BLUE),
     ("THE PRACTICE LINE","Knowledge-based services drift into the bad third stage more readily than capital-intensive firms. And almost nobody can tell when they have gone too far.",BLUE),
     ("MEZIAS","Everyone agreed liability of foreignness existed and nobody could isolate it. He stopped trying to fix the measure and replaced it — labour lawsuits isolate one disadvantage where performance measures blend everything.",TEAL),
     ("THE CONCLUSION","All four, including yours. Contractor measured segments of a curve. Mezias's field measured aggregate performance and thought it had measured foreignness. Ghemawat's practitioners measured market size and thought they had measured opportunity. Arregle shows it unresolved after 220 studies.",GOLD),
     ("THE CLOSE","Sumit Kundu of FIU is an author on both Contractor 2003 and Arregle 2021. Eighteen years apart, same question, still open — and performance is only 12% of those 220 studies.",RUST)]
t=170
for k,v,col in say:
    box(M,t,3.5,58,fill=col)
    txt(k,M+16,t,MONOB,9.5,col,track=1.3)
    h=para(v,M+16,t+16,W-2*M-30,BODY,13,BODYC,lead=17)
    t+=max(58,h+26)+8

box(M,t+2,W-2*M,46,fill=WARM,stroke=HexColor("#E4D3A8"),r=4)
para("If your framing differs from mine, yours wins — you are opening, and a shared presentation where the halves argue different things reads badly to a room. Tell me and I will change the conclusion.",
     M+18,t+14,W-2*M-36,DISPI,14,INK,lead=18)
chrome(); c.showPage()
c.save()
print("wrote",out,"·",_n[0],"pages")
