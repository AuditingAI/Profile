# The house résumé format — read this before building any résumé

**The one résumé (owner, 8 Oct 2026):** `Yasir_A_Malik_Resume.pdf`, built from `builders/the-one-resume.html`, goes with every application. Build a tailored copy only when he asks for one.

Set by the owner on 7 Oct 2026. Every résumé built after this date starts as a copy of
`builders/TEMPLATE.html`. Nothing in the header, the section order, the type or the
margins changes per application; only the words in the `{{SLOTS}}` do. If the format
itself needs to change, change `TEMPLATE.html` once and rebuild every builder that
descends from it.

Machine-readable twin: `agent-kit/rules.json` → `resume_format`.

## The signature header

The top of the page is the owner's signature, lifted from
`assets/brand/reference-mark/Signature.dc.html`:

| Element | Value | Why |
|---|---|---|
| Mark | The Audit Lens (`assets/images/audit-lens-mark.svg`), inline SVG, 44 px: navy magnifier `#1B365D`, orange A `#E0662E`. **The same mark as the CV header** (`logo-mark.png`); owner, 8 Oct 2026: résumé and CV stay in sync | The owner's brand; an ATS ignores it, a reader remembers it |
| Reference line | 2 px navy rule to the left of the text block | The same line the email signature uses |
| Name | `YASIR A. MALIK`, Georgia bold 17 pt, **letter-spacing 0** | Above 1.5 px Chromium spaces the characters in the text layer and an ATS cannot match the name |
| Kicker | `AUDIT · RISK · GOVERNANCE`, Arial 7.4 pt, deep orange `#AD4317`, tracking 0.8 px | The signature's second line; tracking above ~1 px at this size also breaks the text layer |
| Tagline | Georgia italic 9.2 pt, three phrases in the posting's own words, separated by `|` | The only header line that changes per application |
| Contact | Arial 8 pt grey, two lines: Newark, NJ · email · +1 (786) 704-8536 · linkedin.com/in/yasiramalik, then `Profile: auditingai.github.io · Code and materials: github.com/MalikAI-786` | The 305 number is retired. **Résumé points to the profile (main) page; the CV points to the research page** (`auditingai.github.io/research.html`). Owner, 8 Oct 2026 |

## Section order — fixed

1. **Profile** — exactly two sentences. One: what he is for this role and the single
   employer fact that proves it. Two: the second proof and the data or examiner angle.
2. **Selected Results** — four rows, never more. Number in orange, what it is in the
   posting's vocabulary, employer in grey italic on the right. Three columns, no grid.
3. **Experience** — Citi (2–3 bullets), JPMorgan Treasury & CIO (2–3 bullets), JPMorgan
   Capital Controller (one sentence), JPMorgan CIB RRP (one sentence). Titles and dates
   are fixed; see `rules.json` → `facts_of_record`.
4. **Earlier Career** — one line, roles before 2016: title, employer, place, dates.
   No bullets. Those accomplishments are for the interview.
5. **Skills** — two labelled lines of posting keywords the record supports, plus the
   fixed Tools line.
6. **Education** — fixed line. No DBA completion year, no GPA, until the program office
   confirms them.

## Hard rules

- **One page.** Letter, margins 0.34 in × 0.55 in, body Georgia 8.8 pt. If it runs over,
  cut words, not sections, and never shrink the type below 8.6 pt.
- **No rule lines under headings, no gridded tables.** Both can break applicant tracking
  systems (Newark Public Library review, 30 Sep 2026). Section heads are small-cap Arial
  in `#AD4317` with nothing underneath.
- **The text layer must read as words.** After every build:
  `pdftotext out.pdf - | grep -c "YASIR A. MALIK"` must be 1, and the kicker must extract
  as `AUDIT · RISK · GOVERNANCE`, not `A U D I T`.
- **Everything the harness checks still applies**: `python3 scripts/verify_documents.py`
  must end `READY`, and the builder must be registered in `HTML_OUTPUTS`.
- **Claims come from the record.** Never state a report, tool, title or certification
  the facts of record do not hold. The Amex regulatory-reporting résumé leaves out
  FR Y-9C, the Call Report, FR Y-11 and FR 2314 for exactly that reason.
- **The content rules in `rules.json` → `never_write`** (no named federal examiner agency, no career-length number,
  no "Dr.", no unqualified CIA, no Snowflake / Oracle HCM / data mesh / Jira / R) stand.

## Building one

```bash
cp applications/resume/builders/TEMPLATE.html applications/resume/builders/<employer-role>.html
# fill the slots, then:
CHROME=$(ls /opt/pw-browsers/chromium*/chrome-linux/chrome | head -1)
"$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=applications/resume/Yasir_Malik_Resume_<Employer>_<Role>.pdf \
  "file://$PWD/applications/resume/builders/<employer-role>.html"
python3 scripts/verify_documents.py
```

Register the pair in `scripts/verify_documents.py` → `HTML_OUTPUTS`, add a row to
`builders/README.md`, and if it serves a family of postings copy it into `family/` under
the neutral name.

## First résumé built on this format

`builders/amex-audit-regreporting-director.html` →
`Yasir_Malik_Resume_Amex_Audit_RegReporting.pdf` — American Express, Director-Audit,
Regulatory Reporting SME (job 26014669), 7 Oct 2026. It is the worked example: copy its
shape, not its words.
