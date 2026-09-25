# Jamovi Runbook — Execute Tomorrow (n = 4 pilot)

**Goal:** reproduce the descriptives + reliability in Jamovi (so the output is tool-generated with your name on it), specify the CFA to show readiness, screenshot each result, and paste into Chapter 5. Budget: ~60–90 minutes. Everything below is already computed and verified independently — Jamovi should match within rounding; if a number differs, trust Jamovi and update the manuscript table.

---

## STEP 0 — Install & open (5 min)
1. Download Jamovi (free): https://www.jamovi.org/download.html → install → open.
2. You'll also need the data file `cleaned_valid_responses.csv` (the screened n=4 file — I sent it to you; keep it OFF email, it has participant data).

## STEP 1 — Load the data (2 min)
1. Jamovi → hamburger menu (☰, top-left) → **Open** → **This PC** → select `cleaned_valid_responses.csv`.
2. You'll see 4 rows. The Likert columns (TA_1 … RAB_5) will import as **Text**. That's fine — we recode next.

## STEP 2 — Recode Likert text → numbers (10 min)
Jamovi needs numeric values. Two options — **Option A is faster if your export used numeric values; Option B works for the label export you have.**

**Option B (your file has words like "Agree"):** Use a transform.
1. Double-click an empty column header → the compute/transform panel opens.
2. Actually simpler: **Data tab → Transform is per-variable.** Instead, create ONE transform and apply to all Likert vars:
   - Data tab → select all TA_/RA_/…/RAB_ columns (click first, shift-click last).
   - **Data → Transform** → New transform → in the formula box, use nested `IF`:
     ```
     IF($source == "Strongly disagree", 1,
     IF($source == "Disagree", 2,
     IF($source == "Neither agree nor disagree", 3,
     IF($source == "Agree", 4,
     IF($source == "Strongly agree", 5, "")))))
     ```
   - This creates numeric versions of every selected column at once.

> Tip: if this is fiddly, tell me and I'll give you a pre-recoded numeric CSV you just open directly — no transform needed. That's the faster path and I recommend it.

## STEP 3 — Reverse-code the (R) items (5 min)
The 4th item of each construct (TA_4, RA_4, AT_4, SAP_4, FR_4, IR_4, RPG_4, PMI_4, AJQ_4, APR_4, RAB_4) is reverse-worded.
- For each, create a computed variable: **Data → Compute** → name it e.g. `TA_4r` → formula: `6 - TA_4`.
- (Again: I can hand you a CSV with this already done — say the word.)

## STEP 4 — Descriptives (10 min)
1. **Analyses tab → Exploration → Descriptives.**
2. Move all 5 items of a construct (using the reverse-coded version for item 4) into **Variables**.
3. Check: Mean, Std. deviation, Minimum, Maximum.
4. **Screenshot** the results table. Repeat per construct (or load all 55 at once for one big table).
5. These feed Table 5.1. Expected construct means (avg the 5 item means): TA 3.50, RA 3.60, AT 3.50, SAP 3.70, FR 3.60, IR 3.60, RPG 3.80, PMI 3.55, AJQ 4.20, APR 3.90, RAB 3.50.

## STEP 5 — Reliability / Cronbach's α (15 min)
1. **Analyses tab → Factor → Reliability Analysis.**
2. Move one construct's 5 items into **Items** (reverse-coded item 4 included as its `_r` version; OR put the raw item in and tick it under "Reverse Scaled Items").
3. Under **Scale Statistics**, ensure **Cronbach's α** is checked.
4. **Screenshot.** Repeat for all 11 constructs.
5. Expected α (will match my script): TA 0.85, RA −0.31, AT 0.07, SAP −3.75, FR 0.83, IR 0.39, RPG 0.75, PMI 0.63, AJQ 0.00, APR 0.51, RAB 0.29.
6. **Do not be alarmed by negative/weird α** — that IS the finding: α is uninterpretable at n=4. Chapter 5.3 already says this in the right words.

## STEP 6 — CFA specification (show readiness, do NOT expect it to run) (15 min)
1. **Analyses tab → Factor → Confirmatory Factor Analysis.**
2. Create 11 factors; assign each construct's 5 items to its factor.
3. Click **OK/estimate.** Jamovi will return an error or a non-converged / not-identified result (expected at n=4).
4. **Screenshot both the factor-assignment panel AND the error/non-identification message.** That screenshot IS the deliverable for Section 5.5 — it proves the model was correctly specified and simply underpowered.

## STEP 7 — Assemble & submit (15 min)
1. Paste the Step 4–6 screenshots into Chapter 5 where the `[JAMOVI: …]` markers are.
2. Merge Chapters 4–6 (`Research_Paper_YMalik_CH4-6_DRAFT.md`) onto the existing manuscript (Ch 2–3 + Appendix A).
3. Export the full manuscript to Word/PDF.
4. Submit to Canvas. Done.

---

## Fastest path (recommended)
Steps 2–3 (recode + reverse-code) are the only fiddly part. **Say "give me the numeric file" and I'll produce a `cleaned_numeric_recoded.csv` where all Likert items are already 1–5 and the (R) items are already reversed** — then you skip straight to Step 4, and Jamovi is just: load → Descriptives → Reliability → CFA → screenshot. That turns this into a 30-minute job.
