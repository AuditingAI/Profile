# Where credentials live, and why not in GitHub

## The short version

Your passwords are typed into the employer's own login page, in a browser
window on your own computer, once per portal. The resulting session cookie is
stored in `automation/runner/sessions/` on your disk. It is not in this
repository, not in the Docker image, not in any chat, and not recoverable by
any agent reading this repo.

## Why credentials are not stored in GitHub, even privately

This was asked for directly, and the answer is no. Four reasons, in order of
how badly each one ends:

1. **This repository is public.** `AGENTS.md` states it as safeguard 1:
   there is no private directory and nothing is protected by being unlinked.
2. **Git history is permanent.** Committing a secret and deleting it in the
   next commit does not remove it — it stays in the object store, in every
   clone, in every fork, and in the reflog. Removal requires rewriting
   history on every copy that exists, and you cannot reach the forks.
3. **Bank portals are not low-value targets.** Several employers front their
   careers portal with the same identity provider as internal systems. A
   leaked credential there is a fraud and identity-theft exposure, not an
   inconvenience.
4. **Your own control says no.** `AGENTS.md` safeguard 3: "Never commit
   secrets or personal records. No credentials, tokens, API keys, `.env`
   files." An agent that breaks the control it was told to enforce is worth
   less than no agent.

The design below gets the same result — a runner that logs in and applies —
without any of that exposure.

## How it actually works

```
  YOUR MACHINE                          GITHUB
  ────────────                          ──────
  sessions/browser-profile/    ✗───✗    (gitignored, never pushed)
    └ login cookies                     automation/queue/*.json  ← the work
    └ typed once, by you                automation/runner/*      ← the code
         │                              applications/resume/*    ← the PDFs
         ▼
  Docker container ──reads queue──▶ opens posting, already signed in
                   ──fills form───▶ stops before Submit
```

The container is disposable. The volume is not. That split is the whole
security model: code and work are shareable and versioned, sessions are
local and ephemeral.

## Protections in place, and how each was verified

| Protection | Mechanism | Verified |
|---|---|---|
| Sessions cannot be committed | `.gitignore` rules on `sessions/`, `*.env`, `**/cookies.json`, `**/storage-state.json` | A test `storage-state.json` was written into `sessions/` and `git status` did not see it; `git check-ignore` confirmed the matching rule |
| Sessions cannot enter an image | `.dockerignore` excludes `sessions/`, plus `*credential*`, `*secret*`, `*.pem`, `*.key` | Build context excludes the directory |
| Image cannot persist them | `VOLUME ["/sessions"]` in the Dockerfile | Docker refuses to commit volume contents into a layer |
| Runner holds no password logic | No password field, no credential parameter, no keystore call anywhere in `apply_runner.mjs` | `grep -i password` returns only the comment explaining this |
| Repo is read-only to the runner | `../../:/repo:ro` bind mount | Container cannot modify your working tree |
| Not running as root | `USER pwuser` | Files on the mounted volume are owned by you, not root |

## On automatic account creation

The runner does not create accounts, and this is deliberate rather than
unfinished.

Registering an account means accepting terms of service and, on most
employer portals, attesting that the information submitted is true and
submitted by the applicant. That is a legal act. An agent cannot make an
attestation on your behalf — not because the automation is hard, but because
the attestation would be false the moment a machine made it, and a
recruiter's first question on discovering it would be whether anything else
in the application was machine-asserted.

Registration is roughly ninety seconds per employer, once, forever. The
runner opens the registration page for you and waits. You fill it in. From
then on the session persists and the runner uses it indefinitely.

The same reasoning governs what the runner refuses to autofill during an
application: immigration status, work authorisation, EEO and demographic
questions, salary history, criminal history, and any signature or
attestation field. `apply_runner.mjs` hard-skips any field whose label
matches those, and the runner always stops before the final Submit.

## If a credential is ever exposed

1. Change that portal's password immediately, from the employer's site.
2. `rm -rf automation/runner/sessions/` — invalidates every stored session.
3. If it reached git: assume it is compromised regardless of history
   rewriting, and rotate rather than scrub.
