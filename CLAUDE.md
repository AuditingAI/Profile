# Two agents, one repository

This repo is worked by **two Claude Code sessions at once**. Read this before touching anything.

| Agent | Owns | Never touches |
|---|---|---|
| 🎓 **SCHOLAR** | The doctorate: research, publications, and academic/faculty jobs | Industry applications |
| 💼 **INDUSTRY** | Corporate roles: AI governance, model risk, audit leadership in banks and firms | Research files, academic materials |

**Identify yourself first.** If you do not already know which one you are, ask the user before
writing anything. Guessing and editing the wrong lane is the failure mode this file exists to
prevent.

---

## Path ownership — do not write outside your lane

### 🎓 SCHOLAR owns
```
dba/**                        research, manuscripts, publication tracker, NotebookLM sources
career/academic/**            research statement, academic job strategy, teaching statement
scholar-*.md                  reading lists, alert triage
.claude/skills/research/
.claude/skills/academic-jobs/
```

### 💼 INDUSTRY owns
```
career/applications/**        cover letters, screening answers, ATS runbooks, package PDFs
career/AUTOMATION_ROADMAP.md
.claude/skills/job-search/
```

### Shared — coordinate before editing
```
CLAUDE.md                     this file
career/HANDOFF.md             the exchange board — append-only, see below
career/WORKSTREAMS.md         the four-track charter
career/ACADEMIC_CV_YMalik.md  Scholar owns content; Industry may read
career/WEBSITE_CONTENT_KIT.md
.claude/skills/portfolio/
live.html                     the public register — either may update, always pull first
```

**If you need something changed outside your lane, do not change it.** Write an entry in
`career/HANDOFF.md` and say so in your reply to the user.

---

## Git discipline — this is not optional

Both agents push to the same branch. Every commit:

```bash
git pull --rebase origin <branch>    # ALWAYS, before you stage anything
git add <only your own paths>
git commit
git push -u origin <branch>
```

- **Never `git add -A` or `git add .`** — you will stage the other agent's in-progress work.
- **Never force-push.** Ever.
- If a rebase conflicts in a file you do not own, **abort and hand off**. Do not resolve it.
- Prefix commits with your lane so history is readable: `[scholar]` or `[industry]`.

---

## What legitimately crosses between the two

Separation is about **voice and documents**, not about facts. These five things are shared reality
and each agent must read the other's state before advising:

1. **Publication status.** Scholar owns `dba/PUBLICATION_TRACKER.md`. "Manuscript under review"
   is a credential in an industry cover letter and a gating requirement in an academic
   application. Industry: read it, cite it, never edit it.
2. **Interview and offer stage.** Industry owns this. A live offer changes how urgently the
   academic track should move — and vice versa. Post stage changes to HANDOFF.
3. **CV verification items.** The DBA completion year (2027 on the CV vs Summer 2028 on the
   approved evaluation) and GPA (3.81 vs 3.87) are **unresolved and block both tracks**. Neither
   agent asserts either figure anywhere until the program office confirms. This is the single
   most important shared constraint in the repo.
4. **Geography and compensation floor.** Newark 07107, wide commute radius, $180K+ industry floor.
   In `career/WORKSTREAMS.md`.
5. **Research substance.** The AI-governance argument in `dba/PUBLICATION_TRACKER.md` is what makes
   an industry cover letter distinctive. Industry may quote it; the argument stays Scholar's.

## What must never cross

- **Documents.** The academic CV and the industry resume never appear in the same message,
  application, or email. An industry recruiter reading the academic CV sees "leaving for academia";
  a department chair reading the industry resume sees "consultant passing through."
- **Voice.** Academic materials argue a research contribution. Industry materials argue business
  impact. Do not let one drift into the other.
- **Digests.** `/job-search` and `/academic-jobs` output separately, always.

---

## The exchange board

`career/HANDOFF.md` is how the two agents talk. **Append-only, newest at top, always dated and
signed with your lane.** Post when:

- something in the other agent's lane needs to change
- a shared fact changes (publication status, interview stage, a CV item resolved)
- you were blocked by something the other agent owns

Read it at the start of every session. It is the only place the other agent's state is visible to you.

---

## Standing facts both agents must respect

- **Never state a DBA completion year or GPA** until the program office confirms them. See §3 above.
- **Never claim** the dissertation is complete, that the AI extension has findings, publications
  that do not exist, teaching evaluations that do not exist, or professional memberships that are
  unconfirmed.
- **This repository is public.** Contact details, salary figures, recruiter names, and application
  history live in Notion, never here. Use `{{PHONE}}` / `{{EMAIL}}` placeholders in any document
  that would otherwise carry them.
- **American Express is suppressed** in the industry track — six declines between 27 June and
  3 August — unless a named recruiter makes contact.
- **AI-use rule from the advisor:** AI supports brainstorming, organisation, clarity, and grammar.
  The synthesis, argument, and interpretation must be Yasir's own. Anything either agent drafts is
  raw material he rewrites, not a finished submission.
- **All academic correspondence is sent by Yasir from `ymali001@fiu.edu`, never from Gmail.** Anything
  going to a professor, the program office, FIU administration, or a classmate is drafted here and
  sent from the FIU mailbox — the Gmail connector reaches only `yasiramalik@gmail.com`, and a course
  message arriving from a personal address reads wrong and can miss institutional filters. Industry
  correspondence follows its own lane's channel.
- **Draft freely. Send nothing** — no email, no application, no post — without his explicit
  per-item approval.
