# Governance Standard

## 1. Scope

This document specifies what governance *is* in a governed system. It covers four questions:

- what it means for one thing to govern another;
- what governance can say;
- how governance is declared;
- why governance applies to itself.

This is the first document of Part II, and the rest of the part depends on it:

- The Governance Semantic Ontology classifies the governing elements whose semantics this document
  establishes.
- The Machine Block Standard and the Kind Vocabulary govern the surface on which those elements are
  declared.
- Governance Closure & Authority determines how the governance that applies to a subject is
  *resolved*. This document says what is being resolved.
- Enforcement & Refusal covers what happens when governance is evaluated. This document covers what
  governance says.

This document introduces the terms **governing relation**, **modality**, **authorization**,
**requirement**, **permission**, and **prohibition**. The Conceptual Model defines every other term
it uses.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Governance as an architectural concern

A system that makes governance first-class makes three commitments. Each one excludes a familiar
arrangement:

- **Governance is content, not activity.** The system carries governance inside itself, as
  declarations it consumes. People and tools do not perform it around the system. If a system's
  governance lives in documents, review boards or pipeline configuration, those things govern it.
  The system does not govern itself.
- **Governance is a subject, not a substrate.** A system's governance is part of its governed state,
  so it is itself governed (§6). No privileged layer governs without being governed.
- **Governance determines. It does not advise.** If a system gets the same result whether it
  satisfies a governing element or ignores it, that element governs nothing. What governance says
  constrains what the system can do. Otherwise it is not governance (Conceptual Model, *distinguish
  from policy*).

A system does not gain these properties when someone adds governance to it. They are properties of
how the system is built. A later addition cannot give them to a system that lacks them.

## 3. The governing relation

**Governance is a relation.** It holds between a governing element and a governed subject. This
relation is what makes the element *governing* and the subject *governed*. An element governs
nothing until the relation holds. A subject is ungoverned until something stands in that relation to
it. An artifact that governs nothing is still an artifact. It is simply not a governing element.

Write it `G(e, s)`: element `e` governs subject `s`.

### 3.1 What establishes the relation

`G(e, s)` holds when it is **declared**. The declaration may come from `e`, from `s`, or from a
third element with authority over both. Only a declaration establishes the relation.

In particular, none of these establishes it:

| Not by | Why it is tempting | Why it fails |
|---|---|---|
| containment | the subject sits inside the element's region | a region is a location, and locations govern nothing |
| ordering | the element was resolved, loaded, or applied first | order is an artifact of mechanism, not of authority |
| naming | the subject's identifier resembles the element's | a name is a label, and a label is not a claim |
| defaulting | nothing else governs the subject | the absence of governance is not the presence of some |
| proximity | the two were authored or deployed together | co-location is not composition |

This rule is the governance-semantic basis of Architectural Invariant AI-2. Governance that arises
from position is governance nobody declared. So nobody can establish it as an authorized
determination. AI-2 is the architectural consequence of this rule. It is not a separate requirement restated here.

### 3.2 Both directions, and what a disagreement means

Either end may declare the relation, and a system needs both directions. Neither one is enough
alone, for concrete reasons:

- **Subject-side only.** Each subject declares what governs it. A subject can then escape governance
  by omission. A subject that fails to declare its governance is ungoverned. Nobody notices, because
  nobody expected anything.
- **Element-side only.** Each governing element declares its subjects. A subject can then learn what
  governs it only by examining every element in the system. Nobody can establish the closure
  locally.

So a conforming system establishes the relation from both perspectives. Both assertions must exist
and agree. The system need not store two physical declarations.

How it carries each perspective is a representation question, and this document leaves it open. The
two perspectives may be represented independently, derived from one another, or held in one
structure that expresses both. Each must still be separately assertable and separately checkable.

**The two perspectives may disagree. An element may assert a subject that does not assert it, or a
subject may assert an element that does not assert it. That disagreement is a defect and MUST be
refused.** It MUST NOT be resolved by preferring one direction, by taking the union, or by taking the
intersection:

- preferring the element's claim lets governance attach to subjects that never accounted for it;
- preferring the subject's declaration lets a subject decline governance by silence;
- the union admits governance that neither side agreed to;
- the intersection silently drops governance that one side asserted.

Each of these leaves the system running with a governance relation that nobody declared and nobody
can point to. Only refusal keeps the disagreement visible. Governance Closure & Authority specifies
how a system detects and reports the disagreement.

### 3.3 The relation is many-to-many

Many elements may govern one subject. One element may govern many subjects. Neither multiplicity is
a defect, and a system does not resolve either one by choosing:

- **Many elements over one subject** compose into that subject's closure by dominance (Semantic
  Model §6). Adding an element never widens what the subject may do.
- **One element over many subjects** applies to each subject independently. An element that governs
  two subjects creates no relation between them.

## 4. What governance can say

A governing element speaks about its subject in exactly four **modalities**. The set is closed in
this revision of the standard.

| Modality | Says | About |
|---|---|---|
| **Authorization** | this may exist or occur at all | the space of the possible |
| **Requirement** | this must hold, or must occur | obligation on what exists |
| **Permission** | this may occur, in this state | occurrence within the possible |
| **Prohibition** | this must not occur | occurrence within the possible |

Requirement and prohibition are the two forms of obligation the Conceptual Model names.
Authorization and permission are their two positive counterparts.

### 4.1 Governance is positive, not restrictive

This is the standard's central claim about what governance is. It separates PGC from almost every
conventional governance arrangement.

```
conventional:   everything is possible, except what is prohibited
PGC:            nothing is possible, except what is authorized
```

In the conventional arrangement, governance is a set of restrictions over an unbounded space. The
implementation decides what the space contains. Governance carves pieces out of it. Anything nobody
thought to prohibit stays available. The consequences are structural, not accidental:

- governance is always incomplete;
- nobody can know how complete it is;
- every newly discovered capability is permitted until someone notices it.

Under positive authorization, the space is empty until declarations fill it. **What is not
authorized does not exist as part of the governed system**, so nobody needs to prohibit it. A
capability nobody declared is not an unguarded capability of the system. It is not a capability of
the system at all.

This qualification is exact, not a hedge. Unauthorized things can certainly exist in the world. A
candidate artifact sits on disk. An unauthorized request arrives at a boundary. A library offers a
function nobody declared. None of them is part of the governed system on that account, and none
gains standing by being present (Conceptual Model, *nothing is admitted by being present*). Positive
authorization is a claim about membership, not about physics.

Three consequences follow, and they are why the choice matters:

- **Completeness is structural.** Nobody needs to ask whether governance covers everything. Nothing
  exists that governance did not establish.
- **Unauthorized behavior is absent, not blocked.** No path reaches it, so there is nothing to
  defend (AI-1, AI-12).
- **Omission fails safe.** If someone forgets to authorize something, it is unavailable. In the
  conventional arrangement, if someone forgets to prohibit something, it is available. The same
  human error has the opposite consequence.

### 4.2 Why prohibition is still required

Positive authorization does not make prohibition redundant. A standard that concluded so would be
wrong.

Authorization governs **existence**: whether a thing is part of the system at all. Prohibition
governs **occurrence**: whether an authorized thing may happen in a given state. These are different
questions, and the second does not reduce to the first.

A state, an actor or a condition may forbid an authorized capability from occurring. Governance must
still prohibit it there. Withholding authorization would remove the capability everywhere, and that
is not what governance meant to say.

```
authorization    ──▶  may this exist?             answered once, structurally
permission       ──▶  may this occur here, now?   answered per determination
prohibition      ──▶  must this not occur here?   answered per determination
requirement      ──▶  must this hold?             answered per determination
```

The whole family relies on this distinction. Construction settles authorization. Any determination
evaluates prohibition. If the two merged, the boundary between those two activities would merge too
(AI-3).

### 4.3 Modalities and determination

The modalities are what governance *says*. The consequences of the Semantic Model are what a
determination *reaches*. They correspond:

| Modality | Evaluated | Yields on failure |
|---|---|---|
| Authorization | the subject is not authorized | `refuse` |
| Requirement | the required condition does not hold | `refuse` |
| Prohibition | the prohibited condition holds | `refuse` |
| Permission | the permission is conditional and its condition partly holds | `constrain` |

Every modality yields `admit` when satisfied. Every failure yields `refuse`, and that is not a
simplification. A determination reached from many elements needs a single ordering, and `refuse`
dominates (Semantic Model §6). That is what makes a closure composable.

## 5. Governance is declared

A governing element is an artifact (Conceptual Model §3.1). It shares everything with other
artifacts:

- it is declared on the same declaration surface;
- the same admission admits it;
- it is identified the same way;
- the same relation supersedes it.

This is not an economy of mechanism. It is what makes §6 possible. Governance declared some other way
would need a second admission, a second identity scheme and a second account of change. None of
them would govern it.

**What a governing element declares sets it apart, not how it is carried.** An artifact is a
governing element when what it declares stands in the governing relation to another subject. Its
representation, location and naming play no part.

## 6. Governance governs itself

A system's governance is part of that system's governed state (Semantic Model §3). Therefore:

- a governing element is a governed subject;
- a change to a governing element is a governed transition, determined under the closure that
  applies to it;
- no privileged element governs without being governed.

**Reflexivity makes governance real rather than declarative.** A layer that governs everything
except itself has put its own change outside governance. Its own change is exactly where governance
is easiest to lose. If an ungoverned path can edit a system's rules, the system is only as governed
as that path allows.

### 6.1 Where the regress stops

Reflexivity invites an infinite regress. If every governing element is governed, what governs the
first one?

The regress stops at genesis, and not by exception. In genesis, the closure is composed from two
sources (Semantic Model §11):

- the proposal's own declared governance;
- an externally claimed profile that the proposal does not author.

So the first baseline is determined reflexively against the governance it declares, and is also
subject to the claimed profile. No governing element determines itself. The baseline that carries
the elements is determined under a closure they contribute to but do not make up alone.

After genesis, nothing constitutes itself (AI-17). A governing element added later is determined
under the closure already in force. **The claimed profile stops reflexivity from becoming
circularity.** Without it, a system could declare governance that approves of itself. By its own
account, that system would be perfectly governed.

## 7. Composition

When several governing elements apply to one subject, they compose. This document specifies three
properties of that composition. Governance Closure & Authority specifies how a system performs it.

- **Composition is by dominance.** The determination is the dominant consequence among those the
  applicable governing elements yield, as the Semantic Model defines dominance (Semantic Model §6,
  AI-7). This document requires composition by dominance. Defining dominance is not its job.
- **Composition is order-independent.** The result does not depend on the order in which a system
  considers the elements. An order-dependent composition makes governance a property of mechanism,
  and AI-2 forbids that.
- **Composition is closed.** Exactly the elements the closure supplies take part. An element may
  apply without being in the closure, or sit in the closure without applying. Either case is a defect
  in the closure, not a nuance of composition.

## 8. What this document does not specify

This document draws four boundaries. Each one guards against a collapse that has happened in
practice:

- **Not classification.** What *kind* of governing work an element does is the subject of the
  Governance Semantic Ontology. An element's category never establishes its authority. A
  classification that determined what an element governs would be a second, undeclared governance
  layer (Conceptual Model §5).
- **Not resolution.** Which elements apply to a subject, and by what authority, is the subject of
  Governance Closure & Authority. This document specifies that the relation must be declared. It
  does not specify how a system finds it.
- **Not enforcement.** What happens when governance is evaluated is the subject of Enforcement &
  Refusal: how a system reaches, reports and refuses a determination. Governance says. Enforcement
  does. A system may state its governance perfectly and enforce none of it.
- **Not representation.** How a governing element is written is the subject of the Machine Block
  Standard. Nothing here requires a format, and no format makes an artifact governing.

## 9. Normative invariants

- **GS-1.** The governing relation MUST be declared. It MUST NOT be established by containment,
  ordering, naming, defaulting, or proximity (§3.1).
- **GS-2.** A conforming governance arrangement MUST establish the governing relation from both the
  governing-element and governed-subject perspectives. It MUST refuse where the two assertions
  disagree (§3.2).
- **GS-3.** Governance MUST be positive. What is not authorized MUST NOT be admitted into the
  governed system, and MUST NOT require prohibition in order to be unavailable (§4.1).
- **GS-4.** Authorization and prohibition MUST NOT be collapsed. Authorization governs existence.
  Prohibition governs occurrence (§4.2).
- **GS-5.** A governing element MUST be an artifact, admitted, identified and superseded as any other
  artifact is (§5).
- **GS-6.** Every governing element MUST itself be a governed subject. No element may be exempt from
  the governance it participates in (§6).
- **GS-7.** Change to a governing element MUST be a governed transition (§6, SM-9).
- **GS-8.** Composition of applicable elements MUST be by dominance and MUST be order-independent
  (§7).
- **GS-9.** An element's semantic category MUST NOT establish, extend, or limit what it governs (§8).

## 10. Conformance

The conformance subject of this document is a **governance arrangement**: the account a system gives
of what governs what, together with the declarations that carry it.

A governance arrangement conforms when all of the following hold:

- Every governing relation in it is declared, and none arises from position (GS-1).
- It establishes the relation from both perspectives and refuses disagreement (GS-2).
- Authorization establishes the space of what the system may do. Prohibition does not bound that
  space (GS-3).
- Governing elements are ordinary artifacts, and they are themselves governed, including under
  change (GS-5, GS-6, GS-7).
- Its composition is by dominance and order-independent (GS-8).

A system may satisfy every one of these and still refuse nothing, because it has evaluated nothing
yet. That is not a deficiency of the arrangement. What a system does when it evaluates governance
belongs to Enforcement & Refusal, and the two conformances are determined separately.
