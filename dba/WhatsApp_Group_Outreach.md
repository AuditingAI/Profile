# 📱 WhatsApp Group Outreach Kit

**For posting to 1–3 friend groups** (not 1-on-1 DMs — different tone). Goal: 5+ smoke testers across iOS/Android by Saturday noon.

---

## 🔄 Reset / fresh-start guarantee — already baked in

Each tester gets a brand-new preview on every open. Verified:

| Check | Status |
|---|---|
| Preview ID regenerated every page load | ✅ |
| Timer starts at zero every open | ✅ |
| No localStorage / sessionStorage / cookies persisting responses | ✅ |
| No autofill from URL parameters | ✅ |
| Form fields are blank every load | ✅ |

So you can share the same link in multiple groups without worry — one tester's answers cannot bleed into another's. If a tester reloads or hands their phone to someone else, the next session is clean.

If you want to "reset everything" on the dashboard / checklist tools (which **do** use localStorage), each file has a built-in **Reset** button — use those if you've been ticking practice boxes.

---

## ✉️ Three message variants — copy, paste, send

### 📣 Variant 1 — Audit / professional friends group

> Hey everyone 👋 — quick favor if anyone has 5 spare minutes today or tomorrow.
>
> I'm wrapping the survey for my FIU doctoral research on auditor judgment and I need to confirm it actually works on different devices before sending it to real audit pros next week.
>
> **If you're in:**
> 1. Tap the link below
> 2. Click *"Yes, I understand"* on the first page
> 3. Walk through (~5 min — pick anything, your answers don't matter for this)
> 4. On the **LAST page**, tap **📋 Copy feedback to clipboard**
> 5. Paste whatever it gives you back to this chat (or DM me)
>
> Nothing is recorded. No personal info anywhere. Just helping me catch any bugs before the real thing.
>
> 🔗 [link or attached file]
>
> Even one of you would be a huge help 🙏 — Yasir

### 📣 Variant 2 — Family / close-friends group (more casual)

> Hey y'all — random favor 🙏
>
> Testing a survey link for my FIU doctoral research. Need a few people to tap through on their phones to make sure it isn't broken on iPhone vs Android.
>
> **5 minutes, no real answers needed:**
> 1. Tap the link
> 2. Click *"Yes, I understand"*
> 3. Swipe through, tap any answers (doesn't matter)
> 4. Last page → tap **📋 Copy feedback to clipboard**
> 5. Paste whatever comes out back to this chat
>
> Nothing personal recorded, promise. Just need to know it works before the real thing goes out.
>
> 🔗 [link or attached file]
>
> Love you all — Yasir

### 📣 Variant 3 — FIU / academic / mixed-professional group

> Hi all — DBA dissertation update + small ask 📚
>
> I'm running a quick technical test on my qualifying-exam survey before the formal pilot launches with real audit professionals next week. If anyone here has 5 minutes today or tomorrow, the help is gold.
>
> **What to do:**
> 1. Tap the link
> 2. Click *"Yes, I understand"* (it's just a preview — not the real data collection)
> 3. Walk through the questions (any answers are fine)
> 4. On the final page, tap **📋 Copy feedback to clipboard**
> 5. Paste it back here or DM
>
> Also — if anything in the audit-related wording looks off or confusing, that note alone is worth more than the technical confirmation. Reply with what stood out.
>
> 🔗 [link or attached file]
>
> Thanks all — Yasir

---

## 🎬 What testers will see — page-by-page

So you know what to expect when they ask "what is this?":

| Page | What they see | What they do |
|---|---|---|
| 1 | "Preview only — not data collection" banner + 2 options | Tap **Yes, I understand** |
| 2 | One sample eligibility question | Tap Yes or No |
| 3 | Three quality-check items (attention commitment + IMC + audit context) | Tap responses |
| 4 | Five Likert items from different constructs (incl. one reverse-coded) | Tap responses |
| 5 | One highlighted IMC + six more Likert items | Tap responses |
| 6 | Open-text + 2 demographic questions | Type a sentence + tap |
| 7 | **Preview feedback page** — 3 Likert + 2 open-text about the preview itself | This is the part that matters! |
| 8 | Thank-you page with 4 share buttons + 8-char Preview ID | Tap **📋 Copy feedback to clipboard** → paste back to you |

---

## 📝 Worked sample — what a real trial run looks like

This is a realistic example of what your testers will paste back into the chat. Save this as your mental template:

```
Hi Yasir — feedback on the survey preview.

Preview ID: K4N7QP2X
Time on preview: 4m 12s

RATINGS (1=Strongly disagree, 5=Strongly agree):
  Clarity of wording:               4
  Natural for auditors:             5
  15-20 min feels reasonable:       4

WHAT WAS CONFUSING OR OFF:
The reverse-coded item on page 4 felt awkward to read at first — took
me a second to realize I should *disagree* to be saying "yes I do
follow procedures." Maybe move it lower so people are warmed up.

ANYTHING ELSE:
Nice flow overall. The yellow attention-check item really stands out
which is good. One nitpick: on my iPhone the "Begin" button on page 1
felt a tiny bit small for my thumb. Otherwise solid.

— Sent from the preview page
```

### What you log in the backlog from this single response

**Tab 1 (Send Log):**

| T-ID | Name | Relationship | Channel | Device | Sent | Reminder | Response | Notes |
|---|---|---|---|---|---|---|---|---|
| T01 | Sara M. | Friend | WhatsApp "Audit Crew" group | iPhone 15 | 2026-06-20 | No | Yes | Took it twice — once at home, once on the train |

**Tab 2 (Responses) — anonymous-equivalent, no name:**

| Preview ID | T-ID | Device | Browser | Date | Time | Clarity | Audit-Fit | Length |
|---|---|---|---|---|---|---|---|---|
| K4N7QP2X | T01 | iPhone 15 | Safari | 2026-06-20 | 4:12 | 4 | 5 | 4 |

**Tab 3 (Issues Flagged):**

| # | Date | Reporter | Type | Description | Severity | Action | Status |
|---|---|---|---|---|---|---|---|
| 1 | 2026-06-20 | T01 | Wording | Reverse-coded item on p.4 read awkwardly until the reader oriented | Low | Confirmed (R) marker visible — keep wording for now, monitor in real pilot | Closed |
| 2 | 2026-06-20 | T01 | UI | "Begin" button tap target small on iPhone | Low | Increase button to min-height 48px in CSS | Open |

**Tab 4 (Summary) will then auto-show:**
- Total testers sent: 1
- Responses received: 1
- Open issues: 1
- Closed issues: 1
- High-severity issues: 0

---

## 🎯 What "success" looks like by Saturday noon

| Metric | Target |
|---|---|
| Total testers contacted | 5–10 |
| Responses received | ≥5 |
| Devices covered | At least 1 iPhone + 1 Android + 1 desktop |
| Open High-severity issues | **0** (any High = fix before pilot) |
| Open Low/Medium issues | ≤ 3 (defer to post-pilot if non-blocking) |

If you hit those numbers, you can honestly write in Sunday's W06 Weekly Update:

> *"Five informal testers walked the preview across iOS / Android / desktop. Zero critical bugs identified. Two non-substantive wording revisions flagged and applied before the live pilot launch."*

That single sentence in your weekly is **exactly** the kind of "meaningful progress" Dr. Rey said he wants. You'll have evidence to back it.

---

## 🚧 If a tester says something genuinely concerning

| They say | You do |
|---|---|
| "Question X seems to be measuring something different than it claims" | Log as **High** severity, do NOT change wording, escalate to Dr. Rey before pilot |
| "The consent block didn't make it clear this is academic research" | Log as **Medium**, update banner text, no IRB amendment needed |
| "It crashed / didn't load" | Log as **High**, get device details, replicate, fix immediately |
| "I see audit-specific wording that doesn't match what we'd actually say" | Log as **Medium**, propose wording revision (non-substantive only), apply pre-pilot |
| "I think you should add a question about [new construct]" | Politely thank them. Do **not** add. That would be a substantive IRB change. |

---

## 📤 Send sequence — recommended for tonight + tomorrow morning

| When | Group | Variant | Expected responses |
|---|---|---|---|
| Tonight (Fri evening) | Closest friends/family group | Variant 2 | 1–2 by morning |
| Saturday 8 AM | Professional / audit-adjacent group | Variant 1 | 2–4 by noon |
| Saturday 10 AM | FIU classmates / mixed academic group | Variant 3 | 1–3 by noon |
| Saturday 12 PM | **Stop** sending | — | Tally results, prep build |

That gives you Saturday afternoon (1–6 PM) free for the Qualtrics build, with real data on what your testers experienced informing every decision you make in the build.

---

## 📎 What to attach to the WhatsApp message

**Best on phones:** attach the file `Survey_Preview.html` as a **Document** in WhatsApp. Recipient taps it → opens in their default browser → no hosting needed.

**Alternative:** if you've set up Netlify Drop or GitHub Pages (see `Survey_Preview_Sharing_Guide.md`), paste the URL instead.
