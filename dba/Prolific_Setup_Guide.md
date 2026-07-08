---
TITLE: Prolific Setup Guide (Primary Recruiting Route)
AUTHOR: Yasir A. Malik (PID 1687105) — FIU DBA Cohort 7.16
DATE: July 2026
---

# Prolific — Setup Guide (Primary Recruiting Route)

**Why Prolific:** recommended by Dr. Rey. It prescreens participants by employment, industry, and occupation, is researcher-friendly, launches fast, and is cheaper than managed research. Goal: **n = 100 valid** US audit-professional responses.

**Live survey:** https://fiu.qualtrics.com/jfe/form/SV_3lae5xJsPcRfIN0

> **First reality check:** after you apply the filters (Step 3), Prolific shows the number of **eligible participants**. If US-based auditors are too few, note it — we then keep managed research as backup. But try Prolific first.

---

## STEP 1 — Create a researcher account (5 min)
1. Go to **app.prolific.com** → **Sign up** → choose **Researcher**.
2. Use **ymali001@fiu.edu** (academic email helps).
3. Verify email; complete the researcher profile (institution: Florida International University).

## STEP 2 — Create the study (10 min)
1. **New Study** → fill in:
   - **Title (participants see):** Audit Professional Judgment Survey (Academic Research)
   - **Description:** Brief anonymous academic survey for people with audit experience. ~15–20 minutes.
   - **Study type:** *"I'll use an external survey link"* (Qualtrics)
2. **Survey link:** paste your Qualtrics link and enable ID pass-through:
   `https://fiu.qualtrics.com/jfe/form/SV_3lae5xJsPcRfIN0?PROLIFIC_PID={{%PROLIFIC_PID%}}`
3. **How to record completion:** choose **"Redirect to a URL"** — Prolific gives you a **completion URL**; you'll paste it into Qualtrics' end-of-survey (Step 5).
4. **Estimated completion time:** 18 minutes. **Reward:** set so the hourly rate is fair — Prolific requires ~£6/hr min and recommends ~£9/hr. For 18 min, **~£3.50–£4.50 per participant** (it shows the £/hr live — aim for the green "Good/Great" zone).
5. **Devices:** allow mobile + desktop.

## STEP 3 — Prescreening (the key step) (10 min)
Use Prolific's filters to target audit professionals:
- **Country of residence:** **United States** (matches your IRB-approved population)
- **Fluent languages:** English
- **Employment status:** Employed full-time / part-time
- **Industry / Sector:** closest to **Accounting / Finance / Professional services**
- (If available) **Occupation / Job title** filters related to audit/accounting/finance
- Your **survey's own screeners** (S1–S5) do the precise audit-role filtering, so Prolific filters just need to get you in the right pool.

👉 **Check the "eligible participants" number.** If it comfortably exceeds 100, proceed. If it's low, screenshot it and message me — we adjust (loosen a filter or fall back to managed research).

## STEP 4 — Sample size + budget (5 min)
- **Participants:** start with a **soft-launch of 15**, then scale to **100**.
- **Budget estimate:** ~£3.50–£4.50 × 100 = **~£350–£450** + Prolific's service fee (~33%) ≈ **~£465–£600 total (~$600–$750)**.
- Fund via card. Load enough for the soft-launch first (~£70), then top up.

## STEP 5 — Wire the completion redirect into Qualtrics (10 min) — REQUIRED
So finishers get credited/paid:
1. In Qualtrics → **Survey Flow** → add an **End of Survey** element at the very end.
2. Edit → **Redirect to a URL** → paste **Prolific's completion URL** (from Step 2).
3. (Recommended) Capture the ID: Survey Flow → add **Embedded Data** field `PROLIFIC_PID` at the top so it records from the URL.
4. **Republish** the survey.

## STEP 6 — Soft-launch, review, scale
1. Launch the **15-participant soft-launch**.
2. Within hours, review: completion rate, attention-check pass rate, median time, any complaints.
3. If clean → **increase places to 100** and let it run.
4. Approve submissions promptly (Prolific expects timely approvals).

## STEP 7 — Monitor to n = 100
- Track responses in Qualtrics daily; exclude attention-check fails / speeders at cleaning.
- Prolific often fills fast (hours–days) when supply exists.

---

## Prolific vs. our backup
| | Prolific (primary) | CloudResearch Managed (backup) |
|---|---|---|
| Setup | DIY, fast | Full-service, slower |
| Cost (100) | ~$600–$750 | likely higher |
| Auditor reach | prescreened pool (check eligible count) | dedicated recruitment |
| Speed | hours–days | days+ |

**Plan:** launch Prolific first. If US-auditor supply is thin, keep managed research warm.

## Boundaries
Anonymous only · no PII · survey content stays fixed (peer-reviewed + IRB-approved) · Yasir approves all spend.
