# Governed Interaction Boundary

## 1. Scope

This document specifies the **governed interaction boundary**. The boundary admits an interaction
from outside a governed system to governed execution, and projects a governed outcome back out. It
does both **protocol-neutrally**.

This document opens Part V. The Execution Model requires execution to sit *behind* this boundary and
to be unable to observe how an interaction arrived (EX-13). This document specifies the boundary
itself. Governed Inspection specifies the other way to reach a governed system: by asking about it,
not acting on it.

This document specifies a **semantic contract**, not a realization. Wire protocols, serializations,
adapters, artifact kinds and envelope shapes may vary freely. Nothing here requires HTTP, RPC, a
command line, a queue, or any successor to them.

This document introduces the terms **external protocol**, **protocol adapter**, **external protocol
binding**, **operation identity**, **ingress contract**, **egress contract**, **canonical
interaction form**, **governed executable target**, **governed result**, **result class**, and
**response projection**.

### 1.1 Two terms that need holding apart

| Term | Belongs to | Says |
|---|---|---|
| **outcome** | Capability Standard | one of a contract's enumerated results; what traversal routes on, *inside* execution |
| **result class** | this document | the protocol-neutral classification of a governed result, for projection *outward* |

The two operate at different levels and MUST NOT be merged. An outcome selects the next step. A
result class classifies what leaves the system. A boundary that routed on outcomes would be inside
execution. An execution that routed on result classes would be observing its own boundary.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Four separations

The boundary exists to keep apart four things that are normally blended. **This separation is the
whole of the model.** Everything below elaborates it.

```
protocol mechanics  ≠  interaction identity  ≠  governed execution  ≠  outcome projection
```

- **Protocol mechanics**: how bytes or messages are exchanged. It is external to governed interaction
  semantics. An external protocol may of course be governed by something of its own. *This* system's
  declarations do not govern it.
- **Interaction identity**: *which* governed interaction is meant. It is governed.
- **Governed execution**: *what* runs. It is governed, and orthogonal to the boundary.
- **Outcome projection**: how a governed result is represented back out. It is external.

**A realization that merges any two of these is non-conforming.** Each merger has a signature:

- merging the first two makes the governed interaction a property of the protocol that carried it;
- merging the second and third makes the boundary an execution step;
- merging the last two lets an external representation decide what a result means.

## 3. A boundary, not a stage

The boundary is a **ring around governed execution**, not a step within it.

```
                     external world
                          │   adapters + bindings
        ┌─────────────────┼──────────────────┐
        │   ingress  ▼                       │
        │      operation identity            │
        │            │                       │
        │      ingress contract              │
        │            │                       │
        │      governed execution ───────────┼──► governed result
        │            │                       │
        │      egress contract               │
        │   egress   ▲                       │
        └─────────────────┼──────────────────┘
                          │
                     external world
```

**Ingress and egress are contracts at the edge, never execution stages.** A realization MUST NOT
model the boundary as an inline step in an execution structure.

The distinction is not just about presentation. A boundary modelled as a stage becomes routable,
reachable from within, and orderable relative to other steps. Once execution can reach its own
boundary, it can observe how an interaction arrived, and EX-13 forbids that.

Authority, context and evidence are **cross-cutting**. They span the interaction instead of occupying
a position in it, and they are not stages either.

## 4. Three relationships

The boundary consists of three distinct relationships, never one flat resolution:

| | Relates | Answers |
|---|---|---|
| **Identification** | external protocol binding → operation identity | which governed operation is meant? |
| **Admission** | operation identity → applicable ingress contract | under what governed contract may it enter? |
| **Invocation** | ingress contract → governed executable target | what governed execution is invoked? |

A **governed executable target** is the governed execution an admitted interaction invokes: the thing
an ingress contract names to run. Governed declarations resolve the executable target.
**The boundary selects a target. It does not determine what that target means.** The target's own
contract does.

Merging the three produces a single lookup from a protocol selector to something executable. In that
arrangement a route determines behavior, and changing a protocol changes what runs.

## 5. Operation identity

An **operation identity** is the stable, protocol-neutral identity of a governed interaction: an
addressable identity in the governed system, independent of any protocol, executable target or
representation.

- It is an identity in the sense Identity & Addressing specifies: declared, authoritative over
  position, and never derived from an address that reaches it (ID-1, ID-9).
- **An operation identity MUST NOT be the identity of an executable target.** Merging them makes the
  interaction a name for its implementation. Changing what an operation invokes would then change
  what callers name.
- **Many external protocols MAY bind to one operation identity.** Within one applicable governance
  scope, an operation identity MUST resolve to exactly one governed invocation contract (§11).

> **The external protocol is replaceable while the governed interaction stays stable.**

## 6. Ingress

An **ingress contract** declares admission for one operation identity. It declares:

| Declares | Meaning |
|---|---|
| **operation identity** | which interaction it admits |
| **input contract** | *by reference* — a named, declared contract, never request-time schema logic |
| **context requirements** | the authority and context the interaction requires |
| **invocation binding** | the governed executable target the operation reaches |

- **An ingress contract carries no execution logic**, no capability semantics and no effects. It is a
  membrane, not a step. It names an invocation target. A reference is not a semantics, and the
  contract says nothing about what that target does.
- Construction determines its resolution. Execution enforces the constructed boundary and **MUST NOT
  interpret arbitrary semantics at interaction time** (AI-5, GC-5).
- An interaction whose operation identity has no applicable ingress contract is **refused**. It is not
  passed through, not defaulted to a general handler, and not resolved by similarity.

## 7. Egress

An **egress contract** declares how a governed outcome is projected outward. It declares:

| Declares | Meaning |
|---|---|
| **classification** | how an outcome maps to a governed result class (§9) |
| **output projection** | which parts of the result are exposed |
| **evidence exposure** | which evidence references leave the boundary |

- **A governed result exists independently of the boundary.** The egress contract *projects* it. It
  does not own it, and it MUST NOT alter it. What leaves may be less than the result, but it may not
  be other than the result (PJ-4).
- Like ingress, egress carries no execution logic. It is a declaration applied at interaction time,
  not a decision engine consulted then.
- **Evidence exposure is declared, not incidental.** Which evidence leaves the boundary is a governed
  decision. A realization that exposes whatever happens to be attached has made that decision by
  omission.

## 8. The canonical interaction form

Ingress and egress operate over a **canonical interaction form**: a representation-independent
statement of what was asked and what resulted.

- **All conforming adapters MUST normalize ingress into the applicable canonical interaction
  semantics.** They MUST project egress from the applicable canonical outcome semantics. This holds
  whatever the representation shape: a single object, a stream, a batch, or a form not yet devised.
  *Applicable* means as the governance scope determines (§11). Within one scope every adapter
  normalizes to the same semantics. An adapter that normalized to its own would be the boundary
  failing.
- **Raw passthrough is forbidden.** An inbound payload handed onward unnormalized carries
  representation into the governed system. A result emitted unprojected carries governed structure
  out of it. Either way, the boundary has failed to be one.
- A serialization is an encoding of the canonical form and is **not itself normative** (MB-3).
- The applicable profile decides whether any particular element of the canonical form is itself a
  governed artifact. The semantic contract does not force every element of an interaction into the
  artifact ontology.

## 9. Result class and response projection

A **governed result** is what a governed execution produced, as the governed system holds it, before
anything is projected outward. A result class classifies it, and a response projection represents
it. Neither the classification nor the representation is the result.

A **result class** is a member of a governed, protocol-neutral set that classifies a governed result
for projection outward.

- **A result class MUST carry no external representation semantics**: no status code, no error number
  and no exit value. A set of result classes that mirrors one protocol's status vocabulary has
  imported that protocol into the governed system.
- **The mapping from result class to external representation is response projection, and the adapter
  owns it.** It is never part of an egress contract. If it sat inside the boundary, the governed
  system would gain an opinion about a protocol it should be independent of.
- **An outcome whose meaning is domain-specific is a domain result, not a result class.** Result
  classes classify at the boundary. Domain meaning travels in the projected result.

## 10. Adapters and bindings

An **external protocol** is a means of exchanging messages with the world outside the governed
system: a wire protocol, a serialization or a calling convention, in whatever form. It is protocol
mechanics and nothing more (§2). Something of its own may well govern it, but this system's
declarations do not. Nothing about a governed interaction follows from which protocol carried it.

A **protocol adapter** translates between an external protocol and the canonical interaction form.

- **An adapter is non-authorial.** It translates mechanics and **determines no governed or domain
  semantics**. It does not decide what an interaction means, what may be admitted, what a result
  means, or what a system does.
- **Transport validation is permitted. Governed interpretation is not.** An adapter may reject a
  malformed message, an unparseable frame or a protocol violation. Those are facts about the
  protocol, and the protocol is the adapter's subject. The adapter may not decide what a well-formed
  message means.
- An adapter that makes any governed determination has become an ungoverned authority at the edge.
  Its determination is invisible to everything that governs what happens next.

An **external protocol binding** maps a protocol selector, such as a route, a method name, a verb or
a command, to an operation identity.

- The binding is protocol-specific. **Whether it is itself a governed artifact is a realization
  choice.** This document does not decide it.
- The binding MUST NOT carry meaning. It selects an operation identity and nothing more.

## 11. Governance scope

The applicability of an operation identity, an ingress contract and an egress contract MUST be
determined **within an applicable governance scope** (CA-7).

- **A realization MUST NOT silently combine contracts from incompatible governance scopes.**
- One stable operation identity MAY resolve to different contracts across *different* scopes, such as
  a version, a tenant or an authority context. Each resolution must stay within one scope, and the
  scope must be determined, not assumed.
- Within one scope, resolution is single-valued. Two applicable ingress contracts for one operation
  identity is a defect and MUST be refused. It is never resolved by precedence or specificity.

## 12. The boundary is declared and sealed

The boundary is a **declaration**, not behavior authored while running:

```
declare boundary contracts → construct and govern → seal → execution reads the constructed boundary
```

Boundary contracts are governed artifacts. They are admitted, determined against the invariants of
§15, and sealed into the representation execution consumes (SN-4).

**Execution MUST NOT read or author boundary declarations at interaction time.** Nothing determined a
boundary assembled when an interaction arrives. Whatever happened to be present at that moment
decided what it admits.

## 13. Before any boundary

The boundary presupposes a governed system to interact with. **Genesis precedes every interaction.**
The first transformation and the first snapshot are not reached through this boundary, because
nothing yet exists to admit an interaction into (Semantic Model §11, Governed Transformation §12).

It follows that **a realization MUST NOT constitute a system through its interaction boundary.**
Consider an ingress contract that admits an interaction whose effect is to create the governance
under which it would have been admitted. That is genesis disguised as an operation identity. It
escapes the one condition genesis carries: a claimed profile that the proposal did not author.

## 14. What this document does not specify

- **Any external protocol**, or how one is spoken.
- **The shape of the canonical form**: its elements, their names and their encoding.
- **The result class set.** The set must be governed and protocol-neutral. A profile selects its
  members.
- **Whether an external protocol binding is a governed artifact** (§10).
- **Authority evaluation.** This document declares what context an interaction must carry.
  Governance Closure & Authority owns how authority is determined.
- **What executable targets exist**, or which kinds may be invoked.
- **How the system is inspected.** Inspection is a separate boundary of the same standing, reached
  independently of this one (Governed Inspection §2.1). A read operation is not an operation identity
  here. A system that selects no interaction boundary still keeps its read surface.

## 15. Normative invariants

- **IB-1.** No boundary contract MUST depend on any external protocol (§2).
- **IB-2.** An operation identity MUST be uniquely resolvable and MUST NOT be the identity of an
  executable target (§5).
- **IB-3.** The boundary MUST bind to a governed executable target without requiring it to carry any
  particular vocabulary classification (§6).
- **IB-4.** Ingress and egress MUST be contracts at the edge and MUST NOT be modelled as execution
  stages (§3).
- **IB-5.** Operation-to-target resolution, input-contract existence, and closure establishment MUST
  be determined before interaction time. Execution MUST enforce the constructed boundary (§6, §12).
- **IB-6.** Ingress and egress MUST declare explicit normalization to and from the canonical form.
  Raw passthrough of an inbound payload or a governed result MUST NOT occur (§8).
- **IB-7.** An adapter MUST determine no governed or domain semantics (§10).
- **IB-8.** A result class MUST carry no external representation semantics (§9).
- **IB-9.** The mapping from result class to external representation MUST be adapter-owned and
  MUST NOT appear in an egress contract (§9).
- **IB-10.** No boundary contract or adapter MUST introduce domain state-transition, resource, or
  result semantics. Domain meaning MUST enter only through governed execution artifacts (§2, §10).
- **IB-11.** Applicability of boundary contracts MUST be determined within an applicable governance
  scope, and contracts from incompatible scopes MUST NOT be combined (§11).
- **IB-12.** Within one governance scope, an operation identity MUST resolve to exactly one governed
  invocation contract (§5, §11).
- **IB-13.** An interaction with no applicable ingress contract MUST be refused (§6).
- **IB-14.** Evidence leaving the boundary MUST be declared, not incidental (§7).
- **IB-15.** A system MUST NOT be constituted through its own interaction boundary (§13).

## 16. Conformance

The conformance subject of this document is a **boundary**: the ingress and egress contracts of a
governed system, together with the adapters and bindings that reach them.

A boundary conforms when all of the following hold:

- its contracts depend on no external protocol;
- its operation identities are distinct from executable targets;
- its normalization is explicit in both directions;
- its adapters determine nothing governed;
- its result classes carry no protocol semantics;
- its resolution is single-valued within a governance scope.

**Protocol substitution is the decisive demonstration.** For one operation identity, bind a second
external protocol and observe. The governed interaction, the admission determination, the execution
invoked and the governed result MUST be equivalent. They may differ only in external representation.
A boundary that behaves differently under a second protocol has protocol mechanics somewhere inside
it. No amount of inspecting the first protocol's path reveals where.

So a realization that supports exactly one external protocol has not demonstrated the property this
document exists to secure, however correctly that one protocol behaves.

The Conformance Test Specification owns how this is required and evaluated.
