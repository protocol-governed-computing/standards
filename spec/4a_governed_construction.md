# Governed Construction

## 1. Scope

This document specifies **governed construction**: the semantics by which authored declarations
become an authorized representation eligible for acceptance and execution under the applicable
standards.

It says what construction determines, what obligations it must discharge, what it must refuse, and
what it may never do. It does **not** specify a mechanism, a pipeline, a stage sequence, or a
moment. A realization may discharge these obligations in one process or many, long before execution
or immediately before it.

The Snapshot Standard specifies what construction produces and what makes it acceptable; the
Projection Standard covers the representations it derives; Identity & Addressing covers how the
things it resolves are named; Governed Transformation covers how the declarations it consumes came
to be what they are.

This document introduces the terms **normalization**, **materialization**, and **composition
obligation**, and refines the Conceptual Model's **candidate**. Every other term it uses is defined by the Conceptual Model, the
Semantic Model, or Parts II–III.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Three levels, kept apart

```
governed construction    the semantic subject — what this document specifies
        │ realized by
compilation              the governed process that realizes it
        │ which may contain
a step named "construct" one implementation operation within that process
```

**This document is about the first.** *Compilation* is the conventional name for the process
realizing governed construction; it requires no compiler-shaped implementation, no particular
ordering, and no phase bearing any particular name. Where this document names an obligation, it is
naming something that must be discharged — never a stage that must exist.

## 3. Construction as a governed transition

Construction is the transition schema of the Semantic Model applied to one subject:

| | In construction |
|---|---|
| `S` | the authorized declarations as they stand |
| `π` | a candidate — a declaration proposed for authorization |
| `C` | the governance closure applicable to that candidate |
| `S′` | the authorized representation |
| `ε` | evidence of what was determined, and on what basis |

*Refining the Conceptual Model's* **candidate**: in construction the candidate is a declaration,
and that it **does not exist as far as the governed system is concerned** holds until a
determination admits it — it is not partially present, not provisionally available, and not
referenceable by anything already admitted.

**Construction receives candidates; it does not author them.** What the declarations should be is
determined elsewhere (§13).

Everything the Semantic Model requires holds without amendment. Construction determines completely
before anything depends on the result, evaluates the whole closure, produces evidence, and refuses
where the closure cannot be established.

## 4. What construction determines

**Construction determines admissibility: whether a candidate may exist within the governed system.**

### 4.1 Admissibility is not adequacy

Two determinations are distinct and MUST NOT be merged:

| | Asks | Answered by |
|---|---|---|
| **Admissibility** | may this exist? is it structurally and governance-wise sound? | construction |
| **Adequacy** | does this do what was wanted? | a separate determination against declared intent |

Construction answers the first and **MUST NOT answer the second**. A declaration may be perfectly
admissible and entirely wrong for its purpose; a system that refused it on those grounds would be
making a judgment about intent that nothing declared.

The separation matters because merging them makes both unexaminable. A single determination that
weighed soundness and usefulness together could not say which consideration refused a candidate,
and could not be checked by anyone who did not share the judgment.

### 4.2 Admissibility never depends on execution

**Construction MUST NOT execute a realization in order to determine admissibility** (AI-3).

Admissibility is a property of declarations and their governance, determinable from them. A
construction that ran an implementation to decide whether it may exist would have:

- made admissibility depend on the behavior of the thing being admitted, which is circular;
- made the determination environment-dependent, and therefore not reproducible;
- moved a governed decision into execution, which is the boundary AI-3 exists to hold.

Verifying that a realization *satisfies its contract's declared shape* is a determination over
declarations. Running it to see what it does is not.

## 5. The obligations of construction

Construction discharges the obligations below. **These are obligations, not stages**: their names
describe what must be established, not steps that must exist, and their relationships form
**dependency constraints** — each may rely only on what its predecessors established — not a
sequence that must be traversed.

| Obligation | Establishes |
|---|---|
| **admission of candidates** | what is being considered, and that nothing else is |
| **normalization** | one normal form: two expressions of one meaning are one thing |
| **resolution** | every reference names exactly one admitted artifact |
| **governance determination** | every applicable rule evaluated, and the candidate's admissibility determined |
| **structure construction** | the executable structure built over the resolved, admitted graph |
| **projection** | the representations downstream consumers read, derived from what was determined |
| **materialization** | those representations rendered into the form that will be carried |
| **verification** | what was carried matches what was determined |
| **attestation** | an assertion, by an identified party, over the verified result |

A realization MAY discharge several in one operation, or one across several, in any organization
that satisfies those constraints. What it MUST NOT do is **leave any undischarged**, or discharge
one on the basis of something a later obligation was supposed to establish.

### 5.1 Nothing enters by discovery

What is under consideration is what was admitted as a candidate. Construction MUST NOT enlarge that
set by scanning, by convention, by inferring from a name or location, or by following something it
happened to find (AI-12). A declaration nothing admitted is not a candidate; it is a file.

## 6. The determination point

There is a point in construction before which **nothing is assumed legal**, and after which
**nothing is re-decided**.

- Everything before it establishes facts: what the candidates are, what they mean in normal form,
  what their references resolve to.
- The determination itself evaluates the applicable closure and determines admissibility.
- Everything after it **operates on the determined result and MUST NOT revisit it.** Projection,
  materialization, verification and attestation build on an admitted result; none of them may admit
  something, refuse something, or alter what was determined. Operating on a determined result is not
  trusting it blindly — §11 requires that what was carried be checked against what was determined.

This is a semantic requirement, not an ordering of stages. A realization that determines
admissibility incrementally satisfies it if, for each candidate, everything depending on that
candidate's legality follows its determination. What it may not do is **carry an undetermined
candidate forward** in the expectation that something later will catch it.

### 6.1 No partial output

**A construction that refuses produces nothing.**

**No usable authorized representation is produced.** There is no partial authorized representation,
no subset that was admissible, no output marked incomplete. This concerns governed output; transient
internal computation a realization performs and discards is not output. A partially admissible system is not a diminished governed system — it is not a governed
system, because what governs the missing part is unknown and what depends on it is undetermined.

A realization that writes as it goes MUST ensure that a refusal leaves nothing behind that anything
could subsequently accept (AI-8).

## 7. Construction refuses; it never repairs

Where a candidate is inadmissible, construction **refuses**. It MUST NOT correct, complete,
substitute, default, or normalize away the problem.

- Normalization resolves *representation* differences between expressions of one meaning. It MUST
  NOT resolve *semantic* differences, and MUST NOT supply what a declaration omitted.
- A missing reference is a refusal, not an opportunity to infer the intended target.
- An unsatisfied obligation is a refusal, not a warning attached to a result that proceeds.

**A construction that repairs is authoring.** Whatever it supplies, no one declared, and the
resulting system contains behavior whose source is a mechanism. That the repair was obvious, or
correct, changes nothing: it was not determined under a closure, so nothing establishes it.

## 8. Construction derives meaning; it does not create it

Construction may derive, compute, resolve, index, and structure. **It MUST NOT originate meaning.**

- What an artifact means is what its declaration says, interpreted under its kind contract and its
  governance. Construction establishes consequences of that meaning; it does not add to it.
- A derived element is not thereby authoritative (GO-9). That construction computed something does
  not make it a source of governance, however useful the computation.
- Where construction cannot determine what something means, it refuses. It does not choose the
  most likely meaning, and does not adopt a convention to break a tie.

This is the construction-side face of a boundary the family holds throughout: a realization may
derive knowledge, and may not assign significance.

## 9. Determinism and reproducibility

**The same declarations, under the same governance closure, MUST produce the same authorized
representation** — including the same identity (SN-2, SM-10).

Consequently:

- Construction MUST NOT depend on anything undeclared: not wall-clock time, not iteration order over
  an unordered collection, not filesystem ordering, not an environment variable, not the identity of
  whoever invoked it.
- **Reproducibility is checkable, and is the practical test of this section**: reconstructing from
  the same declarations yields the same identity, or something undeclared entered.
- Observational content of construction evidence may vary (EV-5); what was determined may not.

A construction that is not reproducible has an undeclared input or an undeclared nondeterministic
dependency, whether or not anyone can say which. Identity mismatch on rebuild is that input becoming
visible.

## 10. Composition obligations

Some obligations **cannot be discharged over a part**, and exist only over the whole:

- **Identity over the composition.** The identity of the authorized representation is derived from
  all of it. No part carries it, and no part can compute it.
- **Agreement among copies.** Where one governing artifact is authorized into several regions of a
  composition, every copy MUST be compared and MUST agree. A composition whose copies of one
  identity differ MUST be refused — the artifacts are not the same artifact, and each region is
  governed by something slightly different from what the others are governed by.
- **Rules that quantify over the whole.** An obligation of the form *no two…*, *every…*, or *exactly
  one…* is determinable only over the complete composition, and MUST be determined there.
- **Determination against what was actually composed.** Composition-wide obligations MUST be
  evaluated against the governance the composition itself carries — never against what a mechanism
  separately believes the governance to be. A region checked against a mechanism's idea of the rules
  has not been checked against its own governance.

A realization that constructs parts independently MUST still discharge these, and MUST refuse the
composition where any fails. **Parts that are each admissible do not compose into an admissible
whole**, and assuming otherwise is how a composition acquires a contradiction no part contains.

## 11. Verification: carrying is not determining

**What was determined and what was carried are two different things, and the difference MUST be
checked.**

Construction determines a result; materialization renders it into the form that will be carried.
Those can differ — through truncation, encoding loss, partial write, or a defect in rendering — and
every downstream guarantee is stated over what was *carried*.

- Verification MUST establish that what was materialized matches what was determined.
- **A verification failure is a refusal, not a correction.** The materialized result is discarded;
  it is not patched to match.
- Verification is not a repetition of the admissibility determination. It does not re-decide
  legality (§6); it establishes fidelity.

This obligation exists because the failure it catches is invisible to every other check: the
determination was right, the output is wrong, and nothing that reads the output can tell.

## 12. Attestation

Construction MAY conclude with an **attestation** over the verified result: an assertion, by an
identified party, over what was constructed. What an attestation is, what it must identify, and what
it does and does not establish are specified by Evidence, Attestation & Provenance; this section
states only how one relates to construction.

- An attestation MUST identify its attesting party and the subject it covers.
- **Attestation does not confer admissibility** (EV-11). It asserts something about a result already
  determined to be admissible; it does not make it so, and an attested inadmissible result remains
  inadmissible.
- Attestation is what allows a party that did not perform the construction to establish what was
  produced — and it is a claim they may accept, not a proof (EV-9).

## 13. What construction does not do

- **It does not execute.** Not to determine admissibility (§4.2), not to test, not to warm anything.
- **It does not judge adequacy** (§4.1).
- **It does not author.** It refuses rather than repairing (§7).
- **It does not decide what the declarations should be.** That is transformation's subject (Governed
  Transformation), and construction takes candidates as given.
- **It does not seal.** Sealing constitutes a snapshot and is specified by the Snapshot Standard;
  construction produces what is sealed.
- **It does not require a stage bearing any name in §5.**

## 14. Normative invariants

- **GC-1.** Construction MUST determine admissibility, and MUST NOT determine adequacy (§4.1).
- **GC-2.** Admissibility MUST be determinable from declarations and governance alone; construction
  MUST NOT execute a realization to determine it (§4.2).
- **GC-3.** Every obligation of §5 MUST be discharged, and none MUST be discharged on the basis of
  something a later obligation was to establish (§5).
- **GC-4.** Only admitted candidates MUST be considered; nothing MUST enter construction by
  discovery (§5.1).
- **GC-5.** Nothing depending on a candidate's legality MUST precede that candidate's determination,
  and nothing after a determination MUST revisit it (§6).
- **GC-6.** A refused construction MUST produce no usable output (§6.1).
- **GC-7.** Construction MUST refuse rather than repair, complete, substitute, or default (§7).
- **GC-8.** Construction MUST NOT originate meaning, and a derived element MUST NOT thereby become
  a source of authority (§8).
- **GC-9.** The same declarations under the same closure MUST produce the same authorized
  representation and the same identity (§9).
- **GC-10.** Construction MUST NOT depend on any undeclared input (§9).
- **GC-11.** Composition obligations MUST be determined over the whole composition, against the
  governance that composition carries (§10).
- **GC-12.** Copies of one identity within a composition MUST agree, or the composition MUST be
  refused (§10).
- **GC-13.** What was materialized MUST be verified against what was determined, and a mismatch MUST
  be a refusal (§11).
- **GC-14.** Attestation MUST NOT confer admissibility (§12).

## 15. Conformance

The conformance subject of this document is a **construction**: a determination of admissibility
over a set of candidates, together with what it produced and the evidence of how it decided.

A construction conforms when it discharged every obligation of §5, determined admissibility without
executing anything, refused rather than repairing, produced nothing on refusal, verified what it
carried against what it determined, and can be reproduced from the same declarations to the same
identity.

**Reproducibility is the demonstration that subsumes the most.** A construction that yields the same
identity from the same declarations, in a different place, at a different time, by a different
party, has established in one observation that nothing undeclared entered it — which no amount of
inspecting a single successful construction can establish.

How this and the remaining obligations are required and evaluated belongs to the Conformance Test
Specification.
