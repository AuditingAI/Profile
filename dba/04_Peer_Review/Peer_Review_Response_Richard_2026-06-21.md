---
TITLE: Formal Response to Peer Review — Survey Instrument
AUTHOR: Yasir A. Malik (PID 1687105) — FIU DBA Cohort 7.16
COURSE: GEB7913 — Instructor: Prof. Dr. Juan Rey
DATE: Sunday, June 21, 2026
---

# Formal Response to Peer Review — Survey Instrument

**Reviewer:** Richard (audit-experienced peer reviewer)
**Instrument:** Full Survey Questionnaire — Anchoring Bias in Long-Term Auditor Engagements (IRB-25-0462)
**From:** Yasir A. Malik | **Date:** June 21, 2026
**Companion files:** `Richard_Original_Feedback_2026-06-21.md` (verbatim) · `Full_Survey_Questionnaire_v2.md` (revised instrument) · `Qualtrics_Survey_Import.txt` (v2 build)

---

## 1. Summary

Thank you, Richard — this is exactly the kind of review that improves an instrument before it reaches respondents. I worked through every comment and grouped them into three classes:

- **Accepted (11 changes):** wording and coverage improvements applied directly to v2.
- **Reasoned decisions (4 items):** comments I am not adopting verbatim, each with a methodological or theoretical rationale, because the change would either reduce validity or restructure the model.
- **Strengthened by your point (2 items):** places where your question surfaced a hidden assumption, which I addressed by adding a control item rather than changing a construct item.

**Net effect on the design:** the eleven constructs and their five-items-each structure are unchanged (so the exploratory factor analysis plan is preserved). All changes are wording, coverage, or added *controls* — none alters what a construct measures. Two control/demographic items were added. The instrument moves from 71 to 73 respondent-facing items.

**One decision flagged for you and Dr. Rey:** the 5-point vs 7-point scale (Section 3.1). I recommend keeping 5-point and explain why; it is reversible before launch.

---

## 2. Disposition table (every comment)

| # | Item | Your comment | Disposition | What changed in v2 |
|---|---|---|---|---|
| G1 | Response scale | Consider 7-point Likert | **Reasoned decision — keep 5-point** | Unchanged; rationale §3.1 |
| 1 | TA_5 | Offered cleaner alternative | **Accepted** | "I can recognize when an initial reference point is influencing my professional judgment." |
| 2 | RA_5 | Add "requirements" / "auditees" | **Accepted** | "Rotation policies or requirements in my firm meaningfully reduce over-familiarity with clients or auditees." |
| 3 | AT_3 | Add "(multiple sources of evidence)" | **Accepted** | "…draw on data beyond the client's own ledgers (i.e., multiple sources of evidence)." |
| 4 | AT (access) | Does everyone get the prior file? | **Strengthened — added control** | New context item C1 on prior-file access (§4) |
| 5 | SAP_5 | Insert "audit methodology" | **Accepted** | "The structure of my firm's audit methodology reduces reliance on mental shortcuts." |
| 6 | IR_1 | Define "qualified auditor" | **Accepted** | "…reviewed by a senior or equally qualified auditor who was not involved in forming the original judgment." |
| 7 | IR_3 | Don't tie to "prior-year figure"; reword | **Accepted (your wording)** | "Reviewers challenge whether my judgments rely too heavily on prior-year audit conclusions." |
| 8 | RPG (split) | Should regulatory vs professional be separate constructs? | **Reasoned decision — keep combined; EFA tests it** | Unchanged; rationale §3.2 |
| 9 | RPG_1 | Add IIA, COSO | **Accepted** | "Regulatory and professional standards (e.g., PCAOB, AICPA, IIA, COSO) meaningfully shape how I exercise judgment." |
| 10 | RPG_2 | Reword around inspection | **Accepted** | "The possibility of inspection encourages me to double-check the support and analysis behind my judgments." |
| 11 | PMI_3 | "skepticism (or judgment?)" | **Reasoned decision — keep "professional skepticism"** | Unchanged; rationale §3.3 |
| 12 | PMI_4 (R) | Budget pressure may contaminate | **Accepted — de-contaminated** | "My firm's incentive and evaluation system discourages spending the extra time needed to challenge prior-year balances." |
| 13 | APR (charge) | Depends on auditor-in-charge | **Strengthened — see §3.4** | Captured by reworded APR_5 |
| 14 | APR_5 | Potential repeat; replace | **Accepted (your wording)** | "Critical audit procedures are consistently followed across all my engagements." |
| 15 | D1 | Split external vs internal years | **Accepted** | Two items: D1a external years, D1b internal years |

---

## 3. Reasoned decisions (the four I did not adopt verbatim)

### 3.1 — 5-point vs 7-point Likert: keeping 5-point

This is the most consequential question you raised, so it gets the fullest answer.

The measurement literature is clear that the **reliability and validity gains from adding scale points rise only up to about five-to-seven categories and then plateau.** Preston and Colman (2000), testing scales from 2 to 11 points, found that indices of reliability, validity, and discriminating power were poor for 2–4 points, rose through about 7, and that **internal consistency did not differ significantly among the usable scales** — i.e., a 5-point scale is already in the reliable range. Dawes (2008), comparing 5-, 7-, and 10-point versions of the same items experimentally, found the resulting data characteristics **comparable across formats** after rescaling.

Given that, I am keeping 5-point for four practical reasons specific to *this* study:

1. **Respondent burden.** The instrument carries **55 construct items** plus screeners and demographics. Across that many items, a 5-point scale is materially faster and less fatiguing than 7-point, and fatigue is itself a validity threat (it degrades the later blocks, which — because of block randomization — are different constructs for different respondents).
2. **Mobile delivery.** A large share of CloudResearch responses come on phones. A 5-point row renders cleanly on a narrow screen; 7-point rows crowd and increase mis-taps.
3. **Midpoint preserved.** Both 5- and 7-point retain a neutral midpoint, so we lose none of the "neither agree nor disagree" information that a forced-choice even scale would drop.
4. **Negligible psychometric cost.** Per Preston & Colman and Dawes, the factor structure and reliability we need for the EFA are not meaningfully improved by going to 7.

**This is reversible before launch.** If you or Dr. Rey prefer 7-point, the change is ~30 minutes (rebuild the Qualtrics matrices + regenerate the import file and codebook). My recommendation is 5-point; I have flagged it for Dr. Rey in the one-page update.

*Verified sources:* Preston, C. C., & Colman, A. M. (2000), *Acta Psychologica, 104*(1), 1–15; Dawes, J. (2008), *International Journal of Market Research, 50*(1), 61–104.

### 3.2 — Should Regulatory and Professional Guidance (RPG) be two constructs?

Good theoretical question. I am keeping RPG as **one** construct for now, for three reasons, but I am treating its dimensionality as an **empirical** question the analysis will answer rather than something I assert.

1. **Mechanism.** Both regulatory standards (PCAOB inspection risk) and professional requirements (skepticism standards, IIA/COSO) operate through the *same* dual-process lever in this study's theory: they raise accountability, which motivates System-2 reconsideration that can override the anchor (Kennedy, 1993; Nelson, 2009). They are theorized as one external-pressure pathway, not two.
2. **Model parsimony and the hypothesis set.** Splitting RPG into two constructs would change the model from 8 interventions to 9, and the hypothesis count from 16 to 18, with all the downstream EFA and mediation consequences. That is a substantive structural change that should not be made on a wording review alone.
3. **EFA is the right arbiter.** The exploratory factor analysis will tell us empirically whether the five RPG items load on one factor or split into two. **If they split, that is a finding** — I will report it and, with Dr. Rey's sign-off, revise the model for the next stage. So your instinct is not dismissed; it becomes a pre-registered thing to watch in the factor solution.

To make the construct fairer to internal auditors in the meantime, I broadened RPG_1 to name IIA and COSO (change #9).

### 3.3 — PMI_3: "professional skepticism" vs "judgment"

Keeping **"professional skepticism."** The two are deliberately different things in this design: *professional skepticism* is the established, separately-theorized auditor disposition (Nelson, 2009; Hurtt, Brown-Liburd, Earley, & Krishnamoorthy, 2013), whereas *judgment quality* is its own construct in the model — the AJQ mediator (A.9). If I swapped "skepticism" for "judgment" in the incentives block, PMI_3 would start to overlap the AJQ mediator and blur the discriminant validity the EFA is supposed to demonstrate. Keeping the terms distinct is what lets the factor analysis separate "are auditors *rewarded* for skepticism" (PMI) from "is their *judgment* actually high-quality" (AJQ).

### 3.4 — APR "depends on the auditor-in-charge"

You are right that process rigor varies with who runs the engagement — and that is precisely the *between-respondent variance the construct is meant to capture.* If rigor were identical everywhere, APR could not discriminate and would be useless in the factor model. So rather than treat the dependence-on-the-charge as a problem, the construct measures it. I did adopt your specific fix to APR_5 (change #14), replacing the awkward "does not depend on any single individual" (which you flagged as a potential repeat of APR_1/APR_3) with **"Critical audit procedures are consistently followed across all my engagements."** That item now cleanly captures cross-engagement consistency without the redundancy.

---

## 4. Where your question added a control item (rather than changing a construct)

**Prior-file access (your AT question).** You asked whether every auditor actually has access to the prior-year file and whether the manager shares it. This matters because the entire anchoring premise assumes the auditor is *exposed* to the prior-year reference point in the first place. Rather than bend an AT construct item to ask about access (which would muddy what AT measures), I added a single **context/control item**:

> **C1.** On my engagements, prior-year workpapers and conclusions are typically accessible to the audit team.
> *(Strongly disagree → Strongly agree)*

This lets the analysis check whether anchoring effects differ between auditors with high vs low exposure to the prior-year anchor — turning your question into a testable control instead of a confound.

**Split audit experience (your demographics point).** Adopted. v2 separates **D1a — years of external audit experience** and **D1b — years of internal audit experience**, with a note acknowledging that internal auditors frequently have prior external experience. This also improves the role control, because "years of experience" alone hid that dual background.

---

## 4b. Follow-up comments (reviewer chat, June 21) — all accommodated

| # | Comment | Disposition | What changed in v2.1 |
|---|---|---|---|
| 16 | "Add the definition of anchoring bias." | **Accepted** | Neutral, display-only definition added to an orientation screen after consent. Placed as general orientation and kept non-leading to limit priming of specific item responses. |
| 17 | "Access to previous audit files could vary audit by audit — a control variable should be pursued." | **Accepted — strengthened** | The C1 control was converted from an agree/disagree item to a **frequency scale** (every / most / half / some / rarely-or-never), capturing engagement-by-engagement variation. Remains a control, excluded from the EFA. |
| 18 | "Add firm size — Big 4 / mid-tier / small." | **Accepted** | New demographic D3b (Big 4 / Mid-tier / Small / Sole practitioner), separate from organization type. |

*A note on the anchoring definition and priming:* defining the bias up front carries a small risk of nudging socially-desirable answers. I judged the benefit (shared understanding, cleaner comprehension) to outweigh it here because (a) the instrument is a transparent self-report validation study, not a deception experiment, and (b) several items already reference prior-year figures and reference points, so the construct is not concealed. The definition is worded neutrally and not linked to any specific item.

---

## 5. What this means for the model and the timeline

- **Constructs:** unchanged (11). **Items per construct:** unchanged (5). **Hypotheses:** unchanged (16). → The EFA and mediation plan are intact.
- **Wording changes:** 8 construct items reworded for clarity/coverage; 0 construct items added or removed.
- **Controls added:** prior-file access (C1) + split experience (D1a/D1b). Respondent-facing items: 71 → 73.
- **Scope check:** every accepted change is wording, coverage, or a control. **None changes what a construct measures**, so none triggers an IRB substantive-amendment review. The reconciliation against the IRB-approved instrument (Monday) will confirm this item-by-item; if any delta is judged substantive, it halts and escalates to Dr. Rey + IRB before fielding.
- **Timeline:** the changes are folded into the v2 instrument and the Qualtrics import file today, so the survey can field on Dr. Rey's schedule without slippage.

Thank you again — six of these (IR_3, RPG_1, PMI_4, APR_5, the split experience, and the prior-file control) are genuine validity improvements I would not have caught from the inside.

— Yasir
