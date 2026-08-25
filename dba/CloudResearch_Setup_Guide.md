# CloudResearch — Start-Here Guide (Pixel-10 friendly, ADD-friendly)

**Owner:** Yasir A. Malik
**Purpose:** Get CloudResearch from zero to soft-launch-ready by Wed Jun 24.
**Companion:** `03_Recruitment_and_Pilot/YMalik_CloudResearch_Launch_Draft_READY_2026-06-01.docx` (already in repo — your study-listing, screening, and quality filters live there)

> **One task at a time.** Do step N. Stop. Come back. Do step N+1. Don't read ahead.

---

## Before you start — what you need in hand

- [ ] **Anonymous Qualtrics link** (created once the Qualtrics build is published — Tue Jun 23 in the plan)
- [ ] **A funding source** — debit/credit card or wire. CloudResearch is **prepaid** (you load money first, then pay per response).
- [ ] **IRB protocol number** — IRB-25-0462 — keep it copy-paste handy.
- [ ] **Compensation amount** — **$6.00 USD per completed response** (within IRB-approved fixed compensation language).
- [ ] **Target sample size** — soft-launch **15**, full launch **n = 100 valid** (collect extra to net 100 after exclusions). *Budget ≈ 100+ × $6 ≈ $600+.*

---

## Step 1 — Create the account (5 minutes)

1. On your Pixel, open Chrome → go to **`connect.cloudresearch.com`**
2. Tap **Sign Up** → choose **Researcher** (not Participant)
3. Use your **FIU email** if you have one active; otherwise `yasiramalik@gmail.com`. The FIU email helps with the "academic research" trust signal.
4. Verify the email link CloudResearch sends.
5. When asked for organization, enter **Florida International University — DBA Program, Cohort 7.16**.

> ✅ Done? Take a screenshot of the dashboard for your records. Stop here. Move to Step 2 when you have a free 10 minutes.

---

## Step 2 — Add funds (10 minutes) — *do this BEFORE you build the study so launch isn't blocked*

CloudResearch charges **participant pay + platform fee**. Budget for the soft-launch:

| Phase | Responses | Pay/response | Subtotal | Platform fee (~20–35% — confirm on the funding screen) | Load this much |
|---|---|---|---|---|---|
| Soft-launch | 15 | $6.00 | $90 | ~$22–32 | **$120** |
| Full launch | 65 more | $6.00 | $390 | ~$95–137 | **$520** |
| **Total budget for the whole study** | 80 | | $480 | | **~$640** |

1. In the researcher dashboard, find **Billing / Add Funds / Wallet** (whichever label CloudResearch shows you).
2. Start with **$120** to clear the soft-launch. You can top up later.
3. Use a card you're comfortable expensing.

> ⚠️ If the actual fee on screen is different from the table above, **trust the screen, not the table.** Adjust your top-up.

---

## Step 3 — Create the project (10 minutes)

1. Dashboard → **Create New Study / Create Project**
2. **Study title** (what participants see):
   > **Audit Professional Judgment Survey — Academic Research (FIU)**
3. **Internal name** (only you see):
   > `YMalik_Anchoring_Bias_v1_SoftLaunch`
4. **Survey type:** *External study* (because we're routing to Qualtrics)
5. **Survey link:** paste your **anonymous Qualtrics link** (include the completion redirect or completion code per CloudResearch's instructions).
6. **Estimated completion time:** **15–20 minutes**
7. **Compensation:** **$6.00 USD**
8. **IRB info:** paste protocol **IRB-25-0462**, PI/approval per IRB letter.

> ✅ Save as draft. Don't submit yet.

---

## Step 4 — Screening (the most important step) (15 minutes)

This is where you filter for **audit professionals**, not the general population. CloudResearch's Connect platform has pre-screened occupational and demographic filters — use them.

**Required filters (turn ON):**
- Country: **United States** (matches IRB-approved population)
- Language: **English — Fluent**
- Employment status: **Employed full-time** OR **Employed part-time**
- Industry / Occupation: **Accounting / Auditing / Finance** (use the closest match available)
- Education: **Bachelor's degree or higher**

**Custom screener questions (add 2–3 inside CloudResearch):**

> Q1. Are you currently, or have you been within the last 24 months, employed in an audit-related role (external audit, internal audit, or audit support)?
> ○ Yes  ○ No (screen-out)

> Q2. Have you personally worked on at least one continuing audit engagement (multi-year engagement with the same client)?
> ○ Yes  ○ No (screen-out)

> Q3. Confirm you are completing this survey on your own, without sharing it, and you have not seen it before.
> ○ Yes, I confirm  ○ No (screen-out)

**Quality controls (already in the survey, but check the box on CloudResearch where available):**
- Block duplicate IPs
- Block repeat participants
- Enable bot/suspicious-activity detection
- Enable hand-coded review of open-text response

---

## Step 5 — Soft-launch settings (5 minutes)

1. **Sample size:** **15** (soft-launch only)
2. **Launch type:** **Soft-launch / pilot batch** if CloudResearch offers it; otherwise just set N=15 and pause after.
3. **Auto-approve:** **OFF** for soft-launch — you review manually.
4. **Estimated launch date:** **Wed Jun 24, 2026**.

> ✅ Save. Don't submit yet.

---

## Step 6 — Pre-launch review (the night before, Tue Jun 23)

Run through this checklist before clicking Launch:

- [ ] Qualtrics link opens, consent loads, and the survey starts on **a real mobile device** (your Pixel) AND a desktop browser.
- [ ] Eligibility branching works — try one "ineligible" path and confirm screen-out.
- [ ] Completion redirect URL from CloudResearch is pasted into Qualtrics' end-of-survey logic.
- [ ] Compensation amount, IRB number, and study title match the IRB-approved language.
- [ ] Funds in the CloudResearch wallet ≥ $120.
- [ ] Both attention checks fire and the page-timing controls are on.

---

## Step 7 — Launch (2 minutes, Wed Jun 24)

1. Open the project draft → **Submit for Review** (CloudResearch reviews academic studies before activation — typically <24h, sometimes minutes).
2. Once approved, click **Launch** (or **Activate**).
3. **Stay near the dashboard for the first hour.** Watch the first 3–5 responses come in. If anything looks off (every response is 90 seconds, every response fails attention checks, etc.) — **PAUSE THE STUDY** immediately and message me.

---

## Step 8 — Monitor (Wed Jun 24 evening → Thu morning)

After 15 responses land:

- Pause the study (it should auto-pause at N=15 since that's the limit).
- Export the responses from Qualtrics + match against CloudResearch's participant log.
- Check: attention-check pass rate, median completion time, screen-out rate.
- Decision: clean → unpause for full launch (target n=80) OR pause + revise wording.

This decision goes in **W07 (due Sun Jun 28)** as the data-collection-progress update Dr. Rey asked for.

---

## If you get stuck on a step

Tell me which step number and what the screen says. Don't troubleshoot alone for more than 10 minutes — CloudResearch's UI changes faster than docs do, and a quick redirect is cheaper than an hour of friction.

## What this gets you

- **Wed Jun 24 evening:** 10–15 valid responses in hand.
- **Sun Jun 28:** W07 reports "data collection live; n=X collected, attention-check pass rate Y%, soft-launch quality decision: proceed/revise."
- **Jul 5 (W08):** scaling toward n = 100 valid.
- **Jul 12 (W09):** collection closes; cleaning + descriptive analysis begins.
- **Jul 19:** final manuscript with EFA results.

That's the lane. Now go run Step 1.
