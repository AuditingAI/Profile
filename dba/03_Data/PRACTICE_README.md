# PRACTICE (SIMULATED) DATA — READ FIRST

**This folder's `PRACTICE_SIMULATED_*` files contain SIMULATED data. No human participants. Not research findings.**

## Why it exists
The advisor's plan (late-July meeting) includes a **simulated-data exercise, separate from the manuscript and not mentioned in it**, to demonstrate analytic competency. This practice set lets that exercise be executed fluently on arrival — it is a rehearsal, not a substitute.

## Hard boundaries
1. **Never enters the manuscript.** Chapter 5's finding stands unchanged: at the achieved sample the required analyses could not be performed. That is true and stays true.
2. **Never presented as collected data**, to anyone, in any document.
3. Every row carries `SOURCE = SIMULATED_PRACTICE_DATA`; the filename says PRACTICE_SIMULATED.
4. When the advisor's own dataset arrives, **that** is the one used for the graded exercise.

## Files
| File | What it is |
|---|---|
| `make_practice_dataset.py` | Generator — 250 cases, 11 factors x 5 items, correlated factors, known ground truth |
| `PRACTICE_SIMULATED_dataset.csv` | The simulated data (import this to Jamovi to rehearse) |
| `run_practice_efa.py` | Worked example — runs the full Chapter 4 contract in Python |
| `PRACTICE_factor_loadings_oblimin.csv` | Pattern matrix from the worked example |

## Ground truth built into the data (check your Jamovi output against this)
- **11 factors** theorized; parallel analysis recovers ~10 — a realistic near-miss that forces a defensible retention argument rather than a rubber stamp.
- **AT_3** carries a deliberately weak loading (~.40 boundary) → deletion-candidate discussion.
- **PMI_2** cross-loads onto AJQ → flag under the .20 rule (item-rest r = .30, the weakest in its scale).
- **Item _4 of every construct is stored reverse-worded** and must be recoded (6 − x) before analysis. Skipping this is the single most common error — it shows up as a suppressed alpha.
- Factors are genuinely correlated → **Direct Oblimin is the defensible rotation to report**, Varimax run as robustness.

## Worked-example results (what a correct run produces)
KMO = .811 · Bartlett χ²(1485) = 4,633.2, p < .001 · 20 of 250 cases removed on attention checks (n = 230) · all 11 alphas between .71 and .81.
