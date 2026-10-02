# Projection

## 1. Scope

This document specifies the **projection**: a deterministic, machine-consumable representation of
governed information derived from a defined source.

This document specifies the concept first: derivation, faithfulness, regenerability and identity.
Only then does it cover the uses of projections. Canonical forms, indexes, address-resolved forms,
rendered structures and vocabularies are **realizations** of the concept. None of them may become
its definition. A document that defined projection by listing them would freeze one implementation's
outputs into the standard.

Governed Construction names projection among its obligations. The Snapshot Standard carries
projections as constituents. The Execution Model and Governed Inspection consume them. This document
says what a projection *is*.

This document introduces the terms **projection source**, **projection contract**, **faithfulness**,
and **regenerability**. The Conceptual Model, the Semantic Model or Parts II–IV defines every other
term it uses.

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
several, or an entire composition. The source MUST be defined. A projection whose source cannot be
stated is not a projection, because nothing establishes what it represents.

**Machine-consumable** describes the form, not the audience. A projection is structured so that a
consumer can use it without interpreting it. That property lets machines consume a projection. It
does not stop a person reading one, and inspection routinely serves people (§9).

## 3. Derivation

A **declared derivation** produces a projection from its source.

- **The derivation MUST be declared.** A representation that appeared by an undeclared process is not
  a projection. It is content of unknown origin that happens to resemble one.
- **The derivation MUST be deterministic.** The same governed source, under the same declared
  semantics, MUST yield the same projection. A derivation that varies has made the projection depend
  on something other than its source, and that something is undeclared (GC-10).
- **The derivation MUST NOT consult anything but its source.** It consults no environment, no prior
  projection, no accumulated state and no clock.

### 3.1 The projection contract

A **projection contract** governs every projection. It states what the projection derives, from what,
and the declared use it is produced for.

The contract makes omission checkable. Without a contract, an absent element could mean
*deliberately not projected* or *lost*, and no examination could tell which. A projection with no
contract cannot be verified against anything. It can only be compared with expectations.

A projection contract states:

- its **source**: what governed information it derives from;
- its **selection**: what of that source it carries, and what it does not;
- its **derivation**: how the carried content follows from the source.

## 4. Faithfulness

**A projection is faithful when its source entails every claim it makes about governed information,
and it makes no claim its source does not entail.**

Faithfulness is **soundness, not completeness**. A projection may omit. It may not add or alter.

### 4.1 Lossy is not unfaithful

**Projections are lossy by design.** A projection exists because some consumer needs part of the
governed information in a particular shape. Carrying everything would defeat the purpose of deriving
anything.

Omission within what the projection contract declares is correct behavior, not degradation. These
would be defects:

- **addition**: a claim the source does not entail;
- **alteration**: a claim the source contradicts;
- **undeclared omission**: absence of something the contract said would be carried.

The first two are unfaithfulness. The third is a contract violation. It can be told apart from the
first two only because §3.1 requires the contract.

### 4.2 No projection adds meaning

A derivation may compute, index, restructure, resolve and arrange. **It MUST NOT interpret.**

- It MUST NOT supply a default for something the source leaves unstated.
- It MUST NOT resolve an ambiguity by choosing a reading.
- It MUST NOT introduce semantic enrichment, unsupported annotation, or inference. A projection is
  *required* to carry some derived material: its provenance, its derivation record and its identity.
  That material is not enrichment; the derivation itself entails it.
- Where the source does not determine what a projection would need to carry, the derivation
  **refuses**. It does not decide.

A projection that added meaning would be a declaration that nobody authored and no closure admitted.
It would reach consumers as if it were derived fact. This is the most dangerous form of the failure,
because the added meaning arrives with the authority of everything around it.

## 5. The source is authoritative

**Where a projection and its source disagree, the source governs and the projection is defective.**

- Governance **never** reads a projection to determine anything about its source.
- **Nobody may author anything into a projection.** A projection is not a declaration surface.
  Content placed there is not admitted, not governed, and not part of the governed system (MB-1).
- A projection MUST NOT be edited. A projection corrected in place is no longer derived from its
  source, and nobody can establish its relationship to that source any more.

The direction of authority never reverses. It holds even where the projection is more convenient,
more current or more widely consumed than its source. Those are reasons the reversal is tempting.
They are not reasons it is permitted.

## 6. Regenerability

**A projection MUST be reproducible from its source at any time.**

Regenerability makes faithfulness testable. Derive again and compare. Any difference is either an
unfaithful projection or a non-deterministic derivation. Both are findings.

It follows that **a projection contains only what its source contains**. If regeneration loses
something, that something was never derived. It was introduced, and §4.2 forbids that.

A realization MAY retain a materialized projection instead of deriving it on demand. That is a
mechanism decision (RT-5). Retention may change only when the work of producing the projection
happens. It must not change what the projection says.

## 7. Identity, integrity, and provenance

- **A projection's identity derives from the governed content it represents** (AI-9, MB-3), like any
  governed representation's identity.
- **A projection MUST carry provenance** identifying its source and the derivation that produced it
  (GO-9, EV-12). If nobody can establish a projection's source, the projection is unverifiable, and
  nobody can check its faithfulness. Provenance identifies origin. It does not authorize the
  projection.
- **A projection is not authoritative by virtue of being derived** (GO-9). Derivation confers no
  authority. This matters most where a projection is the form a consumer actually reads. There its
  derived status is easiest to forget.

## 8. Multiple projections of one source

One source may have many projections, each with its own contract and purpose.

- **All projections of one source MUST be mutually consistent where their carried claims overlap.** If
  two projections of one source entail contradictory claims, at least one is unfaithful. The
  contradiction is a finding, not a difference of perspective.
- **No projection is privileged.** One projection may be more complete, more often consumed or more
  convenient. That does not make it the source. It does not make another projection wrong where the
  two carry different things.
- Consistency is a property of what projections *claim*, not of what they *carry*. Two projections
  may legitimately carry different subsets of one source. They may not entail different things about
  the part they share.

## 9. What projections are for

Only now, after the concept, does this document turn to uses. Projections exist so a consumer can use
governed information in the shape it needs, without reading the source and forming its own view of
it.

| Consumer | Reads a projection in order to |
|---|---|
| construction | build on what earlier obligations established |
| execution | traverse structure and resolve references without interpretation |
| inspection | answer questions about the system without altering it |
| verification | compare what was carried against the applicable governed determination |

**Each of these consumes a projection. None of them authors one.** A consumer that adjusts a
projection to suit itself has taken the source's authority and left no record of doing so.

## 10. Realizations

The following are projections. **None of them defines the concept.** A system may have any, all or
none of them:

- a **canonical form**: the governed information in one normal form;
- an **index**: an arrangement that lets something be located or enumerated;
- an **address-resolved form**: references replaced by what they resolve to;
- a **structural rendering**: the constructed structure in a form that can be examined;
- a **vocabulary view**: the named concepts of a system, collected;
- an **evidence view**: a derived representation of evidence or provenance information, arranged for
  consumption. Evidence, Attestation & Provenance owns what evidence *is*. This is a projection of
  it.

Each is a projection because it satisfies §2, not because it appears here. A realization may
introduce a projection this list does not name. It has still introduced a projection, and this
document governs it the same way.

## 11. What a projection is not

- **Not a source.** Nothing is declared into it (§5).
- **Not a cache.** A cache is an optimization, and its absence is a miss to fill. A projection is a
  governed representation. Where a snapshot must carry it, its absence is incompleteness (SN-4).
  People conflate the two easily, because both can be recomputed. They differ in what their absence
  means.
- **Not a summary.** Someone composes a summary by judging what matters. A declared derivation
  produces a projection. Judgment about what matters lives in the projection's contract, where it
  was declared and admitted.
- **Not a copy**, though a projection may carry everything its source does. Derivation under a
  contract makes it a projection, not how much it omits.

## 12. What this document does not specify

- **What projections a system has.** A profile selects them, or a kind contract requires them.
- **How a projection is encoded, stored or transported.**
- **What derivations are available.** Any derivation serves that is declared, deterministic, and
  consults only its source.
- **Whether projections are materialized or derived on demand** (§6).

## 13. Normative invariants

- **PJ-1.** A projection MUST have a defined source and a declared derivation (§2, §3).
- **PJ-2.** A derivation MUST be deterministic and MUST consult nothing but its source (§3).
- **PJ-3.** Every projection MUST be governed by a projection contract stating its source, its
  selection, and its derivation (§3.1).
- **PJ-4.** A projection MUST make no claim its source does not entail (§4).
- **PJ-5.** A projection MUST NOT supply a default, resolve an ambiguity, infer, or silently transform
  an unresolved condition into a resolved one. Where its source does not determine what it would
  carry, the derivation MUST refuse (§4.2).
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

A projection conforms when all of the following hold:

- its source and derivation are declared;
- its derivation is deterministic and consults nothing else;
- it carries what its contract says and adds nothing;
- it regenerates identically from its source;
- it entails nothing that contradicts another projection of the same source.

**Regeneration, not inspection, establishes faithfulness.** Reading a projection cannot reveal a
claim its source does not entail. The added claim looks exactly like a derived one. That is why §4.2
calls it the most dangerous failure. Deriving again and comparing reveals it. Anything that differs
was not derived from the source.

The Conformance Test Specification owns how that is required and evaluated.
