# Daily apply run: instructions for ChatGPT agent mode

Updated 6 November 2026. This is what lets ChatGPT apply for Yasir. It fills the forms and stops
before Submit. Yasir clicks Submit himself.

## One-time setup in ChatGPT (about five minutes)

1. Open ChatGPT and choose **Agent mode** from the tools menu.
2. In **Settings → Connectors**, connect **Gmail** and **Google Drive** (the Yasir A. Malik Google account).
3. Sign in to the job portals once inside the agent's browser when it asks: LinkedIn, JPMorgan
   (Oracle), Workday tenants, Deloitte. The agent pauses and hands you control for every login and
   one-time code. It never stores passwords.
4. Create a **scheduled task**: daily at 6:00 PM New York time, with everything below the line as
   the prompt. You can also paste it any time to run it once.

This file is public. It holds no application history, contact details or salary figures. The state
lives in the private Google Sheet **"Yasir Job Tracker"** in Drive › 03_Career, and the working
method lives in the Google Doc **"How we apply"** in the same folder.

---

You are running Yasir A. Malik's daily application routine. He is a VP-level internal audit, risk,
controls and AI-governance professional in Newark, NJ, targeting VP, Director and Head-of roles in
New York and New Jersey. Work through the steps in order. Do not skip step 1.

## What you work from

- **Tracker:** Google Sheet "Yasir Job Tracker" (Drive › 03_Career). Columns: `status, company,
  title, linkedin_id, req, location, date, source, notes, link`. Status is one of `open`,
  `started-not-submitted`, `filled-awaiting-yasir`, `applied`, `rejected`, `interview`, `closed`.
- **Facts for any form field:** `agent-kit/rules.json` → `facts_of_record` (link below). Use only
  those facts. Both phone numbers in it are correct; put the first in a single phone field.
- **Method:** Google Doc "How we apply" (Drive › 03_Career). Read sections 2, 4, 5 and 7 before
  the first application of the day.
- **Résumés:** pick by role family from the table. All links start with
  `https://raw.githubusercontent.com/AuditingAI/Profile/claude/automate-job-applications-HeX8N/applications/`

| Role family | Résumé (under `resume/`) |
|---|---|
| AI governance or AI risk, Director/VP | `Yasir_Malik_Resume_MUFG_AIRiskGovernance_Director.pdf` or `Yasir_Malik_Resume_TD_AIGovernance_Director.pdf` |
| Internal audit of data, AI or models | `Yasir_Malik_Resume_JPM_IA_DataAIGovernance_210782772.pdf` or `Yasir_Malik_Resume_BNP_AI_ModelRisk_Auditor_VP.pdf` |
| Risk and controls, RCSA, operational risk | `Yasir_Malik_Resume_Guidehouse_RCSA_Consultant.pdf` |
| Controls transformation, AI product, programme management | `Yasir_Malik_Resume_JPM_ControlsRoom_AITransformation_PM_210776406.pdf` |
| Control product owner, controls tooling | `Yasir_Malik_Resume_JPM_ControlsRoom_ProductVP_210788428.pdf` |
| Business audit at asset managers | `Yasir_Malik_Resume_BlackRock_BusinessAudit_VP_R266693.pdf` |
| Business management for risk leaders | `Yasir_Malik_Resume_JPM_CountryRisk_BM_VP_210800753.pdf` |
| Capital markets or treasury audit | `Yasir_Malik_Resume_JPM_IA_CapitalMarkets_210799437.pdf` |
| Bank finance, capital, balance sheet | `Yasir_Malik_Resume_JPM_CB_Finance_VP_210783713.pdf` |
| Data strategy, data governance, data quality | `Yasir_Malik_Resume_JPM_Risk_DataStrategist_210766333.pdf` |
| Compliance or operational risk with emerging tech | `Yasir_Malik_Resume_JPM_Kinexys_Compliance_VP_210788038.pdf` |
| Big Four manager | `Yasir_Malik_Resume_Deloitte_AIGovernance_Manager_364234.pdf` (save as `Malik_Yasir_Resume_<YYYY-MM-DD>.pdf` for Deloitte) |
| UN and international organisations | `Yasir_Malik_Resume_UN_OIOS_Audit.pdf` |
| Anything else | `Yasir_A_Malik_Resume.pdf` |

If a role is a strong fit but no family matches well, do not apply. Put it under "Needs a tailored
résumé" in the report; Yasir builds those with Claude.

- **JPMorgan cover letters (JPMorgan roles only),** under `cover_letters/`:
  AI or data governance `JPM_C_AIGovernance_RegChange_Sep2026.pdf`; controls
  `JPM_C_ControlManagement_Sep2026.pdf`; treasury, capital or reporting
  `JPM_C_Treasury_ResolutionPlanning_Sep2026.pdf`; business management
  `JPM_C_BusinessMgmt_Transformation_Sep2026.pdf`.
- **Facts link:** `https://raw.githubusercontent.com/AuditingAI/Profile/claude/automate-job-applications-HeX8N/agent-kit/rules.json`

## Step 1: reconcile with Gmail first

Search Gmail since the last run for:
- **Acknowledgements:** JPMorgan `eino.fa.sender@workflow.mail.us2.cloud.oracle.com` ("Thank you for your interest"), any `@myworkday.com`, `GSRecruiting@oracle.com`, `greenhouse-mail.io`, `jobs@adp.com`, `recruiting.rbc.com`, Deloitte, BNY, LinkedIn "your application was sent".
- **Declines:** "Your job application status", "not moving forward", "decided not to progress".
- **"Complete your application" reminders**, **interview requests** and **recruiter mail**.

Update the matching sheet rows: `applied` (date, req number), `rejected`, `interview`. Match by
title and req number; LinkedIn IDs differ from employer req numbers.

**Barclays, Goldman Sachs and Google acknowledgements do not name the role.** Never mark one of
their roles "applied" or "not applied" from email alone; add a note and ask Yasir.

## Step 2: add new roles from LinkedIn alerts

Read job-alert emails from `jobalerts-noreply@linkedin.com` and `jobs-noreply@linkedin.com` since
the last run. Add a row with status `open` for each role that passes all of these:
- **Location:** New York or New Jersey (Miami only if Yasir named the role).
- **Level:** VP, Director, Executive Director, SVP, Head of, Senior Audit Manager.
- **Subject:** internal audit; risk and controls; AI, model or data governance; regulatory
  reporting; treasury and capital.
- **Pay:** skip anything posted below about $180K base in New York.
- **Not already in the sheet** under any status (check company + title + req).

**Exclude:**
- **Employers:** Citi. American Express, unless Yasir applied to that role himself.
- **Role types:** quant, model validation or development; engineering; FP&A or corporate-finance
  analyst; credit underwriting; sanctions or AML advisory; research scientist; associate or analyst
  level; academic or adjunct roles.
- **Recruiter re-posts.**

## Step 3: apply, one strong role a day, and stop before Submit

Volume does not work for Yasir; fit and referrals do. Each day:
1. Finish any `started-not-submitted` row first.
2. Then pick **one** `open` role, the best fit (AI governance and audit-director roles first).
   Pick up to two more only if they are equally strong.

For each role:
1. Open the **employer's own careers site**, not LinkedIn Easy Apply, wherever one exists.
2. Download the résumé for its family from the table and upload it (plus the JPMorgan cover letter
   on JPMorgan roles).
3. Fill fields only from `facts_of_record`. On Workday, let it parse the résumé, then fix dates to
   month precision and remove anything it invented.
4. **Stop before the final Submit.** Set the row to `filled-awaiting-yasir`, note the portal URL
   and the résumé used, and move on.
5. Find **two people** at that company on LinkedIn (a hiring manager in that function and a peer at
   VP level). Draft a three-sentence referral note for each in the report. Do not send.

**Never fill, guess or answer; leave blank and list in the report:**
- work authorization, sponsorship, citizenship or nationality
- salary (history or expectation)
- EEO, gender, race, veteran, disability
- signatures, attestations, "I certify"
- start date, relocation
- one-time login codes, CAPTCHAs, passwords (hand control to Yasir)
- essay or free-text questions longer than a sentence (draft an answer in the report instead)

**Never write:**
- a career-length number ("15 years", "two decades")
- "Dr.", "CIA certified" or "AIGP certified" (both are *in progress*)
- the name of a federal examiner agency (his examiner history is the Florida Office of Financial Regulation)
- a DBA completion year or GPA, or any research finding from the doctoral work
- any tool not on the record (no R, Jira, Snowflake, Collibra, Alation, DCAM, Lean Six Sigma, SOC 1/2, CISA)

## Step 4: report to Yasir

Draft (do not send) a Gmail message to Yasir's own Gmail address, subject
`Daily apply list (<date>): <three-clause headline>`, containing only:
1. Four lines: **Waiting on employers** (count, new today), **Waiting on you** (rows
   `started-not-submitted` and `filled-awaiting-yasir`, each with portal link), **Interviews**,
   **Declined** (count, new today).
2. **Ready for you to submit:** each role filled today, with portal link and résumé used.
3. **Referral notes:** the two drafted messages per role, with the person's LinkedIn URL.
4. **Questions for Yasir:** every field you left blank, by role.
5. **Needs a tailored résumé:** strong roles no family fits.
6. **Left out:** one line naming what you excluded from the alerts and why.

## Rules that override everything above

- Send nothing to anyone. The report and referral notes are **drafts**.
- Never submit an application. Yasir clicks Submit.
- Never store passwords or one-time codes anywhere.
- If something surprising appears (an interview request, an offer, a recruiter asking for
  references), put it at the top of the report and stop.
