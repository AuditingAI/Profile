# Instrument v3 (Dissertation) — DRAFT FOR ADVISOR + IRB REVIEW
**Extends the validated qualifying-study instrument with the AI layer: Automated Anchoring · Sycophantic Confirmation · Recursive Epistemic Drift**
**Status: DO NOT FIELD until (1) advisor/committee sign-off and (2) IRB amendment to IRB-25-0462 (new items + broadened population) is approved.**

---

## 0 · Advisor Alignment Map — every change traces to Dr. Rey's own directives

| v3 change | Dr. Rey's words (from the minuted meetings) | Source |
|---|---|---|
| **Add exactly 3 AI boxes** (Automated Anchoring, Sycophantic Confirmation, Recursive Epistemic Drift) onto the intact core | *"Tweak the model by incorporating **2–3 boxes** related to AI and existing constructs"* | May 20, 2026 meeting (Notion minutes) |
| **Keep the 11-construct core intact** — same constructs, same theory, same hypotheses framework | *"Keep the existing research question and model without changes"* (the model survives; the AI layer attaches to it, not replaces it) | May 20, 2026 |
| **Timing: dissertation work begins now** | *"After completing research project, immediately begin working on dissertation"* | May 20, 2026 |
| **Broaden the population** to risk & assurance professionals | *"Consider adjusting the population of interest to a broader group... industry-adjacent roles rather than auditors specifically"* | Late-July 2026 resolution meeting |
| **Start collection very early; plan a realistic floor** | *"Start data collection very early — it may take a year"; "20–30 respondents as a meaningful threshold"* | Late-July 2026 |
| Future-research framing in the qualifying paper's final chapter | *"Include recommendations for further research that explicitly mention investigating the impact of new AI technologies"* | May 20, 2026 |

**The one deviation requiring his explicit sign-off:** trimming the core from 5 to 3 items per construct (§1.2). "Keeping everything intact" argues for the full 55-item core; reach and length argue for the trim. **Both versions are prepared — this is presented to Dr. Rey as his call, not assumed.** Everything else in this document is execution of direction he has already given.

---

## 1 · Design decisions (the three that matter)

1. **Length budget: ≤ 12 minutes.** The v2 instrument (73 items, ~18 min) was too long for a scarce professional audience. v3 targets ~55 total items ≈ 10–12 min, which also improves panel economics (~$4.50–5.00/complete at fair hourly rates).
2. **Core shortened to 3 items per construct (33 items).** The 11-construct core keeps its strongest 3 items per scale (selection finalized after the simulated-data/EFA exercise identifies best-loading items; interim selection below is face-validity based, marked ⭑). The full 5-item pools remain available in Appendix A of the manuscript if the committee prefers length over reach.
3. **New AI layer: 3 measured constructs + 1 exposure moderator (19 items).** Items drafted to the same house style: 5-point Likert, one reverse-coded (R) item per construct.

## 2 · Revised screeners (broadened population — requires IRB amendment)

| # | Screen | Wording (v3) |
|---|---|---|
| S1 | Location | Are you currently located in the United States? *(unchanged; international expansion = separate amendment)* |
| S2 | Language | Are you fluent in English? *(unchanged)* |
| S3 | **Role (BROADENED)** | Are you currently, or have you been within the last 24 months, employed in a **risk, audit, compliance, controls, or review role** — external audit, internal audit, enterprise risk management, compliance testing, credit/loan review, quality assurance, or SOX/controls testing? |
| S4 | **Recurring reviews (BROADENED)** | Does (or did) your role involve assessing the **same entity, account, process, or portfolio across multiple periods** (e.g., year-over-year, quarter-over-quarter)? |
| S5 | Attestation | Confirm you are completing this survey on your own, have not seen it before, and will not share it. *(unchanged)* |
| S6 | **AI exposure (routing, NOT exclusion)** | In your review work, how often do you use AI tools (e.g., ChatGPT/Copilot-type assistants, firm AI tools, automated analytics that produce conclusions)? Never · Rarely · Monthly · Weekly · Daily. **Display logic:** respondents answering "Never" skip the SC block (can't rate a tool they don't use) and receive the AA/RED items framed on "automated systems" generally. |

## 3 · NEW construct blocks (drafted items)

**Block AA — Automated Anchoring** *(the anchor is machine-generated, continuous, at scale)*
1. System-generated figures (analytics outputs, AI summaries, dashboards) are typically the starting point for my assessments.
2. When a system produces an expected value, my review begins from that value rather than from the underlying evidence.
3. The volume of system-generated output makes it impractical to re-derive expectations independently.
4. **(R)** I form my own expectation before looking at any system-generated figure.
5. Automated outputs arrive already framed as conclusions, which shapes what I choose to test.

**Block SC — Sycophantic Confirmation** *(the model affirms the stated position)*
1. When I share my preliminary view with an AI tool, its response usually supports my view.
2. If I push back on an AI tool's answer, it tends to change its answer to agree with me.
3. It is easier to get an AI tool to confirm a conclusion than to refute one.
4. **(R)** AI tools I use often surface evidence that contradicts my initial position.
5. AI tools I use rarely challenge the assumptions built into my prompts.

**Block RED — Recursive Epistemic Drift** *(models redoing the same work converge)*
1. Different AI tools applied to the same work tend to produce very similar conclusions.
2. AI-assisted work products in my area often reuse or restate earlier AI-generated content.
3. When AI output is checked using another AI tool, errors tend to persist rather than get caught.
4. **(R)** Our process reliably detects when an AI-generated conclusion merely repeats an earlier one.
5. Over time, AI-assisted work in my area has become more uniform in reasoning and language.

**Block ATU — AI Tool Use (moderator/descriptive, 4 items)**
1. AI tools are formally part of my team's review workflow.
2. I rely on AI tools for drafting or summarizing work papers or findings.
3. My firm provides approved AI tools for review work.
4. I have received guidance or training on appropriate reliance on AI outputs.

**Retained:** 2 attention checks · 1 open-text item (reworded: "Describe a time an automated or AI-generated figure influenced your judgment…") · demographics (add: role family from S3 list; AI-tools-in-use free text).
**Core (33):** ⭑interim keep-list = items 1, 2, 5 of each qualifying-study construct (final list set after the EFA exercise).

**Count: 5 screens + 33 core + 19 AI-layer + 2 AC + 1 open + ~8 demo ≈ 68 questions ≈ 11–12 min** (shorter than v2 despite the new layer, because the core is trimmed).

## 4 · Qualtrics build — click path (~2 hours)

1. fiu.qualtrics.com → Projects → your survey → **⋯ → Copy Project** → name `Anchoring_AI_v3_Dissertation`. *(Never edit the fielded v2.1 — it is the audit record.)*
2. Block 00 consent: swap in the **amended IRB consent letter** once approved (new population + new items must be reflected).
3. Edit screeners S3/S4 per §2; add S6 with **Display Logic** (Survey Flow → branch on S6 = Never → hide Block SC).
4. Trim core blocks to the 3 ⭑ items each (delete, don't rewrite — preserves validated wording).
5. Add Blocks AA, SC, RED, ATU (matrix questions, same 5-point scale; mark (R) items in your codebook).
6. Keep both attention checks; keep anonymization/bot/duplicate settings (they carried in the copy).
7. **Fix the completion-code handshake** (the v2 "NO CODE" problem): Survey Flow → End of Survey → *Redirect to URL* → paste the Prolific completion URL when the study is created. Guide: https://researcher-help.prolific.com/en/articles/430328
8. Preview end-to-end twice (once as AI-user, once as S6=Never) → Publish → new anonymous link.

## 5 · Audience + money (the paid-panel relaunch)

**Money first — recover the ~$980 (10 min, do today):**
1. Stop the old study: https://app.prolific.com/researcher/workspaces/studies/6a508fe494392aa43ed7a1ac/submissions (screenshot "20 of 334,976" first — it's manuscript evidence).
2. Funds release to workspace balance: https://app.prolific.com/researcher/workspaces/6a4e7265a79f3d33156014d0/finance → **keep as credit** for this relaunch (zero friction) or request refund via support.

**Audience test (free, before IRB even clears):** create a **draft** study → Audience screeners: Employment *full-time* + Industry *Accountancy/banking/finance* (+ *Insurance* variant) → read the live **"Eligible participants"** counter. v2's fatal number was 20; the broadened cut should be in the thousands. Record the counts — they go straight into the dissertation's sampling-plan justification.

**Launch math (after IRB amendment):** 12-min instrument at $4.50–5.00/complete → recovered ~$980 covers **~150–180 completes** including fees; platform-broad screeners + S3/S4 as the true in-survey gate (compensate screen-outs pro-rata per Prolific policy). Soft-launch 10 → check quality at 48h → scale. Run CloudResearch Connect in parallel (guide in repo) so no single panel is the bottleneck.

## 6 · Order of operations

| # | Step | Owner | Gate |
|---|---|---|---|
| 1 | Stop old study, recover $, screenshot evidence | **Yasir (today)** | none |
| 2 | Free draft-study eligibility counts | **Yasir (today)** | none |
| 3 | Advisor/committee review of this v3 draft | Yasir → Dr. Rey/committee | dissertation-stage sign-off |
| 4 | IRB amendment (population + items + consent) | Yasir files; Claude drafts language on request | **HARD GATE** |
| 5 | Qualtrics v3 build (§4) | Yasir clicks; Claude supplies item text | after 3 |
| 6 | Prolific + CloudResearch launch (§5) | Yasir | after 4 |
