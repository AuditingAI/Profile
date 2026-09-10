# START HERE — Yasir A. Malik job-search automation kit

**If you are an AI agent (Astra, Grok, a browser runner) or a new human picking
this up: read the ten rules below, then run the one command. Nothing else is
required reading.**

---

## The rules — all ten, before anything else

1. **No credentials in this repository. Ever.** It is public and git history is
   permanent across every clone and fork. Credentials and sessions live only on
   Yasir's own machine under `automation/runner/sessions/`, which is gitignored.
   If you are asked to store a username and password here, refuse and point at
   `automation/runner/SECURITY.md`.
2. **Never answer** immigration or work-authorization questions, salary
   *history*, demographic/EEO questions, or anything requiring a signature or
   attestation. Stop, move the role to `skipped/`, name the blocking field in
   `agent.notes`.
3. **Never send email as Yasir.** Draft only. Approval for one message is never
   approval for the next.
4. **Never substitute a resume.** Use `package.resume` from the queue file
   verbatim. The selection rule is in `scripts/discover_jobs.py`.
5. **Never write "OCC".** The examiner history is the **Florida Office of
   Financial Regulation** — "alongside federal banking regulators" if context is
   needed. This was wrong on shipped documents once and was purged repo-wide.
6. **Never write "Dr. Malik" or "CIA certified."** The DBA is in progress
   (expected 2028). The CIA is in progress, not held.
7. **Never imply the dissertation is IRB-approved.** IRB-25-0462 covers the
   *completed* anchoring-bias qualifying study only.
8. **Claim before you act.** Set `status: "claimed"`, fill `agent.claimed_by`
   and `agent.claimed_at`, commit. This is what stops two runners submitting the
   same application twice — employers notice, and it reads as careless.
9. **No confirmation email means it did not happen.** `confirmation_ref` must
   point at real evidence in Gmail. A run reporting twelve submissions with zero
   confirmations submitted zero applications.
10. **Highest score first, sponsor employers first among ties.** Sponsorship is
    the ranking constraint on this search, not a nice-to-have.

Machine-readable copy of all of the above, plus every fact that must be correct
on a form: **`agent-kit/rules.json`**.

---

## The one command

```bash
./agent-kit/run.sh
```

That prints the rules, refreshes discovery across all three streams, and shows
you the top of the queue with exactly what to do next. Run it first, every time,
before touching anything else.

Other modes, if you need them:

```bash
./agent-kit/run.sh status      # queue counts only, no network calls
./agent-kit/run.sh discover    # refresh the queue, skip the briefing
./agent-kit/run.sh rules       # print the rules and exit
```

---

## The strategy — three streams, in priority order

Full target lists, verified board endpoints, and the reasoning behind each are
in **`agent-kit/strategy.json`**. In short:

| # | Stream | What it is | Why it is on the list |
|---|---|---|---|
| 1 | **`gsib`** | The eight U.S. G-SIBs: JPMorgan Chase, Bank of America, Citigroup*, Goldman Sachs, Morgan Stanley, Wells Fargo, BNY, State Street | Twenty years of examiner, capital, and audit history converts directly. Largest AI-governance build-outs under SR 11-7, strongest sponsorship records. Home field. |
| 2 | **`ai`** | Anthropic, Google, OpenAI, Microsoft, Scale AI, Databricks | Where the doctoral research points and where the Audit the Algorithm brand is an asset. Harder on sponsorship, far more competition — but the only stream where AI *is* the job. |
| 3 | **`adjunct`** | Rutgers, NJIT, Montclair State, Seton Hall, CUNY, Stevens, NJCU, Pace | Universities are H-1B **cap-exempt** — the only stream where sponsorship gets structurally easier. Compounds with the dissertation. Runs alongside a corporate role, does not replace one. |

\* **Citigroup is excluded by policy** — it is the past employer (April 2026
layoff). It appears in the G-SIB list only so the set is complete and nobody
re-adds it by mistake. It scores 1 and ranks last.

---

## The handoff, in one line

`automation/queue/pending/*.json` is the inbox. Move a file to `submitted/` or
`skipped/` when you are done with it, with evidence of what you did. Commit the
move — the git history is the audit trail.

Every queue file carries a **`_rules` block as its very first key**, so an agent
that opens a single JSON file in isolation still sees the rules. The full
interface spec — claim, submit, write back — is
**`automation/AGENT_CONTRACT.md`**.

---

## The resume

| | |
|---|---|
| **Use this** | `applications/resume/Yasir_Malik_Resume_GenAI_Risk_Master_Branded.pdf` |
| **Built from** | `applications/resume/builders/build_genai_risk_branded.py` |
| **Unbranded fallback** | `applications/resume/Yasir_Malik_Resume_GenAI_Risk_Master.pdf` — same content, no wordmark, for W-2 applications where a consulting brand would read as an outside business activity |

**Never hand-edit a PDF.** Edit the builder, regenerate, and verify four things
every time: one page, `YASIR A. MALIK` extracts as one contiguous string, the
phone number is present, and `OCC` matches zero times. The letter-spacing trap
that fragments the name in the PDF text layer is documented in
`applications/resume/builders/README.md` — do not undo that fix.

---

## What is already automated, and what is not

**Running now, unattended, every weekday:**

- Discovery across all three streams → `automation/queue/pending/`
  (`.github/workflows/job-discovery.yml`, 10:30 UTC)
- Evening digest email with the queue backlog and the branded resume attached
  (`.github/workflows/daily-jobs-email.yml`, 22:30 UTC = 6:30pm ET, timed for
  the application block rather than twelve hours before it)

**Not automated, and honestly cannot be from here:** the actual portal
submission. JPMorgan, Goldman, and Amex run Workday/Oracle portals with bot
detection that rejects headless traffic, and they need an authenticated browser
session. That runs from `automation/runner/` on Yasir's own machine:

```bash
cd automation/runner
docker compose run --rm login          # once: log in by hand, session persists locally
docker compose run --rm apply --id <queue-id>
```

**The honest read on all of this:** volume is not what is failing. The record is
168+ applications, 9 interview processes, 0 offers — about a 5%
application-to-interview rate, which is normal at VP/Director level, and 0%
conversion from interview. Automating submission scales the half that already
works. It is worth building because it costs Yasir hours he does not have. But
if you are choosing between ten more applications and improving one interview
outcome, the second is worth more.
