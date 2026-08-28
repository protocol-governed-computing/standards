# Implementation Guidance

*Non-normative. Nothing here is required, and nothing here relaxes anything that is. An
implementation satisfying the normative documents conforms whether or not it follows any of this.
Where this annex and a normative document appear to differ, the document governs.*

## 1. What this annex is for

Twenty-five normative documents state what must be true and deliberately decline to say how. That
leaves an implementer with real questions the standard will not answer: what has been tried, what
worked, what looked reasonable and was not.

This annex answers those from experience rather than from authority. It has three subjects:

- **the reference realization** — what it establishes, and what it does not (§2);
- **techniques** — how properties have been obtained, and why none of them is the property (§3);
- **alternative realization models** — how a system built differently satisfies the same semantics
  (§4).

## 2. The reference realization

A reference realization exists. It is one system, built by one group, and its role is narrow.

**What it establishes:** that the normative documents are satisfiable. A standard nothing has
implemented is a hypothesis, and the realization is the evidence against that charge.

**What it does not establish:**

- **that its choices are required.** Every mechanism it uses is one way of obtaining a property.
- **that its arrangement is correct.** Its repository layout, its component boundaries, and its
  process count are architecture, and the family excludes architecture from normative text.
- **that it conforms.** A realization conforms by discharging claims (7a), not by being the one the
  documents were written alongside. **Resembling it establishes nothing** (CF-5), and a conformance
  regime testing for resemblance tests a choice.

**The direction of authority.** A realization informs the family by exposing concepts that were
missing, distinctions that were conflated, and requirements that could not be met. It never supplies
authority. Where the two disagree, the document governs and the disagreement is resolved by ruling —
never by editing the document to match what was built.

## 3. Techniques are not invariants

Every technique below obtains a property. **None of them is the property**, and a realization
obtaining it differently conforms.

| Technique | Property it serves |
|---|---|
| fully qualified references everywhere | identity is not positional (AI-2, ID-1) |
| resolution through an index rather than a derived path | addressing does not determine identity (ID-9) |
| static imports; no reflective loading | nothing enters by discovery (AI-12) |
| environment-provisioned roots; no path synthesis | behavior does not follow from ambient environment (EE-4) |
| content-addressed identifiers | identity is derived, not assigned (AI-9, SN-2) |
| a failed build writing nothing | refusal leaves no residue (AI-8, GC-6) |
| a closed handler registry, failing on the unknown | check kinds are closed (TR-3) |
| round-trip verification of what was written | carrying is not determining (GC-13) |
| comparing every copy of one identity | copies must agree (GC-12) |

The failure mode is specific: **a conformance regime that tests the left column will reject
conforming systems while passing systems that keep the technique and lose the property.** A
realization can hold fully qualified references everywhere and still derive identity from location
somewhere it matters.

## 4. Alternative realization models

The family has a **centre of gravity** around declare → construct → seal → accept → execute, because
that is what the reference realization does. The normative requirement is different from that
sequence, and the difference is where alternatives live.

### 4.1 What is actually required

| Required | Not required |
|---|---|
| determination completes before the effect it governs (AI-4) | that it complete at a particular time |
| execution consumes sealed, verified, complete state (SN-4, SN-8, RT-3) | that sealing happen long beforehand |
| resolution completes before what depends on it (AI-5) | that all resolution happen in one pass |
| composition obligations are discharged over the whole (GC-11) | that the whole be constructed at once |

**Ordering is required; scheduling is not.**

### 4.2 Construction on admission

An interaction arrives; the candidates it needs are determined, sealed, and verified; execution
proceeds against what was sealed.

This conforms. Governed Construction states explicitly that a realization may discharge its
obligations "long before execution or immediately before it," and the Snapshot Standard that "when
sealing occurs is unconstrained." What such a realization must not do is let the interaction
influence the determination — the arriving request selects among what may be constructed; it does
not extend it (SN-10, IB §8).

### 4.3 Incremental determination

Candidates determined one at a time, with construction proceeding as each is admitted.

This conforms provided that, **for each candidate, everything depending on that candidate's legality
follows its determination** (4a §6). What it may not do is carry an undetermined candidate forward
in the expectation that something later will catch it.

### 4.4 Distributed construction

Parts constructed independently, on different machines, at different times.

This conforms for the parts. **It does not conform until the composition obligations are discharged
over the whole** — identity over the composition, agreement among copies, and rules quantifying
universally (GC-11, GC-12). Parts that are each admissible do not compose into an admissible whole,
and a distributed construction that assembles part-level results has skipped the obligations that
only exist at composition scale.

### 4.5 No retained representation

A system that constructs, seals in memory, verifies, executes, and retains nothing.

This conforms as to execution. What it forfeits is everything downstream of retention: past
determinations become unestablishable, replay becomes impossible, and evidence covers only what was
kept. Whether that is acceptable is a profile's question, and one worth answering deliberately
rather than by default (3e §11).

### 4.6 Determination performed elsewhere

The closure evaluated by a separate service, a shared authority, or another system.

**A determination is a determination regardless of where it was made**; what matters is the closure
it was made under and that its evidence carries it (6b §8.1). What such an arrangement must not do
is let unavailability become permission — an unreachable determination service is an inability to
determine, and inability to determine refuses (AI-6).

### 4.7 The rule for anything not listed

**Where this annex cannot show how an alternative model conforms, that is evidence of an
over-specified normative document, and is handled as a finding against it** — not as a defect in the
alternative.

The family's claim is to specify semantics, not architecture. An alternative that satisfies every
semantic requirement and is nonetheless excluded has found a place where a normative document
described a mechanism while believing it described a meaning.

## 5. Hazards

Each of these has been reached by reasonable people for reasonable-sounding reasons.

| Hazard | Breaches | Why it is attractive |
|---|---|---|
| an execution agent that interprets domain meaning | AI-1, RT-1 | it makes the immediate problem easy |
| a fallback path where the declarations run out | AI-6, EN-10 | it keeps a demonstration working |
| discovery by scanning, convention, or reflection | AI-12 | it removes authoring friction |
| editing a sealed representation | SN-1, SN-12 | the fix is small and the rebuild is slow |
| evidence consulted while determining | AI-15, EV-4 | prior results are right there |
| a client computing what the read surface did not answer | IN-8 | the answer is one join away |
| an inspection returning empty on unreadable material | IN-9 | empty is a valid answer elsewhere |
| a rule set no rule of which has been made to fail | EN-5, TR-3a | it is green |

**The last two are the ones that survive review**, because both produce results that look correct.
An empty answer is indistinguishable from a true negative, and a rule set that has never refused is
indistinguishable from one governing a system that has never violated it.

## 6. The realization map

A mapping from each normative document to where the reference realization demonstrates it —
which declarations, which construction path, which region of the sealed representation, which
evidence — would serve two purposes:

- an implementer reconstructs it anyway, by reading the code; supplying it saves every implementer
  the same rediscovery;
- **a normative document with no demonstration is either unimplemented or unimplementable**, and the
  mapping makes which one visible.

It was parked while most documents were unwritten, on the grounds that a mostly-empty map would
shape documents before they were drafted. That reason has expired: both sides now exist.

**Such a map is maintained alongside this family as the *Realization Map*.** It is partial, it is
stated against a named snapshot of the reference realization, and it is **not a document of this
family** — it declares no part, discharges no membership condition, and does not participate in
revision or supersession. A map inside the revision unit would let a change in a codebase move this
family's revision identity, which is the inverse of the direction of authority §2 states.

What it must not become is a specification — it is evidence about one realization, and §2 governs
what such evidence establishes.

## 7. What this annex cannot do

- **It cannot make anything conformant.** Following every recommendation here discharges no claim.
- **It cannot excuse anything.** No difficulty described here relaxes an obligation; where an
  implementation cannot satisfy one, that is a finding, not an exception.
- **It cannot be cited normatively.** A claim resting on a sentence in this annex rests on nothing
  the family requires.
- **It will age.** Techniques and hazards reflect what has been built and what has gone wrong so
  far. The normative documents are meant to outlast that; this annex is not.
