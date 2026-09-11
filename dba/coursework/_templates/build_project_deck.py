#!/usr/bin/env python3
"""GEB 7365 Project Presentation deck — 16:9. Yasir A. Malik, Cohort 8.14.

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
c.setTitle("Feasibility as a Parameter - GEB 7365 Project Presentation")
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
    txt("GEB 7365  ·  Project Presentation  ·  19 September 2026",W/2,H-24,MONO,8.5,fg,align="c")
    txt(f"{_n[0]}",W-M,H-24,MONOB,8.5,GOLD,align="r")
def ground(dark=False):
    c.setFillColor(BLUE if dark else PAPER); c.rect(0,0,W,H,fill=1,stroke=0)
def eyebrow(s,t,color=GOLD):
    txt(s.upper(),M,t,MONOB,9.5,color,track=2.0)
def title(s,t,size=31,color=INK,w=None):
    return para(s,M,t,w or (W-2*M),DISP,size,color,lead=size*1.14)

FIG1="/home/user/Profile/dba/coursework/GEB7365_International_Business/figures/fig1_feasibility_cliff.png"
def element(n, label, t=112):
    """The five-element spine. Newburry's numbering, visible on every content slide."""
    box(M,t-4,20,20,fill=GOLD,r=3)
    txt(str(n),M+10,t-1,MONOB,11,WHITE,align="c")
    txt(f"ELEMENT {n}  ·  {label.upper()}",M+30,t,MONOB,9.5,BLUE,track=2.0)

# ═══ 1 · TITLE ═══
ground(dark=True); crest(40,light=True)
eyebrow("GEB 7365  ·  Project Presentation  ·  Individual project",150,GOLD)
title("Feasibility as a Parameter",190,size=44,color=WHITE)
title("When comparative research on narrow specialist",244,size=24,color=HexColor("#B9C7D8"))
title("populations can and cannot be executed",274,size=24,color=HexColor("#B9C7D8"))
rule(330,color=HexColor("#1B3252"))
txt("YASIR A. MALIK",M,352,MONOB,11,GOLD,track=2.0)
txt("Doctor of Business Administration  ·  Cohort 8.14",M,372,BODY,13,HexColor("#8FA3BC"))
txt("Instructor: Prof. William Newburry  ·  19 September 2026",M,392,BODY,13,HexColor("#8FA3BC"))
box(W-M-300,150,300,258,fill=HexColor("#0E2949"),r=4)
txt("THE EVIDENCE IS MY OWN FAILED STUDY",W-M-276,176,MONOB,8.5,GOLD,track=1.4)
txt("334,976",W-M-276,204,DISP,40,WHITE)
txt("panel members screened",W-M-276,250,BODY,12,HexColor("#8FA3BC"))
arrow(W-M-276,276,W-M-236,276,color=GOLD,lw=1.6)
txt("20",W-M-222,262,DISP,28,WHITE)
txt("eligible",W-M-176,270,BODY,12,HexColor("#8FA3BC"))
arrow(W-M-276,310,W-M-236,310,color=GOLD,lw=1.6)
txt("4",W-M-222,296,DISP,28,GOLD)
txt("usable",W-M-198,304,BODY,12,HexColor("#8FA3BC"))
rule(340,x=W-M-276,w=252,color=HexColor("#1B3252"))
para("Six per hundred thousand. I did not set out to study this. The constraint arrived as a result.",
     W-M-276,356,252,DISPI,12,HexColor("#B9C7D8"),lead=16)
chrome(light=True); c.showPage()

# ═══ 2 · ELEMENT 1 — the topic ═══
ground(); crest()
element(1,"Research topic and importance")
title("Comparative research has a requirement it never states as one",140,size=27)
para("To compare a phenomenon across countries you must reach the same population in every "
     "country, at the same time, with an instrument that means the same thing in each place.",
     M,196,W-2*M,BODY,15.5,BODYC,lead=22)
rule(242)
COLW=(W-2*M-36)/2
box(M,256,COLW,172,fill=WHITE,stroke=RULE,r=4)
txt("WHEN THE POPULATION IS GENERAL",M+18,278,MONOB,8.5,MUTE,track=1.4)
para("The requirement is demanding but routine. Effort and money convert into responses at a rate "
     "that differs by country and is always positive, always improvable.",
     M+18,300,COLW-36,BODY,13,BODYC,lead=18)
txt("A FIELDWORK PROBLEM",M+18,398,MONOB,9,TEAL,track=1.4)
box(M+COLW+36,256,COLW,172,fill=WARM,stroke=GOLD,r=4)
txt("WHEN THE POPULATION IS RARE",M+COLW+54,278,MONOB,8.5,HexColor("#8A6A1F"),track=1.4)
para("Conversion is governed by arithmetic fixed before the first contact. That arithmetic does "
     "not add across borders. It compounds, and in one direction only.",
     M+COLW+54,300,COLW-36,BODY,13,BODYC,lead=18)
txt("A DESIGN PARAMETER",M+COLW+54,398,MONOB,9,RUST,track=1.4)
para("A design that is marginal in one country is not four times harder in four. It can be "
     "structurally impossible in four while remaining marginal in each one separately.",
     M,446,W-2*M,DISPI,13.5,INK,lead=18)
chrome(); c.showPage()

# ═══ 3 · ELEMENT 1 — the gap and the question ═══
ground(); crest()
element(1,"Research topic and importance")
title("The gap, and the question",140,size=27)
rows=[("THE TOPIC","Reaching a narrow specialist professional population in several national frames at once.",SOFT,BLUE),
      ("THE RECEIVED WISDOM","Sampling difficulty is an execution problem. It belongs to budget and local partners, and it appears in print as a limitation paragraph.",PALE,MUTE),
      ("THE GAP","Nobody has asked what happens when the population is rare. The quantities that decide it are observable before fielding, and they compound across frames.",WARM,GOLD),
      ("THE RESEARCH QUESTION","Under what conditions is a comparative multi-country design on a narrow specialist population feasible at all, and where must a survey give way to another method?",SOFT,BLUE)]
tt=186
for lab,body,fill,accent in rows:
    box(M,tt,W-2*M,72,fill=fill,r=3)
    box(M,tt,4,72,fill=accent)
    txt(lab,M+20,tt+13,MONOB,9,accent,track=1.6)
    para(body,M+20,tt+30,W-2*M-44,BODY,12.5,BODYC,lead=16.5)
    tt+=80
chrome(); c.showPage()

# ═══ 4 · ELEMENT 2 — the model ═══
ground(); crest()
element(2,"Study model and hypotheses")
title("The model: four terms, four different levels",140,size=27)
para("Reachable usable sample is a product, not a sum. Each term is decided at a different level, "
     "and attributing a failed frame to the country assigns to one level what another produced.",
     M,190,W-2*M,BODY,14.5,BODYC,lead=20)
terms=[("FRAME SIZE","panel members","POPULATION",TEAL),
       ("× PREVALENCE","how rare the specialty is","INFRASTRUCTURE",BLUE),
       ("× RESPONSE RATE","who answers","INSTRUMENT",RUST),
       ("× SCREEN SURVIVAL","who survives eligibility","DESIGN",GOLD)]
bw=(W-2*M-3*14)/4
for i,(t1,t2,lvl,col) in enumerate(terms):
    x=M+i*(bw+14)
    box(x,258,bw,128,fill=WHITE,stroke=col,lw=1.4,r=4)
    box(x,258,bw,5,fill=col)
    txt(t1,x+14,282,MONOB,11,INK,track=0.8)
    para(t2,x+14,304,bw-28,BODY,12,BODYC,lead=15)
    txt(lvl,x+14,356,MONOB,8,col,track=1.5)
arrow(M+bw*2+14,404,M+bw*2+14,424,color=STEEL,lw=1.4)
box(M,432,W-2*M,52,fill=BLUE,r=4)
txt("=  REACHABLE USABLE SAMPLE",M+20,450,MONOB,13,WHITE,track=1.6)
txt("observable before a study is fielded, at no cost, on the panel's own interface",
    W-M-20,452,BODY,12.5,HexColor("#8FA3BC"),align="r")
chrome(); c.showPage()

# ═══ 5 · ELEMENT 2 — the binding-frame result ═══
ground(); crest()
element(2,"Study model and hypotheses")
title("The result that makes this a paper and not a complaint",140,size=27)
try:
    c.drawImage(FIG1,M,y(186+272),width=W-2*M-286,height=272,mask='auto',preserveAspectRatio=True)
except Exception:
    box(M,186,W-2*M-286,272,fill=PALE,stroke=RULE,r=4)
bx=W-M-268
box(bx,186,268,272,fill=WARM,stroke=GOLD,r=4)
txt("ADD FOUR COUNTRIES",bx+18,208,MONOB,8.5,HexColor("#8A6A1F"),track=1.5)
txt("Mean response rate",bx+18,232,BODY,12,BODYC)
txt("15.4%  →  9.2%",bx+18,250,DISP,19,MUTE)
txt("barely moves",bx+18,276,DISPI,11.5,MUTE)
rule(300,x=bx+18,w=232,color=HexColor("#E0D2AE"))
txt("Panel needed in EACH",bx+18,312,BODY,12,BODYC)
txt("18.8M  →  72.2M",bx+18,330,DISP,19,RUST)
txt("a factor of four",bx+18,356,DISPI,11.5,RUST)
rule(380,x=bx+18,w=232,color=HexColor("#E0D2AE"))
para("The design is priced by its worst frame, not its average one. Reporting an overall response "
     "rate reports the wrong statistic.",bx+18,394,232,DISPI,12,INK,lead=16)
chrome(); c.showPage()

# ═══ 6 · ELEMENT 2 — the five hypotheses ═══
ground(); crest()
element(2,"Study model and hypotheses")
title("Five hypotheses",140,size=27)
hyps=[("H1","Joint feasibility is set by the least feasible frame, not the mean. Adding a country can only weakly decrease it.","Analytic  ·  the structure of a conjunction",BLUE),
      ("H2","Specialist prevalence on a panel is higher inside the panel provider's home region.","Rugman & Verbeke (2004)",TEAL),
      ("H3","Studies described as cross-national achieve regionally concentrated coverage, more so as the population narrows.","Lopez, Kundu & Ciravegna (2009)",TEAL),
      ("H4","Mode explains more variance in response than country does.","Meyer, Li & Schotter (2020)",RUST),
      ("H5","Standardization is negatively associated with response, worst in the frames that already bind.","Zeng et al. (2023)",GOLD)]
txt("EACH TAKES ITS LOGIC FROM ONE OF THIS WEEK'S FOUR PAPERS",M,176,MONOB,8,MUTE,track=1.4)
tt=196
for tag,body,src,col in hyps:
    box(M,tt,W-2*M,58,fill=WHITE,stroke=RULE,r=3)
    box(M,tt,44,58,fill=col,r=3)
    txt(tag,M+22,tt+20,MONOB,15,WHITE,align="c")
    para(body,M+60,tt+12,W-2*M-360,BODY,12.5,INK,lead=15.5)
    txt(src.upper(),W-M-20,tt+24,MONOB,8,col,track=1.2,align="r")
    tt+=62
chrome(); c.showPage()

# ═══ 7 · ELEMENT 3 — H1 justification ═══
ground(); crest()
element(3,"Justification of hypotheses")
title("H1  ·  A comparison is a conjunction, not an average",140,size=27)
para("To say a relationship differs between Spain and China is to assert something about Spain and "
     "something about China. The assertion fails if either component fails.",
     M,192,W-2*M,BODY,15,BODYC,lead=21)
box(M,250,W-2*M,96,fill=SOFT,r=4)
txt("AN AVERAGE CANNOT SATISFY A CONJUNCTION",M+22,272,MONOB,9.5,BLUE,track=1.8)
para("A design with one excellent frame and one hopeless frame has a respectable mean and no "
     "comparison. The requirement is set by the minimum.",
     M+22,294,W-2*M-44,BODY,14,INK,lead=19)
para("Because a set's minimum can only fall or stay level when an element is added, every "
     "additional country weakly worsens the design and no additional country can improve it.",
     M,366,W-2*M,BODY,15,BODYC,lead=21)
box(M,422,W-2*M,58,fill=WARM,stroke=GOLD,r=4)
para("Breadth is treated in comparative work as a virtue. It is purchased at a price that rises "
     "faster than the count of frames. A design covering more countries has not become more "
     "ambitious. It has become more fragile.",
     M+22,436,W-2*M-44,DISPI,13.5,INK,lead=17)
chrome(); c.showPage()

# ═══ 8 · ELEMENT 3 — H2 and H3 ═══
ground(); crest()
element(3,"Justification of hypotheses")
title("H2 and H3  ·  A research panel is a firm",140,size=27)
para("Rugman and Verbeke showed that firms called global are home-region bound, because "
     "firm-specific advantages transfer within a region cheaply and across regions only by being "
     "rebuilt. Lopez, Kundu and Ciravegna found the same gap in ventures called born global.",
     M,192,W-2*M,BODY,14.5,BODYC,lead=20)
box(M,268,W-2*M,64,fill=SOFT,r=4)
para("A commercial research panel is a firm. It recruits through professional associations, "
     "employment platforms, advertising markets and payment rails, each denser and cheaper inside "
     "the region where the provider originated.",
     M+22,282,W-2*M-44,BODY,13.5,INK,lead=17)
arrow(W/2,340,W/2,360,color=STEEL,lw=1.4)
box(M,368,COLW,112,fill=WHITE,stroke=TEAL,lw=1.4,r=4)
txt("WHY IT BITES HARDER FOR SPECIALISTS",M+18,388,MONOB,8.5,TEAL,track=1.4)
para("A consumer panel is built by broad advertising anywhere. A panel of experienced auditors is "
     "built through professional bodies whose reach is national by construction.",
     M+18,408,COLW-36,BODY,12.5,BODYC,lead=16)
box(M+COLW+36,368,COLW,112,fill=WHITE,stroke=TEAL,lw=1.4,r=4)
txt("AND WHY THE SAMPLE COLLAPSES",M+COLW+54,388,MONOB,8.5,TEAL,track=1.4)
para("Set a global target, accept what arrives, and the result is formally multinational and "
     "substantively regional, with no decision ever taken to that effect.",
     M+COLW+54,408,COLW-36,BODY,12.5,BODYC,lead=16)
chrome(); c.showPage()

# ═══ 9 · ELEMENT 3 — H4 and H5 ═══
ground(); crest()
element(3,"Justification of hypotheses")
title("H4 and H5  ·  Level of analysis, and the price of equivalence",140,size=27)
box(M,188,COLW,268,fill=WHITE,stroke=RUST,lw=1.4,r=4)
box(M,188,COLW,5,fill=RUST)
txt("H4  ·  MODE OVER COUNTRY",M+18,212,MONOB,10,RUST,track=1.6)
para("Response is the outcome of an encounter between a person and a request. Whether it arrives "
     "by telephone from a human being or by email from a platform is a property of the instrument, "
     "not of the country.",M+18,234,COLW-36,BODY,12.5,BODYC,lead=16)
para("Mode changes the cost of refusing. Country changes only the disposition toward it.",
     M+18,320,COLW-36,DISPI,12.5,INK,lead=16)
box(M+18,356,COLW-36,84,fill=HexColor("#FBEFE9"),r=3)
txt("THE ONE DATUM",M+32,372,MONOB,8,RUST,track=1.4)
para("Harzing's 47% in Korea was telephone. It exceeds the entire country spread in the same "
     "project by about five times. One observation is not evidence. It is why this is worth testing.",
     M+32,390,COLW-64,BODY,11.5,BODYC,lead=14.5)
box(M+COLW+36,188,COLW,268,fill=WHITE,stroke=GOLD,lw=1.4,r=4)
box(M+COLW+36,188,COLW,5,fill=GOLD)
txt("H5  ·  CONTROL AGAINST COORDINATION",M+COLW+54,212,MONOB,10,HexColor("#8A6A1F"),track=1.6)
para("Zeng and colleagues separate control, a standard imposed from the centre, from coordination, "
     "the alignment of units that keep discretion. The two trade off.",
     M+COLW+54,234,COLW-36,BODY,12.5,BODYC,lead=16)
para("Equivalence needs an identical instrument. Response needs adaptation of length, channel, "
     "sponsorship and register. They pull the same instrument in opposite directions.",
     M+COLW+54,300,COLW-36,BODY,12.5,BODYC,lead=16)
box(M+COLW+54,378,COLW-36,62,fill=WARM,r=3)
para("A strong frame can afford the loss. A weak frame had no margin, and under H1 the weak frames "
     "bind the design.",M+COLW+68,392,COLW-64,DISPI,12,INK,lead=15)
chrome(); c.showPage()

# ═══ 10 · ELEMENT 4 — data collection ═══
ground(); crest()
element(4,"Data collection plan")
title("What gets measured, and why it can be measured at all",140,size=27)
box(M,190,W-2*M,62,fill=SOFT,r=4)
para("Panel providers expose an audience-configuration interface that returns an estimated "
     "reachable count once screening criteria are entered, before any commitment and at no cost. "
     "That is what makes feasibility a parameter rather than a limitation.",
     M+22,204,W-2*M-44,BODY,13.5,INK,lead=17)
cells=[("UNIT OF ANALYSIS","One occupation, on one panel provider, in one national frame"),
       ("THE MATRIX","6+ occupations  ×  8+ national frames  ×  3+ providers  ≈  144 cells"),
       ("PROVIDERS CHOSEN TO VARY","On home region, deliberately. H2 is unidentifiable otherwise"),
       ("THE VALIDATING CASE","My own study. A model that cannot reproduce 334,976 → 20 → 4 is rejected")]
tt=266
for lab,body in cells:
    box(M,tt,W-2*M,44,fill=WHITE,stroke=RULE,r=3)
    txt(lab,M+18,tt+15,MONOB,8.5,BLUE,track=1.5)
    txt(body,M+286,tt+15,BODY,12.5,BODYC)
    tt+=52
txt("NO DATA HAVE BEEN COLLECTED FOR THIS PROJECT. THIS IS THE DESIGN, NOT A RESULT.",
    M,H-56,MONOB,8,RUST,track=1.4)
chrome(); c.showPage()

# ═══ 11 · ELEMENT 5 — analysis plan ═══
ground(); crest()
element(5,"Empirical analysis plan")
title("Two different kinds of claim, two different treatments",140,size=27)
box(M,192,COLW,244,fill=WHITE,stroke=BLUE,lw=1.4,r=4)
box(M,192,COLW,5,fill=BLUE)
txt("H1  ·  ANALYTIC",M+18,216,MONOB,10,BLUE,track=1.6)
para("Established by demonstration and probed by sensitivity analysis across the plausible range of "
     "prevalence, response and screen survival, reporting the region of the parameter space where "
     "a comparative design stays viable.",M+18,238,COLW-36,BODY,12.5,BODYC,lead=16)
box(M+18,340,COLW-36,80,fill=SOFT,r=3)
para("The claim is about the structure of a conjunction. It would not be made more true by a "
     "p-value, and reporting one would present a deductive result as an empirical one.",
     M+32,356,COLW-64,DISPI,12,INK,lead=15)
box(M+COLW+36,192,COLW,244,fill=WHITE,stroke=TEAL,lw=1.4,r=4)
box(M+COLW+36,192,COLW,5,fill=TEAL)
txt("H2 – H5  ·  INFERENTIAL",M+COLW+54,216,MONOB,10,TEAL,track=1.6)
para("Hierarchical linear models. Cells nested in national frames, frames nested in regions, random "
     "intercepts at frame and provider level.",
     M+COLW+54,238,COLW-36,BODY,12.5,BODYC,lead=16)
para("The nesting is not a convenience. It is the structure Meyer and colleagues argue must be "
     "modelled, and ignoring it attributes to countries the variance that belongs to providers.",
     M+COLW+54,300,COLW-36,BODY,12.5,BODYC,lead=16)
box(M+COLW+54,378,COLW-36,42,fill=HexColor("#E8F1F0"),r=3)
txt("H5 IS SUPPORTED ONLY BY THE INTERACTION, NOT THE MAIN EFFECT",
    M+COLW+68,394,MONOB,8,TEAL,track=1.2)
chrome(); c.showPage()

# ═══ 12 · WHAT IT DOES NOT CLAIM ═══
ground(); crest()
eyebrow("Before you ask  ·  the limits, stated first",112,RUST)
title("What this model does not claim",140,size=27)
lims=[("Prevalence is held constant across countries","It almost certainly is not. No cross-national prevalence data for these populations exists, which is why obtaining it is the contribution rather than an assumption."),
      ("The response rates come from one study","One instrument, one period. Treating them as a general country characteristic would commit the level-of-analysis error the paper itself identifies."),
      ("Rates are treated as independent","They are not. Frames within a region share institutional conditions and will correlate."),
      ("Panel estimates are vendor-supplied and unaudited","They are the same numbers researchers already rely on, so this adds no new exposure, but estimated against achieved is a validation step not yet in the design.")]
tt=196
for lab,body in lims:
    box(M,tt,W-2*M,66,fill=WHITE,stroke=RULE,r=3)
    box(M,tt,4,66,fill=RUST)
    txt(lab,M+20,tt+14,DISP,14,INK)
    para(body,M+20,tt+34,W-2*M-44,BODY,12.5,BODYC,lead=16)
    tt+=76
chrome(); c.showPage()

# ═══ 13 · CLOSE ═══
ground(dark=True); crest(40,light=True)
eyebrow("The contribution",130,GOLD)
title("A parameter is estimated before a design.",178,size=32,color=WHITE)
title("A limitation is confessed after it fails.",220,size=32,color=GOLD)
rule(274,color=HexColor("#1B3252"))
para("Comparative international business has treated who can be reached as a matter of execution. "
     "For general populations that is harmless. For narrow specialist populations it is not, "
     "because the arithmetic compounds across frames in one direction and is decided by the weakest "
     "frame rather than the average one.",
     M,300,W-2*M-300,BODY,14.5,HexColor("#B9C7D8"),lead=20)
para("The quantities are observable before a study is fielded. Making them part of the design, "
     "rather than part of the confession, is a small change in practice and a substantial change "
     "in what the field can claim to have compared.",
     M,392,W-2*M-300,DISPI,14.5,WHITE,lead=20)
box(W-M-268,300,268,158,fill=HexColor("#0E2949"),r=4)
txt("AND THE SECOND IMPLICATION",W-M-246,322,MONOB,8.5,GOLD,track=1.4)
para("Where the arithmetic rules out a survey it does not rule out the study. Twenty reachable "
     "participants are a failed survey and a well-powered phenomenological one.",
     W-M-246,344,224,BODY,12.5,HexColor("#B9C7D8"),lead=16)
txt("THE THRESHOLD IS LOCATABLE IN ADVANCE",W-M-246,428,MONOB,8,GOLD,track=1.2)
chrome(light=True); c.showPage()

c.save(); print("wrote",out,"·",_n[0],"slides")
