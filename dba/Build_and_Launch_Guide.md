# 🛠️ Build & Launch Guide — Qualtrics, Pilot, CloudResearch

**Who this is for:** Yasir — the hands-on steps to clear the three blockers and go live. These are the things only *you* can do (they need your FIU + platform logins). I can't click through them for you, but this is the exact click-path.

**ADD rules (same as the NotebookLM playbook):** every step has ⏱ a time estimate, an **action verb**, and a **"✅ Done when…"** finish line. One thing at a time. Stop when a part is done — you don't have to do all four parts in one sitting.

**The order is fixed. Do not skip ahead.**
> Part A (build in Qualtrics) → Part B (test it) → Part C (pilot) → Part D (CloudResearch). Part E (MTurk) only if D underperforms.

**Total time:** Part A ≈ 2–3 hrs · Part B ≈ 30 min · Part C ≈ 3–4 days elapsed (mostly waiting) · Part D ≈ 1–2 hrs setup + collection window.

---

## 🔑 Before you start — gather these (10 min)

- [ ] FIU Qualtrics login (https://fiu.qualtrics.com — sign in with your FIU credentials)
- [ ] The **IRB-approved instrument** file (`Updated Measurement Instrument – Malik, Y.docx`) — this governs the wording
- [ ] **Appendix A** from `Research_Paper_YMalik_v4.docx` — the 55 items + demographics
- [ ] The **IRB-approved Informational Letter** (consent text) — goes on the first screen
- [ ] Your IRB protocol number handy: **IRB-25-0462**

---

# PART A — Build the survey in Qualtrics ⏱ 2–3 hrs

### A1 — **Create** the survey ⏱ 5 min
1. Go to **https://fiu.qualtrics.com** → sign in
2. Click **Create new project** → **Survey** → **From scratch**
3. Name it: `Auditors' Professional Judgments and Audit Work Practices`
4. Click **Create project**

✅ **Done when** you're looking at an empty survey editor.

---

### A2 — **Reconcile** Appendix A against the IRB-approved instrument ⏱ 30 min
This is the most important step. **The IRB-approved wording wins** wherever the two differ.

1. Open `Updated Measurement Instrument – Malik, Y.docx` and Appendix A side by side
2. Go construct by construct (TA, RA, AT, SAP, FR, IR, RPG, PMI, AJQ, APR, RAB)
3. For each item, ask: *does the approved instrument already have this item?*
   - **Same meaning, same wording** → use it as-is
   - **Same meaning, nicer wording in Appendix A** → this is a *non-substantive* change; you may use the cleaner wording, but **log it**
   - **New item not in the approved instrument** → this may need an IRB amendment. **Do not add it silently.** Flag for Dr. Rey / Topaz first.
4. Keep a running list of every delta in the **Revision Log** tab of `YMalik_Pilot_Feedback_Form_and_Revision_Log_READY_2026-06-01.xlsx`

✅ **Done when** you have one final, reconciled item list and a logged record of any wording change.

> ⚠️ If you're unsure whether a change is "substantive," treat it as substantive and ask Dr. Rey. Cheaper to ask than to breach IRB scope.

---

### A3 — **Build** the consent block (first screen) ⏱ 15 min
1. In the editor, the first block should be **Informed Consent**
2. Add a **Text/Graphic** question → paste the IRB-approved Informational Letter verbatim
3. Below it, add a **Multiple Choice** question: *"Do you consent to participate?"* → options **Yes / No**
4. Add **Survey Flow** logic (top-right **Survey Flow** button): if **No**, route straight to **End of Survey** with a polite thank-you message

✅ **Done when** selecting "No" ends the survey and "Yes" continues.

---

### A4 — **Build** the eligibility screeners ⏱ 20 min
Add these as a **Screeners** block right after consent:
1. *"Are you 18 or older?"* (Yes/No)
2. *"Do you currently, or did you recently, work in an audit role?"* (Yes/No)
3. *"How many years of audit experience do you have?"* (drop-down: <2 / 2–5 / 6–10 / 10+)
4. *"Do you have experience with recurring/long-term engagements or prior-period audit evidence?"* (Yes/No)

Then in **Survey Flow**, add a **Branch**: if `18+ = No` OR `audit role = No` OR `experience < 2 years` OR `long-term exposure = No` → route to a **screen-out** End of Survey ("Thank you, but you don't meet the eligibility criteria for this study").

✅ **Done when** an ineligible combination ends the survey gracefully, and an eligible one continues.

---

### A5 — **Enter** the construct blocks ⏱ 60–75 min
1. Create **one block per construct** (11 blocks): TA, RA, AT, SAP, FR, IR, RPG, PMI, AJQ, APR, RAB
2. In each block, add the 5 reconciled items as **Matrix Table** or individual **Likert** questions:
   - Scale: **5-point** — Strongly disagree / Disagree / Neither / Agree / Strongly agree
3. Mark your **reverse-coded item** in each block (note it in Qualtrics' question notes — you'll reverse it in analysis, not in display)
4. Add your **two attention checks** where the READY protocol specifies (e.g., *"Please select 'Disagree' for this item"*)
5. Add the **demographics block** last (experience, role, firm type, industry, credential, region)

✅ **Done when** all 11 construct blocks + demographics are entered and every item has a response option.

---

### A6 — **Randomize** block order ⏱ 5 min
1. Open **Survey Flow**
2. Wrap the 11 construct blocks in a **Randomizer** element → set **"Randomly present [all] of the following"** with **Evenly present elements** checked
3. Leave consent, screeners, and demographics *outside* the randomizer (those stay in fixed position)

✅ **Done when** the construct blocks are inside a randomizer and the consent/screener/demographics are not.

> Why: randomizing block order reduces order effects — which matters doubly for an *anchoring* study.

---

### A7 — **Set** anonymity + survey options ⏱ 10 min
1. Go to **Survey Options** (gear icon) → **Survey Protection / Security**
2. Turn **ON** "Anonymize responses" (do **not** record IP/location) — this matches your IRB language
3. Turn **ON** a **progress bar**
4. Turn **ON** "Prevent ballot-box stuffing" (one response per browser)
5. Add a **completion message** + (for later platform use) a **redirect/completion-code** screen
6. Set the survey to **force-response** or **request-response** on key items (your call; request-response is gentler)

✅ **Done when** anonymity is on, IP is not recorded, and a progress bar shows.

---

### A8 — **Add** the debrief screen ⏱ 5 min
Add a final **Text/Graphic** screen thanking the participant, restating that responses are anonymous, and giving your FIU contact + IRB protocol number (IRB-25-0462) for questions.

✅ **Done when** the last screen is a proper debrief.

---

# PART B — Test it before anyone sees it ⏱ 30 min

### B1 — **Preview** the eligible path ⏱ 10 min
1. Click **Preview** (top of editor)
2. Walk through as an **eligible** auditor: consent Yes → pass screeners → answer all blocks → reach debrief
3. Time yourself. **Target: 15–20 minutes.** If it's over 20, note redundancy candidates (do not delete items without Dr. Rey).

✅ **Done when** an eligible run reaches the debrief and lands in the 15–20 min window.

### B2 — **Preview** the screen-out path ⏱ 5 min
1. Preview again, this time answer a screener as **ineligible** (e.g., experience <2 years)
2. Confirm you hit the polite screen-out message and the survey ends

✅ **Done when** an ineligible run ends correctly.

### B3 — **Export** test ⏱ 10 min
1. Submit 2–3 preview responses
2. Go to **Data & Analysis** → **Export & Import** → **Export Data** → **CSV**
3. Open the CSV and confirm: variable names are sensible, every construct's items are present, and you can identify which item is the reverse-coded one for each construct
4. Confirm there is **no IP / location column** populated

✅ **Done when** the export's variable names and reverse-code flags match your analysis map, with no IP data.

### B4 — **Publish** + get the anonymous link ⏱ 5 min
1. Click **Publish**
2. Go to **Distributions** → **Anonymous Link** → copy it
3. This single anonymous link is what goes to pilot participants *and* later to CloudResearch

✅ **Done when** you have a live anonymous link you can open in a private/incognito window and complete.

> 🛑 **STOP here and get Dr. Rey's face-validity sign-off** before sending the link to anyone. This is blocker #2. Screen-share the preview with him (or send him the anonymous link to click through).

---

# PART C — Run the informed pilot ⏱ 3–4 days elapsed

Use `YMalik_Informed_Pilot_Protocol_READY_2026-06-01.docx` and the xlsx workbook as you go.

### C1 — **Pick** 6–10 pilot auditors ⏱ 20 min
1. From your LinkedIn audit contacts, pick 6–10 who meet eligibility (≥2 yrs, long-term-engagement exposure)
2. Log them as **P01–P10** (anonymous IDs only) in the **Pilot Participant Log** tab — **no employer/client names**

✅ **Done when** you have 6–10 names mapped to pilot IDs.

### C2 — **Send** the pilot invitation ⏱ 20 min
Send each a short, friendly message:
> Hi [name] — I'm running a brief academic survey for my FIU doctoral research on how auditors make professional judgments (IRB-25-0462). It's anonymous and takes ~18 minutes. I'd be grateful if you'd take it and then give me 2 minutes of feedback on clarity and length. Survey: [anonymous link]. Feedback form: [feedback link]. Thank you!

✅ **Done when** all invitations are sent and logged.

### C3 — **Collect** survey + feedback ⏱ 2–3 days (waiting)
1. Ask each to complete the **survey first**, then the **Feedback Form** (PF1–PF10)
2. Track completion time, confusing items, technical issues
3. Send one gentle reminder after 48 hours

✅ **Done when** you have ≥6 completed surveys + feedback forms.

### C4 — **Apply** decision rules ⏱ 1 hr
Use the decision table from the protocol (also in the dashboard's Pilot tab):
- Clarity < 4/5 or repeated confusion → **revise wording only**
- Construct-fit < 4/5 → review wording, **flag Dr. Rey** if meaning may shift
- Not natural for auditors → revise audit phrasing, **no new constructs**
- Time > 20 min / fatigue → review redundancy, **no item removal without Dr. Rey**
- Any suggestion to add AI / new populations / sensitive data → **STOP, flag for IRB**

Log every change in the **Revision Log** tab, then close the 6 gates in the **Decision Summary** tab.

✅ **Done when** all pilot feedback is logged, in-scope revisions are applied in Qualtrics, and the Decision Summary shows all 6 gates passed.

---

# PART D — CloudResearch (primary recruiting) ⏱ 1–2 hrs setup + collection window

Use `YMalik_CloudResearch_Launch_Draft_READY_2026-06-01.docx`.

### D1 — **Create** the account + project ⏱ 30 min
1. Go to **https://www.cloudresearch.com** → sign in / create a researcher account
2. Have your IRB protocol info ready
3. Create a new study/project; paste the **study title + short description** from the launch draft

✅ **Done when** a draft project exists in your CloudResearch dashboard.

### D2 — **Configure** screening + routing ⏱ 30 min
1. Set worker/auditor screening where available (occupation, US/Canada, approval history)
2. Set the participant link to your **anonymous Qualtrics link**
3. Set the return path: **redirect or completion code** — do **not** collect participant IDs inside Qualtrics
4. Enter the **fixed compensation** amount (confirm this with Dr. Rey first — blocker for full launch)

✅ **Done when** screening, the Qualtrics link, and the completion-code return are all configured.

### D3 — **Soft-launch** 10–15 responses ⏱ 1 day
1. Launch a small batch first (≈10–15)
2. Review: eligibility pass rate, attention-check performance, completion time, duplicate risk, export integrity
3. Flag anyone who misses 2 of 3 attention checks or completes unrealistically fast

✅ **Done when** the soft-launch batch is in and the quality checks look clean.

### D4 — **Full-launch** toward n = 60–80 ⏱ collection window
1. Only after soft-launch QA passes, scale to the full target
2. Monitor quality continuously; apply the same exclusion rules
3. Close at **n = 60 minimum / 80 target** valid responses after cleaning

✅ **Done when** you have 60–80 clean responses ready for the EFA + PROCESS analysis (paper § 4.4).

---

# PART E — MTurk backup ⏱ only if needed

Use `YMalik_MTurk_Backup_Launch_Draft_READY_2026-06-01.docx`. **Only** open this channel if CloudResearch yield or eligibility fit is insufficient after the initial window. Same Qualtrics instrument, same export map, same quality rules (95%+ approval, 100+ approved HITs, 2-of-3 attention-check exclusion).

---

## 🧭 If you get lost

Open the **dashboard** (`dba/dashboard.html`) → **Pilot launch** tab. It has the same steps as checkboxes that save your place. Tick them there as you go and the progress bar moves.

## 🚧 The three things blocking launch (in plain terms)
1. **Finish Part A + B** (build + test in Qualtrics) — *yours to do*
2. **Get Dr. Rey's face-validity sign-off** — *ask in the meeting*
3. **Get Dr. Rey's LinkedIn-copy sign-off + CloudResearch compensation amount** — *ask in the meeting*

Everything after that is the pilot (Part C) and CloudResearch (Part D), both of which already have READY drafts.

## ⚠️ Hard boundaries (do not cross without Dr. Rey + IRB)
- No AI/LLM items in *this* survey (they stay in future-research)
- No employer / client / account-level / confidential / sensitive personal data
- No new constructs or populations during the pilot — wording/flow revisions only
