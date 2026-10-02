# Governed Transformation

## 1. Scope

This document specifies **governed transformation**: how a stated need becomes governed artifacts of
an existing system. Transformation works under rules. It engages human judgement where that judgement
is irreducible, and nowhere else.

This document closes Part IV. Governed Construction determines whether candidate declarations may
exist. This document specifies where those candidates come from and under what governance they were
produced. **Transformation is itself a governed subject** (SM-9). It is not a practice that surrounds
a governed system and stands exempt from it.

This document specifies a **semantic contract**, not a realization. Phase names, register shapes,
rule identifiers and artifact kinds may vary freely. Nothing here requires a particular pipeline,
tooling or number of steps.

This document introduces the terms **dossier**, **phase**, **register**, **check kind**, **verdict**,
**gate**, **worker**, **rung**, **grounding**, **sufficiency**, and **realization**. The Conceptual
Model, the Semantic Model or Parts II–IV defines every other term it uses.

### 1.1 Three terms that differ from earlier usage

Earlier working material used some terms that this family has since defined differently. Where that
happened, this document uses the family's term:

| Earlier usage | Here | Because |
|---|---|---|
| *determination* — a design fixing an artifact completely | **sufficiency** | *determination* is the Semantic Model's term for the result of evaluating a closure |
| *composition* — the governed system being changed | **baseline**, or *governed system* | *composition* is the Conceptual Model's term for combining separately owned parts |
| *projection* — a phase determined by its prior | **projection**, unchanged | it is a projection in the Projection Standard's sense: a deterministic derivation from a defined source |

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Transformation as a governed transition

Transformation is the Semantic Model's transition schema applied to one subject:

| | In transformation |
|---|---|
| `S` | the baseline — what the system currently is |
| `π` | a stated need, together with the human answers it requires |
| `C` | the governance applicable to changing this system |
| `S′` | the next baseline |
| `ε` | the dossier and the record of what was determined at each phase |

**If the baseline did not change, the system did not change.** Transformation takes an existing
baseline as input and produces the next one. It is not authoring beside a system (Conceptual Model,
*transformation*).

## 3. Five separations

This model exists to keep apart five things that people often blend:

```
what is decided  ≠  who decides it  ≠  what makes a design sufficient  ≠  what proves it works
                      and, orthogonal to all four:   may it proceed  ≠  how good it is
```

- **Decisions** are recorded in registers and judged by declared rules.
- **Deciders** are human where judgement is irreducible. A worker may draft, but it never decides.
- **Sufficiency** is the property that a design states every fact realization requires. It is
  measured, never assumed.
- **Proof** is execution against real state. Document admissibility is not proof.

**A realization that merges any two of these is non-conforming.** Each merger has a signature:

- merging the first two produces a pipeline that invents business content;
- merging the second two produces a pipeline that reports success over a system that does nothing;
- merging the last pair produces a quality score that has quietly become a second gate.

## 4. The sequence

A transformation is a set of **phases**, ordered by what each depends on. Each phase reads what
precedes it, emits what it declares it emits, and is judged. The **dossier** is what the phases
emit, together with the record of what was determined at each.

The order is a dependency order, not necessarily a line. Two phases that do not read each other may
be produced in either order, or at once. The diagram below shows the common case, not the required
shape.

```
need → P₀ → P₁ → … → Pₙ → sufficiency → realization → execution
       └─ rule set per phase ─┘   └ measured ┘        └ proves ┘
```

- **A dossier is evidence, never a member of the governed system.** It records how a change was
  reached. It is not admitted, not executed, and not part of any baseline.
- **Phases hand off explicitly.** A phase declares what it emits and what the phases that depend on
  it consume. An unchecked handoff looks the same as a preserved one. So **absence MUST be reported,
  not passed silently**.
- **Phases differ in kind.** Some decide. Some only restate. A phase that decides nothing is a
  projection (§10) and MUST NOT be authored by hand.
- The sequence is validated against a baseline (§11), never against "the current system".

## 5. Registers and rules

A phase document consists of **registers**, not prose. Each register is named and has a declared
field set. This document does not specify whether a register is realized as a table, as typed
records or in some other form. It requires that the register's fields are declared and that content
is addressed by them.

- Governed content MUST live in registers. Prose in a phase document is commentary and MUST NOT carry
  governed content.
- **A rule MUST be declared as data**, and MUST NOT be expressed as procedure. The declaration states
  the rule's identity, the register it governs, the **check kind** that evaluates it, and its
  parameters. Adding a governed rule MUST NOT require a new mechanism, and a new mechanism MUST NOT
  carry a rule's intent.
- A **check kind** is a mechanism, such as *is this field empty* or *does this identity exist in the
  baseline*. It carries no policy and knows nothing of why it matters.
- **The set of check kinds MUST be closed**, and an unknown check kind MUST fail hard. A silently
  skipped rule reports green over an unevaluated subject.
- **Every declared rule MUST be evaluated.** There MUST be no short-circuiting on the first failure.
- **Every declared rule MUST be demonstrated capable of refusing.** A rule set is not evidence that
  its rules can fail (EN-5).
- A **verdict** is the determination reached by applying a phase's rule set to its document. For each
  finding, a verdict MUST name the rule and the location. A **location** identifies the register, the
  entry and the field the finding concerns. A count is not a verdict.

A realization SHOULD derive structural rules from the phase's own document declaration instead of
restating them. A document's shape then has one declaration, not two that can disagree.

**Registers, rules and check kinds are declaration elements, not artifacts** (Machine Block §7.1).
They are governed because the phase document that carries them is governed. They are closed because
its surface is closed. **They need no artifact kind of their own.** A profile that closes a kind
vocabulary need not admit a kind for a rule or a register. A profile that does has begun classifying
fields rather than representations. What a profile decides here is the sufficiency criterion (§13),
not a taxonomy of the machinery that evaluates it.

The **check kind** is called a kind but is not one. It is a mechanism identifier within a closed set
declared here. It is unrelated to the artifact kinds the Kind Vocabulary admits. The two never appear
in one registry.

### 5.1 A rule set is not evidence that its rules can fail

A rule may be unable to refuse anything. **Register rules fail this way in forms that no reading of
the rule reveals:**

- a rule whose parameters name a field the register does not declare **reads every value as empty and
  reports clean**;
- a check that resolves a field name by prefix is satisfied by a longer sibling, so **a register can
  lose a field and report clean**.

Both failures are silent. Both leave a rule set reporting green over an unevaluated subject. Neither
can be found by inspecting the rule. So a realization must **demonstrate refusal, not declare
intent**. For each declared rule, it must exhibit a document the rule refuses.

This is the transformation-side form of the vacuity rule (Enforcement & Refusal §4.2). This document
states it separately for two reasons. The failure modes are specific to rules over registers. And a
rule that cannot fire looks the same as a subject that never violated it.

## 6. Declared fields

- A field constrained to a set of values MUST declare that set **as part of the register's own
  declaration**. A vocabulary held apart from the declaration it constrains is a second declaration,
  and it can disagree with the first.
- **A register's entries MUST be individually addressable.** A determination about one entry MUST be
  able to name that entry and no other. This document does not specify how an entry is addressed, by
  declared key, by position or otherwise. Addressability is what makes a finding reportable rather
  than merely counted.
- **Emptiness MUST be declared, never inferred.** A register with nothing in it MUST say so.
  Otherwise a register nobody filled in looks the same as a register whose author considered it and
  found nothing. Only the second is an answer.
- A register MAY be optional. **Optional means *may be empty*. It does not mean *may be absent*, and
  it never means *may be unconsidered*.**

## 7. The purity ladder

A transformation moves from business language to bound identity, and the **rungs** MUST be kept
apart.

- Each register MUST declare its rung.
- **A register at a business rung MUST NOT name a constructed artifact identity.** Naming one is design
  leaking into a phase that has not reached design.
- Where a rung cites evidence from the baseline, the citation MUST occupy a field declared for it,
  never the content field itself. The business meaning and the identity that grounds it are two
  facts. Merging them makes the first uncheckable.
- A capability MAY be named before it is identified. Where a realization does this, the provisional
  name and the identity later bound to it MUST be reconciled **in both directions** (§9).

This is the separation of behavior from implementation, applied *within* the transformation as well
as to its output. A realization that lets a business register name an implementation has no rung
left to protect.

## 8. Admissibility is not quality

Where a realization scores documents:

- **Only the rule set MUST decide whether a document may proceed.**
- **A quality score MUST NOT gate.** An admissible document MAY score poorly. Declared open questions
  are the ordinary reason. An inadmissible document MAY score well.
- What is scored MUST be declared, and declared where the governance lives, not inside a tool.
- **A value that admission refuses MUST NOT also be scored.** Admission has already refused the
  document. Scoring the value again counts one defect twice. A reader comparing two documents would
  then see a gap that measures how many ways one fact was counted. So when a rule starts refusing a
  value, the same change removes the scoring term for that value.

## 9. Human engagement

This model engages human judgement exactly where it is irreducible. It makes that boundary explicit,
not cultural.

### 9.1 Questions are asked, never guessed

- A phase that cannot determine a value MUST record it as an **open question against a named
  owner**. It MUST NOT fill the value in. It MUST NOT hedge it with a placeholder. A field stating
  that the question is unanswered reads as decided to every later phase.
- **An unresolved blocking question MUST make its document inadmissible.** Otherwise the next phase
  answers it by invention.

### 9.2 Preservation is bidirectional

- Human semantic content enters **exactly once**. A later phase MUST preserve it, reference it, or
  supersede it while declaring that it has done so. Silent replacement MUST be refused. This applies
  to narrative content that no register can derive, as much as to rows.
- A phase MUST NOT drop what its prior committed to, **and MUST NOT state what its prior does not.**
  Usually only the first is checked. **A fabricated fact walks through a pipeline that checks only
  for loss.**

### 9.3 Gates

A **gate** is a point at which a person accepts a phase's document. **A gate is not a verdict.** A
document may be admissible and still not accepted.

- Gates MUST be declared, and a phase MUST NOT pass one implicitly.
- A document SHOULD carry the lifecycle state it has reached, from a declared vocabulary. Then nobody
  reads *admissible* and *accepted* as one claim.

### 9.4 A worker may draft; it MUST NOT decide

A **worker** is whatever produces a phase document: a person, an interactive assistant, or a
programmatic model.

- The rule set answers whether a document is admissible. The human answers whether a business
  question is answered.
- **A human answer MUST be recorded as declared register content**, addressed by the field of the
  register the question was opened against (§5, §9.1). An answer given in conversation and never
  recorded in a register has not been given. It is not addressable, not preserved and not comparable.
- **Given the same human answers, any worker MUST yield the same admissible registers**, and so the
  same artifacts. Prose wording may differ. Nothing governed may.

**"The same human answers" means the same declared field values, and nothing looser.** Over free
prose, nobody could check the obligation. Two answers that mean the same thing in different words
would look the same as two different answers. An obligation nothing can refuse is not in force
(EN-1). Over declared fields, comparison decides the obligation. The demonstration TR-13 requires is
to run two workers against one recorded answer set and compare their registers.

This is the same line §5 draws for everything else the transformation governs. Governed content lives
in registers, and prose is commentary. **A human answer is governed content.**

This makes workers interchangeable. It is the transformation-side form of the family's standing
rule: a realization may derive knowledge and may not assign significance (GC-8).

## 10. Projected phases

After everything above, a phase's content may be **uniquely determined by its prior**. Such a phase
MUST be produced mechanically and MUST NOT be hand-authored.

Such a phase is a projection in the Projection Standard's sense: a deterministic derivation from a
defined source. Everything that document requires of a projection holds of it, including
faithfulness and regenerability.

- A realization that declares a projected phase MUST declare **where a question discovered while
  producing it goes**. It goes back to the phase that owns it, which is then projected again. It
  MUST NOT enter at the projected phase.
- **A projection MUST refuse to run against an inadmissible prior.** Otherwise it launders an open
  question into a document that reads as settled.
- **A projected phase's rules govern amendment, not authorship.** A projection cannot fail the rules
  that check what it was built from. So a realization MUST NOT read a projected document's verdict as
  evidence about the change.

## 11. Baseline and grounding

- Every transformation MUST be validated against a **named, frozen baseline**, identified by content
  and not by location (SN-2). If validation used "whatever is current", a regression would look the
  same as a rebuild.
- **A transformation MUST NOT be judged against a baseline that already contains its own output.**
  Every identity it assigns would collide with itself.
- Re-baselining MUST be a deliberate, recorded act.

### 11.1 Grounding

A claim about what the system already provides MUST be **grounded**: read from the baseline through a
declared inspection interface. It MUST NOT be asserted.

Three things MUST be kept in separate registers, because two of the three failures are silent:

| | Authoritative | Resolved by |
|---|---|---|
| a business truth | the human | taken as given |
| a belief about what exists | nobody yet | grounding against the baseline |
| an open question | nobody | asking the named owner |

**A belief recorded as a truth is never verified. A question recorded as a truth is answered by
invention.**

### 11.2 Grounding must answer about a named thing

**The inspection interface MUST be able to answer about a named artifact, not only enumerate.**

Some rules must compare a design against what one existing artifact currently declares. If grounding
produces only inventories, nobody can write such a rule at all. A realization with enumeration-only
grounding will find whole classes of rule inexpressible at design time. Those rules will migrate to
later, weaker checks. **That is a limitation of the interface, not of the rule.**

### 11.3 Evolution is never greenfield

A transformation's distinguishing logic, such as reuse against authoring, placement and preservation,
has meaning only against a baseline. **A realization that validates only greenfield runs leaves all
of that logic unexercised while reporting success.**

Exactly one transformation legitimately has no baseline: the first (§12). Every later transformation
has one. Validating any of them as if it were the first exercises none of the logic that makes
transformation *transformation*.

## 12. The first transformation

Every requirement above presumes a baseline. **The first transformation of a system has none.** It
proceeds from the empty governed state to the first baseline (Semantic Model §11).

This is not an exemption, and a realization MUST NOT treat it as one. Exactly what a baseline would
have supplied differs, and nothing else.

### 12.1 What differs

| | Ordinarily | At genesis |
|---|---|---|
| the input `S` | the baseline | the empty governed state |
| grounding reads from | the baseline | nothing — there is nothing to read |
| the closure judging it | the governance already in force | the proposal's own declared governance composed with the profile it claims |

### 12.2 What does not differ

Everything else holds unchanged:

- declared rules judge the phases;
- questions are asked, not guessed;
- human content enters once and is preserved in both directions;
- gates are declared;
- sufficiency is measured before realization;
- execution against real state proves the result.

**A first transformation is judged more, not less.** A later transformation can ground a claim
against a baseline. This one cannot. So it carries the full burden of every claim it makes about what
exists. And no prior state exists whose survival would signal a mistake.

### 12.3 Emptiness is declared, not skipped

Grounding registers are not omitted at genesis. **They are declared empty** (§6). Otherwise a register
nobody filled looks the same as a register whose author established there was nothing to find. At
genesis every grounding register is legitimately the second kind. That is exactly when the first kind
is easiest to mistake for it.

### 12.4 The claimed profile stands in for the baseline

A genesis transformation MUST name the profile it claims, and that profile MUST NOT be authored by the
transformation claiming it (SN-7).

This keeps the first transformation from certifying itself. Ordinarily a transformation is judged
against governance already in force, and against a baseline it did not write. At genesis both are
absent. The claimed profile is the only thing left that the transformation did not author. **Without
it, a first transformation would declare its own rules, satisfy them, and be, by its own account,
perfectly governed.**

### 12.5 Once

**Only the first transformation of a system may proceed without a baseline.** Every later one has a
baseline, and MUST be validated against it (TR-15).

A later transformation MUST NOT claim genesis. That holds for a new domain, a new region, a subsystem
introduced whole, and a baseline that is inconvenient to obtain. After genesis, nothing constitutes
itself (AI-17). A transformation that claims otherwise proposes to introduce governance that nothing
in force admitted.

## 13. Sufficiency and realization

Design and realization fail differently, and a realization MUST keep them apart:

| Failure | Statement | Repaired by |
|---|---|---|
| **design** | the register is incomplete or contradictory | re-authoring a register |
| **sufficiency** | the design is valid and does not fix an artifact | amending the design language |

- **Sufficiency MUST be determined before realization, and realization MUST refuse a design that does
  not fix every fact the realization needs.** **A generator that supplies a fact the design omits is a
  second, ungoverned design authority.** This document leaves open how sufficiency is determined. Two
  approaches discharge it equally: a proportion of required facts against a declared threshold, and a
  per-artifact test that refuses on the first artifact the design does not fix. The determination
  must complete before anything is written.
- **A realized artifact MUST be a function of the design alone.** It MUST NOT be a function of the
  design and the current baseline. Otherwise the same dossier realizes differently against two
  baselines, and sufficiency stops meaning anything.
- **Amending an existing artifact is a whole redeclaration, not a delta.** So a design may state less
  than the artifact already holds. A realization MUST therefore compare an amendment against what it
  replaces, and **MUST refuse one that narrows it**.
- **The realization order MUST be a schedule, not a list.** It MUST cover everything it schedules
  without gaps. It MUST place everything an artifact depends on before that artifact. A gap is a
  dropped artifact that reads as an ordering choice. This document does not specify whether mutually
  independent artifacts are ordered relative to one another.
- **Scheduling and amendment are different acts, and a realization MUST perform both.** An artifact
  that already exists cannot be scheduled for authoring. If only scheduled artifacts are realized,
  amendments are silently not applied.
- Every realized artifact MUST trace to something the transformation asked for, **and everything
  asked for MUST be realized.** Both directions MUST be checked. Usually only one is.

## 14. Proof

Three results are **jointly insufficient** to establish that anything works: document admissibility,
determined sufficiency, and realization at zero differences.

**A transformation MUST NOT be considered complete until the system it produced has been executed
against real state and the stated acceptance criteria observed.**

- An acceptance criterion MUST assert **the state it claims**, never the status a call returned. A
  success code over an operation that did the wrong thing does not satisfy the criterion.
- A criterion about **data** MUST be settled by operating on such data. An example is the claim that
  records written before a change remain usable. A sealed representation cannot resolve such a
  criterion, because it declares stores and never their contents.
- **A rule that passes because a value is absent has not passed.**
- **A refusal the business declared MUST be discharged by the design, and the discharge MUST be
  checked against what it does.** A design that states it has handled a refusal has stated something.
  Whether the artifacts it fixes actually refuse is a different question. Only the second question is
  the discharge. This is the fabrication check of §9.2 applied to refusals. A pipeline that checks
  only that a discharge was declared admits a design that declares it and does nothing.

## 15. What a host must provide

This document requires three capabilities of whatever hosts a transformation. A realization MAY
satisfy them any way it chooses:

- **An addressable system**: artifacts with stable identities that a baseline can name and a design
  can cite (ID-1).
- **An inspection interface**: a way to read facts about a baseline without reaching into the
  machinery that produced it (§11.2). Grounding through construction internals couples the
  transformation to a build mechanism. That is non-conforming in substance, if not in form.
- **A sealing mechanism**: where a rule set is judged inside the governed system as well as outside
  it, some way for the rule set to exist there. A realization that judges documents only outside the
  system needs none.

### 15.1 One rule set, two readers

A realization may judge documents both outside the governed system and inside it. Then **the rule
set MUST have a single declaration**, and the copy the system holds MUST be derived from it.
Divergence MUST be detectable by a check. When two readers disagree about admissibility, nobody can
tell which one is correct.

## 16. What this document does not specify

- **The phases**: how many, what they are called, and what each decides.
- **The register shapes**, column names or document format.
- **The check kinds** available, beyond that the set is closed.
- **The sufficiency criterion**: what counts as fixing every fact the realization needs, and how that
  is determined. The applicable profile declares it (Normative Platform Profile §7).
- **Who the owners are**, or how questions reach them.
- **The mechanism of realization.** Once candidates exist, that is Governed Construction's subject.

## 17. Normative invariants

- **TR-1.** A transformation MUST be a governed transition, and its dossier MUST NOT be a member of
  the governed system (§2, §4).
- **TR-2.** Governed content MUST live in registers. A phase document's prose MUST NOT carry it (§5).
- **TR-3.** Rules MUST be declared data. Check kinds MUST be closed and MUST fail hard on the unknown.
  Every declared rule MUST be evaluated (§5).
- **TR-3a.** Every declared rule MUST be demonstrated capable of refusing. A rule set is not evidence
  that its rules can fail (§5.1).
- **TR-4.** A verdict MUST name, for each finding, the rule and its location, where a location
  identifies the register, the entry, and the field concerned (§5).
- **TR-5.** A constrained field's admissible values MUST be declared with the register's own
  declaration, and emptiness MUST be declared rather than inferred (§6).
- **TR-5a.** A register's entries MUST be individually addressable. The addressing mechanism is not
  specified (§6).
- **TR-6.** Each register MUST declare its rung. A business rung MUST NOT name a constructed
  identity. Grounding evidence MUST occupy a field declared for it (§7).
- **TR-7.** Where a capability is named before it is identified, provisional name and bound identity
  MUST be reconciled in both directions (§7).
- **TR-8.** Admissibility MUST be decided by the rule set alone. A quality score MUST NOT gate, and
  MUST NOT score a value that admission refuses (§8).
- **TR-9.** An unanswered question MUST be recorded as such, and MUST NOT be filled in or hedged. A
  blocking one MUST make its document inadmissible (§9.1).
- **TR-10.** Human semantic content MUST enter once. Later phases MUST preserve, reference, or
  declare supersession of it (§9.2).
- **TR-11.** Preservation MUST be checked in both directions: nothing dropped, nothing invented
  (§9.2).
- **TR-12.** Gates MUST be declared, and acceptance MUST NOT be inferred from admissibility (§9.3).
- **TR-13.** Given the same human answers — the same declared field values (§9) — any worker MUST
  yield the same admissible registers (§9.4).
- **TR-14.** A phase determined by its prior MUST be projected and MUST refuse an inadmissible prior.
  Its verdict MUST NOT be read as evidence about the change (§10).
- **TR-15.** A transformation MUST be validated against a named frozen baseline, and never against
  one containing its own output (§11).
- **TR-15a.** Only the first transformation of a system MAY proceed without a baseline. It MUST name a
  profile it did not author, MUST declare its grounding registers empty rather than omitting them,
  and MUST satisfy every other requirement of this document. No later transformation MUST claim
  genesis (§12).
- **TR-16.** Claims about the existing system MUST be grounded. Truth, belief, and question MUST be
  kept in separate registers. Grounding MUST be able to answer about a named artifact (§11.1,
  §11.2).
- **TR-17.** Sufficiency MUST be determined before realization, and realization MUST refuse a design
  that does not fix every fact the realization needs. How sufficiency is determined is unconstrained
  (§13).
- **TR-18.** A realized artifact MUST be a function of the design alone (§13).
- **TR-19.** An amendment MUST be a whole redeclaration and MUST NOT narrow what it replaces (§13).
- **TR-20.** The realization order MUST be gapless over what it schedules and dependency-respecting.
  Whether independent artifacts are ordered relative to one another is not specified (§13).
- **TR-21.** Realization MUST cover both authored and amended artifacts, and MUST be checked in both
  directions against what was asked for (§13).
- **TR-22.** Completion MUST require execution against real state, with criteria asserting state
  rather than returned status (§14).
- **TR-23.** A refusal the business declares MUST be discharged by the design, and the discharge MUST
  be stated. It MUST be checked against what it does, not only for having been stated (§14).
- **TR-24.** Where a rule set has two readers, they MUST derive from one declaration, and divergence
  MUST be detectable (§15.1).
- **TR-25.** A human answer MUST be recorded as declared register content addressed by field (§9).

## 18. Conformance

The conformance subject of this document is a **transformation**: a dossier, the verdicts reached at
each phase, the realization it produced, and the proof that the result works.

A transformation conforms when all of the following hold:

- declared rules judged its phases;
- its human content entered once and survived in both directions;
- its open questions were asked, not guessed;
- its claims about the existing system were grounded, not asserted;
- its design was measured sufficient before realization;
- its result was executed against real state.

**Two demonstrations tell a conforming transformation apart from one that merely completed:**

- **A run against a baseline that already contains related artifacts.** Greenfield exercises none of
  the logic that makes transformation *transformation* (§11.3).
- **A fabrication check.** A phase states something its prior does not, and passes a pipeline that
  checks only for loss (§9.2).

Both failures report success.

The Conformance Test Specification owns how these are required and evaluated.
