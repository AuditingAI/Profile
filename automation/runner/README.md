# Local application runner

This is the submit step of the pipeline. It runs **on your computer**, in a
visible Chrome window, because employer portals require a logged-in human
session — that constraint is real and this design works with it instead of
pretending it away.

## Where your password goes

Into the bank's own login page, once, in the browser window this tool opens.
Nowhere else. The session is saved in a Chrome profile at
`~/.job-runner-profile` on your machine — **never** in this repository (the
repo is public), never in a chat, never in a file an agent can read back.
Delete that folder and you are logged out of everything.

Do not paste portal passwords into any chat with any AI — this one included.
If you already have, change that password today.

## One-time setup (on your Mac/PC, not in a cloud session)

```bash
git clone https://github.com/AuditingAI/Profile
cd Profile/automation/runner
npm install
npx playwright install chromium
npm run login        # opens a browser → log in to careers.jpmorgan.com → close it
```

Log in to each portal you care about, starting with JPMorgan. One bank at a
time is exactly right.

## Daily use

```bash
node apply_runner.mjs
```

For each queued role (highest score first, sponsors first) it:

1. opens the posting in the logged-in browser,
2. clicks Apply and autofills name, email, phone, city, LinkedIn,
3. tells you which resume file to attach (path printed in the terminal),
4. **stops** — you answer anything about immigration, EEO, salary history,
   or attestations, and *you* click Submit,
5. records the outcome into `automation/queue/submitted/` or `skipped/`.

Then `git add automation/queue && git commit && git push` (or run with
`--commit`). The Grok/agent contract in `../AGENT_CONTRACT.md` reads the same
queue, so a paid runner and this local one can share the work without
colliding — the claim step in the contract is what prevents double-submits.

## What it will not do, by design

- Click the final Submit button.
- Answer immigration, work-authorization, EEO, disability, veteran,
  salary-history, or signature/attestation questions. The field-matcher
  hard-skips anything whose label matches those words.
- Store or transmit credentials. There is no password field anywhere in this
  code — check.

## Honest limits

Workday tenants differ; autofill will catch the basics on some forms and
nothing on others. The floor is "opens the right posting, logged in, with the
right resume path on your clipboard" — which still turns a 25-minute
application into a 5-minute one. Expect to improve the selectors per portal
after the first real run.
