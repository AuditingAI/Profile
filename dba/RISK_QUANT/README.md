# Risk quantification

Quantifying research risk before it is paid for.

The programme's one original finding is that a specialist population's prevalence in a sampling frame
is the binding constraint on empirical work, and is knowable in advance. Currently that finding is a
story about one study. This directory makes it an instrument.

---

## What is here

| | |
|---|---|
| `FEASIBILITY_MODEL.md` | The funnel, the arithmetic, the validation, and what the model cannot do |
| `feasibility.py` | The calculator. Stdlib only, matching `../03_Data/*.py` |

## Start here

```
python3 feasibility.py --validate     # reproduce the qualifying study — the hard test
python3 feasibility.py --sweep        # where a survey stops being viable
```

Then, for a new design:

```
python3 feasibility.py --frame 334976 --prevalence 0.00006 --target 100
```

---

## The one test that matters

`--validate` reproduces the qualifying study from its own rates: 334,976 members → 20 eligible → 4
usable → ~$1,000 spent. **If the model cannot reproduce the case that produced it, nothing else it
says should be believed.** The test runs first and reports PASS or FAIL in plain terms.

---

## What this is not

**Not the AI-governance risk scoring for the consulting practice.** That is a different thing with a
similar name — sycophancy exposure, drift surface, automation-bias exposure across a control
environment. It shares the underlying funnel math and it belongs to the Industry lane. A handoff
entry describes the shared model; nothing about it is built here.

`../../CLAUDE.md`: academic and industry materials never appear in the same document.

**Not a statistical power calculation.** Power asks how large a sample must be to detect an effect.
This asks whether that sample can be obtained at all. They answer different questions and the second
one is asked far less often — which is the whole point.

**Not a substitute for a pilot.** The rates it multiplies have to come from somewhere. A pilot is
where they come from. This tool tells you whether running the pilot is worth it.
