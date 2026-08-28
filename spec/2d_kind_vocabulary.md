# Kind Vocabulary

## 1. Scope

This document defines what a **kind vocabulary** is: the declared, closed set of artifact kinds
a governed system admits, the authority that constitutes it, and the act by which it changes.

It specifies the vocabulary *mechanism*. It does not enumerate kinds. Which kinds a particular
governed system admits is a property of that system's profile, not of this family — a family
that named its kinds would admit exactly one platform, and PGC admits as many as there are
profiles.

The Machine Block Standard governs the surface on which a kind is declared and requires that every
block carry exactly one; the Governance Semantic Ontology covers what role the elements a kind
represents play. This document establishes what makes a kind *exist* for a system, and what it takes
to change that.

This document introduces the terms **kind vocabulary**, **kind registry**, and **vocabulary
revision**. Every other term it uses is defined by the Conceptual Model, the Governance Semantic
Ontology, or the Machine Block Standard.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What a kind vocabulary is

A **kind vocabulary** is the declared set of artifact kinds admissible in a governed system,
closed within a revision of that vocabulary.

It exists because two requirements pull in opposite directions and both must hold:

- **The declaration language must stay open**, so that new kinds — including kinds a domain
  introduces — are admitted without amending the substrate (MB-14) or the ontology (GO-12).
- **The admissible set must be closed**, so that an unrecognized kind is a refusal rather than an
  unexamined passenger, and so that what a system may declare is knowable.

A vocabulary is what reconciles them: the language is open, and a vocabulary is a closed
selection over it. Admitting a kind is then a governed act with a determination, not a
consequence of something appearing.

## 3. Four roles, kept apart

A kind, its admission, its contract, and its resolution are four different things. Collapsing any
two of them puts the authority for what may exist in the wrong place:

| | Establishes | Held by |
|---|---|---|
| **kind** | a semantic classification of representations | the classification itself |
| **vocabulary** | that this kind is admissible in this system | a declared vocabulary |
| **registry** | which contract governs declarations of that kind | a declared kind registry |
| **resolution** | applying the contract to an artifact | construction |

A **kind registry** is the declared binding of admitted kinds to the contracts governing their
declarations. The vocabulary settles which kinds exist; the registry settles which contract applies
to each.

Three consequences are normative:

- **A registry does not invent kinds.** It associates a contract with a kind the vocabulary has
  already admitted. A kind appearing in a registry and not in the vocabulary is a defect in the
  registry, not an admission.
- **A mechanism is never the authority for the vocabulary.** Whatever resolves a kind to its
  contract does so under the vocabulary's authority and never constitutes it. A kind that exists
  because some mechanism recognizes it is a kind nobody declared.
- **A contract does not constitute a kind.** The existence of a kind and the rules governing its
  declarations are separate facts, and a kind may be admitted before its contract is complete
  only if the vocabulary says so — never by the contract's absence being read as permission.

## 4. The discriminator

- Every machine block declares exactly one artifact kind, which is its **authoritative
  discriminator** (MB-8).
- The declared value MUST be **self-describing**: the canonical name of the kind. It MUST NOT be
  an abbreviation, a prefix, a positional convention, or an implementation-local symbol.
- There MUST be exactly one discriminator. A system carrying two — a canonical value and a
  parallel kind-bearing element — has two answers to what an artifact is, and no rule about which
  wins that is not itself a mechanism deciding semantics.
- A naming convention over identifiers MAY reflect a kind. **Nothing may derive a kind from it**
  (MB-6, GO-3). A convention that is read as a classification has become a classification, and an
  identifier is then two things at once — which is the failure GO-11 forbids in a different
  register.

## 5. Closure

**A kind vocabulary is closed within its revision.** A kind not in the vocabulary applicable to
an artifact is an **unregistered kind** and MUST be refused (MB-9).

Closure is what makes the vocabulary meaningful. An open vocabulary — one where an unrecognized
kind is tolerated, defaulted, or passed through — cannot distinguish a kind that was never
declared from one that was declared elsewhere, from one that was introduced by something that
should not have been able to introduce it. All three arrive looking identical.

Refusal on an unrecognized kind is therefore not strictness. It is the only condition under which
the vocabulary states a fact about the system rather than about what happened to be encountered.

### 5.1 Closure states what each kind admits, not only which kinds

A closed vocabulary answers *which kinds may be used*. It does not, by itself, answer *what each of
them may omit* — and the second is where a small vocabulary can be as permissive as a large one.

**A declared vocabulary MUST state, for each kind it admits, whether a governance assertion is
required for that kind's ordinary admission** (MB-10). The disposition belongs with the vocabulary
because that is where a party reading the vocabulary decides what admitting a kind commits them to.
A vocabulary listing ten kinds and their categories, and saying nothing about their governance
assertions, has enumerated a taxonomy and left the question the taxonomy exists to settle.

The failure this closes is not hypothetical and is not confined to realizations: a vocabulary may be
narrowed until it admits very few kinds, one of which needs no governance assertion outside genesis,
and the narrowing will be visible while the widening is not (2c §8, 6a §13). **Size is not the
dimension that matters.**

## 6. Vocabulary revision

Adding, removing, or altering the meaning of a kind is a **vocabulary revision**. It is a
governed transition like any other (SM-9), and it requires:

1. the kind's semantics — what it classifies, and what distinguishes it from every kind already
   admitted;
2. its semantic category and any provenance constraints (Governance Semantic Ontology §8);
3. its kind contract (Machine Block §9);
4. its registration binding kind to contract (§3);
5. a determination admitting the revision under the closure in force.

Two rules bound the act:

- **A vocabulary revision MUST NOT require amending this document, the Machine Block Standard, or
  the Governance Semantic Ontology.** A kind that cannot be admitted without amending one of them
  has revealed that the amended document is carrying semantics that belong to the kind.
- **Removing or redefining a kind invalidates every artifact declared under it**, every contract
  that references it, and every projection derived from those artifacts. A removal is not a
  subtraction; it is a change to what the system's existing declarations mean.

## 7. Aliases and normalization

A system may need to accept a declaration written against an earlier vocabulary or an external
convention. Where it does:

- An alias MAY be accepted at the point of admission and **MUST be normalized to the canonical
  kind before the artifact is treated as conformant.**
- A conforming system **MUST NOT carry an alias as the authoritative classification**, and MUST
  NOT emit one as the classification of a constructed artifact.
- An alias is a courtesy at a boundary, never a second vocabulary. Two names for one kind that
  both remain authoritative are two kinds that happen to agree, and they will eventually stop
  agreeing.

Whether a system accepts aliases at all is its own choice; that acceptance is bounded by
normalization is not.

## 8. Representation change is not semantic change

Bringing an artifact into conformance with a vocabulary — restating its classification in the
canonical form, moving from a superseded discriminator to the current one — is a **representation
change**.

**A representation change MUST NOT increment an artifact's declared version** unless the
artifact's declared semantics also change. Version identifies semantics (Conceptual Model,
*version*); an artifact that means exactly what it meant before has not become a new version by
being written differently.

What a conforming system does regenerate from the normalized representation is everything derived
from it: canonical projections, integrity values, and attestations. Those follow the canonical
form (MB-3), so they change when the representation changes, and they must — an integrity value
computed over a superseded representation attests to something no longer declared.

## 9. Where a vocabulary is declared

**A kind vocabulary belongs to a profile, not to this family.**

This document specifies what a vocabulary is and what governs its change. The enumeration — which
kinds a system admits — is a selection over the open declaration language, and selection is what
a profile does (Open Standard, Part VI). Consequently:

- A conforming system MUST name the vocabulary it operates under, and that vocabulary MUST be
  declared.
- Two systems under different profiles MAY admit different kinds and both conform. Neither
  vocabulary is more canonical than the other.
- **No kind is required by this family.** A requirement that every governed system admit some
  particular kind would make that kind part of the definition of governed computation, which it
  is not.

A family that enumerated its kinds would have exactly one platform, and would have decided by
enumeration what Part VI decides by profile.

## 10. Normative invariants

- **KV-1.** A governed system MUST operate under a declared kind vocabulary, and MUST name it
  (§9).
- **KV-2.** A kind vocabulary MUST be closed within its revision; an unrecognized kind MUST be
  refused (§5).
- **KV-3.** A kind MUST be admitted by its vocabulary. A registry, a contract, or a mechanism
  MUST NOT constitute a kind (§3).
- **KV-4.** A machine block MUST carry exactly one authoritative discriminator, whose value is
  the self-describing canonical kind name (§4).
- **KV-5.** A kind MUST NOT be derived from a prefix, a naming convention, a location, or any
  other positional signal (§4).
- **KV-6.** A vocabulary revision MUST be a governed transition, and MUST NOT require amending
  this document, the Machine Block Standard, or the Governance Semantic Ontology (§6).
- **KV-7.** An accepted alias MUST be normalized to the canonical kind before the artifact is
  treated as conformant, and MUST NOT be carried or emitted as the authoritative classification
  (§7).
- **KV-8.** A representation change MUST NOT increment an artifact's declared version (§8).
- **KV-9.** No particular kind MUST be required of a governed system by this family (§9).
- **KV-10.** A declared vocabulary MUST state, for each kind it admits, whether a governance
  assertion is required for that kind's ordinary admission (§5.1, MB-10).

## 11. Conformance

The conformance subject of this document is a **vocabulary**: the declared set of kinds a
governed system admits, together with the registry binding them to contracts.

A vocabulary conforms when:

- it is declared and named, and the system operating under it identifies it (KV-1);
- it is closed, and an unrecognized kind is refused rather than tolerated (KV-2);
- every kind it admits has a semantic category, provenance constraints where its contract imposes
  them, a stated governance-assertion disposition (KV-10), and a contract bound in the registry
  (§6);
- no kind in the registry is absent from the vocabulary (KV-3);
- every admitted kind is distinguishable from every other by what it classifies, not by naming
  convention (KV-5); and
- any alias it accepts normalizes at admission (KV-7).

A vocabulary may conform and be poorly chosen — kinds drawn too finely, or two kinds that differ
in name and not in what they classify. That is a question of design quality, judged by whether
admitting the next kind requires amending anything above it (KV-6), and it is not a conformance
question.
