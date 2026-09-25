# Prolific Relaunch Guide — Getting the Right Sample This Time
**Step-by-step with links · July 2026 · Companion to `STUDY_OVERVIEW.md` §8**

> **⚠️ THE ONE HARD GATE:** the IRB-approved protocol (IRB-25-0462) specifies **U.S. auditors**. ==Do not launch a broadened-population study until an IRB amendment is approved.== Everything below EXCEPT the final launch step can and should be done now — including the free eligibility test that proves the new population works.

---

## PHASE 1 — Close out the old study & recover the money (today, ~10 min)

| Step | Action | Link |
|---|---|---|
| 1.1 | Open the active study's submissions page | https://app.prolific.com/researcher/workspaces/studies/6a508fe494392aa43ed7a1ac/submissions |
| 1.2 | **Screenshot the study header** showing "2/100" and **"20 of 334,976 eligible participants"** — this is citable evidence; capture before stopping | *(same page)* |
| 1.3 | Also click **"Download demographic data"** for your records (aggregate platform data — keep private) | *(same page)* |
| 1.4 | Top-right **Action** menu → **Pause**, then **Stop study** | *(same page)* |
| 1.5 | Confirm ~$980 released to workspace balance (may take minutes) | https://app.prolific.com/researcher/workspaces/6a4e7265a79f3d33156014d0/finance |
| 1.6 | Decide: leave as credit for the relaunch (recommended) or contact support for refund | https://researcher-help.prolific.com/ |
| 1.7 | **Enable MFA** on the account (it holds real money) | Workspace → account security banner → "More info" |

## PHASE 2 — The free eligibility test (today, ~20 min, costs $0)

This is the trick that prevents a second $1,000 lesson: **Prolific shows you the eligible-participant count for any screener combination in a DRAFT study, before you pay anything.**

| Step | Action |
|---|---|
| 2.1 | New study: https://app.prolific.com/researcher/workspaces/projects/6a4e7265a79f3d33156014d4/new-study — name it "DRAFT — Risk & Assurance Screener Test" |
| 2.2 | In **Audience → Screeners**, build the broadened filter set (below) |
| 2.3 | Watch the **"Eligible participants"** counter update live as you add each screener |
| 2.4 | Record the counts for 2–3 screener variants (strict / medium / broad). **Do NOT publish** — leave as draft. Zero cost. |

**Screener variants to test (Audience → Screeners → search these categories):**

| Variant | Screeners to select | Expect |
|---|---|---|
| A — Strict | Employment status: *Full-time* · Industry: *Accountancy, banking, finance* · Job function/role: anything audit/compliance/risk-related the taxonomy offers | Thousands (vs. your 20) |
| B — Medium | Employment: Full-time · Industry: *Accountancy, banking, finance* OR *Insurance* · Seniority: mid-level+ | Larger still |
| C — Broad | Employment: Full-time · Industry: finance-adjacent set · then **screen precisely INSIDE the survey** (recommended pattern below) | Largest |

**The recommended pattern — platform-broad, survey-precise:** panel taxonomies never map cleanly to "does recurring multi-period reviews." So: use platform screeners only for the broad cut (full-time + finance/accounting industry), then keep your **in-survey screening questions** (rewritten per the IRB amendment) as the true gate: *"Does your role involve audit, risk, compliance, controls, or review work in which you assess the same entity, account, process, or portfolio across multiple periods?"* Prolific permits in-survey screen-outs if screened-out participants are compensated pro-rata or the study description states eligibility clearly — see their screening policy: https://researcher-help.prolific.com/en/articles/425224-prescreening-participants

## PHASE 3 — IRB amendment (this week, before any launch)

| Step | Action |
|---|---|
| 3.1 | FIU IRB (Office of Research Integrity): submit an **amendment** to IRB-25-0462 changing the population from "U.S. auditors" to "U.S. risk & assurance professionals (audit, risk management, compliance, controls, credit/quality review) with recurring multi-period review responsibilities" — via Topaz/the FIU research portal you used originally |
| 3.2 | Include: revised screening questions, revised recruitment text, unchanged instrument (or minimally generalized wording — attach tracked changes if any) |
| 3.3 | Optionally align with Dr. Rey / Miguel Aguirre-Urreta first — the amendment doubles as the dissertation's sampling design |

## PHASE 4 — Relaunch (after IRB approval, ~30 min)

| Step | Action |
|---|---|
| 4.1 | Duplicate the draft test study; paste the Qualtrics live link; set completion-code handshake (fix the "NO CODE" issue: Qualtrics end-of-survey → redirect to Prolific completion URL — https://researcher-help.prolific.com/en/articles/430328) |
| 4.2 | Reward: keep ~$6.00 / 15 min (~$24/hr — above Prolific's good-practice bar) |
| 4.3 | **Soft-launch 10 places first**; check quality of completions in 48h; then scale with remaining budget (~$980 ≈ 120+ more completions incl. fees) |
| 4.4 | Set places to match the IRB-amended target (e.g., 100–150) and monitor via the submissions page |

## PHASE 5 — Parallel channels (so Prolific isn't a single point of failure)

- **CloudResearch Connect** — same broadened screener logic; guide already in repo (`CloudResearch_Setup_Guide.md`).
- **Negotiated access:** IIA/AICPA chapters, ISACA, RIMS; FIU DBA alumni; your London & Canada contacts (add international scope to the IRB amendment if pursued).
- **LinkedIn outreach kit** already in repo (`LinkedIn_Outreach_Pack.docx`) — retarget to risk/compliance groups.

---

**Working hand-in-hand:** you do the clicks (only you have the Prolific/IRB logins); I draft every text artifact on demand — the IRB amendment language, revised screeners, recruitment posts, and the study description. Say "draft the IRB amendment" when you're ready.
