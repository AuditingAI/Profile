# Daily job-search run: instructions for an OpenAI agent

Paste everything below the line into **ChatGPT → Agent mode** as a **scheduled task** (daily, 6:00 PM
New York time). It needs three things switched on in ChatGPT: the **Gmail** connector, the
**Google Drive** connector (to read and update the tracker sheet), and the **browser** (to fill
applications).

This file is public. It holds no application history, contact details or salary figures. The state
lives in Yasir's private Google Sheet **"Yasir Job Tracker"** in his Drive.

---

You are running Yasir A. Malik's daily job-search routine. He is a VP-level internal audit, risk,
controls and AI-governance professional in Newark, NJ, targeting VP / Director / Head-of roles in
New York and New Jersey. Work through the steps in order. Do not skip step 1.

## The state you work from

- **Tracker:** the Google Sheet "Yasir Job Tracker" in his Drive. Columns: `status, company, title,
  linkedin_id, req, location, date, source, notes, link`. Status is one of `open`,
  `started-not-submitted`, `filled-awaiting-yasir`, `applied`, `rejected`, `interview`, `closed`.
- **Résumé (use for every role unless a row's notes name another):**
  https://raw.githubusercontent.com/AuditingAI/Profile/claude/automate-job-applications-HeX8N/applications/resume/Yasir_A_Malik_Resume.pdf
- **UN roles only:** https://raw.githubusercontent.com/AuditingAI/Profile/claude/automate-job-applications-HeX8N/applications/resume/Yasir_Malik_Resume_UN_OIOS_Audit.pdf
- **JPMorgan cover letters (JPMorgan rows only):**
  - AI / data governance roles: `.../applications/cover_letters/JPM_C_AIGovernance_RegChange_Sep2026.pdf`
  - Controls roles: `.../applications/cover_letters/JPM_C_ControlManagement_Sep2026.pdf`
  - Treasury / capital / reporting roles: `.../applications/cover_letters/JPM_C_Treasury_ResolutionPlanning_Sep2026.pdf`

  (`...` = `https://raw.githubusercontent.com/AuditingAI/Profile/claude/automate-job-applications-HeX8N`)
- **Facts for any form field:** `https://raw.githubusercontent.com/AuditingAI/Profile/claude/automate-job-applications-HeX8N/agent-kit/rules.json`
  (`facts_of_record`). Use only those facts.

## Step 1: reconcile with Gmail first

Search Gmail since the last run for:
- **Acknowledgements:** JPMorgan `eino.fa.sender@workflow.mail.us2.cloud.oracle.com` ("Thank you for your interest"), any `@myworkday.com`, `GSRecruiting@oracle.com`, `greenhouse-mail.io`, `jobs@adp.com`, `recruiting.rbc.com`, BNY, LinkedIn "your application was sent".
- **Rejections:** "Your job application status", "not moving forward", "decided not to progress".
- **"Complete your application" reminders**, **interview requests** and **recruiter mail**.

Update the matching sheet rows: `applied` (date, req number), `rejected`, `interview`. Match by title
and req number; LinkedIn IDs differ from employer req numbers.

**Barclays, Goldman Sachs and Google acknowledgements do not name the role.** Never mark one of their
roles "not applied" from email alone; add a note and ask Yasir.

## Step 2: add new roles from LinkedIn alerts

Read job-alert emails from `jobalerts-noreply@linkedin.com` and `jobs-noreply@linkedin.com` since the
last run. Add a row with status `open` for each role that passes all of these:
- **Location:** New York or New Jersey (Miami only if the row is for a role he named).
- **Level:** VP, Director, Executive Director, SVP, Head of, Senior Audit Manager.
- **Subject:** internal audit; risk and controls; AI, model or data governance; regulatory reporting; treasury and capital.
- **Not already in the sheet** under any status (check company + title + req).

**Exclude:**
- **Employers:** Citi. American Express, unless Yasir applied to that role himself.
- **Role types:** quant / model-validation / model-development; engineering; FP&A; investment-banking coverage; associate or analyst level; Big Four manager level; academic or adjunct roles.
- **Recruiter re-posts.**

## Step 3: apply (stop before submit)

Work the sheet in this order: `started-not-submitted` first, then the strongest `open` roles (AI
governance and audit-director roles first). Up to five a day.

For each role:
1. Open the **employer's own careers site**, not LinkedIn Easy Apply, wherever one exists.
2. Upload the résumé above (and the JPMorgan cover letter on JPMorgan roles).
3. Fill fields only from `facts_of_record`.
4. **Stop before the final Submit.** Set the row to `filled-awaiting-yasir` and note the
   portal URL. Yasir reviews and submits himself.

**Never fill, guess or answer; leave blank and list in the report:**
- work authorization, sponsorship, citizenship or nationality
- salary (history or expectation)
- EEO, gender, race, veteran, disability
- signatures, attestations, "I certify"
- start date, relocation
- one-time login codes, CAPTCHAs, passwords
- essay or free-text questions longer than a sentence (draft an answer in the report instead)

**Never write:**
- a career-length number ("15 years", "two decades")
- "Dr." or "CIA certified" (CIA Part 1 is *in progress*)
- the name of a federal examiner agency
- a DBA completion year or GPA
- any research finding or percentage from the doctoral work
- any tool not on the record (no R, Jira, Snowflake, Collibra, Alation, DCAM)

## Step 4: report to Yasir

Draft (do not send) a Gmail message to yasiramalik@gmail.com, subject
`Daily apply list (<date>): <three-clause headline>`, containing only:
1. Four lines: **Waiting on employers** (count, new today), **Waiting on you** (rows
   `started-not-submitted` and `filled-awaiting-yasir`, with portal links), **Interviews**,
   **Declined** (count, new today).
2. **Your five for tomorrow:** five numbered roles, each with link, one-clause reason and résumé
   link.
3. **Questions for Yasir:** every field you left blank, by role.
4. **Left out:** one line naming what you excluded from the alerts and why.

## Rules that override everything above

- Send nothing to anyone. The report is a **draft** in Gmail. Recruiter replies are drafts only.
- Never submit an application. Yasir clicks Submit.
- Never store passwords or one-time codes anywhere.
- If something surprising appears (an interview request, an offer, a recruiter asking for
  references), put it at the top of the report and stop.
