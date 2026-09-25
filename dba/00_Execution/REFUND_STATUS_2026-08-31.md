# The ~$980 — still not recovered, and two records disagree about why

**31 August 2026.** Scholar lane. Notion: [💰 The ~$980](https://app.notion.com/p/3cd4ffd38c7e81509e30d01426bfd43e) · calendar reminder set for Tue 1 Sep, 9:00 AM ET. Nothing has been sent. **Do not send the refund email in
`DATA_COLLECTION_CLOSEOUT.md` as it is currently written** — see §2.

---

## 1 · Where it stands

| | |
|---|---|
| **Amount** | **~$980** on Prolific, plus an unknown CloudResearch balance |
| **Recovered** | **$0** |
| **Age** | Study created **10 July** — **52 days**. Recovery plan written **23 July** — **39 days** |
| **Last verified** | 23 July, from the account dashboard. **Nothing has been checked since** |

Everything below turns on one thing nobody has looked at in five weeks: **the Prolific dashboard.**

---

## 2 · ⚠️ The two records contradict each other, and it matters

| | `Prolific_Recovery_Plan.md` · 23 Jul | `DATA_COLLECTION_CLOSEOUT.md` · 19 Aug |
|---|---|---|
| Study state | **Published 15 Jul, ACTIVE** | **"Awaiting Review" since 10 Jul, never launched** |
| Participants | **2 of 100 filled** | **Zero** |
| Payments | **2 submissions approved and paid** | **"No participants were paid"** |
| The money | **~$980 escrowed inside the running study**, balance $1.67 | Unused balance to be refunded |

**These cannot both be true**, and the difference is not cosmetic.

**The refund draft in the closeout says, in writing, "no submissions were collected and no
participants were paid."** If the recovery plan is the accurate one, that sentence is false — two
people were recruited and paid. Sending a false statement to a vendor about a study running under
IRB-25-0462 is not a small thing, and it is the kind of error that is very hard to walk back.

**So the first action is not an email. It is a two-minute look at the dashboard.**

---

## 3 · What to do, in order

### Step 0 · Screenshot before you touch anything — 2 minutes

**Before stopping, refunding, or closing anything**, capture the study page showing
**"Eligible participants: 20 of 334,976."**

That single screen is the **primary evidence for the central claim of the P1 manuscript** and for the
feasibility argument now on the public research page. If the account closes or the study is deleted
and that screen is gone, the finding rests on recollection. Screenshot it, and export the Qualtrics
responses in full — including partials, metadata and timestamps — while access still exists.

### Step 1 · Establish which record is true — 2 minutes

Open the workspace and read three things off it:

- Is the study **Active**, **Awaiting Review**, **Paused**, or **Completed**?
- How many submissions — **zero, or two approved**?
- What is the **available balance**, and what is committed to the study?

📎 Study submissions · `app.prolific.com/researcher/workspaces/studies/6a508fe494392aa43ed7a1ac/submissions`
📎 Finance · `app.prolific.com/researcher/workspaces/6a4e7265a79f3d33156014d0/finance`

### Step 2 · If the study is still ACTIVE — stop it

This is the part that actually releases the money. **Prolific charges only for approved
submissions; the rest of the committed budget returns to the workspace balance when the study
stops.** While it runs, roughly $980 stays escrowed and no refund request can reach it.

Stopping is the action. Emailing support before stopping achieves nothing.

### Step 3 · Then decide — refund or credit

| | When it is right |
|---|---|
| **Refund to the original method** | If the money is needed now, or if the survey arm is not relaunching |
| **Keep as credit** | If the dissertation relaunches on Prolific with a broadened population. Zero friction later, and ~$980 funds roughly 100–150 completions of a shorter instrument at professional-sample rates |

**This is not a purely financial decision and it should not be made alone.** It depends on whether
the survey arm relaunches at all — which is Dr. Rey's call, is already listed as an open item in
`IRB_STATUS_2026-08-28.md` §3–4, and has never been put to him. **Put both questions in the same
message.**

### Step 4 · Only then, the email — rewritten to match reality

Whichever draft goes out, the facts in it have to match what the dashboard actually showed. If two
participants were paid, the email says so. The methodological reason for withdrawing is strong
enough on its own — roughly twenty eligible against a target of one hundred — and it does not need
help from a claim that is not true.

**Keep point 3 of the existing draft either way:** confirmation that access to the study
configuration and prescreener results survives the closure. That is the manuscript's evidence.

### Step 5 · CloudResearch — confirm before asking

*"Payment in account required"* may mean money was **needed**, not that money was **sent**. Confirm a
balance exists before sending anything. Do not request a refund of an amount that was never
deposited.

---

## 4 · Two things that travel with this

- **Enable MFA on the Prolific account.** It holds real money and the account has been flagging this.
- **Rotate the shared platform credentials.** They were sent by email in plaintext, and a third party
  has been operating these accounts. That is worth doing regardless of how the refund resolves — and
  the access question is entangled with the authorship item in
  `../P1_Feasibility_Note/SUBMISSION_CHECKLIST.md`.

---

## 5 · The honest summary

Fifty-two days, nothing recovered, and the two files describing the situation disagree about whether
the study ever launched. **That is a record-keeping failure, not a Prolific failure**, and it is
worth naming plainly in a repository whose whole argument is that overstatement and drift are what
happen when nobody checks.

**Ten minutes on the dashboard settles all of it.**
