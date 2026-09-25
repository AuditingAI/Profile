# Application packages — Tier 1

**What this is.** For each target role, everything needed to submit, written in advance, so the
act of applying is paste-and-click rather than think-and-write. Tier 1 of
`../AUTOMATION_ROADMAP.md`.

**Target: two minutes per application.** If it takes longer than that, something is missing from
the folder and the folder should be fixed rather than the time absorbed.

## Structure

```
applications/
  COMMON_ANSWERS.md          ← the screening questions every ATS asks. Written once, reused.
  <company>-<role>/
    COVER_LETTER.md          ← paste-ready, names the req
    RESUME_BRIEF.md          ← which bullets to lead with, what to cut, what to rename
    APPLY.md                 ← URL, ATS type, known quirks
```

## Contact details are NOT stored here

This repo is public. Phone number and email appear as `{{PHONE}}` and `{{EMAIL}}` placeholders and
are filled in at paste time. Do not commit real contact details — see the public/private rule in
`../WORKSTREAMS.md`.

## The resume gap

`RESUME_BRIEF.md` tells you how to tailor, not what to send. The tailored resume files live in
Dropbox and could not be reached when these were built (connector toggled off for the session).
Enable the Dropbox connector in chat and the briefs become full resume diffs instead of instructions.

## Rule

A folder that has been here more than **three application windows** without being submitted gets
deleted, not carried. Per the accountability contract in `../WORKSTREAMS.md`, a queue that only
grows is a queue nobody is working.
