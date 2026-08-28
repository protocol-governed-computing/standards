# Evidence, Attestation & Provenance

## 1. Scope

This document specifies the three records by which what a governed system did can be established
afterwards, and holds them apart: **evidence** records what was determined or occurred;
**attestation** is an assertion by an identified party about a record or artifact; **provenance** is
the derivation relation between a governed thing and what it came from.

It completes Part III by closing the loop the earlier documents open. The Semantic Model makes
evidence constitutive of governedness; the Execution Model requires that a path be checkable; the
Snapshot Standard requires that integrity be verifiable by a party that did not build the snapshot;
the Runtime Standard requires that every determination be evidenced. This document says what those
records must carry, and what they may not become.

It also settles a question earlier documents deliberately left open: **which content of evidence
must be identical across two executions of the same transition, and which may vary** (§5).

This document introduces the terms **determinative content**, **observational content**, **attesting
party**, and **trust root**. Every other term it uses is defined by the Conceptual Model, the
Semantic Model, or Parts II–III.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Three records, never merged

| | Answers | About |
|---|---|---|
| **Evidence** | what was determined, and what occurred | an event or a determination |
| **Attestation** | who vouches for this, and for what property | a record or an artifact |
| **Provenance** | where did this come from, and by what derivation | a governed thing |

The three are routinely collapsed into "the audit trail," and each collapse loses something
specific:

- **Evidence merged into attestation** loses the distinction between something happening and someone
  saying it happened. A system then cannot distinguish a determination it made from a claim it
  received.
- **Attestation merged into provenance** loses the distinction between origin and endorsement.
  Something's having come from a trusted source becomes indistinguishable from that source having
  vouched for it, which are different assurances with different failure modes.
- **Provenance merged into evidence** loses the distinction between derivation and occurrence. A
  system then treats "this was produced from that" as though it were "this was determined
  correctly."

**None of the three establishes correctness**, and none is a source of authority (§8).

## 3. Evidence

**Evidence is the semantic record by which a governed determination, construction, or execution can
subsequently be established by a party that did not observe it.**

It is not an audit log, not a diagnostic byproduct, and not a trace kept in case something goes
wrong. It is produced as a governed obligation, because a determination that cannot be established
did not govern anything (SM §8, AI-14).

### 3.1 What evidence must establish

For any determination, its evidence MUST be sufficient to establish:

1. **which closure applied**, and by what authority each governing element in it applied;
2. **which rules that closure supplied**;
3. **what each predicate yielded**;
4. **what the dominant consequence was**; and
5. **that the resulting state is what that consequence permitted**.

For an execution, it MUST additionally be sufficient to establish **the path taken**, so that the
path can be checked against the sealed representation (EX-15).

Evidence that records outcomes without the closure and rules that produced them establishes that
something happened, not that it was governed — and those are the two things the family exists to
separate.

**Evidence MUST identify the sealed representation it was produced under** (SN-2), and the subject
the determination was about. Re-evaluating a record establishes that the record is internally
consistent; it establishes that the record is *about* a particular system only if the record says
which one. A record that does not name its snapshot is checkable against itself and against nothing
else — a producer supplying a permissive closure and a matching determination would re-evaluate
clean, which is exactly the confidence §10 says a checking party must not have to extend.

How that identification is made unforgeable is a question of integrity mechanism and trust root, and
is not settled here (§12) — it is a profile's (6a §7). **That the record states what it is about is
not a mechanism question and is settled here.**

### 3.2 Evidence is output only

**Evidence is never an input to a determination** (AI-15, RT-10).

- No determination consults the record of prior determinations in reaching a present one.
- No evidence is replayed into a system as governed state.
- A system whose behavior changes when prior evidence is withheld has made its history into its
  governance.

Evidence may of course be read — by people, by checkers, by analysis. What it may not do is
participate in determining what the system does next.

### 3.3 Refusals are evidenced as fully as admissions

A system that records what it permitted and not what it refused has no record of its governance
operating — only of its work proceeding (EN-12). A refusal's evidence MUST establish what was
proposed, what refused it, under what closure and authority, and that nothing proceeded (EN-8).

## 4. Completeness

- **Every determination produces evidence.** There is no determination too small, too routine, or
  too internal to evidence, because the exceptions are where an ungoverned determination would sit
  unobserved.
- **Evidence is produced as the determination is made**, not reconstructed afterwards from what a
  system can still recall. A reconstruction is an account of what probably happened, and its
  accuracy depends on exactly the mechanism under examination.
- **What is not evidenced did not happen**, as far as anything checkable is concerned. This is not a
  metaphysical claim; it is the operating rule that makes the evidence record load-bearing rather
  than advisory.

## 5. Determinative and observational content

This section settles what earlier documents left open.

Evidence carries two kinds of content, and **a conforming system distinguishes them**:

| | Content | Across two executions of the same transition |
|---|---|---|
| **Determinative** | everything §3.1 requires: closure, authority, rules, predicate results, consequence, resulting state, path | MUST be identical |
| **Observational** | when it occurred, how long it took, where it ran, what the environment measured, what was recorded about the recording | MAY differ |

### 5.1 The rule

- **Determinative content MUST be identical** for the same `(S, π, C)`. If it differs, the
  determination differed, and SM-10 was violated — the variance is the finding, not noise to be
  tolerated.
- **Observational content MUST NOT be determinative.** Nothing in a determination may depend on it.
  The moment a timestamp, a duration, a node identifier, or an environmental reading can change a
  consequence, it has stopped being observational and the system is no longer deterministic.
- **The distinction MUST be declared, not inferred.** Evidence must state which of its content is
  determinative, so that a checker can compare that content and disregard the rest.

### 5.2 Why the distinction must be declared

Without it, replay comparison is impossible in both directions. A checker that compares everything
fails on every timestamp and learns nothing. A checker that compares nothing established nothing.
And a checker that guesses — comparing what looks stable — is deciding for itself what governance
meant, which is the failure the whole family is arranged against.

**Observational content is still evidence.** It is not discardable metadata: it supports
attestation, forensics, and operational understanding. What it never does is participate in
establishing that a determination was correct.

## 6. Attestation

An **attestation** is an assertion, by an identified party, about the integrity or origin of a
record or artifact.

An attestation MUST identify:

- **the attesting party** — who asserts;
- **the subject** — what is asserted about, by identity;
- **the property asserted** — integrity, origin, or another stated property; and
- **the basis**, where the assertion rests on something other than the party's own observation.

### 6.1 An attestation is a claim, not a proof

**An attestation does not establish that what it asserts is true.** It transfers the question from
*is this so* to *do I accept this party's assertion that it is so*. That is a real and useful
transfer — it is how anything is established across a boundary where the checker cannot observe
directly — but it is a transfer, not an elimination.

A system that treats an attestation as proof has adopted the attesting party's judgment without
saying so, and has no way to state what it is relying on.

### 6.2 Chains and the trust root

An attestation may be about another attestation. Such a chain terminates in something the checking
party accepts without further attestation — a **trust root**.

- **A chain MUST terminate.** An attestation chain with no root establishes nothing, however long.
- **This family does not supply a trust root.** What a checking party accepts axiomatically is a
  property of that party and of the profile under which it operates, not of governed computation.
- A system MUST be able to state what its chains terminate in. A trust root that cannot be named is
  being relied upon without being acknowledged.

### 6.3 Attestation is not governance

An attestation asserts something about a thing. **It does not govern the thing, and it confers no
authority on what it attests** (GO-6, GO-9). An artifact does not become admissible by being
attested, and an attested realization does not thereby satisfy its contract.

Where an attestation is *required* — by a profile, by an obligation — the requirement is what
governs; the attestation satisfies it.

## 7. Provenance

**Provenance is the derivation relation** between a governed thing and what it came from.

- Provenance MUST identify **the source** and **the derivation** by which the thing was produced.
- Provenance is a property of the **semantic element**, established when it came into existence and
  unchanged by subsequent representation (GO-2).
- Provenance MUST be carried by everything derived or produced, sufficient to identify its source or
  producing operation (GO-9).

### 7.1 Provenance is neither authority nor correctness

Two inferences are forbidden, and both are tempting:

- **Derivation from an authoritative source does not confer authority.** A thing computed from a
  governing element does not thereby govern. Being derived is not being authorized (GO-9).
- **Known provenance does not establish correctness.** That a thing came from a stated source by a
  stated derivation says nothing about whether the derivation was right, or whether the result is
  what was wanted. Provenance answers *where from*, and only that.

A system that reads provenance as either is treating lineage as a substitute for determination.

## 8. None of the three is a source of authority

Stated once, because each is separately tempting:

| Record | Tempting inference | Why it fails |
|---|---|---|
| Evidence | it happened, so it is permitted | occurrence is not authorization; an ungoverned transition also occurs |
| Attestation | it is vouched for, so it is admissible | admission is a determination under a closure, not an endorsement |
| Provenance | it came from something authoritative, so it inherits authority | authority is declared, never inherited by derivation |

**Evidence records the past; it does not govern the future.** A normative element may be *informed*
by evidence — someone may read a record and decide to change a rule — but that change is a governed
transformation, and the evidence was an input to a person's judgment, not to a determination
(GO-6, §3.2).

## 9. Four identities, kept apart

Four distinct identities appear in these records and MUST NOT be conflated:

| Identity | Identifies |
|---|---|
| **snapshot identity** | the sealed representation executed against (SN-2) |
| **evidence identity** | the record of a particular determination or execution |
| **attestation identity** | the assertion, distinct from what it asserts about |
| **actor identity** | the participant on whose behalf something occurred |

Each may reference the others; none substitutes for another — but the reference from evidence to the
snapshot it was produced under is required rather than optional (§3.1, EV-17). In particular, **an actor identity is
not an authority** (GO-7): naming who acted says nothing about what they were entitled to do, which
the closure applicable to that determination establishes.

## 10. Independent checkability

Every requirement above serves one property: **a party with no access to the system that produced
these records, and no reason to trust it, can establish what was determined** (AI-16).

- Checking re-evaluates the closure and rules the evidence carries, using the authority and profile
  information the applicable semantic case requires — never a closure rediscovered from a current
  environment (SM-12).
- Where a checker must rely on an assertion rather than re-derive, that reliance is an attestation
  and MUST be visible as one (§6.1).
- A record whose verification requires querying the live system, reconstructing its environment, or
  accepting an unsupported claim does not satisfy this document.

## 11. Retention

This document requires that evidence be **produced** and **sufficient**. It does not specify how
long it is kept, where, or in what form.

But retention has a governed consequence, and one rule follows: **the period over which a
determination can be established is the period over which its evidence is retained.** A system that
discards evidence has not made past determinations ungoverned — they were governed when they were
made — but it has made them unestablishable, and a claim about them can no longer be checked.
Whether that is acceptable is a profile's question, and it should be answered rather than reached by
default.

## 12. What this document does not specify

- **Formats, encodings, or storage.** Any serves that carries what is required.
- **Integrity or signature mechanisms.** Any serves by which a party who did not produce a record
  can detect a difference.
- **The trust root.** Supplied by a profile and by the checking party, never by this family (§6.2).
- **Retention periods.** A profile's question (§11).
- **How conformance is demonstrated.** The Conformance Test Specification's.

## 13. Normative invariants

- **EV-1.** Every determination MUST produce evidence sufficient to establish the five points of
  §3.1, and every execution MUST additionally establish its path (§3.1).
- **EV-2.** Evidence MUST be produced as the determination is made, and MUST NOT be reconstructed
  afterwards (§4).
- **EV-3.** Refusals MUST be evidenced as fully as admissions (§3.3).
- **EV-4.** Evidence MUST NOT be an input to any determination (§3.2).
- **EV-5.** Evidence MUST distinguish its determinative content from its observational content, and
  the distinction MUST be declared rather than inferred (§5.1).
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

An evidence record conforms when it establishes the five points of §3.1 to a party that did not
observe the determination, declares which of its content is determinative, carries provenance for
what was derived, identifies the party behind any assertion it relies on, and can be checked without
recourse to the system that produced it.

**The properties most easily claimed falsely are the negative ones.** That evidence was produced
shows nothing about whether anything was omitted; that a system's records are internally consistent
shows nothing about whether they describe what occurred. What establishes the record is that a
determination the system made can be re-derived from it by someone who was not there — and that a
determination the system did *not* make cannot be.

How that is required and evaluated belongs to the Conformance Test Specification.
