# ChatGPT harness

Everything ChatGPT needs to pick this work up and produce documents in the same format Claude used.

## Set up once (five minutes)

1. ChatGPT, left sidebar, **Projects → New project**. Name it "DBA and applications".
2. Open the project's **Instructions** and paste the whole of `PROJECT_INSTRUCTIONS.md`.
3. **Add files** to the project, all of these:
   - `RESUME_HERE.md` and `CONTEXT_PACK.md` (one folder up)
   - `build_dba_doc.py`, `md_to_doc.py`, `reference-mark.png`
   - The documents you want it to work on, as markdown: `career/academic/ACADEMIC_CV_v2.md`,
     `RESEARCH_STATEMENT.md`, `TEACHING_STATEMENT.md`, and any letter in `career/academic/letters/`
4. Start every chat inside that project.

## Keeping it current

The harness is only as good as `RESUME_HERE.md`. When you switch from Claude to ChatGPT, tell Claude
"update the handoff" first, then re-upload `RESUME_HERE.md` to the project, replacing the old one.
When you switch back, paste ChatGPT's last summary to Claude.

## Tested

The two scripts were run from this folder alone, in a clean directory, with only python-docx
installed, and produced the CV with the mark, contact filled and links live.
