from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
import math

W, H = 13.33*72, 7.5*72                       # 16:9, 960 x 540 pt
NAVY=HexColor("#1F4E79"); DEEP=HexColor("#0E2237"); GOLD=HexColor("#8A6410")
GOLDL=HexColor("#D2A73F"); PAPER=HexColor("#FBFAF7"); INK=HexColor("#14171C")
MUTE=HexColor("#767D86"); SOFT=HexColor("#E9EFF6"); WARM=HexColor("#FBF6EA")
WARMB=HexColor("#E4D3A8"); WHITE=HexColor("#FFFFFF"); RULE=HexColor("#D8D4CB")
TEAL=HexColor("#1C6B63"); WARN=HexColor("#8C3A1B"); BODYC=HexColor("#454B54")
DISP="Times-Bold"; DISPI="Times-Italic"; BODY="Times-Roman"; MONO="Courier"; MONOB="Courier-Bold"

def Y(v): return H - v*72
def X(v): return v*72

c = canvas.Canvas("Malik_GEB7365_IB_Field_Map.pdf", pagesize=(W,H))
c.setTitle("A Map of the International Business Field")
c.setAuthor("Yasir A. Malik")

def box(x,y,w,h,fill=None,stroke=None,lw=1,dash=None):
    if dash: c.setDash(dash)
    else: c.setDash()
    if fill: c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke); c.setLineWidth(lw)
    c.rect(X(x),Y(y+h),X(w),X(h),fill=1 if fill else 0,stroke=1 if stroke else 0)
    c.setDash()

def txt(s,x,y,font=BODY,size=11,color=INK,align="l",tracking=0):
    c.setFont(font,size); c.setFillColor(color)
    if tracking: c._charSpace = tracking
    if align=="c": c.drawCentredString(X(x),Y(y)-size*0.82,s)
    elif align=="r": c.drawRightString(X(x),Y(y)-size*0.82,s)
    else: c.drawString(X(x),Y(y)-size*0.82,s)
    c._charSpace = 0

def para(s,x,y,w,font=BODY,size=11,color=BODYC,lead=None):
    lead = lead or size*1.32
    c.setFont(font,size); c.setFillColor(color)
    words=s.split(); line=""; yy=Y(y)-size*0.82; maxw=X(w)
    for wd in words:
        t=(line+" "+wd).strip()
        if c.stringWidth(t,font,size)<=maxw: line=t
        else:
            c.drawString(X(x),yy,line); line=wd; yy-=lead
    if line: c.drawString(X(x),yy,line)
    return (Y(y)-yy)/72

def circ(cx,cy,r,fill=None,stroke=NAVY,lw=1.25,dash=None):
    if dash: c.setDash(dash)
    else: c.setDash()
    if fill: c.setFillColor(fill)
    c.setStrokeColor(stroke); c.setLineWidth(lw)
    c.circle(X(cx),Y(cy),X(r),fill=1 if fill else 0,stroke=1)
    c.setDash()

def ellip(cx,cy,rx,ry,fill=None,stroke=NAVY,lw=1.25):
    if fill: c.setFillColor(fill)
    c.setStrokeColor(stroke); c.setLineWidth(lw)
    c.ellipse(X(cx-rx),Y(cy+ry),X(cx+rx),Y(cy-ry),fill=1 if fill else 0,stroke=1)

def line(x1,y1,x2,y2,color=NAVY,lw=1.5,dash=None):
    c.setStrokeColor(color); c.setLineWidth(lw)
    c.setDash(dash) if dash else c.setDash()
    c.line(X(x1),Y(y1),X(x2),Y(y2)); c.setDash()

def arrow(x1,y1,x2,y2,color=NAVY,lw=2,head=0.09,dash=None):
    line(x1,y1,x2,y2,color,lw,dash)
    a=math.atan2(-(Y(y2)-Y(y1)),X(x2)-X(x1))
    c.setFillColor(color)
    p=c.beginPath(); p.moveTo(X(x2),Y(y2))
    for s in (2.6,-2.6):
        p.lineTo(X(x2)-X(head)*math.cos(a-s*0.28)*1.0, Y(y2)+X(head)*math.sin(a-s*0.28))
    p.close(); c.drawPath(p,fill=1,stroke=0)

def mark(dark=False):
    c.setFont(DISP,11); c.setFillColor(GOLDL if dark else NAVY)
    c.drawString(X(0.5),Y(0.40),"Audit ")
    wA=c.stringWidth("Audit ",DISP,11)
    c.setFont(DISPI,9); c.setFillColor(HexColor("#8C949E") if dark else MUTE)
    c.drawString(X(0.5)+wA,Y(0.40),"the ")
    wB=c.stringWidth("the ",DISPI,9)
    c.setFont(DISP,11); c.setFillColor(GOLDL if dark else NAVY)
    c.drawString(X(0.5)+wA+wB,Y(0.40),"Algorithm")

def footer(n):
    txt("Yasir A. Malik   ·   github.com/AuditingAI/Profile   ·   %s / 3"%n,
        0.5,7.14,MONO,8.5,MUTE)

# ══ PAGE 1 ══════════════════════════════════════════════
c.setFillColor(PAPER); c.rect(0,0,W,H,fill=1,stroke=0)
box(0,0,13.33,1.45,fill=DEEP); mark(True)
txt("GEB 7365  ·  after Chandra & Newburry (1997), Figure 1, p. 397",0.5,0.58,MONO,9,GOLDL,tracking=0.6)
txt("The Field Never Integrated",0.5,0.82,DISP,26,WHITE)
box(8.15,0.52,0.03,0.74,fill=GOLDL)
para("Run the maps with management split into its sub-fields and two things break — then a third integration point appears.",
     8.35,0.56,4.4,DISPI,11.5,HexColor("#DCE3EA"))

box(0.5,1.62,5.55,3.46,fill=WHITE,stroke=RULE)
txt("(A)",0.72,1.80,MONOB,9.5,NAVY,tracking=0.7); txt("The circle is too coarse",1.14,1.78,DISP,13.5,INK)
ellip(2.32,3.22,0.26,0.62); circ(2.70,2.62,0.34); circ(3.42,2.66,0.34); circ(2.48,3.88,0.32)
ellip(3.02,3.28,0.62,0.62,fill=SOFT); txt("IB",3.02,3.16,DISP,18,NAVY,align="c")
circ(3.32,3.55,0.26,stroke=TEAL); circ(3.48,3.68,0.22,stroke=TEAL); circ(3.56,3.82,0.19,stroke=TEAL)
txt("Economics",2.00,3.16,MONO,9,BODYC,align="r")
for t,x,y in [("Finance",2.70,2.04),("Accounting",3.42,2.06),("Marketing",2.16,4.30)]:
    txt(t,x,y,MONO,9,BODYC,align="c")
txt("MANAGEMENT, fanned",4.42,2.80,MONOB,8.5,TEAL,tracking=0.6)
for lb,ds,yy in [("STRAT","deep inside IB",3.06),("HR","straddles the edge",3.34),("OB","barely grazes it",3.62)]:
    circ(4.52,yy+0.05,0.055,fill=TEAL,stroke=TEAL,lw=0)
    txt(lb,4.64,yy,MONOB,8.5,TEAL); txt(ds,4.64,yy+0.15,MONO,7.5,MUTE)
para("One circle per discipline hides the real picture: strategy sits deep inside IB, HR partly, OB barely touches it.",
     0.72,4.66,5.1,BODY,10.5)

box(6.28,1.62,6.55,3.46,fill=WHITE,stroke=RULE)
txt("(B)",6.50,1.80,MONOB,9.5,NAVY,tracking=0.7); txt("The crossbars run both ways",6.92,1.78,DISP,13.5,INK)
for x,top,n in [(6.90,2.34,"ECON"),(7.80,2.46,"FIN"),(8.70,2.62,"ACCT"),(12.10,2.70,"MKTG")]:
    txt(n,x,top-0.22,MONOB,9,NAVY,align="c"); arrow(x,top,x,4.24)
txt("MGMT",10.55,2.10,MONOB,9,TEAL,align="c")
line(9.80,2.34,11.30,2.34,TEAL,1,(3,2))
arrow(9.86,2.42,9.86,4.24,TEAL); arrow(10.55,3.10,10.55,4.24,TEAL,1.8)
arrow(11.24,4.20,11.24,3.24,TEAL,1.8,dash=(3,2))
for t,x in [("strat",9.86),("HR",10.55),("OB",11.24)]: txt(t,x,4.30,MONO,8,TEAL,align="c")
def bar(x1,x2,y,col=NAVY):
    c.setFillColor(Color(col.red,col.green,col.blue,alpha=0.45)); c.setStrokeColor(col); c.setLineWidth(0.75)
    c.rect(X(x1),Y(y+0.12),X(x2-x1),X(0.12),fill=1,stroke=1)
bar(6.90,7.80,2.92); bar(7.80,8.70,3.24); bar(9.86,12.10,3.62,TEAL)
para("The dashed arrow runs upward: OB flowed back into management from IB, via Hofstede and GLOBE.",6.50,4.90,6.1,BODY,10,TEAL)
box(6.55,4.52,5.4,0.30,stroke=NAVY,lw=1.25,dash=(4,3))
txt("Minor IB field integration — only on strategy issues",9.25,4.60,MONO,8.5,NAVY,align="c")
txt("time",12.52,3.94,MONO,8,MUTE)

box(0.5,5.26,12.33,1.62,fill=WARM,stroke=GOLD,lw=2,dash=(5,4))
txt("THE THIRD INTEGRATION POINT",0.78,5.40,MONOB,8.5,GOLD,tracking=1.1)
para("Management gave IB the integral plan for operations. Nobody has written the integral plan for evidence.",
     0.78,5.60,9.4,DISP,14.5,INK)
para("Both maps describe integration as TOPICAL — disciplines meet where their subject matter overlaps, which is rare and accidental. There is a second kind. Every sub-field above becomes international at the same moment: when it must collect comparable evidence from specialists in more than one country. That is structural, and field-wide by construction.",
     0.78,6.06,9.4,BODY,10)
line(10.42,5.40,10.42,6.74,WARMB,1)
txt("6",10.66,5.52,DISP,34,GOLD)
txt("eligible per 100,000",10.66,6.10,MONO,8.5,MUTE); txt("measured, before fielding",10.66,6.28,MONO,8.5,MUTE)
footer(1); c.showPage()

# ══ PAGE 2 ══════════════════════════════════════════════
c.setFillColor(PAPER); c.rect(0,0,W,H,fill=1,stroke=0); mark(False)
txt("Six disciplines, thirteen shared boundaries — and two that do not exist",0.5,0.74,DISP,19,INK)
para("The relationships are consistent and the gaps are the finding. Drawn as a network rather than as overlapping circles, because six circles cannot hold these thirteen adjacencies without inventing regions that are not claimed.",
     0.5,1.10,9.6,DISPI,11,MUTE)

POS={"SCM":(3.40,2.14),"MKT":(2.28,2.78),"GM":(2.28,4.06),"IB":(3.40,4.70),"CSR":(4.52,4.06),"FIN":(4.52,2.78)}
FULL={"SCM":"Supply Chain","MKT":"Marketing","GM":"Gen. Mgmt","IB":"Int'l Business","CSR":"CSR","FIN":"Finance"}
EDGES=[("MKT","FIN"),("MKT","IB"),("MKT","GM"),("MKT","CSR"),("MKT","SCM"),("FIN","IB"),("FIN","GM"),
       ("FIN","CSR"),("FIN","SCM"),("IB","GM"),("IB","CSR"),("IB","SCM"),("GM","CSR")]
GAPS=[("GM","SCM"),("CSR","SCM")]
for a,b in EDGES:
    c.setStrokeColor(Color(NAVY.red,NAVY.green,NAVY.blue,alpha=0.5)); c.setLineWidth(1.1)
    c.line(X(POS[a][0]),Y(POS[a][1]),X(POS[b][0]),Y(POS[b][1]))
for a,b in GAPS: line(POS[a][0],POS[a][1],POS[b][0],POS[b][1],WARN,1.6,(5,3))
for k,(x,y) in POS.items():
    big = k in ("MKT","FIN","IB")
    circ(x,y,0.40,fill=NAVY if big else WHITE,stroke=WARN if k=="SCM" else NAVY,lw=1 if big else 1.6)
    txt(k,x,y-0.07,MONOB,10.5,WHITE if big else NAVY,align="c")
    txt(FULL[k],x,y+0.46,MONO,7.5,MUTE,align="c")
line(0.72,5.60,1.06,5.60,WARN,1.6,(5,3)); txt("no shared region",1.16,5.54,MONO,8.5,WARN)
circ(3.10,5.60,0.07,fill=NAVY,stroke=NAVY,lw=0); txt("overlaps all five",3.26,5.54,MONO,8.5,MUTE)

box(6.55,1.72,6.28,3.62,fill=WHITE,stroke=RULE)
txt("Every pairing, read off",6.82,1.94,DISP,13.5,INK)
KEYS=["MKT","FIN","IB","GM","CSR","SCM"]
AD={"MKT":{"FIN","IB","GM","CSR","SCM"},"FIN":{"MKT","IB","GM","CSR","SCM"},"IB":{"MKT","FIN","GM","CSR","SCM"},
    "GM":{"IB","CSR","MKT","FIN"},"CSR":{"GM","MKT","FIN","IB"},"SCM":{"MKT","FIN","IB"}}
CX,CY,CS=9.15,2.62,0.36
for j,k in enumerate(KEYS): txt(k,CX+j*CS+(CS-0.05)/2,CY-0.20,MONOB,8,NAVY,align="c")
for i,r in enumerate(KEYS):
    txt(r,CX-0.12,CY+i*CS+0.10,MONOB,8,WARN if r=="SCM" else NAVY,align="r")
    for j,cc in enumerate(KEYS):
        self_=r==cc; on=cc in AD[r]
        f = HexColor("#EDEAE3") if self_ else (NAVY if on else HexColor("#FBF0EB"))
        st = RULE if self_ else (NAVY if on else HexColor("#E0BCAE"))
        box(CX+j*CS,CY+i*CS,CS-0.05,CS-0.05,fill=f,stroke=st,lw=0.75)
        if not self_ and not on: txt("—",CX+j*CS+(CS-0.05)/2,CY+i*CS+0.10,MONO,10,WARN,align="c")
para("Marketing, Finance and International Business each touch all five others. General Management and CSR touch everything except Supply Chain. Supply Chain touches only those three central disciplines — the two blank cells are the whole structure of the map.",
     6.82,4.92,5.74,BODY,10)

box(0.5,5.86,12.33,1.04,fill=WARM,stroke=GOLD,lw=2,dash=(5,4))
txt("WHAT THE MAP STILL DOES NOT SAY",0.78,6.10,MONOB,9,GOLD,tracking=1.1)
para("It shows WHO touches WHOM, not what happens at the touch point. Name the intersections — international marketing, cross-border capital, global sourcing — and the same structural question returns: each one becomes international only when evidence must be gathered comparably in more than one country.",
     0.78,6.36,11.8,BODY,11.5)
footer(2); c.showPage()

# ══ PAGE 3 ══════════════════════════════════════════════
c.setFillColor(WHITE); c.rect(0,0,W,H,fill=1,stroke=0); mark(False)
txt("Questions I expect",0.5,0.84,DISP,26,INK)
txt("and the answers I am prepared to defend",0.5,1.30,DISPI,12.5,MUTE)
FAQ=[("Isn't a shared difficulty just a shared tool? Physics and biology both need microscopes.",
      "It is not a tool, it is a definition. What makes a study international is comparison across countries — and comparison requires comparable populations. The constraint sits at the definition of the field, not at its equipment."),
     ("Doesn't strategy already cover this?",
      "Strategy is topical integration — the disciplines meet because their subject matter overlaps. This is structural: it binds every sub-field the moment it goes cross-national, whether or not the topics have anything in common."),
     ("Where is the evidence?",
      "Screening a commercial research panel of 334,976 members against one specialist professional criterion returned roughly twenty eligible people — near six per hundred thousand. Visible on the platform's own configuration screen before any money was committed."),
     ("Which discipline does this belong to?",
      "None of them, and that is the argument. It is a constraint on the act of comparing, so it sits between the circles rather than inside one."),
     ("How would you test it?",
      "Replicate the prevalence check across countries for the same specialist role, and report the distribution. If reachability varies sharply by country, comparative designs in every one of these sub-fields rest on an assumption nobody states."),
     ("Are you claiming the existing maps are wrong?",
      "No. They are right about topical integration and honest that neither map resolves every classification difficulty. I am proposing a second axis they do not draw — not replacing theirs.")]
for i,(q,a) in enumerate(FAQ):
    col,row=i%2,i//2; x=0.5+col*6.42; y=1.62+row*1.80
    box(x,y,6.15,1.66,fill=PAPER,stroke=RULE)
    txt("Q",x+0.24,y+0.38,MONOB,10,GOLD)
    para(q,x+0.60,y+0.36,5.35,DISP,12,INK)
    txt("A",x+0.24,y+0.90,MONOB,10,NAVY)
    para(a,x+0.60,y+0.88,5.35,BODY,10.5)
footer(3); c.save()
print("wrote Malik_GEB7365_IB_Field_Map.pdf")
