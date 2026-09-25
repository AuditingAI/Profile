#!/usr/bin/env python3
"""GEB 7365 residency readings deck: institutions, culture, and a question about H2 — 16:9. Yasir A. Malik, Cohort 8.14.

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
c.setTitle("Institutions and Culture - a question about H2 - GEB 7365")
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
    txt("GEB 7365  ·  Residency readings  ·  19 September 2026",W/2,H-24,MONO,8.5,fg,align="c")
    txt(f"{_n[0]}",W-M,H-24,MONOB,8.5,GOLD,align="r")
def ground(dark=False):
    c.setFillColor(BLUE if dark else PAPER); c.rect(0,0,W,H,fill=1,stroke=0)
def eyebrow(s,t,color=GOLD):
    txt(s.upper(),M,t,MONOB,9.5,color,track=2.0)
def title(s,t,size=31,color=INK,w=None):
    return para(s,M,t,w or (W-2*M),DISP,size,color,lead=size*1.14)

FIGD="/home/user/Profile/dba/coursework/GEB7365_International_Business/figures/"
COLW=(W-2*M-36)/2

# 1 TITLE
ground(dark=True); crest(40,light=True)
eyebrow("GEB 7365  ·  Residency, 18 and 19 September  ·  Institutions and Culture",150,GOLD)
title("A Question About H2",190,size=44,color=WHITE,w=W-2*M-350)
title("Is the triad the right unit for this hypothesis?",248,size=23,color=HexColor("#B9C7D8"),w=W-2*M-350)
rule(306,x=M,w=W-2*M-350,color=HexColor("#1B3252"))
txt("YASIR A. MALIK",M,328,MONOB,11,GOLD,track=2.0)
txt("Doctor of Business Administration  ·  Cohort 8.14",M,348,BODY,13,HexColor("#8FA3BC"))
txt("For Prof. William Newburry  ·  19 September 2026",M,368,BODY,13,HexColor("#8FA3BC"))
box(W-M-320,150,320,300,fill=HexColor("#0E2949"),r=4)
txt("THE SHORT VERSION",W-M-296,176,MONOB,8.5,GOLD,track=1.4)
para("My hypothesis says a commercial research panel should be home-region bound. I have been "
     "measuring region on the triad.",W-M-296,202,272,BODY,13,HexColor("#B9C7D8"),lead=18)
para("Fainshmidt and colleagues suggest the triad may be the wrong unit, and they have already built "
     "the alternative.",W-M-296,286,272,BODY,13,HexColor("#B9C7D8"),lead=18)
rule(374,x=W-M-296,w=272,color=HexColor("#1B3252"))
para("This is a question, not a conclusion. Nobody has tested either version.",
     W-M-296,392,272,DISPI,12.5,WHITE,lead=17)
chrome(light=True); c.showPage()

# 2 THROUGH LINE
ground(); crest()
eyebrow("All five readings",112,BLUE)
title("Each one denies that the backdrop holds still",140,size=27)
para("Most international business research treats institutions and culture as a stable setting "
     "against which firms act. These five deny that in five different ways.",
     M,190,W-2*M,BODY,14.5,BODYC,lead=20)
rows=[("Fainshmidt et al. (2018)","There are seven kinds of institutional system, not two",TEAL),
      ("Cuervo-Cazurra et al. (2019)","Institutions swing back and forth. Reform reverses",RUST),
      ("House et al. (2002)","Culture is nine-dimensional, and mostly universal anyway",BLUE),
      ("Deephouse, Newburry & Soleimani (2016)","The same firm earns a different reputation depending where it sits",GOLD),
      ("Samiee et al. (2024)","After sixty years the field still cannot agree what origin does",STEEL)]
tt=238
for name,claim,col in rows:
    box(M,tt,W-2*M,42,fill=WHITE,stroke=RULE,r=3); box(M,tt,4,42,fill=col)
    txt(name,M+20,tt+12,DISP,14,INK)
    txt(claim,M+330,tt+13,BODY,12.5,BODYC)
    tt+=46
para("The session is not really about institutions. It is about what happens to a comparative claim "
     "when the thing you were holding constant turns out to vary.",
     M,478,W-2*M,DISPI,13.5,INK,lead=17)
chrome(); c.showPage()

# 3 DEEPHOUSE
ground(); crest()
eyebrow("The one I read first",112,GOLD)
title("Deephouse, Newburry & Soleimani (2016)",140,size=27)
para("401 corporations across 25 countries, reputation measured in 2007, 2009 and 2011, with "
     "independent variables lagged so respondents could plausibly have known them.",
     M,190,W-2*M,BODY,14.5,BODYC,lead=20)
box(M,250,COLW,150,fill=WHITE,stroke=GOLD,lw=1.4,r=4); box(M,250,COLW,5,fill=GOLD)
txt("THE RESULT THAT IS WORTH THE PAPER",M+18,274,MONOB,9,HexColor("#8A6A1F"),track=1.4)
para("Reputation is NEGATIVELY related to institutional development, at p < 0.001. In less developed "
     "economies corporations fill institutional voids and expectations of them are lower.",
     M+18,296,COLW-36,BODY,13,BODYC,lead=17)
box(M+COLW+36,250,COLW,150,fill=SOFT,r=4)
txt("THE SENTENCE I WILL BORROW",M+COLW+54,274,MONOB,9,BLUE,track=1.4)
para("In a cross-national study the relevant comparison group is not the same in every country. That "
     "is the cleanest statement I have found of why one average conceals more than it reports.",
     M+COLW+54,296,COLW-36,BODY,13,INK,lead=17)
box(M,424,W-2*M,58,fill=WARM,stroke=GOLD,r=4)
para("It is the same claim I make about overall response rates in comparative survey work: the mean "
     "across frames is nearly uninformative, and the minimum is decisive. Their version is better "
     "evidenced than mine.",M+20,438,W-2*M-40,DISPI,13.5,INK,lead=17)
chrome(); c.showPage()

# 4 FAINSHMIDT
ground(); crest()
eyebrow("The one that changed the design",112,TEAL)
title("Fainshmidt, Judge, Aguilera & Smith (2018)",140,size=27)
para("Institutional profiles of 68 economies across 13 elements, built from expert judgement and "
     "sorted by two-step cluster analysis. Aimed deliberately at the economies Varieties of "
     "Capitalism and National Business Systems leave out.",
     M,190,W-2*M,BODY,14.5,BODYC,lead=20)
box(M,256,COLW,200,fill=WHITE,stroke=TEAL,lw=1.4,r=4); box(M,256,COLW,5,fill=TEAL)
txt("FIVE DIMENSIONS",M+18,280,MONOB,9,TEAL,track=1.5)
for i,dd in enumerate(["The state","Financial markets","Human capital","Social capital","Corporate governance"]):
    txt("·  "+dd,M+18,304+i*26,BODY,13.5,BODYC)
txt("AND THE STATE ITSELF IS TYPED",M+18,442,MONOB,8.5,TEAL,track=1.2)
box(M+COLW+36,256,COLW,200,fill=HexColor("#E8F1F0"),stroke=TEAL,lw=1.4,r=4)
box(M+COLW+36,256,COLW,5,fill=TEAL)
txt("SEVEN TYPES",M+COLW+54,280,MONOB,9,TEAL,track=1.5)
for i,tt2 in enumerate(["State-Led","Fragmented with a Fragile State","Family-Led","Centralized Tribe",
                        "Emergent LME","Collaborative Agglomerations","Hierarchically Coordinated"]):
    txt("·  "+tt2,M+COLW+54,302+i*22,BODY,12.5,INK)
para("Predatory, developmental, welfare or regulatory, measured separately from direct dominance and "
     "indirect intervention. Fainshmidt is at FIU.",
     M,476,W-2*M,DISPI,13.5,INK,lead=18)
chrome(); c.showPage()

# 5 MY RESEARCH
ground(); crest()
eyebrow("Where my project stands",112,BLUE)
title("H2, as I wrote it for the 18 September deck",140,size=27)
box(M,186,W-2*M,62,fill=SOFT,r=4)
para("H2. The observable prevalence of a narrow specialist professional population on a commercial "
     "research panel is higher within the panel provider's home region than outside it.",
     M+20,200,W-2*M-40,BODY,14,INK,lead=18)
para("The logic is Rugman and Verbeke's own. Of the 380 largest multinationals with usable sales "
     "data, 320 were home-region oriented at 80.3 percent of sales, and only nine were global. Their "
     "mechanism is that upstream advantages in technology travel while downstream advantages such as "
     "branding are location-bound.",M,270,W-2*M,BODY,14,BODYC,lead=19)
box(M,362,W-2*M,80,fill=WHITE,stroke=BLUE,lw=1.4,r=4)
para("A research panel is a firm whose entire product is a downstream asset: its membership, and its "
     "standing with that membership. Survey software is a commodity, so there is almost no upstream "
     "advantage to carry abroad. On their own account a panel should be MORE home-region bound than "
     "a manufacturer, not less.",M+20,378,W-2*M-40,BODY,13.5,INK,lead=17)
para("That argument I am confident in. What I am no longer confident in is the unit I chose to test "
     "it on.",M,464,W-2*M,DISPI,14,RUST,lead=18)
chrome(); c.showPage()

# 6 THE QUESTION (chart)
ground(); crest()
eyebrow("The question",112,RUST)
title("Is the triad the right unit for this hypothesis?",140,size=27)
try:
    from PIL import Image as _I
    iw,ih=_I.open(FIGD+"h2_triad_vs_vis.png").size
    w=W-2*M; h=w*ih/iw
    if h>250: h=250; w=h*iw/ih
    c.drawImage(FIGD+"h2_triad_vs_vis.png",(W-w)/2,y(192+h),width=w,height=h,mask='auto',preserveAspectRatio=True)
    bot=192+h
except Exception:
    box(M,192,W-2*M,250,fill=PALE,stroke=RULE,r=4); bot=442
para("If what actually determines whether a panel can reach a specialist professional population is "
     "the configuration of human capital institutions, social capital and the character of the state, "
     "then two countries inside one triad region can differ more than two countries across regions.",
     M,bot+20,W-2*M,DISPI,13.5,INK,lead=18)
chrome(); c.showPage()

# 7 WHAT IT WOULD TAKE
ground(); crest()
eyebrow("If the answer is yes",112,TEAL)
title("What testing it would actually require",140,size=27)
t=[("1","Nothing new to collect","Both classifications are published. Rugman and Verbeke assign the triad; Fainshmidt and colleagues assign 68 economies to seven types.",TEAL),
   ("2","The panel providers still have to vary","H2 is unidentifiable if every provider originates in one place. That constraint is unchanged.",BLUE),
   ("3","It becomes a competing-specifications test","Run the model both ways and report which classification explains more. That is a stronger paper than assuming one.",GOLD),
   ("4","The risk is coverage","Fainshmidt covers 68 economies and the triad covers everything. If my frames fall outside the 68, the comparison narrows.",RUST)]
tt=196
for n,head,body,col in t:
    box(M,tt,W-2*M,70,fill=WHITE,stroke=RULE,r=3)
    box(M,tt,46,70,fill=col,r=3); txt(n,M+23,tt+25,MONOB,17,WHITE,align="c")
    txt(head,M+62,tt+14,DISP,15,INK)
    para(body,M+62,tt+36,W-2*M-84,BODY,12.5,BODYC,lead=15)
    tt+=78
chrome(); c.showPage()

# 8 CLOSE
ground(dark=True); crest(40,light=True)
eyebrow("What I am asking",130,GOLD)
title("Is this worth doing, or am I",178,size=34,color=WHITE)
title("complicating a hypothesis that works?",220,size=34,color=GOLD)
rule(276,color=HexColor("#1B3252"))
para("I can defend the argument behind H2. I am less sure the triad is the unit that tests it, and I "
     "would rather hear that now than in the October report.",
     M,302,W-2*M-300,BODY,15,HexColor("#B9C7D8"),lead=21)
para("The taxonomy already exists, it was built for exactly the economies a commercial panel is "
     "least likely to cover, and one of its authors is at FIU.",
     M,384,W-2*M-300,DISPI,15,WHITE,lead=21)
box(W-M-268,302,268,156,fill=HexColor("#0E2949"),r=4)
txt("THE HONEST POSITION",W-M-246,324,MONOB,8.5,GOLD,track=1.4)
para("This is a question about a design, not a finding. No data has been collected for the project, "
     "and neither version of H2 has been tested by anyone.",
     W-M-246,346,224,BODY,12.5,HexColor("#B9C7D8"),lead=16)
txt("YASIR A. MALIK  ·  COHORT 8.14",W-M-246,430,MONOB,8,GOLD,track=1.2)
chrome(light=True); c.showPage()

c.save(); print("wrote",out,"·",_n[0],"slides")
