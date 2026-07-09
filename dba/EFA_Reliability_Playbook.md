---
TITLE: EFA + Reliability Playbook (Your Data Analysis Roadmap)
AUTHOR: Yasir A. Malik (PID 1687105) — FIU DBA Cohort 7.16
COURSE: GEB7913 — Instructor: Prof. Dr. Juan Rey
DATE: July 1, 2026
---

# EFA + Reliability Playbook — Your Analysis, Step by Step

> Built directly from Dr. Rey's **Assignment #4 guided solution** (the EFA + Reliability procedure on the SAQ dataset), applied to *your* instrument. Follow this in SPSS the moment your data is in. It also doubles as the skeleton of your **Data Analysis** section.

**Your parameters (per Dr. Rey's directive):**
- **Items analyzed:** the **55 construct items** only (TA_1…RAB_5). *Exclude* the control item (C1), attention checks, demographics, and the open-text from the EFA.
- **Extraction:** Principal Axis Factoring (PAF)
- **Rotation:** **Direct Oblimin** (oblique — your constructs are correlated)
- **Suppress loadings:** below **.30**
- **Target n:** 100 valid
- **Expected structure:** ~11 factors (11 constructs × 5 items) — but the data decides; report what you find.
- **Item-removal rule:** remove loadings **< .30**; for **.30–.40 decide item-by-item** (keep an item if removing it makes the pattern matrix *worse*).

---

## STEP 0 — Prepare the data (do this first, in SPSS)

1. **Get SPSS** — free for FIU students via the FIU software portal (or use SPSS in a campus lab).
2. **Export** your Qualtrics data → SPSS (.sav) or CSV → open in SPSS.
3. **Clean the sample:**
   - Remove anyone who **failed the eligibility screeners** (shouldn't be there, but check).
   - Remove **attention-check failures** (AC1 ≠ "Disagree", AC2 ≠ "Agree").
   - Remove **speeders** (implausibly fast page times) and straight-liners.
   - Document how many you removed → this is your **analytic n**.
4. **Outlier analysis (its own Results subsection — both course exemplars report it):** after cleaning, screen each construct with **boxplots and z-scores** (|z| > 3.29 as the conventional flag); document every keep/drop decision with a one-line rationale in the exclusion log. Removal is the exception, not the rule — an extreme-but-genuine professional opinion is data, not noise.
5. **⚠ Reverse-code the (R) items** — item 4 of every construct: `TA_4, RA_4, AT_4, SAP_4, FR_4, IR_4, RPG_4, PMI_4, AJQ_4, APR_4, RAB_4`.
   - In SPSS: Transform → Recode into Same/Different Variables → `1→5, 2→4, 3→3, 4→2, 5→1` (i.e., `new = 6 − old`).
   - **This is mandatory before both EFA interpretation and reliability** — Dr. Rey's assignment flags exactly this (their item 3 was reverse-coded).

---

## STEP 1 — Run the EFA (mirrors the assignment)

**Analyze → Dimension Reduction → Factor**

1. Move **all 55 construct items** into the **Variables** box.
2. **Descriptives** button → select **all options** (gives you KMO, Bartlett's, anti-image matrix, correlation matrix, determinant, reproduced correlations).
3. **Extraction** button → Method = **Principal axis factoring**; check **Scree plot**.
4. **Rotation** button → run the analysis **twice — once with Varimax, once with Direct Oblimin** (one rotation per run, exactly as Assignment 4 teaches). **Report Direct Oblimin** with the theoretical justification that the constructs are correlated; the Varimax run is your comparison evidence that the solution is stable across rotations.
5. **Options** button → **Sorted by size** + **Suppress small coefficients** = **.30**.
6. **OK** to run.

---

## STEP 2 — Read the output (in this order)

| Output | What to check | Rule of thumb |
|---|---|---|
| **Descriptives** | Means, SDs per item; watch for ceiling effects (very high means, low variance) | Report; flag low-variance items |
| **KMO** | Sampling adequacy | ≥ .50 minimum, ≥ .70 good, ≥ .80 great |
| **Bartlett's test** | Correlations differ from identity matrix | Want **significant** (p < .001) |
| **Anti-image matrix (diagonal)** | Per-item sampling adequacy | Each **> .50**; if below, consider removing that item (then rerun) |
| **Correlation matrix + determinant** | Multicollinearity | No items uncorrelated with all others (most r < .3); none too high (r > .9); **determinant > .00001** |
| **Total Variance Explained + Scree plot** | How many factors | eigenvalues > 1, scree inflexion, ≥ 50% variance, and your **theoretical expectation (~11)** |
| **Reproduced correlations (residuals)** | Model fit | Want residuals < .05; concern if > 50% exceed .05 |
| **Pattern Matrix** | **THE table you report** | Which items load on which factor (loadings ≥ .30 shown) |

---

## STEP 3 — Refine the factor solution

1. Look at the **Pattern Matrix**. For each item:
   - **Loads clean (≥ .40 on one factor):** keep.
   - **Loads < .30 everywhere / doesn't show:** **remove**, then rerun.
   - **Loads .30–.40, or cross-loads on two factors:** **decide one-by-one** — try removing it; if the pattern matrix gets *cleaner*, drop it; **if it gets worse, keep it** (this is Dr. Rey's exact rule).
2. **Rerun after each removal** (removing an item changes everything — KMO, loadings, factors).
3. Repeat until you have a clean, interpretable structure.
4. **Name each factor** from the items that cluster on it (they should map to your constructs — TA, RA, AT, etc.). Where they don't map cleanly, **that is a validation finding** — report it honestly.

---

## STEP 4 — Reliability (Cronbach's α per factor)

**Analyze → Scale → Reliability Analysis**

1. For **each retained factor**, move its items into the **Items** box.
2. Give the scale a meaningful name (e.g., "Training & Awareness").
3. **Statistics** button → check **Scale if item deleted**.
4. **OK.** Record **Cronbach's α**.
   - **α ≥ .70** = acceptable. If lower, look at "Cronbach's Alpha if Item Deleted" — dropping a weak item may raise it.
   - *(Make sure reverse-coded items were recoded in Step 0, or α will be wrong.)*

---

## STEP 5 — Write it up (template from Dr. Rey's model paragraph)

Fill the blanks from your output. Mirror his example almost exactly:

> *A principal axis factor analysis was conducted on the 55 items with oblique rotation (Direct Oblimin) on a sample of N = ___ valid responses. The Kaiser–Meyer–Olkin measure verified sampling adequacy, KMO = ___ (___ per Kaiser & Rice, 1974), and all individual-item KMO values were greater than ___, above the acceptable limit of .50. Bartlett's test of sphericity, χ²(___) = ___, p < .001, indicated correlations sufficient for FA. ___ factors had eigenvalues over Kaiser's criterion of 1 and together explained ___% of the variance. The scree plot ___ [supported/was ambiguous about] retaining ___ factors; ___ factors were retained based on ___. The pattern matrix (Table ___) shows the rotated factor loadings. The items clustering on each factor correspond to [Training & Awareness, Rotation of Auditors, …]. Reliabilities were: [Factor 1] α = ___, [Factor 2] α = ___, … Items ___ were removed for low or cross-loadings.*

**Report:** the pattern matrix table (always), KMO + Bartlett's, variance explained, the scree plot, and the reliability (α) for each factor. That IS your Data Analysis section — nothing more is required this term (no mediation/hypothesis testing).

---

## What's next for YOU (right now)

1. **You can't run this until data is in** — so the critical path is still **data collection to n = 100** (the Sarmed sprint).
2. **This playbook is ready and waiting** — the analysis is turnkey the moment you hit 100.
3. **Get SPSS installed** now (FIU portal) so it's not a last-minute scramble.
4. **Short thank-you to Dr. Rey** for the assignment (draft below).

> Dr. Rey — thank you, the guided EFA assignment is exactly what I needed; I've mapped the procedure onto my instrument and will follow it (PAF + Direct Oblimin, suppress < .30, your item-removal rule) once collection reaches n = 100. — Yasir

*(Reference: procedure adapted from Assignment #4 guided solution; classic EFA reporting per Field, and Kaiser & Rice, 1974, as cited in the assignment.)*
