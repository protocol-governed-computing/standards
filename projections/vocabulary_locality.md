# Evidence — single-document terms

Bearing on a question the family does not answer: **when must a word become a term?**

CM-3 requires a document that introduces a term to define it. CM-8 requires the term to sit with
the document whose subject matter principally establishes it. Neither says when a word must be
introduced at all, so nothing distinguishes a term the family needs from a word an author chose to
bold. This is the evidence available for deciding whether that rule is worth stating. It is
recorded as Finding **E** against `v0`.

**It is evidence, not a proposal.** No rule is drafted here, and the reading below argues that the
obvious rule would be wrong.

---

## The population

Of 167 PGC terms, **31 appear in no document but the one that defines them.** They are not evenly
distributed:

| Document | Terms it owns | Used only there |
|---|---|---|
| `5a` Governed Interaction Boundary | 11 | 5 |
| `2c` Machine Block | 8 | 5 |
| `4d` Governed Transformation | 11 | 4 |
| `1a` Conceptual Model | 52 | 2 |
| `6a`, `4b`, `2e`, `7b` | 4–5 each | 2 each |
| `6c` | 1 | 1 |
| `2a`, `2d`, `2f`, `3e`, `4e`, `5b`, `6b` | 3–6 each | 1 each |

## The obvious rule would be wrong

The rule that suggests itself — *a term used by only one document is not family vocabulary* — fails
against the evidence. **Fifteen of the 31 carry a requirement in their own document's invariants:**

| Term | Document | Uses | Invariants citing it |
|---|---|---|---|
| inheritance | 2e | 16 | 2 |
| gate | 4d | 9 | 2 |
| delegation | 2e | 8 | 1 |
| worker | 4d | 8 | 1 |
| parameterization | 6a | 8 | 1 |
| query | 5b | 7 | 2 |
| universal envelope | 2c | 7 | 1 |
| dossier, rung | 4d | 7 | 1 each |
| projection contract | 4b | 6 | 1 |
| referential closure | 4e | 6 | 1 |
| negative demonstration | 7b | 6 | 1 |
| determinative content | 3e | 4 | 2 |
| vocabulary revision | 2d | 4 | 1 |
| semantic owner | 2c | 3 | 1 |

A term stating one of its document's obligations is load-bearing whether or not any other document
needs it. CA-8 is *"Inheritance MUST be declared; containment MUST NOT carry governance of
itself"* —
`2e` cannot state it without the term, and no other document has occasion to use it.
**Locality is not the defect.**

## A limitation of this measurement, found later

**An occurrence count over the full term cannot distinguish disuse from abbreviation.** Six terms
below are recorded as used nowhere after being defined. Five of them are used throughout their own
document under a shortened name — `projection source` appears as *source* fifty-nine times,
`protocol adapter` as *adapter* eighteen. Only `1a`'s `Promotion` is genuinely unused.

Read as disuse, this section would have struck five live concepts. What it actually surfaces is
**name drift**: a term declared in full and used in short. Corrected when the finding was
dispositioned; the counts below are left as measured.

## The signal that does hold

A sharper line separates the same population: **whether the term is used at all after being
defined.**

Six terms are declared, defined, and then used nowhere — the two occurrences are the declaration
sentence and the definition itself:

| Term | Document |
|---|---|
| Promotion | 1a |
| construction disposition | 2c |
| projection source | 4b |
| protocol adapter | 5a |
| profile derivation | 6a |
| demonstration coverage | 7b |

These carry no requirement, appear in no invariant, and nothing in the family reads differently if
they are struck. That is a defect of a different kind from locality, and it is mechanically
detectable, which locality's legitimate cases are not.

**Two more were produced by `v0` Change 1 and then struck.** `6c`'s `platform-owned
governance` and `domain-owned governance` were reported by the first harvest as declared and
unused; the triage judged that §3 is the ownership boundary those terms name and defined them
rather than striking them. They were then declared, defined, and still unused. Change 1 strikes
them as the triage first proposed, and `6c` §3 stands as it did in `draft-3` — its table draws the
distinction without naming it.

The lesson is the one worth carrying: **writing a definition is the tempting remedy for an unused
declaration, and it is the wrong one.** A definition does not create a use.

## The sharpest case is `1a`

Part I exists to supply the vocabulary every other document uses. **Two of its 52 terms are used in
no other document**: `Promotion` (2 uses, no invariant) and `Software governance` (3 uses, no
invariant).

A Part I term nothing outside Part I uses is either a concept the family needs and has not taken
up, or a concept that does not belong in Part I under CM-8. Which one is a determination about each
term, not a fact the projection can supply.

## Bearing on carried-forward Finding D

`draft-3` carried forward, unclosed, that `4d` "remains the document with the most vocabulary of its
own and the largest invariant set", and that a clause-by-clause re-review against `8a` §4.7 would
settle it. This is the first measurement of that claim: `4d` owns 11 terms and 4 are local to it —
`dossier`, `gate`, `rung`, `worker`. All four are load-bearing by the test above, each appearing in
at least one `4d` invariant.

**That narrows Finding D rather than closing it.** `4d`'s vocabulary is not idle, so the concern
cannot be that it invented terms nothing uses. If the concern survives, it is that `4d`'s subject
requires that much vocabulary at all — which is the `8a` §4.7 re-review, and is still not done.

`5a` and `2c` each carry 5 local terms and were never the subject of a finding. Whatever is decided
about `4d` should be decided about them on the same basis.

## What this evidence does not establish

- **That any of the 31 should be struck.** Fifteen are load-bearing, and the other sixteen require
  a reading of what their document needs.
- **That a rule is worth stating.** Six unused terms out of 167 may not justify an invariant, and
  CM-9 would need to be discharged by a document, which means every document would have to
  demonstrate that each term it introduces is used.
- **That "used in an invariant" is the right test.** It is the test that separates this population
  cleanly. Whether it is the correct criterion is a judgment the projection cannot make, and a term
  can be essential to a document's prose while appearing in none of its invariants — `governed
  result` in `5a` is used ten times and cited by no invariant.
