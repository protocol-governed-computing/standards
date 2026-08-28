# Architectural Invariants

## 1. Scope

This document states the properties that must remain true of any realization of governed
computation, whatever its architecture. It is the third document of Part I: the Conceptual
Model specifies what the things are, the Semantic Model specifies what governed computation means, and
this document specifies what must hold of a system that claims to perform it.

Every invariant here is derived from the Semantic Model. None introduces a new requirement of
its own; each states, as a property of a built system, something the model requires of a
semantics. Where an invariant and the Semantic Model appear to differ, the Semantic Model
governs.

This document names no component, prescribes no mechanism, and requires no technique. It states
what must remain true, never how to achieve it.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Three tiers, and why they must not be confused

Three kinds of statement are routinely called "invariants," and treating them alike is the most
common way a standard becomes a description of one implementation.

| Tier | Kind of claim | Violated by | Owned by |
|---|---|---|---|
| **Semantic invariant** | what governed computation *is* | an account that isn't governed computation | Semantic Model (SM-1 … SM-12) |
| **Architectural invariant** | what must remain true of a realization | a built system that believes itself conformant | this document (AI-1 … AI-17) |
| **Implementation technique** | how one realization preserves an invariant | nothing — a technique is a choice | no normative document |

A semantic invariant cannot be violated by a system; it can only be misunderstood by an
account. `SM-4` — an unestablishable closure determines `refuse` — is true of governed
computation by definition. A system that admits on unestablishable closure has not violated the
definition; it has failed to be a governed system.

That failure is what an architectural invariant names. **AI-6** says the same thing in the mood
that can be checked against a running system: *absence of applicable governance and inability to
determine it MUST NOT produce the same outcome.* One is a truth about the model; the other is
an obligation on a realization, and it can be tested.

### 2.1 The test

A statement is an architectural invariant when all three hold:

1. **It can be violated by a system that looks conformant.** If no plausible realization could
   breach it, it is definitional, and belongs to the Semantic Model.
2. **Its violation is observable.** There is something one could examine — evidence, a
   representation, a refusal — that distinguishes a system that preserves it from one that does
   not. An invariant nothing could disconfirm constrains nothing.
3. **It names no mechanism.** If the statement cannot be made without naming a component, a
   file format, a language feature, or a stage, it is a technique.

### 2.2 Techniques are not invariants

Techniques are how a particular realization preserves an invariant. They are legitimate,
frequently excellent, and never normative here:

| Technique | Invariant it serves |
|---|---|
| fully qualified references everywhere | AI-2 — authority and identity are not positional |
| resolution through an index rather than a derived path | AI-2 |
| static imports; no reflective loading | AI-12 — nothing enters execution by discovery |
| environment-provisioned roots; no path synthesis | AI-12 |
| content-addressed identifiers | AI-9 — identity is derived, not assigned |
| a failed build writing nothing | AI-8 — refusal leaves no residue |

Each row's left column is one way to obtain the right column. A realization that obtains the
invariant differently conforms. **A conformance regime that tests the left column tests a
choice, and will reject conforming systems while passing systems that preserve the technique and
lose the property.**

## 3. How to read an invariant

Each invariant states what must remain true, what it is violated by, and what would show the
violation. The second and third are normative in effect: an invariant nobody can check is an
aspiration.

Each also cites what it derives from. An invariant with no derivation would be a requirement
this document invented, and Part I invents nothing.

---

## 4. Authority

### AI-1 — Behavior originates in declaration
*Derives from: SM-1, authority chain (Conceptual Model §3.3)*

No agent of a governed system originates behavior that no declaration determines. Every governed
behavior of the system traces to a declaration admitted into it; no semantic behavior may
originate outside the declarations that determine it.

This constrains *semantic* behavior, not mechanism. Evaluating a predicate, verifying an
identity, writing evidence, and traversing a representation are things a realization does in
order to preserve the invariants; they are not behaviors requiring declarations of their own.

- **Violated when** an agent decides something no declaration settled — choosing a path, supplying
  a default, inventing a step, resolving an ambiguity by preference.
- **Shown by** behavior that cannot be traced to any admitted declaration, or a change in
  behavior with no change in declarations.

### AI-2 — No ambient authority
*Derives from: SM-5, §7 non-ambient composition; Conceptual Model §3.2*

Authority derives only from declaration. Nothing acquires authority from position, containment,
ordering, load order, call site, or the identity of whatever invoked it.

- **Violated when** something is permitted because of where it sits or what reached it — a
  caller trusted for being internal, a rule applied for being loaded first, a reference resolved
  by proximity.
- **Shown by** the same proposal being determined differently from two positions, or authority
  in evidence that traces to no declaration.

### AI-3 — The activities do not trade places
*Derives from: Conceptual Model §3.3; SM-9*

Construction determines what may be executed; execution realizes what the sealed representation
determines; transformation determines what the declarations are. No activity assumes authority
to make a determination assigned to another activity.

An activity makes determinations of its own — execution determines execution-local outcomes,
and must. What it may not do is reach for authority that is not its.

- **Violated when** execution decides admissibility, construction executes to decide it, or
  either changes declarations that transformation is supposed to govern.
- **Shown by** an admissibility determination in execution evidence, or execution occurring
  during construction to establish whether something may be constructed.

---

## 5. Determination

### AI-4 — Determination precedes effect
*Derives from: SM-2*

Nothing takes effect before the determination governing it completes. There is no provisional
application awaiting a verdict, and no verdict reached by observing effects.

- **Violated when** work is done and then validated, or a determination consults the outcome of
  the thing it determines.
- **Shown by** effects timestamped or ordered before the determination that permitted them, or
  evidence in which the determination's input includes its own result.

### AI-5 — Resolution completes before what depends on it
*Derives from: SM-3*

Every reference a determination depends on is resolved before that determination is reached. An
unresolved reference is a failure of the activity that required it, never a condition discovered
later.

- **Violated when** something unresolved is carried forward in the expectation that it will
  resolve later, or resolution is attempted during execution.
- **Shown by** a resolution failure surfacing at execution, which is the observable signature of
  a construction that did not complete.

This invariant specifies an ordering, not a time. Whether resolution happens long before execution
or immediately before it is unconstrained; that it happens *first* is not.

### AI-6 — Absence is not permission
*Derives from: SM-4*

Inability to determine the applicable governance MUST NOT produce the same outcome as governance
that permits. An unknown closure is not an empty closure.

- **Violated when** an unresolvable governing element, an undeclared authority, or an
  unreachable rule set is treated as nothing to check.
- **Shown by** an admission whose evidence records no rules where rules should have been
  supplied — the signature that distinguishes governed permission from unnoticed absence.

This is the invariant whose violation is least visible from inside a system and most damaging: a
system breaching it behaves indistinguishably from a governed one until the case arrives that
governance would have refused.

### AI-7 — Refusal dominates
*Derives from: SM-5*

Where the rules applicable to a proposal yield differing consequences, the determination is the
most restrictive of them. No rule admits what another applicable rule refuses, and adding a rule
to a closure never widens what the system may do.

- **Violated when** consequences are combined permissively — an allowance read as overriding a
  prohibition, a specific permission taken to defeat a general refusal, or a first or last
  matching rule taken as the answer.
- **Shown by** evidence recording a refusal among the evaluated rules and an admission as the
  determination.

### AI-8 — Refusal leaves no residue
*Derives from: SM-7*

A refused proposal does not partly take effect. After refusal the governed state is as though
the proposal had not been made, except for the evidence that it was refused.

- **Violated when** a partial result survives a refusal — output written before the refusal,
  state advanced and not reverted, a side effect already emitted.
- **Shown by** governed state differing between a refused proposal and no proposal.

### AI-9 — Identity is derived, sealing is real
*Derives from: SM-10; Conceptual Model, sealing*

The identity of a sealed representation is derived from its sealed content, never assigned; and
after sealing, that content does not change. Two sealed representations bearing the same
identity MUST have identical content.

- **Violated when** an identity is allocated rather than computed, when sealed content is
  modified in place, or when two artifacts share an identity and differ.
- **Shown by** identical identifiers over differing content, or content that changed without its
  identifier changing.

---

## 6. Execution

### AI-10 — Execution consumes a verified sealed representation
*Derives from: SM-1, SM-2*

Execution proceeds only against a representation confirmed to be exactly what construction
authorized. On mismatch, execution does not occur.

- **Violated when** execution begins without verification, or continues after a failed one.
- **Shown by** execution evidence carrying no verification, or a representation whose identity
  does not match what construction attested.

When sealing occurs is unconstrained (AI-5). That execution consumes something sealed and
verified is not.

### AI-11 — Structure is complete before execution
*Derives from: SM-3; Conceptual Model, execution*

The structure execution traverses is complete before traversal begins. No part of it is
constructed, extended, or rerouted during the run.

- **Violated when** a step, route, or handler is synthesized from payload, environment, or
  accumulated state.
- **Shown by** evidence that the structure was constructed, extended, rerouted, or resolved
  after execution began. Divergent traversals under an identical sealed representation and
  identical inputs are one observable consequence, not the definition: a structure may be
  mutated dynamically and still happen to traverse identically in any given test.

### AI-12 — Nothing enters by discovery
*Derives from: SM-3, §7 boundedness*

What participates in a determination or an execution is what was declared and admitted. Nothing
enters by being found — not by scanning, not by convention, not by defaulting.

- **Violated when** behavior depends on something located rather than declared, or a default
  supplies what a declaration omitted.
- **Shown by** behavior changing in response to a change in surroundings while declarations and
  inputs are unchanged. This is the sharpest single test of a governed system: **move it without
  changing its declarations, its sealed representation, its governed inputs, or any explicitly
  declared environment, and it must not behave differently.** An environment that is itself a
  declared, governed input may legitimately change behavior; an environment that is merely
  present may not.

### AI-13 — Effects occur only through declared surfaces
*Derives from: SM-1; Conceptual Model, side effect*

Every effect a governed system has beyond its own governed state occurs through a declared,
governed surface. The set of ways it can affect the world is closed and known.

- **Violated when** an effect reaches the world through a path no declaration establishes.
- **Shown by** an observed external effect with no corresponding declared surface in evidence.

---

## 7. Evidence

### AI-14 — Every determination is evidenced
*Derives from: SM-8, §8.5*

Every determination produces evidence adequate to establish what was evaluated and what
resulted. A determination without adequate evidence did not govern anything, whatever it decided.

- **Violated when** evidence records outcomes without the closure and rules that produced them,
  or is produced for admissions and not refusals.
- **Shown by** evidence from which the determination cannot be re-derived.

### AI-15 — Evidence is output only
*Derives from: SM-6; Conceptual Model, trace*

Evidence is never an input to a determination. Nothing reads the record of what happened in
order to decide what happens.

- **Violated when** a determination consults a trace, or evidence is replayed into the system as
  state.
- **Shown by** a determination whose result changes when prior evidence is withheld, all else
  equal.

### AI-16 — Evidence is checkable without its producer
*Derives from: SM-12, §13*

Evidence establishes what it establishes to a party with no access to the system that produced
it, and without that party trusting it. Checking re-evaluates the recorded closure and rules
represented by the evidence, using the authority and profile information the applicable semantic
case requires — for an ordinary transition the closure inherited from the baseline, for genesis
the proposal's declared governance together with the claimed profile (Semantic Model §11).
Checking never rediscovers a closure from a current environment.

- **Violated when** establishing what happened requires querying the live system, reconstructing
  its environment, or accepting an unsupported assertion.
- **Shown by** a check that cannot be performed on the evidence alone.

---

## 8. Change

### AI-17 — Change occurs only by governed transformation
*Derives from: SM-9, SM-11*

The declarations of a governed system change only through a transformation of its baseline,
determined and evidenced like any other transition. After genesis, nothing constitutes itself:
no subsystem, domain, artifact, or deployment declares itself into a system by its own authority.

- **Violated when** declarations are altered by a path that is not a determined transformation —
  edited in place, injected at load, or introduced by a deployment; or when a later addition
  claims genesis and supplies its own admission.
- **Shown by** a baseline that differs with no transformation evidence accounting for the
  difference.

The single exception is genesis itself, which is not an exception to governance but a closure
composed from the proposal and a profile the proposal does not author (Semantic Model §11).

---

## 9. What follows from the invariants

The properties governed computation is valued for are **consequences** of the invariants above,
not additional requirements and not design goals. Each follows; none needs to be separately
pursued.

| Property | Follows because |
|---|---|
| **Determinism** | nothing originates behavior (AI-1) and nothing enters by discovery (AI-12), so nothing can vary |
| **Replayability** | behavior is a function of a sealed representation, inputs, and state (AI-10, AI-11) |
| **Portability** | behavior lives in the representation rather than the agent (AI-1, AI-3) |
| **Auditability** | no behavior is originated off the record (AI-1, AI-14) |
| **Verifiability** | structure is closed before it runs, so it can be examined instead of explored (AI-11) |
| **Substitutability** | effects reach the world only through declared surfaces (AI-13), so what is beneath them is interchangeable |
| **Governability** | no ungoverned decision is left anywhere for behavior to escape through (AI-1, AI-6, AI-17) |
| **Security by construction** | unauthorized behavior is never constructed rather than blocked at runtime (AI-1, AI-4, AI-12) — what was not built has nowhere to occur |

The direction of this table is normative. **A system that exhibits these properties without
preserving the invariants has them by circumstance, and will lose them without warning.**
Determinism obtained by implementation discipline rather than by preserving the invariants
survives only until a change introduces an undeclared source of variation.

## 10. Violation

An architectural invariant is not a quality target. Violation is not a degree of
non-conformance to be traded against other properties; it is the system ceasing to be a governed
system with respect to everything downstream of the breach.

Three consequences:

- **A breach is not local.** AI-6 breached in one closure means every determination that relied
  on that closure is unestablished, including determinations that were individually correct.
- **A breach cannot be compensated.** No amount of additional checking downstream restores a
  determination that was never made. Enforcement added after the fact detects; it does not
  govern. A downstream check may detect a breach, and remediation may restore conformance for
  future transitions; neither retroactively makes the breached transition governed.
- **A breach is not repaired by evidence of good outcomes.** That a system behaved acceptably
  while breaching an invariant is the expected case, not a mitigating one (AI-6).

## 11. Conformance

The conformance subject of this document is a **realization**: a built system claiming to
perform governed computation.

A realization conforms when each invariant AI-1 … AI-17 holds of it, and when for each one the
realization can point to the observation that would show a violation. The second half is not
decoration: an invariant a realization cannot demonstrate it preserves is an invariant it has
asserted.

Conformance to this document is **not** demonstrated by exhibiting the properties of §9. Those
follow from the invariants and can be present without them; testing for consequences in place of
premises is the error §9 exists to prevent.

How conformance is claimed, levelled, and demonstrated — and what evidence discharges each
invariant — belongs to the Conformance Model and the Conformance Test Specification. This
document specifies what must be true.
