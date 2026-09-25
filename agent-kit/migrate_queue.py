"""Bring existing queue files up to the current rules, resume, and streams.

Queue entries are written once at discovery time, so a change to the default
resume or to the stream strategy leaves everything already queued stale. This
rewrites pending entries in place:

  - stamps _rules as the first key
  - re-runs the resume selection rule, so the current default applies
  - tags each entry with the stream its employer belongs to, or "legacy" for
    employers no longer on the target list

It never deletes anything. Off-strategy roles are tagged and reported, not
removed - some of them are good roles, and that call is Yasir's.

    python3 agent-kit/migrate_queue.py --dry-run
    python3 agent-kit/migrate_queue.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent
ROOT = KIT.parent
PENDING = ROOT / "automation" / "queue" / "pending"

sys.path.insert(0, str(ROOT / "scripts"))

from discover_jobs import QUEUE_RULES, load_strategy, pick_resume  # noqa: E402


def stream_for(company: str) -> str:
    """Which of the three streams this employer belongs to, if any."""
    low = company.lower()
    for stream in load_strategy()["streams"]:
        for target in stream["targets"]:
            name = target["company"].lower()
            # Match on the distinctive head of the name so "BNY" matches
            # "BNY Mellon" and "Google" matches "Google Cloud".
            head = name.split(" (")[0].split(" / ")[0]
            if head in low or low in head:
                return stream["id"]
    return "legacy"


def migrate(entry: dict) -> tuple[dict, list[str]]:
    changed: list[str] = []

    if entry.get("_rules") != QUEUE_RULES:
        changed.append("rules")

    want = pick_resume(entry.get("title", ""))
    if entry.get("package", {}).get("resume") != want:
        changed.append("resume")
        entry.setdefault("package", {})["resume"] = want

    stream = stream_for(entry.get("company", ""))
    if entry.get("stream") != stream:
        changed.append("stream")
        entry["stream"] = stream

    # Rebuild so _rules lands first regardless of the original key order.
    rebuilt = {"_rules": QUEUE_RULES}
    rebuilt.update({k: v for k, v in entry.items() if k != "_rules"})
    return rebuilt, changed


def main() -> int:
    dry = "--dry-run" in sys.argv
    if not PENDING.exists():
        print("no pending queue")
        return 0

    touched = 0
    by_stream: dict[str, int] = {}
    off_strategy: list[str] = []

    for path in sorted(PENDING.glob("*.json")):
        entry = json.loads(path.read_text(encoding="utf-8"))
        rebuilt, changed = migrate(entry)
        stream = rebuilt["stream"]
        by_stream[stream] = by_stream.get(stream, 0) + 1
        if stream == "legacy":
            off_strategy.append(f"{rebuilt.get('company')} - {rebuilt.get('title', '')[:50]}")
        if changed:
            touched += 1
            print(f"  {path.name}  {'+'.join(changed)}")
            if not dry:
                path.write_text(json.dumps(rebuilt, indent=2) + "\n",
                                encoding="utf-8")

    print(f"\n{'would update' if dry else 'updated'} {touched} entr"
          f"{'y' if touched == 1 else 'ies'}")
    print("by stream: " + ", ".join(f"{k} {v}" for k, v in sorted(by_stream.items())))

    if off_strategy:
        print(f"\n{len(off_strategy)} role(s) are from employers not on any of the "
              f"three target streams.")
        print("Tagged 'legacy' and left in place - decide whether to work or drop them:")
        for line in off_strategy:
            print(f"  {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
