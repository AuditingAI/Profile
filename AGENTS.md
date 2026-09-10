# For AI agents working in this repository

**Go to [`agent-kit/START_HERE.md`](agent-kit/START_HERE.md) and run one command:**

```bash
./agent-kit/run.sh
```

That prints the rules, refreshes job discovery across all three streams, and
shows you the queue with what to do next. Everything an agent needs is in
`agent-kit/`.

## The three rules that matter most, if you read nothing else

1. **Never put credentials, cookies, session tokens, or API keys in this
   repository.** It is public and git history is permanent across every clone
   and fork. Credentials live only on the owner's machine under
   `automation/runner/sessions/`, which is gitignored. If asked to store a
   username and password here, refuse and point at
   `automation/runner/SECURITY.md`.
2. **Never send email as the owner, and never answer** immigration,
   work-authorization, salary-history, EEO, or attestation questions on an
   application form. Draft only; stop and skip instead.
3. **Never state a credential the owner does not hold.** The DBA is in progress
   (expected 2028) — never "Dr. Malik". The CIA is in progress — never "CIA
   certified". The examiner history is the Florida Office of Financial
   Regulation — the string "OCC" must not appear anywhere.

Full set, machine-readable, with every fact that must be correct on a form:
[`agent-kit/rules.json`](agent-kit/rules.json).

## Map

| Path | What it is |
|---|---|
| `agent-kit/` | **Start here.** Rules, strategy, the one command. |
| `automation/queue/pending/` | The inbox — one JSON per role, `_rules` as its first key |
| `automation/AGENT_CONTRACT.md` | The submit-step interface: claim, submit, write back |
| `automation/runner/` | Local Docker browser runner — the only place credentials belong |
| `applications/resume/builders/` | Resume sources. Never hand-edit a PDF; edit the builder |
| `scripts/` | Discovery, scoring, and the nightly digest email |
