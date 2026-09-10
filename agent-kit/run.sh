#!/usr/bin/env bash
# The one command. Run this first, every time.
#
#   ./agent-kit/run.sh            rules + streams + refresh discovery + queue
#   ./agent-kit/run.sh status     queue counts and top roles, no network
#   ./agent-kit/run.sh discover   refresh the queue only
#   ./agent-kit/run.sh migrate    re-stamp queued roles after a config change
#   ./agent-kit/run.sh rules      print the rules and exit
#
# Reads only committed files and public job boards. Never touches a credential
# and never submits anything - see agent-kit/rules.json rule 1.

set -euo pipefail

KIT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$KIT")"
cd "$ROOT"

PY="${PYTHON:-python3}"
MODE="${1:-all}"

case "$MODE" in
  rules)
    exec "$PY" agent-kit/brief.py --rules
    ;;
  status)
    exec "$PY" agent-kit/brief.py --status
    ;;
  discover)
    exec "$PY" scripts/discover_jobs.py
    ;;
  migrate)
    # Re-stamp already-queued roles after the default resume or the stream
    # strategy changes. Never deletes anything.
    exec "$PY" agent-kit/migrate_queue.py "${@:2}"
    ;;
  all)
    "$PY" agent-kit/brief.py --rules

    echo
    echo "=========================================================================="
    echo "DISCOVERY - refreshing the queue across all three streams"
    echo "=========================================================================="
    echo
    # A dead source is reported, not fatal. Discovery failing entirely still
    # leaves the existing queue worth working, so keep going either way.
    if ! "$PY" scripts/discover_jobs.py; then
      echo
      echo "  [warn] discovery did not complete. The existing queue below is"
      echo "         still valid - work it. If every source failed, you are"
      echo "         probably behind a proxy that blocks job boards."
    fi

    "$PY" agent-kit/brief.py --status
    "$PY" agent-kit/brief.py --next
    ;;
  *)
    echo "unknown mode: $MODE" >&2
    echo "use: rules | status | discover | all" >&2
    exit 2
    ;;
esac
