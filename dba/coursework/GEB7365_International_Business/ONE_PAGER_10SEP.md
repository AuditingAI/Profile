# One page — 10 September, GEB 7365

**Print this or keep it open. Everything you need is on this page.**

---

## The five theories, in plain language

| Paper | The claim, in one line | The word that matters |
|---|---|---|
| **Rugman & Verbeke (2004)** | Firms we call "global" mostly are not. Look at where their sales actually land and most is in the home region | **Regional, not global** |
| **Lopez, Kundu & Ciravegna (2009)** | Runs the same test on start-ups that look international from day one. Are "born globals" actually born *regional*? *(Kundu is FIU and is on your Module 2 paper)* | **Born regional** |
| **Aguilera, Marano & Haxhi (2019)** | How a firm is governed depends on the country it sits in. There is no single global governance model | **Institutional variation** |
| **Meyer, Li & Schotter (2020)** | The overseas subsidiary is not a branch that takes orders. It has its own agency and negotiates with headquarters | **Subsidiary agency** |
| **Zeng et al. (2023)** | How headquarters actually controls and coordinates units that are far away | **Control vs coordination** |

**The thread running through all five:** the multinational is less unified than the label suggests.
Sales are regional, governance is local, subsidiaries push back, and control is harder than the org
chart implies. **Every one of these papers is about a gap between the label and the reality.**

---

## What you are expected to talk about

**Two things, and only two.**

**1 · The model you promised.** You wrote to Newburry on 3 September: *"I will bring a first version
of it to the next session."* Tonight is that session. Lead with the exhibit below.

**2 · One contribution on the readings**, if the room turns that way:

> "Rugman and Verbeke say the firms we call global are mostly regional once you look at where the
> sales actually are. My project has the same shape on the research side. A study we call
> cross-national is often single-country work with other countries named in the title, because the
> frames in those countries could never have supported the design. In both cases the label outruns
> what the data can carry."

**If you have not read the papers:** *"I read it for the structure argument rather than the
empirics. What struck me was..."* then the one-liner from the table. Do not invent detail.

---

## The model, before and after

### Before tonight — the single-country model

> **usable = frame × prevalence × response × screening survival**

Validated against your own study: 334,976 panel members × 6 per 100,000 × screening = **4 usable
against a target of 100**. It answered one question: *is this design viable in one country?* Answer:
no, and the number said why.

**What it could not do:** anything about more than one country. Response rate was a placeholder,
not a measurement.

### After tonight — the cross-national model

Newburry's own Harzing paper supplied the missing parameter. Response rate is now empirical, and
varies by country: **4.0% in China to 15.4% in Spain**, 9.6% overall.

> **The design clears only if EVERY national frame clears. So it is priced by the weakest, not the average.**

**Target: 30 usable responses in every country.**

| Design | Mean response | **Binding rate** | Frame needed in EACH country |
|---|---|---|---|
| Spain | 15.4% | 15.4% | 18,760,831 |
| + Germany | 13.2% | 11.1% | 26,028,541 |
| + Japan | 12.3% | 10.4% | 27,780,462 |
| + UK | 10.5% | 5.2% | 55,560,923 |
| + China | 9.2% | **4.0%** | **72,229,200** |

**Say this:**

> "The mean barely moves. Fifteen point four percent down to nine point two. The requirement moves
> by a factor of four, because a comparative design is priced by its worst country, not its average
> one. Every frame you add can only lower the binding rate. It can never raise it. That is what I
> mean by compounding, and it only runs one direction."

**Live demo, if you want it:** `python3 dba/RISK_QUANT/crossnational.py`

---

## The three caveats — say them before you are asked

This is what makes it a model rather than a claim, and it will earn you more than the result does.

1. **Prevalence is held constant across countries and almost certainly is not.** No cross-national
   prevalence data for this population exists. **Getting it is the contribution I am proposing.**
2. **Harzing's rates are one study, one instrument, one period.** Best available anchor, not a
   population parameter.
3. **Korea's 47% is a telephone effect, not a country effect.** Changing instrument moved the number
   about five times more than any country difference in the same table. If that holds, *which
   instrument at what prevalence* may matter more than *which country*.

---

## Sequencing tonight

| If | Then |
|---|---|
| He asks for the project update | Lead with the exhibit, then the caveats. Two minutes |
| He does not ask | Offer once: *"I have a first version of the model if it is useful, or I can hold it for the residency."* |
| The room is deep in MNE structure | Use the Rugman bridge, hold the model |

**Either way the promise is kept.** That was what was actually at stake tonight.
