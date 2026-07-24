---
name: job-search
description: Yasir's daily job-hunt automation for AI governance, audit, and risk leadership roles in the NYC metro. Scans Gmail LinkedIn job alerts, runs live Indeed searches, scores every role against Yasir's profile, matches top roles to his tailored resume packages in Dropbox, logs the digest to Notion, and outputs a ranked shortlist with apply links. Use this skill whenever the user asks to run the job search, check job alerts, find new roles, build a shortlist or daily digest, asks "anything new worth applying to," mentions LinkedIn job emails, or wants to know which resume to use for a role — even if they don't say "job search" explicitly.
---

# Job Search — Daily Digest for Yasir Malik

Produce a ranked, actionable shortlist of AI governance / audit / risk leadership roles, matched to ready-to-send resume packages. The goal is not a list of links — it is a decision: **what should Yasir apply to today, with which resume.**

## Who you're searching for

Yasir A. Malik — NYC metro. 15 years audit/risk at Citi and JPMorgan; former bank examiner (OCC, Federal Reserve, FDIC); built a production RAG/AI tool inside Citi that cut audit cycle time 35%; DBA candidate researching AI decision risk. Target level: VP / Director / Head-of. Target comp: $180K+ (flag as priority when the top of the posted range is $250K+). Dates in the digest and Notion log use today's date, Eastern Time.

**Bullseye titles** (score 5): AI governance, AI risk management, AI audit/assurance, responsible AI, model risk — at Director/VP/Head level.
**Strong** (score 4): technology audit, third-party/vendor risk, data governance, AI product leadership at a bank or regulated enterprise.
**Adjacent** (score 3): general internal audit VP, risk transformation, AI strategy at non-regulated firms.
**Off-lane** (score 1–2): government affairs, pure engineering, finance/treasury, anything below VP. List these only in a collapsed "everything else" section, never in the shortlist.

## Workflow

Run steps 1–2 in parallel. If any connector is unavailable, say so plainly in the output and continue with the rest — never fabricate results for a source you couldn't reach.

### 1. Gmail — harvest the alerts

Search with the Gmail connector:
- `from:jobalerts-noreply@linkedin.com newer_than:2d` — job alerts (use `newer_than:7d` if the user asks for "this week")
- `from:hit-reply@linkedin.com newer_than:7d` — **recruiter DMs. These outrank every alert.** A human who already replied is worth more than any posting. Read the thread state before prescribing the action: an unread cold DM gets "reply today"; an in-flight thread (calls done, link sent) gets the specific next step ("complete the link they sent"); threads in Trash get skipped.

Parse company, title, and comp from subjects/snippets. Note which are UNREAD. Alert subjects carry no apply URL — for any alert role that makes the top picks, open the thread to pull the job link from the body; if none is extractable, mark it "(via LinkedIn alert)" rather than inventing a link.

### 2. Indeed — live search

Run these three searches via the Indeed connector (location "New York, NY", country US, fulltime):
- `AI governance risk director`
- `AI audit assurance vice president`
- `model risk management director`

Narrow queries sometimes return nothing — if a query comes back empty, retry it once broadened (e.g. `AI audit vice president`, `model risk director`) and note in the digest which lanes came back thin. Keep apply URLs exactly as returned — embed each as a link on the job title.

### 3. Score and dedupe

Score every role 1–5 with the rubric above. Dedupe across sources (same company + similar title = one entry; keep the one with an apply link). LinkedIn re-sends the same alert on consecutive days — collapse repeats and note "seen 2×" as a freshness signal, not a new role.

### 4. Match to a resume package

Tailored packages live in Dropbox under `/Resume/Application_Package_*/`. **Search Dropbox for `Application_Package` first to get the live inventory** — packages get added over time (e.g. a generic `Application_Package_AI_Governance` exists beyond the table below). Match by company first, then by role family:

| Package | Covers |
|---|---|
| Citi_ChiefAuditor_AIAssurance | Citi + any AI audit/assurance role |
| JPMorgan_IA_VP_AIML | JPMorgan + AI/ML internal audit |
| MorganStanley_AIGovernance_VP, WellsFargo_AIGovernance_ED, StateStreet_DataAI_Governance | AI/data governance at banks |
| Barclays_IA_ModelRisk_VP, BNY_VP_FinancialModelRiskAuditor | model risk |
| GoldmanSachs_IA_TechRiskCyber_VP, BlackRock_VP_BusinessAudit_DigitalAssets, HSBC_IA_AIRisk_VP | tech risk / AI risk audit |
| Microsoft_SrTPM_ResponsibleAI, Google_Director_AINativeWorkLabs, Apple_AIML_Compliance_PoliciesLead, Anthropic_PublicPolicy_SOps | big tech / responsible AI |
| Prudential_DataAI_Platforms | insurance / data platforms |

No close match → recommend adapting the nearest package from the master `Yasir_Malik_Resume_2026.docx`, and name which package to start from. Verify the package still exists with a Dropbox search before citing it.

### 5. Log to Notion

Append a dated entry to the **Weekly Status Log** page (ID `3734ffd3-8c7e-8191-93ec-d970bc0003e5`): date, roles scanned (count per source), top picks (title/company/score), and actions recommended. One compact block per run — this page is a running history, so keep each entry short and don't restructure existing content.

### 6. Output the digest

ALWAYS use this exact structure:

```
# Job Digest — [date]

## 🔥 Act today
[Recruiter threads needing replies; anything expiring or posted <48h with score 5]

## Top picks (apply this week)
| # | Role (linked) | Company | Comp | Score | Resume package | Why it fits |

## Seen again / lower priority
[one-line each]

## Logged
[Confirmation the Notion entry was written + any connector that was down]
```

Keep "Why it fits" to one clause (e.g., "your exact Citi audit track"). 5–8 top picks maximum — a shortlist that isn't short gets ignored. End with the single next action you'd take first if you were him.
