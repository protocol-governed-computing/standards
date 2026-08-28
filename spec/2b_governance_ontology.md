# Governance Semantic Ontology

## 1. Scope

This document defines the closed classification of **semantic roles** played by the elements of
a governance universe, and the obligations each role carries.

It answers one question — *what role does this element play in the governed system?* — and
deliberately answers no other. In particular it does not answer *what type of artifact is this?*
(the Kind Vocabulary), *what may this artifact declare?* (the Machine Block Standard), *by what
right does this govern that?* (Governance Closure & Authority), or *what happens when governance
is evaluated?* (Enforcement & Refusal).

**This ontology is subordinate to the Governance Standard.** It classifies elements whose
governance semantics that document has already specified. It establishes no authority, no scope, no
admission, and no enforcement. An ontology that determined any of those would be a second,
undeclared governance layer, and its classifications would silently become permissions.

Its value is a small vocabulary, closed within each revision, in which cross-cutting obligations
can be stated once per role rather than re-declared per kind.

### 1.1 Closed is not a ceiling

**"Closed" constrains the set of *roles*, not the set of systems.** It means that within one
revision the categories are settled, so that classification cannot be widened quietly and an
obligation stated per category cannot be escaped by inventing a category. It does not mean the
ontology describes only simple systems, and it is not a limit on what may be governed.

Everything a more complex governed system needs is admitted as **kinds**, which are open:
signing and attestation authorities, distributed and multi-node execution, replicated or
partitioned state, cross-organizational federation, delegated and revocable authority, sealed
transport between authorities, external attestors. Each of these introduces elements that *define*
something, *require* something, *expose* something, *do* something, *act*, or *record* — and each
is therefore classified by naming which existing role it occupies. GO-12 is the test that this
remains true: if admitting such a kind forced a new category, the categories were drawn around
the kinds that happened to exist rather than around the roles that exist.

A genuinely new *role* — a way of participating in governance that none of the six describes —
is possible, and is handled by ontology revision (§9). That is a defined procedure with stated
consequences, not a wall. What the closure prevents is a new category arriving by accident,
which is how a classification stops being able to carry obligations.

Nothing in this document is scoped to a particular deployment shape, trust model, or number of
authorities.

This document introduces the terms **governance universe**, **semantic category**, and **category
contract**, and refines the Conceptual Model's **provenance**. Every other term it uses is defined
by the Conceptual Model or the Governance Standard.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What is classified

### 2.1 Element, artifact, kind

Three things are routinely conflated, and the ontology is unusable if they are:

| | What it is | Classified by |
|---|---|---|
| **Element** | a semantic object of the governance universe | this ontology |
| **Artifact** | a representation of an element | the Kind Vocabulary |
| **Artifact kind** | the taxonomy of representations | the Kind Vocabulary |

**This document classifies elements.** Artifacts represent them; kinds classify the
representations. Category is a property of the *semantic element*; a kind **declares** the
primary semantic category of the elements it represents. The category is not a kind and a kind
is not a category — a classification that migrated from ontology to taxonomy would make the role
an element plays a consequence of how it happens to be written down.

### 2.2 The governance universe

The **governance universe** is the bounded semantic domain comprising the entities,
declarations, authorities, behaviors, participants, and evidence that are subject to,
participate in, or are produced by the governance of a system.

The universe is wider than the set of governing elements. Behavior that is governed, and
evidence that records what occurred, are elements of the universe without governing anything.
**Classification is therefore not a statement that an element governs** — most elements do not.
Only elements the Governance Standard's relation makes governing elements govern, and their
category does not make them so.

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

Many kinds may share one category; a kind has exactly one. The vocabulary of kinds is open so
that new kinds may be admitted; the ontology is closed so that admitting them changes nothing
about what roles exist.

## 3. The primary dimension — semantic category

Every element of a governance universe has exactly **one primary semantic category**. In
architectural prose the categories are the *governance strata* of a system; *stratum* expresses
separation, not rank — a participant is not above or below a behavior.

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
  categories, but MUST NOT make its primary classification ambiguous. Classification stays
  single-valued; the model does not force an element to be split because it relates outward.
- **Closed within a revision.** A new kind — including a domain kind — is admitted by naming
  which existing category it occupies. Adding a kind does not add a category. Adding a category
  is an ontology revision (§9).
- **Category is not status.** The six are roles, not ranks, and the ontology asserts no ordering
  among them.

## 4. Category contracts

A category is a name; a **category contract** is what the name entails. Each category carries
one, and it is where the ontology does its work: an obligation stated in a category contract is
stated once and binds every kind in that category, rather than being re-declared per kind and
diverging.

A category contract states the category's semantic meaning, its relationship to authority, the
dependencies its members may have, and its category invariants.

### 4.1 Category invariants

- **Definitional** — MUST be resolvable before anything that references it is determined.
  Referenced by other categories; depends on none.
- **Normative** — MUST be governed by a constitutive authority. A normative element MAY be
  *informed* by evidence, but evidence MUST NOT thereby become a source of its authority.
- **Contractual** — MUST declare a closed interface. Binds operational elements to the normative
  obligations that constrain them.
- **Operational** — MUST be governed by a norm, and MUST satisfy the applicable contractual
  requirements governing its exposed behavior. MUST NOT be a source of authority. All exposed
  operational behavior is contract-bound; the requirement is on the behavior being governed by a
  contract, not on each operational element having a separately instantiated one.
- **Participatory** — MUST carry declared identity, with identity held separate from authority.
  MUST NOT carry behavior.
- **Evidential** — append-only. MUST NOT be referenced as authority: evidence records what
  occurred, and what occurred does not thereby become what must hold.

Two of these deserve emphasis, because both are violated by systems that appear well governed:

**Evidence does not govern.** A system that derives a rule from what has happened has made its
past into its authority, and can no longer distinguish what it is required to do from what it
happens to have done.

**Identity is not authority.** A participatory element names who acts; what they may do comes
from a normative element that says so. Collapsing the two makes every identity a permission.

### 4.2 Runtime disposition

Disposition is a property of the category contract, not of the category itself — it says how
elements of the category stand with respect to execution:

| Category | Disposition |
|---|---|
| Definitional | not executable |
| Normative | not executable |
| Contractual | not independently executable |
| Operational | executable |
| Participatory | may participate in execution through an operational element |
| Evidential | produced by execution |

Only **Operational** elements enter execution as behavior. That this is a single category is not
a convenience; it is what makes the space of things that can happen enumerable.

## 5. Secondary relationships

The primary category answers what an element *is*. Secondary relationships answer what it
*governs, exposes, constrains, or produces*. An element may relate into other categories without
its primary classification changing:

```
a capability contract
  primary category:  Contractual
  relationships:
      governed by  →  Normative
      constrains   →  Operational
      exposes      →  Operational
```

Relationships are how categories compose into a system; the primary category is how each element
is classified. The two MUST NOT be conflated — an element that *constrains* operational elements
is not thereby operational, and an element *governed by* a norm is not thereby normative.

## 6. The second dimension — provenance

Orthogonal to category, and not derivable from it: how the element came to exist.

| Provenance | Definition |
|---|---|
| **authored** | created as a source declaration, independently governed |
| **derived** | synthesized deterministically from one or more declarations |
| **produced** | arising as a consequence of execution or system operation |

*Refining the Conceptual Model's* **provenance**: within the ontology, provenance is the **origin
relation of a semantic element**, not a lifecycle state and not a property of any one
representation of it. It records how that element came into existence, and it
is settled at that moment.

**Subsequent representations do not change it.** One semantic element may have source,
constructed, runtime, and evidence representations; an authored element that is later
materialized, projected, or indexed remains authored. A representation being computed does not
make the element derived — what was derived is that representation, not the element it carries.
Reading provenance off a representation is the error this axis exists to prevent.

Two obligations attach:

- **Derived and produced elements MUST NOT become sources of governance authority** by virtue of
  having been derived or produced. Being computed is not being authorized.
- **Derived and produced elements MUST carry provenance sufficient to identify their source or
  producing operation**, and MUST NOT be admitted as independent authoritative source
  declarations.

Provenance is a separate axis because it is not recoverable from category: an element derived
from a norm and the norm it was derived from occupy the same category and differ in what may be
done with them.

## 7. What is not an ontology axis

### 7.1 Rejected axes

Governance *function*, execution *phase*, authority *level*, and *lifecycle* are not independent
ontology axes. Each is either the category restated as a verb, or a property of a category
contract. Modelling any of them as ontology multiplies the classification without adding a
distinction.

### 7.2 What partitions a universe is not what classifies its elements

Four concepts describe how a governance universe is *organized or related*. They are not roles,
they do not classify elements, and they are independent of both dimensions above:

| | Answers | Is not |
|---|---|---|
| **Authority** | who may decide | a category, and not derivable from one |
| **Concern** | what is being decided about | authority — a concern may be organized and governed with no authority constituted over it |
| **Federation** | how distinct authorities coexist, delegate, and bound one another | a property of any single authority |
| **Namespace** | how identity is carried and resolved | a claim of authority, concern, or federation |

**Authority ≠ Concern ≠ Federation ≠ Namespace.** A representation that encodes more than one of
these in a single identifier makes them indistinguishable to any check, and the distinctions
become unenforceable however plainly they are declared elsewhere.

An element has a category and a provenance; it also falls under some authority and concerns some
subject, and none of the four is recoverable from the others. **The semantics of authority,
concern, and federation belong to the Governance Standard and to Governance Closure & Authority.**
This document specifies only that they are not ontology axes, and that classification never supplies
them.

This revision treats federation as a **relation among authorities** rather than as a governed
subject an authority owns. That treatment is not settled (§10): if federation were a subject, it
would need a classification, and the question of whether it has one is precisely the question of
whether it is a subject.

## 8. Relationship to artifact kind

- Each artifact kind declares the **semantic category** of the elements it represents, and —
  where its kind contract constrains provenance — the provenance values permitted for that kind.
  Category follows from the kind; provenance does not always, because the same kind may represent
  elements of differing origin. The **provenance of an individual element MUST be established
  explicitly** and MUST NOT be inferred from an artifact's name, location, or content.
- Because the ontology is closed and the vocabulary of kinds is open, a new kind is classified
  purely by naming its category. **No ontology change is required to admit a new kind.**
- A kind's category MUST be consistent with what its kind contract requires it to declare. The
  category contract states what is expected *where applicable*; it does not require every kind
  in a category to expose an identical declaration surface.

## 9. Extension

Admitting a **kind** requires naming the category it occupies and the provenance it carries.
Nothing in this document changes.

Adding, removing, or merging a **category** is an ontology revision. It MUST be deliberate, and
it invalidates every category contract, kind classification, and cross-cutting obligation stated
in terms of the affected category. A revision is not an addition.

The design criterion is therefore not whether the ontology describes today's elements elegantly.
It is whether **admitting a genuinely new kind requires changing the ontology**. If it does not,
the ontology is at the right level of abstraction; if it does, the categories have been drawn
around the kinds that happened to exist.

## 10. What this ontology does not specify

Four classification questions are deliberately left open in this revision. They are recorded
because a document that silently assumed answers to them would foreclose them:

- **Whether Evidential is a peer category.** *Definitional* through *Participatory* describe the
  semantic role of a declaration; *Evidential* describes a record's relationship to execution.
  This revision treats it as a peer category; whether it is instead an orthogonal produced-state
  dimension is unresolved.
- **Whether provenance remains an independent axis** or folds into the kind contract. It is
  retained as an axis because it is not reducible to category.
- **Whether Participatory is primary** or a sub-role of normative authority.
- **Whether federation is a relation or a governed subject.** §7.2 treats it as a relation among
  authorities, which is why it receives no category. Were it a subject an authority owns, it
  would require one, and the ontology would need to say which. The two possibilities are not
  stylistic: a relation cannot be classified, and a subject must be.

Each is resolved by demonstrating that a candidate answer classifies real elements without
collapsing a distinction §7 forbids — not by argument about which is more elegant.

A fifth question is of a different order and MUST NOT be confused with these: **whether the
six-category set is minimal**, or whether one pair merges without loss. That is a question of
design quality, judged by GO-12, and it is not a classification question. An ontology may be
non-minimal and entirely valid; minimality is not a precondition of conformance and never
becomes one.

## 11. Normative invariants

- **GO-1.** Every element MUST have exactly one primary semantic category (§3).
- **GO-2.** Every semantic element MUST have exactly one provenance — authored, derived, or
  produced — describing how that element came into existence. Subsequent representations or
  materializations MUST NOT change it (§6).
- **GO-3.** A kind MUST declare its semantic category and any provenance constraint its kind
  contract imposes. An element's provenance MUST be established explicitly, and neither category
  nor provenance MUST be inferred from an artifact's name, location, or content (§8).
- **GO-4.** A secondary relationship MUST NOT alter, extend, or make ambiguous an element's
  primary category (§5).
- **GO-5.** No element's declarations may violate its category contract (§4).
- **GO-6.** An evidential element MUST NOT be referenced as a source of authority (§4.1).
- **GO-7.** A participatory element MUST NOT carry behavior, and its identity MUST NOT
  constitute authority (§4.1).
- **GO-8.** An operational element MUST NOT be a source of authority (§4.1).
- **GO-9.** Derived and produced elements MUST NOT be sources of governance authority, and MUST
  carry provenance identifying their source or producing operation (§6).
- **GO-10.** A semantic category MUST NOT establish, extend, or limit what an element governs
  (§1, §7.2).
- **GO-11.** Authority, concern, federation, and namespace MUST NOT be encoded in a single
  identifier (§7.2).
- **GO-12.** Admitting a new kind MUST NOT require an ontology revision (§9).

## 12. Conformance

The conformance subject of this document is a **classification**: the assignment of categories
and provenance to the kinds of a governance universe, together with the category contracts they
inherit.

A classification conforms when:

- every kind declares exactly one category and one provenance (GO-1, GO-2, GO-3);
- no artifact's declarations violate the category contract its kind inherits (GO-5);
- the authority-bearing prohibitions hold — evidential, operational, derived, and produced
  elements are not sources of authority, and identity is not authority (GO-6 … GO-9);
- no category is relied on to establish what an element governs (GO-10); and
- the four partitioning concepts remain separately expressible (GO-11).

A classification that satisfies all of these may still be a poor ontology — categories drawn too
finely, or contracts carrying obligations that belong to a single kind. That is a question of
design quality, judged by GO-12, and it is not a conformance question.
