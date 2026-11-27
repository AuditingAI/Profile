# Concept note: does groundwater depletion follow the institutional map?

Yasir A. Malik · November 2026 · concept stage, no analysis yet

## The gap

Two strands of work on Indus Basin groundwater have not met.

- **Measurement.** GRACE satellite gravimetry, downscaled to about 1 km, now shows groundwater
  storage declining across all 20 Indus sub-regions from 2002 to 2023, fastest downstream. The
  decline is explained with climate and land use (Arshad et al., 2024).
- **Governance.** A long-standing argument holds that Punjab's groundwater problem is an
  institutional one. It runs through the design of the canal system, where a farmer sits on
  it, what electricity costs, and how land is held (Nabeel, 2021; World Bank evidence on
  head- and tail-end watercourses).

The satellite work has the measurement but no institutional variables. The governance work has
the mechanisms but no spatial measure of depletion to test them against.

## The question

After controlling for rainfall, cropping and surface-water supply, does groundwater depletion
vary with institutional geography?

## The approach

1. **Outcome:** the downscaled depletion surface, aggregated to each main canal command. The
   variation within each command serves as a second outcome.
2. **Institutional variables:** head, middle or tail position; electricity tariff regime;
   tubewell density; historical tenure class where it can be coded.
3. **Controls:** rainfall (CHIRPS), evapotranspiration (MODIS), cropping intensity (Sentinel-2),
   and canal deliveries where available.
4. **Model:** a spatial regression across roughly 45 main canal commands, with spatial
   dependence handled explicitly. With about 45 units the model stays small.
5. **Commitment:** the design is fixed before results are seen. A null result will be
   reported.

## The binding constraint

**Digital canal-command boundaries for Punjab.** Command-level maps appear in an IFPRI
remote-sensing study and in an IWMI canal-crops dataset, but no open boundary file has been
found. If boundaries cannot be obtained, the project shifts to a smaller question: how much
uncertainty sits in published Indus abstraction figures.

## What each side would bring

- **Governance and institutional knowledge:** what the institutions are, and how to code them
  faithfully.
- **Quantitative design and data joining**, together with an auditor's question: how far can
  the satellite measure itself be trusted?

## Next step

A conversation about whether the question is well posed, and whether the boundaries exist.

Project page: https://github.com/MalikAI-786/indus-groundwater-institutions
