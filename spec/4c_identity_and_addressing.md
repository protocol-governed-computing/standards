# Identity & Addressing

## 1. Scope

This document specifies two subjects, and it emphasizes the separation between them:

- **Identity** answers *what is this?*
- **Addressing** answers *how is it reached?*

This document specifies them together for two reasons. **Neither may substitute for authority,
ownership, concern or governance.** And keeping the two apart is itself the normative content. Every
other document in this family may treat one subject. This one exists to state that these two are not
one subject, and what goes wrong when someone treats them as one.

The Machine Block Standard requires that identity be declared in the envelope and be authoritative
over position. This document says what identity *is*. The Snapshot Standard defers the structure and
resolution of identity to this document. Governed Construction requires that references resolve.
This document says what resolution means.

This document introduces the terms **address**, **namespace**, and **composite identity**, and
refines the Conceptual Model's **resolution** for identity and addressing. The Conceptual Model, the
Semantic Model or Parts II–IV defines every other term it uses.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Identity

**An identity is what makes a governed thing that thing.** It is the answer that stays the same
through every change that does not change what the thing is.

### 2.1 Identity is declared

An artifact's identity is **declared**, and it is authoritative over every other signal (MB-6,
AI-2).

It MUST NOT be derived from:

| Not from | Because |
|---|---|
| a filename or path | a thing does not become a different thing by being moved |
| a containing document or region | containment is location, and location identifies nothing |
| a position or ordering | order is a property of a mechanism, not of a thing |
| a naming convention or prefix | a convention describes; it does not constitute |
| the manner of its discovery | **a thing does not acquire identity by being found** |

The last row is the sharpest. Locating something does not identify it. What was found is whatever its
governed representation declares. Where nothing is declared, nothing was identified. Something was
only encountered.

### 2.2 Identity is over the semantic object

Identity is defined over the **semantic object**, not over any encoding of it (MB-3).

- Two encodings that resolve to the same semantic object bear the same identity. Key order,
  whitespace and container syntax are not identity.
- **A representation change that keeps the meaning does not change identity** (KV-8).
- **A change of identity is itself a governed change.** It follows from a determination that the
  declared semantics differ (§2.4). Movement, re-addressing, re-indexing and observation cannot
  change identity.
- To compute identity, a realization needs a canonical form over which identity is determined. **This
  document requires that one exist, but it specifies no scheme.** A realization may adopt any scheme
  that yields one identity for one semantic object.

### 2.3 Uniqueness

Within the scope where it has meaning, an identity denotes exactly one thing.

- **Two admitted things bearing one identity is a defect.** It is not a coincidence to resolve by
  precedence, recency or position. It MUST be refused (MB-1, GC-12).
- One thing bearing two identities is also a defect. To anything that compares by identity, the
  thing becomes two things. The divergence appears only when someone compares the two.

### 2.4 Identity and version

A version identifies an artifact's **semantics** (Conceptual Model, *version*). It follows that:

- **Two versions are two artifacts.** Each has its own identity. A declared relation relates them,
  not a resemblance of name.
- A change of semantics is a new identity. A change of representation that keeps the semantics is
  not (KV-8, §2.2).
- **Identity carries no ordering.** That one identity supersedes another is a declared relation.
  Nobody can derive it by comparing identities, even where a naming convention makes an order look
  obvious. Supersession owns what supersession means.

## 3. Addressing

An **address** is a means of reaching a thing. **Resolution** is the act of turning an address into
the thing it reaches.

### 3.1 An address is a means, not a claim

An address says where to look or how to ask. **It makes no claim about what will be found.** That
claim is the identity declared as part of whatever governed representation is found there.

- An address MUST NOT be treated as an assertion of identity.
- An address tells you where to look. It does not tell you what you found. Reaching something
  establishes only that something was reached. What it *is* comes from the identity declared as part
  of its governed representation (§2.1, MB-6). Nothing identifies itself by assertion outside that
  declaration surface.

### 3.2 Many addresses, one identity

- One thing MAY be reachable through many addresses. None of them is its identity, and **none
  establishes a more authoritative identity than another**. A realization may of course prefer one
  address for operational reasons, such as locality, cost or availability. Operational preference is
  a mechanism decision (RT-5). It settles nothing about what the thing is.
- An address MAY change **while the identity stays the same**. A thing may be relocated, re-hosted or
  re-indexed.
- An address MAY stop resolving. That is a failure of reach, not a change in what the thing is.

## 4. The separation

Two rules apply, one in each direction. Each prevents a failure:

### 4.1 Identity MUST NOT be derived from addressing

If identity derives from address, then **moving a thing changes what it is**. Every downstream
consequence follows:

- a reference that resolved yesterday resolves to something with a different identity today;
- a snapshot's composite identity changes when nothing governed changed;
- two copies of one artifact in two locations become two artifacts.

Most damaging of all, **governance follows identity**. So a thing whose identity changed by moving has
silently changed what governs it. No determination anywhere records the change. A change of identity
requires a governed determination, never a change of location.

### 4.2 Addressing MUST NOT redefine identity

If addressing can redefine identity, then **what a thing is depends on how it was reached**. The same
artifact, resolved by two paths, becomes two things. Or it becomes one thing whose identity depends on
who asks.

- A resolution mechanism MUST NOT assign, alter, normalize, or complete an identity.
- An address may resolve to something whose declared identity differs from what was expected. **That
  is a finding and MUST be refused.** It is never reconciled by preferring one identity over the
  other.

### 4.3 Neither is the other's authority, and neither is attestation

Neither identity nor addressing establishes **authority** (CA-1). That a thing can be reached says
nothing about what may reach it. That a thing is identified says nothing about what it may do.
Identity, addressing, authority and concern are four separate questions. None can be recovered from
another (GO-11, MB-7).

**Nor does attestation create identity.** An attestation about an identity claim is evidence about a
declared identity. It asserts that some party vouches for something about it (EV-9). It does not
constitute the identity. A signature, certificate or endorsement is not a source of identity. Where
an attested claim and a declared identity differ, the declaration governs, and the attestation is
about something else.

## 5. Namespaces

A **namespace** is a mechanism for carrying and resolving **names that reference identity**. It
bounds the scope within which a name denotes one thing. The identity stays with the governed thing. A
namespace supplies the naming context in which others can refer to it.

**A namespace carries identity. It does not carry authority, concern or federation** (GO-11).

- Two things that share a namespace have their names resolved together. That establishes nothing
  about who governs them, what subject they concern, or whether they belong to one jurisdiction.
- **A namespace is not an ownership boundary.** A system's namespaces may coincide with its
  authorities. That coincidence is a property of that system's arrangement, not a consequence of
  namespaces.
- A namespace MUST NOT be used to encode authority or concern alongside identity (GO-11, MB-7). An
  identifier that carries two of these makes them indistinguishable to any check, whatever is
  declared elsewhere.

This document does not specify what form a namespace takes, how it is expressed, or what a system's
namespaces are.

## 6. Reference and resolution

*Refining the Conceptual Model's* **resolution**: the Conceptual Model states what resolution is.
This section states what resolution must do where it resolves an identity.

- **Artifacts reference one another by declared identity** (MB-6). They never reference by name
  resemblance, path, position or proximity.
- **Resolution completes before anything that depends on it proceeds** (AI-5, GC-3). An unresolved
  reference is a failure of the activity that required it, never a condition discovered later.
- **Resolution is total or it refuses.** There is no partial resolution, no best match, no most likely
  candidate and no fallback to a default (AI-6).
- **Resolution MUST NOT search.** Where an address is ambiguous, resolution refuses. It does not
  choose among what it found. Selecting a candidate is a determination, and resolution holds no
  authority to make one.

An unresolvable reference is not a gap to work around. It means something references a thing that is
not in the system. Admitting it anyway would create a dependency on something no closure governs.

## 7. Composite identity

A composition of governed things has an identity of its own, a **composite identity**, derived from
the identities of its constituents (SN-2).

- **A composite identity is a function of its constituents' identities.** If any constituent changes,
  the composite identity changes. If every constituent stays the same, it stays the same.
- **A composite identity is not a name for a set.** Two compositions of the same constituents are the
  same composition. Two compositions that differ in one constituent are different, whatever they are
  called.
- **No constituent carries the composite identity**, and none can compute it alone (GC-11). The
  composite exists only over the whole.

That is why comparing composite identities compares the systems, not their descriptions. An identity
derived from constituents cannot agree while the constituents differ.

## 8. What this document does not specify

- **The form of an identity**: its syntax, its structure, whether it is hierarchical, and what
  separates its parts.
- **The form of an address**, and whether identity and address are expressed alike or differently.
- **A canonicalization scheme** (§2.2). One must exist. This document does not say which.
- **What namespaces a system has**, or how they are arranged. That is a profile's question.
- **What supersession means** between two identities. That is Supersession's subject.
- **How authority and concern are represented.** They must be separately expressible (GO-11, MB-7).
  The representation is unspecified.

## 9. Normative invariants

- **ID-1.** An identity MUST be declared and MUST be authoritative over filename, path, containment,
  position, convention, and manner of discovery (§2.1).
- **ID-2.** Nothing MUST acquire identity by being found (§2.1).
- **ID-3.** Identity MUST be defined over the semantic object, and a representation change preserving
  meaning MUST NOT change identity (§2.2).
- **ID-4.** Two admitted things bearing one identity MUST be refused (§2.3).
- **ID-5.** A change of declared semantics MUST be a new identity (§2.4).
- **ID-6.** Identity MUST NOT carry ordering. Supersession MUST be a declared relation (§2.4).
- **ID-7.** An address MUST NOT be treated as an assertion of identity (§3.1).
- **ID-8.** A change of address MUST NOT change identity (§3.2, §4.1).
- **ID-9.** Identity MUST NOT be derived from an address (§4.1).
- **ID-10.** A resolution mechanism MUST NOT assign, alter, normalize, or complete an identity
  (§4.2).
- **ID-11.** Where a resolved thing's declared identity differs from what was expected, the
  difference MUST be refused (§4.2).
- **ID-12.** A namespace MUST NOT establish authority, concern, or federation, and MUST NOT encode
  them alongside identity (§5).
- **ID-13.** References MUST be by declared identity, and resolution MUST complete before anything
  depending on it proceeds (§6).
- **ID-14.** Resolution MUST NOT search, select among candidates, or fall back. An ambiguous or
  unresolvable reference MUST be refused (§6).
- **ID-15.** A composite identity MUST be derived from its constituents' identities, and MUST change
  when any constituent changes (§7).

## 10. Conformance

The conformance subject of this document is an **identity scheme**: how a governed system identifies
its things, how it addresses them, and how it resolves references between them.

An identity scheme conforms when all of the following hold:

- identities are declared and authoritative over position;
- identities are defined over semantic objects;
- identities are unique within their scope;
- relocation leaves identities unchanged;
- addresses are treated as means, not claims;
- resolution refuses instead of searching;
- neither identity nor addressing carries authority or concern.

**Relocation is the decisive test.** Move a governed thing: change its path, its container, its
address, or the order in which it is encountered. Nothing about its identity, its governance, or the
composite identity of anything containing it may change. A scheme that survives relocation has
declared its identity. A scheme that does not has been deriving identity from address, however
plainly it says otherwise.

The Conformance Test Specification owns how this is required and evaluated.
