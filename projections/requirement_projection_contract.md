# Projection contract — the normative requirement index

The contract `4b` PJ-3 requires for the machine-readable projection of this family, declared under
`0z` §5.2.

**This document is not a document of the family.** It declares no part and states no requirement. It
sits in `projections/` with the other derivations of this family, outside the family it derives
from.

---

## Source

`spec/` at a named revision. **The revision is part of the source identity**: a projection of
`draft-2` is not a projection of `draft-3`, and one carrying no revision identifies nothing (`7a`
CF-1).

## Selection — what it carries

- every **normative requirement** in `spec/`, being a line matching the family's invariant form:
  an identifier of the shape `XX-n` or `XX-na`, its requirement text, and its parenthesised
  references;
- for each, its **source document** and the **section it appears in**;
- the **cross-references** the requirement states.

## Selection — what it does not carry

Declared explicitly, because `4b` §3.1 exists so that an absent element is never ambiguous between
deliberately excluded and lost:

- **the sections a requirement cites.** Many requirements are one sentence over a section that
  supplies the substance — `2a` GS-9's ground is §8's prose, `4d` TR-3a's test is §5.1, `3e` EV-1's
  five points are §3.1. **The projection carries the reference, never the referenced text.**
- **rationale, derivation and worked reasoning**, which is the majority of each document's value and
  the reason the prose is the source rather than a rendering of the index;
- **the does-not-specify lists**, the conformance sections, and all narrative;
- **the non-normative annex** and Part 0.

**Consequence, stated so no consumer has to infer it:** *this projection is an index of requirement
identities, not a statement of the obligations themselves.* A consumer that treats a carried
requirement line as the whole obligation has made a claim the source does not entail — which is the
consumer's defect, not the projection's, because this contract says otherwise.

## Derivation

Mechanical extraction from the Markdown source. Deterministic, consulting nothing but `spec/`
(PJ-2), and regenerable from it alone (PJ-9).

The derivation depends on two conventions of the source, and **states that dependence rather than
assuming it**:

- a requirement appears in **one of two forms**, and a derivation that knows only one reports a
  whole document as carrying none:
  - **bullet** — a list item opening with a bolded identifier and a full stop, `- **GS-1.** …`;
  - **heading** — a third-level heading carrying the identifier, `### AI-1 — …`, with the
    requirement stated in the prose that follows. `1c` uses this form and no other;
- a section heading carries a number, with or without a trailing full stop;
- an identifier may carry a letter suffix — `SM-7a` — which a stated range cannot express.

**A change to either convention changes what this projection carries, silently.** That is the
characteristic failure of a derived index, and the guard is below.

## Verification

The contract is checkable, and a projection that cannot be checked against its contract is the
defect `4b` §3.1 describes:

| Check | Property |
|---|---|
| every extracted identifier is unique across the family | no two requirements collide |
| every extracted requirement carries a source document and a section | nothing is orphaned |
| every stated cross-reference resolves in its own document | PJ-4, no unentailed claim |
| re-derivation from an unchanged `spec/` yields an identical projection | PJ-2, PJ-9 |
| the count matches `0z` §2's declared ranges plus suffixed identifiers, checked by a script sharing no code with the extractor | **the guard against silent convention drift** |

**The last check is the load-bearing one.** An extractor that silently stops matching a requirement
form reports fewer requirements and passes every other check. Counting the source by a second,
independent means is what makes that visible.

## Status against `v0`

Harvested, verified, and published as `requirement_index.md`:

```
356 requirements · 26 documents · 356 unique identifiers
339 bullet form · 17 heading form
356/356 carry a source document and a section
0 unresolved cross-references
0z §2 declares 350 across 26 documents, plus 6 suffixed identifiers = 356 · agreed
```

**The previous harvest reported 317 across 24 documents, and was wrong by two whole documents.**
It knew only the bullet form, so `1c` — which states AI-1 … AI-17 as headings and uses no bullets —
read as carrying nothing. `1a` was the second, and it carried nothing to find until Change 1 gave it
CM-1 … CM-8.

**The count check did not catch it, and that is the more important failure.** The independent count
was derived the same way as the extractor, so a convention the extractor did not recognize was
equally invisible to its guard. `tools/check_requirement_count.py` now counts against a **different
artifact** — `0z` §2's declared ranges — and shares no code with the extractor. It fired twice
before it agreed: once because a range cannot express a suffixed identifier, and once because a
document citing another's suffixed invariant does not thereby carry it.

**A projection names the revision it derives from.** This count is `v0`'s. A projection of
`draft-3` is not a projection of `v0`, which is why the revision is part of the source
identity above.

**Authority.** None. `0z` §5.2 and PJ-7: where this projection and the documents disagree, **the
documents govern.**
