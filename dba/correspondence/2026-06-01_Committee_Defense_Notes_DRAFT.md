# Committee-Defense Notes — Three Items to Pre-Position with Dr. Rey

**Status:** DRAFT for Yasir's review. Not a chapter rewrite.
**Date:** 2026-06-01
**Purpose:** Pre-position three issues a defense committee will press, before they land as surprise comments. None of these block the informed pilot, the recruiting platforms, or the v4.2 paper. They are committee-defense readiness for later in the year.

---

## Why this brief exists

Dr. Rey's June 1 note approves the current path and asks for Qualtrics → informed pilot → CloudResearch / MTurk. None of the three items below block that sequence. They are surfaced now only because (a) raising them in a draft proposal is far cheaper than fielding them as objections at the defense, and (b) two of them have framing fixes Yasir can adopt before the proposal is finalized that cost little and pay a lot.

Walk Dr. Rey through this brief at the meeting after the Qualtrics build sign-off. Frame as: *"Three things I want to get ahead of for the committee — what's your view?"*

---

## Item 1 — Reframe the method as EFA + PLS-SEM (not "EFA-based")

**The issue.** The current title and method language is *"An EFA-Based Validation Study,"* and §3.5 says Chapter 4 will use "exploratory-factor-analytic and mediation procedures." A committee member will ask: *EFA cannot test mediation. How does EFA test H2, H4, H6, H8, H10, H12, H14, or H16?*

EFA validates the measurement model — that the items load on the 11 intended factors. It does not estimate directional or indirect (mediated) effects. The eight mediation hypotheses require a structural method.

**Recommended framing change (proposal-level, not new research).**

> *"This is a two-stage analytic design. Stage 1 uses exploratory factor analysis (EFA) on a split-sample to validate the measurement model implied by the eleven-construct instrument. Stage 2 estimates the structural model — the eight direct paths and eight mediated paths — using partial least squares structural equation modeling (PLS-SEM), with bootstrapped indirect-effect tests for the mediation hypotheses. PLS-SEM is selected over covariance-based SEM because (a) the model is large (eleven constructs, sixteen hypothesized paths) for the achievable sample size, (b) the focus is explanatory-predictive, and (c) PLS-SEM accommodates the mediation tests required by H2-H16 without imposing the multivariate-normality assumptions of CB-SEM."*

**What changes in the paper:**
- Title: *"Mitigating Anchoring Bias in Long-Term Auditor Engagements — A Survey-Based EFA and PLS-SEM Study."*
- §3.5 conclusion: replace the sentence "Chapter 4 operationalizes these constructs in a measurement instrument and specifies the exploratory-factor-analytic and mediation procedures…" with language pointing forward to a two-stage EFA + PLS-SEM analysis.
- Chapter 4 (not yet in this branch): when written, include the PLS-SEM specification, model fit indices, and the bootstrap protocol for indirect effects.

**Effort:** ~30 minutes of editing in the master.md plus a placeholder in the front-matter NOTE that Ch. 4 will specify the structural method. No new research, no IRB implications.

---

## Item 2 — Reframe the dependent variable honestly as self-assessed anchoring resistance

**The issue.** The DV (Reduction in Anchoring Bias, RAB) is measured by self-report Likert items (Appendix A.11), such as *"I adjust fully away from the prior-year balance when current evidence warrants."* A committee member will note that anchoring is paradigmatically a bias people cannot see in themselves (the bias blind spot, Pronin et al., 2002 — easily verifiable, not in the current ref pool), and that the dual-process theory selected as the study's lens explicitly says the mechanism is automatic (System 1). The auditors most anchored are the least able to report it. Self-reported debiasing is therefore a soft proxy for the construct as the theory defines it.

**Recommended framing change (no new data collection needed).**

Rename the DV operationally as *"Self-Assessed Anchoring-Resistant Work Practices (SAARP)"* or, more conservatively, retain RAB as the conceptual variable but add a precise paragraph to §2.3 distinguishing the *construct* (the auditor's actual anchoring) from the *operationalization* (their reported anchoring-resistant practices). This is honest, it positions the contribution as a measurement-development step toward a behavioral DV in a follow-on study, and it removes the largest construct-validity attack surface.

**Draft paragraph to insert at the end of §2.3:**

> *"A measurement note is necessary before the construct can be linked to its mediators. The conceptual DV — anchoring bias itself — is observed behaviorally in the seminal audit experiments by manipulating an anchor and measuring residual pull on a judgment (Joyce & Biddle, 1981; Kinney & Uecker, 1982; Northcraft & Neale, 1987). The present study, by design, uses a cross-sectional survey, which cannot manipulate an anchor in vivo. The instrument therefore operationalizes RAB as auditors' self-assessed engagement in anchoring-resistant work practices — independent expectation formation, full adjustment from prior-period figures, active search for disconfirming evidence (Appendix A.11). This operationalization is acknowledged as a soft proxy: dual-process theory holds that anchoring is partly automatic and therefore partly invisible to self-report (Evans, 2008; Kahneman, 2011). The study's contribution under this measurement choice is the validated, model-tested relationship of eight interventions to a survey-based behavioral-intent measure; an experimental follow-on with a manipulated anchor and a behavioral residual-pull DV is the natural next step the present work is intended to enable."*

**Effort:** ~15 minutes of editing. Adds two real citations (Pronin et al., 2002 if you want to be explicit about bias blind spot; Joyce, Kinney, Northcraft already in pool). No IRB implication. No instrument change.

---

## Item 3 — Handle the common-method-variance and firm-level confounding issue in Chapter 4

**The issue.** Every construct — 8 IVs, 2 mediators, 1 DV — is measured by the same respondent, the same instrument, the same Likert scale, in the same sitting. This is the textbook common-method-variance (CMV) condition. Compounding it: firm quality is a plausible common cause for several IV/DV pairs (good firms train *and* rotate *and* invest in analytics *and* review *and* are less anchored), which creates the appearance of intervention effects that are really firm-level confounding.

**Recommended fix (Chapter 4-level, no rework of the existing chapters).**

When Chapter 4 is written, include:
1. **Procedural CMV remedies already in the instrument:** anonymity, mixed item ordering, attention checks, reverse-coded items. These are already in Appendix A — name them as procedural CMV remedies.
2. **Statistical CMV tests after data collection:**
   - **Harman's single-factor test** (descriptive; weak but expected).
   - **Marker-variable test** using a theoretically unrelated marker item (e.g., a brief environmental-attitude item) to estimate and adjust the inter-construct correlations. Add one marker item to the instrument if IRB scope allows (likely a non-substantive change).
   - **Full collinearity assessment** (VIF) in the PLS-SEM, per Kock (2015), as a CMV diagnostic in PLS.
3. **Firm-level controls in the structural model:** add firm type (already collected in A.12) and firm size if collectible as covariates on AJQ, APR, and RAB. This soaks up firm-level variance and isolates the within-firm intervention effect.
4. **Acknowledge causal limits.** The hypotheses are framed *"is positively associated with"* — keep that exact wording in Ch. 4 and Ch. 5; do not slip into causal language.

**Effort:** Zero today. This is a Chapter 4 specification item. Marker item to instrument: ~1 minute of wording plus the IRB non-substantive change filing already in the action list.

---

## Recommended pilot-meeting talking-point order for Item-level discussion

If Dr. Rey opens any time for these:

1. **Method reframe.** *"For the committee, I'm thinking I retitle the study to EFA + PLS-SEM so the mediation hypotheses have a method that can actually test them. Same data, same instrument, same plan — just truth in labeling."*
2. **DV honesty.** *"I want to add a measurement-note paragraph to §2.3 saying the survey DV is self-assessed anchoring-resistant practices, not anchoring itself. This sets up the experimental follow-on as a planned next study rather than letting the committee say I should have done it now."*
3. **CMV plan for Chapter 4.** *"For Chapter 4 I'd add the procedural CMV remedies that are already in the instrument, plan a marker variable, and add firm type as a control on the mediators and DV. Want to flag this now so the Chapter 4 spec doesn't surprise the committee."*

---

## What's NOT in this brief (intentionally)

- **Instrument rewording** for cross-loading items (AJQ A.9-4 vs. RAB A.11-4; SAP A.4-2 vs. RAB A.11-2 vs. RA A.2-3). These would require an IRB amendment and delay the pilot. Park until post-pilot revision log identifies cross-loading empirically; address then.
- **Single-mediator-per-intervention** assignment scrutiny. Address in the PLS-SEM as: estimate all 16 paths from every IV through both mediators, report dominant pathway. No structural rewrite needed.
- **Theory–APR seam** (APR mechanism sits slightly outside the dual-process lens). One-paragraph fix during the proposal-defense draft, not today.

---

## Suggested next versions

- **v4.2 (today):** mechanical cleanup — Optional further reading boxes removed, orphan refs dropped. ALREADY APPLIED.
- **v4.3 (post-meeting, with Dr. Rey's input):** title change to EFA + PLS-SEM, §3.5 forward-pointer to PLS-SEM, §2.3 DV honesty paragraph. ~1 hour of editing.
- **v5.0 (after pilot data):** instrument cross-loading revisions, Chapter 4 with full CMV / marker-variable / firm-control plan, hypotheses refined where pilot data warrant.

---

*End of brief. — Claude, 2026-06-01*
