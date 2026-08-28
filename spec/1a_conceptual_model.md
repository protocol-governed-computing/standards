# Conceptual Model & Terminology

## 1. Scope

This document establishes the vocabulary of Protocol-Governed Computing and the relations
among its concepts. It is the first document of the family: every other document uses these
terms with exactly the meanings specified here.

It defines concepts, not representations. A concept defined here says what a thing *is* and
what distinguishes it from its neighbours; how such a thing is encoded, stored, named, or
built is specified elsewhere. A conforming realization may represent any concept here in any way
that carries its meaning without loss.

This document defines no artifact kind, states no execution behavior, and imposes no
structure on an implementation. Its normative content is the model in §3, the definitions in
§4–§11, and the usage rules in §12, carried as CM-1 … CM-8 (§13).

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. How the definitions work

Each entry states what the concept *is*. Where a concept is routinely confused with a
neighbour, the entry also states what it is **not** — those exclusions are normative. A
definition that draws a distinction draws it because collapsing it has consequences
elsewhere in the family.

Three rules govern the vocabulary as a whole:

- **A concept is defined once.** Where a later document needs more than this one supplies, it
  refines the concept it inherits; it does not redefine the term.
- **A definition is independent of representation.** No definition here may be read as
  requiring a file, a format, a component, a process, or a stage.
- **A term not defined here is not a PGC term.** A document that needs a new one defines it
  locally and says so, or the vocabulary is revised (§12).

## 3. The conceptual model

The definitions in §4–§11 give the concepts. This section gives the model: which concepts
stand in which relations. The model is normative — a realization may represent these
concepts however it likes, but it may not relate them differently.

### 3.1 The four levels

Software governance is conventionally a *practice* — something people do around software.
PGC's central move is to carry it *inside* the software as content the software itself
consumes. Four levels must therefore be held apart, because the same word is used for all of
them in ordinary usage:

| Level | What it is |
|---|---|
| **Governance** | the discipline: establishing, enforcing, verifying, evolving, and retiring the conditions under which software may act and may change |
| **Governance system** | the authorities, rules, mechanisms, and evidence through which a particular software system is governed |
| **Governance artifacts** | the declarative representations of that system — the form in which it is carried |
| **Behavior** | the execution that results from those declarations |

A statement true at one level is routinely false at another. A governance system may be
sound while its artifacts are incomplete; artifacts may be complete while the behavior they
produce is inadequate.

This family occupies the **arrows**, not any single level:

```
Governance ──▶ Governance system ──▶ Governance artifacts ──▶ Behavior
                    └──────── what PGC standardizes ────────┘
```

**PGC standardizes the semantics by which a governance system is carried as artifacts, and by
which those artifacts determine construction and execution.** A reader asking whether PGC is a
governance standard, a software architecture, or an execution model is asking a question with
one answer: it makes governance into machine-consumable system content and defines how that
content determines what is built and what runs.

Not every artifact is a governing element. An artifact is the unit of declared content; it is
a governing element only when what it declares governs another subject. A workflow, a
capability contract, and a constitution are all artifacts; only the last of the three is
necessarily a governing element. Collapsing the two would erase the difference between
governed content and the governance over it.

### 3.2 The relations

Every relation the family relies on is one of these:

| Relation | Holds between | Meaning |
|---|---|---|
| **declares** | artifact → what it states | the artifact is the statement, not a report of one |
| **governs** | governing element → governed subject | the element determines what the subject may be or do |
| **has authority over** | governing element → subject | by what right the element governs |
| **is scoped to** | governing element → extent | how far it reaches |
| **admits** | closure → artifact | the artifact becomes part of the system |
| **composes** | parts → whole | separately owned parts become one governed whole |
| **exposes** | domain → surface | what is reachable across a boundary |
| **constructs** | declarations → snapshot | authorized representation is produced |
| **executes** | runtime × snapshot → result, evidence | determined behavior is realized |
| **evidences** | record → determination or occurrence | what happened can be established afterwards |
| **transforms** | baseline × purpose → baseline | one governed state becomes the next |
| **supersedes** | governed thing → governed thing | one replaces another, references resolved |
| **conforms to** | subject → requirements | the subject satisfies them, demonstrably |

Two rules constrain the relation set. **No relation may be inferred from another** — that an
element is scoped to a subject does not give it authority over that subject, that an artifact
is present does not mean it was admitted, that a thing was constructed does not mean it
conforms. And **no relation may be inferred from position** — containment, ordering,
location, and load order relate nothing.

### 3.3 The three activities

A governed system's life consists of exactly three activities over four states:

```
purpose ──transforms──▶ declarations ──constructs──▶ snapshot ──executes──▶ result + evidence
              │                                          │                       │
              └──────────────── the prior snapshot is the baseline ──────────────┘
                                       evidence of each activity is retained
```

- **Transformation** determines what the declarations are. Its input includes the current
  baseline; a system whose baseline did not change did not change.
- **Construction** determines whether those declarations may exist and produces the
  authorized representation. It decides admissibility, never adequacy.
- **Execution** realizes what the snapshot already determines. It originates nothing.

Each activity produces evidence, and each is itself a governed subject — including
transformation, which is why the loop closes rather than running off the end.

This is a model of *activities and their authority*, not of components. One agent may perform
all three; three agents may divide one. What may not vary is which activity holds which
authority: **construction determines what may be executed; execution realizes what the
snapshot determines.** Neither may take the other's part. The authority chain runs

```
governance → declarations → construction → authorized snapshot → execution
```

and each link determines the next without reaching past it. Behavior is determined by the
declarations and carried by the snapshot; construction determines which declarations are
authorized to reach it. Everything the family requires about determinism, replay, refusal, and
evidence follows from that division rather than being added to it.

## 4. Foundational concepts

**Protocol-Governed Computing (PGC).** A model of computing in which what software may
construct and may execute is determined by explicit, versioned, machine-consumable
declarations, and in which nothing may be constructed or executed that those declarations do
not authorize.

**Governed system.** A system whose behavior and construction are determined by declarations
rather than by the code that realizes it. A system is governed to the extent that removing
its governing declarations would leave it unable to act, not merely unsupervised.

**Declaration.** A statement of what *is*, made in a form a machine can consume and act on.
A declaration is not a description of something decided elsewhere; it is the thing itself
being decided. Declarations are the substance of PGC.

- *Distinguish from documentation.* Documentation describes a system and has no effect on it.
  A declaration determines the system, and a system that diverges from it is in violation
  rather than out of date.
- *Distinguish from configuration.* Configuration parameterizes behavior that already exists.
  A declaration establishes whether the behavior exists at all.

**Declarative.** The property of stating governed facts, constraints, relationships, and
permitted behavior without prescribing the procedure by which they are realized. A declarative
statement may state what must, may, or must not occur; what it does not carry is the control
procedure that brings it about.

- *Distinguish from imperative.* The line is not *what* against *what to do* — an obligation
  states what must be done and is declarative. The line is between the governed semantics and
  the steps that realize them: the first is declared, the second is not part of the
  declaration.

**Artifact.** A single, bounded, identified declaration, together with everything needed to
interpret it. The artifact is the unit of identity, of governance, and of change: things are
governed, versioned, superseded, and referenced one artifact at a time.

**Artifact kind.** The classification that determines what an artifact declares, what it must
carry, and what may be said about it. The kind is a property of the artifact, established by
declaration and never inferred from the artifact's name, location, or content.

**Governed subject.** Whatever a governing element applies to — an artifact, a class of
artifacts, a construction, an execution, a boundary, or another governing element. Governance
is always governance *of* something; a governing element with no subject governs nothing.

## 5. Governance

**Software governance.** The establishment, enforcement, verification, evolution, and
retirement of the rules, constraints, authorities, and evidence that determine what software
**may do, must do, and must not do** within a defined context of use, across its lifecycle,
in pursuit of a defined purpose.

The definition has four dimensions and one span, and both are load-bearing:

| Dimension | Establishes |
|---|---|
| **Rules** | normative requirements — what must hold |
| **Constraints** | limits on behavior — what may and may not occur |
| **Authorities** | who or what may authorize an action or a change |
| **Evidence** | demonstration that the rules were in fact followed |

The **span** is the whole lifecycle, from inception to retirement. Governance that covers
what software does but not who may change what it does is incomplete in the dimension that
matters most: *who or what is allowed to change what the software does* is a governance
question, not a process question, and this family treats it as one throughout.

**Governance.** In this family, the unqualified term **governance** always means *software
governance* as defined above. Wherever governance appears without qualification, it is the
governance of the software itself — its construction, its execution, and its change.

- *Distinguish from governance as subject matter.* A governed system may have a domain whose
  business is governing something in the world — agents, transactions, licences, people. That
  domain is an application built with this family, and its rules are business declarations
  like any other. It is not the governance this family defines, and the two MUST NOT be
  conflated: one determines what the software may do, the other is what some software does.
- *Distinguish from adjacent governance disciplines.* Corporate, data, hardware, and IT
  governance are outside this family's scope. Where a governed system must satisfy an
  obligation originating in one of them, that obligation enters as a declaration like any
  other and is governed as software governance from that point on.
- *Distinguish from review.* Review is an activity performed on a system by people, producing
  a judgment about it. Governance is content the system holds, which determines what it can
  do. A system passes review and remains ungoverned if nothing in it changed.
- *Distinguish from policy.* A policy is a statement of intent, enforceable only insofar as
  something enforces it. A governing declaration is not separable from its enforcement: an
  unenforced governing declaration is a defect, not a weaker form of governance.

In PGC governance is a property of the system, carried inside it as declarations the system
itself consumes — not a discipline applied to the system from outside (§3.1).

**Governing element.** A declaration whose subject is another part of the system rather than
behavior of its own. Governing elements determine what may exist, what must hold, who may
act, and what is exposed.

**Authority.** The capacity of a governing element to bind a subject — the answer to *by what
right does this determine that?* Authority is declared, never assumed and never acquired by
position: an element does not govern a subject because it precedes it, contains it, or was
loaded before it.

**Obligation.** A requirement that a governing element places on a subject: something that
must hold of it, or something it must do or must not do. An obligation that nothing can
evaluate is not an obligation.

**Scope.** The extent of a subject over which a governing element applies. Scope answers *how
far*, authority answers *by what right*, and the two are independent: an element may have
authority over a subject and a scope that excludes it.

**Governance closure.** The complete set of governing elements applicable to a subject,
together with the determination of how they compose. A closure is *closed* in the strict
sense: governance may not enter it and may not escape it without that entry or exit being
declared.

**Admission.** The act by which something not previously part of a governed system becomes
part of it. Admission is a governed act with a determination and a result; something is never
part of a system by having been placed where the system would find it.

- *Distinguish from presence.* Presence is a fact about where something is. Admission is a
  fact about what the system has accepted. Nothing is admitted by being present.

The semantics of authority, scope, admission, and closure — how each is determined and
composed — are specified by the Governance Closure & Authority Standard. This document specifies only
that they are distinct concepts and that none may be inferred from another.

## 6. Structure and composition

**Domain.** A bounded region of a governed system that owns its declarations and is
responsible for them. A domain is a governance boundary, not a directory, a package, or a
team.

**Surface.** What a domain or system exposes to another. A surface is declared: what is not
on the surface is not reachable across the boundary, whether or not it exists behind it.

**Composition.** The bringing together of separately owned parts of a governed system into one
governed whole, under a stated basis for their combination. Composition is an act with a
result, not an arrangement that obtains because parts are co-located.

**Profile.** A statement of which facilities of this family a particular governed system
selects, constrains, or requires, and of the conformance claims it must support. A profile
selects; it does not redefine.

**Platform.** A governed composition that provides a defined governance and execution surface
for the workloads and domains composed into it, under a named profile.

- *Distinguish from a thing that can be pointed at.* A platform is constituted by an act of
  composition under a profile. No repository, package, deployment, or installation is a
  platform, however completely it contains one; what makes a platform is the composition and
  the profile it was composed under, neither of which is a location.

What constitutes a particular platform, how platforms relate to the profiles that constitute
them, and whether any platform is minimal, are specified by the Normative Platform Profile.

## 7. Construction

**Construction.** The activity by which authored declarations become an authorized
representation that may be executed. Construction discovers, resolves, validates, constructs,
projects, verifies, and attests; whether one agent or many perform it, and whether it happens
long before execution or immediately before it, is unconstrained.

**Admissibility.** The property of a candidate declaration that it is structurally and
governance-wise sound — that it *may* exist. Admissibility is determined during construction
and is a question about soundness, never about quality, usefulness, or behavioral adequacy.

- *Distinguish from adequacy.* That a thing may exist and that it does what was wanted are
  different determinations with different evidence. Nothing that judges admissibility may
  judge adequacy, or the two become one unexaminable act.

**Resolution.** The act of turning a reference into the thing it refers to. Where the family
requires resolution to happen during construction, an unresolved reference is a failure of
construction and never a condition discovered during execution.

**Projection.** A deterministic, machine-consumable representation of governed information,
derived from a defined source. A projection carries meaning that is already settled; it never
adds meaning of its own.

**Sealing.** The act that renders a constructed representation immutable and gives it an
identity derived from its content. After sealing, the representation cannot change without
becoming a different representation.

**Snapshot.** A sealed representation of a governed system, complete enough to be executed
and identified by its content. The snapshot is what execution consumes.

**Baseline.** The snapshot that defines what a governed system currently *is* — the state any
change transforms. A system has exactly one baseline at a time.

## 8. Execution

**Execution.** The activity of realizing behavior that a snapshot already determines.
Execution produces results and evidence; it originates no behavior.

**Runtime.** The agent that performs execution. A runtime is defined by what it may not do:
it holds no domain meaning, makes no governing determination, and adds nothing to the
snapshot it executes. A runtime is a role, not a component; a realization may perform it with
any number of programs or processes.

**Workflow.** A declared structure of governed steps and the transitions among them. A
workflow states what may happen and in what order; it is executed according to its declared
transitions, and execution neither infers nor invents a transition the workflow does not
declare.

**Step.** A position in a workflow's declared structure at which a capability is reached and one
of its declared outcomes reported. A step is part of the structure the workflow declares, never a
unit of work formed while the workflow runs.

**Capability.** A governed unit of execution through which a system reaches computational or
external effect, reachable only through its declared contract.

**Contract.** The declared interface of a capability: its inputs, outputs, and enumerated
outcomes. The contract is the entire interface — nothing below it is visible to execution,
which is why realizations of a capability are interchangeable.

**Outcome.** One of the enumerated results a contract declares. An outcome that is not
enumerated cannot occur; if a realization can produce one, the contract is wrong.

**Governed state.** State whose location, ownership, and permitted transitions are determined
by declaration. Execution maintains governed state but does not own it and does not decide
its shape.

**Side effect.** An effect of execution that is not confined to the governed system's own
state. Side effects are declared and closed: a system's ability to affect the world is part
of what is governed about it.

**Refusal.** The determined response to a requirement that cannot be satisfied: the act does
not occur, and the reason is recorded. Refusal is a governed outcome, not an error condition
and not a failure of the mechanism that produced it.

- *Distinguish from degradation.* Degradation continues in a reduced form and hides the
  violation that caused it. Refusal stops and makes the violation the result.

## 9. Evidence

**Evidence.** The record by which a determination, a construction, or an execution can be
established afterwards by a party that did not observe it. Evidence is produced as a
governed obligation, not as a byproduct of running.

**Trace.** Evidence of an execution: the account of what occurred, written as execution
proceeds and never read back as an input. What is not in the trace did not happen.

**Attestation.** An assertion, by an identified party, about the integrity or origin of a
record or artifact. Attestation is about a thing; evidence is about an event.

**Provenance.** The derivation relation between a governed thing and what it came from.
Provenance answers *where did this come from*, evidence answers *what happened*, and
attestation answers *who vouches for it*.

**Determinism.** The property that the same governed input, against the same sealed
representation and the same initial state, determines the same result and the same governed
consequences, and that the evidence of the execution remains sufficient to establish that
determination. Determinism is a consequence of where behavioral authority sits, not a feature
added to an execution agent.

- *Distinguish from byte-identical evidence.* Evidence may carry observational material —
  when a thing occurred, what vouched for it, what the environment was — that varies between
  executions without any governed consequence varying. Which parts of evidence are
  deterministic and which are observational is specified by the Evidence, Attestation &
  Provenance Standard; determinism is a property of the determination, not of the record's
  every byte.

**Replay.** Reproduction of a past execution by executing the same sealed representation
against the same inputs and initial state. Replay is structural: it re-executes an artifact
rather than reconstructing an environment.

## 10. Change

**Transformation.** The governed act by which one baseline becomes the next. Transformation is
itself a governed subject with its own declarations, determinations, and evidence — not a
process that surrounds a governed system and is exempt from it.

- *Distinguish from authoring.* Authoring produces a new thing beside the system. A
  transformation takes an existing baseline as its input and produces the next one; a system
  whose baseline did not change did not change.

**Candidate.** A proposed part of a governed system that has been produced but not yet
admitted. A candidate does not exist as far as the system is concerned.

**Promotion.** The act that installs an admitted candidate as the new baseline — the moment a
governed system changes. Promotion verifies integrity and re-judges nothing: every
determination it relies on was made before it.

**Supersession.** The relation by which one governed thing replaces another, and the rules
determining what becomes of references to what was replaced. Supersession is declared; nothing
is superseded by being deleted, renamed, or left unused.

**Version.** A declared identifier of an artifact's semantics. A change of representation that
preserves meaning is not a version change; a change of meaning is, whether or not the
representation changed.

## 11. Conformance

**Conformance.** The relation between a subject and the requirements governing it: the subject
satisfies them, and there is evidence sufficient for an independent party to determine so.

**Conformance subject.** What a conformance claim is about — an artifact, a governed
representation, an execution, an implementation, or a system instance. These are five
different claims with five different discharges, and a claim that does not name its subject
is not a claim.

**Enforcement.** What a governed system does when a requirement applies to it: evaluate,
determine, and act — including refusing. Enforcement is the system's behavior; conformance is
a judgment about the system. A system may enforce perfectly and fail to conform.

**Invariant.** A property required to hold of a governed system at all times, rather than at
one moment or on one path. An invariant that holds only where something checks it is not an
invariant of the system; it is a property of that check.

## 12. Normative usage

- A document of this family MUST use the terms defined here with the meanings defined here.
- A document MUST NOT redefine a term defined here. Where it needs more, it MUST refine the
  inherited concept and say what it is refining.
- A document that introduces a term not defined here MUST define it, and MUST NOT define it
  such that it overlaps a term defined here. Two names for one concept is a defect.
- A distinction drawn in §4–§11 as *distinguish from* MUST be preserved. A document that
  treats two distinguished concepts as one is non-conforming, whether or not its requirements
  are otherwise sound.
- A profile MUST NOT alter the meaning of any term defined here. Selecting facilities is
  permitted; renaming or re-scoping a concept is not.
- A term MUST be defined by the document whose subject matter principally establishes it. A term
  required to understand several parts of the family, whose identity does not depend on any one
  later standard's mechanism, belongs here; a term that exists principally because of a later
  standard's subject matter belongs to that standard, and this document MUST NOT define it.
  **Ownership follows semantic primacy, never the order in which documents appear** — the contrary
  rule would make this document a warehouse for every term that was written down first.
- Adding, removing, or altering a definition here is a revision of this document, and requires
  every document that used the affected term to be re-examined. Terminology change is never
  editorial.

## 13. Normative invariants

- **CM-1.** A document of this family MUST use the terms defined here with the meanings defined
  here (§12).
- **CM-2.** A document MUST NOT redefine a term defined here; where it needs more, it MUST refine the
  inherited concept and state what it is refining (§12).
- **CM-3.** A document introducing a term not defined here MUST define it, and MUST NOT define it so
  as to overlap a term defined here (§12).
- **CM-4.** A distinction drawn in §4–§11 as *distinguish from* MUST be preserved by every document
  that relies on it (§12).
- **CM-5.** A profile MUST NOT alter the meaning of any term defined here (§12).
- **CM-6.** A document MUST relate the concepts as §3 relates them, MUST introduce no relation §3
  does not provide, and MUST NOT draw an inference between relations that §3.2 forbids (§3, §14).
- **CM-7.** Adding, removing, or altering a definition here MUST be a revision of this document, and
  MUST require every document that used the affected term to be re-examined (§12).
- **CM-8.** A term MUST be defined by the document whose subject matter principally establishes it,
  and ownership of a term MUST NOT be assigned by the order in which documents appear (§12).

## 14. Conformance

This document is satisfied by a document, not by an implementation: the conformance subject is
a specification document of this family.

A document conforms to this document when:

- every PGC term it uses is either defined here and used with that meaning, or defined by that
  document itself and non-overlapping with the vocabulary here;
- every distinction marked *distinguish from* that the document relies on is preserved
  throughout it;
- it relates the concepts as §3 relates them, and introduces no relation that §3 does not
  provide and no inference between relations that §3.2 forbids; and
- every term it defines is one its own subject matter principally establishes, rather than one
  belonging here or to another standard; and
- no requirement it states depends on a reading of a term that this document excludes.

A conflict between this vocabulary and another document of the family is a defect in one of
them, resolved by ruling and by revising the document found wrong — never by both documents
carrying a term in two senses.
