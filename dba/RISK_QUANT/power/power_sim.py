#!/usr/bin/env python3
"""
Monte Carlo power and sample-size sensitivity for the DBA research models.

AI-use disclosure: simulation code and tables drafted with Claude (Anthropic) on 20 Oct 2026 as an analysis aid; assumptions and interpretation to be reviewed and owned by Yasir Malik.

Extends ../feasibility.py. That file asks whether a sample can be obtained at
all. This one asks how large the sample must be before the planned tests can
detect an effect, and then hands that N back to the feasibility funnel to ask
what sampling frame it implies.

Two models, kept separate on purpose
------------------------------------
  QUAL   The qualifying study as specified (IRB-25-0462): 11 reflective
         constructs, 5 items each (55 items), 16 hypotheses. Eight
         interventions -> two mediators (AJQ, APR) -> one outcome (RAB).
         Specified for PLS-SEM. No moderation hypothesis exists in this model.
  CHAIN  ILLUSTRATIVE ONLY. The dissertation's three-link chain has no
         committed instrument (dba/Dissertation_Instrument_v3_DRAFT.md is a
         parked concept sketch). It is represented here as a simple path
         model X -> M1 -> M2 -> Y with a moderator W on X -> M1, so that the
         order of magnitude of N for serial mediation and moderation is
         visible. It is not a specification of the dissertation model.

Estimation is an APPROXIMATION of PLS-SEM: each construct is scored as the
mean of its items (equal weights), standardised, and paths are estimated by
OLS on the composites. PLS mode A weights would differ slightly from equal
weights; with homogeneous loadings the difference is small but not zero.

Tests (two-tailed, alpha = .05)
  direct     t test on the focal path (OLS standard error, t with N-k-1 df)
  indirect   Monte Carlo confidence interval (Preacher & Selig, 2012):
             product of normal draws around each path estimate, 95% interval
             excludes zero. Joint significance is also recorded.
  moderation t test on the product-of-composites term (two-stage style)
An optional percentile bootstrap check (--boot-check) compares the Monte Carlo
interval with a bootstrap interval in one cell.

Usage
    python3 power_sim.py                    # full grid, 2000 reps per cell,
                                            # plus a 300-rep bootstrap check
    python3 power_sim.py --reps 200 --boot-check 0      # quick run
    python3 power_sim.py --items 3 --boot-check 0       # 3 items per construct
                                                        # (v3 concept sketch)

Requires numpy. Everything else is standard library. Fixed seed.
"""

import argparse
import csv
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)

# Reuse the validated funnel from ../feasibility.py without writing a
# __pycache__ folder into the parent directory.
sys.dont_write_bytecode = True
sys.path.insert(0, PARENT)
from feasibility import CASE, feasibility  # noqa: E402

GRID_N = (30, 50, 75, 100, 150, 200, 300, 500, 750, 1000)
GRID_BETA = (0.10, 0.20, 0.30)
ALPHA = 0.05


# ── t distribution, standard library only ─────────────────────────────────────

def _betacf(a, b, x, itmax=300, eps=3e-14):
    """Continued fraction for the incomplete beta (Lentz's method)."""
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, itmax + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c
        c = c if abs(c) > tiny else tiny
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c
        c = c if abs(c) > tiny else tiny
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            break
    return h


def betainc_reg(a, b, x):
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbt = (math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
           + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return math.exp(lbt) * _betacf(a, b, x) / a
    return 1.0 - math.exp(lbt) * _betacf(b, a, 1.0 - x) / b


def t_two_tailed_p(t, df):
    return betainc_reg(df / 2.0, 0.5, df / (df + t * t))


_TCRIT = {}


def t_crit(df, alpha=ALPHA):
    """Two-tailed critical value by bisection on the t CDF."""
    if df not in _TCRIT:
        lo, hi = 0.0, 50.0
        for _ in range(200):
            mid = (lo + hi) / 2.0
            if t_two_tailed_p(mid, df) > alpha:
                lo = mid
            else:
                hi = mid
        _TCRIT[df] = (lo + hi) / 2.0
    return _TCRIT[df]


# ── Population models ─────────────────────────────────────────────────────────

class Model:
    """A recursive structural model with standardised latent variables.

    exo:   exogenous latent names (unit variance), with correlation matrix phi
    eqs:   list of (endogenous name, {predictor: standardised path})
    prods: {product name: (a, b)} latent product terms treated as exogenous
           (valid because a, b are independent standard normals, so the
           product has unit variance and zero covariance with a and b)
    """

    def __init__(self, name, exo, phi, eqs, prods=None):
        self.name = name
        self.exo = list(exo)
        self.phi = np.asarray(phi, dtype=float)
        self.eqs = eqs
        self.prods = prods or {}
        self.order = self.exo + list(self.prods) + [t for t, _ in eqs]
        self.measured = [v for v in self.order if v not in self.prods]
        self._solve_residuals()

    def _solve_residuals(self):
        """Residual variances that make every latent variance exactly 1."""
        idx = {v: i for i, v in enumerate(self.order)}
        n = len(self.order)
        S = np.zeros((n, n))
        k = len(self.exo)
        S[:k, :k] = self.phi
        for p in self.prods:
            S[idx[p], idx[p]] = 1.0
        self.psi, self.r2 = {}, {}
        for tgt, paths in self.eqs:
            j = idx[tgt]
            pi = [idx[p] for p in paths]
            b = np.array([paths[p] for p in paths])
            cov_prev = S[pi, :].T @ b         # cov(target, every variable)
            explained = float(b @ S[np.ix_(pi, pi)] @ b)
            if explained >= 1.0:
                raise ValueError(f"{self.name}: R2 for {tgt} is {explained:.3f} "
                                 ">= 1; paths are not admissible")
            S[j, :] = cov_prev
            S[:, j] = cov_prev
            S[j, j] = 1.0
            self.psi[tgt] = 1.0 - explained
            self.r2[tgt] = explained
        self.sigma = S

    def simulate_latent(self, rng, R, N):
        L = {}
        chol = np.linalg.cholesky(self.phi)
        z = rng.standard_normal((R, N, len(self.exo))) @ chol.T
        for i, v in enumerate(self.exo):
            L[v] = z[:, :, i]
        for p, (a, b) in self.prods.items():
            L[p] = L[a] * L[b]
        for tgt, paths in self.eqs:
            y = np.sqrt(self.psi[tgt]) * rng.standard_normal((R, N))
            for p, coef in paths.items():
                y = y + coef * L[p]
            L[tgt] = y
        return L


def qual_model(beta, background, rho):
    """Qualifying study. TA is the focal intervention.

    Focal paths (set to beta): TA -> RAB (direct), TA -> AJQ and AJQ -> RAB
    (the mediated path). Every other structural path is set to `background`.
    Interventions intercorrelate at `rho` (an assumption).
    """
    ivs = ["TA", "RA", "AT", "SAP", "FR", "IR", "RPG", "PMI"]
    judgment = ["TA", "AT", "FR", "IR", "RPG", "PMI"]   # route via AJQ
    structural = ["RA", "SAP"]                          # route via APR
    phi = np.full((8, 8), rho)
    np.fill_diagonal(phi, 1.0)
    ajq = {v: (beta if v == "TA" else background) for v in judgment}
    apr = {v: background for v in structural}
    rab = {v: (beta if v == "TA" else background) for v in ivs}
    rab["AJQ"] = beta
    rab["APR"] = background
    eqs = [("AJQ", ajq), ("APR", apr), ("RAB", rab)]
    m = Model("QUAL", ivs, phi, eqs)
    m.tests = {
        "direct":   ("RAB", "TA"),
        "indirect": [("AJQ", "TA"), ("RAB", "AJQ")],
    }
    m.true = {"direct": beta, "indirect": beta * beta}
    return m


def chain_model(beta, background):
    """ILLUSTRATIVE three-link chain. Not the dissertation specification.

    X  AI output reliance      M1 anchoring on system output
    M2 confirmation / sycophancy   Y  convergence of conclusions
    W  moderator on X -> M1 (for example AI tool use or reliance training)
    Focal paths (beta): X -> M1, M1 -> M2, M2 -> Y, and X*W -> M1.
    Background paths: W -> M1 and a residual direct X -> Y.
    """
    phi = np.eye(2)                    # X and W independent (assumption)
    eqs = [
        ("M1", {"X": beta, "W": background, "XW": beta}),
        ("M2", {"M1": beta}),
        ("Y",  {"M2": beta, "X": background}),
    ]
    m = Model("CHAIN", ["X", "W"], phi, eqs, prods={"XW": ("X", "W")})
    m.tests = {
        "direct":     ("Y", "M2"),
        "indirect":   [("M1", "X"), ("M2", "M1"), ("Y", "M2")],
        "moderation": ("M1", "XW"),
    }
    m.true = {"direct": beta, "indirect": beta ** 3, "moderation": beta}
    return m


# ── Measurement and estimation ────────────────────────────────────────────────

def standardise(a):
    a = a - a.mean(axis=1, keepdims=True)
    return a / a.std(axis=1, ddof=1, keepdims=True)


def composites(model, L, rng, items, lo, hi):
    """Reflective indicators, then equal-weight composite scores."""
    R, N = next(iter(L.values())).shape
    C = {}
    for v in model.measured:
        lam = rng.uniform(lo, hi, size=(R, 1, items))
        eps = rng.standard_normal((R, N, items))
        x = lam * L[v][:, :, None] + np.sqrt(1.0 - lam ** 2) * eps
        C[v] = standardise(x.mean(axis=2))
    for p, (a, b) in model.prods.items():
        C[p] = standardise(C[a] * C[b])
    return C


def ols(C, target, preds):
    """Batched OLS on standardised composites. Returns coef, se, df."""
    X = np.stack([C[p] for p in preds], axis=2)          # R, N, k
    y = C[target]
    R, N, k = X.shape
    XtX = np.einsum("rnk,rnj->rkj", X, X)
    Xty = np.einsum("rnk,rn->rk", X, y)
    inv = np.linalg.inv(XtX)
    b = np.einsum("rkj,rj->rk", inv, Xty)
    resid = y - np.einsum("rnk,rk->rn", X, b)
    df = N - k - 1                                        # intercept is implicit
    s2 = (resid ** 2).sum(axis=1) / df
    se = np.sqrt(s2[:, None] * np.diagonal(inv, axis1=1, axis2=2))
    return b, se, df


def equations(model):
    return {t: list(p) for t, p in model.eqs}


def run_cell(model, N, reps, rng, items, lo, hi, mc_draws, chunk):
    eqs = equations(model)
    tests = model.tests
    acc = {k: [] for k in ("direct", "indirect", "joint", "moderation",
                           "est_direct", "est_indirect", "est_moderation")}
    done = 0
    while done < reps:
        R = min(chunk, reps - done)
        L = model.simulate_latent(rng, R, N)
        C = composites(model, L, rng, items, lo, hi)
        fits = {t: ols(C, t, eqs[t]) for t in eqs}

        def coef(tgt, pred):
            b, se, df = fits[tgt]
            i = eqs[tgt].index(pred)
            return b[:, i], se[:, i], df

        b, se, df = coef(*tests["direct"])
        acc["direct"].append(np.abs(b / se) > t_crit(df))
        acc["est_direct"].append(b)

        parts = [coef(*leg) for leg in tests["indirect"]]
        joint = np.ones(R, dtype=bool)
        draws = np.ones((R, mc_draws))
        point = np.ones(R)
        for bb, ss, dd in parts:
            joint &= np.abs(bb / ss) > t_crit(dd)
            draws *= bb[:, None] + ss[:, None] * rng.standard_normal((R, mc_draws))
            point *= bb
        lo_ci = np.quantile(draws, ALPHA / 2, axis=1)
        hi_ci = np.quantile(draws, 1 - ALPHA / 2, axis=1)
        acc["indirect"].append((lo_ci > 0) | (hi_ci < 0))
        acc["joint"].append(joint)
        acc["est_indirect"].append(point)

        if "moderation" in tests:
            b, se, df = coef(*tests["moderation"])
            acc["moderation"].append(np.abs(b / se) > t_crit(df))
            acc["est_moderation"].append(b)
        done += R
    return {k: np.concatenate(v) for k, v in acc.items() if v}


def boot_check(model, N, reps, B, rng, items, lo, hi, mc_draws):
    """Percentile bootstrap vs Monte Carlo interval for the indirect effect."""
    eqs = equations(model)
    legs = model.tests["indirect"]
    agree = mc_hits = boot_hits = 0
    for _ in range(reps):
        L = model.simulate_latent(rng, 1, N)
        C = composites(model, L, rng, items, lo, hi)
        # Monte Carlo interval on the original sample
        prod_draw = np.ones((1, mc_draws))
        for tgt, pred in legs:
            b, se, _ = ols(C, tgt, eqs[tgt])
            i = eqs[tgt].index(pred)
            prod_draw = prod_draw * (b[0, i] + se[0, i]
                                     * rng.standard_normal((1, mc_draws)))
        mc_sig = not (np.quantile(prod_draw, .025) <= 0 <= np.quantile(prod_draw, .975))
        # Bootstrap: resample respondents, re-standardise, re-estimate
        idx = rng.integers(0, N, size=(B, N))
        CB = {}
        for v, arr in C.items():
            CB[v] = standardise(arr[0][idx])
        for a_, (x1, x2) in model.prods.items():
            CB[a_] = standardise(CB[x1] * CB[x2])
        prod = np.ones(B)
        for tgt, pred in legs:
            b, _, _ = ols(CB, tgt, eqs[tgt])
            prod *= b[:, eqs[tgt].index(pred)]
        bt_sig = not (np.quantile(prod, .025) <= 0 <= np.quantile(prod, .975))
        mc_hits += mc_sig
        boot_hits += bt_sig
        agree += (mc_sig == bt_sig)
    return mc_hits / reps, boot_hits / reps, agree / reps


# ── Rules of thumb ────────────────────────────────────────────────────────────

def inverse_sqrt_root(p_min, z=2.486):
    """Kock & Hadaya (2018): N_min > (2.486 / |p_min|)^2 at 5%, 80% power."""
    return math.floor((z / abs(p_min)) ** 2) + 1


def ten_times(max_arrows):
    """10 x the largest number of structural paths pointing at one construct
    (all constructs here are reflective, so no formative-indicator count)."""
    return 10 * max_arrows


# ── Summaries ─────────────────────────────────────────────────────────────────

def min_n_for(rows, model, test, beta, target=0.80):
    """Smallest grid N reaching the target, linearly interpolated."""
    pts = sorted((r["N"], r["power"]) for r in rows
                 if r["model"] == model and r["test"] == test
                 and abs(r["beta"] - beta) < 1e-9)
    prev = None
    for n, p in pts:
        if p >= target:
            if prev is None:
                return f"<= {n}"
            n0, p0 = prev
            est = n0 + (target - p0) * (n - n0) / (p - p0)
            return f"~{int(math.ceil(est / 5.0) * 5)}"
        prev = (n, p)
    return f"> {pts[-1][0]}" if pts else "n/a"


def frame_needed(target, prevalence, response, survival):
    r = feasibility(frame=1, prevalence=prevalence, response_rate=response,
                    completion_rate=1.0, exclusion_rate=1.0 - survival,
                    target=target)
    return r["frame_needed"]


def human(n):
    if n == float("inf"):
        return "inf"
    if n >= 1e6:
        return f"{n / 1e6:.1f}M"
    if n >= 1e4:
        return f"{n / 1e3:.0f}k"
    return f"{n:,.0f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--reps", type=int, default=2000, help="replications per cell")
    ap.add_argument("--seed", type=int, default=20261020)
    ap.add_argument("--items", type=int, default=5, help="indicators per construct")
    ap.add_argument("--loading-lo", type=float, default=0.70)
    ap.add_argument("--loading-hi", type=float, default=0.80)
    ap.add_argument("--background", type=float, default=0.10,
                    help="size of every non-focal structural path")
    ap.add_argument("--rho", type=float, default=0.30,
                    help="correlation among the eight interventions (QUAL)")
    ap.add_argument("--mc-draws", type=int, default=2000)
    ap.add_argument("--chunk", type=int, default=250)
    ap.add_argument("--boot-check", type=int, default=300,
                    help="reps for the bootstrap-vs-MC check (0 = skip)")
    ap.add_argument("--boot-B", type=int, default=1000)
    ap.add_argument("--outdir", default=HERE)
    a = ap.parse_args()

    t0 = time.time()
    rows = []
    r2_notes = []
    for mi, (mname, build) in enumerate(
            (("QUAL", lambda b: qual_model(b, a.background, a.rho)),
             ("CHAIN", lambda b: chain_model(b, a.background)))):
        for bi, beta in enumerate(GRID_BETA):
            model = build(beta)
            r2_notes.append((mname, beta, dict(model.r2)))
            for N in GRID_N:
                ss = np.random.SeedSequence([a.seed, mi, bi, N, a.items])
                rng = np.random.default_rng(ss)
                res = run_cell(model, N, a.reps, rng, a.items,
                               a.loading_lo, a.loading_hi, a.mc_draws, a.chunk)
                tests = [("direct", "direct", "est_direct"),
                         ("indirect_mc", "indirect", "est_indirect"),
                         ("indirect_joint", "joint", "est_indirect")]
                if "moderation" in res:
                    tests.append(("moderation", "moderation", "est_moderation"))
                for tname, key, est in tests:
                    p = float(res[key].mean())
                    truth = model.true["indirect" if "indirect" in tname else tname]
                    rows.append({
                        "model": mname, "test": tname, "beta": beta, "N": N,
                        "reps": a.reps, "items": a.items, "power": p,
                        "mc_se": math.sqrt(p * (1 - p) / a.reps),
                        "true_value": truth,
                        "mean_estimate": float(res[est].mean()),
                    })
                print(f"  {mname:<5} beta={beta:.2f} N={N:<4} "
                      + "  ".join(f"{r['test']}={r['power']:.3f}"
                                  for r in rows[-len(tests):]),
                      flush=True)
    sim_secs = time.time() - t0

    suffix = "" if a.items == 5 else f"_items{a.items}"
    csv_path = os.path.join(a.outdir, f"power_results{suffix}.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        for r in rows:
            w.writerow({k: (f"{v:.4f}" if isinstance(v, float) else v)
                        for k, v in r.items()})

    boot = None
    if a.boot_check:
        rng = np.random.default_rng(np.random.SeedSequence([a.seed, 99]))
        model = qual_model(0.20, a.background, a.rho)
        tb = time.time()
        boot = boot_check(model, 100, a.boot_check, a.boot_B, rng, a.items,
                          a.loading_lo, a.loading_hi, a.mc_draws)
        boot = boot + (time.time() - tb,)

    write_table(a, rows, r2_notes, boot, sim_secs, suffix)
    print(f"\nSimulation time {sim_secs:.0f}s; total {time.time() - t0:.0f}s")
    print(f"Wrote {csv_path}")
    return 0


def write_table(a, rows, r2_notes, boot, secs, suffix):
    L = []
    L.append("# Sample size table")
    L.append("")
    L.append("AI-use disclosure: simulation code and tables drafted with Claude (Anthropic) on 20 Oct 2026 as an analysis aid; assumptions and interpretation to be reviewed and owned by Yasir Malik.")
    L.append("")
    L.append(f"Generated by `power_sim.py` (seed {a.seed}, {a.reps} replications "
             f"per cell, {a.items} items per construct, loadings "
             f"U({a.loading_lo:.2f}, {a.loading_hi:.2f}), background paths "
             f"{a.background:.2f}, intervention intercorrelation {a.rho:.2f}). "
             f"Simulation time {secs:.0f} s.")
    L.append("")
    L.append("Two-tailed alpha = .05. Power = share of replications in which the "
             "test rejects. Estimation = mean-score composites + OLS, an "
             "approximation of PLS-SEM. Minimum N is interpolated between grid "
             "points (30, 50, 75, 100, 150, 200, 300, 500, 750, 1000) and rounded up to 5.")
    L.append("")
    L.append("## 1. Minimum N for 80% power")
    L.append("")
    L.append("Effect size = every focal standardised path in the cell. The indirect "
             "effect is therefore beta^2 (QUAL, two legs) or beta^3 (CHAIN, three legs).")
    L.append("")
    L.append("| Model | Test | beta = 0.10 | beta = 0.20 | beta = 0.30 |")
    L.append("|---|---|---|---|---|")
    labels = [("QUAL", "direct", "Direct path (TA -> RAB)"),
              ("QUAL", "indirect_mc", "Indirect TA -> AJQ -> RAB, MC CI"),
              ("QUAL", "indirect_joint", "Indirect, joint significance"),
              ("QUAL", "moderation", "Moderation"),
              ("CHAIN", "direct", "Direct path (M2 -> Y)"),
              ("CHAIN", "indirect_mc", "Serial indirect X -> M1 -> M2 -> Y, MC CI"),
              ("CHAIN", "indirect_joint", "Serial indirect, joint significance"),
              ("CHAIN", "moderation", "Moderation (X x W -> M1)")]
    for m, t, lab in labels:
        if m == "QUAL" and t == "moderation":
            L.append("| QUAL | Moderation | not hypothesised | not hypothesised "
                     "| not hypothesised |")
            continue
        cells = [min_n_for(rows, m, t, b) for b in GRID_BETA]
        tag = "CHAIN (illustrative)" if m == "CHAIN" else m
        L.append(f"| {tag} | {lab} | " + " | ".join(cells) + " |")
    L.append("")
    L.append("## 2. Power at each N")
    L.append("")
    for m in ("QUAL", "CHAIN"):
        tests = ["direct", "indirect_mc", "indirect_joint"] + \
            (["moderation"] if m == "CHAIN" else [])
        L.append(f"### {m}{' (illustrative)' if m == 'CHAIN' else ''}")
        L.append("")
        L.append("| beta | Test | " + " | ".join(f"N={n}" for n in GRID_N) + " |")
        L.append("|---|---|" + "---|" * len(GRID_N))
        for b in GRID_BETA:
            for t in tests:
                vals = [next(r["power"] for r in rows if r["model"] == m and
                             r["test"] == t and abs(r["beta"] - b) < 1e-9 and
                             r["N"] == n) for n in GRID_N]
                L.append(f"| {b:.2f} | {t} | " +
                         " | ".join(f"{v:.2f}" for v in vals) + " |")
        L.append("")
    L.append("Monte Carlo standard error of a power estimate is at most "
             f"{0.5 / math.sqrt(a.reps):.3f} (at power 0.50).")
    L.append("")
    L.append("## 3. Attenuation from composite scoring (N = 1000)")
    L.append("")
    L.append("Mean estimated path vs the true latent path. Mean scores carry "
             "measurement error, so estimates shrink toward zero; this is one "
             "reason simulated N exceeds the rule-of-thumb N.")
    L.append("")
    L.append("| Model | Test | beta | true | mean estimate |")
    L.append("|---|---|---|---|---|")
    for r in rows:
        if r["N"] == 1000 and r["test"] in ("direct", "moderation"):
            L.append(f"| {r['model']} | {r['test']} | {r['beta']:.2f} | "
                     f"{r['true_value']:.3f} | {r['mean_estimate']:.3f} |")
    L.append("")
    L.append("Population R-squared of endogenous constructs (latent level): " +
             "; ".join(f"{m} b={b:.2f}: " +
                       ", ".join(f"{k} {v:.2f}" for k, v in r2.items())
                       for m, b, r2 in r2_notes) + ".")
    L.append("")
    if boot:
        mc, bt, ag, bs = boot
        L.append("## 4. Bootstrap check (QUAL indirect, beta = 0.20, N = 100)")
        L.append("")
        L.append(f"{a.boot_check} replications, {a.boot_B} percentile bootstrap "
                 f"resamples each ({bs:.0f} s). Power with Monte Carlo CI "
                 f"{mc:.2f}; with percentile bootstrap {bt:.2f}; the two "
                 f"intervals reached the same decision in {ag * 100:.0f}% of "
                 "replications.")
        L.append("")

    L.append("## 5. Rules of thumb for comparison")
    L.append("")
    L.append("Inverse square root method (Kock & Hadaya, 2018): N_min > "
             "(2.486 / |p_min|)^2, for 5% significance and 80% power. The "
             "constant 2.486 is 1.645 + 0.842, a one-tailed 5% test. The "
             "simulation above is two-tailed, which by itself requires about "
             "26% more N.")
    L.append("")
    L.append("| p_min | Inverse square root N_min | Two-tailed analogue ((1.960 + 0.842) / p_min)^2 |")
    L.append("|---|---|---|")
    for b in GRID_BETA:
        two = math.floor(((1.95996 + 0.84162) / b) ** 2) + 1
        L.append(f"| {b:.2f} | {inverse_sqrt_root(b)} | {two} |")
    L.append("")
    L.append("Ten-times rule (10 x the largest number of arrows pointing at one "
             "construct; all constructs here are reflective):")
    L.append("")
    L.append("| Model | Largest in-degree | Ten-times N |")
    L.append("|---|---|---|")
    L.append(f"| QUAL | 10 (RAB: 8 interventions + AJQ + APR) | {ten_times(10)} |")
    L.append(f"| CHAIN (illustrative) | 3 (M1: X, W, X x W) | {ten_times(3)} |")
    L.append("")
    L.append("The ten-times rule does not depend on effect size, which is why it "
             "can sit far below the simulated N for small paths.")
    L.append("")

    # ── Frame sizes ──
    prev = CASE["eligible"] / CASE["frame"]
    surv = CASE["usable"] / CASE["raw"]
    targets = sorted({ten_times(3), ten_times(10)} |
                     {inverse_sqrt_root(b) for b in GRID_BETA})
    sim_targets = []
    for m, t in (("QUAL", "direct"), ("QUAL", "indirect_mc")):
        for b in GRID_BETA:
            s = min_n_for(rows, m, t, b)
            if s.startswith("~"):
                sim_targets.append(int(s[1:]))
    targets = sorted(set(targets) | set(sim_targets) | {30, 100})

    L.append("## 6. Sampling frame needed to reach each N")
    L.append("")
    L.append("Frame needed = N / (prevalence x response x screen survival), "
             "computed with `feasibility()` from `../feasibility.py`. Completion "
             "is folded into response.")
    L.append("")
    L.append(f"### 6a. General research panel, observed prevalence "
             f"({prev * 1e5:.1f} per 100,000 = {CASE['eligible']} / "
             f"{CASE['frame']:,}), observed screen survival "
             f"{surv * 100:.0f}% ({CASE['usable']} / {CASE['raw']})")
    L.append("")
    L.append("Observed response among eligible was about 1.0 (23 starts from "
             "about 20 eligible). Lower response rates are shown for comparison.")
    L.append("")
    rr = (1.0, 0.50, 0.25, 0.10)
    L.append("| Target N | " + " | ".join(f"response {x:.2f}" for x in rr) + " |")
    L.append("|---|" + "---|" * len(rr))
    for n in targets:
        L.append(f"| {n} | " + " | ".join(
            human(frame_needed(n, prev, x, surv)) for x in rr) + " |")
    L.append("")

    scen = [
        ("Panel, broadened population, 50x observed prevalence",
         prev * 50, 1.0, surv,
         "50x is the low end of the repo's own estimate (STUDY_OVERVIEW.md s8), "
         "not a measurement. Observed survival kept."),
        ("Panel, broadened population, 100x observed prevalence",
         prev * 100, 1.0, surv, "High end of the same estimate."),
        ("Professional association list (cold email)",
         0.40, 0.08, 0.70,
         "ASSUMPTIONS: 40% of members eligible, 8% respond, 70% survive screening."),
        ("Referral / snowball from known professionals",
         0.60, 0.30, 0.80,
         "ASSUMPTIONS: 60% of referred contacts eligible, 30% respond, 80% survive. "
         "Frame = people contacted."),
    ]
    L.append("### 6b. Targeted channels and broadened population (ASSUMED rates)")
    L.append("")
    L.append("Every rate in this table is an assumption to be replaced by observed "
             "rates from the first wave or a pilot. None is measured.")
    L.append("")
    L.append("| Scenario | prevalence | response | survival | " +
             " | ".join(f"N={n}" for n in targets) + " |")
    L.append("|---|---|---|---|" + "---|" * len(targets))
    for name, p, r, s, _ in scen:
        L.append(f"| {name} | {p:.4f} | {r:.2f} | {s:.2f} | " + " | ".join(
            human(frame_needed(n, p, r, s)) for n in targets) + " |")
    L.append("")
    for name, _, _, _, note in scen:
        L.append(f"- {name}: {note}")
    L.append("")
    path = os.path.join(a.outdir, f"sample_size_table{suffix}.md")
    with open(path, "w") as f:
        f.write("\n".join(L))
    print(f"Wrote {path}")


if __name__ == "__main__":
    sys.exit(main())
