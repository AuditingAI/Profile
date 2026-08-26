---
name: airun
description: Run an AI research runbook — a portable, model-agnostic hunt for recruitment precedent, AI-and-audit empirical literature, or regulatory drift. Use when he says "run RB01", "run a runbook", asks to hunt for recruitment precedent, asks what the literature says about auditors and AI, asks what changed in the regulations, or wants the context pack for pasting into Perplexity, ChatGPT or another model. Also use when he asks how to point another AI at this research. Scholar lane. Captures and characterises sources; never synthesises.
---

# Run an AI runbook

The runbooks live in `dba/AI_RUNBOOKS/`. They are plain markdown so that any model can run them —
Perplexity first, but the design assumes the best tool changes. This skill runs one here, or prepares
it for pasting elsewhere.

## Step 0 — always

Read `dba/AI_RUNBOOKS/README.md` and `dba/AI_RUNBOOKS/SCHEMAS.md` before anything else. The schema is
the contract; a capture that does not match it cannot be absorbed downstream.

Check the date on `dba/AI_RUNBOOKS/CONTEXT_PACK.md`. **If it is more than a month old, say so and
offer to refresh it before running.** A stale pack is how a model gets told the wrong state of the
work and confidently produces something built on it.

## The three runbooks

| Ask | Runbook |
|---|---|
| Recruitment, sampling, "how do I reach auditors", Directive 5 | `perplexity/RB01_recruitment_precedent.md` |
| What the literature says on auditors and AI, the §7 gap | `perplexity/RB02_ai_audit_empirics.md` |
| NIST, SR 11-7, EU AI Act, PCAOB, "what changed" | `perplexity/RB03_regulatory_drift.md` |

## Running it here

1. Load the runbook. Work its queries **in order** with WebSearch/WebFetch.
2. Apply its gate. Most results die there — that is the gate working, not a thin search.
3. **Verify every URL resolves.** A dead link is a dropped row, never a softened one.
4. Capture to the runbook's schema. Every row starts `read_state: lead`.
5. Write `dba/AI_RUNBOOKS/RESULTS/YYYY-MM-DD_RBnn.md` — append-only, never overwrite.
6. Update the run log table in `RESULTS/README.md`.
7. Report: screened, captured, why the rest died, what landed, one next action.

## Preparing it for another model

He asks for this often — he works in Perplexity directly.

Output, ready to paste, in this order:
1. The whole of `CONTEXT_PACK.md`
2. The runbook's prompt block
3. Its query list

Tell him: **fresh thread, not a continuation.** Prior turns contaminate the context, and the pack is
written to be the first thing a model sees.

## Guardrails

- **Capture, do not interpret.** These runbooks produce rows. What the rows mean is his work — Dr.
  Rey's standing instruction, and not negotiable.
- **Report a quiet run as quiet.** "Nothing qualified" is a result. Padding a sweep is how a
  literature review drifts for a semester.
- **Surface contradicting findings first, never buried.** A review that only accumulates support is
  the failure mode a bias researcher can least afford.
- **Never move `read_state` to `read`.** Only he does that, after reading the paper in full.
- **Never claim the AI extension has findings.** It is argued, not tested.
- **RB03 forks.** Dissertation relevance stays in the Scholar lane; brand relevance goes to
  `career/HANDOFF.md` and nowhere else. Never draft industry material from it.
