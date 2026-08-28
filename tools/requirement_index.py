"""Derive the PGC normative requirement index from spec/.

Writes into projections/, governed by projections/requirement_projection_contract.md.

The family states an invariant in two forms, and a derivation that knows only one
reports a whole document as carrying none:

  bullet    - **GS-1.** The governing relation MUST be declared ... (Sec 3.1)
  heading   ### AI-1 — Behavior originates in declaration
            followed by the requirement's prose

The contract's guard is a count taken independently of this extractor. It is in
check_requirement_count.py, which shares no code with this file on purpose: the
first requirement projection derived its own guard the same way it derived the
index, so a convention it stopped recognizing went unreported.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

FENCE = re.compile(r"^\s*(```|~~~)")
SECTION = re.compile(r"^##\s+(\d+(?:\.\d+)*)\.?\s+(.*)$")
TITLE = re.compile(r"^#\s+(.*)$")

# An identifier is two capitals, a number, and an optional letter suffix: GS-1, SM-7a.
IDENT = r"[A-Z]{2}-\d+[a-z]?"
BULLET = re.compile(r"^-\s+\*\*(%s)\.\*\*\s*(.*)$" % IDENT)
HEADING = re.compile(r"^###\s+(%s)\s+[—-]\s*(.*)$" % IDENT)
XREF = re.compile(r"(%s)" % IDENT)
SECREF = re.compile(r"§+\s*\d+(?:\.\d+)*")

# Part 0 and the non-normative annex carry no invariants and are not harvested.
EXCLUDED = {"0a", "0b", "0c", "0d", "0z", "8a"}


@dataclass
class Requirement:
    ident: str
    doc: str
    section: str
    line: int
    form: str                       # "bullet" or "heading"
    text: str
    xrefs: list[str] = field(default_factory=list)
    secrefs: list[str] = field(default_factory=list)


def harvest(spec_dir: Path) -> tuple[list[Requirement], dict[str, str]]:
    reqs: list[Requirement] = []
    titles: dict[str, str] = {}

    for path in sorted(spec_dir.glob("*.md")):
        stem = path.stem.split("_")[0]
        lines = path.read_text(encoding="utf-8").splitlines()
        titles[stem] = next((m.group(1).strip() for m in (TITLE.match(l) for l in lines[:5]) if m), stem)
        if stem in EXCLUDED:
            continue

        section, in_fence, pending = "", False, None
        for i, line in enumerate(lines, start=1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue

            m = SECTION.match(line)
            if m:
                section = f"§{m.group(1)}"

            # A heading-form invariant states its requirement in the prose that
            # follows, so the identifier is recorded and the text collected after.
            m = HEADING.match(line)
            if m:
                pending = Requirement(m.group(1), stem, section, i, "heading", m.group(2).strip())
                reqs.append(pending)
                continue

            m = BULLET.match(line)
            if m:
                pending = Requirement(m.group(1), stem, section, i, "bullet", m.group(2).strip())
                reqs.append(pending)
                continue

            if pending is None:
                continue
            if not line.strip():
                # One blank line ends a bullet; a heading's prose may span several.
                if pending.form == "bullet":
                    pending = None
                continue
            if line.startswith(("#", "- ", "| ")) or line.startswith("*Derives from"):
                pending = None
                continue
            if pending.form == "bullet" and not line.startswith("  "):
                pending = None
                continue
            pending.text += " " + line.strip()

    for r in reqs:
        body = f"{r.text}"
        r.xrefs = sorted({x for x in XREF.findall(body) if x != r.ident})
        r.secrefs = sorted(set(SECREF.findall(body)))
    return reqs, titles


def verify(reqs: list[Requirement], spec_dir: Path) -> list[str]:
    """The contract's checks, minus the count, which is guarded separately."""
    out = []

    seen = defaultdict(list)
    for r in reqs:
        seen[r.ident].append(f"{r.doc} line {r.line}")
    for ident, where in sorted(seen.items()):
        if len(where) > 1:
            out.append(f"duplicate identifier {ident}: {', '.join(where)}")

    for r in reqs:
        if not r.section:
            out.append(f"{r.ident} ({r.doc} line {r.line}) carries no section")
        if not r.text.strip():
            out.append(f"{r.ident} ({r.doc} line {r.line}) carries no requirement text")

    known = {r.ident for r in reqs}
    for r in reqs:
        for x in r.xrefs:
            if x not in known:
                out.append(f"{r.ident} ({r.doc}) references {x}, which resolves to no requirement")

    # 0z Sec 2 is authoritative on which documents carry invariants.
    mapped = set()
    zdoc = (spec_dir / "0z_open_pgc_standard_document_set.md").read_text(encoding="utf-8")
    for row in re.findall(r"^\|\s*`(\w+)`\s*\|[^|]*\|[^|]*\|\s*([^|]+?)\s*\|", zdoc, re.M):
        stem, invariants = row
        if invariants.strip() != "—":
            mapped.add(stem)
    harvested = {r.doc for r in reqs}
    for stem in sorted(mapped - harvested):
        out.append(f"{stem} is mapped in 0z §2 as carrying invariants and none was harvested")
    for stem in sorted(harvested - mapped):
        out.append(f"{stem} yielded invariants and 0z §2 maps it as carrying none")
    return out


def render(reqs: list[Requirement], titles: dict[str, str]) -> str:
    by_doc = defaultdict(list)
    for r in reqs:
        by_doc[r.doc].append(r)
    forms = defaultdict(int)
    for r in reqs:
        forms[r.form] += 1

    lines = [
        "# PGC Normative Requirement Index",
        "",
        "Derived from the documents of the family by `tools/requirement_index.py`, governed by",
        "`requirement_projection_contract.md`. It is an index of requirement identities, not a",
        "statement of the obligations themselves: it carries each requirement's text and the",
        "references that text states, and never the sections those references reach.",
        "",
        "**Authority.** None. Where this projection and the documents disagree, the documents govern",
        "(`0z` §5.2, PJ-7).",
        "",
        f"{len(reqs)} requirements · {len(by_doc)} documents · "
        f"{forms['bullet']} bullet · {forms['heading']} heading",
        "",
    ]
    for doc in sorted(by_doc):
        lines += [f"## {doc} — {titles.get(doc, doc)}", ""]
        for r in sorted(by_doc[doc], key=lambda r: r.line):
            refs = []
            if r.xrefs:
                refs.append("requirements: " + ", ".join(r.xrefs))
            if r.secrefs:
                refs.append("sections: " + ", ".join(r.secrefs))
            suffix = f" — *{'; '.join(refs)}*" if refs else ""
            lines.append(f"- **{r.ident}** ({r.section}) {r.text}{suffix}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", type=Path, default=root / "spec")
    ap.add_argument("--out", type=Path, default=root / "projections")
    ap.add_argument("--check", action="store_true", help="exit non-zero if any check fails")
    args = ap.parse_args()

    reqs, titles = harvest(args.spec)
    if not reqs:
        print(f"no requirements found in {args.spec}", file=sys.stderr)
        return 2
    problems = verify(reqs, args.spec)

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "requirement_index.md").write_text(render(reqs, titles), encoding="utf-8")

    docs = len({r.doc for r in reqs})
    print(f"{len(reqs)} requirements, {docs} documents")
    print(f"wrote {args.out / 'requirement_index.md'}")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  {p}")
    else:
        print("all contract checks passed (count guard runs separately)")
    return 1 if (args.check and problems) else 0


if __name__ == "__main__":
    raise SystemExit(main())
