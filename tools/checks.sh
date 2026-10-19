#!/usr/bin/env bash
#
# Every guard in this folder, in one run.
#
# The guards check different things by deliberately different routes, and running them
# together is how their disagreement becomes visible. `check_requirement_count` derives the
# family's invariant count from the ranges `0z` §2 declares; `check_realization_coverage`
# parses the declaration sites in the documents themselves. Neither is authoritative over the
# other. When they disagree, one of them is reading the family wrongly, and which one is the
# question to answer before trusting either number.
#
# Each guard exits non-zero on its own failure. This runs all of them before reporting, so a
# single run shows every failure rather than the first.

set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="${PYTHON:-python3}"
failed=0

run() {
  local name="$1"; shift
  echo "── $name"
  if "$PYTHON" "$HERE/$name" "$@"; then
    echo
  else
    echo "   FAILED ($name)"; echo
    failed=1
  fi
}

run check_requirement_count.py
run check_realization_coverage.py --quiet

if [ "$failed" -ne 0 ]; then
  echo "one or more guards failed"
  exit 1
fi
echo "all guards passed"
