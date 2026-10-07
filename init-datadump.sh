#!/usr/bin/env bash
#
# init-datadump.sh — scaffold a data-dump workspace.
#
# Creates a staging area for collecting raw files from arbitrary sources,
# tracking where each one came from, and verifying nothing rots on disk.
#
# Usage: ./init-datadump.sh [TARGET_DIR] [options]

set -euo pipefail

DATADUMP_VERSION="1.0.0"

usage() {
  cat <<'USAGE'
Usage: init-datadump.sh [TARGET_DIR] [options]

Initialize a data-dump workspace at TARGET_DIR (default: ./data-dump).

Options:
  -f, --force    Reinitialize: overwrite README.md and meta/dump.json.
                 Never deletes data already under the dump.
      --git      Run `git init` inside the dump (off by default — dumps
                 usually hold large binaries you do not want versioned).
  -h, --help     Show this help.

Re-running without --force is safe and idempotent: missing directories are
recreated and the bin/ helpers are refreshed, but your data and metadata
are left alone.

Layout created:
  inbox/       drop zone for unsorted files awaiting ingest
  raw/         immutable originals, organized as raw/<source>/<batch>/
  processed/   derived or cleaned output
  exports/     things headed back out of the dump
  logs/        init and ingest logs
  meta/        dump.json, manifest.jsonl, checksums.sha256
  bin/         ingest.sh, verify.sh
USAGE
}

TARGET=""
FORCE=0
DO_GIT=0

while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help) usage; exit 0 ;;
    -f|--force) FORCE=1; shift ;;
    --git) DO_GIT=1; shift ;;
    --) shift; break ;;
    -*) echo "init-datadump: unknown option: $1" >&2; usage >&2; exit 2 ;;
    *)
      if [ -n "$TARGET" ]; then
        echo "init-datadump: unexpected extra argument: $1" >&2
        exit 2
      fi
      TARGET="$1"; shift ;;
  esac
done

[ -n "$TARGET" ] || TARGET="./data-dump"

# Expand a leading ~ that arrived quoted, then resolve to an absolute path.
case "$TARGET" in
  "~") TARGET="$HOME" ;;
  "~/"*) TARGET="$HOME/${TARGET#\~/}" ;;
esac

if [ -e "$TARGET" ] && [ ! -d "$TARGET" ]; then
  echo "init-datadump: $TARGET exists and is not a directory" >&2
  exit 1
fi

mkdir -p "$TARGET"
DUMP_ROOT="$(cd -- "$TARGET" && pwd)"

ALREADY_INIT=0
[ -f "$DUMP_ROOT/meta/dump.json" ] && ALREADY_INIT=1

for d in inbox raw processed exports logs meta bin; do
  mkdir -p "$DUMP_ROOT/$d"
done

# Keep the skeleton visible to git even when the payload directories are empty.
for d in inbox raw processed exports; do
  [ -e "$DUMP_ROOT/$d/.gitkeep" ] || : > "$DUMP_ROOT/$d/.gitkeep"
done

[ -e "$DUMP_ROOT/meta/manifest.jsonl" ] || : > "$DUMP_ROOT/meta/manifest.jsonl"
[ -e "$DUMP_ROOT/meta/checksums.sha256" ] || : > "$DUMP_ROOT/meta/checksums.sha256"

NOW="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

# ---------------------------------------------------------------- dump.json
if [ "$ALREADY_INIT" -eq 0 ] || [ "$FORCE" -eq 1 ]; then
  cat > "$DUMP_ROOT/meta/dump.json" <<JSON
{
  "schema": "datadump/v1",
  "tool_version": "$DATADUMP_VERSION",
  "created_utc": "$NOW",
  "root": "$DUMP_ROOT",
  "layout": ["inbox", "raw", "processed", "exports", "logs", "meta", "bin"]
}
JSON
fi

# ---------------------------------------------------------------- .gitignore
# Regenerated on every run: it is derived, not authored.
cat > "$DUMP_ROOT/.gitignore" <<'GITIGNORE'
# Data payloads stay out of version control; the skeleton and metadata stay in.
inbox/*
raw/*
processed/*
exports/*
logs/*

!.gitkeep
!*/.gitkeep

.DS_Store
GITIGNORE

# ---------------------------------------------------------------- README.md
if [ ! -f "$DUMP_ROOT/README.md" ] || [ "$FORCE" -eq 1 ]; then
  cat > "$DUMP_ROOT/README.md" <<README
# Data dump

Initialized $NOW by \`init-datadump.sh\` v$DATADUMP_VERSION.

## Layout

| Path | Holds |
| --- | --- |
| \`inbox/\` | Unsorted drops waiting to be ingested. Treated as scratch. |
| \`raw/\` | Immutable originals, as \`raw/<source>/<batch-timestamp>/\`. Never edit in place. |
| \`processed/\` | Anything derived from \`raw/\` — cleaned, parsed, converted. Reproducible. |
| \`exports/\` | Artifacts leaving the dump. |
| \`logs/\` | \`init.log\`, \`ingest.log\`. |
| \`meta/\` | \`dump.json\` (dump identity), \`manifest.jsonl\` (one record per ingested file), \`checksums.sha256\`. |
| \`bin/\` | \`ingest.sh\`, \`verify.sh\`. |

## Ingesting

Copy specific files in, tagged with the source they came from:

    bin/ingest.sh --source gmail ~/Downloads/takeout-*.zip

Sweep whatever has accumulated in \`inbox/\` (files are **moved** out of the
inbox, unlike named files, which are copied and left where they are):

    bin/ingest.sh --source misc

Each ingested file lands under \`raw/<source>/<UTC batch timestamp>/\`, gets a
record appended to \`meta/manifest.jsonl\`, and gets its SHA-256 recorded in
\`meta/checksums.sha256\`.

## Verifying

    bin/verify.sh

Re-hashes every ingested file and exits non-zero if anything is missing or
has changed on disk.
README
fi

# ---------------------------------------------------------------- bin/ingest.sh
cat > "$DUMP_ROOT/bin/ingest.sh" <<'INGEST'
#!/usr/bin/env bash
#
# ingest.sh — copy files into the dump's raw/ tree with provenance recorded.

set -euo pipefail

DUMP_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
MANIFEST="$DUMP_ROOT/meta/manifest.jsonl"
CHECKSUMS="$DUMP_ROOT/meta/checksums.sha256"
LOG="$DUMP_ROOT/logs/ingest.log"

SOURCE="misc"
FILES=()

usage() {
  cat <<'USAGE'
Usage: ingest.sh [--source NAME] [FILE...]

Copy FILEs into raw/<source>/<batch>/ and record provenance.
With no FILEs, sweeps everything under inbox/ (moving it out of the inbox).

Options:
  -s, --source NAME   Source label for this batch (default: misc).
  -h, --help          Show this help.
USAGE
}

while [ $# -gt 0 ]; do
  case "$1" in
    -h|--help) usage; exit 0 ;;
    -s|--source)
      [ $# -ge 2 ] || { echo "ingest: --source needs a value" >&2; exit 2; }
      SOURCE="$2"; shift 2 ;;
    --source=*) SOURCE="${1#--source=}"; shift ;;
    --) shift; while [ $# -gt 0 ]; do FILES+=("$1"); shift; done ;;
    -*) echo "ingest: unknown option: $1" >&2; exit 2 ;;
    *) FILES+=("$1"); shift ;;
  esac
done

# Keep source labels safe as a single path component.
SOURCE="$(printf '%s' "$SOURCE" | tr -c 'A-Za-z0-9._-' '_')"
[ -n "$SOURCE" ] || SOURCE="misc"

sha256_of() {
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum -- "$1" | awk '{print $1}'
  else
    shasum -a 256 -- "$1" | awk '{print $1}'
  fi
}

json_escape() {
  printf '%s' "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g' -e 's/\t/\\t/g'
}

FROM_INBOX=0
if [ "${#FILES[@]}" -eq 0 ]; then
  FROM_INBOX=1
  while IFS= read -r f; do
    case "$(basename -- "$f")" in .gitkeep) continue ;; esac
    FILES+=("$f")
  done < <(find "$DUMP_ROOT/inbox" -type f | sort)
fi

if [ "${#FILES[@]}" -eq 0 ]; then
  echo "ingest: nothing to ingest (inbox/ is empty and no files were named)"
  exit 0
fi

BATCH="$(date -u +%Y%m%dT%H%M%SZ)"
DEST_REL="raw/$SOURCE/$BATCH"
DEST="$DUMP_ROOT/$DEST_REL"
mkdir -p "$DEST"

count=0
for src in "${FILES[@]}"; do
  if [ ! -f "$src" ]; then
    echo "ingest: skipping (not a regular file): $src" >&2
    continue
  fi

  abs_src="$(cd -- "$(dirname -- "$src")" && pwd)/$(basename -- "$src")"
  name="$(basename -- "$src")"

  # Never clobber within a batch.
  target="$DEST/$name"
  n=1
  while [ -e "$target" ]; do
    target="$DEST/${name%.*}-$n${name##"${name%.*}"}"
    [ "$name" = "${name%.*}" ] && target="$DEST/$name-$n"
    n=$((n + 1))
  done

  cp -p -- "$src" "$target"

  hash="$(sha256_of "$target")"
  if [ "$hash" != "$(sha256_of "$abs_src")" ]; then
    echo "ingest: copy verification failed for $src" >&2
    rm -f -- "$target"
    exit 1
  fi

  bytes="$(wc -c < "$target" | tr -d ' ')"
  rel="${target#"$DUMP_ROOT/"}"
  ts="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

  printf '{"ts":"%s","source":"%s","batch":"%s","origin":"%s","stored":"%s","bytes":%s,"sha256":"%s"}\n' \
    "$ts" "$(json_escape "$SOURCE")" "$BATCH" "$(json_escape "$abs_src")" \
    "$(json_escape "$rel")" "$bytes" "$hash" >> "$MANIFEST"

  printf '%s  %s\n' "$hash" "$rel" >> "$CHECKSUMS"

  # Files swept from the inbox are moved, not copied — the inbox is scratch.
  [ "$FROM_INBOX" -eq 1 ] && rm -f -- "$abs_src"

  count=$((count + 1))
done

if [ "$count" -eq 0 ]; then
  rmdir "$DEST" 2>/dev/null || true
  echo "ingest: no files ingested"
  exit 0
fi

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ingest source=$SOURCE batch=$BATCH files=$count" >> "$LOG"
echo "ingest: $count file(s) -> $DEST_REL"
INGEST

# ---------------------------------------------------------------- bin/verify.sh
cat > "$DUMP_ROOT/bin/verify.sh" <<'VERIFY'
#!/usr/bin/env bash
#
# verify.sh — re-hash every ingested file and report drift.

set -euo pipefail

DUMP_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
CHECKSUMS="$DUMP_ROOT/meta/checksums.sha256"

cd "$DUMP_ROOT"

if [ ! -s "$CHECKSUMS" ]; then
  echo "verify: nothing ingested yet"
  exit 0
fi

if command -v sha256sum >/dev/null 2>&1; then
  sha256sum -c -- "$CHECKSUMS"
else
  shasum -a 256 -c -- "$CHECKSUMS"
fi
VERIFY

chmod +x "$DUMP_ROOT/bin/ingest.sh" "$DUMP_ROOT/bin/verify.sh"

# ---------------------------------------------------------------- git (opt-in)
if [ "$DO_GIT" -eq 1 ]; then
  if [ -d "$DUMP_ROOT/.git" ]; then
    echo "init-datadump: git repo already present, leaving it alone"
  elif command -v git >/dev/null 2>&1; then
    git -C "$DUMP_ROOT" init -q
    echo "init-datadump: initialized git repo in $DUMP_ROOT"
  else
    echo "init-datadump: git not found, skipping --git" >&2
  fi
fi

echo "$NOW init version=$DATADUMP_VERSION force=$FORCE git=$DO_GIT" >> "$DUMP_ROOT/logs/init.log"

if [ "$ALREADY_INIT" -eq 1 ] && [ "$FORCE" -eq 0 ]; then
  echo "init-datadump: refreshed existing dump at $DUMP_ROOT (data untouched)"
else
  echo "init-datadump: initialized dump at $DUMP_ROOT"
fi

echo
echo "  ingest:  $DUMP_ROOT/bin/ingest.sh --source <name> [files...]"
echo "  verify:  $DUMP_ROOT/bin/verify.sh"
