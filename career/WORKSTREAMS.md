# Workstream Charter — four tracks, one operating system

**Purpose:** Yasir runs four things at once that compete for the same hours. This file is the contract
that keeps them from colliding: what each track is, what "done this week" means, where its data lives,
and which automation owns it.

**Public/private rule (applies to every track):** mechanics live here in git; identity, contacts,
comp figures, application history, and anything a stranger could use to impersonate or profile him
live in Notion. No exception, no "just this once." If a file in this repo needs a name, a salary, or
a recruiter's email to be useful, it is the wrong file.

---

## The four tracks

| # | Track | Outcome that ends it | Cadence | Skill | Private store |
|---|---|---|---|---|---|
| 1 | **Industry roles** — AI governance / model risk / audit leadership | Signed offer, NY/NJ metro or remote | Daily | `/job-search` | 🔒 Job Search Profile + Weekly Status Log |
| 2 | **Academic track** — teaching appointment | Adjunct or lecturer contract, FIU or Rutgers | Weekly | `/job-search` (academic lane) | Academic CV confirmations |
| 3 | **Research** — DBA dissertation | Approved proposal → defense | Weekly sweep, daily inbox | `/research` | Scholar alerts, advisor correspondence |
| 4 | **Practice** — Audit the Algorithm advisory | First paid engagement | Monthly | — | Client conversations |

Tracks 1 and 2 use **different resumes and are never mixed in one message.** An industry recruiter
who sees the academic CV reads "leaving for academia." A department chair who sees the industry
resume reads "consultant passing through." Two profiles, two voices, permanently separate.

---

## Geography (tracks 1 and 2)

Home base **Newark, NJ 07107**. Motorcycle — commute radius is wide and traffic-tolerant, so the
search should not be pinned to Newark itself.

**In scope, in priority order:**
1. **Jersey City / Downtown NYC** — where the AI-governance and model-risk roles actually are
   (JPMorganChase, BNY, Amex, State Street, MUFG). 20–35 min from 07107.
2. **Manhattan midtown / Harrison NY / Whippany–Parsippany NJ** — second ring, still routine.
3. **Fully remote** — no geographic constraint.
4. **Miami / FIU** — track 2 only, and only if hybrid or fully online.

**Out of scope:** anything requiring relocation, and Newark-proper-only searches — that lane is
thin and off-target (verified 2026-08-03: `risk management director` and `internal audit director`
in Newark returned almost entirely finance-ops and HR roles, nothing in lane).

---

## What each source is actually good for

Measured over ten runs, not assumed:

| Source | Verdict |
|---|---|
| **LinkedIn job alerts (Gmail)** | Carries the entire AI-governance / model-risk lane. Primary source. |
| **Indeed API** | Returned **zero** for `model risk management director` eight consecutive days while LinkedIn delivered three such roles. Keep as a wide net for adjacent risk/GRC titles; do not rely on it in lane. |
| **Recruiter DMs** | Highest value per item, lowest volume. Zero for three consecutive runs. When one arrives it outranks everything. |
| **Indeed for teaching** | Useless. Academic hiring runs through institutional portals, HigherEdJobs, and faculty referral. Do not search it here. |
| **Institutional portals** | The only real channel for track 2 — `search.careers.fiu.edu`, Rutgers Newark. Must be checked by hand. |

---

## The accountability contract

The failure mode in this system is **not discovery**. Ten runs have surfaced good roles every time.
The failure mode is the **send step** — the one action that requires a human.

Evidence, 2026-08-03: an American Express Audit Director follow-up sat unsent for **17 days** across
eight consecutive morning briefings, each of which correctly flagged it. A recruiter who requested a
resume on Jul 21 went 13 days without one and aged out of the pipeline. Two score-5 roles have been
recommended four times each without an application.

So the contract is written against that specific failure:

1. **Every digest ends with exactly one action**, not a list. Lists get deferred; single actions get done.
2. **Anything unsent after 48 hours gets escalated in the digest headline**, not buried in "open loops."
3. **Anything unsent after 7 days is declared dead** and either re-opened deliberately or dropped.
   Carrying a stale item forward for two weeks is not follow-through; it is a way of feeling busy.
4. **Calendar blocks are the enforcement layer** — a recurring window that exists to do the send,
   not to plan the send.

---

## Automation boundary — what is and is not possible

**Automated today:** alert harvesting, live search, scoring, dedupe, package matching, digest
assembly, draft generation, calendar scheduling, Notion logging, scheduled recurrence.

**Not automated:** the submission itself. Applying through Workday/Taleo/Greenhouse means signing
in as Yasir and asserting things on his behalf. That requires his credentials, and it is an
irreversible outward-facing act. See `AUTOMATION_ROADMAP.md` for what closing that gap would
actually take and what it would cost.

The honest framing: this system can reduce the human step from *"research and write an application"*
to *"read a finished draft and click send."* It cannot yet remove the click, and pretending
otherwise would produce applications Yasir has not seen going out under his name.

---

*Reviewed weekly. If a track has had no movement in two weeks, it gets cut or explicitly parked —
four live tracks is already one more than most people can carry.*
