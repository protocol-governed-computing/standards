# Capability

## 1. Scope

This document specifies the **capability**: the governed unit through which a system reaches
computational or external effect. It also specifies the contract, which is all that execution knows
about a capability.

The Execution Model says that execution dispatches capabilities and respects their declared effect
boundary. The Runtime Standard says the dispatching agent knows nothing beneath a contract. This
document says:

- what a capability is;
- what its contract must declare;
- what the contract bounds;
- just as important, what the contract does not bound.

This document prescribes **no realization**. A capability may be realized as a local computation, a
service, a remote operation, a hardware function, a manual procedure, or anything else. The
requirements cover what is declared and what is preserved, never how the work is done.

This document introduces the terms **capability contract**, **binding**, **effecting**,
**non-effecting**, and **non-deterministic**. The Conceptual Model, the Semantic Model or Parts II–III defines every other term
it uses.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What a capability is

A **capability** is a governed unit of execution: the thing a traversal dispatches to when it reaches
a step.

A capability has two parts. This document is about the separation between them:

```
capability contract    what is declared    governed, and known to execution
        │  bound to
realization            what does the work  opaque to execution except through the contract
```

**As far as the governed system is concerned, the contract is the capability.** The realization is
how the contract is met. A system's declarations reach exactly to the contract and stop there.

## 3. The contract

A **capability contract** declares:

| Declares | Meaning |
|---|---|
| **inputs** | what the capability requires, and in what form |
| **outputs** | what it produces on each outcome |
| **outcomes** | the closed, enumerated set of results it may report |
| **effect disposition** | whether it may produce effects beyond governed state (§5) |
| **determinism disposition** | whether its declared inputs determine its result (§5.3) |

All four declarations are closed. The contract declares the complete interface and disposition that
matter to execution. This is closure of the *interface*, not of the value domain. A contract may
accept an input whose possible values are unbounded, provided it declares what it accepts. A contract
that leaves any of the four open has declared that something about the capability is ungoverned.
Execution would then dispatch to something whose shape it cannot state.

### 3.1 The contract is the entire interface

**Execution knows the contract and nothing beneath it.** It does not know what the capability means,
how it is realized, what it does internally or what it costs. It knows only that the capability
takes these inputs and reports one of these outcomes.

This ignorance is deliberate, and it makes realizations interchangeable (§8). An execution agent
that knew more than the contract could act on what it knew. Acting on knowledge no declaration
supplied is origination (AI-1, RT-1).

### 3.2 Outcomes

A contract's outcomes are the **only** thing traversal routes on (EX-2). Consequently:

- The outcome set MUST be closed and enumerated. "Whatever the realization returns" is not an
  outcome set.
- **Failure outcomes are declared alongside successes.** A capability that can fail declares how. Each
  failure is routed like any other outcome (EX-6).
- A realization that reports something outside the set has violated its contract. Execution refuses
  and MUST NOT route on it (EX-5). **The undeclared value does not thereby become an extra outcome.**
  Only declaration extends an outcome set. A returned value never does.
- **An outcome named for refusal is a declared result, not a governance refusal** (Execution Model
  §4.4, EX-16). A contract that names one carries the distinction explicitly and does not rely on
  the word. What the capability reported about its own subject matter is not a determination that
  the capability could be reached.

## 4. Inputs and outputs

- A capability receives its inputs through declared references resolved before dispatch (EX-7). It
  MUST NOT reach for anything else: not context, not environment, not ambient state, and not the
  identity of whatever invoked it.
- A capability's outputs MUST conform to what its contract declares for the outcome reported (EX-12).
  Execution may route an output. It may not redefine one.
- **A capability's only channel to execution is its declared outcome and outputs.** It has no side
  channel, no out-of-band signal, and no shared location for conveying governed information the
  contract did not declare. What a realization does internally is its own business, whether it uses
  shared memory, a store or hardware state. What it may convey *to execution* is the contract and
  nothing else.

## 5. The effect distinction

Every capability declares whether it may produce effects beyond the governed state of the system.
The distinction is **enforced, not conventional**.

### 5.1 Non-effecting capabilities

A capability declared **non-effecting** produces no effect beyond returning its declared outputs.

- It MUST NOT write governed state, reach an external system, or produce any governed or external
  effect other than returning its declared outputs. Incidental consequences of computing, such as
  time taken and resources consumed, are not effects in this sense.
- **It MUST NOT invoke an effecting capability**, directly or transitively. A non-effecting
  capability that can reach an effect through another capability is effecting, and its declaration
  is false.
- It MAY invoke other non-effecting capabilities.

The transitive clause carries the weight. Without it, the distinction holds only at the first level,
and one more hop reaches any effect.

### 5.2 Effecting capabilities

A capability declared **effecting** may produce effects. Every effect it may produce is within what
its contract declares.

**The set of effecting capabilities is the system's entire governed mutation surface.** There is no
implicit write path and no incidental output. Effects reach the world only through declared effecting
capabilities (EX-10).

This makes the question *what can this system do?* answerable. A system whose effects all pass
through declared, enumerable capabilities can state its reach. A system whose effects can originate
anywhere cannot, and no amount of inspection recovers the answer.

### 5.3 Non-deterministic capabilities

A capability is **non-deterministic** when its declared inputs do not determine its result. It reads
a clock, draws a random value, or asks something outside the governed system. Its contract MUST
declare that it is non-deterministic.

- Each result it produces is a **captured input** (Conceptual Model, *captured input*). The result
  MUST be recorded once, where it is produced, before anything consumes it.
- Its result and its outcome select no route. A deterministic step must judge the result first
  (EX-17).
- The non-deterministic disposition is independent of the effect disposition. A non-deterministic
  capability may be non-effecting, such as one that reads a clock.

A contract that declares a capability deterministic makes a claim that substitution can test (§8). A
realization whose result varies for the same inputs breaks that claim.

## 6. Binding

A **binding** associates a contract with a realization.

- A binding MUST be declared. Execution never reaches a realization by discovery, naming convention,
  location, or registration that happened at load (AI-12, AI-2).
- A binding MUST resolve before the capability is dispatched (AI-5). An unresolved binding at
  execution is a refusal. It is the signature of a construction that did not complete.
- **A binding carries no semantics.** It says which realization meets a contract. It never modifies,
  extends, narrows or reinterprets what the contract declares. A binding that changes a contract's
  meaning is an undeclared amendment to governance.
- A contract MAY have different bindings in different systems, or over time. Changing a binding is a
  governed transition.

## 7. What the contract bounds — and what it does not

An objection arises here, and it deserves a direct answer. If realizations are ordinary code, has
behavior simply moved *into* the code? Is the arrangement then intact in name and lost in fact?

The answer has three parts, and honesty requires all three.

**First, the contract bounds the shape.** Inputs, outputs, outcomes and effect disposition are
declared, and conformance to them is determined, not assumed. A realization cannot widen its
outcomes, reroute execution, produce an undeclared effect, or reinterpret what it was asked for.
Whatever it does, it does inside those bounds.

**Second, the contract does not establish that the realization is correct.** A capability can satisfy
its contract completely and still compute the wrong thing. **This residue is real, and this document
does not close it.** No declaration of shape can determine that an implementation computes what was
wanted.

**Third, no *ungoverned* behavior survives in the gap.** The realization contributes effort, not
authority. It cannot change what may be reached, what may follow, what may be affected, or what the
system may become. All of that was settled upstream. The residue is a question of correctness.
Correctness is judged by validating a realized system against **declared intent**. That
determination is made elsewhere, never by dispatch.

A plain statement of the residue is better than a standard that appears to remove it. A reader who
believes contract conformance implies correctness will stop looking for the thing that actually
checks correctness.

## 8. Substitutability

**Any realization that satisfies a contract may replace any other, and execution cannot tell.**

- Two realizations of one contract MUST produce the same declared outcome and the same governed
  outputs for the same inputs. Otherwise at least one does not satisfy the contract. For a
  non-deterministic capability, the comparison holds the captured inputs constant (§5.3). Observational
  content that is not a governed output may differ without violating the contract. Examples are a
  measurement, a generated identifier, and a reading taken at the moment of execution.
- Replacing a realization MUST NOT change any governed consequence, and MUST NOT require a change to
  any declaration.
- A realization MUST NOT be depended upon for anything its contract does not declare. Code that
  relies on a realization's incidental behavior has taken a dependency that the governed system does
  not carry and cannot honor.

Substitutability is not a convenience. It is the observable form of the claim that behavior lives in
the declarations. If swapping a realization changed something governed, behavior was living in the
realization.

## 9. Capabilities are governed

A capability contract is a declared artifact, governed as any other artifact is. It has an identity,
a declared classification, a closure, and obligations that apply to it.

- **A capability is not a source of authority.** It performs work. It does not determine what may be
  done (GO-8). A capability whose invocation confers permission has become a governing element nobody
  declared.
- **Invocability is not permission.** A capability that exists and can be reached is not thereby
  open to a given actor, interaction or state. The governance applicable to that determination
  decides whether it may be reached. The capability's presence does not.

## 10. What a capability is not

- **Not a function.** A function is one way to realize a capability. Nothing about a capability
  requires local invocation, synchronous return or a single address space.
- **Not a service.** A service is another way. Nothing requires remoteness, a network or an
  independent lifecycle.
- **Not a plugin.** A capability is declared and bound, not discovered and loaded. The difference is
  whether something admitted it.
- **Not an extension point.** Adding a capability extends what a system may do only through
  declaration and admission. Placing a realization where something will find it extends nothing.

## 11. What this document does not specify

- **How a capability is realized**, in what language, on what substrate, or with what lifecycle.
- **How a contract is expressed.** Any form serves that closes inputs, outputs, outcomes and effect
  disposition.
- **What outcomes a system's contracts declare.** A profile selects an outcome vocabulary.
- **How correctness is validated.** The residue of §7 is judged against declared intent, elsewhere.
- **What kinds of capability a system distinguishes** beyond the effect disposition this document
  requires. A profile may distinguish more. It may not collapse this one.

## 12. Normative invariants

- **CP-1.** A capability MUST be reachable only through its declared contract (§3.1).
- **CP-2.** A contract MUST declare closed sets of inputs, outputs, and outcomes, and MUST declare its
  effect disposition (§3).
- **CP-3.** Execution MUST NOT depend on anything beneath a contract (§3.1).
- **CP-4.** A result that is not a declared outcome MUST NOT be routed on (§3.2).
- **CP-5.** A capability MUST NOT acquire inputs other than through declared references (§4).
- **CP-6.** A capability MUST NOT communicate with execution other than through its declared outcome
  and outputs (§4).
- **CP-7.** A non-effecting capability MUST produce no effect and MUST NOT invoke an effecting
  capability, directly or transitively (§5.1).
- **CP-8.** Every effect a system produces MUST pass through a declared effecting capability (§5.2).
- **CP-9.** A binding MUST be declared and MUST resolve before dispatch. It MUST NOT alter what the
  contract declares (§6).
- **CP-10.** Replacing a realization that satisfies a contract MUST NOT change a governed consequence
  and MUST NOT require a declaration to change (§8).
- **CP-11.** A capability MUST NOT be a source of authority, and its reachability MUST NOT constitute
  permission to reach it (§9).
- **CP-12.** A contract MUST declare whether its capability is non-deterministic. Each result a
  non-deterministic capability produces MUST be recorded as a captured input before anything
  consumes it (§5.3).

## 13. Conformance

The conformance subject of this document is a **capability**: a contract, its binding, and the
realization bound to it.

A capability conforms when all of the following hold:

- its contract closes what §3 requires;
- its binding is declared and resolves before dispatch;
- its realization reports only declared outcomes and produces only effects its disposition permits;
- nothing about it is reachable or dependable except through the contract.

**The effect disposition is the claim most easily made falsely.** A non-effecting declaration is
satisfied on every run that does not take the effect path. Observing runs does not establish the
disposition. The absence of any reachable path from the realization to an effect, direct or
transitive, establishes it.

The Conformance Test Specification owns how that is required and evaluated.
