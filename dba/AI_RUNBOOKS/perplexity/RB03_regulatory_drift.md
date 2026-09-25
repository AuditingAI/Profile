# RB03 · Regulatory and standards drift

**Tool: Perplexity** · fresh thread · paste `../CONTEXT_PACK.md` first · capture to Schema C in
`../SCHEMAS.md` · output to `../RESULTS/YYYY-MM-DD_RB03.md`

**Cadence: monthly.** More often is noise; this material moves in quarters, not days.

---

## The question

> **What changed in the rules governing AI in regulated financial institutions, and does any of it
> bear on human oversight of model output?**

## Why this one exists

Two audiences, one sweep:

1. **The dissertation.** The practice contribution rests on a claim that regulators increasingly
   require *meaningful* human oversight of model output. If that requirement tightens — or is
   softened — the practical stakes of the L1/L2 argument change with it.
2. **The consulting brand.** `Audit the Algorithm` sells governance work aligned to NIST AI RMF,
   SR 11-7 and the EU AI Act. Stale framework knowledge is a credibility risk in front of a client.

⚠️ **The two outputs never appear in the same document.** That is the standing separation in
`../../../CLAUDE.md` — academic and industry materials do not share a page. This runbook captures
once and the rows fork: `dissertation_relevance` stays in the Scholar lane; `brand_relevance` goes to
the Industry agent via `../../../career/HANDOFF.md`. **This runbook never drafts industry material.**

---

## The prompt to paste after the context pack

```
I need changes over the last 6 months to the rules and standards governing artificial
intelligence and model risk in regulated financial institutions.

Cover: NIST AI Risk Management Framework, Federal Reserve/OCC SR 11-7 model risk guidance,
EU AI Act implementation and its timetable, PCAOB standards and inspection focus, AICPA
guidance, IIA guidance, COSO, and any US state-level AI legislation touching financial
services.

For each item I need:
  - the instrument and issuing body
  - jurisdiction
  - status (in force / proposed / consultation / withdrawn)
  - effective date, or "not set"
  - what actually changed, in one sentence
  - whether it bears on HUMAN OVERSIGHT of model output specifically, as opposed to
    model performance, documentation, or bias testing

Rules:
  - Primary sources only. Link the regulator, the register, or the standard-setter — not a
    law-firm summary or a vendor blog.
  - Every item needs a resolving URL.
  - Distinguish clearly between what is IN FORCE and what is PROPOSED. Conflating the two is
    the most common error in this area and the most damaging.
  - If nothing changed in a category, say so. A quiet quarter is a real answer.

Return one row per item:
instrument | jurisdiction | status | effective_date | change | bears_on | url
```

---

## Queries — run in order

1. `NIST AI Risk Management Framework update profile generative AI 2026`
2. `EU AI Act implementation timeline high-risk obligations financial services 2026`
3. `SR 11-7 model risk management guidance artificial intelligence supervisory update`
4. `PCAOB standards technology-assisted analysis inspection focus auditor use of AI`
5. `AICPA OR "Institute of Internal Auditors" guidance artificial intelligence audit 2026`
6. `financial regulator guidance human oversight automated decision model output`
7. `state artificial intelligence legislation financial services enacted 2026`

**Query 6 is the one that matters for the dissertation.** Everything else is context; a regulator
writing down what "meaningful human oversight" actually requires is directly load-bearing for the
practice contribution.

---

## The gate

**Accept:** primary-source items from a regulator, standard-setter or official register, with a
resolving link, dated in the last six months.

**Reject:** law-firm client alerts · vendor content marketing · press coverage without a primary link
· anything undated · commentary presented as guidance.

**The distinction that must not blur:** `in force` versus `proposed`. A proposed rule described as
current is the kind of error that ends a consulting engagement and embarrasses a dissertation.

---

## What a good run produces

| Outcome | Meaning |
|---|---|
| **Anything specifying what human oversight of model output requires** | 🔥 Directly load-bearing. Read in full |
| **A change to SR 11-7's treatment of AI** | Core to the model-risk framing throughout the programme |
| **EU AI Act timetable movement** | Brand-relevant; dissertation-relevant only if it touches oversight |
| **Nothing changed** | Report it. Monthly sweeps mostly return quiet, and quiet is the correct answer most months |

---

## Where it lands

- Rows → `../RESULTS/YYYY-MM-DD_RB03.md`
- `dissertation_relevance` → the practice section of the manuscript, and
  `../../KNOWLEDGE/01_THEORY.md` where it bears on the oversight argument
- `brand_relevance` → **a `HANDOFF.md` entry only.** Scholar does not write industry material

**Every row lands as `read_state: lead`.** A regulatory summary is a pointer to a primary document.
Nothing is asserted about what a rule requires until the rule itself has been read.
