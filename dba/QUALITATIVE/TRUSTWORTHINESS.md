# Trustworthiness

Four criteria, each mapped to a procedure that is actually performed and leaves evidence. A
trustworthiness section that lists criteria without procedures is a claim, not a control — and this
programme is run by someone who spends his working life distinguishing the two.

*After Lincoln & Guba's four criteria and Creswell & Miller's validation strategies (2000, `Theory
into Practice` 39(3) — the GEB 7911 Week 7 reading). `[VERIFY]` specific strategy names against the
5th edition of Creswell & Poth before this enters the proposal.*

---

## 1 · Credibility — are the findings a defensible reading of what participants said?

| Procedure | What it looks like | Evidence left behind |
|---|---|---|
| **Member checking** | Each participant receives their textural description — not the raw transcript — and is asked: *"Does this read like your experience? What is wrong or missing?"* | Dated response logged; any change made recorded in `AUDIT_TRAIL.md` |
| **Verbatim throughout** | The textural description quotes rather than paraphrases | Reader can check every claim against words |
| **Outsider review** | Every third transcript read cold by the outsider (`PROTOCOL_phenomenology.md` §5) asking *where is the researcher in this data?* | Dated review notes |
| **The disconfirming pass** | Mandatory re-read for contradicting material before write-up | Findings recorded in `CODING_PLAN.md` output, contradictions reported |
| **Prolonged engagement** | Fifteen years in the practice | Stated as strength **and** as bias in the epoché |

**Member checking is returned on the description, not the transcript.** People rarely disagree with a
recording of themselves; they will readily disagree with an interpretation. Only the second is a
check.

---

## 2 · Transferability — can a reader judge whether this applies to their setting?

**The study does not generalise and will not claim to.** Transferability is offered, not asserted —
the reader decides.

What that requires:

- **Thick description** of setting: firm type and size, function, engagement type, tool category,
  seniority, industry — enough that a reader recognises their own context or does not
- **The sample described honestly**, including what it is not: no claim to represent auditors, any
  jurisdiction, or any firm
- **Maximum-variation sampling stated** (`SAMPLING_AND_RECRUITMENT.md` §2), so the reader can see the
  range the essence was drawn across
- **Boundary conditions named** — where the description would be expected to fail

---

## 3 · Dependability — would the process bear inspection?

| Procedure | Evidence |
|---|---|
| **The protocol was written before data collection** | These files, dated and in git history with commit timestamps |
| **Every design decision logged as made** | `AUDIT_TRAIL.md`, append-only |
| **The stopping rule stated in advance** | `SAMPLING_AND_RECRUITMENT.md` §3 — three consecutive interviews with no new surviving unit |
| **Falsification conditions stated in advance** | `PROTOCOL_phenomenology.md` §6, written before a participant existed |
| **AI use logged at every step** | `CODING_PLAN.md` boundary + trail entries |

**Git is doing real work here.** The commit history is a timestamped, third-party-verifiable record
that the protocol preceded the data. Very few qualitative studies can demonstrate that. This one can,
because the repository is public and the history is not rewritable without it showing.

That is also why **`git push --force` is prohibited in this repository.** The rule is in `CLAUDE.md`
for collaboration reasons; it is *also* a methodological control.

---

## 4 · Confirmability — do the findings come from the data or from me?

This is the hard one, and the honest answer is that it cannot be fully achieved — only made visible.

| Procedure | What it addresses |
|---|---|
| **The epoché statement** (`PROTOCOL_phenomenology.md` §3) | Names four specific commitments, including the stake in the answer |
| **Reflexive memo before each listen-back** | Catches the interpretation forming before it hardens |
| **Leading questions flagged in the margin** | Marks where I supplied the answer |
| **The insider/outsider split** | A second person whose only job is finding me in the data |
| **The confirmation hazard log** | ⬇ see below |
| **Traceability** | Every claim answers "which units?" |

### The confirmation hazard log

Every occasion on which I noticed myself feeling **confirmed** by a participant is logged in
`AUDIT_TRAIL.md` the same day, with what was said and what I felt confirmed about.

**Why this is not decoration.** The study asks what happens to a professional's judgment when
something reaches a conclusion that agrees with the one they already held. A researcher hearing a
participant describe exactly the deference his three-link chain predicts **is an instance of the
phenomenon under study, occurring inside the study.**

Unlogged, this arm becomes a demonstration of its own argument rather than an examination of it. That
is not a clever framing — it is the most likely way this study fails, and it fails invisibly.

---

## 5 · What is deliberately not claimed

| Not claimed | Why |
|---|---|
| Generalisability to auditors | Wrong criterion for the design. Transferability is offered instead |
| Frequency of anything | Phenomenology does not license counting |
| Causation | An essence describes; it does not explain |
| That the L2 link is established | This arm describes an experience. It does not test the chain |
| Objectivity | The design makes subjectivity visible rather than pretending it is absent |

---

## 6 · The threats, ranked by how likely they are to sink this

1. **Confirmation.** I want the chain to be right. Controlled by the hazard log, the outsider, and the
   disconfirming pass — and still the largest threat by a distance.
2. **Fluency.** Domain expertise makes the interviews good and the analysis dangerous. I can finish
   participants' sentences and will want to. Controlled by margin-flagging and outsider review.
3. **Recruiting opinion instead of experience.** Controlled by screen criterion 4, which is the whole
   screen.
4. **Saturation declared to fit a deadline.** Controlled by the stopping rule being written in advance
   and requiring the outsider's agreement.
5. **The public repository.** A participant could in principle be identified through detail. Controlled
   by redaction at transcription and by nothing identifiable ever being committed.
