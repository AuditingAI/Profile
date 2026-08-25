# 📡 Sharing the Survey Preview — Hosting & Feedback Channels

## TL;DR — what to actually share

**Pick one of these depending on what you want:**

| Option | URL pattern | When to use | Reliability |
|---|---|---|---|
| **A. GitHub Pages on main** (recommended) | `https://auditingai.github.io/Profile/Survey_Preview.html` (after one-time setup) | Public link, persistent, no warnings | 🟢 Highest |
| **B. Send the .html file directly** | Attach in WhatsApp / iMessage / email | When you only need 3–5 reviewers | 🟢 High |
| **C. htmlpreview.github.io wrapper** | `https://htmlpreview.github.io/?https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Survey_Preview.html` | Quick demo, no setup | 🟡 Works in browsers but rate-limited |
| **D. raw GitHub URL** | `https://raw.githubusercontent.com/AuditingAI/Profile/claude/scholar-links-review-Plgk6/dba/Survey_Preview.html` | Last resort — most browsers will *download* instead of render | 🔴 Low |

---

## ⚙️ Option A — Set up GitHub Pages (one-time, ~3 min)

This is the cleanest solution and the link never breaks.

1. Go to **https://github.com/AuditingAI/Profile/settings/pages**
2. Under **Source**, select **Deploy from a branch**
3. Choose branch: **`main`** (or `claude/scholar-links-review-Plgk6` if you want the preview from this branch)
4. Folder: **`/ (root)`**
5. Click **Save**
6. Wait ~1 minute. Page goes live at:
   `https://auditingai.github.io/Profile/dba/Survey_Preview.html`
   *(only if served from `claude/scholar-links-review-Plgk6` and the `dba/` path resolves; otherwise merge `Survey_Preview.html` to the main branch root or to `/dba/` on main)*

**The simplest variant:** copy `Survey_Preview.html` to the repo root on `main`, set Pages to deploy from `main`/`root`. URL becomes `https://auditingai.github.io/Profile/Survey_Preview.html`.

---

## ⚙️ Option B — Send the file directly (no hosting needed)

The HTML file is self-contained (~32 KB, no external dependencies). It runs **offline** in any modern browser.

How to send:
- **WhatsApp:** "Document" attachment → choose `Survey_Preview.html`
- **iMessage:** drag the file in, recipient taps to open in Safari
- **Email:** attach the file, recipient downloads + opens
- **LinkedIn DM:** the doc-attachment system works; recipient downloads + opens

**Trade-off:** every recipient needs to download. But for 3–5 audit-friend previewers, this is faster than setting up hosting.

---

## ⚙️ Option C — htmlpreview.github.io (quick, brittle)

Paste this anywhere as a tappable link:

```
https://htmlpreview.github.io/?https://github.com/AuditingAI/Profile/blob/claude/scholar-links-review-Plgk6/dba/Survey_Preview.html
```

It works in real browsers (Chrome on Pixel, Safari on iPhone) most of the time. **Rate-limited** for high volume. Don't post on LinkedIn to a wide audience — fine for DMs to a few people.

---

## 📥 Multi-channel feedback collection (already built into the HTML)

When a previewer reaches the thank-you page, they see **four ways** to send their feedback. Each one auto-fills with their actual feedback-page answers + an **anonymous 8-character Preview ID** (e.g., `K4N7QP2X`).

| Button | What happens | Best for |
|---|---|---|
| **📋 Copy feedback to clipboard** | Copies the formatted feedback. They paste anywhere. | Universal — works on every device |
| **💬 Share via WhatsApp** | Opens WhatsApp with text pre-filled; they pick the chat | Auditors who already chat with you on WhatsApp |
| **📱 Share via Text Message** | Opens SMS composer with text pre-filled | Quick mobile send |
| **✉️ Send via email** | Opens default mail app to yasiramalik@gmail.com with text pre-filled | Desktop reviewers |

**Why this is research-grade:** every channel produces an **identical structured feedback string** with the Preview ID. When responses arrive (by email, WhatsApp, SMS, or pasted into LinkedIn DM), you can paste them straight into a tracking spreadsheet keyed by Preview ID.

---

## 📊 Optional research upgrade — Google Form auto-collection (10 min setup)

For higher-volume previewers (>10) or when you want clean spreadsheet output, replace the multi-channel buttons with a single button that opens a pre-filled Google Form.

**Setup (one-time):**

1. Go to **https://forms.google.com** → start a blank form
2. Title: `DBA Survey Preview Feedback`
3. Add these fields (all short-answer / paragraph as noted):
   | Field | Type | Why |
   |---|---|---|
   | Preview ID | Short answer | Anonymous tracking |
   | Time on preview (seconds) | Short answer | Pacing data |
   | Clarity of wording (1–5) | Short answer | Quantitative |
   | Natural for auditors (1–5) | Short answer | Quantitative |
   | 15–20 min reasonable (1–5) | Short answer | Quantitative |
   | What was confusing | Paragraph | Qualitative |
   | Anything else | Paragraph | Qualitative |
4. Click **Send** → **Link** → toggle **Shorten URL** → copy the link
5. Right-click the form → **Get pre-filled link** → fill the fields with placeholder text → **Get Link** → copy
6. Send me (Yasir or your AI) the pre-filled link template; I'll wire it into the HTML so the buttons open the form with answers pre-filled

**Why this is a step up:** Google Forms auto-collects to Sheets, timestamps every response, lets you sort/filter, and exports cleanly to CSV for the eventual Chapter 5 methodology footnote.

---

## 🔒 Privacy & IRB notes

- The preview HTML **does not transmit anything** without an explicit tap on a share button.
- The Preview ID is **client-generated and anonymous** — there is no identity linkage.
- The page banner says "preview only" and "no data is recorded or transmitted from this page" — true.
- A Preview ID maps to a *specific browser session*, not to a person. Two previews from the same device get different IDs (each page load generates a new one).
- This is *informal previewer feedback*, not the IRB-covered pilot. No consent banner is required because no research data is being collected. The IRB-approved informational letter still appears (shortened) so previewers know what the live study would look like.

---

## ✅ Recommended workflow for tomorrow (Saturday)

1. **Saturday 9 AM — before reconciliation**: send 3–5 DMs with the htmlpreview link (Option C) to audit-friends you trust. *"Quick favor, 5-min preview, tap when convenient."*
2. **By Saturday afternoon**: most previewers will respond. Check responses by Preview ID; flag any item-clarity comments.
3. **Saturday 1 PM — Qualtrics build**: incorporate the live previewer feedback into the build. (Reverse-coded item too tricky? Drop the (R) marker. Audit-language complaint? Rewording stays in scope.)
4. **Saturday evening — commit revised list to repo**
5. **Sunday — pilot launch**: real 6–10 LinkedIn pilot with the (better-because-preview-tested) instrument.

---

## 🧪 What to test before sending the link to anyone

Open the file in **Chrome on your Pixel 10** (this is what your previewers will use). Walk through all 8 pages. Specifically check:

- [ ] Page 1 consent: "Begin" button advances
- [ ] Page 3 quality screen: tap the Likert pills, confirm they highlight correctly
- [ ] Page 4 reverse-coded item: tag "(reverse-coded)" visible
- [ ] Page 5 yellow-highlighted IMC: visually distinct from the other items
- [ ] Page 7 feedback: open-text areas work
- [ ] Page 8: all four buttons appear; tap **Copy feedback to clipboard** and confirm it copies; preview pane shows the formatted body
- [ ] Page 8: Preview ID shows (8 characters, e.g., `K4N7QP2X`)

If anything looks off, tell me and I'll fix it before you share.
