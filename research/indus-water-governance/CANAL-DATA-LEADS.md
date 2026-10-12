# Canal-Command Data — Leads for the Project 01 Go/No-Go

Searched 12 Oct 2026. **Status: leans GO, not confirmed.** Every item below comes
from search-result snippets, not from the documents themselves. All `[unverified]`
until opened and read.

## What the search found

| Lead | What it suggests | Link |
|---|---|---|
| IFPRI/CGIAR, *Assessment of water allocations using remote sensing and GIS modeling for Indus Basin, Pakistan* (2016) | Maps of land use, crop water use, groundwater use and quality, salinity and yield at 250 m, reported **per canal command**. Open access on CGSpace. Most promising lead. | https://cgspace.cgiar.org/items/1a20b4a4-fb33-478e-99ad-1a3e2d881143 |
| IWMI canal-crops dataset, 1981–2009 | Crop area and production **by main canal command**, built by apportioning district data to commands. Shows IWMI holds command geography; unclear whether boundary files are included. | https://gender.cgiar.org/publications/crop-area-and-production-pakistan-canal-crops-pakistan |
| Punjab Government irrigation report (2024) | Lists irrigation zones with gross and culturable command areas. Index plan is a map figure, not a downloadable layer. | https://urbanunit.gov.pk/Download/publications/Files/19/2024/SRDP%20Irrigation%20Report%2024072024.pdf |
| Indiana DLC, *Land and Water Productivity: Trends Across Punjab Canal Commands* | Command-level analysis exists, so a command-level unit of analysis is accepted practice. | https://dlc.dlib.indiana.edu/dlc/items/d0517e5c-3f50-4b67-91a4-1a269faa50c5 |

No dedicated open boundary shapefile for Punjab canal commands turned up in two
searches.

## What this changes

**The unit of analysis is probably the canal command, not the district.** The
Indus system has about 45 major canal commands, so a regression across them has
roughly 45 observations. That is enough for a descriptive spatial join and thin
for a multivariable model.

Consequences for Project 01:

- State the sample size in every draft. Do not claim district-level resolution.
- Keep the control set small. With n ≈ 45, six or seven covariates is the ceiling.
- The 1 km depletion surface still earns its keep: aggregate it *within* each
  command, and use the within-command spread as a second outcome.
- The finer watercourse-outlet evidence (≈4,000 outlets, World Bank annex) is
  the route to a larger n, if outlet coordinates exist. Still unknown.

## What to ask her on the call

The brief asks "do digital canal-command boundaries exist, and who holds them?"
Sharper version, now that there are leads:

1. "I found command-level maps in an IFPRI study and an IWMI crop dataset. Are
   the boundary layers behind those obtainable, and from whom?"
2. "Is 45 commands enough resolution for your governance argument, or does the
   argument only show up at watercourse level?"

Question 2 is the one she can answer and he cannot. It tests whether her claim is
even testable at the available resolution.

## Still to do

- [ ] Open the IFPRI/CGSpace record; check whether the boundary layer is a
      downloadable file or only a published map.
- [ ] Open the IWMI canal-crops record; same check.
- [ ] If neither has a file: ask IWMI Pakistan, and ask her.
