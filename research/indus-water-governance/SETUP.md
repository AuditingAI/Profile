# Setup — Accounts and Alerts

Everything here needs your own logins, so it can't be automated. Total time
**about 40 minutes.** Do it in this order — later steps depend on earlier ones.

---

## Step 1 — ORCID iD (5 min) · DO THIS FIRST

Your ORCID is the permanent identifier that links every output you ever
publish, across every venue. Every other account below asks for it.

1. Go to **https://orcid.org/register**
2. Register with the email you will use for research permanently. Not a work
   address you might lose.
3. Under *Name*, set the **exact author string** you will use on every paper
   forever. Pick one form and never vary it:
   - Recommended: `Yasir A. Malik` — or whichever form you choose
   - Do not alternate between `Y. Malik`, `Yasir Malik`, and `Yasir A. Malik`.
     Name inconsistency is the single most common cause of a fragmented Scholar
     profile, and it is painful to repair later.
4. Set visibility to **Everyone**.
5. **Record your ORCID iD in `PUBLICATION-PIPELINE.md`** — format
   `0000-0000-0000-0000`.

---

## Step 2 — Google Scholar profile (5 min)

1. Go to **https://scholar.google.com/citations** while signed in to Google
2. *My profile* → complete the form
3. Affiliation: use something accurate. If you have no institutional
   affiliation, say `Independent Researcher` — that is a real and accepted
   category. Do not claim an affiliation you do not hold; it is checkable and
   the damage is permanent.
4. Use the **same name string** as Step 1
5. Add your ORCID in the homepage field
6. Set the profile to **Public**
7. Turn ON *Email me new citations to my articles*

The profile will be empty until you publish. That is expected and fine.

---

## Step 3 — Scholar alerts (15 min) · THE HIGH-VALUE STEP

This is the one that pays for itself. The Project 01 rescope came out of a
single search; these alerts run that search continuously.

For each query below:

1. Go to **https://scholar.google.com** and search the query
2. On the results page, click **Create alert** (envelope icon, left sidebar)
3. Confirm your email, leave results-per-alert at 20

| # | Query — paste exactly |
|---|---|
| 1 | `Indus groundwater governance` |
| 2 | `Indus basin GRACE groundwater depletion` |
| 3 | `GRACE downscaling groundwater machine learning` |
| 4 | `Pakistan tubewell irrigation policy` |
| 5 | `"Indus Waters Treaty"` |
| 6 | `Punjab Pakistan irrigation political ecology` |
| 7 | `canal command groundwater depletion institutional` |
| 8 | `groundwater electricity subsidy irrigation Pakistan` |

Queries 3 and 7 are the ones that matter most for Project 01 — 3 tells you if
the method literature moves under you, 7 tells you if someone else closes your
gap.

**Manage or delete alerts later at** https://scholar.google.com/scholar_alerts

### Author follows

On any author's Scholar profile there is a **Follow** button → *New articles by
this author*. Worth doing for several researchers across **both** strands.
Following one person is not a literature review, and a feed built around a
single name is a worse input than a feed built around a topic.

---

## Step 4 — Zenodo (5 min)

Zenodo is where the monthly output goes. Each release mints a DOI and is
Scholar-indexable.

1. **https://zenodo.org/signup/**
2. Sign up **with your ORCID** (button on the signup page) — this auto-links them
3. Go to *Settings → Linked accounts* → connect **GitHub**
4. Go to *Settings → GitHub* → toggle ON the repository you want archived

Once toggled on, **every GitHub release you tag gets an automatic DOI.** That is
the mechanism that makes a monthly cadence realistic — you tag a release, Zenodo
does the rest.

---

## Step 5 — EarthArXiv (5 min)

For the quarterly preprints.

1. **https://eartharxiv.org/** → *Sign up*
2. Add your ORCID in your profile
3. Subscribe to the RSS feed for hydrology / water resources subjects

---

## Step 6 — Journal TOC alerts (5 min)

Sign up for table-of-contents email alerts. Prioritise the first three:

| Journal | URL | Note |
|---|---|---|
| Water Alternatives | https://www.water-alternatives.org/ | Open access, governance-friendly. Plausible first target. |
| HESS | https://hess.copernicus.org/ | Open access, RSS available |
| Water Resources Research | https://agupubs.onlinelibrary.wiley.com/journal/19447973 | Where Arshad et al. published |
| Nature Water | https://www.nature.com/natwater/ | |
| Water International | Taylor & Francis | |
| Environmental Research Letters | https://iopscience.iop.org/journal/1748-9326 | |

---

## Completion checklist

- [ ] ORCID created · iD: `________________________`
- [ ] Author name string chosen: `________________________`
- [ ] Scholar profile created and public
- [ ] All 8 Scholar alerts created
- [ ] Zenodo created, linked to ORCID and GitHub
- [ ] EarthArXiv account created
- [ ] At least 3 journal TOC alerts active

When the ORCID and name string are filled in above, commit this file — the rest
of the repo references them.
