# 📱 Preview Test — Outreach Messages & Backlog Protocol

**Purpose:** before sending the link to real audit-professional previewers, get 3–8 friends/family/colleagues to tap through the survey on different devices so any technical issues surface first. Their *answers* don't matter — only that the survey *works*.

---

## ✅ What you'll capture from each tester

| Field | Source | Why |
|---|---|---|
| Preview ID (8-char, e.g. `K4N7QP2X`) | They paste it back to you | Anonymous tracking — confirms they actually completed the flow |
| Their device (iPhone / Android / Desktop) | Ask in your message | Catch device-specific issues |
| Any bugs / weirdness | Their reply | The whole point |
| Completion time | In their pasted feedback | Sanity-check the 15–20 min estimate |
| Did the feedback buttons work? | Their reply | Confirms the copy/whatsapp/sms/email channels |

---

## ✉️ Message templates — pick by audience and paste

### Template A — Close friends / family (most casual)

> Hey — tiny favor, ~5 min on your phone. I'm testing a survey for my doctoral research at FIU before I send it to real audit pros next week. **Click the link**, tap **"Yes, I understand"** on the first page, swipe through, and on the **last page tap "Copy feedback to clipboard"** — paste whatever it gives you back to me. Your actual answers don't matter for this — I just need to confirm the survey works on different devices. Also let me know if anything looked broken. Thanks 🙏
>
> 📎 [paste link or attach the HTML file]

### Template B — Colleagues / professional contacts (slightly more formal)

> Hi [name] — I'm finishing the survey for my FIU DBA dissertation and need to confirm it works on different devices before the real pilot. ~5 min on your phone. Tap the link, click **"Yes, I understand"** to start, walk through, and on the **last page** hit **"Copy feedback to clipboard"** and paste the result back to me. Doesn't matter what you select for the ratings — this is a tech test, not the real data collection. Also let me know if you spot anything visibly broken or wrong. Appreciate it.
>
> 📎 [paste link or attach the HTML file]

### Template C — Audit-adjacent contacts (could become real previewers later)

> Hi [name] — running a quick technical test on my FIU dissertation survey before the real audit-professional pilot next week. ~5 min on your phone. Tap the link, **click "Yes, I understand"** to start, walk through, and on the **last page tap "Copy feedback to clipboard"** and paste the result back to me. Answers don't need to be real — I just need to confirm the survey works on your device. If anything looks confusing or off, drop a quick comment too. Thanks!
>
> 📎 [paste link or attach the HTML file]

### Template D — Short LinkedIn DM (1 message, mobile-friendly)

> Quick favor — testing my dissertation survey link for tech before the real pilot. ~5 min. Tap → "Yes, I understand" → walk through → last page: "Copy feedback to clipboard" → paste back. Any answers fine, just confirming it works. Thanks!
>
> 📎 [paste link]

---

## 📋 Step-by-step instructions to include in EVERY message (optional)

If your tester is less tech-savvy, paste this short block at the bottom of any message above:

> **Quick guide:**
> 1. Tap the link / open the file on your phone
> 2. First page asks "Do you understand this is a preview?" — tap **Yes, I understand**
> 3. Tap through the questions — pick anything (answers don't matter for this test)
> 4. On the very last page, tap **📋 Copy feedback to clipboard**
> 5. Paste it back to me in this chat. Done!

---

## 🗂️ Backlog — track everyone you sent it to

A live tracking spreadsheet is in `dba/Preview_Test_Backlog.xlsx`. It has four tabs:

| Tab | What it tracks |
|---|---|
| **1. Send Log** | Who you sent the link to, when, on what channel — keyed by tester ID T01, T02, etc. |
| **2. Responses** | Preview IDs received back, device, completion time, any notes |
| **3. Issues Flagged** | Every bug, wording complaint, or "didn't work for me" comment with action status |
| **4. Summary** | Auto-summary of count sent / received / open issues |

### Privacy rule (important)

The **tester's real name / handle stays in tab 1 only** (the send log) and is **never tied to the Preview ID** in tab 2. That keeps the response side anonymous-equivalent — even if you forward the spreadsheet later, tab 2 alone reveals no identities.

---

## 🎯 Workflow when a tester responds

1. They paste back something like:
   ```
   Preview ID: K4N7QP2X
   Time on preview: 4m 12s
   Clarity: 4
   ...
   ```
2. Open the backlog spreadsheet
3. **Tab 2 (Responses):** new row → Preview ID = K4N7QP2X, link to their tester ID (T03), device, time, notes
4. **Tab 3 (Issues):** if they mentioned a bug or wording concern, add a row, set Severity, mark advisor-review flag if needed
5. **Tab 1 (Send Log):** mark their row as "Received"

That keeps the chain of evidence clean for Sunday's W06 weekly update, where you can honestly say *"5 informal testers walked the preview; 0 critical bugs; 2 wording revisions identified and applied before the live pilot."*

---

## ⚠️ What to do if a tester says something bad

| Tester said… | What to do |
|---|---|
| "Couldn't open the link" | Note the device, send the .html file directly as a WhatsApp document instead |
| "Some buttons didn't work" | Get their device + browser; replicate on yours; fix in the HTML before more sends |
| "Question X was confusing" | Log in Issues tab; don't change the live preview mid-send (consistency across testers matters) |
| "I think this is the real survey, sorry — I tried" | Reassure them: nothing was recorded; nothing happens unless they tap a share button |
| Silence after 24 hrs | Send one gentle nudge: "Hey, no rush, but did you get a chance to take a peek?" |

---

## 🌅 Recommended order of testing

| When | Who | Why |
|---|---|---|
| **Tonight (Fri evening)** | 1 close friend on iPhone, 1 close friend on Android | Cross-device smoke test — catches the showstoppers |
| **Saturday 8 AM** | 2 colleagues (any device) | Quick wording sanity-check before reconciliation block |
| **Saturday 10 AM** | 1–2 audit-adjacent contacts | More realistic perspective on audit-language fit |
| **Saturday afternoon** | Stop testing | Get to the Qualtrics build — testers are saturated |
