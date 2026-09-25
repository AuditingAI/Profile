# The eleven constructs — defined / measured / related

**This is Dr. Rey's Directive 2 table.** The literature review is to be reorganised construct by
construct: how each is *defined*, how it has been *measured*, and what it has been *related to*.

Currently the `defined` and `measured` columns are populated from this programme's own instrument.
The `related` column is largely empty — that is the honest state, and it is what
`../AI_RUNBOOKS/perplexity/RB02_ai_audit_empirics.md` feeds. Every accepted paper from that runbook
produces at least one row here or it does not belong in the review.

**Terminology, per Directive 3:** these are **constructs** in Chapter 2. Variable roles —
independent, mediator, outcome — are used only from Chapter 3 onward, after the model is specified.
The role column below is for navigation, not for chapter prose.

**Instrument:** five Likert items per construct, one reverse-coded. 55 substantive items, plus five
eligibility screens and two attention checks. Source: `../Dissertation_Instrument_v3_DRAFT.md` and
`../STUDY_OVERVIEW.md` §2.

---

## The eight interventions

| # | Construct | Defined as | Measured by (this programme) | Related to — from the literature |
|---|---|---|---|---|
| 1 | **Training & Awareness** (TA) | Firm training on cognitive biases and concrete de-anchoring techniques | 5 items. Anchor: *"My firm provides specific training on cognitive biases (such as anchoring) that can affect audit judgments."* | `[EMPTY]` — needs debiasing-training literature. Known weak spot: awareness training rarely changes judgment |
| 2 | **Rotation of Auditors** (RA) | Personnel rotation bringing a fresh look to recurring engagements | 5 items. Anchor: *"Rotation in my firm is frequent enough to bring a 'fresh look' to recurring clients."* | `[EMPTY]` — substantial partner-rotation literature exists in auditing. **Highest-yield gap on this page** |
| 3 | **Use of Analytical Tools** (AT) | Data analytics generating independent, current-period expectations | 5 items. Anchor: *"I routinely use data-analytics tools that flag anomalies in client data."* | `[EMPTY]` — audit analytics adoption literature. ⚠️ **This construct is where L1 enters the existing model** |
| 4 | **Structured Auditing Processes** (SAP) | Standardised procedures forcing evidence-before-anchor evaluation | 5 items. Anchor: *"Procedures require me to evaluate current evidence before consulting the prior-year conclusion."* | `[EMPTY]` — decision-aid and structured-audit-approach literature |
| 5 | **Feedback & Reflection** (FR) | Debriefs and judgment-quality feedback loops | 5 items. Anchor: *"Post-engagement debriefs prompt me to reflect on judgment errors."* | `[EMPTY]` — feedback and expertise literature |
| 6 | **Independent Reviews** (IR) | Substantive re-examination by uninvolved reviewers | 5 items. Anchor: *"Reviewers challenge whether my judgments rely too heavily on prior-year audit conclusions."* | `[EMPTY]` — review-process and accountability literature |
| 7 | **Regulatory & Professional Guidance** (RPG) | PCAOB/AICPA/IIA/COSO standards shaping judgment discipline | 5 items. Anchor: *"The possibility of inspection encourages me to double-check the support behind my judgments."* | `[EMPTY]` — inspection-effects literature. Also fed by `RB03` |
| 8 | **Performance Metrics & Incentives** (PMI) | Evaluation systems rewarding judgment quality over speed | 5 items. Anchor: *"My performance evaluation rewards judgment quality, not only efficiency."* | `[EMPTY]` — incentives and audit quality literature |

## The two mediators and the outcome

| # | Construct | Role | Defined as | Measured by | Related to |
|---|---|---|---|---|---|
| 9 | **Auditor Judgment Quality** (AJQ) | Cognitive mediator | Careful, objective evaluation of independent evidence | 5 items | `[EMPTY]` — professional skepticism scales are the obvious neighbours and **may already supply a validated instrument.** Priority for `RB02` |
| 10 | **Audit Process Rigor** (APR) | Procedural mediator | Thorough, consistent, disciplined execution of the audit process | 5 items | `[EMPTY]` |
| 11 | **Reduction in Anchoring Bias** (RAB) | Outcome | Final judgments driven by current evidence rather than initial reference points | 5 items | `[EMPTY]` — ⚠️ see the measurement problem below |

---

## The sixteen hypotheses, in two sentences

**Eight direct paths** (H1, H3, H5, H7, H9, H11, H13, H15) — each intervention reduces anchoring bias
directly. **Eight mediated paths** (even numbers) — the six judgment-oriented interventions operate
through **AJQ**, the cognitive pathway; the two structural interventions (RA, SAP) operate through
**APR**, the procedural pathway.

**Status: fully argued in Chapter 3, none tested.** Not testable at the achieved sample of four.

---

## The measurement problem nobody has solved

**RAB is self-reported.** Construct 11 asks auditors to report the extent to which their own
judgments were driven by current evidence rather than by a reference point.

Anchoring is, by definition, a bias people do not notice themselves exhibiting. **An instrument that
asks people to self-report the degree to which they were anchored is asking them to report on
precisely the thing the bias prevents them from observing.**

This is stated in `../STUDY_OVERVIEW.md` §7 as a limitation *"pending the method-diversified
follow-up."* It is more than a limitation — it is the strongest available criticism of the
quantitative arm, and any committee member who works on bias will raise it.

**Two responses, and only the second is any good:**

1. The instrument measures perceived judgment discipline, not anchoring magnitude — a defensible
   retreat, but a smaller claim than the model advertises.
2. **The construct needs a behavioural or experimental measure** — a vignette with a manipulated
   anchor, where the adjustment is observed rather than reported. That is a different study, and it
   is the strongest case for the "method-diversified follow-up" the manuscript already promises.

*Also worth noticing: this problem is why the qualitative arm asks what auditors **describe and
account for**, not how much they were anchored. Phenomenology does not need people to be accurate
about their own cognition — only to report their experience.*

---

## The widening, and what it does to these constructs

The population was widened from *US auditors* to *auditors and risk governance professionals*.
`../STUDY_OVERVIEW.md` §8 gives the argument: **none of the eleven constructs is audit-licence
specific.** Every one describes judgment discipline under recurring evidence, which operates
identically for a model validator, a credit reviewer, or a compliance tester.

**The construct logic survives the widening. The item wording does not.** Items referring to
"engagements," "clients," "workpapers" and "the prior-year audit conclusion" read as audit-specific
and would need generic equivalents. `[OPEN]` — not yet done, and it is a prerequisite for any future
fielding.

---

## How rows get filled

Every accepted paper from `RB02` produces at least one row in the `related` column, carrying:
how that paper **defines** the construct · how it **measured** it (scale name, item count, α) · what
it **related** it to, and in which direction.

**A paper that cannot produce such a row does not belong in the literature review** — that is the
whole point of Directive 2 and of `../00_Execution/RESEARCH_AGENT_DESIGN.md` pass 2.
