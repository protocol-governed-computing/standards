# Open PGC Standard — Document Set

This document is the map of the Open Protocol-Governed Computing Standard. It states what the
standard contains, how its documents relate, how they are addressed, and what makes a document a
member of the family.

It gives no motivation and defines no architecture. Part 0 makes the case. Parts I–VII specify the
standard.

**Normative status.** Part 0 is non-normative with respect to governed systems: it requires nothing
of them. This document is the one exception, and only in one direction. **§3–§6 are normative about
the documents of this family.** They say nothing about anything a family document governs.

## 1. Structure

The family has seven normative parts. Each part answers one question. Non-normative front matter
comes before them, and a non-normative annex comes after.

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
| **Annex** | How has it been realized, and how is it adopted? *(non-normative)* |

The parts form a **dependency order, not a pipeline.**

- Every other part presupposes Part I.
- Part II defines what governs. Part III defines what is governed at execution. Neither can be
  derived from the other.
- Part IV depends on Parts II and III.
- Part V depends on Part III.
- Part VI constrains Parts I–V. It does not follow them.
- Part VII applies to all of the above, and to itself.

Two subjects cut across the parts:

- **Evidence** serves execution, construction and conformance alike. The family places it where it
  originates, in Part III.
- **Supersession** governs how any governed thing is replaced, including the documents of this
  family. It sits with identity and change, in Part IV.

## 2. Document map

A file identifier is an **address, not an identity**. Its digit names the part, and its letter names
the position within the part. Documents refer to one another **by name**. Nothing normative depends on
an identifier, so a document can move to a new address without breaking any reference. For the same
reason, an invariant identifier carries its document's prefix — `MB-`, `CA-`, `SM-` — and never the
document's file identifier.

| File | Part | Document | Invariants |
|---|---|---|---|
| `0a` | 0 | Problem and Motivation | — |
| `0b` | 0 | Diagnosis and Principles | — |
| `0c` | 0 | Visual Representation of the Standard | — |
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
| `4e` | IV | Supersession | SU-1 … SU-12 |
| `5a` | V | Governed Interaction Boundary | IB-1 … IB-15 |
| `5b` | V | Governed Inspection | IN-1 … IN-16 |
| `6a` | VI | Normative Platform Profile | NP-1 … NP-12 |
| `6b` | VI | Execution Environment Profiles | EE-1 … EE-8 |
| `6c` | VI | Domain Profiles | DP-1 … DP-11 |
| `7a` | VII | Conformance Model | CF-1 … CF-14 |
| `7b` | VII | Conformance Test Specification | CD-1 … CD-17 |
| `8a` | Annex | Implementation Guidance | — |
| `8b` | Annex | Migration and Adoption | — |

Draft material is not an approved document. Drafts live in `spec/holding/`. They are named by subject,
not by identifier, and they carry no authority.

## 3. The derivation rule

Every normative statement in this family MUST be derivable along one path:

```
CONCEPT  →  SEMANTICS  →  NORMATIVE REQUIREMENT  →  CONFORMANCE
```

Each step builds on the one before:

1. A concept is named and bounded.
2. Its semantics are stated independently of any representation.
3. A requirement is stated over those semantics.
4. Conformance is stated as an observable demonstration of the requirement.

**The inverse path is not admissible.** The family must not describe what an implementation does and
then declare that description to be the standard. A realization informs the family in three ways. It
exposes concepts that were missing, distinctions that were conflated, and requirements that could not
be met. It never supplies authority. When a document and a realization disagree, the document
governs, and a ruling resolves the disagreement.

**The family starts from semantic distinctions, not implementation boundaries.** Suppose a
realization exposes a distinction the standard does not carry. The right question is which semantic
concept was missing. The wrong question is which document to create for the code that happens to
exist. A part, document or section that exists because a component exists is a defect.

## 4. Editorial rules

- **One subject per document.** Where history fused two subjects in one document, the fusion is a
  defect, and the subjects must be separated. A document MAY carry two subjects only when keeping them
  apart is itself the normative content. *Identity & Addressing* is the one such case.
- **Semantics before representation.** Every document defines the semantic object first. Its
  encoding, if it has one, comes second and is non-normative.
- **No architecture in normative text.** Component names, module boundaries, process counts and
  directory layouts belong in the annex. If a normative sentence cannot be stated without naming a
  component, it is about the wrong subject.
- **Terminology is load-bearing.** A term defined in Part I keeps exactly that meaning everywhere.
  Whoever renames a concept revises the whole family.
- **Closed sets are declared closed.** Each closed set comes with the procedure by which a revision
  extends it.
- **Openness is a requirement, not a courtesy.** Where an implementation choice is permitted, the
  document says so. Silence is not permission.

## 5. Membership

A document belongs to this family when it does all of the following:

- it declares which part it occupies;
- it derives its requirements along the path in §3;
- it states its conformance obligations in terms that an independent implementation could
  discharge; and
- it introduces only terms that Part I defines or that the document defines itself.

### 5.1 Revision

A document changes by revision. **A revision supersedes the revision it replaces**, in exactly the
sense that Supersession specifies (`4e` §9). The supersession is declared, never inferred from a
number or a date. Referential closure and blast radius apply to family documents just as they apply to
anything else.

- **A revision is proposed against a named predecessor.** It states what it changes and what that
  change invalidates.
- **Experience from a realization may occasion a revision.** A realization exposes concepts that
  were missing, distinctions that were conflated, and requirements that could not be met. A family
  with no path for that evidence either freezes, or whoever holds the code quietly amends it. But
  such evidence may not decide the outcome. It occasions a ruling. It is not itself a ruling (§3).
- **A conformance claim is made against a named revision** (CF-1). A later revision does not reach
  back into claims discharged against an earlier one.

Whoever maintains this family decides who proposes, reviews and admits a revision. The family itself
does not decide it.

### 5.2 Projection

**A machine-readable rendering of this family is a projection, in the Projection Standard's sense,
and the Projection Standard governs it.** This is the third place where the family applies its own
rules to itself:

1. Part VII applies to itself (§1).
2. Supersession governs the replacement of these documents (§1, `4e` §9).
3. A derivation from these documents is a projection.

All three follow from the same reason. Suppose a family specifies how derived representations
behave, and then derives a representation of itself under no rule. It has placed its own derivation
outside the standard it asserts.

- **The prose is the source.** When a projection and these documents disagree, **these documents
  govern** (PJ-7). A projection is not a second statement of the family, and it carries no authority
  of its own (PJ-11).
- **A projection MUST have a declared contract** that states its source, its selection and its
  derivation (PJ-3). The contract declares what the projection carries and what it does not. So an
  absent element is never ambiguous: the reader can tell a deliberate exclusion from a loss.
- **A projection MUST be regenerable** from the documents alone (PJ-9), and **MUST NOT be authored
  into or edited** (PJ-8).
- **Lossy is not unfaithful** (`4b` §4.1). Consider a projection that carries requirement identities
  and their references, but not the sections that supply their substance. It is faithful **if its
  contract says so**. It is unfaithful if it presents itself as carrying the obligations whole.

**Nothing here requires such a projection to exist.** Where one exists, the rules above govern it.

## 6. Claims

**A named subject always makes a PGC conformance claim, against a named profile and a named revision
of this family.** No conformance claim is unqualified. The Conformance Model specifies which
subjects are admissible and what discharges each claim.

## 7. Where to start

| To understand | Read |
|---|---|
| why this exists | Part 0 |
| the shape of all of it, before the detail | `0c` |
| what the terms mean | `1a`, then `1b` |
| what must be true of any realization | `1c` |
| how governance works | Part II, beginning at `2a` |
| what a running system does | Part III, beginning at `3a` |
| how a system is built and changed | Part IV |
| how a system is reached | Part V |
| how a concrete platform is specified | Part VI |
| how any of it is established | Part VII |
| how an organization adopts it | `8b`, after the parts above |

An implementer starting work reads Part I in full. Next they read the parts that cover the subjects
they intend to realize. They read Part VII before claiming anything.
