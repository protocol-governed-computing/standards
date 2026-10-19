# Governance Closure & Authority

## 1. Scope

This document specifies how the governance that applies to a subject is **determined, composed and
bounded**. It covers:

- what constitutes an authority;
- what an authority may reach;
- how governing elements enter a closure;
- what it means for a closure to be complete.

The Governance Standard states what governance is and what the governing relation means. This
document establishes which governing elements actually apply to a given subject, and by what right.
The Semantic Model requires a closure to be determinate, bounded and non-ambient. It also requires
an unestablishable closure to determine `refuse`. This document says what establishing a closure
consists of.

This document introduces the terms **constituting act**, **jurisdiction**, **delegation**,
**inheritance**, and **import**. The Conceptual Model or the Governance Standard defines every other
term it uses.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Seven concepts, none derivable from another

The Conceptual Model defines authority, ownership, scope, admission and closure as distinct concepts.
This document adds inheritance and import. **None of the seven can be inferred from any other.**
Every conflation below has happened in practice, and each produced a system that believed itself
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

The independence is not a matter of style. Each pairing above merges two questions into one answer.
After that, no check can tell them apart, however plainly a document states the distinction
elsewhere.

That is why the distinction must stay visible in the system.

## 3. Authority

An **authority** is the entity from which governance jurisdiction derives. It answers the question
*who may decide*.

A **jurisdiction** is what an authority may decide: the subjects it may govern and the governance
decisions it may make about them. The act that constitutes an authority also constitutes its
jurisdiction. An authority never gains jurisdiction by reaching a subject, containing it or
classifying it. Scope, containment and concern are separate questions (§2, §5, CA-6).

### 3.1 Constitution

An authority exists by a **constituting act**: a declared act that brings it into being and states
what it may decide. None of these constitutes an authority:

- **being needed.** A subject that requires governance does not thereby create something entitled
  to supply it.
- **being first.** Precedence in resolution, loading or authoring order is mechanism (AI-2).
- **containing something.** Containment is location (§7).
- **naming something.** An identifier is a label, not a claim.
- **classifying something.** A concern may be organized, indexed and reasoned about with no
  jurisdiction constituted over it (§5).

### 3.2 What an authority must be able to answer

A purported authority MUST be able to answer all five of the following **from declared artifacts
alone**. If it cannot, it has not demonstrated distinct governance authority and MUST NOT be
admitted as one:

1. **Who** the authority is.
2. **What constituting act** created it.
3. **What subjects** fall within its jurisdiction.
4. **What governance decision it may make that no other authority may.**
5. **How it relates** to the authorities above it and beside it.

Question 4 does the most work. Suppose an authority can make only decisions that another authority
could also make. It then has no jurisdiction of its own. It is a name for a subset of someone else's.

These questions establish that an authority **has jurisdiction**. They do not establish the
**scope** of any individual governing element under that authority. Scope is determined separately
(§5). Question 3 asks what subjects fall within the authority's reach. It does not ask the authority
to enumerate the extent of every element it governs through. That reading would merge authority
back into scope.

### 3.3 Independence

Passing §3.2 is necessary but **not sufficient**.

**The authority that constitutes and exercises a jurisdiction MUST be distinguishable from the
authority whose subjects that jurisdiction governs.** An authority that governs its own constituting
artifacts is exercising self-governance. That is a concern of the one authority, not a second
authority.

This test separates a genuine division of jurisdiction from a division of subject matter dressed in
jurisdiction's vocabulary. Applying the test to a particular arrangement is a determination about
that system. This document specifies the test, not its outcome anywhere.

### 3.4 Delegation

An authority MAY **delegate** part of its jurisdiction to another. Delegation is itself a governed
act, and three rules bound it:

- **No delegation exceeds its source.** An authority cannot delegate what it does not hold.
- **Delegation is declared and revocable.** An undeclared delegation looks the same as an authority
  that constituted itself.
- **Delegation does not divide responsibility.** The delegating authority stays answerable for what
  it delegated. Delegation moves the decision, not the accountability.

### 3.5 No enumeration of authorities

**This family defines the condition under which an authority may exist. It does not define how many
may exist, and it does not enumerate which.** A ceiling, a whitelist or a fixed roster would be the
same error in a new place. An authority could then be legitimate by appearing on a list rather than
by meeting the condition. And an authority that meets the condition could be refused for missing
from the list.

## 4. Ownership

**Ownership** is responsibility for a subject: who maintains it, answers for it, and is expected to
change it.

Ownership is not authority. An owner may hold no jurisdiction over what it owns. An authority may
govern subjects it does not own. The two coincide often, so the conflation is easy, and it has
consequences. If a system reads ownership as authority, whoever happens to maintain an artifact gains
the right to decide what governs it.

## 5. Scope and concern

**Scope** is the extent of subjects over which a governing element applies. Scope answers *how far*.
Authority answers *by what right*. The two are independent:

- an element may hold authority over a subject and have a scope that excludes it;
- an element may have a scope that reaches a subject over which it holds no authority.

The second case is a defect, not a grant.

**Concern** is the semantic subject matter being decided about. A concern may be organized,
classified, indexed and governed without any authority constituted over it. **A concern
classification MUST NOT by itself constitute an authority or a jurisdiction.**

### 5.1 Universal scope is not scope

**A governing element whose scope is everything is bounded over nothing in particular.**

An authority holds jurisdiction over a named set of subjects. A rule that asserts universal scope
negates a named set. Nobody can tell it apart from a rule that belongs to the root of governance. If
several elements assert universal scope, nobody can tell their jurisdictions apart from one another.

This does not forbid rules that apply broadly. It requires breadth to be *stated as a set*, however
large, and not as the absence of a boundary. A scope with no boundary gives a determination nothing
to check. It also gives a conflicting claim nothing to be tested against.

## 6. Admission

**Admission** is the determination by which something becomes part of a governed system (§2). It is
a governed transition, with a closure, a determination, a result and evidence.

- Only a determination admits. Being present, discoverable, referenced or expected admits nothing.
- **Admission determines membership in the governed system. Closure determines which admitted
  governing elements apply to a given subject.** Admission does not place an element in every
  subject's closure, or in any subject's closure. The two determinations are separate. An element
  may be admitted and apply to nothing.
- Admission does not confer authority. An admitted governing element governs what it is declared to
  govern and nothing else.
- A subject admitted without a determinable closure is not admitted (§10.3).

## 7. Inheritance

**Inheritance** is the passing of governance from one subject to another by a declared structural
relation between them.

- **Inheritance MUST be declared.** A structural relation that carries governance says so. A relation
  that does not say so carries no governance.
- **Containment is not inheritance.** A subject that sits inside a region, a domain, a namespace or
  a document gains no governance from that alone. Where containment does carry governance, a
  declaration says so. Then the declaration governs, not the containment.
- **Inherited governance is not weakened governance.** An inherited element applies as fully as a
  directly declared one, and composes with it by dominance (§10.2).
- **Inheritance does not enlarge authority or silently enlarge scope.** It carries the declared
  governance relation to the inheriting subject. The governing element's authority stays the same.
  Its declared scope also stays the same, except where the inheritance declaration itself
  establishes the applicable subject relation.
- **Inheritance does not transfer authority.** A subject inherits the governance that applies to it,
  never the right to govern.

## 8. Import

**Import** is the deliberate bringing of a governing element across a boundary, so that it applies
to subjects on the far side.

**Inheritance extends applicability through a declared relation between subjects. Import establishes
applicability by a declaration of the receiving closure.** Neither changes the authority of the
inherited or imported element. Governance reaches a subject in two different ways, and the two
mechanisms match them:

- because of what the subject *is related to* (inheritance);
- because a closure *took the element in* (import).

A system with only one of them cannot express either structural governance or deliberate crossing.

Import exists because governance must sometimes cross boundaries, and must never do so by accident.
Four rules bound it:

- **The receiving closure declares the import at the point of entry.** A closure states what it
  takes in. Being reachable imports nothing.
- **Import does not extend the imported element's authority.** An element imported into a closure
  governs there because that closure admitted it. Its own authority does not reach further.
- **Import is not re-authorship.** The imported element stays the same element under the same
  authority. A closure cannot alter what it imports by importing it.
- **What is imported is bounded and enumerable.** A closure that imports "whatever applies" has not
  stated what it imported.

## 9. Federation

**Federation** is the relation among *distinct* authorities: how separate jurisdictions coexist,
delegate to one another, and bound one another.

- Federation is a relation, not a property of any single authority. An authority does not "have" a
  federation.
- Federation has instances only where §3.2 and §3.3 are satisfied on both sides. Two named regions
  of one authority's concerns are not federated. They are that authority's concerns.
- This revision does not specify whether federation is only a relation, or also a governed subject
  in its own right (Governance Semantic Ontology §10).

## 10. Closure

The **governance closure** of a subject is the complete determination of which governing elements
apply to it, by what authority each applies, and how their rules compose.

### 10.1 Establishment

To establish a closure for a subject, a system determines:

1. every governing element **admitted as applicable to it**, by direct declaration (Governance
   Standard §3.2), by declared inheritance (§7), or by declared import (§8). Applicability arises
   only by these three paths. The closure is the result of resolving them, not a prior fact about
   what applies;
2. the authority under which each element applies, and that the authority holds jurisdiction over
   this subject (§3);
3. that each element's scope reaches this subject (§5);
4. how the applicable elements compose (§10.2).

A closure is either established or not. No determination may proceed against a partially
established closure.

### 10.2 Composition

Applicable elements compose by dominance, as the Semantic Model defines it, and independently of
order (Governance Standard §7). Composition adds no element and drops none. Exactly the elements
that §10.1 determined compose.

### 10.3 Boundedness

**Governance enters or leaves a closure only by declaration.**

- **Nothing enters undeclared.** An element that applies without §10.1 establishing it is governance
  nobody admitted. Its effect looks the same as a mechanism's behavior.
- **Nothing escapes undeclared.** A subject for which no applicable closure can be established is
  ungoverned. Suppose a subject can become ungoverned in a system without a determination making it
  so. That system has a hole in it, not a gap. A subject outside one closure while inside another is
  not ungoverned. Closure is per subject, and it is not globally unique.
- **The closure is enumerable.** A system can state, finitely, what applies to a subject before any
  determination over that subject begins (Semantic Model §7).

### 10.4 Failure

Sometimes a closure cannot be established. An element may be unresolvable, an authority undeclared or
undemonstrated, a scope indeterminate, or an import unbounded. Then **the determination is `refuse`**
(SM-4, AI-6).

This is a closure-failure determination, not the outcome of evaluating rules. The rule set could not
be established, so no rule was evaluated. A system that reports the two alike misdirects every
remedy. Declaration repairs a closure failure. Changing what was proposed repairs a rule refusal.

## 11. Normative invariants

- **CA-1.** Authority, ownership, scope, concern, admission, inheritance, and import MUST be
  separately determinable, and none MUST be inferred from another (§2).
- **CA-2.** An authority MUST exist by a declared constituting act. It MUST NOT be constituted by
  need, precedence, containment, naming, or classification (§3.1).
- **CA-3.** A purported authority MUST answer all five questions of §3.2 from declared artifacts
  alone, or MUST NOT be admitted as an authority.
- **CA-4.** The authority constituting and exercising a jurisdiction MUST be distinguishable from the
  authority whose subjects it governs (§3.3).
- **CA-5.** A delegation MUST be declared, MUST NOT exceed its source, and MUST NOT transfer
  answerability (§3.4).
- **CA-6.** A concern classification MUST NOT constitute an authority or a jurisdiction (§5).
- **CA-7.** A governing element MUST declare its scope as a set of subjects. Scope MUST NOT be
  represented by the absence of a boundary, or by an unbounded assertion of everything (§5.1).
- **CA-8.** Inheritance MUST be declared. Containment MUST NOT carry governance of itself (§7).
- **CA-9.** Import MUST be declared by the receiving closure and MUST be enumerable. It MUST NOT
  extend the imported element's authority (§8).
- **CA-10.** A closure MUST be fully established before any determination over its subject. It MUST
  be enumerable before evaluation begins (§10.1, §10.3).
- **CA-11.** No governing element may apply to a subject without having been established in that
  subject's closure (§10.3).
- **CA-12.** Where a closure cannot be established, the determination MUST be `refuse`. That
  determination MUST be distinguishable from a rule refusal (§10.4).

## 12. Conformance

The conformance subject of this document is a **closure determination**: the account a system gives,
for a subject, of what governs it and by what right.

A closure determination conforms when all of the following hold:

- Every applicable element was established by declaration, declared inheritance or declared import,
  and none by position (CA-11, AI-2).
- Every authority under which an element applies satisfies §3.2 and §3.3 (CA-3, CA-4).
- Every element's scope is a stated set that reaches the subject (CA-7).
- The closure was enumerable before evaluation and complete at determination (CA-10).
- A closure that could not be established produced a refusal distinguishable from a rule refusal
  (CA-12).

This document leaves two things undecided. A conforming system may settle either one either way:

- **Whether any particular arrangement of authorities is legitimate.** §3.2 and §3.3 are the test.
  Whether a given domain, region or boundary passes it is a determination about that system, made
  under its own governance.
- **How authority, concern and scope are represented.** They must remain separately determinable
  (CA-1, GO-11, MB-7). This document does not specify the form.
