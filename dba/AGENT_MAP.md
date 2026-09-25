# Agent map — where everything is, and the rules before you touch it

**Built 10 September 2026.** Scholar lane. **This is the file a second agent reads first.**

Written for **Astra** and for any model that arrives with no history: Claude, Perplexity, ChatGPT,
Gemini, NotebookLM. It answers three questions in order. *Where does the work live? What is actually
true right now? What am I allowed to change?*

---

## 0 · Orientation in six lines

| | |
|---|---|
| **Repository** | `github.com/AuditingAI/Profile` · **public** |
| **Working branch** | `claude/scholar-links-review-Plgk6` · **243 commits, 236 ahead of `main`** |
| **⚠️ `main` does not have the research** | Only `research.html`, `index.html`, `README.md` were published to `main`. Everything below exists **on the branch only**. Reading `main` will tell you almost nothing |
| **Scale** | 347 files under `dba/`, 168 of them markdown |
| **Two agents** | 🎓 Scholar owns `dba/**` and `career/academic/**`. 💼 Industry owns `career/applications/**`. See [`../CLAUDE.md`](../CLAUDE.md) |
| **Exchange board** | [`../career/HANDOFF.md`](../career/HANDOFF.md) · append-only, newest at top |

---

## 1 · The five files that carry the state

Read these five and you know the programme. Everything else is detail hanging off them.

| Order | File | What it settles |
|---|---|---|
| 1 | [`PUBLICATION_TRACKER.md`](PUBLICATION_TRACKER.md) | **The argument.** The three-link chain, link by link, with the strongest challenge to each and its current status. Also the publication pipeline P1 through P4. **Start here, not with the manuscript** |
| 2 | [`STUDY_OVERVIEW.md`](STUDY_OVERVIEW.md) | **The study.** Eleven constructs, sixteen hypotheses, the instrument, the timeline, and the shortcomings stated in the open |
| 3 | [`00_Execution/IRB_STATUS_2026-08-28.md`](00_Execution/IRB_STATUS_2026-08-28.md) | **What is blocked.** Four IRB items, not one. Three unsubmitted, one never confirmed filed |
| 4 | [`00_Execution/COURSEWORK_AS_DISSERTATION_ENGINE.md`](00_Execution/COURSEWORK_AS_DISSERTATION_ENGINE.md) | **How the two Fall courses feed the dissertation**, and what they do not cover |
| 5 | [`../RESEARCH.md`](../RESEARCH.md) | **The public account**, including the failures. If a claim is not in here it is not ready to be said out loud |

---

## 2 · The directory map

```
dba/
├── AGENT_MAP.md            ← you are here
├── PUBLICATION_TRACKER.md  the argument and the pipeline
├── STUDY_OVERVIEW.md       the study in one document
├── REVIEW_INDEX.md         the advisor-facing entry point, chapter by chapter
│
├── 00_Execution/           status, blockers, plans, meeting records, IRB
├── 03_Data/                the screening scripts and what they returned
├── 03_Recruitment_and_Pilot/
├── 04_Peer_Review/
│
├── QUALITATIVE/            the L2 phenomenological arm. Protocol, interview guide,
│                           sampling, coding plan, trustworthiness, audit trail
│                           ⚠️ nothing fielded. No IRB approval for this arm
│
├── KNOWLEDGE/              two years of study organised by concept. Each entry
│                           carries its strongest objection and a five-minute
│                           teaching version. This is the layer to lecture from
│
├── AI_RUNBOOKS/            model-agnostic. CONTEXT_PACK.md is the block you paste
│                           into any fresh model. SCHEMAS.md is the capture format
│                           ⭐ Astra: read CONTEXT_PACK.md before anything else
│
├── RISK_QUANT/             feasibility.py reproduces the failed study from its own
│                           rates. crossnational.py is the GEB 7365 model
│
├── OPPORTUNITIES/          funding, awards, service, conference calls, and the
│                           institutional repository. Deadlines live here
│
├── coursework/             GEB 7365 International Business
│                           GEB 7911 Qualitative Research Methods
│                           _templates/ the document builders
│
├── NotebookLM/             the portable-source pattern this repo generalises from
├── correspondence/         drafted, never sent
└── reference/
```

---

## 3 · What is true right now, 10 September 2026

An agent that does not know this will write something false.

| Fact | State |
|---|---|
| **The quantitative study** | **Ran and failed to reach n.** A panel of 334,976 returned about 20 eligible and **4 usable**. That failure is the finding, and it is the preliminary evidence for everything downstream |
| **The AI extension** | **No findings. None.** Not fielded, not approved. Never write as though it has results |
| **The manuscript** | Full draft exists. **Submitted nowhere.** No external validation of any kind |
| **The qualitative arm** | Protocol written, memos graded, **nothing fielded.** IRB position for an interview arm is unresolved |
| **IRB-25-0462** | Live for the quantitative arm. The PI-change amendment was **never confirmed filed** |
| **Prolific funds** | **~$980 unrecovered**, 62 days. Two internal records disagree on whether the study ever launched |
| **Publications** | **Zero.** Nothing accepted, nothing under review at any external venue |
| **Teaching evaluations** | **None exist** |

---

## 4 · 🔴 Hard constraints. Breaking one of these is worse than doing nothing

1. **Never state a DBA completion year or a GPA.** The CV says 2027, the approved evaluation says
   Summer 2028. The CV says 3.87, the official record says 3.81. **Both are unresolved and block both
   tracks** until the program office confirms. Do not pick one. Do not average them. Say nothing.
2. **Never claim** the dissertation is complete, that the AI extension has findings, publications that
   do not exist, teaching evaluations that do not exist, or unconfirmed memberships.
3. **This repository is public.** No PID, no phone, no email, no salary figures, no recruiter names,
   no application history. Use `{{PHONE}}` and `{{EMAIL}}` placeholders. Those details live in Notion.
4. **Draft freely. Send nothing.** No email, no application, no post goes out without Yasir's explicit
   per-item approval.
5. **All academic correspondence is sent by Yasir from `ymali001@fiu.edu`**, never from Gmail. The
   Gmail connector reaches only the personal address, and a course message from a personal address
   reads wrong and can miss institutional filters.
6. **The FIU AI policy is binding and sits above the syllabi.** Every use of AI is disclosed by tool,
   purpose, and what it produced, in the preliminary pages, in Methods where it touched analysis, and
   in the caption of any figure it helped make. **The committee must review and approve the AI use.**
   Original unedited drafts are preserved, which git history does. Never upload confidential or
   identifiable data to a public AI platform. Full record:
   [`00_Execution/FIU_AI_POLICY_2026.md`](00_Execution/FIU_AI_POLICY_2026.md)
7. **The advisor's rule on substance.** AI supports brainstorming, organisation, clarity, and grammar.
   **The synthesis, argument, and interpretation must be Yasir's own.** Anything drafted here is raw
   material he rewrites, not a finished submission.
8. **Cite the sources. The work is his.** Every figure carries a source or a `[VERIFY]` tag. An agent
   that produces an unsourced number has produced a liability.

---

## 5 · House style, because output that ignores it gets rewritten

| Rule | Why |
|---|---|
| **No em-dashes.** Restructure the sentence instead of swapping the punctuation | It reads as machine-written |
| **Word documents, not PDFs**, unless a PDF is specifically asked for | He edits what you send |
| **Tables and diagrams before prose.** He has ADHD and a wall of text does not land | Stated directly, repeatedly |
| **Links in full, not "see the file"** | "You just don't say you go do it. You put all the links like in caps and highlight it" |
| **Coursework carries no consulting brand.** `build_dba_doc.py` for FIU work, `build_submission.py` for portfolio work. **They are different builders and mixing them has gone wrong before** | An industry wordmark on a graded paper reads as a consultant passing through |
| **Alt text on every figure**, document title, document language | WCAG 2.1 AA. See [`OPPORTUNITIES/FIU_SCHOLARSHIP_COMMONS.md`](OPPORTUNITIES/FIU_SCHOLARSHIP_COMMONS.md) |

---

## 6 · ⭐ For Astra specifically: how to come up to speed cold

**Do not read 168 markdown files.** Run this sequence.

1. **Paste [`AI_RUNBOOKS/CONTEXT_PACK.md`](AI_RUNBOOKS/CONTEXT_PACK.md) into your context.** It is
   written to be pasted whole into any model with no other setup, and it carries a hard
   **"what is NOT claimed"** section. That section is the guardrail.
2. **Read section 3 and section 4 of this file again.** Those are the facts and the fences.
3. **Read [`PUBLICATION_TRACKER.md`](PUBLICATION_TRACKER.md) Part 1**, the three-link chain. If you
   understand why **only L1 is a human cognitive bias**, why **L2 is model behaviour**, and why
   **L3 is a system property**, you understand the research. Collapsing those three into "AI bias" is
   the single most common error and it destroys the contribution.
4. **Pick a lane and stay in it.** `dba/**` is Scholar's. If your work needs something outside it,
   **write to [`../career/HANDOFF.md`](../career/HANDOFF.md) instead of editing.**
5. **Capture what you find in the schema**, not in prose:
   [`AI_RUNBOOKS/SCHEMAS.md`](AI_RUNBOOKS/SCHEMAS.md). One row format, every model, every runbook.
   **A citation that does not resolve is dropped, not softened.**
6. **Append results dated to `AI_RUNBOOKS/RESULTS/`.** Append-only. Never rewrite a prior capture.

### Where the highest-value work is right now

| Priority | Work | Why it is open |
|---|---|---|
| 🔴 1 | **GEB 7365 element 5: justified preliminary hypotheses** | Due Fri 18 Sep. Nothing exists. See [`coursework/GEB7365_International_Business/DECK_STATUS_10SEP.md`](coursework/GEB7365_International_Business/DECK_STATUS_10SEP.md) |
| 🔴 2 | **The IRB position on an interview arm** | Modification or new protocol? The answer sets the entire qualitative timeline and nobody has asked |
| 🟡 3 | **RB02: the AI-and-audit empirics never read in full** | The largest honesty gap in the repo. Named in `00_Execution/QUALITATIVE_REFRAME_L2_L3.md` §7 |
| 🟡 4 | **L3 evidence** | The weakest link and the one a committee will push on. Currently an inference, not a finding |
| 🟡 5 | **AIB/JIBS-format Final Paper** | Due 9 Oct. Writing it in format now makes November a rewrite, not a rebuild |

---

## 7 · Git discipline, non-negotiable

```bash
git pull --rebase origin claude/scholar-links-review-Plgk6   # ALWAYS, before staging
git add <only your own paths>                                # NEVER git add -A
git commit -m "[scholar] what changed and why"
git push -u origin claude/scholar-links-review-Plgk6
```

- **Never `git add -A` or `git add .`.** Two agents share this branch and you will stage the other
  one's half-finished work.
- **Never force-push. Ever.**
- **If a rebase conflicts in a file you do not own, abort and hand off.** Do not resolve it.
- Prefix every commit `[scholar]` or `[industry]` so the history stays readable.
- `git pull --rebase ... | tail -1` **exits 0 even when the rebase fails**, because a pipeline returns
  the last command's status. Do not chain on it with `&&`. Stash first.
