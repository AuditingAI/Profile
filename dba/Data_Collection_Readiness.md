# Data Collection Readiness Checklist

**Project:** Mitigating Anchoring Bias in Long-Term Auditor Engagements
**Author:** Yasir A. Malik (PID on file) — FIU DBA Cohort 7.16
**Advisor:** Prof. Dr. Juan Rey
**Compiled:** June 1, 2026 — updated with 03_Recruitment_and_Pilot READY packet
**Owner of unchecked items:** Yasir (this is the work that must happen before pilot launch)

---

## Stage 0 — Ethics & Regulatory 🟢 COMPLETE

- ✅ **IRB approval** — FIU IRB Protocol IRB-25-0462, approved September 2, 2025, effective through September 2, 2030 (5-year exempt status)
- ✅ **Informed consent letter** — IRB-approved Informational Letter presented as the first screen of the survey before any item
- ✅ **Compensation structure** — fixed, Florida-compliant amount paid on submission; no incentive tied to answer content
- ⏳ **IRB PI-change amendment** — to be filed in Topaz this week per Weekly Update W01 v2
- ✅ **Data-handling protocol** — anonymous collection via FIU Qualtrics, IP retention disabled, FIU-secured storage, access limited to investigator and advisor

---

## Stage 1 — Instrument 🟡 FINAL BUILD IN PROGRESS

- ✅ **Constructs defined** — 11 constructs operationalized in `Research_Paper_YMalik_v4.docx` §§ 2.4–2.13 (8 IVs + 2 mediators + 1 DV)
- ✅ **Items drafted** — 5 items × 11 constructs = 55 construct items + 12 demographics, in v4 Appendix A
- ✅ **Reverse-coded items** — one reverse-coded item per construct, embedded
- ✅ **Attention checks** — two embedded ("select Disagree", "select Agree")
- ⏳ **Reconciled against IRB-approved instrument** — Appendix A is a draft for reconciliation; the IRB-approved instrument (`Updated Measurement Instrument – Malik, Y.docx`) governs where they differ. **ACTION:** open both side-by-side, confirm wording matches, log any differences as either (a) non-substantive or (b) requiring a Topaz amendment.
- ⏳ **Loaded into Qualtrics** — final reconciled items entered into FIU Qualtrics. **ACTION:** complete before today's meeting if possible; if not, screen-share whatever state the build is in.
- ⏳ **Survey logic** — consent block → demographics → randomized construct blocks → debrief → submission confirmation. **ACTION:** verify in Qualtrics.
- ⏳ **Face-validity walk-through with Dr. Rey** — this is the explicit ask from his 2026-06-01 email.

---

## Stage 2 — Informed Pilot 🟢 READY PACKET COMPLETE (awaits Stage 1 closure)

**📦 READY packet** filed at `dba/03_Recruitment_and_Pilot/` as of 2026-06-01:

| Artifact | Status | Path |
|---|---|---|
| Informed Pilot Protocol | ✅ READY | `03_Recruitment_and_Pilot/YMalik_Informed_Pilot_Protocol_READY_2026-06-01.docx` |
| Pilot Feedback Form + Revision Log (xlsx, 4 tabs) | ✅ READY | `03_Recruitment_and_Pilot/YMalik_Pilot_Feedback_Form_and_Revision_Log_READY_2026-06-01.xlsx` |
| CloudResearch Launch Draft | ✅ READY | `03_Recruitment_and_Pilot/YMalik_CloudResearch_Launch_Draft_READY_2026-06-01.docx` |
| MTurk Backup Launch Draft | ✅ READY | `03_Recruitment_and_Pilot/YMalik_MTurk_Backup_Launch_Draft_READY_2026-06-01.docx` |
| Recruiting Launch Checklist | ⚠️ MISSING — referenced in README but not yet in repo | (`YMalik_Recruiting_Launch_Checklist_READY_2026-06-01.xlsx` to be added) |

**Pilot protocol (confirmed in READY packet):**
- ✅ **Target n = 6–10** eligible auditors (face-validity / clarity / timing / technical pilot, not statistical)
- ✅ **Eligibility = survey eligibility** — age 18+, current/recent auditor, ≥2 yrs experience, recurring/long-term engagement exposure
- ✅ **Boundaries** — no employer/client/account-level/confidential data requested in pilot or full survey
- ✅ **Scope discipline** — current model only (TA, RA, AT, SAP, FR, IR, RPG, PMI → AJQ/APR → RAB); AI/LLM constructs reserved for future research, not in this data collection
- ✅ **Decision rules** — clarity < 4/5 triggers wording revision; construct-fit < 4/5 triggers advisor review; IRB-scope-affecting feedback halts and triggers Topaz amendment
- ✅ **Feedback instrument** — 10 questions (PF1–PF10): clarity of consent, eligibility, audit-language fit, length, technical flow, confusing items, redundancy, sensitive-data flag, completion time, open comments
- ✅ **Participant log structure** — 10-row template, anonymous Pilot IDs only (P01–P10); no employer/client names recorded
- ✅ **Revision log structure** — 20-row template, severity-tagged, advisor/IRB-review flag column
- ✅ **Decision summary** — 6 launch-gating criteria pre-defined (size, timing, no sensitive data, scope, revision boundary, launch decision)

**Pre-launch tasks (remaining):**
- ⏳ Pilot recipient identification — 6–10 LinkedIn audit contacts who meet eligibility
- ⏳ Pilot invitation copy — short, friendly, IRB-aligned, time estimate (~18 min)
- ⏳ Qualtrics preview testing — both eligible and screen-out paths
- ⏳ Pilot link distribution after face-validity sign-off

---

## Stage 3 — Recruiting Platforms 🟢 LAUNCH DRAFTS READY (sequencing locked)

### Sequencing rule (per CloudResearch READY draft)

**CloudResearch first**, because (a) Dr. Rey explicitly identified recruiting platforms in his 2026-06-01 message and (b) the IRB file references CloudResearch for subject recruitment. **MTurk second**, only if CloudResearch yield or quality is insufficient after the initial window.

### 3a — CloudResearch (primary) ✅ Launch draft READY

- ✅ **Study title** — "Auditors' Professional Judgments and Audit Work Practices"
- ✅ **Short description** — 15-20 min anonymous academic survey
- ✅ **Eligibility filters** — age 18+, current/recent auditor, ≥2 yrs experience, recurring-engagement exposure
- ✅ **Compensation** — fixed platform amount, value pending advisor confirmation
- ✅ **Soft-launch protocol** — 10-15 responses first; review eligibility pass rate, attention checks, completion time, duplicate risk, export integrity *before* full launch
- ✅ **Quality filters** — duplicate prevention, suspicious-activity controls, page-timing flags, 2-of-3 attention-check exclusion rule
- ✅ **Target** — n = 60-80 valid responses after cleaning
- ✅ **Do-not-add boundaries** — no AI/LLM items in this survey, no employer/client/confidential/sensitive data, no scope-affecting changes without advisor/IRB
- ⏳ Account setup with researcher credentials + IRB on file
- ⏳ Project creation in CloudResearch dashboard
- ⏳ Compensation amount confirmation with Dr. Rey

### 3b — MTurk (backup) ✅ Launch draft READY

- ✅ **HIT title + description + eligibility + instructions + qualifications + compensation language** — drafted
- ✅ **Use condition** — backup or second channel only if CloudResearch insufficient
- ✅ **Quality review** — screen-out rate, eligibility fit, attention checks, page timing, straight-line detection, duplicate exclusion
- ✅ **Boundary** — same model, no AI/LLM scope creep, no IRB-scope changes
- ✅ **Quality threshold** — 95%+ approval, 100+ approved HITs (if consistent with platform plan)

### 3c — LinkedIn (parallel channel) ✅ Outreach copy READY (awaiting sign-off)

- ✅ **Outreach copy** — three IRB-aligned templates in `LinkedIn_Outreach_Pack.docx`
- ⏳ **Advisor sign-off on copy** — explicit ask in today's meeting
- ⏳ **Outreach log spreadsheet** — IRB-compliant fields only (no identity-to-submission linkage)

### 3d — IIA chapter referrals (backfill) ⏳ Pending

- ⏳ Identify South Florida / Miami chapter contacts
- ⏳ Email-introduction copy + advisor sign-off

---

## Stage 4 — Analysis Readiness 🟢 PIPELINE SPECIFIED

- ✅ **Analysis plan documented** — `Research_Paper_YMalik_v4.docx` § 4.4 (cleaning → descriptives → reliability α ≥ .70 → EFA with PAF + varimax + KMO + Bartlett + parallel analysis → correlations → regression → PROCESS Model 4 mediation, 5,000 bootstraps)
- ⏳ **Software access** — SPSS + PROCESS macro confirmed available via FIU
- ⏳ **EFA decision rules pre-specified** — Kaiser–Guttman + scree + parallel analysis convergence; minimum factor loading 0.40; cross-loading threshold 0.30
- ⏳ **Sample-size monitoring rule** — close collection at n = 60 minimum / 80 target / hard stop at 100

---

## What's actually blocking the pilot, in one sentence

**Once the instrument is reconciled with the IRB-approved version, loaded into Qualtrics, and Dr. Rey has signed off on its face validity and the LinkedIn outreach copy, the pilot launches** — and the pilot protocol, feedback form, revision log, and both recruiting-platform drafts are already READY in `dba/03_Recruitment_and_Pilot/`.

---

## Status traffic light, as of 2026-06-01 (after READY packet)

| Stage | Status | Change since v1 |
|---|---|---|
| 0 — Ethics / IRB | 🟢 Complete | — |
| 1 — Instrument | 🟡 Draft complete; Qualtrics build + face-validity walkthrough pending | — |
| 2 — Informed pilot | 🟢 **READY packet complete** (was 🟡) | ⬆️ Protocol, feedback form, revision log, decision rules all filed |
| 3 — Recruiting platforms | 🟢 **CloudResearch + MTurk drafts READY** (was 🔴) | ⬆️ Launch drafts filed; sequencing locked |
| 4 — Analysis pipeline | 🟢 Plan documented | — |

**Net read for the advisor:** project moved from "paper-only" to "READY-to-launch" in one cycle. Three remaining blockers are all addressable in one meeting (Qualtrics build, face-validity sign-off, LinkedIn copy sign-off). After that, soft-launch can begin within the same week.
