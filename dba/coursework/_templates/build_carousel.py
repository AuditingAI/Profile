#!/usr/bin/env python3
"""
House carousel builder — Yasir A. Malik.  4:5 shareable slides, 1080 x 1350.

Palette and type from live.html.  Monochrome wordmark (academic work).
Usage:  python3 build_carousel.py <out.pdf>
"""
import sys, math
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

W, H = 1080, 1350
NAVY=HexColor("#1F4E79"); DEEP=HexColor("#0E2237"); GOLD=HexColor("#8A6410")
PAPER=HexColor("#FBFAF7"); INK=HexColor("#14171C"); MUTE=HexColor("#767D86")
RULE=HexColor("#D8D4CB"); SOFT=HexColor("#E9EFF6"); WARM=HexColor("#FBF6EA")
WHITE=HexColor("#FFFFFF"); BODYC=HexColor("#454B54"); TEAL=HexColor("#1C6B63")
WARN=HexColor("#8C3A1B"); LINE=HexColor("#C8D6E4")
DISP="Times-Bold"; DISPI="Times-Italic"; BODY="Times-Roman"
MONO="Courier"; MONOB="Courier-Bold"

out = sys.argv[1] if len(sys.argv)>1 else "carousel.pdf"
c = canvas.Canvas(out, pagesize=(W,H))
c.setTitle("Two Classes, One Week — GEB 7911 + GEB 7365")
c.setAuthor("Yasir A. Malik")

M = 78                       # margin
_pg = [0]

def y(v): return H - v       # top-down coords

def box(x,t,w,h,fill=None,stroke=None,lw=1,dash=None,r=None):
    c.setDash(dash) if dash else c.setDash()
    if fill: c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke); c.setLineWidth(lw)
    if r: c.roundRect(x,y(t+h),w,h,r,fill=1 if fill else 0,stroke=1 if stroke else 0)
    else: c.rect(x,y(t+h),w,h,fill=1 if fill else 0,stroke=1 if stroke else 0)
    c.setDash()

def txt(s,x,t,font=BODY,size=20,color=INK,align="l",track=0):
    c.setFont(font,size); c.setFillColor(color)
    if track: c._charSpace=track
    if align=="c": c.drawCentredString(x,y(t)-size*0.84,s)
    elif align=="r": c.drawRightString(x,y(t)-size*0.84,s)
    else: c.drawString(x,y(t)-size*0.84,s)
    c._charSpace=0

def para(s,x,t,w,font=BODY,size=20,color=BODYC,lead=None,align="l"):
    lead = lead or size*1.42
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
    c.setStrokeColor(color); c.setLineWidth(lw); c.setDash()
    c.line(x,y(t),x+w,y(t))

def wordmark(t=60,color=NAVY,small=False):
    s1,s2 = (26,19) if not small else (19,14)
    c.setFont(DISP,s1); c.setFillColor(color)
    c.drawString(M,y(t)-s1*0.84,"Audit")
    w1=c.stringWidth("Audit ",DISP,s1)
    c.setFont(DISPI,s2); c.setFillColor(MUTE)
    c.drawString(M+w1,y(t)-s1*0.84,"the")
    w2=w1+c.stringWidth("the ",DISPI,s2)
    c.setFont(DISP,s1); c.setFillColor(color)
    c.drawString(M+w2,y(t)-s1*0.84,"Algorithm")

def chrome(label, dark=False):
    """Footer: slide number, handle, section label."""
    _pg[0]+=1
    fg = HexColor("#7E93A8") if dark else MUTE
    rule(H-96, color=HexColor("#24405C") if dark else RULE)
    txt(label.upper(), M, H-78, MONOB, 13, fg, track=1.6)
    txt("github.com/AuditingAI/Profile", W/2, H-78, MONO, 13, fg, align="c")
    txt(f"{_pg[0]:02d}", W-M, H-78, MONOB, 13,
        NAVY if not dark else HexColor("#8FB6D8"), align="r")

def ground(dark=False):
    c.setFillColor(DEEP if dark else PAPER)
    c.rect(0,0,W,H,fill=1,stroke=0)

def eyebrow(s,t,color=GOLD):
    txt(s.upper(), M, t, MONOB, 15, color, track=2.4)

def title(s,t,size=54,color=INK,w=None):
    return para(s, M, t, w or (W-2*M), DISP, size, color, lead=size*1.12)

# ═══ 01 · COVER ═══════════════════════════════════════════════════════
ground(dark=True)
wordmark(72, HexColor("#9FC4E4"))
txt("github.com/AuditingAI/Profile", M, 108, MONO, 15, HexColor("#6E8AA6"))

box(M, 300, 96, 5, fill=HexColor("#C8A23C"))
eyebrow("Cohort 8.14  ·  Fall 2026  ·  Week 2", 350, HexColor("#C8A23C"))
para("Two classes, one week, two opposite methods.",
     M, 400, W-2*M-40, DISP, 70, WHITE, lead=80)

para("A working preparation deck for GEB 7911 Qualitative Research Methods "
     "and GEB 7365 International Business — the four philosophical assumptions, "
     "the interpretive frameworks, and the four papers on internationalization "
     "and performance.", M, 700, W-2*M-30, BODY, 24, HexColor("#B8C9D9"), lead=36)

rule(880, color=HexColor("#24405C"))
txt("YASIR A. MALIK", M, 906, MONOB, 17, WHITE, track=2.2)
para("DBA Candidate, Florida International University · Chapman Graduate School",
     M, 942, W-2*M, BODY, 21, HexColor("#8FA8BE"), lead=30)

box(M, 1010, W-2*M, 3, fill=HexColor("#24405C"))
txt("PRE-DISCUSSION  ·  IN-CLASS  ·  POST-DISCUSSION", M, 1046, MONOB, 15,
    HexColor("#C8A23C"), track=2.0)
chrome("Cover", dark=True)
c.showPage()

# ═══ 02 · WHO I AM ════════════════════════════════════════════════════
ground()
wordmark(72)
eyebrow("Who is presenting", 170)
title("Fifteen years auditing\nother people's judgment.", 210, 50)

rule(370)
rows=[("Now","DBA candidate, FIU Chapman. Researching what happens to an auditor's judgment when an AI system reaches a conclusion first."),
      ("Before","Citigroup and JPMorgan Chase — audit and risk, fifteen years."),
      ("Before that","Bank examiner, Florida Office of Financial Regulation."),
      ("The question","Not whether AI is accurate. Whether a professional who sees its answer first can still form an independent one.")]
t=410
for k,v in rows:
    txt(k.upper(), M, t, MONOB, 14, GOLD, track=1.8)
    h=para(v, M, t+30, W-2*M-20, BODY, 23, BODYC, lead=33)
    t += 30+h+34

box(M, 1020, W-2*M, 130, fill=SOFT, r=6)
txt("WHY THIS WEEK MATTERS TO ME", M+34, 1052, MONOB, 13, NAVY, track=1.8)
para("My last study specified 55 items and could not be fielded. This week is where I "
     "find out whether that was a recruitment problem or a philosophical one.",
     M+34, 1082, W-2*M-68, DISPI, 22, INK, lead=31)
chrome("Introduction")
c.showPage()

# ═══ 03 · THE WEEK ════════════════════════════════════════════════════
ground()
wordmark(72)
eyebrow("The week ahead", 170)
title("Tuesday asks how to listen.\nThursday asks how to measure.", 210, 46)

items=[("TUE 25 AUG","7:00–9:30pm  ·  Zoom","GEB 7911 — Qualitative Research Methods","Dr. Cristina Gonzalez","Week 2 · Assumptions, Frameworks, Study Design", NAVY),
       ("THU 27 AUG","7:00–9:30pm  ·  Zoom","GEB 7365 — International Business","Prof. William Newburry","Module 2 · Internationalization and Performance", TEAL)]
t=400
for tag,when,course,prof,topic,col in items:
    box(M, t, W-2*M, 200, fill=WHITE, stroke=RULE, r=8)
    box(M, t, 8, 200, fill=col)
    txt(tag, M+38, t+34, MONOB, 15, col, track=2.0)
    txt(when, W-M-38, t+34, MONO, 15, MUTE, align="r")
    para(course, M+38, t+70, W-2*M-76, DISP, 30, INK, lead=38)
    txt(prof, M+38, t+118, DISPI, 22, MUTE)
    rule(t+154, M+38, W-2*M-76)
    txt(topic, M+38, t+164, BODY, 21, BODYC)
    t += 232

box(M, t+10, W-2*M, 150, fill=WARM, stroke=HexColor("#E4D3A8"), r=6)
txt("THE THING WORTH NOTICING", M+34, t+42, MONOB, 13, GOLD, track=1.8)
para("These two courses want opposite methods from the same researcher in the same week. "
     "That is not a conflict to resolve. It is the clearest possible lesson in matching "
     "a method to a question.", M+34, t+74, W-2*M-68, DISPI, 22, INK, lead=31)
chrome("Orientation")
c.showPage()

# ═══ 04 · DIVIDER — TUESDAY ═══════════════════════════════════════════
ground(dark=True)
wordmark(72, HexColor("#9FC4E4"))
box(M, 380, 96, 5, fill=HexColor("#C8A23C"))
eyebrow("Pre-discussion  ·  Tuesday", 430, HexColor("#C8A23C"))
para("What Dr. Gonzalez\nis actually asking.", M, 490, W-2*M, DISP, 62, WHITE, lead=74)
para("The Week 2 memo asks two questions of one qualitative article: name the four "
     "philosophical assumptions its researchers made, and identify the interpretive "
     "framework they worked inside. Neither is usually stated. You reason backwards "
     "from the design.", M, 700, W-2*M-30, BODY, 24, HexColor("#B8C9D9"), lead=36)
box(M, 900, W-2*M, 150, fill=HexColor("#16293C"), stroke=HexColor("#24405C"), r=6)
txt("THE ARTICLE I CHOSE", M+34, 932, MONOB, 13, HexColor("#C8A23C"), track=1.8)
para("Gioia, D. A., & Chittipeddi, K. (1991). Sensemaking and sensegiving in strategic "
     "change initiation. Strategic Management Journal, 12(6), 433–448.",
     M+34, 964, W-2*M-68, DISPI, 22, WHITE, lead=31)
chrome("Section 1 of 2", dark=True)
c.showPage()

# ═══ 05 · FOUR ASSUMPTIONS — the matrix ═══════════════════════════════
ground()
wordmark(72)
eyebrow("Textbook Ch. 2, Table 2.1", 170)
title("Four questions every study\nanswers, stated or not.", 210, 46)

quad=[("ONTOLOGICAL","What is the nature of reality?","Multiple realities, or one?",NAVY),
      ("EPISTEMOLOGICAL","What counts as knowledge, and how close does the researcher stand?","Proximity, or distance?",TEAL),
      ("AXIOLOGICAL","What part do values play?","Declared, or controlled away?",GOLD),
      ("METHODOLOGICAL","What procedures follow from the answers above?","Emergent, or fixed?",WARN)]
gx, gy, bw, bh, gap = M, 400, (W-2*M-24)/2, 210, 24
for i,(k,q,alt,col) in enumerate(quad):
    x = gx + (i%2)*(bw+gap); t = gy + (i//2)*(bh+gap)
    box(x, t, bw, bh, fill=WHITE, stroke=RULE, r=8)
    box(x, t, bw, 6, fill=col)
    txt(k, x+26, t+38, MONOB, 14, col, track=1.6)
    para(q, x+26, t+70, bw-52, DISP, 23, INK, lead=30)
    para(alt, x+26, t+156, bw-52, DISPI, 20, MUTE, lead=27)

box(M, 880, W-2*M, 170, fill=SOFT, r=6)
txt("THE POINT OF THE EXERCISE", M+34, 912, MONOB, 13, NAVY, track=1.8)
para("You cannot opt out of these four. A study that never states them has still answered "
     "them — it has just let the instrument answer on its behalf. That is the difference "
     "between choosing a position and inheriting one.",
     M+34, 944, W-2*M-68, DISPI, 22, INK, lead=31)
chrome("The four assumptions")
c.showPage()

# ═══ 06 · GIOIA'S FOUR ANSWERS ════════════════════════════════════════
ground()
wordmark(72)
eyebrow("Gioia & Chittipeddi (1991) — reasoned from the design", 170)
title("They never state them.\nHere is what they did.", 210, 46)

ans=[("ONTOLOGICAL","Reality is multiple and participant-constructed. The change exists as the president's vision, the deans' reading of it, and the faculty's reading of the deans. Under a single-reality assumption that divergence would be error to minimise. Here it is the finding.",NAVY),
     ("EPISTEMOLOGICAL","One author embedded on site as participant-observer; the other deliberately kept from direct contact. Closeness generates understanding and also threatens it — so the team is built to hold both positions at once.",TEAL),
     ("AXIOLOGICAL","Values acknowledged rather than controlled away. The insider/outsider split is a reflexivity mechanism: instead of asserting neutrality, they install a colleague to interrogate the insider.",GOLD),
     ("METHODOLOGICAL","Inductive and emergent. First-order informant terms up to second-order theoretical constructs, across two phases, adapting as understanding develops.",WARN)]
t=390
for k,v,col in ans:
    box(M, t, 6, 118, fill=col)
    txt(k, M+26, t+4, MONOB, 14, col, track=1.6)
    para(v, M+26, t+34, W-2*M-40, BODY, 20.5, BODYC, lead=28)
    t += 154

box(M, t+4, W-2*M, 118, fill=WARM, stroke=HexColor("#E4D3A8"), r=6)
txt("QUESTION FOR THE ROOM", M+34, t+34, MONOB, 13, GOLD, track=1.8)
para("If the insider/outsider split is doing both the epistemological and the axiological "
     "work, is it one design choice or two?", M+34, t+64, W-2*M-68, DISPI, 22, INK, lead=30)
chrome("Gioia's answers")
c.showPage()

# ═══ 07 · THREE FRAMEWORKS ════════════════════════════════════════════
ground()
wordmark(72)
eyebrow("Textbook Ch. 2, Tables 2.2 – 2.3", 170)
title("Three frameworks that\nmatter to business research.", 210, 46)

cols=[("POST-POSITIVISM","Deductive",
       ["One reality, imperfectly apprehended","Researcher stands apart","Bias controlled and minimised",
        "Theory tested against data","Rigour = procedure followed"], NAVY),
      ("SOCIAL CONSTRUCTIVISM","Inductive",
       ["Multiple constructed realities","Researcher is close, and says so","Values declared, not removed",
        "Theory built up from participants","Rigour = route shown to reader"], TEAL),
      ("PRAGMATISM","Both",
       ["Reality is what works","Whatever distance the question needs","Values judged by consequences",
        "Method chosen to fit the problem","Rigour = does it answer the question"], GOLD)]
cw=(W-2*M-32)/3
for i,(name,mode,pts,col) in enumerate(cols):
    x=M+i*(cw+16)
    box(x, 390, cw, 500, fill=WHITE, stroke=RULE, r=8)
    box(x, 390, cw, 6, fill=col)
    para(name, x+20, 426, cw-40, DISP, 21, col, lead=26)
    txt(mode.upper(), x+20, 492, MONOB, 13, MUTE, track=1.6)
    rule(524, x+20, cw-40)
    tt=546
    for p in pts:
        c.setFillColor(col); c.circle(x+26, y(tt+9), 3, fill=1, stroke=0)
        h=para(p, x+38, tt, cw-58, BODY, 17.5, BODYC, lead=24)
        tt += h+14

box(M, 918, W-2*M, 160, fill=SOFT, r=6)
txt("WHAT THE TABLE CANNOT SHOW", M+34, 950, MONOB, 13, NAVY, track=1.8)
para("These are drawn as three clean columns. Real articles do not sit in one column — "
     "which is the whole of my next slide, and the thing I most want to argue in class.",
     M+34, 982, W-2*M-68, DISPI, 22, INK, lead=31)
chrome("The frameworks")
c.showPage()

# ═══ 08 · WHERE GIOIA SITS — the spectrum ═════════════════════════════
ground()
wordmark(72)
eyebrow("My argument for Tuesday", 170)
title("Constructivist ontology,\npost-positivist discipline.", 210, 48)

# spectrum
sx, sw, st = M+40, W-2*M-80, 470
c.setStrokeColor(RULE); c.setLineWidth(3); c.setDash()
c.line(sx, y(st), sx+sw, y(st))
# endpoints: hollow anchors, labels BELOW the axis
for frac,lab,col in [(0.0,"POST-POSITIVISM",NAVY),(0.5,"PRAGMATISM",GOLD),(1.0,"SOCIAL CONSTRUCTIVISM",TEAL)]:
    px=sx+sw*frac
    c.setFillColor(PAPER); c.setStrokeColor(col); c.setLineWidth(2.5)
    c.circle(px, y(st), 8, fill=1, stroke=1)
    txt(lab, px, st+26, MONOB, 12.5, col,
        align="c" if 0<frac<1 else ("l" if frac==0 else "r"), track=1.2)

# markers: filled dots ABOVE the axis, well clear of the endpoints
def marker(frac,label,sub,col):
    px=sx+sw*frac
    c.setStrokeColor(col); c.setLineWidth(2); c.setDash(3,3)
    c.line(px, y(st)+9, px, y(st)+62); c.setDash()
    c.setFillColor(col); c.circle(px, y(st), 6.5, fill=1, stroke=0)
    para(label, px, st-96, 400, DISP, 22, col, lead=27, align="c")
    para(sub, px, st-68, 400, DISPI, 17.5, MUTE, lead=23, align="c")
marker(0.82, "Its ontology", "multiple realities, built upward", TEAL)
marker(0.22, "Its procedures", "staged design, systematic coding", NAVY)

box(M, 620, W-2*M, 210, fill=WHITE, stroke=NAVY, lw=1.5, r=8)
txt("THE CLAIM", M+34, 652, MONOB, 13, NAVY, track=1.8)
para("Gioia and Chittipeddi are social constructivist in what they take reality to be, "
     "and they run procedural discipline underneath it that is ordinarily post-positivist. "
     "The rigour is not a contradiction of the constructivism. It is what makes the "
     "constructivism credible rather than merely asserted.",
     M+34, 684, W-2*M-68, BODY, 22, BODYC, lead=31)

box(M, 858, W-2*M, 196, fill=WARM, stroke=HexColor("#E4D3A8"), r=6)
txt("WHY I CARE — AND THE QUESTION I WILL ASK", M+34, 890, MONOB, 13, GOLD, track=1.8)
para("My own study committed to an ontology in which anchoring is a stable quantity you "
     "can ask \"how much\" about. I never argued for it — it arrived with the 55-item "
     "instrument. So: is a framework a label you select before fieldwork, or a position "
     "you can only describe afterwards?",
     M+34, 922, W-2*M-68, DISPI, 22, INK, lead=31)
chrome("The argument")
c.showPage()

# ═══ 09 · DIVIDER — THURSDAY ══════════════════════════════════════════
ground(dark=True)
wordmark(72, HexColor("#9FC4E4"))
box(M, 380, 96, 5, fill=HexColor("#C8A23C"))
eyebrow("Pre-discussion  ·  Thursday", 430, HexColor("#C8A23C"))
para("Four papers.\nOne diagnosis.", M, 490, W-2*M, DISP, 62, WHITE, lead=74)
para("Module 2 — Internationalization and Performance. Presenting with Daniela Garcia "
     "Aguirre. These are usually read as four contributions to one literature. They are "
     "better read as the same failure happening four times.",
     M, 660, W-2*M-30, BODY, 24, HexColor("#B8C9D9"), lead=36)
box(M, 830, W-2*M, 220, fill=HexColor("#16293C"), stroke=HexColor("#24405C"), r=6)
txt("THE SPINE", M+34, 862, MONOB, 13, HexColor("#C8A23C"), track=1.8)
para("At each stage the field measured the wrong thing, or measured one thing while "
     "believing it had measured another.", M+34, 894, W-2*M-68, DISP, 27, WHITE, lead=36)
para("That is not four topics. It is one diagnosis, four times.",
     M+34, 986, W-2*M-68, DISPI, 21, HexColor("#8FA8BE"), lead=28)
chrome("Section 2 of 2", dark=True)
c.showPage()

# ═══ 10 · THE FOUR PAPERS ═════════════════════════════════════════════
ground()
wordmark(72)
eyebrow("GEB 7365 · Module 2", 170)
title("What each one got wrong,\nand what it took to see it.", 210, 46)

papers=[("CONTRACTOR, KUNDU & HSU (2003)","JIBS 34(1)",
         "The literature reported positive, negative, U and inverted-U findings for one relationship. All four were segments of a single sigmoid curve.",
         "“Depending on which part of Figure 1 we examined, we can find linear, U-shaped, and inverted-U-shaped segments.”", NAVY),
        ("MEZIAS (2002)","SMJ 23(3)",
         "Liability of foreignness was accepted and never isolated, because performance measures aggregate everything. He abandons them for US labour lawsuit judgments — 486 foreign firms matched to 486 US firms.",
         "“Labor lawsuits only measure labor-related disadvantage.”", TEAL),
        ("GHEMAWAT (2001)","HBR 79(8)",
         "Country portfolio analysis reads GDP and consumer wealth — it measures market size and is used as though it measured opportunity. Star TV: $825m paid, ~$500m lost.",
         "“It ignores the costs and risks of doing business in a new market.”", GOLD),
        ("ARREGLE ET AL. (2021)","JIBS 52",
         "220 studies across three decades of family firm internationalization. Theme 7 is Contractor's question, eighteen years later.",
         "“Varied and at times incompatible findings.”", WARN)]
def _lines(sx, w, font, size):
    n=1; line=""
    for wd in sx.split():
        cand=(line+" "+wd).strip()
        if c.stringWidth(cand,font,size)<=w: line=cand
        else: n+=1; line=wd
    return n

t=388
for name,jr,body,quote,col in papers:
    bh = 30 + _lines(body, W-2*M-40, BODY, 20)*27 + 4 + _lines(quote, W-2*M-60, DISPI, 19)*26
    box(M, t, 6, bh, fill=col)              # bar sized to its own content
    txt(name, M+26, t, MONOB, 14, col, track=1.2)
    txt(jr, W-M, t, MONO, 14, MUTE, align="r")
    h=para(body, M+26, t+30, W-2*M-40, BODY, 20, BODYC, lead=27)
    para(quote, M+26, t+34+h, W-2*M-60, DISPI, 19, INK, lead=26)
    t += bh + 40
chrome("The four papers")
c.showPage()

# ═══ 11 · THE SIGMOID CURVE ═══════════════════════════════════════════
ground()
wordmark(72)
eyebrow("Contractor, Kundu & Hsu (2003), after Figure 1", 170)
title("Why the field disagreed\nfor thirty years.", 210, 48)

# axes
ox, oy, aw, ah = M+70, 760, W-2*M-140, 300
c.setStrokeColor(HexColor("#9AA4AE")); c.setLineWidth(1.5); c.setDash()
c.line(ox, y(oy), ox+aw, y(oy))                 # x
c.line(ox, y(oy), ox, y(oy-ah))                 # y
txt("DEGREE OF INTERNATIONALIZATION", ox+aw/2, oy+26, MONOB, 13, MUTE, align="c", track=1.4)
c.saveState(); c.translate(ox-30, y(oy-ah/2)); c.rotate(90)
c.setFont(MONOB,13); c.setFillColor(MUTE); c._charSpace=1.4
c.drawCentredString(0,0,"PERFORMANCE"); c._charSpace=0; c.restoreState()

# sigmoid: down, up, down  (three stages)
import math as _m
def _ease(t):                    # smoothstep — derivative 0 at both ends,
    return t*t*(3-2*t)           # so the segments join without a corner
def curve_y(f):
    # f in 0..1 → normalized height 0..1.  Three stages, smoothly joined.
    if f<0.28:   return 0.52 - 0.42*_ease(f/0.28)                 # stage 1 falling
    if f<0.72:   return 0.10 + 0.80*_ease((f-0.28)/0.44)          # stage 2 rising
    return 0.90 - 0.34*_ease((f-0.72)/0.28)                       # stage 3 falling
c.setStrokeColor(NAVY); c.setLineWidth(4); c.setDash()
pth=c.beginPath(); first=True
for i in range(0,241):
    f=i/240.0; px=ox+aw*f; py=y(oy-ah*curve_y(f)*0.94)-0
    if first: pth.moveTo(px,py); first=False
    else: pth.lineTo(px,py)
c.drawPath(pth)

# stage bands + labels
bands=[(0.0,0.28,"STAGE 1","Negative — liability of\nforeignness, learning costs",NAVY),
       (0.28,0.72,"STAGE 2","Positive — scale, scope\nand learning outweigh cost",TEAL),
       (0.72,1.0,"STAGE 3","Negative — cost of managing\nscattered operations",WARN)]
for f0,f1,lab,sub,col in bands:
    x0=ox+aw*f0; x1=ox+aw*f1
    c.setStrokeColor(HexColor("#DDE4EA")); c.setLineWidth(1); c.setDash(3,4)
    c.line(x1, y(oy), x1, y(oy-ah)); c.setDash()
    txt(lab, (x0+x1)/2, oy+58, MONOB, 14, col, align="c", track=1.4)
    yy=oy+84
    for ln in sub.split("\n"):
        txt(ln, (x0+x1)/2, yy, BODY, 16.5, MUTE, align="c"); yy+=22

box(M, 940, W-2*M, 128, fill=SOFT, r=6)
txt("THE MOVE THAT MAKES IT A CONTRIBUTION", M+34, 972, MONOB, 13, NAVY, track=1.8)
para("Sample only the middle and you report a positive linear relationship. Sample the "
     "ends and you report an inverted U. The disagreement was partly artefactual.",
     M+34, 1004, W-2*M-68, DISPI, 22, INK, lead=30)
chrome("Contractor · the curve")
c.showPage()

# ═══ 12 · CAGE ════════════════════════════════════════════════════════
ground()
wordmark(72)
eyebrow("Ghemawat (2001) — the CAGE framework", 170)
title("Distance is four things.\nStar TV solved one.", 210, 48)

cage=[("C","CULTURAL","Language, ethnicity, social norms, religion",NAVY),
      ("A","ADMINISTRATIVE","Colonial ties, currency, trade blocs, political hostility",TEAL),
      ("G","GEOGRAPHIC","Physical distance, borders, transport, climate",GOLD),
      ("E","ECONOMIC","Consumer wealth, cost and quality of resources, infrastructure",WARN)]
t=400
for letter,name,desc,col in cage:
    box(M, t, W-2*M, 118, fill=WHITE, stroke=RULE, r=8)
    box(M, t, 96, 118, fill=col, r=8)
    box(M+60, t, 36, 118, fill=col)
    txt(letter, M+48, t+36, DISP, 46, WHITE, align="c")
    txt(name, M+126, t+30, MONOB, 15, col, track=1.8)
    para(desc, M+126, t+60, W-2*M-260, BODY, 21, BODYC, lead=28)
    if letter=="G":
        tw=112
        box(W-M-tw-22, t+24, tw, 30, fill=WARM, stroke=HexColor("#E4D3A8"), r=4)
        txt("SOLVED", W-M-tw/2-22, t+31, MONOB, 12, GOLD, align="c", track=1.4)
        txt("the only one", W-M-tw/2-22, t+62, DISPI, 16, MUTE, align="c")
    t += 134

box(M, t+6, W-2*M, 216, fill=WARM, stroke=HexColor("#E4D3A8"), r=6)
txt("STAR TV  ·  NEWS CORPORATION, 1993–95", M+34, t+38, MONOB, 13, GOLD, track=1.8)
para("Roughly $825 million paid, on the reasoning that satellite delivery defeated "
     "geographic distance and English-language programming defeated the rest. Losses of "
     "approximately $500 million followed across fiscal 1996–99.",
     M+34, t+70, W-2*M-68, BODY, 21, BODYC, lead=29)
para("Geographic distance was the only kind they had actually addressed.",
     M+34, t+164, W-2*M-68, DISPI, 22, INK, lead=30)
chrome("Ghemawat · CAGE")
c.showPage()

# ═══ 13 · POST-DISCUSSION ═════════════════════════════════════════════
ground()
wordmark(72)
eyebrow("Post-discussion  ·  what I am taking away", 170)
title("The questions I want\nanswered by Friday.", 210, 48)

qs=[("TUESDAY","Is an interpretive framework a label you choose before fieldwork, or a position you can only describe afterwards?",NAVY),
    ("TUESDAY","If the insider/outsider design does both epistemological and axiological work, can reflexivity ever be a procedure rather than a stance?",NAVY),
    ("THURSDAY","If contradictory findings are partly artefacts of where you sampled a curve, what does replication mean in this literature?",TEAL),
    ("THURSDAY","Mezias made progress by abandoning aggregate measures. What is the equivalent move in audit judgment research?",TEAL),
    ("BOTH","A literature that cannot converge because it cannot agree on a measure has a methods problem, not a theory problem. Does mine?",GOLD)]
t=400
for tag,q,col in qs:
    box(M, t, 6, 108, fill=col)
    txt(tag, M+26, t, MONOB, 13, col, track=1.8)
    para(q, M+26, t+28, W-2*M-46, BODY, 21.5, BODYC, lead=29)
    t += 126

box(M, t+8, W-2*M, 168, fill=SOFT, r=6)
txt("HOW I WILL LOG THE ANSWERS", M+34, t+40, MONOB, 13, NAVY, track=1.8)
para("Every one of these goes into the public course record with the date and the source. "
     "If it came from the room, it is attributed to the room. If it is still open on "
     "Friday, it stays marked open.", M+34, t+72, W-2*M-68, DISPI, 22, INK, lead=31)
chrome("Post-discussion")
c.showPage()

# ═══ 14 · CLOSE ═══════════════════════════════════════════════════════
ground(dark=True)
wordmark(72, HexColor("#9FC4E4"))
box(M, 340, 96, 5, fill=HexColor("#C8A23C"))
para("Everything here is\nworking material,\nnot a finished claim.", M, 400, W-2*M, DISP, 56, WHITE, lead=68)
para("The readings are the professors'. The synthesis, the argument and any error in it "
     "are mine. Sources are cited on every slide that carries one, and anything still "
     "unresolved is marked as unresolved rather than smoothed over.",
     M, 640, W-2*M-30, BODY, 23, HexColor("#B8C9D9"), lead=34)

rule(800, color=HexColor("#24405C"))
txt("YASIR A. MALIK", M, 828, MONOB, 18, WHITE, track=2.2)
para("DBA Candidate · Florida International University, Chapman Graduate School\n"
     "Cohort 8.14 · Fall 2026", M, 866, W-2*M, BODY, 21, HexColor("#8FA8BE"), lead=30)

box(M, 950, W-2*M, 110, fill=HexColor("#16293C"), stroke=HexColor("#24405C"), r=6)
txt("THE FULL COURSE RECORD, OPEN", M+34, 980, MONOB, 13, HexColor("#C8A23C"), track=1.8)
txt("github.com/AuditingAI/Profile", M+34, 1010, MONO, 22, WHITE)
chrome("Close", dark=True)
c.showPage()

c.save()
print("wrote", out, "·", _pg[0], "slides")
