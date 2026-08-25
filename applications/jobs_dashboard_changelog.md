# Job Pipeline Dashboard — Build Changelog

**Run date:** 2026-05-22 · **Built by:** Claude (Opus 4.7)
**Output:** `/home/user/workspace/yasir_malik_jobs_dashboard.xlsx`

## What this run produced

- **49 curated roles** across NJ + NY corridor + hybrid/remote.
- **Tier mix:** 9 × Tier 1 (bullseye, 9.0+), 17 × Tier 2 (strong VP-level, 7.5–8.4), 11 × Tier 3 (solid backup, 6.5–7.4), 12 × Tier 4 (adjunct / supplemental).
- **Salary headline:** median mid $190K · top composite $285K · avg fit 7.4.
- **Roles ≥ $200K mid:** 19. **Roles with Fit ≥ 9.0:** 9.

## Top 3 picks for this week

1. **Prudential Financial — VP, Internal Audit, AI & Model Risk** (Newark, $200–290K, fit 9.6). Same town, exact mandate. Apply first.
2. **JPMorgan Chase — Executive Director, AI/ML Audit** (JC/NYC, $250–350K, fit 9.5). Boomerang to a known employer with a brand-new lane.
3. **Bristol Myers Squibb — Executive Director, Internal Audit** (Princeton, $220–310K, fit 9.4). Big Pharma ED title, sane commute.

## Quality gates — all green

| Gate | Result |
|---|---|
| Zero formula errors after recalc | ✅ 0 errors across 1,672 evaluated cells |
| All 6 KPI cards resolve | ✅ `[49, 19, 9, 190000, 285000, 7.4]` |
| Top-10 leaderboard aligns with TRJ rows 7–16 | ✅ rank-by-rank match |
| By Company / By Type cross-tabs sum to total | ✅ both = 49 |
| Tier Summary roles sum to total | ✅ T1+T2+T3+T4 = 49 |
| Auto-filter on Top Ranked Jobs | ✅ B6:Q55 |
| Freeze panes set | ✅ TRJ B7, Action Plan B6 |
| Hyperlinks point to stable search pages | ✅ 59 hyperlinks, all parametric search URLs (per spec §5) |

## Cover-letter targets to draft next

Prioritized by composite × fit and ease of internal-referrer outreach:

1. **Prudential VP, IA — AI & Model Risk.** Lead with Newark address + Citi consent-order experience.
2. **JPMorgan ED, AI/ML Audit.** Boomerang framing: prior CCAR + RRP scope on a $2.6T balance sheet.
3. **BMS ED, Internal Audit.** Pharma + AI controls angle; lean on DBA dissertation framing.
4. **Merck Director, Internal Audit — Technology & AI.** Rahway proximity + 3LOD AI assurance.

## URL strategy notes (regressions, if any)

No regressions. All employers in §5 of the spec resolve via the documented parametric search URLs. Two employers required slight URL pattern adjustments from the spec table:

- **Insmed:** uses a dedicated `careers.insmed.com/jobs` listing rather than a `peopleadmin` site.
- **Embecta** and **Legend Biotech:** both moved to Workday (`myworkdayjobs.com`); URLs in the data file reflect the current Workday tenant slugs.

## Recalc engine note

`scripts/recalc.py` tries LibreOffice headless first, then falls back to the `formulas` Python package as an in-process evaluator. In this sandbox LibreOffice could not load any file (a missing X11 dependency in the LO install) — the `formulas` fallback evaluated all 1,672 cells with zero errors. When the workbook is opened in Microsoft Excel, Excel's own recalculation engine will populate the cached value layer that the formulas engine just verified.

## Next refresh (Mon Jun 1, 2026)

1. Re-pull listing pages for each employer in §7.2 of the spec.
2. Add any new roles meeting fit ≥ 6.5; move closed roles to a `History` sheet (TODO — not yet implemented; this run produced a fresh workbook with no archive layer).
3. Re-run `scripts/build_jobs_dashboard.py`.
4. Email digest per spec §7 (uses existing `scripts/daily_jobs_email.py` plumbing).
