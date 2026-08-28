# Identity & Addressing

## 1. Scope

This document specifies two subjects and, above all, the separation between them:

- **Identity** answers *what is this?*
- **Addressing** answers *how is it reached?*

They are specified here because **neither may be used as a substitute for authority, ownership,
concern, or governance** — and because keeping the two apart is itself the normative content. Every
other document in this family may treat one subject per document; this one exists to state that
these two are not one subject, and what goes wrong when they are treated as one.

The Machine Block Standard requires that identity be declared in the envelope and be authoritative
over position; this document says what identity *is*. The Snapshot Standard defers the structure and
resolution of identity here. Governed Construction requires that references resolve; this document
says what resolution means.

This document introduces the terms **address**, **namespace**, and **composite identity**, and
refines the Conceptual Model's **resolution** for identity and addressing. Every other term it uses is defined by the Conceptual Model, the Semantic Model, or
Parts II–IV.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Identity

**An identity is what makes a governed thing that thing** — the answer that stays the same through
everything that does not change what it is.

### 2.1 Identity is declared

An artifact's identity is **declared**, and is authoritative over every other signal (MB-6, AI-2).

It MUST NOT be derived from:

| Not from | Because |
|---|---|
| a filename or path | a thing does not become a different thing by being moved |
| a containing document or region | containment is location, and location identifies nothing |
| a position or ordering | order is a property of a mechanism, not of a thing |
| a naming convention or prefix | a convention describes; it does not constitute |
| the manner of its discovery | **a thing does not acquire identity by being found** |

The last is the sharpest. Something located is not thereby identified: what was found is whatever
its governed representation declares, and where nothing is declared, nothing was identified — only
encountered.

### 2.2 Identity is over the semantic object

Identity is defined over the **semantic object**, not over any encoding of it (MB-3).

- Two encodings that resolve to the same semantic object bear the same identity. Key order,
  whitespace, and container syntax are not identity.
- **A representation change that preserves meaning does not change identity** (KV-8).
- **A change of identity is itself a governed change.** It follows from a determination that the
  declared semantics differ (§2.4); it cannot occur through movement, re-addressing, re-indexing, or
  observation.
- Making this computable requires a canonical form over which identity is determined. **This
  document requires that one exist; it specifies no scheme**, and a realization may adopt any that
  yields one identity for one semantic object.

### 2.3 Uniqueness

Within the scope in which it is meaningful, an identity denotes exactly one thing.

- **Two admitted things bearing one identity is a defect**, not a coincidence to be resolved by
  precedence, recency, or position. It MUST be refused (MB-1, GC-12).
- One thing bearing two identities is likewise a defect: it makes the thing two things to anything
  that compares by identity, and the divergence appears only when the two are compared.

### 2.4 Identity and version

A version identifies an artifact's **semantics** (Conceptual Model, *version*). It follows that:

- **Two versions are two artifacts**, each with its own identity, related by a declared relation and
  not by resemblance of name.
- A change of semantics is a new identity. A change of representation that preserves semantics is
  not (KV-8, §2.2).
- **Identity carries no ordering.** That one identity supersedes another is a declared relation, not
  something derivable by comparing identities — even where a naming convention makes an order look
  obvious. What supersession means belongs to Supersession.

## 3. Addressing

An **address** is a means of reaching a thing. **Resolution** is the act of turning an address into
the thing it reaches.

### 3.1 An address is a means, not a claim

An address says where to look or how to ask. **It makes no claim about what will be found** — that
claim is the identity declared as part of whatever governed representation is found there.

- An address MUST NOT be treated as an assertion of identity.
- Reaching something through an address does not establish that it is what the address suggested. It
  establishes only that something was reached; what it *is* comes from the identity declared as part
  of its governed representation (§2.1, MB-6). Nothing identifies itself by assertion outside that
  declaration surface.

### 3.2 Many addresses, one identity

- One thing MAY be reachable through many addresses. None of them is its identity, and **none
  establishes a more authoritative identity than another**. A realization may of course prefer one
  address operationally — for locality, cost, or availability; operational preference is a mechanism
  decision (RT-5) and settles nothing about what the thing is.
- An address MAY change — a thing may be relocated, re-hosted, re-indexed — **without its identity
  changing.**
- An address MAY cease to resolve. That is a failure of reach, not a change in what the thing is.

## 4. The separation

Two rules, one in each direction, each with a failure it prevents:

### 4.1 Identity MUST NOT be derived from addressing

If identity is derived from address, then **moving a thing changes what it is**. Every downstream
consequence follows: a reference that resolved yesterday resolves to something with a different
identity today; a snapshot's composite identity changes when nothing governed changed; two copies of
one artifact in two locations become two artifacts.

Most damagingly, **governance follows identity** — so a thing whose identity changed by being moved
has silently changed what governs it, with no determination anywhere recording the change. A change
of identity requires a governed determination, never a change of location.

### 4.2 Addressing MUST NOT redefine identity

If addressing can redefine identity, then **what a thing is depends on how it was reached**. The same
artifact resolved by two paths becomes two things, or one thing whose identity depends on the
questioner.

- A resolution mechanism MUST NOT assign, alter, normalize, or complete an identity.
- Where an address resolves to something whose declared identity differs from what was expected,
  **that is a finding and MUST be refused** — never reconciled by preferring one over the other.

### 4.3 Neither is the other's authority, and neither is attestation

Neither identity nor addressing establishes **authority** (CA-1). That a thing can be reached says
nothing about what may reach it; that a thing is identified says nothing about what it may do.
Identity, addressing, authority, and concern are four separate questions, and none is recoverable
from another (GO-11, MB-7).

**Nor does attestation create identity.** An attestation about an identity claim is evidence
concerning a declared identity — it asserts that some party vouches for something about it (EV-9).
It does not constitute the identity, and a signature, certificate, or endorsement is not an identity
source. Where an attested claim and a declared identity differ, the declaration governs and the
attestation is about something else.

## 5. Namespaces

A **namespace** is a mechanism for carrying and resolving **names that reference identity**: it
bounds the scope within which a name denotes one thing. The identity remains with the governed
thing; a namespace supplies the naming context in which it can be referred to.

**A namespace carries identity. It does not carry authority, concern, or federation** (GO-11).

- That two things share a namespace establishes that their names are resolved together. It
  establishes nothing about who governs them, what subject they concern, or whether they belong to
  one jurisdiction.
- **A namespace is not an ownership boundary.** Where a system's namespaces coincide with its
  authorities, that coincidence is a property of that system's arrangement, not a consequence of
  namespaces.
- A namespace MUST NOT be used to encode authority or concern alongside identity (GO-11, MB-7). An
  identifier that carries two of these makes them indistinguishable to any check, whatever is
  declared elsewhere.

What form a namespace takes, how it is expressed, and what a system's namespaces are, this document
does not specify.

## 6. Reference and resolution

*Refining the Conceptual Model's* **resolution**: the Conceptual Model states what resolution is;
this section states what it must do where an identity is what is being resolved.

- **References between artifacts are by declared identity** (MB-6). Not by name resemblance, not by
  path, not by position, not by proximity.
- **Resolution completes before anything depending on it proceeds** (AI-5, GC-3). An unresolved
  reference is a failure of the activity that required it, never a condition discovered later.
- **Resolution is total or it refuses.** There is no partial resolution, no best match, no most
  likely candidate, and no fallback to a default (AI-6).
- **Resolution MUST NOT search.** Where an address is ambiguous, resolution refuses; it does not
  choose among what it found. Selecting a candidate is a determination, and resolution holds no
  authority to make one.

An unresolvable reference is not a gap to be worked around. It means something references a thing
that is not in the system, and admitting it anyway would place a dependency on something no closure
governs.

## 7. Composite identity

A composition of governed things has an identity of its own — a **composite identity** — derived
from the identities of its constituents (SN-2).

- **A composite identity is a function of its constituents' identities.** Change any constituent and
  the composite identity changes; leave every constituent unchanged and it does not.
- **A composite identity is not a name for a set.** Two compositions of the same constituents are the
  same composition; two compositions differing in one constituent are different, whatever they are
  called.
- **No constituent carries the composite identity**, and none can compute it alone (GC-11). The
  composite exists only over the whole.

This is why comparing composite identities compares the systems rather than their descriptions: an
identity derived from constituents cannot agree while the constituents differ.

## 8. What this document does not specify

- **The form of an identity** — its syntax, its structure, whether it is hierarchical, and what
  separates its parts.
- **The form of an address**, and whether identity and address are expressed alike or differently.
- **A canonicalization scheme** (§2.2). That one exists is required; which one is not.
- **What namespaces a system has**, or how they are arranged. A profile's question.
- **What supersession means** between two identities. Supersession's subject.
- **How authority and concern are represented** — required to be separately expressible (GO-11,
  MB-7), with the representation unspecified.

## 9. Normative invariants

- **ID-1.** An identity MUST be declared and MUST be authoritative over filename, path, containment,
  position, convention, and manner of discovery (§2.1).
- **ID-2.** Nothing MUST acquire identity by being found (§2.1).
- **ID-3.** Identity MUST be defined over the semantic object, and a representation change
  preserving meaning MUST NOT change identity (§2.2).
- **ID-4.** Two admitted things bearing one identity MUST be refused (§2.3).
- **ID-5.** A change of declared semantics MUST be a new identity (§2.4).
- **ID-6.** Identity MUST NOT carry ordering; supersession MUST be a declared relation (§2.4).
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
- **ID-14.** Resolution MUST NOT search, select among candidates, or fall back; an ambiguous or
  unresolvable reference MUST be refused (§6).
- **ID-15.** A composite identity MUST be derived from its constituents' identities, and MUST change
  when any constituent changes (§7).

## 10. Conformance

The conformance subject of this document is an **identity scheme**: how a governed system identifies
its things, how it addresses them, and how it resolves references between them.

An identity scheme conforms when identities are declared and authoritative over position, defined
over semantic objects, unique within their scope, and unchanged by relocation; when addresses are
treated as means rather than claims; when resolution refuses rather than searching; and when neither
identity nor addressing carries authority or concern.

**The decisive test is relocation.** Move a governed thing — change its path, its container, its
address, the order in which it is encountered — and nothing about its identity, its governance, or
the composite identity of anything containing it may change. A scheme that survives relocation has
its identity declared; one that does not has been deriving identity from address, however plainly it
says otherwise.

How this is required and evaluated belongs to the Conformance Test Specification.
