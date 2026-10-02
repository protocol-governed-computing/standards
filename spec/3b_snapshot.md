# Snapshot

## 1. Scope

This document specifies the **snapshot**: the sealed, complete, content-identified representation of
a governed system that execution consumes as its governed representation. It also specifies the
conditions under which a snapshot may be accepted.

This document treats a snapshot as a **portable governed artifact**, not as the output of any
particular mechanism. Governed Construction covers what produces a snapshot. The Execution Model
and the Runtime Standard cover what consumes one. This document says three things:

- what a snapshot *is*;
- what it must carry;
- what must be true before anything executes against it.

Adjacent subjects belong to other documents. This document references them and does not restate
them:

- the Projection Standard owns what a projection is and what makes one faithful;
- Identity & Addressing owns how identity is structured and resolved;
- Evidence, Attestation & Provenance owns what an attestation asserts.

This document introduces the terms **constituent**, **self-description**, **execution closure**,
and **acceptance**, and refines the Conceptual Model's **snapshot**. The Conceptual Model, the
Semantic Model or Part II defines every other term it uses.

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

A **constituent** is anything the snapshot carries as part of itself: a projection of a
declaration, an index over those projections, an integrity value, a provenance record, or the
self-description. The snapshot's identity covers every constituent.

**A snapshot is the baseline of the system it represents.** It is what the system currently *is*
(Conceptual Model, *baseline*), and it is the subject that a transformation transforms.

## 3. Sealing

**Sealing** is the act that constitutes a snapshot. It makes the representation immutable and
derives its identity from its content.

- Before sealing, there is a representation under construction. After sealing, there is a snapshot.
  The act is the boundary, not a location or a stage.
- **A sealed snapshot MUST NOT change.** There is no amendment, no patch, no append and no
  correction. A representation that changed after sealing was not sealed.
- **Any change produces a different snapshot**, with a different identity (§4). The two are not two
  versions of one artifact. They are two artifacts.

**This document leaves open when sealing occurs.** A realization may seal long before execution,
just before it, or when an interaction is admitted. This document requires an order: execution
consumes something already sealed and already verified (§7). The sealing must have happened. When it
happened does not matter.

## 4. Identity

**A snapshot's identity is derived from its content and never assigned** (AI-9).

- Two snapshots bearing the same identity MUST have identical content.
- Any difference in content MUST produce a different identity.
- An identity MUST NOT be allocated, reserved, chosen, or carried forward from a predecessor.

Derived identity makes the other properties checkable. An assigned identity attests to whatever the
assigner intended. A derived identity attests to what is actually there, and anyone holding the
content can recompute it.

Identity & Addressing owns how an identity is structured, expressed and resolved. This document
requires only that identity be derived and total over the snapshot's constituents. Equivalent
representations of the same governed content may need to yield one identity. Whether and how they do
is a question for Identity & Addressing, together with the canonical-form rule of the Machine Block
Standard. Nothing here imposes a canonicalization scheme.

## 5. Completeness — execution closure

**A snapshot has execution closure: everything required to execute is present within it.**

Execution closure concerns **governed behavior and declared dependencies**. It does not concern the
physical substrate on which a conforming agent performs execution. Compute, storage, scheduling and
network availability are properties of an environment. A snapshot does not carry them as
constituents. If they are missing, the environment has failed. The snapshot is not incomplete.

At execution time, nothing is fetched, resolved, discovered, downloaded, inherited from an
environment, or supplied by an agent. If execution needs something, it is in the snapshot. If it is
not in the snapshot, execution does not need it, and reaching for it is a refusal (AI-12).

This property makes every other execution guarantee possible:

- determinism, because only the snapshot and the inputs can vary;
- replay, because reproducing an execution requires the snapshot, not an environment;
- portability, because what travels carries its behavior with it;
- verifiability, because anyone can examine what a system can do without running it.

**Completeness is a property of the snapshot, not of the environment it happens to run in.** Suppose
a snapshot executes correctly because a particular agent supplies something the snapshot lacks. That
snapshot is not complete. It has an undeclared dependency, and the dependency is invisible exactly
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

- The enumeration MUST be total. A constituent present in the snapshot and absent from the
  self-description is undeclared content, and MUST be refused at acceptance.
- The self-description is itself a constituent, and the snapshot's identity covers it. Suppose the
  self-description sat outside the identity. It would not be part of what the snapshot identifies.
  The claims made about a snapshot could then change while its identity stayed the same, and every
  claim in it would be unfounded.
- **The claimed profile is not self-authored.** A snapshot claims evaluation against a profile it
  does not define. The profile states requirements from outside the system being represented
  (Semantic Model §11). A snapshot carries a claim. It does not determine that the claim holds. That
  determination is made about it, from outside. Without an externally authored profile, the claim
  would be a claim about itself.

**The integrity value over the whole MUST NOT cover itself.** A value computed over a set that
contains that value has no determinate result. Two realizations might resolve the circularity
differently. They would produce incompatible snapshots that both appear to conform. So a snapshot
declares **what the whole-integrity value covers**: a canonically determined set that excludes the
value itself. The exclusion is part of the declaration. It is not a property of whatever computed
the value.

This is a requirement on the declaration, not a choice of mechanism. This document does not specify
which function computes the value, how constituents are serialized, or how the set is ordered (§10).
It does require the covered set to be determinate and declared, and to exclude the value.

This document does not specify what form the self-description takes. It requires that the
self-description exists, is total, is covered by the identity, and declares what its integrity value
covers.

## 7. Verification and acceptance

**Acceptance** is the determination by which an execution agent takes a snapshot as its input.
Acceptance is a governed determination, not a load.

Before anything executes against a snapshot, all of the following MUST be established:

1. **Integrity.** Each constituent matches the integrity value the self-description carries for it.
2. **Identity.** The identity derived from the content matches the identity the snapshot bears.
3. **Totality.** Every constituent present is enumerated, and every constituent enumerated is
   present.
4. **Profile.** The accepting execution context conforms to the profile the snapshot claims.

**On any failure, the snapshot MUST be refused and nothing MUST execute against it.** There is no
partial acceptance, no acceptance with warnings, and no acceptance of the constituents that did
verify.

A snapshot that fails verification is not a damaged snapshot to work around. Nobody can establish
its relationship to what was constructed. Executing it would produce evidence attesting to a
determination that never happened.

## 8. The sole-input rule

**Only behavior present in the snapshot may enter execution.**

- The snapshot is the sole source of governed behavior for the executions performed against it.
- An agent MUST NOT supplement it: not with configuration, not with defaults, not with anything found
  in an environment, and not with anything carried over from a previously accepted snapshot.
- Interactions and their payloads are inputs to execution, not sources of behavior. **An interaction
  may select among declared alternatives. It MUST NOT introduce one.** It selects among what the
  snapshot already contains, and never extends it.

This is the execution-time face of AI-1. If behavior can enter from outside the snapshot, the
snapshot is no longer the authority. It has become a default that something else may override.

## 9. Portability and equivalence

A snapshot is a governed artifact, and it **travels**. It is bound neither to the mechanism that
produced it, nor to the agent that executes it, nor to the environment either one ran in.

- **The same snapshot, the same inputs and the same initial state produce the same governed
  consequences on any conforming agent** (SM-10, AI-9). Observations that are not governed
  consequences, such as timings and environmental measurements, may differ. The equivalence still
  holds.
- **A deployment decision changes where execution happens. It MUST NOT change what execution
  means.**

Suppose two agents execute one snapshot and reach different governed consequences. That establishes
that at least one of them does not conform. Derived identity and execution closure together make
this detectable. It is not a matter of opinion about implementations.

## 10. Change

**A snapshot changes by being replaced, never by being modified.**

A governed transformation produces the next snapshot from the current one (Semantic Model §10). That
act leaves the predecessor unchanged, exactly what it was. The successor supersedes it. Supersession
covers what becomes of references to the predecessor.

- **Correcting a snapshot means constructing another one.** There is no repair in place. A
  realization that offers one has an ungoverned path into what execution consumes.
- A snapshot's identity says nothing about its order relative to another. That one snapshot
  supersedes another is a declared relation. Nobody can derive it from their identities.

## 11. The first snapshot

The first snapshot of a system is constituted at genesis, from the empty governed state. Its closure
is composed from the proposal's declared governance and the profile it claims (Semantic Model §11).

It is a snapshot in every respect this document requires: sealed, complete, self-identifying,
self-describing and verifiable. **Genesis constrains where its closure came from. It relieves it of
nothing.** A first snapshot may not be accepted if it is incomplete, unverifiable, or self-certifying
against a profile it authored.

## 12. What a snapshot is not

People often mistake a snapshot for four other things. Each mistake has a consequence:

- **Not a build artifact.** It is a governed representation that construction happens to produce. If
  someone treats it as a build output, they assume rebuilding it is routine and its identity
  incidental.
- **Not a serialization of the source.** It contains projections of declarations. Those carry what
  the kind contracts project, not a copy of everything declared (MB-13). Nobody can recover a
  snapshot into its sources, and it is not meant to be recoverable.
- **Not a cache.** Nothing in it is a materialized convenience that could be recomputed if absent.
  Absence is not a miss to fill. It is incompleteness (§5).
- **Not a package.** Its constituents are not independently meaningful units to select among. A
  snapshot is accepted whole or refused whole (§7). **A constituent's presence grants no independent
  authority to consume, modify or replace it.**

## 13. What this document does not specify

- **How a snapshot is produced.** Governed Construction covers that. It permits one mechanism or
  several, ahead of time or on admission.
- **What its constituents look like.** The Projection Standard owns projections, indexes and their
  faithfulness.
- **What integrity mechanism is used.** Any mechanism is admissible that lets a party who did not
  build the snapshot detect a difference in content.
- **How identity is structured or resolved.** Identity & Addressing covers that.
- **What profiles exist.** A snapshot claims one. Part VI owns which profiles exist.

## 14. Normative invariants

- **SN-1.** A snapshot MUST be immutable from the moment of sealing. Any change MUST produce a
  different snapshot (§3).
- **SN-2.** A snapshot's identity MUST be derived from its content, MUST cover every constituent, and
  MUST NOT be assigned (§4).
- **SN-3.** Two snapshots bearing the same identity MUST have identical content (§4).
- **SN-4.** A snapshot MUST have execution closure: nothing required to execute may be obtained from
  outside it (§5).
- **SN-5.** A snapshot MUST carry a self-description enumerating its constituents, their integrity,
  its provenance, and the profile it claims (§6).
- **SN-6.** The self-description MUST be a constituent and MUST be covered by the snapshot's identity
  (§6).
- **SN-7.** The claimed profile MUST NOT be authored by the snapshot that claims it (§6, §11).
- **SN-8.** A snapshot MUST be verified for integrity, identity, totality, and claimed profile before
  anything executes against it (§7).
- **SN-9.** A snapshot that fails any acceptance check MUST be refused whole. Partial acceptance
  MUST NOT occur (§7).
- **SN-10.** No behavior MUST enter execution from outside the accepted snapshot (§8).
- **SN-11.** The same snapshot, inputs, and initial state MUST produce the same governed consequences
  on any conforming agent (§9).
- **SN-12.** A snapshot MUST NOT be modified in place. Change MUST proceed by constructing a successor
  (§10).
- **SN-13.** A first snapshot MUST satisfy every requirement above. Genesis MUST NOT relieve it of
  any (§11).
- **SN-14.** A snapshot MUST declare what its whole-integrity value covers, and that covered set
  MUST NOT contain the value itself (§6).

## 15. Conformance

The conformance subject of this document is a **snapshot**, together with the acceptance
determination made about it.

A snapshot conforms when two conditions hold:

- it is sealed, content-identified over every constituent, complete for execution, and
  self-describing in the terms §6 requires;
- the party accepting it can establish all four checks of §7 without access to whatever produced it.

**Successful execution is weak evidence of any of this.** The reason lies in snapshots, not in test
design. A snapshot with an undeclared environmental dependency executes successfully in the
environment that supplies the dependency. So a successful run does not show completeness. Behavior
where nothing supplies anything shows it. Likewise, a snapshot that verified does not show
verifiability. A corrupted or substituted constituent being refused shows it.

The Conformance Test Specification owns which demonstrations are required, how they are designed,
and how their results are evaluated. This document says what a snapshot must be.
