#!/usr/bin/env python3
"""
Pre-fielding feasibility calculator for specialist-population research.

Turns the qualifying study's finding into an instrument: given a sampling frame
and the rates that apply to it, how many usable responses are actually reachable,
what will they cost, and is the design viable at all?

The model is validated against the case that produced it — 334,976 panel members,
~20 eligible, 4 usable, ~$1,000 spent. Run `python3 feasibility.py --validate`.

Stdlib only, matching ../03_Data/*.py. No dependencies.

Usage
    python3 feasibility.py --validate
    python3 feasibility.py --frame 334976 --prevalence 0.00006 --target 100
    python3 feasibility.py --frame 500 --prevalence 0.42 --target 12 --cost-per-invite 0
    python3 feasibility.py --sweep
"""

import argparse
import sys

# ── The qualifying study, as fielded ──────────────────────────────────────────
# Source: dba/STUDY_OVERVIEW.md §5, §7 and dba/03_Data/exclusion_log.csv
CASE = {
    "label": "Qualifying study — Prolific panel, July 2026",
    "frame": 334_976,      # panel members screened
    "eligible": 20,        # returned by the platform's own screening tool
    "raw": 23,             # raw starts (exceeds eligible: partials, re-entries)
    "usable": 4,           # survived the 9-step screening protocol
    "target": 100,
    "spend": 1000.0,
}


def feasibility(frame, prevalence, response_rate, completion_rate,
                exclusion_rate, target, cost_per_invite=0.0,
                incentive_per_complete=0.0):
    """Walk the funnel from frame to usable responses.

    Every rate is the proportion SURVIVING that stage, except exclusion_rate,
    which is the proportion REMOVED at screening.
    """
    eligible = frame * prevalence
    reached = eligible * response_rate
    completed = reached * completion_rate
    usable = completed * (1.0 - exclusion_rate)

    cost = eligible * cost_per_invite + completed * incentive_per_complete
    unit_cost = cost / usable if usable > 0 else float("inf")

    # Frame size needed to hit the target, holding every rate constant
    per_member = prevalence * response_rate * completion_rate * (1.0 - exclusion_rate)
    frame_needed = target / per_member if per_member > 0 else float("inf")

    return {
        "eligible": eligible,
        "reached": reached,
        "completed": completed,
        "usable": usable,
        "target": target,
        "shortfall": target - usable,
        "pct_of_target": (usable / target * 100.0) if target else 0.0,
        "cost": cost,
        "unit_cost": unit_cost,
        "frame_needed": frame_needed,
        "frame_multiple": frame_needed / frame if frame > 0 else float("inf"),
    }


def verdict(r, floor_survey=100, floor_interview=10):
    """Which design is viable at this reachable n?

    The whole point of the calculator: the same population that kills a survey
    can comfortably support an interview study.
    """
    n = r["usable"]
    if n >= floor_survey:
        return "SURVEY VIABLE", "Reachable n supports factor-analytic work."
    if n >= floor_interview:
        return ("INTERVIEW VIABLE — SURVEY IS NOT",
                "Too few for a survey. Sufficient for a phenomenological or "
                "case design. Change the method, not the budget.")
    if n >= 1:
        return ("NEITHER — REDEFINE THE FRAME",
                "Below an interview floor. The sampling frame is wrong, not "
                "the recruitment effort.")
    return "NO STUDY IS POSSIBLE HERE", "The population is not in this frame."


def fmt(r, label=""):
    v, why = verdict(r)
    out = []
    if label:
        out += [label, "=" * len(label)]
    out += [
        "",
        "  Funnel",
        f"    eligible in frame     {r['eligible']:>14,.0f}",
        f"    responded             {r['reached']:>14,.0f}",
        f"    completed             {r['completed']:>14,.0f}",
        f"    USABLE                {r['usable']:>14,.0f}",
        "",
        f"    target                {r['target']:>14,.0f}",
        f"    shortfall             {r['shortfall']:>14,.0f}"
        f"   ({r['pct_of_target']:.1f}% of target)",
    ]
    if r["cost"] > 0:
        out += [
            "",
            "  Cost",
            f"    total                 {r['cost']:>14,.2f}",
            f"    per usable response   {r['unit_cost']:>14,.2f}",
        ]
    out += [
        "",
        "  To hit the target at these rates",
        f"    frame needed          {r['frame_needed']:>14,.0f}"
        f"   ({r['frame_multiple']:.1f}x the frame you have)",
        "",
        f"  >> {v}",
        f"     {why}",
        "",
    ]
    return "\n".join(out)


def validate():
    """Reproduce the qualifying study from its own rates.

    If this does not land on the real figures, the model is wrong and nothing
    else in this file should be trusted.
    """
    c = CASE
    prevalence = c["eligible"] / c["frame"]
    # Raw starts exceeded the eligible count (partials, re-entries), so response
    # is capped at 1.0 and the overshoot is carried in completion.
    response_rate = min(1.0, c["raw"] / c["eligible"])
    completion_rate = c["raw"] / c["eligible"] / response_rate
    exclusion_rate = 1.0 - (c["usable"] / c["raw"])

    r = feasibility(
        frame=c["frame"], prevalence=prevalence, response_rate=response_rate,
        completion_rate=completion_rate, exclusion_rate=exclusion_rate,
        target=c["target"],
        incentive_per_complete=c["spend"] / c["raw"],
    )

    print(fmt(r, c["label"]))
    print("  Validation against what actually happened")
    print(f"    prevalence            {prevalence:.8f}"
          f"  ({prevalence * 100_000:.1f} per 100,000)")

    checks = [
        ("eligible", r["eligible"], c["eligible"], 0.5),
        ("usable",   r["usable"],   c["usable"],   0.5),
        ("spend",    r["cost"],     c["spend"],    1.0),
    ]
    ok = True
    for name, got, want, tol in checks:
        good = abs(got - want) <= tol
        ok = ok and good
        print(f"    {name:<10} modelled {got:>10,.1f}   actual {want:>10,.1f}"
              f"   {'PASS' if good else 'FAIL'}")

    print()
    if ok:
        print("  PASS — the model reproduces the study that produced it.")
    else:
        print("  FAIL — do not trust any other output from this file.")
    return 0 if ok else 1


def sweep():
    """Where the survey dies and the interview study lives.

    Same instrument, same rates, same target. Only the frame changes.
    """
    c = CASE
    prevalence = c["eligible"] / c["frame"]
    excl = 1.0 - (c["usable"] / c["raw"])

    print("Sensitivity — a general panel at 6 per 100,000")
    print(f"(prevalence {prevalence * 100_000:.1f}/100k, "
          f"exclusion {excl * 100:.0f}%, target 100)\n")
    print(f"  {'frame':>12}  {'eligible':>9}  {'usable':>7}   verdict")
    print(f"  {'-' * 12}  {'-' * 9}  {'-' * 7}   {'-' * 40}")
    for frame in (100_000, 334_976, 1_000_000, 5_000_000,
                  17_000_000, 50_000_000):
        r = feasibility(frame, prevalence, 1.0, 1.0, excl, 100)
        v, _ = verdict(r)
        print(f"  {frame:>12,}  {r['eligible']:>9,.0f}  "
              f"{r['usable']:>7,.0f}   {v}")

    print("\n  A survey needs a frame of roughly "
          f"{feasibility(1, prevalence, 1.0, 1.0, excl, 100)['frame_needed']:,.0f} "
          "members at this prevalence.")
    print("  No commercial panel is that large. The design is not "
          "under-resourced; it is impossible.\n")

    print("The same population, asked for an interview study")
    print("  The survey's 83% exclusion rate does not carry over. It came from")
    print("  attention checks, partial completions and screen failures on an")
    print("  anonymous instrument. An interview study contacts eligible people")
    print("  directly and loses them to declining and no-shows instead.")
    print("  Rates below are ESTIMATES and are marked [VERIFY].\n")

    r = feasibility(c["frame"], prevalence,
                    response_rate=0.80,     # [VERIFY] agrees to be contacted
                    completion_rate=0.80,   # [VERIFY] interview actually happens
                    exclusion_rate=0.05,    # [VERIFY] fails screen criterion 4
                    target=12)
    v, why = verdict(r)
    print(f"  eligible {r['eligible']:,.0f} -> {r['usable']:,.0f} interviews "
          f"against a target of 12")
    print(f"  >> {v}\n     {why}\n")
    print("  Same population. Same 20 people. The method changed, and with it")
    print("  what counts as enough.\n")
    return 0


def main():
    p = argparse.ArgumentParser(
        description="Pre-fielding feasibility for specialist populations.")
    p.add_argument("--validate", action="store_true",
                   help="reproduce the qualifying study and check the model")
    p.add_argument("--sweep", action="store_true",
                   help="show where a survey stops being viable")
    p.add_argument("--frame", type=float, help="sampling frame size")
    p.add_argument("--prevalence", type=float,
                   help="proportion of the frame that is eligible")
    p.add_argument("--target", type=float, default=100, help="usable n needed")
    p.add_argument("--response-rate", type=float, default=1.0)
    p.add_argument("--completion-rate", type=float, default=1.0)
    p.add_argument("--exclusion-rate", type=float, default=0.0,
                   help="proportion REMOVED at screening")
    p.add_argument("--cost-per-invite", type=float, default=0.0)
    p.add_argument("--incentive-per-complete", type=float, default=0.0)
    a = p.parse_args()

    if a.validate:
        return validate()
    if a.sweep:
        return sweep()
    if a.frame is None or a.prevalence is None:
        p.print_help()
        print("\nStart with:  python3 feasibility.py --validate")
        return 1

    r = feasibility(a.frame, a.prevalence, a.response_rate,
                    a.completion_rate, a.exclusion_rate, a.target,
                    a.cost_per_invite, a.incentive_per_complete)
    print(fmt(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
