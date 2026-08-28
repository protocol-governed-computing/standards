# Open Protocol-Governed Computing Standard

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22150615.svg)](https://doi.org/10.5281/zenodo.22150615)

A specification for computing in which the construction and execution of software are governed by
explicit, versioned, machine-consumable declarations rather than by convention, documentation, or
code inspection.

**Start with [`spec/0z_open_pgc_standard_document_set.md`](spec/0z_open_pgc_standard_document_set.md)** —
the map of the family: what it contains, how its documents relate, and where to begin.

## Structure

```
spec/0a-0c   Part 0    why this exists                      non-normative
spec/0z      Part 0    document set map
spec/1a-1c   Part I    Model
spec/2a-2f   Part II   Governance
spec/3a-3e   Part III  Execution
spec/4a-4e   Part IV   Construction & Transformation
spec/5a-5b   Part V    Interchange
spec/6a-6c   Part VI   Profiles
spec/7a-7b   Part VII  Conformance
spec/8a      Annex     Implementation Guidance              non-normative
```

Parts I–VII are normative. A file identifier is an address, not an identity: documents refer to one
another by name, and an invariant identifier carries its document's prefix — `MB-`, `CA-`, `SM-` —
never a file identifier.

## Status

**`draft-3`** — the current revision, carried in `VERSION`. Its supersession of `draft-2`, and every
change it makes, are declared in `revisions.md`; a revision that appears in `VERSION` and not
there has not been declared.

A conformance claim is always a claim by a named subject, against a named profile and a named
revision. There is no unqualified conformance claim.

## Review

**This specification is seeking critical review, not adoption.** What is claimed, what would falsify
it, what has not yet been established, and the one thing this project cannot supply for itself are
stated in [doc/call_for_review.md](doc/call_for_review.md).

Eighteen of `draft-3`'s twenty-eight declared changes came from readers who did not build the
reference realization. A finding that survives review becomes a declared change against a named
predecessor; a finding declined is recorded with the reason.

## Relationship to implementations

This repository contains the standard and nothing else. A reference realization exists separately;
it demonstrates that these documents are satisfiable, and establishes nothing about what conformance
requires. Where a document and a realization disagree, the document governs.

## Licence

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
