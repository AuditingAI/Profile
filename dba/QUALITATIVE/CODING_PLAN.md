# Coding plan — from transcript to description

Implements steps 2–7 of `PROTOCOL_phenomenology.md` §4. This file exists so the analysis has a
procedure that a reader can follow and a committee can check, rather than a claim that themes
"emerged."

---

## The AI boundary — read first, it governs everything below

| AI **may** | AI **may not** |
|---|---|
| Transcribe audio | Assign a code or a meaning unit |
| Format, reorder, and tabulate what I have already coded | Name a theme or a cluster |
| Check my prose for clarity and grammar | Write any part of the textural or structural description |
| Act as an adversary — "what have I missed, what am I over-reading?" | Decide what a participant meant |
| Find literature | Decide when saturation is reached |

**Four reasons this line is where it is, in ascending order of importance:**

0. **FIU University Graduate School policy**, binding and above the syllabi. It prohibits "using AI
   to generate or re-write substantive portions" of a proposal or dissertation, and requires every
   use to be disclosed and **approved by the committee**. See
   `../00_Execution/FIU_AI_POLICY_2026.md`.
1. Dr. Rey's standing instruction: AI supports brainstorming, organisation, clarity and grammar. The
   synthesis, argument and interpretation must be the researcher's own.
2. GEB 7911 caps AI-created content at 25% and requires labelling what was AI-written.
3. **The topic.** This study examines what happens to professional judgment when a machine reaches a
   conclusion first and the human agrees with it. Letting a model propose themes and then agreeing
   with them would reproduce the phenomenon inside the analysis of the phenomenon. It would not be a
   procedural violation. It would make the finding worthless.

**Recorded compliance:** every use of AI at any analysis step is logged in `AUDIT_TRAIL.md` with
date, tool, what it was asked, and what was done with the output.

---

## Step 2 · Horizontalisation

Every statement bearing on the phenomenon is listed, **flat, unranked, nothing discarded yet.**
"Horizontal" means no statement is treated as more important than another at this stage — the
hierarchy is what the analysis is supposed to discover, not what it starts with.

**Practically:** one row per statement, in the participant's own words, with a locator.

| ID | Participant | Locator | Statement (verbatim) |
|---|---|---|---|
| P03-014 | P03 | 12:40 | "I read it and I thought, good, that's what I had." |

**Done when** re-reading the transcript yields no further statement about the phenomenon.

**The discipline that is hard here:** statements that contradict the chain go in the list exactly as
readily as statements that support it. A horizontalisation that is already filtered is a coded
transcript pretending to be a raw one.

---

## Step 3 · Reduction to meaning units

Delete statements that are **repetitive** or **overlapping**. Delete nothing for being inconvenient.

Each surviving unit is written as a short non-interpretive phrase that stays close to the words used.

| Keep | Reject |
|---|---|
| "Agreement read as permission to move on" | "Participant was anchored" ← my construct, not theirs |
| "Checked less because two sources matched" | "Automation bias observed" ← a finding, not a unit |

**Done when** no two units say the same thing.

---

## Step 4 · Clustering into themes

Group units into clusters. Name each cluster **in language a participant would recognise.**

Rules:
- Every unit sits in exactly one cluster, **or** is explicitly parked in a `NOT YET PLACED` list.
- The parked list is reported. A parked unit is a signal the cluster structure is wrong; quietly
  dropping it is how a tidy finding gets manufactured.
- A cluster supported by a single participant stays a cluster. Frequency is not the criterion in
  phenomenology; being part of the structure is.

**Done when** every unit is placed or parked, and the outsider reviewer can follow every placement.

---

## Step 5 · Textural description — *what*

What participants experienced, written **from the clustered units, with verbatim quotation
throughout.** No inference. If a sentence cannot be traced to units, it does not belong.

**Test:** every claim in the textural description must be answerable with "which units?" If it
cannot, it is interpretation that arrived early.

---

## Step 6 · Structural description — *how and in what context*

Imaginative variation: what conditions, settings and pressures shaped the experience? Deadline
pressure, review hierarchy, tool familiarity, engagement history, firm culture.

Each textural element gets a context attached. This is where the study stops being a list of
sentiments and becomes a description of a situated experience.

---

## Step 7 · Composite / essence

One synthesis: the invariant structure — what the experience *is*, for these participants.

**Two hard limits:**

1. **No causal language.** "Because," "leads to," "results in" do not belong here. An essence
   describes; a variance model explains; this is not a variance model and the reader must not be able
   to mistake it for one.
2. **No frequency claims.** Not "most participants," not "8 of 12." Phenomenology does not license
   counting, and reporting counts is the fastest route to a reviewer dismissing the whole arm.

**If an exception exists, state it.** An essence that holds for eleven of twelve is reported as
holding for eleven, with the twelfth described. A tidy essence purchased by omitting a participant is
the exact failure this programme studies.

---

## The disconfirming pass — run before writing anything up

After step 7 and **before** the description is drafted, deliberately re-read every transcript looking
only for material that contradicts the emerging essence.

The prompts, asked of the data and not of a model:

- Where did someone describe checking **harder** when the system agreed?
- Where did someone describe **no difference** between an AI conclusion and a prior-year workpaper?
- Where did someone describe AI agreement as corroboration they then **tested**?
- What did I hear as deference that could equally be read as ordinary professional efficiency?

Anything found goes into the write-up. `PROTOCOL_phenomenology.md` §6 already states what each of
these would mean for the argument, written before the data existed — which is the only time such a
table can honestly be written.

---

## Tooling

| Task | Tool |
|---|---|
| Transcription | `[VERIFY]` — pending IRB approval of an automated service |
| Coding | Manual. Spreadsheet or plain markdown tables in this repo |
| Storage | Recordings encrypted and outside this repository. **This repo is public** |
| Audit trail | `AUDIT_TRAIL.md`, append-only |

**No transcript, no recording, no participant identifier, and no linking key is ever committed to
this repository.** Only de-identified, quotable extracts approved at member check, and only once the
write-up requires them.
