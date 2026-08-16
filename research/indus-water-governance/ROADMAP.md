# Roadmap

Last updated: 2026-08-16

This describes what is *happening*, not what was hoped. The biweekly check-in
updates it when reality diverges from the plan. If a phase has sat unchanged for
three check-ins, that is a signal to shrink it, not to restate it.

---

## The end state

A public, citable body of work on **why groundwater is disappearing from the
Indus Basin and what institutional arrangements make it worse or better** — with
the data, code, and methods open so that people working on Pakistani water
scarcity can build on it rather than rebuild it.

That is the goal. It is also several years of work, and it does not start by
being announced. It starts by doing one solid piece of work well.

---

## Phases

### Phase 0 — Infrastructure `IN PROGRESS · blocked on user`

Accounts and alerts so that outputs are attributable and the field is legible.

- [ ] ORCID (the blocker — everything references it)
- [ ] Google Scholar profile
- [ ] Scholar alerts (8 queries)
- [ ] Zenodo linked to ORCID + GitHub
- [ ] EarthArXiv

**Status:** not started. Calendar block set for Mon 17 Aug, 09:00 ET.
**Cost of delay:** low for a week, high after a month — without alerts you are
blind to someone publishing your project, which has already nearly happened once.

### Phase 1 — Read and decide `NOT STARTED`

- [ ] World Bank *Groundwater Irrigation in Punjab* (Annex 3) — free PDF
- [ ] Nabeel (2021), *Groundwater Crisis: A Crisis of Governance?*
- [ ] Arshad et al. (2024), *Downscaled-GRACE ... Indus Basin*
- [ ] **GO/NO-GO: do digital Punjab canal command boundaries exist?**
- [ ] Rewrite `RELATED-WORK.md` against what was actually read

**This phase decides whether Project 01 is real.** If canal geography is not
obtainable, the project changes shape here — not after three months of building.

### Phase 2 — Acquire and replicate `NOT STARTED`

- [ ] Obtain the downscaled depletion surface (public release, or author request)
- [ ] Reproduce one published basin-scale figure — proves the toolchain works
- [ ] Assemble institutional covariates that survived Phase 1
- [ ] Publish the assembled dataset to Zenodo with a DOI

The dataset release is the first citable output, and it is genuinely useful to
others whether or not the analysis ever lands.

### Phase 3 — The join `NOT STARTED`

Spatial regression of depletion on institutional variables, controlling for
rainfall, cropping pattern, and surface-water delivery. Spatial autocorrelation
handled properly.

- [ ] Analysis
- [ ] Preprint to EarthArXiv
- [ ] Journal submission — Water Alternatives or HESS

**Pre-committed:** a null result gets published. Decided now, before any results
are seen.

### Phase 4 — Open the work `NOT STARTED`

Split this research out of the profile repo into its own public repository:
data, code, methods, and a plain-language summary of what was found.

Preconditions — all three, no exceptions:

1. At least one output exists with a DOI. An empty public repo is noise.
2. Every `[unverified]` marker in the repo is resolved or removed. Publishing
   unverified claims about other people's work is the fastest way to lose
   standing in a small field.
3. Nothing in the repo depends on private correspondence or restricted data.

---

## What "merge" means here

Three distinct things, worth not confusing:

**1. Merging the two literatures.** The intellectual core. Governance research
has the causal argument and no data at testable resolution; satellite hydrology
just produced that data and explained it without institutions. Joining them is
the contribution. This is entirely within your control and needs nobody's
permission. See `RELATED-WORK.md`.

**2. Merging with existing programmes.** Living Indus, IWMI, and PCRWR all need
measurement infrastructure. Once a dataset with a DOI exists, it becomes
something to contribute rather than something to propose. Sequence matters: the
artifact first, the conversation second.

**3. Merging with individual collaborators.** Downstream of both of the above.
The norms are in `projects/01-...md` and they do not change: approach on the
work, cite what you have actually read, one message, no co-authorship without
written consent, publish under your own name regardless of who joins.

The through-line: **build the thing, then the collaborations become available.**
Reversing that order is the most common way projects like this stall.

---

## Honest assessment

The plan is sound and the gap is real. The risk is not intellectual — it is
attention. This competes with everything else you are building, and it has
already lost traction once.

The mitigation is that Phase 1 is cheap and decisive. Two PDFs and one question
about whether a shapefile exists. That is a few hours, not a quarter, and it
either unlocks a genuinely novel project or redirects you before you have spent
anything. Do not start Phase 2 until Phase 1 has actually been done.

If three check-ins pass with no movement, the right answer is to pause the
project honestly rather than let it become a source of low-grade guilt. A paused
project with good notes can be restarted. A project you have started avoiding
cannot.
