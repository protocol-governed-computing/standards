# Machine Block

## 1. Scope

This document defines the **machine block**: the bounded declaration surface from which every
governed artifact is constructed. It specifies:

- what a declaration surface is;
- what every artifact carries, whatever its kind;
- who owns each part of the surface;
- how the surface is closed and extended.

This is the substrate level of Part II. The Kind Vocabulary establishes which kinds exist. The
Governance Semantic Ontology covers what role their elements play. The Governance Standard states
what governance means. This document specifies the surface on which all of that is said.

This document is deliberately **kind-extensible**. A system admits new artifact kinds and new domains
by declaration, and admitting them requires no amendment here. It is also deliberately
**encoding-neutral**. It is defined over a semantic object, never over a file format.

This document introduces the terms **machine block**, **universal envelope**, **kind
declaration**, **declared extension**, **kind contract**, **semantic owner**, **semantic role**,
and **construction disposition**. The Conceptual Model defines every other term it uses.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. The machine block as a semantic object

A **machine block** is a typed declaration whose type is its artifact kind. Write it
`MachineBlock⟨kind⟩`.

Four properties are constitutive:

- **It is the sole normative declaration surface of the artifact.** Anything outside it is
  non-normative and MUST NOT determine anything. That includes narrative, rationale, examples and
  commentary. A governing artifact and the applicable kind contract may constrain how the block is
  *interpreted*. They supply normative context, never extra declaration surface.
- **It is declarative.** It states governed facts, constraints, relationships and permitted
  behavior. It does not carry the procedure that realizes them (Conceptual Model, *declarative*).
  It may state what must, may or must not occur.
- **Its meaning is self-contained.** Its meaning MUST NOT depend on where it is stored, what
  surrounds it, or the byte-level form in which it happens to be serialized.
- **It is bounded.** One artifact has one declaration surface. Only what is on that surface is
  declared.

The last two properties together make AI-12 achievable at the level of the artifact. If a block's
meaning depended on its surroundings, moving the block would import ungoverned content.

## 3. Encoding neutrality

**This document is defined over the semantic object, not over any file format.**

- An encoding conforms if and only if it carries the semantic object defined here without loss. It
  may be a text format, a structured document, a relational schema, a graph store or a signed
  binary record. Each artifact needs a single bounded declaration surface. This document does not
  specify how a realization builds that surface.
- **Equality and identity are defined over the semantic object.** Key order, whitespace and
  container syntax are not identity. Two encodings are equal exactly when they resolve to the same
  semantic object.
- **Content integrity is computed over a canonical form** of the semantic object, so integrity stays
  stable across re-encoding. Suppose an integrity value changed when a block was re-serialized with
  no semantic change. That value would measure the encoding, not the declaration.

A realization that embeds its blocks in one particular document format has made a choice. It has not
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
different layers in one mapping, provided each element's ownership and closure stay unambiguous.
Another encoding MAY separate the layers entirely. Both conform.

- **Universal envelope.** The small fixed set every artifact carries, whatever its kind: its
  identity, its classification and its governance assertion (§6–§8).
- **Kind declaration.** The artifact's payload. The kind contract defines its shape (§9–§10). This
  document specifies the contract *between* the envelope and the declaration. It does not prescribe
  the declaration's shape.
- **Declared extensions.** An optional, named, governed extension surface (§11).

## 5. Ownership

Every declaration element has exactly **one semantic owner**: the universal envelope, one artifact
kind, or one declared extension.

The owner determines which contract defines the element's meaning and how construction treats it.

**An element with no owner is inadmissible.** A realization does not ignore it, pass it through, or
preserve it as opaque data. Nothing is responsible for interpreting an unowned element. Its meaning
then becomes whatever some mechanism happens to make of it.

## 6. The universal envelope

The envelope carries what every artifact must carry, whatever its kind:

| Carries | Requirement | Specified by |
|---|---|---|
| **identity** | REQUIRED | §6.1 |
| **classification** | REQUIRED | §7 |
| **version** | REQUIRED | §6.1 |
| **governance assertion** | KIND-DEPENDENT | §8 |

The envelope is **closed**. An unrecognized envelope element is a hard failure (§11). A kind MUST NOT
redefine envelope semantics, extend the envelope, or reinterpret an envelope element for its own
purposes.

Note that **universal is not universally required**. Every artifact's envelope has a recognized place
for the governance assertion. Each kind sets whether the assertion is *required* (§8).

### 6.1 Identity

- The artifact's identity is declared in the envelope and is **authoritative**. Filename, folder,
  containing document, position and surrounding prose have no authority over it (AI-2).
- Identity is global and unambiguous within the system that admitted the artifact. A duplicate
  identity is a hard failure.
- **Artifacts reference one another by declared identity only.** There is no short-name resolution,
  no positional resolution, no search and no fallback.
- A naming convention over identifiers, such as a prefix, a suffix or a pattern, is a
  **convention**. A kind MAY define and enforce one. Nothing MUST derive an artifact's kind,
  category, authority, or governance from its name (AI-2, GO-3).

**Identity & Addressing specifies what identity means, how it is structured and how it resolves.
This document does not.** This document specifies only three things: the envelope carries identity,
identity is declared rather than derived, and identity is authoritative over position.

One requirement does follow here, because it constrains the surface: **identity, authority, and
concern MUST remain separately expressible** (GO-11). On a declaration surface where they cannot be
told apart, the distinction is unenforceable, however clearly another document draws it. This
revision does not specify which envelope elements carry authority and concern, or in what form.

## 7. Classification

- Every machine block MUST declare exactly one artifact kind. The kind is the **authoritative
  discriminator** and the sole determinant of the block's type.
- In one step, the kind selects the kind contract (§9): structural constraints, invariants,
  reference rules, governance requirement and projection.
- The admissible kinds are those that a declared **kind registry** admits. A kind absent from the
  registry that applies to the artifact is an **unknown kind** and MUST be refused.
- The kind MUST NOT be inferred: not from a name, a prefix, a location, a schema that happens to
  validate, or the shape of the declaration.

Three concerns stay distinct. Merging any two of them is a defect:

```
artifact kind      the classification itself
kind registry      the authority for classification    — which kinds may be used
kind contract      the semantics of classification     — what the kind means
```

### 7.1 What is classified by a kind, and what is not

A kind classifies **artifacts**: representations of elements of the governance universe (Governance
Semantic Ontology §2.1). It does not classify everything a governed system declares. People often
confuse two things. A system that confuses them either splits one artifact into many or hides many
inside one:

| | What it is | Carries a kind |
|---|---|---|
| **artifact** | a representation of an element, with its own identity, its own admission, and its own governance assertion | **yes** — exactly one (§7) |
| **declaration element** | a part of an artifact's declaration surface, owned by that artifact and meaningful only within it (§12, MB-4) | **no** |

**The test is admission, not size or structure.** An element is an artifact when the system admits it
on its own. Such an element is:

- determined against governance in its own right;
- identified independently;
- referenced from outside the artifact that would otherwise contain it;
- capable of being superseded without superseding a container.

An element that can be none of those is a declaration element of something that can, however
elaborate its internal structure.

Two consequences follow:

- **Structured data inside an artifact does not become an artifact by being structured.** A routing
  table, a rule set, a register, a parameter block and a list of steps are all examples. Each is a
  declaration element of the artifact whose surface declares it, and none needs a kind. It is
  governed, because the artifact carrying it is governed. It is closed, because that surface is
  closed (§11). It has an owner, because MB-4 requires one.
- **An artifact does not stop being one by being carried somewhere.** Where an element is stored,
  serialized or bundled does not decide the question. MB-2 already forbids meaning from depending on
  location. An element referenced by identity from outside is admitted on its own, whatever file it
  arrives in.

**A vocabulary that admits no kind for a declaration element is still complete.** A closed
vocabulary must admit a kind for every artifact the system declares. It need not admit one for every
declared thing. Kinds added for declaration elements would make a taxonomy of fields, not of
representations (Kind Vocabulary §11).

## 8. The governance assertion

The envelope carries the artifact's **assertion of what governs it**. This is the subject-side half
of the governing relation. The Governance Standard requires that relation to be established from
both ends (§3.2 there). The governing element carries the element-side half. The two must agree,
and a disagreement is refused.

The assertion is **not universally mandatory**. Every kind declares whether its governance model
requires it:

- A kind whose authority derives from a governing element MUST require it.
- A kind that takes part in constituting the system's root of governance MAY omit the governance
  assertion **only in the genesis case** that Semantic Model §11 defines. At genesis, no predecessor
  closure exists from which the assertion could be inherited. Such kinds are determined at genesis
  against the closure composed from the proposal's declared governance and the claimed profile.
  **Omission here is not exemption from governance.**

The justification is semantic, not practical. Omission is permitted because at genesis there is
nothing to assert. It is not permitted because asserting would be circular or inconvenient. A kind
that omits the assertion outside genesis has not avoided a dependency. It has escaped determination.

## 9. Kind contract

An artifact kind resolves to a **kind contract**: the complete agreement governing the
**kind-specific** admissibility and interpretation of that kind. The kind contract does not restate
the semantics that Parts I and II already specify, and it cannot override them. A structural schema
is one part of the contract, not the whole:

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

Not every kind carries every part. A purely definitional kind may have no projection. A
root-of-governance kind may have no governance requirement.

**A kind states its structural constraints in whatever form those constraints take.** A closed
document schema is one realization, and it is not privileged. A kind whose constraints are
relational, graph-shaped, temporal or cryptographic states them in the fitting form. The kind
contract is normative. No particular schema language is.

Validation has two stages. Both complete before anything that depends on them proceeds (AI-5):

- **structural**: shape and closure;
- **semantic**: invariants and reference resolution.

## 10. The kind declaration surface

- The kind declaration is **owned entirely by the kind**. It may consist of scalar elements,
  mappings, sequences, nested sections, or several named top-level sections. This document does not
  prescribe how it decomposes.
- A kind may name a section as its semantic payload. That name is a **convention of the kind**, not
  a universal element. It means *this kind's semantic core*. It never means "everything that is not
  envelope". A kind whose payload lives under any other named surface is equally valid and needs no
  such section.

## 11. Closure and extension

There are three levels of closure, strongest first:

1. **Envelope closure.** The universal envelope is closed. An unrecognized envelope element is a
   hard failure.
2. **Kind closure.** The kind's structural constraints close the kind declaration. An unrecognized
   element within it is a hard failure.
3. **Extension closure.** A kind MAY declare a named extension surface. Only declared extensions are
   admissible.

**There is no open kind.** Every surface admits only declared elements. Adding a kind, an element or
an extension is a declaration act (§14), never undeclared behavior.

Closure makes an unknown element a *finding* rather than a silent passenger. On an open surface, an
element nobody defined looks the same as an element somebody forgot to implement. Both look the same
as an element someone inserted.

## 12. Declaration elements — role and disposition

A **declaration element** is any named element, section, mapping, sequence, or nested value whose
meaning a kind contract defines. A kind contract MAY define a subtree as a single semantic element,
without specifying every leaf.

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

The first three answer *what happens to the element*. `validation-only` answers *does it produce a
projection?* The answer is no. **A validation-only element is not discardable metadata.** It has
semantic meaning, and its absence changes admissibility.

**An element with no role and no disposition is inadmissible.** Together with §5, this rule closes
the gap through which unexamined declaration content would otherwise reach a built system.

## 13. Projection and provenance

- Construction is the only transform from declaration to executable form. **A sealed representation
  is not another encoding of the machine block. It is a governed projection of it.** Each element is
  consumed, derived from, preserved or validation-only (§12). So a projection contains what the
  contract projects. It never contains a serialized copy of everything declared.
- A constructed artifact MUST retain **canonical source provenance** sufficient for identity,
  verification and audit. That provenance is the normalized semantic object together with an
  integrity value over its canonical form (§3). This document does not specify what these are named.
- **Traceability.** Every semantic element in a sealed representation MUST be traceable to at least
  one of: a declared machine block, a governing artifact, a declared construction transformation, or
  a required integrity mechanism. **Domain behavior may enter a sealed representation only through
  declared machine blocks and the governance that admitted them.**
- Nothing in execution may synthesize identity, structure or binding (AI-11, AI-12).

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

A kind whose projection reuses existing machinery needs **no change to a construction mechanism**. A
novel projection is itself declared, not built in. Suppose a kind cannot be admitted without amending
a mechanism. That reveals that the mechanism, not the kind, carries the semantics.

## 15. Normative invariants

- **MB-1.** An artifact MUST have exactly one bounded declaration surface, and nothing outside it
  MUST determine anything about the artifact (§2).
- **MB-2.** A machine block's meaning MUST NOT depend on its location, its surroundings, or its
  serialized form (§2, §3).
- **MB-3.** Equality and identity MUST be defined over the semantic object. Integrity MUST be
  computed over a canonical form of the semantic object (§3).
- **MB-4.** Every declaration element MUST have exactly one semantic owner (§5).
- **MB-5.** The universal envelope MUST be closed, and a kind MUST NOT redefine or extend it (§6).
- **MB-6.** Identity MUST be declared and MUST be authoritative over position. It MUST NOT be derived
  from a name or location (§6.1).
- **MB-7.** Identity, authority, and concern MUST remain separately expressible at the declaration
  surface. Their representation MUST NOT collapse these distinctions (§6.1, GO-11).
- **MB-8.** Every block MUST declare exactly one artifact kind, and the kind MUST NOT be inferred
  (§7).
- **MB-9.** An unregistered kind MUST be refused (§7).
- **MB-10.** A kind MUST declare whether its ordinary use requires a governance assertion. Omission
  MUST be permitted only where the applicable semantic model authorizes it, and MUST NOT constitute
  exemption from governance (§8).
- **MB-11.** Every surface MUST be closed. No surface may admit undeclared elements (§11).
- **MB-12.** Every normative declaration element MUST carry a semantic role and a construction
  disposition (§12).
- **MB-13.** Every semantic element of a sealed representation MUST have a declared provenance to at
  least one of: a declared machine block, a governing artifact, a declared construction
  transformation, or a required integrity mechanism (§13).
- **MB-14.** Admitting a kind MUST NOT require amending this document (§14).
- **MB-15.** An element MUST carry a kind if and only if it is admitted as an artifact in its own
  right. A declaration element of an artifact MUST NOT carry one (§7.1).

## 16. Conformance

The conformance subject of this document is a **declaration surface**: the machine blocks of a
governed system together with the contracts that own them.

An individual machine block is **admissible** when all of the following hold:

- Its envelope validates and is closed (MB-5).
- Its kind declaration satisfies its kind contract, both structural and semantic constraints, and
  is closed at the kind level (§9, MB-11).
- Only declared extensions are present (§11).
- Every reference it carries resolves within the admitted set (§6.1).
- Its governance requirement is met (§8).
- Every declaration element has an owner, a role and a disposition (MB-4, MB-12).

A conforming realization distinguishes the following findings. It determines each one before
anything that depends on the artifact proceeds:

- **unrecognized envelope element**
- **unrecognized kind element**
- **undeclared extension**
- **unowned element**
- **element without role or disposition**
- **unresolved reference**
- **unregistered kind**
- **duplicate identity**
- **unmet governance requirement**

Every one of them is a refusal. **Closed surfaces fail hard.** There is no warning-only degradation,
no partial admission, and no recovery during execution (AI-6, AI-8).
