---
name: reading
description: Log a paper he has read, write its note card, and keep the reading register current. Use when he says he read or skimmed an article, pastes a citation or PDF, asks what a paper argues, asks what to read next, or says "log this", "note card", "what's left to read". Scholar lane, both DBA courses.
---

# Reading — capture it once, use it four times

A paper read and not carded is an unread paper. The card serves class participation, the module
write-up, the proposal, and the literature chapter — written once.

## Step 0 — orient

`dba/coursework/READINGS.md` (the index, both courses), `READING_QUEUE.md` (what is next),
`HOW_TO_READ.md` (the protocol). Nothing else unless the question demands it.

## The card — the only format

Write to `dba/coursework/_library/NOTES_<year>_<firstauthor>_<shorttitle>.md`:

```
# Author (Year) — Short Title
Journal vol(issue): pages · Course/session · Read: YYYY-MM-DD

Claim.          One sentence.
Contribution.   What it added that was not there.
Leaves open.    The gap it names, or the one it walks past.
Use.            Which assignment, which argument.
Quote.          One citable line, with page number.
```

**"Unclear" is a valid entry.** A blank card is an unread paper; an honest "unclear" is a finding.

## When he asks what to read next

One paper. Not a list. Give the session it is for, the one question to answer while reading, and the
time it takes. Then stop.

## When he pastes a paper

Extract citation, place it in the index if missing, and offer the card — **prompted, not written for
him** unless he asks outright. He engages with the material by writing the card; that is the point
of it.

For scanned PDFs: `pymupdf` text extraction first; zero characters means it is an image, so render
to PNG at 140 dpi and read the pages needed. Never render the whole file.

## Chart column

Every reading in the index carries the visual form that fits its argument. When a card is written,
say in one line what the paper would look like drawn. If he wants it built, hand to `/chartit`.

## Guardrails

- **Never characterise a paper he has not read as though it were verified.** Say plainly when a
  summary comes from general knowledge rather than the PDF, and mark it in the card
- Never invent a page number, a finding, or a quote
- Licensed PDFs never enter this public repository — cards only
