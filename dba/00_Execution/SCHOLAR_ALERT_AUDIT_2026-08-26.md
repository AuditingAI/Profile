# Scholar alert audit — the alert is the wrong instrument

**26 August 2026.** Triggered by Yasir's standing instruction: the purpose of this system is to
watch Gmail, pull the Scholar links, and extract **sycophancy** and **epistemic drift** relative to
the anchoring work — and to track how the study is changing.

**The short answer: you cannot extract what was never collected.**

---

## 1 · What the corpus actually contains

`scholar-links-all.md` — 1,637 unique papers, Sept 2025 to May 2026, from one alert.

| Term | Hits in 1,637 papers | Which link |
|---|---|---|
| `automation bias` | **23** | L1 ✅ |
| `anchor` | 18 | L1 ✅ |
| `professional skeptic` | 25 | L1 ✅ |
| `LLM` | 228 | context |
| `large language model` | 90 | context |
| **`sycophan`** | **5** | **L2** ⚠️ |
| **`epistemic drift`** | **0** | **L3** ❌ |
| **`model collapse`** | **0** | **L3** ❌ |
| **`recursive`** | **1** | **L3** ❌ |
| `algorithm avers` | **0** | the counter-literature ❌ |
| `algorithmic appreciat` | **0** | the counter-literature ❌ |
| `decision aid` | **0** | L1 mechanism ❌ |

**L1 is well covered. L2 is barely present. L3 is absent. The counter-literature is absent
entirely.**

That last row matters most. `KNOWLEDGE/01_THEORY.md` §3 names the automation-bias / algorithm-aversion
contradiction as the programme's most serious unaddressed theoretical gap. **Zero papers in the
corpus touch it.** The instrument has never once been pointed at the thing most likely to sink the
argument.

---

## 2 · Why — a term collision

**37 alert emails in the last 60 days. Every one is the same alert: "Auditor Bias — new results."**

Reading what it actually returns:

> Bias auditing in hate speech detection · vision model bias · satellite precipitation bias
> correction · gender bias in Indian sports · real estate algorithmic decision-making · L2 speaking
> assessment · video anomaly detection · volatility forecasting · text-to-image cultural bias ·
> e-recruitment cultural bias

**"Auditor Bias" is matching the *algorithmic fairness auditing* sense of "audit," not the
*accountant exhibiting bias* sense.** It is dredging the AI-fairness literature, which is large,
fast-moving, and almost entirely irrelevant to auditor judgment.

Of thirty recent alerts inspected, **roughly four were usable.** That is not a triage problem the
`/research` sweep can fix downstream. The collection is wrong at the source.

---

## 3 · Sitting unread in the inbox since 1 August

**The single most L3-relevant paper the alert has ever returned, and it was never opened.**

> **"How LLMs Audit Each Other: Five Mechanisms of Auditor Bias in Cross-Model Peer Review Under
> Identity Disclosure and Cross-Lingual Conditions"** — O. EFT, 2026
> Scholar alert, 1 Aug 2026 · thread `19fbefcb9b71ecc9` · **status: unread**

Models evaluating models. Cross-model peer review. Named mechanisms of bias in that evaluation.
**That is recursive epistemic drift, described by someone else, in the exact terms L3 argues.**
`read_state: lead` — pull it and read it in full before anything is claimed about it.

Three others worth pulling from the same 60 days:

| Paper | Why | Link |
|---|---|---|
| Che & Liu (2026), *Schizophrenia Bulletin* — "Mental Health-Focused Intervention for Enhancing Professional Judgment in National Auditors: A Cognitive Bias Perspective" | Auditor judgment + cognitive bias + an **intervention**. Closest thing to a construct row the alert has produced | 21 Aug |
| Arslan (2026), arXiv — "Does Splitting a Triage Decision Across Agents Hide Bias or Help Catch It? A Multi-Agent Simulation Study of LLM-Based Resource Allocation Under Audit Capacity" | Multi-agent LLM decisions under audit. Possible L3 mechanism | 13 Aug |
| Krey, Rancati, Parajuli & Srivastava (2026), *Int. J. Bank Marketing* — "Artificial intelligence and bias in banking and financial services: a comprehensive review" | Domain review, banking. Practice-section material | 19 Jul |

All four are **leads**. None has been read. Per `../AI_RUNBOOKS/SCHEMAS.md`, a lead is not a citation.

---

## 4 · The fix — four alerts, not one

Create these at `scholar.google.com` → Alerts. Keep "Auditor Bias" running; it is cheap and it
occasionally throws something like the EFT paper.

| # | Alert string | Hunts |
|---|---|---|
| **A** | `sycophancy OR "sycophantic" "language model"` | **L2.** The mechanism, from the model-evaluation side |
| **B** | `"model collapse" OR "self-consuming" OR "recursive training" language model` | **L3.** The technical literature on models trained on model output |
| **C** | `"algorithm aversion" OR "algorithmic appreciation" expert judgment` | **The counter-literature.** The gap in `KNOWLEDGE/01_THEORY.md` §3 |
| **D** | `auditor "professional skepticism" "artificial intelligence" reliance` | **L1/L2 in the domain.** Narrow enough to avoid the fairness-auditing collision |

**Alert C is the one to create first.** It is the only one pointed at evidence that would *weaken*
the argument, and it is the pass a bias researcher can least afford to skip. Everything else
accumulates support.

**Why "Auditor Bias" cannot be repaired by narrowing.** The collision is in the word *audit* itself.
Adding terms to that alert filters the fairness literature down but never reaches the sycophancy or
model-collapse literature, which does not use the word "audit" at all. Four narrow alerts beat one
broad one that is fishing in the wrong pond.

---

## 5 · What this means for the study

The programme's own diagnosis of the IB literature — *the field kept measuring the wrong thing, or
measuring one thing while believing it had measured another* — **applies to its own literature
surveillance.**

One alert has been running for a year. It was configured for the anchoring study, which was a pure
L1 question. The study has since grown two more links and a qualitative arm, and the instrument that
watches the literature never changed.

`KNOWLEDGE/03_METHOD.md` §6 already lists three instances of this error in the programme. **This is
the fourth**, and unlike the others it was still happening at the moment it was found.

---

## Actions

- [ ] **Create alerts A–D.** Ten minutes at `scholar.google.com/scholar_alerts`. Start with **C**.
- [ ] **Pull and read the EFT paper.** It has been unread since 1 August and it is the closest thing
      to external support L3 has.
- [ ] Pull the other three leads.
- [ ] Update `RESEARCH_AGENT_DESIGN.md` §1 — the relevance gate assumes the alerts are aimed
      correctly. They are not, and the gate cannot compensate for a collection error upstream.
- [ ] Re-run this count after alerts A–D have been live a month. If `epistemic drift` is still 0,
      the terms are wrong, not the literature.
