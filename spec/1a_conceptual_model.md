# Conceptual Model & Terminology

## 1. Scope

This document sets out the vocabulary of Protocol-Governed Computing and the relations among its
concepts. It is the first document of the family. Every other document uses these terms with exactly
the meanings given here.

This document defines concepts, not representations. A definition here says what a thing *is* and
what sets it apart from its neighbours. Other documents specify how a realization encodes, stores,
names or builds that thing. A conforming realization may represent any concept here in any way that
carries its full meaning.

This document defines no artifact kind. It states no execution behavior. It imposes no structure on
an implementation. Its normative content is:

- the model in §3;
- the definitions in §4–§11;
- the usage rules in §12, carried as CM-1 … CM-8 (§13).

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. How the definitions work

Each entry states what the concept *is*. Some concepts are often confused with a neighbour. For
those, the entry also states what the concept is **not**, and those exclusions are normative. A
definition draws a distinction only where merging the two concepts would cause harm elsewhere in the
family.

Three rules govern the vocabulary as a whole:

- **A concept is defined once.** A later document that needs more than this one supplies refines the
  concept it inherits. It does not redefine the term.
- **A definition is independent of representation.** No definition here requires a file, a format,
  a component, a process or a stage.
- **A PGC term is a term defined here.** A document that needs a new term defines it locally and
  says so. Otherwise the vocabulary must be revised (§12).

## 3. The conceptual model

The definitions in §4–§11 give the concepts. This section gives the model: which concepts stand in
which relations. The model is normative. A realization may represent these concepts however it
likes, but it must relate them as the model relates them.

### 3.1 The four levels

People usually treat software governance as a *practice*: something they do around software. PGC
moves governance *inside* the software, as content the software itself consumes. So this family must
keep four levels apart. Ordinary usage applies the same word to all four.

| Level | What it is |
|---|---|
| **Governance** | the discipline: establishing, enforcing, verifying, evolving, and retiring the conditions under which software may act and may change |
| **Governance system** | the authorities, rules, mechanisms, and evidence through which a particular software system is governed |
| **Governance artifacts** | the declarative representations of that system — the form in which it is carried |
| **Behavior** | the execution that results from those declarations |

A statement can be true at one level and false at another. A governance system may be sound even if
its artifacts are incomplete. The artifacts may be complete even when the behavior they produce is
inadequate.

This family occupies the **arrows**, not any single level:

```
Governance ──▶ Governance system ──▶ Governance artifacts ──▶ Behavior
                    └──────── what PGC standardizes ────────┘
```

PGC standardizes two things. **It standardizes how artifacts carry a governance system. It also
standardizes how those artifacts determine construction and execution.** So is PGC a governance
standard, a software architecture, or an execution model? The answer is one statement. PGC turns
governance into content a machine consumes, and defines how that content determines what is built
and what runs.

Not every artifact is a governing element. An artifact is the unit of declared content. It is a
governing element only when it declares something that governs another subject. A workflow, a
capability contract and a constitution are all artifacts. Of the three, only the constitution is
always a governing element. If the two concepts merged, the difference between governed content and
the governance over it would disappear.

### 3.2 The relations

The family relies on these relations and no others:

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

Two rules constrain the relation set.

- **Each relation stands on its own evidence.** No relation may be inferred from another.
  An element scoped to a subject may still lack authority over it. An artifact may be present and
  not admitted. A constructed thing may still fail to conform.
- **Position establishes no relation.** Containment, ordering, location and load order relate
  nothing.

### 3.3 The three activities

A governed system's life consists of exactly three activities over four states:

```
purpose ──transforms──▶ declarations ──constructs──▶ snapshot ──executes──▶ result + evidence
              │                                          │                       │
              └──────────────── the prior snapshot is the baseline ──────────────┘
                                       evidence of each activity is retained
```

- **Transformation** determines what the declarations are. Its input includes the current baseline.
  If the baseline did not change, the system did not change.
- **Construction** determines whether those declarations may exist, and produces the authorized
  representation. It decides admissibility, never adequacy.
- **Execution** realizes what the snapshot already determines. It originates nothing.

Each activity produces evidence. Each activity is also a governed subject, transformation included.
That is why the loop closes instead of running off the end.

This is a model of *activities and their authority*, not of components. One agent may perform all
three activities, and three agents may divide one. What stays fixed is which activity holds which
authority. **Construction determines what may be executed. Execution realizes what the snapshot
determines.** Neither activity takes the other's part. The authority chain runs:

```
governance → declarations → construction → authorized snapshot → execution
```

Each link determines the next and reaches no further. The declarations determine behavior, and the
snapshot carries it. Construction determines which declarations may reach the snapshot. Everything
the family requires about determinism, replay, refusal and evidence follows from this division. None
of it is added on top.

## 4. Foundational concepts

**Protocol-Governed Computing (PGC).** A model of computing in which explicit, versioned,
machine-consumable declarations determine what software may construct and may execute. Software
constructs and executes only what those declarations authorize.

**Governed system.** A system whose declarations determine its behavior and construction. The code
that realizes it does not. A system is governed to the extent that it could not act at all without
its governing declarations. Without them it would be disabled, not merely unsupervised.

**Declaration.** A statement of what *is*, in a form a machine can consume and act on. A declaration
does not describe a decision made elsewhere. It is the decision itself. Declarations are the
substance of PGC.

- *Distinguish from documentation.* Documentation describes a system and has no effect on it. A
  declaration determines the system. A system that diverges from its declaration is in violation,
  not merely out of date.
- *Distinguish from configuration.* Configuration parameterizes behavior that already exists. A
  declaration establishes whether the behavior exists at all.

**Declarative.** The property of stating governed facts, constraints, relationships and permitted
behavior without prescribing the procedure that realizes them. A declarative statement may state
what must, may or must not occur. It omits the control procedure that brings that about.

- *Distinguish from imperative.* The line does not fall between *what* and *what to do*. An
  obligation states what must be done, and it is declarative. The line falls between the governed
  semantics and the steps that realize them. The declaration carries the semantics. The steps lie
  outside it.

**Artifact.** A single, bounded, identified declaration, together with everything needed to
interpret it. The artifact is the unit of identity, of governance and of change. Things are
governed, versioned, superseded and referenced one artifact at a time.

**Artifact kind.** The classification that determines what an artifact declares, what it must carry,
and what may be said about it. The kind is a property of the artifact. Declaration establishes it.
Nobody infers it from the artifact's name, location or content.

**Governed subject.** Whatever a governing element applies to: an artifact, a class of artifacts, a
construction, an execution, a boundary, or another governing element. Governance is always
governance *of* something. A governing element with no subject governs nothing.

## 5. Governance

**Software governance.** The establishment, enforcement, verification, evolution, and retirement of
the rules, constraints, authorities, and evidence that determine what software **may do, must do,
and must not do** within a defined context of use, across its lifecycle, in pursuit of a defined
purpose.

The definition has four dimensions and one span. Each one carries weight:

| Dimension | Establishes |
|---|---|
| **Rules** | normative requirements — what must hold |
| **Constraints** | limits on behavior — what may and may not occur |
| **Authorities** | who or what may authorize an action or a change |
| **Evidence** | demonstration that the rules were in fact followed |

The **span** is the whole lifecycle, from inception to retirement. Governance must cover who may
change what software does, as well as what it does. Without the first, it is incomplete where it
matters most. *Who or what may change what the software does* is a governance question, not a
process question. This family treats it as one throughout.

**Governance.** In this family, the unqualified term **governance** always means *software
governance* as defined above. It is the governance of the software itself: its construction, its
execution and its change.

- *Distinguish from governance as subject matter.* A governed system may have a domain whose
  business is governing something in the world, such as agents, transactions, licences or people.
  That domain is an application built with this family. Its rules are business declarations like
  any other. They are not the governance this family defines, and a document MUST NOT conflate the
  two. One determines what the software may do. The other is what some software does.
- *Distinguish from adjacent governance disciplines.* Corporate, data, hardware and IT governance lie
  outside this family's scope. A governed system may have to meet an obligation from one of them.
  That obligation enters as a declaration like any other. From then on, software governance governs
  it.
- *Distinguish from review.* People perform review on a system and produce a judgment about it.
  Governance is content the system holds, and it determines what the system can do. A system can
  pass review and still be ungoverned, if nothing in it changed.
- *Distinguish from policy.* A policy states intent. It binds only as far as something enforces it.
  A governing declaration and its enforcement are inseparable. An unenforced governing declaration
  is a defect, not a weaker form of governance.

In PGC, governance is a property of the system. The system carries it inside as declarations it
consumes. Governance is not a discipline applied to the system from outside (§3.1).

**Governing element.** A declaration whose subject is another part of the system, rather than its
own behavior. Governing elements determine what may exist, what must hold, who may act and what is
exposed.

**Authority.** The capacity of a governing element to bind a subject. It answers the question *by
what right does this determine that?* Authority is always declared. An element never assumes it and
never gains it by position. An element does not govern a subject because it precedes it, contains
it, or loaded before it.

**Obligation.** A requirement that a governing element places on a subject: something that must hold
of the subject, or something the subject must or must not do. An obligation must be something a
party can evaluate. A requirement nothing can evaluate is not an obligation.

**Scope.** The extent of a subject over which a governing element applies. Scope answers *how far*.
Authority answers *by what right*. The two are independent. An element may hold authority over a
subject and still have a scope that excludes it.

**Governance closure.** The complete set of governing elements that apply to a subject, together with
the determination of how they compose. A closure is *closed* in the strict sense. Governance enters
or leaves it only by a declared entry or exit.

**Admission.** The act by which something becomes part of a governed system for the first time.
Admission is a governed act with a determination and a result. Placing something where the system
would find it never makes it part of the system.

- *Distinguish from presence.* Presence is a fact about where something is. Admission is a fact
  about what the system has accepted. Presence admits nothing.

The Governance Closure & Authority Standard specifies the semantics of authority, scope, admission
and closure: how a realization determines and composes each one. This document specifies only that
they are distinct concepts and that none follows from another.

## 6. Structure and composition

**Domain.** A bounded region of a governed system that owns its declarations and answers for them. A
domain is a governance boundary, not a directory, a package or a team.

**Surface.** What a domain or system exposes to another. A surface is declared. Only what is on the
surface is reachable across the boundary, whatever else exists behind it.

**Composition.** The act of bringing separately owned parts of a governed system into one governed
whole, on a stated basis for combining them. Composition is an act with a result. Parts placed side
by side are not thereby composed.

**Profile.** A statement of which facilities of this family a particular governed system selects,
constrains or requires, and of the conformance claims it must support. A profile selects. It does
not redefine.

**Platform.** A governed composition that provides a defined governance and execution surface for the
workloads and domains composed into it, under a named profile.

- *Distinguish from a thing that can be pointed at.* An act of composition under a profile
  constitutes a platform. No repository, package, deployment or installation is a platform, however
  completely it contains one. The composition and its profile make the platform, and neither is a
  location.

The Normative Platform Profile specifies what constitutes a particular platform, how platforms
relate to the profiles that constitute them, and whether any platform is minimal.

## 7. Construction

**Construction.** The activity that turns authored declarations into an authorized representation
that may be executed. Construction discovers, resolves, validates, constructs, projects, verifies
and attests. This document leaves open how many agents perform it, and whether it runs long before
execution or just before it.

**Admissibility.** The property that a candidate declaration is sound in structure and in
governance: that it *may* exist. Construction determines admissibility. Admissibility is a question
about soundness, never about quality, usefulness or behavioral adequacy.

- *Distinguish from adequacy.* Whether a thing may exist and whether it does what was wanted are
  different determinations, with different evidence. Whatever judges admissibility may not also
  judge adequacy. Otherwise the two merge into one act that nobody can examine.

**Resolution.** The act of turning a reference into the thing it refers to. Where the family
requires resolution during construction, an unresolved reference is a construction failure. It is
never a condition that execution discovers.

**Projection.** A deterministic, machine-consumable representation of governed information, derived
from a defined source. A projection carries meaning already settled. It never adds meaning of its
own.

**Sealing.** The act that makes a constructed representation immutable and gives it an identity
derived from its content. Once sealed, the representation can change only by becoming a different
representation.

**Snapshot.** A sealed representation of a governed system, complete enough to execute and
identified by its content. Execution consumes the snapshot.

**Baseline.** The snapshot that defines what a governed system currently *is*: the state that any
change transforms. A system has exactly one baseline at a time.

## 8. Execution

**Execution.** The activity of realizing behavior that a snapshot already determines. Execution
produces results and evidence. It originates no behavior.

**Runtime.** The agent that performs execution. What a runtime may not do defines it. It holds no
domain meaning, makes no governing determination, and adds nothing to the snapshot it executes. A
runtime is a role, not a component. A realization may fill the role with any number of programs or
processes.

**Workflow.** A declared structure of governed steps and the transitions among them. A workflow
states what may happen and in what order. The runtime executes it by its declared transitions. The
runtime never infers or invents a transition the workflow does not declare.

**Step.** A position in a workflow's declared structure. At a step, execution reaches a capability
and reports one of its declared outcomes. A step is part of the structure the workflow declares. It
is never a unit of work formed while the workflow runs.

**Capability.** A governed unit of execution through which a system reaches computational or
external effect. Execution reaches a capability only through its declared contract.

**Contract.** The declared interface of a capability: its inputs, outputs and enumerated outcomes.
The contract is the entire interface. Execution sees nothing below it, so realizations of a
capability are interchangeable.

**Outcome.** One of the enumerated results a contract declares. Only enumerated outcomes can occur.
If a realization can produce any other, the contract is wrong.

**Governed state.** State whose location, ownership and permitted transitions are set by
declaration. Execution maintains governed state. It does not own that state and does not decide its
shape.

**Side effect.** An effect of execution that reaches beyond the governed system's own state. Side
effects are declared and closed. A system's ability to affect the world is part of what is governed
about it.

**Refusal.** The determined response to a requirement that cannot be satisfied. The act does not
occur, and the reason is recorded. Refusal is a governed outcome. It is neither an error condition
nor a failure of the mechanism that produced it.

- *Distinguish from degradation.* Degradation continues in a reduced form and hides the violation
  that caused it. Refusal stops and makes the violation the result.

## 9. Evidence

**Evidence.** The record that lets a party who did not observe a determination, a construction or an
execution establish it afterwards. A system produces evidence as a governed obligation, not as a
byproduct of running.

**Trace.** Evidence of an execution: the account of what occurred. Execution writes the trace as it
proceeds and never reads it back as an input. If something is absent from the trace, it did not
happen.

**Attestation.** An assertion, by an identified party, about the integrity or origin of a record or
artifact. Attestation is about a thing. Evidence is about an event.

**Provenance.** The derivation relation between a governed thing and what it came from. Provenance
answers *where did this come from*. Evidence answers *what happened*. Attestation answers *who
vouches for it*.

**Determinism.** The property that the same governed input, against the same sealed representation
and the same initial state, determines the same result and the same governed consequences. Governed
input includes every captured input. It also
requires that the evidence of the execution remains sufficient to establish that determination.
Determinism follows from where behavioral authority sits. It is not a feature added to an execution
agent.

- *Distinguish from byte-identical evidence.* Evidence may carry observational material, such as
  when a thing occurred, what vouched for it, or what the environment was. That material may vary
  between executions while every governed consequence stays the same. The Evidence, Attestation &
  Provenance Standard specifies which parts of evidence are deterministic and which are
  observational. Determinism is a property of the determination, not of every byte of the record.

**Replay.** The reproduction of a past execution by executing the same sealed representation against
the same inputs, the same captured inputs and the same initial state. Replay is structural. It
re-executes an artifact. It does not reconstruct an environment. Replay substitutes each captured
input from its record, and never re-invokes the step that produced it.

**Captured input.** A value that a non-deterministic capability produces during execution, recorded
once where it is produced and treated from then on as a governed input. A capability is
non-deterministic when its declared inputs do not determine its result: it reads a clock, draws a
random value, or asks something outside the governed system. A captured input is an input. It is
neither a decision nor evidence.

- *Distinguish from observational content.* Observational content may vary between executions and
  never affects a governed consequence. A captured input may affect governed consequences, so it is
  recorded and held constant wherever two executions are compared.
- *Distinguish from evidence.* Evidence records what happened and is never an input. A captured input
  is held in its own record. Evidence refers to that record. It is not that record.

## 10. Change

**Transformation.** The governed act by which one baseline becomes the next. Transformation is itself
a governed subject, with its own declarations, determinations and evidence. It is not a process
that surrounds a governed system and stands exempt from it.

- *Distinguish from authoring.* Authoring produces a new thing beside the system. A transformation
  takes an existing baseline as input and produces the next one. If the baseline did not change, the
  system did not change.

**Candidate.** A proposed part of a governed system that has been produced and not yet admitted. As
far as the system is concerned, a candidate does not exist.

**Promotion.** The act that installs an admitted candidate as the new baseline. Promotion is the
moment a governed system changes. It verifies integrity and re-judges nothing. Every determination
it relies on was made before it.

**Supersession.** The relation by which one governed thing replaces another, together with the rules
for what becomes of references to the replaced thing. Supersession is always declared. Deleting,
renaming or abandoning a thing does not supersede it.

**Version.** A declared identifier of an artifact's semantics. A change of meaning is a version
change, whether or not the representation changed. A change of representation that keeps the
meaning is not.

## 11. Conformance

**Conformance.** The relation between a subject and the requirements that govern it. The subject
satisfies them, and evidence exists that lets an independent party determine so.

**Conformance subject.** What a conformance claim is about: an artifact, a governed representation,
an execution, an implementation or a system instance. These are five different claims with five
different discharges. A claim must name its subject. Without a subject it is not a claim.

**Enforcement.** What a governed system does when a requirement applies to it: it evaluates,
determines and acts, which includes refusing. Enforcement is the system's behavior. Conformance is a
judgment about the system. A system may enforce perfectly and still fail to conform.

**Invariant.** A property required to hold of a governed system at all times, not at one moment or on
one path. An invariant must hold everywhere, not only where something checks it. A property that
holds only under a check belongs to the check, not to the system.

## 12. Normative usage

- A document of this family MUST use the terms defined here with the meanings defined here.
- A document MUST NOT redefine a term defined here. Where it needs more, it MUST refine the inherited
  concept and say what it is refining.
- A document that introduces a term not defined here MUST define it. It MUST NOT define the term so
  that it overlaps a term defined here. Two names for one concept is a defect.
- A document MUST preserve each distinction that §4–§11 draws as *distinguish from*. A document that
  treats two distinguished concepts as one is non-conforming, even if its requirements are otherwise
  sound.
- A profile MUST NOT alter the meaning of any term defined here. A profile may select facilities. It
  may not rename or re-scope a concept.
- The document whose subject matter principally establishes a term MUST define it. Two cases follow:
  - A term belongs here if several parts of the family need it and its identity depends on no later
    standard's mechanism.
  - A term belongs to a later standard if it exists principally because of that standard's subject
    matter. This document MUST NOT define it.

  **Semantic primacy decides ownership, never the order in which documents appear.** The contrary
  rule would turn this document into a warehouse for every term written down first.
- Adding, removing or altering a definition here is a revision of this document. That revision
  requires a re-examination of every document that used the affected term. A terminology change is
  never editorial.

## 13. Normative invariants

- **CM-1.** A document of this family MUST use the terms defined here with the meanings defined here
  (§12).
- **CM-2.** A document MUST NOT redefine a term defined here. Where it needs more, it MUST refine the
  inherited concept and state what it is refining (§12).
- **CM-3.** A document introducing a term not defined here MUST define it. It MUST NOT define the term
  so that it overlaps a term defined here (§12).
- **CM-4.** Every document that relies on a distinction drawn in §4–§11 as *distinguish from* MUST
  preserve it (§12).
- **CM-5.** A profile MUST NOT alter the meaning of any term defined here (§12).
- **CM-6.** A document MUST relate the concepts as §3 relates them. It MUST introduce no relation §3
  does not provide, and MUST NOT draw an inference between relations that §3.2 forbids (§3, §14).
- **CM-7.** Adding, removing or altering a definition here MUST be a revision of this document. That
  revision MUST require a re-examination of every document that used the affected term (§12).
- **CM-8.** The document whose subject matter principally establishes a term MUST define it. A
  document MUST NOT assign ownership of a term by the order in which documents appear (§12).

## 14. Conformance

A document satisfies this document. An implementation does not. The conformance subject is a
specification document of this family.

A document conforms to this document when all of the following hold:

- Each PGC term it uses is either defined here and used with that meaning, or defined by the
  document itself without overlapping the vocabulary here.
- It preserves throughout every *distinguish from* distinction it relies on.
- It relates the concepts as §3 relates them. It introduces no relation §3 does not provide, and no
  inference between relations that §3.2 forbids.
- Its own subject matter principally establishes every term it defines. None of those terms belongs
  here or to another standard.
- None of its requirements depends on a reading of a term that this document excludes.

A conflict between this vocabulary and another document of the family is a defect in one of them.
The family resolves it by ruling, and by revising the document found wrong. It never lets both
documents carry a term in two senses.
