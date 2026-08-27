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
    txt("GEB 7365  ·  Module 2  ·  27 August 2026",W/2,H-24,MONO,8.5,fg,align="c")
    txt(f"{_n[0]}",W-M,H-24,MONOB,8.5,GOLD,align="r")
def ground(dark=False):
    c.setFillColor(BLUE if dark else PAPER); c.rect(0,0,W,H,fill=1,stroke=0)
def eyebrow(s,t,color=GOLD):
    txt(s.upper(),M,t,MONOB,9.5,color,track=2.0)
def title(s,t,size=31,color=INK,w=None):
    return para(s,M,t,w or (W-2*M),DISP,size,color,lead=size*1.14)

# ═══ 1 · HANDOFF — picks up Daniela's exact closing line ═══
ground(dark=True); crest(40,light=True)
eyebrow("Part two  ·  picking up where Daniela ended",112,GOLD)
para("Distance can be priced. Can it be measured?",M,142,W-2*M-30,DISP,34,WHITE,lead=42)

box(M,214,W-2*M,66,fill=HexColor("#0C2547"),stroke=HexColor("#1B3252"),r=4)
txt("DANIELA JUST SAID",M+20,230,MONOB,9,HexColor("#7E93A8"),track=1.5)
para("“Who owns and runs the firm changes how that same distance is perceived and acted on.”",
     M+20,248,W-2*M-40,DISPI,16,WHITE,lead=21)

arrow(W/2,286,W/2,306,GOLD,2)
box(M,312,W-2*M,58,fill=HexColor("#12325C"),stroke=GOLD,lw=1.4,r=4)
txt("SO MY QUESTION",M+20,328,MONOB,9,GOLD,track=1.5)
para("When the field tried to measure any of this — did it measure what it thought it was measuring?",
     M+20,346,W-2*M-40,DISPI,16,WHITE,lead=21)

bw=(W-2*M-16)/2
for i,(nm,yr,sub) in enumerate([("CONTRACTOR, KUNDU & HSU","2003","the shape of the relationship"),
                                ("MEZIAS","2002","the cost of being foreign")]):
    x=M+i*(bw+16)
    box(x,392,bw,72,fill=HexColor("#0C2547"),stroke=HexColor("#1B3252"),r=4)
    txt(nm,x+bw/2,410,MONOB,10,GOLD,align="c",track=1.2)
    txt(yr,x+bw/2,428,BODY,13,HexColor("#5E7793"),align="c")
    txt(sub,x+bw/2,446,DISPI,13,WHITE,align="c")
txt("THEN THE CONCLUSION — ALL FOUR PAPERS, ONE DIAGNOSIS",M,486,MONOB,9,GOLD,track=1.7)
chrome(light=True); c.showPage()

# ═══ 2 · THE SIGMOID ═══
ground(); crest()
eyebrow("Contractor, Kundu & Hsu (2003) · JIBS 34(1): 5–18 · after Figure 1",104)
title("Four findings. One curve.",128)
ox,oy,aw,ah=M+52,398,W-2*M-286,182
c.setStrokeColor(STEEL); c.setLineWidth(1.3)
c.line(ox,y(oy),ox+aw,y(oy)); c.line(ox,y(oy),ox,y(oy-ah))
txt("DEGREE OF INTERNATIONALIZATION",ox+aw/2,oy+18,MONOB,8.5,MUTE,align="c",track=1.2)
c.saveState(); c.translate(ox-20,y(oy-ah/2)); c.rotate(90)
c.setFont(MONOB,8.5); c.setFillColor(MUTE); c._charSpace=1.2
c.drawCentredString(0,0,"PERFORMANCE"); c._charSpace=0; c.restoreState()
def ease(t): return t*t*(3-2*t)
def cy(f):
    if f<0.28: return 0.52-0.42*ease(f/0.28)
    if f<0.72: return 0.10+0.80*ease((f-0.28)/0.44)
    return 0.90-0.34*ease((f-0.72)/0.28)
def px(f): return ox+aw*f
def py(f): return y(oy-ah*cy(f)*0.94)
for f0,f1,tint in [(0.05,0.26,"#F6EBE6"),(0.34,0.66,"#EDF3F2"),(0.74,0.97,"#F2ECE2")]:
    c.setFillColor(HexColor(tint)); c.rect(px(f0),y(oy),px(f1)-px(f0),ah*0.98,fill=1,stroke=0)
c.setStrokeColor(BLUE); c.setLineWidth(3.4)
pth=c.beginPath(); first=True
for i in range(241):
    f=i/240.0
    (pth.moveTo(px(f),py(f)) if first else pth.lineTo(px(f),py(f))); first=False
c.drawPath(pth)
for f0,f1,lab,col in [(0.05,0.26,"1",RUST),(0.34,0.66,"2",TEAL),(0.74,0.97,"3",GOLD)]:
    txt(lab,(px(f0)+px(f1))/2,oy-ah+16,DISP,15,col,align="c")
sx=ox+aw+30
txt("SAMPLE ONLY…",sx,196,MONOB,9,MUTE,track=1.4)
t=216
for lab,res,col in [("segment 1","a NEGATIVE linear result",RUST),
                    ("segment 2","a POSITIVE linear result",TEAL),
                    ("segments 1+2","a U",TEAL),
                    ("segments 2+3","an INVERTED U",GOLD)]:
    c.setFillColor(col); c.circle(sx+4,y(t+7),3.2,fill=1,stroke=0)
    txt(lab,sx+16,t,MONOB,9,col,track=1.0)
    para("you publish "+res,sx+16,t+13,W-M-sx-20,BODY,12,BODYC,lead=15); t+=48
box(M,432,W-2*M,52,fill=SOFT,r=4)
para("Thirty years of contradiction, and none of it was about firms. The literature was sampling different segments of one sigmoid and reporting each as a finding about the whole.",
     M+18,446,W-2*M-36,DISPI,14,INK,lead=18)
chrome(); c.showPage()

# ═══ 3 · WHO OVER-EXPANDS ═══
ground(); crest()
eyebrow("Contractor, Kundu & Hsu (2003) — the finding that reaches practice",104)
title("Some firms walk into stage three more easily.",128)
ox,oy,aw,ah=M+52,392,W-2*M-300,168
c.setStrokeColor(STEEL); c.setLineWidth(1.3)
c.line(ox,y(oy),ox+aw,y(oy)); c.line(ox,y(oy),ox,y(oy-ah))
txt("DEGREE OF INTERNATIONALIZATION",ox+aw/2,oy+18,MONOB,8.5,MUTE,align="c",track=1.2)
def px2(f): return ox+aw*f
def py2(f): return y(oy-ah*cy(f)*0.94)
c.setFillColor(HexColor("#F6EBE6")); c.rect(px2(0.72),y(oy),px2(1.0)-px2(0.72),ah*0.98,fill=1,stroke=0)
c.setStrokeColor(BLUE); c.setLineWidth(3.4)
pth=c.beginPath(); first=True
for i in range(241):
    f=i/240.0
    (pth.moveTo(px2(f),py2(f)) if first else pth.lineTo(px2(f),py2(f))); first=False
c.drawPath(pth)
txt("STAGE 3 — THE EXPENSIVE ONE",px2(0.86),oy-ah-16,MONOB,9,RUST,align="c",track=1.2)
for f,col in [(0.86,RUST),(0.48,TEAL)]:
    c.setFillColor(col); c.circle(px2(f),py2(f),6.5,fill=1,stroke=0)
    c.setFillColor(PAPER); c.circle(px2(f),py2(f),2.4,fill=1,stroke=0)
sx=ox+aw+26
c.setFillColor(RUST); c.circle(sx+5,y(214),5,fill=1,stroke=0)
txt("KNOWLEDGE-BASED SERVICES",sx+18,206,MONOB,9,RUST,track=1.1)
para("Advertising · market research · securities · publishing. “More driven by intangible assets” with “a much lower fixed capital cost burden” — so one more market is cheap to say yes to.",
     sx+18,222,W-M-sx-22,BODY,12,BODYC,lead=15.5)
c.setFillColor(TEAL); c.circle(sx+5,y(310),5,fill=1,stroke=0)
txt("CAPITAL-INTENSIVE",sx+18,302,MONOB,9,TEAL,track=1.1)
para("Airlines · hotels · construction · retail. Fixed assets make every additional market an expensive commitment, so they stop sooner.",
     sx+18,318,W-M-sx-22,BODY,12,BODYC,lead=15.5)
box(M,412,W-2*M,56,fill=WARM,stroke=HexColor("#E4D3A8"),r=4)
para("“Few companies possess the managerial tools (such as regression plotting of firms in a sector) that would tell them when they have over-internationalized.”",
     M+18,425,W-2*M-36,DISPI,15,INK,lead=20)
txt("→ “SHOULD WE INTERNATIONALISE?” IS THE WRONG QUESTION. “WHERE ARE WE ON THE CURVE?” IS THE RIGHT ONE.",
    M,480,MONOB,9,BLUE,track=1.1)
chrome(); c.showPage()

# ═══ 4 · MEZIAS ═══
ground(); crest()
eyebrow("Mezias (2002) · SMJ 23(3): 229–244 · the craft lesson",104)
title("He did not fix the measure. He replaced it.",128)
lx=M; lw=(W-2*M-40)/2
box(lx,178,lw,150,fill=WHITE,stroke=RULE,r=5)
txt("WHAT PERFORMANCE MEASURES DO",lx+18,196,MONOB,9,MUTE,track=1.2)
for i,(lab,col) in enumerate([("advantages",TEAL),("disadvantages",RUST),("transfer pricing",STEEL)]):
    box(lx+18,222+i*26,124,18,fill=col,r=2)
    txt(lab,lx+80,225+i*26,MONOB,8,WHITE,align="c",track=0.8)
for i in range(3): arrow(lx+146,231+i*26,lx+192,257,STEEL,1.2)
box(lx+196,240,lw-214,34,fill=HexColor("#E9E5DC"),stroke=STEEL,r=3)
txt("ONE NUMBER",lx+196+(lw-214)/2,250,MONOB,9,INK,align="c",track=1.2)
txt("nothing isolable",lx+196+(lw-214)/2,290,DISPI,12,MUTE,align="c")
rx=M+lw+40
box(rx,178,lw,150,fill=WHITE,stroke=BLUE,lw=1.6,r=5)
txt("WHAT LABOUR LAWSUITS DO",rx+18,196,MONOB,9,BLUE,track=1.2)
box(rx+18,222,124,18,fill=RUST,r=2)
txt("disadvantages",rx+80,225,MONOB,8,WHITE,align="c",track=0.8)
for i,lab in enumerate(["advantages","transfer pricing"]):
    box(rx+18,248+i*26,124,18,fill=None,stroke=STEEL,dash=(2,2),r=2)
    txt(lab,rx+80,251+i*26,MONOB,8,STEEL,align="c",track=0.8)
    c.setStrokeColor(STEEL); c.setLineWidth(1); c.line(rx+18,y(257+i*26),rx+142,y(257+i*26))
arrow(rx+146,231,rx+192,257,BLUE,1.4)
box(rx+196,240,lw-214,34,fill=SOFT,stroke=BLUE,r=3)
txt("ONE CONSTRUCT",rx+196+(lw-214)/2,250,MONOB,9,BLUE,align="c",track=1.2)
txt("labour-related disadvantage only",rx+196+(lw-214)/2,290,DISPI,12,BLUE,align="c")
box(M,344,W-2*M,44,fill=SOFT,r=4)
para("“While most performance measures aggregate advantages and disadvantages, labor lawsuits only measure labor-related disadvantage.”",
     M+18,356,W-2*M-36,DISPI,14,INK,lead=18)
bw=(W-2*M-24)/3
for i,(v,k) in enumerate([("486","foreign subsidiaries"),("486","matched US firms"),("$600k+","average jury award")]):
    x=M+i*(bw+12)
    box(x,400,bw,64,fill=WHITE,stroke=RULE,r=4)
    txt(v,x+bw/2,414,DISP,24,BLUE,align="c")
    txt(k,x+bw/2,446,MONOB,8.5,MUTE,align="c",track=1.0)
txt("MATCHED ON INDUSTRY AND CITY — SO THE ONLY REMAINING DIFFERENCE IS FOREIGNNESS",M,482,MONOB,9,BLUE,track=1.1)
chrome(); c.showPage()

# ═══ 5 · CONCLUSION — built on Daniela's own line ═══
ground(); crest()
eyebrow("Conclusion — all four",104)
title("Daniela already named it. It is true of all four.",128,29)

box(M,168,W-2*M,50,fill=HexColor("#E3EFEC"),stroke=TEAL,r=4)
txt("HER SLIDE 7",M+18,182,MONOB,9,TEAL,track=1.4)
para("“Contradictions trace to unmeasured heterogeneity, not weak theory.”",
     M+18,198,W-2*M-36,DISPI,15,INK,lead=19)

hx1=M+118; hx2=M+430
txt("WHAT WAS MEASURED",hx1,238,MONOB,9,MUTE,track=1.4)
txt("BELIEVED TO BE",hx2,238,MONOB,9,MUTE,track=1.4)
rule(252)
rows=[("CONTRACTOR","segments of one curve","the shape of the relationship",BLUE),
      ("MEZIAS","aggregate performance","the cost of foreignness",TEAL),
      ("GHEMAWAT","market size","opportunity",GOLD),
      ("ARREGLE","220 studies","a settled question",RUST)]
t=266
for nm,got,thought,col in rows:
    box(M,t,3.5,30,fill=col)
    txt(nm,M+14,t+6,MONOB,9.5,col,track=1.1)
    txt(got,hx1,t+6,BODY,13.5,INK)
    arrow(hx2-46,t+14,hx2-12,t+14,STEEL,1.2)
    txt(thought,hx2,t+6,DISPI,13.5,MUTE)
    t+=38
box(M,424,W-2*M,64,fill=WARM,stroke=HexColor("#E4D3A8"),r=5)
para("Not one of them was fixed by more data. Every one made progress by changing WHAT was measured — which is why this is a methods problem, not a theory problem.",
     M+18,438,W-2*M-36,DISPI,16,INK,lead=21)
chrome(); c.showPage()

# ═══ 6 · CLOSE ═══
ground(dark=True); crest(40,light=True)
eyebrow("One last thing",112,GOLD)
para("Eighteen years. Same question.",M,140,W-2*M,DISP,32,WHITE,lead=38)
tx0=M+96; tx1=W-M-96; ty=246
c.setStrokeColor(HexColor("#1B3252")); c.setLineWidth(2.5)
c.line(tx0,y(ty),tx1,y(ty))
for frac,yr,pap,ven in [(0.0,"2003","Contractor, Kundu & Hsu","JIBS 34(1)"),
                        (1.0,"2021","Arregle, … Kundu, …","JIBS 52")]:
    x=tx0+(tx1-tx0)*frac
    c.setFillColor(GOLD); c.circle(x,y(ty),8,fill=1,stroke=0)
    txt(yr,x,ty-58,DISP,26,WHITE,align="c")
    txt(pap,x,ty-30,MONOB,9,GOLD,align="c",track=1.0)
    txt(ven,x,ty+22,BODY,12,HexColor("#7E93A8"),align="c")
mid=(tx0+tx1)/2
c.setStrokeColor(GOLD); c.setLineWidth(1.2); c.setDash(3,3)
c.line(mid,y(ty-8),mid,y(ty-52)); c.setDash()
txt("SUMIT K. KUNDU  ·  FIU",mid,ty-72,MONOB,11,GOLD,align="c",track=1.8)
txt("author on both",mid,ty+22,DISPI,13,HexColor("#8FA3BC"),align="c")
box(M,298,W-2*M,52,fill=HexColor("#0C2547"),stroke=GOLD,lw=1.3,r=4)
para("The same question about multinationality and performance, asked of a different population eighteen years later — and Daniela's numbers show it is still the theme the field has looked at least.",
     M+18,312,W-2*M-36,DISPI,14.5,WHITE,lead=19)
conn=[("3 SEP","ENTRY MODE","If stage one is negative, mode choice is a decision about how much of that cost to absorb at once."),
      ("24 SEP","INSTITUTIONS","CAGE is a pre-Hofstede way of saying what that session says with formal distance measures.")]
t=368
for d,k,v in conn:
    box(M,t,3,44,fill=GOLD)
    txt(d,M+16,t,MONOB,9,GOLD,track=1.3)
    txt(k,M+70,t,MONOB,9,HexColor("#8FA3BC"),track=1.3)
    para(v,M+16,t+16,W-2*M-36,BODY,13,HexColor("#B8C9D9"),lead=17); t+=52
chrome(light=True); c.showPage()
# ═══ 7 · BACKUP — only if asked how this connects to his own work ═══
ground(); crest()
eyebrow("Backup  ·  only if asked",104)
title("The same error, in my own study.",128,30)

box(M,168,W-2*M,46,fill=SOFT,r=4)
para("Tversky & Kahneman (1974) — a wheel of fortune gave subjects 10 or 65 before they estimated the share of African countries in the UN. Median answers: 25 and 45.",
     M+18,180,W-2*M-36,BODY,14,BODYC,lead=18)

lw=(W-2*M-24)/2
box(M,232,lw,150,fill=WHITE,stroke=RULE,r=5); box(M,232,lw,5,fill=BLUE)
txt("WHAT MY MODEL MEASURES",M+18,252,MONOB,9,BLUE,track=1.2)
para("Eight organisational interventions — training, rotation, analytical tools, structured processes, feedback, independent review, regulatory guidance, incentives — against anchoring bias, with expertise and confidence as moderators.",
     M+18,272,lw-40,BODY,12.5,BODYC,lead=16)

x2=M+lw+24
box(x2,232,lw,150,fill=WHITE,stroke=RUST,lw=1.6,r=5); box(x2,232,lw,5,fill=RUST)
txt("WHAT IT ACTUALLY MEASURES",x2+18,252,MONOB,9,RUST,track=1.2)
para("Anchoring bias is captured by self-report, reverse-coded. It asks auditors to report how far their judgment was driven by a reference point — the one thing the bias reliably prevents them from noticing.",
     x2+18,272,lw-40,BODY,12.5,BODYC,lead=16)
para("Perceived judgment discipline, described as anchoring reduction.",
     x2+18,352,lw-40,DISPI,12,RUST,lead=15)

box(M,398,W-2*M,50,fill=WARM,stroke=HexColor("#E4D3A8"),r=4)
para("Contractor measured segments of a curve. Mezias's field measured aggregate performance. I measured self-reported bias resistance. Three instances of the same error, and one of them is mine.",
     M+18,410,W-2*M-36,DISPI,15,INK,lead=19)
txt("→ AND TVERSKY & KAHNEMAN ALREADY WARNED ME: “PAYOFFS FOR ACCURACY DID NOT REDUCE THE ANCHORING EFFECT.”",
    M,464,MONOB,8.5,BLUE,track=0.9)
txt("WHICH IS A PROBLEM FOR MY OWN HYPOTHESIS ON INCENTIVES.",M,482,MONOB,8.5,RUST,track=0.9)
chrome(); c.showPage()

c.save(); print("wrote",out,"·",_n[0],"slides")
