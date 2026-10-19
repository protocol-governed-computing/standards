# Architectural Invariants

## 1. Scope

This document states the properties that must stay true of any realization of governed computation,
whatever its architecture. It is the third document of Part I:

- the Conceptual Model specifies what the things are;
- the Semantic Model specifies what governed computation means;
- this document specifies what must hold of a system that claims to perform it.

Every invariant here derives from the Semantic Model. None adds a requirement of its own. Each one
restates, as a property of a built system, something the model requires of a semantics. Where an
invariant and the Semantic Model appear to differ, the Semantic Model governs.

This document names no component, prescribes no mechanism and requires no technique. It states what
must stay true, never how to achieve it.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Three tiers, and why they must not be confused

People often call three kinds of statement "invariants". A standard that treats them alike usually
ends up describing one implementation.

| Tier | Kind of claim | Violated by | Owned by |
|---|---|---|---|
| **Semantic invariant** | what governed computation *is* | an account that isn't governed computation | Semantic Model (SM-1 … SM-12) |
| **Architectural invariant** | what must remain true of a realization | a built system that believes itself conformant | this document (AI-1 … AI-17) |
| **Implementation technique** | how one realization preserves an invariant | nothing — a technique is a choice | no normative document |

A system cannot violate a semantic invariant. Only an account can misunderstand one. Take `SM-4`: an
unestablishable closure determines `refuse`. That is true of governed computation by definition.

A system that admits on an unestablishable closure has not violated the definition. It has failed to
be a governed system.

An architectural invariant names that failure. **AI-6** says the same thing in a form a party can
check against a running system: *absence of applicable governance and inability to determine it MUST
NOT produce the same outcome.* SM-4 is a truth about the model. AI-6 is an obligation on a
realization, and a party can test it.

### 2.1 The test

A statement is an architectural invariant when all three conditions hold:

1. **A system that looks conformant can violate it.** If no plausible realization could breach it,
   the statement is definitional and belongs to the Semantic Model.
2. **Its violation is observable.** Something exists that one could examine, such as evidence, a
   representation or a refusal. That thing distinguishes a system that preserves the invariant from
   one that does not. An invariant nothing could disconfirm constrains nothing.
3. **It names no mechanism.** If stating it requires naming a component, a file format, a language
   feature or a stage, it is a technique.

### 2.2 Techniques are not invariants

A technique is how a particular realization preserves an invariant. Techniques are legitimate, often
excellent, and never normative here:

| Technique | Invariant it serves |
|---|---|
| fully qualified references everywhere | AI-2 — authority and identity are not positional |
| resolution through an index rather than a derived path | AI-2 |
| static imports; no reflective loading | AI-12 — nothing enters execution by discovery |
| environment-provisioned roots; no path synthesis | AI-12 |
| content-addressed identifiers | AI-9 — identity is derived, not assigned |
| a failed build writing nothing | AI-8 — refusal leaves no residue |

Each left-hand entry is one way to obtain the invariant on its right. A realization that obtains the
invariant another way conforms. **A conformance regime that tests the left column tests a choice.
It will reject conforming systems. It will also pass systems that keep the technique and lose the
property.**

## 3. How to read an invariant

Each invariant states three things:

- what must stay true;
- what violates it;
- what would show the violation.

The second and third are normative in effect. An invariant nobody can check is only an aspiration.

Each invariant also cites what it derives from. An invariant with no derivation would be a
requirement this document invented, and Part I invents nothing.

---

## 4. Authority

### AI-1 — Behavior originates in declaration
*Derives from: SM-1, authority chain (Conceptual Model §3.3)*

Every governed behavior of the system traces to a declaration admitted into it. Agents of a governed
system originate only behavior that a declaration determines. Semantic behavior originates only in
the declarations that determine it.

This invariant constrains *semantic* behavior, not mechanism. A realization evaluates predicates,
verifies identities, writes evidence and traverses representations. It does these things to preserve
the invariants. They are not behaviors that need declarations of their own.

- **Violated when** an agent decides something no declaration settled. Examples: it chooses a path,
  supplies a default, invents a step, or resolves an ambiguity by preference.
- **Shown by** behavior that traces to no admitted declaration, or by a change in behavior with no
  change in declarations.

### AI-2 — No ambient authority
*Derives from: SM-5, §7 non-ambient composition; Conceptual Model §3.2*

Authority derives only from declaration. Nothing gains authority from position, containment,
ordering, load order, call site, or the identity of whatever invoked it.

- **Violated when** a system permits something because of where it sits or what reached it.
  Examples: it trusts a caller for being internal, applies a rule for loading first, or resolves a
  reference by proximity.
- **Shown by** the same proposal reaching different determinations from two positions, or by
  authority in evidence that traces to no declaration.

### AI-3 — The activities do not trade places
*Derives from: Conceptual Model §3.3; SM-9*

Each activity holds its own authority:

- construction determines what may be executed;
- execution realizes what the sealed representation determines;
- transformation determines what the declarations are.

No activity assumes authority to make a determination assigned to another activity.

An activity does make determinations of its own. Execution determines execution-local outcomes, and
it must. What an activity may not do is reach for authority that belongs to another.

- **Violated when** execution decides admissibility, or construction executes something to decide
  it. Also violated when either activity changes declarations that transformation should govern.
- **Shown by** an admissibility determination in execution evidence. Also shown when execution runs
  during construction to establish whether something may be constructed.

---

## 5. Determination

### AI-4 — Determination precedes effect
*Derives from: SM-2*

Every effect waits until the determination governing it completes. No provisional application awaits
a verdict, and no verdict comes from observing effects.

- **Violated when** a system does work first and validates it afterwards, or when a determination
  consults the outcome of the thing it determines.
- **Shown by** effects timestamped or ordered before the determination that permitted them. Also
  shown by evidence in which the determination's input includes its own result.

### AI-5 — Resolution completes before what depends on it
*Derives from: SM-3*

Every reference a determination depends on is resolved before the determination is reached. An
unresolved reference is a failure of the activity that required it. It is never a condition
discovered later.

- **Violated when** an activity carries something unresolved forward and expects it to resolve
  later, or attempts resolution during execution.
- **Shown by** a resolution failure that surfaces at execution. That failure is the observable
  signature of a construction that did not complete.

This invariant specifies an order, not a time. Resolution may happen long before execution or just
before it. It must happen *first*.

### AI-6 — Absence is not permission
*Derives from: SM-4*

Inability to determine the applicable governance MUST NOT produce the same outcome as governance
that permits. An unknown closure is not an empty closure.

- **Violated when** a system treats an unresolvable governing element, an undeclared authority, or
  an unreachable rule set as nothing to check.
- **Shown by** an admission whose evidence records no rules where rules should have been supplied.
  That signature tells governed permission apart from unnoticed absence.

Of all the invariants, a breach of this one is the least visible from inside a system and the most
damaging. A system that breaches it behaves exactly like a governed one. The difference appears only
when a case arrives that governance would have refused.

### AI-7 — Refusal dominates
*Derives from: SM-5*

When the rules that apply to a proposal yield different consequences, the determination is the most
restrictive of them. No rule admits what another applicable rule refuses. Adding a rule to a closure
never widens what the system may do.

- **Violated when** a system combines consequences permissively. Examples: it reads an allowance as
  overriding a prohibition, lets a specific permission defeat a general refusal, or takes the first
  or last matching rule as the answer.
- **Shown by** evidence that records a refusal among the evaluated rules and an admission as the
  determination.

### AI-8 — Refusal leaves no residue
*Derives from: SM-7*

A refused proposal takes no partial effect. After refusal, the governed state is as though nobody
had made the proposal. The only trace is the evidence of the refusal.

- **Violated when** a partial result survives a refusal. Examples: output written before the
  refusal, state advanced and not reverted, or a side effect already emitted.
- **Shown by** governed state that differs between a refused proposal and no proposal.

### AI-9 — Identity is derived, sealing is real
*Derives from: SM-10; Conceptual Model, sealing*

A realization derives the identity of a sealed representation from its sealed content. It never
assigns that identity. After sealing, that content does not change. Two sealed representations
bearing the same identity MUST have identical content.

- **Violated when** a realization allocates an identity instead of computing it, or modifies sealed
  content in place. Also violated when two artifacts share an identity and differ.
- **Shown by** identical identifiers over different content, or by content that changed while its
  identifier stayed the same.

---

## 6. Execution

### AI-10 — Execution consumes a verified sealed representation
*Derives from: SM-1, SM-2*

Execution proceeds only against a representation confirmed to be exactly what construction
authorized. On a mismatch, execution does not occur.

- **Violated when** execution begins without verification, or continues after a failed one.
- **Shown by** execution evidence that carries no verification. Also shown by a representation whose
  identity differs from what construction attested.

This document leaves open when sealing occurs (AI-5). It requires that execution consume something
sealed and verified.

### AI-11 — Structure is complete before execution
*Derives from: SM-3; Conceptual Model, execution*

The structure that execution traverses is complete before traversal begins. Execution constructs,
extends and reroutes no part of it during the run.

- **Violated when** a realization synthesizes a step, route or handler from payload, environment or
  accumulated state.
- **Shown by** evidence that the structure was constructed, extended, rerouted or resolved after
  execution began. Divergent traversals under an identical sealed representation and identical
  inputs are one observable consequence. They are not the definition. A structure may mutate
  dynamically and still traverse identically in any given test.

### AI-12 — Nothing enters by discovery
*Derives from: SM-3, §7 boundedness*

Only what was declared and admitted takes part in a determination or an execution. Nothing enters by
being found, whether by scanning, by convention or by default.

- **Violated when** behavior depends on something located rather than declared, or when a default
  supplies what a declaration omitted.
- **Shown by** behavior that changes in response to a change in surroundings while declarations and
  inputs stay the same.

This is the sharpest single test of a governed system. **Move the system and keep these unchanged:
its declarations, its sealed representation, its governed inputs, and any explicitly
declared environment. It must then behave the same.** An environment that is a declared, governed input may
legitimately change behavior. An environment that is merely present may not.

### AI-13 — Effects occur only through declared surfaces
*Derives from: SM-1; Conceptual Model, side effect*

Every effect a governed system has beyond its own governed state passes through a declared, governed
surface. The set of ways the system can affect the world is closed and known.

- **Violated when** an effect reaches the world through a path no declaration establishes.
- **Shown by** an observed external effect with no matching declared surface in evidence.

---

## 7. Evidence

### AI-14 — Every determination is evidenced
*Derives from: SM-8, §8.5*

Every determination produces evidence adequate to establish what was evaluated and what resulted. A
determination without adequate evidence governed nothing, whatever it decided.

- **Violated when** evidence records outcomes without the closure and rules that produced them, or
  when a system produces evidence for admissions and not for refusals.
- **Shown by** evidence from which a party cannot re-derive the determination.

### AI-15 — Evidence is output only
*Derives from: SM-6; Conceptual Model, trace*

Evidence is never an input to a determination. Nothing reads the record of what happened in order to
decide what happens.

- **Violated when** a determination consults a trace, or a system replays evidence into itself as
  state.
- **Shown by** a determination whose result changes when prior evidence is withheld, all else equal.

### AI-16 — Evidence is checkable without its producer
*Derives from: SM-12, §13*

Evidence establishes what it establishes to a party that has no access to the system that produced
it and does not trust that system. A checker re-evaluates the recorded closure and rules the evidence
represents. It uses the authority and profile information that the applicable semantic case requires:

- for an ordinary transition, the closure inherited from the baseline;
- for genesis, the proposal's declared governance together with the claimed profile (Semantic Model
  §11).

A checker never rediscovers a closure from a current environment.

- **Violated when** a party can establish what happened only by querying the live system,
  reconstructing its environment, or accepting an unsupported assertion.
- **Shown by** a check that a party cannot perform on the evidence alone.

---

## 8. Change

### AI-17 — Change occurs only by governed transformation
*Derives from: SM-9, SM-11*

The declarations of a governed system change only through a transformation of its baseline. That
transformation is determined and evidenced like any other transition. After genesis, nothing
constitutes itself. No subsystem, domain, artifact or deployment declares itself into a system by its
own authority.

- **Violated when** declarations change by a path other than a determined transformation. Examples:
  someone edits them in place, a loader injects them, or a deployment introduces them. Also violated
  when a later addition claims genesis and supplies its own admission.
- **Shown by** a baseline that differs with no transformation evidence to account for the
  difference.

Genesis is the single exception. It is not an exception to governance. Its closure is composed from
the proposal and from a profile the proposal does not author (Semantic Model §11).

---

## 9. What follows from the invariants

People value governed computation for certain properties. Those properties are **consequences** of
the invariants above. They are not extra requirements, and they are not design goals. Each one
follows, so none needs separate pursuit.

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

The direction of this table is normative. **A system can show these properties without preserving
the invariants. It then has them by circumstance, and it will lose them without warning.** Suppose
implementation discipline, not the invariants, produces a system's determinism. That determinism
lasts only until a change brings in an undeclared source of variation.

## 10. Violation

An architectural invariant is not a quality target. A violation is not a degree of non-conformance
to trade against other properties. When a system breaches an invariant, it stops being a governed
system with respect to everything downstream of the breach.

Three consequences follow:

- **A breach is not local.** Suppose AI-6 is breached in one closure. Then every determination that
  relied on that closure is unestablished, including determinations that were individually correct.
- **Nothing compensates for a breach.** Extra checking downstream cannot restore a determination
  that was never made. Enforcement added after the fact detects. It does not govern. A downstream
  check may detect a breach, and remediation may restore conformance for future transitions.
  Neither one makes the breached transition governed after the fact.
- **Good outcomes do not repair a breach.** A system that behaved acceptably while breaching an
  invariant is the expected case, not a mitigating one (AI-6).

## 11. Conformance

The conformance subject of this document is a **realization**: a built system that claims to perform
governed computation.

A realization conforms when two conditions hold for each invariant AI-1 … AI-17:

- the invariant holds of the realization;
- the realization can point to the observation that would show a violation.

The second condition is essential. If a realization cannot demonstrate that it preserves an
invariant, it has only asserted that invariant.

A realization does **not** demonstrate conformance to this document by exhibiting the properties of
§9. Those properties follow from the invariants, but they can also appear without them. A regime that
tests consequences in place of premises makes the error §9 exists to prevent.

The Conformance Model and the Conformance Test Specification own how a party claims, levels and
demonstrates conformance, and what evidence discharges each invariant. This document specifies what
must be true.
