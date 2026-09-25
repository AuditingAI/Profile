#!/usr/bin/env python3
"""
Cross-national feasibility: what happens to a specialist-population design
when it has to clear its threshold in several countries at once.

The single-country case is feasibility.py. This is the extension promised to
Prof. Newburry on 3 September 2026, built from two empirical inputs:

  prevalence   — the qualifying study's own panel screen: 20 eligible of
                 334,976, about six per hundred thousand.
  response     — Harzing, Reiche & Pudelko (2012), Challenges in International
                 Survey Research, Illustration 7. Their project 2 response
                 rates, by country.

The claim the model makes precise: a comparative design needs EVERY national
frame to clear the threshold at the same time, so joint feasibility is the
PRODUCT of per-country probabilities, not their average. That is why adding
countries breaks a design faster than adding respondents fixes it.

Stdlib only. Run:  python3 crossnational.py
"""

# ── Empirical inputs ─────────────────────────────────────────────────────────
# Harzing et al. (2012), Illustration 7. Response rates from their project 2.
# NOTE: Korea's 47% was achieved by telephone through a survey company, not by
# the same instrument as the rest. It is carried here but flagged, because a
# method effect that large is not a country effect.
HARZING_2012 = {
    "China":            0.040,
    "UK":               0.052,
    "France":           0.066,
    "Japan":            0.104,
    "Germany":          0.111,
    "Nordic countries": 0.113,
    "Australia/NZ":     0.127,
    "Spain":            0.154,
    "Korea (telephone)": 0.470,
}
OVERALL_EX_KOREA = 0.096

# The qualifying study, as fielded. Source: dba/STUDY_OVERVIEW.md
PREVALENCE   = 20 / 334_976     # ≈ 5.97 per 100,000
SCREEN_SURVIVAL = 4 / 23        # usable ÷ raw starts ≈ 0.174


def reachable(frame, prevalence, response, screen_survival=SCREEN_SURVIVAL):
    """Usable responses reachable from one national frame."""
    return frame * prevalence * response * screen_survival


def frame_needed(target, prevalence, response, screen_survival=SCREEN_SURVIVAL):
    """Panel members required in one country to reach `target` usable responses."""
    denom = prevalence * response * screen_survival
    return float("inf") if denom == 0 else target / denom


def joint_feasible(countries, frame_per_country, target_per_country,
                   prevalence=PREVALENCE):
    """Probability-style joint check across countries.

    A comparative design is viable only if EVERY frame clears its threshold.
    Returns per-country results and whether all clear.
    """
    rows, all_clear = [], True
    for name in countries:
        r = HARZING_2012[name]
        got = reachable(frame_per_country, prevalence, r)
        clears = got >= target_per_country
        all_clear = all_clear and clears
        rows.append((name, r, got, clears))
    return rows, all_clear


def main():
    print("=" * 74)
    print("CROSS-NATIONAL FEASIBILITY — specialist professional population")
    print("=" * 74)
    print(f"prevalence      {PREVALENCE:.8f}  ({PREVALENCE*100_000:.1f} per 100,000)")
    print(f"screen survival {SCREEN_SURVIVAL:.3f}  (4 usable of 23 raw)")
    print(f"response rates  Harzing et al. (2012), Illustration 7")
    print()

    # 1 · One country at a time: what frame is needed for 30 usable responses?
    TARGET = 30
    print(f"[1] Frame required for {TARGET} usable responses, per country")
    print("-" * 74)
    print(f"{'country':<20}{'resp.':>8}{'frame needed':>20}")
    for name, r in sorted(HARZING_2012.items(), key=lambda kv: kv[1]):
        need = frame_needed(TARGET, PREVALENCE, r)
        print(f"{name:<20}{r*100:>7.1f}%{need:>20,.0f}")
    print()

    # 2 · The compounding claim, stated as arithmetic
    print("[2] Adding countries — what the DESIGN then requires")
    print("-" * 74)
    TARGET_PC = 30
    order = ["Spain", "Germany", "Japan", "UK", "China"]
    print(f"target {TARGET_PC} usable responses in EVERY country in the design.")
    print("A comparative design is only as feasible as its weakest frame.")
    print()
    print(f"{'design':<40}{'mean resp':>11}{'binding':>10}{'frame needed EACH':>19}")
    for k in range(1, len(order) + 1):
        subset = order[:k]
        rates = [HARZING_2012[c] for c in subset]
        mean_r = sum(rates) / len(rates)
        binding_country = min(subset, key=lambda c: HARZING_2012[c])
        binding_r = HARZING_2012[binding_country]
        need = frame_needed(TARGET_PC, PREVALENCE, binding_r)
        label = " + ".join(subset)
        if len(label) > 38:
            label = label[:35] + "..."
        print(f"{label:<40}{mean_r*100:>10.1f}%{binding_r*100:>9.1f}%{need:>19,.0f}")
    print()
    print("The mean barely moves: 15.4% down to 9.2%. The requirement moves by")
    print("a factor of four, because the design is priced by its worst country,")
    print("not its average one. Every added frame can only lower the binding rate,")
    print("never raise it. That is the compounding, and it is one-directional.")
    print()

    # 3 · The honest caveat
    print("[3] What this model does NOT claim")
    print("-" * 74)
    print("· Prevalence is held constant across countries. It almost certainly is not.")
    print("  No cross-national prevalence data for this population exists yet; obtaining")
    print("  it is the empirical contribution the project proposes.")
    print("· Harzing's rates are from ONE study, one instrument, one period.")
    print("· Korea's 47% is a telephone effect, not a country effect. A method change")
    print("  moved the number roughly five times more than any country difference here,")
    print("  which suggests instrument choice may matter more than site selection.")
    print("· Rates are treated as independent. In reality they correlate.")
    print()


if __name__ == "__main__":
    main()
