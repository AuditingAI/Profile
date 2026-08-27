#!/usr/bin/env python3
"""Module presentation deck — 16:9 PDF, house brand. Yasir A. Malik."""
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

W, H = 960, 540
NAVY=HexColor("#1F4E79"); DEEP=HexColor("#0E2237"); GOLD=HexColor("#8A6410")
PAPER=HexColor("#FBFAF7"); INK=HexColor("#14171C"); MUTE=HexColor("#767D86")
RULE=HexColor("#D8D4CB"); SOFT=HexColor("#E9EFF6"); WARM=HexColor("#FBF6EA")
WHITE=HexColor("#FFFFFF"); BODYC=HexColor("#454B54"); TEAL=HexColor("#1C6B63")
WARN=HexColor("#8C3A1B"); HOLD=HexColor("#9AA4AE")
DISP="Times-Bold"; DISPI="Times-Italic"; BODY="Times-Roman"
MONO="Courier"; MONOB="Courier-Bold"
M=56
out=sys.argv[1] if len(sys.argv)>1 else "deck.pdf"
c=canvas.Canvas(out,pagesize=(W,H))
c.setTitle("Internationalization and Performance — Module 2")
c.setAuthor("Yasir A. Malik")
_n=[0]

def y(v): return H-v
def box(x,t,w,h,fill=None,stroke=None,lw=1,r=None):
    if fill: c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke); c.setLineWidth(lw)
    if r: c.roundRect(x,y(t+h),w,h,r,fill=1 if fill else 0,stroke=1 if stroke else 0)
    else: c.rect(x,y(t+h),w,h,fill=1 if fill else 0,stroke=1 if stroke else 0)
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
    c.setStrokeColor(color); c.setLineWidth(lw); c.line(x,y(t),x+w,y(t))
def chrome(presenter="Yasir A. Malik", dark=False):
    _n[0]+=1
    fg=HexColor("#7E93A8") if dark else MUTE
    rule(H-34,color=HexColor("#24405C") if dark else RULE)
    txt(presenter,M,H-26,MONOB,9,fg,track=1.2)
    txt("GEB 7365 · Module 2 · 27 Aug 2026",W/2,H-26,MONO,9,fg,align="c")
    txt(f"{_n[0]}",W-M,H-26,MONOB,9,NAVY if not dark else HexColor("#8FB6D8"),align="r")
def ground(dark=False):
    c.setFillColor(DEEP if dark else PAPER); c.rect(0,0,W,H,fill=1,stroke=0)
def eyebrow(s,t,color=GOLD):
    txt(s.upper(),M,t,MONOB,10,color,track=2.0)
def title(s,t,size=34,color=INK):
    return para(s,M,t,W-2*M,DISP,size,color,lead=size*1.12)

# ─── YASIR'S HALF ────────────────────────────────────────────────────
# Split per Daniela Garcia Aguirre's message of 23 Aug: she opens with the
# introduction plus Arregle and Ghemawat; Yasir takes Contractor and Mezias
# and closes.  Five minutes each.

# ═══ 1 · HANDOFF ═════════════════════════════════════════════════════
ground()
c.setFont(DISP,17); c.setFillColor(NAVY)
c.drawString(M,y(46)-14,"Audit"); w1=c.stringWidth("Audit ",DISP,17)
c.setFont(DISPI,13); c.setFillColor(MUTE); c.drawString(M+w1,y(46)-14,"the")
w2=w1+c.stringWidth("the ",DISPI,13)
c.setFont(DISP,17); c.setFillColor(NAVY); c.drawString(M+w2,y(46)-14,"Algorithm")

eyebrow("Part two",120)
title("Two papers about what we were\nmeasuring all along.",150,32)

box(M,258,W-2*M,74,fill=SOFT,r=5)
para("Daniela has shown us where the field disagrees and what distance is made of. I want to ask a narrower question: when the field could not agree, what exactly was it measuring?",
     M+22,276,W-2*M-44,DISPI,16,INK,lead=21)

nxt=[("CONTRACTOR, KUNDU & HSU (2003)","The curve that reconciles thirty years of contradiction",NAVY),
     ("MEZIAS (2002)","The study that made progress by throwing the measure away",TEAL)]
t=360
for k,v,col in nxt:
    box(M,t,4,42,fill=col)
    txt(k,M+18,t,MONOB,11,col,track=1.4)
    txt(v,M+18,t+18,BODY,16,BODYC)
    t+=56
txt("THEN THE CONCLUSION — WHAT ALL FOUR HAVE IN COMMON",M,474,MONOB,10,GOLD,track=1.8)
chrome(); c.showPage()

# ═══ 2 · CONTRACTOR — THE CURVE ══════════════════════════════════════
ground()
eyebrow("Contractor, Kundu & Hsu (2003) · JIBS 34(1) · after Figure 1",62)
title("Why the field disagreed for thirty years.",96,32)

ox,oy,aw,ah=M+56,392,W-2*M-300,190
c.setStrokeColor(HexColor("#9AA4AE")); c.setLineWidth(1.4)
c.line(ox,y(oy),ox+aw,y(oy)); c.line(ox,y(oy),ox,y(oy-ah))
txt("DEGREE OF INTERNATIONALIZATION",ox+aw/2,oy+20,MONOB,9,MUTE,align="c",track=1.2)
c.saveState(); c.translate(ox-22,y(oy-ah/2)); c.rotate(90)
c.setFont(MONOB,9); c.setFillColor(MUTE); c._charSpace=1.2
c.drawCentredString(0,0,"PERFORMANCE"); c._charSpace=0; c.restoreState()

def ease(t): return t*t*(3-2*t)
def cy(f):
    if f<0.28: return 0.52-0.42*ease(f/0.28)
    if f<0.72: return 0.10+0.80*ease((f-0.28)/0.44)
    return 0.90-0.34*ease((f-0.72)/0.28)
c.setStrokeColor(NAVY); c.setLineWidth(3.5)
pth=c.beginPath(); first=True
for i in range(241):
    f=i/240.0; px=ox+aw*f; py=y(oy-ah*cy(f)*0.94)
    (pth.moveTo(px,py) if first else pth.lineTo(px,py)); first=False
c.drawPath(pth)
for f0,f1,lab,col in [(0,.28,"1",NAVY),(.28,.72,"2",TEAL),(.72,1,"3",WARN)]:
    x1=ox+aw*f1
    if f1<1:
        c.setStrokeColor(HexColor("#DDE4EA")); c.setLineWidth(1); c.setDash(3,4)
        c.line(x1,y(oy),x1,y(oy-ah)); c.setDash()
    txt(lab,ox+aw*(f0+f1)/2,oy-ah+22,DISP,17,col,align="c")

sx=ox+aw+34
for n,sl,why,col in [("1","Negative","liability of foreignness, learning costs",NAVY),
                     ("2","Positive","scale, scope and learning outweigh cost",TEAL),
                     ("3","Negative","cost of managing scattered operations",WARN)]:
    pass
t=196
for n,sl,why,col in [("1","Negative","liability of foreignness, learning costs",NAVY),
                     ("2","Positive","scale, scope and learning outweigh cost",TEAL),
                     ("3","Negative","cost of managing scattered operations",WARN)]:
    txt(f"STAGE {n} — {sl.upper()}",sx,t,MONOB,10,col,track=1.2)
    para(why,sx,t+16,W-M-sx,BODY,13,BODYC,lead=17); t+=58

box(M,428,W-2*M,50,fill=SOFT,r=4)
para("Sample only the middle and you report a positive linear relationship. Sample the ends and you report an inverted U. The disagreement was partly artefactual.",
     M+20,442,W-2*M-40,DISPI,14,INK,lead=19)
chrome(); c.showPage()

# ═══ 3 · CONTRACTOR — THE PRACTICE LINE ══════════════════════════════
ground()
eyebrow("Contractor, Kundu & Hsu (2003) — and why it matters outside the journal",62)
title("Nobody can tell when they have gone too far.",96,32)

box(M,164,(W-2*M-20)/2,146,fill=WHITE,stroke=RULE,r=5)
box(M,164,(W-2*M-20)/2,5,fill=WARN)
txt("OVER-EXPAND MORE READILY",M+22,188,MONOB,10,WARN,track=1.4)
para("Knowledge-based services — advertising, market research, securities, publishing. Lower fixed-asset exposure, so one more market is easy to underwrite.",
     M+22,210,(W-2*M-20)/2-44,BODY,14,BODYC,lead=19)
x2=M+(W-2*M-20)/2+20
box(x2,164,(W-2*M-20)/2,146,fill=WHITE,stroke=RULE,r=5)
box(x2,164,(W-2*M-20)/2,5,fill=TEAL)
txt("OVER-EXPAND LESS READILY",x2+22,188,MONOB,10,TEAL,track=1.4)
para("Capital-intensive — airlines, hotels, construction, retail. Fixed assets make each additional market an expensive commitment.",
     x2+22,210,(W-2*M-20)/2-44,BODY,14,BODYC,lead=19)

box(M,338,W-2*M,80,fill=WARM,stroke=HexColor("#E4D3A8"),r=5)
txt("THEIR WORDS",M+24,358,MONOB,10,GOLD,track=1.6)
para("“Few companies possess the managerial tools that would tell them when they have over-internationalized.”",
     M+24,380,W-2*M-48,DISPI,19,INK,lead=25)
para("If the relationship is sigmoid, “should we internationalise?” is the wrong question. “Where are we on the curve?” is the right one — and almost nobody can answer it.",
     M,436,W-2*M,BODY,15,BODYC,lead=20)
chrome(); c.showPage()

# ═══ 4 · MEZIAS ══════════════════════════════════════════════════════
ground()
eyebrow("Mezias (2002) · SMJ 23(3) · the craft lesson",62)
title("He made progress by throwing the measure away.",96,32)

para("Everyone agreed the liability of foreignness existed. Nobody could isolate it — because performance measures aggregate advantages and disadvantages into one number, and transfer pricing contaminates what is left.",
     M,158,W-2*M,BODY,16,BODYC,lead=22)

box(M,222,W-2*M,72,fill=SOFT,r=4)
txt("HIS JUSTIFICATION — A METHODOLOGICAL ARGUMENT, NOT AN EMPIRICAL ONE",M+22,240,MONOB,9.5,NAVY,track=1.4)
para("“While most performance measures aggregate advantages and disadvantages, labor lawsuits only measure labor-related disadvantage.”",
     M+22,260,W-2*M-44,DISPI,16,INK,lead=21)

bw=(W-2*M-24)/3
for i,(v,k) in enumerate([("486","foreign subsidiaries"),("486","matched US firms"),("$600k+","average jury award")]):
    x=M+i*(bw+12)
    box(x,312,bw,76,fill=WHITE,stroke=RULE,r=5)
    txt(v,x+bw/2,330,DISP,26,TEAL,align="c")
    txt(k,x+bw/2,368,MONOB,9,MUTE,align="c",track=1.0)
para("British, German and Japanese subsidiaries in the US, matched to US-owned firms in the same industries and cities. Then, within the foreign sample: staffing strategy, autonomy, affiliated firms, age.",
     M,400,W-2*M,BODY,14,BODYC,lead=19)
box(M,448,W-2*M,44,fill=WARM,stroke=HexColor("#E4D3A8"),r=4)
para("He did not improve the measurement of performance. He abandoned it.",
     M+22,460,W-2*M-44,DISPI,16,INK,lead=20)
chrome(); c.showPage()

# ═══ 5 · THE CONCLUSION ══════════════════════════════════════════════
ground()
eyebrow("Conclusion",62)
title("One diagnosis, four times.",96,34,NAVY)

box(M,158,W-2*M,66,fill=WARM,stroke=HexColor("#E4D3A8"),r=5)
para("At each stage the field measured the wrong thing — or measured one thing while believing it had measured another.",
     M+22,176,W-2*M-44,DISPI,18,INK,lead=24)

rows=[("CONTRACTOR","measured segments of one curve, reported them as different relationships",NAVY),
      ("MEZIAS","measured aggregate performance, believed it had measured foreignness",TEAL),
      ("GHEMAWAT","measured market size, believed it had measured opportunity",GOLD),
      ("ARREGLE","30 years, 220 studies, still “varied and at times incompatible findings”",WARN)]
t=248
for k,v,col in rows:
    box(M,t,4,26,fill=col)
    txt(k,M+18,t+3,MONOB,11,col,track=1.4)
    txt(v,M+150,t+3,BODY,15,BODYC)
    t+=36

box(M,404,W-2*M,88,fill=SOFT,r=5)
txt("SO WHAT FOLLOWS",M+22,422,MONOB,10,NAVY,track=1.6)
para("Every one of them made progress by changing what was measured — not by collecting more of the same thing. A literature that cannot converge because it cannot agree on a measure has a methods problem, not a theory problem.",
     M+22,442,W-2*M-44,BODY,15,BODYC,lead=20)
chrome(); c.showPage()

# ═══ 6 · CLOSE ═══════════════════════════════════════════════════════
ground(dark=True)
c.setFont(DISP,17); c.setFillColor(HexColor("#9FC4E4"))
c.drawString(M,y(46)-14,"Audit"); w1=c.stringWidth("Audit ",DISP,17)
c.setFont(DISPI,13); c.setFillColor(MUTE); c.drawString(M+w1,y(46)-14,"the")
w2=w1+c.stringWidth("the ",DISPI,13)
c.setFont(DISP,17); c.setFillColor(HexColor("#9FC4E4")); c.drawString(M+w2,y(46)-14,"Algorithm")

eyebrow("Two things to leave you with",118,HexColor("#C8A23C"))
para("Where this goes next.",M,148,W-2*M,DISP,32,WHITE,lead=38)

box(M,206,W-2*M,92,fill=HexColor("#16293C"),stroke=HexColor("#24405C"),r=5)
txt("ACROSS THE ROOM",M+22,224,MONOB,10,HexColor("#C8A23C"),track=1.6)
para("Sumit K. Kundu of FIU is an author on both Contractor (2003) and Arregle (2021). Eighteen years apart, the same question about performance, still unresolved.",
     M+22,244,W-2*M-44,DISPI,16,WHITE,lead=21)

conn=[("3 SEP · ENTRY MODE","If Stage 1 is negative, mode choice is a decision about how much of that cost to absorb at once."),
      ("24 SEP · INSTITUTIONS","CAGE is a pre-Hofstede way of saying what that session says with formal distance measures."),
      ("RESIDENCY 1","Firm-specific advantages are what carry a firm through Stage 1 at all.")]
t=318
for k,v in conn:
    box(M,t,3,44,fill=HexColor("#C8A23C"))
    txt(k,M+16,t,MONOB,9.5,HexColor("#C8A23C"),track=1.3)
    para(v,M+16,t+15,W-2*M-36,BODY,13,HexColor("#B8C9D9"),lead=17); t+=52

rule(482,color=HexColor("#24405C"))
txt("github.com/AuditingAI/Profile",M,494,MONO,10,HexColor("#6E8AA6"))
chrome(dark=True); c.showPage()

c.save()
print("wrote",out,"·",_n[0],"slides")
