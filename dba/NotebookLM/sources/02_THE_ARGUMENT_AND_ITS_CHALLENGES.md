# Source 2 — The dissertation argument, and every challenge to it

*The AI extension. This is the material to be able to **defend**, not merely recite.
Chain version 1.1, current as of 11 August 2026.*

---

## 1. The chain

```
AI tool enters recurring review work
        ↓  L1
system output becomes the anchor — automated, continuous,
arriving before the reviewer has formed a view
        ↓  L2
the model confirms the position the reviewer has already stated
rather than challenging it
        ↓  L3
successive models reprocess the same work; conclusions converge
on each other rather than on evidence
        ↓
recurring professional judgment degrades
while every individual model passes its own validation
```

That last line is the thesis. **The failure is invisible to model validation** because no single
model is malfunctioning. Each performs to specification. The degradation lives in the sequence
between the model and the human, and in the loop between models — neither of which any validation
plan currently inspects.

## 2. Why each link is claimed, and where each is weak

### L1 — system output becomes the anchor

**The claim.** When an AI tool produces a conclusion before the reviewer forms their own, that output
functions as an anchor. Unlike a prior-year figure, it is generated automatically, continuously, and
at scale.

**Support.** Anchoring-and-adjustment is among the most replicated findings in judgment research, and
the qualifying study's entire model rests on it.

**The strongest challenge.** Classic anchoring effects have taken replication damage in adjacent
literatures, and effect sizes in expert populations run smaller than in the undergraduate samples
that produced the canonical results.

**Status: defensible — but only if argued with expert-population evidence.** Citing undergraduate lab
studies to a committee of accounting academics is the weakest possible version of this argument.

### L2 — the model confirms rather than challenges

**The claim.** Language models tend to agree with a position the user has already stated instead of
contesting it. A reviewer who says "this looks reasonable" gets agreement, not challenge.

**Support.** Sycophancy is documented and named in the LLM literature; vendors publish on mitigating
it, which is itself evidence it exists.

**The strongest challenge.** Sycophancy is a moving target. Each model generation is explicitly
trained against it. **A claim true in 2026 may be false at a 2028 defense.**

**Status: time-sensitive, and must always carry a date.** The defensible framing is *mechanism, not
artifact*: sycophancy arises from optimising on human approval, and that optimisation pressure
persists across generations even as each generation is patched. Argue the pressure, not the symptom.

### L3 — models converge on each other

**The claim.** As successive models reprocess work that earlier models produced, conclusions converge
on one another rather than on the underlying evidence.

**Support.** Model-collapse and synthetic-data-contamination results. **And, since August 2026,
external support:** *How LLMs Audit Each Other: Five Mechanisms of Auditor Bias in Cross-Model Peer
Review Under Identity Disclosure and Cross-Lingual Conditions* (2026). Cross-model peer review **is**
this link, instrumented by someone else, with five named mechanisms.

**The strongest challenge.** Nearly all of that evidence concerns *training corpora* — models
degrading when trained on model output. The step from "models degrade on synthetic data" to
"auditors converge because the models they consult converge" is **an inference, not a finding.**

**Status: weakest link.** This is where a committee pushes. It is also the largest opportunity — see
§4.

### The whole chain

**Status: untested. Say so.** No data exists. Nothing in this argument is a finding.

## 3. Three standing challenges — carry these until answered

**1 · The improvement case.** A 2026 study found AI assistance *reduced* bias in a judgment task
(news summarisation, lay readers). Different domain, non-professional task — so not fatal. But an
argument that AI degrades professional judgment has to engage the case that it sometimes improves it.
If it doesn't, a committee member will raise it first, and the argument will look one-sided.

**2 · The moving-target problem.** See L2. Any claim about model behaviour needs a date attached and
a mechanism underneath it.

**3 · L3's inferential gap.** Model-to-model convergence is documented. Auditor-to-auditor
convergence *via* models is not.

## 4. Where the contribution actually is

The weakest link is also the most valuable one, because it is the one a well-designed study could
**measure**.

Nobody has shown that professionals reading model output converge on each other. That is an
empirical question with a tractable design: give reviewers the same case, vary whether they see model
output and whose output they see, and measure dispersion of conclusions.

**The dissertation's contribution is closing L3's gap, not restating the chain.** Restating it is
commentary. Measuring it is research.

## 5. Practice questions — try these before opening the sources

1. A committee member says: *"Anchoring has replication problems. Why should I believe your L1?"*
2. *"You're describing 2026 model behaviour. Your defense is in 2028. Why won't this be obsolete?"*
3. *"Model collapse is about training data. Your claim is about people. Where's the bridge?"*
4. *"There's evidence AI reduces bias. Why does your chain only run one direction?"*
5. *"If every model passes validation, why should a regulator care?"*
6. *"Which single link, if false, collapses the whole argument?"*
7. *"What would falsify your chain?"*

Question 7 is the one to be able to answer instantly. An argument with no falsification condition is
not a research argument.

## 6. Change log

- **v1.1 — 10 Aug 2026.** L3 upgraded from conjecture to weakest-link-with-external-support after the
  cross-model peer-review paper. Improvement-case challenge added. L2 reframed as mechanism.
- **v1.0 — Jul 2026.** Chain first stated in the qualifying manuscript. Praised as sound research
  judgment; no link individually defended.

**The chain is re-tested at every literature sweep.** A link that survives unchanged still gets its
date bumped, so "defensible" never quietly means "unexamined since last year."
