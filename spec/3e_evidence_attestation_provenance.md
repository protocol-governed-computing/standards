# Evidence, Attestation & Provenance

## 1. Scope

This document specifies the three records that let a party establish afterwards what a governed
system did. It keeps the three apart:

- **evidence** records what was determined or occurred;
- **attestation** is an assertion by an identified party about a record or artifact;
- **provenance** is the derivation relation between a governed thing and what it came from.

This document completes Part III by closing the loop the earlier documents open:

- the Semantic Model makes evidence constitutive of governedness;
- the Execution Model requires that a path be checkable;
- the Snapshot Standard requires that a party that did not build the snapshot can verify its
  integrity;
- the Runtime Standard requires that every determination be evidenced.

This document says what those records must carry, and what they may not become.

This document settles a question that earlier documents deliberately left open: **which evidence
content must be identical across two executions of the same transition, and which content may
vary** (§5).

This document introduces the terms **determinative content**, **observational content**, **attesting
party**, and **trust root**. The Conceptual Model, the Semantic Model or Parts II–III defines every
other term it uses.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Three records, never merged

| | Answers | About |
|---|---|---|
| **Evidence** | what was determined, and what occurred | an event or a determination |
| **Attestation** | who vouches for this, and for what property | a record or an artifact |
| **Provenance** | where did this come from, and by what derivation | a governed thing |

People often lump the three together as "the audit trail". Each merger loses something specific:

- **Evidence merged into attestation** loses the difference between something happening and someone
  saying it happened. The system can then no longer tell a determination it made from a claim it
  received.
- **Attestation merged into provenance** loses the difference between origin and endorsement. A thing
  that came from a trusted source then looks the same as a thing that source vouched for. These are
  different assurances, with different failure modes.
- **Provenance merged into evidence** loses the difference between derivation and occurrence. The
  system then treats "this was produced from that" as if it meant "this was determined correctly".

**None of the three establishes correctness**, and none is a source of authority (§8).

## 3. Evidence

**Evidence is the semantic record that lets a party who did not observe a governed determination,
construction or execution establish it afterwards.**

Evidence is not an audit log, not a diagnostic byproduct, and not a trace kept in case something goes
wrong. A system produces it as a governed obligation, because a determination that cannot be
established did not govern anything (Semantic Model §8, AI-14).

### 3.1 What evidence must establish

For any determination, its evidence MUST be sufficient to establish:

1. **which closure applied**, and by what authority each governing element in it applied;
2. **which rules that closure supplied**;
3. **what each predicate yielded**;
4. **what the dominant consequence was**;
5. **that the resulting state is what that consequence permitted**.

For an execution, the evidence MUST also be sufficient to establish **the path taken**, so a party
can check the path against the sealed representation (EX-15).

Evidence that records outcomes without the closure and rules that produced them establishes that
something happened, not that it was governed. The family exists to separate those two things.

**Evidence MUST identify the sealed representation it was produced under** (SN-2), and the subject the
determination was about. Re-evaluating a record establishes that the record is internally
consistent. It establishes that the record is *about* a particular system only if the record says
which one. A record that does not name its snapshot can be checked against itself and against
nothing else. A producer could supply a permissive closure and a matching determination, and the
record would re-evaluate clean. §10 says a checking party must never have to extend exactly that
confidence.

How that identification is made unforgeable is a question of integrity mechanism and trust root.
This document does not settle it (§12). It belongs to a profile (Normative Platform Profile §7).
**That the record states what it is about is not a mechanism question. This document settles it.**

### 3.2 Evidence is output only

**Evidence is never an input to a determination** (AI-15, RT-10).

- No determination consults the record of earlier determinations to reach a present one.
- No system replays evidence into itself as governed state.
- A system whose behavior changes when prior evidence is withheld has made its history its
  governance.

People, checkers and analyses may of course read evidence. What evidence may not do is take part in
determining what the system does next.

### 3.3 Refusals are evidenced as fully as admissions

A system that records what it permitted and not what it refused has no record of its governance at
work. It has a record only of its work proceeding (EN-12). A refusal's evidence MUST establish what
was proposed, what refused it, under what closure and authority, and that nothing proceeded (EN-8).

## 4. Completeness

- **Every determination produces evidence.** No determination is too small, too routine or too
  internal to evidence. The exceptions are exactly where an ungoverned determination would sit
  unobserved.
- **A system produces evidence as it makes the determination.** It does not reconstruct evidence
  afterwards from what it can still recall. A reconstruction is an account of what probably
  happened. Its accuracy depends on exactly the mechanism under examination.
- **What is not evidenced did not happen**, as far as anything checkable is concerned. This is not a
  metaphysical claim. It is the operating rule that makes the evidence record carry weight, rather
  than serve as advice.

## 5. Determinative and observational content

This section settles what earlier documents left open.

Evidence carries two kinds of content, and **a conforming system distinguishes them**:

| | Content | Across two executions of the same transition |
|---|---|---|
| **Determinative** | everything §3.1 requires: closure, authority, rules, predicate results, consequence, resulting state, path | MUST be identical |
| **Observational** | when it occurred, how long it took, where it ran, what the environment measured, what was recorded about the recording | MAY differ |

### 5.1 The rule

- **Determinative content MUST be identical** for the same `(S, π, C)`. If it differs, the
  determination differed, and SM-10 was violated. The variance is the finding, not noise to
  tolerate.
- **Observational content MUST NOT be determinative.** No determination may depend on it. Suppose a
  timestamp, a duration, a node identifier or an environmental reading can change a consequence. At
  that moment it stops being observational, and the system is no longer deterministic.
- **The distinction MUST be declared, not inferred.** Evidence must state which of its content is
  determinative, so a checker can compare that content and ignore the rest.

### 5.2 Why the distinction must be declared

Without a declared distinction, replay comparison fails in every direction:

- A checker that compares everything fails on every timestamp and learns nothing.
- A checker that compares nothing establishes nothing.
- A checker that guesses, comparing whatever looks stable, decides for itself what governance meant.
  The whole family is arranged against that failure.

**Observational content is still evidence.** It is not discardable metadata. It supports
attestation, forensics and operational understanding. It never takes part in establishing that a
determination was correct.

## 6. Attestation

An **attestation** is an assertion, by an identified party, about the integrity or origin of a
record or artifact.

An attestation MUST identify:

- **the attesting party**: who asserts;
- **the subject**: what the assertion is about, by identity;
- **the property asserted**: integrity, origin, or another stated property;
- **the basis**, where the assertion rests on something other than the party's own observation.

### 6.1 An attestation is a claim, not a proof

**An attestation does not establish that what it asserts is true.** It moves the question from *is
this so?* to *do I accept this party's assertion that it is so?* That move is real and useful. It is
how anything is established across a boundary where the checker cannot observe directly. But it moves
the question. It does not remove it.

A system that treats an attestation as proof has silently adopted the attesting party's judgment. It
has no way to state what it relies on.

### 6.2 Chains and the trust root

An attestation may be about another attestation. Such a chain ends in something the checking party
accepts without further attestation: a **trust root**.

- **A chain MUST terminate.** An attestation chain with no root establishes nothing, however long it
  is.
- **This family does not supply a trust root.** What a checking party accepts as an axiom is a
  property of that party and of the profile it operates under. It is not a property of governed
  computation.
- A system MUST be able to state what its chains terminate in. A system that relies on a trust root
  it cannot name relies on it without acknowledging it.

### 6.3 Attestation is not governance

An attestation asserts something about a thing. **It does not govern the thing, and it confers no
authority on what it attests** (GO-6, GO-9). Attesting an artifact does not make it admissible.
Attesting a realization does not make it satisfy its contract.

A profile or an obligation may *require* an attestation. Then the requirement governs, and the
attestation satisfies it.

## 7. Provenance

**Provenance is the derivation relation** between a governed thing and what it came from.

- Provenance MUST identify **the source** and **the derivation** that produced the thing.
- Provenance is a property of the **semantic element**. It is established when the element comes into
  existence, and later representations do not change it (GO-2).
- Everything derived or produced MUST carry provenance sufficient to identify its source or producing
  operation (GO-9).

### 7.1 Provenance is neither authority nor correctness

Two inferences are forbidden, and both are tempting:

- **Derivation from an authoritative source does not confer authority.** A thing computed from a
  governing element does not thereby govern. Being derived is not being authorized (GO-9).
- **Known provenance does not establish correctness.** A thing may come from a stated source by a
  stated derivation. That says nothing about whether the derivation was right, or whether the result
  is what was wanted. Provenance answers *where from*, and only that.

A system that reads provenance as either one is treating lineage as a substitute for determination.

## 8. None of the three is a source of authority

This section states the point once, because each record is separately tempting:

| Record | Tempting inference | Why it fails |
|---|---|---|
| Evidence | it happened, so it is permitted | occurrence is not authorization; an ungoverned transition also occurs |
| Attestation | it is vouched for, so it is admissible | admission is a determination under a closure, not an endorsement |
| Provenance | it came from something authoritative, so it inherits authority | authority is declared, never inherited by derivation |

**Evidence records the past. It does not govern the future.** Evidence may *inform* a normative
element: someone may read a record and decide to change a rule. That change is a governed
transformation. The evidence was an input to a person's judgment, not to a determination (GO-6,
§3.2).

## 9. Four identities, kept apart

Four distinct identities appear in these records, and they MUST NOT be conflated:

| Identity | Identifies |
|---|---|
| **snapshot identity** | the sealed representation executed against (SN-2) |
| **evidence identity** | the record of a particular determination or execution |
| **attestation identity** | the assertion, distinct from what it asserts about |
| **actor identity** | the participant on whose behalf something occurred |

Each may reference the others, and none substitutes for another. The reference from evidence to the
snapshot it was produced under is required, not optional (§3.1, EV-17). In particular, **an actor
identity is not an authority** (GO-7). Naming who acted says nothing about what they were entitled to
do. The closure applicable to that determination establishes that.

## 10. Independent checkability

Every requirement above serves one property: **a party with no access to the system that produced
these records, and no reason to trust it, can establish what was determined** (AI-16).

- A checker re-evaluates the closure and rules the evidence carries. It uses the authority and
  profile information the applicable semantic case requires. It never uses a closure rediscovered
  from a current environment (SM-12).
- Where a checker must rely on an assertion instead of re-deriving, that reliance is an attestation
  and MUST be visible as one (§6.1).
- A record does not satisfy this document if verifying it requires querying the live system,
  reconstructing its environment, or accepting an unsupported claim.

## 11. Retention

This document requires that evidence be **produced** and **sufficient**. It does not specify how long
evidence is kept, where, or in what form.

Retention does have a governed consequence, and one rule follows: **a determination can be
established for exactly as long as its evidence is retained.** A system that discards evidence has not
made past determinations ungoverned. They were governed when they were made. But it has made them
unestablishable, and nobody can check a claim about them any more. Whether that is acceptable is a
profile's question. The profile should answer it, not reach an answer by default.

## 12. What this document does not specify

- **Formats, encodings or storage.** Any one serves that carries what is required.
- **Integrity or signature mechanisms.** Any one serves that lets a party who did not produce a
  record detect a difference.
- **The trust root.** A profile and the checking party supply it, never this family (§6.2).
- **Retention periods.** A profile's question (§11).
- **How conformance is demonstrated.** The Conformance Test Specification owns that.

## 13. Normative invariants

- **EV-1.** Every determination MUST produce evidence sufficient to establish the five points of
  §3.1. Every execution MUST also establish its path (§3.1).
- **EV-2.** Evidence MUST be produced as the determination is made, and MUST NOT be reconstructed
  afterwards (§4).
- **EV-3.** Refusals MUST be evidenced as fully as admissions (§3.3).
- **EV-4.** Evidence MUST NOT be an input to any determination (§3.2).
- **EV-5.** Evidence MUST distinguish its determinative content from its observational content. The
  distinction MUST be declared rather than inferred (§5.1).
- **EV-6.** Determinative content MUST be identical across determinations over the same state,
  proposal, and closure (§5.1).
- **EV-7.** Observational content MUST NOT participate in any determination (§5.1).
- **EV-8.** An attestation MUST identify its attesting party, its subject, and the property asserted
  (§6).
- **EV-9.** An attestation MUST NOT be treated as establishing the truth of what it asserts (§6.1).
- **EV-10.** An attestation chain MUST terminate in a nameable trust root (§6.2).
- **EV-11.** An attestation MUST NOT confer authority or admissibility on what it attests (§6.3).
- **EV-12.** Every derived or produced element MUST carry provenance identifying its source and
  derivation (§7).
- **EV-13.** Provenance MUST NOT confer authority, and MUST NOT be read as establishing correctness
  (§7.1).
- **EV-14.** Evidence, attestation, and provenance MUST NOT be sources of governance authority (§8).
- **EV-15.** Snapshot, evidence, attestation, and actor identities MUST be separately determinable
  (§9).
- **EV-16.** Records MUST be checkable without access to, or trust in, the system that produced them
  (§10).
- **EV-17.** Evidence MUST identify the sealed representation it was produced under and the subject
  of the determination it records (§3.1).

## 14. Conformance

The conformance subject of this document is an **evidence record**: what a governed system produced
about a determination, together with any attestations and provenance attached to it.

An evidence record conforms when all of the following hold:

- it establishes the five points of §3.1 to a party that did not observe the determination;
- it declares which of its content is determinative;
- it carries provenance for what was derived;
- it identifies the party behind any assertion it relies on;
- a party can check it without recourse to the system that produced it.

**The properties most easily claimed falsely are the negative ones.** Evidence that was produced
shows nothing about whether anything was omitted. Records that are internally consistent show nothing
about whether they describe what occurred. The record is established by two things. Someone who was
not there can re-derive from it a determination the system made. And nobody can re-derive from it a
determination the system did *not* make.

The Conformance Test Specification owns how that is required and evaluated.
