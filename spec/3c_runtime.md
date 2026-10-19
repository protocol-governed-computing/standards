# Runtime

## 1. Scope

This document specifies the **runtime**: the agent that performs execution. It establishes:

- what a runtime consumes;
- what it may decide;
- what it must produce;
- what it must refuse;
- most important of all, what it may not be.

The Execution Model says what execution is. This document bounds the thing that performs it. The
Snapshot Standard says what the runtime consumes. This document states the runtime's obligations
toward that input. The Capability Standard covers the units the runtime dispatches. Evidence,
Attestation & Provenance covers what it records.

**A runtime is a role, not a component.** Nothing here requires a program, a process, a service, a
language, or a count of any of them. A realization satisfies this document by what its execution
agency does and does not do, however that agency is organized.

This document introduces the terms **governed decision** and **mechanism decision**. The Conceptual
Model, the Semantic Model or Parts II–III defines every other term it uses.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. The runtime is defined by what it may not do

Most components are specified by their capabilities. A runtime is specified by its
**incapacities**. That inversion is the point, not a matter of style.

A runtime:

- holds no domain meaning;
- makes no governing determination;
- adds nothing to the representation it executes;
- originates no governed behavior.

**The exclusions set the boundary. The obligations in this document set the permitted role within
it.** A specification that started from the runtime's capabilities would have to list them all. It
would fail closed only by accident. Starting from the exclusions, anything that is neither excluded
nor obliged is permitted, because it cannot matter (§4).

## 3. What a runtime consumes

A runtime receives only the governed inputs the applicable standards define. At present those are:

| Input | What it is |
|---|---|
| **an accepted snapshot** | the governed representation, verified before use (§3.1) |
| **an interaction** | what is presented for execution, in canonical form |
| **governed state** | the state the snapshot declares, as it currently stands |

**It receives nothing else.** It receives no configuration, no environment and no defaults. It
receives nothing carried over from a previously accepted snapshot, and nothing discovered where it
happens to run (SN-10, AI-12). The requirement is the exclusion, not the count of inputs: **every
source of behavior that reaches execution is declared.** A later standard may define a further
governed input. Only inputs that some standard defines may reach the runtime.

### 3.1 Acceptance is the runtime's obligation

A runtime MUST establish the acceptance conditions of the Snapshot Standard **before executing
anything against a snapshot**. Those conditions are integrity, identity, totality and claimed
profile. The runtime MUST refuse the snapshot whole where any condition fails.

Two consequences follow:

- **Verification precedes the first execution, not the first failure.** Suppose a runtime verifies
  lazily, or verifies a constituent only when it first reaches for it. It has then executed against
  unverified content, and it cannot say afterwards what it executed.
- **Acceptance is not a load.** The runtime performs acceptance as a determination against the
  Snapshot Standard's conditions. A runtime that loads a snapshot and reports nothing has made no
  determination anyone can check. Evidence, Attestation & Provenance owns how that determination is
  evidenced.

After acceptance, the runtime treats the snapshot as immutable for as long as it executes against
it. A runtime MUST NOT modify, extend, annotate, or repair an accepted snapshot.

## 4. What a runtime may decide

A runtime necessarily decides things. It schedules, allocates, orders and places. A standard that
claimed the runtime decides nothing would be false, and someone would exploit the falsehood.

The line is exact:

> **A decision is permitted if and only if varying it cannot vary any declared governed
> consequence.**

Such a decision is a **mechanism decision**. A decision that can vary a governed consequence is a
**governed decision**, and a runtime makes none (§5).

These decisions are permitted, because none of them can change what the snapshot determines:

- when work is scheduled, and how long it takes;
- how resources are allocated, and how much;
- where a step is performed, and on what substrate;
- how the runtime internally represents or retains what it has read from the snapshot;
- the order in which it performs steps that the declarations state are independent;
- how many executions proceed concurrently.

The test is not whether a decision is small, or whether it is internal. **The test is whether a
different choice could produce a different governed consequence.** If it could, the decision belongs
to the declarations. A runtime that takes it has taken authority it does not hold, however reasonable
the choice was.

## 5. What a runtime must not decide

A runtime MUST NOT determine:

| It must not decide | Because that belongs to |
|---|---|
| whether something may exist or be admitted | the governance declarations, realized by construction |
| which step follows a step | declared routing |
| what an outcome means, or which outcome obtained | the capability's contract |
| whether an obligation applies to a subject | the governance closure |
| what governed state may become | the declared transition |
| whether to proceed where the declarations do not answer | nothing — it refuses (§7) |

It may not decide any of these *partially* either. Examples of partial decisions:

- supplying a default where a declaration is silent;
- selecting among candidates where a reference is ambiguous;
- choosing an interpretation where a value is unexpected;
- retrying where an outcome was not routed.

**Each of these is a governed decision that looks like an implementation detail.** Each is a point
where behavioral authority re-enters a system that was otherwise governed.

## 6. What a runtime must produce

- **The governed consequences the snapshot determines** for the interaction presented, and nothing
  beyond them.
- **Evidence** adequate to establish what was determined and what occurred (SM-8). The evidence
  includes the path taken, sufficient for the path check of Execution Model §12.
- **A refusal, evidenced**, wherever it refuses (§7).

A runtime MUST NOT produce effects the declarations did not establish, and MUST NOT withhold evidence
of effects it did produce. A runtime that produced an effect it cannot account for has placed
something outside governance, whether or not the effect was desirable.

## 7. Refusal is the runtime's one enforcement function

Where the declarations do not answer, the runtime **refuses**. This is the only enforcement function
it performs, and it performs it by declining, not by deciding. It enforces a boundary. It does not
exercise governance. The runtime governs nothing. Refusing is how it declines to act where nothing
governs.

Refusal does not originate behavior. It is the **enforcement of the declarations' boundary**. Where
the declarations answer, the runtime realizes. Where they do not, it refuses. In neither case does
it choose an outcome.

### 7.1 Evaluating a sealed obligation is not making a determination

Two statements in this document might seem to conflict. §2 says a runtime *makes no governing
determination*. The list below says a runtime refuses on *an obligation, applicable and evaluated,
that is not satisfied*. They are consistent, and this section says why, so the reader need not work
it out.

**Two acts are distinct, and only the second belongs to the runtime:**

| | The act | When | By what |
|---|---|---|---|
| **determination** | establishing *what governs* — which closure applies, under what authority, composing how | before sealing, at construction | governance (Governance Closure & Authority §10.1) |
| **application** | evaluating a sealed assertion against the sealed declarations, and refusing where it is unsatisfied | at execution | the runtime |

A runtime evaluates. **It does not decide what it evaluates, or what follows if the answer is no.**
Both were settled and sealed before it ran. Evaluating an already-determined obligation originates
nothing. Run it twice against the same sealed representation and the same governed state, and it
yields the same answer. Nothing about the answer is the runtime's to supply.

The distinction is checkable, not rhetorical. **A runtime that could have refused differently has
made a determination**, whatever it is called. It could have done so by consulting anything not in
the snapshot, by resolving an ambiguity the declarations left, or by selecting among applicable
obligations. It then broke SN-10 and RT-6. A runtime that could only have refused as it did has
applied an obligation.

A runtime MUST refuse, and MUST NOT improvise, default, degrade, retry, or continue, on:

- a snapshot that fails acceptance (§3.1);
- a reference that does not resolve;
- an outcome for which no routing is declared;
- a result that is not a declared outcome of the contract that produced it;
- an obligation, applicable and evaluated, that is not satisfied;
- any condition the declarations do not cover.

**A runtime with a recovery path nobody declared has a second, undeclared runtime inside it.** That
second runtime governs the cases that matter most.

## 8. Deliberate incapability

A runtime's ignorance is a **property**, not a limitation to engineer around.

The same agency executes a governed system of any domain. The declarations differ. The runtime does
not. Because it cannot tell one domain from another, it is substitutable, its behavior is
examinable, and it is small enough to reason about.

It is also a security property, and the strongest one available here: **anything a runtime cannot
use as a source of governed behavior cannot become an authority path through it.** A runtime with no
routing logic of its own cannot be manipulated into an alternate route. A runtime with no
interpretation path for unstructured input cannot be injected through it into behavior. Nobody added
these as defenses. They are authority paths that nobody ever built (AI-1, and Architectural
Invariants §9, *security by construction*).

This is a claim about governance surface, not about implementation soundness. A runtime still
suffers the ordinary failures of any built thing: resource exhaustion, memory faults, defects. What
it is free of is an attacker reaching *behavioral authority* through it, because no path exists by
which behavior enters.

Every capability given back to a runtime returns surface to an attacker and authority to the engine.
That includes every convenience, every helpful default and every "just in case" fallback.

## 9. Carrying nothing forward

A runtime **carries no behavioral state between executions or across snapshots.**

- It MUST NOT adapt, learn, tune, or accumulate anything that changes a governed consequence.
- It MUST NOT retain anything from a previously accepted snapshot that affects execution against the
  current one.
- It MUST NOT consult evidence of earlier executions in determining a present one (AI-15).

An optimization that cannot change a governed consequence is a mechanism decision, and it is
permitted (§4). An optimization that can is a governed decision, and it is forbidden, however small
the effect. A runtime whose behavior depends on what it has seen before is not deterministic with
respect to the governed execution model. Its executions are no longer functions of the snapshot.

## 10. Multiplicity and substitutability

**One snapshot, many conforming runtimes.**

- Any conforming runtime executing a given snapshot against given inputs and initial state, subject
  to the same declared external interactions, produces the same governed consequences (SN-11).
- A runtime MAY be replaced entirely, with a different implementation, language or substrate,
  without any governed consequence changing.
- Conversely, **declarations may change entirely while the runtime stays the same**. The runtime
  holds no domain meaning to update.

This is the practical form of the whole arrangement. Behavior lives in what travels, so whatever
executes it is replaceable. The governed system outlives any particular agent that ran it.

## 11. What a runtime is not

- **Not an orchestrator.** It does not arrange work. It traverses declared structure.
- **Not a framework.** Nothing extends it with domain behavior. A runtime with an extension point
  through which undeclared governed behavior can enter has an ungoverned path into execution.
  Extensions that carry no governed behavior are mechanism, and this rule does not exclude them.
  Examples are a storage engine, a hardware adapter and a transport binding.
- **Not a policy point.** Governance is in the snapshot. A runtime that carries policy carries
  governance nobody declared and no closure supplied.
- **Not a place for correctness.** Whether a capability computes the right answer is not the
  runtime's question, and cannot be. The runtime dispatches against contracts and knows nothing
  beneath them.

## 12. What this document does not specify

- **The internal organization of the agent.** Components, processes, threading, memory and
  concurrency mechanism are unconstrained.
- **The capability interface.** The Capability Standard owns what a contract is, and how a
  capability is bound and invoked.
- **The evidence format.** Evidence, Attestation & Provenance owns what evidence must establish.
- **The interaction boundary.** The Governed Interaction Boundary owns how an interaction reaches the
  runtime in canonical form.
- **Performance.** Nothing here constrains speed, throughput or resource use. Nothing here may be
  traded away to obtain them.

## 13. Normative invariants

- **RT-1.** A runtime MUST originate no governed behavior, hold no domain meaning, make no governing
  determination, and add nothing to the representation it executes (§2).
- **RT-2.** A runtime MUST consume only an accepted snapshot, an interaction, and declared governed
  state (§3).
- **RT-3.** A runtime MUST establish every acceptance condition before executing against a snapshot,
  and MUST refuse the snapshot whole on any failure (§3.1).
- **RT-4.** A runtime MUST NOT modify, extend, annotate, or repair an accepted snapshot (§3.1).
- **RT-5.** A runtime MAY take a decision only where varying it cannot vary a governed consequence
  (§4).
- **RT-6.** A runtime MUST NOT supply a default, select among ambiguous candidates, interpret an
  unexpected value, or retry an unrouted outcome (§5).
- **RT-7.** A runtime MUST produce the governed consequences the snapshot determines and nothing
  beyond them (§6).
- **RT-8.** A runtime MUST evidence every determination it makes, including every refusal (§6, §7).
- **RT-9.** A runtime MUST refuse wherever the declarations do not answer, and MUST NOT improvise,
  default, degrade, or continue (§7).
- **RT-10.** A runtime MUST NOT carry behavioral state between executions or across snapshots. It
  MUST NOT consult prior evidence in a present determination (§9).
- **RT-11.** A runtime MUST NOT expose an extension point through which domain behavior enters
  execution (§11).
- **RT-12.** Replacing a conforming runtime with another MUST NOT change any governed consequence
  (§10).
- **RT-13.** A runtime MUST NOT establish what governs a subject. It MUST evaluate obligations
  already determined and sealed, and MUST refuse rather than resolve what they leave open (§7.1).

## 14. Conformance

The conformance subject of this document is a **runtime**: the execution agency of a governed
system, however organized.

A runtime conforms when all of the following hold:

- it consumes only what §3 permits;
- it verifies before executing;
- it takes no decision that could vary a governed consequence;
- it produces the consequences the snapshot determines, together with evidence of them;
- it refuses wherever the declarations run out.

**Substitution, not inspection, establishes two properties:**

- A runtime holds no domain meaning if it executes a snapshot from a different domain unchanged.
- A runtime originates no behavior if another conforming runtime reaches the same governed
  consequences from the same snapshot.

Neither property is visible from one runtime's behavior on one snapshot. That is exactly where a
runtime that has quietly gained authority looks most correct.

The Conformance Test Specification owns how these properties are required and evaluated.
