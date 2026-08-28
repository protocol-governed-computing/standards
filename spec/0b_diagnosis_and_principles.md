# Diagnosis and Principles

*Non-normative. Problem and Motivation states that the problem is real, expensive, and structural.
This document states why it persists, and what a solution would have to be true of. It creates no
obligation; the normative parts do that.*

## 1. The diagnosis is about authority

The failures of the previous document are not failures of skill, discipline, or tooling. They are
consequences of **where behavioral authority sits** — of which thing in a system is entitled to
decide what the system does.

Conventional software places that authority in two places where it cannot be examined: **in the
engine at run time**, and **nowhere at all when the system changes**. Each produces four
difficulties, and neither set is an accident of any particular language or framework.

## 2. Authority held by the runtime

A conventional runtime does not merely carry out decisions already made. It makes them — evaluating
conditions, choosing branches, resolving dispatch, sometimes constructing the very structure it is
about to execute.

| Difficulty | Because |
|---|---|
| **runtime decisioning** | behavior is a property of the run rather than of the artifact |
| **hidden behavior** | it cannot be fully known before execution, so learning what a system does means running it and watching the paths that run happened to take |
| **poor replay** | re-running does not reliably reproduce, because decisions depended on ambient conditions that are not part of the artifact |
| **platform dependence** | behavior is entangled with the engine that produced it, and cannot travel, because it never wholly lived in the thing that travels |

## 3. Authority lost at the specification

Conventional development is **open-loop**: requirements go in, a running system comes out, and the
two are never systematically compared in a governed way.

| Difficulty | Because |
|---|---|
| **requirements leakage** | a requirements document has no structural guard against design decisions accumulating inside it |
| **rationale decay** | it records what was decided but rarely why, so the system inherits decisions and loses their justification |
| **governance externalization** | governance becomes a wrapper around engineering rather than a property of it |
| **evolution amnesia** | when the system must change, the thing being changed is opaque, so evolution becomes archaeology |

**The second set returns in full the moment a system must change.** That is what makes the process
of change itself a subject to be governed, rather than a practice surrounding one.

## 4. Why the prevailing model produces both

The application-centric model — in which the application is the fundamental unit of design — has
three structural properties, and they are invisible because the model is assumed rather than chosen:

- **Behavior is embedded.** What a system does is inseparable from how it does it. To understand the
  intent, read the code.
- **Governance is implicit.** The rules that constrain the system are real and load-bearing, and
  live in comments, conventions, and memory — invisible to any structural check.
- **Structure is emergent.** The true architecture is not declared but discovered afterwards, by
  reading code and tracing execution.

The model was not a mistake. It was efficient when systems were small and change moved at human
speed. **It made software possible. It did not make software governable** — and it is now being used
to build at a scale and speed it was never adequate for.

## 5. What follows

If the difficulties come from where authority sits, then relocating authority is the only response
that reaches them. Everything below is a consequence of moving behavioral authority **out of
implementation and out of the engine, into explicit, versioned, machine-consumable declarations
validated before anything runs** — and then governing the process by which those declarations
change.

## 6. Principles

These are the architectural stance from which PGC was developed and against which its reference
realization was built.

- **Protocol is the source of truth.** Behavior is carried by declared artifacts, not by code. Code
  may be regenerated, replaced, or machine-authored without governance being affected.
- **Behavior is complete before execution begins.** If behavior must not emerge at run time, it must
  already exist, whole, when run time starts.
- **Resolution happens before execution.** A path not constructed during construction cannot be
  traversed during execution.
- **The engine is deliberately incapable.** An execution engine that interprets no domain meaning is
  not a limitation to be worked around; every judgment it declines to make was made earlier, where
  it could be reviewed.
- **Zero inference.** No implicit defaults, no heuristics, no discovery by scanning. Undeclared means
  absent.
- **Fail hard.** A missing artifact, a missing binding, or a violated invariant produces refusal.
  Graceful degradation hides architectural violation.
- **Determinism and structural replay.** The same governed input yields the same result. Replay is a
  property of the artifact, not a reconstruction of an environment.
- **No ambient authority.** Authority comes from declaration, never from execution context — so that
  whole classes of confused-deputy failure are structurally absent rather than defended against.
- **Sealed execution input.** Execution consumes sealed state exclusively. Behavior changes by
  changing declarations and reconstructing, never by acting on the running system.
- **Compression is a feature.** A small vocabulary with strong invariants is preferable to a large
  one with heuristic flexibility. Growing the ontology without governing necessity is debt.
- **The process of change is itself governed.** Evolution is transformation of a governed state into
  the next, declared and evidenced — not authoring beside the system.

## 7. Principles are not requirements

**A principle discharges no obligation.** It does not substitute for a normative statement, does not
license behavior the normative documents do not, and cannot be cited in place of one.

Where a principle and a normative document appear to differ, **the document governs**; the principle
was an argument, never an authority. This is the same rule the family applies to its own sources:
the papers and the reference realization may argue from what was built, and this family may not.

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

What these principles require, precisely, is the subject of Parts I–VII.
