# Project 01 — Institutional Determinants of Groundwater Depletion in the Indus Basin

Status: **rescoped 2026-08-11** · Owner: YA · Opened 2026-08-11

> **Scope change.** This project originally proposed downscaling GRACE
> groundwater depletion to governance-unit resolution. **That has been done.**
> The literature search that was step 1 has now been run, and it killed the
> original contribution. What survives — and is now cheaper to execute — is the
> institutional half. See "What the search found" below.

## What the search found

The GRACE-downscaling method for the Indus is published and mature:

- **Arshad et al. (2024).** *Downscaled-GRACE Data Reveal Anthropogenic and
  Climate-Induced Water Storage Decline Across the Indus Basin.* Water Resources
  Research. Downscales GRACE/GRACE-FO to **1 km²** across **20 Indus
  sub-regions**, 2002–2023, using a geographically-weighted random forest
  (RFgw). Finds irreversible TWS and GWS decline in all 20 sub-regions, steepest
  downstream. `[verified — citation and abstract; full text paywalled, not yet read]`
  https://doi.org/10.1029/2023WR035882
- **"Downscaling GRACE/GRACE-FO data for improving terrestrial and groundwater
  storage monitoring and assessment in transboundary Indus Basin and its
  sub-regions."** ESS Open Archive preprint. `[verified — preprint exists]`
  https://doi.org/10.22541/essoar.173395770.08839790/v1
- **"Bridging the resolution gap: Machine learning for local-scale groundwater
  drought monitoring in Punjab, Pakistan."** Journal of Hydrology: Regional
  Studies (2025). `[unverified — title and venue only]`
- **Systematic review (2025):** *GRACE Downscaling and Machine Learning Models
  for Groundwater Prediction.* Hydrology. `[verified]`
  https://doi.org/10.3390/hydrology13050135

**Conclusion: do not build a downscaling pipeline.** Reproducing this would be
a training exercise, not a contribution. It would also be visible as such to
anyone in the field.

## The gap that survives

The two literatures still do not touch each other:

- **Satellite work** (Arshad et al. and successors) produces a fine-resolution
  depletion surface, and explains it with *climatic and anthropogenic* drivers
  in the broad sense — precipitation, irrigated area, population. It contains no
  institutional variables.
- **Institutional work** establishes the mechanisms — tail-enders receive less
  canal water and pump deeper, more brackish groundwater (World Bank evidence
  from ~4,000 watercourse outlets); electricity subsidies function as de facto
  abstraction policy. But this evidence is farm-survey cross-section, not
  spatially joined to a depletion surface. `[verified — mechanisms are
  established in the literature; the absence of a spatial join is our
  assessment, and must be confirmed by a proper systematic search before it is
  claimed in print]`

Nobody appears to have asked: **does the depletion surface line up with the
institutional geography?** That is a question the governance strand has been
arguing about qualitatively for years without a spatial test.

## Revised contribution

Take the published downscaled depletion surface as input. Join it spatially to
institutional variables. Test whether institutional geography explains variance
in depletion after controlling for the physical and climatic drivers already
identified.

### Independent variables

| Variable | Source | Obtainability |
|---|---|---|
| Canal command position (head / middle / tail) | Punjab Irrigation Dept. watercourse outlet data; World Bank annex | `[unverified]` — likely the hard one |
| Electricity tariff regime and subsidy history | NEPRA tariff notifications, by feeder/region | `[unverified]` |
| Tubewell density | Pakistan Agricultural Census | `[unverified]` |
| Cropping pattern (rice/sugarcane share) | Sentinel-2 / provincial crop reporting | Open |
| Colonial-era settlement and tenure class | Historical settlement reports, canal colony boundaries | `[assumption]` — may not be machine-readable |

### Controls

Precipitation (CHIRPS), evapotranspiration (MOD16), surface-water delivery
where available — the drivers Arshad et al. already established, so that any
institutional effect is measured net of them.

### Why this is defensible

It is the only version of this project where the technical work and the
governance framing are both load-bearing. A hydrologist cannot code canal-tail
position and colonial tenure class as meaningful variables. A political
ecologist cannot run a spatial regression on a 1 km depletion surface. That is
what makes it a genuine two-sided problem rather than a request for someone's
time.

## Honest risks

- **The institutional data may not exist at usable resolution.** This is now the
  binding constraint, not the satellite work. Canal command boundaries in
  digital form are the single point of failure — resolve this before anything
  else.
- **The result may be null.** Depletion may be explained entirely by cropping
  pattern and rainfall, with no residual institutional signal. That is a
  publishable finding and should be published if found. Decide now, before
  seeing results, that a null goes to press — otherwise this becomes an exercise
  in finding the answer you wanted.
- **Spatial autocorrelation will inflate significance** if handled naively. Use
  spatial error / spatial lag models or cluster standard errors by canal command.
- **Ecological inference.** A district-level correlation between tariff regime
  and depletion does not establish that individual farmers responded to tariffs.
  State this limit explicitly rather than letting a reader over-read it.
- **The gap claim needs verification.** "Nobody has joined these" is currently
  `[assumption]` based on one search round. Run a proper systematic search
  before asserting novelty in any draft.

## Immediate next steps

- [ ] Systematic search to confirm the gap is real — Scopus/Web of Science, not
      just Google. If someone has done this, rescope again.
- [ ] Read Arshad et al. (2024) in full. Determine whether the downscaled
      product is publicly released or must be requested from the authors.
- [ ] Establish whether digital canal command boundaries exist for Punjab. This
      is the go/no-go item.
- [ ] Write the one-page problem statement.

## On collaboration

The sequence matters. Do the systematic search, secure the depletion surface,
and confirm the canal data exists — *then* approach anyone. At that point the
message is "I have the depletion surface and the canal geography joined, the
institutional coding is where I'm out of my depth, here is the notebook." That
is a proposal. Before that point it is a request for someone else's time, and
it will be read as one.

Norms:

- Approach on the work, citing papers actually read in full.
- One message. No reply is a reply.
- No one is listed as a co-author without explicit written consent.
- Publish under your own name regardless of who joins. Work that stands alone is
  what makes it worth joining.
