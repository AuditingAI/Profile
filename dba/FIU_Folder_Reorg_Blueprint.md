# FIU-DBA 7.10 — Folder Reorganization Blueprint
**Target:** `C:\Users\yasir\OneDrive - Florida International University\FIU-DBA 7.10`
**Principle:** nothing is deleted — unused files go to a quarantine folder you empty manually after 30 days.

## The target structure ("the house")

```
FIU-DBA 7.10\
│
├── 00_READ_FIRST\                 ← the top of the house: what you open daily
│     Research_Paper_FULL_DRAFT.pdf      (the complete manuscript)
│     STUDY_OVERVIEW.pdf                 (whole study, highlights, red shortcomings)
│     OPEN_QUESTIONS_to_resolve.docx     (your live to-do)
│     REVIEW_INDEX link.url              (the GitHub dashboard)
│
├── 01_NotebookLM_Library\         ← everything you upload to NotebookLM to learn from
│     (drop the NotebookLM_Source_Pack contents here, plus course books/PDFs
│      you're reading while defining the dissertation research)
│
├── 02_GEB7913_Research_Project\   ← the current course, live work
│     Manuscript\        (chapter files, appendix, references)
│     Data_PRIVATE\      (Qualtrics exports, cleaned CSVs — NEVER share/upload)
│     Correspondence\    (all Dr. Rey emails, meeting confirmations)
│     Admin_IRB\         (IRB-25-0462 letters, consent forms, amendment drafts)
│     Simulated_Exercise\ (Dr. Rey's dataset when it arrives + Jamovi outputs)
│
├── 03_Dissertation_Pipeline\      ← where the next phase grows
│     AI_Audit_Risk_Research\  (research brief, verified sources, scholar alerts)
│     Sampling_Relaunch\       (Prolific relaunch guide, IRB amendment, screeners)
│
├── 04_Course_Archive\             ← completed terms/courses (read-only history)
│     (one subfolder per prior course/term, moved as-is)
│
├── 05_Reference_Library\          ← books, standards, methods texts (PCAOB, Hair, etc.)
│
├── _UNSORTED_REVIEW\              ← script puts anything it can't classify here
└── _TO_BE_DELETED_REVIEW\         ← obvious duplicates/superseded versions; empty manually after 30 days
```

## The rules the script applies (safe by design)
1. **Dry-run first.** The script's default mode only PRINTS what it would do. You review, then re-run with `-Apply`.
2. **Move, never delete.** Suspected-obsolete files (names containing `old`, `copy`, `backup`, `v1`, `superseded`, `~$` temp files) go to `_TO_BE_DELETED_REVIEW`, everything unrecognized to `_UNSORTED_REVIEW`.
3. **Inventory first.** Run `-Inventory` to produce `FIU_inventory.csv` listing every file. Send me that CSV and I'll tailor the rules to your actual files before you apply anything.
4. **OneDrive-safe:** plain `Move-Item` within the synced folder — history preserved by OneDrive versioning.

## Daily workflow after reorg
- Morning: open `00_READ_FIRST` — everything current is there.
- Learning: open NotebookLM ↔ `01_NotebookLM_Library` (same sources both places).
- Working: `02_GEB7913...` until submission; `03_Dissertation_Pipeline` after.
- Monthly: glance at `_TO_BE_DELETED_REVIEW`, empty it if nothing is missed.
