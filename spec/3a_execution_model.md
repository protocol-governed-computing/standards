# Execution Model

## 1. Scope

This document specifies the semantics of **governed execution**. It covers:

- what happens when a governed system acts;
- how workflows, capabilities, state, effects, events and outcomes relate to one another;
- what a party may conclude about a run.

This is the first document of Part III. The Snapshot Standard governs what execution consumes. The
Runtime Standard bounds the agent that performs it. The Capability Standard covers the units it
dispatches. Evidence, Attestation & Provenance states what it must record. This document says what
execution *is*.

This document defines observable execution consequences **independently of the physical
environment**. Nothing here assumes a process, a machine, a scheduler, a network or a number of
nodes.

This document introduces the terms **traversal**, **routing**, **outcome vocabulary**, **declared
composition** and **continuation**, and refines the Conceptual Model's **step**. The Conceptual Model, the Semantic Model or Part II defines
every other term it uses.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Execution as a governed transition

Execution is the Semantic Model's transition schema applied to one subject:

| | In execution |
|---|---|
| `S` | the governed state under a sealed representation |
| `π` | an interaction presented to the system, with the captured inputs its execution records |
| `C` | the closure the sealed representation supplies for that interaction |
| `S′` | the governed state after |
| `ε` | the evidence of what was determined and what occurred |

Everything the Semantic Model requires of a governed transition holds here without amendment:

- determination precedes effect;
- the closure is evaluated completely;
- a refused interaction leaves no residue;
- evidence is produced.

**Execution adds no semantics of its own.** It is not a second kind of governance operating at run
time. It is the same determination, over a different subject, at a different moment.

## 3. Traversal without decision

**Execution includes traversal.** Traversal is the execution of a declared workflow structure. In a
traversal:

- an interaction is admitted;
- a workflow is traversed;
- capabilities are dispatched;
- results are produced;
- state transitions and effects occur as declared;
- evidence is written.

No step invents behavior.

*Refining the Conceptual Model's* **step**: within a run, a step is the unit traversal advances
through, and the position at which a capability is dispatched. The Conceptual Model states what a
step is. Execution adds where a step comes from: a step is a position the sealed representation
carries, and it stays fixed for the duration of the run (§3.2).

```
sealed representation  →  workflow  →  capability  →  contract  →  effect
```

The path taken is **a reading of the declarations, not a computation over them**.

### 3.1 What this means precisely

"Declarative execution" does not mean that a system is configured rather than coded. It means that
**no step of execution originates behavior**:

- execution evaluates only branches the declarations settled;
- execution plans, generates and extends no structure;
- execution infers no meaning from a value, a name, a context or a caller;
- no default supplies what a declaration omitted.

Each step faithfully realizes behavior already determined (AI-1).

**Behavioral origination is forbidden. Computation is not.** A capability may compute whatever its
contract requires. That includes determining which of its declared outcomes obtains. Execution may
not originate the behavioral rules that govern those computations, or the routing that follows them.
The prohibition is on inventing the rules, not on evaluating under them.

### 3.2 Routing is data

A workflow is a **governed structure of steps**. Traversal advances by *declared routing*. A step
completes and reports one of its enumerated outcomes. That outcome selects the next step, by routing
settled before execution began.

**Execution performs no routing logic of its own.** It does not decide where to go. It reads where to
go. That is the difference between orchestration and traversal. It is also what makes a run a
property of the sealed representation, not of the engine.

- Routing MUST be resolvable from the sealed representation alone.
- Routing MUST NOT be computed from a payload, an environment, an accumulated state, or the identity
  of a caller.
- A step MUST NOT be added, removed, or rerouted during a run (AI-11).

## 4. Outcomes

An **outcome** is one of the enumerated results a step's contract declares. The set of outcomes a
contract declares is its **outcome vocabulary**, and that set is closed.

### 4.1 Outcomes are the only routing signal

Traversal advances on outcomes and on nothing else. Execution MUST NOT route on a returned value, an
error class, a state inspection, or anything a contract did not declare as an outcome.

A conforming capability produces only outcomes its governing contract declares. A realization can
still produce a result that is not a declared outcome. That is why refusal exists. When it happens,
the execution is non-conforming, and execution **MUST NOT route on that result**. Three things are
distinct here and MUST stay so:

- what the declarations permit;
- what a realization actually produced;
- what execution must do when the second departs from the first.

**The obligation falls on the second and third, never on the first.** No obligation of this family
forbids a realization from *producing* an undeclared result. Nothing could enforce that, and an
obligation nothing can refuse is not in force (EN-1). What is forbidden is **admitting** one. Admitting
means routing on it, recording it as an outcome, letting an effect follow from it, or treating it as
anything but the occasion for refusal. **Execution must detect an undeclared result. It must not
tolerate one.** A realization that could not detect it could not refuse it either.

### 4.2 Failure is a declared outcome

**The negative path is as declared as the positive one.** A capability that can fail declares its
failure outcomes alongside its successes. The routing for each is settled before execution.

Conventional runtimes concentrate origination here. Retries, fallbacks, defaults and degraded modes
are all invented at the moment of need. In a governed system, each of those that exists at all is a
declared outcome with declared routing. **A recovery path nobody declared is behavior nobody
governed.** It appears exactly when the system is least observed.

### 4.3 An unrouted outcome is a refusal

When a step reports an outcome for which the traversal declares no routing, execution **refuses**.
It MUST NOT select a default path, halt silently, or treat the absence of routing as completion.

An unrouted outcome means the declarations are incomplete for a case that arose. That is a finding
about the declarations, and refusal is what makes it one.

The rule holds at every level of a declared composition (§9). A composed step that reports an outcome
with no declared continuation refuses. It does not proceed to the next composed step.

Construction refuses such declarations before execution (Governed Construction §7.1). This refusal
stays in place as the safeguard for any case construction did not reach.

### 4.4 An outcome named for refusal is not a refusal

A profile or a contract chooses its outcome vocabulary (§14). Either one may name an outcome
`refused`, `denied` or `rejected`. **Such an outcome is a declared result of a capability. It is not
a governance refusal, and the two MUST NOT be conflated.**

| | What happened | What follows |
|---|---|---|
| **a governance refusal** (Enforcement & Refusal §6) | a proposal was not permitted | nothing proceeds; the refusal is evidenced with what refused it, under what closure and authority (EN-8) |
| **an outcome named for refusal** | the capability completed and reported a declared result | traversal routes on it like any other outcome, and something proceeds |

The collision is not just about words. EN-8 requires a refusal to establish **that nothing
proceeded**. An outcome exists to be routed on, and routing is proceeding. Suppose a realization
treats a routed outcome as discharging a governance refusal. It has then recorded that nothing
proceeded while something did. A party checking the evidence cannot tell which happened.

So a contract or profile that uses such a name carries the distinction explicitly:

- the outcome is the capability's report about its own subject matter;
- the refusal is a determination about whether the capability could be reached at all;
- no evidence of the first is evidence of the second.

**Where the distinction cannot be carried, change the name.** The family reserves no outcome names,
and it does not need to. This section fixes what a name may not do, whatever the name is.

### 4.5 A captured input is judged before it routes

A non-deterministic capability produces a captured input (Conceptual Model, *captured input*).
**Neither the captured input, nor the outcome of the capability that produced it, may select a
route.** Traversal reaches routing through a deterministic step that evaluates the captured input
and reports one of its own declared outcomes.

- A step that dispatches a non-deterministic capability MUST have one declared continuation. Its
  outcome selects nothing.
- Where the non-deterministic capability fails to produce a value, execution refuses (§11). It does
  not route on the failure.
- The captured input MUST be recorded before anything consumes it (Capability Standard §5.3).

The rule keeps routing where §3.2 puts it. Every route still follows a declared outcome of a
deterministic determination. A non-deterministic value may influence a route only after a
deterministic step has judged it, and the judgement is what the route follows.

## 5. Inputs and resolution

A step receives its inputs through **declared references**, resolved against results the traversal
has already produced.

- A step MUST NOT search for its inputs, infer them from context, or select among candidates.
- Every reference a step depends on MUST resolve before that step is dispatched (AI-5).
- An unresolvable reference during execution is a refusal. It is the observable signature of a
  construction that did not complete.

## 6. Governed state

**Governance defines state. Execution maintains it.** Declarations settle which entities are stored,
under whose ownership, and which transitions are permitted. Execution does not decide these while
running.

### 6.1 A state transition is declared behavior

A change to governed state is governed exactly as control flow is. When a step writes, **the
write performed, the location targeted and the conditions permitting it were all determined before
execution began.**

Execution does not decide *that* the state changes, or *how*, any more than it decides which step
comes next. It realizes a transition the declarations already settled.

This closes the last route by which authority could re-enter. If execution owned a system's state,
it would own behavior through the back door. What a system may become is part of what it may do.

### 6.2 Ownership

- Every governed store has a declared owner.
- **A governed store MUST be written only through a declared transition authorized by the governance
  applicable to that store.** Ownership means the owner controls that authorization. It does not mean
  writes may never cross a boundary. What is forbidden is authority gained by reach: **nothing gains
  write authority merely by being able to address or access a store** (AI-2).

## 7. Effects and the mutation boundary

An **effect** is a change that reaches beyond the system's own governed state.

- **The set of ways a system can affect anything is closed and declared** (AI-13). There is no
  implicit write path, no incidental output and no side channel.
- **Execution MUST respect the effect boundary its governing contract declares.** A capability
  declared as non-effecting MUST NOT produce an external effect, and MUST NOT reach one indirectly.
  The Capability Standard owns which distinctions of capability exist, what they are called, and how
  a capability declares which one it is. This document specifies only that the declared boundary
  binds execution.

The boundary exists for enumerability. A system whose effects all pass through declared surfaces can
state what it can do to the world. A system whose effects can originate anywhere cannot, and no
amount of inspection recovers the answer.

## 8. Events

An **event** records that a declared moment occurred. It is evidential (Governance Semantic Ontology
§4.1), and it governs nothing.

- **An event MUST NOT itself cause a subsequent execution.** Any subsequent activity MUST arise from a
  declared interaction or from the declared execution structure.
- No subscription exists by which recording something causes something else to happen.

The reason: an event that could cause execution would turn the record of what happened into a cause
of what happens next. A system's history would become an input to its determinations.

## 9. Composition

- **Any composition, repetition, nesting, or concurrency that affects execution MUST be represented in
  the governed structure before execution begins, and MUST NOT be introduced by the executing
  agent.** This document does not specify how a structure represents these, whether through a step,
  a declared relation or another form.
- **Every level of a declared composition is traversal.** A **declared composition** is a contract
  realized as governed steps, each dispatching a contract of its own. Each composed step is a step.
  It reports one of the outcomes its dispatched contract declares. It advances only by the
  **continuation** the composition declares for that outcome: the next composed step, an end of the
  composition with a declared outcome, or a route. Every requirement on steps holds at every level
  (EX-18).
- Composition rules are declared and settled before execution. Two workflows are related only when a
  declaration relates them. Running side by side or sharing state does not relate them.
- A step's result MUST conform to the surface its governing contract declares. **Execution may route
  a result. It may not redefine one.**

## 10. Boundary neutrality

**A workflow cannot tell how an interaction arrived, and MUST NOT be able to.**

Execution receives interactions in the canonical semantic form that the applicable interaction
boundary defines. It **MUST NOT vary its behavior according to the transport or arrival mechanism**.
A canonical semantic form is required. This document does not specify what form it takes. A workflow
that could detect its transport could behave differently per caller. That is origination by another
name. It would make behavior a property of the arrival path, not of the declarations.

The Governed Interaction Boundary owns the mechanics of the boundary. This document specifies that
execution sits *behind* it. Nothing about how an interaction was carried may reach the traversal.

## 11. Refusal

Execution may meet a case the declarations do not answer: an unresolvable reference, an unrouted
outcome, an undeclared condition, or a violated obligation. Then it **refuses**. It does not
improvise, default or degrade.

Refusal does not originate behavior. It is **the enforcement of the declarations' boundary**, and it
is execution's one governance function. Where the declarations answer, execution realizes. Where they
do not, execution refuses. In neither case does it decide.

A system that refuses where its declarations run out shows that the declared world is closed. A
system that improvises there shows that it was never closed. Every earlier guarantee weakens by the
same amount.

## 12. What a run establishes

Execution originates nothing, so a run supports two independent checks. The second is the one that
matters:

| Check | Question | Establishes |
|---|---|---|
| **Result** | does the result conform to what the governing contract declared? | result conformance |
| **Path** | was the path recorded in evidence contained in the sealed representation? | path conformance |

The first check tests the result against its contract. **The second tests the architecture.** It asks
whether the sealed representation permitted what happened. That is a question about governance, not
about the answer produced. A system can produce acceptable results by ungoverned means, and only the
second check detects that.

**Neither check establishes that the result was the right one to want.** Whether an execution solved
the problem it was meant to solve is a judgment against an intent this document does not carry. That
judgment belongs to the mechanism that validates against declared intent, not to execution
semantics.

A party performs both checks against evidence, and need not have observed the run (AI-16).

## 13. Structural independence

Where steps are independent, the declarations state that independence. It is not a scheduling
decision.

- Where a system exhibits concurrency, it **reads that concurrency from the declared structure**. The
  concurrency is not engineered into the agent that performs execution.
- **Executions MUST NOT depend on undeclared ambient state.** Where independence is declared, no
  undeclared shared state or interaction may introduce a dependency between executions. Executions
  may interact through governed state where declarations establish that they do. What is excluded is
  dependency nobody declared.

This document requires no concurrency and forbids none. It requires that a system declare whatever
independence it exploits. Then a run's meaning does not depend on how much parallelism the substrate
happened to apply.

## 14. What this document does not specify

- **The environment.** Node count, process model, scheduling, distribution and placement are
  unconstrained. A deployment decision changes *where* execution happens. It MUST NOT change what
  execution means.
- **The agent.** The Runtime Standard owns what performs execution and how it is organized
  internally.
- **The capability model.** The Capability Standard owns contracts, kinds of capability and bindings.
- **The outcome vocabulary.** A profile selects which outcomes a system's contracts declare. This
  family does not.

## 15. Normative invariants

- **EX-1.** Execution MUST NOT originate behavior. Every step MUST realize behavior the sealed
  representation already determined (§3).
- **EX-2.** Traversal MUST advance only on declared outcomes, according to routing resolvable from the
  sealed representation alone (§3.2, §4.1).
- **EX-3.** Routing MUST NOT be computed from payload, environment, accumulated state, or caller
  identity (§3.2).
- **EX-4.** The structure traversed MUST NOT be added to, removed from, or rerouted during a run
  (§3.2).
- **EX-5.** A result a contract does not declare as an outcome MUST NOT be routed on, admitted into
  the governed transition, or recorded as an outcome, and MUST produce refusal. An outcome for which
  no routing is declared MUST produce refusal (§4.1, §4.3).
- **EX-6.** Failure paths MUST be declared outcomes with declared routing. No recovery, retry,
  fallback, or degraded path MUST exist that the declarations did not specify (§4.2).
- **EX-7.** A step's inputs MUST be resolved from declared references, and MUST NOT be searched for
  or inferred (§5).
- **EX-8.** Every change to governed state MUST be a transition the declarations determined,
  including its target and its permitting conditions (§6.1).
- **EX-9.** A governed store MUST be written only through its owner's declarations (§6.2).
- **EX-10.** The set of effects a system can produce MUST be closed and declared. No implicit effect
  path MUST exist (§7).
- **EX-11.** An event MUST NOT trigger execution (§8).
- **EX-12.** A step's result MUST conform to its governing contract's declared surface (§9).
- **EX-13.** No property of how an interaction arrived MUST be observable to the traversal (§10).
- **EX-14.** Where the declarations do not answer, execution MUST refuse, and MUST NOT default,
  improvise, or degrade (§11).
- **EX-15.** An execution MUST produce enough evidence for the path taken to be independently checked
  against the sealed representation (§12).
- **EX-16.** An outcome MUST NOT be treated as a governance refusal, whatever it is named. A refusal
  MUST NOT be reported as a routable outcome (§4.4, EN-8).
- **EX-17.** A captured input, and the outcome of the non-deterministic capability that produced it,
  MUST NOT select a route. They MAY influence routing only through the declared outcome of a
  deterministic step that evaluates the captured input (§4.5).
- **EX-18.** At every level of a declared composition, an outcome for which no continuation is
  declared MUST produce refusal. Execution MUST NOT proceed past it, and MUST NOT treat a missing
  continuation as a default (§4.3, §9).

## 16. Conformance

The conformance subject of this document is an **execution**: a single run of a governed system,
together with the evidence it produced.

An execution conforms when all of the following hold:

- Every step it performed was a step the sealed representation contained, reached by declared
  routing on a declared outcome (EX-1, EX-2, EX-5).
- No structure was constructed, extended or rerouted during it (EX-4).
- Every state change and every effect passed through a declared, owned surface (EX-8 … EX-10).
- It refused where its declarations did not answer, rather than proceeding, at every level of
  composition (EX-14, EX-18).
- Its evidence supports the path check of §12 by a party that did not observe it (EX-15).

**An execution that produced the expected result is not thereby conformant.** The result is one
check, and the weaker one. A run may reach an acceptable answer by a path the sealed representation
did not contain. That run is a non-conforming execution that happens to look successful. The path
check exists to catch exactly that case.

The Conformance Model and the Conformance Test Specification own how a party claims, levels and
demonstrates conformance, and what evidence discharges each invariant above. This document specifies
what an execution must be, not how a claim about one is established.
