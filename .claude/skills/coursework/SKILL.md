---
name: coursework
description: Run the DBA coursework track — deadlines, readings, note cards, and class preparation for the FIU DBA. Use when the user asks what is due, what to read, to prep for a class or residency, to log a paper he has read, to recap where a course stands, or uploads a syllabus, assignment brief, or article. Also use when he asks "what do I do today" in a coursework context. Scholar lane only — never touches the industry job search.
---

# Coursework — DBA course management

Keep Yasir honest on what is due, what has actually been read, and what he must walk into a room
already knowing. **He is one person doing a doctorate while job-hunting and running a property
dispute. The scarce resource is his attention, not information.**

## Step 0 — Orient cheaply. Always.

Read these three, in order, and nothing else at first:

1. `dba/coursework/READING_LIBRARY.md` — entry point, reading register, how papers are obtained
2. `dba/coursework/FIU_DBA_ACADEMIC_CALENDAR.md` — **primary-source dates. This governs.**
3. The tracker for the course in question

That is the whole context needed for most requests. **Do not** open every course file, re-read PDFs
already noted, or re-derive dates. If a note card exists, the paper has been read — use the card.

## The token discipline

- **Note cards, not papers.** A paper is read once and reduced to a card. Never re-read a PDF to
  answer a question the card answers.
- **One session at a time.** Never pull readings for a session more than two ahead.
- **Append, don't rewrite.** Trackers gain rows; they are not regenerated.
- **Scanned PDFs:** extract with `pymupdf`; if a page yields zero characters it is an image — render
  to PNG at 140 dpi and read the image. Render only the pages needed.
- **Delegate breadth, not depth.** A subagent for "search everywhere for X" is worth it. A subagent
  to read one known file is not.

## Recapping — the thing that gets hard as this grows

Every substantive session appends one dated block to `dba/coursework/COURSE_LOG.md`:

```
## YYYY-MM-DD · <course or "both">
Decided: …            (things now settled, with the source)
Changed: …            (what moved, and what it superseded)
Open: …               (what is still unresolved, and who resolves it)
Next: …               (the single next action)
```

Newest at top. **To recap, read this file — not the conversation.** It is the memory.

## Source hierarchy — non-negotiable

When sources disagree, this order decides:

1. **Instructor's own email or Canvas announcement** — most recent wins
2. **Canvas assignment table** — auto-generated, carries real configured due dates
3. **FIU DBA published academic calendar** — for residency and term dates
4. **Syllabus PDF**
5. **Syllabus prose schedule** — *demonstrated stale*: GEB 7365's carried Fall 2025 dates into a
   Fall 2026 document

**Never** a briefing, a summary, or an earlier assistant message. That is how a fabricated "23%
anchoring effect" and a wrong residency date both entered this project. When a date cannot be traced
to 1–4, say so and mark it unconfirmed rather than asserting it.

## Standing constraints — carry into everything

- **AI caps are per course and differ.** GEB 7911: ≤25%, disclosure required, violation = automatic
  zero plus possible misconduct referral. GEB 7365 states no cap and points to a Canvas page —
  **do not assume they match.** Check before drafting anything graded.
- **Draft scaffolds and questions, never finished graded prose.** The advisor's standing rule is
  that synthesis, argument and interpretation must be his own. A scaffold that makes him think is
  more useful than a draft he has to disown.
- **Never assert:** a GPA · a DBA completion year other than "expected Summer 2028" (Office of
  Doctoral Programs, 26 Mar 2026) · findings from the AI extension, which is argued not tested ·
  the "23% anchoring effect", which does not exist.
- **Citable and real:** ~20 eligible of 334,976 panel members (~6 per 100,000); four valid responses;
  zero attention-check failures.
- **This repo is public.** No PDFs of licensed articles, no account numbers, no phone numbers, no
  credentials.

## Lane

Scholar only. Coursework, research, academic materials. **Never** industry applications — that is
`/job-search`. If something crosses, write to `career/HANDOFF.md` and say so.

## Common requests

**"What's due / what do I do today"** → Step 0, then the calendar. Output: what is due in the next
7 days, soonest first, with the hours it needs. Name **one** next action. Flag anything whose
deadline collides with travel.

**"Prep me for class"** → the session's readings with a **reading order and a rationale for the
order**, what will be assessed in the room, what to have a position on, and what to ask the
instructor. Papers by the instructor get read first and closely.

**"I read X"** → write the note card to `dba/coursework/_library/`, flip the register to ✅, append
to the log.

**"Here is a syllabus / assignment"** → extract; reconcile against the source hierarchy and **state
every conflict found**; update the tracker; add calendar events; append to the log. Do not silently
pick a date when two sources disagree.

**"Where do I stand"** → read `COURSE_LOG.md`. Report Decided / Open / Next. Do not re-derive.

## Output

Short. Tables for schedules. Bold the thing that will hurt if missed. One next action, named.
No preamble, no restating the question, no reciting what was already established.
