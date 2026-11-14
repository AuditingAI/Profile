# Work order for Codex · AIB-LAC 2027, ID 69

You work on Yasir's Mac in the local clone of `AuditingAI/Profile` (branch `claude/scholar-links-review-Plgk6`) and in
his FIU OneDrive working folder. Read `00_READ_FIRST.md` first. **Do one task at a time, in order, and stop after each
to report.** Log every task in `RESULTS/CODEX_LOG.md`: date, task, what changed, what could not be verified.

## Hard limits
- No email, payment, registration, portal upload or submission. Prepare; Yasir acts.
- Do not write or rewrite the paper's argument. Build, format, check and assemble.
- Do not log in to anything for Yasir, and never store a password or card number.
- No contact details in the repository (public). Use `{{EMAIL}}` and `{{PHONE}}`.
- If a fact is not on a source you opened, write `[CHECK]`.

## Tasks
| # | Task | Input | Output | Done when |
|---|---|---|---|---|
| **C1** | Save the reviews verbatim | Yasir pastes the Reviews page | `RESULTS/REVIEWS_ID69.md`, one section per reviewer, unedited | Yasir confirms nothing is missing |
| **C2** | Save the decision email's facts | Yasir pastes the chair's email | Dates, fees, final-version rules and session format written into `02_STATE.md`, each with its source line | Every `[CHECK]` in `02_STATE.md` that the email answers is resolved |
| **C3** | Registration and funding checklist | The chapter's site (lac.aib.world), FIU pages Yasir opens | `RESULTS/REGISTRATION_AND_FUNDING.md`: deadline, fee, membership, each funding route with its form and deadline | Each line has a URL that resolves |
| **C4** | Verify Gemini's captures | `RESULTS/GEMINI_S*.md` | Same file with a `verified` column: `resolves` / `dead` / `mismatch` (title or authors differ from the DOI record). Drop dead rows to a "Dropped" list | Every row checked; no row verified from memory |
| **C5** | Response-to-reviewers table | `RESULTS/REVIEWS_ID69.md` | `RESULTS/RESPONSE_TABLE.md`: comment (verbatim), response `[YASIR]`, change, location. Leave the response column for Yasir | One row per comment |
| **C6** | Rebuild the paper | `dba/coursework/_templates/build_aiblac_v2.py`, Yasir's edits | Revised PDF and Word; unblinded version only if the chair's email asks for one | Word count and abstract length reported; a search for "Insert" and "[CHECK]" returns nothing |
| **C7** | Interactive-session materials | The chair's format instructions; the FIU house deck style in `dba/coursework/_templates/` | Deck or poster with a figure on every slide; the feasibility-cliff figure (`dba/coursework/GEB7365_International_Business/figures/fig1_feasibility_cliff.png`) | Rendered to PDF and checked page by page |
| **C8** | Copy the working set to OneDrive | This folder | `FIU/TODO/AIBLAC2027/WORKING` mirrors `RESULTS/` and the built files | File list reported |

## Order
C1 and C2 now. C3 this week. C4 after each Gemini search. C5 after C1. C6 to C8 only when Yasir says go.

## Git
`git pull --rebase origin claude/scholar-links-review-Plgk6` before staging; add only files under
`dba/P1_Feasibility_Note/AIBLAC2027_HARNESS/` and the paper's own paths; commit with the `[scholar]` prefix.
