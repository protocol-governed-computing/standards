# Normative Platform Profile

## 1. Scope

This document specifies the **profile**: the instrument by which the facilities of this family are
selected and constrained, **under which** a concrete, interoperable governed system may be
constituted — and the **platform** that results.

A profile does not construct anything. It constrains a system that claims it.

It opens Part VI. Every document before it deliberately left decisions unmade, on the grounds that
making them would fix one platform where the family admits many. A profile is where those decisions
are made. **The family says what must be true; a profile says which of the permitted things a
particular system does.**

A profile is also load-bearing for something more basic than configuration. A snapshot must claim
one (SN-5, SN-7) and a genesis proposal must name one (SM-11) — because the claimed profile is the
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

**An additional requirement does not extend the semantics of the family; it constrains systems
claiming the profile.** A profile that appears to add meaning has redefined something (§4).

A profile is **normative for systems that claim it** and for parties evaluating those systems. It is
not normative for this family: a profile cannot alter what the family requires of anything.

## 3. What a profile may do

> A profile MAY constrain, select, parameterize, or require facilities defined by the core
> standards, and MAY add requirements within an explicitly permitted extension point.

An **extension point** is a place where a core standard explicitly permits a profile to add
requirements. It exists only where a standard declares one: an area the standards leave unspecified
is not an extension point, and a profile adding requirements there would be adding to the family
rather than within it (§2).

### 3.1 It may narrow, never widen

**This is the whole of the rule, and everything else in §4 follows from it.**

- A profile MAY require *more* than the family requires.
- A profile MAY permit *less* than the family permits — narrowing what is **optional**.
- **A profile MUST NOT permit more, or require less.**

Permitting less and requiring less are different acts, and only the first is available. A profile
narrows the choices the family leaves open; it never removes an obligation the family imposes.

A conforming system under any profile is a conforming system under the family. If claiming a profile
could make something permissible that the family forbids, then a profile would be a route around the
family, and the family would constrain only systems claiming no profile at all.

### 3.2 What narrowing looks like

- **Selection** — using some facilities and not others. A profile requiring no interaction boundary
  yields systems that are not interacted with; it does not yield systems whose boundaries are
  ungoverned.
- **Constraint** — admitting a subset. A profile may admit five artifact kinds where the family
  admits any declared vocabulary.
- **Parameterization** — supplying a value the family requires but leaves open (§7).
- **Additional requirement** — an obligation of the profile's own, consistent with the family's.

## 4. What a profile must not do

| MUST NOT | Because |
|---|---|
| redefine a core facility's semantics | the term would mean two things, and no check could tell which |
| give a normative term an incompatible meaning | 1a §12 — terminology is family-wide |
| weaken or exempt anything from an invariant | invariants are what conformance is (1c §10) |
| relax a refusal into a warning | 2f §6.3 — an obligation reduced to a report is not an obligation |
| make itself the authority for its own satisfaction | §6 |
| introduce a facility with no home in the family | it would be governed by nothing this family specifies |

The last deserves stating plainly. **A profile that introduces a new facility has written a new
standard and called it a profile.** Where a facility is genuinely needed and the family has no home
for it, the remedy is a family revision, proposed through the path Supersession
specifies — not a profile that quietly extends the model for the systems that adopt it.

## 5. Additional requirements

A profile MAY impose obligations the family does not, provided they narrow (§3.1) and provided their
subject is something the family governs.

**An additional obligation must add something.** An obligation that restates a family requirement, or
restates one of the profile's own selections or parameterizations, is not an additional obligation
and MUST NOT be declared as one — it is satisfied by everything that already satisfies what it
restates, so nothing can breach it that has not already breached that. The cost is not only
redundancy: under §9, every later adjustment to it is a new profile identity.

Two consequences follow:

- **A claim against a profile is a claim about two things**: that the system conforms to the family,
  and that it satisfies the profile's additional obligations. Neither implies the other in reverse —
  family conformance does not establish profile satisfaction.
- **A profile's additional obligations are enforced as governance is enforced.** They are not
  advisory, and a profile obligation that nothing can refuse is not in force (EN-1). A profile
  declaring obligations it cannot have checked has declared intentions.

## 6. A profile is external to what claims it

**A profile MUST NOT be authored by the system that claims it** (SN-7).

This is the requirement that makes the whole instrument work, and it is not a formality:

- At genesis, the claimed profile is the *only* thing constraining a system that has no predecessor
  and no governance in force (SM-11). A self-authored profile at genesis is a system declaring the
  standard it will be judged against — and it will pass.
- After genesis, a system that authored its own profile could relax the profile's obligations by the
  same transformation that violates them, and both changes would be internally consistent.

Externality is a property of **authorship**, not of storage. A profile may be carried anywhere,
including within a system's own repository; what matters is that changing it is not within the
authority of the system that claims it.

## 7. What a profile decides

The family defers specific decisions to profiles. A profile that leaves one undecided yields systems
that cannot be checked on it.

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

**A profile need not decide every item — but it MUST decide every item bearing on a conformance
claim it supports.** A profile supporting a claim about evidence while leaving retention undecided
supports a claim nobody can evaluate.

**A decision MUST be the profile's own.** An item is not decided by requiring the system to decide
it. A profile that admits "whatever vocabulary the system declares," "whatever outcomes its contracts
declare," or "whatever namespaces it names" has restated what the family already requires and left
the item exactly where the family left it — and two systems agreeing on nothing both satisfy it. This
is the more dangerous of the two failures, because it reads as a decision: it satisfies §6 in form
while inverting it in substance, handing the constraint back to the party the profile constrains.

**The test for whether an item is decided is whether two systems that disagree on it could both
claim the profile.** If they could, the profile has not decided it, whatever the text says.

**A profile MUST NOT support a claim no system under it could discharge.** Naming a demonstration —
a second runtime, a second protocol, a second environment — while constraining systems such that the
substitution cannot be performed supports a claim nobody can evaluate, in the same way leaving
retention undecided does. Which discharge class establishes an obligation is the evaluator's
question, and the Conformance Model's; whether a system under this profile can be subjected to that
class at all is the profile's.

Three of these deserve emphasis because they are commonly assumed rather than decided:

- **The trust root.** A profile that does not name what its checking parties accept axiomatically has
  left every attestation chain unterminated (EV-10), and each party will terminate it differently.
- **Read surface openness.** A system whose read surface is universally open has decided that, and a
  profile is where the decision is recorded rather than reached by default (5b §11). **What a
  profile decides here is the policy, not the determination.** A profile MAY fix which callers its
  systems admit to which declared read operations, up to and including all callers to all of them;
  it MUST NOT thereby permit a read to be answered without the determination 5b §11 requires. The
  first is the most permissive parameterization available; the second is a widening wearing a
  parameterization's clothes (NP-11).
- **Reachability of what a selection leaves standing.** Selecting a facility away does not select
  away the obligations that depended on it. A profile admitting no interaction boundary still
  requires a read surface (5b §10), and 5b §2.1 obliges it to say by what means that surface is
  reached. **Excluding a facility is a decision about what a system has; it is not a decision about
  how what remains is obtained** — and a read surface no checking party can reach discharges
  nothing.

**Genesis is in scope wherever a first snapshot is.** A profile whose systems are constituted rather
than inherited supports a claim about genesis whether it says so or not: the claimed profile is the
only thing constraining the proposal (§1, SM-11), so the profile is the subject of that constraint.
Such a profile decides what discharges the claim (7b §9) or supports a claim about the one moment it
was written to govern and leaves nobody able to evaluate it.

## 8. Platform

A **platform** is a governed composition that provides a defined governance and execution surface
for the workloads and domains composed into it, **under a named profile** (1a).

Three consequences, relocated here from the vocabulary because they are claims about profiles rather
than definitions of a term:

- **A platform is always constituted under a profile, and different profiles constitute different
  platforms.** Two compositions under two profiles are two platforms, however similar their
  contents. One profile may constitute many platforms, and one platform may be deployed many times
  — deployment multiplies instances of a platform, never platforms.
- **No platform is minimal by nature.** Minimality is relative to a profile — a profile may define a
  smallest conforming composition under itself, and that says nothing about any other profile. There
  is no minimal PGC platform, and a claim to be one is a claim about an unnamed profile.
- **No repository, package, deployment, or installation is a platform**, however completely it
  contains one. What makes a platform is the composition and the profile it was composed under,
  neither of which is a location (1a).

## 9. Profile identity and change

- **A profile MUST have an identity** by which a system can name the profile it claims and a checking
  party can obtain the same one (ID-1).
- **A change to a profile's obligations is a new profile identity.** A system claiming a profile
  claims the profile as it was identified, and a profile whose obligations can change under a
  stable identity makes every claim against it unverifiable after the fact.
- **A change to a profile does not retroactively alter systems that claimed its predecessor.** They
  claimed what they claimed; whether they satisfy the successor is a fresh question, determined
  fresh.
- What supersession between profiles means — how references to a superseded profile resolve — belongs
  to Supersession.

## 10. Profile derivation

A profile MAY be **derived** from another: adopting its selections and obligations, and narrowing
further.

- **A derived profile MUST NOT widen its base.** The narrowing rule (§3.1) applies transitively; a
  system conforming to a derived profile conforms to its base, and to the family.
- **A derived profile MUST name its base by identity** (§9), so that what it inherits is
  determinable rather than described.
- Derivation is not composition: a profile derived from two bases MUST resolve any difference between
  them by narrowing to what both permit, never by choosing between them.

## 11. What this document does not specify

- **Which profiles exist.** None is defined here, and none is privileged.
- **The content of any particular profile**, including whatever profile a reference realization
  claims.
- **The form a profile takes** — its encoding, structure, or how it is published.
- **Execution environment constraints**, which are Execution Environment Profiles' subject.
- **Domain-specific obligations**, which are Domain Profiles' subject.
- **How conformance to a profile is claimed or evaluated**, which is Part VII's.

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
- **NP-11.** A profile MUST NOT use selection, parameterization, or an additional requirement to
  make a behavior the family prohibits appear permitted (§13).
- **NP-12.** A profile MUST NOT decide a deferred item by deferring it to the system that claims the
  profile (§7).

## 13. Conformance

The conformance subject of this document is a **profile**: the declared selections, constraints,
parameterizations, additional obligations, and supported claims of a named profile.

A profile conforms when it narrows without widening, redefines nothing, exempts nothing, introduces
no facility with no home in the family, decides what its claims require rather than re-deferring it,
is identified, and is not authored by what claims it.

**The failure to look for is widening that reads as narrowing.** A profile that admits a small kind
vocabulary while permitting one of those kinds to omit a governance assertion has narrowed in the
visible dimension and widened in the one that matters. **This case is checkable rather than only
warned against:** a profile that closes a kind vocabulary states each admitted kind's
governance-assertion disposition alongside it (KV-10), which puts the dimension that matters on the
page next to the dimension that is visible. What distinguishes them is not size but
direction: every profile obligation must be satisfiable only by systems that already satisfy the
family.

**A conforming profile may still be a poor one** — too permissive to be interoperable, too specific
to be adopted, or deciding items no claim it supports depends on. That is a question of design, and
it is not a conformance question.

How conformance to this document and to any profile is claimed and evaluated belongs to the
Conformance Model and the Conformance Test Specification.
