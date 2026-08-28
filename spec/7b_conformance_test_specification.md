# Conformance Test Specification

## 1. Scope

This document specifies the **demonstrations** by which a conformance claim is established: what a
demonstration must state, what makes one adequate, and what a result does and does not establish.

It closes Part VII. The Conformance Model specifies what a claim is and which discharge class
establishes which kind of obligation; this document specifies what a demonstration of that discharge
must look like.

**It specifies no framework, no harness, no language, and no test suite.** What is required is what
must be shown; how it is shown is unconstrained. A demonstration may be an execution, an analysis, a
comparison, a re-derivation, or an inspection performed by a person.

**It also specifies no tests for any particular realization.** A demonstration that cannot name the
obligation it discharges is not a conformance demonstration — it is a test of an implementation, and
this document is not about implementations.

This document introduces the terms **demonstration**, **fixture**, **negative demonstration**, and
**demonstration coverage**.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What a demonstration is

A **demonstration** discharges one obligation for one subject. *Discharge* is the Conformance
Model's term and covers positive obligations, prohibitions, and refusals alike (7a §4).

Every demonstration MUST state:

| States | Meaning |
|---|---|
| **the obligation** | the one it discharges, by its identifier |
| **the subject** | what is examined, and of which subject class (7a §3) |
| **the discharge class** | observational, structural, comparative, or derivational (7a §7) |
| **what must be shown** | the condition establishing the obligation holds |
| **what constitutes failure** | the condition establishing it does not |

**A demonstration stating no obligation demonstrates nothing about conformance.** It may be a
perfectly good test of something; it is not part of a conformance claim, and including it inflates
the claim without strengthening it.

### 2.1 A demonstration is not necessarily an execution

Structural and comparative discharges are not run. A demonstration that a path does not exist is an
analysis; a demonstration that two runtimes agree is a comparison of two results.

**A conformance regime that can only execute cannot discharge negative properties** (CF-9), and will
report success over exactly the obligations that matter most.

## 3. Positive and negative demonstrations

| | Shows | Required for |
|---|---|---|
| **positive** | the subject does what the obligation requires | every obligation stating something must hold or occur |
| **negative — refusal** | the subject refuses what the obligation forbids, when presented with it | an obligation whose consequence is a refusal of something that can be presented (§3.1) |
| **negative — absence** | the forbidden thing does not exist to be presented — no such path, capability, representation, or reachability | an obligation forbidding a structural possibility, which no input can elicit (§3.2) |

**Negative demonstrations are not optional, and they are not error handling.** This family's
obligations are dominated by refusal: what may not be admitted, what may not be routed on, what may
not be read, what may not proceed. A claim demonstrating only that a system works has demonstrated
the smaller half.

### 3.1 Required refusals

**For every obligation whose consequence is refusal, a demonstration MUST exhibit the refusal.**

It is not sufficient to show that the refusing mechanism exists, that it is reachable, or that it
refused something once. The demonstration MUST present a subject the obligation refuses, and
establish that:

- **the refusal occurred** — the act did not proceed;
- **nothing partly proceeded** (EN-10, GC-6);
- **the grounds were established** — what was proposed, what refused it, under what closure and
  authority (EN-8);
- **the cause was distinguished** — rule refusal or closure failure (EN-9).

A refusal demonstration that checks only that something failed has established an error, not a
governed refusal.

### 3.2 Absence demonstrations

**Not every prohibition can be demonstrated by refusing something.** An obligation stating that a
path does not exist, that a capability is unreachable, or that a representation cannot be produced
forbids a *structural possibility*, and there is no input that elicits it — the demonstration that
would exhibit a refusal is the demonstration that would exhibit the defect.

For such an obligation the demonstration MUST establish absence over a **stated search space**,
which is what distinguishes it from having looked and found nothing:

- **what was searched** — the sealed representation, the declared surface, the reachable call graph,
  whichever the obligation is stated over;
- **that the search was total over that space** — an absence established over part of a space is an
  absence nowhere;
- **that the space is the one the obligation speaks of.** An obligation about reachable execution
  paths is not discharged by searching declared ones.

These are structural or comparative discharges (7a §7.2, §7.3), never observational: **a system
having run without exhibiting the forbidden thing is not evidence that it cannot** (7a §8). The
family's negative properties are dominated by this form — no ungoverned read path, no execution
reachable from inspection, no behavior entering from outside a snapshot — and a regime that
recognises only the refusal form reports conformance while never establishing the prohibitions that
matter most.

**CD-4 applies unchanged.** An absence demonstration must be capable of failing, which means it must
be shown to find the forbidden thing when the forbidden thing is present — established against a
fixture that contains one.

## 4. A demonstration must be able to fail

**A test suite is not evidence that its tests can fail.**

This is the same rule the family applies to rules (2f §4.2) and to transformation rule sets (4d
§5.1), applied to demonstrations themselves — and it is where conformance regimes most reliably
become ceremonial.

- **Every demonstration MUST be shown capable of failing**: exhibit a subject or condition under
  which it does not establish the obligation. For an observational demonstration that is a subject
  it rejects; for a structural one, a reachable path it finds; for a comparative one, variants that
  differ; for a derivational one, a re-derivation that does not match.
- A demonstration that has never failed is not thereby sound. A demonstration that *cannot* fail is
  vacuous, and passes forever over an unexamined subject.
- **Vacuous demonstrations are worse than absent ones**, because they produce results. Coverage
  appears complete; the obligation is no more established than if nothing had been written.

The failure modes are specific and none is visible by reading the demonstration:

- a demonstration that examines the wrong artifact, and finds nothing wrong with it;
- a demonstration whose subject does not contain the condition it checks, so the check never applies;
- a demonstration resolving a name loosely, satisfied by something adjacent;
- a demonstration that reports success on absent material rather than refusing (5b §9).

**Confidently empty and wrong is the characteristic result.** A demonstration MUST refuse where its
subject is malformed, absent, or unreadable, and MUST NOT report success (IN-9).

## 5. Demonstrating by discharge class

### 5.1 Observational

Exercise the subject and compare behavior against the obligation.

- The subject MUST be exercised in a state where the obligation applies. A demonstration that
  exercises a path the obligation does not govern establishes nothing about it.
- **Both branches MUST be exercised** where an obligation has one: the case that proceeds and the
  case that refuses.

### 5.2 Structural

Examine the subject for the absence of a path, without running it.

- The demonstration MUST state **what path is sought** and **over what** the search was total. A
  structural demonstration that examined part of a subject has established the property over that
  part only, and MUST say so.
- **Transitive reach MUST be followed** where the obligation is transitive (CP-7). A search stopping
  at first-level references establishes a first-level property.
- Where totality cannot be established, the demonstration **fails**; it does not report the property
  as holding over what it managed to examine.

### 5.3 Comparative

Vary what must not matter, and compare governed consequences.

- The demonstration MUST state **what was varied**, **what was held constant**, and **what
  equivalence was required**.
- **The variants MUST be genuinely independent.** Two runtimes sharing the component under test, two
  protocols sharing an adapter, or two environments differing only in name establish nothing — the
  substitution did not substitute.
- Observational differences that are not governed consequences MUST be excluded from the comparison
  by the declared determinative/observational split (EV-5), not by ad-hoc filtering.

### 5.4 Derivational

Re-derive from what was supplied and compare with what was recorded.

- The demonstration MUST re-derive **from the evidence, representation, or source representation the
  claim supplied**, and MUST NOT consult the producing system (EV-16).
- Where the re-derivation and the record differ, **the difference is the finding**, and the
  demonstration MUST NOT reconcile them.

## 6. Fixtures

A **fixture** is material a demonstration is performed against.

- **A fixture MUST be declared and identified**, and MUST be part of what a claim supplies. A
  demonstration against material an evaluator cannot obtain is not a demonstration to that evaluator.
- **A negative demonstration requires a fixture that violates the obligation.** A fixture set
  containing only well-formed material cannot exhibit a refusal, and a claim whose fixtures are all
  valid has no negative demonstrations however many it lists.
- **A fixture MUST NOT be repaired to make a demonstration pass.** Where a demonstration fails
  against a fixture believed correct, either the fixture or the subject is wrong, and determining
  which is the work. Adjusting the fixture until the result is green destroys the finding.
- Fixtures are versioned with the claim. A demonstration result is against the fixtures that produced
  it.

## 7. Coverage

**Demonstration coverage** is the relation between the obligations binding a subject and the
demonstrations establishing them.

- **Every obligation binding a claimed subject MUST have at least one demonstration.**
- **An obligation with no demonstration MUST be reported** as part of the claim, not omitted. A claim
  silently covering some obligations is indistinguishable from one covering all of them.
- **Coverage counts obligations, not demonstrations.** Ten demonstrations of one obligation are one
  obligation covered.

### 7.1 What coverage does not establish

Full coverage establishes that every obligation was addressed. It does not establish that:

- the demonstrations were adequate (§4);
- the discharge classes were correct (CF-8);
- the fixtures could exhibit failure (§6).

**A claim with complete coverage, all-observational discharges, and no failing fixtures has
established very little at considerable expense** — and will present as more rigorous than a claim
with three structural demonstrations that could each have failed.

## 8. Demonstrations for a system instance

A system instance claim is discharged by discharging every applicable subject class (CF-3). Its
demonstrations are the demonstrations of those subjects, plus one class that exists only over the
whole:

- **composition obligations** (GC-11) — rules quantifying over the whole, agreement among copies of
  one identity, and composite identity. These cannot be demonstrated over any part, and a claim
  assembling part-level results has not addressed them.

## 9. Genesis demonstrations

The first transformation and the first snapshot are governed like any other and MUST be demonstrated
like any other (TR-15a, SN-13).

Two demonstrations are specific to genesis:

- **that the claimed profile was not authored by what claims it** (NP-7, SN-7) — a structural
  demonstration about authorship, not a check that a profile was named;
- **that the first baseline satisfies both conditions** — consistency with its own declared
  governance, and satisfaction of the claimed profile (1b §11). A demonstration establishing only the
  first has demonstrated self-consistency, which every vacuous genesis also satisfies.

**A profile whose systems are constituted rather than inherited is the subject of both.** At genesis
the claimed profile is the only thing constraining the proposal (6a §1, SM-11), so a profile
supporting a claim about a system it constitutes supports a claim about genesis whether it names one
or not, and 6a §7 requires it to decide what discharges that claim. **What such a profile decides is
what its fixtures are** — which proposal, which authorship record, which baseline — not which
discharge class applies, which is settled above and is the evaluator's question (CF-8).

## 10. What a result establishes

- **A passing demonstration establishes its obligation for its subject, against its fixtures, under
  its discharge class.** It establishes nothing broader, and a claim that generalizes from it has
  overclaimed.
- **A failing demonstration establishes a finding.** It is not a flaky result to be re-run until it
  passes; a demonstration that passes on repetition after failing has established that something
  varies, which is itself a finding (GC-10).
- **An unrun demonstration establishes nothing**, and MUST NOT be reported as anything other than
  unrun.

## 11. What this document does not specify

- **Any framework, harness, runner, or language.**
- **Any test for any particular realization.** No demonstration here names an implementation.
- **How demonstrations are automated, scheduled, or integrated.**
- **Who runs them.** A claimant may; an evaluator may; the result is what was established, not who
  established it.
- **Pass thresholds.** There are none: an obligation is discharged or it is not (CF-11).

## 12. Normative invariants

- **CD-1.** A demonstration MUST state the obligation it discharges, its subject, its discharge
  class, what must be shown, and what constitutes failure (§2).
- **CD-2.** A demonstration stating no obligation MUST NOT form part of a conformance claim (§2).
- **CD-3.** Every obligation whose consequence is refusal MUST have a demonstration exhibiting the
  refusal, its grounds, its cause, and that nothing partly proceeded (§3.1).
- **CD-4.** Every demonstration MUST be shown capable of failing (§4).
- **CD-5.** A demonstration MUST refuse where its subject is malformed, absent, or unreadable, and
  MUST NOT report success (§4).
- **CD-6.** A structural demonstration MUST state what path was sought and over what its search was
  total, and MUST follow transitive reach where the obligation is transitive (§5.2).
- **CD-7.** A comparative demonstration MUST use genuinely independent variants, and MUST state what
  was varied and held constant (§5.3).
- **CD-8.** A derivational demonstration MUST re-derive from supplied material and MUST NOT consult
  the producing system (§5.4).
- **CD-9.** A fixture MUST be declared, identified, and supplied with the claim (§6).
- **CD-10.** A negative demonstration MUST use a fixture that violates the obligation (§6).
- **CD-11.** A fixture MUST NOT be adjusted to make a demonstration pass (§6).
- **CD-12.** Every obligation binding a claimed subject MUST have a demonstration, and any obligation
  without one MUST be reported (§7).
- **CD-13.** A system instance claim MUST include demonstrations of composition obligations, which
  MUST NOT be assembled from part-level results (§8).
- **CD-14.** A genesis claim MUST demonstrate that the claimed profile was not authored by what
  claims it (§9).
- **CD-15.** A failing demonstration MUST be reported as a finding, and MUST NOT be discharged by
  repetition (§10).
- **CD-16.** A demonstration MUST NOT be reported as establishing anything broader than its stated
  subject, obligation, fixtures, and discharge class (§10).
- **CD-17.** An obligation forbidding a structural possibility MUST be discharged by an absence
  demonstration over a stated and totally searched space, and MUST NOT be discharged by a refusal or
  by observation (§3.2).

## 13. Conformance

The conformance subject of this document is a **demonstration set**: the demonstrations, fixtures,
and results supplied to discharge a conformance claim.

A demonstration set conforms when every demonstration names its obligation and class, every refusal
obligation is exhibited, every demonstration has been shown capable of failing, negative
demonstrations use violating fixtures, coverage is stated including its gaps, and no result claims
more than it established.

**The test to apply to a demonstration set is the one it applies to everything else: can it fail?**
A set that has never failed, over a system that has never been wrong, examined by demonstrations
none of which has been shown able to reject anything, is not evidence of conformance. It is evidence
that nothing has been checked — and it is indistinguishable, from the outside, from the case where
everything is correct.

That indistinguishability is the whole reason this document requires what it requires.
