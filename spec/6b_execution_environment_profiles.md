# Execution Environment Profiles

## 1. Scope

This document specifies how PGC semantics are preserved across **execution environments** — and,
more consequentially, what an environment may and may not change about them.

An environment is where execution happens: a single machine, a container, an orchestrated cluster, a
distributed system, an embedded device, a substrate not yet built. The environment is broader than a
deployment: it includes the substrate, its orchestration, its placement, and its distribution.

**A deployment decision changes where execution happens; it MUST NOT change what execution means**
(3a §14, 3b §9) — and the same holds of every other environment decision. Everything below
elaborates that one sentence.

An execution environment profile is a **profile** in the sense the Normative Platform Profile
specifies, and every rule there applies here unchanged: it narrows and never widens, redefines
nothing, exempts nothing, and is not authored by the system that claims it. This document specifies
what is distinctive about profiles whose subject is an environment.

This document introduces the terms **execution constraint**, **declared environment**, and **ambient
environment**.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. The invariance requirement

**Governed consequences MUST NOT vary with the environment.**

The same snapshot, the same inputs, and the same initial state produce the same governed
consequences wherever they are executed, **under equivalent declared inputs** (SN-11). Where a
system declares an environmental fact as a governed input, that input is part of *the same inputs*
(§6); what may not vary is anything the system did not declare.

An environment may determine whether execution happens, when, how fast, and where — and nothing
about what it means.

This is not an aspiration about portability. It is what makes an environment profile *a profile*
rather than a variant standard: if governed consequences could differ by environment, a snapshot
would mean different things in different places, and no claim about a governed system would be
portable with it.

## 3. What an environment may constrain

An environment introduces **execution constraints**: facts about the substrate that bound whether
and how execution proceeds, without bearing on what it determines.

| Constraint | Concerns |
|---|---|
| **availability** | whether a resource, node, or dependency can be reached |
| **placement** | where a step is performed, and on what |
| **resource** | how much compute, memory, or storage is available, and to what |
| **timing** | how long things take, and what deadlines apply |
| **isolation** | what is separated from what, and by what mechanism |
| **failure mode** | how the substrate fails, and what a failure looks like |

Every one of these is a **mechanism** concern (RT-5): varying it cannot vary a declared governed
consequence. That is precisely the test for whether something belongs in this document.

They may of course determine whether execution proceeds *at all* — an unreachable dependency stops
things. That is availability, not semantics: **none of them changes the governed execution model**.

An environment profile MAY require any of them — a profile may demand redundancy, bound latency,
mandate isolation, or forbid co-location. These are real obligations, checkable and enforceable, and
none of them touches what a determination determines.

## 4. What an environment may not introduce

An environment profile MUST NOT introduce:

- **a governance kind or semantic category.** The ontology is closed within a revision (GO-1, and
  2b §1.1); an environment is not a reason to extend it, and adding one is an ontology revision
  reached by a route that was not deliberate.
- **an authority.** An environment does not govern. Nothing acquires the right to decide by being
  the substrate on which deciding happens (CA-2).
- **a determination point.** Where a determination is made is a mechanism decision; *that* a
  determination is made, and by what closure, is not the environment's to arrange.
- **environment-derived behavior.** No governed consequence may follow from a property of the
  substrate that no declaration established (AI-12, EX-3).
- **an exemption.** An environment that "cannot" satisfy an invariant has not earned relief from it;
  it has established that it is not an environment in which that system may run.

The last is where pressure actually arrives. An environment profile is the natural place to ask for
an exception — the substrate is awkward, the guarantee is expensive, the alternative is not shipping.
**A profile cannot grant it** (NP-4), and the honest outcome is that some systems do not run in some
environments.

## 5. The standing test

Every environment that arrives claiming to be special is answered the same way:

> **Does this environment require new *governance* semantics — or only new *constraints*?**

The default answer is constraints, and the burden is on the claim that it is not. A new governance
semantics is established only where the Semantic Model requires one: where some change of governed
state cannot be expressed as a governed transition under an existing governed closure.

**A named platform, orchestrator, runtime substrate, or cloud is the subject of a profile, never a
new governing concept.** That an environment has its own vocabulary — its own units of scheduling,
placement, or isolation — is a fact about the environment, and belongs in the profile that describes
it. It does not become PGC vocabulary by being widely used.

## 6. Declared environment and ambient environment

The distinction that makes §2 usable:

| | Is | May influence governed consequences |
|---|---|---|
| **declared environment** | an environment property **declared by the system** as a governed input | yes — it is a declaration like any other |
| **ambient environment** | an environment property that is merely present | **never** |

- A system MAY declare an environmental fact as a governed input — a region, a tier, an available
  substrate property — and behavior may then depend on it, because the dependence is declared and
  governed.
- **A system MUST NOT depend on an environmental fact it did not declare.** The property is present
  either way; what differs is whether anything governs the dependence.

This is what AI-12's relocation test detects: move a system without changing its declarations, its
snapshot, its governed inputs, or any explicitly declared environment, and nothing may behave
differently (1c AI-12).

**An environment profile MUST NOT convert an ambient property into a governed one by requiring it.**
Requiring that an environment provide something makes it a precondition for running; it does not
make it a governed input to determinations. If behavior is to depend on it, the *system* declares it.

Stated generally: **an environment profile cannot convert presence into authority** (CA-2). That
something is there, and that a profile insists it be there, establishes nothing about what may
depend on it.

## 7. Equivalence across environments

The obligation an environment profile carries is **equivalence**:

- Two conforming environments executing the same snapshot with the same inputs and initial state
  MUST produce the same governed consequences (SN-11, RT-12).
- They MAY differ in everything else: timing, resource use, placement, the order of steps the
  declarations state to be independent, and every observational element of evidence (EV-5, EV-7).

**Equivalence is established by comparison, not by inspection.** That a system produces correct
consequences in one environment establishes nothing about the second — which is where an
environmental dependency hides, because it is invisible in the environment that satisfies it (SN-4,
3b §15).

## 8. Distribution

Distribution is the environment most often argued to require new governance semantics. It does not,
and the reason is worth stating rather than asserting.

### 8.1 Its characteristic failures already have determinations

| Distributed condition | Already determined by |
|---|---|
| a node is unreachable | inability to establish state or closure → **refuse** (SM-4, AI-6) |
| a partition divides the system | the same: what cannot be determined is refused |
| replicas disagree | copies of one identity that differ are a defect and MUST be refused (GC-12, SN-3) |
| a determination is made elsewhere | a determination is a determination; what matters is the closure it was made under, not the machine (RT-5) |
| a transition applies partly | an admitted transition MUST NOT come to rest partly applied; a realization able to apply one partly MUST determine what state results (SM-7a) |

**Distribution does not introduce a new kind of governed change. It introduces new ways to be unable
to determine one** — and inability to determine already has an answer, which is to refuse.

### 8.2 Ordering

Where the order of two effects matters, **the declarations say so**; where they do not, order is a
mechanism decision (EX-4, 3a §13).

Distribution does not change this. What it does is make an existing under-specification visible: a
system whose declarations left an ordering unstated will exhibit different orders in a distributed
environment and identical ones on a single node. **The distributed environment did not introduce the
ambiguity; it revealed it**, and the remedy is to declare the ordering, not to constrain the
environment into hiding it again.

### 8.3 What distribution legitimately requires

A distributed environment profile MAY require what any environment profile may (§3): replication,
reachability, bounded staleness, agreement about which snapshot is current, isolation between
tenants — each **declared as an environmental constraint, and none used as an undeclared source of
governed behavior** (§6). All are execution constraints. None is a governance semantics, and none may relieve a
distributed system of a single invariant a single-node system carries.

## 9. What an environment profile declares

An execution environment profile declares:

- **the environment it profiles** — bounded well enough that a system can determine whether it is in
  one;
- **the execution constraints it requires**, and the obligations they place on a system claiming it
  (§3);
- **what it excludes** — systems whose requirements the environment cannot meet;
- **the conformance claims it supports** (NP-8).

It does not declare governance, kinds, categories, authorities, or determinations — a profile
declaring any of those has left this document's subject (§4).

## 10. What this document does not specify

- **Any particular environment.** None is named normatively, and none is privileged.
- **Deployment, orchestration, scheduling, or operations.**
- **Performance requirements.** A profile may impose them; this family does not, and nothing this
  family requires may be traded away to obtain them (3c §12).
- **Availability or reliability targets.** A profile's subject.
- **How a system determines which environment it is in**, where a profile requires it to.

## 11. Normative invariants

- **EE-1.** Governed consequences MUST NOT vary with the environment (§2).
- **EE-2.** An environment profile MUST NOT introduce a governance kind, semantic category,
  authority, or determination point (§4).
- **EE-3.** An environment profile MUST NOT exempt a system from any invariant of this family (§4).
- **EE-4.** A governed consequence MUST NOT follow from an environmental property no declaration
  established (§6).
- **EE-5.** An environment profile MUST NOT convert an ambient environmental property into a
  governed input; only the system may declare one (§6).
- **EE-6.** Two conforming environments executing the same snapshot, inputs, and initial state MUST
  produce the same governed consequences (§7).
- **EE-7.** Inability to establish governed state or an applicable closure MUST produce refusal,
  whatever the environmental cause (§8.1).
- **EE-8.** A distributed environment MUST NOT relieve a system of any invariant a single-node
  system carries (§8.3).

## 12. Conformance

The conformance subject of this document is an **execution environment profile**: the environment it
bounds, the constraints it requires, and the claims it supports.

An environment profile conforms when it constrains only mechanism, introduces no governance, exempts
nothing, and leaves governed consequences invariant.

**A system's conformance under an environment profile is established by substitution.** Execute the
same snapshot with the same inputs in a second conforming environment and compare governed
consequences. Identical consequences establish that the environment contributed nothing; differing
consequences establish that it did, and locate the finding in the system rather than in either
environment.

This is why **a realization that has only ever run in one environment has not demonstrated
environmental invariance**, however carefully that environment was configured — the same way a
boundary bound to one protocol has not demonstrated protocol neutrality (5a §16).

How this is required and evaluated belongs to the Conformance Test Specification.
