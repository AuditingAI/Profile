"""
SYNTHETIC PRACTICE DATASET GENERATOR — NOT RESEARCH DATA.

Generates a simulated dataset with the same 11-construct / 55-item structure as the
study instrument, for the purpose of PRACTISING and DEMONSTRATING the EFA + reliability
pipeline (Jamovi runbook / advisor's analytic-competency exercise).

HARD BOUNDARY, stated in the file so it travels with the data:
  * This data is SIMULATED. No human participants are involved.
  * It must NEVER be reported in the manuscript, cited as findings, or presented as
    collected data. The manuscript's Chapter 5 finding stands: with the achieved
    sample the required analyses could not be performed.
  * Every row carries SOURCE = "SIMULATED_PRACTICE_DATA" and the file name says so.

Design (a known ground truth, so the analysis can be checked against it):
  - n = 250 simulated respondents (adequate for an 11-factor EFA)
  - 11 factors x 5 items, loadings drawn ~ .55-.80 (clean but not artificial)
  - Correlated factors (oblique structure) -> justifies Direct Oblimin over Varimax
  - Item 4 of each construct is REVERSE-WORDED and stored RAW (un-reversed), so the
    analyst must reverse-code it — that step is part of the exercise
  - Two deliberate imperfections so the item-retention rules actually bite:
        AT_3  -> weak primary loading (~.30) : should be a deletion candidate
        PMI_2 -> cross-loads onto the AJQ factor : should be flagged
  - 5-point Likert integers, 1-5
"""
import numpy as np
import pandas as pd

SEED = 7913           # course number, for reproducibility
N = 250
rng = np.random.default_rng(SEED)

CONSTRUCTS = ["TA", "RA", "AT", "SAP", "FR", "IR", "RPG", "PMI", "AJQ", "APR", "RAB"]
K = len(CONSTRUCTS)
REVERSE_ITEM = 4      # item _4 of each construct is reverse-worded

# --- factor correlations: interventions correlate moderately; mediators/outcome higher
Phi = np.full((K, K), 0.30)
np.fill_diagonal(Phi, 1.0)
idx = {c: i for i, c in enumerate(CONSTRUCTS)}
for a, b, r in [("AJQ", "APR", 0.45), ("AJQ", "RAB", 0.55), ("APR", "RAB", 0.50),
                ("SAP", "APR", 0.42), ("IR", "APR", 0.40), ("TA", "AJQ", 0.42)]:
    Phi[idx[a], idx[b]] = Phi[idx[b], idx[a]] = r

# nearest positive-definite safeguard
w, V = np.linalg.eigh(Phi)
w = np.clip(w, 1e-6, None)
Phi = V @ np.diag(w) @ V.T
d = np.sqrt(np.diag(Phi))
Phi = Phi / np.outer(d, d)

F = rng.multivariate_normal(np.zeros(K), Phi, size=N)   # latent factor scores

data = {}
for ci, c in enumerate(CONSTRUCTS):
    for j in range(1, 6):
        name = f"{c}_{j}"
        lam = rng.uniform(0.55, 0.80)

        if name == "AT_3":            # weak item — deletion candidate
            lam = 0.30
        latent = lam * F[:, ci]

        if name == "PMI_2":           # cross-loading item
            latent = 0.45 * F[:, idx["PMI"]] + 0.40 * F[:, idx["AJQ"]]
            lam = 0.45

        err = rng.normal(0, np.sqrt(max(1 - lam ** 2, 0.15)), N)
        z = latent + err

        # map to 5-point Likert with a mild agreement skew (realistic for self-report)
        x = np.clip(np.round(3.55 + 0.95 * z), 1, 5).astype(int)

        if j == REVERSE_ITEM:         # store reverse-worded item UN-reversed
            x = 6 - x
        data[name] = x

df = pd.DataFrame(data)

# --- attention checks (a small number fail, as in real collection)
df.insert(0, "AC1", np.where(rng.random(N) < 0.04, rng.integers(1, 6, N), 2))  # correct = 2 (Disagree)
df.insert(1, "AC2", np.where(rng.random(N) < 0.04, rng.integers(1, 6, N), 4))  # correct = 4 (Agree)

# --- demographics
df.insert(0, "D_ROLE", rng.choice(
    ["External audit", "Internal audit", "Enterprise risk", "Compliance testing",
     "Credit/loan review", "Quality assurance", "SOX controls"], N,
    p=[.20, .26, .14, .14, .10, .08, .08]))
df.insert(1, "D_EXP", rng.choice(
    ["Less than 2 years", "2 to 5 years", "6 to 10 years", "11 to 15 years", "16+ years"], N,
    p=[.14, .30, .28, .18, .10]))
df.insert(0, "SOURCE", "SIMULATED_PRACTICE_DATA")
df.insert(1, "RID", [f"SIM_{i:04d}" for i in range(1, N + 1)])

out = "PRACTICE_SIMULATED_dataset.csv"
df.to_csv(out, index=False)

print(f"wrote {out}: {df.shape[0]} rows x {df.shape[1]} cols  [SIMULATED — NOT RESEARCH DATA]")
print("Ground truth for checking your analysis:")
print("  - 11 factors expected; AT_3 should show a weak (<.40) loading -> deletion candidate")
print("  - PMI_2 should cross-load onto the AJQ factor -> flag under the .20 rule")
print("  - item _4 of every construct is stored REVERSE-WORDED and must be recoded (6 - x)")
print("  - factors are correlated -> Direct Oblimin is the defensible rotation to report")
