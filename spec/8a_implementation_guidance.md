# Implementation Guidance

*Non-normative. Nothing here is required, and nothing here relaxes anything that is required. An
implementation that satisfies the normative documents conforms whether or not it follows any of
this. Where this annex and a normative document appear to differ, the document governs.*

## 1. What this annex is for

Twenty-five normative documents state what must be true, and deliberately decline to say how. That
leaves an implementer with real questions the standard will not answer: what has been tried, what
worked, and what looked reasonable and was not.

This annex answers those questions from experience, not from authority. It has three subjects:

- **the reference realization**: what it establishes, and what it does not (§2);
- **techniques**: how properties have been obtained, and why none of them is the property (§3);
- **alternative realization models**: how a system built differently satisfies the same semantics
  (§4).

## 2. The reference realization

A reference realization exists. It is one system, built by one group, and its role is narrow.

**What it establishes:** that the normative documents can be satisfied. A standard that nothing has
implemented is a hypothesis. The realization is the evidence against that charge.

**What it does not establish:**

- **that its choices are required.** Every mechanism it uses is one way of obtaining a property.
- **that its arrangement is correct.** Its repository layout, its component boundaries and its
  process count are architecture. The family excludes architecture from normative text.
- **that it conforms.** A realization conforms by discharging claims (Conformance Model). Being the
  one the documents were written alongside does not make it conform. **Resembling it establishes
  nothing** (CF-5). A conformance regime that tests for resemblance tests a choice.

**The direction of authority.** A realization informs the family. It exposes concepts that were
missing, distinctions that were conflated, and requirements that could not be met. It never supplies
authority. Where the two disagree, the document governs, and a ruling resolves the disagreement.
No one edits the document to match what was built.

## 3. Techniques are not invariants

Every technique below obtains a property. **None of them is the property.** A realization that
obtains the property another way conforms.

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
conforming systems, and will pass systems that keep the technique while losing the property.** A
realization can use fully qualified references everywhere and still derive identity from location
somewhere it matters.

## 4. Alternative realization models

The family has a **centre of gravity** around declare → construct → seal → accept → execute, because
that is what the reference realization does. The normative requirement differs from that sequence,
and alternatives live in the difference.

### 4.1 What is actually required

| Required | Not required |
|---|---|
| determination completes before the effect it governs (AI-4) | that it complete at a particular time |
| execution consumes sealed, verified, complete state (SN-4, SN-8, RT-3) | that sealing happen long beforehand |
| resolution completes before what depends on it (AI-5) | that all resolution happen in one pass |
| composition obligations are discharged over the whole (GC-11) | that the whole be constructed at once |

**Order is required. Scheduling is not.**

### 4.2 Construction on admission

An interaction arrives. The system determines, seals and verifies the candidates it needs. Execution
proceeds against what was sealed.

This conforms. Governed Construction states explicitly that a realization may discharge its
obligations "long before execution or just before it". The Snapshot Standard leaves open when
sealing occurs. Such a realization must not let the interaction influence the determination. The
arriving request selects among what may be constructed. It does not extend it (SN-10, Governed
Interaction Boundary §8).

### 4.3 Incremental determination

The system determines candidates one at a time, and construction proceeds as each is admitted.

This conforms provided that, **for each candidate, everything that depends on that candidate's
legality follows its determination** (Governed Construction §6). Such a realization may not carry an
undetermined candidate forward and expect something later to catch it.

### 4.4 Distributed construction

The system constructs parts independently, on different machines, at different times.

This conforms for the parts. **It does not conform until the composition obligations are discharged
over the whole**: identity over the composition, agreement among copies, and rules that quantify
universally (GC-11, GC-12). Parts that are each admissible need not compose into an admissible whole.
A distributed construction that assembles part-level results has skipped the obligations that exist
only at composition scale.

### 4.5 No retained representation

The system constructs, seals in memory, verifies, executes, and retains nothing.

This conforms as to execution. It gives up everything that depends on retention. Past determinations
become unestablishable. Replay becomes impossible. Evidence covers only what was kept. Whether that is
acceptable is a profile's question, and one worth answering deliberately, not by default (Evidence,
Attestation & Provenance §11).

### 4.6 Determination performed elsewhere

A separate service, a shared authority or another system evaluates the closure.

**A determination is a determination wherever it was made.** What matters is the closure it was made
under, and that its evidence carries that closure (Execution Environment Profiles §8.1). Such an
arrangement must not let unavailability become permission. An unreachable determination service is
an inability to determine, and inability to determine refuses (AI-6).

### 4.7 The rule for anything not listed

**Suppose this annex cannot show how an alternative model conforms. That is evidence of an
over-specified normative document, and it is handled as a finding against that document.** It is not
a defect in the alternative.

The family claims to specify semantics, not architecture. Suppose an alternative satisfies every
semantic requirement and is still excluded. It has found a place where a normative document described
a mechanism while believing it described a meaning.

## 5. Hazards

Reasonable people have reached each of these for reasonable-sounding reasons.

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

**The last two survive review**, because both produce results that look correct. An empty answer
looks the same as a true negative. A rule set that has never refused looks the same as one governing
a system that has never violated it.

## 6. The realization map

Picture a mapping from each normative document to where the reference realization demonstrates it:
which declarations, which construction path, which region of the sealed representation, and which
evidence. It would serve two purposes:

- An implementer reconstructs it anyway, by reading the code. Supplying it saves every implementer
  the same rediscovery.
- **A normative document with no demonstration is either unimplemented or unimplementable.** The
  mapping shows which.

The map was parked while most documents were unwritten. A mostly empty map would have shaped
documents before anyone drafted them. That reason has expired, because both sides now exist.

**Such a map is maintained alongside this family as the *Realization Map*.** It is partial. It is
stated against a named snapshot of the reference realization. It is **not a document of this
family**. It declares no part, discharges no membership condition, and takes no part in revision or
supersession. A map inside the revision unit would let a change in a codebase move this family's
revision identity. That reverses the direction of authority stated in §2.

The map must never become a specification. It is evidence about one realization, and §2 governs what
such evidence establishes.

**The map carries a second part.** For each finding, it asks one question. Is the finding evidence
that a normative document underdetermines something? Or is it evidence that one realization erred
inside a space a document already determines? Only the first kind bears on this annex. A hazard named
in §5 arrives that way. Some entries cannot be stated without describing what one realization built.
Such an entry is that realization's answer, not a problem with the family, and this annex does not
state it.

## 7. What this annex cannot do

- **It cannot make anything conformant.** Following every recommendation here discharges no claim.
- **It cannot excuse anything.** No difficulty described here relaxes an obligation. Where an
  implementation cannot satisfy one, that is a finding, not an exception.
- **It cannot be cited normatively.** A claim that rests on a sentence in this annex rests on nothing
  the family requires.
- **It will age.** Its techniques and hazards reflect what has been built and what has gone wrong so
  far. The normative documents are meant to outlast that. This annex is not.
