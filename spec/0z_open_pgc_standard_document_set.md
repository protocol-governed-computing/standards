# Open PGC Standard — Document Set

This document is the map of the Open Protocol-Governed Computing Standard: what it contains, how
its documents relate, how they are addressed, and what makes one of them a member of the family.

It explains no motivation and defines no architecture. Part 0 makes the case; Parts I–VII specify
the standard.

**Normative status.** Part 0 is non-normative with respect to governed systems: it requires nothing
of them. This document is the exception, and only in one direction — **§3–§6 are normative about the
documents of this family**, not about anything a family document governs.

## 1. Structure

The family has seven normative parts, each answering one question, preceded by non-normative front
matter and followed by a non-normative annex.

| Part | Question it answers |
|---|---|
| **0** | Why does this exist? *(non-normative)* |
| I — Model | What does PGC mean? |
| II — Governance | What governs what? |
| III — Execution | What does governed execution do? |
| IV — Construction & Transformation | How does governed software come into existence and change? |
| V — Interchange | How is a governed system reached and read? |
| VI — Profiles | How is a concrete PGC system profiled? |
| VII — Conformance | How do we know it conforms? |
| **Annex** | How has it been realized? *(non-normative)* |

The parts are a **dependency order, not a pipeline.** Part I is presupposed by every other part.
Part II defines what governs; Part III what is governed at execution; neither is derivable from the
other. Part IV depends on II and III. Part V depends on III. Part VI constrains I–V rather than
following them. Part VII applies to all of the above, and to itself.

Two subjects are cross-cutting. **Evidence** serves execution, construction, and conformance alike,
and is placed where it originates (Part III). **Supersession** governs how any governed thing is
replaced — including the documents of this family — and sits with identity and change (Part IV).

## 2. Document map

A file identifier is an **address, not an identity**: a digit for the part, a letter for the position
within it. Documents refer to one another **by name**; nothing normative depends on an identifier, so
a document may be re-addressed without invalidating a reference. For the same reason an invariant
identifier carries its document's prefix — `MB-`, `CA-`, `SM-` — and never its file identifier.

| File | Part | Document | Invariants |
|---|---|---|---|
| `0a` | 0 | Problem and Motivation | — |
| `0b` | 0 | Diagnosis and Principles | — |
| `0c` | 0 | Migration and Adoption | — |
| `0d` | 0 | Visual Representation of the Standard | — |
| `0z` | 0 | Open PGC Standard — Document Set | — |
| `1a` | I | Conceptual Model & Terminology | CM-1 … CM-8 |
| `1b` | I | Semantic Model | SM-1 … SM-12 |
| `1c` | I | Architectural Invariants | AI-1 … AI-17 |
| `2a` | II | Governance Standard | GS-1 … GS-9 |
| `2b` | II | Governance Semantic Ontology | GO-1 … GO-12 |
| `2c` | II | Machine Block | MB-1 … MB-15 |
| `2d` | II | Kind Vocabulary | KV-1 … KV-10 |
| `2e` | II | Governance Closure & Authority | CA-1 … CA-12 |
| `2f` | II | Enforcement & Refusal | EN-1 … EN-14 |
| `3a` | III | Execution Model | EX-1 … EX-16 |
| `3b` | III | Snapshot | SN-1 … SN-14 |
| `3c` | III | Runtime | RT-1 … RT-13 |
| `3d` | III | Capability | CP-1 … CP-11 |
| `3e` | III | Evidence, Attestation & Provenance | EV-1 … EV-17 |
| `4a` | IV | Governed Construction | GC-1 … GC-14 |
| `4b` | IV | Projection | PJ-1 … PJ-12 |
| `4c` | IV | Identity & Addressing | ID-1 … ID-15 |
| `4d` | IV | Governed Transformation | TR-1 … TR-25 |
| `4e` | IV | Supersession | SU-1 … SU-11 |
| `5a` | V | Governed Interaction Boundary | IB-1 … IB-15 |
| `5b` | V | Governed Inspection | IN-1 … IN-16 |
| `6a` | VI | Normative Platform Profile | NP-1 … NP-12 |
| `6b` | VI | Execution Environment Profiles | EE-1 … EE-8 |
| `6c` | VI | Domain Profiles | DP-1 … DP-11 |
| `7a` | VII | Conformance Model | CF-1 … CF-14 |
| `7b` | VII | Conformance Test Specification | CD-1 … CD-17 |
| `8a` | Annex | Implementation Guidance | — |

Draft material is not an approved document. Drafts live in `spec/holding/`, are named by subject
rather than identifier, and carry no authority.

## 3. The derivation rule

Every normative statement in this family MUST be derivable along one path:

```
CONCEPT  →  SEMANTICS  →  NORMATIVE REQUIREMENT  →  CONFORMANCE
```

A concept is named and bounded; its semantics stated independently of representation; a requirement
stated over those semantics; conformance stated as an observable demonstration of it.

**The inverse path is not admissible** — describing what an implementation does and declaring the
description to be the standard. A realization informs this family by exposing concepts that were
missing, distinctions that were conflated, and requirements that could not be met; it never supplies
authority. Where a document and a realization disagree, the document governs and the disagreement is
resolved by ruling.

**The family proceeds from semantic distinctions, not implementation boundaries.** When a realization
exposes a distinction the standard does not carry, the question is which semantic concept was
missing — not which document should be created for the code that happens to exist. A part, a
document, or a section that exists because a component exists is a defect.

## 4. Editorial rules

- **One subject per document.** Where two subjects were historically fused, the fusion is a defect to
  be separated. A document MAY carry two only where keeping them apart is itself the normative
  content — *Identity & Addressing* is the one such case.
- **Semantics before representation.** Every document defines the semantic object first; its
  encoding, if any, second and non-normatively.
- **No architecture in normative text.** Component names, module boundaries, process counts, and
  directory layouts belong to the annex. A normative sentence that cannot be stated without naming a
  component is about the wrong subject.
- **Terminology is load-bearing.** A term defined in Part I is used with exactly that meaning
  everywhere. Renaming a concept is a family-wide revision.
- **Closed sets are declared closed**, with the procedure by which a revision extends them.
- **Openness is a requirement, not a courtesy.** Where an implementation choice is permitted, the
  document says so. Silence is not permission.

## 5. Membership

A document belongs to this family when it:

- declares which part it occupies;
- derives its requirements along §3;
- states its conformance obligations in terms an independent implementation could discharge; and
- introduces no term that Part I does not define or that it does not itself define.

### 5.1 Revision

A document changes by revision, and **a revision supersedes the revision it replaces** in exactly
the sense Supersession specifies — declared, not inferred from a number or a date, with referential
closure and blast radius applying to family documents as to anything else (`4e` §9).

- **A revision is proposed against a named predecessor**, states what it changes, and states what
  that invalidates.
- **Experience from a realization may occasion a revision.** A realization exposes concepts that
  were missing, distinctions that were conflated, and requirements that could not be met — and a
  family with no path for that evidence either ossifies or is quietly amended by whoever holds the
  code. What such evidence may not do is decide the outcome: it occasions a ruling, it is not one
  (§3).
- **A conformance claim is against a named revision** (CF-1). A later revision does not reach
  backwards into claims discharged against an earlier one.

Who proposes, reviews, and admits a revision is a property of whoever maintains this family, not of
the family itself.

### 5.2 Projection

**A machine-readable rendering of this family is a projection in the Projection Standard's sense, and
is governed by it.** This is the third place the family applies its own rules to itself: Part VII
applies to itself (§1), Supersession governs the replacement of these documents (§1, `4e` §9), and a
derivation from them is a projection.

The reason is the same one that makes the other two necessary. A family that specifies how derived
representations behave, and then derives one of itself under no rule, has placed its own derivation
outside the standard it is asserting.

- **The prose is the source.** Where a projection and these documents disagree, **these documents
  govern** (PJ-7). A projection is not a second statement of the family and carries no authority of
  its own (PJ-11).
- **A projection MUST have a declared contract** stating its source, its selection, and its
  derivation (PJ-3). What it carries and what it does not is declared, so that an absent element is
  never ambiguous between deliberately excluded and lost.
- **It MUST be regenerable** from the documents alone (PJ-9), and **MUST NOT be authored into or
  edited** (PJ-8).
- **Lossy is not unfaithful** (`4b` §4.1). A projection carrying requirement identities and their
  references, and not the sections that supply their substance, is faithful **if its contract says
  so** — and unfaithful if it presents itself as carrying the obligations whole.

**Nothing here requires that such a projection exist.** Where one does, it is governed as above.

## 6. Claims

**A claim of PGC conformance is always a claim by a named subject, against a named profile and a
named revision of this family.** There is no unqualified conformance claim. What the admissible
subjects are, and what discharges each, is specified by the Conformance Model.

## 7. Where to start

| To understand | Read |
|---|---|
| why this exists | Part 0 |
| the shape of all of it, before the detail | `0d` |
| what the terms mean | `1a`, then `1b` |
| what must be true of any realization | `1c` |
| how governance works | Part II, beginning at `2a` |
| what a running system does | Part III, beginning at `3a` |
| how a system is built and changed | Part IV |
| how a system is reached | Part V |
| how a concrete platform is specified | Part VI |
| how any of it is established | Part VII |

An implementer beginning work reads Part I in full, then the parts covering the subjects they
intend to realize, then Part VII before claiming anything.
