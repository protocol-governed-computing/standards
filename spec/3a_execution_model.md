# Execution Model

## 1. Scope

This document specifies the semantics of **governed execution**: what happens when a governed system
acts, how workflows, capabilities, state, effects, events, and outcomes relate to one another, and
what may be concluded about a run.

It is the first document of Part III. The Snapshot Standard governs what execution consumes; the
Runtime Standard bounds the agent that performs it; the Capability Standard covers the units it
dispatches; Evidence, Attestation & Provenance states what it must record. This document says what
execution *is*.

It defines observable execution consequence **independently of the physical environment**. Nothing
here assumes a process, a machine, a scheduler, a network, or a number of nodes.

This document introduces the terms **traversal**, **routing**, and **outcome vocabulary**, and
refines the Conceptual Model's **step**. Every other term it uses is defined by the Conceptual
Model, the Semantic Model, or Part II.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Execution as a governed transition

Execution is the transition schema of the Semantic Model applied to one subject:

| | In execution |
|---|---|
| `S` | the governed state under a sealed representation |
| `π` | an interaction presented to the system |
| `C` | the closure the sealed representation supplies for that interaction |
| `S′` | the governed state after |
| `ε` | the evidence of what was determined and what occurred |

Everything the Semantic Model requires of a governed transition holds here without amendment:
determination precedes effect, the closure is evaluated completely, a refused interaction leaves no
residue, and evidence is produced.

**Execution adds no semantics of its own.** It is not a second kind of governance operating at run
time; it is the same determination, over a different subject, at a different moment.

## 3. Traversal without decision

**Execution includes traversal.** Traversal is the execution of a declared workflow structure: an
interaction is admitted; a workflow is traversed; capabilities are dispatched; results are
produced; state transitions and effects occur as declared; and evidence is written. At no step is
behavior invented.

*Refining the Conceptual Model's* **step**: within a run, a step is the unit traversal advances
through, and the position at which a capability is dispatched. The Conceptual Model states what a
step is; execution adds where it comes from — a step is a position the sealed representation
carries, fixed for the duration of the run (§3.2).

```
sealed representation  →  workflow  →  capability  →  contract  →  effect
```

The path taken is **a reading of the declarations, not a computation over them**.

### 3.1 What this means precisely

"Declarative execution" does not mean that a system is configured rather than coded. It means
that **no step of execution originates behavior**:

- no branch is evaluated that the declarations did not settle;
- no structure is planned, generated, or extended;
- no meaning is inferred from a value, a name, a context, or a caller;
- no default supplies what a declaration omitted.

Each step is the faithful realization of behavior already determined (AI-1).

**Computation is not the forbidden thing; behavioral origination is.** A capability may compute
whatever its contract requires of it, including determining which of its declared outcomes
obtains. What execution may not do is originate the behavioral rules governing those computations
or the routing that follows them. The prohibition is on inventing the rules, never on evaluating
under them.

### 3.2 Routing is data

A workflow is a **governed structure of steps**, and traversal advances by *declared routing*: a
step completes, reports one of its enumerated outcomes, and that outcome selects the next step
according to routing settled before execution began.

**Execution performs no routing logic of its own.** It does not decide where to go; it reads where
to go. This is the difference between orchestration and traversal, and it is what makes a run a
property of the sealed representation rather than of the engine.

- Routing MUST be resolvable from the sealed representation alone.
- Routing MUST NOT be computed from a payload, an environment, an accumulated state, or the
  identity of a caller.
- A step MUST NOT be added, removed, or rerouted during a run (AI-11).

## 4. Outcomes

An **outcome** is one of the enumerated results a step's contract declares. The set of outcomes a
contract declares is its **outcome vocabulary**, and it is closed.

### 4.1 Outcomes are the only routing signal

Traversal advances on outcomes and on nothing else. Execution MUST NOT route on a returned value,
an error class, a state inspection, or anything a contract did not declare as an outcome.

A conforming capability produces only outcomes its governing contract declares. A realization can
nevertheless produce a result that is not a declared outcome — which is why refusal exists. Where
it does, the execution is non-conforming and execution **MUST NOT route on that result**. Three
things are distinct here and MUST stay so: what the declarations permit, what a realization
actually produced, and what execution must do when the second departs from the first.

**The obligation is on the second and third, never on the first.** No obligation of this family
forbids a realization from *producing* an undeclared result — nothing could enforce that, and an
obligation nothing can refuse is not in force (EN-1). What is forbidden is **admitting** one:
routing on it, recording it as an outcome, letting an effect follow from it, or treating it as
anything but the occasion for refusal. **Detecting an undeclared result is required; tolerating one
is what is prohibited**, and a realization that could not detect it could not refuse it either.

### 4.2 Failure is a declared outcome

**The negative path is as declared as the positive one.** A capability that can fail declares its
failure outcomes alongside its successes, and the routing for each is settled before execution.

This is where conventional runtimes concentrate origination — retries, fallbacks, defaults,
degraded modes, all invented at the moment of need. In a governed system each of those, where it
exists at all, is a declared outcome with declared routing. **A recovery path nobody declared is
behavior nobody governed**, and it appears exactly when the system is least observed.

### 4.3 An unrouted outcome is a refusal

Where a step reports an outcome for which the traversal declares no routing, execution **refuses**.
It MUST NOT select a default path, halt silently, or treat the absence of routing as completion.

An unrouted outcome means the declarations are incomplete for a case that arose. That is a finding
about the declarations, and refusal is what makes it one.

### 4.4 An outcome named for refusal is not a refusal

An outcome vocabulary is a profile's or a contract's to choose (§14), and nothing stops either from
naming an outcome `refused`, `denied`, or `rejected`. **Such an outcome is a declared result of a
capability. It is not a governance refusal, and the two MUST NOT be conflated.**

| | What happened | What follows |
|---|---|---|
| **a governance refusal** (2f §6) | a proposal was not permitted | nothing proceeds; the refusal is evidenced with what refused it, under what closure and authority (EN-8) |
| **an outcome named for refusal** | the capability completed and reported a declared result | traversal routes on it like any other outcome, and something proceeds |

The collision is not verbal. EN-8 requires a refusal to establish **that nothing proceeded**; an
outcome exists to be routed on, and routing is proceeding. A realization that treats a routed
outcome as discharging a governance refusal has recorded that nothing proceeded while something
did — and a party checking the evidence cannot tell which happened.

A contract or profile that uses such a name therefore carries the distinction explicitly: the
outcome is the capability's report about its own subject matter, the refusal is a determination
about whether the capability was permitted to be reached at all, and no evidence of the first is
evidence of the second. **Where the distinction cannot be carried, the name is the thing to
change** — the family reserves no outcome names, and it does not need to, because what a name may
not do is fixed here whatever it is called.

## 5. Inputs and resolution

A step receives its inputs through **declared references**, resolved against results the traversal
has already produced.

- A step MUST NOT search for its inputs, infer them from context, or select among candidates.
- Every reference a step depends on MUST resolve before that step is dispatched (AI-5).
- An unresolvable reference during execution is a refusal, and is the observable signature of a
  construction that did not complete.

## 6. Governed state

**Governance defines state; execution maintains it.** Which entities are stored, under whose
ownership, and what transitions are permitted are declarations, not decisions taken while running.

### 6.1 A state transition is declared behavior

A change to governed state is governed exactly as control flow is. When a step writes, **the write
performed, the location targeted, and the conditions permitting it were all determined before
execution began.**

Execution does not decide *that* the state changes, or *how* it changes, any more than it decides
which step comes next. It realizes a transition the declarations already settled.

This closes the last route by which authority could re-enter: a system whose execution owned its
state would own behavior through the back door, because what a system may become is part of what it
may do.

### 6.2 Ownership

- Every governed store has a declared owner.
- **A governed store MUST be written only through a declared transition authorized by the
  governance applicable to that store.** Ownership means the owner controls that authorization; it
  does not mean writes may never cross a boundary. What is forbidden is authority acquired by
  reach: **nothing acquires write authority merely by being able to address or access a store**
  (AI-2).

## 7. Effects and the mutation boundary

An **effect** is a change reaching beyond the governed state of the system itself.

- **The set of ways a system can affect anything is closed and declared** (AI-13). There is no
  implicit write path, no incidental output, and no side channel.
- **Execution MUST respect the effect boundary its governing contract declares.** A capability
  declared as non-effecting MUST NOT produce an external effect, and MUST NOT reach one
  indirectly. Which distinctions of capability exist, what they are called, and how a capability
  declares which it is belong to the Capability Standard; this document specifies only that the
  declared boundary binds execution.

The purpose of the boundary is enumerability. A system whose effects all pass through declared
surfaces can state what it is capable of doing to the world; one whose effects can originate
anywhere cannot, and no amount of inspection recovers the answer.

## 8. Events

An **event** records that a declared moment occurred. It is evidential (Governance Semantic
Ontology §4.1) and it governs nothing.

- **An event MUST NOT itself cause a subsequent execution.** Any subsequent activity MUST arise
  from a declared interaction or from the declared execution structure.
- There is no subscription by which recording something causes something else to happen.

The reason: an event that could cause execution would make the record of what happened into a
cause of what happens next, and a system's history would become an input to its determinations.

## 9. Composition

- **Any composition, repetition, nesting, or concurrency that affects execution MUST be represented
  in the governed structure before execution begins, and MUST NOT be introduced by the executing
  agent.** How a structure represents these — whether through a step, a declared relation, or
  another form — is not specified here.
- Composition rules are declared and settled before execution. Two workflows are related when a
  declaration relates them, never because they run adjacently or share state.
- A step's result MUST conform to the surface its governing contract declares. **Routing a result
  is permitted; redefining one is not.**

## 10. Boundary neutrality

**A workflow cannot tell how an interaction arrived, and MUST NOT be able to.**

Execution receives interactions through the canonical semantic form the applicable interaction
boundary defines, and **MUST NOT vary its behavior according to the transport or arrival
mechanism**. That there is a canonical semantic form is required; what form it takes is not specified
here. A workflow that could detect its transport could behave differently per caller — which
is origination by another name, and would make behavior a property of the arrival path rather than
of the declarations.

The mechanics of the boundary belong to the Governed Interaction Boundary. What this document specifies
is that execution is *behind* it: nothing about how an interaction was carried may reach the
traversal.

## 11. Refusal

Where execution encounters what the declarations do not answer — an unresolvable reference, an
unrouted outcome, an undeclared condition, a violated obligation — it **refuses**. It does not
improvise, default, or degrade.

Refusal is not an origination of behavior. It is **the enforcement of the declarations' boundary**,
and it is execution's one governance function: where the declarations answer, execution realizes;
where they do not, execution refuses. In neither case does it decide.

A system that refuses where its declarations run out is demonstrating that the declared world is
closed. A system that improvises there has demonstrated that it was never closed, and every earlier
guarantee is weakened by the same amount.

## 12. What a run establishes

Because execution originates nothing, a run supports two independent checks — and the second is the
one that matters:

| Check | Question | Establishes |
|---|---|---|
| **Result** | does the result conform to what the governing contract declared? | result conformance |
| **Path** | was the path recorded in evidence contained in the sealed representation? | path conformance |

The first tests the result against its contract. **The second tests the architecture**: it asks
whether what happened was something the sealed representation permitted, which is a question about
governance rather than about the answer produced. A system can produce acceptable results by
ungoverned means, and only the second check detects it.

**Neither check establishes that the result was the right one to want.** Whether an execution
resolved the problem it was meant to resolve is a judgment against an intent this document does not
carry, and it belongs to the mechanism that validates against declared intent — not to execution
semantics.

Both checks are performed against evidence, by a party that need not have observed the run (AI-16).

## 13. Structural independence

Where steps are independent, their independence is a property the declarations state, not a
scheduling decision.

- Concurrency, where a system exhibits it, is **read from the declared structure** rather than
  engineered into the agent performing execution.
- **Executions MUST NOT depend on undeclared ambient state.** Where independence is declared, no
  undeclared shared state or interaction may introduce a dependency between executions. Executions
  may interact through governed state where declarations establish that they do; what is excluded
  is dependency nobody declared.

This document requires no concurrency and forbids none. It requires that whatever independence a
system exploits be declared, so that a run's meaning does not depend on how much parallelism the
substrate happened to apply.

## 14. What this document does not specify

- **The environment.** Node count, process model, scheduling, distribution, and placement are
  unconstrained. A deployment decision changes *where* execution happens; it MUST NOT change what
  execution means.
- **The agent.** What performs execution, and how it is organized internally, belongs to the
  Runtime Standard.
- **The capability model.** Contracts, kinds of capability, and bindings belong to the Capability
  Standard.
- **The outcome vocabulary.** Which outcomes a system's contracts declare is a profile's selection,
  not this family's.

## 15. Normative invariants

- **EX-1.** Execution MUST NOT originate behavior; every step MUST realize behavior the sealed
  representation already determined (§3).
- **EX-2.** Traversal MUST advance only on declared outcomes, according to routing resolvable from
  the sealed representation alone (§3.2, §4.1).
- **EX-3.** Routing MUST NOT be computed from payload, environment, accumulated state, or caller
  identity (§3.2).
- **EX-4.** The structure traversed MUST NOT be added to, removed from, or rerouted during a run
  (§3.2).
- **EX-5.** A result a contract does not declare as an outcome MUST NOT be routed on, admitted into
  the governed transition, or recorded as an outcome, and MUST produce refusal; an outcome for which
  no routing is declared MUST produce refusal (§4.1, §4.3).
- **EX-6.** Failure paths MUST be declared outcomes with declared routing; no recovery, retry,
  fallback, or degraded path MUST exist that the declarations did not specify (§4.2).
- **EX-7.** A step's inputs MUST be resolved from declared references, and MUST NOT be searched for
  or inferred (§5).
- **EX-8.** Every change to governed state MUST be a transition the declarations determined,
  including its target and its permitting conditions (§6.1).
- **EX-9.** A governed store MUST be written only through its owner's declarations (§6.2).
- **EX-10.** The set of effects a system can produce MUST be closed and declared; no implicit
  effect path MUST exist (§7).
- **EX-11.** An event MUST NOT trigger execution (§8).
- **EX-12.** A step's result MUST conform to its governing contract's declared surface (§9).
- **EX-13.** No property of how an interaction arrived MUST be observable to the traversal (§10).
- **EX-14.** Where the declarations do not answer, execution MUST refuse, and MUST NOT default,
  improvise, or degrade (§11).
- **EX-15.** An execution MUST produce sufficient evidence to permit the path taken to be
  independently checked against the sealed representation (§12).
- **EX-16.** An outcome MUST NOT be treated as a governance refusal, whatever it is named, and a
  refusal MUST NOT be reported as a routable outcome (§4.4, EN-8).

## 16. Conformance

The conformance subject of this document is an **execution**: a single run of a governed system,
together with the evidence it produced.

An execution conforms when:

- every step it performed was a step the sealed representation contained, reached by declared
  routing on a declared outcome (EX-1, EX-2, EX-5);
- no structure was constructed, extended, or rerouted during it (EX-4);
- every state change and every effect passed through a declared, owned surface (EX-8 … EX-10);
- it refused where its declarations did not answer, rather than proceeding (EX-14); and
- its evidence supports the path check of §12 by a party that did not observe it (EX-15).

**An execution that produced the expected result is not thereby conformant.** The result is one
check and the weaker one; a run that reached an acceptable answer by a path the sealed
representation did not contain is a non-conforming execution that happens to look successful, and
it is precisely the case the path check exists to catch.

How conformance is claimed, levelled, and demonstrated — and what evidence discharges each
invariant above — belongs to the Conformance Model and the Conformance Test Specification. This
document specifies what an execution must be, not how a claim about one is established.
