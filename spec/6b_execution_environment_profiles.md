# Execution Environment Profiles

## 1. Scope

This document specifies how PGC semantics are preserved across **execution environments**. More
important, it specifies what an environment may and may not change about them.

An environment is where execution happens: a single machine, a container, an orchestrated cluster, a
distributed system, an embedded device, or a substrate not yet built. An environment is broader than
a deployment. It includes the substrate, its orchestration, its placement and its distribution.

**A deployment decision changes where execution happens. It MUST NOT change what execution means**
(Execution Model §14, Snapshot §9). The same holds for every other environment decision. Everything
below elaborates that one rule.

An execution environment profile is a **profile** in the sense the Normative Platform Profile
specifies, and every rule there applies here unchanged. It narrows and never widens. It redefines
nothing and exempts nothing. The system that claims it does not author it. This document specifies
what is distinctive about profiles whose subject is an environment.

This document introduces the terms **execution constraint**, **declared environment**, and **ambient
environment**.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. The invariance requirement

**Governed consequences MUST NOT vary with the environment.**

The same snapshot, the same inputs and the same initial state produce the same governed consequences
wherever they are executed, **under equivalent declared inputs** (SN-11). A system may declare an
environmental fact as a governed input. That input is then part of *the same inputs* (§6). Only what
the system did not declare must stay fixed.

An environment may determine whether execution happens, when, how fast and where. It determines
nothing about what execution means.

This is not an aspiration about portability. It is what makes an environment profile *a profile*,
not a variant standard. If governed consequences could differ by environment, a snapshot would mean
different things in different places. No claim about a governed system would travel with it.

## 3. What an environment may constrain

An environment introduces **execution constraints**: facts about the substrate that bound whether and
how execution proceeds, without bearing on what it determines.

| Constraint | Concerns |
|---|---|
| **availability** | whether a resource, node, or dependency can be reached |
| **placement** | where a step is performed, and on what |
| **resource** | how much compute, memory, or storage is available, and to what |
| **timing** | how long things take, and what deadlines apply |
| **isolation** | what is separated from what, and by what mechanism |
| **failure mode** | how the substrate fails, and what a failure looks like |

Every one of these is a **mechanism** concern (RT-5). Varying it cannot vary a declared governed
consequence. That is exactly the test for whether something belongs in this document.

These constraints may of course decide whether execution proceeds *at all*. An unreachable
dependency stops things. That is availability, not semantics: **none of them changes the governed
execution model**.

An environment profile MAY require any of them. A profile may demand redundancy, bound latency,
mandate isolation or forbid co-location. These are real obligations, checkable and enforceable, and
none of them touches what a determination determines.

## 4. What an environment may not introduce

An environment profile MUST NOT introduce:

- **a governance kind or semantic category.** The ontology is closed within a revision (GO-1, and
  Governance Semantic Ontology §1.1). An environment is no reason to extend it. Adding a category
  this way would be an ontology revision reached by a route that was not deliberate.
- **an authority.** An environment does not govern. Being the substrate on which deciding happens
  gives nothing the right to decide (CA-2).
- **a determination point.** Where a determination is made is a mechanism decision. *That* a
  determination is made, and by what closure, is not the environment's to arrange.
- **environment-derived behavior.** No governed consequence may follow from a property of the
  substrate that no declaration established (AI-12, EX-3).
- **an exemption.** An environment that "cannot" satisfy an invariant has not earned relief from it.
  It has shown that it is not an environment where that system may run.

The last item is where pressure actually arrives. An environment profile is the natural place to ask
for an exception. The substrate is awkward, the guarantee is expensive, or the alternative is not
shipping. **A profile cannot grant the exception** (NP-4). The honest outcome is that some systems do
not run in some environments.

## 5. The standing test

Every environment that claims to be special gets the same question:

> **Does this environment require new *governance* semantics — or only new *constraints*?**

The default answer is constraints. The burden falls on the claim that the answer is otherwise. A new
governance semantics is established only where the Semantic Model requires one: where some change of
governed state cannot be expressed as a governed transition under an existing governed closure.

**A named platform, orchestrator, runtime substrate or cloud is the subject of a profile, never a new
governing concept.** An environment may have its own vocabulary, with its own units of scheduling,
placement or isolation. That is a fact about the environment, and it belongs in the profile that
describes it. Wide use does not make it PGC vocabulary.

## 6. Declared environment and ambient environment

This distinction makes §2 usable:

| | Is | May influence governed consequences |
|---|---|---|
| **declared environment** | an environment property **declared by the system** as a governed input | yes — it is a declaration like any other |
| **ambient environment** | an environment property that is merely present | **never** |

- A system MAY declare an environmental fact as a governed input, such as a region, a tier or an
  available substrate property. Behavior may then depend on it, because the dependence is declared
  and governed.
- **A system MUST NOT depend on an environmental fact it did not declare.** The property is present
  either way. The difference is whether anything governs the dependence.

AI-12's relocation test detects this. Move a system without changing its declarations, its snapshot,
its governed inputs or any explicitly declared environment. Nothing may behave differently
(Architectural Invariants, AI-12).

**An environment profile MUST NOT convert an ambient property into a governed one by requiring it.**
If a profile requires an environment to provide something, that makes it a precondition for running.
It does not make it a governed input to determinations. If behavior is to depend on it, the *system*
must declare it.

In general: **an environment profile cannot convert presence into authority** (CA-2). Something being
there, and a profile insisting that it be there, establishes nothing about what may depend on it.

## 7. Equivalence across environments

The obligation an environment profile carries is **equivalence**:

- Two conforming environments executing the same snapshot with the same inputs and initial state MUST
  produce the same governed consequences (SN-11, RT-12).
- They MAY differ in everything else: timing, resource use, placement, the order of steps the
  declarations state are independent, and every observational element of evidence (EV-5, EV-7).

**Comparison, not inspection, establishes equivalence.** Correct consequences in one environment
establish nothing about a second. The second is where an environmental dependency hides, because the
dependency is invisible in the environment that satisfies it (SN-4, Snapshot §15).

## 8. Distribution

People most often argue that distribution requires new governance semantics. It does not, and the
reason is worth stating, not just asserting.

### 8.1 Its characteristic failures already have determinations

| Distributed condition | Already determined by |
|---|---|
| a node is unreachable | inability to establish state or closure → **refuse** (SM-4, AI-6) |
| a partition divides the system | the same: what cannot be determined is refused |
| replicas disagree | copies of one identity that differ are a defect and MUST be refused (GC-12, SN-3) |
| a determination is made elsewhere | a determination is a determination; what matters is the closure it was made under, not the machine (RT-5) |
| a transition applies partly | an admitted transition MUST NOT come to rest partly applied; a realization able to apply one partly MUST determine what state results (SM-7a) |

**Distribution does not introduce a new kind of governed change. It introduces new ways to be unable
to determine one.** Inability to determine already has an answer: refuse.

### 8.2 Ordering

Where the order of two effects matters, **the declarations say so**. Where they do not, order is a
mechanism decision (EX-4, Execution Model §13).

Distribution does not change this. It does make an existing gap in the declarations visible. Suppose
a system's declarations left an ordering unstated. It will show different orders in a distributed
environment and identical ones on a single node. **The distributed environment did not introduce the
ambiguity. It revealed it.** The remedy is to declare the ordering, not to constrain the environment
into hiding it again.

### 8.3 What distribution legitimately requires

A distributed environment profile MAY require what any environment profile may (§3). Examples are
replication, reachability, bounded staleness, agreement about which snapshot is current, and
isolation between tenants. Each is **declared as an environmental constraint, and none is used as an
undeclared source of governed behavior** (§6). All are execution constraints. None is a governance
semantics. None may relieve a distributed system of a single invariant that a single-node system
carries.

## 9. What an environment profile declares

An execution environment profile declares:

- **the environment it profiles**, bounded well enough that a system can determine whether it is in
  one;
- **the execution constraints it requires**, and the obligations they place on a system that claims
  it (§3);
- **what it excludes**: systems whose requirements the environment cannot meet;
- **the conformance claims it supports** (NP-8).

It does not declare governance, kinds, categories, authorities or determinations. A profile that
declares any of those has left this document's subject (§4).

## 10. What this document does not specify

- **Any particular environment.** This document names none normatively, and none is privileged.
- **Deployment, orchestration, scheduling or operations.**
- **Performance requirements.** A profile may impose them. This family does not, and nothing this
  family requires may be traded away to obtain them (Runtime §12).
- **Availability or reliability targets.** These are a profile's subject.
- **How a system determines which environment it is in**, where a profile requires it to.

## 11. Normative invariants

- **EE-1.** Governed consequences MUST NOT vary with the environment (§2).
- **EE-2.** An environment profile MUST NOT introduce a governance kind, semantic category,
  authority, or determination point (§4).
- **EE-3.** An environment profile MUST NOT exempt a system from any invariant of this family (§4).
- **EE-4.** A governed consequence MUST NOT follow from an environmental property no declaration
  established (§6).
- **EE-5.** An environment profile MUST NOT convert an ambient environmental property into a governed
  input. Only the system may declare one (§6).
- **EE-6.** Two conforming environments executing the same snapshot, inputs, and initial state MUST
  produce the same governed consequences (§7).
- **EE-7.** Inability to establish governed state or an applicable closure MUST produce refusal,
  whatever the environmental cause (§8.1).
- **EE-8.** A distributed environment MUST NOT relieve a system of any invariant a single-node system
  carries (§8.3).

## 12. Conformance

The conformance subject of this document is an **execution environment profile**: the environment it
bounds, the constraints it requires, and the claims it supports.

An environment profile conforms when all of the following hold:

- it constrains only mechanism;
- it introduces no governance;
- it exempts nothing;
- it leaves governed consequences invariant.

**Substitution establishes a system's conformance under an environment profile.** Execute the same
snapshot with the same inputs in a second conforming environment, and compare governed consequences.
Identical consequences establish that the environment contributed nothing. Different consequences
establish that it did, and place the finding in the system, not in either environment.

So **a realization that has only ever run in one environment has not demonstrated environmental
invariance**, however carefully that environment was configured. In the same way, a boundary bound to
one protocol has not demonstrated protocol neutrality (Governed Interaction Boundary §16).

The Conformance Test Specification owns how this is required and evaluated.
