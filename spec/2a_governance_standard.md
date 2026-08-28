# Governance Standard

## 1. Scope

This document specifies what governance *is* in a governed system: what it means for one thing to
govern another, what governance can say, how it is declared, and why it applies to itself.

It is the first document of Part II and the one the rest of the part depends on. The Governance
Semantic Ontology classifies governing elements whose semantics this document establishes. The
Machine Block Standard and the Kind Vocabulary govern the surface on which they are declared.
Governance Closure & Authority determines how the governance applicable to a subject is *resolved*;
this document says what is being resolved. Enforcement & Refusal covers what happens when governance
is evaluated; this document, what it says.

This document introduces the terms **governing relation**, **modality**, **authorization**,
**requirement**, **permission**, and **prohibition**. Every other term it uses is defined by the
Conceptual Model.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Governance as an architectural concern

To make governance first-class is to make three commitments, each of which excludes a familiar
arrangement:

- **Governance is content, not activity.** It is carried inside the system as declarations the
  system consumes, not performed around the system by people or tools. A system whose governance
  lives in documents, review boards, or pipeline configuration is governed by those things and
  not by itself.
- **Governance is a subject, not a substrate.** The governance of a system is part of its
  governed state, and is therefore itself governed (§6). There is no privileged layer that
  governs without being governed.
- **Governance determines, it does not advise.** A governing element that can be satisfied or
  ignored with the same result governs nothing. What governance says constrains what the system
  can do, or it is not governance (Conceptual Model, *distinguish from policy*).

These are not properties a system acquires by adding governance to it. They are properties of
how it is built, and a system that lacks them cannot be given them by a later addition.

## 3. The governing relation

**Governance is a relation.** It holds between a governing element and a governed subject, and
it is the relation that makes the element a *governing* element and the subject a *governed*
subject: an element governs nothing until the relation holds, and a subject is ungoverned until
something stands in that relation to it. An artifact remains an artifact when it governs
nothing; what it does not remain is a governing element.

Write it `G(e, s)` — element `e` governs subject `s`.

### 3.1 What establishes the relation

`G(e, s)` holds when it is **declared** — by `e`, by `s`, or by a third element with authority
over both. Nothing else establishes it.

In particular, the relation is not established by:

| Not by | Why it is tempting | Why it fails |
|---|---|---|
| containment | the subject sits inside the element's region | a region is a location, and locations govern nothing |
| ordering | the element was resolved, loaded, or applied first | order is an artifact of mechanism, not of authority |
| naming | the subject's identifier resembles the element's | a name is a label, and a label is not a claim |
| defaulting | nothing else governs the subject | the absence of governance is not the presence of some |
| proximity | the two were authored or deployed together | co-location is not composition |

This is the governance-semantic basis of Architectural Invariant AI-2: governance that arises
from position is governance nobody declared, and therefore nobody can establish as an authorized
determination. AI-2 is the architectural consequence of this rule, not a separate requirement
restated here.

### 3.2 Both directions, and what a disagreement means

The relation may be declared from either end, and both directions are necessary. Neither alone
is sufficient, and the reason in each case is concrete:

- **Subject-side only** — each subject declares what governs it. A subject then escapes
  governance by omission: what fails to declare its governance is ungoverned, and the failure is
  invisible because nothing was expected.
- **Element-side only** — each governing element declares its subjects. A subject then cannot
  determine what governs it without examining every element in the system, and the closure
  cannot be established locally.

A conforming system therefore establishes the relation from both perspectives. What is required
is that both assertions exist and agree — not that two declarations be physically stored. How
each perspective is carried is a representation question this document does not decide; the two
may be represented independently, derived from one another, or held in a single structure that
expresses both, provided each is separately assertable and separately checkable.

**Where the two disagree — an element asserts a subject that does not assert it, or a subject
asserts an element that does not assert it — the disagreement is a defect and MUST be
refused.** It MUST NOT be resolved by preferring one
direction, by taking the union, or by taking the intersection:

- preferring the element's claim lets governance be attached to subjects that never accounted
  for it;
- preferring the subject's declaration lets a subject decline governance by silence;
- the union admits governance neither side agreed to;
- the intersection silently drops governance one side asserted.

Each of these produces a system that continues running with a governance relation that no one
declared and no one can point to. Refusal is the only resolution that leaves the disagreement
visible. How the disagreement is detected and reported is specified by Governance Closure &
Authority.

### 3.3 The relation is many-to-many

A subject may be governed by many elements; an element may govern many subjects. Neither
multiplicity is a defect, and neither is resolved by choosing one:

- **Many elements over one subject** compose into that subject's closure by dominance (Semantic
  Model §6). Adding an element never widens what the subject may do.
- **One element over many subjects** applies to each independently. That an element governs two
  subjects creates no relation between those subjects.

## 4. What governance can say

A governing element speaks about its subject in exactly four **modalities**. The set is closed
within this revision of the standard.

| Modality | Says | About |
|---|---|---|
| **Authorization** | this may exist or occur at all | the space of the possible |
| **Requirement** | this must hold, or must occur | obligation on what exists |
| **Permission** | this may occur, in this state | occurrence within the possible |
| **Prohibition** | this must not occur | occurrence within the possible |

Requirement and prohibition are the two forms of obligation the Conceptual Model names;
authorization and permission are its two positive counterparts.

### 4.1 Governance is positive, not restrictive

This is the standard's central claim about what governance is, and it separates PGC from
essentially every conventional governance arrangement.

```
conventional:   everything is possible, except what is prohibited
PGC:            nothing is possible, except what is authorized
```

Under the conventional arrangement, governance is a set of restrictions over an unbounded space.
The space is whatever the implementation happens to permit; governance carves pieces out of it;
and anything nobody thought to prohibit is available. The consequences are structural, not
accidental: governance is always incomplete, its completeness is unknowable, and every newly
discovered capability is permitted until someone notices it.

Under positive authorization, the space is empty until declarations populate it. **What is not
authorized does not exist as part of the governed system**, and therefore need not be
prohibited. A capability nobody declared is not an unguarded capability of the system; it is not
a capability of the system at all.

The qualification is exact and not a hedge. Unauthorized things may certainly exist in the
world: a candidate artifact sits on disk, an unauthorized request arrives at a boundary, a
library offers a function nobody declared. None of them is thereby part of the governed system,
and none acquires standing by being present (Conceptual Model, *nothing is admitted by being
present*). Positive authorization is a claim about membership, not about physics.

Three consequences follow, and they are why the choice matters:

- **Completeness is structural.** There is no question of whether governance covers everything,
  because nothing exists that governance did not establish.
- **Unauthorized behavior is absent rather than blocked.** There is no path to reach it and
  therefore nothing to defend (AI-1, AI-12).
- **Omission fails safe.** Forgetting to authorize something makes it unavailable. Under the
  conventional arrangement, forgetting to prohibit something makes it available — the same
  human error with the opposite consequence.

### 4.2 Why prohibition is still required

Positive authorization does not make prohibition redundant, and a standard that concluded so
would be wrong.

Authorization governs **existence**: whether a thing is part of the system at all. Prohibition
governs **occurrence**: whether an authorized thing may happen in a given state. These are
different questions, and the second does not reduce to the first.

An authorized capability must still be prohibited from occurring where a state, an actor, or a
condition forbids it. Declining to authorize it would remove it everywhere, which is not what
governance meant to say.

```
authorization    ──▶  may this exist?             answered once, structurally
permission       ──▶  may this occur here, now?   answered per determination
prohibition      ──▶  must this not occur here?   answered per determination
requirement      ──▶  must this hold?             answered per determination
```

The distinction is load-bearing for the whole family: authorization is settled during
construction and prohibition is evaluated during any determination, so collapsing them would
collapse the boundary between the two activities (AI-3).

### 4.3 Modalities and determination

The modalities are what governance *says*; the consequences of the Semantic Model are what a
determination *reaches*. They correspond:

| Modality | Evaluated | Yields on failure |
|---|---|---|
| Authorization | the subject is not authorized | `refuse` |
| Requirement | the required condition does not hold | `refuse` |
| Prohibition | the prohibited condition holds | `refuse` |
| Permission | the permission is conditional and its condition partly holds | `constrain` |

Every modality yields `admit` when satisfied. That every failure yields `refuse` is not a
simplification — it is what makes a closure composable, since a determination reached from many
elements needs a single ordering, and `refuse` dominates (Semantic Model §6).

## 5. Governance is declared

A governing element is an artifact (Conceptual Model §3.1): it is declared on the same
declaration surface as anything else, admitted by the same admission, identified the same way,
and superseded by the same relation.

This is not an economy of mechanism. It is what makes §6 possible: governance that were declared
some other way would need a second admission, a second identity scheme, and a second account of
change — and would be governed by none of them.

**Governing elements are distinguished by what they declare, not by how they are carried.** An
artifact is a governing element when what it declares stands in the governing relation to
another subject. Nothing about its representation, location, or naming makes it one.

## 6. Governance governs itself

The governance of a system is part of that system's governed state (Semantic Model §3).
Therefore:

- a governing element is a governed subject;
- changing a governing element is a governed transition, determined under the closure applicable
  to it; and
- there is no privileged element that governs without being governed.

**Reflexivity is the property that makes governance real rather than declarative.** A layer that
governs everything except itself has placed its own change outside governance, and its own change
is precisely where governance is most easily lost — a system whose rules can be edited by an
ungoverned path is exactly as governed as that path allows.

### 6.1 Where the regress stops

Reflexivity invites an infinite regress: if every governing element is governed, what governs the
first one?

The regress terminates at genesis, and not by exception. In genesis the closure is composed from
the proposal's own declared governance together with an externally claimed profile the proposal
does not author (Semantic Model §11). The first baseline is therefore determined reflexively
against the governance it declares, subject also to the externally claimed profile. No governing
element determines itself; the baseline carrying them is determined under a closure they
contribute to but do not constitute alone.

After genesis, nothing constitutes itself (AI-17). A governing element added later is determined
under the closure already in force. **The claimed profile is what prevents reflexivity from
becoming circularity**: without it, a system could declare governance that approves of itself and
be, by its own account, perfectly governed.

## 7. Composition

Where several governing elements apply to one subject, they compose. This document specifies three
properties of that composition; Governance Closure & Authority specifies how it is performed.

- **Composition is by dominance.** The determination is the dominant consequence, as the
  Semantic Model defines dominance, among the consequences the applicable governing elements
  yield (Semantic Model §6, AI-7). This document requires that composition be by dominance; what
  dominance means is not its to define.
- **Composition is order-independent.** The result does not depend on the sequence in which
  elements are considered. An order-dependent composition makes governance a property of
  mechanism, which AI-2 forbids.
- **Composition is closed.** The elements that compose are exactly those the closure supplies.
  An element that applies without being in the closure, or is in the closure without applying,
  is a defect in the closure and not a nuance of composition.

## 8. What this document does not specify

Four boundaries, each guarding against a collapse that has occurred in practice:

- **Not classification.** What *kind* of governing work an element does is the Governance
  Semantic Ontology's subject. An element's category never establishes its authority; a
  classification that determined what an element governs would be a second, undeclared
  governance layer (Conceptual Model §5).
- **Not resolution.** Which elements apply to a subject, and by what authority, is Governance
  Closure & Authority's subject. This document specifies that the relation must be declared, not how
  it is found.
- **Not enforcement.** What happens when governance is evaluated — how a determination is
  reached, reported, and refused — is Enforcement & Refusal's subject. Governance says;
  enforcement does. A system may state its governance perfectly and enforce none of it.
- **Not representation.** How a governing element is written is the Machine Block Standard's
  subject. Nothing here requires a format, and no format makes an artifact governing.

## 9. Normative invariants

- **GS-1.** The governing relation MUST be declared. It MUST NOT be established by containment,
  ordering, naming, defaulting, or proximity (§3.1).
- **GS-2.** A conforming governance arrangement MUST establish the governing relation from both
  the governing-element and governed-subject perspectives, and MUST refuse where the two
  assertions disagree (§3.2).
- **GS-3.** Governance MUST be positive: what is not authorized MUST NOT be admitted into the
  governed system, and MUST NOT require prohibition in order to be unavailable (§4.1).
- **GS-4.** Authorization and prohibition MUST NOT be collapsed. Authorization governs existence;
  prohibition governs occurrence (§4.2).
- **GS-5.** A governing element MUST be an artifact, admitted, identified, and superseded as any
  other artifact is (§5).
- **GS-6.** Every governing element MUST itself be a governed subject. No element may be exempt
  from the governance it participates in (§6).
- **GS-7.** Change to a governing element MUST be a governed transition (§6, SM-9).
- **GS-8.** Composition of applicable elements MUST be by dominance and MUST be order-independent
  (§7).
- **GS-9.** An element's semantic category MUST NOT establish, extend, or limit what it governs
  (§8).

## 10. Conformance

The conformance subject of this document is a **governance arrangement**: the account a system
gives of what governs what, together with the declarations that carry it.

A governance arrangement conforms when:

- every governing relation in it is declared, and none arises from position (GS-1);
- the relation is established from both perspectives and disagreement is refused (GS-2);
- the space of what the system may do is established by authorization rather than bounded by
  prohibition (GS-3);
- governing elements are ordinary artifacts and are themselves governed, including under change
  (GS-5, GS-6, GS-7); and
- its composition is by dominance and order-independent (GS-8).

A system may satisfy every one of these and still refuse nothing, because nothing has yet been
evaluated. That is not a deficiency of the arrangement: what a system does when governance is
evaluated belongs to Enforcement & Refusal, and conformance of the two is determined separately.
