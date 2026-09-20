# Profile template

A structure for authoring a Normative Platform Profile, **derived from `6a` and adding nothing to
it.** Every section below exists because `6a` requires the profile to state something; the citation
is given for each, and a section whose citation you cannot follow should be dropped rather than
filled.

**This is not part of the family and carries no authority.** `6a` §11 declines to specify *"the form
a profile takes — its encoding, structure, or how it is published."* A profile that ignores this
template is not thereby defective, and a profile that follows it is not thereby conforming.

**Do not give this to an authoring trial.** The point of such a trial is to find what the standard
alone leads an author to produce. Supplying the structure answers that in advance, and three
independently authored profiles organising the same content three ways is the evidence that the
structure was not determined.

---

## 1. Identity

*Required by `6a` §9, NP-9, and ID-1.* An identity by which a system names the profile it claims and
a checking party obtains the same one.

State also that **a change to the obligations below is a new identity** — a profile whose
obligations move under a stable name makes every claim against it unverifiable after the fact.

## 2. What this profile profiles

*Required by `6a` §1.* The class of systems the profile is for. Not an inventory of what any
particular system contains.

`6a` §8: **do not call it minimal.** No platform is minimal by nature; minimality is relative to a
profile. Say what the profile is *for*.

## 3. Selections and exclusions

*Required by `6a` §5, bounded by NP-1, NP-2, NP-4, NP-5.* Which facilities of the family this
profile selects, and which it does not.

A profile **narrows**: it may require more than the family requires and permit less than the family
permits. It may not permit more, require less, weaken an invariant, or introduce a facility the
family has no home for.

## 4. Deferred decisions

*Required by `6a` §7 and NP-8: a profile MUST decide every deferred item bearing on a conformance
claim it supports.* NP-12: **it may not decide one by deferring it to the system that claims it.**
"Whatever the system declares" is not a decision.

The items `6a` §7 hands to a profile. Decide those bearing on the claims in §7 below; state that the
rest do not bear on them.

| Deferred item | Decision |
|---|---|
| which artifact kinds are admissible | |
| which outcomes contracts may declare | |
| the result classes at the interaction boundary | |
| which projections a system carries | |
| what namespaces exist and how they are arranged | |
| what a checking party accepts as a trust root | |
| how long evidence is retained | |
| how open the read surface is | |
| whether reads are attributed | |
| the sufficiency criterion below which realization refuses | |
| whether a given interaction-form element is itself a governed artifact | |
| whether an external protocol binding is a governed artifact | |
| how the read surface is reached, where no interaction boundary is selected | |
| what discharges a genesis claim, where the scope includes a first snapshot | |

**Where a profile closes a kind vocabulary**, `2d` requires it closed within a revision and `6a`
requires each admitted kind's declaration stated. That is the first row, expanded.

## 5. Additional obligations

*Required by `6a` §5, bounded by NP-6: an additional obligation MUST be enforceable, and an
unenforceable one MUST NOT be declared as one.*

For each, state **what would establish a breach**. An obligation nothing could refuse is not in
force (`2f` EN-1), and one that merely restates a selection above is not additional.

## 6. Derivation

*Required by `6a` §10 and NP-10, where the profile is derived.* Name the base **by identity**, and
state that this profile does not widen it. Omit this section entirely where the profile is not
derived — an absent section is clearer than one saying "none".

## 7. Supported claims and discharge

*Required by `6a` §5 and Part VII.* Which conformance claims this profile supports, and for each,
what discharges it — a discharge class from `7a` §7 capable of establishing it (CF-8), and
demonstrations per `7b`.

`7b` CD-4: a demonstration must be **capable of failing** if the system were non-conforming. A
claim whose fixtures are all well-formed has no negative demonstrations however many it lists.

## 8. Excluded systems

*Follows from §3 and NP-1.* Systems whose requirements this profile does not admit. Stating this
plainly is what lets a reader tell in one pass whether the profile is theirs.

---

## Not a section: authorship

`6a` §6 and NP-7 require that **a profile not be authored by the system that claims it.** That is a
constraint on who may write the profile, not something the profile must state, and this template
had it as a section until all three existing profiles were checked and none had one. They were
right. Externality is a property of authorship, not of declaration — a profile asserting its own
independence establishes nothing.

## Say why, not only what

Not required by `6a`, and worth doing anyway. Where a decision could reasonably have gone the other
way, one sentence on why it went this way is what makes a profile reviewable rather than merely
followed.
