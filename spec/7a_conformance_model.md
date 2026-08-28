# Conformance Model

## 1. Scope

This document specifies what it means to conform to this family: what a conformance claim is about,
what discharges it, what may be concluded from it, and what may not.

It opens Part VII. Every document before it states obligations and names the subject those
obligations bind. **This document does not restate them.** It specifies how a claim about any of
those subjects is made, what evidence discharges it, and how obligations of different kinds are
established by different means. The Conformance Test Specification specifies the demonstrations
themselves.

The division is exact and is the reason both documents exist:

```
Parts I–VI   what must be true of a subject          obligation
7a           what a claim is, and what discharges it  evaluation
7b           what demonstrations establish it         method
```

This document introduces the terms **conformance claim**, **claimant**, **evaluator**, **discharge**,
and **discharge class**.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. There is no unqualified conformance claim

**An unqualified statement of "PGC conformant" is not a conformance claim.** It names no subject, no
profile, and no revision, and there is nothing an evaluator could check.

A conformance claim MUST name:

| Names | Because without it |
|---|---|
| **a subject** | different subjects are discharged differently (§3) |
| **a profile** | the family leaves decisions open that a profile closes (NP-8) |
| **a revision** | obligations change between revisions of this family |
| **a claimant** | a claim is made by someone, and stands or falls with what they supplied |

A claim missing any of these is not a weaker claim. It is not a claim.

**The revision identifies the family obligations against which discharge is evaluated.** It does not
identify an implementation revision, a platform version, or a software release — those are facts
about the subject, not about what it was judged against.

## 3. Conformance subjects

**A conformance subject is what a claim is about.** The subjects differ in kind, and treating them
alike is the most common way a conformance regime becomes unfalsifiable — a claim about an
implementation discharged by evidence about an execution establishes nothing about either.

Each document of this family names the subject it evaluates. Those subjects group into seven
**conformance subject classes**:

| Class | Is | Evaluated by |
|---|---|---|
| **specification** | a document of this family | Conceptual Model, Semantic Model |
| **artifact** | a declaration and what it declares | Machine Block, Governance Ontology, Kind Vocabulary, Capability, Identity & Addressing |
| **governed representation** | something derived and carried | Snapshot, Projection, Evidence |
| **determination** | an act of deciding, and its result | Governance Closure & Authority, Execution Model, Governed Construction, Governed Transformation |
| **arrangement** | what a system says about itself structurally | Governance Standard, Enforcement & Refusal |
| **realization** | a built mechanism | Architectural Invariants, Runtime, Interaction Boundary, Governed Inspection |
| **profile** | a selection over the family | Normative Platform Profile, Execution Environment Profiles, Domain Profiles |

### 3.1 The system instance

An eighth subject is composite: **a system instance** — a governed system, composed under a named
profile, running.

A claim about a system instance is a claim about **all applicable subject classes represented in that
system**, and **it is discharged only by discharging each.** Not every system contains every class;
what a system does contain, it must discharge. **Which classes a system contains is a fact about the
system, established at claim time, not something its profile settles in advance** — a profile cannot
know what a system claiming it will be built from. A profile that enumerates subject classes states
a floor, and a claimant whose system contains more discharges more.

**That fact is read off the system, not asserted by the claimant.** The applicable set is determined
from the accepted snapshot's own self-description — whose constituent enumeration is required to be
total, and under which a constituent present and undeclared is refused at acceptance (SN-5, SN-8) —
together with the claimed profile. A claimant does not select the classes it will be evaluated on.

The reason is the one NP-12 states on the profile side, arriving here by a different door: **an
applicable set the constrained party enumerates is a claim defeatable by omission.** A claimant that
leaves a class out has not made a smaller claim honestly; it has made the largest claim available
while excluding the part it would fail, and nothing in the claim shows that it did. Deriving the set
from the sealed enumeration removes the choice — what the snapshot declares it contains is what must
be discharged, and a class present in the system and absent from that enumeration was already a
defect at acceptance rather than a narrowing of the claim.

A system instance claim is therefore never a shortcut:
it is the largest claim available and the most expensive to establish, and a claimant asserting one
without the constituent discharges has asserted a summary of work not done.

**An instance is bounded by the snapshot it accepted.** It begins at acceptance (RT-3) and ends when
another snapshot is accepted or the system stops; two snapshots are two instances, however
continuous the mechanism between them. Idleness does not end an instance, and a claim is about the
instance, not about any execution within it — a profile parameterizing anything over an instance's
lifetime (retention, for example) is parameterizing over that period and no other.

### 3.2 Subjects are not interchangeable

- **A discharge for one subject does not discharge another.** That a runtime conforms says nothing
  about the snapshots it accepts; that a snapshot conforms says nothing about any execution against
  it.
- **A claim MUST NOT be discharged by evidence about a different subject.** This is the failure the
  taxonomy exists to prevent, and it is usually accidental: an evaluator holding execution evidence
  concludes something about the implementation that produced it.

## 4. What discharges a claim

An **evaluator** is the party that determines whether a claim is discharged. Claimant and evaluator
are the two roles a claim stands between: the claimant makes the claim and supplies what supports
it, and the evaluator judges what that supports.

A claim is **discharged** when an evaluator, using the evidence and representations the claimant
supplied, establishes that the subject satisfies the obligations binding it.

Three properties of discharge are normative:

- **The evaluator need not trust the claimant** (EV-16). Discharge rests on what can be established,
  not on what is asserted. Where an evaluator must accept an assertion rather than establish it,
  that reliance is an attestation and MUST be visible as one (EV-9).
- **The evaluator need not have observed the subject.** Everything required is carried by evidence,
  by the representation, or by what can be re-derived from them.
- **Discharge is against a stated revision and profile.** An obligation that changed between
  revisions was discharged against the one claimed, and remains discharged against that one only.

## 5. Conformance is over guarantees, not similarity

**Conformance is established over observable semantic guarantees, never over resemblance to any
implementation.**

- Two conforming realizations may share no code, no language, no architecture, and no vocabulary
  beyond this family's.
- **Resembling a reference realization establishes nothing**, and a conformance regime that tests
  for such resemblance tests a choice rather than a property (1c §2.2).
- Conversely, **a realization that resembles a conforming one is not thereby conforming.** The
  property is what was established, not what it looks like.

## 6. How obligations become evaluations

Each document states obligations; this document specifies how an evaluation is derived from them.
**The derivation adds nothing and removes nothing** — it restates an obligation as the question an
evaluator asks.

| Document states | Evaluation asks |
|---|---|
| *a runtime consumes only an accepted snapshot, an interaction, and governed state* (RT-2) | what did it consume, and what establishes that nothing else reached it? |
| *a construction produces nothing on refusal* (GC-6) | what did a refused construction leave behind? |
| *evidence distinguishes determinative from observational content* (EV-5) | which content is declared determinative, and is it identical across the same determination? |

**An obligation with no derivable evaluation is a defect in the obligation** (EN-1). If nothing an
evaluator could examine would distinguish a subject satisfying it from one not, the obligation
constrains nothing, and the finding belongs against the document that states it.

## 7. Discharge classes

Obligations are not all established the same way, and **the most consequential thing this document
specifies is which are established how.** An evaluator applying the wrong class reaches a confident
conclusion that establishes nothing.

### 7.1 Observational

**Established by observing what a subject did.** The subject is exercised; the behavior is compared
against the obligation.

Suitable for obligations about what happens: that a refusal occurred and reported its grounds
(EN-8), that an unrouted outcome refused (EX-5), that acceptance preceded execution (RT-3).

**Limit:** observation establishes what happened, never what could not happen (§8).

### 7.2 Structural

**Established by examining a subject for the absence of a path.** Nothing is run; the representation,
the declarations, or the realization are examined for whether something is reachable at all.

Required for every obligation of the form *X cannot occur*:

| Obligation | What must be shown absent |
|---|---|
| a non-effecting capability produces no effect (CP-7) | any path, direct or transitive, from realization to effect |
| inspection introduces no execution (IN-2) | any path from a read operation to an executable target |
| no ungoverned read path exists (IN-13) | any reach into system contents outside a declared read operation |
| a runtime exposes no extension point for domain behavior (RT-11) | any admitted path by which behavior enters |

**Observation cannot substitute.** A non-effecting declaration is satisfied on every run in which the
effect path is not taken, so no number of successful runs establishes it.

### 7.3 Comparative

**Established by substitution** — varying something that must not matter and comparing governed
consequences.

| Obligation | Substitute |
|---|---|
| replacing a conforming runtime changes no governed consequence (RT-12) | a second runtime |
| a boundary is protocol-neutral (5a §16) | a second external protocol |
| governed consequences do not vary with environment (EE-6) | a second environment |
| construction is reproducible (GC-9) | a different time, place, and party |
| a caller does not derive (5b §16) | a second, independently written client |

**A subject exercised in only one configuration has not been comparatively discharged**, however
thoroughly that configuration was tested. This is why a realization supporting one protocol, one
environment, or one runtime has not established the properties those obligations name.

### 7.4 Derivational

**Established by re-deriving from what was supplied** and comparing with what was recorded.

| Obligation | Re-derive |
|---|---|
| a determination was the correct determination (SM-12, 1b §14) | the determination, from the closure and rules the evidence carries |
| the path taken was in the sealed representation (EX-15) | the path, against the representation |
| a projection is faithful (PJ-4, PJ-9) | the projection, from its source |
| a snapshot's identity is derived from its content (SN-2) | the identity, from the constituents |

Each re-derivation proceeds **according to the declarations and rules available for that derivation**
— the closure the evidence carries, the source a projection names, the constituents an identity
covers — and never according to anything the evaluator supplies.

Derivational discharge is what makes conformance checkable **without access to the producing system**
— the evaluator re-does the derivation rather than trusting its result.

### 7.5 Selecting a class

An evaluation MUST use a class capable of establishing the obligation:

- an obligation about **what happened** → observational;
- an obligation about **what cannot happen** → structural;
- an obligation about **what must not vary** → comparative;
- an obligation about **what must be re-establishable** → derivational.

**Using observation where structure is required is the characteristic failure**, because it produces
evidence, passes, and establishes nothing (2f §4.2).

## 8. Negative properties

An obligation stating that something *cannot* occur is a **negative property**, and negative
properties are not established by anything going well.

This family states many, and they are where a conformance regime most easily becomes ceremonial:

- no effect from a non-effecting capability (CP-7);
- no execution reachable from inspection (IN-2);
- no undeclared input to construction (GC-10);
- no behavior entering execution from outside a snapshot (SN-10);
- no environmental dependency (EE-4);
- no ungoverned read path (IN-13);
- no override of a refusal (EN-10);
- no path by which governance is weakened by a profile (NP-1).

Each is discharged structurally (§7.2) or comparatively (§7.3). **None is discharged by a system
having worked.**

## 9. Levels

**This family admits no partial conformance to an obligation.** An invariant is satisfied or it is
not (1c §10); there is no degree, no percentage, and no level at which an obligation is partly met.

Where "level" is meaningful, it names **scope of claim**, never depth of satisfaction:

- **which subjects** a claim covers — a runtime claim is narrower than a system instance claim,
  and both are complete claims about what they name;
- **which profile** the claim is against — a claim under a demanding profile establishes more than
  one under a permissive profile, because the profile required more.

**A conformance level that means "most obligations were met" MUST NOT be defined.** It would convert
invariants into targets, and 1c §10 exists to prevent exactly that: a breach is not a degree of
non-conformance; it is the system ceasing to be governed with respect to everything downstream of
the breach.

## 10. Equivalence

**Equivalence is always relative to a stated profile and revision.** Two systems under different
profiles are not comparable by this relation, and finding that they differ establishes nothing.

Two independently produced systems conforming to the same profile and revision are **equivalent in
governed consequence**: given the same snapshot, inputs, and initial state, they produce the same
governed consequences (SN-11, RT-12).

- They are equivalent in **what they determine**, not in how they are built, how fast they are, or
  what they cost.
- **Equivalence is the interoperability claim** this family exists to support: a snapshot means the
  same thing to any conforming system that accepts it.
- Where two conforming systems produce different governed consequences from the same inputs, **at
  least one does not conform**, and that this is decidable rather than a matter of interpretation is
  a consequence of derived identity, execution closure, and declared determinative evidence together.

## 11. What conformance is not

- **Not enforcement.** Enforcement is what a governed system does when a requirement applies;
  conformance is a judgment about the system, made from outside. A system may enforce perfectly and
  fail to conform, and may conform while enforcing obligations that were badly chosen (2f §1).
- **Not correctness.** That a system conforms says nothing about whether its declarations express
  what anyone wanted. Correctness is judged against declared intent, elsewhere (3d §7).
- **Not certification.** This family defines no certifying authority, issues no marks, and confers
  no status. **A conformance claim is a claim, and its weight is the weight of the evidence
  supplied.**
- **Not quality.** A conforming system may be badly designed, and a well-designed one may not
  conform. The two are unrelated judgments.

## 12. What this document does not specify

- **The demonstrations themselves** — what tests exist, how they are constructed, what fixtures they
  require. The Conformance Test Specification's subject.
- **Who evaluates**, or by what process a claim is reviewed, accepted, or disputed.
- **How claims are published**, registered, or discovered.
- **Any obligation.** Every obligation is stated by the document that owns it, and this document
  neither adds nor relaxes one.

## 13. Normative invariants

- **CF-1.** A conformance claim MUST name its subject, its profile, its revision, and its claimant
  (§2).
- **CF-2.** A claim MUST NOT be discharged by evidence about a different subject (§3.2).
- **CF-3.** A system instance claim MUST be discharged by discharging every constituent class (§3.1).
- **CF-4.** Discharge MUST NOT require the evaluator to trust the claimant; reliance on an assertion
  MUST be visible as an attestation (§4).
- **CF-5.** Conformance MUST be established over semantic guarantees, and MUST NOT be established by
  resemblance to any realization (§5).
- **CF-6.** An evaluation MUST derive from a stated obligation, and MUST NOT add to or relax one
  (§6).
- **CF-7.** An obligation with no derivable evaluation MUST be a finding against the document stating
  it (§6).
- **CF-8.** An evaluation MUST use a discharge class capable of establishing the obligation (§7.5).
- **CF-9.** A negative property MUST NOT be discharged observationally (§7.2, §8).
- **CF-10.** An obligation about what must not vary MUST be discharged by substitution, and a subject
  exercised in one configuration MUST NOT be treated as having discharged it (§7.3).
- **CF-11.** No conformance level denoting partial satisfaction of an obligation MUST be defined
  (§9).
- **CF-12.** Two conforming systems under one profile and revision producing different governed
  consequences from the same inputs MUST be a finding against at least one (§10).
- **CF-13.** A conformance claim MUST identify, for each discharge, whether it is observational,
  structural, comparative, or derivational (§7).
- **CF-14.** The subject classes applicable to a system-instance claim MUST be determined from the
  accepted snapshot's self-description and its claimed profile, and MUST NOT be enumerated by the
  claimant (§3.1).

## 14. Conformance of this document

The conformance subject of this document is a **conformance claim**: what was claimed, about what,
against what, by whom, and what was supplied to discharge it.

A claim conforms when it names its four elements, its discharges use classes capable of establishing
what they address, its negative properties are established structurally or comparatively, and nothing
in it rests on the evaluator's trust in the claimant.

**The failure to look for is a discharge that establishes something adjacent.** A claim supported by
extensive evidence, all of it observational, about a set of obligations half of which are negative,
is a claim that has been thoroughly and expensively not established — and it will look more rigorous
than one that ran a single structural check.
