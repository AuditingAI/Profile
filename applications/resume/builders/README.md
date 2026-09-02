# Resume builders

The sources that generate the delivered PDFs. Edit these, then regenerate —
never hand-edit a PDF.

| Source | Produces | How |
|---|---|---|
| `build_branded_resume.py` | `Yasir_Malik_Resume_Google_CloudRAI_Branded.pdf` | `python3 build_branded_resume.py` (needs `reportlab`) |
| `master-resume.html` | `A_Yasir_Malik_Resume_2026.pdf` (carries the portfolio URL) | headless Chromium, below |
| `master-resume-no-url.html` | `Yasir_Malik_Resume_Master.pdf` (no portfolio URL — safe while that URL is dead) | headless Chromium, below |
| `genai-risk-master.html` | **`Yasir_Malik_Resume_GenAI_Risk_Master.pdf` — the current default.** Repositioned around the risks GenAI introduces (sycophancy, judgment drift, automation bias, hallucination, adversarial input, third-party AI) with a three-row "Where the Research Is Going" table. Same Georgia/Harvard ATS design, one page. Built 2 Sep 2026. | headless Chromium, below |

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

## Why the branded resume draws the wordmark as text

`build_branded_resume.py` renders "Audit the Algorithm" with coloured text
rather than embedding `assets/images/logo.svg`. Two reasons: an ATS reads the
brand instead of skipping an opaque graphic, and the file lands at ~6 KB
instead of ~67 KB, which is what makes it small enough to attach to an email
reliably.

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
