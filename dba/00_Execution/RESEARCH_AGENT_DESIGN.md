# Research Agent Design — turning Scholar alerts into dissertation progress

**The problem with the current sweep.** `/research` triages Scholar alerts into five buckets and
reports what is interesting. Interesting is not the bar. The bar is: *does this paper change a
sentence in Chapter 2, an argument in Chapter 3, or the recruitment plan?* Most papers do not, and
the ones that do get lost among the ones that merely sound relevant.

**The fix.** Five specialised passes over each paper, each answering one question that maps onto a
directive Dr. Rey actually issued. A paper that fails every pass is filed and never mentioned again.

---

## Where this has to land

Dr. Rey's five directives (`Rey_Final_Feedback_Dissertation_Plan.md`) are the acceptance criteria:

1. Expand Chapter 2 theory beyond single paragraphs
2. Reorganise the review **construct by construct** — defined / measured / related
3. Terminology: "constructs" in Ch. 2, variable roles only after Ch. 3
4. Each of the 16 hypotheses argued from the Ch. 2 synthesis
5. **A comprehensive recruitment strategy built before the dissertation begins**

Directive 5 is sequenced first, because recruitment is what broke the qualifying study. The agent
design reflects that: the method-mining pass is not an afterthought, it is the one with a deadline.

---

## The five passes

### 1 · Relevance gate
*Does this touch the argument at all?*

Accept only if it bears on one of: anchoring and adjustment · dual-process theory · automation bias
or algorithmic appreciation · auditor judgment in recurring engagements · LLM sycophancy or
agreement bias · model-to-model convergence and epistemic drift · audit analytics adoption.

Everything else is rejected here with one line. Most alerts die at this gate — that is the point.

### 2 · Construct mapper
*Which of the eleven constructs does this define, measure, or relate?*

Returns a row for the construct-by-construct table Directive 2 requires:

| Construct | How this paper **defines** it | How it **measured** it (scale, items, α) | What it **related** it to (and direction) |

This pass is the one that mechanically builds Chapter 2. Every accepted paper produces at least one
row or it does not belong in the review.

### 3 · Method miner
*What can be stolen for the recruitment plan and the instrument?*

Extract: population definition · sampling frame and channel · achieved n · incentive and unit cost ·
response and screen-out rates · time in field · attrition · any reported difficulty reaching
professional samples.

This directly serves Directive 5. Studies that successfully recruited auditors or comparable
specialist professionals are the highest-value output of the entire sweep — higher than theory
papers — because the qualifying study proved the population is roughly six per hundred thousand on
a general panel. Anyone who has solved this is worth more than another citation.

### 4 · Hypothesis arguer
*Does this strengthen, weaken, or complicate one of the 16 hypotheses?*

Returns the hypothesis number, the direction of the effect on the argument, and a drafted two-to-three
sentence passage in Yasir's voice that could sit in Chapter 3 — with the citation attached.

Drafted, not final. Directive 4 asks for argument that emerges from synthesis; this pass supplies raw
material, and the synthesis stays his. Dr. Rey's course-closing note about Turnitin and the AI Writing
report applies squarely here: these drafts are input to his thinking, not a substitute for it.

### 5 · Adversary
*What in this paper undercuts the study?*

Explicitly hunts for: null or contradictory findings on the interventions · critiques of the
anchoring literature's replicability · evidence that AI assistance *improves* rather than degrades
judgment · measurement critiques of the scales in use.

Runs on every accepted paper. A literature review that only accumulates support is the failure mode
Directive 1 is pointed at, and it is the failure mode a bias researcher can least afford.

---

## How they compose

Gate first — it is cheap and kills most items. The remaining four run in parallel per surviving
paper, because none depends on another's output.

```
alerts → [1 gate] → survivors → [2 construct] ┐
                                 [3 method]   ├→ merge → append to reading list + brief
                                 [4 hypothesis]│
                                 [5 adversary] ┘
```

Output per accepted paper is a single block: construct rows, method figures, hypothesis drafts,
adversarial notes, full citation. That block is append-ready for the reading list — no reformatting
between the sweep and the writing.

---

## What the sweep should report

Not "here are seven interesting papers." Instead:

- **N screened, M accepted, and the reason the rest died** — proves the gate is doing work
- **New construct rows** added to the Chapter 2 table
- **Any recruitment precedent found** — flagged loudly, because this is the binding constraint
- **Hypotheses whose argument moved**, with the drafted passage
- **Anything adversarial**, always surfaced, never buried
- **One next action**

If a week's sweep produces no construct rows and no recruitment precedent, say so plainly. A quiet
week is information; dressing it up as progress is how a literature review drifts for a semester.

---

## Boundaries

- Simulated or practice data never enters the manuscript (`03_Data/PRACTICE_README.md`).
- Drafted passages are marked as drafts until Yasir has rewritten them. The scholarly voice is the
  contribution and it has to be his.
- Sources are verified before they enter the brief — a citation that does not resolve is worse than
  no citation.
