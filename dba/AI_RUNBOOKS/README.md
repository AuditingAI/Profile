# AI runbooks — portable, model-agnostic

**The problem this solves.** `CLAUDE.md` and `.claude/skills/` are read by Claude Code and nothing
else. Perplexity, ChatGPT, Gemini and NotebookLM cannot see them. Every time work moves to another
tool, the context is rebuilt by hand — badly, and differently each time.

**The fix.** Plain markdown, self-contained, at stable public URLs. Paste `CONTEXT_PACK.md` into any
model, add a runbook, get output in a schema this repository already knows how to absorb.

---

## The design principle

**The repository is the memory. The model is swappable.**

Models are commoditising fast. Prompt tricks tuned to one model age badly; a well-specified context,
a fixed capture schema and hard verification rules do not. So the durable assets live here in git —
versioned, dated, publicly addressable — and whichever model is best next year plugs into the same
sockets.

That has a second consequence worth naming. This pipeline refuses unsourced claims, requires
resolving URLs, and runs an adversarial pass on its own output. **That discipline is the subject of
the research programme** — an AI research workflow built against sycophancy and drift is a working
demonstration of the L2/L3 argument, and it is teachable as one.

---

## Which model for which job

| Job | Tool | Why |
|---|---|---|
| **Find current outside literature, with citations** | **Perplexity** | Live search, sources attached to claims, and it will say when it found nothing. This is what the runbooks here are for |
| Interrogate documents I already have | **NotebookLM** | Grounded in uploaded sources only; cannot invent a citation. See `../NotebookLM/README.md` |
| Draft, restructure, argue against me | Claude / ChatGPT | Long context, adversarial framing. **Never for synthesis that must be mine** |
| Adversarial pass on accepted papers | **Claude** | `../00_Execution/RESEARCH_AGENT_DESIGN.md` pass 5. Falsification needs reasoning over a corpus, not search |
| Statistics | jamovi, `../03_Data/*.py` | Not a language model's job |

**Perplexity is a search tool, not a thinker.** It is used here to find and characterise sources.
Every runbook stops at capture. Nothing in this directory asks a model to decide what the literature
means.

---

## How to run one

1. Open a **fresh** thread. Not a continuation — prior turns contaminate the context.
2. Paste **`CONTEXT_PACK.md`** whole.
3. Paste the runbook.
4. Work the queries in order. Capture into the schema in `SCHEMAS.md`.
5. Save output to `RESULTS/YYYY-MM-DD_RBnn.md`. **Append-only — never overwrite a prior capture.**
6. Verify before anything propagates: **every URL must resolve.** A citation that does not resolve is
   dropped, not softened.

Or run it here: `/airun RB01`.

---

## The runbooks

| ID | Hunts for | Serves |
|---|---|---|
| **RB01** | Recruitment precedent — studies that reached auditors or comparable specialist populations | Rey's Directive 5. The binding constraint on the whole programme |
| **RB02** | The AI-and-audit empirical literature currently marked *"none read in full"* | The largest honesty gap in the repo |
| **RB03** | Regulatory and standards drift — NIST AI RMF, SR 11-7, EU AI Act, PCAOB/AICPA | The dissertation's practice section **and** the consulting brand, from one sweep |

**Not here: the adversarial pass.** Hunting evidence that AI assistance *improves* auditor judgment,
and replication failures in the anchoring literature, requires reasoning across a corpus rather than
retrieval. That stays with Claude — `../00_Execution/RESEARCH_AGENT_DESIGN.md` pass 5.

---

## ⚠️ The rule that overrides everything here

**FIU University Graduate School policy §9: never upload confidential, sensitive, identifiable,
proprietary or restricted data to a public AI platform.**

For this programme that means, without exception: **no interview recording, no transcript, no
participant identifier, no linking key and no un-de-identified survey response ever goes into
Perplexity, ChatGPT, NotebookLM, Claude, or anything else.** The runbooks here search *published
literature*. They never touch study data, and no future runbook may.

Every use of these runbooks is disclosable under §3.1 and must be named in the preliminary pages of
any proposal or dissertation drawing on their output. Record:
`../00_Execution/FIU_AI_POLICY_2026.md`.

## Rules every runbook inherits

1. **Nothing is asserted without a resolving source.** A dead URL is a dropped row.
2. **A quiet run is reported as quiet.** "Found nothing that qualifies" is a result. Padding a sweep
   is how a literature review drifts for a semester.
3. **Capture, do not interpret.** Runbooks produce rows. What the rows mean is Yasir's work, and
   Dr. Rey's instruction on that is not negotiable.
4. **Nothing in `RESULTS/` enters a chapter until it has been read in full.** A captured abstract is a
   lead. Leads are not citations.
5. **Overstatement is the failure mode this programme studies.** Any model output claiming the AI
   extension has findings, or that the chain is established, is a red flag about the context — go back
   to step 1 and check the pack was pasted whole.

---

## Keeping it current

`CONTEXT_PACK.md` carries a date and a state block. **It goes stale silently** — the same failure
already documented for NotebookLM in `../NotebookLM/README.md`, where a pack sat unchanged from
24 July while the exam result, five directives and a drafted manuscript all landed.

Update the pack whenever: publication status changes · the qualitative arm moves · a directive is
satisfied · the recruitment count changes.
