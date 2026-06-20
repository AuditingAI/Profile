"""
Build the actionable pilot-launch checklist as:
  1. Pilot_Action_Checklist.html (browser-clickable + print-styled)
  2. Pilot_Action_Checklist.pdf  (reportlab native — square checkboxes you can tick by hand)
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.platypus.flowables import Flowable

# ---------- structured task list ----------
# Each block: (day_label, date, header_color, tasks)
# Each task: (time_estimate, description, sub_items_optional)

PLAN = [
    ("DAY 0 — TONIGHT", "Friday, June 19, 2026 (evening)", colors.HexColor("#1a4e8a"), [
        ("0 min",   "Rest. Tomorrow is the focused build day.", []),
        ("2 min",   "Print this checklist + put it next to your coffee maker", []),
        ("1 min",   "Set an 8 AM alarm. Block calendar 9 AM – 6 PM for the build.", []),
    ]),
    ("DAY +1 — THE FOCUSED BUILD DAY", "Saturday, June 20, 2026", colors.HexColor("#b8650a"), [
        ("3 hr",    "9 AM – 12 PM — Reconcile Appendix A vs. IRB-approved instrument",
            ["Open both Word docs side by side",
             "Go construct-by-construct: TA, RA, AT, SAP, FR, IR, RPG, PMI, AJQ, APR, RAB",
             "For each item: same / wording-only revision / new (flag) — log in Revision Log",
             "Save the reconciled final item list"]),
        ("1 hr",    "12 PM – 1 PM — Lunch + walk away from screen", []),
        ("4 hr",    "1 PM – 5 PM — Build Qualtrics survey",
            ["Create project: \"Auditors' Professional Judgments and Audit Work Practices\"",
             "Block 1 — Informed Consent: paste IRB letter + Yes/No + screen-out on No",
             "Block 2 — Eligibility screeners (4 items) with screen-out branching",
             "Blocks 3–13 — 11 construct blocks × 5 items each (5-point Likert)",
             "Mark reverse-coded item per block",
             "Add 2 attention checks at specified positions",
             "Block 14 — Demographics (experience, role, firm, industry, credential, region)",
             "Survey Flow — wrap 11 construct blocks in Randomizer",
             "Survey Options — anonymize ON, IP OFF, progress bar ON, ballot-box stuffing OFF",
             "Add debrief screen (IRB protocol #, thank you)"]),
        ("1 hr",    "5 PM – 6 PM — Save, commit progress to repo, close laptop", []),
    ]),
    ("DAY +2 — PILOT LAUNCH + W06 CANVAS", "Sunday, June 21, 2026", colors.HexColor("#1e7a46"), [
        ("30 min",  "Preview-test both paths",
            ["Eligible path: complete fully, time it (target 15–20 min)",
             "Screen-out path: trigger ineligible response, confirm screen-out works"]),
        ("10 min",  "Publish + export test (check variable names + reverse-codes + no IP column)", []),
        ("5 min",   "Copy the Anonymous Link", []),
        ("20 min",  "Pick 6–10 LinkedIn audit contacts (≥2 yrs, long-term exposure)", []),
        ("30 min",  "Send personalized invitations with Qualtrics link + feedback link", []),
        ("10 min",  "Log each as P01–P10 in Pilot Participant Log (anonymous IDs only)", []),
        ("30 min",  "Draft Weekly Update W06 (stage format, progress-only, no repetition)", []),
        ("5 min",   "Upload W06 docx to Canvas + add submission comment + screenshot confirmation", []),
        ("0 min",   "🚀 Pilot is live. Stop. Sleep.", []),
    ]),
    ("DAY +3 — PILOT RUNNING", "Monday, June 22, 2026", colors.HexColor("#1e7a46"), [
        ("ongoing", "Log each pilot response: completion time + PF1–PF10 ratings", []),
        ("5 min",   "Send a one-line reminder to any non-responders", []),
    ]),
    ("DAY +4 — CLOSE PILOT + APPLY REVISIONS", "Tuesday, June 23, 2026", colors.HexColor("#b8650a"), [
        ("15 min",  "Confirm ≥6 completed responses", []),
        ("1 hr",    "Apply pilot decision rules",
            ["Clarity < 4/5 → revise wording only",
             "Construct-fit < 4/5 → review + flag advisor",
             "Audit-language fit complaint → revise phrasing only",
             "Time > 20 min → review redundancy, no removal without advisor",
             "IRB-scope feedback → HALT, escalate Topaz"]),
        ("30 min",  "Apply wording-only revisions in Qualtrics; log every change in Revision Log", []),
        ("15 min",  "Close the 6 launch-gating criteria in Decision Summary tab", []),
    ]),
    ("DAY +5 — CLOUDRESEARCH GOES LIVE 🚀", "Wednesday, June 24, 2026", colors.HexColor("#1a4e8a"), [
        ("30 min",  "Create CloudResearch account / project; load study listing", []),
        ("30 min",  "Configure screening (age 18+, audit role, ≥2 yrs, recurring-engagement exposure)", []),
        ("15 min",  "Set Qualtrics anonymous link as participant URL; set completion code route", []),
        ("10 min",  "Set compensation to $6.00 USD (within IRB fixed-comp language)", []),
        ("1 hr",    "🚀 Soft-launch 10–15 responses — DATA COLLECTION OFFICIALLY BEGINS", []),
    ]),
    ("DAYS +6 to +11 — FULL COLLECTION WEEK", "Thu Jun 25 – Tue Jun 30, 2026", colors.HexColor("#1e7a46"), [
        ("Thu",     "QA soft-launch batch (eligibility, attention checks, timing, duplicates, export)", []),
        ("daily",   "Monitor: response rate, exclusions, valid n count", []),
        ("Sun",     "Submit Weekly Update W07 — DATA COLLECTION PROGRESS (Dr. Rey's ask)", []),
        ("by Tue",  "Scale to n = 60–80 valid responses after cleaning rules applied", []),
    ]),
    ("DAYS +12 to +18 — CLEAN + ANALYZE", "Wed Jul 1 – Tue Jul 7, 2026", colors.HexColor("#1a4e8a"), [
        ("1 day",   "Close CloudResearch when n ≥ 60 valid; final export", []),
        ("1 day",   "Data cleaning: missing data, outliers, attention-check failures, duplicates", []),
        ("1 day",   "Descriptives: demographics, M/SD, frequencies, normality tests", []),
        ("2 days",  "EFA: correlation matrix, KMO, Bartlett, scree, parallel analysis, pattern matrix",
            ["PAF + varimax", "Loadings ≥ 0.40", "Cross-loadings ≤ 0.30"]),
        ("1 day",   "Reliability: Cronbach's α per construct (target ≥ 0.70)", []),
        ("1 day",   "PROCESS Model 4 mediation, 5,000 bootstraps, AJQ and APR paths", []),
        ("Sun",     "Submit Weekly Update W08 — analysis progress", []),
    ]),
    ("DAYS +19 to +28 — WRITE CHAPTER 5", "Wed Jul 8 – Fri Jul 17, 2026", colors.HexColor("#b8650a"), [
        ("2 days",  "Draft Chapter 5 (Results) — descriptives + EFA + reliability + regression + mediation", []),
        ("1 day",   "Update Chapter 6 (Discussion) with empirical findings", []),
        ("1 day",   "Revise Chapter 4 (Methodology) to match what was actually executed", []),
        ("1 day",   "Tighten Chapters 1–3 for consistency with results", []),
        ("Sun",     "Submit Weekly Update W09 — manuscript progress", []),
        ("1 day",   "Integrate any pilot revisions back into Appendix A instrument section", []),
        ("1 day",   "Buffer / advisor follow-up if needed", []),
    ]),
    ("DAYS +29 to +30 — SUBMIT 🏁", "Fri Jul 18 – Sat Jul 19, 2026", colors.HexColor("#b3261e"), [
        ("4 hr",    "Final proofread: full manuscript end-to-end, check references, check figure", []),
        ("1 hr",    "Format check: title page, TOC, references list, page numbers", []),
        ("30 min",  "Convert to PDF, verify it renders correctly", []),
        ("10 min",  "Upload to Canvas, add submission comment, screenshot confirmation", []),
        ("0 min",   "🏁 DONE. Stage 4a manuscript submitted.", []),
    ]),
]

# ---------- PDF rendering ----------
class CheckBox(Flowable):
    def __init__(self, size=10):
        super().__init__()
        self.size = size
        self.width = size
        self.height = size
    def draw(self):
        self.canv.setLineWidth(0.8)
        self.canv.rect(0, 0, self.size, self.size, stroke=1, fill=0)

styles = getSampleStyleSheet()
h_top = ParagraphStyle("h_top", parent=styles["Title"], fontSize=16, leading=20,
                       textColor=colors.HexColor("#1a1a1a"), spaceAfter=4, alignment=TA_LEFT)
h_sub = ParagraphStyle("h_sub", parent=styles["Normal"], fontSize=10, leading=12,
                       textColor=colors.HexColor("#5b6470"), spaceAfter=10, alignment=TA_LEFT)
day_h = ParagraphStyle("day_h", parent=styles["Heading2"], fontSize=12, leading=14,
                       textColor=colors.white, spaceAfter=0, alignment=TA_LEFT,
                       fontName="Helvetica-Bold")
day_d = ParagraphStyle("day_d", parent=styles["Normal"], fontSize=9, leading=11,
                       textColor=colors.HexColor("#e0e0e0"), spaceAfter=0, alignment=TA_LEFT)
task   = ParagraphStyle("task", parent=styles["Normal"], fontSize=10, leading=13,
                        textColor=colors.HexColor("#1a1a1a"), spaceAfter=2,
                        leftIndent=0, fontName="Helvetica-Bold")
task_t = ParagraphStyle("task_t", parent=styles["Normal"], fontSize=8, leading=10,
                        textColor=colors.HexColor("#5b6470"), fontName="Helvetica-Oblique")
sub    = ParagraphStyle("sub", parent=styles["Normal"], fontSize=9, leading=11,
                        textColor=colors.HexColor("#1a1a1a"), spaceAfter=1, leftIndent=14)
foot   = ParagraphStyle("foot", parent=styles["Normal"], fontSize=8, leading=10,
                        textColor=colors.HexColor("#5b6470"), alignment=TA_LEFT, spaceBefore=14)

def day_header_table(label, date, color):
    t = Table([[Paragraph(label, day_h), Paragraph(date, day_d)]],
              colWidths=[3.6*inch, 3.2*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), color),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING",(0,0), (-1,-1), 10),
        ("RIGHTPADDING",(0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING",(0,0),(-1,-1),6),
        ("ALIGN",      (1,0), (1,0), "RIGHT"),
    ]))
    return t

def task_row(est, desc):
    # checkbox | bold task with time estimate appended
    para = Paragraph(f"<b>{desc}</b> &nbsp; <font color='#5b6470'>({est})</font>", task)
    t = Table([[CheckBox(11), para]], colWidths=[0.30*inch, 6.5*inch])
    t.setStyle(TableStyle([
        ("VALIGN",     (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",(0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    return t

def sub_row(desc):
    para = Paragraph(desc, sub)
    # Indent by widening the first (spacer) col; box stays small at the right edge of it
    t = Table([["", CheckBox(9), para]], colWidths=[0.25*inch, 0.22*inch, 6.33*inch])
    t.setStyle(TableStyle([
        ("VALIGN",     (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",(0,0), (-1,-1), 0),
        ("RIGHTPADDING",(0,0),(-1,-1), 4),
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    return t

# ---------- assemble ----------
PDF = "Pilot_Action_Checklist.pdf"
doc = SimpleDocTemplate(PDF, pagesize=letter,
                        leftMargin=0.55*inch, rightMargin=0.55*inch,
                        topMargin=0.5*inch, bottomMargin=0.5*inch,
                        title="Pilot Action Checklist — Yasir A. Malik")

story = []
story.append(Paragraph("Pilot Run — Action Checklist", h_top))
story.append(Paragraph(
    "Yasir A. Malik · DBA Cohort 7.16 · GEB7913 — anchored Fri Jun 19, 2026 evening · "
    "30 days to Stage 4a manuscript milestone (Sat Jul 19, 2026)",
    h_sub))

for label, date, color, tasks in PLAN:
    block = [day_header_table(label, date, color), Spacer(1, 4)]
    for tup in tasks:
        if len(tup) == 3:
            est, desc, subs = tup
        else:
            est, desc, subs = tup[0], tup[1], []
        block.append(task_row(est, desc))
        for sub_desc in subs:
            block.append(sub_row(sub_desc))
        block.append(Spacer(1, 2))
    block.append(Spacer(1, 10))
    # Keep day block together when possible
    story.append(KeepTogether(block))

story.append(Paragraph(
    "Three milestones only — Sat Jun 20 (pilot link out) · Tue Jun 23 (CloudResearch live, data collection officially begins) · "
    "Sat Jul 19 (submit). Everything else is mechanics. "
    "Live source: dba/Pilot_Run_Status.md on the project branch.",
    foot))

doc.build(story)
print("wrote", PDF)

# ---------- printable/clickable HTML ----------
HTML = "Pilot_Action_Checklist.html"
html_parts = ['''<!doctype html>
<html lang="en"><head><meta charset="utf-8"/>
<title>Pilot Action Checklist — Yasir A. Malik</title>
<style>
  body { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
         max-width: 880px; margin: 24px auto; padding: 0 18px; color:#1a1a1a; line-height:1.4; }
  h1 { font-size: 22px; margin: 0 0 4px; }
  .sub { color:#5b6470; font-size:12px; margin-bottom:18px; }
  .day { color:white; padding:8px 12px; border-radius:6px; margin:18px 0 8px;
         display:flex; justify-content:space-between; align-items:baseline; }
  .day .lbl { font-weight:700; font-size:13px; }
  .day .dat { font-size:11px; opacity:0.9; }
  .task { display:flex; align-items:flex-start; gap:10px; margin:4px 0 2px; padding:4px 6px; border-radius:4px; }
  .task:hover { background:#f4f6fa; }
  .task input { margin-top:5px; transform: scale(1.2); cursor:pointer; }
  .task label { font-weight:600; font-size:13px; cursor:pointer; flex:1; }
  .task .est { color:#5b6470; font-weight:400; font-size:11px; margin-left:6px; }
  .sub-task { display:flex; align-items:flex-start; gap:8px; margin:2px 0; padding:2px 6px 2px 36px; }
  .sub-task input { margin-top:4px; cursor:pointer; }
  .sub-task label { font-size:12px; cursor:pointer; flex:1; }
  .done > label { text-decoration: line-through; color:#5b6470; }
  .foot { color:#5b6470; font-size:11px; margin-top:24px; padding-top:10px; border-top:1px solid #e5e8ee; }
  .reset { float:right; font-size:11px; color:#5b6470; cursor:pointer; border:1px solid #e5e8ee; padding:3px 7px; border-radius:4px; background:white; }
  @media print {
    body { max-width:none; margin:0; padding:0 0.4in; font-size:11px; }
    .task:hover { background:none; }
    .reset { display:none; }
    .day { page-break-inside:avoid; }
  }
</style>
</head><body>
<button class="reset" onclick="if(confirm(\\'Reset all checks?\\')){localStorage.removeItem(\\'pilot-checklist-v2\\');location.reload();}">Reset checks</button>
<h1>Pilot Run — Action Checklist</h1>
<div class="sub">Yasir A. Malik · DBA Cohort 7.16 · GEB7913 — anchored Fri Jun 19, 2026 evening · 30 days to Stage 4a manuscript milestone (Sat Jul 19, 2026)</div>
''']

color_map = {
    "#1a4e8a": "#1a4e8a", "#b8650a": "#b8650a",
    "#1e7a46": "#1e7a46", "#b3261e": "#b3261e",
}
cid = 0
for label, date, color, tasks in PLAN:
    hexc = color.hexval()[2:8] if hasattr(color, "hexval") else "1a4e8a"
    html_parts.append(f'<div class="day" style="background:#{hexc}"><span class="lbl">{label}</span><span class="dat">{date}</span></div>')
    for tup in tasks:
        if len(tup) == 3:
            est, desc, subs = tup
        else:
            est, desc, subs = tup[0], tup[1], []
        cid += 1
        html_parts.append(f'''<div class="task"><input type="checkbox" id="c{cid}"><label for="c{cid}">{desc}<span class="est">({est})</span></label></div>''')
        for sub_desc in subs:
            cid += 1
            html_parts.append(f'''<div class="sub-task"><input type="checkbox" id="c{cid}"><label for="c{cid}">{sub_desc}</label></div>''')

html_parts.append('''<div class="foot">Three milestones only — Sun Jun 21 (pilot link out) · Wed Jun 24 (CloudResearch live) · Sat Jul 19 (submit). Checks persist in your browser (localStorage). Use your browser's Print → Save as PDF for a paper copy.</div>
<script>
const K="pilot-checklist-v2";
const s=JSON.parse(localStorage.getItem(K)||"{}");
document.querySelectorAll('input[type=checkbox]').forEach(cb=>{
  if(s[cb.id]) cb.checked=true;
  cb.closest('.task,.sub-task').classList.toggle('done', cb.checked);
  cb.addEventListener('change',()=>{
    s[cb.id]=cb.checked; localStorage.setItem(K, JSON.stringify(s));
    cb.closest('.task,.sub-task').classList.toggle('done', cb.checked);
  });
});
</script>
</body></html>''')
open(HTML, "w", encoding="utf-8").write("\n".join(html_parts))
print("wrote", HTML)

import os
print("PDF size:", os.path.getsize(PDF), "bytes")
print("HTML size:", os.path.getsize(HTML), "bytes")
