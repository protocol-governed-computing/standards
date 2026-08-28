# Runtime

## 1. Scope

This document specifies the **runtime**: the agent that performs execution. It establishes what a
runtime consumes, what it may decide, what it must produce, what it must refuse, and — most
consequentially — what it may not be.

The Execution Model says what execution is; this document bounds the thing that performs it. The
Snapshot Standard says what it consumes; this document states its obligations toward that input.
The Capability Standard covers the units it dispatches; Evidence, Attestation & Provenance covers
what it records.

**A runtime is a role, not a component.** Nothing here requires a program, a process, a service, a
language, or a count of any of them. A realization satisfies this document by what its execution
agency does and does not do, however that agency is organized.

This document introduces the terms **governed decision** and **mechanism decision**. Every other
term it uses is defined by the Conceptual Model, the Semantic Model, or Parts II–III.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. The runtime is defined by what it may not do

Most components are specified by their capabilities. A runtime is specified by its **incapacities**,
and this inversion is the point rather than a stylistic choice.

A runtime:

- holds no domain meaning;
- makes no governing determination;
- adds nothing to the representation it executes;
- originates no governed behavior.

**The exclusions establish the boundary; the obligations in this document establish the permitted
role within it.** A specification that began from the runtime's capabilities would have to
enumerate them exhaustively and would fail closed only by accident; beginning from the exclusions,
anything not excluded and not obliged is permitted precisely because it cannot matter (§4).

## 3. What a runtime consumes

A runtime receives only the governed inputs the applicable standards define. At present those are:

| Input | What it is |
|---|---|
| **an accepted snapshot** | the governed representation, verified before use (§3.1) |
| **an interaction** | what is presented for execution, in canonical form |
| **governed state** | the state the snapshot declares, as it currently stands |

**It receives nothing else.** Not configuration, not environment, not defaults, not anything carried
over from a previously accepted snapshot, not anything discovered where it happens to be running
(SN-10, AI-12). The requirement is not the count of inputs but the exclusion: **no undeclared source
of behavior reaches execution.** A later standard may define a further governed input; nothing may
reach the runtime that no standard defined.

### 3.1 Acceptance is the runtime's obligation

A runtime MUST establish the acceptance conditions of the Snapshot Standard — integrity, identity,
totality, claimed profile — **before executing anything against a snapshot**, and MUST refuse the
snapshot whole where any fails.

Two consequences:

- **Verification precedes the first execution, not the first failure.** A runtime that verifies
  lazily, or verifies a constituent when it first reaches for it, has executed against unverified
  content and cannot say afterwards what it executed.
- **Acceptance is not a load.** It is a determination the runtime performs against the Snapshot
  Standard's conditions, and a runtime that loads a snapshot and reports nothing has made no
  determination anyone can check. How that determination is evidenced belongs to Evidence,
  Attestation & Provenance.

After acceptance, the runtime treats the snapshot as immutable for as long as it executes against
it. A runtime MUST NOT modify, extend, annotate, or repair an accepted snapshot.

## 4. What a runtime may decide

A runtime necessarily decides things. It schedules, allocates, orders, and places. A standard
claiming it decides nothing would be false, and the falsehood would be exploited.

The line is exact:

> **A decision is permitted if and only if varying it cannot vary any declared governed
> consequence.**

Such a decision is a **mechanism decision**. One that can vary a governed consequence is a
**governed decision**, and a runtime makes none (§5).

Permitted, because none of them can change what the snapshot determines:

- when work is scheduled, and how long it takes;
- how resources are allocated, and how much;
- where a step is performed, and on what substrate;
- how the runtime internally represents or retains what it has read from the snapshot;
- the order in which steps the declarations state to be independent are performed;
- how many executions proceed concurrently.

The test is not "is this decision small" or "is this decision internal." **It is whether a different
choice could produce a different governed consequence.** If it could, the decision belongs to the
declarations, and a runtime taking it has taken authority it does not hold — regardless of how
reasonable the choice was.

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

Nor may it decide any of these *partially*: supplying a default where a declaration is silent,
selecting among candidates where a reference is ambiguous, choosing an interpretation where a value
is unexpected, or retrying where an outcome was not routed. **Each of these is a governed decision
wearing the appearance of an implementation detail**, and each is where behavioral authority
re-enters a system that was otherwise governed.

## 6. What a runtime must produce

- **The governed consequences the snapshot determines** for the interaction presented — and nothing
  beyond them.
- **Evidence** adequate to establish what was determined and what occurred (SM-8), including the
  path taken, sufficient for the path check of the Execution Model §12.
- **A refusal, evidenced**, wherever it refuses (§7).

A runtime MUST NOT produce effects the declarations did not establish, and MUST NOT withhold
evidence of effects it did produce. A runtime that produced an effect it cannot account for has
placed something outside governance, whether or not the effect was desirable.

## 7. Refusal is the runtime's one enforcement function

Where the declarations do not answer, the runtime **refuses**. This is the only enforcement function
it performs, and it performs it by declining rather than by deciding. It is enforcement of a
boundary, not an exercise of governance: the runtime governs nothing, and refusing is how it
declines to act where nothing governs.

Refusal is not origination. It is the **enforcement of the declarations' boundary**: where the
declarations answer, the runtime realizes; where they do not, it refuses. In neither case does it
choose an outcome.

### 7.1 Evaluating a sealed obligation is not making a determination

§2's exclusion — a runtime *makes no governing determination* — and the trigger below — *an
obligation, applicable and evaluated, that is not satisfied* — are consistent, and the sentence that
reconciles them belongs here rather than in a reader's head.

**Two acts are distinct, and only the second is the runtime's:**

| | The act | When | By what |
|---|---|---|---|
| **determination** | establishing *what governs* — which closure applies, under what authority, composing how | before sealing, at construction | governance (2e §10.1) |
| **application** | evaluating a sealed assertion against the sealed declarations, and refusing where it is unsatisfied | at execution | the runtime |

A runtime evaluates. **What it does not do is decide what it is evaluating, or what follows if the
answer is no** — both were settled and sealed before it ran. Evaluation of an already-determined
obligation originates nothing: run twice against the same sealed representation and the same
governed state, it yields the same answer, because nothing about the answer is the runtime's to
supply.

The distinction is checkable rather than rhetorical. **A runtime that could have refused differently
— by consulting anything not in the snapshot, by resolving an ambiguity the declarations left, by
selecting among applicable obligations — has made a determination**, whatever it is called, and
SN-10 and RT-6 are the invariants it broke. A runtime that could only have refused as it did has
applied one.

A runtime MUST refuse — and MUST NOT improvise, default, degrade, retry, or continue — on:

- a snapshot that fails acceptance (§3.1);
- a reference that does not resolve;
- an outcome for which no routing is declared;
- a result that is not a declared outcome of the contract that produced it;
- an obligation, applicable and evaluated, that is not satisfied;
- any condition the declarations do not cover.

**A runtime with a recovery path nobody declared has a second, undeclared runtime inside it**, and
that one governs the cases that matter most.

## 8. Deliberate incapability

A runtime's ignorance is a **property**, not a limitation to be engineered around.

The same agency executes a governed system of any domain — the declarations differ, the runtime
does not. That it cannot distinguish one domain from another is what makes it substitutable, what
makes its behavior examinable, and what makes it small enough to be reasoned about.

It is also a security property, and the strongest one available here: **what a runtime cannot use as
a source of governed behavior cannot become an authority path through it.** A runtime with no
routing logic of its own cannot be manipulated into an alternate route. One with no interpretation
path for unstructured input cannot be injected through it into behavior. These are not defenses that
were added; they are authority paths that were never constructed (AI-1, and Architectural Invariants
§9, *security by construction*).

This is a claim about governance surface, not about implementation soundness. A runtime remains
subject to the ordinary failures of any built thing — resource exhaustion, memory faults, defects.
What it is not subject to is an attacker reaching *behavioral authority* through it, because there
is no path by which behavior enters.

Every capability a runtime is given back — every convenience, every helpful default, every "just in
case" fallback — is surface returned to an attacker and authority returned to the engine.

## 9. Carrying nothing forward

A runtime **carries no behavioral state between executions or across snapshots.**

- It MUST NOT adapt, learn, tune, or accumulate anything that changes a governed consequence.
- It MUST NOT retain anything from a previously accepted snapshot that affects execution against
  the current one.
- It MUST NOT consult evidence of prior executions in determining a present one (AI-15).

Optimization that cannot change a governed consequence is a mechanism decision and permitted (§4).
Optimization that can is a governed decision and forbidden, however marginal the effect — a runtime
whose behavior depends on what it has seen before is not deterministic with respect to the governed
execution model, and its executions are no longer functions of the snapshot.

## 10. Multiplicity and substitutability

**One snapshot, many conforming runtimes.**

- Any conforming runtime executing a given snapshot against given inputs and initial state, subject
  to the same declared external interactions, produces the same governed consequences (SN-11).
- A runtime MAY be replaced entirely — different implementation, different language, different
  substrate — without any governed consequence changing.
- Conversely, **declarations may change entirely without the runtime changing**, because the runtime
  holds no domain meaning to update.

This is the practical form of the whole arrangement: behavior lives in what travels, so what
executes it is replaceable, and the governed system outlives any particular agent that ran it.

## 11. What a runtime is not

- **Not an orchestrator.** It does not arrange work; it traverses declared structure.
- **Not a framework.** Nothing extends it with domain behavior. A runtime with an extension point
  through which undeclared governed behavior can enter has an ungoverned path into execution.
  Extensions that carry no governed behavior — a storage engine, a hardware adapter, a transport
  binding — are mechanism, and are not what this excludes.
- **Not a policy point.** Governance is in the snapshot. A runtime that carries policy carries
  governance nobody declared and no closure supplied.
- **Not a place for correctness.** Whether a capability computes the right answer is not the
  runtime's question and cannot be; it dispatches against contracts and knows nothing beneath them.

## 12. What this document does not specify

- **The internal organization of the agent.** Components, processes, threading, memory, and
  concurrency mechanism are unconstrained.
- **The capability interface.** What a contract is, and how a capability is bound and invoked,
  belongs to the Capability Standard.
- **The evidence format.** What evidence must establish belongs to Evidence, Attestation &
  Provenance.
- **The interaction boundary.** How an interaction reaches the runtime in canonical form belongs to
  the Governed Interaction Boundary.
- **Performance.** Nothing here constrains speed, throughput, or resource use, and nothing here may
  be traded away to obtain them.

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
- **RT-10.** A runtime MUST NOT carry behavioral state between executions or across snapshots, and
  MUST NOT consult prior evidence in a present determination (§9).
- **RT-11.** A runtime MUST NOT expose an extension point through which domain behavior enters
  execution (§11).
- **RT-12.** Replacing a conforming runtime with another MUST NOT change any governed consequence
  (§10).
- **RT-13.** A runtime MUST NOT establish what governs a subject; it MUST evaluate obligations
  already determined and sealed, and MUST refuse rather than resolve what they leave open (§7.1).

## 14. Conformance

The conformance subject of this document is a **runtime**: the execution agency of a governed
system, however organized.

A runtime conforms when it consumes only what §3 permits, verifies before executing, takes no
decision that could vary a governed consequence, produces the consequences the snapshot determines
together with evidence of them, and refuses wherever the declarations run out.

**Two properties are established by substitution rather than by inspection.** That a runtime holds
no domain meaning is shown by executing a differently-domained snapshot unchanged; that it
originates no behavior is shown by another conforming runtime reaching the same governed
consequences from the same snapshot. Neither is visible from reading one runtime's behavior on one
snapshot, which is where a runtime that has quietly acquired authority looks most correct.

How these are required and evaluated belongs to the Conformance Test Specification.
