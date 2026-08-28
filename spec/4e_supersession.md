# Supersession

## 1. Scope

This document specifies **supersession**: how one governed thing is stood down in favour of another,
and what a reference to the stood-down thing means afterwards.

It closes Part IV. Identity & Addressing specifies what an identity is and states that identity
carries no ordering; this document specifies the relation that supplies the ordering identity does
not. Governed Transformation specifies how a system changes; this document specifies what becomes of
what it changed.

Its subject is **any governed thing**: an artifact, a kind, a category, a profile, a snapshot — and,
reflexively, a document of this family (§9).

This document introduces the terms **successor**, **predecessor**, **referential closure**, and
**retirement**.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What supersession is

**Supersession is a declared relation between two exact identities.** Where `X` supersedes `Y`, `X`
is the **successor**, `Y` the **predecessor**, and the relation is a governed fact like any other:
declared, admitted, determined, and evidenced.

It is **not a resolution rule.** A reference names an exact identity and continues to name it;
supersession never causes a reference to resolve somewhere else. Nothing is silently redirected,
upgraded, or aliased.

This is the distinction the whole document turns on. A resolution rule would make a reference mean
different things at different times, and a system's meaning would depend on when it was read.

**Nothing is superseded by being deleted, renamed, deprecated in prose, or left unused** (1a). Those
are events; supersession is a declaration.

## 3. Supersession is declared on the successor

The relation is stated **once, on the thing being authored**: the successor names its predecessor.

- Construction establishes both sides from that one declaration — the successor's claim and the
  predecessor's stood-down state. **A relation stated twice can disagree with itself**, and one of
  the two statements would then be authoritative without anything saying which.
- A successor naming no predecessor supersedes nothing. A predecessor recorded as superseded by
  nothing is a defect, and MUST be refused.
- What form the declaration takes is not specified here.

## 4. Referential closure

> **Where `X` supersedes `Y`, nothing in the governed system may reference `Y`.**

This is what makes supersession mean something rather than record something. Without it, a
stood-down thing is annotated and still load-bearing, and the annotation misleads every reader who
trusts it.

- The requirement is **strict**: *no* reference, not *no executable reference*. **A system that
  mentions a retired identity has not finished retiring it.**
- **What is forbidden is a dependency on the predecessor, not the record of its retirement.** The
  supersession declaration SU-3 requires necessarily names `Y`, and is the one reference that does
  not make `Y` load-bearing — it is what establishes that `Y` is not. Excluding it is not a
  weakening of the strictness above: every other mention remains forbidden, including a prose one,
  and a realization that cannot tell the two apart has not implemented referential closure.
- Closure MUST be determined during construction, with every other reference obligation (AI-5,
  GC-3). A dangling reference to a superseded thing MUST refuse the composition.
- Closure is a **composition obligation** (GC-11): it quantifies over the whole, and no part can
  discharge it. A domain individually free of such references may still compose into a system that
  is not.

Retiring something is therefore **not complete when the successor exists.** It is complete when
nothing refers to the predecessor — and the work of re-pointing referrers is part of the
transformation that retires it, not follow-up.

## 5. Unreachable is not absent

A superseded thing is **excluded from what can be reached** and **retained in what can be examined**.

| | Superseded thing |
|---|---|
| reachable by execution | no — excluded from every projection execution consumes |
| reachable by reference | no — referential closure forbids it (§4) |
| present in the canonical record | **yes** |
| visible to inspection | **yes** |

**Reachability is determined within the composition.** The rows above state what the composition's
own closure establishes. A party outside the composition that names a superseded identity directly is
not constrained by that closure — not because the supersession is incomplete, but because the
composition cannot enumerate parties it does not carry. Such a party is informed, not prevented
(§8).

**The record of what a system once contained is evidence.** Removing it destroys the ability to
establish what the system was at some earlier point, which is the thing evidence exists to preserve
(EV-1). A system that cannot answer *what was authoritative last year* has lost something no current
correctness recovers.

So: it stops being reachable. It does not stop having existed.

## 6. Retirement is not deletion

**No mechanism deletes.** Not construction, not sealing, not the agent performing execution, not
inspection.

A retired thing remains where it is, with its stood-down state declared. **Deletion is a separate,
deliberate human act**, taken if and when someone decides the history is no longer worth carrying —
and it is not supersession, produces no governed relation, and leaves no successor.

A mechanism that deleted on supersession would make retirement and destruction the same act, and
every retirement would be irreversible by default.

## 7. Supersession and amendment

Supersession and amendment are **both available**, and they are different acts:

| | Changes | Predecessor |
|---|---|---|
| **amendment** | the thing itself, in place — a whole redeclaration (TR-19) | there is none; there is one thing, changed |
| **supersession** | nothing; a new thing exists and the old is stood down | retained, unreachable |

- **Amendment is the ordinary case.** Nothing here mandates supersession, and a system that
  supersedes on every change has made every change a cascade.
- Supersession is chosen where the predecessor's identity must remain distinguishable — because
  something claimed it, executed under it, or must be able to name it later.
- **A change of declared semantics is a new identity** (ID-5). Whether the old identity is then
  superseded or simply ceases to be used is a separate declaration; ceasing to be used is not
  supersession (§2).

**What amendment may change follows from that, and is worth stating rather than inferring.**
Amendment is available for everything about a declaration that is not its declared semantics —
representation, encoding, presentation, correction of a rendering, anything KV-8 already says does
not increment a version. **An in-place change to declared semantics is not an amendment.** It is a
new identity that has been written over the old one, and every reference to the old identity now
resolves to something it was not admitted against.

The two are not distinguished by how much text moved. A whole redeclaration that leaves the declared
semantics identical is an amendment; a single field whose change alters what the artifact means is
not, however small the edit looks in a diff.

## 8. What supersession invalidates

Supersession has a blast radius, and it differs by subject. **Each is a determination to be made,
not a consequence to be discovered afterwards:**

| Superseded | Invalidates |
|---|---|
| **an artifact** | every reference to it, which MUST be re-pointed or itself retired (§4) |
| **a kind** | every artifact declared under it, every contract referencing it, and every projection derived from those artifacts (2d §6) |
| **a semantic category** | every category contract, every kind classification, and every cross-cutting obligation stated in terms of it (2b §9) |
| **a profile** | nothing retroactively — systems that claimed the predecessor claimed what they claimed; whether they satisfy the successor is a fresh question (6a §9) |
| **a snapshot** | nothing already executed; the successor becomes the baseline, and the predecessor remains what it was |

The profile row is the one most often got wrong. **A superseded profile does not reach backwards.**
A claim discharged against it was discharged against it, and remains so; re-evaluating that claim
against the successor is a new evaluation with a new result (CF-1).

**A blast radius is determined over the composition.** A supersession MUST determine what within the
composition is affected. It cannot determine what outside the composition holds the predecessor's
identity, because a composition that cannot enumerate its callers cannot enumerate what to include.
**Superseding does not redirect a caller: the caller moves.** A party that goes on naming a
predecessor is refused by it, which is correct behaviour by an artifact nobody has told it is
retired.

This is a limit on what a supersession can determine, not a permission to leave it undetermined.
Where a system does know its external callers, informing them is that system's obligation and not a
property of the supersession relation.

## 9. This family supersedes itself the same way

The documents of this family are governed things, and **their revision is supersession in exactly
the sense above** — the same reflexive move that makes governance govern itself (2a §6).

- **A revision of a document supersedes the revision it replaces**, and the relation is declared
  rather than inferred from a number or a date.
- **Referential closure applies.** A family document referring to a superseded revision of another
  is a defect in this family, found the same way.
- **The blast radius applies.** Revising a term in Part I invalidates every document that used it;
  revising an invariant invalidates every conformance claim discharged against it.
- **A claim is against a named revision** (CF-1), and a later revision does not reach backwards into
  claims discharged against an earlier one — the same rule as profiles (§8).

There is no outer mechanism governing the family's evolution. There is this document, applied to
itself.

## 10. What this document does not specify

- **The form of the declaration** — how a successor names a predecessor, or how a stood-down state
  is expressed.
- **What projections a system carries**, and therefore which ones exclusion operates over. A
  profile's selection (4b, 6a §7).
- **Whether any particular thing should be superseded or amended.** A determination made under a
  system's own governance.
- **Retention periods** for what is retained but unreachable. A profile's question (3e §11).
- **How a revision of this family is proposed, reviewed, and admitted.** That is process rather than
  semantics, and belongs with the family's own membership rules (0z §5).
- **How a system informs parties outside the composition** that an identity they hold has been
  superseded (§8).

## 11. Normative invariants

- **SU-1.** Supersession MUST be a declared relation between two exact identities, and MUST NOT
  cause any reference to resolve to a different identity (§2).
- **SU-2.** Nothing MUST be treated as superseded by deletion, renaming, deprecation in prose, or
  disuse (§2).
- **SU-3.** The relation MUST be declared once, on the successor; both sides MUST be established
  from that declaration (§3).
- **SU-4.** A predecessor recorded as superseded by nothing MUST be refused (§3).
- **SU-5.** Where `X` supersedes `Y`, nothing in the governed system MUST reference `Y` other than
  the supersession declaration SU-3 requires, and the
  closure MUST be determined during construction (§4).
- **SU-6.** Referential closure MUST be determined over the whole composition (§4).
- **SU-7.** A superseded thing MUST be excluded from every projection execution consumes, and MUST
  be retained in the canonical record and reachable by inspection (§5).
- **SU-8.** No mechanism MUST delete a superseded thing (§6).
- **SU-9.** A supersession MUST determine its blast radius over the composition rather than leaving
  it to be discovered, and MUST NOT be treated as determining the state of parties the composition
  does not carry (§8).
- **SU-10.** A superseded profile or family revision MUST NOT retroactively alter claims discharged
  against it (§8, §9).
- **SU-11.** An amendment MUST NOT change an artifact's declared semantics; such a change MUST be a
  new identity (§7, ID-5).

## 12. Conformance

The conformance subject of this document is a **supersession**: a declared relation between two
identities, together with the state of the composition that carries it.

A supersession conforms when it is declared on the successor, both sides are established from that
declaration, nothing in the composition references the predecessor, the predecessor is unreachable
and retained, nothing was deleted, and the invalidation its subject implies was determined.

**The demonstration is the dangling reference.** A supersession is established by exhibiting a
composition in which a reference to the predecessor survives, and showing that it is refused. A
system whose supersessions have never refused anything has not established that its closure check
can fire — and the first real retirement is a poor moment to discover it (CD-4).
