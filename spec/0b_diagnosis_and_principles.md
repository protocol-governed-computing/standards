# Diagnosis and Principles

*This document explains why the problem persists and what any solution must satisfy. Problem and
Motivation, the document before it, shows that the problem is real, expensive and structural. This
document is non-normative: only the normative parts create obligations.*

## 1. The diagnosis is about authority

The failures in the previous document do not come from a lack of skill, discipline or tools. They
come from **where behavioral authority sits**: which part of a system has the right to decide what
the system does.

Conventional software puts that authority in two places where nobody can examine it. At run time,
**the engine holds it**. When the system changes, **nothing holds it**. Each placement causes four
difficulties. Neither set depends on a particular language or framework.

## 2. Authority held by the runtime

A conventional runtime does more than carry out decisions already made. It makes them. It evaluates
conditions, chooses branches and resolves dispatch. Sometimes it even builds the structure it is
about to execute.

| Difficulty | Because |
|---|---|
| **runtime decisioning** | behavior belongs to the run, not to the artifact |
| **hidden behavior** | nobody can fully know the behavior before execution; to learn what a system does, you must run it and watch which paths that run happened to take |
| **poor replay** | a second run may not reproduce the first, because decisions depended on surrounding conditions that the artifact does not contain |
| **platform dependence** | behavior is tangled up with the engine that produced it; it cannot move to another platform, because it never lived wholly in the thing that moves |

## 3. Authority lost at the specification

Conventional development is **open-loop**. Requirements go in and a running system comes out.
Nobody systematically compares the two in a governed way.

| Difficulty | Because |
|---|---|
| **requirements leakage** | nothing in a requirements document stops design decisions from piling up inside it |
| **rationale decay** | the document records what was decided but rarely why; the system inherits the decisions and loses their reasons |
| **governance externalization** | governance becomes a wrapper around engineering instead of a property of it |
| **evolution amnesia** | when the system must change, nobody can see inside the thing being changed, so changing it becomes archaeology |

**The second set of difficulties returns in full whenever a system must change.** So the process of
change must itself be governed. Good practice around it is not enough.

## 4. Why the prevailing model produces both

In the application-centric model, the application is the basic unit of design. The model has three
structural properties. Nobody notices them, because everyone assumes the model instead of choosing
it.

- **Behavior is embedded.** What a system does cannot be separated from how it does it. To understand
  the intent, you must read the code.
- **Governance is implicit.** Real rules constrain the system, and the system depends on them. Those
  rules live in comments, conventions and memory, where no structural check can see them.
- **Structure is emergent.** Nobody declares the true architecture. People discover it afterwards, by
  reading code and tracing execution.

The model was not a mistake. It was efficient when systems were small and change moved at human
speed. **It made software possible. It did not make software governable.** Today people use it to
build at a scale and speed it was never able to handle.

## 5. What follows

If the difficulties come from where authority sits, only moving the authority can fix them. Every
principle below follows from one move. Behavioral authority leaves the implementation and the engine.
It moves **into explicit, versioned, machine-consumable declarations, which are validated before
anything runs**. A governed process then controls how those declarations change.

## 6. Principles

PGC was developed from these principles, and its reference realization was built against them.

- **Protocol is the source of truth.** Declared artifacts carry behavior. Code does not. You can
  regenerate code, replace it or have a machine write it, and governance is unaffected.
- **Behavior is complete before execution begins.** Behavior must not emerge at run time. So it must
  already exist, whole, when run time starts.
- **Resolution happens before execution.** Execution can traverse only the paths that construction
  built.
- **The engine is deliberately incapable.** The execution engine interprets no domain meaning. This
  is a design choice, not a limitation to work around. Every judgment the engine declines to make was
  made earlier, where someone could review it.
- **Zero inference.** There are no implicit defaults, no heuristics and no discovery by scanning.
  What is undeclared is absent.
- **Fail hard.** A missing artifact, a missing binding or a violated invariant causes a refusal.
  Graceful degradation would hide an architectural violation.
- **Determinism and structural replay.** The same governed input yields the same result. Replay is a
  property of the artifact. It does not require rebuilding an environment.
- **No ambient authority.** Authority comes only from declarations, never from the execution
  context. As a result, whole classes of confused-deputy failure cannot occur, so nobody needs to
  defend against them.
- **Sealed execution input.** Execution consumes only sealed state. To change behavior, you change
  the declarations and construct again. You never act on the running system.
- **Compression is a feature.** A small vocabulary with strong invariants beats a large one with
  heuristic flexibility. An ontology that grows without a governed need adds debt.
- **The process of change is itself governed.** Evolution transforms one governed state into the
  next, and each step is declared and evidenced. Nobody authors changes off to the side of the
  system.

## 7. Principles are not requirements

**A principle discharges no obligation.** It cannot stand in for a normative statement. It does not
permit any behavior that the normative documents do not permit. Nobody may cite it in place of a
normative statement.

When a principle and a normative document seem to differ, **the normative document governs**. The
principle was an argument, never an authority. The family applies the same rule to its own sources.
The papers and the reference realization may argue from what was built. This family may not.

## 8. Where this is developed

- **The prevailing model and its structural properties**: *Protocol-Governed Systems*, Chapter 1,
  "Why Software Breaks at Scale."
- **Where behavioral authority sits, and the four difficulties of §2**: Ganti, B.
  *Protocol-Governed Computing: An Architecture for Deterministic Declarative Execution.*
  <https://doi.org/10.5281/zenodo.21879516>
- **The open loop and the four difficulties of §3**: Ganti, B. *Protocol-Governed Computing: An
  Architecture for Closed-Loop Governed Transformation.*
  <https://doi.org/10.5281/zenodo.21879948>
- **The principles in operational form**: Ganti, B. *Protocol-Governed Computing: Field Manual.*
  <https://doi.org/10.5281/zenodo.21898082>

Parts I–VII state precisely what these principles require.
