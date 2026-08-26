# RB01 · Recruitment precedent

**Tool: Perplexity** · fresh thread · paste `../CONTEXT_PACK.md` first · capture to Schema A in
`../SCHEMAS.md` · output to `../RESULTS/YYYY-MM-DD_RB01.md`

---

## The question

> **Who has successfully recruited auditors — or a comparably rare professional population — for
> empirical research, and exactly how did they do it?**

## Why this outranks everything else in the programme

Rey's Directive 5 requires a comprehensive recruitment strategy **before** the dissertation begins.
The qualifying study proved this population sits near **six per hundred thousand** on a general
research panel: ~20 eligible out of 334,976 members, 4 usable of 23 raw responses.

Recruitment is the binding constraint on the entire programme. **Anyone who has solved it is worth
more than another theory citation.** A theory paper improves a paragraph; a recruitment precedent
changes whether the dissertation can be run.

---

## The prompt to paste after the context pack

```
I need you to find empirical studies that successfully recruited hard-to-reach professional
populations — specifically auditors, internal auditors, risk and assurance professionals, or
comparable low-prevalence specialists (compliance officers, actuaries, clinical specialists,
forensic accountants).

For each study, I need the RECRUITMENT MECHANICS, not the findings:
  - exactly who they defined as eligible
  - the sampling frame and the channel used to reach them
  - target n, raw responses, and USABLE n
  - screen-out rate
  - incentive amount and form
  - cost per usable response if derivable
  - time in field
  - ANY verbatim sentence where the authors describe difficulty reaching this population

Rules:
  - Every study must have a resolving URL. Drop anything you cannot link.
  - I want mechanics, not conclusions. Do not summarise their findings.
  - If a query returns nothing that qualifies, say so plainly. Do not pad.
  - Prefer studies from 2015 onward, but a landmark methods paper of any age qualifies.

Return one row per study in a markdown table with these columns:
citation | url | access | population | specialist | frame | channel | n_target | n_raw |
n_achieved | screen_out_rate | incentive | unit_cost | time_in_field | difficulty_noted |
transferable
```

---

## Queries — run in order, stop when yield collapses

1. `empirical study recruiting external auditors survey sample size response rate methodology`
2. `"internal auditors" survey research "response rate" recruitment strategy professional association`
3. `hard-to-reach professional populations survey recruitment methods low prevalence screening`
4. `recruiting accounting professionals for academic research LinkedIn snowball sampling`
5. `Prolific OR MTurk OR CloudResearch specialist professional sample feasibility prevalence screening`
6. `qualitative interview study auditors sample size saturation recruitment`
7. `"Institute of Internal Auditors" OR "AICPA" membership survey research access academic`
8. `elite interviewing hard to access professionals recruitment gatekeepers methods`

**Queries 5 and 6 are the two that matter most.** Query 5 hunts for anyone who has documented the
panel prevalence problem — that is direct evidence for the P1 manuscript. Query 6 is the closest
precedent for the qualitative arm's own recruitment, which needs about thirty warm asks, not
two hundred and fifty.

---

## The gate

**Accept only if** the study reports at least three of: achieved n · sampling frame · channel ·
screen-out rate · incentive · time in field.

**Reject** — one line each, in the "why the N died" block:

- Findings-only papers with no methods detail
- Student or convenience samples described as professionals
- General-population studies
- Anything without a resolving link
- Methods textbooks with no empirical case

Most results die at this gate. That is the gate working.

---

## What a good run produces

| Outcome | Meaning |
|---|---|
| **1–3 strong precedents with full mechanics** | A very good run. Enough to build Directive 5 on |
| **Any verbatim admission of difficulty reaching the population** | 🔥 **Flag loudly.** Direct evidence for the P1 argument that this problem is general and under-reported |
| **A documented panel-prevalence check by someone else** | The highest-value find available. It means the contribution has a precedent to cite and build on |
| **Nothing** | Also useful — and itself evidence for P1. Report it as nothing, not as "limited results" |

---

## Where it lands

- Rows → `../RESULTS/YYYY-MM-DD_RB01.md`
- Anything transferable → `../../00_Execution/RECRUITMENT_PLAN_LinkedIn.md`, cited
- Anything on the qualitative arm's ~30-warm-ask funnel →
  `../../QUALITATIVE/SAMPLING_AND_RECRUITMENT.md` §4
- Difficulty quotes and any prevalence precedent → `../../P1_Feasibility_Note/MANUSCRIPT_DRAFT_v1.md`
- The generalised arithmetic → `../../RISK_QUANT/FEASIBILITY_MODEL.md`

**Every row lands as `read_state: lead`.** Nothing from this runbook enters a manuscript before the
paper is pulled through the FIU library and read in full.
