# Resume design canvas

Where the resume layout gets refined visually, in Claude Design.

**Canvas:** https://claude.ai/code/artifact/51f52f0f-eddb-4f98-af9a-40af97273492

| File | What it is |
|---|---|
| `Main.dc.html` | The artboard source — one Letter page (816x1056 at 96px/in) |
| `canvas.json` | Layout manifest: one fixed print artboard, opens focused |
| `yasir-malik-resume.html` | The seeded canvas that was published. Regenerated, never hand-edited |

## The thing to keep straight

**The canvas is not the build.** The PDF that actually gets attached to
applications comes from `../build_genai_risk_branded.py` (ReportLab). The canvas
is a visual reference built from the same brand values and the same content.

A change made on the canvas does not reach a shipped PDF until someone ports it
into the builder and regenerates. If the two drift, the resume being sent stops
matching the resume being designed — which is the failure mode this note exists
to prevent.

Brand values are lifted from `../build_branded_resume.py` and must stay in sync
with it: gold `#B8860B`, muted `#6F6754`, Times faces, hairline rules under
section heads.

## Re-seeding after an edit

Edit `Main.dc.html`, then re-run the seeder from the `/design` skill and
republish to the same artifact URL. Never edit `yasir-malik-resume.html` by hand
— it is generated output.
