# 🤖 AI Reconciliation Workflow — Appendix A vs. IRB-Approved Instrument

**For Saturday morning (June 20, 2026, 9 AM–10:30 AM).** Estimated time: **60–90 minutes** (vs. 3 hours manual).

**The rule that never changes:** the IRB-approved instrument wording **wins** wherever they differ. AI helps you *see* the deltas; you make the call on whether each is non-substantive (use cleaner wording) or substantive (escalate before changing).

---

## What you need before you start

- [ ] `Research_Paper_YMalik_v4.docx` — your Appendix A is at the end
- [ ] `Updated Measurement Instrument – Malik, Y.docx` — the IRB-approved version (on your computer)
- [ ] The Pilot Feedback & Revision Log workbook open (you'll log every delta in the **Revision Log** tab)
- [ ] One of: **NotebookLM** (recommended), **Claude.ai**, or **ChatGPT**

> 💡 **Why NotebookLM is the best choice for this:** it only answers from sources you upload, so it cannot invent items that don't exist in either document. If you have to defend a wording decision later, the citation chip shows the exact passage. Claude.ai and ChatGPT both work fine but you need to read more carefully.

---

## ▶️ Setup — 5 minutes

### If using NotebookLM (https://notebooklm.google.com)

1. Create a new notebook: **`Instrument Reconciliation — Jun 20 2026`**
2. Upload **both** files: `Research_Paper_YMalik_v4.docx` and `Updated Measurement Instrument – Malik, Y.docx`
3. Wait for green checkmarks
4. Paste this verification prompt:
   ```
   Confirm both sources are loaded by listing their titles and the number
   of measurement items each contains. If either has fewer than 50 items,
   stop and tell me — the upload may be incomplete.
   ```
5. ✅ Done when the response confirms both docs are loaded.

### If using Claude.ai or ChatGPT

1. Start a new conversation
2. Upload **both** files as attachments
3. Paste this verification prompt:
   ```
   I've uploaded two documents:
   - Source A = Research_Paper_YMalik_v4.docx (Appendix A starts ~p. 30)
   - Source B = Updated Measurement Instrument – Malik, Y.docx (governs)

   Confirm you can read both, and quote the first measurement item from
   each so I know you have them open correctly.
   ```

---

## ▶️ The reconciliation loop — 5 minutes per construct × 11 = 55 minutes

Run these three prompts **once per construct**, in this exact order. Constructs: TA → RA → AT → SAP → FR → IR → RPG → PMI → AJQ → APR → RAB.

### Prompt 1 — Side-by-side extraction

Replace `[CONSTRUCT]` with the construct code (e.g., `TA`):

```
For the construct [CONSTRUCT], list every measurement item from BOTH
sources, in this exact table format:

| Item # | Appendix A wording (Source A) | IRB-approved wording (Source B) |
|---|---|---|

If a construct uses a different code in Source B (e.g., TRAIN instead of
TA), note that mapping at the top of the table. If either source has
fewer items than the other, list the extras with the missing cell blank.
Do not paraphrase — quote the wording verbatim from each source.
```

✅ **You should get back** a side-by-side table per construct.

### Prompt 2 — Classify each delta

```
For the same construct [CONSTRUCT], classify each row in the previous
table as one of:

  SAME        — wording is identical or trivially identical (whitespace,
                punctuation only)
  WORDING     — same construct meaning, different surface wording
                (non-substantive)
  SUBSTANTIVE — meaning has shifted; would change what the item measures
  A-ONLY      — item exists only in Appendix A (new); needs IRB amendment
                to use
  B-ONLY      — item exists only in IRB-approved instrument; must be
                included in the final survey

Output as a 3-column table: Item # | Classification | One-line reason.
Be conservative — if you're not sure something is non-substantive,
classify it SUBSTANTIVE.
```

✅ **You should get back** a classification table with one row per item.

### Prompt 3 — Final decision row for the Revision Log

```
Based on the classification, give me the ROW(s) I should paste into my
Pilot Revision Log workbook for the construct [CONSTRUCT]. One row per
non-SAME item. Columns:

  # | Date | Source/Pilot ID | Issue or Feedback | Severity | Decision |
  Action Taken | Advisor/IRB Review Needed? | Status

Use these conventions:
- Date: 2026-06-20
- Source/Pilot ID: "Pre-pilot reconciliation"
- Severity: Low for SAME/WORDING, Medium for A-ONLY, HIGH for SUBSTANTIVE
  or B-ONLY-missing
- Decision: "Use IRB-approved wording" (default), or "Escalate to advisor"
  for SUBSTANTIVE/A-ONLY
- Action Taken: leave blank, I'll fill after I apply it
- Advisor/IRB Review Needed: Yes for SUBSTANTIVE and A-ONLY; No otherwise
- Status: Open
```

✅ **You should get back** ready-to-paste rows for your Revision Log spreadsheet.

---

## ▶️ After all 11 constructs — 15 minutes

### Step A — Build the final reconciled item list

```
Now produce the final reconciled measurement instrument. For each
construct, list all items that will appear in the live Qualtrics survey,
using IRB-approved wording where available and Appendix A wording only
where an item is A-ONLY and you have flagged it for advisor escalation.

Mark each item with:
- (R) for reverse-coded items
- (AC) for attention checks
- (KEEP) for items that survive reconciliation
- (HOLD) for items pending advisor decision

Output as a clean Markdown document I can paste into the repo.
```

Save the output as `Reconciled_Instrument_2026-06-20.md` and drop it into your `dba/` folder.

### Step B — Identify what needs advisor escalation

```
Make me a short list of every SUBSTANTIVE delta and every A-ONLY item
that needs Dr. Rey's review before going into the survey. For each:
- Item code and construct
- The two competing wordings
- Why it matters (one sentence)
- My recommended path

Keep this list under 10 items if possible. If it's longer, group the
similar ones together.
```

✅ **If this list has zero items** → you're clear to build Qualtrics using the IRB-approved wording for everything. **Proceed to Saturday's 1 PM Qualtrics-build block.**
✅ **If this list has 1–3 items** → email Dr. Rey a single 5-line note with the questions; build Qualtrics with the IRB wording in the meantime; revise after he responds.
🛑 **If this list has 4+ items** → stop. Send the list to Dr. Rey before building. Substantive scope drift needs a real decision, not 4 separate decisions.

---

## What the AI is allowed to do (and what it isn't)

| ✅ AI can do | ❌ AI cannot do |
|---|---|
| Quote items verbatim from both sources | Decide whether a wording change is substantive (you decide) |
| Classify by surface similarity | Authorize an IRB scope change |
| Format Revision Log rows | Edit your Qualtrics survey for you |
| Produce a reconciled list | Sign off on face validity (that's the pilot's job) |

The AI is your reading assistant, not your IRB officer.

---

## What goes in the Revision Log

After this workflow you should have, in the Revision Log tab of the workbook:
- One row per non-SAME item across all 11 constructs (typical: 20–40 rows)
- Severity, decision, and advisor-review flag filled in
- Status = Open until you've actually applied each in Qualtrics

When you apply each in Qualtrics (the 1–5 PM block on Saturday), update Status = Closed and fill in Action Taken.

---

## If the AI hallucinates an item

NotebookLM should never do this (it's grounded in sources). If you're using Claude.ai or ChatGPT and something feels off:

```
You appear to have listed an item that I cannot find in either source.
Re-check the verbatim text from both uploaded documents and tell me
which document and which page that item appears on. If you cannot
locate it, drop it from the table.
```

---

## Saturday morning timing

| | Time | What |
|---|---|---|
| Block 1 | 9:00 – 9:05 | Setup (upload both files, verification prompt) |
| Block 2 | 9:05 – 10:00 | 11 constructs × 5 min each (Prompts 1–3 per construct) |
| Block 3 | 10:00 – 10:15 | Final reconciled list + escalation list |
| Block 4 | 10:15 – 10:30 | Send any advisor escalations; commit the reconciled list to repo |

By 10:30 AM you have a defensible, documented final item set. Walk away from screens until lunch. **1 PM is when the Qualtrics build starts.**
