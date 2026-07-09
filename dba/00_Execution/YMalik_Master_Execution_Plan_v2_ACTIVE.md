# Master Execution Plan v2 — DBA Research Project
Yasir A. Malik | v2: 2026-07-08 (supersedes v1, archived in 99_Archive_Older_Drafts)
Governing deadlines: **n=100 valid by Jul 11** · **Final manuscript Jul 18–19**

> **⚠ SCOPE AMENDMENT v2.1 (2026-07-08, confirmed by Yasir).** Per Dr. Rey's written directive of Jun 30 — *"Your summer research project does not require testing any of the hypotheses (including mediation). Instead, your Data Analysis section should cover until EFA + Reliabilities"* — **Phase 3 step 8 (regressions + mediation) and all hypothesis testing are OUT OF SCOPE for this manuscript.** The analysis ends at EFA + reliabilities. H1–H16 remain in Section III as the proposed framework and are addressed in Conclusions as future research. The Results narrative's final analytical subsection is Reliability, not hypothesis tests.

**What changed in v2:** every phase is now aligned to Dr. Rey's own materials — the Assignment 4 EFA/reliability guided solution, the two Summer Research Exemplars (manuscript structure + Results narrative), the Prolific Setup Guide, the informed-pilot instrument template, and the Qualtrics collaborator/link instructions. Change log at the bottom.

---

## Prime directive (unchanged)
Approved mediator model only: TA, RA, AT, SAP, FR, IR, RPG, PMI → AJQ/APR → RAB. No AI/LLM anywhere except future research. Survey wording frozen.

---

## Phase 0 — Sync the two worlds (TODAY, Jul 8) — unchanged from v1

**YOU DO:** copy repo branch `claude/scholar-links-review-Plgk6` `dba/` folder into this project folder as `09_Repo_Sync`; confirm whether the Qualtrics pipeline is scripts or manual exports.
**CLAUDE DOES:** drift report, merged source of truth, standing `04_Data_and_Analysis` structure (raw / cleaned / outputs / decision log).

## Phase 1 — Hit n=100 (Jul 8–11) — now runs the professor's Prolific playbook

**YOU DO (daily ~10 min):**
1. Evening count to me (or drop the daily Qualtrics export in `04_Data_and_Analysis/raw/`).
2. **Prolific hygiene per Dr. Rey's guide:** approve submissions promptly (Prolific expects it); keep reward in the fair-pay green zone (~£3.50–£4.50 for 18 min); budget envelope ≈ $600–750 total for 100.
3. If scaling stalls: screenshot the eligible-participant count — that's the guide's trigger for loosening a filter or going to CloudResearch Managed.
4. **Decision gate — Thu Jul 9 evening:** valid trajectory < ~85 → trigger backup + free outreach (LinkedIn per the sample post format, IIA/AICPA chapters, FIU alumni).

**CLAUDE DOES:**
- Daily burn-down: valid n vs raw completes, attention-check fails, speeders (guide standard: exclude at cleaning, not mid-collection), oversample math.
- Soft-launch-style quality review on every batch: completion rate, attention-check pass rate, median completion time (the guide's Step 6 checks, applied daily).
- Draft outreach copy + Sarmed escalation + Dr. Rey status email the moment the gate trips.

## Phase 2 — Freeze, clean, validate (Jul 11–12) — now includes explicit outlier analysis

**YOU DO:** final Qualtrics export (numeric + choice text) into `raw/`; freeze survey; approve exclusion rules; confirm PROLIFIC_PID captured in embedded data.

**CLAUDE DOES (skills: data:explore-data, data:validate-data, xlsx):**
- **Data validation subsection evidence (exemplar structure):** duplicates, missingness, straight-lining, speeders, attention-check fails, PROLIFIC_PID integrity, screener consistency.
- **Outlier analysis (NEW — both exemplars report it):** boxplot/z-score screen per construct, document keep/drop decisions with rationale.
- Exclusion log → manuscript table + audit trail; update Analysis Decision Log.
- Reverse-code before reliability (PMI_4R — Assignment 4 flags this explicitly), compute construct scores, lock dataset.
- Demographics per exemplar style: means/SD/min/max by group, role/experience/education splits, external vs internal audit years.

## Phase 3 — Analysis (Jul 12–15) — now mirrors Assignment 4 step-for-step

This is Dr. Rey's own guided methodology; the manuscript's Data Analysis section (12 rubric pts) should read like his solution document.

**CLAUDE DOES (skills: data:statistical-analysis, data:analyze, data:create-viz):**
1. **Descriptives + distribution:** per-item and per-construct stats, histograms, boxplots, normality tests (skewness/kurtosis, Shapiro-Wilk; exemplar 2 also shows Q-Q plots) → manuscript Appendix (exemplar 1 has "Appendix D. Normality Tests").
2. **EFA pre-checks (Assignment 4 order):** KMO overall (report with Kaiser & Rice adjective, e.g., ".93 'marvelous'"); Bartlett's test; **anti-image diagonal per-item KMO ≥ .50** (drop + rerun if below); correlation-matrix screen (most rs ≥ .3, none > .9); **determinant > .00001**.
3. **Extraction:** Principal Axis Factoring + scree plot. Retention by convergence: eigenvalues > 1, scree inflexion, ≥ 50% variance explained, expected count (11).
4. **Rotation:** run BOTH Varimax and Direct Oblimin (the guide teaches both; report one with theoretical justification — oblique fits correlated constructs). **Suppress loadings < .3, sorted by size** (guide: .4 acceptable, never higher). The rotated loadings table is "the main one that should always be reported."
5. **Model fit check:** reproduced correlations — residuals < .05, report the percentage; concern threshold >50%.
6. **Watch item:** RPG dimensionality — if it splits, pre-agreed protocol: report + Dr. Rey sign-off (I draft the email).
7. **Reliability:** Cronbach's alpha per scale + item-total statistics with alpha-if-item-deleted (exact Assignment 4 output set).
8. ~~**Hypotheses (16):** regressions for direct paths; mediation via AJQ/APR (bootstrapped indirect effects, 5,000 resamples).~~ **OUT OF SCOPE per Scope Amendment v2.1** — analysis ends at step 7 (reliability). Hypotheses discussed qualitatively in Conclusions as future research.
9. **Write-up in the guide's reporting voice** — the Assignment 4 closing paragraph is the template sentence structure for the EFA narrative.
10. **Verification pass (data:validate-data):** every number re-derived programmatically before it enters the manuscript.

**Tooling note:** Assignment 4 is SPSS-based. I replicate the exact parameterization in Python and format outputs SPSS-style; if you also run SPSS at FIU, we cross-check — strongest possible evidence trail.

**YOU DO:** two ~20-min checkpoints — approve EFA solution + item drops; approve hypothesis interpretations.

## Phase 4 — Manuscript (Jul 13–17) — now built on the exemplar skeleton

Target: 11,000–16,500 words (both exemplars sit in this band). Structure (exemplar-conformant, rubric-complete):

| # | Section | Contents (rubric criteria folded in) |
|---|---|---|
| — | Title page | FIU DBA program, GEB7913, Dr. Rey, PID, date |
| — | Abstract | 150–250 words: objectives, methods, findings, significance |
| I | Introduction | Context, problem statement, significance, ends with explicit research question(s) |
| II | Literature Review | Constructs TA→RAB from 08_Expansion drafts; gaps; hypotheses emerge with rationale |
| III | Research Model & Hypotheses | Model diagram, construct definitions, H1–H16 formal statements |
| IV | Methodology | Design, instrument, 5-pt Likert justification (Preston & Colman 2000; Dawes 2008), sampling, Prolific procedure, IRB-25-0462, consent, anonymity |
| V | Results | **Exemplar narrative order (per Scope Amendment v2.1):** Informed Pilot (Richard review + pilot, using the question-quality typology: double-barreled/leading/loaded/confusing) → Qualtrics & Survey Instrument build (consent letter, screeners, force-response, attention checks — document what IS in the live build) → Data Collection → Data Validation → Outliers → Demographics → Normality → EFA → **Reliability (final analytical subsection)** → interpretation of the validated measurement model |
| — | Conclusions & Recommendations | Findings per RQ (measurement-model validation); practice implications; limitations; **hypotheses H1–H16 positioned as the tested-next framework**; **future research = AI/LLM dissertation bridge (only AI mention)** |
| VI | References | APA 7, DOI-formatted like exemplar 2 |
| — | Appendices (lettered) | Instrument v2, recruitment materials, IRB letter, informed-pilot feedback matrix (professor's xlsx format), exclusion log, Normality appendix, full EFA outputs |

**CLAUDE DOES:** assemble Jul 13–14 (front half needs no data); Results + Conclusions Jul 15–16; rubric self-score before your read.
**YOU DO:** full read Jul 16–17; Turnitin when possible (20-pt Ethics bucket); add Dr. Rey as Qualtrics collaborator if he asks to verify the build (pptx instructions are in Professor Intructions).

## Phase 5 — Final package + submission (Jul 17–19) — unchanged

Final consistency sweep, `07_Final_Submission` with FINAL naming, submit, confirm with Dr. Rey.

## Recurring — unchanged
Sunday weekly update (next: **Jul 12**; confirm W08 vs W09 numbering). Advisor questions logged before emailing.

---

## Change log: v1 → v2 (what the professor's materials changed)

1. **EFA spec rewritten to Assignment 4:** PAF + scree; retention by convergence (eigenvalues>1, scree, ≥50% variance); BOTH rotations run, one reported with justification; loading suppression at .3 (v1 said .40 — guide caps at .4, teaches .3); added per-item KMO ≥ .50 via anti-image diagonal, correlation screen (.3/.9), determinant > .00001, reproduced-correlation residuals < .05. KMO reported with Kaiser & Rice adjective.
2. **Reliability spec:** added item-total statistics table + reverse-coding-before-alpha requirement (PMI_4R).
3. **Outlier analysis added to Phase 2** — both exemplars report it as its own Results subsection; v1 only had exclusion cleaning.
4. **Manuscript reorganized to exemplar skeleton** (I–VI + lettered appendices): problem statement/RQs fold INTO Introduction; pilot + Qualtrics build + data collection move INTO Results as narrative subsections; conclusions/recommendations after Results. v1 treated rubric rows as standalone sections.
5. **Results must tell the execution story** — informed pilot (with the professor's question-quality typology), survey build details, validation, demographics in means/SD/min-max style. Richard's review + your pilot log are the raw material; they become Appendix + narrative.
6. **Word-count target set:** 11,000–16,500 (exemplar band), consistent with 40–60 page scaffold.
7. **Phase 1 adopts the Prolific guide operationally:** prompt approvals, fair-pay zone, $600–750 envelope, eligible-count screenshot as the backup trigger, soft-launch quality checks applied daily.
8. **SPSS alignment noted:** analysis replicates Dr. Rey's SPSS parameterization; optional SPSS cross-check.
9. **Qualtrics collaborator/link pptx logged** as the mechanism if Dr. Rey wants direct survey access at review.
10. **Abstract length pinned:** 150–250 words per rubric.

## Rubric traceability (updated)

| Rubric item (pts) | Covered by |
|---|---|
| Title, Abstract, Intro incl. problem + RQs (14) | Phase 4 §I + title page + abstract (150–250 w) |
| Literature Review (8) | Phase 4 §II from 08_Expansion |
| Model & Hypotheses (8) | Phase 4 §III — diagram + definitions + H1–H16 |
| Methodology (8) | Phase 4 §IV + IRB documentation |
| **Data Analysis (12)** | Phases 2–3 run Assignment 4's exact recipe: cleaning, descriptives, normality, outliers, EFA (full pre-checks), reliability + item-total, charts/tables — **ends at reliability per Scope Amendment v2.1 (no mediation)** |
| Conclusions + Recommendations (6) | Phase 4, per-hypothesis + limitations |
| References + Appendices (4) | APA 7 sweep + lettered appendices incl. instrument, recruitment, pilot matrix, data tables |
| Academic Writing (20) | Exemplar-benchmarked prose, APA 7, consistency sweep |
| Ethical Considerations (20) | IRB + consent + anonymity narrative; Turnitin (you) |

## Risk register — unchanged top 3
1. n<100 by Jul 11 → Jul 9 gate; CloudResearch Managed + outreach; document shortfall honestly, never slip the manuscript.
2. RPG splits in EFA → report + Dr. Rey sign-off (email pre-drafted).
3. Jul 15–17 compression → front-half drafted by Jul 14; rubric self-score before your read.

---

*Discipline now is cheap; regret later is expensive. Three days of counting responses, then we let the data speak.*
