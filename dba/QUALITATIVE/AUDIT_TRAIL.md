# Audit trail — qualitative arm

**Append-only. Newest at top. Dated. Written when the decision is made, never reconstructed.**

This file is the confirmability evidence for the qualitative arm (`TRUSTWORTHINESS.md` §4). A
reconstructed audit trail is a narrative about a study, not evidence of one — so an entry written
late is marked late, and an entry that should exist and does not is a gap that gets reported rather
than filled in.

---

## What gets an entry

| Category | Tag | Examples |
|---|---|---|
| Design decision | `DESIGN` | Method chosen, scope changed, protocol revised |
| Sampling | `SAMPLING` | Participant screened in or out, referral accepted, stop-or-continue call |
| Analysis | `ANALYSIS` | Cluster created, renamed or dissolved; unit parked; saturation assessed |
| **Confirmation hazard** | `HAZARD` | Any occasion I noticed myself feeling confirmed by a participant |
| Leading question | `LEADING` | Where I supplied the answer in an interview |
| AI use | `AI` | Tool, what it was asked, what was done with the output |
| Outsider review | `OUTSIDER` | Review conducted, what it found, what changed |
| Ethics | `IRB` | Submission, approval, modification, participant withdrawal |

**Format:**

```
### YYYY-MM-DD · TAG
**Decision / event.** One line.
**Reason.** Why, in the researcher's own words.
**Consequence.** What changes as a result. "Nothing" is a valid answer.
```

---

## Entries

### 2026-08-27 · DESIGN
**FIU University Graduate School AI guidelines received and recorded as binding.**
**Reason.** Circulated by Dr. René M. Price, Associate Dean UGS. They sit above the course syllabi
and above Dr. Rey's instruction; where standards differ, the stricter one applies.
**Consequence.** Three things this arm did not previously account for. (1) Disclosure must appear in
the preliminary pages of every proposal draft, in the Methods section where AI touched analysis, and
in the caption of any AI-assisted figure. (2) **The committee must review and approve the AI use** —
this has not been done and is now an open item for Dr. Rey. (3) Original unedited drafts must be
preserved, which git history already satisfies more strongly than the policy requires. Full record
and a draft disclosure statement: `../00_Execution/FIU_AI_POLICY_2026.md`.

### 2026-08-27 · DESIGN
**UGS §7 names "obsequiousness" as an unavoidable property of large language models.**
**Reason.** Noted because it is directly relevant to the L2 link, which has until now been argued
only from model-evaluation literature. FIU's own graduate school lists, among the risks of
generative AI, the "tendency to agree, reinforce user assumptions, or provide overly confident
answers."
**Consequence.** A citable institutional acknowledgement that the phenomenon is recognised. It does
**not** make L2 established — a policy document naming a risk is not evidence that the risk operates
in audit judgment, and the distinction must be stated wherever this is cited.


### 2026-08-26 · DESIGN
**The qualitative arm is scoped to L2 only. L3 is not designed.**
**Reason.** L3 asks how the evidentiary basis of a judgment changes across successive engagements —
a process-over-time question. Answering it needs multi-year engagement files or repeated access to
the same auditors across engagement years. Neither exists. Writing a protocol for a study that cannot
be run is the qualifying study's error committed a second time with more paperwork.
**Consequence.** L3 research questions stay on the record in
`../00_Execution/QUALITATIVE_REFRAME_L2_L3.md` §4 as future work. Nothing in this directory addresses
them.

### 2026-08-26 · DESIGN
**Method is phenomenology, not the Gioia method.**
**Reason.** Dr. Gonzalez recommended phenomenology for translating an existing quantitative research
question, and the recommendation fits the question: L2 asks what auditors experience and how they
account for it, not how much, how often, or what causes what. Gioia is a theory-building design and
would answer a different question.
**Consequence.** `../00_Execution/QUALITATIVE_REFRAME_L2_L3.md` §6, which called Gioia "the L2
method," is corrected. Gioia is retained for the **reflexivity architecture** — the declared
insider/outsider split — and for nothing else.

### 2026-08-26 · DESIGN
**Falsification conditions written before any data exists.**
**Reason.** A design that cannot be disconfirmed is not a design, and a falsification table written
after data collection is a rationalisation. Four outcomes that would weaken or collapse the L2
argument are stated in `PROTOCOL_phenomenology.md` §6.
**Consequence.** Any of the four, if observed, is written up as the finding. Committing this before
recruitment means the commitment is timestamped in git history and cannot be quietly revised.

### 2026-08-26 · DESIGN
**Saturation defined as a stopping rule, in advance.**
**Reason.** Saturation declared at write-up is unfalsifiable and usually means "the deadline
arrived." Stated in advance it is a control.
**Consequence.** Stop at three consecutive interviews producing no new surviving meaning unit, with
the outsider reviewer's agreement, and never below 10 participants. See
`SAMPLING_AND_RECRUITMENT.md` §3.

### 2026-08-26 · DESIGN
**The confirmation hazard log is established as a required control.**
**Reason.** The study examines what happens to judgment when something reaches a conclusion that
agrees with one already held. A researcher who feels confirmed by a participant describing exactly
the deference his chain predicts is experiencing the phenomenon under study, inside the study. This
is the most likely way this arm fails, and it fails invisibly.
**Consequence.** Every such occasion is logged here the same day, tagged `HAZARD`, with what was said
and what I felt confirmed about.

### 2026-08-26 · AI
**Protocol, interview guide, sampling plan, coding plan and trustworthiness criteria drafted with
Claude (Claude Code), 26 August 2026.**
**Reason.** Organisation and drafting of research infrastructure — permitted under Dr. Rey's standing
instruction and GEB 7911's policy, which allow AI for brainstorming, organisation and clarity.
**Consequence.** These are **drafts, and raw material for rewriting.** No participant data existed and
none was involved. The AI boundary governing the analysis itself is set in `CODING_PLAN.md` and is
considerably narrower than what was permitted here: AI may not assign a code, name a theme, or write
any part of the description. Nothing in this directory has been reviewed by Dr. Gonzalez.

### 2026-08-26 · IRB
**Not submitted. No participant may be approached.**
**Reason.** IRB-25-0462 approves an anonymous online survey. This arm is audio-recorded interviews
with identifiable participants describing their own judgment practices — a different risk profile
requiring a modification or a new protocol.
**Consequence.** Recruitment is blocked until approval. Three open questions to put to the FIU IRB
office are listed in `SAMPLING_AND_RECRUITMENT.md` §5. Compensation must be decided before the
submission, not after.
