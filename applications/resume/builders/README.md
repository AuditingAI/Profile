# Resume builders

The sources that generate the delivered PDFs. Edit these, then regenerate —
never hand-edit a PDF.

| Source | Produces | How |
|---|---|---|
| `build_branded_resume.py` | `Yasir_Malik_Resume_Google_CloudRAI_Branded.pdf` | `python3 build_branded_resume.py` (needs `reportlab`) |
| `master-resume.html` | `A_Yasir_Malik_Resume_2026.pdf` (carries the portfolio URL) | headless Chromium, below |
| `master-resume-no-url.html` | `Yasir_Malik_Resume_Master.pdf` (no portfolio URL — safe while that URL is dead) | headless Chromium, below |
| `build_genai_risk_branded.py` | **`Yasir_Malik_Resume_GenAI_Risk_Master_Branded.pdf` — the current default (owner's call, 3 Sep 2026).** Same GenAI-risk content as the row below, in the Audit the Algorithm brand: wordmark as gold text, Times faces, hairline rules, research table as a reportlab `Table`. One page, ~7 KB. | `python3 applications/resume/builders/build_genai_risk_branded.py` (needs `reportlab`) |
| `genai-risk-master.html` | `Yasir_Malik_Resume_GenAI_Risk_Master.pdf` — unbranded twin of the row above, for any portal that objects to a consulting wordmark. Repositioned around the risks GenAI introduces (sycophancy, judgment drift, automation bias, hallucination, adversarial input, third-party AI) with a three-row "Where the Research Is Going" table. Same Georgia/Harvard ATS design, one page. Built 2 Sep 2026. | headless Chromium, below |
| `gs-gbm-src-vp.html` | `Yasir_Malik_Resume_GS_GBM_SRC_VP.pdf` — Goldman Sachs GBM Supervisory Risk & Controls VP (req 183007). Harvard ATS, **unbranded on purpose**: Goldman requires OBA disclosure and a consulting wordmark raises the question early. First-line positioning with a three-row role-mapping table. Built 12 Sep 2026. | headless Chromium, below |
| `gs-ia-data-analytics-vp.html` | `Yasir_Malik_Resume_GS_IA_DataAnalytics_VP.pdf` — Goldman Sachs Internal Audit, Data Analytics VP. Harvard ATS, unbranded (Goldman OBA disclosure). **Leads technical**: skills block high for the ATS, a requirements-mapping table second, audit management supporting rather than leading — the inverse of every other resume here, because the JD asks for a data scientist. Body type is 7.9pt to hold one page. Built 12 Sep 2026. | headless Chromium, below |
| `build_master_branded.py` | **`Yasir_Malik_Resume_Master_Branded.pdf` — the broad master.** Wordmark + Harvard layout, every lane on one page: internal audit, first-line risk and controls, capital and financial control, data governance, AI governance. Five-row results table. The one to send when no tailored variant fits. Built 13 Sep 2026. | `python3 applications/resume/builders/build_master_branded.py` (needs `reportlab`; optional scale arg) |
| `build_academic_cv_branded.py` | `Yasir_Malik_CV_Academic_Branded.pdf` — **academic CV**, two pages, for adjunct / lecturer applications. Education and the doctoral research programme lead; research status is stated to the standard the public research page sets (no hypotheses tested, no publications to date, AI extension argued not tested). Carries `[TO CONFIRM: …]` placeholders in red for the SAAC tutoring, graduate TA, FIU guest lectures and the Rutgers class visit — the build prints how many remain; do not send while any do. Built 13 Sep 2026. | `python3 applications/resume/builders/build_academic_cv_branded.py` (optional scale arg) |
| `build_gs_ia_regulatory_relations_branded.py` | `Yasir_Malik_Resume_GS_IA_RegRelations_VP_Branded.pdf` — Goldman Sachs Internal Audit, Regulatory Relations VP. Branded at the owner's request. Header drawn by **`brand.py`**: the text wordmark (which is what `assets/images/logo.svg` is), or a raster mark above it the moment `assets/images/logo-mark.png` exists. Built 14 Sep 2026. | `python3 applications/resume/builders/build_gs_ia_regulatory_relations_branded.py` |
| `build_gs_transformation_pm_branded.py` | `Yasir_Malik_Resume_GS_Transformation_PM_VP_Branded.pdf` — Goldman Sachs Office of Transformation, Digital Transformation PM VP. Branded. Built around the posting's own triad — revenue, risk and control, efficiency — as a priced table; programme delivery leads and the audit record supports. Built 14 Sep 2026. | `python3 applications/resume/builders/build_gs_transformation_pm_branded.py` |
| `build_bny_treasury_cio_auditor_branded.py` | `Yasir_Malik_Resume_BNY_Treasury_CIO_Auditor_VP_Branded.pdf` — BNY VP Auditor, Corporate Treasury, CIO & Risk. Branded. **The best-matched role on the board**: his JPMorgan title was Risk Control Manager, Treasury & CIO, so he audits the function he ran. Leads with a table mapping each function in the role title to the seat he held in it. Built 14 Sep 2026. | `python3 applications/resume/builders/build_bny_treasury_cio_auditor_branded.py` |
| `build_gs_hcm_data_product_branded.py` | `Yasir_Malik_Resume_GS_HCM_DataProduct_VP_Branded.pdf` — Goldman Sachs HCM Strategy, Data Program Product Management VP. Branded. **Built at the owner's explicit request after the fit was argued against** — he has never held a product-manager title. Leads with data products: the Citi GLEM legal-entity programme is promoted out of chronological order to sit first, because it is the only data product on the record. Claims no Snowflake, no Oracle HCM, no data mesh and no Jira, and the harness enforces that. Built 18 Sep 2026. | `python3 applications/resume/builders/build_gs_hcm_data_product_branded.py` |
| `google-core-ai-foundations-vp.html` | **`Yasir_Malik_Resume_Google_CoreAIFoundations_VP.pdf` — the plain executive cut.** Unbranded, Harvard ATS, one page, but set for a VP reader rather than a screener: 18.5pt name, a short Profile paragraph instead of a keyword block, a numbers-first **Selected Results** table, and two or three bullets per role with the older roles collapsed to a single line. Owner's preferred format for the Google Core AI Foundations application, 20 Sep 2026. | headless Chromium, below |

Chromium render:

```bash
CHROME=$(ls /opt/pw-browsers/chromium*/chrome-linux/chrome | head -1)
"$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="out.pdf" "file://$PWD/master-resume.html"
```

Then stamp metadata with `pypdf` (`/Title`, `/Author: Yasir A. Malik`) and
confirm `len(reader.pages) == 1`.

## The letter-spacing trap — do not undo this

`h1` letter-spacing must stay at or below **1.5px**. Above that, Chromium
writes the name into the PDF text layer with a space between every character:

```
YA S I R  A .  M A L I K
```

An applicant tracking system searching for "Yasir Malik" then fails to match
the candidate's own name — the single most important field in the document.
This shipped undetected in every Harvard-template resume built before
2026-08-07.

After any header change, verify:

```bash
pdftotext out.pdf - | grep -c "YASIR A. MALIK"   # must be 1, not 0
```

## The A mark

`assets/images/logo-mark.svg` (and its 600px raster twin `logo-mark.png`) is the
**A monogram**: the letter in the brand gold gradient (#B8860B → #DAA520), with
the crossbar drawn as a hairline rule that runs clean through the letter and
past both stems — the same rule that separates sections on the resume, so the
mark and the document read as one system.

Every branded builder draws it through `brand.py`, so it appears once, at the
top, above the wordmark, which drops to a supporting line beneath it. The mark
is 0.38 in tall; larger pushed the broad master onto a second page.

**To swap in a different mark** (for example the one in Google Drive,
`Edu_Photo_Audit_the_Algorithm_Logo.png`): replace
`assets/images/logo-mark.png`, keep it square-ish and under ~600 px wide, then

```bash
cd applications/resume && for b in builders/build_*.py; do python3 "$b"; done
python3 scripts/verify_documents.py --rebuild
```

Nothing else changes — `brand.py` picks the file up by path. Delete the file and
every builder falls back to the wordmark alone.

The unbranded Chromium resumes (`gs-gbm-src-vp.html`,
`gs-ia-data-analytics-vp.html`, `genai-risk-master.html`,
`master-resume-no-url.html`) carry no mark **on purpose** — Goldman requires
outside-business-activity disclosure, and a consulting mark raises that question
before anyone has read the first line.

## Why the branded resume draws the wordmark as text

`build_branded_resume.py` renders "Audit the Algorithm" with coloured text
rather than embedding `assets/images/logo.svg`. Two reasons: an ATS reads the
brand instead of skipping an opaque graphic, and the file lands at ~6 KB
instead of ~67 KB, which is what makes it small enough to attach to an email
reliably.

## The harness — run it, do not re-derive it

```bash
./agent-kit/run.sh verify --rebuild        # add --html to re-render the Chromium resumes
```

`scripts/verify_documents.py` runs every check on this page across every PDF in
`applications/resume/` and `applications/cover_letters/`, plus the builders and
markdown that generate them: one page, a real text layer, the name extracting
contiguously, the phone and email, and every standing content rule below.
`--rebuild` regenerates each PDF from its source and fails if the committed file
no longer matches — which is how an edited builder with an uncommitted PDF gets
caught. Rebuilds that change nothing are restored, so a verify run leaves no
diff behind.

`scripts/verify_selftest.py` injects each of those failures into a throwaway
copy and asserts the harness catches it. Run it after changing a rule.

The notes below explain *why* each check exists. They are not a substitute for
running it.

## Verifying without pdftotext

`pdftotext` is not installed in the cloud session image, and the system
`cryptography` package there is broken, which takes `pypdf` and `pdfminer`
down with it on import. `pip install cffi` repairs it. If it does not, pypdf
supports running without cryptography — set `sys.modules["cryptography"] =
None` before importing and it uses its pure-Python provider. The check that
matters is the same either way: one page, `YASIR A. MALIK` extracts as one
string, the phone is present, and `\bOCC\b` matches zero times.

## Standing content rules

- **Never write "OCC".** The examiner history is the Florida Office of
  Financial Regulation, "alongside federal banking regulators" if context is
  needed. This was wrong on shipped documents and was purged repo-wide on
  26–27 Aug 2026; do not reintroduce it.

- **Never state a career-length number** — "20 years", "15+ years", "two
  decades", "a decade". Owner's rule, 12 Sep 2026: it dates him. Name the
  institutions (Citi, JPMorgan Chase, Florida OFR) and let the dates on the
  experience entries speak. Employer-specific spans ("six years at JPMorgan")
  are fine. Purged repo-wide on 12 Sep; the verify step greps for it.
- Phone is **+1 (786) 704-8536**. The 305 number is personal and retired.
- **DBA in progress, expected 2028**, GPA 3.81. Never "Dr. Malik".
- The IRB approval (IRB-25-0462) covers the **completed anchoring-bias
  qualifying research**, not the automation-bias dissertation, which is in
  development and not approved.
- Never write "CIA certified" — that certification is in progress.
- The branded variant carries the consulting wordmark. For W-2 applications
  consider the unbranded master instead: a consulting brand on a resume
  signals an outside business activity, which some employers require to be
  disclosed.

## The GenAI-risk master (Sep 2026)

`genai-risk-master.html` → `Yasir_Malik_Resume_GenAI_Risk_Master.pdf`. The
default resume for every application from September 2026 onward. Repositions
the candidate around the risks generative AI introduces (sycophancy and
judgment drift, automation bias, hallucination, adversarial input, third-party
AI) and carries a three-row "Where the Research Is Going" table with honest
statuses: completed / in development / planned. Never states or implies the
dissertation is approved. Examiner history is the Florida Office of Financial
Regulation only — the string "OCC" must not appear anywhere in the output, and
the build verifies that along with the one-page and name-extraction checks.
