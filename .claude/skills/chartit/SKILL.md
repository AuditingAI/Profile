---
name: chartit
description: Turn a paper, a model, or a set of findings into the chart that fits what it actually argues, and ship it as PDF, PPTX, or a published page. Use when he asks for a diagram, a figure, a model drawn, a slide, "chart it", "make it visual", or wants a reading represented graphically. Scholar lane.
---

# Chart it

Drawing a paper forces a decision about what its claim is. A chart you can defend is a paper you
have understood — which is why the reading index carries a chart form for every entry.

## Match the form to the argument

| The paper does this | Draw it as |
|---|---|
| Claims a relationship | **Plot the relationship.** A three-stage theory means a curve with three stages on it |
| Offers a framework | The framework's own axes — CAGE is four distances, so four axes |
| Builds a typology | A matrix, with the **empty cells visible** — the gaps are usually the finding |
| Describes a process | A loop or phase sequence, direction marked |
| Reviews a domain | A stream map or timeline — what entered when, what is unresolved |
| Critiques measurement | A comparison table where the disagreement itself is the content |
| Proposes a model | A path diagram — boxes, arrows, signs on the arrows |

**Never a generic bar chart for something that is not a quantity.**

## House identity — non-negotiable

Palette and type come from `live.html` and are used across every artefact:

`#1F4E79` accent · `#8A6410` gold · `#FBFAF7` paper · `#14171C` ink · `#767D86` muted ·
`#D8D4CB` rule · `#0E2237` deep ground

Serif display, mono for labels and metadata. The **monochrome** wordmark on academic work; the gold
one is for public and portfolio pieces only.

## How to build

| Output | Route |
|---|---|
| **PDF** — the reliable one | `dba/coursework/_templates/build_field_map_pdf.py`, reportlab, direct |
| PPTX — when he must edit it | `_templates/build_deck_full.js`, pptxgenjs. **Avoid `flipH` on lines** — it corrupts the file in PowerPoint |
| Published page | Artifact, house palette, both themes |
| Word | `_templates/build_submission.py` |

**Prefer PDF.** LibreOffice does not run in this container and PowerPoint has rejected generated
files before.

## Always render and look before shipping

This is not optional and it is the step most often skipped. Structural validation passes files that
are visually broken.

```
python3 -c "import pymupdf; d=pymupdf.open('out.pdf'); [d[i].get_pixmap(dpi=80).save(f'p{i+1}.png') for i in range(d.page_count)]"
```

Then read the PNGs. Six defects were caught this way on one three-page file that had passed every
structural check — including circles that were not overlapping at all in a diagram whose entire
argument was about overlap.

Check for: clipped text · labels over their own shapes · captions overflowing panels · headings
wrapping into subtitles · elements colliding · geometry that does not match the claim.

## Guardrails

- Never publish a figure whose geometry contradicts the caption
- Attribute redrawn figures — author, year, and the figure number
- Flag anything drawn from a paper not actually read
