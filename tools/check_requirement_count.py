"""The requirement projection's count guard, per its contract's Verification section.

**This file deliberately shares no code with `requirement_index.py`.** The first
requirement projection derived its guard the same way it derived the index, so a
convention the extractor stopped recognizing produced a smaller count that every
other check accepted. A guard that fails the same way as the thing it guards is
not a guard.

It counts by a different route and against a different artifact: `0z` §2 declares
each document's invariant range, and the sum of those ranges is what the family
says it carries. The index is what the documents actually yield. They must agree.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RANGE = re.compile(r"^\|\s*`(\w+)`\s*\|[^|]*\|[^|]*\|\s*([A-Z]{2})-(\d+)\s*…\s*[A-Z]{2}-(\d+)\s*\|")


def declared() -> dict[str, tuple[str, int]]:
    """What 0z Sec 2 says each document carries: its prefix, and its range span."""
    text = (ROOT / "spec" / "0z_open_pgc_standard_document_set.md").read_text(encoding="utf-8")
    out = {}
    for line in text.splitlines():
        m = RANGE.match(line)
        if m:
            stem, prefix, lo, hi = m.groups()
            out[stem] = (prefix, int(hi) - int(lo) + 1)
    return out


def suffixed(prefixes: dict[str, str]) -> dict[str, list[str]]:
    """Identifiers a range cannot express: SM-7a sits inside SM-1 … SM-12.

    Counted straight out of `spec/` with no form parsing, so a change to how an
    invariant is laid out cannot hide one. Restricted to identifiers the document
    owns — 0z names each document's prefix, and a document citing another's
    suffixed invariant does not thereby carry it.
    """
    out: dict[str, list[str]] = {}
    for path in sorted((ROOT / "spec").glob("*.md")):
        stem = path.stem.split("_")[0]
        prefix = prefixes.get(stem)
        if not prefix:
            continue
        found = sorted(set(re.findall(r"\b(%s-\d+[a-z])\b" % prefix,
                                      path.read_text(encoding="utf-8"))))
        if found:
            out[stem] = found
    return out


def indexed() -> dict[str, int]:
    """What the published index carries, read as text rather than re-derived."""
    path = ROOT / "projections" / "requirement_index.md"
    if not path.exists():
        print(f"no index at {path} — run tools/requirement_index.py first", file=sys.stderr)
        raise SystemExit(2)
    out, doc = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## (\w+) — ", line)
        if m:
            doc = m.group(1)
            out[doc] = 0
        elif doc and re.match(r"^- \*\*[A-Z]{2}-\d+[a-z]?\*\*", line):
            out[doc] += 1
    return out


def main() -> int:
    d = declared()
    i, sfx = indexed(), suffixed({k: v[0] for k, v in d.items()})
    problems = []

    for stem in sorted(set(d) | set(i)):
        want = d[stem][1] + len(sfx.get(stem, [])) if stem in d else None
        got = i.get(stem)
        if want is None:
            problems.append(f"{stem}: indexed {got}, and 0z §2 states no range")
        elif got is None:
            problems.append(f"{stem}: 0z §2 states {want}, and the index carries none")
        elif want != got:
            problems.append(f"{stem}: 0z §2 plus suffixes gives {want}, index carries {got}")

    extra = sum(len(v) for v in sfx.values())
    spans = sum(v[1] for v in d.values())
    print(f"0z §2 declares {spans} across {len(d)} documents")
    print(f"suffixed identifiers a range cannot express: {extra}")
    for stem in sorted(k for k in sfx if k in d):
        print(f"  {stem}: {', '.join(sfx[stem])}")
    print(f"expected {spans + extra} · index carries {sum(i.values())} "
          f"across {len(i)} documents")

    if not problems:
        print("agreed — every mapped range, plus its suffixed identifiers, matches the index")
        return 0
    print(f"\n{len(problems)} disagreement(s):")
    for p in problems:
        print(f"  {p}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
