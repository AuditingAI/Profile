# Job applications automation

Sources, PDFs, and the daily-email workflow live here.

## Layout

```
applications/
  resume/
    resume.md                    <- edit this
    Yasir_Malik_Resume.pdf       <- generated
  cover_letters/
    <slug>.md                    <- one markdown per role
    <slug>.pdf                   <- generated
scripts/
  build_pdfs.py                  <- markdown -> PDF
  daily_jobs_email.py            <- daily search + email
.github/workflows/
  daily-jobs-email.yml           <- cron 11:00 UTC = 07:00 ET
```

## Generate PDFs locally

```bash
pip install reportlab
python scripts/build_pdfs.py
```

To convert an ad-hoc cover letter:

```bash
python scripts/build_pdfs.py --md applications/cover_letters/foo.md \
  --out applications/cover_letters/foo.pdf --title "Cover Letter - Foo"
```

## Daily email - one-time setup

The GitHub Actions workflow runs every morning at 07:00 ET, searches Google
careers (NY) and Anthropic's Greenhouse board for roles matching the configured
keywords, regenerates PDFs from the markdown sources, and emails the digest
with the resume + seed cover letters attached.

Add three repository secrets at
`https://github.com/AuditingAI/Profile/settings/secrets/actions`:

| Secret | Value |
|---|---|
| `GMAIL_ADDRESS` | `YasirAMalik@gmail.com` |
| `GMAIL_APP_PASS` | A Gmail **App Password** - create one at https://myaccount.google.com/apppasswords (requires 2FA) |
| `EXTRA_RECIPIENTS` | *(optional)* comma-separated extra To addresses |

Then trigger a manual test run from the Actions tab -> "Daily jobs email" ->
"Run workflow". You should get an email within a minute.

## Tuning

- **Add a target company / keyword set:** edit the `*_KEYWORDS` /
  `GOOGLE_QUERIES` lists at the top of `scripts/daily_jobs_email.py`.
- **Change the schedule:** edit the `cron:` line in
  `.github/workflows/daily-jobs-email.yml`. Cron runs in UTC.
- **Add a new tailored cover letter:** drop a markdown file in
  `applications/cover_letters/` and add it to the `pairs` list in
  `scripts/build_pdfs.py` (or just point `--md`/`--out` at it).
