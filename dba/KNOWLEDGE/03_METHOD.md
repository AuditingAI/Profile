# Method — what I can actually do

Not a methods textbook. A record of the procedures this programme has run, or is now committed to
running, with the file that holds each one. **Nothing is copied here that can be linked.**

---

## 1 · Survey construction

**Done.** Fielded July 2026, Qualtrics, v2.1 post-pilot.

| Element | Detail | Where |
|---|---|---|
| Structure | 5 eligibility screens → 55 items in 11 blocks → 2 embedded attention checks → open-ended anchoring-experience item → demographics | `../Dissertation_Instrument_v3_DRAFT.md` |
| Item design | 5 Likert items per construct, **one reverse-coded per block** | `../Full_Survey_Questionnaire_v2.md` |
| Quality architecture | Anonymised, bot-detected, duplicate-protected | `../Qualtrics_Codebook_and_Setup.md` |
| Pilot | LinkedIn contacts → wording refinements → v2.1 | `../Informed_Pilot_Run_Plan.md` |

**What was proven:** the instrument administered cleanly. Zero attention-check failures among
complete respondents; platform response-quality index 95%. **The instrument was never the problem.**

**What I would do differently.** Run the prevalence check before building anything. See
`04_THE_FAILURE.md` — the sequence was instrument → IRB → panel → discover the population does not
exist, and the arithmetic was available at step one.

---

## 2 · Data cleaning and screening

**Done, and reproducible.** A scripted nine-step protocol with exclusion logging, not a manual pass.

| Script | Does |
|---|---|
| `../03_Data/clean_and_screen.py` | The nine-step protocol |
| `../03_Data/exclusion_log.csv` | Every exclusion, with reason |
| `../03_Data/descriptives_reliability.py` | Descriptives and α |
| `../03_Data/make_jamovi_file.py` | Export for jamovi |

**The discipline worth keeping:** every exclusion is logged with a reason, so the path from 23 raw to
4 usable is auditable by someone who was not there. That is why the prevalence finding is credible
rather than an excuse — the arithmetic can be checked.

⚠️ **`PRACTICE_SIMULATED_dataset.csv` and everything derived from it never enters a manuscript.**
The boundary is stated in `../03_Data/PRACTICE_README.md` and it is absolute.

---

## 3 · Exploratory factor analysis and reliability

**Specified in full, never executed on real data.** Not executable at n=4.

| | |
|---|---|
| Extraction | Principal Axis Factoring |
| Rotation | Direct Oblimin — oblique, because the constructs are expected to correlate |
| Target n | 100 (advisor directive, 30 June 2026) |
| Reliability | Cronbach's α per construct |
| Playbook | `../EFA_Reliability_Playbook.md` |
| Practised on | Simulated data only — `../03_Data/run_practice_efa.py` |

**What comes after, specified but not reached:** CFA → regression → PLS-SEM, with explicit decision
criteria at each step (`../Research_Paper_YMalik_v4_master.md` Ch. 4).

**The honest statement:** *the study validates nothing statistically.* That sentence is already in
`../STUDY_OVERVIEW.md` §7 and it stays there.

**What I can teach from this anyway.** The methodology chapter is contract-grade — decision criteria
stated in advance for every step. That is worth more pedagogically than a chapter that reports
results, because it shows what committing to an analysis before seeing data actually looks like.

---

## 4 · Phenomenology

**New. Protocol written 26 August 2026. Nothing fielded.**

| | |
|---|---|
| Design | Modified Stevick–Colaizzi–Keen |
| Sequence | Epoché → horizontalisation → meaning units → clusters → textural → structural → composite |
| Sample | 10–15, criterion-sampled, maximum variation within the criterion |
| Stopping rule | Three consecutive interviews with no new surviving unit, outsider agreeing, never below 10 |
| Reflexivity | Declared insider/outsider split, after Gioia & Chittipeddi (1991) |
| Protocol | `../QUALITATIVE/PROTOCOL_phenomenology.md` |

**The two things I did not know before building this:**

1. **Every step needs a stopping condition.** Qualitative analysis without finish lines runs until it
   feels done, which is exactly when a researcher's prior commitments have finished asserting
   themselves. Each step in the protocol has a "done when."
2. **Falsification conditions must be written before the data exists.** `PROTOCOL_phenomenology.md`
   §6 lists four outcomes that would weaken or collapse the L2 argument. Written afterwards it would
   be a rationalisation; written before and committed to git it is timestamped and checkable.

---

## 5 · What I have never done

Stated plainly, because knowing the edge of your competence is part of the competence.

| | Status |
|---|---|
| Confirmatory factor analysis on real data | Never |
| PLS-SEM on real data | Never |
| Experimental / vignette design with a manipulated anchor | Never — **and this is what construct 11 actually needs.** See `02_CONSTRUCTS.md` |
| Longitudinal or archival analysis | Never — which is why L3 is scoped out |
| Conducting a research interview | **Never.** The protocol is written; the skill is not yet practised |

**Item 5 deserves a note.** Fifteen years of audit interviewing is not research interviewing. Audit
interviews establish facts against a control objective; phenomenological interviews follow someone
into an experience and resist closing it down. The habits transfer badly in one specific way: an
auditor knows how to get to the answer, and getting to the answer is exactly what ruins this kind of
interview. **Practise on two people who are not participants before the first real one.**

---

## 6 · The methodological through-line

The programme's own diagnosis of the international business literature applies to itself: *the field
kept measuring the wrong thing, or measuring one thing while believing it had measured another.*

- The survey measured **perceived judgment discipline** and was described as measuring **anchoring
  reduction** (`02_CONSTRUCTS.md`).
- The recruitment plan measured **budget and effort** when the binding constraint was **prevalence**
  (`04_THE_FAILURE.md`).
- The qualitative arm is designed to describe an **experience**, and must not be allowed to drift
  into claiming an **effect** (`../QUALITATIVE/CODING_PLAN.md` step 7).

Three instances of the same error in one programme. Noticing it is the reason the third one has a
control written against it in advance.
