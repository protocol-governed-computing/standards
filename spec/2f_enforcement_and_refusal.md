# Enforcement & Refusal

## 1. Scope

This document specifies how a declared obligation becomes an **enforceable** one. It also specifies
what a governed system observably does when it evaluates governance.

The Governance Standard states what governance says. Governance Closure & Authority establishes
which governance applies to a subject. This document covers what happens next:

- how an obligation is rendered evaluable;
- what obliges a system to evaluate it;
- what a refusal must establish;
- what separates enforcement from watching.

This document specifies **observable enforcement behavior**. It does not prescribe an enforcement
mechanism, a stage at which enforcement occurs, or a form for writing assertions. It does not define
conformance. A system may enforce its governance perfectly and still fail to conform. A system may
also conform in every respect this family requires while enforcing poorly chosen obligations.

This document introduces the terms **assertion**, **coverage**, and **vacuous enforcement**. The
Conceptual Model, the Semantic Model, the Governance Standard or Governance Closure & Authority
defines every other term it uses.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. From obligation to enforcement

An obligation passes through three steps before it constrains anything:

```
obligation      what a governing element requires of a subject      declared
    │  rendered as
assertion       the evaluable form of that obligation               derived
    │  supplied by the closure, evaluated at a determination
rule            predicate and consequence over (S, π)               evaluated
```

Each step can fail on its own, and each failure produces a system that looks governed:

- An obligation **never rendered** as an assertion is an intention. It constrains nothing, and
  nothing reports that it constrains nothing.
- An assertion **that no applicable closure can supply** is unreachable. It is correct and
  evaluable, but it is never evaluated.
- An assertion **that cannot refuse** is vacuous. The system evaluates it every time, and it can do
  nothing (§4.2).

**Enforcement is the whole chain, not the last step.** A system that diligently evaluates what was
never derived enforces nothing. The diligence is what makes the failure hard to see.

## 3. Assertions

An **assertion** is the evaluable form of an obligation: a predicate over a governed state and a
proposal, together with the consequence that follows from what it yields.

### 3.1 Derivation

An assertion is **derived** from the obligation it enforces (Governance Semantic Ontology §6,
*derived*). Derivation carries three requirements:

- **An assertion MUST identify the obligation it enforces.** Suppose nobody can establish an
  assertion's source obligation. The system then applies a rule for no declared reason. To any later
  reader, that looks the same as a mechanism's behavior.
- **An assertion MUST NOT impose a normative consequence beyond its obligation.** It may refuse only
  what the obligation prohibits or fails to require. An assertion that refuses more has amended the
  governance it should enforce, and that amendment was not a governed transition. This rule bounds
  the assertion's *consequence*, not its input domain. An assertion may be evaluable over a wider
  space than the cases its obligation reaches. It may also be reused across several obligations. In
  each case it may refuse only what that obligation makes refusable.
- **An assertion MUST NOT be a source of authority.** It is derived, and derived elements do not gain
  authority by being computed (GO-9). The obligation governs. The assertion is how a system checks
  it.

### 3.2 The assertion is not the obligation

The obligation states what must hold. The assertion states how a particular kind of determination
decides whether it holds. Several assertions may enforce one obligation, at different activities or
over different subjects. They all enforce the same obligation.

The distinction matters when the two disagree. **Where an assertion and its obligation differ, the
obligation governs and the assertion is defective.** Repairing the assertion is a correction.
Altering the obligation to match the assertion is a governed transition. A system that treats the
second as the first lets governance come to mean whatever the checks happen to check.

## 4. Coverage

**Coverage** is the relation between the obligations in force and the assertions that enforce them.

An invariant is an obligation required to hold at all times, not at one moment or along one path
(Conceptual Model, *invariant*). So an invariant enforced only where some assertion happens to exist
is not an invariant of the system. It is a property of that assertion's reach alone.

### 4.1 The enforcement obligation

**An obligation is in force only if some assertion can refuse its violation, however plainly the
obligation is written.**

This failure mode most reliably produces a system that people believe is governed and that is not.
The obligation is present, quotable and reviewed. Nothing evaluates it. No determination ever reports
its absence, because an assertion cannot detect a missing assertion.

Consequently:

- **Every obligation in force MUST have coverage.** Coverage means at least one assertion capable of
  refusing the obligation's violation. Every applicable closure supplies that assertion at every
  determination where it supplies the obligation. Coverage requires the obligation to be evaluable
  wherever it applies. It does not require a separate assertion for each closure.
- **An obligation without coverage MUST be a finding.** A system determines and reports it. It does
  not tolerate it as a weaker form of governance.
- **Declaring an obligation and declaring its enforcement are one act, not two.** A system that
  admits the first without the second has admitted an intention.

### 4.2 Vacuous enforcement

An assertion is **vacuous** when its predicate has no admissible input for which its determined
consequence is `refuse`.

Vacuity is a property of the assertion, not of what its closure happens to present. Suppose an
assertion *could* refuse some admissible state. It is not vacuous merely because no current subject
reaches that state. Suppose instead it could refuse nothing. A closure that exercises it often does
not rescue it.

Vacuous enforcement is worse than absent enforcement, because it produces evidence. Every
determination records the assertion as evaluated and satisfied. Coverage looks complete. Yet the
obligation is no more in force than if nobody had written it.

- **An assertion MUST be capable of refusing.** An assertion for which no admissible input yields
  refusal MUST be a finding.
- **Capability of refusal is a property of the assertion, not of its history.** An assertion that has
  never refused may still be able to. An assertion that has refused may still fail to cover the
  obligation. Neither observation substitutes for a predicate that is able to fail.

## 5. When enforcement occurs

**A system enforces an obligation at every determination whose closure supplies it.** This document
specifies no stage, no phase and no moment.

- A system MAY enforce the same obligation at more than one activity. It enforces an obligation about
  what may exist when it determines existence. It enforces an obligation about what may occur when it
  determines occurrence. It enforces an obligation about both at both.
- **Enforcement MUST complete before the effect it governs** (AI-4). This is the only timing
  requirement. It is an ordering, not a schedule.
- An obligation may apply at more than one determination. Enforcing it at an earlier determination
  **does not discharge it at a later one**. A later determination may skip it only where the
  obligation does not apply to that determination. An earlier evaluation is never a reason to skip
  it. The earlier determination governed a different subject, and its result says nothing about this
  one.

## 6. Refusal

Refusal is the determined response to a proposal that governance does not permit. Semantic Model §9
specifies its semantics: a transition to a state in which the proposal was refused, with evidence.
This section specifies what a refusing system must observably do.

### 6.1 What a refusal must establish

A refusal MUST establish, to a party that did not observe it:

- **what was proposed**;
- **what refused it**: the obligation, and the assertion that evaluated it;
- **under what closure**, and by what authority that obligation applied;
- **that nothing proceeded** (§6.3).

A refusal that reports only that something failed has recorded an event, not a determination. The
difference is whether a party can check the refusal or must believe it.

**Calling something a refusal does not make it one.** A capability may declare an outcome named
`refused`. A boundary may declare a result class named for denial. A report may use the word. None
of these is a refusal in this document's sense unless it establishes the four things above. In
particular it must establish *that nothing proceeded*, and a routed outcome by definition does not
(Execution Model §4.4, EX-16). The converse holds too: a refusal MUST NOT be delivered as a value the
system then acts on, because acting on it is proceeding.

### 6.2 Two causes, never merged

Every refusal has exactly one of two causes, and they MUST be distinguishable:

| Cause | What happened | Repaired by |
|---|---|---|
| **Rule refusal** | the closure was established, its rules were evaluated, and the dominant consequence was `refuse` | changing what was proposed |
| **Closure failure** | the closure could not be established, so no rule was evaluated (SM-4, CA-12) | declaring what was missing |

The two produce the same consequence and mean opposite things. A rule refusal says the system worked
and did not permit the proposal. A closure failure says the system could not determine what governs.
It would have said so whatever was proposed.

**A system that reports them alike misdirects every remedy it prompts.** It sends an author to change
a proposal that was never the problem. Or it sends the author to declare governance that was already
present and already refused them.

### 6.3 Refusal is total

A refused proposal does not partly proceed (AI-8, SM-7). There is no reduced form, no best-effort
application, and no partial write kept because it had already happened.

- **No degraded mode.** A system that continues in a reduced form after refusal has substituted its
  own judgment for the determination.
- **No warning-only obligation.** An obligation whose violation produces a report and no refusal is
  not an obligation. If a report was the intent, it should be declared as a non-governing
  observation, and nothing should call it governance.
- **No override.** A mechanism that can set a refusal aside makes governance optional. The
  mechanism's existence is the defect, not its use.

## 7. Enforcement is not detection

**Enforcement precedes the effect it governs. Detection follows it.**

Both may be valuable, and they are not interchangeable:

| | Occurs | Result | Establishes |
|---|---|---|---|
| **Enforcement** | before the effect | the effect does not occur | the transition was governed |
| **Detection** | after the effect | the effect is reported | the transition happened |

A detection mechanism added after the fact reports breaches. It does not make the breached
transitions governed. Remediation restores conformance for future transitions only (AI-10,
Architectural Invariants §10). A system whose governance is entirely detective records what it
failed to prevent.

This is not an argument against detection. It requires that a system not count detection as
coverage (§4.1). An obligation that a system watches but cannot enforce has no coverage. The
watching is what hides that.

## 8. Evidence of enforcement

Every determination produces evidence adequate to establish what was evaluated and what resulted
(SM-8, AI-14). Three consequences are specific to enforcement:

- **Refusals are evidenced as fully as admissions.** A system that records what it permitted and not
  what it refused has no record of its governance at work. It has a record only of its work
  proceeding.
- **Evidence records the obligation, not only the outcome.** The evidence must carry which obligation
  applied and which assertion evaluated it (Semantic Model §13). Nobody can re-derive a
  determination from an outcome alone.
- **Evidence of enforcement is not an input to enforcement** (AI-15). No determination consults the
  record of earlier determinations to decide the present one. A system that enforces more leniently
  because it refused recently has made its history its governance.

## 9. What this document does not specify

- **How an assertion is expressed.** Any form is admissible in which a predicate is total and
  effect-free (Semantic Model §5). No language, notation or evaluation strategy is required.
- **What mechanism enforces.** One mechanism or many, at one activity or several. The requirement is
  that the system evaluate the obligation wherever its closure supplies it.
- **Whether an implementation conforms.** Enforcement is what a governed system does. Conformance is
  a judgment about a system, made against evidence, and it belongs to the Conformance Model. A
  perfectly enforcing system whose obligations were badly chosen enforces exactly what it was told.

## 10. Normative invariants

- **EN-1.** An obligation MUST be rendered as at least one assertion capable of refusing its
  violation. An obligation without such coverage MUST be a finding (§4.1).
- **EN-2.** An assertion MUST identify the obligation it enforces (§3.1).
- **EN-3.** An assertion MUST NOT impose a normative consequence beyond its obligation, and MUST NOT
  be a source of authority (§3.1).
- **EN-4.** Where an assertion and its obligation differ, the obligation MUST govern (§3.2).
- **EN-5.** An assertion whose predicate has no admissible input yielding `refuse` MUST be a finding
  (§4.2).
- **EN-6.** An obligation MUST be evaluated at every determination whose closure supplies it (§5).
- **EN-7.** Enforcement MUST complete before the effect it governs (§5, AI-4).
- **EN-8.** A refusal MUST establish what was proposed, what refused it, under what closure and
  authority, and that nothing proceeded (§6.1).
- **EN-9.** Rule refusal and closure failure MUST be distinguishable in the determination and in its
  evidence (§6.2, CA-12).
- **EN-10.** A refused proposal MUST NOT partly proceed, and no mechanism MUST exist by which a
  refusal is set aside (§6.3).
- **EN-11.** An obligation whose violation produces only a report MUST NOT be declared as governance
  (§6.3).
- **EN-12.** Refusals MUST be evidenced as fully as admissions (§8).
- **EN-13.** Evidence MUST NOT be an input to a determination (§8, AI-15).
- **EN-14.** A determination MUST NOT be reported as a refusal unless it establishes what §6.1
  requires. A refusal MUST NOT be delivered as a value that is acted on (§6.1).

## 11. Conformance

The conformance subject of this document is an **enforcement arrangement**: the assertions of a
governed system, their derivation from obligations, and the behavior the system shows when it
evaluates those assertions.

An enforcement arrangement conforms when all of the following hold:

- Every obligation in force has coverage, and every gap is a determined finding (EN-1).
- Every assertion identifies its obligation, is bounded by it, and is capable of refusing (EN-2,
  EN-3, EN-5).
- The system evaluates obligations wherever their closures supply them, before the effects they
  govern (EN-6, EN-7).
- Refusals establish their grounds, distinguish their cause, are total, and are evidenced (EN-8 …
  EN-12).
- No path exists by which a refusal is overridden or an obligation reduced to a warning (EN-10,
  EN-11).

**Two demonstrations deserve naming, because an absence of refusals does not show a conforming
arrangement.** A system that has never refused shows nothing. That record fits a system where
nothing violated its governance. It fits equally a system where nothing could. Enforcement is shown
by two things: each assertion *can* refuse, and when it refuses, the system establishes why. The
Conformance Test Specification owns how those demonstrations are required and evaluated.
