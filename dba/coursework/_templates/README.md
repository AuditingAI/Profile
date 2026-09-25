# Submission templates

`academic-submission.html` — the house letterhead for anything handed to an instructor.

**Design decisions, so they are not re-litigated each time:**

- **Palette and type come from `live.html`** — the same accent `#1F4E79`, paper `#FBFAF7`, ink
  `#14171C`, and the Iowan Old Style / Palatino serif stack. One visual identity across the
  register, the site, and coursework.
- **The wordmark is the monochrome variant**, `assets/images/logo-mono.svg`, not the gold
  `logo.svg`. A gold marketing logo on a graded class memo reads as self-promotion to a professor.
  The blue wordmark reads as someone who takes their own work seriously. Keep the gold mark for the
  site, the portfolio, and anything public.
- **If a submission portal wants plain Word or PDF with no letterhead**, delete the `<img>` line and
  print. The typography still carries.
- **The AI-disclosure footer is part of the template, not an afterthought.** GEB 7911 requires it.
  Never ship a submission with the placeholder still in it.

**To use:** copy the file, replace `{{TITLE}}`, `{{COURSE}}`, `{{INSTRUCTOR}}`, `{{DATE}}`,
`{{BODY}}` (one `<p>` per paragraph) and `{{DISCLOSURE}}`. Open in a browser → Print → Save as PDF.
Page setup is US Letter with 0.9in margins; ~500 words lands on one page.
