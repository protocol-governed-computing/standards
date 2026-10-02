# Semantic Model

## 1. Scope

This document defines the abstract machinery of governed computation. It says:

- what a governed state is;
- what it means for one governed state to become another;
- what makes such a change *governed*, rather than something that merely happens.

At this layer, the word "governed" gets a meaning that depends on no artifact kind, no governance
vocabulary and no activity. Documents that define kinds, execution, construction or transformation
inherit their semantics from here. None of them may give a different account of what governance does
to a change.

This document introduces the terms **transition**, **governed transition**, **proposal**,
**determination**, **rule**, **predicate**, **consequence**, **rule set**, **evaluation**, **empty
governed state**, and **genesis**. The Conceptual Model defines every other term it uses, with the
meaning given there.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What this model must account for

A semantic model earns its place only if it explains what the vocabulary alone cannot. This model
must account for four things:

1. **Why the same machinery governs execution, construction and change.** The Conceptual Model
   names three activities. If each had its own semantics, "governed" would mean three different
   things. The family would then be three families.
2. **What separates a governed change from an ungoverned one.** The model must state the difference
   precisely enough that a party can check it, not merely assert it.
3. **Why refusal is an outcome rather than a failure.** If a model treats refusal as an error, it
   cannot explain why a refusing system is working correctly.
4. **How a third party who observed nothing can establish what was determined.** A conformance
   claim is made to someone. A model that cannot support that claim cannot support conformance.

## 3. Governed state

A **governed state** is a complete assignment of values to everything a governance closure applies
to at one moment. It is the *subject* of governance: the thing rules are about.

- A governed state is complete with respect to its closure. The state settles everything the closure
  can speak about. Whatever the state leaves open, the closure does not govern.
- A governed state differs from stored data. Data becomes governed state exactly when a closure
  applies to it. Data that no closure speaks about sits in the system without being part of its
  governed state.
- Governed state includes the declarations themselves. So the system's own governance can be
  governed. That is why the model needs no second, outer mechanism to govern change.

Write a governed state `S`.

## 4. The governed transition

Everything that happens in a governed system has one shape:

```
        proposal π
             │
    S ───────┴──────▶  Δ = determine(S, π, C)  ───────▶  (S′, ε)
  governed state              determination            next state, evidence
                       under closure C
```

A **proposal** `π` is a candidate change presented to a governed state. A proposal is a request for a
change, not a change. It has no effect until it is determined.

A **determination** `Δ` is the result of evaluating the rules that the governance closure `C`
supplies for `(S, π)`. It is a value, not an action. The transition is what follows from it.

A **transition** combines three things: a governed state, a determination made over a proposal, and
the resulting state with the evidence of that determination. Written:

```
τ = ⟨ S, Δ, (S′, ε) ⟩       where Δ = determine(S, π, C)
```

A transition is the shape a change takes. Whether a given transition is *governed* is a separate
question, which §8 answers. The model allows ungoverned transitions to exist and be classified. A
model that forbade them from existing could not say what is wrong with a system that produces one.

A governed transition has four required properties. §8 states them as conditions rather than
assuming them here:

- **Priority.** The determination completes before the governed-state change it governs occurs. A
  determination MUST NOT depend on observing the change it determines.
- **Totality.** Every proposal reaches a determination. Each proposal is either admitted or refused.
- **Closure-completeness.** Every rule the closure supplies for `(S, π)` is evaluated. A result
  reached from part of a closure is not a determination.
- **Evidence.** The determination produces `ε`. That evidence suffices to establish what was
  evaluated and what resulted (§13).

## 5. Rules

A **rule** is a normative condition over a governed state, a proposal or a transition, stated so that
it can be evaluated. A rule has exactly two parts:

- a **predicate**: the condition evaluated, which yields a value over `(S, π)`;
- a **consequence**: what follows from each value the predicate can yield.

A rule carries an obligation in evaluable form. A governing element places that obligation on a
subject. The rule renders the obligation so a machine can determine whether it holds.

An obligation with no rule is only an intention. The model gives it no effect.

A **rule set** is the collection of rules that a closure supplies for a given `(S, π)`. The rule set
is always derived from the closure, never authored beside it. A rule that the applicable closure
does not supply plays no part in the determination, whatever else it may be.

**Evaluation** is the application of a predicate to `(S, π)` to yield a value. Evaluation has two
required properties:

- **Total.** A predicate yields a value for every `(S, π)` in its domain. Otherwise it is not a
  predicate.
- **Free of effect.** Evaluating a rule changes no governed state. A predicate that alters what it
  evaluates makes the determination unrepeatable, so the model excludes it.

## 6. Consequence

A consequence is one of exactly three:

| Consequence | Meaning |
|---|---|
| **admit** | the proposal may proceed, on its own terms |
| **constrain** | the proposal may proceed only in a restricted form the rule states |
| **refuse** | the proposal does not proceed |

Consequences are ordered: `refuse` dominates `constrain`, and `constrain` dominates `admit`. When a
rule set yields several consequences, the determination is the dominant one. This ordering is not a
policy choice. It is what makes a closure composable at all. Under any other ordering, adding a rule
to a closure could widen what the system may do. A closure that grows more permissive as it grows
larger governs nothing.

**Where several rules constrain, the constraints compose by conjunction.** The ordering settles which
consequence a rule set yields. It does not settle which restricted form applies when two applicable
rules each state one. A proposal satisfies the composed constraint only where it satisfies every
constituent constraint. This is the ordering's requirement again, one level down. Any other
composition would let a proposal proceed in a form that some applicable rule restricts. Adding a rule
would again widen what the system may do.

**Rules never grant.** A rule may permit, restrict or refuse a proposal. A rule may not cause the
admission of a proposal that another rule refuses. Authority to act comes from the governing
declarations, which establish that the proposal may proceed. A rule may not override a refusal that
another applicable rule supplies. A proposal holds no authority of its own. It is a candidate. The
determination decides what it may become, and the proposal never asserts that for itself.

## 7. The closure and its evaluation

The **governance closure** `C` for a subject determines, completely, three things: *which* governing
elements apply to it, *by what authority* each applies, and *how* their rules compose:

```
C : (S, π) ⟼ ⟨ applicable governing elements with their authority, composition ⟩
                              │
                              ▼
                          rule set          — what evaluation consumes
```

The closure is not the rule set. A rule applies *because a particular governing element had
authority over this subject*. Flattening the closure into a rule set loses that fact. That fact is
the difference between a rule that governs and a rule that merely appeared. Evidence must carry
this difference (§13), so the model must preserve it.

Every closure has three required properties:

- **Determinacy.** The same `(S, π)` yields the same rule set. If a closure supplied different rules
  on different occasions, every determination would be provisional.
- **Boundedness.** The rule set is finite and known before evaluation begins. A determination cannot
  depend on discovering another rule during evaluation.
- **Non-ambient composition.** The rule set derives from declared authority and scope. It never
  derives from the position, ordering, containment or load order of what carries the rules.

### 7.1 Incompleteness

Sometimes the closure cannot be established for `(S, π)`. A governing element may be unresolvable,
an authority undeclared, or a rule set unbounded. In that case the model mandates the determination
`refuse`.

This is a **closure-failure determination**. The model imposes it. Rule evaluation does not produce
it. The rule set could not be established, so no rule was evaluated. The model itself refuses.

This distinction matters wherever enforcement must report *why* it refused. A closure failure and a
rule refusal call for entirely different remedies.

This is the model's most consequential rule, and it is deliberately asymmetric. An unknown closure
is not an empty closure. If a system treats what it could not establish as permission, ungoverned
change enters a system that believes itself governed. No later evidence can tell that change apart
from governed change. **Absence of applicable governance and inability to determine applicable
governance MUST NOT produce the same outcome.**

## 8. What "governed" means

A transition is **governed** when all five of these hold:

1. a closure `C` was established for `(S, π)`;
2. every rule that `C` supplied for `(S, π)` was evaluated;
3. the determination is the dominant consequence of those evaluations;
4. the resulting state is what that determination permits, and nothing more;
5. evidence `ε` was produced, sufficient to establish 1–4 to a party that did not observe them.

**The closure is established for the state the transition applies to.** Suppose a determination is
made against one state and applied to another. It is then not a determination of that transition. No
closure was established for the pair it actually governed. If two proposals are determined against
the same state and both are applied, at most one of them is a governed transition. This follows from
clause 1. The model states it because a sequential realization never has to derive it.

**Clause 4 bounds the result in both directions.** A transition that applies less than *"what that
determination permits"* also fails it. A transition that applied part of what it was permitted
produced a state no determination permitted. Clause 4 makes it ungoverned, just as it makes a
transition that exceeded its permission ungoverned. **A realization in which a transition can apply
partly MUST determine what state results.** It may prevent the partial application, complete it, or
reduce it to a state some determination permits. This document does not specify which, or by what
mechanism.

A transition that fails any of 1–5 is **ungoverned**, even if its result is the one governance would
have permitted. Two cases are often mistaken for governed changes, so the model names them:

- *A permitted outcome reached without determination is not a governed outcome.* If the result
  happens to match what governance would have allowed, that is coincidence, not discharge.
- *A determination that cannot be established is not a determination.* Suppose a transition
  satisfies 1–4 but lacks adequate evidence. It is ungoverned. Its state change may well be what
  the determination permitted. But being governed includes being able to establish that it was. A
  party who must take the system's word is not governed by the system's rules. That party is
  trusting them.

So evidence is **constitutive**, not diagnostic. It is not a record kept about governance. It is part
of what governance is. The rest of the family follows from this single distinction.

A **governed system** is one in which every transition of its governed state is a governed
transition. Governance is not a property some changes have and others lack. A system with one
ungoverned path is an ungoverned system that happens to be governed on most paths.

## 9. Refusal

When the determination is `refuse`, the transition still occurs. It leads to a state in which the
proposal was refused, with evidence of the refusal:

```
τ = ⟨ S, refuse, (S, ε) ⟩
```

The governed state is unchanged with respect to the proposal, and the system has done exactly what
it should. Refusal therefore has three properties:

- **It is an outcome, not an error.** Refusal means the determination succeeded, not that the
  mechanism failed. A system that refuses correctly is working. A model that treats refusal as
  failure cannot say so.
- **It is evidenced like any determination.** A refusal that leaves no record looks the same as a
  proposal never made.
- **It is not degradation.** A refused proposal has no reduced form in which it partly proceeds. A
  partial application after refusal is an ungoverned transition. Its resulting state is not what the
  determination permitted (§8.4).

## 10. One schema, three subjects

The Conceptual Model names three activities. They do not have three semantics. Each one is the schema
of §4 applied to a different subject:

| Activity | `S` is | `π` is | `S′` is |
|---|---|---|---|
| **Transformation** | the baseline | a proposed change to the declarations | the next baseline |
| **Construction** | the authorized declarations | a candidate declaration | the authorized representation |
| **Execution** | the governed state under a snapshot | an interaction presented to the system | the governed state after it |

This is the model's central claim. The four properties of §4 apply identically to all three
activities. Three consequences follow directly:

- **Transformation is not exempt.** A change to a governed system is itself a governed transition. A
  closure determines it, and it produces evidence. Suppose a system's declarations can change by any
  path of another shape. That system is ungoverned with respect to its own governance, whatever its
  execution does.
- **Admission is a determination.** A candidate becomes part of a system only when a determination
  admits it. That is why presence never constitutes admission. Being found admits nothing.
- **The activities compose without a fourth mechanism.** Each activity's resulting governed
  representation supplies the governed input to the next. The links follow the authority chain the
  Conceptual Model specifies. The three results are different kinds of object: a baseline, an
  authorized representation, and a governed execution state. So what holds between them is semantic
  continuity, not identity. No activity reaches past its successor. The composition needs no outer
  supervisor to be governed, because the same schema governs each link.

The activities differ in what they determine, never in how determination works:

```
transformation determines what the declarations are
construction   determines which declarations are authorized to be executed
execution      determines what occurs under those declarations
```

## 11. Genesis

The schema of §4 takes a governed state as input. The first transition of a governed system has no
earlier baseline. Its input is the **empty governed state** `∅`. No prior closure exists from which
it could inherit governance.

```
∅ ──────▶ the first baseline
```

This case, the constitution of a platform from nothing, is **not an exemption**. The model allows
none. An ungoverned first transition would put the whole system on an ungoverned foundation. Every
later transition would inherit governance from a state that was never determined. A system cannot be
governed from an ungoverned origin.

**The empty governed state.** `∅` is the governed state in which nothing is declared and nothing is
governed. It is a legitimate governed state, not the absence of one.

**Reflexive determination.** In genesis, and only in genesis, the proposal itself supplies part of
the closure. The proposed baseline carries the governance that governs it. To that extent the
determination is reflexive: it evaluates the proposed state against the rules that state declares.
Genesis handles two failures:

- A proposed baseline that violates its own governance is refused.
- A proposed baseline that cannot be evaluated against its own governance is a closure failure
  (§7.1), and is refused for that reason.

The proposal supplies the subject's *declared governance*. It does not supply the external
requirements against which genesis is admitted.

**The vacuity problem.** Reflexive determination alone is not enough, for an immediate reason. A
baseline that declares no rules satisfies its own closure trivially. So self-consistency is
necessary but not sufficient. Genesis needs a second condition that the proposal does not author.

**The claimed profile.** A genesis proposal MUST name the profile it claims. The profile is not part
of the proposal, and the proposal does not author it. The profile states requirements the resulting
baseline must satisfy, and they come from outside the system being constituted. Genesis is admitted
when the proposed baseline meets both conditions:

- it is consistent with the governance it declares, **and**
- it satisfies the profile it claims.

The first condition stops a system from contradicting itself. The second stops it from governing
itself vacuously.

**The genesis closure.** The two sources compose into one closure. So genesis uses the same
determination schema as every other transition:

```
C_gen(π, P) = C_π ⊕ P        C_π  the governance declared within the proposal
                             P    the requirements of the claimed profile

Δ = determine(∅, π, C_gen(π, P))
```

Genesis differs only in *how `C` is established*, never in what determination is. Elsewhere, the
closure is inherited from the governed system. Here, the proposal's declared governance and the
externally claimed profile compose it. That composition works by dominance like any other (§6). So
the profile can refuse what the proposal's own governance would admit, and that is its purpose.

A genesis transition is therefore a governed transition in the full sense of §8. A closure was
established, and its rules were evaluated. The determination is the dominant consequence. The
resulting state is what that determination permitted, and evidence establishes all of it. Genesis
differs only in *where the closure comes from*: the proposal and the claimed profile, not a
predecessor state.

Every later transition inherits its closure from the baseline. Genesis is the one transition where
that is impossible. It is the one place where the model lets a closure originate with what it
governs.

## 12. Determinism

The determination function is deterministic. For the same `(S, π, C)` it yields the same `Δ`.

This is a property of the model, not a goal for an implementation. It follows from two earlier
sections: evaluation is total and effect-free (§5), and the closure is determinate and bounded (§7).

The property reaches the resulting state through one further step. The model states this step rather
than assuming it: **the same determination, applied to the same governed state, permits the same
resulting state.** The determination and the state it applies to fix the state update. Nothing else
does. So, given the same `(S, π, C)`, a governed transition reaches the same `Δ` and the same `S′`.

In execution, the proposal `π` includes every captured input the execution records (Conceptual
Model, *captured input*). So determinism holds relative to captured inputs. Two executions that
capture different values have different proposals, and may reach different determinations. Two
executions that hold the same captured inputs reach the same `Δ` and the same `S′`.

Determinism constrains the determination and the resulting state. It does not require identical
evidence between two executions of the same transition. Evidence may carry observational material
that varies while every governed consequence stays the same (Conceptual Model, *Determinism*). §13
states what is required.

## 13. Evidence in the model

Evidence is a term of the model, not a record kept about it. For a transition `τ`, evidence `ε` is
adequate when it suffices to establish:

- which closure applied;
- which rules that closure supplied;
- what each predicate yielded;
- what the dominant consequence was;
- that `S′` is what that consequence permitted.

Adequate evidence supports the conformance relation of §14. The party checking it need not have
observed the transition, held the state, or trusted the system that produced it. Evidence that
establishes the result but not the determination is inadequate. It shows what happened, not that it
was governed, and §8 exists to separate those two things.

The Evidence, Attestation & Provenance Standard specifies which parts of evidence must be identical
across executions and which are observational. This document requires only that evidence suffice for
the five points above.

## 14. The conformance relation

At the semantic level, conformance is a relation between a transition and the governing requirements
that apply to it. This document defines that transition-level relation and nothing beyond it. The
Conformance Model owns conformance for the family. It specifies how the relation lifts to the other
conformance subjects: an artifact, a governed representation, an implementation, a system instance.

A transition `τ` **conforms** when two conditions hold:

- it is governed (§8);
- its determination was the correct determination. That is, a re-evaluation of **the closure and
  rules recorded in its evidence** yields the same dominant consequence that `τ` recorded.

The checker re-evaluates what the evidence carries. It MUST NOT rediscover the closure from a live
system or a current environment. A closure rediscovered later may differ from the one that applied.
A check against a closure that did not govern the transition establishes nothing about the
transition. That is why §13 requires evidence to carry the closure, not merely the outcome.

Two things follow, and they are why anyone can check conformance at all:

- **A party decides conformance over evidence, not over behavior.** A checking party re-derives the
  determination from `ε` and compares. It does not re-run the system, and it needs no access to it.
- **Conformance is a property of transitions, and of systems only through them.** A system conforms
  with respect to a set of transitions when each of them conforms. A claim about a system must name
  transitions and evidence. Without them it is not a conformance claim.

Non-conformance has exactly two forms, and they are not interchangeable:

| Form | What happened | What it indicates |
|---|---|---|
| **Ungoverned transition** | the transition fails one or more constitutive conditions of §8 — no determination, an unestablished or partial closure, incomplete evaluation, a resulting state the determination did not permit, or inadequate evidence | the mechanism is wrong |
| **Incorrect determination** | the determination was made and is not what the closure yields | a rule, or its evaluation, is wrong |

A new rule cannot repair the first form. Added enforcement cannot repair the second. A conformance
regime that reports them as one defect misdirects every remedy.

## 15. What this model omits

This model omits five things on purpose. A document that fills one of them in here is out of scope,
not helpful:

- **Time.** The model orders determinations relative to the transitions they govern. It says nothing
  about duration, concurrency, or when a determination occurs in wall-clock terms.
- **Distribution.** `S`, `C` and the determination are semantic objects. Whether they are
  co-located, replicated or partitioned is not a semantic question.
- **Artifact kinds.** Nothing here depends on which kinds of declaration exist. The model is the
  reason a realization can add kinds without changing the meaning of "governed".
- **Representation.** No term above implies an encoding, schema or format.
- **Rule expression.** This document leaves open how a predicate is written, and in what language.
  The model requires only that evaluation be total and effect-free.

## 16. Normative invariants

- **SM-1.** Every change to governed state MUST be a governed transition (§4).
- **SM-2.** A determination MUST complete before the transition it governs occurs.
- **SM-3.** A determination MUST be reached over the complete rule set the closure supplies. A
  partial evaluation MUST NOT yield a determination.
- **SM-4.** Where a closure cannot be established, the determination MUST be `refuse` (§7.1).
- **SM-5.** Consequences MUST compose by dominance, and no rule may admit what another refuses (§6).
- **SM-5a.** Where several applicable rules constrain, their constraints MUST compose by
  conjunction. A proposal satisfies the composed constraint only where it satisfies every
  constituent constraint (§6).
- **SM-6.** Predicate evaluation MUST NOT alter governed state.
- **SM-7.** A refused proposal MUST NOT partly proceed (§9).
- **SM-7a.** An admitted transition MUST NOT come to rest having applied part of what its
  determination permits. Where a realization can apply a transition partly, it MUST determine what
  state results (§8).
- **SM-7b.** A closure MUST be established for the state the transition applies to (§8).
- **SM-8.** Every determination MUST produce evidence adequate by §13.
- **SM-9.** Transformation of the declarations MUST itself be a governed transition (§10).
- **SM-10.** The same `(S, π, C)` MUST yield the same determination. The same determination applied
  to the same governed state MUST permit the same resulting state (§12).
- **SM-11.** A genesis transition MUST be determined reflexively against the closure its proposal
  declares. It MUST also satisfy the profile it claims, and it MUST NOT be exempt from §8 (§11).
- **SM-12.** Conformance checking MUST re-evaluate the closure and rules recorded in evidence. It
  MUST NOT rediscover a closure from a live system or current environment (§14).

## 17. Conformance

This document states the semantic requirements against which conformance is evaluated. It does not
define conformance subjects, claims, levels or demonstration procedures. The Conformance Model and
the Conformance Test Specification own those. This document deliberately sets up no second account
of them.

This document does specify what a **semantics** must satisfy to count as an account of governed
computation under this model. The semantics may come from another document of this family or from an
implementation. It must meet all of the following:

- Every change of governed state it describes has the shape of §4.
- Every change it treats as governed satisfies all five conditions of §8.
- It gives `refuse` the standing of §9, and treats refusal as an outcome, not a failure.
- It composes consequences by dominance, and resolves an unestablishable closure to `refuse`.
- It produces evidence adequate by §13 for every determination it describes.
- It constitutes an initial state only as §11 permits.
- It changes governed state only through governed transitions.

How a party claims, levels and demonstrates satisfaction of these requirements is not this
document's business.
