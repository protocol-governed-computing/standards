# Projection contract — the terminology index

The contract `4b` PJ-3 requires for the terminology projection of this family, declared under
`0z` §5.2. It governs `terminology_index.md` and `vocabulary_violations.md`.

**This document is not a document of the family.** It declares no part, states no requirement, and
carries no file identifier.

---

## Source

`spec/` at a named revision. **The revision is part of the source identity**: a terminology index of
`draft-3` is not one of `v0`, and one carrying no revision identifies nothing (`7a` CF-1).

## Selection — what it carries

- every **PGC term**, being a term a document declares it introduces, or that `1a` defines. A
  term is a PGC term because a document declares it (`1a` §2) — never because a word is bolded,
  capitalized, or load-bearing. Outside `1a` an undeclared paragraph-leading bold is as often an
  emphasised sentence (`7b` §3, "**CD-4 applies unchanged.**") as a definition, and is not carried;
- for each, the **document that defines it**, the section, and the line;
- the **form** the definition site takes, where it is not the paragraph-leading form;
- the **distinctions** `1a` draws as *distinguish from*;
- the **refinements** a later document declares over a term Part I defines;
- the **occurrences** of the term in every other document, by document and line.

## Selection — what it does not carry

Declared explicitly, because `4b` §3.1 exists so that an absent element is never ambiguous between
deliberately excluded and lost:

- **the meaning of any term.** The index states where a term is defined, never what it means. This
  is the whole of the distinction between an index and a glossary: a glossary would be a second
  statement of the vocabulary, and the family would then have two.
- **any judgment of a definition's quality.** The index locates a definition; it does not grade the
  sentence. A term sited in a section named for it is carried as defined, whatever its prose does.
- **terms of ordinary English**, however load-bearing, that no document declares or defines.
- **the prose that gives a term its force** — the exclusions, the *distinguish from* reasoning, the
  worked consequences — which is the majority of each definition's value and the reason the prose is
  the source rather than a rendering of the index.

**Consequence, stated so no consumer has to infer it:** *this projection is an index of where terms
are defined, not a statement of what they mean.* A consumer that reads a carried entry as the
definition has made a claim the source does not entail — which is the consumer's defect, not the
projection's, because this contract says otherwise.

## Derivation

Mechanical extraction from the Markdown source. Deterministic, consulting nothing but `spec/`
(PJ-2), and regenerable from it alone (PJ-9).

The derivation depends on conventions of the source, and **states that dependence rather than
assuming it**:

- a document declares its terms in a sentence of the form *"This document introduces the terms
  `**x**`, `**y**`, and `**z**`"*;
- a definition is sited in one of five forms — a paragraph opening `**Term.**`; a copula sentence
  (*"A `**binding**` associates…"*); a numbered section named for the term; a table row; or the term
  bolded at first substantive use;
- a bold mark does not straddle a line break;
- a section heading carries a number;
- a document that refines an inherited concept says so, naming the term (CM-2).

**A change to any of these changes what this projection carries, silently.** That is the
characteristic failure of a derived index. Three of the four were learned by getting them wrong: an
earlier derivation reported 124 defects, of which 111 were its own blindness to conventions the
documents had used all along. The guard is below.

## Verification

The contract is checkable, and a projection that cannot be checked against its contract is the
defect `4b` §3.1 describes:

| Check | Property |
|---|---|
| every declared term resolves to a definition site | CM-3, nothing declared and undefined |
| no term carries a definition site in two documents | CM-2, a concept is defined once |
| every term a document declares is defined by that document | CM-3, no misplaced ownership |
| re-derivation from an unchanged `spec/` yields an identical projection | PJ-2, PJ-9 |
| the term count matches the source's declared-term count, derived independently of the extractor | **the guard against silent convention drift** |
| — | CM-8 is not checked: ownership is a semantic determination, not a derivable fact |

**The last check is the load-bearing one.** An extractor that silently stops recognizing a
definition form reports the term as an undefined gap and passes every other check — or worse, stops
recognizing a declaration and drops the term from the index entirely, where nothing reports it at
all. Counting the source by a second, independent means is what makes that visible.

## Status against `v0`

Harvested and verified:

```
167 terms · 25 defining documents · 0 declared without a definition site
definition sites: 56 lead · 71 section · 15 copula · 9 table · 16 emphasis
5 declared refinements · 0 defects
```

Every declared term resolves to a definition site, no term is defined in two documents, and each is
defined by the document that declares it. The four ownership conflicts the first harvest found were
settled as refinements under CM-2 and are recorded in `revisions.md` as `v0` Change 1.

**A clean run is not a claim that the vocabulary is right.** It says the declarations and the
definitions agree — nothing declared and undefined, nothing defined twice.

**CM-8 is not among the checks and cannot be.** Whether a term sits with the document whose subject
matter principally establishes it is a semantic determination: settling it for `candidate` meant
reading `1b` §4 and finding that a Part I document defines **proposal** in terms of it. Nothing
mechanical reaches that. This projection reports where terms are defined; it does not judge whether
that is where they belong.

**Authority.** None. `0z` §5.2 and PJ-7: where this projection and the documents disagree, **the
documents govern.**
