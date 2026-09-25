"""Print the agent briefing: rules, streams, and the top of the queue.

Called by agent-kit/run.sh. Reads only committed files - no network, no
credentials, no side effects. Safe to run anywhere, any number of times.

    python3 agent-kit/brief.py            # rules + streams + queue + next steps
    python3 agent-kit/brief.py --rules    # rules only
    python3 agent-kit/brief.py --status   # queue counts and top roles only
    python3 agent-kit/brief.py --next     # next-steps block only
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent
ROOT = KIT.parent
QUEUE = ROOT / "automation" / "queue"

BAR = "=" * 74


def load(name: str) -> dict:
    return json.loads((KIT / name).read_text(encoding="utf-8"))


def print_rules() -> None:
    rules = load("rules.json")
    head = rules["_READ_THIS_FIRST"]
    print(BAR)
    print("RULES - read before doing anything")
    print(BAR)
    print(f"\nYou are: {head['you_are']}")
    print(f"The job: {head['the_job']}\n")
    for line in head["rules"]:
        print(f"  {line}")
    print("\nFacts that must be correct on every form:")
    ident, facts = rules["identity"], rules["facts_of_record"]
    for label, value in [
        ("Name", ident["name"]),
        ("Email", ident["email"]),
        ("Phone", ident["phone"]),
        ("Location", ident["location"]),
        ("Current employer", facts["current_employer"]),
        ("Degree in progress", facts["degree_in_progress"]),
        ("Examiner history", facts["examiner_history"]),
    ]:
        print(f"  {label:20} {value}")
    print(f"\nNever answer: {', '.join(rules['never_answer'])}")
    print(f"\nResume to attach: {rules['resume']['default']}")


def print_streams() -> None:
    strategy = load("strategy.json")
    print(f"\n{BAR}")
    print(f"STRATEGY - three streams, priority order ({strategy['version']})")
    print(BAR)
    for stream in strategy["streams"]:
        targets = stream["targets"]
        live = [t for t in targets if t.get("verified") and not t.get("excluded")]
        todo = [t for t in targets if not t.get("verified")]
        print(f"\n  {stream['priority']}. {stream['name']}  [{stream['id']}]")
        print(f"     {stream['why']}")
        print(f"     Wired and verified ({len(live)}): "
              f"{', '.join(t['company'] for t in live) or 'none yet'}")
        if todo:
            print(f"     Needs an endpoint ({len(todo)}): "
                  f"{', '.join(t['company'] for t in todo)}")
        for t in targets:
            if t.get("excluded"):
                print(f"     EXCLUDED: {t['company']} - {t['note']}")


def read_queue(folder: str) -> list[dict]:
    d = QUEUE / folder
    if not d.exists():
        return []
    out = []
    for path in sorted(d.glob("*.json")):
        try:
            out.append(json.loads(path.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError) as exc:
            print(f"  [warn] unreadable queue file {path.name}: {exc}",
                  file=sys.stderr)
    return out


def print_status() -> None:
    pending = read_queue("pending")
    submitted = read_queue("submitted")
    skipped = read_queue("skipped")

    print(f"\n{BAR}")
    print("QUEUE")
    print(BAR)
    print(f"\n  pending {len(pending)}   submitted {len(submitted)}   "
          f"skipped {len(skipped)}")

    if pending and not submitted:
        print(f"\n  {len(pending)} roles are queued and NONE have been submitted.")
        print("  Nothing downstream of discovery has ever run. Start with the")
        print("  local runner: cd automation/runner && docker compose run --rm login")

    pending.sort(key=lambda e: (-e.get("score", 0),
                                not e.get("sponsor_employer"),
                                e.get("company", "")))
    if pending:
        print(f"\n  Top {min(10, len(pending))} by score, work these first:\n")
        for e in pending[:10]:
            flag = "sponsor" if e.get("sponsor_employer") else "-"
            print(f"    [{e.get('score', 0)}] {flag:8} {e.get('company', '')[:20]:20} "
                  f"{e.get('title', '')[:44]}")
            print(f"        id {e.get('id')}  resume {Path(e.get('package', {}).get('resume', '')).name}")

    claimed = [e for e in pending if e.get("status") == "claimed"]
    if claimed:
        print(f"\n  {len(claimed)} claimed but not finished - check these are not "
              f"abandoned:")
        for e in claimed:
            agent = e.get("agent", {})
            print(f"    {e.get('id')} by {agent.get('claimed_by')} "
                  f"at {agent.get('claimed_at')}")


def print_next() -> None:
    print(f"\n{BAR}")
    print("WHAT TO DO NEXT")
    print(BAR)
    print("""
  1. Pick the highest-scoring pending role above.
  2. Set status to "claimed", fill agent.claimed_by and agent.claimed_at,
     and commit before you touch the employer's portal.
  3. Submit using package.resume verbatim. Stop at any immigration, salary
     history, EEO, or attestation field - those are Yasir's to answer.
  4. Move the file to automation/queue/submitted/ with a confirmation_ref
     pointing at the employer's confirmation email, or to skipped/ with a
     one-sentence reason. Commit the move.

  Full interface spec: automation/AGENT_CONTRACT.md
  Credential handling:  automation/runner/SECURITY.md
""")


def main() -> int:
    args = sys.argv[1:]
    if "--rules" in args:
        print_rules()
        return 0
    if "--status" in args:
        print_status()
        return 0
    if "--next" in args:
        print_next()
        return 0
    print_rules()
    print_streams()
    print_status()
    print_next()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
