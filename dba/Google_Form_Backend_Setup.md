# 📊 Research-Grade Backend — Google Form + Sheet (3-min mobile setup)

**What you get:** every tester response auto-collected to a Google Sheet you control. Export to CSV / Excel / SPSS at any time. Timestamps automatic. Free, permanent, no servers, no broken links.

**Replaces:** the copy-paste feedback flow in `Survey_Preview.html` for actual data collection (the HTML stays useful as a UX demo if you want; you can use either or both).

---

## ⏱️ Setup in 3 minutes on your Pixel 10

### Step 1 — Open the Apps Script editor (30 sec)
1. In Chrome on your Pixel, go to **https://script.google.com**
2. Sign in with **yasiramalik@gmail.com**
3. Tap **+ New project** (top-left)
4. The project opens with a placeholder `function myFunction() { }`

### Step 2 — Paste the form-builder script (30 sec)
1. Tap into the editor area
2. **Select all** the placeholder code → delete
3. Open the file `dba/google_form_builder.gs` from the repo (or use the link below) → tap-and-hold → **Select all** → copy
4. Paste into the script editor

Direct link to the script (raw text — works on mobile):
**https://raw.githubusercontent.com/AuditingAI/Profile/claude/scholar-links-review-Plgk6/dba/google_form_builder.gs**

### Step 3 — Save and run (45 sec)
1. Tap the **💾 Save** icon (top of editor)
2. Optionally rename the project to *"DBA Preview Form Builder"*
3. Tap **Run ▶**
4. **First time only:** Google asks for permission to create files in your Drive
   - Tap **Review permissions** → choose your account → tap **Allow**
5. Script runs in ~5 seconds and writes URLs to the **Execution log** at the bottom

### Step 4 — Grab your three URLs (15 sec)
At the bottom of the script editor, you'll see a banner like:

```
========== DBA Preview Form READY ==========
FORM URL (share this with testers):
  https://docs.google.com/forms/d/e/.../viewform

SHORT FORM URL (better for WhatsApp):
  https://forms.gle/AbCdEfGhIjKlMn

EDIT URL (only you — to change questions later):
  https://docs.google.com/forms/d/.../edit

RESPONSE SHEET URL (your live backend):
  https://docs.google.com/spreadsheets/d/.../edit
============================================
```

**Copy the SHORT FORM URL** — that's what you paste into WhatsApp. It's <30 characters and looks clean.

### Step 5 — Open your backend (30 sec)
- Tap the **RESPONSE SHEET URL** → it opens in Google Sheets
- Bookmark it / add to home screen
- Every time a tester submits, a new row appears here automatically
- Each row is timestamped by Google

✅ **Done.** You now have a research-grade backend.

---

## 📝 Updated WhatsApp message — using the Google Form

Once you have the short Form URL, send this to your groups:

```
Hey y'all — 5-minute favor for my FIU doctoral research 🙏

Trying to confirm my survey wording reads naturally before I send
it to real audit professionals next week. Quick Google Form below
— just tap through and answer honestly.

What I need from you:
1. Tap the link
2. Pick a device + role
3. Tap any answers for the 3 sample items
4. Give me your real feedback on clarity / wording / length
5. Hit Submit

That's it. Anonymous, no contact info needed (optional field if
you want me to thank you).

🔗 [paste your SHORT FORM URL — looks like https://forms.gle/AbC123]

Massive help 🙏 — Yasir
```

---

## 📈 What the backend Sheet looks like

When a tester submits, you get a row like this:

| Timestamp | Preview ID | Device | Audit role? | Sample item 1 | Sample item 2 | Sample item 3 | Clarity | Audit-lang fit | Length reasonable | Confusing items | Anything else | Name (optional) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-06-20 09:14:33 | K4N7QP2X | iPhone | Yes — external audit | 4 | 5 | 4 | 4 | 5 | 4 | Reverse-coded item read awkwardly | Solid flow | (blank) |
| 2026-06-20 10:02:18 | (blank) | Android | Yes — internal audit | 4 | 4 | 5 | 5 | 4 | 4 | All clear | (blank) | Sara M. |

Sortable, filterable, exportable. Tap **File → Download → Comma-separated values** at any point for a clean CSV.

---

## 🔄 How this compares to the HTML preview

| Feature | HTML preview | Google Form |
|---|---|---|
| Shows the real survey's look-and-feel | ✅ | ❌ (Forms have their own UI) |
| Auto-collects to backend | ❌ (copy-paste only) | ✅ (Sheets) |
| Mobile-friendly | ✅ | ✅✅ |
| Hostable | ⚠️ (needs Netlify/Pages) | ✅ (Google hosts) |
| Timestamps automatic | ❌ | ✅ |
| Export to CSV / SPSS | (manual) | ✅ (built-in) |
| Anonymous | ✅ | ✅ |
| Setup time | (already built) | 3 min |
| Best for | Showing UX to early reviewers | Actual data collection from the test pool |

### My recommendation
- **HTML preview** for 1–2 close friends who want to see how the real survey will look
- **Google Form** for the 5–10 friends/family/colleagues you're actually trying to get research-grade feedback from
- Reference the **same Preview ID** field across both so you can link a tester's HTML walkthrough to their formal Form response (if they happened to do both)

---

## 🔗 Quick links

- Apps Script editor (where you paste the code): **https://script.google.com**
- The script (paste this in): **https://raw.githubusercontent.com/AuditingAI/Profile/claude/scholar-links-review-Plgk6/dba/google_form_builder.gs**
- Google Sheets help — exporting to CSV: **https://support.google.com/docs/answer/40608**
- Google Forms help — sharing form link: **https://support.google.com/docs/answer/2839588**

---

## 🧠 Why this is genuinely research-grade

| Property | Why it matters for your DBA |
|---|---|
| Every response timestamped server-side | Auditable provenance (can prove when feedback arrived, not after-the-fact) |
| Single canonical Sheet | No "did I miss a WhatsApp reply?" anxiety |
| Identical fields across all testers | Comparable across rows, can compute means / counts |
| Anonymous by default | Matches your IRB framing for the formal pilot |
| Exportable to SPSS-friendly CSV | Same analysis pipeline you'll use for the formal data |
| Optional name field | Lets you privately thank testers without contaminating analysis columns |
| Linked Preview ID column | Cross-references with the HTML preview backlog if a tester took both |

This is the bare minimum for research-grade backend collection. You can grow it later by adding a Pivot Sheet for descriptives, a Charts tab for at-a-glance summaries, or a Apps Script trigger that emails you when a high-severity comment comes in — but for tonight, the Form + Sheet is enough.

---

## ⚠️ Things to NOT do with this Form

- **Don't use this as the real pilot instrument.** The real one goes in FIU Qualtrics per IRB-25-0462. This Google Form is for *informal preview feedback only*.
- **Don't paste FIU/employer/client information** into the test. The Form is your personal Google account, not FIU-managed storage.
- **Don't ask testers for sensitive demographics** here. The Form is for surface-level UX feedback, not real data.

---

## ⏭️ If the Apps Script feels intimidating

**Alternative (slower but no code):** open https://forms.google.com → start a blank form → manually add the questions listed below.

Field list (copy-paste each title, set type as marked):

1. *"Preview ID (8-char code from HTML preview, optional)"* — Short answer
2. *"What device are you using?"* — Multiple choice: iPhone / Android phone / iPad-tablet / Desktop-laptop
3. *"Are you in an audit-related role?"* — Multiple choice: External / Internal / Other audit / No
4. *"My firm provides specific training on cognitive biases (such as anchoring) that can affect audit judgments."* — Linear scale 1–5
5. *"When I join a continuing engagement, I form my own view before reading prior auditors' conclusions."* — Linear scale 1–5
6. *"My work is reviewed by a qualified auditor who was not involved in forming the original judgment."* — Linear scale 1–5
7. *"Instructions and item wording were clear."* — Linear scale 1–5
8. *"The items sounded natural for an audit professional."* — Linear scale 1–5
9. *"A 15–20 minute version would feel reasonable."* — Linear scale 1–5
10. *"Which items were confusing or felt off?"* — Paragraph text
11. *"Anything else I should know?"* — Paragraph text
12. *"Your name (optional, not analyzed)"* — Short answer

Then tap **Responses → ⋮ → Select response destination → Create a new spreadsheet** to wire up the Sheet backend. Done.
