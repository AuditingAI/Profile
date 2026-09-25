# Attention & Focus Quality Controls — Initial + Embedded

**Purpose:** weed out inattentive, straight-lining, or bot-driven responses *before* they pollute the EFA dataset, without burdening attentive professional auditors.

**IRB scope note:** these are standard **data-quality controls**, not new measurements. They do **not** change what the instrument measures, do not introduce new constructs or populations, and do not request sensitive data. Standard practice in PCAOB / behavioral-auditing research (Bonner, 2008; Hurtt, 2010; Meade & Craig, 2012). No IRB amendment is required. Add as Quality Controls in the survey logic; document briefly in Chapter 4 (Methodology) as "data-quality screening." If unsure, flag Q-A3 (eligibility-comprehension hybrid) to Dr. Rey in next week's update.

---

## Block placement in the Qualtrics survey

```
Block 1  — Informed Consent (IRB-approved letter + Yes/No)
Block 2  — Eligibility Screeners (4 items with screen-out branching)
Block 3  — INITIAL QUALITY SCREEN (this document, 3 items, ~60 seconds)
Block 4–14 — 11 Construct Blocks (in Randomizer)
            ↳ Embedded IMC after Block 7 and Block 11 (this document)
Block 15 — Demographics
Block 16 — Final Quality Check (this document, 1 open-text item)
Block 17 — Debrief
```

**Page timer:** enable Qualtrics' page-level timer on every construct block. Built-in, no item displayed. Used in exclusion rules only.

---

## Initial Quality Screen (Block 3) — three items, ~60 seconds total

### Q-A1 — Up-front attention commitment

> **Survey research depends on respondents reading each item carefully and providing thoughtful answers. Will you commit to doing that throughout this 15–20 minute survey?**

| Option | Pass / Fail |
|---|---|
| Yes, I commit to reading each item carefully | **Pass** |
| I'm not sure | **Soft-fail** — allow continue, flag for review |
| No, I cannot commit | **Hard-fail** — branch to End-of-Survey thank-you |

**Why it works:** Clifford & Jerit (2015) and Geisen (2022) showed up-front attention commitments improve subsequent response quality by 10–20% with no other intervention. Costs ~10 seconds.

---

### Q-A2 — Instructional manipulation check (early)

> **Audit professionals make many judgments every day. To confirm you are reading carefully, please select "Strongly disagree" for this item.**

Response: 5-point Likert (matches the rest of the instrument)

| Selected | Action |
|---|---|
| Strongly disagree | **Pass** |
| Any other option | **Fail** — flag for exclusion |

**Why it works:** standard Oppenheimer et al. (2009) IMC. The matching Likert scale prevents auditors from spotting it as a "trick" — it looks like a real item.

---

### Q-A3 — Audit-context comprehension (eligibility + comprehension double-check)

> **Which of the following best describes a "long-term auditor engagement" as used in this study?**

| Option | Action |
|---|---|
| A first-year engagement with a new audit client | Fail — flag |
| **A recurring engagement with a continuing client across multiple years** | **Pass** |
| A one-time forensic investigation engagement | Fail — flag |
| An internal training or coaching program | Fail — flag |

**Why it works:** eligible auditors will know this immediately; failure is a strong signal of either inattention or off-target respondent. ⚠️ **Flag this one to Dr. Rey in W06** because it doubles as an eligibility refinement — even though it's not a measurement item, the doubling makes it a borderline call.

---

## Embedded mid-survey IMCs (already drafted; positions confirmed here)

### Q-B1 — After construct block 4 (whichever block randomizer presents 4th)

> **Please select "Agree" for this item to confirm you are paying attention.**

Pass: selected "Agree". Fail: flag.

### Q-B2 — After construct block 8

> **To verify careful reading, please select "Disagree" for this item.**

Pass: selected "Disagree". Fail: flag.

> 💡 **Why both directions:** mixing "Agree" and "Disagree" required responses prevents respondents from learning that "the attention checks always want X."

---

## Final Quality Check (Block 16) — one open-text item, ~30 seconds

### Q-C1 — Substantive judgment description

> **In your own words, briefly describe one situation in your audit work where you've had to compare current-period evidence against a prior-period balance. (Two sentences is plenty.)**

| Response | Action |
|---|---|
| Substantive sentence (≥10 words, audit-relevant terms) | **Pass** |
| Blank, "n/a", "none", "yes", obvious copy-paste, or off-topic | **Fail** — flag |

**Why it works:** open-text at the end catches anyone who Likert-pattern-clicked through. Real auditors will produce something specific in seconds. Costs ~30 seconds for honest respondents; bots and click-farms produce blank or generic responses.

---

## Page-level timing controls (no item shown to respondent)

In Qualtrics, on **every construct block**, add a hidden **page timer** question.

| Threshold | Rule |
|---|---|
| Page time < 3 seconds | Item-level too-fast flag |
| Total survey time < 7 minutes | Whole-response too-fast exclusion |
| Total survey time > 60 minutes | Whole-response possible-distraction flag |

These don't display anything to the respondent — they're logged only.

---

## Exclusion rule (apply during data cleaning, Stage 3b)

A respondent is **excluded from analysis** if **any one** of the following is true:

- Q-A2 failed (initial IMC failed)
- 2 of 3 IMCs failed (Q-A2 + either Q-B1 or Q-B2)
- Q-C1 substantively failed
- Total survey time < 7 minutes
- Straight-line response pattern across ≥3 construct blocks (Mahalanobis distance flag in cleaning)

A respondent is **flagged for review** (not auto-excluded) if **any one** of the following:

- Q-A1 was "I'm not sure"
- Q-A3 failed but other checks passed (possible inattention vs. category confusion)
- Total time 7–9 minutes (borderline fast)
- Single IMC failure (one of three)

Flagged responses get reviewed manually (typical decision: include if other checks all pass).

---

## Documentation for Chapter 4 (Methodology), ~1 paragraph to add

> *Data-quality controls.* Five quality screens were embedded in the survey to detect inattentive or non-substantive responses. An up-front attention commitment (Clifford & Jerit, 2015), two instructional manipulation checks (Oppenheimer, Meyvis, & Davidenko, 2009) — one in the initial screen and one each after the fourth and eighth construct blocks (Meade & Craig, 2012) — an open-ended substantive prompt at survey close, and page-level timers were used. Responses failing the initial IMC, failing two of three IMCs overall, failing the substantive prompt, completing in under seven minutes, or showing straight-line patterns across three or more construct blocks were excluded from analysis.

---

## What to do Saturday afternoon (1 PM Qualtrics build block)

When you reach the Qualtrics build, **add Block 3 (initial screen) right after eligibility** and **Block 16 (final quality check) right before demographics-and-debrief**. The embedded Q-B1 and Q-B2 already exist in Appendix A.

Time cost in the build: ~15 minutes for the new blocks + 5 minutes for the page-timer setup = ~20 extra minutes inside the existing 4-hour Qualtrics block. Net respondent time added: ~90 seconds for honest respondents.

---

## Citations for the Methodology paragraph (all real, verified earlier)

- Clifford, S., & Jerit, J. (2015). Do attempts to improve respondent attention increase social desirability bias? *Public Opinion Quarterly, 79*(3), 790–802.
- Meade, A. W., & Craig, S. B. (2012). Identifying careless responses in survey data. *Psychological Methods, 17*(3), 437–455.
- Oppenheimer, D. M., Meyvis, T., & Davidenko, N. (2009). Instructional manipulation checks: Detecting satisficing to increase statistical power. *Journal of Experimental Social Psychology, 45*(4), 867–872.
- (Hurtt, 2010 and Bonner, 2008 are already in your verified reference pool.)
