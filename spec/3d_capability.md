# Capability

## 1. Scope

This document specifies the **capability**: the governed unit through which a system reaches
computational or external effect, and the contract that is the whole of what execution knows about
it.

The Execution Model says that execution dispatches capabilities and respects their declared effect
boundary; the Runtime Standard says the dispatching agent knows nothing beneath a contract. This
document says what a capability is, what its contract must declare, what the contract bounds, and —
importantly — what it does not.

It prescribes **no realization**. A capability may be realized as a local computation, a service, a
remote operation, a hardware function, a manual procedure, or anything else. What is required is
what is declared and what is preserved, never how the work is done.

This document introduces the terms **capability contract**, **binding**, **effecting**, and
**non-effecting**. Every other term it uses is defined by the Conceptual Model, the Semantic Model,
or Parts II–III.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What a capability is

A **capability** is a governed unit of execution: the thing a traversal dispatches to when a step is
reached.

It has two parts, and the separation between them is the subject of this document:

```
capability contract    what is declared    governed, and known to execution
        │  bound to
realization            what does the work  opaque to execution except through the contract
```

**The contract is the capability, as far as the governed system is concerned.** The realization is
how the contract is met. A system's declarations reach exactly to the contract and stop there.

## 3. The contract

A **capability contract** declares:

| Declares | Meaning |
|---|---|
| **inputs** | what the capability requires, and in what form |
| **outputs** | what it produces on each outcome |
| **outcomes** | the closed, enumerated set of results it may report |
| **effect disposition** | whether it may produce effects beyond governed state (§5) |

All four declarations are closed: the contract declares the complete interface and disposition
relevant to execution. This is closure of the *interface*, not of the value domain — a contract may
accept an input whose possible values are unbounded, provided what it accepts is declared. A
contract that leaves any of the four open has declared that something about the capability is not
governed, and execution would be dispatching to something whose shape it cannot state.

### 3.1 The contract is the entire interface

**Execution knows the contract and knows nothing beneath it.** Not what the capability means, not
how it is realized, not what it does internally, not what it costs — only that it takes these
inputs and reports one of these outcomes.

This ignorance is what makes realizations interchangeable (§8), and it is deliberate: an execution
agent that knew more than the contract could act on what it knew, and acting on knowledge no
declaration supplied is origination (AI-1, RT-1).

### 3.2 Outcomes

A contract's outcomes are the **only** thing traversal routes on (EX-2). Consequently:

- The outcome set MUST be closed and enumerated. "Whatever the realization returns" is not an
  outcome set.
- **Failure outcomes are declared alongside successes.** A capability that can fail declares how,
  and each failure is routed like any other outcome (EX-6).
- A realization that reports something outside the set has violated its contract; execution refuses
  and MUST NOT route on it (EX-5). **The undeclared value is not thereby an additional outcome** —
  an outcome set is extended by declaration, never by something having been returned.
- **An outcome named for refusal is a declared result, not a governance refusal** (3a §4.4, EX-16).
  A contract naming one carries the distinction rather than relying on the word: what the capability
  reported about its own subject matter is not a determination that the capability was permitted to
  be reached.

## 4. Inputs and outputs

- A capability receives its inputs through declared references resolved before dispatch (EX-7). It
  MUST NOT reach for anything else — not context, not environment, not ambient state, not the
  identity of whatever invoked it.
- A capability's outputs MUST conform to what its contract declares for the outcome reported
  (EX-12). Routing an output is permitted; redefining one is not.
- **A capability has no channel to execution other than its declared outcome and outputs.** There is
  no side channel, no out-of-band signal, and no shared location through which it may communicate
  governed information the contract did not declare. What a realization does internally — shared
  memory, a store, hardware state — is its own business; what it may convey *to execution* is the
  contract and nothing else.

## 5. The effect distinction

Every capability declares whether it may produce effects beyond the governed state of the system.
The distinction is **enforced, not conventional**.

### 5.1 Non-effecting capabilities

A capability declared **non-effecting** produces no effect beyond returning its declared outputs.

- It MUST NOT write governed state, reach an external system, or produce any governed or external
  effect other than returning its declared outputs. Incidental consequences of computing — time
  taken, resources consumed — are not effects in this sense.
- **It MUST NOT invoke an effecting capability**, directly or transitively. A non-effecting
  capability that can reach an effect through another capability is effecting, and its declaration
  is false.
- It MAY invoke other non-effecting capabilities.

The transitive clause is the load-bearing one. Without it, the distinction survives only at the
first level and any effect is reachable by one more hop.

### 5.2 Effecting capabilities

A capability declared **effecting** may produce effects, and every effect it may produce is within
what its contract declares.

**The set of effecting capabilities is the system's entire governed mutation surface.** There is no implicit
write path, no incidental output, and no effect that reaches the world other than through a
declared effecting capability (EX-10).

This is what makes the question *what can this system do?* answerable. A system whose effects all
pass through declared, enumerable capabilities can state its reach; one whose effects can originate
anywhere cannot, and no amount of inspection recovers the answer.

## 6. Binding

A **binding** associates a contract with a realization.

- A binding MUST be declared. A realization is never reached by discovery, by naming convention, by
  location, or by registration that happened at load (AI-12, AI-2).
- A binding MUST resolve before the capability is dispatched (AI-5). An unresolved binding at
  execution is a refusal, and is the signature of a construction that did not complete.
- **A binding carries no semantics.** It says which realization meets a contract; it never modifies,
  extends, narrows, or reinterprets what the contract declares. A binding that changes the meaning
  of a contract is an undeclared amendment to governance.
- A contract MAY have different bindings in different systems, or over time. Changing a binding is a
  governed transition.

## 7. What the contract bounds — and what it does not

An objection arrives here and deserves a direct answer: if realizations are ordinary code, has
behavior not simply moved *into* the code, leaving the arrangement intact in name and lost in fact?

The answer has three parts, and honesty requires all three.

**First, the contract bounds the shape.** Inputs, outputs, outcomes, and effect disposition are
declared, and conformance to them is determined rather than assumed. A realization cannot widen its
outcomes, reroute execution, produce an undeclared effect, or reinterpret what it was asked for.
Whatever it does, it does inside those bounds.

**Second, the contract does not establish that the realization is correct.** A capability can
satisfy its contract completely and compute the wrong thing. **This residue is real and this
document does not close it** — no declaration of shape can determine that an implementation computes
what was wanted.

**Third, no *ungoverned* behavior survives in the gap.** What the realization contributes is effort,
not authority. It cannot change what may be reached, what may follow, what may be affected, or what
the system may become; all of that sat upstream. The residue is a question of correctness, and
correctness is judged by validating a realized system against **declared intent** — a determination
made elsewhere, and never by dispatch.

Stating the residue plainly is preferable to a standard that appears to eliminate it. A reader who
believes contract conformance implies correctness will stop looking for the thing that actually
checks it.

## 8. Substitutability

**Any realization satisfying a contract may replace any other, and execution cannot tell.**

- Two realizations of one contract MUST produce the same declared outcome and the same governed
  outputs for the same inputs, or at least one does not satisfy the contract. Observational content
  that is not a governed output — a measurement, a generated identifier, a reading taken at the
  moment of execution — may differ without the contract being violated.
- Replacing a realization MUST NOT change any governed consequence, and MUST NOT require a change to
  any declaration.
- A realization MUST NOT be depended upon for anything its contract does not declare. Code that
  relies on a realization's incidental behavior has taken a dependency the governed system does not
  carry and cannot honor.

Substitutability is not a convenience. It is the observable form of the claim that behavior lives in
the declarations: if a realization could be swapped and something governed changed, behavior was
living in the realization.

## 9. Capabilities are governed

A capability contract is a declared artifact and is governed as any other is: it has an identity, a
declared classification, a closure, and obligations that apply to it.

- **A capability is not a source of authority.** It performs work; it does not determine what may be
  done (GO-8). A capability whose invocation confers permission has become a governing element
  nobody declared.
- **Invocability is not permission.** That a capability exists and can be reached does not establish
  that a given actor, interaction, or state may reach it. Whether it may is determined by the
  governance applicable to that determination, not by the capability being present.

## 10. What a capability is not

- **Not a function.** A function is one way to realize one. Nothing about a capability requires
  local invocation, synchronous return, or a single address space.
- **Not a service.** A service is another way. Nothing requires remoteness, a network, or an
  independent lifecycle.
- **Not a plugin.** A capability is declared and bound, not discovered and loaded. The difference is
  whether something admitted it.
- **Not an extension point.** Adding a capability extends what a system may do only through
  declaration and admission — never by placing a realization where something will find it.

## 11. What this document does not specify

- **How a capability is realized**, in what language, on what substrate, or with what lifecycle.
- **How a contract is expressed.** Any form serves that closes inputs, outputs, outcomes, and effect
  disposition.
- **What outcomes a system's contracts declare.** An outcome vocabulary is a profile's selection.
- **How correctness is validated.** The residue of §7 is judged against declared intent, elsewhere.
- **What kinds of capability a system distinguishes** beyond the effect disposition this document
  requires. A profile may distinguish more; it may not collapse this one.

## 12. Normative invariants

- **CP-1.** A capability MUST be reachable only through its declared contract (§3.1).
- **CP-2.** A contract MUST declare closed sets of inputs, outputs, and outcomes, and MUST declare
  its effect disposition (§3).
- **CP-3.** Execution MUST NOT depend on anything beneath a contract (§3.1).
- **CP-4.** A result that is not a declared outcome MUST NOT be routed on (§3.2).
- **CP-5.** A capability MUST NOT acquire inputs other than through declared references (§4).
- **CP-6.** A capability MUST NOT communicate with execution other than through its declared outcome
  and outputs (§4).
- **CP-7.** A non-effecting capability MUST produce no effect and MUST NOT invoke an effecting
  capability, directly or transitively (§5.1).
- **CP-8.** Every effect a system produces MUST pass through a declared effecting capability (§5.2).
- **CP-9.** A binding MUST be declared, MUST resolve before dispatch, and MUST NOT alter what the
  contract declares (§6).
- **CP-10.** Replacing a realization that satisfies a contract MUST NOT change a governed
  consequence and MUST NOT require a declaration to change (§8).
- **CP-11.** A capability MUST NOT be a source of authority, and its reachability MUST NOT
  constitute permission to reach it (§9).

## 13. Conformance

The conformance subject of this document is a **capability**: a contract, its binding, and the
realization bound to it.

A capability conforms when its contract closes what §3 requires, its binding is declared and
resolves before dispatch, its realization reports only declared outcomes and produces only effects
its disposition permits, and nothing about it is reachable or dependable except through the
contract.

**The effect disposition is the claim most easily made falsely**, because a non-effecting
declaration is satisfied on every run in which the effect path is not taken. What establishes it is
not observation of runs but the absence of any reachable path — direct or transitive — from the
realization to an effect.

How that is required and evaluated belongs to the Conformance Test Specification.
