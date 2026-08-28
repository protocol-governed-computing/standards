# Governed Interaction Boundary

## 1. Scope

This document specifies the **governed interaction boundary**: how an interaction from outside a
governed system is admitted to governed execution, and how a governed outcome is projected back out
— **protocol-neutrally**.

It opens Part V. The Execution Model requires that execution sit *behind* this boundary and be
unable to observe how an interaction arrived (EX-13); this document specifies the boundary itself.
Governed Inspection specifies the other way a governed system is reached — by being asked about
rather than acted upon.

It specifies a **semantic contract**, not a realization. Wire protocols, serializations, adapters,
artifact kinds, and envelope shapes are free to vary. Nothing here requires HTTP, RPC, a command
line, a queue, or any successor to them.

This document introduces the terms **external protocol**, **protocol adapter**, **external protocol
binding**, **operation identity**, **ingress contract**, **egress contract**, **canonical
interaction form**, **governed executable target**, **governed result**, **result class**, and
**response projection**.

### 1.1 Two terms that need holding apart

| Term | Belongs to | Says |
|---|---|---|
| **outcome** | Capability Standard | one of a contract's enumerated results; what traversal routes on, *inside* execution |
| **result class** | this document | the protocol-neutral classification of a governed result, for projection *outward* |

They operate at different levels and MUST NOT be merged. An outcome selects the next step; a result
class classifies what leaves the system. A boundary that routed on outcomes would be inside
execution; an execution that routed on result classes would be observing its own boundary.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Four separations

The boundary exists to keep four things distinct that are normally blended. **This separation is the
whole of the model**; everything below elaborates it.

```
protocol mechanics  ≠  interaction identity  ≠  governed execution  ≠  outcome projection
```

- **Protocol mechanics** — how bytes or messages are exchanged. External to governed interaction
  semantics. An external protocol may of course be governed by something of its own; it is not
  governed by *this* system's declarations.
- **Interaction identity** — *which* governed interaction is meant. Governed.
- **Governed execution** — *what* runs. Governed, and orthogonal to the boundary.
- **Outcome projection** — how a governed result is represented back out. External.

**A realization that collapses any two of these is non-conforming.** Each collapse has a signature:
merging the first two makes the governed interaction a property of the protocol that carried it;
merging the second and third makes the boundary an execution step; merging the last two lets an
external representation determine what a result means.

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

The distinction is not presentational. A boundary modelled as a stage becomes routable, reachable
from within, and orderable relative to other steps — and once execution can reach its own boundary,
it can observe how an interaction arrived, which EX-13 forbids.

Authority, context, and evidence are **cross-cutting**: they span the interaction rather than
occupying a position in it, and are not stages either.

## 4. Three relationships

The boundary is three distinct relationships, never one flat resolution:

| | Relates | Answers |
|---|---|---|
| **Identification** | external protocol binding → operation identity | which governed operation is meant? |
| **Admission** | operation identity → applicable ingress contract | under what governed contract may it enter? |
| **Invocation** | ingress contract → governed executable target | what governed execution is invoked? |

A **governed executable target** is the governed execution an admitted interaction invokes — what
an ingress contract names as the thing to run. The executable target is resolved according to
governed declarations. **The boundary selects a
target; it does not determine what that target means** — that belongs to the target's own contract.

Collapsing them produces a single lookup from a protocol selector to something executable — which is
exactly the arrangement in which a route determines behavior, and in which changing a protocol
changes what runs.

## 5. Operation identity

An **operation identity** is the stable, protocol-neutral identity of a governed interaction: an
addressable identity in the governed system, independent of any protocol, executable target, or
representation.

- It is an identity in the sense Identity & Addressing specifies: declared, authoritative over
  position, and not derived from any address that reaches it (ID-1, ID-9).
- **An operation identity MUST NOT be the identity of an executable target.** Conflating them makes
  the interaction a name for its implementation, so that changing what an operation invokes changes
  what callers name.
- **Many external protocols MAY bind to one operation identity.** Within one applicable governance
  scope, an operation identity MUST resolve to exactly one governed invocation contract (§11).

> **The external protocol is replaceable while the governed interaction remains stable.**

## 6. Ingress

An **ingress contract** declares admission for one operation identity. It declares:

| Declares | Meaning |
|---|---|
| **operation identity** | which interaction it admits |
| **input contract** | *by reference* — a named, declared contract, never request-time schema logic |
| **context requirements** | the authority and context the interaction requires |
| **invocation binding** | the governed executable target the operation reaches |

- **An ingress contract carries no execution logic**, no capability semantics, and no effects. It
  is a membrane, not a step. It names an invocation target — a reference is not a semantics — and
  says nothing about what that target does.
- Its resolution is determined during construction; execution enforces the constructed boundary and
  **MUST NOT interpret arbitrary semantics at interaction time** (AI-5, GC-5).
- An interaction whose operation identity has no applicable ingress contract is **refused**. It is
  not passed through, not defaulted to a general handler, and not resolved by similarity.

## 7. Egress

An **egress contract** declares projection of a governed outcome outward. It declares:

| Declares | Meaning |
|---|---|
| **classification** | how an outcome maps to a governed result class (§9) |
| **output projection** | which parts of the result are exposed |
| **evidence exposure** | which evidence references leave the boundary |

- **A governed result exists independently of the boundary.** The egress contract *projects* it; it
  does not own it, and it MUST NOT alter it. What leaves may be less than the result; it may not be
  other than the result (PJ-4).
- Like ingress, egress carries no execution logic. It is a declaration applied at interaction time,
  not a decision engine consulted then.
- **Evidence exposure is declared, not incidental.** What evidence leaves the boundary is a governed
  decision; a realization that exposes whatever happens to be attached has made that decision by
  omission.

## 8. The canonical interaction form

Ingress and egress operate over a **canonical interaction form**: a representation-independent
statement of what was asked and what resulted.

- **All conforming adapters MUST normalize ingress into the applicable canonical interaction
  semantics**, and MUST project egress from the applicable canonical outcome semantics, whatever the
  representation shape — a single object, a stream, a batch, or a form not yet devised. *Applicable*
  means as the governance scope determines (§11); within one scope every adapter normalizes to the
  same semantics, and an adapter normalizing to its own would be the boundary failing.
- **Raw passthrough is forbidden.** An inbound payload handed onward unnormalized, or a result
  emitted unprojected, carries representation into the governed system or governed structure out of
  it. Both are the boundary failing to be one.
- A serialization is an encoding of the canonical form and is **not itself normative** (MB-3).
- Whether any particular element of the canonical form is itself a governed artifact is a question
  for the applicable profile. The semantic contract does not force every element of an interaction
  into the artifact ontology.

## 9. Result class and response projection

A **governed result** is what a governed execution produced, as the governed system holds it and
before anything is projected outward. It is what a result class classifies and what a response
projection represents; neither the classification nor the representation is the result.

A **result class** is a member of a governed, protocol-neutral set that classifies a governed result
for projection outward.

- **A result class MUST carry no external representation semantics** — no status code, no error
  number, no exit value. A set of result classes that mirrors one protocol's status vocabulary has
  imported that protocol into the governed system.
- **The mapping from result class to external representation is response projection, and it is
  adapter-owned** — never part of an egress contract. Where it sits inside the boundary, the
  governed system acquires an opinion about a protocol it is supposed to be independent of.
- **An outcome whose meaning is domain-specific is a domain result, not a result class.** Result
  classes classify at the boundary; domain meaning travels in the projected result.

## 10. Adapters and bindings

An **external protocol** is a means of exchanging messages with the world outside the governed
system — a wire protocol, a serialization, a calling convention, in whatever form. It is protocol
mechanics and nothing more (§2): it may well be governed by something of its own, it is not
governed by this system's declarations, and nothing about a governed interaction follows from which
protocol carried it.

A **protocol adapter** translates between an external protocol and the canonical interaction form.

- **An adapter is non-authorial.** It translates mechanics and **determines no governed or domain
  semantics** — it does not decide what an interaction means, what may be admitted, what a result
  means, or what a system does.
- **Transport validation is permitted; governed interpretation is not.** An adapter may reject a
  malformed message, an unparseable frame, or a protocol violation — those are facts about the
  protocol, which is the adapter's subject. What it may not do is decide what a well-formed message
  means.
- An adapter that makes any governed determination has become an ungoverned authority at the edge,
  and the determination it makes is invisible to everything that governs what happens next.

An **external protocol binding** maps a protocol selector — a route, a method name, a verb, a
command — to an operation identity.

- The binding is protocol-specific. **Whether it is itself a governed artifact is a realization
  choice**, and this document does not decide it.
- What the binding MUST NOT do is carry meaning: it selects an operation identity and nothing more.

## 11. Governance scope

The applicability of an operation identity, an ingress contract, and an egress contract MUST be
determined **within an applicable governance scope** (CA-7).

- **A realization MUST NOT silently combine contracts from incompatible governance scopes.**
- One stable operation identity MAY resolve to different contracts across *different* scopes — a
  version, a tenant, an authority context — provided each resolution is within one scope and the
  scope is determined rather than assumed.
- Within one scope, resolution is single-valued. Two applicable ingress contracts for one operation
  identity is a defect and MUST be refused, never resolved by precedence or specificity.

## 12. The boundary is declared and sealed

The boundary is a **declaration**, not behavior authored while running:

```
declare boundary contracts → construct and govern → seal → execution reads the constructed boundary
```

Boundary contracts are governed artifacts. They are admitted, determined against the invariants of
§15, and sealed into the representation execution consumes (SN-4).

**Execution MUST NOT read or author boundary declarations at interaction time.** A boundary
assembled when an interaction arrives is a boundary nothing determined, and what it admits was
decided by whatever was present at that moment.

## 13. Before any boundary

The boundary presupposes a governed system to interact with. **Genesis precedes every interaction**:
the first transformation and the first snapshot are not reached through this boundary, because there
is nothing yet to admit an interaction into (Semantic Model §11, 4d §12).

It follows that **a realization MUST NOT constitute a system through its interaction boundary.** An
ingress contract that admits an interaction whose effect is to create the governance under which it
would have been admitted is genesis wearing an operation identity, and it escapes the one condition
genesis carries — a claimed profile the proposal did not author.

## 14. What this document does not specify

- **Any external protocol**, or how one is spoken.
- **The canonical form's shape** — its elements, their names, and their encoding.
- **The result class set.** That it is governed and protocol-neutral is required; its members are a
  profile's selection.
- **Whether an external protocol binding is a governed artifact** (§10).
- **Authority evaluation.** What context an interaction must carry is declared here; how authority is
  determined belongs to Governance Closure & Authority.
- **What executable targets exist**, or which kinds may be invoked.
- **How the system is inspected.** Inspection is a separate boundary of the same standing, reached
  independently of this one (5b §2.1). A read operation is not an operation identity here, and
  selecting no interaction boundary does not remove the read surface.

## 15. Normative invariants

- **IB-1.** No boundary contract MUST depend on any external protocol (§2).
- **IB-2.** An operation identity MUST be uniquely resolvable and MUST NOT be the identity of an
  executable target (§5).
- **IB-3.** The boundary MUST bind to a governed executable target without requiring it to carry any
  particular vocabulary classification (§6).
- **IB-4.** Ingress and egress MUST be contracts at the edge and MUST NOT be modelled as execution
  stages (§3).
- **IB-5.** Operation-to-target resolution, input-contract existence, and closure establishment MUST
  be determined before interaction time; execution MUST enforce the constructed boundary (§6, §12).
- **IB-6.** Ingress and egress MUST declare explicit normalization to and from the canonical form;
  raw passthrough of an inbound payload or a governed result MUST NOT occur (§8).
- **IB-7.** An adapter MUST determine no governed or domain semantics (§10).
- **IB-8.** A result class MUST carry no external representation semantics (§9).
- **IB-9.** The mapping from result class to external representation MUST be adapter-owned and MUST
  NOT appear in an egress contract (§9).
- **IB-10.** No boundary contract or adapter MUST introduce domain state-transition, resource, or
  result semantics; domain meaning MUST enter only through governed execution artifacts (§2, §10).
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

A boundary conforms when its contracts depend on no external protocol, its operation identities are
distinct from executable targets, its normalization is explicit in both directions, its adapters
determine nothing governed, its result classes carry no protocol semantics, and its resolution is
single-valued within a governance scope.

**The decisive demonstration is protocol substitution.** For one operation identity, bind a second
external protocol to it and observe: the governed interaction, the admission determination, the
execution invoked, and the governed result MUST be equivalent, differing only in external
representation. A boundary that behaves differently under a second protocol has protocol mechanics
somewhere inside it — and no amount of inspecting the first protocol's path reveals where.

This is why a realization supporting exactly one external protocol has not demonstrated the property
this document exists to secure, however correctly that one protocol behaves.

How this is required and evaluated belongs to the Conformance Test Specification.
