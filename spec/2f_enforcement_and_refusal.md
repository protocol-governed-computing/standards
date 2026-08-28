# Enforcement & Refusal

## 1. Scope

This document specifies how a declared obligation becomes an **enforceable** one, and what a governed
system observably does when governance is evaluated.

The Governance Standard states what governance says. Governance Closure & Authority establishes
which governance applies to a subject. This document covers what happens next: how an obligation is
rendered evaluable, what obliges a system to evaluate it, what a refusal must establish, and what
distinguishes enforcement from watching.

It specifies **observable enforcement behavior**. It does not prescribe an enforcement mechanism, a
stage at which enforcement occurs, or a form in which assertions are written. It does not define
conformance: a system may enforce its governance perfectly and fail to conform, and may conform in
every respect this family requires while enforcing obligations that were poorly chosen.

This document introduces the terms **assertion**, **coverage**, and **vacuous enforcement**. Every
other term it uses is defined by the Conceptual Model, the Semantic Model, the Governance
Standard, or Governance Closure & Authority.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. From obligation to enforcement

An obligation travels three steps before it constrains anything:

```
obligation      what a governing element requires of a subject      declared
    │  rendered as
assertion       the evaluable form of that obligation               derived
    │  supplied by the closure, evaluated at a determination
rule            predicate and consequence over (S, π)               evaluated
```

Each step can fail independently, and each failure produces a system that looks governed:

- an obligation **never rendered** as an assertion is an intention — it constrains nothing and
  nothing reports that it constrains nothing;
- an assertion **for which no applicable closure can supply it** is unreachable — correct,
  evaluable, and never evaluated;
- an assertion **that cannot refuse** is vacuous — evaluated every time, capable of nothing (§4.2).

**Enforcement is the whole chain, not the last step.** A system that evaluates diligently what was
never derived is enforcing nothing, and the diligence is what makes it hard to see.

## 3. Assertions

An **assertion** is the evaluable form of an obligation: a predicate over a governed state and a
proposal, together with the consequence that follows from what it yields.

### 3.1 Derivation

An assertion is **derived** from the obligation it enforces (Governance Semantic Ontology §6,
*derived*), and derivation carries three requirements:

- **An assertion MUST identify the obligation it enforces.** An assertion whose source obligation
  cannot be established is a rule the system applies for no declared reason — which is
  indistinguishable, to any later reader, from a mechanism's behavior.
- **An assertion MUST NOT impose a normative consequence beyond its obligation.** It may refuse
  only what the obligation prohibits or fails to require. An assertion that refuses more has
  amended the governance it was supposed to enforce, without that amendment being a governed
  transition. This bounds the assertion's *consequence*, not its input domain: an assertion may
  be evaluable over a wider space than the cases its obligation reaches, and may be reused across
  several, provided it refuses only what that obligation makes refusable.
- **An assertion MUST NOT be a source of authority.** It is derived, and derived elements do not
  acquire authority by being computed (GO-9). What governs is the obligation; the assertion is how
  it is checked.

### 3.2 The assertion is not the obligation

The obligation states what must hold. The assertion states how that is determined at a particular
kind of determination. One obligation may be enforced by several assertions — at different
activities, over different subjects — and they are all the same obligation.

The distinction matters when they disagree. **Where an assertion and its obligation differ, the
obligation governs and the assertion is defective.** Repairing the assertion is a correction;
altering the obligation to match the assertion is a governed transition, and treating the second
as though it were the first is how governance comes to mean whatever the checks happen to check.

## 4. Coverage

**Coverage** is the relation between the obligations in force and the assertions that enforce
them.

An invariant is an obligation required to hold at all times, rather than at one moment or along
one path (Conceptual Model, *invariant*). It follows that an invariant enforced only where some
assertion happens to exist is not an invariant of the system — it is a property of that
assertion's reach.

### 4.1 The enforcement obligation

**A declared obligation with no assertion capable of refusing its violation is not in force,
however plainly it is written.**

This is the failure mode that most reliably produces a system believed to be governed and not
governed. The obligation is present, quotable, and reviewed; nothing evaluates it; and no
determination ever reports its absence, because absence of an assertion is not something an
assertion can detect.

Consequently:

- **Every obligation in force MUST have coverage**: at least one assertion capable of refusing its
  violation, supplied by every applicable closure at every determination at which that closure
  supplies the obligation. Coverage is a requirement that the obligation be evaluable wherever it
  applies — not a requirement that a separate assertion be instantiated per closure.
- **An obligation without coverage MUST be a finding**, determined and reported — not tolerated as
  a weaker form of governance.
- **Declaring an obligation and declaring its enforcement are one act**, not two, and a system
  that admits the first without the second has admitted an intention.

### 4.2 Vacuous enforcement

An assertion is **vacuous** when its predicate has no admissible input for which its determined
consequence is `refuse`.

Vacuity is a property of the assertion, not of what its closure happens to present. An assertion
that *could* refuse some admissible state is not vacuous merely because no current subject reaches
that state, and one that could refuse nothing is not rescued by a closure that happens to exercise
it often.

Vacuous enforcement is worse than absent enforcement, because it produces evidence. Every
determination records the assertion evaluated and satisfied; coverage appears complete; and the
obligation is no more in force than if nothing had been written.

- **An assertion MUST be capable of refusing.** An assertion for which no admissible input yields
  refusal MUST be a finding.
- **Capability of refusal is a property of the assertion, not of its history.** That an assertion
  has never refused is not evidence that it cannot; that it has refused is not evidence that it
  covers the obligation. Neither observation substitutes for the predicate being able to fail.

## 5. When enforcement occurs

**An obligation is enforced at every determination whose closure supplies it** — and this document
specifies no stage, no phase, and no moment.

- The same obligation MAY be enforced at more than one activity. An obligation about what may
  exist is enforced when existence is determined; an obligation about what may occur is enforced
  when occurrence is determined; an obligation about both is enforced at both.
- **Enforcement MUST complete before the effect it governs** (AI-4). This is the only timing
  requirement, and it is an ordering rather than a schedule.
- Where an obligation applies at more than one determination, enforcing it at an earlier
  determination **does not discharge it at a later one**. A later determination need not evaluate
  it only where the obligation does not apply to that determination. That something else evaluated
  it earlier is never the reason to skip it: the earlier determination governed a different
  subject, and its result says nothing about this one.

## 6. Refusal

Refusal is the determined response to a proposal that governance does not permit. Its semantics —
a transition to a state in which the proposal was refused, with evidence — are specified by the
Semantic Model §9. This section specifies what a refusing system must observably do.

### 6.1 What a refusal must establish

A refusal MUST establish, to a party that did not observe it:

- **what was proposed**;
- **what refused it** — the obligation, and the assertion that evaluated it;
- **under what closure**, and by what authority that obligation applied;
- **that nothing proceeded** (§6.3).

A refusal that reports only that something failed has recorded an event, not a determination. The
difference is whether the refusal can be checked or must be believed.

**Nothing becomes a refusal by being called one.** A capability may declare an outcome named
`refused`, a boundary may declare a result class named for denial, and a report may use the word.
None of these is a refusal in this document's sense unless it establishes the four things above —
and in particular *that nothing proceeded*, which a routed outcome by definition does not (3a §4.4,
EX-16). The converse holds equally: a refusal MUST NOT be delivered as a value the system then acts
on, because acting on it is proceeding.

### 6.2 Two causes, never merged

Every refusal has exactly one of two causes, and they MUST be distinguishable:

| Cause | What happened | Repaired by |
|---|---|---|
| **Rule refusal** | the closure was established, its rules were evaluated, and the dominant consequence was `refuse` | changing what was proposed |
| **Closure failure** | the closure could not be established, so no rule was evaluated (SM-4, CA-12) | declaring what was missing |

They produce the same consequence and mean opposite things. A rule refusal says the system worked
and the proposal was not permitted. A closure failure says the system could not determine what
governs, and would have said so whatever was proposed.

**A system that reports them alike misdirects every remedy it prompts** — sending an author to
change a proposal that was never the problem, or to declare governance that was already present
and already refused them.

### 6.3 Refusal is total

A refused proposal does not partly proceed (AI-8, SM-7). There is no reduced form, no best-effort
application, no partial write retained because it had already happened.

- **No degraded mode.** A system that continues in a diminished form after refusal has substituted
  its own judgment for the determination.
- **No warning-only obligation.** An obligation whose violation produces a report and no refusal
  is not an obligation. If that is what was intended, it should be declared as a non-governing
  observation, and nothing should call it governance.
- **No override.** A mechanism by which a refusal can be set aside is a mechanism by which
  governance is optional, and its existence — not its use — is the defect.

## 7. Enforcement is not detection

**Enforcement precedes the effect it governs. Detection follows it.**

Both may be valuable and they are not interchangeable:

| | Occurs | Result | Establishes |
|---|---|---|---|
| **Enforcement** | before the effect | the effect does not occur | the transition was governed |
| **Detection** | after the effect | the effect is reported | the transition happened |

A detection mechanism added after the fact reports breaches; it does not make the breached
transitions governed, and remediation restores conformance for future transitions only (AI-10,
Architectural Invariants §10). A system whose governance is entirely detective is a system that
records what it failed to prevent.

This is not an argument against detection. It is a requirement that a system not count detection
as coverage (§4.1): an obligation watched but not enforceable has no coverage, and its watchfulness
is what conceals that.

## 8. Evidence of enforcement

Every determination produces evidence adequate to establish what was evaluated and what resulted
(SM-8, AI-14). Three consequences are specific to enforcement:

- **Refusals are evidenced as fully as admissions.** A system that records what it permitted and
  not what it refused has no record of its governance operating — only of its work proceeding.
- **Evidence records the obligation, not only the outcome.** Which obligation applied, and which
  assertion evaluated it, are part of what the evidence must carry (Semantic Model §13); an
  outcome alone cannot be re-derived.
- **Evidence of enforcement is not an input to enforcement** (AI-15). No determination consults
  the record of prior determinations to decide the present one. A system that enforces more
  leniently because it refused recently has made its history into its governance.

## 9. What this document does not specify

- **How an assertion is expressed.** Any form is admissible in which a predicate is total and
  effect-free (Semantic Model §5). No language, notation, or evaluation strategy is required.
- **What mechanism enforces.** One mechanism or many, at one activity or several. What is required
  is that the obligation be evaluated wherever its closure supplies it.
- **Whether an implementation conforms.** Enforcement is what a governed system does; conformance
  is a judgment about a system, made against evidence, and it belongs to the Conformance Model. A
  perfectly enforcing system whose obligations were badly chosen enforces exactly what it was
  told.

## 10. Normative invariants

- **EN-1.** An obligation MUST be rendered as at least one assertion capable of refusing its
  violation, and an obligation without such coverage MUST be a finding (§4.1).
- **EN-2.** An assertion MUST identify the obligation it enforces (§3.1).
- **EN-3.** An assertion MUST NOT impose a normative consequence beyond its obligation, and MUST
  NOT be a source of authority (§3.1).
- **EN-4.** Where an assertion and its obligation differ, the obligation MUST govern (§3.2).
- **EN-5.** An assertion whose predicate has no admissible input yielding `refuse` MUST be a
  finding (§4.2).
- **EN-6.** An obligation MUST be evaluated at every determination whose closure supplies it (§5).
- **EN-7.** Enforcement MUST complete before the effect it governs (§5, AI-4).
- **EN-8.** A refusal MUST establish what was proposed, what refused it, under what closure and
  authority, and that nothing proceeded (§6.1).
- **EN-9.** Rule refusal and closure failure MUST be distinguishable in the determination and in
  its evidence (§6.2, CA-12).
- **EN-10.** A refused proposal MUST NOT partly proceed, and no mechanism MUST exist by which a
  refusal is set aside (§6.3).
- **EN-11.** An obligation whose violation produces only a report MUST NOT be declared as
  governance (§6.3).
- **EN-12.** Refusals MUST be evidenced as fully as admissions (§8).
- **EN-13.** Evidence MUST NOT be an input to a determination (§8, AI-15).
- **EN-14.** A determination MUST NOT be reported as a refusal unless it establishes what §6.1
  requires, and a refusal MUST NOT be delivered as a value that is acted on (§6.1).

## 11. Conformance

The conformance subject of this document is an **enforcement arrangement**: the assertions of a
governed system, their derivation from obligations, and the behavior the system exhibits when
those assertions are evaluated.

An enforcement arrangement conforms when:

- every obligation in force has coverage, and every gap is a determined finding (EN-1);
- every assertion identifies its obligation, is bounded by it, and is capable of refusing
  (EN-2, EN-3, EN-5);
- obligations are evaluated wherever their closures supply them, before the effects they govern
  (EN-6, EN-7);
- refusals establish their grounds, distinguish their cause, are total, and are evidenced
  (EN-8 … EN-12); and
- no path exists by which a refusal is overridden or an obligation reduced to a warning
  (EN-10, EN-11).

**Two demonstrations are worth naming, because a conforming arrangement is not shown by an absence
of refusals.** That a system has never refused shows nothing: it is equally consistent with
nothing violating its governance and with nothing being able to. What shows enforcement is that
each assertion *can* refuse, and that when refused, the system establishes why. How those
demonstrations are required and evaluated belongs to the Conformance Test Specification.
