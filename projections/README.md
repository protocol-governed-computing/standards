# Projections

Derivations of the standard in `spec/`. A projection is a representation of the family, never a
member of it (`0z` §5.2, `4b`).

**Nothing here is a document of the family.** These files declare no part, state no requirement, and
carry no file identifier. None appears in `0z` §2.

**None of them carries authority.** Where a projection and the documents disagree, **the documents
govern** (PJ-7, PJ-11). A projection is not a second statement of the family.

## What is here

| Projection | Contract | State |
|---|---|---|
| `terminology_index.md`, `vocabulary_violations.md` | `terminology_projection_contract.md` | generated |
| `requirement_index.md` | `requirement_projection_contract.md` | generated |

Two files are neither projection nor contract. They are readings of what the terminology projection
found — written, not derived:

- `vocabulary_triage.md` — what the first harvest reported, and what was done about it.
- `vocabulary_locality.md` — evidence on the 33 terms used only in their defining document, bearing
  on a question the family does not answer: when a word must become a term.

## Regenerating

Both projections are produced by `tools/` and are regenerated rather than edited. Hand edits are
discarded on the next run.

```
python tools/vocab_index.py                  # terminology
python tools/vocab_index.py --check

python tools/requirement_index.py            # requirements
python tools/requirement_index.py --check
python tools/check_requirement_count.py      # the count guard, run separately
```

**The count guard is a separate script on purpose.** It shares no code with the extractor and counts
against `0z` §2 rather than re-reading the documents. A guard that fails the same way as the thing it
guards is not a guard — which is how the previous requirement harvest reported two documents as
empty and passed every check it had.

**A projection names the revision it derives from** (`7a` CF-1). Each contract carries the figures
for the revision it was last harvested against.
