# Semantic Model

## 1. Scope

This document defines the abstract machinery of governed computation: what a governed state
is, what it means for one governed state to become another, and what makes such a change
*governed* rather than merely occurring.

It is the layer at which the word "governed" acquires a meaning that does not depend on any
artifact kind, any governance vocabulary, or any activity. Documents that define kinds,
execution, construction, or transformation inherit their semantics from here; none of them may
supply a different account of what governance does to a change.

This document introduces the terms **transition**, **governed transition**, **proposal**,
**determination**, **rule**, **predicate**, **consequence**, **rule set**, **evaluation**,
**empty governed state**, and **genesis**. Every other term it uses is defined by the
Conceptual Model, with the meaning specified there.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What this model must account for

A semantic model earns its place only if it explains things the vocabulary cannot. This one is
required to account for four:

1. **Why the same machinery governs execution, construction, and change.** The Conceptual Model
   names three activities. If each had its own semantics, "governed" would mean three
   different things and the family would be three families.
2. **What distinguishes a governed change from an ungoverned one** — precisely enough that the
   difference can be checked, rather than asserted.
3. **Why refusal is an outcome rather than a failure.** A model in which refusal is an error
   cannot explain why a refusing system is working correctly.
4. **How a third party who observed nothing can establish what was determined.** Conformance is
   a claim made to someone; a model that cannot support that claim cannot support conformance.

## 3. Governed state

A **governed state** is a complete assignment of values to everything a governance closure
applies to at one moment. It is the *subject* of governance: the thing rules are about.

- A governed state is complete with respect to its closure. Anything the closure can speak
  about, the state settles; anything the state leaves open, the closure does not govern.
- A governed state is not the same as stored data. Data becomes governed state exactly when a
  closure applies to it; data no closure speaks about is present in a system without being part
  of its governed state.
- Governed state includes the declarations themselves. This is what allows the system's own
  governance to be governed, and it is the reason the model does not need a second, outer
  mechanism to govern change.

Write a governed state `S`.

## 4. The governed transition

Everything that happens in a governed system is one shape:

```
        proposal π
             │
    S ───────┴──────▶  Δ = determine(S, π, C)  ───────▶  (S′, ε)
  governed state              determination            next state, evidence
                       under closure C
```

A **proposal** `π` is a candidate change presented to a governed state. A proposal is not a
change: it is a request for one, and it has no effect until determined.

A **determination** `Δ` is the result of evaluating the rules that the governance closure `C`
supplies for `(S, π)`. It is a value, not an action — what follows from it is the transition.

A **transition** is a governed state, a determination made over a proposal, and the resulting
state together with the evidence of that determination. Written

```
τ = ⟨ S, Δ, (S′, ε) ⟩       where Δ = determine(S, π, C)
```

A transition is the shape a change takes. Whether a given transition is *governed* is a
further question, answered in §8 — the model admits ungoverned transitions as things that can
exist and be classified, because a model in which they cannot exist cannot say what is wrong
with a system that produces one.

Four properties are required of a governed transition, and §8 states them as conditions rather
than assuming them here:

- **Priority.** The determination completes before the governed-state change it governs
  occurs. A determination MUST NOT depend on observing the change it determines.
- **Totality.** A determination is reached for every proposal. There is no proposal that is
  neither admitted nor refused.
- **Closure-completeness.** Every rule the closure supplies for `(S, π)` is evaluated. A
  determination reached from part of a closure is not a determination.
- **Evidence.** The determination produces `ε`, sufficient to establish what was evaluated and
  what resulted (§13).

## 5. Rules

A **rule** is a normative condition over a governed state, a proposal, or a transition,
expressed so that it can be evaluated. A rule has exactly two parts:

- a **predicate** — the condition evaluated, which yields a value over `(S, π)`; and
- a **consequence** — what follows from each value the predicate can yield.

A rule is the evaluable form in which an obligation is carried. The obligation is what a
governing element places on a subject; the rule is that obligation rendered so that a machine
can determine whether it holds. An obligation with no rule is an intention, and the model
gives it no effect.

A **rule set** is the collection of rules that a closure supplies for a given `(S, π)`. A rule
set is derived from the closure, never authored beside it: a rule that is not supplied by the
closure applicable to the subject is not part of the determination, whatever else it may be.

**Evaluation** is the application of a predicate to `(S, π)` yielding a value. Evaluation is
total — a predicate that cannot yield a value for some `(S, π)` in its domain is not a
predicate — and free of effect: evaluating a rule changes no governed state. A predicate whose
evaluation alters what it evaluates makes the determination unrepeatable and is excluded.

## 6. Consequence

A consequence is one of exactly three:

| Consequence | Meaning |
|---|---|
| **admit** | the proposal may proceed, on its own terms |
| **constrain** | the proposal may proceed only in a restricted form the rule states |
| **refuse** | the proposal does not proceed |

Consequences are ordered: `refuse` dominates `constrain`, which dominates `admit`. When a rule
set yields several consequences, the determination is the dominant one. This ordering is not a
policy choice — it is what makes a closure composable at all. Under any other ordering, adding
a rule to a closure could increase what the system may do, and a governance closure that grows
more permissive as it grows larger governs nothing.

**Where several rules constrain, the constraints compose by conjunction.** The ordering above
resolves which consequence a rule set yields; it does not by itself say which restricted form
applies when two applicable rules each state one. A proposal satisfies the composed constraint only
where it satisfies every constituent constraint. This is the same requirement as the ordering, one
level down: any other composition would let a proposal proceed in a form some applicable rule
restricts, and adding a rule would again enlarge what the system may do.

**No rule grants.** A rule may permit, restrict, or refuse a proposal, but no rule may cause a
proposal to be admitted that another rule refuses. Authority to act comes from the governing
declarations establishing that the proposal may proceed; no rule may override a refusal
supplied by another applicable rule. A proposal holds no authority of its own — it is a
candidate, and what it may become is determined about it, never asserted by it.

## 7. The closure and its evaluation

The **governance closure** `C` for a subject is the complete determination of *which* governing
elements apply to it, *by what authority* each applies, and *how* their rules compose:

```
C : (S, π) ⟼ ⟨ applicable governing elements with their authority, composition ⟩
                              │
                              ▼
                          rule set          — what evaluation consumes
```

The closure is not the rule set. Flattening it into one loses the fact that a rule applied
*because a particular governing element had authority over this subject* — which is the
difference between a rule that governs and a rule that merely appeared. Evidence is required to
carry that difference (§13), so the model must preserve it.

Three properties are required of any closure:

- **Determinacy.** The same `(S, π)` yields the same rule set. A closure that supplies
  different rules on different occasions makes every determination provisional.
- **Boundedness.** The rule set is finite and known before evaluation begins. A determination
  cannot depend on discovering, while evaluating, that there was another rule.
- **Non-ambient composition.** The rule set is derived from declared authority and scope, never
  from the position, ordering, containment, or load order of what carries the rules.

### 7.1 Incompleteness

If the closure cannot be established for `(S, π)` — a governing element is unresolvable, an
authority is undeclared, a rule set cannot be bounded — the model mandates the determination
`refuse`.

This is a **closure-failure determination**: it is imposed by the model, not produced by
evaluating rules. No rule was evaluated, because the rule set could not be established; what
refuses is the model itself. The distinction matters wherever enforcement must report *why*
something was refused, since a closure failure and a rule refusal call for entirely different
remedies.

This is the model's most consequential rule, and it is deliberately asymmetric. An unknown
closure is not an empty closure. Treating what could not be established as permission is the
mechanism by which ungoverned change enters a system that believes itself governed, and no
subsequent evidence can distinguish it from governed change. **Absence of applicable
governance and inability to determine applicable governance MUST NOT produce the same
outcome.**

## 8. What "governed" means

A transition is **governed** when:

1. a closure `C` was established for `(S, π)`;
2. every rule that `C` supplied for `(S, π)` was evaluated;
3. the determination is the dominant consequence of those evaluations;
4. the resulting state is what that determination permits, and nothing more; and
5. evidence `ε` was produced sufficient to establish 1–4 to a party that did not observe them.

**The closure is established for the state the transition applies to.** A determination made against
one state and applied to another is not a determination of that transition: no closure was
established for the pair it actually governed. Where two proposals are determined against the same
state and both applied, at most one of them is a governed transition. This follows from clause 1 and
is stated because it is the derivation a sequential realization never has to make.

**Clause 4 bounds the result in both directions.** *"What that determination permits"* is not
satisfied by less than it either: a transition that applied part of what it was permitted produced a
state no determination permitted, and is ungoverned by clause 4 as surely as one that exceeded it.
**A realization in which a transition can apply partly MUST determine what state results** — by
preventing the partial application, by completing it, or by reducing it to a state some determination
permits. Which of those, and by what mechanism, is not specified here.

A transition failing any of 1–5 is **ungoverned**, regardless of whether its result was the one
governance would have permitted. Two cases deserve naming, because both are routinely mistaken
for governed changes:

- *A permitted outcome reached without determination is not a governed outcome.* That the
  result happens to be what governance would have allowed is a coincidence, not a discharge.
- *A determination that cannot be established is not a determination.* A transition satisfying
  1–4 but lacking adequate evidence is ungoverned: the state change may well have been what
  the determination permitted, but governedness includes being able to establish that it was,
  and a party who must take the system's word for it is not governed by the system's rules —
  they are trusting them.

Evidence is therefore **constitutive**, not diagnostic. It is not a record kept about
governance; it is part of what governance is. This is the single distinction from which the
rest of the family follows.

A **governed system** is one in which every transition of its governed state is a governed
transition. Governance is not a property some changes have and others lack: a system with one
ungoverned path is an ungoverned system that is governed on most paths.

## 9. Refusal

When the determination is `refuse`, the transition still occurs — as a transition to a state
in which the proposal was refused, with evidence of the refusal.

```
τ = ⟨ S, refuse, (S, ε) ⟩
```

The governed state is unchanged with respect to the proposal, and the system has done exactly
what it should. Refusal is therefore:

- **an outcome, not an error.** It is the determination succeeding, not the mechanism failing.
  A system that refuses correctly is working; a model in which refusal is a failure cannot say
  so.
- **evidenced like any determination.** A refusal that leaves no record is indistinguishable
  from a proposal never made.
- **not degradation.** There is no reduced form in which a refused proposal partly proceeds.
  Partial application after refusal is an ungoverned transition, because the state that results
  is not what the determination permitted (§8.4).

## 10. One schema, three subjects

The Conceptual Model names three activities. They are not three semantics. Each is the schema
of §4 applied to a different subject:

| Activity | `S` is | `π` is | `S′` is |
|---|---|---|---|
| **Transformation** | the baseline | a proposed change to the declarations | the next baseline |
| **Construction** | the authorized declarations | a candidate declaration | the authorized representation |
| **Execution** | the governed state under a snapshot | an interaction presented to the system | the governed state after it |

This is the model's central claim, and the four properties of §4 apply identically to all
three. Three consequences follow directly:

- **Transformation is not exempt.** Change to a governed system is itself a governed
  transition, determined under a closure, producing evidence. A system whose declarations may
  change by any path not of this shape is ungoverned with respect to its own governance,
  whatever its execution does.
- **Admission is a determination.** A candidate becomes part of a system by a determination
  admitting it — which is why presence never constitutes admission. Nothing is admitted by
  being found.
- **The activities compose without a fourth mechanism.** The governed representation resulting
  from one activity supplies the governed input to the next, along the authority chain the
  Conceptual Model specifies. The three results are not the same kind of object — a baseline, an
  authorized representation, and a governed execution state are distinct — so what holds
  between them is semantic continuity, not identity. No activity reaches past its successor,
  and no outer supervisor is needed to make the composition governed, because each link is
  governed by the same schema.

The activities differ in what they determine, never in how determination works:

```
transformation determines what the declarations are
construction   determines which declarations are authorized to be executed
execution      determines what occurs under those declarations
```

## 11. Genesis

The schema of §4 takes a governed state as its input. The first transition of a governed
system has no previously constituted baseline: its input is the **empty governed state** `∅`.
There is no prior closure from which governance could be inherited.

```
∅ ──────▶ the first baseline
```

This case — the constitution of a platform from nothing — is **not an exemption**, and the
model does not admit one. An ungoverned first transition would place the entire system on an
ungoverned foundation, and every later transition would inherit governance from a state that
was never determined. A system cannot be governed from an ungoverned origin.

**The empty governed state.** `∅` is the governed state in which nothing is declared and
nothing is governed. It is a legitimate governed state, not the absence of one.

**Reflexive determination.** In genesis, and only in genesis, part of the closure is supplied
by the proposal itself: the proposed baseline carries the governance that governs it. The
determination is to that extent reflexive — the proposed state is evaluated against the rules
it itself declares. A proposed baseline that violates its own governance is refused; a
baseline that cannot be evaluated against its own governance is a closure failure (§7.1) and
is refused for that reason.

The proposal supplies the subject's *declared governance*. It does not thereby supply the
external requirements against which genesis is admitted.

**The vacuity problem.** Reflexive determination alone is not sufficient, and the reason is
immediate: a baseline declaring no rules satisfies its own closure trivially. Self-consistency
is therefore necessary and not sufficient, and genesis requires a second condition the
proposal does not author.

**The claimed profile.** A genesis proposal MUST name the profile it claims. The profile is
not part of the proposal and is not authored by it: it states requirements the resulting
baseline must satisfy, supplied from outside the system being constituted. Genesis is admitted
when the proposed baseline is consistent with the governance it declares **and** satisfies the
profile it claims. The first condition prevents a system from contradicting itself; the second
prevents it from governing itself vacuously.

**The genesis closure.** The two sources compose into one closure, so that genesis uses the
same determination schema as every other transition:

```
C_gen(π, P) = C_π ⊕ P        C_π  the governance declared within the proposal
                             P    the requirements of the claimed profile

Δ = determine(∅, π, C_gen(π, P))
```

Genesis is special only in *how `C` is established*, never in what determination is. Elsewhere
the closure is inherited from the governed system; here it is composed from the proposal's own
declared governance and the externally claimed profile. The composition is by dominance like
any other (§6), so the profile can refuse what the proposal's own governance would admit — and
that direction is the point of it.

A genesis transition is therefore a governed transition in the full sense of §8 — a closure
was established, its rules were evaluated, the determination is the dominant consequence, the
resulting state is what it permitted, and evidence establishes all of it. What distinguishes
genesis is only *where the closure comes from*: from the proposal and the claimed profile,
rather than from a predecessor state.

Every subsequent transition inherits its closure from the baseline. Genesis is the single
transition where that is impossible, and the single place where the model permits a closure to
originate with what it governs.

## 12. Determinism

The determination function is deterministic: for the same `(S, π, C)` it yields the same `Δ`.

This is a property of the model, not an ambition for an implementation. It follows from §5
(evaluation is total and effect-free) and §7 (the closure is determinate and bounded).

Its consequence reaches the resulting state through one further step, which the model states
rather than assumes: **the same determination, applied to the same governed state, permits the
same resulting state.** The state update is determined by the determination and the state it
applies to, and by nothing else. Given the same `(S, π, C)` a governed transition therefore
reaches the same `Δ` and the same `S′`.

Determinism constrains the determination and the resulting state. It does not require that the
evidence be identical between two executions of the same transition — evidence may carry
observational material that varies without any governed consequence varying (Conceptual Model,
*Determinism*). What is required is stated in §13.

## 13. Evidence in the model

Evidence is not a record kept about the model; it is a term of it. For a transition `τ`,
evidence `ε` is adequate when it is sufficient to establish:

- which closure applied;
- which rules that closure supplied;
- what each predicate yielded;
- what the dominant consequence was; and
- that `S′` is what that consequence permitted.

Evidence adequate by this definition supports the conformance relation of §14 without the
party checking it having observed the transition, held the state, or trusted the system that
produced it. Evidence that establishes the result but not the determination is inadequate: it
shows what happened and not that it was governed, and those are the two things §8 exists to
separate.

Which parts of evidence must be identical across executions, and which are observational, is
specified by the Evidence, Attestation & Provenance Standard. This document requires only
sufficiency for the five points above.

## 14. The conformance relation

At the semantic level, conformance is a relation between a transition and the governing
requirements applicable to it. This document defines that transition-level relation and
nothing beyond it: how the relation lifts to the other conformance subjects — an artifact, a
governed representation, an implementation, a system instance — is specified by the Conformance
Model, which owns conformance for the family.

A transition `τ` **conforms** when it is governed (§8) and its determination was the correct
determination — that is, when re-evaluating **the closure and rules recorded in its evidence**
yields the same dominant consequence that `τ` recorded.

The checker re-evaluates what the evidence carries. It does not rediscover the closure from a
live system or a current environment, and it MUST NOT: a closure rediscovered later may differ
from the one that applied, and a check against a closure that did not govern the transition
establishes nothing about the transition. This is why §13 requires evidence to carry the
closure and not merely the outcome.

Two things follow, and they are why conformance is checkable at all:

- **Conformance is decided over evidence, not over behavior.** A checking party re-derives the
  determination from `ε` and compares. It does not re-run the system, and it need not have
  access to it.
- **Conformance is a property of transitions, and of systems only through them.** A system
  conforms with respect to a set of transitions when each of them conforms. A claim about a
  system that names no transitions and no evidence is not a conformance claim.

Non-conformance has exactly two forms, and they are not interchangeable:

| Form | What happened | What it indicates |
|---|---|---|
| **Ungoverned transition** | the transition fails one or more constitutive conditions of §8 — no determination, an unestablished or partial closure, incomplete evaluation, a resulting state the determination did not permit, or inadequate evidence | the mechanism is wrong |
| **Incorrect determination** | the determination was made and is not what the closure yields | a rule, or its evaluation, is wrong |

The first cannot be repaired by specifying a rule; the second cannot be repaired by adding
enforcement. A conformance regime that reports them as one defect misdirects every remedy.

## 15. What this model omits

The omissions are deliberate, and a document that fills one of them here is out of scope
rather than helpful:

- **Time.** The model orders determinations relative to the transitions they govern and says
  nothing about duration, concurrency, or when a determination occurs in wall-clock terms.
- **Distribution.** `S`, `C`, and the determination are semantic objects. Whether they are
  co-located, replicated, or partitioned is not a semantic question.
- **Artifact kinds.** Nothing here depends on what kinds of declaration exist. The model is the
  reason kinds can be added without the meaning of "governed" changing.
- **Representation.** No encoding, schema, or format is implied by any term above.
- **Rule expression.** How a predicate is written, and in what language, is unconstrained. The
  model requires only that evaluation be total and effect-free.

## 16. Normative invariants

- **SM-1.** Every change to governed state MUST be a governed transition (§4).
- **SM-2.** A determination MUST complete before the transition it governs occurs.
- **SM-3.** A determination MUST be reached over the complete rule set the closure supplies;
  a partial evaluation MUST NOT yield a determination.
- **SM-4.** Where a closure cannot be established, the determination MUST be `refuse` (§7.1).
- **SM-5.** Consequences MUST compose by dominance, and no rule may admit what another refuses
  (§6).
- **SM-5a.** Where several applicable rules constrain, their constraints MUST compose by
  conjunction: a proposal satisfies the composed constraint only where it satisfies every
  constituent constraint (§6).
- **SM-6.** Predicate evaluation MUST NOT alter governed state.
- **SM-7.** A refused proposal MUST NOT partly proceed (§9).
- **SM-7a.** An admitted transition MUST NOT come to rest having applied part of what its
  determination permits; where a realization can apply a transition partly, it MUST determine what
  state results (§8).
- **SM-7b.** A closure MUST be established for the state the transition applies to (§8).
- **SM-8.** Every determination MUST produce evidence adequate by §13.
- **SM-9.** Transformation of the declarations MUST itself be a governed transition (§10).
- **SM-10.** The same `(S, π, C)` MUST yield the same determination, and the same determination
  applied to the same governed state MUST permit the same resulting state (§12).
- **SM-11.** A genesis transition MUST be determined reflexively against the closure its
  proposal declares, MUST additionally satisfy the profile it claims, and MUST NOT be exempt
  from §8 (§11).
- **SM-12.** Conformance checking MUST re-evaluate the closure and rules recorded in evidence,
  and MUST NOT rediscover a closure from a live system or current environment (§14).

## 17. Conformance

This document states the semantic requirements against which conformance is evaluated. It does
not define conformance subjects, claims, levels, or demonstration procedures: those belong to
the Conformance Model and the Conformance Test Specification, and this document deliberately
establishes no second account of them.

What it does specify is what a **semantics** must satisfy to be an account of governed computation
under this model — whether that account is given by another document of this family or
realized by an implementation:

- every change of governed state it describes has the shape of §4;
- every change it treats as governed satisfies all five conditions of §8;
- it gives `refuse` the standing of §9, and does not treat refusal as failure;
- it composes consequences by dominance and resolves an unestablishable closure to `refuse`;
- it produces evidence adequate by §13 for every determination it describes;
- it constitutes an initial state only as §11 permits; and
- it introduces no mechanism by which governed state changes outside a governed transition.

How satisfaction of these requirements is claimed, levelled, and demonstrated is not this
document's business.
