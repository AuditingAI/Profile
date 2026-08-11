# Field Map — Indus Basin Water Governance

Last updated: 2026-08-11

Status markers: `[verified]` primary source checked · `[unverified]` secondary
source only · `[assumption]` our inference.

---

## The core problem

The Indus Basin Irrigation System (IBIS) is among the largest contiguous
irrigation networks in the world. Its surface-water allocation is
institutionally formalised (Indus Waters Treaty 1960 internationally, the Water
Apportionment Accord 1991 between provinces). Its **groundwater** abstraction is
effectively ungoverned — millions of private tubewells, no abstraction
licensing regime, no metering, and no reliable measurement of total withdrawal.

This produces the central research gap: **the field argues about groundwater
governance without a defensible estimate of groundwater use.** That gap is where
a technically-skilled outsider can contribute something real.

---

## Research strands

### 1. Political ecology / governance history
Treats the groundwater crisis as an institutional and historical problem —
colonial-era canal irrigation design creating path dependencies that shape
present-day abstraction behaviour.

### 2. Hydrology and remote sensing
Estimating storage change, recharge, and abstraction from satellite and
in-situ data. GRACE/GRACE-FO gravimetry, land-surface modelling, evapotranspiration
retrieval.

### 3. Transboundary law and policy
Indus Waters Treaty interpretation, India–Pakistan disputes, and increasingly
Afghanistan–Pakistan questions on the Kabul River.

### 4. Agricultural economics
Tubewell economics, energy subsidies (electricity and diesel pricing as de facto
groundwater policy), cropping patterns, water productivity.

**The interesting work is at the seams.** Strand 1 has the institutional
argument but thin quantitative evidence; strand 2 has the data but often no
governance framing. A contribution that bridges them is more valuable than one
that deepens either.

---

## Researchers and practitioners

Listed as authors of public work, with sources. Affiliations change — re-verify
before citing.

### Fazilda Nabeel
- PhD Development Studies, University of Sussex (ESRC-funded) `[verified]`
- MSc Economics, LUMS · MPA, Brown University (Fulbright) `[verified]`
- Provincial (Punjab) Coordinator, Living Indus Initiative (GoP / UN) `[unverified — secondary sources; confirm current status]`
- Visiting/adjunct faculty, LUMS MGSHSS and Rausing Executive Development Centre `[unverified]`
- Strand: political ecology of groundwater governance; colonial roots of
  present-day non-governance in Punjab.
- Profile: https://www.sussex.ac.uk/profiles/363755
- Scholar: https://scholar.google.com/citations?user=3SYX5NYAAAAJ&hl=en
- Public writing: https://dialogue.earth/en/author/fazilda-nabeel/ ·
  https://theconversation.com/profiles/fazilda-nabeel-379764

Key works:
- Nabeel, F. (2021). *Groundwater Crisis: A Crisis of Governance?* In: Water
  Resources of Pakistan. Springer. `[verified — citation exists; full text not yet read]`
- Nabeel, F. & Cheema, M.J.M. (2021). *Pakistan's Transboundary Water
  Challenge.* Same volume. `[verified — citation exists; full text not yet read]`
- Chaudhry, T.T. & Nabeel, F. (2013). *Microinsurance in Pakistan: Progress,
  Problems, and Prospects.* Lahore Journal of Economics. `[verified]`
- Chapters in *Human Development in South Asia* 2012, 2013. `[unverified]`

### M.J.M. Cheema
- Co-author on the transboundary water chapter above. `[verified]`
- Works the remote-sensing / water-resources side. Affiliation reported as
  University of Agriculture Faisalabad. `[unverified — confirm]`
- **This is the technical seam.** A remote-sensing contribution has a more
  natural point of contact here than with the governance strand.

### To research and add
- [ ] IWMI Pakistan country office — current groundwater research staff
- [ ] PCRWR (Pakistan Council of Research in Water Resources) — publication output
- [ ] Authors of recent GRACE-based Indus depletion papers (see `SOURCES.md`)
- [ ] LUMS Water Informatics / Technology group `[unverified — confirm this exists]`
- [ ] Daanish Mustafa (KCL) — political ecology of water in Pakistan `[unverified]`

---

## Institutions

| Institution | Role | Notes |
|---|---|---|
| Living Indus Initiative | GoP + UN Indus restoration programme | https://livingindus.org.pk/ `[verified]` |
| IWMI | International water research, Pakistan office | Publishes openly |
| PCRWR | Federal water research council | Operates groundwater monitoring wells |
| WAPDA | Water and Power Development Authority | Infrastructure, some hydrological data |
| IRSA | Indus River System Authority | Inter-provincial surface allocation |
| LUMS MGSHSS | Academic | Teaching + research base |
| Sussex IDS / Dept. International Development | Academic | Governance strand |

---

## Venues

**Journals** — Water Resources Research · Hydrology and Earth System Sciences
(HESS, open access) · Journal of Hydrology · Water International · Water
Alternatives (open access, governance-friendly) · Water Policy · Environmental
Research Letters · Nature Water · Remote Sensing of Environment

**Preprints and repositories** — EarthArXiv · ESS Open Archive (AGU) · SSRN ·
Zenodo

Water Alternatives and HESS are the most plausible first targets: both open
access, both receptive to work that bridges hydrology and governance.

---

## Datasets

| Dataset | What it gives | Access |
|---|---|---|
| GRACE / GRACE-FO mascon | Total water storage anomaly, ~300 km resolution | NASA JPL, open |
| GLDAS / NOAH | Modelled soil moisture, snow, surface water | NASA GES DISC, open |
| CHIRPS | Precipitation, 0.05° | Open |
| ERA5 / ERA5-Land | Reanalysis climate | Copernicus, open |
| MODIS MOD16 | Evapotranspiration | Open |
| Sentinel-1 SAR | Surface water, soil moisture proxies, subsidence (InSAR) | Copernicus, open |
| Sentinel-2 / Landsat | Cropping patterns, irrigated area | Open |
| PCRWR monitoring wells | In-situ water table depth | Restricted / request `[unverified]` |
| Tubewell census | Abstraction point density | Pakistan Agricultural Census `[unverified]` |

**The standard method** — groundwater storage anomaly = GRACE total water
storage minus modelled soil moisture, snow, and surface water — is well
established globally. The Indus-specific difficulty is that GRACE's footprint is
coarse relative to the governance units (districts, canal commands) that policy
actually operates on. Bridging that resolution gap is the open problem.

---

## Open questions worth a paper

1. ~~Can GRACE-derived depletion be downscaled to canal-command or district
   resolution?~~ **Closed 2026-08-11 — this is done.** Arshad et al. (2024,
   Water Resources Research) downscale to 1 km² across 20 Indus sub-regions
   using geographically-weighted random forest. See Project 01.
2. Does groundwater depletion rate correlate with the *institutional* variables
   the governance literature proposes — canal-tail position, colonial-era
   settlement type, electricity tariff regime — at a resolution where that
   correlation is testable?
3. What is the measurement uncertainty on published Indus abstraction figures,
   and how much of the policy debate is downstream of a number nobody can defend?

Question 2 is the bridge between the two strands and the most defensible
collaboration premise: it requires both the governance framing and the technical
work, and neither side can do it alone. **With question 1 now closed by
published work, question 2 is also cheaper to attempt** — the depletion surface
is an input rather than something to build. This is now Project 01.

---

## Quantitative strand — key works

- **Arshad et al. (2024).** *Downscaled-GRACE Data Reveal Anthropogenic and
  Climate-Induced Water Storage Decline Across the Indus Basin.* Water Resources
  Research. 1 km² downscaling, 20 sub-regions, 2002–2023, RFgw model. Declining
  TWS/GWS in all 20 sub-regions, steepest downstream. No institutional
  variables. `[verified — citation and abstract; full text paywalled]`
  https://doi.org/10.1029/2023WR035882
- *Downscaling GRACE/GRACE-FO data ... transboundary Indus Basin and its
  sub-regions.* ESS Open Archive preprint. `[verified — preprint exists]`
  https://doi.org/10.22541/essoar.173395770.08839790/v1
- *Bridging the resolution gap: ML for local-scale groundwater drought
  monitoring in Punjab, Pakistan.* J. Hydrology: Regional Studies (2025).
  `[unverified — title/venue only]`
- *GRACE Downscaling and Machine Learning Models for Groundwater Prediction: A
  Systematic Review.* Hydrology (2025). `[verified]`
  https://doi.org/10.3390/hydrology13050135

## Institutional strand — established mechanisms

- **Canal position.** Tail-end farmers receive less canal water (partly from
  upstream theft) and pump deeper, more brackish groundwater than head-reach
  farmers. Evidence base is ~4,000 watercourse outlets across Punjab, via World
  Bank analysis. `[verified — mechanism established]`
  https://documents1.worldbank.org/curated/en/099141503012329215/pdf/P17671802abac1004084c10f1343a94e4fe.pdf
- **Electricity subsidies** function as de facto abstraction policy, encouraging
  extraction above the unsubsidised level. `[verified — mechanism established]`
- Farm-level demand estimation exists for Punjab, Pakistan (positive
  mathematical programming, n≈200 farms). `[unverified]`

**The seam:** these mechanisms are established at farm-survey scale and have not
been spatially joined to the downscaled depletion surface. `[assumption — needs
a systematic search to confirm]`
