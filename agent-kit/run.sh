#!/usr/bin/env bash
# The one command. Run this first, every time.
#
#   ./agent-kit/run.sh            rules + streams + refresh discovery + queue
#   ./agent-kit/run.sh verify     check every document before you send one
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

  verify)
    # Run this before attaching anything to a real application. --rebuild
    # regenerates every PDF from its source and fails if the committed file
    # no longer matches; --html also re-renders the Chromium resumes.
    exec "$PY" scripts/verify_documents.py "${@:2}"
    ;;

  selftest)
    exec "$PY" scripts/verify_selftest.py
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

    echo
    echo "=========================================================================="
    echo "VERIFY - are the documents actually sendable"
    echo "=========================================================================="
    echo
    # A failure here means do not apply yet. It never blocks discovery: the
    # queue is still worth reading, you just cannot attach anything until the
    # failures below are fixed.
    "$PY" scripts/verify_documents.py || VERIFY_FAILED=1

    "$PY" agent-kit/brief.py --status
    "$PY" agent-kit/brief.py --next

    if [ "${VERIFY_FAILED:-0}" = "1" ]; then
      echo
      echo "  [stop] verification failed. Fix the documents before you apply."
      exit 1
    fi
    ;;
  *)
    echo "unknown mode: $MODE" >&2
    echo "use: rules | status | discover | verify | selftest | migrate | all" >&2
    exit 2
    ;;
esac
