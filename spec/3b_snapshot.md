# Snapshot

## 1. Scope

This document specifies the **snapshot**: the sealed, complete, content-identified representation
of a governed system that execution consumes as its governed representation, and the conditions
under which it may be accepted.

A snapshot is treated here as a **portable governed artifact**, not as the output of any particular
mechanism. What produces one is the subject of Governed Construction; what consumes one is the
subject of the Execution Model and the Runtime Standard. This document says what a snapshot *is*,
what it must carry, and what must be true before anything executes against it.

Adjacent subjects belong elsewhere and are referenced, not restated: what a projection is and what
makes one faithful belong to the Projection Standard; how identity is structured and resolved
belongs to Identity & Addressing; what an attestation asserts belongs to Evidence, Attestation &
Provenance.

This document introduces the terms **constituent**, **self-description**, **execution closure**,
and **acceptance**, and refines the Conceptual Model's **snapshot**. Every other term it uses is
defined by the Conceptual Model, the Semantic Model, or Part II.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What a snapshot is

*Refining the Conceptual Model's* **snapshot**: a snapshot is a representation of a governed
system that is:

| Property | Meaning |
|---|---|
| **sealed** | immutable from the moment it is constituted (§3) |
| **complete** | everything required to execute is present in it (§5) |
| **self-identifying** | its identity is derived from its content (§4) |
| **self-describing** | it states what it contains and what it claims (§6) |
| **verifiable** | its integrity and identity can be checked by a party that did not build it (§7) |

A **constituent** is anything the snapshot carries as part of itself: a projection of a declaration,
an index over those projections, an integrity value, a provenance record, or the self-description.
Every constituent is covered by the snapshot's identity.

**A snapshot is the baseline of the system it represents.** It is what the system currently *is*
(Conceptual Model, *baseline*), and the subject that a transformation transforms.

## 3. Sealing

**Sealing** is the act that constitutes a snapshot: it renders the representation immutable and
derives its identity from its content.

- Before sealing there is a representation under construction; after sealing there is a snapshot.
  The boundary is the act, not a location or a stage.
- **A sealed snapshot MUST NOT change.** There is no amendment, no patch, no append, and no
  correction. A representation that changed after sealing was not sealed.
- **Changing anything produces a different snapshot**, with a different identity (§4). This is not
  a version relation between two states of one artifact; they are two artifacts.

**When sealing occurs is unconstrained.** A realization may seal long before execution, immediately
before it, or on admission of an interaction. What this document requires is the ordering: execution
consumes something already sealed and already verified (§7). That the sealing happened is required;
when it happened is not.

## 4. Identity

**A snapshot's identity is derived from its content and never assigned** (AI-9).

- Two snapshots bearing the same identity MUST have identical content.
- Any difference in content MUST produce a different identity.
- An identity MUST NOT be allocated, reserved, chosen, or carried forward from a predecessor.

Derived identity is what makes the other properties checkable. An assigned identity attests to
whatever the assigner intended; a derived identity attests to what is actually there, and can be
recomputed by anyone holding the content.

How an identity is structured, expressed, and resolved belongs to Identity & Addressing. This
document requires only that it be derived and total over the snapshot's constituents. Whether and
how equivalent representations of the same governed content are made to yield one identity is a
question for Identity & Addressing, together with the canonical-form rule of the Machine Block
Standard; nothing here imposes a canonicalization scheme.

## 5. Completeness — execution closure

**A snapshot has execution closure: everything required to execute is present within it.**

Execution closure concerns **governed behavior and declared dependencies**, not the physical
substrate on which a conforming agent performs execution. Compute, storage, scheduling, and network
availability are properties of an environment; they are not constituents a snapshot carries, and
their absence is a failure of the environment rather than an incompleteness of the snapshot.

Nothing is fetched, resolved, discovered, downloaded, inherited from an environment, or supplied by
an agent at execution time. If it is needed to execute, it is in the snapshot; if it is not in the
snapshot, it is not needed, and reaching for it is a refusal (AI-12).

This is the property that makes every other execution guarantee possible:

- determinism, because nothing can vary that is not in the snapshot or the inputs;
- replay, because reproducing an execution requires the snapshot rather than an environment;
- portability, because what travels carries its behavior with it;
- verifiability, because what a system can do is examinable without running it.

**Completeness is a property of the snapshot, not of the environment it happens to run in.** A
snapshot that executes correctly because a particular agent supplies something it lacks is not
complete; it is a snapshot with an undeclared dependency, and the dependency is invisible precisely
where it matters.

## 6. Self-description

A snapshot **states what it contains and what it claims**. Its self-description MUST carry:

| Carries | Establishing |
|---|---|
| **identity** | what this snapshot is (§4) |
| **constituents** | what it contains, enumerably |
| **integrity** | a value over each constituent, and over the whole |
| **provenance** | what it was derived from, and by what construction |
| **claimed profile** | the profile against which it claims evaluation |

- The enumeration MUST be total: a constituent present in the snapshot and absent from the
  self-description is undeclared content, and MUST be refused at acceptance.
- The self-description is itself a constituent and is covered by the snapshot's identity. A
  self-description outside the identity would not be part of what the snapshot identifies —
  allowing the claims made about a snapshot to change without the snapshot's identity changing,
  which would leave every claim in it unfounded.
- **The claimed profile is not self-authored.** A snapshot claims evaluation against a profile it
  does not define; the profile states requirements from outside the system being represented
  (Semantic Model §11). A snapshot carries a claim; it does not determine that the claim holds —
  that determination is made about it, from outside. Without an externally authored profile, the
  claim would be a claim about itself.

**The integrity value over the whole MUST NOT cover itself.** A value computed over a set that
contains that value has no determinate result, and two realizations resolving the circularity
differently produce incompatible snapshots that both appear to conform. A snapshot therefore
declares **what the whole-integrity value covers** — a canonically determined set from which the
value itself is excluded — and the exclusion is part of the declaration rather than a property of
whatever computed it.

This is a requirement on the declaration, not a choice of mechanism. Which function computes the
value, how constituents are serialized, and how the set is ordered are not specified here (§10);
that the covered set is determinate, declared, and does not contain the value, is.

What form the self-description takes is not specified here. That it exists, is total, is covered
by the identity, and declares what its integrity value covers, is.

## 7. Verification and acceptance

**Acceptance** is the determination by which an execution agent takes a snapshot as its input.
Acceptance is a governed determination, not a load.

Before anything executes against a snapshot, all of the following MUST be established:

1. **Integrity** — each constituent matches the integrity value the self-description carries for it.
2. **Identity** — the identity derived from the content matches the identity the snapshot bears.
3. **Totality** — every constituent present is enumerated, and every constituent enumerated is
   present.
4. **Profile** — the profile the snapshot claims is one for which the accepting execution context
   is conformant.

**On any failure, the snapshot MUST be refused and nothing MUST execute against it.** There is no
partial acceptance, no acceptance with warnings, and no acceptance of the constituents that did
verify.

A snapshot that fails verification is not a damaged snapshot to be worked around. It is a
representation whose relationship to what was constructed cannot be established — and executing it
would produce evidence attesting to a determination that never happened.

## 8. The sole-input rule

**No behavior may enter execution that was not present in the snapshot.**

- The snapshot is the sole source of governed behavior for the executions performed against it.
- An agent MUST NOT supplement it — not with configuration, not with defaults, not with anything
  found in an environment, not with anything carried over from a previously accepted snapshot.
- Interactions and their payloads are inputs to execution, not sources of behavior. **An
  interaction may select among declared alternatives; it MUST NOT introduce one.** It selects among
  what the snapshot already contains, and never extends it.

This is the execution-time face of AI-1. Where behavior can enter from outside the snapshot, the
snapshot has stopped being the authority and has become a default that something else may override.

## 9. Portability and equivalence

A snapshot is a governed artifact and **travels**. It is not bound to the mechanism that produced
it, the agent that executes it, or the environment either ran in.

- **The same snapshot, the same inputs, and the same initial state produce the same governed
  consequences on any conforming agent** (SM-10, AI-9). Observations that are not governed
  consequences — timings, environmental measurements — may differ without that equivalence failing.
- **A deployment decision changes where execution happens. It MUST NOT change what execution
  means.**

Two agents that execute one snapshot and reach different governed consequences have established
that at least one of them is not conforming — and that this is detectable, rather than a matter of
opinion about implementations, is a consequence of derived identity and execution closure together.

## 10. Change

**A snapshot changes by being replaced, never by being modified.**

A governed transformation produces the next snapshot from the current one (Semantic Model §10). The
predecessor is unchanged by that act and remains exactly what it was; the successor supersedes it,
and what becomes of references to the predecessor is the subject of supersession.

- **Correcting a snapshot means constructing another one.** There is no repair-in-place, and a
  realization that offers one has an ungoverned path into what execution consumes.
- A snapshot's identity says nothing about its ordering relative to another. That one snapshot
  supersedes another is a declared relation, not something derivable from their identities.

## 11. The first snapshot

The first snapshot of a system is constituted at genesis, from the empty governed state, under the
closure composed from the proposal's declared governance and the profile it claims (Semantic Model
§11).

It is a snapshot in every respect this document requires: sealed, complete, self-identifying,
self-describing, and verifiable. **Genesis constrains where its closure came from; it relieves it of
nothing.** A first snapshot that is incomplete, unverifiable, or self-certifying against a profile
it authored is not a snapshot that may be accepted.

## 12. What a snapshot is not

Four things it is routinely mistaken for, each mistake with a consequence:

- **Not a build artifact.** It is a governed representation that happens to be produced by
  construction. Treating it as a build output invites the assumption that rebuilding it is
  routine and that its identity is incidental.
- **Not a serialization of the source.** It contains projections of declarations, which carry what
  the kind contracts project — not a copy of everything declared (MB-13). A snapshot is not
  recoverable into its sources, and is not meant to be.
- **Not a cache.** Nothing in it is a materialized convenience that could be recomputed if absent.
  Absence is not a miss to be filled; it is incompleteness (§5).
- **Not a package.** Its constituents are not independently meaningful units to be selected among.
  A snapshot is accepted whole or refused whole (§7), and **a constituent's presence grants no
  independent authority to consume, modify, or replace it.**

## 13. What this document does not specify

- **How a snapshot is produced.** Governed Construction covers that, and permits one mechanism or
  several, ahead of time or on admission.
- **What its constituents look like.** Projections, indexes, and their faithfulness belong to the
  Projection Standard.
- **What integrity mechanism is used.** Any is admissible that lets a party who did not build the
  snapshot detect a difference in content.
- **How identity is structured or resolved.** Identity & Addressing covers that.
- **What profiles exist.** A snapshot claims one; which exist is Part VI's subject.

## 14. Normative invariants

- **SN-1.** A snapshot MUST be immutable from the moment of sealing; any change MUST produce a
  different snapshot (§3).
- **SN-2.** A snapshot's identity MUST be derived from its content, MUST cover every constituent,
  and MUST NOT be assigned (§4).
- **SN-3.** Two snapshots bearing the same identity MUST have identical content (§4).
- **SN-4.** A snapshot MUST have execution closure: nothing required to execute may be obtained
  from outside it (§5).
- **SN-5.** A snapshot MUST carry a self-description enumerating its constituents, their integrity,
  its provenance, and the profile it claims (§6).
- **SN-6.** The self-description MUST be a constituent and MUST be covered by the snapshot's
  identity (§6).
- **SN-7.** The claimed profile MUST NOT be authored by the snapshot that claims it (§6, §11).
- **SN-8.** A snapshot MUST be verified for integrity, identity, totality, and claimed profile
  before anything executes against it (§7).
- **SN-9.** A snapshot that fails any acceptance check MUST be refused whole; partial acceptance
  MUST NOT occur (§7).
- **SN-10.** No behavior MUST enter execution from outside the accepted snapshot (§8).
- **SN-11.** The same snapshot, inputs, and initial state MUST produce the same governed
  consequences on any conforming agent (§9).
- **SN-12.** A snapshot MUST NOT be modified in place; change MUST proceed by constructing a
  successor (§10).
- **SN-13.** A first snapshot MUST satisfy every requirement above; genesis MUST NOT relieve it of
  any (§11).
- **SN-14.** A snapshot MUST declare what its whole-integrity value covers, and that covered set
  MUST NOT contain the value itself (§6).

## 15. Conformance

The conformance subject of this document is a **snapshot**, together with the acceptance
determination made about it.

A snapshot conforms when it is sealed, content-identified over every constituent, complete for
execution, and self-describing in the terms §6 requires — and when the party accepting it can
establish all four of §7 without access to whatever produced it.

**Successful execution is weak evidence of any of this**, and the reason is a property of snapshots
rather than a matter of test design: a snapshot with an undeclared environmental dependency executes
successfully in the environment that supplies it. Completeness is therefore not observable from a
run that succeeded; it is observable from behavior where nothing supplies anything. Verifiability is
likewise not observable from a snapshot that verified, but from a corrupted or substituted
constituent being refused.

What demonstrations are required, how they are designed, and how their results are evaluated belong
to the Conformance Test Specification. This document says what a snapshot must be.
