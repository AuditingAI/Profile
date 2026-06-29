# Qualtrics Codebook + Post-Import Setup Guide

**Companion file:** `Qualtrics_Survey_Import.txt` (v2 — post peer review)
**Purpose:** Import the full instrument in 30 seconds, then run the 7 post-import steps below so launch-day is clean.

> **v2.1 note (post Richard's peer review + follow-up chat):** Eight construct items were reworded (TA_5, RA_5, AT_3, SAP_5, IR_1, IR_3, RPG_1, RPG_2, PMI_4, APR_5 — see `Full_Survey_Questionnaire_v2.md` change log). Added: an orientation screen with a neutral **anchoring-bias definition** (`ORIENT_DEF`, display only); a context-control item **C1_PRIORFILE** (now a **frequency** scale: every / most / half / some / rarely — captures engagement-by-engagement variation); split experience into **D1A_EXT_EXP** and **D1B_INT_EXP**; and a firm-size demographic **D3B_FIRM_SIZE** (Big 4 / mid-tier / small / sole practitioner). Reverse-coded items are unchanged (still position 4 in each construct). Note: **C1_PRIORFILE is a control on a frequency scale, not a Likert construct item — exclude it from the factor analysis.**

---

## How to import (60 seconds)

1. Open **fiu.qualtrics.com** → sign in → **Create new project** → **From scratch** (Survey).
2. In the editor, click the **Tools** menu (top-right) → **Import survey** → **Import from a TXT file**.
3. Upload `Qualtrics_Survey_Import.txt`.
4. Qualtrics builds: 1 consent + 5 screeners + 11 construct matrices + 2 attention checks + 1 open-text + 7 demographics + 1 debrief.

After import: do the 7 steps below before publishing. Each is a one-time setup.

---

## STEP 1 — Replace the consent placeholder with the IRB letter

- Open **Block 00 — Welcome and Informed Consent**.
- Delete the placeholder text inside the description block.
- Paste the **IRB-approved consent letter verbatim** (from your IRB-25-0462 file).
- Keep the `CONSENT` question — it gates the rest of the survey.

---

## STEP 2 — Wire screen-out branching (Survey Flow)

This is the only step the TXT format cannot do for you. Click **Survey Flow** (left sidebar) and add **Branches** in this order:

| If question | Equals | Then |
|---|---|---|
| CONSENT | No, I do not consent | **End of Survey** with ineligible message |
| S1_COUNTRY | No | End of Survey |
| S2_LANGUAGE | No | End of Survey |
| S3_AUDIT_ROLE | No | End of Survey |
| S4_CONTINUING_ENG | No | End of Survey |
| S5_ATTESTATION | No | End of Survey |

**Block order in Survey Flow:**
1. Block 00 (Consent)
2. Branch: end if CONSENT = No
3. Block 01 (Eligibility)
4. Branches: end if any screener fails
5. **Randomizer** containing blocks 02–05 + 07–10 (the 8 intervention IVs). Present 8 in random order.
6. Block 06 (Attention Check 1) — fixed position after the first 4 IV blocks the respondent sees
7. Block 11 (Attention Check 2) — fixed position after the next 4 IV blocks
8. Blocks 12, 13, 14 (AJQ, APR, RAB) — fixed order, after IVs
9. Block 15 (Open-text)
10. Block 16 (Demographics)
11. Block 17 (Debrief)
12. **End of Survey** with redirect URL to CloudResearch (Step 7)

> Simpler alternative if randomizing-around-attention-checks gets fiddly: keep blocks in import order (TA→RA→AT→SAP→AC1→FR→IR→RPG→PMI→AC2→AJQ→APR→RAB). Less ideal for EFA defense but acceptable for a 60–80-n study.

---

## STEP 3 — Variable naming (rename matrix rows for EFA-friendly exports)

After import, each matrix question's rows are auto-named `TA_1`, `TA_2`, ..., `TA_5`. That's already EFA-friendly. The only thing you need to do is **document which items are reverse-coded** so the data-cleaning step in Stage 3b flips them correctly.

### Reverse-coded items (flip these at cleaning, BEFORE EFA)

| Construct | Item position | Statement |
|---|---|---|
| TA  | 4 (`TA_4`) | I have received little or no training on how initial reference points can distort judgment. |
| RA  | 4 (`RA_4`) | The same individuals remain on my engagements for many years without change. |
| AT  | 4 (`AT_4`) | I rely mainly on prior-year workpapers rather than on current-period analytics. |
| SAP | 4 (`SAP_4`) | My approach to recurring tasks is mostly informal and ad hoc. |
| FR  | 4 (`FR_4`) | I rarely learn whether my professional judgments were accurate. |
| IR  | 4 (`IR_4`) | Reviews in my firm mostly confirm the preparer's conclusion without independent analysis. |
| RPG | 4 (`RPG_4`) | Regulatory guidance has little practical effect on my day-to-day judgments. |
| PMI | 4 (`PMI_4`) | Pressure to meet budgets discourages me from re-examining prior-year balances. |
| AJQ | 4 (`AJQ_4`) | My conclusions often default to last year's position. |
| APR | 4 (`APR_4`) | Execution on my engagements is often rushed or inconsistent. |
| RAB | 4 (`RAB_4`) | My estimates tend to stay close to the prior-year figure even when evidence suggests otherwise. |

**Reverse-code formula (SPSS / R / Python at cleaning):** `recoded = 6 - original` (because the scale is 1–5).

---

## STEP 4 — Force-response + page-timing

For every matrix and screener question:

- **Force Response:** ON (right panel → Behavior → Force Response)
- **Page Timing:** add a **Timing question** (Question type → Timing) hidden on each construct block page, capture First Click + Last Click + Page Submit + Click Count. Use these in Stage 3b to flag speeders (<5 sec per construct block is suspicious).

Quick way: turn on **Force Response** once at the survey level via **Survey Options → Responses → Force response**, then override per-question for the open-text item (which should be optional).

---

## STEP 5 — Survey-level settings

In **Survey Options** (gear icon):

| Setting | Value |
|---|---|
| Anonymize responses | **ON** |
| Record IP address | **OFF** |
| Record location data | **OFF** |
| Prevent ballot-box stuffing | **ON** |
| Prevent indexing | **ON** |
| Show progress bar | **ON** (gradual) |
| Allow back button | **OFF** |
| Survey expiration | **Jul 12, 2026 11:59 PM** |
| Auto-advance | OFF for matrices, ON for single MC |

---

## STEP 6 — Bot/quality protections

Under **Survey Options → Security** (and **Fraud Detection** if available):

- ReCAPTCHA score check: **ON**
- Relevant ID fraud detection (CloudResearch-friendly): **ON** if available
- Bot detection: **ON**
- Duplicate response prevention (cookie-based): **ON**

---

## STEP 7 — Completion redirect to CloudResearch

Once your CloudResearch project is drafted (Tuesday night per the Master Action Pack), CloudResearch will give you a **completion URL** unique to that study. Then in Qualtrics:

1. Survey Flow → **End of Survey** element at the very bottom.
2. Edit → **Redirect to a URL**.
3. Paste the CloudResearch completion URL.
4. Make sure this End of Survey is reached ONLY by respondents who finish (after Block 17), NOT by screen-outs.

Add a **second End of Survey** for screen-outs that shows a polite "Thank you, you are not eligible for this study" message and does NOT redirect (no payment for screen-outs).

---

## Pre-publish preview test (Tuesday before launch)

- [ ] Preview as **eligible** respondent — full survey flows, lands on CloudResearch redirect.
- [ ] Preview as **ineligible** respondent (fail S3 or S4) — gets the polite screen-out message immediately.
- [ ] Preview on Pixel mobile browser — matrices render readably.
- [ ] Preview on desktop — matrices render as grids.
- [ ] Attention checks fire at the right time.
- [ ] Both reverse-coded items in TA and RPG read naturally (no double negatives that confuse).
- [ ] Anonymous distribution link generated and copied (this is the URL you paste into CloudResearch).

---

## Item count summary

| Block group | # questions |
|---|---|
| Consent | 1 |
| Screeners | 5 |
| 8 IV construct matrices (5 items each) | 40 |
| 2 mediator matrices (5 items each) | 10 |
| 1 DV matrix (5 items) | 5 |
| Attention checks | 2 |
| Open-text substantive check | 1 |
| Demographics | 7 |
| Debrief | 1 (display only) |
| **Total respondent-facing items** | **71** (plus 1 consent + 1 debrief) |

Median completion time at this length is typically 12–18 minutes for an audit professional — well inside the IRB-approved 15–20 minute window.

---

## After all 7 steps are done

1. Click **Publish** in Qualtrics.
2. Copy the **anonymous distribution link** (under Distributions → Anonymous Link).
3. That link is what you paste into CloudResearch on Tuesday night (Action Pack page 7).
4. You're ready for Wednesday's launch.
