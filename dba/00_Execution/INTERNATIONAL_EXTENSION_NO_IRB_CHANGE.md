# Extending the question internationally — and why it needs no IRB change

**3 September 2026.** Scholar lane. Written after the Newburry call and the Harzing paper.

---

## The answer in one line

**The international extension needs no change to IRB-25-0462, because the data it collects is not
data about people.** It is a research panel's own aggregate audience-count screen, read before any
study is fielded. There are no participants, no interaction, no identifiable private information —
and therefore no human subjects.

**Precedent already set, in work Dr. Rey passed.** The figure *"20 eligible of 334,976"* is cited in
Chapter 5.3 of the qualifying manuscript **as aggregate platform data**. The same treatment,
repeated across countries, is the international study.

---

## The line — what sits inside human-subjects research and what does not

| Activity | Human subjects? | IRB position |
|---|---|---|
| Reading a panel's audience-configuration screen: *"N eligible of M members"* for a set of criteria | **No.** Aggregate counts, no interaction, no individual data | **No change needed.** Already precedented in Ch. 5.3 |
| Recording the platform's own published response-rate and completion statistics | **No.** Vendor documentation | No change needed |
| Extracting response rates from published studies — e.g. Harzing et al.'s country table | **No.** Published literature | No change needed |
| Fielding the 55-item instrument to **US auditors** | Yes | **Already approved** under IRB-25-0462 |
| Fielding it to auditors **outside the US** | Yes | ⛔ **Major amendment.** New population, international sites |
| Fielding it to a **broadened** risk-and-assurance population | Yes | ⛔ Amendment — already an open item |
| **Interviewing** anyone, anywhere | Yes | ⛔ Modification or new protocol — unsubmitted |

**The extension lives entirely in the top three rows.** That is not a loophole; it is what the study
actually is. The research question is about *whether a population can be reached*, and the evidence
for that is a property of the sampling frame, not of the people in it.

⚠️ **`[VERIFY]` — confirm, do not assume.** The reasoning above is sound and it is precedented in
your own passed manuscript, but the determination is the IRB's to make, not yours or mine. **Put it
to the FIU IRB office in one line**, alongside the interview-arm question already waiting:

> *"Does reading a commercial research panel's aggregate eligibility counts — no interaction with
> participants, no individual-level data — require any modification to IRB-25-0462, or does it fall
> outside human-subjects research?"*

A written "no modification required" is worth having on file before it appears in a paper.

---

## How the original question extends without being rewritten

**The original question stays exactly as it is.** Nothing is bolted onto it.

| | |
|---|---|
| **Original** | Which organisational interventions reduce anchoring bias in long-term audit engagements? *(Variance model, US auditors, survey.)* |
| **What was learned** | The population is ~6 per 100,000. The design could not be executed |
| **The extension** | Under what conditions is a study of a rare professional population feasible **across national frames**? |

The extension does not modify the original question. **It asks a prior question that the original
one ran into** — and that is a cleaner relationship than an amendment, because the original study
becomes the worked case rather than something needing revision.

---

## The model, now that Harzing supplies the second parameter

Reachable respondents in country *c*:

> **n_c ≈ frame_c × prevalence_c × eligibility_c × response_c**

| Parameter | Source | Status |
|---|---|---|
| `frame_c` | Panel's stated member count in that country | Readable, per panel |
| `prevalence_c` | The panel's own eligibility screen | **Readable. This is the contribution** |
| `eligibility_c` | Screen-out rate | From his own study: 23 raw → 4 |
| `response_c` | **Harzing et al. (2012), Illustration 7** — 4.0% China to 15.4% Spain, 9.6% overall | **Newburry handed this over** |

A comparative design needs **every** frame to clear the threshold simultaneously, so the joint
feasibility is the **product**, not the average. That is the whole argument, and it is arithmetic
rather than assertion.

`../RISK_QUANT/feasibility.py` already computes the single-country case.

---

## The connection to Dr. Rey — "we need the data"

**Directive 5, verbatim:** *"Implementing a comprehensive participant recruitment strategy before
beginning the dissertation."* His words on the qualifying study's failure: the Chapter 6
recommendations were *"an adequate starting point"* and now have to become an operational plan.

**This is that plan, with numbers instead of intentions.** A prevalence map across countries and
panels *is* the recruitment strategy — it says which populations are reachable, at what cost, and
where the design has to change instrument. That is the difference between "I will recruit harder"
and "here is what the frame contains."

**And it produces data he can be shown, without waiting for anyone's approval.** That matters,
because every other route to data is currently blocked:

| Route | Blocked by |
|---|---|
| Survey relaunch | IRB amendment not submitted · relaunch decision never put to him |
| Interviews (L2) | IRB unsubmitted; modification-or-new-protocol question unanswered |
| **Panel prevalence data** | **Nothing.** Readable this week |

**The panel screens are the only dataset currently reachable, and they answer his fifth directive
directly.** Worth saying to him in exactly those terms.

---

## What to put to Dr. Rey — one message, three things

He has three open items and none has been put to him. They belong together:

1. **"Does the survey arm relaunch?"** — closes or activates two IRB amendments and decides the
   Prolific refund-versus-credit question.
2. **"Will you review and approve the AI use?"** — FIU UGS §3.2 requires committee approval. Never
   requested.
3. **"Here is the data route that is not blocked."** — the cross-national prevalence map, framed as
   Directive 5 delivered rather than as a new idea.

Item 3 is what makes the message worth sending rather than a list of problems.

---

## ⛔ The drift to watch for

The moment this stops being about **frames** and starts being about **people**, the IRB position
changes completely. Two specific temptations:

- *"While I'm on the panel, I could run a quick pilot in one other country."* — that is fielding to a
  non-approved population. Amendment first, no exceptions.
- *"I'll just ask a few auditors abroad informally what they think."* — informal does not mean
  outside the protocol. If it informs findings, it is data collection.

**The feasibility study's strength is that it needs nobody's permission. Do not spend that.**
