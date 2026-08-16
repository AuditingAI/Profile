# Related Work — How the Governance Literature Maps to Project 01

Last updated: 2026-08-16

**Standing caveat.** Everything below is built from abstracts, chapter titles,
and profile summaries. **None of the primary sources have been read in full
yet.** This document is therefore a *hypothesis about what the literature
claims*, not a summary of it. Every mapping below must be re-checked against the
actual text before any of it goes in a draft. Reading I2 (Nabeel 2021) is the
single highest-value action for this file.

---

## Why this document exists

Project 01 tests whether institutional geography explains groundwater depletion.
But "institutional geography" is not a variable you can download — it is a set of
claims made by the governance literature, which have to be translated into
things that can be measured and joined to a map.

That translation is the actual intellectual work of the project. This document
is where it happens.

---

## The governance literature's claims

Reconstructed from public summaries. Confidence markers apply.

### Claim 1 — The crisis is one of governance, not scarcity

The framing in Nabeel (2021), *Groundwater Crisis: A Crisis of Governance?* —
the Indus groundwater problem is not primarily a hydrological shortage but an
institutional failure: no abstraction licensing, no metering, no effective
regulation of millions of private tubewells. `[unverified — inferred from title
and abstract; must read]`

**What this claims empirically:** that depletion patterns should track
*institutional* boundaries and regimes, not just physical water availability.

**Why it has not been tested:** until the downscaled depletion surface existed
(Arshad et al. 2024), there was nothing to test it against at a resolution where
institutional boundaries are visible.

### Claim 2 — Path dependence from colonial canal design

The doctoral argument: present-day groundwater non-governance traces to the
historical evolution of the canal irrigation system, with colonial-era
institutional choices creating dependencies that persist. `[unverified —
inferred from thesis description; must read]`

**What this claims empirically:** that depletion should vary systematically with
*historical* institutional categories — canal colony boundaries, settlement
type, tenure class — even after controlling for present-day physical and
economic conditions.

This is the strongest claim in the literature and the least tested, because
coding colonial settlement categories spatially is laborious and hydrologists
have no reason to do it.

### Claim 3 — Transboundary framing

Nabeel & Cheema (2021), *Pakistan's Transboundary Water Challenge.* Surface-water
allocation is treaty-governed; groundwater is not, and the two interact.
`[unverified]`

**Relevance to Project 01:** mostly scoping. It argues surface allocation and
groundwater abstraction are coupled — which is why surface-water delivery has to
be a control variable, not ignored.

---

## The mapping — claims to testable variables

| Literature claim | Project 01 variable | Measurable? | Source |
|---|---|---|---|
| No effective abstraction regulation → depletion tracks incentives, not rules | Electricity tariff regime by feeder/region | Probably | NEPRA tariff notifications `[unverified]` |
| Tail-enders compensate for canal shortfall by pumping | Canal command position (head/middle/tail) | **Unknown — go/no-go** | Punjab Irrigation Dept.; World Bank annex |
| Colonial path dependence | Canal colony boundary, settlement/tenure class | Doubtful | Historical settlement reports `[assumption]` |
| Surface and groundwater are coupled | Canal surface-water delivery volume | Probably | Provincial irrigation records `[unverified]` |
| Cropping choice drives abstraction | Rice/sugarcane share | Yes | Sentinel-2, crop reporting |

**The honest read of this table:** two of the five are probably obtainable, one
is the project's go/no-go, one is doubtful, and one is easy. The colonial
path-dependence variable — the most interesting claim in the literature — is the
least likely to be codeable. Do not build the project's headline around it.

---

## What each side has that the other lacks

**The governance strand has** the causal mechanisms, the historical archive, the
institutional vocabulary, and the reason anyone should care. It has no
quantitative test of its central claim, because until 2024 the data did not
exist at usable resolution.

**The quantitative strand has** a 1 km depletion surface for 2002–2023 across 20
sub-regions. It explains that surface with rainfall, irrigated area, and
population — none of which are institutions. Arshad et al. attribute decline to
"anthropogenic" drivers without asking *which human institutions*. `[unverified
— based on abstract; the full paper may contain more]`

**The join is the contribution.** Not a new method, not a new dataset — the
observation that one field produced the exact measurement the other field needed
to test its central claim, and nobody has connected them.

---

## How to build on this rather than restate it

Three postures, in descending order of value:

1. **Test the claim.** Take Claim 1 or 2 as a stated hypothesis, operationalise
   it, run it against the depletion surface, report what happens including a
   null. This *adds* to the literature — it converts an argument into a finding.
2. **Bound the claim.** Establish the measurement uncertainty on published
   abstraction figures and show how much of the policy debate rests on numbers
   nobody can defend. This is question 3 in `FIELD-MAP.md` and is a genuinely
   useful paper.
3. **Restate the claim with new decoration.** Add a map to an existing argument.
   Contributes nothing and is transparent to reviewers. Avoid.

Posture 1 is the project. Posture 2 is the fallback if the canal data does not
exist.

---

## Reading queue — in order

1. **World Bank, Groundwater Irrigation in Punjab (Annex 3)** — free PDF, and it
   determines whether the canal-position variable is obtainable. Read first
   because it can kill or unblock the project.
2. **Nabeel (2021), Groundwater Crisis: A Crisis of Governance?** — the primary
   statement of Claim 1 and 2. Everything in this document above is
   reconstruction until this is read. Available via ResearchGate request.
3. **Arshad et al. (2024)** — confirm what the depletion surface actually
   contains, whether it is publicly released, and whether they already tested
   any institutional variable.
4. **Nabeel & Cheema (2021)** — scoping, lower priority.

After reading 1–3, rewrite this document. It should look substantially different,
and if it does not, the reading was not careful enough.

---

## Note on approach

If this work reaches the point of a draft, standard scholarly practice applies:
cite the governance literature properly, and if the work directly tests a
specific author's stated claim, it is normal and courteous to send them the
preprint when it is public. That is a professional courtesy extended after the
work exists — not a precondition for doing it, and not a reason to do it.
