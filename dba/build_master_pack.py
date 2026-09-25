"""
Build the DBA Master Action Pack — a clickable, ADD-friendly PDF covering
tonight (Sun Jun 21) through Final Manuscript (Sun Jul 19).

One major action per page. Big headings. Live hyperlinks. Step checkboxes.
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUT = "DBA_Master_Action_Pack.pdf"

# ---- colors ----
NAVY    = HexColor("#1A4E8A")
ORANGE  = HexColor("#B8650A")
GREEN   = HexColor("#1E7A46")
GREY    = HexColor("#5A6068")
LIGHT   = HexColor("#F4F6F9")
WARNBG  = HexColor("#FFF8E1")
GOODBG  = HexColor("#E9F7EF")

# ---- styles ----
ss = getSampleStyleSheet()

def style(name, **k):
    base = ss["Normal"]
    kw = dict(name=name, fontName=k.pop("font", "Helvetica"),
              fontSize=k.pop("size", 11), leading=k.pop("leading", 14),
              textColor=k.pop("color", black), alignment=k.pop("align", TA_LEFT),
              spaceAfter=k.pop("after", 6), spaceBefore=k.pop("before", 0),
              leftIndent=k.pop("li", 0))
    kw.update(k)
    return ParagraphStyle(**kw)

H_DAY   = style("HDay",  font="Helvetica-Bold", size=10, color=GREY, after=2)
H_TITLE = style("HT",    font="Helvetica-Bold", size=24, color=NAVY, leading=28, after=4)
H_SUB   = style("HSub",  font="Helvetica-Bold", size=14, color=ORANGE, after=10)
H_SECT  = style("HSect", font="Helvetica-Bold", size=13, color=NAVY,  after=6, before=8)
BODY    = style("Body",  size=11, leading=15, after=6)
TIGHT   = style("Tight", size=10.5, leading=14, after=3)
STEP    = style("Step",  size=11.5, leading=15, font="Helvetica", after=4, li=14)
NOTE    = style("Note",  size=10, leading=13, color=GREY, after=4)
LINK    = style("Link",  size=10.5, leading=14, color=NAVY, after=4)
TLDR    = style("Tldr",  size=11, leading=15, font="Helvetica-Bold", color=GREEN, after=6)
WARN    = style("Warn",  size=11, leading=15, font="Helvetica-Bold", color=ORANGE, after=6)

def cb(text, body_style=STEP):
    """Checkbox bullet."""
    return Paragraph(f"<font name='Helvetica' size='14'>&#9744;</font>&nbsp;&nbsp;{text}",
                     body_style)

def link(text, url, size=11):
    return Paragraph(f'<a href="{url}" color="#1A4E8A"><u>{text}</u></a>',
                     style("L", size=size, color=NAVY))

def box(content_paras, fill=WARNBG, border=ORANGE):
    """Wrap a list of paragraphs in a shaded box."""
    t = Table([[content_paras]], colWidths=[6.6*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), fill),
        ("BOX",(0,0),(-1,-1), 1, border),
        ("LEFTPADDING",(0,0),(-1,-1), 12),
        ("RIGHTPADDING",(0,0),(-1,-1), 12),
        ("TOPPADDING",(0,0),(-1,-1), 10),
        ("BOTTOMPADDING",(0,0),(-1,-1), 10),
    ]))
    return t

def page_header(label, title):
    return [
        Paragraph(label, H_DAY),
        Paragraph(title, H_TITLE),
        Spacer(1, 6),
    ]

# ---- repo + reference URLs (all clickable) ----
REPO        = "https://github.com/AuditingAI/Profile/tree/claude/scholar-links-review-Plgk6/dba"
W06         = "https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Weekly_Update_W06_2026-06-21_FINAL.docx"
CRGUIDE     = "https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/CloudResearch_Setup_Guide.docx"
CR_DRAFT    = "https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/03_Recruitment_and_Pilot/YMalik_CloudResearch_Launch_Draft_READY_2026-06-01.docx"
PROTOCOL    = "https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/03_Recruitment_and_Pilot/YMalik_Informed_Pilot_Protocol_READY_2026-06-01.docx"
DASHBOARD   = "https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/dashboard.html"
CONNECT     = "https://connect.cloudresearch.com"
QUALTRICS   = "https://fiu.qualtrics.com"
CANVAS      = "https://fiu.instructure.com"
SCRIPT_GS   = "https://script.google.com"

# ---- doc ----
doc = SimpleDocTemplate(
    OUT, pagesize=LETTER,
    leftMargin=0.7*inch, rightMargin=0.7*inch,
    topMargin=0.6*inch, bottomMargin=0.6*inch,
    title="DBA Master Action Pack — Yasir A. Malik",
    author="Yasir A. Malik (PID 1687105) — FIU DBA Cohort 7.16",
)

story = []

# ========================================================================
# PAGE 1 — COVER / TL;DR
# ========================================================================
story += page_header("FIU DBA COHORT 7.16 — GEB7913 — PROF. DR. JUAN REY",
                     "Master Action Pack")
story.append(Paragraph(
    "Anchoring Bias in Long-Term Auditor Engagements — IRB-25-0462",
    style("Sub2", size=12, color=GREY, after=12)))

story.append(Paragraph("What this is", H_SECT))
story.append(Paragraph(
    "Everything you need to go from <b>tonight (Sun Jun 21)</b> through the "
    "<b>Final Manuscript deadline (Sun Jul 19)</b>. One action per page. "
    "Tap any blue underlined text to open the link. Tick the boxes as you finish.",
    BODY))

story.append(Paragraph("The four-week runway", H_SECT))
runway = [
    ["Due (Sun 11:59pm)", "Deliverable", "Critical action"],
    ["TONIGHT  Jun 21", "W06 weekly update", "Upload .docx to Canvas (page 2)"],
    ["Jun 28  (W07)",  "Data-collection progress", "CloudResearch live by Wed Jun 24"],
    ["Jul 5   (W08)",  "Scaling update",       "Push toward n = 40–60"],
    ["Jul 12  (W09)",  "Collection close",     "n = 60–80; cleaning starts"],
    ["Jul 19  (W10)",  "FINAL MANUSCRIPT",     "EFA results + discussion"],
]
t = Table(runway, colWidths=[1.4*inch, 1.85*inch, 3.35*inch])
t.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0), NAVY),
    ("TEXTCOLOR",(0,0),(-1,0), white),
    ("FONTNAME",(0,0),(-1,0), "Helvetica-Bold"),
    ("FONTSIZE",(0,0),(-1,-1), 10),
    ("ALIGN",(0,0),(-1,-1), "LEFT"),
    ("VALIGN",(0,0),(-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1), [white, LIGHT]),
    ("BACKGROUND",(0,1),(-1,1), GOODBG),
    ("FONTNAME",(0,1),(-1,1), "Helvetica-Bold"),
    ("BACKGROUND",(0,5),(-1,5), WARNBG),
    ("FONTNAME",(0,5),(-1,5), "Helvetica-Bold"),
    ("GRID",(0,0),(-1,-1), 0.5, GREY),
    ("LEFTPADDING",(0,0),(-1,-1), 8),
    ("RIGHTPADDING",(0,0),(-1,-1), 6),
    ("TOPPADDING",(0,0),(-1,-1), 7),
    ("BOTTOMPADDING",(0,0),(-1,-1), 7),
]))
story.append(t)
story.append(Spacer(1, 10))

story.append(Paragraph("Tonight, in order", H_SECT))
story.append(cb(f'<b>Action 1</b> — Upload <b>Weekly_Update_W06</b> to Canvas. <a href="{CANVAS}" color="#1A4E8A"><u>open Canvas</u></a> &nbsp;&nbsp;<font color="#5A6068">[page 2]</font>'))
story.append(cb(f'<b>Action 2</b> — Create CloudResearch account. <a href="{CONNECT}" color="#1A4E8A"><u>open Connect</u></a> &nbsp;&nbsp;<font color="#5A6068">[page 3]</font>'))
story.append(cb(f'<b>Action 3</b> — Load $120 into the wallet. &nbsp;&nbsp;<font color="#5A6068">[page 4]</font>'))
story.append(Spacer(1, 6))
story.append(box([
    Paragraph("<b>Time tonight: ~30 minutes total.</b> After Action 3 you stop. "
              "Mon/Tue/Wed work is on pages 5–9. You do not need to read those tonight.",
              BODY),
], fill=GOODBG, border=GREEN))

story.append(Spacer(1, 10))
story.append(Paragraph("Repository (everything lives here)", H_SECT))
story.append(link(REPO, REPO, size=10.5))
story.append(PageBreak())

# ========================================================================
# PAGE 2 — TONIGHT ACTION 1: CANVAS UPLOAD
# ========================================================================
story += page_header("TONIGHT — SUN JUN 21 — ACTION 1 of 3",
                     "Upload W06 to Canvas")
story.append(Paragraph("5 minutes. This is the only deadline item tonight.", H_SUB))

story.append(Paragraph("Steps", H_SECT))
canvas_link = '<a href="' + CANVAS + '" color="#1A4E8A"><u>fiu.instructure.com</u></a>'
story.append(cb(f'Open Canvas on your Pixel: {canvas_link}'))
story.append(cb("Sign in with your FIU credentials"))
story.append(cb("Go to <b>GEB7913</b> course"))
story.append(cb("Open <b>Week 6: Student Project Update</b> (or the open W5/W6 assignment)"))
story.append(cb("Tap <b>Submit Assignment</b> → <b>File Upload</b>"))
story.append(cb("Select <b>Weekly_Update_W06_2026-06-21_FINAL.docx</b> from your Downloads"))
story.append(cb("Tap <b>Submit</b>. Screenshot the confirmation screen."))
story.append(Spacer(1, 6))

story.append(Paragraph("If you don't have the file on your phone", H_SECT))
story.append(Paragraph(
    "Open this link in Chrome → tap the <b>Download</b> button (top-right of the GitHub view) "
    "→ then come back to Canvas:", BODY))
story.append(link(W06, W06, size=10))
story.append(Spacer(1, 8))

story.append(box([
    Paragraph("<b>What you are NOT doing tonight:</b> emailing Dr. Rey, posting to LinkedIn, "
              "or building Qualtrics. Just the Canvas upload, then CloudResearch sign-up.", BODY)
], fill=WARNBG, border=ORANGE))
story.append(PageBreak())

# ========================================================================
# PAGE 3 — TONIGHT ACTION 2: CLOUDRESEARCH SIGN-UP
# ========================================================================
story += page_header("TONIGHT — SUN JUN 21 — ACTION 2 of 3",
                     "Create CloudResearch account")
story.append(Paragraph("5 minutes. Free to sign up — you only pay when you launch.", H_SUB))

story.append(Paragraph("Steps", H_SECT))
story.append(cb(f'On Pixel Chrome → open <a href="{CONNECT}" color="#1A4E8A"><u>connect.cloudresearch.com</u></a>'))
story.append(cb("Tap <b>Sign Up</b>"))
story.append(cb("Choose <b>Researcher</b> (NOT Participant)"))
story.append(cb("Use your <b>FIU email</b> if active, otherwise yasiramalik@gmail.com"))
story.append(cb("Set a strong password. Save it in your password manager."))
story.append(cb("Verify the email link CloudResearch sends (check spam too)"))
story.append(cb("Organization: <b>Florida International University — DBA Program</b>"))
story.append(cb("Take a screenshot of the dashboard once you're in"))
story.append(Spacer(1, 6))

story.append(Paragraph("Why CloudResearch (your reference)", H_SECT))
story.append(Paragraph(
    "Dr. Rey specifically named CloudResearch as your primary recruiting platform. "
    "It pre-screens audit/finance professionals so you skip the eligibility-yield "
    "problem MTurk has.", BODY))
story.append(link(f"Open CloudResearch Launch Draft (already in repo) →", CR_DRAFT, size=10.5))
story.append(Spacer(1, 8))

story.append(box([
    Paragraph("<b>If you hit any wall</b> (verification email doesn't arrive, sign-up form asks "
              "for something weird) — stop, take a screenshot, message me. Don't fight the "
              "UI alone for more than 10 minutes.", BODY)
], fill=WARNBG, border=ORANGE))
story.append(PageBreak())

# ========================================================================
# PAGE 4 — TONIGHT ACTION 3: ADD FUNDS
# ========================================================================
story += page_header("TONIGHT — SUN JUN 21 — ACTION 3 of 3",
                     "Load $120 into CloudResearch")
story.append(Paragraph("10 minutes. Pre-funding now prevents a launch block Wed Jun 24.", H_SUB))

story.append(Paragraph("Why $120", H_SECT))
budget = [
    ["Phase", "N", "Pay/response", "Subtotal", "Platform fee (~20–35%)", "Load"],
    ["Soft-launch (tonight's load)", "15", "$6.00", "$90", "~$22–32", "$120"],
    ["Full launch (load later)",     "65", "$6.00", "$390", "~$95–137", "$520"],
    ["TOTAL study budget",           "80", "",     "$480", "",          "~$640"],
]
t = Table(budget, colWidths=[2.2*inch, 0.4*inch, 0.9*inch, 0.8*inch, 1.2*inch, 0.6*inch])
t.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0), NAVY),
    ("TEXTCOLOR",(0,0),(-1,0), white),
    ("FONTNAME",(0,0),(-1,0), "Helvetica-Bold"),
    ("FONTSIZE",(0,0),(-1,-1), 9.5),
    ("ALIGN",(1,0),(-1,-1), "CENTER"),
    ("ALIGN",(0,0),(0,-1), "LEFT"),
    ("VALIGN",(0,0),(-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1), [white, LIGHT]),
    ("BACKGROUND",(0,1),(-1,1), GOODBG),
    ("FONTNAME",(0,1),(-1,1), "Helvetica-Bold"),
    ("FONTNAME",(0,3),(-1,3), "Helvetica-Bold"),
    ("GRID",(0,0),(-1,-1), 0.5, GREY),
    ("LEFTPADDING",(0,0),(-1,-1), 5),
    ("RIGHTPADDING",(0,0),(-1,-1), 4),
    ("TOPPADDING",(0,0),(-1,-1), 6),
    ("BOTTOMPADDING",(0,0),(-1,-1), 6),
]))
story.append(t)
story.append(Spacer(1, 10))

story.append(Paragraph("Steps", H_SECT))
story.append(cb("In the CloudResearch dashboard, find <b>Billing</b> / <b>Add Funds</b> / <b>Wallet</b>"))
story.append(cb("Enter <b>$120</b>"))
story.append(cb("Pay with the card you're comfortable expensing"))
story.append(cb("Confirm balance shows $120 (give or take fees)"))
story.append(cb("Screenshot the wallet balance for your records"))
story.append(Spacer(1, 6))

story.append(box([
    Paragraph("<b>If the platform fee on screen differs from the table:</b> trust the screen. "
              "Adjust your top-up so the soft-launch (15 × $6 + fee) is fully covered.", BODY),
    Spacer(1, 4),
    Paragraph("<b>You are now done for tonight.</b> Sleep. Pages 5–9 are for Mon/Tue/Wed.", BODY),
], fill=GOODBG, border=GREEN))
story.append(PageBreak())

# ========================================================================
# PAGE 5 — MONDAY JUN 22: RECONCILIATION
# ========================================================================
story += page_header("MONDAY — JUN 22 — Day 1 of CloudResearch ramp",
                     "Reconcile Appendix A vs IRB instrument")
story.append(Paragraph("90 minutes. The single most important wording-quality step before Qualtrics.", H_SUB))

story.append(Paragraph("Goal", H_SECT))
story.append(Paragraph(
    "Make sure every item in Appendix A of the manuscript exactly matches the "
    "IRB-approved instrument (Updated Measurement Instrument – Malik, Y.docx). "
    "Any mismatch is logged, classified, and either fixed (wording-only) or "
    "escalated to advisor + IRB (substantive).", BODY))

story.append(Paragraph("Steps", H_SECT))
story.append(cb("Open <b>Research_Paper_YMalik_v4.docx</b> → jump to Appendix A"))
story.append(cb("Open the IRB-approved instrument side-by-side (split screen on desktop ideal)"))
story.append(cb("Go construct-by-construct. For each item, classify the delta:"))
story.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;<b>SAME</b> — no change needed.<br/>"
                       "&nbsp;&nbsp;&nbsp;&nbsp;<b>WORDING</b> — typo or phrasing tweak. Fix to match IRB. Log.<br/>"
                       "&nbsp;&nbsp;&nbsp;&nbsp;<b>SUBSTANTIVE</b> — changes meaning. <b>STOP.</b> Flag for advisor + IRB.",
                       BODY))
story.append(cb("Update Appendix A in the manuscript with the reconciled wording"))
story.append(cb("Log every WORDING/SUBSTANTIVE delta in the Pilot Revision Log workbook"))
story.append(cb("Commit + push the reconciled manuscript to the repo"))
story.append(Spacer(1, 8))

story.append(Paragraph("How to use AI for this (Comet/Claude on your Pixel)", H_SECT))
story.append(Paragraph(
    "Paste each construct's items side-by-side into Claude and ask: "
    "<i>'Classify each item as SAME / WORDING / SUBSTANTIVE. For WORDING, give me the IRB-aligned wording verbatim. "
    "For SUBSTANTIVE, explain what changed and why it needs IRB review.'</i> "
    "Then double-check Claude's classification yourself — you're the human in the loop.",
    BODY))
story.append(PageBreak())

# ========================================================================
# PAGE 6 — TUESDAY JUN 23: QUALTRICS BUILD
# ========================================================================
story += page_header("TUESDAY — JUN 23 — Day 2 of CloudResearch ramp",
                     "Build the survey in FIU Qualtrics")
story.append(Paragraph("Full day. This is the gate to launch Wednesday.", H_SUB))

story.append(Paragraph(f"Open Qualtrics", H_SECT))
story.append(link("fiu.qualtrics.com → sign in with FIU SSO", QUALTRICS, size=11))
story.append(Spacer(1, 6))

story.append(Paragraph("Build sequence (in this order)", H_SECT))
story.append(cb("<b>Block 1: Informed Consent</b> — paste the IRB-approved consent letter verbatim. Require acceptance to continue."))
story.append(cb("<b>Block 2: Eligibility screeners</b> (4 questions) — country, English fluency, audit role within 24mo, continuing engagement experience. Each with screen-out branching to the debrief."))
story.append(cb("<b>Blocks 3–13: Eleven construct blocks</b>, randomized order. 5 Likert items per construct. One reverse-coded item per construct."))
story.append(cb("<b>Embedded attention check #1</b> — place after block 4. Item: 'For quality, please select Agree.'"))
story.append(cb("<b>Embedded attention check #2</b> — place after block 8. Item: 'For quality, please select Disagree.'"))
story.append(cb("<b>Block 14: Demographics</b> — role, years of experience, firm size, country."))
story.append(cb("<b>Block 15: Open-text substantive check</b> — 'In your own words, describe a time you noticed an anchoring effect in audit work.'"))
story.append(cb("<b>Block 16: Debrief screen</b> + completion code (for CloudResearch redirect)"))
story.append(Spacer(1, 6))

story.append(Paragraph("Survey-level settings", H_SECT))
story.append(cb("Anonymous responses: <b>ON</b> &nbsp;|&nbsp; IP capture: <b>OFF</b>"))
story.append(cb("Prevent ballot-box stuffing (one response per browser): <b>ON</b>"))
story.append(cb("Progress bar: <b>ON</b> &nbsp;|&nbsp; Back button: <b>OFF</b>"))
story.append(cb("Page-level timing: <b>ON</b> on all construct blocks"))
story.append(cb("Survey expiry: <b>Jul 12, 2026 11:59 PM</b>"))
story.append(Spacer(1, 6))

story.append(Paragraph("Preview test (both paths!)", H_SECT))
story.append(cb("Run it as an eligible respondent — confirm full flow + redirect works"))
story.append(cb("Run it as an ineligible respondent — confirm screen-out fires"))
story.append(cb("Test on your Pixel AND a desktop browser"))
story.append(cb("Generate the <b>anonymous distribution link</b> — copy and save it. This is what goes into CloudResearch tomorrow."))
story.append(PageBreak())

# ========================================================================
# PAGE 7 — TUESDAY NIGHT: CLOUDRESEARCH STEPS 3-6
# ========================================================================
story += page_header("TUESDAY NIGHT — JUN 23",
                     "CloudResearch — build the project")
story.append(Paragraph("45 minutes. Project + screeners + soft-launch settings. Save as DRAFT — do not submit yet.", H_SUB))

story.append(Paragraph("Create the project", H_SECT))
story.append(cb("Dashboard → <b>Create New Study</b>"))
story.append(cb("Title participants see: <b>Audit Professional Judgment Survey — Academic Research (FIU)</b>"))
story.append(cb("Internal name: <b>YMalik_Anchoring_Bias_v1_SoftLaunch</b>"))
story.append(cb("Type: <b>External study</b>"))
story.append(cb("Paste the <b>anonymous Qualtrics link</b> from Tuesday's build"))
story.append(cb("Estimated time: <b>15–20 minutes</b> &nbsp;|&nbsp; Compensation: <b>$6.00 USD</b>"))
story.append(cb("IRB: <b>IRB-25-0462</b> + PI/approval info per IRB letter"))
story.append(Spacer(1, 6))

story.append(Paragraph("Screening filters (THE most important step)", H_SECT))
story.append(cb("Country: <b>United States</b>"))
story.append(cb("Language: <b>English — Fluent</b>"))
story.append(cb("Employment: <b>Full-time</b> or <b>Part-time</b>"))
story.append(cb("Industry: <b>Accounting / Auditing / Finance</b>"))
story.append(cb("Education: <b>Bachelor's degree or higher</b>"))
story.append(Spacer(1, 6))

story.append(Paragraph("Custom screener questions", H_SECT))
story.append(Paragraph(
    "<b>Q1.</b> Are you currently, or have you been within the last 24 months, employed in "
    "an audit-related role? &nbsp;&nbsp;Yes / No (screen-out)", BODY))
story.append(Paragraph(
    "<b>Q2.</b> Have you personally worked on at least one continuing audit engagement? "
    "&nbsp;&nbsp;Yes / No (screen-out)", BODY))
story.append(Paragraph(
    "<b>Q3.</b> Confirm you are completing this on your own and have not seen it before. "
    "&nbsp;&nbsp;Yes / No (screen-out)", BODY))
story.append(Spacer(1, 6))

story.append(Paragraph("Soft-launch settings", H_SECT))
story.append(cb("Sample size: <b>15</b>"))
story.append(cb("Launch type: <b>Soft-launch / pilot batch</b> (if available)"))
story.append(cb("Auto-approve: <b>OFF</b> (you review the first 15 manually)"))
story.append(cb("Launch date: <b>Wed Jun 24, 2026</b>"))
story.append(cb("Quality controls: block duplicate IPs, repeat participants, bot detection"))
story.append(cb("<b>Save as DRAFT.</b> Do NOT submit for review yet."))
story.append(PageBreak())

# ========================================================================
# PAGE 8 — WEDNESDAY JUN 24: LAUNCH
# ========================================================================
story += page_header("WEDNESDAY — JUN 24 — LAUNCH DAY",
                     "Data collection officially begins")
story.append(Paragraph("Morning pre-flight + afternoon launch + evening watch.", H_SUB))

story.append(Paragraph("Morning pre-flight checklist (30 min)", H_SECT))
story.append(cb("Qualtrics link opens on <b>both</b> mobile and desktop"))
story.append(cb("Consent loads in full, blocks submission until accepted"))
story.append(cb("Both eligibility paths work (eligible → continues; ineligible → screen-out)"))
story.append(cb("Completion redirect URL from CloudResearch is pasted in Qualtrics end-of-survey"))
story.append(cb("Attention checks fire at the right points"))
story.append(cb("Compensation amount in CloudResearch matches IRB ($6.00)"))
story.append(cb("Wallet balance ≥ $120"))
story.append(Spacer(1, 6))

story.append(Paragraph("Launch (2 minutes)", H_SECT))
story.append(cb("Open project draft → <b>Submit for Review</b>"))
story.append(cb("CloudResearch reviews academic studies (usually <24h, sometimes minutes)"))
story.append(cb("Once approved → <b>Launch</b> / <b>Activate</b>"))
story.append(cb("Note launch time. Start the response watch."))
story.append(Spacer(1, 6))

story.append(Paragraph("First-hour watch (DO NOT WALK AWAY)", H_SECT))
story.append(Paragraph(
    "Watch the first 3–5 responses. If any of these red flags appears, <b>PAUSE THE STUDY</b> "
    "immediately:", BODY))
story.append(Paragraph(
    "&nbsp;&bull;&nbsp; Every response &lt; 90 seconds (means people are speeding)<br/>"
    "&nbsp;&bull;&nbsp; Every response fails an attention check<br/>"
    "&nbsp;&bull;&nbsp; Identical text in the open-text item (bot signature)<br/>"
    "&nbsp;&bull;&nbsp; All responses from one IP range",
    BODY))
story.append(Spacer(1, 6))

story.append(box([
    Paragraph("<b>By Wed evening:</b> you should have 5–15 responses landed. Auto-pause at N=15. "
              "Export from Qualtrics. Email yourself the count.", BODY)
], fill=GOODBG, border=GREEN))
story.append(PageBreak())

# ========================================================================
# PAGE 9 — THU/FRI/SAT/SUN: MONITOR + W07
# ========================================================================
story += page_header("THU JUN 25 → SUN JUN 28",
                     "Quality review + W07 submission")
story.append(Paragraph("Decision week: scale or revise.", H_SUB))

story.append(Paragraph("Thursday — review the soft-launch", H_SECT))
story.append(cb("Export Qualtrics responses → match to CloudResearch participant log"))
story.append(cb("Calculate: attention-check pass rate, median completion time, screen-out rate"))
story.append(cb("Check open-text item for substantive engagement (any blank/garbage responses?)"))
story.append(cb("Decision: <b>proceed to full launch</b> OR <b>pause for wording revisions</b>"))
story.append(Spacer(1, 6))

story.append(Paragraph("Friday — full-launch (if soft-launch passed)", H_SECT))
story.append(cb("Top up CloudResearch wallet to ~$640 total"))
story.append(cb("Increase sample target to <b>80</b>"))
story.append(cb("Unpause the study"))
story.append(cb("Monitor daily, but you don't need to babysit hour-by-hour"))
story.append(Spacer(1, 6))

story.append(Paragraph("Sunday Jun 28 — W07 submission to Canvas (this is the big one)", H_SECT))
story.append(Paragraph("Dr. Rey explicitly asked for <b>data-collection progress</b> in W07. Write it stage-by-stage:", BODY))
story.append(cb("<b>Stage 2a</b> — Qualtrics build complete, published, preview-tested"))
story.append(cb("<b>Stage 2b</b> — CloudResearch project live, screening filters active"))
story.append(cb("<b>Stage 3a</b> — Data collection: <b>n = X of 80 valid responses, attention-check pass rate Y%</b>"))
story.append(cb("Everything else: 'No update'"))
story.append(Spacer(1, 6))

story.append(box([
    Paragraph("<b>If by Sun Jun 28 you have ≥10 valid responses</b> — you have moved the project. "
              "W07 is meaningful regardless of total count. The professor wants progress, not perfection.",
              BODY)
], fill=GOODBG, border=GREEN))
story.append(PageBreak())

# ========================================================================
# PAGE 10 — JUL 5 / JUL 12 / JUL 19
# ========================================================================
story += page_header("JUL 5 → JUL 19",
                     "Scaling, closing, and the final manuscript")
story.append(Spacer(1, 4))

story.append(Paragraph("Sun Jul 5 — W08 scaling update", H_SECT))
story.append(cb("Target: <b>n ≥ 40</b> valid responses by this submission"))
story.append(cb("Add Stage 3b: 'Data cleaning protocol drafted' (attention-check failures, speeders, duplicates)"))
story.append(cb("If yield is weak: file W08 honestly + start MTurk backup launch draft"))
story.append(Spacer(1, 6))

story.append(Paragraph("Sun Jul 12 — W09 collection close", H_SECT))
story.append(cb("Target: <b>n = 60–80</b> valid responses, study closed"))
story.append(cb("Stage 3b: cleaning complete; final analytic sample documented"))
story.append(cb("Stage 3c: descriptive statistics computed (means, SDs, correlations matrix)"))
story.append(cb("Begin Stage 3d EFA prep — KMO + Bartlett's test + parallel analysis"))
story.append(Spacer(1, 6))

story.append(Paragraph("Sun Jul 19 — W10 FINAL MANUSCRIPT", H_SECT))
story.append(cb("Stage 3d: EFA complete — pattern matrix + factor loadings + reliability (α)"))
story.append(cb("Stage 4a: manuscript finalized with empirical results section + discussion"))
story.append(cb("Update Ch. 4 (Results) and Ch. 5 (Discussion) — the hypothesis sections in Ch. 3 don't change"))
story.append(cb("Citation pool re-verified (no broken references)"))
story.append(cb("Final PDF + .docx uploaded to Canvas"))
story.append(Spacer(1, 6))

story.append(box([
    Paragraph("<b>The lane is tight but achievable</b> if CloudResearch launches Wed Jun 24. "
              "Every day slipped on launch is a day stolen from analysis. That's why tonight's "
              "Actions 2 + 3 matter — not because the deadline is tonight, but because they "
              "unlock the runway.", BODY)
], fill=WARNBG, border=ORANGE))
story.append(PageBreak())

# ========================================================================
# PAGE 11 — QUICK REFERENCE: LINKS + WHO TO ASK
# ========================================================================
story += page_header("REFERENCE",
                     "All links + escalation paths")

story.append(Paragraph("Project repository (open this any time)", H_SECT))
story.append(link(REPO, REPO, size=10))
story.append(Spacer(1, 6))

story.append(Paragraph("Key documents (tap to open)", H_SECT))
story.append(link("• Weekly Update W06 (tonight's Canvas upload)", W06, size=10.5))
story.append(link("• CloudResearch Setup Guide (8-step walkthrough)", CRGUIDE, size=10.5))
story.append(link("• CloudResearch Launch Draft (study listing + filters)", CR_DRAFT, size=10.5))
story.append(link("• Informed Pilot Protocol", PROTOCOL, size=10.5))
story.append(link("• Interactive Project Dashboard", DASHBOARD, size=10.5))
story.append(Spacer(1, 8))

story.append(Paragraph("Live platforms (tap to open)", H_SECT))
story.append(link(f"• Canvas (FIU)", CANVAS, size=10.5))
story.append(link(f"• FIU Qualtrics", QUALTRICS, size=10.5))
story.append(link(f"• CloudResearch Connect", CONNECT, size=10.5))
story.append(link(f"• Google Apps Script (for the preview-test Form)", SCRIPT_GS, size=10.5))
story.append(Spacer(1, 8))

story.append(Paragraph("Who to ask (escalation)", H_SECT))
esc = [
    ["Topic", "Who", "When to escalate"],
    ["Survey wording — SUBSTANTIVE change", "Dr. Rey + IRB", "Before applying the change"],
    ["IRB protocol amendment", "FIU IRB / Topaz", "Before any scope-affecting move"],
    ["CloudResearch technical issue", "CloudResearch support chat", "After 10 min of UI struggle"],
    ["Qualtrics technical issue", "FIU Qualtrics support", "After 15 min stuck"],
    ["Canvas submission issue", "FIU course admin", "Before the deadline, not after"],
    ["Anything else / lost", "Message me (Claude in this thread)", "As soon as you feel stuck"],
]
t = Table(esc, colWidths=[2.3*inch, 2.1*inch, 2.3*inch])
t.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0), NAVY),
    ("TEXTCOLOR",(0,0),(-1,0), white),
    ("FONTNAME",(0,0),(-1,0), "Helvetica-Bold"),
    ("FONTSIZE",(0,0),(-1,-1), 9.5),
    ("ALIGN",(0,0),(-1,-1), "LEFT"),
    ("VALIGN",(0,0),(-1,-1), "MIDDLE"),
    ("ROWBACKGROUNDS",(0,1),(-1,-1), [white, LIGHT]),
    ("GRID",(0,0),(-1,-1), 0.5, GREY),
    ("LEFTPADDING",(0,0),(-1,-1), 6),
    ("RIGHTPADDING",(0,0),(-1,-1), 6),
    ("TOPPADDING",(0,0),(-1,-1), 6),
    ("BOTTOMPADDING",(0,0),(-1,-1), 6),
]))
story.append(t)
story.append(Spacer(1, 10))

story.append(Paragraph("Boundaries (Dr. Rey + IRB approved)", H_SECT))
story.append(Paragraph(
    "• No AI/LLM items in this survey (reserved for future research extension).<br/>"
    "• No employer / client / engagement-level / sensitive personal data requested.<br/>"
    "• Wording-and-flow-only revisions during pilot. Any scope change → escalate.",
    BODY))

story.append(Spacer(1, 14))
story.append(Paragraph("<i>End of Action Pack — keep this PDF on your home screen.</i>",
                       style("End", size=10, color=GREY, align=TA_CENTER)))

# ---- build ----
doc.build(story)
print("wrote", OUT)
