#!/usr/bin/env python3
"""Research status & roadmap deck — diagrams, not bullet lists.

FIU institutional identity. No consulting wordmark: this goes to professors.
"""
import pymupdf

FD = '/mnt/skills/examples/canvas-design/canvas-fonts/'
FONTS = {"ser": FD+"IBMPlexSerif-Regular.ttf", "serb": FD+"IBMPlexSerif-Bold.ttf",
         "seri": FD+"IBMPlexSerif-Italic.ttf", "mono": FD+"IBMPlexMono-Regular.ttf",
         "monob": FD+"IBMPlexMono-Bold.ttf"}
FF = {k: pymupdf.Font(fontfile=v) for k, v in FONTS.items()}

W, H, M = 960.0, 540.0, 54.0
NAVY  = (8/255, 30/255, 63/255)
GOLD  = (182/255, 134/255, 44/255)
PAPER = (0.988, 0.984, 0.972)
INK   = (0.078, 0.090, 0.110)
MUTED = (0.463, 0.490, 0.525)
RULE  = (0.847, 0.831, 0.796)
CARD  = (0.949, 0.941, 0.925)
BLUE  = (0.121, 0.306, 0.475)
RED   = (0.647, 0.196, 0.184)
GREEN = (0.129, 0.412, 0.353)

doc = pymupdf.open()

def page():
    p = doc.new_page(width=W, height=H)
    p.draw_rect(pymupdf.Rect(0,0,W,H), color=None, fill=PAPER)
    for k,v in FONTS.items(): p.insert_font(fontname=k, fontfile=v)
    return p

def T(p,x,y,s,f="ser",sz=10,c=INK):
    p.insert_text((x,y), s, fontname=f, fontsize=sz, color=c)

def TC(p,cx,y,s,f="ser",sz=10,c=INK):
    p.insert_text((cx - FF[f].text_length(s,sz)/2, y), s, fontname=f, fontsize=sz, color=c)

def BOX(p,x,y,w,s,f="ser",sz=9,c=INK,lead=1.32,align=0):
    r = pymupdf.Rect(x, y-sz, x+w, y-sz+400)
    left = p.insert_textbox(r, s, fontname=f, fontsize=sz, color=c, lineheight=lead, align=align)
    if left < 0: raise SystemExit(f"OVERFLOW {s[:44]!r} needs {-left:.0f}pt")
    return y - sz + (400-left)

def chrome(p, eyebrow, title, num, sub=None):
    p.draw_rect(pymupdf.Rect(0,0,W,4), color=None, fill=NAVY)
    T(p,M,44,"FLORIDA INTERNATIONAL UNIVERSITY","monob",7.0,NAVY)
    T(p,M,55,"Chapman Graduate School of Business  ·  Doctor of Business Administration","ser",6.8,MUTED)
    T(p,M,92,eyebrow,"monob",7.2,GOLD)
    T(p,M,120,title,"serb",21,NAVY)
    if sub: T(p,M,140,sub,"seri",10.2,MUTED)
    p.draw_line(pymupdf.Point(M,H-38), pymupdf.Point(W-M,H-38), color=RULE, width=0.7)
    T(p,M,H-24,"Yasir A. Malik  ·  DBA Cohort 8.14","mono",6.6,MUTED)
    T(p,W-M-FF["mono"].text_length(num,6.6),H-24,num,"mono",6.6,MUTED)

def card(p,r,fill=CARD,stroke=RULE,w=0.8):
    p.draw_rect(r, color=stroke, fill=fill, width=w)

def arrow(p,x0,y0,x1,y1,c=NAVY,w=1.1,head=5):
    p.draw_line(pymupdf.Point(x0,y0), pymupdf.Point(x1,y1), color=c, width=w)
    import math
    a = math.atan2(y1-y0, x1-x0)
    for s in (2.6, -2.6):
        p.draw_line(pymupdf.Point(x1,y1),
                    pymupdf.Point(x1-head*math.cos(a-s*0.35+0), y1-head*math.sin(a-s*0.35)),
                    color=c, width=w)

# ═════════════════════════════════ 1 · title
p = page()
p.draw_rect(pymupdf.Rect(0,0,W,H), color=None, fill=NAVY)
p.draw_rect(pymupdf.Rect(M,150,M+4,196), color=None, fill=GOLD)
T(p,M+16,168,"FLORIDA INTERNATIONAL UNIVERSITY","monob",8,(1,1,1))
T(p,M+16,182,"Chapman Graduate School of Business  ·  DBA Cohort 8.14","ser",8.4,(0.66,0.72,0.81))
T(p,M,258,"Where the research stands,","serb",38,(1,1,1))
T(p,M,300,"and what unlocks the next step.","serb",38,GOLD)
BOX(p,M,344,600,"A status read on the anchoring-bias programme: the model as built, the constraint "
    "that stopped it, the AI extension, and the five approvals that gate everything downstream.",
    "ser",11.5,(0.72,0.78,0.86))
p.draw_line(pymupdf.Point(M,412), pymupdf.Point(M+320,412), color=GOLD, width=1.2)
T(p,M,436,"Yasir A. Malik","serb",13,(1,1,1))
T(p,M,454,"28 August 2026","mono",8,(0.55,0.62,0.72))

# ═════════════════════════════════ 2 · the model
p = page()
chrome(p,"THE MODEL AS BUILT","Eleven constructs, sixteen hypotheses.","2",
       "Eight organisational interventions, two mediators, one outcome. 55 Likert items.")
IV = [("TA","Training &\nAwareness"),("RA","Rotation of\nAuditors"),("AT","Analytical\nTools"),
      ("SAP","Structured\nProcesses"),("FR","Feedback &\nReflection"),("IR","Independent\nReviews"),
      ("RPG","Regulatory\nGuidance"),("PMI","Metrics &\nIncentives")]
y0, bh, gap = 176, 30, 6
T(p,M,168,"EIGHT INTERVENTIONS","monob",6.4,GOLD)
BUS = 276.0
for i,(k,lab) in enumerate(IV):
    yy = y0 + i*(bh+gap)
    r = pymupdf.Rect(M, yy, M+152, yy+bh)
    card(p,r,fill=(1,1,1))
    p.draw_rect(pymupdf.Rect(M,yy,M+2.5,yy+bh), color=None, fill=BLUE)
    T(p,M+9,yy+12,k,"monob",6.4,BLUE)
    T(p,M+9,yy+22,lab.replace("\n"," "),"ser",7.2,INK)
    p.draw_line(pymupdf.Point(M+152, yy+bh/2), pymupdf.Point(BUS, yy+bh/2),
                color=(0.62,0.68,0.74), width=0.6)
# the collector bus, then one arrow into each mediator
p.draw_line(pymupdf.Point(BUS, y0+bh/2), pymupdf.Point(BUS, y0+7*(bh+gap)+bh/2),
            color=(0.62,0.68,0.74), width=0.8)
arrow(p, BUS, 242, 318, 242, c=BLUE, w=1.2, head=5)
arrow(p, BUS, 346, 318, 346, c=BLUE, w=1.2, head=5)

T(p,318,164,"TWO MEDIATORS","monob",6.4,GOLD)
MED = [("AJQ","Auditor Judgment Quality","Cognitive — careful, objective\nevaluation of independent evidence"),
       ("APR","Audit Process Rigor","Procedural — thorough, consistent,\ndisciplined execution")]
for i,(k,t,d) in enumerate(MED):
    yy = 200 + i*104
    r = pymupdf.Rect(318, yy, 318+228, yy+84)
    card(p,r,fill=(1,1,1),stroke=BLUE,w=1.0)
    T(p,332,yy+20,k,"monob",8,BLUE)
    T(p,332,yy+38,t,"serb",10,INK)
    for j,ln in enumerate(d.split("\n")):
        T(p,332,yy+54+j*11,ln,"ser",7.8,MUTED)
    arrow(p, 546, yy+42, 638, 252, c=BLUE, w=1.2, head=5)

T(p,638,164,"OUTCOME","monob",6.4,GOLD)
r = pymupdf.Rect(638,200,638+230,200+104)
card(p,r,fill=NAVY,stroke=GOLD,w=1.4)
T(p,654,224,"RAB","monob",8.4,GOLD)
T(p,654,244,"Reduction in","serb",12.5,(1,1,1))
T(p,654,261,"Anchoring Bias","serb",12.5,(1,1,1))
BOX(p,654,282,200,"Final judgments driven by current evidence, not initial reference points.",
    "ser",7.8,(0.70,0.76,0.85))
r2 = pymupdf.Rect(638,326,868,404)
card(p,r2,fill=(0.98,0.94,0.93),stroke=RED,w=1.0)
T(p,652,344,"THE MEASUREMENT PROBLEM","monob",6.4,RED)
BOX(p,652,362,202,"RAB is captured by self-report. It asks auditors to report how far judgment was "
    "driven by a reference point — the one thing the bias reliably prevents them from noticing.",
    "ser",7.6,INK)
T(p,M,H-52,"8 interventions × 2 mediators + direct paths = 16 hypotheses.  Each construct: 5 items, one reverse-coded.","mono",6.8,MUTED)

# ═════════════════════════════════ 3 · the funnel
p = page()
chrome(p,"WHAT ACTUALLY HAPPENED","The instrument worked. The population did not exist.","3",
       "Applying the eligibility criteria to a commercial research panel, July 2026.")
stages = [("334,976","panel members screened",760,BLUE),
          ("~20","matched the eligibility criteria",300,BLUE),
          ("23","raw responses recorded (Qualtrics, organic outreach)",190,GOLD),
          ("4","survived screening",96,RED)]
yy = 178
for i,(n,lab,wid,col) in enumerate(stages):
    x = M + (852-wid)/2
    r = pymupdf.Rect(x, yy, x+wid, yy+50)
    card(p,r,fill=(1,1,1),stroke=col,w=1.2)
    T(p,x+14,yy+31,n,"serb",21,col)
    T(p,x+14+FF["serb"].text_length(n,21)+14,yy+31,lab,"ser",9.4,MUTED)
    if i < 3:
        arrow(p, W/2, yy+50, W/2, yy+62, c=(0.70,0.72,0.74), w=0.9, head=4)
    yy += 62
r = pymupdf.Rect(M,428,W-M,494)
card(p,r,fill=NAVY,stroke=GOLD,w=1.2)
T(p,M+16,450,"PREVALENCE ≈ 6 PER 100,000","monob",7.2,GOLD)
T(p,M+16,470,"A survey at this prevalence needed a sampling frame of roughly 9.6 million. The panel held 3.5% of that.","ser",9.2,(0.88,0.91,0.95))
T(p,M+16,486,"Source: dba/03_Data/EXCLUSION_LOG_2026-07-22.md  ·  dba/RISK_QUANT/feasibility.py reproduces this end to end.","mono",6.4,(0.55,0.62,0.72))

# ═════════════════════════════════ 4 · the chain
p = page()
chrome(p,"THE EXTENSION","Three links. Only the first is a cognitive bias.","4",
       "What happens when the anchor stops being a workpaper and becomes a machine.")
LNK = [("L1","Automated anchoring","The anchor is system-generated — continuous, and arriving BEFORE the reviewer forms a view",
        "Automation bias","HOW MUCH · magnitude","Survey / experiment","Human cognitive bias",GREEN),
       ("L2","Sycophantic confirmation","The system AGREES with a position the auditor already stated, rather than challenging it",
        "Sycophancy","HOW · mechanism","Interviews — phenomenology","Model behaviour, not a bias",GOLD),
       ("L3","Recursive epistemic drift","Successive models reprocess earlier AI-influenced work; the evidentiary basis thins",
        "Model collapse","HOW, OVER TIME · process","Longitudinal / archival","Property of a system of models",RED)]
bw = (852 - 2*22)/3
for i,(k,t,d,phen,qt,meth,note,col) in enumerate(LNK):
    x = M + i*(bw+22)
    r = pymupdf.Rect(x,168,x+bw,392)
    card(p,r,fill=(1,1,1),stroke=col,w=1.3)
    p.draw_rect(pymupdf.Rect(x,168,x+bw,192), color=None, fill=col)
    T(p,x+12,185,k,"monob",9.5,(1,1,1))
    T(p,x+12,214,t,"serb",11.5,NAVY)
    yb = BOX(p,x+12,234,bw-24,d,"ser",8.2,INK)
    p.draw_line(pymupdf.Point(x+12,yb+8), pymupdf.Point(x+bw-12,yb+8), color=RULE, width=0.6)
    T(p,x+12,yb+26,"PHENOMENON","monob",5.8,MUTED); T(p,x+12,yb+38,phen,"serb",9,col)
    T(p,x+12,yb+58,"QUESTION TYPE","monob",5.8,MUTED); T(p,x+12,yb+70,qt,"mono",7.2,INK)
    T(p,x+12,yb+90,"METHOD THAT FITS","monob",5.8,MUTED); T(p,x+12,yb+102,meth,"ser",8.6,INK)
    T(p,x+12,376,note,"seri",7.6,MUTED)
    if i < 2: arrow(p, x+bw+3, 280, x+bw+19, 280, c=NAVY, w=1.2, head=5)
r = pymupdf.Rect(M,406,W-M,458)
card(p,r,fill=(0.97,0.96,0.92),stroke=GOLD,w=1.0)
T(p,M+16,426,"THE PRECISION THAT MATTERS WHEN A PROFESSOR PUSHES","monob",6.6,GOLD)
T(p,M+16,444,"Only L1 involves a human cognitive bias. L2 is model behaviour interacting with human judgment. L3 is a property of a system of models. Calling all three \"biases\" loses the argument.","ser",9,INK)
T(p,M,H-58,"L3 is deliberately NOT designed — it needs longitudinal access that does not exist. Stated as future work, not claimed.","mono",6.6,MUTED)

# ═════════════════════════════════ 5 · courses
p = page()
chrome(p,"HOW THIS TERM FEEDS THE DISSERTATION","Two courses, two arms, no double-submission.","5",
       "Each course builds a real piece. Neither collects a single response.")
LANES = [("GEB 7365 · INTERNATIONAL BUSINESS","Prof. William Newburry",
          "Feasibility as a design parameter","Requires a data-collection plan and explicitly NO collected data — the first time the recruitment constraint can be worked on without being blocked by it.",
          ["Study model + 2–3 hypotheses","Cross-national feasibility argument","Presentation 19 Sep · Paper 9 Oct"], BLUE),
         ("GEB 7911 · QUALITATIVE METHODS","Dr. Gonzalez",
          "The L2 phenomenology arm","The research proposal is 50% of that grade and IS the L2 design — protocol, sampling, coding plan, trustworthiness, audit trail.",
          ["Proposal presentations 6 Oct","Learning memos, weekly","Method: phenomenology, her recommendation"], GOLD)]
for i,(hdr,who,claim,body,bul,col) in enumerate(LANES):
    x = M + i*(426+16)
    r = pymupdf.Rect(x,168,x+426,364)
    card(p,r,fill=(1,1,1),stroke=col,w=1.2)
    p.draw_rect(pymupdf.Rect(x,168,x+426,4+168), color=None, fill=col)
    T(p,x+16,196,hdr,"monob",7,col)
    T(p,x+16,210,who,"ser",7.6,MUTED)
    T(p,x+16,236,claim,"serb",13,NAVY)
    yb = BOX(p,x+16,258,394,body,"ser",8.6,INK)
    for j,b in enumerate(bul):
        T(p,x+16,yb+22+j*15,"›","monob",8,col)
        T(p,x+28,yb+22+j*15,b,"ser",8.4,INK)
    arrow(p, x+213, 364, 480, 396, c=(0.66,0.70,0.75), w=0.8, head=0)
r = pymupdf.Rect(M,396,W-M,468)
card(p,r,fill=(0.98,0.94,0.93),stroke=RED,w=1.1)
T(p,M+16,416,"WHAT NEITHER COURSE DOES — SAID PLAINLY","monob",6.8,RED)
BOX(p,M+16,434,820,"Neither collects a response, so the achieved n is still four. Neither rebuilds Chapters 2 and 3 — "
    "those are still owed and Chapters 4–6 are overdue since 28 July. A course grade is not committee approval. "
    "And the 7365 topic STUDIES the feasibility problem; it does not solve it.","ser",8.8,INK)

# ═════════════════════════════════ 6 · approval gates
p = page()
chrome(p,"WHOSE APPROVAL UNLOCKS WHAT","Five gates. Four are open and one was never asked.","6",
       "The honest answer to \"which approval do I need to level up.\"")
G = [("DR. JUAN REY","Advisor · chair",
      "Chapters 4–6 · the Ch 2–3 rebuild · whether the survey arm relaunches · AI-use approval",
      "Ch 4–6 OVERDUE since 28 Jul. AI approval NEVER REQUESTED", RED, "THE BINDING ONE"),
     ("FIU IRB OFFICE","Office of Research Integrity",
      "Whether interviews are a modification or a new protocol · approval before ANY participant",
      "3 items unsubmitted · 1 never confirmed filed", RED, "BLOCKS ALL L2 DATA"),
     ("DR. GONZALEZ","GEB 7911",
      "The qualitative proposal — 50% of that grade · whether phenomenology fits the question",
      "Protocol drafted. She has never seen it", GOLD, "ASK EARLY"),
     ("PROF. NEWBURRY","GEB 7365",
      "Project topic approval before extensive work",
      "Zoom Tue 1 Sep — this one is in motion", GREEN, "IN MOTION"),
     ("THE COMMITTEE","Dissertation committee",
      "Proposal defence · AI-use review required by FIU UGS §3.2",
      "Composition [VERIFY] · UGS §3.2 review never requested", MUTED, "DOWNSTREAM")]
yy = 166
for name,role,gates,status,col,tag in G:
    r = pymupdf.Rect(M,yy,W-M,yy+58)
    card(p,r,fill=(1,1,1))
    p.draw_rect(pymupdf.Rect(M,yy,M+3.5,yy+58), color=None, fill=col)
    T(p,M+16,yy+19,name,"monob",8,NAVY)
    T(p,M+16,yy+31,role,"ser",7.2,MUTED)
    T(p,M+16,yy+49,tag,"monob",5.8,col)
    T(p,238,yy+19,"GATES","monob",5.8,MUTED)
    BOX(p,238,yy+31,380,gates,"ser",8.2,INK)
    T(p,642,yy+19,"STATUS","monob",5.8,MUTED)
    BOX(p,642,yy+31,218,status,"serb",8.2,col)
    yy += 62
T(p,M,H-58,"Two of the open items cost nothing: verifying the Topaz record, and asking the IRB office one question. A question is not a submission.","mono",6.6,MUTED)

# ═════════════════════════════════ 7 · improving the model
p = page()
chrome(p,"IMPROVING THE MODEL","Three known weaknesses, and what each one actually needs.","7",
       "Written down because a model whose weaknesses are named is defensible; one whose are not is fragile.")
Wk = [("1","Construct 11 measures the wrong thing",
       "RAB — the outcome — is self-report, reverse-coded. It asks auditors to report how far their judgment was driven by an anchor. That is precisely what anchoring prevents them from noticing.",
       "Either rename it honestly to PERCEIVED JUDGMENT DISCIPLINE, or replace it with a behavioural measure: a task with a planted anchor and an observable adjustment.",
       "This is the single most serious threat to the model's validity."),
      ("2","Automation bias and algorithm aversion contradict",
       "The literature supports BOTH — people over-trust algorithms and people under-trust them. L1 assumes over-trust. The model currently has no account of when each occurs.",
       "Specify the moderators rather than picking a side: task type, perceived expertise, stakes, and whether the system's output is visible before or after the human forms a view.",
       "Resolving this is a theoretical contribution in its own right."),
      ("3","The sample constraint is structural, not effort",
       "Six eligible per hundred thousand is not fixed by working harder or spending more. A survey design at this prevalence is not viable at any realistic budget.",
       "Two moves, both already underway: a qualitative design for L2 that twelve people CAN sustain, and treating feasibility as a parameter — the GEB 7365 project.",
       "The failure became the research question. That is the strongest thing here.")]
yy = 166
for n,t,prob,fix,note in Wk:
    r = pymupdf.Rect(M,yy,W-M,yy+102)
    card(p,r,fill=(1,1,1))
    p.draw_rect(pymupdf.Rect(M,yy,M+3.5,yy+102), color=None, fill=GOLD)
    T(p,M+16,yy+25,n,"serb",20,GOLD)
    T(p,M+40,yy+23,t,"serb",12.5,NAVY)
    T(p,M+40,yy+41,"THE PROBLEM","monob",5.8,RED)
    BOX(p,M+40,yy+53,368,prob,"ser",8.0,INK)
    T(p,500,yy+41,"WHAT IT NEEDS","monob",5.8,GREEN)
    BOX(p,500,yy+53,360,fix,"ser",8.0,INK)
    T(p,M+40,yy+94,note,"seri",7.6,MUTED)
    yy += 110

# ═════════════════════════════════ 8 · positioning
p = page()
chrome(p,"WHY THIS RESEARCH, AND WHY NOW","The question the AI-governance market has not answered.","8",
       "Where a doctorate on AI-influenced professional judgment actually sits.")
r = pymupdf.Rect(M,168,W-M,244)
card(p,r,fill=NAVY,stroke=GOLD,w=1.3)
T(p,M+20,196,"THE POSITION","monob",7,GOLD)
BOX(p,M+20,218,816,"Every framework now governing AI — SR 11-7, the NIST AI Risk Management Framework, the EU AI Act — "
    "assumes a competent human reviewer sits above the model. None of them measures whether that reviewer's "
    "judgment survives contact with it.","ser",11,(0.92,0.94,0.97))
COL = [("WHAT THE FRAMEWORKS ASSUME",["A human reviews model output","Review is independent of the model","Oversight is a control that works"],RED),
       ("WHAT THIS PROGRAMME ASKS",["Does the reviewer defer? (L1)","Does agreement stop the checking? (L2)","Does the evidence base thin? (L3)"],GOLD),
       ("WHY IT IS CREDIBLE HERE",["15 years audit — Citi, JPMorgan","Former state bank examiner","A study that failed honestly and said so"],GREEN)]
for i,(h,items,col) in enumerate(COL):
    x = M + i*(284+8)
    r = pymupdf.Rect(x,266,x+284,378)
    card(p,r,fill=(1,1,1),stroke=col,w=1.1)
    T(p,x+14,290,h,"monob",6.4,col)
    for j,it in enumerate(items):
        T(p,x+14,314+j*22,"›","monob",8,col)
        BOX(p,x+26,314+j*22,244,it,"ser",8.6,INK)
r = pymupdf.Rect(M,394,W-M,468)
card(p,r,fill=(0.97,0.96,0.92),stroke=GOLD,w=1.1)
T(p,M+20,416,"THE ONE-SENTENCE VERSION","monob",6.8,GOLD)
BOX(p,M+20,438,816,"Auditing is the profession that already knows how to test whether a control works. "
    "This programme turns that competence on the control everyone is now relying on and nobody has "
    "measured: the human being asked to check the machine.","serb",11.5,NAVY)

OUT = '/home/user/Profile/dba/00_Execution/RESEARCH_STATUS_DECK.pdf'
doc.save(OUT, garbage=3, deflate=True)
print("wrote", OUT, doc.page_count, "pages")
