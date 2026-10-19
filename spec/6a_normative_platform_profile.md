# Normative Platform Profile

## 1. Scope

This document specifies the **profile** and the **platform** that results from it. A profile is the
instrument that selects and constrains the facilities of this family. A concrete, interoperable
governed system may be constituted **under** a profile.

A profile constructs nothing. It constrains a system that claims it.

This document opens Part VI. Every document before it deliberately left some decisions unmade,
because making them would fix one platform where the family admits many. A profile makes those
decisions. **The family says what must be true. A profile says which of the permitted things a
particular system does.**

A profile also carries weight for something more basic than configuration. A snapshot must claim a
profile (SN-5, SN-7), and a genesis proposal must name one (SM-11). The claimed profile is the
**external governing selection**: the constraint a system being constituted did not author for
itself. Without profiles, a governed system could declare its own rules, satisfy them, and be
perfectly governed by its own account.

This document introduces the terms **selection**, **constraint**, **parameterization**, **extension
point**, and **profile derivation**.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What a profile is

A **profile** is a declared statement of:

| Declares | Meaning |
|---|---|
| **selection** | which facilities of this family the system uses |
| **constraint** | how those facilities are narrowed beyond what the family requires |
| **parameterization** | values the family leaves open (§7) |
| **additional requirements** | obligations beyond the family's, where permitted (§5) |
| **conformance claims** | which claims a system under this profile must support |

**An additional requirement does not extend the semantics of the family. It constrains systems that
claim the profile.** A profile that appears to add meaning has redefined something (§4).

A profile is **normative for systems that claim it**, and for parties that evaluate those systems. It
is not normative for this family. A profile cannot alter what the family requires of anything.

## 3. What a profile may do

> A profile MAY constrain, select, parameterize, or require facilities defined by the core
> standards, and MAY add requirements within an explicitly permitted extension point.

An **extension point** is a place where a core standard explicitly permits a profile to add
requirements. An extension point exists only where a standard declares one. An area the standards
leave unspecified is not an extension point. A profile that added requirements there would be adding
to the family, not working within it (§2).

### 3.1 It may narrow, never widen

**This is the whole of the rule, and everything in §4 follows from it.**

- A profile MAY require *more* than the family requires.
- A profile MAY permit *less* than the family permits, by narrowing what is **optional**.
- **A profile MUST NOT permit more, or require less.**

Permitting less and requiring less are different acts, and only the first is available. A profile
narrows the choices the family leaves open. It never removes an obligation the family imposes.

A conforming system under any profile is a conforming system under the family. Suppose claiming a
profile could make something permissible that the family forbids. A profile would then be a route
around the family. The family would constrain only systems that claim no profile at all.

### 3.2 What narrowing looks like

- **Selection**: using some facilities and not others. A profile that requires no interaction
  boundary yields systems that nobody interacts with. It does not yield systems with ungoverned
  boundaries.
- **Constraint**: admitting a subset. A profile may admit five artifact kinds where the family admits
  any declared vocabulary.
- **Parameterization**: supplying a value that the family requires but leaves open (§7).
- **Additional requirement**: an obligation of the profile's own, consistent with the family's.

## 4. What a profile must not do

| MUST NOT | Because |
|---|---|
| redefine a core facility's semantics | the term would mean two things, and no check could tell which |
| give a normative term an incompatible meaning | Conceptual Model §12 — terminology is family-wide |
| weaken or exempt anything from an invariant | invariants are what conformance is (Architectural Invariants §10) |
| relax a refusal into a warning | Enforcement & Refusal §6.3 — an obligation reduced to a report is not an obligation |
| make itself the authority for its own satisfaction | §6 |
| introduce a facility with no home in the family | it would be governed by nothing this family specifies |

The last row deserves a plain statement. **A profile that introduces a new facility has written a new
standard and called it a profile.** Suppose a facility is genuinely needed and the family has no home
for it. The remedy is a family revision, proposed through the path Supersession specifies. It is not
a profile that quietly extends the model for the systems that adopt it.

## 5. Additional requirements

A profile MAY impose obligations the family does not impose. They must narrow (§3.1), and their
subject must be something the family governs.

**An additional obligation must add something.** Some obligations only restate a family requirement,
or one of the profile's own selections or parameterizations. Such an obligation is not an additional
obligation and MUST NOT be declared as one. Everything that satisfies what it restates also satisfies
it. So nothing can breach it without having already breached the original. The cost is more than
redundancy. Under §9, every later adjustment to it is a new profile identity.

Two consequences follow:

- **A claim against a profile is a claim about two things**: that the system conforms to the family,
  and that it satisfies the profile's additional obligations. Neither implies the other. In
  particular, family conformance does not establish profile satisfaction.
- **A profile's additional obligations are enforced as governance is enforced.** They are not
  advisory. A profile obligation that nothing can refuse is not in force (EN-1). A profile that
  declares obligations nothing can check has declared intentions.

## 6. A profile is external to what claims it

**A profile MUST NOT be authored by the system that claims it** (SN-7).

This requirement makes the whole instrument work, and it is not a formality:

- At genesis, the claimed profile is the *only* constraint on a system that has no predecessor and no
  governance in force (SM-11). A self-authored profile at genesis lets a system declare the standard
  it will be judged against. It will pass.
- After genesis, a system that authored its own profile could relax the profile's obligations in the
  same transformation that violates them. Both changes would be internally consistent.

Externality is a property of **authorship**, not of storage. A profile may be stored anywhere,
including within a system's own repository. What matters is that changing it lies outside the
authority of the system that claims it.

## 7. What a profile decides

The family defers specific decisions to profiles. A profile that leaves one undecided yields systems
that nobody can check on it.

| Decision | Deferred by |
|---|---|
| which artifact kinds are admissible | Kind Vocabulary — KV-9, and no kind is required by the family |
| which outcomes contracts may declare | Execution Model, Capability Standard |
| the result classes at the interaction boundary | Governed Interaction Boundary |
| which projections a system carries | Projection Standard |
| what namespaces exist and how they are arranged | Identity & Addressing |
| what a checking party accepts as a trust root | Evidence, Attestation & Provenance |
| how long evidence is retained | Evidence, Attestation & Provenance |
| how open the read surface is | Governed Inspection |
| whether reads are attributed | Governed Inspection |
| the sufficiency criterion below which realization refuses | Governed Transformation |
| whether a given interaction-form element is itself a governed artifact | Governed Interaction Boundary |
| whether an external protocol binding is a governed artifact | Governed Interaction Boundary |
| how the read surface is reached, where no interaction boundary is selected | Governed Inspection |
| what discharges a genesis claim, where the profile's scope includes a first snapshot | Conformance Test Specification |

**A profile need not decide every item, but it MUST decide every item that bears on a conformance
claim it supports.** Suppose a profile supports a claim about evidence and leaves retention
undecided. Nobody can evaluate that claim.

**A decision MUST be the profile's own.** A profile does not decide an item by requiring the system
to decide it. Suppose a profile admits "whatever vocabulary the system declares", "whatever outcomes
its contracts declare", or "whatever namespaces it names". It has restated what the family already
requires. It has left the item exactly where the family left it, and two systems that agree on
nothing both satisfy it. This is the more dangerous failure, because it reads as a decision. It
satisfies §6 in form while inverting it in substance: it hands the constraint back to the party the
profile constrains.

**An item is decided only if two systems that disagree on it could not both claim the profile.** If
they could, the profile has not decided it, whatever the text says.

**A profile MUST NOT support a claim that no system under it could discharge.** A profile may name a
demonstration, such as a second runtime, a second protocol or a second environment. If it also
constrains systems so that the substitution cannot be performed, it supports a claim nobody can
evaluate. That is the same failure as leaving retention undecided. Which discharge class establishes
an obligation is a question for the evaluator and the Conformance Model. Whether a system under this
profile can be subjected to that class at all is a question for the profile.

Three of these items need emphasis, because people commonly assume them instead of deciding them:

- **The trust root.** A profile that does not name what its checking parties accept as an axiom has
  left every attestation chain unterminated (EV-10). Each party will terminate it differently.
- **Read surface openness.** A system whose read surface is open to everyone has decided that. A
  profile is where the decision is recorded, rather than reached by default (Governed Inspection
  §11). **A profile decides the policy here, not the determination.** A profile MAY fix which callers
  its systems admit to which declared read operations, up to and including all callers to all of
  them. It MUST NOT thereby permit a read to be answered without the determination Governed
  Inspection §11 requires. The first is the most permissive parameterization available. The second
  is a widening disguised as a parameterization (NP-11).
- **Reachability of what a selection leaves standing.** Selecting a facility away does not select
  away the obligations that depended on it. A profile that admits no interaction boundary still
  requires a read surface (Governed Inspection §10). Governed Inspection §2.1 obliges the profile to
  say how that surface is reached. **Excluding a facility decides what a system has. It does not
  decide how a party obtains what remains.** A read surface that no checking party can reach
  discharges nothing.

**Genesis is in scope wherever a first snapshot is.** Suppose a profile's systems are constituted
rather than inherited. That profile supports a claim about genesis whether it says so or not. The
claimed profile is the only constraint on the proposal (§1, SM-11), so the profile is the subject of
that constraint. Such a profile either decides what discharges the claim (Conformance Test
Specification §9), or it supports a claim about the one moment it was written to govern and leaves
nobody able to evaluate it.

## 8. Platform

A **platform** is a governed composition that provides a defined governance and execution surface
for the workloads and domains composed into it, **under a named profile** (Conceptual Model,
*platform*).

Three consequences follow. They are relocated here from the vocabulary because they are claims about
profiles, not definitions of a term:

- **A platform is always constituted under a profile, and different profiles constitute different
  platforms.** Two compositions under two profiles are two platforms, however similar their contents.
  One profile may constitute many platforms, and one platform may be deployed many times. Deployment
  multiplies instances of a platform, never platforms.
- **No platform is minimal by nature.** Minimality is relative to a profile. A profile may define a
  smallest conforming composition under itself. That says nothing about any other profile. There is
  no minimal PGC platform. A claim to be one is a claim about an unnamed profile.
- **No repository, package, deployment or installation is a platform**, however completely it
  contains one. The composition and the profile it was composed under make a platform. Neither one
  is a location (Conceptual Model, *platform*).

## 9. Profile identity and change

- **A profile MUST have an identity.** A system uses it to name the profile it claims, and a checking
  party uses it to obtain the same profile (ID-1).
- **A change to a profile's obligations is a new profile identity.** A system that claims a profile
  claims it as it was identified. If a profile's obligations could change under a stable identity,
  nobody could verify any claim against it after the fact.
- **A change to a profile does not retroactively alter systems that claimed its predecessor.** They
  claimed what they claimed. Whether they satisfy the successor is a fresh question, determined
  fresh.
- Supersession owns what supersession between profiles means, including how references to a
  superseded profile resolve.

## 10. Profile derivation

A profile MAY be **derived** from another. It adopts the other's selections and obligations, and
narrows further.

- **A derived profile MUST NOT widen its base.** The narrowing rule (§3.1) applies transitively. A
  system that conforms to a derived profile conforms to its base, and to the family.
- **A derived profile MUST name its base by identity** (§9). Then what it inherits is determinable,
  not merely described.
- Derivation is not composition. A profile derived from two bases MUST resolve any difference between
  them by narrowing to what both permit, never by choosing between them.

## 11. What this document does not specify

- **Which profiles exist.** This document defines none, and none is privileged.
- **The content of any particular profile**, including any profile a reference realization claims.
- **The form a profile takes**: its encoding, its structure, or how it is published.
- **Execution environment constraints.** Execution Environment Profiles owns them.
- **Domain-specific obligations.** Domain Profiles owns them.
- **How conformance to a profile is claimed or evaluated.** Part VII owns that.

## 12. Normative invariants

- **NP-1.** A profile MUST NOT permit what the family forbids, and MUST NOT require less than the
  family requires (§3.1).
- **NP-2.** A conforming system under any profile MUST be a conforming system under the family
  (§3.1).
- **NP-3.** A profile MUST NOT redefine the semantics of a core facility or give a normative term an
  incompatible meaning (§4).
- **NP-4.** A profile MUST NOT weaken, exempt from, or relax any invariant of this family (§4).
- **NP-5.** A profile MUST NOT introduce a facility the family has no home for (§4).
- **NP-6.** A profile's additional obligations MUST be enforceable, and an unenforceable one MUST NOT
  be declared as an obligation (§5).
- **NP-7.** A profile MUST NOT be authored by a system that claims it (§6).
- **NP-8.** A profile MUST decide every deferred item bearing on a conformance claim it supports
  (§7).
- **NP-9.** A profile MUST have an identity, and a change to its obligations MUST be a new identity
  (§9).
- **NP-10.** A derived profile MUST name its base by identity and MUST NOT widen it (§10).
- **NP-11.** A profile MUST NOT use selection, parameterization, or an additional requirement to make
  a behavior the family prohibits appear permitted (§13).
- **NP-12.** A profile MUST NOT decide a deferred item by deferring it to the system that claims the
  profile (§7).

## 13. Conformance

The conformance subject of this document is a **profile**: the declared selections, constraints,
parameterizations, additional obligations and supported claims of a named profile.

A profile conforms when all of the following hold:

- it narrows without widening;
- it redefines nothing and exempts nothing;
- it introduces no facility without a home in the family;
- it decides what its claims require, instead of re-deferring it;
- it is identified;
- no system that claims it authored it.

**Look for widening that reads as narrowing.** Consider a profile that admits a small kind vocabulary
while letting one of those kinds omit a governance assertion. It has narrowed in the visible
dimension and widened in the one that matters. **This case is checkable, not only warned against.** A
profile that closes a kind vocabulary states each admitted kind's governance-assertion disposition
alongside it (KV-10). That puts the dimension that matters on the page next to the visible one. Size
does not tell the two apart. Direction does: every profile obligation must be satisfiable only by
systems that already satisfy the family.

**A conforming profile may still be a poor one.** It may be too permissive to interoperate, too
specific to be adopted, or decide items that no claim it supports depends on. That is a question of
design, not a conformance question.

The Conformance Model and the Conformance Test Specification own how conformance to this document,
and to any profile, is claimed and evaluated.
