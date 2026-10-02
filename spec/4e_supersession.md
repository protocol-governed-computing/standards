# Supersession

## 1. Scope

This document specifies **supersession**: how one governed thing is stood down in favour of another,
and what a reference to the stood-down thing means afterwards.

This document closes Part IV. Identity & Addressing specifies what an identity is, and states that
identity carries no ordering. This document specifies the relation that supplies the ordering
identity lacks. Governed Transformation specifies how a system changes. This document specifies what
becomes of what it changed.

Its subject is **any governed thing**: an artifact, a kind, a category, a profile, a snapshot, and,
reflexively, a document in this family (§9).

This document introduces the terms **successor**, **predecessor**, **referential closure**, and
**retirement**.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What supersession is

**Supersession is a declared relation between two exact identities.** Where `X` supersedes `Y`, `X`
is the **successor** and `Y` the **predecessor**. The relation is a governed fact like any other:
declared, admitted, determined and evidenced.

Supersession is **not a resolution rule.** A reference names an exact identity and keeps naming it.
Supersession never makes a reference resolve somewhere else. Nothing is silently redirected,
upgraded or aliased.

The whole document turns on this distinction. A resolution rule would make a reference mean different
things at different times. A system's meaning would then depend on when someone read it.

**Deleting, renaming, deprecating in prose or abandoning a thing does not supersede it** (Conceptual
Model, *supersession*). Those are events. Supersession is a declaration.

## 3. Supersession is declared on the successor

The relation is stated **once, on the thing being authored**. The successor names its predecessor.

- Construction establishes both sides from that one declaration: the successor's claim and the
  predecessor's stood-down state. **A relation stated twice can disagree with itself.** One of the two
  statements would then be authoritative, with nothing saying which.
- A successor that names no predecessor supersedes nothing. A predecessor recorded as superseded by
  nothing is a defect, and MUST be refused.
- This document does not specify what form the declaration takes.

## 4. Referential closure

> **Where `X` supersedes `Y`, nothing in the governed system may reference `Y`.**

This rule makes supersession mean something rather than merely record something. Without it, a
stood-down thing is annotated and still carries weight. The annotation then misleads every reader who
trusts it.

- The requirement is **strict**: *no* reference, not just *no executable reference*. **A system that
  mentions a retired identity has not finished retiring it.**
- **The rule forbids a dependency on the predecessor, not the record of its retirement.** The
  supersession declaration that SU-3 requires necessarily names `Y`. It is the one reference that does
  not make `Y` carry weight. It is what establishes that `Y` does not. Excluding it does not weaken the
  strictness above. Every other mention stays forbidden, including a mention in prose. A realization
  that cannot tell the two apart has not implemented referential closure.
- Closure MUST be determined during construction, with every other reference obligation (AI-5,
  GC-3). A dangling reference to a superseded thing MUST refuse the composition.
- Closure is a **composition obligation** (GC-11). It quantifies over the whole, and no part can
  discharge it. Each domain may be free of such references and still compose into a system that is
  not.

So retiring something is **not complete when the successor exists.** It is complete when nothing
refers to the predecessor. Re-pointing the referrers is part of the transformation that retires it,
not follow-up work.

## 5. Unreachable is not absent

A superseded thing is **excluded from what can be reached** and **retained in what can be examined**.

| | Superseded thing |
|---|---|
| reachable by execution | no — excluded from every projection execution consumes |
| reachable by reference | no — referential closure forbids it (§4) |
| present in the canonical record | **yes** |
| visible to inspection | **yes** |

**Reachability is determined within the composition.** The rows above state what the composition's own
closure establishes. A party outside the composition may name a superseded identity directly. That
closure does not constrain such a party. The reason is not that the supersession is incomplete. The
composition cannot enumerate parties it does not carry. Such a party is informed, not prevented (§8).

**The record of what a system once contained is evidence.** Removing it destroys the ability to
establish what the system was at some earlier point. Evidence exists to preserve exactly that (EV-1).
A system that cannot answer *what was authoritative last year* has lost something no current
correctness can recover.

So a superseded thing stops being reachable. It does not stop having existed.

## 6. Retirement is not deletion

**No mechanism deletes.** Construction, sealing, the agent performing execution and inspection all
leave retired things in place.

A retired thing stays where it is, with its stood-down state declared. **Deletion is a separate,
deliberate human act.** Someone takes it if and when they decide the history is no longer worth
carrying. Deletion is not supersession. It produces no governed relation and leaves no successor.

A mechanism that deleted on supersession would make retirement and destruction the same act. Every
retirement would then be irreversible by default.

## 7. Supersession and amendment

Supersession and amendment are **both available**, and they are different acts:

| | Changes | Predecessor |
|---|---|---|
| **amendment** | the thing itself, in place — a whole redeclaration (TR-19) | there is none; there is one thing, changed |
| **supersession** | nothing; a new thing exists and the old is stood down | retained, unreachable |

- **Amendment is the ordinary case.** Nothing here mandates supersession. A system that supersedes on
  every change has made every change a cascade.
- A system chooses supersession where the predecessor's identity must stay distinguishable. That is
  the case when something claimed it, executed under it, or must be able to name it later.
- **A change of declared semantics is a new identity** (ID-5). Whether the old identity is then
  superseded or simply falls out of use is a separate declaration. Falling out of use is not
  supersession (§2).

**What amendment may change follows from this, and is worth stating outright.** Amendment covers
everything about a declaration except its declared semantics. That includes representation,
encoding, presentation, correction of a rendering, and anything KV-8 already says does not increment
a version. **An in-place change to declared semantics is not an amendment.** It is a new identity
written over the old one. Every reference to the old identity now resolves to something it was not
admitted against.

How much text moved does not tell the two apart. A whole redeclaration that leaves the declared
semantics identical is an amendment. A single field change that alters what the artifact means is
not, however small the edit looks in a diff.

## 8. What supersession invalidates

Supersession has a blast radius, and it differs by subject. **Each one is a determination to make,
not a consequence to discover afterwards:**

| Superseded | Invalidates |
|---|---|
| **an artifact** | every reference to it, which MUST be re-pointed or itself retired (§4) |
| **a kind** | every artifact declared under it, every contract referencing it, and every projection derived from those artifacts (Kind Vocabulary §6) |
| **a semantic category** | every category contract, every kind classification, and every cross-cutting obligation stated in terms of it (Governance Semantic Ontology §9) |
| **a profile** | nothing retroactively — systems that claimed the predecessor claimed what they claimed; whether they satisfy the successor is a fresh question (Normative Platform Profile §9) |
| **a snapshot** | nothing already executed; the successor becomes the baseline, and the predecessor remains what it was |

People most often get the profile row wrong. **A superseded profile does not reach backwards.** A
claim discharged against it was discharged against it, and stays so. Re-evaluating that claim against
the successor is a new evaluation with a new result (CF-1).

**A blast radius is determined over the composition.** A supersession MUST determine what within the
composition it affects. It cannot determine what outside the composition holds the predecessor's
identity. A composition that cannot enumerate its callers cannot enumerate what to include.
**Superseding does not redirect a caller. The caller moves.** A party that keeps naming a predecessor
is refused by it. That is correct behaviour by an artifact whose caller nobody has told it is retired.

This is a limit on what a supersession can determine. It does not permit leaving the blast radius
undetermined. Where a system does know its external callers, informing them is that system's
obligation. It is not a property of the supersession relation.

## 9. This family supersedes itself the same way

The documents of this family are governed things. **Their revision is supersession in exactly the
sense above.** It is the same reflexive move that makes governance govern itself (Governance Standard
§6).

- **A revision of a document supersedes the revision it replaces.** The relation is declared, not
  inferred from a number or a date.
- **Referential closure applies.** A family document that refers to a superseded revision of another
  is a defect in this family, found the same way.
- **The blast radius applies.** Revising a term in Part I invalidates every document that used it.
  Revising an invariant invalidates every conformance claim discharged against it.
- **A claim is against a named revision** (CF-1). A later revision does not reach backwards into
  claims discharged against an earlier one. Profiles follow the same rule (§8).

No outer mechanism governs the family's evolution. There is this document, applied to itself.

## 10. What this document does not specify

- **The form of the declaration**: how a successor names a predecessor, or how a stood-down state is
  expressed.
- **What projections a system carries**, and so which ones exclusion operates over. A profile selects
  them (Projection Standard; Normative Platform Profile §7).
- **Whether any particular thing should be superseded or amended.** A system determines that under
  its own governance.
- **Retention periods** for what is retained but unreachable. That is a profile's question (Evidence,
  Attestation & Provenance §11).
- **How a revision of this family is proposed, reviewed and admitted.** That is process, not
  semantics. It belongs with the family's own membership rules (Open PGC Standard — Document Set §5).
- **How a system informs parties outside the composition** that an identity they hold has been
  superseded (§8).

## 11. Normative invariants

- **SU-1.** Supersession MUST be a declared relation between two exact identities, and MUST NOT cause
  any reference to resolve to a different identity (§2).
- **SU-2.** Nothing MUST be treated as superseded by deletion, renaming, deprecation in prose, or
  disuse (§2).
- **SU-3.** The relation MUST be declared once, on the successor. Both sides MUST be established from
  that declaration (§3).
- **SU-4.** A predecessor recorded as superseded by nothing MUST be refused (§3).
- **SU-5.** Where `X` supersedes `Y`, nothing in the governed system MUST reference `Y` other than the
  supersession declaration SU-3 requires, and the closure MUST be determined during construction
  (§4).
- **SU-6.** Referential closure MUST be determined over the whole composition (§4).
- **SU-7.** A superseded thing MUST be excluded from every projection execution consumes, and MUST be
  retained in the canonical record and reachable by inspection (§5).
- **SU-8.** No mechanism MUST delete a superseded thing (§6).
- **SU-9.** A supersession MUST determine its blast radius over the composition rather than leaving
  it to be discovered. It MUST NOT be treated as determining the state of parties the composition does
  not carry (§8).
- **SU-10.** A superseded profile or family revision MUST NOT retroactively alter claims discharged
  against it (§8, §9).
- **SU-11.** An amendment MUST NOT change an artifact's declared semantics. Such a change MUST be a
  new identity (§7, ID-5).

## 12. Conformance

The conformance subject of this document is a **supersession**: a declared relation between two
identities, together with the state of the composition that carries it.

A supersession conforms when all of the following hold:

- it is declared on the successor;
- both sides are established from that declaration;
- nothing in the composition references the predecessor;
- the predecessor is unreachable and retained;
- nothing was deleted;
- the invalidation its subject implies was determined.

**The dangling reference is the demonstration.** A party establishes a supersession by exhibiting a
composition in which a reference to the predecessor survives, and showing that it is refused. A system
whose supersessions have never refused anything has not established that its closure check can fire.
The first real retirement is a poor moment to discover that (CD-4).
