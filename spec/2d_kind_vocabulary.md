# Kind Vocabulary

## 1. Scope

This document defines what a **kind vocabulary** is. It covers three things:

- the declared, closed set of artifact kinds that a governed system admits;
- the authority that constitutes that set;
- the act by which the set changes.

This document specifies the vocabulary *mechanism*. It does not enumerate kinds. A system's profile
decides which kinds that system admits. This family does not. A family that named its kinds would
admit exactly one platform. PGC admits as many platforms as there are profiles.

The Machine Block Standard governs the surface on which a kind is declared, and requires every block
to carry exactly one kind. The Governance Semantic Ontology covers what role the elements a kind
represents play. This document establishes what makes a kind *exist* for a system, and what it takes
to change that.

This document introduces the terms **kind vocabulary**, **kind registry**, and **vocabulary
revision**. The Conceptual Model, the Governance Semantic Ontology or the Machine Block Standard
defines every other term it uses.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What a kind vocabulary is

A **kind vocabulary** is the declared set of artifact kinds admissible in a governed system, closed
within a revision of that vocabulary.

A vocabulary exists because two requirements pull in opposite directions, and both must hold:

- **The declaration language must stay open.** A system can then admit new kinds, including kinds a
  domain introduces, without amending the substrate (MB-14) or the ontology (GO-12).
- **The admissible set must be closed.** An unrecognized kind is then a refusal, not an unexamined
  passenger. Any party can then know what a system may declare.

The vocabulary reconciles the two. The language is open, and a vocabulary is a closed selection over
it. So admitting a kind is a governed act with a determination. It is not a consequence of something
appearing.

## 3. Four roles, kept apart

A kind, its admission, its contract and its resolution are four different things. Merging any two of
them puts the authority for what may exist in the wrong place:

| | Establishes | Held by |
|---|---|---|
| **kind** | a semantic classification of representations | the classification itself |
| **vocabulary** | that this kind is admissible in this system | a declared vocabulary |
| **registry** | which contract governs declarations of that kind | a declared kind registry |
| **resolution** | applying the contract to an artifact | construction |

A **kind registry** is the declared binding of admitted kinds to the contracts governing their
declarations. The vocabulary settles which kinds exist. The registry settles which contract applies
to each kind.

Three consequences are normative:

- **A registry does not invent kinds.** It associates a contract with a kind the vocabulary has
  already admitted. A kind that appears in a registry and not in the vocabulary is a defect in the
  registry. It is not an admission.
- **A mechanism is never the authority for the vocabulary.** Whatever resolves a kind to its
  contract acts under the vocabulary's authority and never constitutes the vocabulary. A kind that
  exists because some mechanism recognizes it is a kind nobody declared.
- **A contract does not constitute a kind.** The existence of a kind and the rules governing its
  declarations are separate facts. A kind may be admitted before its contract is complete only if the
  vocabulary says so. A system must never read the contract's absence as permission.

## 4. The discriminator

- Every machine block declares exactly one artifact kind. That kind is its **authoritative
  discriminator** (MB-8).
- The declared value MUST be **self-describing**: the canonical name of the kind. It MUST NOT be an
  abbreviation, a prefix, a positional convention, or an implementation-local symbol.
- There MUST be exactly one discriminator. Suppose a system carries two: a canonical value and a
  parallel element that also names a kind. It then has two answers to what an artifact is. Any rule
  for which one wins would be a mechanism deciding semantics.
- A naming convention over identifiers MAY reflect a kind. **Nothing may derive a kind from it**
  (MB-6, GO-3). A convention that someone reads as a classification has become a classification. The
  identifier is then two things at once. GO-11 forbids that same failure in a different register.

## 5. Closure

**A kind vocabulary is closed within its revision.** A kind absent from the vocabulary that applies to
an artifact is an **unregistered kind** and MUST be refused (MB-9).

Closure makes the vocabulary meaningful. An open vocabulary tolerates, defaults or passes through an
unrecognized kind. It then cannot tell apart three cases:

- a kind that was never declared;
- a kind that was declared elsewhere;
- a kind introduced by something that should not have been able to introduce it.

All three arrive looking identical.

So refusal on an unrecognized kind is not strictness. Only under refusal does the vocabulary state a
fact about the system, rather than about what the system happened to encounter.

### 5.1 Closure states what each kind admits, not only which kinds

A closed vocabulary answers *which kinds may be used*. It does not, alone, answer *what each of them
may omit*. A small vocabulary can be as permissive as a large one on that second question.

**A declared vocabulary MUST state, for each kind it admits, whether that kind's ordinary admission
requires a governance assertion** (MB-10). This disposition belongs with the vocabulary. A party
reading the vocabulary decides there what admitting a kind commits them to. A vocabulary may list
ten kinds and their categories and say nothing about their governance assertions. It has then
enumerated a taxonomy and skipped the question the taxonomy exists to settle.

The failure this rule closes is real, and it is not confined to realizations. Someone may narrow a
vocabulary until it admits very few kinds, one of which needs no governance assertion outside
genesis. The narrowing will be visible. The widening will not (Machine Block §8, Normative Platform
Profile §13). **Size is not the dimension that matters.**

## 6. Vocabulary revision

Adding, removing or altering the meaning of a kind is a **vocabulary revision**. It is a governed
transition like any other (SM-9), and it requires:

1. the kind's semantics: what it classifies, and what sets it apart from every kind already admitted;
2. its semantic category and any provenance constraints (Governance Semantic Ontology §8);
3. its kind contract (Machine Block §9);
4. its registration, binding kind to contract (§3);
5. a determination admitting the revision under the closure in force.

Two rules bound the act:

- **A vocabulary revision MUST NOT require amending this document, the Machine Block Standard, or
  the Governance Semantic Ontology.** Suppose a kind cannot be admitted without amending one of them.
  That reveals that the amended document carries semantics that belong to the kind.
- **Removing or redefining a kind invalidates every artifact declared under it.** It also
  invalidates every contract that references the kind, and every projection derived from those
  artifacts. A removal is not a subtraction. It changes what the system's existing declarations mean.

## 7. Aliases and normalization

A system may need to accept a declaration written against an earlier vocabulary or an external
convention. Where it does:

- An alias MAY be accepted at the point of admission and **MUST be normalized to the canonical kind
  before the artifact is treated as conformant.**
- A conforming system **MUST NOT carry an alias as the authoritative classification**, and MUST NOT
  emit one as the classification of a constructed artifact.
- An alias is a courtesy at a boundary, never a second vocabulary. Two names for one kind that both
  stay authoritative are two kinds that happen to agree. Eventually they will stop agreeing.

Each system chooses whether to accept aliases at all. If it does, normalization bounds that
acceptance.

## 8. Representation change is not semantic change

A system may bring an artifact into conformance with a vocabulary. It may restate the artifact's
classification in canonical form, or move it from a superseded discriminator to the current one.
That is a **representation change**.

**A representation change MUST NOT increment an artifact's declared version** unless the artifact's
declared semantics also change. Version identifies semantics (Conceptual Model, *version*). An
artifact that means exactly what it meant before has not become a new version by being written
differently.

A conforming system does regenerate everything derived from the normalized representation: canonical
projections, integrity values and attestations. These follow the canonical form (MB-3). So they
change when the representation changes, and they must. An integrity value computed over a superseded
representation attests to something no longer declared.

## 9. Where a vocabulary is declared

**A kind vocabulary belongs to a profile, not to this family.**

This document specifies what a vocabulary is and what governs its change. The enumeration, meaning
which kinds a system admits, is a selection over the open declaration language. Selection is what a
profile does (Open Standard, Part VI). Consequently:

- A conforming system MUST name the vocabulary it operates under, and that vocabulary MUST be
  declared.
- Two systems under different profiles MAY admit different kinds and both conform. Neither
  vocabulary is more canonical than the other.
- **No kind is required by this family.** If the family required every governed system to admit some
  particular kind, that kind would become part of the definition of governed computation. It is not.

A family that enumerated its kinds would have exactly one platform. It would decide by enumeration
what Part VI decides by profile.

## 10. Normative invariants

- **KV-1.** A governed system MUST operate under a declared kind vocabulary, and MUST name it (§9).
- **KV-2.** A kind vocabulary MUST be closed within its revision. An unrecognized kind MUST be
  refused (§5).
- **KV-3.** A kind MUST be admitted by its vocabulary. A registry, a contract, or a mechanism
  MUST NOT constitute a kind (§3).
- **KV-4.** A machine block MUST carry exactly one authoritative discriminator, whose value is the
  self-describing canonical kind name (§4).
- **KV-5.** A kind MUST NOT be derived from a prefix, a naming convention, a location, or any other
  positional signal (§4).
- **KV-6.** A vocabulary revision MUST be a governed transition, and MUST NOT require amending this
  document, the Machine Block Standard, or the Governance Semantic Ontology (§6).
- **KV-7.** An accepted alias MUST be normalized to the canonical kind before the artifact is treated
  as conformant. It MUST NOT be carried or emitted as the authoritative classification (§7).
- **KV-8.** A representation change MUST NOT increment an artifact's declared version (§8).
- **KV-9.** No particular kind MUST be required of a governed system by this family (§9).
- **KV-10.** A declared vocabulary MUST state, for each kind it admits, whether that kind's ordinary
  admission requires a governance assertion (§5.1, MB-10).

## 11. Conformance

The conformance subject of this document is a **vocabulary**: the declared set of kinds a governed
system admits, together with the registry that binds them to contracts.

A vocabulary conforms when all of the following hold:

- It is declared and named, and the system operating under it identifies it (KV-1).
- It is closed, and it refuses an unrecognized kind rather than tolerating it (KV-2).
- Every kind it admits has a semantic category, provenance constraints where its contract imposes
  them, a stated governance-assertion disposition (KV-10), and a contract bound in the registry (§6).
- Every kind in the registry is also in the vocabulary (KV-3).
- What each admitted kind classifies sets it apart from every other kind. Naming convention does not
  (KV-5).
- Any alias it accepts normalizes at admission (KV-7).

A vocabulary may conform and still be poorly chosen. Its kinds may be drawn too finely, or two kinds
may differ in name and not in what they classify. That is a question of design quality. The test is
whether admitting the next kind requires amending anything above it (KV-6). It is not a conformance
question.
