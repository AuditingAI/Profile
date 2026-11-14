# AIB-LAC 2027 · harness · READ FIRST (created 14 Nov 2026)

**Paper:** *Feasibility as a Parameter: When Comparative International Research on Narrow Specialist Professional
Populations Can and Cannot Be Executed.* Sole author: Yasir A. Malik. Manuscript ID 69, Track 1
(Internationalization Strategies and Process).
**Status:** **Accept for Interactive Session** (AIB-LAC author system, seen 14 Nov 2026).
**Conference:** AIB Latin America and the Caribbean Chapter, San Juan, 3 to 5 March 2027 [CHECK on lac.aib.world].

This folder is the hand-off pack for every AI working on the paper. The repository is the memory; the model is
swappable (see `dba/AI_RUNBOOKS/README.md`).

## Who does what
| Who | Job | File |
|---|---|---|
| **Yasir** | Decides. Reads every source before it is cited. Signs, pays, sends, submits | `05_DECISIONS_FOR_YASIR.md` |
| **Gemini** (Deep Research) | Literature search only: finds and captures sources. Never writes the paper | `03_GEMINI_DEEP_SEARCH.md` |
| **Codex** (on the Mac) | Carries out tasks: saves files, builds documents and slides, checks links | `04_CODEX_WORK_ORDER.md` |
| **Claude** | Plans, checks the others' output against the sources, keeps this folder and the tracker current | `01_MASTER_PLAN.md`, `02_STATE.md` |

## Read order
1. `00_READ_FIRST.md` (this file)
2. `02_STATE.md`: where things stand today and the one next action
3. `01_MASTER_PLAN.md`: the phases and dates to San Juan
4. Your own brief: Gemini reads 03, Codex reads 04
5. `RESULTS/`: where Gemini's captures and Codex's logs are saved

## Rules for every AI (not negotiable)
1. **Draft only.** No email, payment, registration, portal upload or submission without Yasir's approval, item by item.
2. **Academic email goes from the FIU mailbox**, never Gmail. Use `{{EMAIL}}` and `{{PHONE}}` in files: this repo is public.
3. **Never invent** a citation, number, date, fee or quote. Anything not read on the source is marked `[CHECK]`.
4. **A search result is a lead, not a citation.** `read_state` starts at `lead`; only Yasir moves it to `read`
   (`dba/AI_RUNBOOKS/SCHEMAS.md`). Nothing enters the paper until he has read it.
5. **Say "accepted for presentation", never "published".** No data have been collected; claim no findings.
6. **No DBA completion year and no GPA** anywhere.
7. **AI use:** AI supports search, organisation, clarity and grammar. The argument and interpretation are Yasir's.
   Disclose AI use wherever the venue or FIU policy requires it.
8. **Git:** Scholar lane, branch `claude/scholar-links-review-Plgk6`, commits prefixed `[scholar]`, never `git add -A`,
   never force-push.

## Where the paper lives
- Submitted (blinded) files: `dba/coursework/GEB7365_International_Business/AIBLAC2027_SUBMITTED_ID69/`
- Builder: `dba/coursework/_templates/build_aiblac_v2.py`
- Prof. Newburry's comments: `dba/coursework/GEB7365_International_Business/FEEDBACK_Newburry_AIBLAC_2026-09-28.md`
- Feasibility model: `dba/RISK_QUANT/FEASIBILITY_MODEL.md`, `dba/RISK_QUANT/feasibility.py`
- Tracker: `dba/PUBLICATION_TRACKER.md`
