# Tonight · Thu 10 Sep, 7:00-9:30pm ET — GEB 7365, Structuring the MNE

## The one thing that matters tonight

**You told Newburry, in writing, on 3 September:** *"That combination is, I think, the model:
reachable sample as prevalence multiplied by response rate, compounding across national frames
rather than averaging. **I will bring a first version of it to the next session.**"*

**Tonight is that session.** He sent you the Harzing paper unprompted and you promised him a model.
Professors remember that. It now exists: `../../RISK_QUANT/crossnational.py`.

---

## The model, in one exhibit

Run `python3 dba/RISK_QUANT/crossnational.py` to show it live, or read this table out.

**Target: 30 usable responses in every country in the design.**

| Design | Mean response rate | Binding rate | Frame needed in EACH country |
|---|---|---|---|
| Spain | 15.4% | 15.4% | 18,760,831 |
| + Germany | 13.2% | 11.1% | 26,028,541 |
| + Japan | 12.3% | 10.4% | 27,780,462 |
| + UK | 10.5% | 5.2% | 55,560,923 |
| + China | 9.2% | 4.0% | **72,229,200** |

**The sentence that carries it:**

> "The mean barely moves. Fifteen point four percent down to nine point two. The requirement moves
> by a factor of four, because a comparative design is priced by its worst country, not its average
> one. Every frame you add can only lower the binding rate. It can never raise it. That is what I
> mean by compounding, and it only runs one direction."

**Where the two numbers come from, if asked:**
- **Prevalence, 6 per 100,000** — my own panel screen. 20 eligible of 334,976.
- **Response rates** — Harzing, Reiche and Pudelko (2012), Illustration 7. The paper he sent me.

---

## The three caveats — say them before anyone asks

This is what separates a model from a claim, and Newburry will respect it more than the result.

1. **Prevalence is held constant across countries and almost certainly is not.** No cross-national
   prevalence data for this population exists. **Obtaining it is the empirical contribution I am
   proposing.** That is the study.
2. **Harzing's rates are one study, one instrument, one period.** They are the best available
   anchor, not a population parameter.
3. **Korea's 47% is a telephone effect, not a country effect.** Switching instrument moved the
   number roughly five times more than any country difference in the same table. If that holds,
   *which instrument at what prevalence* may matter more than *which country* — which is a finding
   in its own right and points at the qualitative design.

---

## Tonight's readings — one line each, if you have not read them

The session is **Structuring the Multinational Corporation**. Five papers. You do not need them to
contribute, because your model is the contribution tonight.

| Paper | The one thing it says |
|---|---|
| **Rugman & Verbeke (2004)** *JIBS* | Most "global" MNEs are not global. They are regional. The data on the world's largest firms shows sales concentrated in the home region |
| **Lopez, Kundu & Ciravegna (2009)** *JIBS* | Applies that test to born-global firms and asks whether they are actually born *regional*. **Kundu is FIU, and he is on your Module 2 paper too** |
| **Aguilera, Marano & Haxhi (2019)** *JIBS* | A review of international corporate governance. Governance varies by national institutional setting |
| **Meyer, Li & Schotter (2020)** *JIBS* | Managing the subsidiary. The subsidiary is not a passive unit; it has its own agency and its own relationship to headquarters |
| **Zeng et al. (2023)** | MNE control and coordination |

**The honest line if called on cold:** *"I read it for the structure argument rather than the
empirics. What struck me was..."* then the one-liner. Do not invent detail.

---

## The connection, if you want one contribution beyond the model

> "Rugman and Verbeke say the firms we call global are mostly regional once you look at where the
> sales actually are. My project has the same shape on the research side. A study we would call
> cross-national is often single-country work with extra countries named in the title, because the
> frames in the other countries could never have supported the design. In both cases the label
> outruns what the data can carry."

That ties tonight's core reading to your project without hijacking the session.

---

## Sequencing

- **If he asks for the update:** lead with the exhibit, then the three caveats. Two minutes.
- **If he does not ask:** offer it once, briefly. *"I have a first version of the model if it is
  useful — happy to hold it for the residency."* Do not force it into a session about MNE structure.
- **Either way, the promise is kept**, which is the thing that was actually at stake tonight.
