# Agent contract — the submit step

This is the interface an external agent (Grok, a browser-automation runner, or
a human) implements to take a role from *discovered* to *submitted*.

Everything before this point is already automated and running in this repo.
Everything after this point needs a browser session that is logged in as Yasir,
which is why it lives outside.

---

## The handoff, in one line

`automation/queue/pending/*.json` is the inbox. Move a file to `submitted/`
or `skipped/` when you are done with it, with evidence of what you did.

---

## 1. Read the queue

Every pending role is one JSON file in `automation/queue/pending/`:

```json
{
  "id": "a3f9c1d8e2b40567",
  "discovered_at": "2026-08-21T18:00:00Z",
  "stream": "corporate",
  "company": "JPMorgan Chase",
  "title": "Internal Audit Manager, Vice President - CIB Finance",
  "location": "Jersey City, NJ",
  "url": "https://jpmc.wd1.myworkdayjobs.com/External/job/...",
  "score": 5,
  "score_reasons": ["ai governance", "vp level", "in market"],
  "sponsor_employer": true,
  "status": "pending",
  "package": {
    "resume": "applications/resume/Yasir_Malik_Resume_JPM_CIB_Finance_Audit.pdf",
    "cover_letter": null
  },
  "agent": {
    "claimed_by": null,
    "claimed_at": null,
    "submitted_at": null,
    "confirmation_ref": null,
    "notes": null
  }
}
```

Work highest `score` first, and among equal scores prefer
`sponsor_employer: true`. Sponsorship is the ranking constraint on this
search, not a nice-to-have.

## 2. Claim before you act

Set `status` to `claimed` and fill `agent.claimed_by` / `agent.claimed_at`,
then commit. This is what stops two runners submitting the same application
twice — which employers notice, and which reads as careless.

## 3. Submit

Use `package.resume` — the path is relative to the repo root and the file is
committed here. Do not substitute a different resume; the selection rule is in
`scripts/discover_jobs.py` and exists so the document matches the role.

**Facts that must be correct on every form.** These have each been wrong on a
shipped document at least once:

| Field | Correct value |
|---|---|
| Phone | +1 (786) 704-8536 (the 305 number is retired) |
| Email | YasirAMalik@gmail.com |
| Location | Newark, NJ |
| Current employer | None — Citi role ended April 2026 (layoff) |
| Degree in progress | DBA, Florida International University, expected 2028 |
| Certifications | FDIC Bank Examiner I. **CIA is in progress, not held.** |
| Examiner history | Florida Office of Financial Regulation |

**Never answer these; leave them for Yasir.** Immigration and work
authorization questions, salary *history* (as opposed to expectation),
demographic/EEO questions, and anything requiring a signature or attestation.
If a form blocks on one of these, stop and move the file to `skipped/` with
`agent.notes` saying which field blocked it.

## 4. Write back

On success, move the file to `automation/queue/submitted/` with:

```json
"status": "submitted",
"agent": {
  "claimed_by": "grok-runner-1",
  "claimed_at": "2026-08-22T14:02:11Z",
  "submitted_at": "2026-08-22T14:06:48Z",
  "confirmation_ref": "Req 210759059 - confirmation email received",
  "notes": "Workday profile already existed; used saved profile."
}
```

On anything else, move it to `automation/queue/skipped/` with `status` set to
`skipped` or `failed` and `agent.notes` explaining why in one sentence. A
skipped role with a reason is useful. A silently dropped one is not.

Commit the move. The git history is the audit trail.

## 5. What confirms it actually worked

Employer confirmation emails land in Gmail and are the only real evidence a
submission went through. `confirmation_ref` should point at one. A run that
reports twelve submissions and produces zero confirmation emails did not
submit twelve applications.

---

## Hard limits — read before promising this works end to end

**Portal submission cannot be done from this repo.** JPMorgan, Goldman, and
Amex run Workday/Oracle portals that require an authenticated browser session,
and several use bot detection that rejects headless traffic. That is why the
handoff exists. It is a real constraint, not an unfinished feature.

**Volume is not the bottleneck on this search.** The record so far: 168+
applications, 9 interview processes, 0 offers. Roughly a 5% application-to-
interview rate, which is normal at VP/Director level, and 0% conversion from
interview. Automating submissions scales the half that already works. It is
worth building because it costs Yasir's time to do by hand — but it is not
what is failing.

**Nothing sends mail as Yasir.** Drafts only. Approval for one message is
never approval for the next.
