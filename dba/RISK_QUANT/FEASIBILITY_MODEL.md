# The feasibility model

Turns the qualifying study's finding into an instrument. The claim it operationalises:

> **The binding constraint on specialist-population research is prevalence in the sampling frame, and
> it is knowable before a dollar is spent.**

---

## The funnel

```
frame  ──prevalence──▶  eligible  ──response──▶  reached
                                                    │
                                              completion
                                                    ▼
                            usable  ◀──(1 − exclusion)──  completed
```

| Term | Is | Where it comes from |
|---|---|---|
| `frame` | Members of the sampling frame | The panel, the association list, the network |
| `prevalence` | Proportion of the frame that is **eligible** | **The number nobody checks.** Often visible before launch |
| `response` | Proportion of eligible who start | Platform history or pilot |
| `completion` | Proportion of starters who finish | Pilot |
| `exclusion` | Proportion **removed** at screening | Attention checks, partials, screen failures |

**Usable = frame × prevalence × response × completion × (1 − exclusion)**

And, rearranged — the form that actually settles a design decision:

**Frame needed = target ÷ [prevalence × response × completion × (1 − exclusion)]**

---

## Validated against the case that produced it

```
python3 feasibility.py --validate
```

| | Modelled | Actual | |
|---|---|---|---|
| Eligible in a 334,976 panel | 20.0 | 20 | ✅ |
| Usable responses | 4.0 | 4 | ✅ |
| Spend | $1,000 | ~$1,000 | ✅ |
| Prevalence | 0.00005971 | — | **6.0 per 100,000** |
| Cost per usable response | **$250** | — | Against a planned rate of $28/hr effective |

**If the model cannot reproduce the study that produced it, nothing else it says is worth reading.**
That is the only hard test in this directory and it is the first thing `--validate` reports.

---

## What it says about the qualifying study

**A survey at this prevalence needs a frame of roughly 9.6 million members.** Prolific had 334,976 —
about 3.5% of what the design required.

That reframes the whole thing. The study was not under-recruited, under-funded, or under-promoted.
**It was impossible**, and it was impossible in a way that was computable before the instrument was
built. No incentive rate fixes a 25× frame shortfall.

```
        frame   eligible   usable   verdict
      100,000          6        1   NEITHER — REDEFINE THE FRAME
      334,976         20        3   NEITHER — REDEFINE THE FRAME   ← where it was run
    1,000,000         60       10   INTERVIEW VIABLE — SURVEY IS NOT
    5,000,000        299       52   INTERVIEW VIABLE — SURVEY IS NOT
   17,000,000      1,015      177   SURVEY VIABLE
```

---

## The cliff — and why the method changes, not the budget

The same twenty people support a different design entirely.

**The survey's 83% exclusion rate does not carry over.** It came from attention checks, partial
completions and screen failures on an anonymous instrument. An interview study contacts eligible
people directly and loses them to declining and no-showing instead — a materially gentler funnel.

| | Survey | Interview study |
|---|---|---|
| Target | 100 | **12** |
| Eligible available | ~20 | ~20 |
| Loss profile | 83% — attention checks, partials, screen failures | ~35% — declines and no-shows `[VERIFY]` |
| Reachable | **3** | **12** |
| Verdict | Impossible | **Viable** |

> **Same population. Same twenty people. The method changed, and with it what counts as enough.**

That single line is the qualitative arm's feasibility argument
(`../QUALITATIVE/SAMPLING_AND_RECRUITMENT.md` §1), and it is now arithmetic rather than assertion.

`[VERIFY]` — the interview-side rates (0.80 response, 0.80 completion, 0.05 exclusion) are estimates,
marked as such in the code. Replace them with observed rates after the first five approaches.

---

## Using it before a study

Four numbers, before anything is built:

1. **Frame size.** How many people are in the pool you can actually reach?
2. **Prevalence.** What proportion meet every eligibility criterion — simultaneously? Panels report
   this in their configuration screens. Professional bodies will often tell you if asked.
3. **Target n.** What the planned analysis requires, not what feels respectable.
4. **Run it.** `python3 feasibility.py --frame N --prevalence P --target T`

**If the answer is "frame needed: 25× what you have," you have learned something more valuable than a
failed study would have told you — and you have learned it for free.**

---

## Limitations of the model

Stated because the programme's failure mode is overstatement, and a tool built from one case is
exactly where overstatement would be easiest.

- **Rates are multiplicative and independent.** In reality they correlate — a rarer population is
  usually also a busier one, so low prevalence and low response arrive together. The model is
  therefore **optimistic**.
- **Prevalence is treated as observable.** For panels it usually is. For professional bodies and
  networks it is an estimate, and a wrong estimate propagates straight through.
- **One validation case.** The model reproduces one study on one platform. `RB01` exists to find
  others — see `../AI_RUNBOOKS/perplexity/RB01_recruitment_precedent.md`. **If precedent studies
  contradict these funnel shapes, this model is wrong and gets rewritten.**
- **Design floors are conventions, not laws.** The survey floor of 100 comes from Dr. Rey's directive
  for this instrument; the interview floor of 10 from phenomenological convention. Both are arguable
  and both are parameters, not constants.
- **It says nothing about data quality.** A reachable n is not a good n.

---

## Where this goes

| | |
|---|---|
| **P1 manuscript** | The sensitivity table is the paper's central figure — `../P1_Feasibility_Note/MANUSCRIPT_DRAFT_v1.md` |
| **The qualitative arm** | Supplies the feasibility argument as arithmetic |
| **Teaching** | The left-handed-neurosurgeons opener in `../KNOWLEDGE/04_THE_FAILURE.md`, with live numbers behind it |
| **Industry lane** | The same funnel math underlies AI-governance risk scoring. **Handed off, not built here** — see `../../career/HANDOFF.md` |
