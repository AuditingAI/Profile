# Publication Pipeline

## How Google Scholar actually works

Google Scholar is **an index, not a venue.** You cannot publish to it. It
crawls the web for documents that look like scholarly works and attaches them
to author profiles. To appear in Scholar, a document must be:

1. **Hosted somewhere Scholar crawls** — a publisher site, a recognised
   preprint server, an institutional repository, or a personal page that meets
   Scholar's inclusion guidelines.
2. **Structurally scholarly** — title, authors, abstract, references, and a
   PDF. Scholar parses layout; a blog post in HTML usually will not qualify.
3. **Discoverable via metadata** — Dublin Core or Highwire Press meta tags in
   the hosting page's `<head>`, or a registered DOI.

Indexing latency is typically days to weeks after crawl, not instant.

**Reference:** Scholar's own inclusion guidelines —
https://scholar.google.com/intl/en/scholar/inclusion.html

## The monthly cadence problem

Peer-reviewed journal articles take 6–24 months from submission to print. A
monthly peer-reviewed cadence is not achievable and attempting it produces
salami-sliced work that damages a reputation rather than building one.

What *is* achievable monthly, and *is* Scholar-indexed:

| Output type | Venue | Indexed? | Realistic cadence |
|---|---|---|---|
| Preprint | EarthArXiv, ESS Open Archive | Yes | 1 per 2–3 months |
| Dataset + data descriptor | Zenodo (mints a DOI) | Yes | Monthly |
| Working paper | SSRN, institutional series | Yes | 1 per quarter |
| Technical report | Zenodo / institutional repo | Yes | Monthly |
| Journal article | WRR, HESS, Water Alternatives, etc. | Yes | 1–2 per year |

### Recommended rhythm

- **Monthly:** one versioned dataset or technical note to **Zenodo**. Each
  release mints a DOI and is Scholar-indexable. This is the honest way to hit a
  monthly cadence — you are publishing *data and methods*, which genuinely can
  be produced monthly, rather than pretending to produce monthly findings.
- **Quarterly:** one preprint to **EarthArXiv** synthesising the accumulated
  monthly work.
- **Annually:** one or two of those preprints developed into journal
  submissions.

The monthly Zenodo releases build the citable record and the DOI trail. The
preprints build the argument. The journal articles build the career.

## Setup checklist (one-time, manual)

- [ ] Create an **ORCID iD** — https://orcid.org/register. This is the
      identifier that links your outputs across venues. Do this first.
- [ ] Create a **Google Scholar profile** —
      https://scholar.google.com/citations. Set it to public.
- [ ] Create a **Zenodo** account and link it to ORCID and GitHub. Linking
      GitHub means a tagged release in a repo can auto-archive with a DOI.
- [ ] Create an **EarthArXiv** account — https://eartharxiv.org/
- [ ] Decide an author-name string and use it identically everywhere. Name
      inconsistency is the single most common cause of a fragmented Scholar
      profile.

## Quality gate

Before anything is released under a DOI:

- Every factual claim traces to a `[verified]` source in this repo.
- Data and code are included, and the analysis reruns from a clean checkout.
- Limitations are stated explicitly, including what the data cannot support.
- Any co-author has seen and agreed to the draft. No one is listed as a
  co-author without their explicit written consent.

A DOI is permanent. Retracting is far more costly than delaying.
