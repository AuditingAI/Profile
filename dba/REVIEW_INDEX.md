# 📖 Reviewer's Guide — Anchoring Bias Study (YMalik, GEB7913)

**For:** Professor Juan Rey · **Student:** Yasir A. Malik (PID 1687105) · FIU DBA Cohort 7.16
**Updated:** July 23, 2026 · **Branch:** `claude/scholar-links-review-Plgk6`

This page is the single entry point to the live project record. Every link below opens the current version of the document on this branch — the repository updates as the work progresses, so what you see is always the latest state.

---

## 📊 Chapter Status Dashboard

| Chapter | Status | Per the late-July meeting | Direct link |
|---|---|---|---|
| **📕 FULL PAPER (assembled)** | 🟢 **DRAFT READY** | Complete manuscript, Ch. 1–6 + references + Appendix A (~16,200 words) | [📄 PDF](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Research_Paper_YMalik_FULL_DRAFT.pdf) · [Markdown](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Research_Paper_YMalik_FULL_DRAFT.md) |
| **Ch. 1 — Introduction** | 🟢 **REWRITTEN** | Fresh introduction framing the study as executed: background, problem, purpose, RQs, significance (incl. AI direction), definitions, organization | [Open](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Research_Paper_YMalik_CH1_DRAFT.md) |
| **Ch. 2 — Literature Review** | ✅ **STANDS** | No changes — 11 construct sections + theory treatment as approved May 30 | [Open](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Research_Paper_YMalik_v4_master.md#chapter-2--review-of-the-literature) |
| **Ch. 3 — Model & Hypotheses** | ✅ **STANDS** | No changes — model figure + 16 hypothesis sections as approved May 30 | [Open](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Research_Paper_YMalik_v4_master.md#chapter-3--research-model-and-hypotheses) |
| **Ch. 4 — Methodology** | 🟢 **REWRITTEN (v2)** | Contract-level detail of every planned analysis: cleaning protocol, EFA criteria, reliability, CFA, regression, PLS-SEM | [Open](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Research_Paper_YMalik_CH4-6_DRAFT.md#chapter-4--research-methodology) |
| **Ch. 5 — Data Analysis** | 🟢 **REWRITTEN (v2)** | Full collection experience (pilot, Qualtrics, CloudResearch, economics, population-specificity); closes: required analyses could not be performed | [Open](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Research_Paper_YMalik_CH4-6_DRAFT.md#chapter-5--data-analysis) |
| **Ch. 6 — Conclusions** | 🟢 **REWRITTEN (v2)** | Limitations → recommendations (start early; 20–30 floor; broaden population) → dissertation transition incl. AI/LLM audit-risk direction | [Open](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Research_Paper_YMalik_CH4-6_DRAFT.md#chapter-6--conclusions) |
| Appendix A — Instrument | ✅ **STANDS** | Full 11-construct, 55-item measurement instrument | [Open](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Research_Paper_YMalik_v4_master.md#appendix-a--measurement-instrument-draft-for-review) |

**Timeline:** submission target Friday · Sunday latest · Tuesday hard deadline. Literature currency: Scholar alerts re-swept July 23 — no new human-auditor anchoring work; Ch. 2 remains current.

---

## 1 · The Manuscript

| Document | What it contains | Link |
|---|---|---|
| **Chapters 4–6 (NEW, per our meeting)** | Ch. 4 Methodology written as a full analysis contract (cleaning protocol, EFA criteria, reliability, CFA, regression, PLS-SEM); Ch. 5 Data Analysis (collection experience, pilot, platforms, economics, population-specificity; closes: required analyses could not be performed); Ch. 6 Conclusions (limitations → recommendations → dissertation transition) | [Read Ch. 4–6](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Research_Paper_YMalik_CH4-6_DRAFT.md) |
| **Chapters 2–3 + Appendix A (standing)** | Literature review (11 construct sections + theory treatment), research model with figure, 16 hypothesis sections, full measurement instrument, verified reference pool | [Read Ch. 2–3](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Research_Paper_YMalik_v4_master.md) |
| **Research model figure** | The 11-construct dual-pathway model diagram | [View figure](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Anchoring_Bias_Research_Model.png) |

## 2 · Data Collection Record (no participant data in this public repository)

| Document | What it contains | Link |
|---|---|---|
| **Screening method & exclusion log** | The full screening protocol and per-step exclusion accounting from the July export — methodology and counts only; respondent-level data withheld for confidentiality | [Screening log](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/03_Data/EXCLUSION_LOG_2026-07-22.md) |
| **Screening script (reproducible)** | The exact Python script that applies the cleaning protocol — every exclusion is mechanical, none discretionary | [clean_and_screen.py](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/03_Data/clean_and_screen.py) |
| **Survey instrument (as fielded)** | The full questionnaire (v2.1, post-pilot) | [Questionnaire](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Full_Survey_Questionnaire_v2.md) |
| **Live survey** | The fielded Qualtrics instrument | [Qualtrics link](https://fiu.qualtrics.com/jfe/form/SV_3lae5xJsPcRfIN0) |
| Recruitment record | CloudResearch setup, Prolific setup, LinkedIn/WhatsApp outreach kits, pilot plan and status | [Pilot status](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Pilot_Run_Status.md) · [CloudResearch guide](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/CloudResearch_Setup_Guide.md) · [Prolific guide](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Prolific_Setup_Guide.md) |

> **Confidentiality note:** raw and cleaned response-level datasets are deliberately excluded from this public repository (IRB-25-0462; platform terms). They are held privately by the student and available to the instructor on request through a secure channel.

## 3 · Project Governance

| Document | What it contains | Link |
|---|---|---|
| **Progress tracker (live status)** | Current state, deadlines, and the full status history of the final sprint | [PROGRESS_TRACKER](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/PROGRESS_TRACKER.md) |
| **Advisor meeting record** | Minuted directives from our May 20, May 30, and late-July meetings — the study's governing decisions | [Meeting record](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/00_Execution/Advisor_Meeting_Record.md) |
| Master execution plan + tasks | The governing plan (v2) and task ledger | [Plan](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/00_Execution/YMalik_Master_Execution_Plan_v2_ACTIVE.md) · [TASKS](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/00_Execution/TASKS.md) |
| Analysis playbook | The pre-registered EFA/reliability procedure (June 30 scope directive) | [EFA playbook](https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/EFA_Reliability_Playbook.md) |
| Correspondence archive | Dated record of all substantive advisor correspondence | [correspondence/](https://github.com/AuditingAI/Profile/tree/claude/scholar-links-review-Plgk6/dba/correspondence) |

## 4 · Full History

Every change to this project is version-controlled with a dated, descriptive message: [complete commit history](https://github.com/AuditingAI/Profile/commits/claude/scholar-links-review-Plgk6) — a verifiable audit trail of when each piece of work was done.

---

*Repository maintained by Yasir A. Malik · ymali001@fiu.edu*
