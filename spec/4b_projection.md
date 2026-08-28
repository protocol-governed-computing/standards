# Projection

## 1. Scope

This document specifies the **projection**: a deterministic, machine-consumable representation of
governed information derived from a defined source.

It specifies the concept first — derivation, faithfulness, regenerability, identity — and only then
the uses to which projections are put. Canonical forms, indexes, address-resolved forms, rendered
structures, and vocabularies are **realizations** of the concept. None of them may become its
definition, and a document that defined projection by enumerating them would have frozen one
implementation's outputs into the standard.

Governed Construction names projection among its obligations; the Snapshot Standard carries
projections as constituents; the Execution Model and Governed Inspection consume them. This document
says what one *is*.

This document introduces the terms **projection source**, **projection contract**, **faithfulness**,
and **regenerability**. Every other term it uses is defined by the Conceptual Model, the Semantic
Model, or Parts II–IV.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What a projection is

A **projection** is a representation with four properties:

| Property | Meaning |
|---|---|
| **derived** | produced from a defined source by a declared derivation (§3) |
| **deterministic** | the same governed source under the same declared semantics yields the same projection (§3) |
| **faithful** | it makes no claim its source does not entail (§4) |
| **regenerable** | it can be reproduced from its source at any time (§6) |

**A projection carries meaning that is already settled. It never adds meaning of its own**
(Conceptual Model, *projection*).

A **projection source** is the governed information a projection is derived from: one artifact,
several, or an entire composition. The source MUST be defined — a projection whose source cannot be
stated is not a projection, because nothing establishes what it is a representation *of*.

**Machine-consumable** describes the form, not the audience: a projection is structured so that it
can be consumed without being interpreted. That property is what lets a projection be consumed
mechanically; it does not exclude a person reading one, and inspection routinely serves people
(§9).

## 3. Derivation

A projection is produced by a **declared derivation** from its source.

- **The derivation MUST be declared.** A representation that appeared by a process nothing declared
  is not a projection; it is content of unknown origin that happens to resemble one.
- **The derivation MUST be deterministic.** The same governed source, under the same declared
  semantics, MUST yield the same projection. A derivation that varies has made the projection a
  function of something other than its source, and that something is undeclared (GC-10).
- **The derivation MUST NOT consult anything but its source** — not an environment, not a prior
  projection, not accumulated state, not the time at which it ran.

### 3.1 The projection contract

Every projection is governed by a **projection contract** stating what it derives, from what, and
the declared use for which it is produced.

The contract is what makes omission checkable. Without it, an absent element is ambiguous between
*deliberately not projected* and *lost*, and no examination can tell which — so a projection with no
contract cannot be verified against anything, only compared with expectations.

A projection contract states:

- its **source** — what governed information it derives from;
- its **selection** — what of that source it carries, and what it does not;
- its **derivation** — how the carried content follows from the source.

## 4. Faithfulness

**A projection is faithful when every claim it makes about governed information is entailed by its
source, and it makes no claim its source does not entail.**

Faithfulness is **soundness, not completeness**. A projection may omit; it may not add or alter.

### 4.1 Lossy is not unfaithful

**Projections are lossy by design.** A projection exists because some consumer needs part of the
governed information in a particular shape, and carrying everything would defeat the purpose of
deriving anything.

Omission within what the projection contract declares is correct behavior, not degradation. What
would be a defect is:

- **addition** — a claim the source does not entail;
- **alteration** — a claim the source contradicts;
- **undeclared omission** — absence of something the contract said would be carried.

The first two are unfaithfulness. The third is a contract violation, and it is distinguishable from
the first two only because §3.1 requires the contract.

### 4.2 No projection adds meaning

A derivation may compute, index, restructure, resolve, and arrange. **It MUST NOT interpret.**

- It MUST NOT supply a default for something the source leaves unstated.
- It MUST NOT resolve an ambiguity by choosing a reading.
- It MUST NOT introduce semantic enrichment, unsupported annotation, or inference. Derived material
  a projection is *required* to carry — its provenance, its derivation record, its identity — is not
  enrichment: it is entailed by the derivation itself.
- Where the source does not determine what a projection would need to carry, the derivation
  **refuses**; it does not decide.

A projection that added meaning would be a declaration that nobody authored and no closure admitted
— reaching consumers as though it were derived fact. That is the most dangerous form the failure
takes: the added meaning arrives with the authority of everything around it.

## 5. The source is authoritative

**Where a projection and its source disagree, the source governs and the projection is defective.**

- A projection is **never** the thing governance reads to determine anything about its source.
- **Nothing may be authored into a projection.** A projection is not a declaration surface; content
  placed there is not admitted, not governed, and not part of the governed system (MB-1).
- A projection MUST NOT be edited. A projection corrected in place is no longer derived from its
  source, and its relationship to that source can no longer be established.

The direction of authority never reverses. This holds even where the projection is more convenient,
more current, or more widely consumed than its source — those are reasons the reversal is tempting,
not reasons it is permitted.

## 6. Regenerability

**A projection MUST be reproducible from its source at any time.**

Regenerability is the check that makes faithfulness testable: derive again, compare, and any
difference is either an unfaithful projection or a non-deterministic derivation. Both are findings.

It follows that **a projection contains nothing its source does not**. If regenerating loses
something, that something was never derived — it was introduced, and §4.2 forbids it.

A realization MAY retain a materialized projection rather than deriving it on demand. That is a
mechanism decision (RT-5): retention must not change what the projection says, only when the work
of producing it happens.

## 7. Identity, integrity, and provenance

- **A projection's identity is derived from the governed content it represents** (AI-9, MB-3), as
  any governed representation's is.
- **A projection MUST carry provenance** identifying its source and the derivation that produced it
  (GO-9, EV-12). A projection whose source cannot be established is unverifiable, and its
  faithfulness is not a claim anyone can check. Provenance identifies origin; it does not authorize
  the projection.
- **A projection is not authoritative by virtue of being derived** (GO-9). Derivation confers no
  authority — a point that matters most where a projection is the form a consumer actually reads,
  and its derived status is easiest to forget.

## 8. Multiple projections of one source

One source may have many projections, each with its own contract and purpose.

- **All projections of one source MUST be mutually consistent where their carried claims overlap.**
  Two projections of one source that entail contradictory claims establish that at least one is
  unfaithful; the contradiction is a finding, not a difference of perspective.
- **No projection is privileged.** That one projection is more complete, more frequently consumed,
  or more convenient does not make it the source, and does not make another one wrong where they
  differ in what they carry.
- Consistency is a property of what they *claim*, not of what they *carry*. Two projections
  legitimately carry different subsets of one source; what they may not do is entail different
  things about the part they share.

## 9. What projections are for

Only after the concept: projections exist so that governed information can be consumed in the shape
a consumer needs, without the consumer reading the source and forming its own view of it.

| Consumer | Reads a projection in order to |
|---|---|
| construction | build on what earlier obligations established |
| execution | traverse structure and resolve references without interpretation |
| inspection | answer questions about the system without altering it |
| verification | compare what was carried against the applicable governed determination |

**Each of these is a consumer of a projection, never an author of one.** A consumer that adjusts a
projection to suit itself has taken the source's authority and left no record of doing so.

## 10. Realizations

The following are projections. **None of them defines the concept**, and a system may have any,
all, or none of them:

- a **canonical form** — the governed information in one normal form;
- an **index** — an arrangement permitting something to be located or enumerated;
- an **address-resolved form** — references replaced by what they resolve to;
- a **structural rendering** — the constructed structure in a form that can be examined;
- a **vocabulary view** — the named concepts of a system, collected;
- an **evidence view** — a derived representation of evidence or provenance information, arranged
  for consumption. What evidence *is* belongs to Evidence, Attestation & Provenance; this is a
  projection of it.

Each is a projection because it satisfies §2, not because it appears here. A realization that
introduces a projection this list does not name has introduced a projection, and this document
governs it identically.

## 11. What a projection is not

- **Not a source.** Nothing is declared into it (§5).
- **Not a cache.** A cache is an optimization whose absence is a miss to be filled. A projection is a
  governed representation whose absence, where a snapshot is required to carry it, is incompleteness
  (SN-4). The two are easy to conflate because both are recomputable; they differ in what their
  absence means.
- **Not a summary.** A summary is composed by a judgment about what matters. A projection is derived
  by a declared derivation, and judgment about what matters lives in its contract, where it was
  declared and admitted.
- **Not a copy** — though a projection may carry everything its source does. What makes it a
  projection is derivation under a contract, not how much it omits.

## 12. What this document does not specify

- **What projections a system has.** A profile's selection, or a kind contract's requirement.
- **How a projection is encoded, stored, or transported.**
- **What derivations are available.** Any that is declared, deterministic, and consults only its
  source.
- **Whether projections are materialized or derived on demand** (§6).

## 13. Normative invariants

- **PJ-1.** A projection MUST have a defined source and a declared derivation (§2, §3).
- **PJ-2.** A derivation MUST be deterministic and MUST consult nothing but its source (§3).
- **PJ-3.** Every projection MUST be governed by a projection contract stating its source, its
  selection, and its derivation (§3.1).
- **PJ-4.** A projection MUST make no claim its source does not entail (§4).
- **PJ-5.** A projection MUST NOT supply a default, resolve an ambiguity, infer, or silently
  transform an unresolved condition into a resolved one; where its source does not determine what it
  would carry, the derivation MUST refuse (§4.2).
- **PJ-6.** A projection MUST NOT omit anything its contract declares it carries (§4.1).
- **PJ-7.** Where a projection and its source disagree, the source MUST govern (§5).
- **PJ-8.** Nothing MUST be authored into a projection, and a projection MUST NOT be edited (§5).
- **PJ-9.** A projection MUST be regenerable from its source (§6).
- **PJ-10.** A projection MUST carry provenance identifying its source and derivation (§7).
- **PJ-11.** Derivation MUST NOT confer authority on a projection (§7).
- **PJ-12.** Projections of one source MUST NOT entail contradictory claims (§8).

## 14. Conformance

The conformance subject of this document is a **projection**: a derived representation together with
its contract, its provenance, and the derivation that produced it.

A projection conforms when its source and derivation are declared, its derivation is deterministic
and consults nothing else, it carries what its contract says and adds nothing, it regenerates
identically from its source, and it entails nothing contradicting another projection of the same
source.

**Faithfulness is established by regeneration, not by inspection.** Reading a projection cannot
reveal a claim its source does not entail — the added claim looks exactly like a derived one, which
is why §4.2 calls it the most dangerous failure. What reveals it is deriving again and comparing:
anything that differs was not derived from the source.

How that is required and evaluated belongs to the Conformance Test Specification.
