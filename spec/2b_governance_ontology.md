# Governance Semantic Ontology

## 1. Scope

This document defines the closed classification of **semantic roles** that the elements of a
governance universe play. It also defines the obligations each role carries.

It answers one question: *what role does this element play in the governed system?* It deliberately
answers no other. In particular, other documents answer these:

| Question | Answered by |
|---|---|
| *what type of artifact is this?* | the Kind Vocabulary |
| *what may this artifact declare?* | the Machine Block Standard |
| *by what right does this govern that?* | Governance Closure & Authority |
| *what happens when governance is evaluated?* | Enforcement & Refusal |

**This ontology is subordinate to the Governance Standard.** It classifies elements whose governance
semantics that document has already specified. It establishes no authority, no scope, no admission
and no enforcement. An ontology that determined any of those would be a second, undeclared
governance layer. Its classifications would silently become permissions.

The ontology's value is a small vocabulary, closed within each revision. In it, a cross-cutting
obligation is stated once per role, not re-declared for each kind.

### 1.1 Closed is not a ceiling

**"Closed" constrains the set of *roles*, not the set of systems.** Within one revision, the
categories are settled. So nobody can quietly widen the classification. Nobody can escape an
obligation stated per category by inventing a new category. "Closed" does not mean the ontology
describes only simple systems. It does not limit what may be governed.

A more complex governed system admits everything it needs as **kinds**, and kinds are open. Examples:

- signing and attestation authorities;
- distributed and multi-node execution;
- replicated or partitioned state;
- cross-organizational federation;
- delegated and revocable authority;
- sealed transport between authorities;
- external attestors.

Each of these introduces elements that *define* something, *require* something, *expose* something,
*do* something, *act*, or *record*. So each is classified by naming the existing role it occupies.
GO-12 tests that this stays true. If admitting such a kind forced a new category, the categories
were drawn around the kinds that happened to exist, not around the roles that exist.

A genuinely new *role* is possible: a way of taking part in governance that none of the six
describes. Ontology revision handles it (§9). That is a defined procedure with stated
consequences, not a wall.

The closure prevents only one thing: a new category arriving by accident. That is how a
classification loses the ability to carry obligations.

Nothing in this document is scoped to a particular deployment shape, trust model or number of
authorities.

This document introduces the terms **governance universe**, **semantic category**, and **category
contract**, and refines the Conceptual Model's **provenance**. The Conceptual Model or the
Governance Standard defines every other term it uses.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What is classified

### 2.1 Element, artifact, kind

People often conflate three things. If they are conflated, the ontology is unusable:

| | What it is | Classified by |
|---|---|---|
| **Element** | a semantic object of the governance universe | this ontology |
| **Artifact** | a representation of an element | the Kind Vocabulary |
| **Artifact kind** | the taxonomy of representations | the Kind Vocabulary |

**This document classifies elements.** Artifacts represent elements. Kinds classify the
representations. Category is a property of the *semantic element*. A kind **declares** the primary
semantic category of the elements it represents. A category is not a kind, and a kind is not a
category. If the classification moved from ontology to taxonomy, the role an element plays would
depend on how someone happened to write it down.

### 2.2 The governance universe

The **governance universe** is the bounded semantic domain comprising the entities, declarations,
authorities, behaviors, participants, and evidence that are subject to, participate in, or are
produced by the governance of a system.

The universe is wider than the set of governing elements. Governed behavior is an element of the
universe, and so is evidence that records what occurred. Neither governs anything. **So
classification does not state that an element governs.** Most elements do not. An element governs
only when the Governance Standard's relation makes it a governing element. Its category does not.

```
governance universe        the bounded subject of governance
        │  classified by
        ▼
semantic categories        the closed set of roles (§3)
        │  represented by
        ▼
governance artifacts       authored, derived, or produced representations
```

### 2.3 Three levels that stay separate

```
artifact kind ......  TAXONOMY   — what type of representation is this?   open, extensible
semantic category ..  ONTOLOGY   — what role does the element play?       closed, stable
category contract ..  OBLIGATION — what does that role entail?            per category
```

Many kinds may share one category. Each kind has exactly one. The vocabulary of kinds is open, so a
system may admit new kinds. The ontology is closed, so admitting them changes nothing about which
roles exist.

## 3. The primary dimension — semantic category

Every element of a governance universe has exactly **one primary semantic category**. Architectural
prose calls the categories the *governance strata* of a system. *Stratum* expresses separation, not
rank. A participant is not above or below a behavior.

| Category | Answers | Establishes |
|---|---|---|
| **Definitional** | what things *are* | terms, shape, and identity definitions |
| **Normative** | what must hold, and who may | obligation |
| **Contractual** | what is *exposed* | a typed boundary |
| **Operational** | what the system *does* | behavior |
| **Participatory** | *who* acts | governed identities |
| **Evidential** | what *occurred* | the record |

Three rules govern the dimension:

- **Exactly one primary category.** Secondary relationships (§5) may connect an element to other
  categories. They MUST NOT make its primary classification ambiguous. Classification stays
  single-valued. The model does not force a system to split an element because it relates outward.
- **Closed within a revision.** A system admits a new kind, including a domain kind, by naming the
  existing category it occupies. Adding a kind does not add a category. Adding a category is an
  ontology revision (§9).
- **Category is not status.** The six are roles, not ranks. The ontology asserts no ordering among
  them.

## 4. Category contracts

A category is a name. A **category contract** is what the name entails. Each category carries one,
and the ontology does its work there. An obligation in a category contract is stated once and binds
every kind in that category. Without it, each kind would re-declare the obligation, and the copies
would drift apart.

A category contract states four things about its category:

- its semantic meaning;
- its relationship to authority;
- the dependencies its members may have;
- its category invariants.

This is the category's contract, not a second taxonomy.

### 4.1 Category invariants

- **Definitional** — MUST be resolvable before anything that references it is determined. Other
  categories reference it. It depends on none.
- **Normative** — MUST be governed by a constitutive authority. A normative element MAY be *informed*
  by evidence, but evidence MUST NOT thereby become a source of its authority.
- **Contractual** — MUST declare a closed interface. It binds operational elements to the normative
  obligations that constrain them.
- **Operational** — MUST be governed by a norm, and MUST satisfy the applicable contractual
  requirements governing its exposed behavior. MUST NOT be a source of authority. All exposed
  operational behavior is contract-bound. The requirement is that a contract governs the behavior.
  It does not require each operational element to have a separately instantiated contract.
- **Participatory** — MUST carry declared identity, with identity held separate from authority.
  MUST NOT carry behavior.
- **Evidential** — append-only. MUST NOT be referenced as authority. Evidence records what occurred.
  What occurred does not thereby become what must hold.

Two points need emphasis. Systems that look well governed violate both:

**Evidence does not govern.** A system that derives a rule from what has happened has made its past
its authority. It can no longer tell what it is required to do from what it happens to have done.

**Identity is not authority.** A participatory element names who acts. A normative element states
what they may do. If the two merge, every identity becomes a permission.

### 4.2 Runtime disposition

Disposition is a property of the category contract, not of the category itself. It says how the
category's elements stand with respect to execution:

| Category | Disposition |
|---|---|
| Definitional | not executable |
| Normative | not executable |
| Contractual | not independently executable |
| Operational | executable |
| Participatory | may participate in execution through an operational element |
| Evidential | produced by execution |

Only **Operational** elements enter execution as behavior. That single category is not a
convenience. It is what makes the space of things that can happen enumerable.

## 5. Secondary relationships

The primary category answers what an element *is*. Secondary relationships answer what it *governs,
exposes, constrains or produces*. An element may relate into other categories while its primary
classification stays the same:

```
a capability contract
  primary category:  Contractual
  relationships:
      governed by  →  Normative
      constrains   →  Operational
      exposes      →  Operational
```

Relationships are how categories compose into a system. The primary category is how each element is
classified. The two MUST NOT be conflated. An element that *constrains* operational elements is not
thereby operational. An element *governed by* a norm is not thereby normative.

## 6. The second dimension — provenance

Provenance is how the element came to exist. It is independent of category, and nobody can derive it
from category.

| Provenance | Definition |
|---|---|
| **authored** | created as a source declaration, independently governed |
| **derived** | synthesized deterministically from one or more declarations |
| **produced** | arising as a consequence of execution or system operation |

*Refining the Conceptual Model's* **provenance**: within the ontology, provenance is the **origin
relation of a semantic element**. It is not a lifecycle state, and it is not a property of any one
representation of the element. It records how the element came into existence, and it is settled at
that moment.

**Later representations do not change it.** One semantic element may have source, constructed,
runtime and evidence representations. An authored element that is later materialized, projected or
indexed remains authored. A computed representation does not make the element derived. The
representation was derived, not the element it carries. This axis exists to prevent one error:
reading provenance off a representation.

Two obligations attach:

- **Derived and produced elements MUST NOT become sources of governance authority** by virtue of
  having been derived or produced. Being computed is not being authorized.
- **Derived and produced elements MUST carry provenance sufficient to identify their source or
  producing operation**, and MUST NOT be admitted as independent authoritative source declarations.

Provenance is a separate axis because category cannot recover it. Take an element derived from a
norm, and the norm it was derived from. Both occupy the same category. They differ in what a system
may do with them.

## 7. What is not an ontology axis

### 7.1 Rejected axes

Governance *function*, execution *phase*, authority *level* and *lifecycle* are not independent
ontology axes. Each is either the category restated as a verb, or a property of a category contract.
If the ontology modelled any of them, it would multiply the classification without adding a
distinction.

### 7.2 What partitions a universe is not what classifies its elements

Four concepts describe how a governance universe is *organized or related*. They are not roles. They
do not classify elements. They are independent of both dimensions above:

| | Answers | Is not |
|---|---|---|
| **Authority** | who may decide | a category, and not derivable from one |
| **Concern** | what is being decided about | authority — a concern may be organized and governed with no authority constituted over it |
| **Federation** | how distinct authorities coexist, delegate, and bound one another | a property of any single authority |
| **Namespace** | how identity is carried and resolved | a claim of authority, concern, or federation |

**Authority ≠ Concern ≠ Federation ≠ Namespace.** A representation might encode more than one of
these in a single identifier. No check could then tell them apart. The distinctions would become
unenforceable, however plainly a document declared them elsewhere.

An element has a category and a provenance. It also falls under some authority and concerns some
subject. None of the four can be recovered from the others. **The semantics of authority, concern
and federation belong to the Governance Standard and to Governance Closure & Authority.** This
document specifies only that they are not ontology axes, and that classification never supplies
them.

This revision treats federation as a **relation among authorities**, not as a governed subject that
an authority owns. That treatment is not settled (§10). If federation were a subject, it would need
a classification. Whether it has one is exactly the question of whether it is a subject.

## 8. Relationship to artifact kind

- Each artifact kind declares the **semantic category** of the elements it represents. Where its
  kind contract constrains provenance, the kind also declares the provenance values permitted for
  it. Category follows from the kind. Provenance does not always follow, because one kind may
  represent elements of different origin. The **provenance of an individual element MUST be
  established explicitly** and MUST NOT be inferred from an artifact's name, location, or content.
- The ontology is closed and the vocabulary of kinds is open. So a new kind is classified purely by
  naming its category. **Admitting a new kind requires no ontology change.**
- A kind's category MUST be consistent with what its kind contract requires it to declare. The
  category contract states what is expected *where applicable*. It does not require every kind in a
  category to expose an identical declaration surface.

## 9. Extension

To admit a **kind**, a system names the category it occupies and the provenance it carries. Nothing
in this document changes.

Adding, removing or merging a **category** is an ontology revision. It MUST be deliberate. It
invalidates every category contract, kind classification and cross-cutting obligation stated in
terms of the affected category. A revision is not an addition.

So the design criterion is not whether the ontology describes today's elements elegantly. It is
whether **admitting a genuinely new kind requires changing the ontology**. If it does not, the
ontology is at the right level of abstraction. If it does, the categories were drawn around the
kinds that happened to exist.

## 10. What this ontology does not specify

This revision deliberately leaves four classification questions open. They are recorded here because
a document that silently assumed answers would close them off:

- **Whether Evidential is a peer category.** *Definitional* through *Participatory* describe the
  semantic role of a declaration. *Evidential* describes a record's relationship to execution. This
  revision treats it as a peer category. Whether it is instead an orthogonal produced-state
  dimension is unresolved.
- **Whether provenance remains an independent axis** or folds into the kind contract. This revision
  keeps it as an axis because it does not reduce to category.
- **Whether Participatory is primary** or a sub-role of normative authority.
- **Whether federation is a relation or a governed subject.** §7.2 treats it as a relation among
  authorities, so it receives no category. If it were a subject that an authority owns, it would
  need a category, and the ontology would have to say which. The two possibilities are not a matter
  of style. A relation cannot be classified, and a subject must be.

Each question is resolved by demonstration, not by argument about elegance. A candidate answer must
classify real elements without merging any distinction that §7 forbids.

A fifth question is of a different order, and a reader MUST NOT confuse it with these: **whether the
six-category set is minimal**, or whether one pair could merge without loss. That is a question of
design quality, judged by GO-12. It is not a classification question. An ontology may be non-minimal
and entirely valid. Minimality is not a precondition of conformance and never becomes one.

## 11. Normative invariants

- **GO-1.** Every element MUST have exactly one primary semantic category (§3).
- **GO-2.** Every semantic element MUST have exactly one provenance — authored, derived, or produced
  — describing how that element came into existence. Later representations or materializations
  MUST NOT change it (§6).
- **GO-3.** A kind MUST declare its semantic category and any provenance constraint its kind
  contract imposes. An element's provenance MUST be established explicitly, and neither category
  nor provenance MUST be inferred from an artifact's name, location, or content (§8).
- **GO-4.** A secondary relationship MUST NOT alter, extend, or make ambiguous an element's primary
  category (§5).
- **GO-5.** No element's declarations may violate its category contract (§4).
- **GO-6.** An evidential element MUST NOT be referenced as a source of authority (§4.1).
- **GO-7.** A participatory element MUST NOT carry behavior, and its identity MUST NOT constitute
  authority (§4.1).
- **GO-8.** An operational element MUST NOT be a source of authority (§4.1).
- **GO-9.** Derived and produced elements MUST NOT be sources of governance authority. They MUST
  carry provenance identifying their source or producing operation (§6).
- **GO-10.** A semantic category MUST NOT establish, extend, or limit what an element governs (§1,
  §7.2).
- **GO-11.** Authority, concern, federation, and namespace MUST NOT be encoded in a single
  identifier (§7.2).
- **GO-12.** Admitting a new kind MUST NOT require an ontology revision (§9).

## 12. Conformance

The conformance subject of this document is a **classification**: the assignment of categories and
provenance to the kinds of a governance universe, together with the category contracts they inherit.

A classification conforms when all of the following hold:

- Every kind declares exactly one category and one provenance (GO-1, GO-2, GO-3).
- No artifact's declarations violate the category contract its kind inherits (GO-5).
- The authority-bearing prohibitions hold. Evidential, operational, derived and produced elements
  are not sources of authority, and identity is not authority (GO-6 … GO-9).
- No category is relied on to establish what an element governs (GO-10).
- The four partitioning concepts remain separately expressible (GO-11).

A classification that satisfies all of these may still be a poor ontology. Its categories may be
drawn too finely, or its contracts may carry obligations that belong to a single kind. That is a
question of design quality, judged by GO-12. It is not a conformance question.
