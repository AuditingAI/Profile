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

# ═══ 1 · TITLE ═══════════════════════════════════════════════════════
ground(dark=True)
c.setFont(DISP,17); c.setFillColor(HexColor("#9FC4E4"))
c.drawString(M,y(46)-14,"Audit"); w1=c.stringWidth("Audit ",DISP,17)
c.setFont(DISPI,13); c.setFillColor(MUTE); c.drawString(M+w1,y(46)-14,"the")
w2=w1+c.stringWidth("the ",DISPI,13)
c.setFont(DISP,17); c.setFillColor(HexColor("#9FC4E4")); c.drawString(M+w2,y(46)-14,"Algorithm")

box(M,150,72,4,fill=HexColor("#C8A23C"))
eyebrow("Module 2 · GEB 7365 International Business",184,HexColor("#C8A23C"))
para("Internationalization and Performance",M,214,W-2*M-40,DISP,44,WHITE,lead=52)
rule(360,color=HexColor("#24405C"))
txt("DANIELA GARCIA AGUIRRE  ·  YASIR A. MALIK",M,384,MONOB,11,WHITE,track=1.8)
para("Contractor, Kundu & Hsu (2003) · Mezias (2002) · Ghemawat (2001) · Arregle et al. (2021)",
     M,412,W-2*M,BODY,13,HexColor("#8FA8BE"),lead=19)
chrome(dark=True)
c.showPage()

# ═══ 2 · THE SPINE ═══════════════════════════════════════════════════
ground()
eyebrow("The through-line",62)
title("These are not four topics.",96,36)
title("They are one diagnosis, four times.",140,36,NAVY)

box(M,204,W-2*M,74,fill=WARM,stroke=HexColor("#E4D3A8"),r=5)
para("At each stage the field measured the wrong thing — or measured one thing while believing it had measured another.",
     M+24,224,W-2*M-48,DISPI,19,INK,lead=26)

rows=[("CONTRACTOR","measured segments of one curve, reported them as different relationships",NAVY),
      ("MEZIAS","measured aggregate performance, believed it had measured foreignness",TEAL),
      ("GHEMAWAT","measured market size, believed it had measured opportunity",GOLD),
      ("ARREGLE","30 years, 220 studies, still “varied and at times incompatible findings”",WARN)]
t=306
for k,v,col in rows:
    box(M,t,4,26,fill=col)
    txt(k,M+18,t+3,MONOB,11,col,track=1.4)
    txt(v,M+150,t+3,BODY,15,BODYC)
    t+=38
chrome(); c.showPage()

# ═══ 3 · CONTRACTOR — THE CURVE ══════════════════════════════════════
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
p=c.beginPath(); first=True
for i in range(241):
    f=i/240.0; px=ox+aw*f; py=y(oy-ah*cy(f)*0.94)
    (p.moveTo(px,py) if first else p.lineTo(px,py)); first=False
c.drawPath(p)
for f0,f1,lab,col in [(0,.28,"1",NAVY),(.28,.72,"2",TEAL),(.72,1,"3",WARN)]:
    x1=ox+aw*f1
    if f1<1:
        c.setStrokeColor(HexColor("#DDE4EA")); c.setLineWidth(1); c.setDash(3,4)
        c.line(x1,y(oy),x1,y(oy-ah)); c.setDash()
    txt(lab,ox+aw*(f0+f1)/2,oy-ah+22,DISP,17,col,align="c")

sx=ox+aw+34
stages=[("1","Negative","liability of foreignness, learning costs",NAVY),
        ("2","Positive","scale, scope and learning outweigh cost",TEAL),
        ("3","Negative","cost of managing scattered operations",WARN)]
t=196
for n,sl,why,col in stages:
    txt(f"STAGE {n} — {sl.upper()}",sx,t,MONOB,10,col,track=1.2)
    para(why,sx,t+16,W-M-sx,BODY,13,BODYC,lead=17)
    t+=58
box(M,428,W-2*M,50,fill=SOFT,r=4)
para("Sample only the middle and you report a positive linear relationship. Sample the ends and you report an inverted U. The disagreement was partly artefactual.",
     M+20,442,W-2*M-40,DISPI,14,INK,lead=19)
chrome(); c.showPage()

# ═══ 4 · CONTRACTOR — THE SUB-FINDING ════════════════════════════════
ground()
eyebrow("Contractor, Kundu & Hsu (2003) — the practical finding",62)
title("Who over-expands, and why nobody notices.",96,32)

box(M,164,(W-2*M-20)/2,150,fill=WHITE,stroke=RULE,r=5)
box(M,164,(W-2*M-20)/2,5,fill=WARN)
txt("OVER-EXPAND MORE READILY",M+22,190,MONOB,10,WARN,track=1.4)
para("Knowledge-based service firms — advertising, market research, securities, publishing.",
     M+22,214,(W-2*M-20)/2-44,BODY,15,INK,lead=20)
para("Lower fixed-asset exposure, so the cost of one more market is easier to underwrite.",
     M+22,268,(W-2*M-20)/2-44,DISPI,13,MUTE,lead=18)

x2=M+(W-2*M-20)/2+20
box(x2,164,(W-2*M-20)/2,150,fill=WHITE,stroke=RULE,r=5)
box(x2,164,(W-2*M-20)/2,5,fill=TEAL)
txt("OVER-EXPAND LESS READILY",x2+22,190,MONOB,10,TEAL,track=1.4)
para("Capital-intensive firms — airlines, hotels, construction, retail.",
     x2+22,214,(W-2*M-20)/2-44,BODY,15,INK,lead=20)
para("Fixed assets make each additional market an expensive commitment.",
     x2+22,268,(W-2*M-20)/2-44,DISPI,13,MUTE,lead=18)

box(M,342,W-2*M,74,fill=WARM,stroke=HexColor("#E4D3A8"),r=5)
txt("THEIR WORDS",M+24,362,MONOB,10,GOLD,track=1.6)
para("“Few companies possess the managerial tools that would tell them when they have over-internationalized.”",
     M+24,384,W-2*M-48,DISPI,19,INK,lead=25)
para("That turns a JIBS paper into a contribution to practice, not only to theory — and it is the line to say out loud.",
     M,436,W-2*M,BODY,14,BODYC,lead=19)
chrome(); c.showPage()

# ═══ 5 · ARREGLE ═════════════════════════════════════════════════════
ground()
eyebrow("Arregle, Chirico, Kano, Kundu, Majocchi & Schulze (2021) · JIBS 52",62)
title("Thirty years later. Same question. Still unresolved.",96,32)

stats=[("220","studies reviewed"),("30","years"),("7","IB themes"),("7th","is Contractor's question")]
bw=(W-2*M-36)/4
for i,(v,k) in enumerate(stats):
    x=M+i*(bw+12)
    box(x,164,bw,84,fill=WHITE,stroke=RULE,r=5)
    txt(v,x+bw/2,182,DISP,30,NAVY if i<3 else WARN,align="c")
    txt(k,x+bw/2,224,MONOB,9,MUTE,align="c",track=1.0)

box(M,274,W-2*M,62,fill=SOFT,r=4)
txt("VERBATIM",M+22,292,MONOB,10,NAVY,track=1.6)
para("“…has offered varied and at times incompatible findings on how family ownership and management shape internationalization.”",
     M+22,312,W-2*M-44,DISPI,15,INK,lead=20)

para("The seven themes: scale · scope · entry mode · location · process · timing and rhythm · performance. "
     "Theme 7 is the multinationality–performance question asked of a different population, eighteen years on.",
     M,360,W-2*M,BODY,15,BODYC,lead=21)
box(M,414,W-2*M,62,fill=WARM,stroke=HexColor("#E4D3A8"),r=4)
para("Two hundred and twenty studies is not too few. A literature that stays incompatible at that volume is signalling a problem upstream of any single study.",
     M+22,432,W-2*M-44,DISPI,16,INK,lead=21)
chrome(); c.showPage()

# ═══ 6 · DANIELA — MEZIAS (placeholder) ══════════════════════════════
ground()
eyebrow("Daniela's half · Mezias (2002) · SMJ 23(3)",62,MUTE)
title("Liability of foreignness, isolated at last.",96,32,HOLD)
box(M,160,W-2*M,250,fill=None,stroke=HOLD,lw=1.5,r=6)
txt("DANIELA — YOUR SLIDE",W/2,186,MONOB,11,HOLD,align="c",track=2.0)
notes=["486 British, German and Japanese subsidiaries matched against 486 US-owned firms, same industries and cities",
       "The measure: US labour lawsuit judgments — “labor lawsuits only measure labor-related disadvantage”",
       "Transfer pricing does not contaminate it, which aggregate performance measures cannot claim",
       "Within the foreign subsample: staffing strategy, autonomy, affiliated firms, subsidiary age",
       "Employee plaintiffs won 78.9% of defamation, 70.0% of discrimination, 58.4% of wrongful discharge"]
t=218
for n in notes:
    c.setFillColor(HOLD); c.circle(M+28,y(t+8),2.5,fill=1,stroke=0)
    h=para(n,M+40,t,W-2*M-70,BODY,14,MUTE,lead=19); t+=h+8
para("Placeholder — Daniela builds this. Talking points supplied so the deck is complete either way.",
     M,432,W-2*M,DISPI,13,HOLD,lead=18)
chrome("Daniela Garcia Aguirre"); c.showPage()

# ═══ 7 · DANIELA — GHEMAWAT (placeholder) ════════════════════════════
ground()
eyebrow("Daniela's half · Ghemawat (2001) · HBR 79(8)",62,MUTE)
title("Distance is four things. Star TV solved one.",96,32,HOLD)
box(M,160,W-2*M,250,fill=None,stroke=HOLD,lw=1.5,r=6)
txt("DANIELA — YOUR SLIDE",W/2,186,MONOB,11,HOLD,align="c",track=2.0)
cage=[("C","Cultural — language, ethnicity, social norms, religion"),
      ("A","Administrative — colonial ties, currency, trade blocs, hostility"),
      ("G","Geographic — physical distance, borders, transport, climate"),
      ("E","Economic — consumer wealth, cost of resources, infrastructure")]
t=222
for L,d in cage:
    txt(L,M+34,t,DISP,20,HOLD)
    txt(d,M+66,t+4,BODY,14,MUTE); t+=32
para("Star TV: ~$825m paid 1993–95, ~$500m lost FY1996–99. Satellite delivery beat geographic distance. "
     "It was the only kind they had addressed.",M+34,354,W-2*M-70,DISPI,14,MUTE,lead=19)
para("Placeholder — Daniela builds this.",M,432,W-2*M,DISPI,13,HOLD,lead=18)
chrome("Daniela Garcia Aguirre"); c.showPage()

# ═══ 8 · THE COMPARISON ══════════════════════════════════════════════
ground()
eyebrow("Together",62)
title("Four designs, one problem.",96,32)
hdr=["","Contractor 2003","Mezias 2002","Ghemawat 2001","Arregle 2021"]
data=[["Type","Empirical, theory-building","Empirical, matched-pair","Practitioner framework","Systematic review"],
      ["Sample","US service-sector MNEs","486 foreign + 486 US","Cases, incl. Star TV","220 studies, 30 years"],
      ["Measure","Multiple DOI measures","Labour lawsuit judgments","CAGE distance","Synthesis"],
      ["Claim","M–P is sigmoid","LOF is isolable","Distance is four things","Findings incompatible"]]
cw=[92,(W-2*M-92)/4]*1
colw=(W-2*M-100)/4
t=160
for i,h in enumerate(hdr):
    x=M+(0 if i==0 else 100+(i-1)*colw)
    txt(h,x+(0 if i==0 else 6),t,MONOB,9,NAVY,track=1.1)
rule(t+18)
t+=28
for row in data:
    for i,cell in enumerate(row):
        x=M+(0 if i==0 else 100+(i-1)*colw)
        if i==0: txt(cell,x,t,MONOB,9,MUTE,track=1.1)
        else: para(cell,x+6,t-3,colw-12,BODY,12.5,INK,lead=15)
    rule(t+30,color=HexColor("#EAE6DE")); t+=44
box(M,398,W-2*M,74,fill=SOFT,r=4)
txt("THE THROUGH-LINE",M+22,416,MONOB,10,NAVY,track=1.6)
para("Every one of them made progress by changing what was measured — not by collecting more of the same thing.",
     M+22,438,W-2*M-44,DISPI,16,INK,lead=21)
chrome(); c.showPage()

# ═══ 9 · CONNECTIONS + THE CLOSER ════════════════════════════════════
ground(dark=True)
eyebrow("Forward, and one thing worth saying out loud",62,HexColor("#C8A23C"))
para("Where this goes next.",M,96,W-2*M,DISP,34,WHITE,lead=40)
conn=[("3 SEP · ENTRY MODE","If Stage 1 is negative, mode choice is a decision about how much of that early cost to absorb at once."),
      ("24 SEP · INSTITUTIONS","Ghemawat's CAGE is a pre-Hofstede way of saying what that session says with formal distance measures."),
      ("BACK TO RESIDENCY 1","Rugman and Verbeke's firm-specific advantages are what carry a firm through Stage 1 at all.")]
t=166
for k,v in conn:
    box(M,t,3,50,fill=HexColor("#C8A23C"))
    txt(k,M+18,t,MONOB,10,HexColor("#C8A23C"),track=1.4)
    para(v,M+18,t+18,W-2*M-40,BODY,14,HexColor("#B8C9D9"),lead=19); t+=66
box(M,376,W-2*M,96,fill=HexColor("#16293C"),stroke=HexColor("#24405C"),r=5)
txt("ACROSS THE ROOM",M+24,396,MONOB,10,HexColor("#C8A23C"),track=1.6)
para("Sumit K. Kundu of FIU is an author on both Contractor (2003) and Arregle (2021) — eighteen years apart, "
     "the same question about performance, still unresolved.",M+24,418,W-2*M-48,DISPI,17,WHITE,lead=23)
chrome(dark=True); c.showPage()

c.save()
print("wrote",out,"·",_n[0],"slides")
