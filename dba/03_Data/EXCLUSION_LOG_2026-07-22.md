# Data Screening & Exclusion Log — Jul 22, 2026 Export

**Source:** `raw_export_2026-07-22.csv` (Qualtrics export, 23 raw recorded responses)
**Method:** `clean_and_screen.py` — deterministic screening, not manual judgment calls, to keep this defensible.

## Result: n = 4 valid responses (of 23 raw)

| ResponseId | Recorded | Notes |
|---|---|---|
| R_5XWxEfPGGJzpso9 | 2026-06-30 16:05 | Internal audit, Big 4, Financial services, 6-10yr int. exp. |
| R_65Wleya4RqVqfN3 | 2026-07-01 10:04 | 17.8hr duration (left open, not continuous) — flagged, not excluded, since data is complete |
| R_3neXhvsYnz0duIf | 2026-07-15 13:07 | External audit, Mid-tier, Financial services |
| R_9GYSf7lLWWrP1jr | 2026-07-15 13:45 | External audit, Small firm, Government/nonprofit |

## Exclusion breakdown (19 excluded) — v2, corrected labels (2026-07-22 re-run)

| Reason | Count |
|---|---|
| Did not finish (Finished=False, 3-39% progress) | 9 |
| Finished=True but substantive Likert blocks blank | 5 |
| Failed screen S1: not US-based | 2 |
| Failed screen S3: no audit role in last 24mo | 1 |
| Researcher's own survey preview | 1 |
| Self-identified "Test run" | 1 |

**Correction vs. v1:** the response previously labeled "failed attention check AC1" (R_7SdF53CX9nnr1s4) was in fact substantively blank — reclassified. Among complete, eligible respondents, **zero failed either attention check** (consistent with the 95% Qualtrics response-quality score). All screens now applied exactly as built into the IRB-approved instrument, including S4 (continuing-engagement) and S5 (attestation) — all 4 valid respondents pass every screen.

## Recoverable-if-criteria-relaxed (complete + substantive, failed exactly one screen)
- R_2XpqjoL5dSyhAqL — failed only S1 (non-US); complete, 11-15yr internal audit experience.
- R_4T1UzLbMr2PSwgN — failed only S1 (non-US); complete.
- R_6o6epBI1rJUJTkC — failed only S3 (audit-role); complete; D2_ROLE self-report ("Audit support / other audit-related role") arguably contradicts the S3=No answer — possible respondent confusion, worth manual review.

If the US-only restriction is relaxed: **n = 6** (7 if the S3-conflict case is also admitted). Still below any CFA/EFA feasibility threshold, but materially better for descriptive + reliability reporting.

## Why CFA is not feasible at this n
11 constructs × 5 items = 55 observed variables. A CFA model of this size has far more free parameters (factor loadings, error variances, factor covariances) than there are data points at n=4 — the model is not identified, and even where software would return a solution, it would be a computational artifact, not a valid statistical result. This must be raised with Dr. Rey before Friday — his instruction (CFA via Jamovi) was almost certainly given without knowing the true screened n is 4, not the ~22-23 raw count.

## Recommended path (for Friday's meeting)
1. Report the honest screening result and why formal CFA is not viable at this n.
2. Offer the recoverable-criteria option (n=7) for his input — is US-only a hard requirement given the research question is about auditor judgment generally, or was it a convenience restriction?
3. Propose the fallback already pre-agreed in the small-n contingency plan (`Daily_Sprint_Jul09_to_Jul19.md`): at n<30, default to descriptives + reliability (if computable) + item-level qualitative analysis of the open-text responses, presenting the study honestly as a pilot/feasibility study rather than a validated CFA.
4. The four (or seven) open-text responses are genuinely rich and audit-literate — worth a short qualitative synthesis regardless of what quantitative path is chosen.
