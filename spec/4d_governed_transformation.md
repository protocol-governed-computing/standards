# Governed Transformation

## 1. Scope

This document specifies **governed transformation**: how a stated need becomes governed artifacts of
an existing system, under rules, with human judgement engaged where it is irreducible and nowhere
else.

It closes Part IV. Governed Construction determines whether candidate declarations may exist; this
document specifies where those candidates come from and under what governance they were produced.
**Transformation is itself a governed subject** (SM-9) — not a practice surrounding a governed system
and exempt from it.

It specifies a **semantic contract**, not a realization. Phase names, register shapes, rule
identifiers, and artifact kinds are free to vary. Nothing here requires a particular pipeline,
tooling, or number of steps.

This document introduces the terms **dossier**, **phase**, **register**, **check kind**, **verdict**,
**gate**, **worker**, **rung**, **grounding**, **sufficiency**, and **realization**. Every other term
it uses is defined by the Conceptual Model, the Semantic Model, or Parts II–IV.

### 1.1 Three terms that differ from earlier usage

Where earlier working material used a term this family has since defined otherwise, this document
uses the family's term:

| Earlier usage | Here | Because |
|---|---|---|
| *determination* — a design fixing an artifact completely | **sufficiency** | *determination* is the Semantic Model's term for the result of evaluating a closure |
| *composition* — the governed system being changed | **baseline**, or *governed system* | *composition* is the Conceptual Model's term for combining separately owned parts |
| *projection* — a phase determined by its prior | **projection**, unchanged | it is a projection in the Projection Standard's sense: a deterministic derivation from a defined source |

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Transformation as a governed transition

Transformation is the transition schema of the Semantic Model applied to one subject:

| | In transformation |
|---|---|
| `S` | the baseline — what the system currently is |
| `π` | a stated need, together with the human answers it requires |
| `C` | the governance applicable to changing this system |
| `S′` | the next baseline |
| `ε` | the dossier and the record of what was determined at each phase |

**A system whose baseline did not change did not change.** Transformation takes an existing baseline
as input and produces the next one; it is not authoring beside a system (Conceptual Model,
*transformation*).

## 3. Five separations

This model exists to keep five things distinct that are routinely blended:

```
what is decided  ≠  who decides it  ≠  what makes a design sufficient  ≠  what proves it works
                      and, orthogonal to all four:   may it proceed  ≠  how good it is
```

- **Decisions** are recorded in registers and judged by declared rules.
- **Deciders** are human where judgement is irreducible; a worker may draft, never decide.
- **Sufficiency** is the property that a design states every fact realization requires — measured,
  never assumed.
- **Proof** is execution against real state. Document admissibility is not proof.

**A realization that collapses any two of these is non-conforming**, and each collapse has a
signature: collapsing the first two produces a pipeline that invents business content; the second
two, a pipeline that reports success over a system that does nothing; the last pair, a quality score
that has quietly become a second gate.

## 4. The sequence

A transformation is a set of **phases** ordered by what each depends on. Each reads what precedes it,
emits what it declares it emits, and is judged. What the phases emit, together with the record of
what was determined at each, is the **dossier**.

The order is a dependency order, not necessarily a line: two phases neither of which reads the other
may be produced in either order or at once. The diagram below is the common case, not the required
shape.

```
need → P₀ → P₁ → … → Pₙ → sufficiency → realization → execution
       └─ rule set per phase ─┘   └ measured ┘        └ proves ┘
```

- **A dossier is evidence, never a member of the governed system.** It records how a change was
  arrived at; it is not admitted, not executed, and not part of any baseline.
- **Phases hand off explicitly.** A phase declares what it emits and what the phases depending on it
  consume. An unchecked handoff is indistinguishable from a preserved one, so **absence MUST be
  reported rather than pass silently**.
- **Phases differ in kind.** Some decide; some only restate. A phase that decides nothing is a
  projection (§9) and MUST NOT be authored by hand.
- The sequence is validated against a baseline (§10), never against "the current system".

## 5. Registers and rules

A phase document is **registers** — each named, with a declared field set — not prose. Whether a
register is realized as a table, as typed records, or as any other representation is not specified
here; what is required is that its fields are declared and that content is addressed by them.

- Governed content MUST live in registers. Prose in a phase document is commentary and MUST NOT
  carry governed content.
- **A rule MUST be declared as data** — its identity, the register it governs, the **check kind**
  that evaluates it, and its parameters — and MUST NOT be expressed as procedure. Adding a governed
  rule MUST NOT require a new mechanism, and a new mechanism MUST NOT carry a rule's intent.
- A **check kind** is a mechanism: *is this field empty*, *does this identity exist in the baseline*.
  It carries no policy and knows nothing of why it matters.
- **The set of check kinds MUST be closed**, and an unknown check kind MUST fail hard. A silently
  skipped rule reports green over an unevaluated subject.
- **Every declared rule MUST be evaluated**; there MUST be no short-circuiting on first failure.
- **Every declared rule MUST be demonstrated capable of refusing.** A rule set is not evidence that
  its rules can fail (EN-5).
- A **verdict** — the determination reached by applying a phase's rule set to its document — MUST
  name, for each finding, the rule and the location, where a **location** identifies the register,
  the entry, and the field the finding concerns. A count is not a verdict.

A realization SHOULD derive structural rules from the phase's own document declaration rather than
restating them, so that a document's shape has one declaration and not two that can disagree.

**Registers, rules, and check kinds are declaration elements, not artifacts** (2c §7.1). They are
governed because the phase document carrying them is governed, they are closed because its surface
is closed, and **they require no artifact kind of their own.** A profile that closes a kind
vocabulary is not obliged to admit a kind for a rule or a register, and one that does has begun
classifying fields rather than representations. What a profile decides here is the sufficiency
criterion (§13) — not a taxonomy of the machinery that evaluates it.

The **check kind** is named a kind and is not one: it is a mechanism identifier within a closed set
declared here, unrelated to the artifact kinds the Kind Vocabulary admits. The two never appear in
one registry.

### 5.1 A rule set is not evidence that its rules can fail

A rule may be unable to refuse anything, and **register rules fail this way in forms no reading of
the rule reveals**:

- a rule whose parameters name a field the register does not declare **reads every value as empty and
  reports clean**;
- a check that resolves a field name by prefix is satisfied by a longer sibling, so **a register can
  lose a field and report clean**.

Both failures are silent, both leave a rule set reporting green over an unevaluated subject, and
neither is reachable by inspecting the rule. What a realization must do is therefore **demonstrate
refusal, not declare intent**: for each declared rule, exhibit a document the rule refuses.

This is the transformation-side form of the vacuity rule (2f §4.2). It is stated separately because
the failure modes are specific to rules over registers, and because a rule that cannot fire is
indistinguishable from a subject that never violated it.

## 6. Declared fields

- A field constrained to a set of values MUST declare that set **as part of the register's own
  declaration**. A vocabulary held apart from the declaration it constrains is a second declaration
  that can disagree with the first.
- **A register's entries MUST be individually addressable.** A determination about one entry MUST be
  able to name that entry and no other. How an entry is addressed — by declared key, by position, or
  otherwise — is not specified; that it is addressable at all is what makes a finding reportable
  rather than merely counted.
- **Emptiness MUST be declared, never inferred.** A register with nothing in it MUST say so. A
  register nobody filled in and a register whose author considered it and found nothing are
  otherwise indistinguishable, and only one of them is an answer.
- A register MAY be optional. **Optional means *may be empty*. It does not mean *may be absent*, and
  it never means *may be unconsidered*.**

## 7. The purity ladder

A transformation moves from business language to bound identity, and the **rungs** MUST be kept
apart.

- Each register MUST declare its rung.
- **A register at a business rung MUST NOT name a constructed artifact identity.** Naming one is
  design leaking into a phase that has not reached design.
- Where a rung cites evidence from the baseline, the citation MUST occupy a field declared for it,
  never the content field itself. The business meaning and the identity grounding it are two facts, and
  merging them makes the first uncheckable.
- A capability MAY be named before it is identified. Where a realization does this, the provisional
  name and the identity later bound to it MUST be reconciled **in both directions** (§9).

This is the separation of behavior from implementation applied *within* the transformation, not only
to its output. A realization that lets a business register name an implementation has no rung left
to protect.

## 8. Admissibility is not quality

Where a realization scores documents:

- **Whether a document may proceed MUST be decided by its rule set and by nothing else.**
- **A quality score MUST NOT gate.** An admissible document MAY score poorly — carrying declared open
  questions is the ordinary reason — and an inadmissible one MAY score well.
- What is scored MUST be declared, and declared where the governance lives rather than inside a
  tool.
- **A value that admission refuses MUST NOT also be scored.** The document is already refused;
  scoring it again counts one defect twice, and a reader comparing two documents sees a gap
  measuring how many ways the same fact was counted. It follows that when a rule begins refusing a
  value, the scoring term for that value is removed in the same change.

## 9. Human engagement

Human judgement is engaged exactly where it is irreducible, and this model makes that boundary
explicit rather than cultural.

### 9.1 Questions are asked, never guessed

- A phase that cannot determine a value MUST record it as an **open question against a named
  owner**. It MUST NOT fill it in, and MUST NOT hedge it with a placeholder — a field stating that
  the question is unanswered reads as decided to every later phase.
- **An unresolved blocking question MUST make its document inadmissible.** Otherwise the next phase
  answers it by invention.

### 9.2 Preservation is bidirectional

- Human semantic content enters **exactly once**. A later phase MUST preserve it, reference it, or
  supersede it while declaring that it has done so. Silent replacement MUST be refused. This applies
  to narrative content no register can derive as much as to rows.
- A phase MUST NOT drop what its prior committed to, **and MUST NOT state what its prior does not.**
  Only the first is usually checked — and **a fabricated fact walks through a pipeline that checks
  only for loss.**

### 9.3 Gates

A **gate** is a point at which a person accepts a phase's document. **A gate is not a verdict**: a
document may be admissible and still not accepted.

- Gates MUST be declared, and a phase MUST NOT pass one implicitly.
- A document SHOULD carry the lifecycle state it has reached, from a declared vocabulary, so that
  *admissible* and *accepted* are never read as one claim.

### 9.4 A worker may draft; it MUST NOT decide

A **worker** is whatever produces a phase document — a person, an interactive assistant, a
programmatic model.

- Whether a document is admissible is the rule set's answer. Whether a business question is answered
  is the human's.
- **A human answer MUST be recorded as declared register content**, addressed by the field of the
  register the question was opened against (§5, §9.1). An answer given in conversation and not
  landed in a register has not been given: it is not addressable, not preserved, and not comparable.
- **Given the same human answers, any worker MUST yield the same admissible registers**, and
  therefore the same artifacts. Prose wording may differ; nothing governed may.

**"The same human answers" means the same declared field values, and nothing looser.** Stated over
free prose the obligation could not be checked — two answers meaning the same thing in different
words would be indistinguishable from two different answers, and an obligation nothing can refuse is
not in force (EN-1). Stated over declared fields it is decidable by comparison, and the
demonstration TR-13 requires is running two workers against one recorded answer set and comparing
registers.

This is the same line §5 draws for everything else the transformation governs: governed content
lives in registers, and prose is commentary. **A human answer is governed content.**

This is what makes workers interchangeable, and it is the transformation-side form of the family's
standing rule: a realization may derive knowledge and may not assign significance (GC-8).

## 10. Projected phases

If, after everything above, a phase's content is **uniquely determined by its prior**, that phase
MUST be produced mechanically and MUST NOT be hand-authored.

Such a phase is a projection in the Projection Standard's sense — a deterministic derivation from a
defined source — and everything that document requires of a projection holds of it, including
faithfulness and regenerability.

- A realization declaring a projected phase MUST declare **where a question discovered while
  producing it goes**: back to the phase that owns it, to be projected again. It MUST NOT enter at
  the projected phase.
- **A projection MUST refuse to run against an inadmissible prior**, or it launders an open question
  into a document that reads as settled.
- **A projected phase's rules govern amendment, not authorship.** A projection cannot fail the rules
  that check what it was built from, so a realization MUST NOT read a projected document's verdict
  as evidence about the change.

## 11. Baseline and grounding

- Every transformation MUST be validated against a **named, frozen baseline**, identified by content
  and not by location (SN-2). Validating against "whatever is current" makes a regression
  indistinguishable from a rebuild.
- **A transformation MUST NOT be judged against a baseline that already contains its own output.**
  Every identity it assigns would collide with itself.
- Re-baselining MUST be a deliberate, recorded act.

### 11.1 Grounding

A claim about what the system already provides MUST be **grounded** — read from the baseline through
a declared inspection interface — and MUST NOT be asserted.

Three things MUST be kept in separate registers, because two of the three failures are silent:

| | Authoritative | Resolved by |
|---|---|---|
| a business truth | the human | taken as given |
| a belief about what exists | nobody yet | grounding against the baseline |
| an open question | nobody | asking the named owner |

**A belief recorded as a truth is never verified; a question recorded as a truth is answered by
invention.**

### 11.2 Grounding must answer about a named thing

**The inspection interface MUST be able to answer about a named artifact, not only to enumerate.**

A rule that must compare a design against what one existing artifact currently declares cannot be
written at all if grounding produces only inventories. A realization whose grounding is
enumeration-only will find whole classes of rule inexpressible at design time, and those rules will
migrate to later, weaker checks — **which is a limitation of the interface, not of the rule.**

### 11.3 Evolution is never greenfield

A transformation's distinguishing logic — reuse against authoring, placement, preservation — is
meaningful only against a baseline. **A realization that validates only greenfield runs leaves all of
it unexercised while reporting success.**

Exactly one transformation legitimately has no baseline, and it is the first (§13). Every
transformation after it has one, and validating any of them as though it were the first exercises
none of the logic that makes transformation *transformation*.

## 12. The first transformation

Every requirement above presumes a baseline. **The first transformation of a system has none** — it
proceeds from the empty governed state to the first baseline (Semantic Model §11).

This is not an exemption, and a realization MUST NOT treat it as one. What differs is precisely and
only what a baseline would have supplied.

### 12.1 What differs

| | Ordinarily | At genesis |
|---|---|---|
| the input `S` | the baseline | the empty governed state |
| grounding reads from | the baseline | nothing — there is nothing to read |
| the closure judging it | the governance already in force | the proposal's own declared governance composed with the profile it claims |

### 12.2 What does not differ

Everything else holds unchanged. The phases are judged by declared rules; questions are asked rather
than guessed; human content enters once and is preserved in both directions; gates are declared;
sufficiency is measured before realization; the result is proved by execution against real state.

**A first transformation is judged more, not less.** Where a later transformation can ground a claim
against a baseline, this one cannot — so every claim it makes about what exists is a claim it must
carry the burden of, and there is no prior state whose survival would signal a mistake.

### 12.3 Emptiness is declared, not skipped

Grounding registers are not omitted at genesis; **they are declared empty** (§6). A register nobody
filled and a register whose author established there was nothing to find are otherwise
indistinguishable, and at genesis every grounding register is legitimately the second — which is
exactly the condition under which the first is easiest to mistake for it.

### 12.4 The claimed profile stands in for the baseline

A genesis transformation MUST name the profile it claims, and that profile MUST NOT be authored by
the transformation claiming it (SN-7).

This is what keeps the first transformation from being self-certifying. Ordinarily a transformation
is judged against governance already in force and against a baseline it did not write; at genesis
both are absent, and the claimed profile is the only thing left that the transformation did not
author. **Without it, a first transformation would declare its own rules, satisfy them, and be — by
its own account — perfectly governed.**

### 12.5 Once

**Only the first transformation of a system may proceed without a baseline.** Every subsequent one
has one, and MUST be validated against it (TR-15).

A later transformation MUST NOT claim genesis — not for a new domain, not for a new region, not for
a subsystem introduced whole, not because a baseline is inconvenient to obtain. After genesis,
nothing constitutes itself (AI-17), and a transformation asserting otherwise is proposing to
introduce governance that nothing in force admitted.

## 13. Sufficiency and realization

Design and realization fail differently, and a realization MUST keep them apart:

| Failure | Statement | Repaired by |
|---|---|---|
| **design** | the register is incomplete or contradictory | re-authoring a register |
| **sufficiency** | the design is valid and does not fix an artifact | amending the design language |

- **Sufficiency MUST be determined before realization, and realization MUST refuse a design that
  does not fix every fact the realization needs.** **A generator that supplies a fact the design
  omits is a second, ungoverned design authority.** How sufficiency is determined is unconstrained:
  a proportion of required facts against a declared threshold, and a per-artifact test that refuses
  on the first artifact the design does not fix, discharge this equally. What is required is that
  the determination complete before anything is written.
- **A realized artifact MUST be a function of the design alone.** It MUST NOT be a function of the
  design and the current baseline, or the same dossier realizes differently against two baselines
  and sufficiency stops meaning anything.
- **Amending an existing artifact is a whole redeclaration, not a delta.** It follows that a design
  may state less than the artifact already holds, so a realization MUST compare an amendment against
  what it replaces and **MUST refuse one that narrows it**.
- **The realization order MUST be a schedule, not a list.** It MUST cover everything it schedules
  without gaps, and MUST place everything an artifact depends on before that artifact. A gap is a
  dropped artifact and reads as an ordering choice. Whether artifacts that depend on each other not
  at all are ordered relative to one another is not specified.
- **Scheduling and amendment are different acts, and a realization MUST perform both.** An artifact
  that already exists cannot be scheduled for authoring, and if only scheduled artifacts are
  realized, amendments are silently not applied.
- Every artifact realized MUST trace to something the transformation asked for, **and everything
  asked for MUST be realized.** Both directions MUST be checked; only one usually is.

## 14. Proof

Document admissibility, sufficiency determined, and realization at zero differences are
**jointly insufficient** to establish that anything works.

**A transformation MUST NOT be considered complete until the system it produced has been executed
against real state and the stated acceptance criteria observed.**

- An acceptance criterion MUST assert **the state it claims**, never the status a call returned. A
  criterion satisfied by a success code over an operation that did the wrong thing is not satisfied.
- A criterion about **data** — that records written before a change remain usable — MUST be settled
  by operating on such a record. It is unresolvable from a sealed representation, which declares
  stores and never their contents.
- **A rule that passes because a value is absent has not passed.**
- **A refusal the business declared MUST be discharged by the design, and the discharge MUST be
  checked against what it does.** A design that states it has handled a refusal has stated something;
  whether the artifacts it fixes actually refuse is a different question, and only the second one is
  the discharge. This is §9.2's fabrication check applied to refusals: a pipeline that checks only
  that a discharge was declared admits one that declares it and does nothing.

## 15. What a host must provide

This document requires three capabilities of whatever hosts a transformation, and a realization MAY
satisfy them any way it chooses:

- **An addressable system** — artifacts with stable identities a baseline can name and a design can
  cite (ID-1).
- **An inspection interface** — a way to read facts about a baseline without reaching into the
  machinery that produced it (§11.2). Grounding through construction internals couples the
  transformation to a build mechanism and is non-conforming in substance if not in form.
- **A sealing mechanism** — where a rule set is judged inside the governed system as well as outside
  it, some way for it to exist there. Where a realization judges documents only outside the system,
  none is needed.

### 15.1 One rule set, two readers

Where a realization judges documents both outside the governed system and inside it, **the rule set
MUST have a single declaration**, and the copy the system holds MUST be derived from it. Divergence
MUST be detectable by a check — two readers disagreeing about admissibility is indistinguishable
from either being correct.

## 16. What this document does not specify

- **The phases.** How many, what they are called, what each decides.
- **The register shapes**, column names, or document format.
- **The check kinds** available, beyond that the set is closed.
- **The sufficiency criterion** — what counts as fixing every fact the realization needs, and how
  that is determined — which the applicable profile declares (6a §7).
- **Who the owners are**, or how questions reach them.
- **The mechanism of realization**, which is Governed Construction's subject once candidates exist.

## 17. Normative invariants

- **TR-1.** A transformation MUST be a governed transition, and its dossier MUST NOT be a member of
  the governed system (§2, §4).
- **TR-2.** Governed content MUST live in registers; a phase document's prose MUST NOT carry it
  (§5).
- **TR-3.** Rules MUST be declared data; check kinds MUST be closed and MUST fail hard on the
  unknown; every declared rule MUST be evaluated (§5).
- **TR-3a.** Every declared rule MUST be demonstrated capable of refusing; a rule set is not evidence
  that its rules can fail (§5.1).
- **TR-4.** A verdict MUST name, for each finding, the rule and its location, where a location
  identifies the register, the entry, and the field concerned (§5).
- **TR-5.** A constrained field's admissible values MUST be declared with the register's own
  declaration, and emptiness MUST be declared rather than inferred (§6).
- **TR-5a.** A register's entries MUST be individually addressable; the addressing mechanism is not
  specified (§6).
- **TR-6.** Each register MUST declare its rung; a business rung MUST NOT name a constructed
  identity; grounding evidence MUST occupy a field declared for it (§7).
- **TR-7.** Where a capability is named before it is identified, provisional name and bound identity
  MUST be reconciled in both directions (§7).
- **TR-8.** Admissibility MUST be decided by the rule set alone; a quality score MUST NOT gate, and
  MUST NOT score a value that admission refuses (§8).
- **TR-9.** An unanswered question MUST be recorded as such, MUST NOT be filled in or hedged, and a
  blocking one MUST make its document inadmissible (§9.1).
- **TR-10.** Human semantic content MUST enter once; later phases MUST preserve, reference, or
  declare supersession of it (§9.2).
- **TR-11.** Preservation MUST be checked in both directions — nothing dropped, nothing invented
  (§9.2).
- **TR-12.** Gates MUST be declared, and acceptance MUST NOT be inferred from admissibility (§9.3).
- **TR-13.** Given the same human answers — the same declared field values (§9) — any worker MUST
  yield the same admissible registers
  (§9.4).
- **TR-14.** A phase determined by its prior MUST be projected, MUST refuse an inadmissible prior,
  and its verdict MUST NOT be read as evidence about the change (§10).
- **TR-15.** A transformation MUST be validated against a named frozen baseline, and never against
  one containing its own output (§11).
- **TR-15a.** Only the first transformation of a system MAY proceed without a baseline; it MUST name
  a profile it did not author, MUST declare its grounding registers empty rather than omitting them,
  and MUST satisfy every other requirement of this document. No later transformation MUST claim
  genesis (§12).
- **TR-16.** Claims about the existing system MUST be grounded; truth, belief, and question MUST be
  kept in separate registers; grounding MUST be able to answer about a named artifact (§11.1,
  §11.2).
- **TR-17.** Sufficiency MUST be determined before realization, and realization MUST refuse a design
  that does not fix every fact the realization needs; how it is determined is unconstrained (§13).
- **TR-18.** A realized artifact MUST be a function of the design alone (§13).
- **TR-19.** An amendment MUST be a whole redeclaration and MUST NOT narrow what it replaces (§13).
- **TR-20.** The realization order MUST be gapless over what it schedules and dependency-respecting;
  whether independent artifacts are ordered relative to one another is not specified (§13).
- **TR-21.** Realization MUST cover both authored and amended artifacts, and MUST be checked in both
  directions against what was asked for (§13).
- **TR-22.** Completion MUST require execution against real state, with criteria asserting state
  rather than returned status (§14).
- **TR-23.** A refusal the business declares MUST be discharged by the design, the discharge MUST be
  stated, and it MUST be checked against what it does rather than only that it was stated (§14).
- **TR-24.** Where a rule set has two readers, they MUST derive from one declaration, and divergence
  MUST be detectable (§15.1).
- **TR-25.** A human answer MUST be recorded as declared register content addressed by field (§9).

## 18. Conformance

The conformance subject of this document is a **transformation**: a dossier, the verdicts reached at
each phase, the realization it produced, and the proof that the result works.

A transformation conforms when its phases were judged by declared rules, its human content entered
once and survived in both directions, its open questions were asked rather than guessed, its claims
about the existing system were grounded rather than asserted, its design was measured sufficient
before realization, and its result was executed against real state.

**Two demonstrations distinguish a conforming transformation from one that merely completed.** The
first is a run against a baseline that already contains related artifacts — greenfield exercises none
of the logic that makes transformation *transformation* (§11.3). The second is a fabrication check:
a phase that states something its prior does not, passing a pipeline that checks only for loss
(§9.2). Both failures report success.

How these are required and evaluated belongs to the Conformance Test Specification.
