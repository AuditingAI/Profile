# Project 01 — Downscaling Indus Groundwater Depletion to Governance Units

Status: **scoping** · Owner: YA · Opened 2026-08-11

## The gap

Groundwater governance in the Indus Basin is debated at the level of provinces,
districts, and canal commands. Groundwater *measurement* from satellite
gravimetry (GRACE / GRACE-FO) resolves at roughly 300 km — coarser than every
unit at which policy is made. So the governance literature argues about
institutions using a depletion signal that cannot be attributed to any specific
institution.

That is a genuine, stateable gap. It is also the kind of gap that is closed by
methods work rather than by fieldwork, which makes it tractable from outside
Pakistan and outside a hydrology department.

## Proposed contribution

Estimate groundwater storage change at district / canal-command resolution by
downscaling the GRACE signal using higher-resolution covariates, then test
whether the resulting spatial pattern correlates with institutional variables
the governance literature proposes.

### Method sketch

1. **Baseline.** Groundwater storage anomaly = GRACE total water storage anomaly
   − (soil moisture + snow water equivalent + surface water), the latter three
   from GLDAS/NOAH. This is the standard approach; reproduce it first for the
   whole basin and validate against any available PCRWR well records.
2. **Covariates at fine resolution.**
   - Sentinel-1 InSAR land subsidence — subsidence is a physical consequence of
     aquifer compaction and is available at tens of metres.
   - Sentinel-2 / Landsat cropping intensity and crop type — proxies for
     irrigation demand.
   - MODIS MOD16 evapotranspiration — the consumptive-use term.
   - Canal surface-water delivery records where obtainable — abstraction is
     partly a residual of surface supply shortfall.
3. **Downscaling.** Fit a statistical model (random forest or a Bayesian
   spatial model) mapping covariates to the coarse GRACE signal, then predict at
   covariate resolution. Validate with held-out in-situ wells.
4. **Institutional test.** Regress district-level depletion rate on:
   - position on the canal (head / middle / tail)
   - electricity tariff regime and subsidy history
   - colonial-era settlement and land-tenure classification
   - tubewell density from agricultural census

### Honest risks

- **Downscaling can manufacture structure.** A model trained to predict a coarse
  signal from fine covariates will produce fine-resolution output whether or not
  that output is real. Validation against independent in-situ data is not
  optional; without it this is not publishable, and should not be published.
- **In-situ well data may be unobtainable.** PCRWR access is the critical
  dependency. If it fails, the project reduces to a methods paper with synthetic
  validation only — still publishable, considerably weaker.
- **The institutional variables may be uncodeable.** Colonial settlement
  classification in particular may not exist in machine-readable form.
- **This may already exist.** GRACE downscaling is an active global literature.
  **Do the literature search before writing any code.** If someone has done this
  for the Indus, the contribution is the institutional test, not the method.

## Immediate next steps

- [ ] Literature search: "GRACE downscaling", "groundwater downscaling machine
      learning", restricted to Indus / South Asia. Establish what exists.
- [ ] Reproduce the standard basin-scale GRACE groundwater anomaly. This is a
      solved problem and a good calibration of whether the toolchain works.
- [ ] Establish whether PCRWR well data is obtainable, and on what terms.
- [ ] Write a one-page problem statement. If it cannot be stated in one page,
      it is not yet a project.

## On collaboration

The point of doing steps 1–4 above *before* approaching anyone is that it
changes the nature of the approach. "I have reproduced the basin-scale signal,
here is the notebook, I think it can be pushed to district resolution but I need
ground-truth wells" is a collaboration proposal. "I would like to collaborate"
is a request for someone else's time.

Norms worth holding to:

- Approach on the work, citing specific papers you have actually read.
- One message. If there is no reply, that is a reply.
- Never list anyone as a co-author without explicit written consent.
- Publish what you produce under your own name regardless of whether anyone
  joins. The work should stand alone; that is what makes it worth joining.
