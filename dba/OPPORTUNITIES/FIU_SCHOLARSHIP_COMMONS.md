# FIU Scholarship Commons — the institutional repository

**Filed 10 September 2026.** Scholar lane. Source: the announcement from **Dr. Miguel Aguirre-Urreta,
Director of Doctoral Programs**, and the submission guide saved beside this file as
[`FIU_Scholarship_Commons_guide.pdf`](FIU_Scholarship_Commons_guide.pdf).

**Repository:** https://digitalscholarship.fiu.edu/
**Collection:** College of Business → *Doctorate in Business Administration – Student Research*
**Help:** `dcc@fiu.edu`

---

## 🔴 Read this first: nothing you have today is eligible

The announcement sets one gate, and it is the whole story.

> The repository is **not for research-in-progress work.** Work must be **externally validated**,
> meaning accepted by somebody outside the DBA program. Dissertations are deposited elsewhere.

Held against that gate, the current inventory:

| What exists | Where | Eligible? | Why not |
|---|---|---|---|
| P1 manuscript, full draft | `dba/Research_Paper_YMalik_FULL_DRAFT.docx` | ❌ | Never submitted anywhere. No external acceptance |
| Module 2 deck and write-up | `dba/coursework/GEB7365_International_Business/` | ❌ | Coursework. Graded inside the program, which is the definition of internal |
| Memo 4 and the qualitative memos | `dba/coursework/GEB7911_.../` | ❌ | Coursework |
| The prevalence finding, 334,976 → ~20 → 4 | `dba/RISK_QUANT/` | ❌ | A result, not a publication. It needs a venue first |
| Research status deck | `dba/00_Execution/RESEARCH_STATUS_DECK.pdf` | ❌ | Internal status reporting |
| Dissertation | not written | ❌ | Explicitly routed elsewhere, not to this collection |

**So this is not a thing to do this month.** It is a thing to build toward, and it changes what
"finished" means for two pieces of work already on the calendar.

---

## The one path that opens the door

```
GEB 7365 Formal Report (9 Oct, Newburry's format, ≤30 pages)
        ↓  rewrite out of coursework voice
AIB-LAC 2027 Doctoral Consortium / PDW (deadline 20 Nov 2026)
   or   AIB Kuala Lumpur 2027 paper (deadline Jan 2027, TBD)
        ↓  acceptance = external validation by people outside the DBA program
FIU Scholarship Commons, DBA Student Research collection
        ↓  DOI assigned
Google Scholar indexes it in 4 to 8 weeks
```

⚠️ **Corrected 11 Sep 2026.** This file first recorded 20 November as the AIB submission window. It
is not. **The AIB-LAC paper deadline is 30 September 2026**; 20 November covers posters, the
Doctoral Consortium and PDWs. Source: Newburry Session 4 deck, slide 28. The 30 September paper
deadline falls **nine days before the course report is due**, so the Doctoral Consortium is the
realistic route and Kuala Lumpur in January is the realistic paper route.

That chain matters more than it looks. It is the first route by which anything in this repository
becomes a **citable object with a DOI** rather than a file on a branch. Everything currently on the
Scholar profile points at GitHub. GitHub is a record. A DOI in an institutional repository is a
citation.

**The AIB Latin America deadline is the real gate, not the repository.** Track it in
[`README.md`](README.md).

---

## ⚠️ The accessibility bar, and why it fails today

New submissions must meet **WCAG 2.1 AA**. The guide is blunt about the consequence: documents that
do not meet it "may be returned to the submitter for correction, and publication may be delayed or
withheld." Anything posted or updated must clear it now to survive the **April 2027** deadline.
**PDF/A-2u is the recommended format.**

Required in every submitted document:

- searchable and selectable text
- properly structured headings, lists, and tables
- **alternative text for every meaningful image, chart, and figure**
- a logical reading and tab order
- meaningful hyperlink text, not bare URLs
- sufficient colour contrast
- captions or transcripts for embedded multimedia
- accurate document properties, including **title and language**

### Verified 10 Sep 2026: every PDF in this repository would fail

Checked directly for the tag structure a screen reader needs:

| File | `/StructTreeRoot` | `/Lang` | Verdict |
|---|---|---|---|
| `00_Execution/RESEARCH_STATUS_DECK.pdf` | absent | absent | untagged |
| `coursework/.../Malik_FIU_DBA_Module2_Deck.pdf` | absent | absent | untagged |
| `Research_Paper_YMalik_FULL_DRAFT.pdf` | absent | absent | untagged |

This is not a surprise and it is not a defect in the writing. It is what the build chain produces:
`reportlab` and `python-pptx` draw pages, they do not tag them. An untagged PDF is a picture of a
document as far as assistive technology is concerned.

**The fix is already in hand and does not require new tooling.** `build_dba_doc.py` writes native
Word Heading 1 / Heading 2 / List Bullet styles, which is exactly the structure the standard wants.
The route to a compliant file is therefore:

1. build the `.docx` with `build_dba_doc.py`
2. open it in Word, run **Review → Check Accessibility**, clear everything it flags
3. **Save as PDF with "Document structure tags for accessibility" ticked**, not Print to PDF

**Changed 10 Sep 2026 in service of this:** `build_dba_doc.py` now writes **alt text on every image**
(`alt` key in the spec, falling back to the caption), sets the **document title and author**, and
declares the **document language**. Those were the three things a checker flags first and they were
all missing. Memo 4 was rebuilt and now carries a real alt-text description of the three-link chain
figure.

**Absolute-positioned artefacts stay a problem.** The decks built by `python-pptx` and the PDFs built
by `reportlab` have no structure to tag. If a deck ever needs to go into the repository it gets
rebuilt through PowerPoint with real placeholders and alt text, or it does not go in.

---

## Rules that will bite if ignored

**One DOI per record. Never a second.** The guide is emphatic:

> DO NOT create a second DOI if you update or reload the same article (this requires our assistance).
> This will cause some DOIs that point to your work to become a broken link and make your work less
> discoverable.

To correct or replace a submitted document, email `dcc@fiu.edu`. Do not resubmit.

**Choose the collection carefully.** Departments manage their own collections and can ask for a work
to be removed if it lands in the wrong one. The correct target is
*Doctorate in Business Administration – Student Research*.

**Sign in with FIU credentials**, then Submissions. Allow up to 20 minutes for a work to appear, and
check the collection page rather than the dashboard.

**Google Scholar indexing takes 4 to 8 weeks** for a well-configured institutional repository. Plan
around it. A deposit made the week before a job application does not exist yet as far as Scholar is
concerned.

---

## What to do, and when

| When | Action |
|---|---|
| **Now** | Nothing to submit. This file is the record so the announcement does not vanish into email |
| **30 Sep** | 🔴 AIB-LAC **paper** deadline. Almost certainly skipped: no data, and the course report is not due for another nine days |
| **9 Oct** | GEB 7365 Formal Report, in Newburry's format from the start, so any submission is a rewrite and not a rebuild |
| **20 Nov** | AIB-LAC **Doctoral Consortium / PDW** deadline. The realistic first external submission |
| **Jan 2027** | AIB Kuala Lumpur paper deadline, TBD. The realistic first external *paper* |
| **On acceptance** | Prepare the accessible PDF/A-2u, then submit to the DBA Student Research collection |
| **Before April 2027** | Any earlier deposit must meet WCAG 2.1 AA or lose continued access |
