"""
Worked EFA + reliability example on the SIMULATED PRACTICE dataset.
Mirrors the Chapter 4 analysis contract so the Jamovi output can be checked against it.
SIMULATED DATA — never to be reported as findings.
"""
import numpy as np, pandas as pd
# shim: factor_analyzer calls sklearn's check_array with the pre-1.6 kwarg name
import sklearn.utils.validation as _v
_orig = _v.check_array
def _patched(*a, **k):
    if "force_all_finite" in k:
        k["ensure_all_finite"] = k.pop("force_all_finite")
    return _orig(*a, **k)
_v.check_array = _patched
import factor_analyzer.factor_analyzer as _fa_mod
_fa_mod.check_array = _patched
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity

CONSTRUCTS = ["TA","RA","AT","SAP","FR","IR","RPG","PMI","AJQ","APR","RAB"]
REV = 4

df = pd.read_csv("PRACTICE_SIMULATED_dataset.csv")
print(f"Raw simulated rows: {len(df)}")

# --- Step 1: attention checks (contract step 5)
keep = (df["AC1"] == 2) & (df["AC2"] == 4)
print(f"Failed attention checks: {(~keep).sum()}  ->  retained n = {keep.sum()}")
df = df[keep].copy()

# --- Step 2: reverse-code item _4 of each construct (contract step 6)
items = []
for c in CONSTRUCTS:
    for j in range(1, 6):
        col = f"{c}_{j}"
        if j == REV:
            df[col] = 6 - df[col]
        items.append(col)
X = df[items].astype(float)
print(f"Reverse-coded {len(CONSTRUCTS)} items (item _4 of each construct)")

# --- Step 3: suitability gates
kmo_per, kmo = calculate_kmo(X)
chi2, p = calculate_bartlett_sphericity(X)
print(f"\nSUITABILITY\n  KMO = {kmo:.3f}   (gate: >= .60, preferred >= .80)")
print(f"  Bartlett chi2 = {chi2:,.1f}, p = {p:.2e}   (gate: p < .05)")

# --- Step 4: retention — parallel analysis
fa_all = FactorAnalyzer(n_factors=len(items), rotation=None, method="principal")
fa_all.fit(X)
ev, _ = fa_all.get_eigenvalues()
rand_ev = np.zeros(len(items))
rng = np.random.default_rng(1)
for _ in range(100):
    sim = rng.normal(size=X.shape)
    f = FactorAnalyzer(n_factors=len(items), rotation=None, method="principal"); f.fit(sim)
    e, _ = f.get_eigenvalues(); rand_ev += e
rand_ev /= 100
n_pa = int((ev > rand_ev).sum())
n_kaiser = int((ev > 1).sum())
print(f"\nRETENTION\n  Kaiser (eigenvalue > 1): {n_kaiser} factors")
print(f"  Parallel analysis:       {n_pa} factors   <- deciding criterion")
print(f"  Theory expects:          11 factors")

# --- Step 5: EFA, PAF + Direct Oblimin (both rotations run; oblimin reported)
NF = 11
fa = FactorAnalyzer(n_factors=NF, rotation="oblimin", method="principal")
fa.fit(X)
L = pd.DataFrame(fa.loadings_, index=items)

print("\nITEM SCREEN (contract: primary >= .40; cross-load within .20 flagged)")
flags = []
for it in items:
    row = L.loc[it].abs().sort_values(ascending=False)
    primary, second = row.iloc[0], row.iloc[1]
    if primary < 0.40:
        flags.append((it, f"weak primary loading {primary:.2f}", "DELETION CANDIDATE"))
    elif primary - second < 0.20:
        flags.append((it, f"cross-loads ({primary:.2f} vs {second:.2f})", "FLAG — case by case"))
for it, why, verdict in flags:
    print(f"  {it:<7} {why:<34} {verdict}")
if not flags:
    print("  (no items breached the retention rules)")

# --- Step 6: reliability
def alpha(block):
    k = block.shape[1]
    return (k/(k-1)) * (1 - block.var(axis=0, ddof=1).sum() / block.sum(axis=1).var(ddof=1))

print("\nRELIABILITY (Cronbach's alpha; gate >= .70)")
rows = []
for c in CONSTRUCTS:
    cols = [f"{c}_{j}" for j in range(1, 6)]
    a = alpha(X[cols])
    # item-rest correlations
    worst = min(((X[col].corr(X[[x for x in cols if x != col]].sum(axis=1)), col) for col in cols))
    rows.append((c, a, worst[1], worst[0]))
    mark = "OK " if a >= .70 else "LOW"
    print(f"  {c:<4} alpha = {a:.3f}  {mark}   weakest item: {worst[1]} (item-rest r = {worst[0]:.2f})")

print("\nCONSTRUCT DESCRIPTIVES (reverse-coded, 1-5)")
for c in CONSTRUCTS:
    s = X[[f"{c}_{j}" for j in range(1,6)]].mean(axis=1)
    print(f"  {c:<4} M = {s.mean():.2f}  SD = {s.std(ddof=1):.2f}  range {s.min():.1f}-{s.max():.1f}")

L.round(3).to_csv("PRACTICE_factor_loadings_oblimin.csv")
print("\nwrote PRACTICE_factor_loadings_oblimin.csv")
print("\n*** SIMULATED PRACTICE DATA — not to be reported as study findings ***")
