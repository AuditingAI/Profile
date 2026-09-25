# RB02 · The AI-and-audit empirical literature

**Tool: Perplexity** · fresh thread · paste `../CONTEXT_PACK.md` first · capture to Schema B in
`../SCHEMAS.md` · output to `../RESULTS/YYYY-MM-DD_RB02.md`

---

## The question

> **What has actually been measured about how auditors rely on AI-generated output — and has anyone
> done it qualitatively?**

## Why this one exists

`../../00_Execution/QUALITATIVE_REFRAME_L2_L3.md` §7 ends with an admission:

> *"None of the AI-and-audit sources above have been read in full. They are leads, found by search, to
> be pulled through the FIU library and read before any of them enters a proposal."*

That is the largest honesty gap in the repository. The gap is not that the claim is wrong — it is
that a literature position is being held on the strength of search snippets. This runbook closes it
by finding the literature properly; **reading it is Yasir's job and cannot be delegated.**

The stated gap in that file is specific and testable: *little qualitative empirical work on auditors'
lived experience of automation bias and skepticism in AI-assisted settings.* If that is wrong, the
qualitative arm's whole justification weakens, and it is far better to find that out now than at a
defence.

---

## The prompt to paste after the context pack

```
I need the EMPIRICAL literature on how auditors and accounting professionals rely on, trust, or
defer to AI, machine learning, or automated analytics output in professional judgment.

For each study I need:
  - design (survey / experiment / interview / archival / review / conceptual)
  - whether it is QUALITATIVE — flag this prominently
  - population and country
  - achieved n
  - what they actually measured, and with what scale (name, items, alpha if reported)
  - the finding in one sentence, in their words
  - whether it SUPPORTS, COMPLICATES, or CONTRADICTS the claim that professionals
    under-scrutinise AI output that agrees with a view they already hold

Rules:
  - Empirical work only at first pass. Mark conceptual and review papers separately.
  - Every study needs a resolving URL. Drop what you cannot link.
  - Report contradicting findings FIRST. I specifically want work suggesting AI assistance
    IMPROVES auditor judgment or skepticism.
  - If a query returns nothing that qualifies, say so plainly.

Return one row per study:
citation | url | access | design | qualitative | population | n | construct_touched |
link_touched | direction | finding | measure
```

---

## Queries — run in order

1. `auditors reliance artificial intelligence professional skepticism empirical study`
2. `automation bias auditors decision aid reliance experiment accounting`
3. `qualitative interview study auditors artificial intelligence experience judgment`
4. `algorithm aversion OR algorithmic appreciation professionals expert judgment`
5. `audit analytics adoption professional judgment survey scale measurement`
6. `LLM sycophancy user agreement confirmation empirical evaluation`
7. `decision aid reliance accounting judgment "prior year" anchoring experiment`
8. `AI assistance improves auditor judgment skepticism evidence`

**Query 3 is the one to watch.** If it returns substantial qualitative work on auditors' lived
experience of AI reliance, the stated gap is smaller than claimed and
`../../QUALITATIVE/PROTOCOL_phenomenology.md` needs revisiting. **Report that honestly and
immediately.** Discovering it now is cheap; discovering it at a proposal defence is not.

**Query 8 is deliberately adversarial.** It hunts for the opposite of what the chain predicts. Run it
even when the earlier queries have gone well — especially then.

---

## The gate

**Accept** empirical work — data collected from real professionals — on reliance, trust, deference,
skepticism, or judgment quality in AI- or analytics-assisted settings.

**Accept separately, marked as such:** systematic reviews and conceptual papers. They map the field
but they are not evidence, and mixing the two is how a review over-claims.

**Reject:** technical papers on audit-tool accuracy with no human judgment component · student
samples presented as professionals · vendor white papers · anything without a resolving link.

---

## What a good run produces

| Outcome | Meaning |
|---|---|
| **Qualitative studies of auditors and AI** | ⚠️ Changes the gap statement. Highest-priority read regardless of what they found |
| **Validated scales for reliance or skepticism** | Feeds `../../KNOWLEDGE/02_CONSTRUCTS.md` and could sharpen the instrument |
| **`direction: contradicts`** | 🔥 Surface first, always. This is the material that protects the argument |
| **Nothing but conceptual work** | Confirms the stated gap — say so plainly, and note it is now search-confirmed rather than assumed |

---

## Where it lands

- Rows → `../RESULTS/YYYY-MM-DD_RB02.md`
- Construct rows → `../../KNOWLEDGE/02_CONSTRUCTS.md`
- Anything qualitative → `../../QUALITATIVE/README.md`, and the gap statement in
  `../../00_Execution/QUALITATIVE_REFRAME_L2_L3.md` §7 is **rewritten**, not quietly amended
- Contradicting findings → the adversarial pass, `../../00_Execution/RESEARCH_AGENT_DESIGN.md` pass 5

**Every row lands as `read_state: lead`.** The §7 admission is only actually resolved when Yasir has
read the papers in full — not when this runbook has found them.
