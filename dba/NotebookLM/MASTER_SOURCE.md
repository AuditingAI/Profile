> ⚠️ **SUPERSEDED — 11 August 2026.** This pack was built 24 July 2026, before the qualifying
> examination result, Dr. Rey's five directives, chain v1.1, and the P1 manuscript draft. Do not
> study from it and do not upload it to NotebookLM.
>
> **Current pack: [`sources/`](sources/) — see [README.md](README.md) for setup and the daily loop.**

# MASTER SOURCE — Anchoring Bias in Audit Judgment & AI Epistemic Risk
Yasir A. Malik · FIU DBA Cohort 7.16 · IRB-25-0462 · July 2026

## 1. What the study is
A measurement-model study of how organizational interventions reduce ANCHORING BIAS in long-term (multi-year) audit engagements, and its extension into AI-assisted judgment.

Core problem: in continuing engagements the anchor is structural, not incidental. Prior-year balances, management estimates, budgets, and prior workpapers are built into the audit file. The auditor does not seek an anchor — the engagement supplies one. Anchoring-and-adjustment (Tversky & Kahneman, 1974) predicts insufficient adjustment away from that starting point.

Research questions:
RQ1. Can the eight interventions, two mediators, and the outcome be measured as distinct, reliable constructs among practicing auditors?
RQ2. What is the factor structure of the 55-item instrument — do items cohere into the eleven theorized constructs?
RQ3. (Framework for later) How are interventions associated with reduced anchoring, directly and through the two mediators?

## 2. The model — 11 constructs
Eight interventions (independent variables):
1. Training & Awareness (TA) — firm training on cognitive bias and de-anchoring technique
2. Rotation of Auditors (RA) — personnel rotation bringing a fresh look to recurring clients
3. Use of Analytical Tools (AT) — analytics generating independent current-period expectations
4. Structured Auditing Processes (SAP) — procedures forcing evidence-before-anchor evaluation
5. Feedback & Reflection (FR) — debriefs and judgment-quality feedback loops
6. Independent Reviews (IR) — substantive re-examination by uninvolved reviewers
7. Regulatory & Professional Guidance (RPG) — PCAOB/AICPA/IIA/COSO discipline
8. Performance Metrics & Incentives (PMI) — evaluation rewarding judgment quality over speed

Two mediators:
9. Auditor Judgment Quality (AJQ) — cognitive pathway: careful, objective evaluation of independent evidence
10. Audit Process Rigor (APR) — procedural pathway: thorough, consistent, disciplined execution

Outcome:
11. Reduction in Anchoring Bias (RAB) — final judgments driven by current evidence, not initial reference points

Sixteen hypotheses: 8 direct paths (each intervention → RAB) + 8 mediated paths. Six judgment-oriented interventions (TA, RA, AT, FR, RPG, PMI) operate through AJQ; two structural interventions (SAP, IR) operate through APR.

Theoretical lens: dual-process theory. Interventions interrupt System-1 reliance on an available anchor and force System-2 evaluation.

## 3. Instrument and method
55 substantive Likert items (5 per construct, 1 reverse-coded each), 5 eligibility screens (US location, English fluency, audit role within 24 months, continuing-engagement experience, attestation), 2 embedded attention checks, 1 open-ended anchoring-experience item, demographics. Built in Qualtrics; anonymized, bot-detected, duplicate-protected.

Planned analysis contract:
- Suitability: KMO ≥ .60 (≥ .80 preferred), Bartlett significant
- EFA: principal-axis factoring (shared common variance, not PCA); retention by eigenvalue + scree + parallel analysis; both rotations run, Direct Oblimin reported; item retention at primary loading ≥ .40, cross-loading within .20 flagged, removed one at a time
- Reliability: Cronbach's α (≥ .70), item-total correlations, alpha-if-deleted, McDonald's ω alongside
- CFA: ML estimation; χ² with df, χ²/df ≤ 3, CFI/TLI ≥ .90, RMSEA ≤ .08 with 90% CI, SRMR ≤ .08; AVE ≥ .50, Fornell-Larcker, HTMT < .85
- Regression: hierarchical entry, VIF < 5, Durbin-Watson, Cook's distance
- PLS-SEM: outer loadings ≥ .708, composite reliability ≥ .70, AVE ≥ .50, HTMT < .85, 5,000-resample bootstrap, f² at .02/.15/.35
Software: Jamovi (EFA/reliability/CFA/regression), SmartPLS for PLS-SEM, Python for scripted cleaning.

Cleaning protocol (order matters, each exclusion has one recorded cause): remove researcher/test records → remove unfinished → remove empty completions → apply eligibility screens → apply attention checks → reverse-code → handle missing data → screen outliers and straight-lining (assessed on RAW responses, before reverse-coding, or the screen cannot work) → log every exclusion.

## 4. What actually happened — the feasibility finding
Target: n = 100. Achieved: four to five usable responses from 23 raw starts.

The decisive evidence is from the recruitment platform's own screening: applying the eligibility criteria to a panel of 334,976 registered participants returned approximately 20 eligible people — a prevalence of roughly six per 100,000. Compensation was not the constraint (effective rate ~$28/hour, well above academic norms). Design was not the constraint (zero attention-check failures among complete respondents; platform response-quality index 95%). The constraint was arithmetic: no budget fills 100 seats from a pool of 20.

Consequence: EFA, reliability, CFA, regression, and PLS-SEM were all infeasible. The study was reframed as a pilot/feasibility study. What it establishes: the instrument fields cleanly, the screening protocol works, and the qualitative accounts from respondents describe the anchoring-and-adjustment mechanism unprompted — an anchor forms, and adjustment occurs only when a specific evidentiary trigger appears (a regulatory change, contradictory documentation, an outlier item). The implication is that absent such a trigger, the anchor persists unadjusted.

## 5. The dissertation extension — the AI layer
Refined causal chain: LLM/AI audit tool → AUTOMATED ANCHORING → SYCOPHANTIC CONFIRMATION → RECURSIVE EPISTEMIC DRIFT → erodes reduction in anchoring bias.

Automated anchoring: when results are generated by the system, the anchor is no longer the auditor's memory of the prior year — it is machine output produced continuously and at scale. This fuses anchoring with automation bias (Parasuraman & Manzey, 2010).

Sycophantic confirmation: LLMs systematically shift toward the position the user has already stated, because preference-based training rewards agreement over truthfulness (Sharma et al., 2024, ICLR; Perez et al., 2023, ACL). Measured sycophancy occurs in a majority of tested cases, including regressive shifts from correct to incorrect answers under user pushback (Fanous et al., 2025). In a continuing engagement, the auditor's prior-year expectation is exactly the kind of pre-stated position a sycophantic model confirms — so the tool does not dislodge the anchor, it re-arms it with apparent independent authority.

Recursive epistemic drift: human bias entering an AI system is absorbed, amplified, and returned, with users largely unaware (Glickman & Sharot, 2025, Nature Human Behaviour). Reliance on generative tools measurably reduces enacted critical thinking (Lee et al., 2025, CHI). Recursive reprocessing of generated content degrades and converges (Shumailov et al., 2024, Nature). Collectively this produces "illusions of understanding" and epistemic monoculture (Messeri & Crockett, 2024, Nature).

Audit-domain and governance anchors: over-reliance on LLM output threatens professional skepticism (Fotoh & Mugwira, 2025, IJAIS). AI investment at firm level associates with fewer restatements (Fedyk et al., 2022). Auditors discount contradictory AI evidence relative to identical human-specialist evidence — algorithm aversion (Commerford et al., 2022, Journal of Accounting Research). Identical algorithmic risk signals produce inconsistent risk responses (Koreff, 2022). Opaque models push auditors back onto existing client knowledge — anchoring by default (Kokina et al., 2025). NIST AI 600-1 (2024) names this risk class "Human-AI Configuration"; PCAOB (2024) requires supervision of generative output; IAASB (2024) folds automated tools into audit-evidence standards.

Contribution claim: sycophancy has validated behavioral measurement (SycophancyEval, SycEval). Epistemic drift has NO standardized instrument. Operationalizing epistemic drift against independent-evidence benchmarks is the dissertation's measurement contribution.

## 6. The path forward
1. Close the course — submit the manuscript.
2. Complete the advisor's simulated-data exercise — full EFA/reliability pipeline on a dataset with the same constructs, demonstrating analytic competency separately from the paper.
3. Recover the escrowed panel budget (~$980) by stopping the underfilled study.
4. Fix the population: broaden from "US auditors" to "risk and assurance professionals" — internal audit, enterprise risk management, compliance testing, credit/loan review, quality assurance, SOX controls testing. The same multi-period anchoring mechanism operates in all of them; the population is orders of magnitude larger. Validate free using the panel's eligibility counter before spending.
5. Re-specify the instrument: keep the eleven-construct core, add three AI blocks (automated anchoring, sycophantic confirmation, recursive epistemic drift) plus an AI-exposure routing item; trim the core to three items per construct so total length lands near 12 minutes. Requires IRB amendment covering both population and new items — hard gate, nothing fields before it.
6. Run the Chapter 4 contract at adequate sample.

## 7. Key limitations to state honestly
The required analyses were not performed; the study validates nothing statistically. Achieved sample was 4-5 against a target of 100. The population definition was too narrow to be reachable on research panels. Approximately $1,000 of paid recruitment yielded almost nothing. Data collection started too late in the term to re-scope within the course window. Self-report measures of one's own bias remain subject to social desirability and limited self-insight.
