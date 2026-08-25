# Job application pipeline

Four stages. Three of them run here on a schedule. The fourth is a documented
handoff to an external agent, because it needs a logged-in browser.

```
  ┌─────────────┐   ┌──────────────┐   ┌──────────────┐   ┌─────────────┐
  │  DISCOVER   │──▶│    QUEUE     │──▶│    SUBMIT    │──▶│  RECONCILE  │
  │  automated  │   │  automated   │   │  external    │   │  automated  │
  └─────────────┘   └──────────────┘   └──────────────┘   └─────────────┘
   Greenhouse        JSON per role      Grok / browser     Gmail confirms
   Workday           committed here     agent, logged in   → status update
   Google Careers    scored + deduped   as Yasir
```

## Stage 1 — Discover (automated, here)

`scripts/discover_jobs.py`. Runs Greenhouse, Workday, and Google Careers
fetchers from `scripts/jobs_sources.py`, scores each role, drops anything
below score 3, drops Citi (former employer), drops anything already seen.

A source that breaks reports `FAILED` in the run output rather than returning
nothing quietly. A dead source that says nothing looks exactly like a quiet
job market, which is the failure mode that wasted the most time here.

```bash
python scripts/discover_jobs.py --dry-run   # see what it would queue
python scripts/discover_jobs.py             # write the queue
```

## Stage 2 — Queue (automated, here)

`automation/queue/pending/` — one JSON file per role, committed to GitHub.
Each carries a score, a sponsorship flag, and the resume file to use.
`automation/queue/seen.json` is the dedupe ledger.

Runs weekday mornings via `.github/workflows/job-discovery.yml`, which commits
new entries back to the branch. GitHub is the shared state — that is what
makes it readable by an agent that is not this session.

## Stage 3 — Submit (external — this is the placeholder)

**Not automated here, and cannot be.** Bank careers portals require an
authenticated browser session and several reject headless traffic outright.

The interface is specified in **`AGENT_CONTRACT.md`**: read `pending/`, claim
a file, submit, move it to `submitted/` or `skipped/` with evidence, commit.

Any runner that honours that contract works — Grok with browser access, a
Playwright script with a persisted profile, or a person working the queue by
hand. The queue does not care which.

## Stage 4 — Reconcile (automated, here)

`scripts/daily_jobs_email.py` already sends the morning digest. Employer
confirmation emails arriving in Gmail are the only real proof a submission
landed; a run claiming twelve submissions with zero confirmations did not
submit twelve applications.

## Setup still required

The digest workflow needs two repository secrets, which only the repo owner
can set (`Settings → Secrets and variables → Actions`):

- `GMAIL_ADDRESS`
- `GMAIL_APP_PASS` — a Google app password, not the account password

Until those exist the workflow runs and fails silently. That is currently the
case.

## What this does not do

- It does not send email as Yasir. Drafts only.
- It does not answer immigration, salary-history, or EEO questions on a form.
- It does not decide that a role is worth applying to at score 1–2; those are
  dropped rather than queued.
