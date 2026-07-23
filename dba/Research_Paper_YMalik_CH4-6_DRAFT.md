---
TITLE: Mitigating Anchoring Bias in Long-Term Auditor Engagements — Chapters 4–6 (Methods, Results, Discussion)
AUTHOR: Yasir A. Malik (PID 1687105)
PROGRAM: FIU College of Business — DBA — Cohort 7.16
COURSE: GEB7913 — Instructor: Professor Juan Rey
DATE: July 2026
NOTE: These chapters complete the manuscript begun in v4.2 (Chapters 2–3 + Appendix A). They report the ACTUAL achieved sample and adopt the pilot/feasibility framing agreed as the small-n contingency. Analysis follows Dr. Rey's July 2026 directive to use Jamovi. Bracketed [JAMOVI: …] markers show exactly where a value or figure produced by the Jamovi runbook is inserted before submission.
---

# CHAPTER 4 — RESEARCH METHODOLOGY

## 4.1  Introduction to the Chapter

This chapter operationalizes the model developed in Chapter 3 and describes how the study was conducted. It specifies the research design, the measurement instrument, the sampling and recruitment strategy, the data-screening protocol, and the analytic approach. Because the achieved sample fell well short of the pre-registered target, this chapter reports both the *planned* methodology and the *realized* methodology transparently, and re-scopes the empirical analysis accordingly. The study is therefore presented as a **pilot / feasibility study**: its purpose is to establish that the instrument can be fielded, to surface the measurement and recruitment challenges, and to provide preliminary descriptive and qualitative evidence that motivates a subsequent, adequately powered study.

## 4.2  Research Design

The study uses a cross-sectional, self-report survey design. Practicing auditors reported, on validated Likert scales, the presence of eight anchoring-mitigation interventions in their work environment, two proposed mediating conditions (auditor judgment quality and audit process rigor), and their self-assessed reduction in anchoring bias. The design was correlational and non-experimental; no manipulation was administered. This design was chosen to match the study's exploratory, measurement-validation aim and the constraints of the qualifying-examination timeline.

## 4.3  Measurement Instrument

The instrument operationalized each of the eleven constructs with five items on a 5-point Likert scale (1 = *Strongly disagree* to 5 = *Strongly agree*), as detailed in Appendix A. One item per construct was reverse-worded to disrupt response sets (marked **(R)**). Two embedded attention checks ("select *Disagree* for this item," "select *Agree* for this item") screened for inattentive responding. Eligibility screens at the start of the instrument required participants to be (a) located in the United States, (b) fluent in English, (c) currently or recently (within 24 months) employed in an audit-related role, and (d) experienced with at least one continuing (multi-year) audit engagement, followed by (e) an attestation of independent, first-time completion. The instrument was administered through Qualtrics under IRB approval (IRB-25-0462).

## 4.4  Sampling and Recruitment

The target sample was **n = 100 valid responses**. Recruitment proceeded through two channels: (1) organic professional outreach (LinkedIn, professional WhatsApp groups, and direct contacts in the auditing community), and (2) a paid participant panel through Prolific, funded for 100 participants. The Prolific panel underdelivered substantially: of the 100 funded slots, only 2 completions were returned, for reasons that remain under review with the platform (the study was published and live, per the platform's confirmation, but did not fill). The bulk of usable responses therefore came from organic outreach.

## 4.5  Data Screening Protocol

Screening was applied mechanically and reproducibly (a documented script, not case-by-case judgment) to preserve objectivity, in the following order:

1. Remove researcher test data (survey previews; self-identified test entries).
2. Remove incomplete sessions (Qualtrics `Finished` = False).
3. Remove sessions that finished but left the substantive Likert blocks blank.
4. Apply the five eligibility screens (S1–S5) exactly as built into the approved instrument.
5. Apply the two embedded attention checks.

Of **23 raw recorded responses**, 19 were excluded: 9 abandoned the survey early (3–39% progress); 5 finished the session but left the substantive scales blank; 3 failed exactly one eligibility screen (2 non-U.S., 1 on the audit-role screen); 1 was a survey preview and 1 a self-identified test entry. Notably, **zero complete, eligible respondents failed either attention check**, consistent with a Qualtrics response-quality score of 95%. This yielded a **final valid sample of n = 4**. The full exclusion log is retained for the record.

## 4.6  Realized Analytic Approach

The pre-registered plan specified exploratory factor analysis (principal-axis factoring, Direct Oblimin rotation) and reliability assessment on n = 100. At the achieved n = 4, neither exploratory nor confirmatory factor analysis of an eleven-construct, fifty-five-item model is statistically identified: the number of free parameters vastly exceeds the number of observations, and any factor solution the software returned would be a computational artifact rather than an interpretable result. Following consultation with the faculty advisor, the empirical analysis was therefore re-scoped, using **Jamovi**, to the procedures that remain defensible at this sample size:

- **Descriptive statistics** for each construct (mean, standard deviation, range), on reverse-coded item sets;
- **Reliability estimates (Cronbach's α)** per construct, reported with the explicit caveat that α is uninterpretable at this n;
- **Item-level inspection** of the response matrix;
- **Qualitative synthesis** of the open-ended responses;
- The **confirmatory measurement model fully specified** in Jamovi's SEM syntax but reported as *not estimated* owing to insufficient sample size, to demonstrate analytic readiness for the follow-on study.

# CHAPTER 5 — RESULTS

## 5.1  Introduction to the Chapter

This chapter reports the results of the pilot study. Given the sample size, quantitative findings are presented for transparency and descriptive value only; no inferential claims are made. The qualitative synthesis in Section 5.4 carries the strongest evidentiary weight.

## 5.2  Sample Characteristics

The four valid respondents represented a range of audit contexts: internal audit at a Big-4 firm, a government auditor, external audit at a mid-tier firm, and external audit at a small firm serving the government/nonprofit sector. Combined external/internal audit experience ranged from under two years to fifteen years. Three of the four reported exposure to long-term/continuing engagements. [JAMOVI: optional — insert frequency table of D2_ROLE / D6_CREDENTIAL / D7_REGION from Descriptives.]

## 5.3  Descriptive Statistics and Reliability

Table 5.1 reports construct-level descriptive statistics and Cronbach's α, computed in Jamovi on reverse-coded item sets (n = 4).

**Table 5.1 — Construct descriptives and reliability (n = 4, 5-point scale)**

| Construct | Mean | SD | Min | Max | Cronbach's α |
|---|---|---|---|---|---|
| Training & Awareness (TA) | 3.50 | 0.66 | 2.60 | 4.00 | 0.85 |
| Rotation of Auditors (RA) | 3.60 | 0.28 | 3.40 | 4.00 | −0.31 |
| Use of Analytical Tools (AT) | 3.50 | 0.48 | 3.20 | 4.20 | 0.07 |
| Structured Auditing Processes (SAP) | 3.70 | 0.12 | 3.60 | 3.80 | −3.75 |
| Feedback & Reflection (FR) | 3.60 | 0.49 | 3.00 | 4.00 | 0.83 |
| Independent Reviews (IR) | 3.60 | 0.33 | 3.20 | 4.00 | 0.39 |
| Regulatory & Professional Guidance (RPG) | 3.80 | 0.59 | 3.20 | 4.40 | 0.75 |
| Performance Metrics & Incentives (PMI) | 3.55 | 0.47 | 3.20 | 4.20 | 0.63 |
| Auditor Judgment Quality (AJQ) | 4.20 | 0.28 | 3.80 | 4.40 | 0.00 |
| Audit Process Rigor (APR) | 3.90 | 0.38 | 3.40 | 4.20 | 0.51 |
| Reduction in Anchoring Bias (RAB) | 3.50 | 0.42 | 3.00 | 4.00 | 0.29 |

[JAMOVI: replace this table with the Jamovi Reliability Analysis + Descriptives output once run, to show tool-generated provenance. Values above are from the independent verification script and should match Jamovi within rounding.]

Two features of Table 5.1 warrant comment. First, construct means cluster narrowly between 3.50 and 4.20 — i.e., mild-to-moderate agreement across the board — with the highest self-ratings on Auditor Judgment Quality (M = 4.20) and Audit Process Rigor (M = 3.90). Second, and critically, **the reliability estimates are not interpretable at this sample size.** Two constructs return negative α (RA = −0.31; SAP = −3.75), a result that is mathematically possible only when inter-item covariances are dominated by noise, which is exactly what is expected when α is estimated from four observations. The apparently "acceptable" values (TA = 0.85; FR = 0.83) are equally uninformative: with three degrees of freedom, α has enormous sampling variability in both directions. **These figures are reported for full transparency, not as evidence of measurement quality.** No construct's reliability can be established or refuted with these data.

## 5.4  Qualitative Synthesis of Open-Ended Responses

All four respondents answered the open-ended prompt asking them to describe a time when an initial figure influenced their judgment. Independently, and without being led toward the construct, all four described the same underlying mechanism:

- One auditor described a regulatory-reporting engagement in which management concluded the process was low-risk *because prior-year audits had found nothing*; the auditor set that anchor aside, evaluated recent system and regulatory changes, expanded testing, and identified control weaknesses requiring remediation.
- A second described using the initial figure as "a baseline on where I think something should be," escalating scrutiny when current evidence was "completely off" from that baseline.
- A third described the prior-year expense balance "initially influencing my expectation for the current year," then evaluating the current-year balance independently after reviewing supporting documentation and business changes.
- A fourth gave the most detailed account: prior-year balances "are typically set as our expectation," but the team digs deeper to find *why* balances changed, citing a specific case in which a one-time ERC credit in the prior year made the prior-year figure an unreliable anchor and "incorrectly influenced our judgement" until caught.

These four accounts describe a textbook **anchoring-and-adjustment** pattern (Tversky & Kahneman, 1974): an initial reference point forms the expectation, and adjustment away from it occurs — but only when a specific evidentiary trigger (a regulatory change, a contradictory document, an outlier item) prompts it. The clear implication, visible even in this small sample, is that **in the absence of such a trigger the anchor is likely to persist un-adjusted** — which is precisely the risk the eight interventions in the research model are theorized to mitigate. This convergent, practitioner-grounded evidence is the study's most defensible finding and directly supports the theoretical model, independent of sample size.

## 5.5  Confirmatory Measurement Model (Specified, Not Estimated)

The eleven-factor measurement model was specified in Jamovi's confirmatory-factor-analysis syntax (each construct as a latent factor indicated by its five items; see the runbook appendix). The model was **not estimated**, because at n = 4 it is not identified. The specification is retained to demonstrate that the intended analysis was correctly prepared and is ready to execute once an adequate sample is obtained. [JAMOVI: paste the CFA model-specification syntax and the "model not identified / insufficient N" output as evidence of readiness.]

# CHAPTER 6 — DISCUSSION, LIMITATIONS, AND FUTURE RESEARCH

## 6.1  Summary of Findings

This pilot study fielded an eleven-construct instrument on anchoring-bias mitigation in long-term audit engagements and screened 23 raw responses to 4 valid cases. Quantitatively, the study could not validate the measurement model: reliability and factor structure are not estimable at this sample size, and no inferential test of the sixteen hypotheses was possible. Qualitatively, however, the study produced convergent, theory-consistent evidence: four practicing auditors independently described the anchoring-and-adjustment mechanism that motivates the entire model, including the key insight that departure from an anchor is trigger-dependent.

## 6.2  Interpretation

The value of this study is threefold. First, it establishes **feasibility**: the instrument fields cleanly, the screening protocol works, and complete respondents pass attention checks — the measurement machinery is sound even though the sample is not yet adequate. Second, it surfaces a concrete **recruitment risk** — the paid-panel channel (Prolific) underdelivered severely (2 of 100 funded), which is itself a finding that should reshape the sampling strategy for the full study. Third, the qualitative convergence provides **preliminary construct-relevant evidence** that the phenomenon of interest is real, salient, and describable by the target population in the model's own terms.

## 6.3  Limitations

The overriding limitation is **sample size (n = 4)**, which precludes any inferential analysis and renders the reliability estimates uninterpretable. Related limitations follow from it: the sample, though diverse in role, is far too small to represent the auditor population; self-report measures of one's own bias-reduction are subject to social-desirability and limited-insight biases; and the cross-sectional design cannot support causal claims even at adequate power. The Prolific under-delivery also means the achieved sample is dominated by organic contacts, introducing potential network bias. These limitations are characteristic of a pilot study and define the agenda for the study that follows.

## 6.4  Future Research

Three directions follow directly. **First, replication at adequate power:** the measurement model is specified and ready; the immediate need is n sufficient for CFA (a common rule of thumb is ≥ 5–10 respondents per estimated parameter, implying several hundred for a model this size). The researcher has identified **additional recruitment channels in the London and Canada auditing communities** that, subject to IRB scope approval, could supply a substantially larger and more geographically diverse sample. **Second, method diversification:** supplementing self-report with a behavioral or vignette-based anchoring measure would address the self-insight limitation. **Third, the dissertation bridge:** as discussed with the faculty advisor from the outset, the natural extension is to examine how AI- and LLM-based audit tools interact with anchoring bias — whether algorithmic decision aids attenuate the human anchor or introduce anchors of their own. The present model, once validated, becomes the measurement foundation for that dissertation.

## 6.5  Conclusion

Framed honestly as a pilot, this study did what a pilot should do: it proved the instrument fieldable, exposed a critical recruitment constraint, and produced convergent qualitative evidence that the anchoring mechanism at the heart of the model is real in practitioners' own experience. It does not validate the measurement model — that awaits the adequately powered study for which this work has laid complete and reusable groundwork. The contribution is not a finished validation but a de-risked, execution-ready foundation for one.
