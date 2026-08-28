# Machine Block

## 1. Scope

This document defines the **machine block**: the bounded declaration surface from which every
governed artifact is constructed. It specifies what a declaration surface is, what every artifact
carries regardless of kind, who owns each part of it, and how it is closed and extended.

It is the substrate level of Part II. The Kind Vocabulary establishes which kinds exist; the
Governance Semantic Ontology covers what role their elements play; the Governance Standard states
what governance means. This document specifies the surface on which all of that is said.

It is deliberately **kind-extensible**: new artifact kinds and new domains are admitted by
declaration, and admitting them requires no amendment here. It is deliberately
**encoding-neutral**: it is defined over a semantic object, never over a file format.

This document introduces the terms **machine block**, **universal envelope**, **kind
declaration**, **declared extension**, **kind contract**, **semantic owner**, **semantic role**,
and **construction disposition**. Every other term it uses is defined by the Conceptual Model.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. The machine block as a semantic object

A **machine block** is a typed declaration whose type is its artifact kind. Write it
`MachineBlock⟨kind⟩`.

Four properties are constitutive:

- **It is the sole normative declaration surface of the artifact.** Anything outside it —
  narrative, rationale, examples, commentary — is non-normative and MUST NOT determine anything.
  A governing artifact and the applicable kind contract may constrain how the block is
  *interpreted*; they supply normative context, never additional declaration surface.
- **It is declarative.** It states governed facts, constraints, relationships, and permitted
  behavior; it does not carry the procedure that realizes them (Conceptual Model,
  *declarative*). It may state what must, may, or must not occur.
- **Its meaning is self-contained.** It MUST NOT depend on where it is stored, what surrounds it,
  or the byte-level form in which it happens to be serialized.
- **It is bounded.** One artifact has one declaration surface, and what is not on it is not
  declared.

The last two together are what make AI-12 achievable at the level of the artifact: a block whose
meaning depended on its surroundings would import ungoverned content by being moved.

## 3. Encoding neutrality

**This document is defined over the semantic object, not over any file format.**

- Any encoding is conformant if and only if it losslessly carries the semantic object defined
  here — a text format, a structured document, a relational schema, a graph store, or a signed
  binary record. What is required is a single bounded declaration surface per artifact; how that
  surface is realized is not specified here.
- **Equality and identity are defined over the semantic object.** Key order, whitespace, and
  container syntax are not identity. Two encodings are equal exactly when they resolve to the
  same semantic object.
- **Content integrity is computed over a canonical form** of the semantic object, so that
  integrity is stable across re-encoding. An integrity value that changed when a block was
  re-serialized without semantic change would be measuring the encoding, not the declaration.

A realization that embeds its blocks in one particular document format has made a choice, not
satisfied a requirement. No format is normative, and none is privileged.

## 4. Structure

Every machine block has three **logical layers**:

```
MachineBlock⟨kind⟩
├── Universal Envelope    fixed, closed, kind-independent
├── Kind Declaration      owned entirely by the artifact kind
└── Declared Extensions   optional, explicitly governed
```

The layers are **semantic, not necessarily physical**. An encoding MAY represent elements of
different layers in one mapping, provided each element's ownership and closure remain
unambiguous; another MAY separate them entirely. Both conform.

- **Universal envelope** — the small fixed set every artifact carries, whatever its kind: its
  identity, its classification, and its governance assertion (§6–§8).
- **Kind declaration** — the artifact's payload, whose shape the kind contract defines (§9–§10).
  This document specifies the contract *between* the envelope and the declaration; it does not
  prescribe the declaration's shape.
- **Declared extensions** — an optional, named, governed extension surface (§11).

## 5. Ownership

Every declaration element has exactly **one semantic owner**: the universal envelope, one
artifact kind, or one declared extension.

Ownership determines which contract defines the element's meaning and its treatment during
construction. **An element with no owner is inadmissible** — not ignored, not passed through, not
preserved as opaque data. An unowned element is a declaration nothing is responsible for
interpreting, which means its meaning is whatever some mechanism happens to make of it.

## 6. The universal envelope

The envelope carries what every artifact must carry regardless of kind:

| Carries | Requirement | Specified by |
|---|---|---|
| **identity** | REQUIRED | §6.1 |
| **classification** | REQUIRED | §7 |
| **version** | REQUIRED | §6.1 |
| **governance assertion** | KIND-DEPENDENT | §8 |

The envelope is **closed**: an unrecognized envelope element is a hard failure (§11). A kind MUST
NOT redefine envelope semantics, extend the envelope, or reinterpret an envelope element for its
own purposes.

Note that **universal is not universally required**. The governance assertion is universally
*recognized* — every artifact's envelope is understood to have a place for it — while whether it
is *required* is set per kind (§8).

### 6.1 Identity

- The artifact's identity is declared in the envelope and is **authoritative**. Filename, folder,
  containing document, position, and surrounding prose have no authority over it (AI-2).
- Identity is global and unambiguous within the system that admitted the artifact. A duplicate
  identity is a hard failure.
- **References between artifacts are by declared identity only.** No short-name resolution, no
  positional resolution, no search, no fallback.
- A naming convention over identifiers — a prefix, a suffix, a pattern — is a **convention**. A
  kind MAY define and enforce one. Nothing MUST derive an artifact's kind, category, authority,
  or governance from its name (AI-2, GO-3).

**What identity means, how it is structured, and how it resolves are specified by Identity &
Addressing, not here.** This document specifies only that identity is carried in the envelope, is
declared rather than derived, and is authoritative over position.

One requirement does follow here, because it constrains the surface: **identity, authority, and
concern MUST remain separately expressible** (GO-11). A declaration surface on which they cannot
be told apart makes the distinction unenforceable no matter how clearly it is drawn elsewhere.
Which envelope elements carry authority and concern, and in what form, is not specified by this
revision.

## 7. Classification

- Every machine block MUST declare exactly one artifact kind. It is the **authoritative
  discriminator** and the sole determinant of the block's type.
- The kind selects, in one step, the kind contract (§9): structural constraints, invariants,
  reference rules, governance requirement, and projection.
- The admissible kinds are those a declared **kind registry** admits. A kind absent from the
  registry applicable to the artifact is an **unknown kind** and MUST be refused.
- The kind MUST NOT be inferred — not from a name, a prefix, a location, a schema that happens to
  validate, or the shape of the declaration.

Three concerns stay distinct, and collapsing any two of them is a defect:

```
artifact kind      the classification itself
kind registry      the authority for classification    — which kinds may be used
kind contract      the semantics of classification     — what the kind means
```

### 7.1 What is classified by a kind, and what is not

A kind classifies **artifacts** — representations of elements of the governance universe (2b §2.1).
It does not classify everything a governed system declares. Two things are routinely confused, and
a system that confuses them either fragments one artifact into many or hides many inside one:

| | What it is | Carries a kind |
|---|---|---|
| **artifact** | a representation of an element, with its own identity, its own admission, and its own governance assertion | **yes** — exactly one (§7) |
| **declaration element** | a part of an artifact's declaration surface, owned by that artifact and meaningful only within it (§12, MB-4) | **no** |

**The test is admission, not size or structure.** An element is an artifact when it is admitted on
its own — determined against governance in its own right, identified independently, referenced from
outside the artifact that would otherwise contain it, and capable of being superseded without
superseding a container. An element that cannot be any of those is a declaration element of
something that can, however elaborate its internal structure.

Two consequences follow:

- **Structured data inside an artifact does not become an artifact by being structured.** A routing
  table, a rule set, a register, a parameter block, a list of steps — each is a declaration element
  of the artifact whose surface declares it, and none requires a kind. It is governed, because the
  artifact carrying it is; it is closed, because that surface is closed (§11); and it has an owner,
  because MB-4 requires one.
- **An artifact does not stop being one by being carried somewhere.** Where an element is stored,
  serialized, or bundled does not decide the question — MB-2 already forbids meaning from depending
  on location. An element referenced by identity from outside is admitted on its own whatever file
  it arrives in.

**A vocabulary is not incomplete because it admits no kind for a declaration element.** A closed
vocabulary is required to admit a kind for every artifact the system declares; it is not required to
admit one for every declared thing, and adding kinds for declaration elements produces a taxonomy of
fields rather than of representations (2d §11).

## 8. The governance assertion

The envelope carries the artifact's **assertion of what governs it** — the subject-side half of
the governing relation the Governance Standard requires be established from both ends (§3.2
there). The element-side half is carried by the governing element; the two must agree, and a
disagreement is refused.

The assertion is **not universally mandatory**. Every kind declares whether its governance model
requires it:

- A kind whose authority derives from a governing element MUST require it.
- A kind that participates in constituting the system's root of governance MAY omit the
  governance assertion **only in the genesis case** defined by Semantic Model §11, because no
  predecessor closure exists from which the assertion could be inherited. Such kinds are
  determined at genesis against the closure composed from the proposal's declared governance and
  the claimed profile; **omission here is not exemption from governance.**

The justification is semantic, not practical. Omission is permitted because at genesis there is
nothing to assert — not because asserting would be circular or inconvenient. A kind that omits
the assertion outside genesis has not avoided a dependency; it has escaped determination.

## 9. Kind contract

An artifact kind resolves to a **kind contract**: the complete agreement governing the
**kind-specific** admissibility and interpretation of that kind. It does not restate the
semantics Parts I and II have already specified, and cannot override them. A structural schema is one part of it, not the
whole:

```
Kind Contract
├── identity rules          where applicable   naming convention, identity rules
├── structural constraints  required           element shape, types, closure
├── governance requirement  where applicable   whether the governance assertion is required
├── semantic constraints    where applicable   purity, acyclicity, resolution
├── reference rules         where applicable   which elements carry references, and their scope
├── lifecycle rules         where applicable   versioning, supersession, deprecation
└── projection contract     required where a projection exists
```

Not every kind carries every part. A purely definitional kind may have no projection; a
root-of-governance kind may have no governance requirement.

**The structural constraints are stated in whatever form the kind's constraints take.** A closed
document schema is one realization and is not privileged; a kind whose constraints are
relational, graph-shaped, temporal, or cryptographic states them in the appropriate form. The
kind contract is normative; no particular schema language is.

Validation has two stages, and both complete before anything depending on them proceeds (AI-5):
**structural** — shape and closure — and **semantic** — invariants and reference resolution.

## 10. The kind declaration surface

- The kind declaration is **owned entirely by the kind**. It may consist of scalar elements,
  mappings, sequences, nested sections, or several named top-level sections. This document does
  not prescribe its decomposition.
- Where a kind names a section as its semantic payload, that name is a **convention of the
  kind**, not a universal element. It means *this kind's semantic core*, never "everything that
  is not envelope." A kind whose payload lives under any other named surface is equally valid and
  requires no such section.

## 11. Closure and extension

Three levels of closure, strongest first:

1. **Envelope closure** — the universal envelope is closed. An unrecognized envelope element is a
   hard failure.
2. **Kind closure** — the kind declaration is closed by its structural constraints. An
   unrecognized element within it is a hard failure.
3. **Extension closure** — a kind MAY declare a named extension surface. Only declared extensions
   are admissible.

**There is no open kind.** No surface admits arbitrary undeclared elements. Adding a kind, an
element, or an extension is a declaration act (§14), never undeclared behavior.

Closure is what makes an unknown element a *finding* rather than a silent passenger. On an open
surface, an element nobody defined is indistinguishable from an element somebody forgot to
implement — and both are indistinguishable from an element someone inserted.

## 12. Declaration elements — role and disposition

A **declaration element** is any named element, section, mapping, sequence, or nested value whose
meaning a kind contract defines. A kind contract MAY define a subtree as a single semantic
element rather than specifying every leaf.

Every normative declaration element MUST be assigned both a role and a disposition by its owning
contract:

**Semantic role** — what the element *is*:

| Role | The element carries |
|---|---|
| identity | what this artifact is |
| governance | what governs it |
| declaration | what it declares |
| constraint | a condition it imposes |
| reference | a relation to another artifact |
| evidence | a record of something that occurred |

**Construction disposition** — what becomes of the element during construction:

| Disposition | Meaning |
|---|---|
| consumed | drives a construction determination or a projection |
| preserved | carried into the canonical record for evidence, not acted on |
| derived-from | an input to a synthesized structure |
| validation-only | participates in admissibility, and produces no projection |

The first three answer *what happens to the element*; `validation-only` answers *does it produce
a projection* — no. **A validation-only element is not discardable metadata**: it is semantically
meaningful and its absence changes admissibility.

**An element with no role and no disposition is inadmissible.** Together with §5, this closes the
gap through which unexamined declaration content otherwise reaches a built system.

## 13. Projection and provenance

- Construction is the only transform from declaration to executable form. **A sealed
  representation is not another encoding of the machine block; it is a governed projection of
  it.** Elements are consumed, derived from, preserved, or validation-only (§12), so a projection
  contains what the contract projects — never a serialized copy of everything declared.
- A constructed artifact MUST retain **canonical source provenance** sufficient for identity,
  verification, and audit: the normalized semantic object together with an integrity value over
  its canonical form (§3). What these are named is not specified here.
- **Traceability.** Every semantic element in a sealed representation MUST be traceable to at
  least one of: a declared machine block; a governing artifact; a declared construction
  transformation; or a required integrity mechanism. **No domain behavior may enter a sealed
  representation except through declared machine blocks and the governance that admitted them.**
- Nothing in execution may synthesize identity, structure, or binding (AI-11, AI-12).

## 14. Admitting a new kind

Admitting a kind is a declaration act, performed in this order:

1. Define the kind's semantics and any naming convention over its identifiers.
2. Define its kind declaration surface (§10) and any declared extension surface (§11).
3. Author its kind contract (§9).
4. Register the kind and its contract in the declared registry (§7).
5. Assign every element a role and a disposition (§12).
6. Declare the semantic category of the elements the kind represents, and any provenance
   constraints its kind contract imposes (Governance Semantic Ontology §8).
7. Supply conformance evidence (§16).

**No change to a construction mechanism is required** for a kind whose projection reuses existing
machinery, and a novel projection is itself declared rather than built in. A kind that cannot be
admitted without amending a mechanism has revealed that the mechanism, not the kind, is carrying
the semantics.

## 15. Normative invariants

- **MB-1.** An artifact MUST have exactly one bounded declaration surface, and nothing outside it
  MUST determine anything about the artifact (§2).
- **MB-2.** A machine block's meaning MUST NOT depend on its location, its surroundings, or its
  serialized form (§2, §3).
- **MB-3.** Equality and identity MUST be defined over the semantic object. Integrity MUST be
  computed over a canonical form of the semantic object (§3).
- **MB-4.** Every declaration element MUST have exactly one semantic owner (§5).
- **MB-5.** The universal envelope MUST be closed, and a kind MUST NOT redefine or extend it
  (§6).
- **MB-6.** Identity MUST be declared, MUST be authoritative over position, and MUST NOT be
  derived from a name or location (§6.1).
- **MB-7.** Identity, authority, and concern MUST remain separately expressible at the
  declaration surface, and their representation MUST NOT collapse these distinctions (§6.1,
  GO-11).
- **MB-8.** Every block MUST declare exactly one artifact kind, and the kind MUST NOT be inferred
  (§7).
- **MB-9.** An unregistered kind MUST be refused (§7).
- **MB-10.** A kind MUST declare whether a governance assertion is required for its ordinary
  use. Omission MUST be permitted only where the applicable semantic model authorizes it, and
  MUST NOT constitute exemption from governance (§8).
- **MB-11.** Every surface MUST be closed; no surface may admit undeclared elements (§11).
- **MB-12.** Every normative declaration element MUST carry a semantic role and a construction
  disposition (§12).
- **MB-13.** Every semantic element of a sealed representation MUST have a declared provenance
  to at least one of: a declared machine block, a governing artifact, a declared construction
  transformation, or a required integrity mechanism (§13).
- **MB-14.** Admitting a kind MUST NOT require amending this document (§14).
- **MB-15.** An element MUST carry a kind if and only if it is admitted as an artifact in its own
  right; a declaration element of an artifact MUST NOT carry one (§7.1).

## 16. Conformance

The conformance subject of this document is a **declaration surface**: the machine blocks of a
governed system together with the contracts that own them.

An individual machine block is **admissible** when:

- its envelope validates and is closed (MB-5);
- its kind declaration satisfies its kind contract — structural constraints and semantic
  constraints alike — and is closed at the kind level (§9, MB-11);
- only declared extensions are present (§11);
- every reference it carries resolves within the admitted set (§6.1);
- its governance requirement is met (§8); and
- every declaration element has an owner, a role, and a disposition (MB-4, MB-12).

The following are the findings a conforming realization distinguishes, each of them determined
before anything depending on the artifact proceeds: **unrecognized envelope element**,
**unrecognized kind element**, **undeclared extension**, **unowned element**, **element without
role or disposition**, **unresolved reference**, **unregistered kind**, **duplicate identity**,
**unmet governance requirement**.

Every one of them is a refusal. **Closed surfaces fail hard**: there is no warning-only
degradation, no partial admission, and no recovery during execution (AI-6, AI-8).
