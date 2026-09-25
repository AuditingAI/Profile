#!/usr/bin/env python3
"""GEB 7911 Week 5 deck: the three readings compared — 16:9. Yasir A. Malik, Cohort 8.14.

Built to Newburry Session 4, slide 14: five elements, 10 to 15 minutes,
content emphasised over presentation style. Name on every slide.
Emailed to Newburry by midnight Friday 18 September; no changes after.

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
c.setTitle("Three Qualitative Studies Compared - GEB 7911 Week 5")
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

SEAL="/home/user/Profile/assets/images/fiu-seal.png"
def crest(t=40, light=False):
    """FIU institutional lockup — official seal plus the school line."""
    fg = WHITE if light else BLUE
    sub = HexColor("#8FA3BC") if light else MUTE
    try:
        c.drawImage(SEAL, M, y(t+34), width=34, height=34,
                    mask='auto', preserveAspectRatio=True)
        ox = M+46
    except Exception:
        box(M,t-2,3,30,fill=GOLD); ox = M+14
    txt("FLORIDA INTERNATIONAL UNIVERSITY",ox,t,MONOB,10,fg,track=1.9)
    txt("Chapman Graduate School of Business  ·  Doctor of Business Administration",
        ox,t+15,BODY,10.5,sub)
def chrome(light=False):
    _n[0]+=1
    fg = HexColor("#7E93A8") if light else MUTE
    rule(H-32,color=HexColor("#1B3252") if light else RULE)
    txt("Yasir A. Malik  ·  Cohort 8.14",M,H-24,MONOB,8.5,fg,track=1.1)
    txt("GEB 7911  ·  Week 5  ·  Qualitative Research Methods",W/2,H-24,MONO,8.5,fg,align="c")
    txt(f"{_n[0]}",W-M,H-24,MONOB,8.5,GOLD,align="r")
def ground(dark=False):
    c.setFillColor(BLUE if dark else PAPER); c.rect(0,0,W,H,fill=1,stroke=0)
def eyebrow(s,t,color=GOLD):
    txt(s.upper(),M,t,MONOB,9.5,color,track=2.0)
def title(s,t,size=31,color=INK,w=None):
    return para(s,M,t,w or (W-2*M),DISP,size,color,lead=size*1.14)

FIGD="/home/user/Profile/dba/coursework/GEB7911_Qualitative_Research_Methods/figures/"
def figslide(png, eyebrow_txt, title_txt, note):
    ground(); crest(); eyebrow(eyebrow_txt,112,BLUE); title(title_txt,140,size=27)
    try:
        from PIL import Image as _I
        iw,ih=_I.open(FIGD+png).size
        w=W-2*M; h=w*ih/iw
        if h>232: h=232; w=h*iw/ih
        c.drawImage(FIGD+png,(W-w)/2,y(200+h),width=w,height=h,mask='auto',preserveAspectRatio=True)
        bot=200+h
    except Exception:
        box(M,200,W-2*M,250,fill=PALE,stroke=RULE,r=4); bot=450
    para(note,M,bot+22,W-2*M,DISPI,14,INK,lead=19)
    chrome(); c.showPage()

# 1 TITLE
ground(dark=True); crest(40,light=True)
eyebrow("GEB 7911  ·  Week 5  ·  Data analysis in three traditions",150,GOLD)
title("Three Studies, One Spiral",190,size=44,color=WHITE)
title("How Gerlach, Cha and Dane each worked",244,size=24,color=HexColor("#B9C7D8"))
title("Creswell and Poth's five analysis activities",274,size=24,color=HexColor("#B9C7D8"))
rule(330,color=HexColor("#1B3252"))
txt("YASIR A. MALIK",M,352,MONOB,11,GOLD,track=2.0)
txt("Doctor of Business Administration  ·  Cohort 8.14",M,372,BODY,13,HexColor("#8FA3BC"))
txt("Instructor: Dr. Cristina Gonzalez  ·  18 September 2026",M,392,BODY,13,HexColor("#8FA3BC"))
box(W-M-300,150,300,258,fill=HexColor("#0E2949"),r=4)
txt("THE CLAIM OF THIS DECK",W-M-276,176,MONOB,8.5,GOLD,track=1.4)
para("All three papers are arguments against knowing the answer before you collect the data. "
     "They make that argument three different ways, and the differences are where the method lives.",
     W-M-276,202,252,BODY,13,HexColor("#B9C7D8"),lead=18)
rule(330,x=W-M-276,w=252,color=HexColor("#1B3252"))
para("Read in full, 18 September. Every figure that follows is built from numbers reported in the papers.",
     W-M-276,348,252,DISPI,12,HexColor("#8FA3BC"),lead=16)
chrome(light=True); c.showPage()

# 2 AT A GLANCE
ground(); crest()
eyebrow("The three papers",112,BLUE)
title("What each one was trying to do",140,size=27)
rows=[("Gerlach & Cenfetelli (2020)","MIS Quarterly","Grounded theory, Glaser",
       "The field's category was BORROWED. Addiction was applied, in their words, in a confirmatory manner",BLUE),
      ("Cha & Edmondson (2006)","Leadership Quarterly","Longitudinal single case",
       "Their OWN category was wrong. They went in to study the positive effects of strong values",TEAL),
      ("Dane (2020)","Acad. Mgmt Discoveries","Modified GT, Corbin & Strauss + Gioia",
       "NO category existed. Nobody had a vocabulary for how people make sense of an epiphany",RUST)]
tt=188
for name,venue,trad,claim,col in rows:
    box(M,tt,W-2*M,88,fill=WHITE,stroke=RULE,r=4)
    box(M,tt,5,88,fill=col)
    txt(name,M+22,tt+18,DISP,17,INK)
    txt(venue+"   ·   "+trad,M+22,tt+42,MONOB,8.5,col,track=1.2)
    para(claim,M+22,tt+58,W-2*M-44,BODY,12.5,BODYC,lead=16)
    tt+=96
txt("ALL THREE ARE INDUCTIVE. NONE STARTED FROM A HYPOTHESIS.",M,H-56,MONOB,8,MUTE,track=1.4)
chrome(); c.showPage()

# 3-5 FIGURES
figslide("w5_fig1_evidence.png","Design shape","Sample size is not the same thing as evidence",
 "Gerlach reached the most people. Cha and Edmondson reached the fewest and learned the most from them, "
 "because they went back three years later. Dane reports no hours at all, which is itself worth noticing.")
figslide("w5_fig2_funnel.png","Prevalence","The same funnel, two orders of magnitude apart",
 "Dane screened 128 people to interview 22. My qualifying study screened 334,976 to keep four. The shape "
 "is identical. What differs is prevalence, and prevalence is not something effort can fix.")
figslide("w5_fig3_distance.png","Evidentiary strategy","How far the measurement sits from the thing itself",
 "This is the question my own design has to answer. Dane's participants recall an epiphany from up to "
 "twenty-nine years ago, and epiphanies are vivid. Mine would recall four seconds nobody marked at the time.")

# 6 THREE LADDERS
ground(); crest()
eyebrow("Ring 3  ·  describing and classifying",112,BLUE)
title("Three ladders, all called inductive",140,size=27)
lad=[("GERLACH","Glaser (1978)",["Open coding","line by line, phrase level","↓","Selective coding","one construct earns the centre","↓","Theoretical coding","relationships, validated"],BLUE),
     ("CHA & EDMONDSON","Emic, inductive",["Observation","across two phases","↓","Interview","36 in phase 2 alone","↓","Archival","the record around it"],TEAL),
     ("DANE","Gioia et al. (2013)",["First-order data","participants' own terms","↓","Theoretical categories","named by the analyst","↓","Aggregate dimensions","four of them"],RUST)]
cw=(W-2*M-2*20)/3
for i,(who,trad,steps,col) in enumerate(lad):
    x=M+i*(cw+20)
    box(x,190,cw,268,fill=WHITE,stroke=col,lw=1.4,r=4); box(x,190,cw,5,fill=col)
    txt(who,x+16,212,MONOB,10,col,track=1.5)
    txt(trad,x+16,230,BODY,12,MUTE)
    yy=256
    for stp in steps:
        if stp=="↓":
            txt("↓",x+cw/2,yy,BODY,13,STEEL,align="c"); yy+=18
        elif stp[0].isupper() and len(stp)<30 and not stp[0].islower():
            txt(stp,x+16,yy,DISP,13.5,INK); yy+=17
        else:
            para(stp,x+16,yy,cw-32,DISPI,11.5,MUTE,lead=14); yy+=17
    chrome_note=None
para("Constant comparison is the engine under the first. A three-year gap is the engine under the second. "
     "Iterating between collection and analysis is the engine under the third.",
     M,472,W-2*M,DISPI,13.5,INK,lead=18)
chrome(); c.showPage()

# 7 RING 4
ground(); crest()
eyebrow("Ring 4  ·  developing and assessing interpretations",112,RUST)
title("Where the three actually separate",140,size=27)
para("Every paper describes how it built an interpretation. Only some describe how they tried to break one.",
     M,190,W-2*M,BODY,14.5,BODYC,lead=20)
a=[("GERLACH","Designed disconfirmation IN, before fielding",
    "Ran anonymous surveys specifically to test for interview bias, and an MTurk sample specifically to test "
    "the convenience sample. Both reported no difference.","...and no threshold was stated for what a "
    "difference would have been. A check that can only return the expected answer is weaker than it looks.",BLUE),
   ("CHA & EDMONDSON","Had their interpretation overturned, and followed it",
    "Went in to document the positive effects of strong values. Developed theory about negative outcomes, in "
    "their words, after we observed them.","The strongest instance of assessment in the three, and it was not "
    "a procedure. It was a willingness to lose the original question.",TEAL),
   ("DANE","Worked alone",
    "Single author, first person throughout: I read each interview transcript multiple times. Four aggregate "
    "dimensions identified.","No inter-coder statistic, and no external check reported. Defensible, and it "
    "should be argued rather than left silent.",RUST)]
tt=232
for who,head,body,crit,col in a:
    box(M,tt,W-2*M,74,fill=WHITE,stroke=RULE,r=3); box(M,tt,4,74,fill=col)
    txt(who,M+20,tt+13,MONOB,9,col,track=1.5)
    txt(head,M+118,tt+12,DISP,14,INK)
    para(body,M+118,tt+32,(W-2*M-140)*0.52,BODY,11.5,BODYC,lead=14)
    para(crit,M+118+(W-2*M-140)*0.55,tt+32,(W-2*M-140)*0.45,DISPI,11.5,RUST,lead=14)
    tt+=82
txt("NOBODY REPORTS INTER-CODER AGREEMENT. THREE DIFFERENT DEFENCES, ALL UNSTATED.",M,H-56,MONOB,8,MUTE,track=1.3)
chrome(); c.showPage()

# ACTIVITY A · ring 1
COLW=(W-2*M-36)/2
ground(); crest()
eyebrow("Hands-on activity  ·  ring 1",112,RUST)
title("We had a data problem before we had data",140,size=27)
para("The artifacts were collected onto loose sheets. Before any coding was possible, the record had "
     "to survive being read by someone who was not in the room.",
     M,190,W-2*M,BODY,14.5,BODYC,lead=20)
box(M,254,COLW,196,fill=WHITE,stroke=RUST,lw=1.4,r=4); box(M,254,COLW,5,fill=RUST)
txt("WHAT THE SHEETS ACTUALLY SAID",M+18,278,MONOB,9,RUST,track=1.5)
for i,ln in enumerate(["One sheet numbered 1 to 6",
                       "Another began at \u201cItem 10\u201d",
                       "A third began at \u201cItem 3\u201d",
                       "The back of one restarted at 1, 2, 3",
                       "Some items carried an owner. Some did not"]):
    txt("\u00b7  "+ln,M+18,302+i*26,BODY,13,BODYC)
box(M+COLW+36,254,COLW,196,fill=WARM,stroke=GOLD,r=4); box(M+COLW+36,254,COLW,5,fill=GOLD)
txt("WHY THAT IS NOT HOUSEKEEPING",M+COLW+54,278,MONOB,9,HexColor("#8A6A1F"),track=1.5)
para("\u201ciPad\u201d appears on two sheets. Nothing in the record tells us whether that is two iPads or "
     "one iPad written down twice. Every count downstream inherits that.",
     M+COLW+54,302,COLW-36,BODY,13,BODYC,lead=17)
para("The fix is one row per object with an owner ID attached: P01-01 Yasir, Beats headphones.",
     M+COLW+54,392,COLW-36,DISPI,12.5,INK,lead=16)
box(M,458,W-2*M,46,fill=SOFT,r=4)
para("Ring 1 is not filing. Get it wrong and rings 3 and 4 inherit the error without knowing it.",
     M+20,470,W-2*M-40,DISPI,13.5,INK,lead=17)
chrome(); c.showPage()

figslide("w5_fig5_ladder.png","Hands-on activity  ·  ring 3","Our data structure, in Gerlach's format",
 "Seven objects, four categories, three themes, in twenty minutes. Nobody was asked for a brand and every "
 "qualifier was volunteered, which is precisely what makes the left column in vivo rather than ours.")

figslide("w5_fig4_quadrant.png","Hands-on activity  ·  rings 4 and 5","What the artifacts turned out to be for",
 "A third of the objects produce nothing at all. The phone and the iPad could not be placed, because they "
 "enable the work and interrupt it, and we had no category for that. The unplaceable case is the finding.")

# 8 FOR MY STUDY
ground(); crest()
eyebrow("What this changes for my proposal",112,GOLD)
title("Four things I take from reading all three",140,size=27)
t=[("1","Ring 4 is where my protocol is thinnest","Member checking and an audit trail are Gerlach's family of answer. I should say so, rather than leaving them as generic trustworthiness language.",BLUE),
   ("2","Ring 5 is a real gap","All three papers end in a figure. Phenomenology ends in prose. I have not decided what a reader actually sees.",TEAL),
   ("3","My phenomenon is a non-event","Dane's problem is that memory is long. Mine is that the event is small. The grounding move is my eligibility screen, not a courtesy.",RUST),
   ("4","Ethics is the spine, and mine is severed","IRB-25-0462 covers an anonymous survey. My arm is audio-recorded interviews with identifiable participants, and it is not submitted.",GOLD)]
tt=196
for n,head,body,col in t:
    box(M,tt,W-2*M,68,fill=WHITE,stroke=RULE,r=3)
    box(M,tt,46,68,fill=col,r=3); txt(n,M+23,tt+24,MONOB,17,WHITE,align="c")
    txt(head,M+62,tt+14,DISP,15,INK)
    para(body,M+62,tt+36,W-2*M-84,BODY,12.5,BODYC,lead=15)
    tt+=76
chrome(); c.showPage()

# 9 CLOSE
ground(dark=True); crest(40,light=True)
eyebrow("The through line",130,GOLD)
title("All three refused to know the answer first.",178,size=32,color=WHITE)
title("They refused it in three different ways.",220,size=32,color=GOLD)
rule(274,color=HexColor("#1B3252"))
para("Gerlach refused a category the field had already assigned. Cha and Edmondson had theirs overturned by "
     "what they saw and followed it rather than defending it. Dane had no category at all and built one.",
     M,300,W-2*M-300,BODY,14.5,HexColor("#B9C7D8"),lead=20)
para("The five analysis activities are not a checklist. They are the machinery that makes refusing to know "
     "the answer first survive contact with a deadline.",
     M,384,W-2*M-300,DISPI,14.5,WHITE,lead=20)
box(W-M-268,300,268,158,fill=HexColor("#0E2949"),r=4)
txt("WHY THIS IS MY TOPIC TOO",W-M-246,322,MONOB,8.5,GOLD,track=1.4)
para("Gerlach's charge is that the addiction literature applied its construct in a confirmatory manner. "
     "My study asks what happens when an auditor agrees with a conclusion that arrived already formed.",
     W-M-246,344,224,BODY,12.5,HexColor("#B9C7D8"),lead=16)
txt("SAME FAILURE. DIFFERENT SETTING.",W-M-246,436,MONOB,8,GOLD,track=1.2)
chrome(light=True); c.showPage()

c.save(); print("wrote",out,"·",_n[0],"slides")
