#!/usr/bin/env python3
"""Check the realization map against the standard: is every invariant accounted for?

The map itself cannot be generated. Its content is judgement — "sealing is detected, not
enforced" is a person reading an implementation against an invariant, and a tool producing
plausible text for that would read complete while being nothing of the kind.

Its *coverage* is mechanical, and that is what this reports. Three questions the map cannot
answer about itself:

  absent   an invariant the standard declares and the map has no entry for
  stale    an entry naming an identifier the standard no longer declares
  orphan   a realization invariant artifact the map never mentions

The first two are drift: a revision adds or retires an invariant, and a hand-maintained map
falls behind silently. The third is the inverse gap the map's own §0.1 records as "24
invariants added" — realization invariants with no counterpart in the documents.

This establishes that an invariant was addressed. It never establishes that the entry is
sound, and it cannot: soundness is the reading, which is the part that is not mechanical.

    python3 tools/check_realization_coverage.py [--snapshot DIR] [--quiet]

Exits 0 when nothing is absent or stale, 1 otherwise. Orphans are reported and do not fail
the run: a realization may carry invariants of its own, and the map is a map of the standard.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The standard declares an invariant in one of two forms, and reading only the first was a
# real defect in this tool: it reported the whole AI family as absent from the standard and
# every map entry naming one as stale, which inverted the finding — the map was right and
# the checker was wrong.
#
#   a bullet in a "Normative invariants" section
#     - **SN-1.** A snapshot MUST be immutable from the moment of sealing.
#   a section heading, which is how the Architectural Invariants are declared
#     ### AI-1 — Behavior originates in declaration
DECLARED_BULLET = re.compile(r"^- \*\*([A-Z]{2}-\d+[a-z]?)\.\*\*", re.M)
DECLARED_HEADING = re.compile(r"^#{2,4}\s+([A-Z]{2}-\d+[a-z]?)\s+[—-]", re.M)

# The map carries one table row per invariant, the class in its final cell. Tables in the
# map differ in width, so the class is taken from the end of the row rather than from a
# fixed column — counting columns reads prose as a class wherever a table has an extra one.
ENTRY_ROW = re.compile(r"^\|\s*\*\*([A-Z]{2}-\d+[a-z]?)\*\*.*\|\s*$", re.M)

# §2: "Partial, Unimplemented and Vacuous entries are findings." Violated, Unimplementable
# and Over-specified are findings too — the first against the realization, the last two
# against the document.
FINDING_CLASSES = {"Partial", "Unimplemented", "Unimplementable",
                   "Over-specified", "Vacuous", "Violated", "Mutated"}
KNOWN_CLASSES = FINDING_CLASSES | {"Demonstrated"}


# The map declares which families it does not cover, and why. Read from the document rather
# than listed here: which invariants a realization can bear is a judgement about the standard,
# and a tool holding its own copy of that judgement is a second place for it to be wrong.
OUT_OF_SCOPE_ROW = re.compile(r"^\|\s*\*\*([A-Z]{2})\*\*\s*\|", re.M)


def out_of_scope(map_path: Path) -> set[str]:
    """Families the map declares it does not cover."""
    text = map_path.read_text(encoding="utf-8")
    m = re.search(r"^### 1\.1 Families out of scope\n(.*?)^## ", text, re.S | re.M)
    return set(OUT_OF_SCOPE_ROW.findall(m.group(1))) if m else set()


def declared_invariants(spec_dir: Path) -> dict[str, str]:
    """Every invariant the standard declares, mapped to the document declaring it."""
    found: dict[str, str] = {}
    for path in sorted(spec_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for pattern in (DECLARED_BULLET, DECLARED_HEADING):
            for ident in pattern.findall(text):
                found.setdefault(ident, path.name)
    return found


def map_entries(map_path: Path) -> dict[str, str]:
    """Every invariant the map carries an entry for, mapped to its declared class.

    Keyed on the identifier rather than appended to a list: an invariant with two entries is
    a defect this does not detect, and detecting it would mean deciding which entry governs.
    """
    entries: dict[str, str] = {}
    for line in map_path.read_text(encoding="utf-8").splitlines():
        m = ENTRY_ROW.match(line)
        if not m:
            continue
        # The map's tables do not agree on where the class sits: some carry it last, after
        # "where demonstrated"; others carry it second, before a note. Reading a fixed column
        # returns a note as a class for every table of the other shape, which is how 22 entries
        # came to report as unclassified. Scan the cells and take the first that names a class.
        cells = [c.strip() for c in line.strip().strip("|").split("|")][1:]
        cls = ""
        for cell in cells:
            head = cell.split("—")[0].split("--")[0].strip().strip("*`‡ ").split(",")[0].strip()
            if head in KNOWN_CLASSES:
                cls = head
                break
        # Not every table in the map carries a class column; some rows are identifier and
        # note alone. Such a row is an entry without a class, which is a different fact from
        # an entry whose class happens to be long — echoing its prose as a class would make
        # the class tally unreadable and would imply a vocabulary the map does not have.
        entries[m.group(1)] = cls if cls in KNOWN_CLASSES else "no class stated"
    return entries


def snapshot_invariants(snapshot: Path) -> list[str]:
    """Identities of every INVARIANT artifact the snapshot carries."""
    out: list[str] = []
    for path in (snapshot / "canonical").rglob("*.json"):
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        if not isinstance(record, dict):
            continue
        kind = (record.get("frontmatter") or {}).get("artifact_kind") or record.get("artifact_type")
        if kind == "INVARIANT":
            identity = record.get("fqdn") or record.get("fqdn_id")
            if identity:
                out.append(identity)
    return sorted(set(out))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--map", type=Path, default=ROOT / "doc" / "realization_map.md")
    ap.add_argument("--spec", type=Path, default=ROOT / "spec")
    ap.add_argument("--snapshot", type=Path, help="an assembled snapshot, to report orphans")
    ap.add_argument("--quiet", action="store_true", help="counts only; omit the identifiers")
    args = ap.parse_args()

    for path in (args.map, args.spec):
        if not path.exists():
            print(f"not found: {path}", file=sys.stderr)
            return 2

    declared = declared_invariants(args.spec)
    entries = map_entries(args.map)

    excluded_families = out_of_scope(args.map)
    excluded = sorted(i for i in declared if i.split("-")[0] in excluded_families)
    absent = sorted(i for i in set(declared) - set(entries)
                    if i.split("-")[0] not in excluded_families)
    stale = sorted(set(entries) - set(declared))

    print(f"map     : {args.map.relative_to(ROOT)}")
    print(f"declared: {len(declared)} invariants across {len(set(declared.values()))} documents")
    print(f"entries : {len(entries)}\n")

    # Coverage by family, because a family entirely unmapped is a different fact from a
    # scattering of gaps — it says a whole part of the standard was never read against this
    # realization, which is not visible in a single percentage.
    fam_declared = Counter(i.split("-")[0] for i in declared)
    fam_absent = Counter(i.split("-")[0] for i in absent)
    incomplete = sorted(f for f in fam_declared
                        if fam_absent[f] and f not in excluded_families)
    if incomplete:
        print("  coverage by family, where incomplete")
        for f in incomplete:
            have = fam_declared[f] - fam_absent[f]
            flag = "  <- none mapped" if have == 0 else ""
            print(f"    {f:<4} {have:>3}/{fam_declared[f]:<3}{flag}")
        print()

    classes = Counter(entries.values())
    findings = sum(n for c, n in classes.items() if c in FINDING_CLASSES)
    print("  entries by class")
    for cls, n in sorted(classes.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"    {cls:<16} {n:>3}{'   (finding)' if cls in FINDING_CLASSES else ''}")
    print(f"\n  findings: {findings} of {len(entries)} entries")
    print("  A finding is resolved by ruling, never by editing a normative document to match")
    print("  what was built.\n")

    if excluded:
        fams = ", ".join(sorted(excluded_families))
        print(f"  OUT OF SCOPE — declared by §1.1, binds documents rather than a realization: "
              f"{len(excluded)} ({fams})\n")
    if absent:
        print(f"  ABSENT — declared by the standard, no entry in the map: {len(absent)}")
        if not args.quiet:
            for ident in absent:
                print(f"    {ident:<8} {declared[ident]}")
        print()
    if stale:
        print(f"  STALE — entry names an identifier the standard no longer declares: {len(stale)}")
        if not args.quiet:
            for ident in stale:
                print(f"    {ident:<8} class={entries[ident]}")
        print()

    if args.snapshot:
        text = args.map.read_text(encoding="utf-8")
        carried = snapshot_invariants(args.snapshot)
        orphans = [i for i in carried if i.split("::")[-1] not in text]
        print(f"  snapshot: {args.snapshot}")
        print(f"  carries {len(carried)} INVARIANT artifacts; {len(orphans)} named nowhere in the map")
        if orphans and not args.quiet:
            for ident in orphans[:20]:
                print(f"    {ident}")
            if len(orphans) > 20:
                print(f"    … and {len(orphans) - 20} more")
        print("  Orphans do not fail this check. A realization may carry invariants of its own,")
        print("  and this map is a map of the standard.\n")

    if absent or stale:
        print(f"NOT COVERED — {len(absent)} absent, {len(stale)} stale")
        return 1
    print("COVERED — every declared invariant has an entry, and every entry names a declared invariant")
    return 0


if __name__ == "__main__":
    sys.exit(main())
