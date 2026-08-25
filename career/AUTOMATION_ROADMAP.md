# Automation Roadmap — how close can "you apply, I confirm" actually get?

The ask: *"fully automate it, where you apply it and you send me your confirmation."*

This document is the straight answer, in three tiers, with what each one costs and what it risks.

---

## Tier 0 — where the system is today

Automated: harvest → score → dedupe → match a resume package → assemble the digest → draft the
email or cover letter → schedule the block → log it.

Manual: the click.

**Time cost to Yasir:** ~10 minutes per application, entirely at the end.
**Actual throughput:** near zero. Ten runs, two score-5 roles recommended four times each, no
applications submitted. Tier 0 is not throughput-limited by tooling; it is limited by the last
ten minutes, which never happen.

---

## Tier 1 — one-click packages (recommended, buildable now)

Instead of a digest that says *"apply to this,"* the pipeline produces, per role, a folder containing:

- resume tailored to the posting, already formatted
- cover letter naming the specific req, hiring manager if findable
- pre-written answers to the standard screening questions (work authorization, sponsorship,
  salary expectation, notice period, "why this company")
- the direct apply URL, and a note on which ATS it uses

Yasir opens the link, pastes, submits. **Two minutes, no thinking.**

**Cost:** a few hours of build. **Risk:** none — nothing leaves without him.
**What it fixes:** the ten-minute tax, which is the actual bottleneck.
**What it does not fix:** if the problem is avoidance rather than time, Tier 1 will not move the number.
That is worth knowing before building Tier 2.

---

## Tier 2 — assisted submission with a human gate

Browser automation (Chromium + Playwright is already available in this environment) drives the ATS
form, fills every field from the package, and **stops at the review screen**. Yasir gets a screenshot,
confirms, and the automation clicks submit.

**What this requires from Yasir:**
- LinkedIn credentials, and credentials for each ATS account (Workday creates a separate login per employer)
- A persistent session store — meaning those credentials live somewhere on disk
- Acceptance that a session may be interrupted by MFA, CAPTCHA, or a "verify it's you" challenge

**Real risks, stated plainly:**
- **Account flagging.** LinkedIn and most ATS vendors run bot detection. Automated form-filling can
  trigger a restriction on the LinkedIn account — the same account that is currently the *only*
  working source of job alerts in his lane. Losing it would cost more than the automation saves.
- **Wrong submissions are not retractable.** A misparsed field in a Workday form goes to a real
  recruiter under his real name. There is no unsend.
- **Credential exposure.** Storing bank-adjacent-employer logins for automation is a genuine
  security decision, not a convenience one.

**Verdict:** technically buildable, and defensible *only* with the human gate at the review screen.
Fully unattended submission is not recommended at any point — the downside is asymmetric.

---

## Tier 3 — unattended apply

Not recommended. Applications go out that Yasir has never read, under his name, to firms he may
later interview with. The failure mode is not "wasted application"; it is "recruiter at BNY reads
something inaccurate about your background that you did not write." One of those costs more than
fifty saved clicks.

---

## Recommendation

Build **Tier 1 now.** It removes the real friction, carries no risk, and is honest about what it is.

Run **Tier 1 for two weeks** and count applications submitted. If the number is still near zero,
the constraint was never the tooling, and Tier 2 will not fix it either — at that point the
conversation is about the calendar and the avoidance, not about the automation.

Revisit **Tier 2** only after that experiment, and only with the review-screen gate.

---

## What Yasir needs to decide

1. Build Tier 1? (yes/no — I can have it running today)
2. If Tier 2 later: is he willing to store ATS credentials, and to accept LinkedIn-account risk?
3. What is the daily application target? The system should hold him to a number he chose, not one
   it invented. Three per weekday reaches fifteen a week without heroics.
