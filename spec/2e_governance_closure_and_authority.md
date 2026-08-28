# Governance Closure & Authority

## 1. Scope

This document specifies how the governance applicable to a subject is **determined, composed, and
bounded**: what constitutes an authority, what an authority may reach, how governing elements
enter a closure, and what it means for a closure to be complete.

The Governance Standard states what governance is and what the governing relation means. This
document establishes which governing elements actually apply to a given subject, and by what right.
The Semantic Model requires that a closure be determinate, bounded, and non-ambient, and that an
unestablishable closure determine `refuse`; this document says what establishing one consists of.

This document introduces the terms **constituting act**, **jurisdiction**, **delegation**,
**inheritance**, and **import**. Every other term it uses is defined by the Conceptual Model or
the Governance Standard.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Seven concepts, none derivable from another

The Conceptual Model defines authority, ownership, scope, admission, and closure as distinct;
this document adds inheritance and import. **None of the seven is inferrable from any other**, and
every conflation below has occurred in practice and produced a system that believed itself
governed:

| | Answers | Conflated with | What the conflation causes |
|---|---|---|---|
| **Authority** | by what right does this govern? | ownership | whoever wrote it governs it |
| **Ownership** | who is responsible for this? | authority | responsibility is read as jurisdiction |
| **Scope** | how far does this reach? | authority | reaching a subject is read as being entitled to |
| **Concern** | what subject matter is this about? | authority | classifying a topic constitutes jurisdiction over it |
| **Admission** | is this part of the system? | presence | being found is being admitted |
| **Inheritance** | what does this receive from above? | containment | location determines governance |
| **Import** | what has been brought across a boundary? | inheritance | crossing a boundary happens silently |

The independence is not stylistic. Each pairing above collapses two questions into one answer,
and thereafter no check can distinguish them however plainly the distinction is documented
elsewhere.

## 3. Authority

An **authority** is the entity from which governance jurisdiction derives — the answer to *who
may decide*.

A **jurisdiction** is what an authority may decide: the subjects it is entitled to govern and the
governance decisions it may make about them. A jurisdiction is constituted by the act that
constitutes the authority holding it. It is never acquired by reaching a subject, containing it, or
classifying it — scope, containment, and concern are separate questions (§2, §5, CA-6).

### 3.1 Constitution

An authority exists by a **constituting act**: a declared act that brings it into being and
states what it may decide. An authority is never constituted by:

- **being needed** — that a subject requires governance does not create something entitled to
  supply it;
- **being first** — precedence in resolution, loading, or authoring order is mechanism (AI-2);
- **containing something** — containment is location (§7);
- **naming something** — an identifier is a label, not a claim;
- **classifying something** — a concern may be organized, indexed, and reasoned about with no
  jurisdiction constituted over it (§5).

### 3.2 What an authority must be able to answer

A purported authority MUST be able to answer all five of the following **from declared artifacts
alone**. One that cannot has not demonstrated distinct governance authority and MUST NOT be
admitted as one:

1. **Who** the authority is.
2. **What constituting act** created it.
3. **What subjects** fall within its jurisdiction.
4. **What governance decision it may make that no other authority may.**
5. **How it relates** to the authorities above it and beside it.

Question 4 does the most work. An authority that can make no decision another authority could not
make has no jurisdiction of its own; it is a name for a subset of someone else's.

These questions establish that an authority **has jurisdiction**. They do not establish the
**scope** of any individual governing element under that authority, which is determined
separately (§5). Question 3 asks what subjects fall within the authority's reach; it does not ask
the authority to enumerate the extent of every element it governs through. Reading it that way
would collapse authority back into scope.

### 3.3 Independence

Passing §3.2 is necessary and **not sufficient**.

**The authority that constitutes and exercises a jurisdiction MUST be distinguishable from the
authority whose subjects that jurisdiction governs.** An authority governing its own constituting
artifacts is exercising self-governance — which is a concern of that authority, not a second
authority.

This is the test that separates a genuine division of jurisdiction from a division of subject
matter wearing jurisdiction's vocabulary. Applying it to any particular arrangement is a
determination about that system; this document specifies the test, not its outcome anywhere.

### 3.4 Delegation

An authority MAY **delegate** part of its jurisdiction to another. Delegation is itself a
governed act and is bounded by three rules:

- **No delegation exceeds its source.** An authority cannot delegate what it does not hold.
- **Delegation is declared and revocable.** An undeclared delegation is indistinguishable from an
  authority that constituted itself.
- **Delegation does not divide responsibility.** The delegating authority remains answerable for
  what it delegated; delegation moves the decision, not the accountability.

### 3.5 No enumeration of authorities

**This family defines the condition under which an authority may exist. It does not define how
many may exist, nor enumerate which.** A ceiling, a whitelist, or a fixed roster would be the
same error relocated: it would let an authority be legitimate by appearing on a list rather than
by meeting the condition, and would let one that meets the condition be refused for absence from
it.

## 4. Ownership

**Ownership** is responsibility for a subject: who maintains it, answers for it, and is expected
to change it.

Ownership is not authority. An owner may hold no jurisdiction over what they own, and an
authority may govern subjects it does not own. The two coincide often enough that the conflation
is easy and consequential: read as authority, ownership makes whoever happens to maintain an
artifact entitled to decide what governs it.

## 5. Scope and concern

**Scope** is the extent of subjects over which a governing element applies. Scope answers *how
far*; authority answers *by what right*. The two are independent: an element may hold authority
over a subject and a scope that excludes it, or a scope that reaches a subject over which it
holds no authority — and the second is a defect, not a grant.

**Concern** is the semantic subject matter being decided about. A concern may be organized,
classified, indexed, and governed without any authority being constituted over it. **A concern
classification MUST NOT by itself constitute an authority or a jurisdiction.**

### 5.1 Universal scope is not scope

**A governing element whose scope is everything is not bounded over anything in particular.**

Jurisdiction over a named set of subjects is what an authority holds. A rule asserting universal
scope is the negation of a named set: it cannot be distinguished from a rule belonging to the
root of governance, and if several elements assert it, their jurisdictions cannot be
distinguished from one another.

This does not forbid rules that apply broadly. It requires that breadth be *stated as a set*,
however large, rather than as the absence of a boundary — because a scope with no boundary
supplies nothing for a determination to check, and nothing for a conflicting claim to be tested
against.

## 6. Admission

**Admission** is the determination by which something becomes part of a governed system (§2). It
is a governed transition: it has a closure, a determination, a result, and evidence.

- Nothing is admitted by being present, discoverable, referenced, or expected.
- **Admission determines membership in the governed system; closure determines which admitted
  governing elements apply to a given subject.** Admission does not place an element in every
  subject's closure, or in any subject's closure. The two determinations are separate, and an
  element may be admitted and apply to nothing.
- Admission does not confer authority: an admitted governing element governs what it is declared
  to govern and nothing else.
- A subject admitted without a determinable closure is not admitted (§10.3).

## 7. Inheritance

**Inheritance** is the passing of governance from one subject to another by a declared structural
relation between them.

- **Inheritance MUST be declared.** A structural relation that carries governance says so; one
  that does not, does not.
- **Containment is not inheritance.** That a subject sits inside a region, a domain, a namespace,
  or a document carries no governance of itself. Where containment does carry governance, it is
  because a declaration says it does — and then the declaration is what governs, not the
  containment.
- **Inherited governance is not weakened governance.** An inherited element applies as fully as a
  directly declared one, and composes by dominance with it (§10.2).
- **Inheritance does not enlarge authority or silently enlarge scope.** It carries the declared
  governance relation to the inheriting subject; the governing element's authority is unchanged,
  and its declared scope is unchanged except where the inheritance declaration itself establishes
  the applicable subject relation.
- **Inheritance does not transfer authority.** A subject inherits the governance applicable to it,
  never the entitlement to govern.

## 8. Import

**Import** is the deliberate bringing of a governing element across a boundary, so that it applies
to subjects on the far side.

**Inheritance extends applicability through a declared relation between subjects; import
establishes applicability by declaration of the receiving closure.** Neither changes the
authority of the element inherited or imported. The two exist because governance reaches a
subject in two different ways — because of what the subject *is related to*, and because a
closure *took the element in* — and a system with only one of them either cannot express
structural governance or cannot express deliberate crossing.

Import exists because governance must sometimes cross boundaries and must never do so by
accident. Four rules bound it:

- **Import is declared at the point of entry**, by the closure receiving it. A closure states what
  it takes in; nothing is imported by being reachable.
- **Import does not extend the imported element's authority.** An element imported into a closure
  governs there because that closure admitted it, not because its own authority now reaches
  further.
- **Import is not re-authorship.** The imported element remains the same element under the same
  authority; a closure cannot alter what it imports by importing it.
- **What is imported is bounded and enumerable.** A closure that imports "whatever applies" has
  not stated what it imported.

## 9. Federation

**Federation** is the relation among *distinct* authorities: how separate jurisdictions coexist,
delegate to one another, and bound one another.

- Federation is a relation, not a property of any single authority. An authority does not "have"
  a federation.
- Federation has instances only where §3.2 and §3.3 are satisfied on both sides. Two named
  regions of one authority's concerns are not federated; they are that authority's concerns.
- Whether federation is a relation only, or is additionally a governed subject in its own right,
  is not specified by this revision (Governance Semantic Ontology §10).

## 10. Closure

The **governance closure** of a subject is the complete determination of which governing elements
apply to it, by what authority each applies, and how their rules compose.

### 10.1 Establishment

Establishing a closure means determining, for a subject:

1. every governing element **admitted as applicable to it** by direct declaration (Governance
   Standard §3.2), by declared inheritance (§7), or by declared import (§8) — these three are the
   only paths by which applicability arises, and the closure is the result of resolving them, not
   a prior fact about what applies;
2. the authority under which each applies, and that the authority holds jurisdiction over this
   subject (§3);
3. that each element's scope reaches this subject (§5); and
4. how the applicable elements compose (§10.2).

A closure is established or it is not. There is no partially established closure that a
determination may proceed against.

### 10.2 Composition

Applicable elements compose by dominance, as the Semantic Model defines it, and
order-independently (Governance Standard §7). Composition adds no element and drops none: the
elements that compose are exactly those §10.1 determined.

### 10.3 Boundedness

**Governance may neither enter a closure nor escape it silently.**

- **Nothing enters undeclared.** An element that applies without having been established by
  §10.1 is governance nobody admitted, and its effect is indistinguishable from a mechanism's
  behavior.
- **Nothing escapes undeclared.** A subject for which no applicable closure can be established is
  ungoverned, and a system in which a subject can come to be so without that being a
  determination has a hole in it rather than a gap. A subject outside one closure while inside
  another is not ungoverned; closure is per subject, and is not globally unique.
- **The closure is enumerable.** What applies to a subject can be stated, finitely, before any
  determination over that subject begins (Semantic Model §7).

### 10.4 Failure

Where a closure cannot be established — an element unresolvable, an authority undeclared or
undemonstrated, a scope indeterminate, an import unbounded — **the determination is `refuse`**
(SM-4, AI-6).

This is a closure-failure determination, not the outcome of evaluating rules: no rule was
evaluated, because the rule set could not be established. A system that reports the two alike
misdirects every remedy, since a closure failure is repaired by declaration and a rule refusal by
changing what was proposed.

## 11. Normative invariants

- **CA-1.** Authority, ownership, scope, concern, admission, inheritance, and import MUST be
  separately determinable, and none MUST be inferred from another (§2).
- **CA-2.** An authority MUST exist by a declared constituting act, and MUST NOT be constituted by
  need, precedence, containment, naming, or classification (§3.1).
- **CA-3.** A purported authority MUST answer all five questions of §3.2 from declared artifacts
  alone, or MUST NOT be admitted as an authority.
- **CA-4.** The authority constituting and exercising a jurisdiction MUST be distinguishable from
  the authority whose subjects it governs (§3.3).
- **CA-5.** A delegation MUST be declared, MUST NOT exceed its source, and MUST NOT transfer
  answerability (§3.4).
- **CA-6.** A concern classification MUST NOT constitute an authority or a jurisdiction (§5).
- **CA-7.** A governing element MUST declare its scope as a set of subjects. Scope MUST NOT be
  represented by the absence of a boundary, or by an unbounded assertion of everything (§5.1).
- **CA-8.** Inheritance MUST be declared; containment MUST NOT carry governance of itself (§7).
- **CA-9.** Import MUST be declared by the receiving closure, MUST be enumerable, and MUST NOT
  extend the imported element's authority (§8).
- **CA-10.** A closure MUST be fully established before any determination over its subject, and
  MUST be enumerable before evaluation begins (§10.1, §10.3).
- **CA-11.** No governing element may apply to a subject without having been established in that
  subject's closure (§10.3).
- **CA-12.** Where a closure cannot be established, the determination MUST be `refuse`, and MUST
  be distinguishable from a rule refusal (§10.4).

## 12. Conformance

The conformance subject of this document is a **closure determination**: the account a system
gives, for a subject, of what governs it and by what right.

A closure determination conforms when:

- every applicable element was established by declaration, declared inheritance, or declared
  import — and none by position (CA-11, AI-2);
- every authority under which an element applies satisfies §3.2 and §3.3 (CA-3, CA-4);
- every element's scope is a stated set that reaches the subject (CA-7);
- the closure was enumerable before evaluation and complete at determination (CA-10); and
- a closure that could not be established produced a refusal distinguishable from a rule refusal
  (CA-12).

Two things this document does not decide, and a conforming system may settle either way:

- **whether any particular arrangement of authorities is legitimate.** §3.2 and §3.3 are the test;
  whether a given domain, region, or boundary passes it is a determination about that system, made
  under its own governance.
- **how authority, concern, and scope are represented.** That they remain separately determinable
  is required (CA-1, GO-11, MB-7); the form is not specified here.
