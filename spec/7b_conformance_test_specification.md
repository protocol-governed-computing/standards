# Conformance Test Specification

## 1. Scope

This document specifies the **demonstrations** that establish a conformance claim. It covers:

- what a demonstration must state;
- what makes a demonstration adequate;
- what a result does and does not establish.

This document closes Part VII. The Conformance Model specifies what a claim is, and which discharge
class establishes which kind of obligation. This document specifies what a demonstration of that
discharge must look like.

**This document specifies no framework, no harness, no language and no test suite.** It requires what
must be shown, and leaves open how it is shown. A demonstration may be an execution, an analysis, a
comparison, a re-derivation, or an inspection performed by a person.

**It also specifies no tests for any particular realization.** A demonstration must name the
obligation it discharges. One that cannot is not a conformance demonstration. It is a test of an
implementation, and this document is not about implementations.

This document introduces the terms **demonstration**, **fixture**, **negative demonstration**, and
**demonstration coverage**.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What a demonstration is

A **demonstration** discharges one obligation for one subject. *Discharge* is the Conformance Model's
term. It covers positive obligations, prohibitions and refusals alike (Conformance Model §4).

A demonstration addresses a single obligation for a single subject. It establishes nothing beyond
them (§10).

Every demonstration MUST state:

| States | Meaning |
|---|---|
| **the obligation** | the one it discharges, by its identifier |
| **the subject** | what is examined, and of which subject class (Conformance Model §3) |
| **the discharge class** | observational, structural, comparative, or derivational (Conformance Model §7) |
| **what must be shown** | the condition establishing the obligation holds |
| **what constitutes failure** | the condition establishing it does not |

**A demonstration that states no obligation demonstrates nothing about conformance.** It may be a
perfectly good test of something. It is not part of a conformance claim. Including it inflates the
claim without strengthening it.

### 2.1 A demonstration is not necessarily an execution

Structural and comparative discharges are not run. A demonstration that a path does not exist is an
analysis. A demonstration that two runtimes agree is a comparison of two results.

**A conformance regime that can only execute cannot discharge negative properties** (CF-9). It will
report success over exactly the obligations that matter most.

## 3. Positive and negative demonstrations

| | Shows | Required for |
|---|---|---|
| **positive** | the subject does what the obligation requires | every obligation stating something must hold or occur |
| **negative — refusal** | the subject refuses what the obligation forbids, when presented with it | an obligation whose consequence is a refusal of something that can be presented (§3.1) |
| **negative — absence** | the forbidden thing does not exist to be presented — no such path, capability, representation, or reachability | an obligation forbidding a structural possibility, which no input can elicit (§3.2) |

**Negative demonstrations are not optional, and they are not error handling.** Refusal dominates this
family's obligations: what may not be admitted, routed on, read or allowed to proceed. A claim that
demonstrates only that a system works has demonstrated the smaller half.

### 3.1 Required refusals

**For every obligation whose consequence is refusal, a demonstration MUST exhibit the refusal.**

It is not enough to show that the refusing mechanism exists, that it is reachable, or that it refused
something once. The demonstration MUST present a subject the obligation refuses, and establish that:

- **the refusal occurred**: the act did not proceed;
- **nothing partly proceeded** (EN-10, GC-6);
- **the grounds were established**: what was proposed, what refused it, and under what closure and
  authority (EN-8);
- **the cause was distinguished**: rule refusal or closure failure (EN-9).

A refusal demonstration that checks only that something failed has established an error, not a
governed refusal.

### 3.2 Absence demonstrations

**Some prohibitions cannot be demonstrated by refusing something.** An obligation may state that a
path does not exist, that a capability is unreachable, or that a representation cannot be produced.
Such an obligation forbids a *structural possibility*, and no input elicits it. The demonstration that
would exhibit a refusal is the demonstration that would exhibit the defect.

For such an obligation, the demonstration MUST establish absence over a **stated search space**. That
is what separates it from having looked and found nothing. The demonstration establishes:

- **what was searched**: the sealed representation, the declared surface or the reachable call
  graph, whichever the obligation is stated over;
- **that the search was total over that space**. An absence established over part of a space is an
  absence nowhere;
- **that the space is the one the obligation speaks of.** Searching declared execution paths does not
  discharge an obligation about reachable ones.

These are structural or comparative discharges (Conformance Model §7.2, §7.3), never observational.
**A system that ran without exhibiting the forbidden thing has not shown that it cannot** (Conformance
Model §8). This form dominates the family's negative properties: no ungoverned read path, no
execution reachable from inspection, no behavior entering from outside a snapshot. A regime that
recognises only the refusal form reports conformance while never establishing the prohibitions that
matter most.

**CD-4 applies unchanged.** An absence demonstration must be capable of failing. So it must be shown
to find the forbidden thing when the forbidden thing is present, against a fixture that contains one.

## 4. A demonstration must be able to fail

**A test suite is not evidence that its tests can fail.**

This is the rule the family applies to rules (Enforcement & Refusal §4.2) and to transformation rule
sets (Governed Transformation §5.1), applied to demonstrations themselves. It is where conformance
regimes most reliably become ceremony.

- **Every demonstration MUST be shown capable of failing.** Exhibit a subject or condition under which
  it does not establish the obligation:
  - for an observational demonstration, a subject it rejects;
  - for a structural one, a reachable path it finds;
  - for a comparative one, variants that differ;
  - for a derivational one, a re-derivation that does not match.
- A demonstration that has never failed is not thereby sound. A demonstration that *cannot* fail is
  vacuous. It passes forever over an unexamined subject.
- **Vacuous demonstrations are worse than absent ones**, because they produce results. Coverage looks
  complete, yet the obligation is no more established than if nobody had written anything.

The failure modes are specific, and reading the demonstration reveals none of them:

- a demonstration that examines the wrong artifact, and finds nothing wrong with it;
- a demonstration whose subject does not contain the condition it checks, so the check never applies;
- a demonstration that resolves a name loosely, and is satisfied by something adjacent;
- a demonstration that reports success on absent material instead of refusing (Governed Inspection
  §9).

**Confidently empty and wrong is the characteristic result.** A demonstration MUST refuse where its
subject is malformed, absent, or unreadable, and MUST NOT report success (IN-9).

## 5. Demonstrating by discharge class

### 5.1 Observational

Exercise the subject, and compare its behavior against the obligation.

- The subject MUST be exercised in a state where the obligation applies. A demonstration that
  exercises a path the obligation does not govern establishes nothing about the obligation.
- **Both branches MUST be exercised** where an obligation has two: the case that proceeds and the case
  that refuses.

### 5.2 Structural

Examine the subject for the absence of a path, without running it.

- The demonstration MUST state **what path it sought** and **over what** its search was total. A
  structural demonstration that examined part of a subject has established the property over that
  part only, and MUST say so.
- **Transitive reach MUST be followed** where the obligation is transitive (CP-7). A search that stops
  at first-level references establishes a first-level property.
- Where totality cannot be established, the demonstration **fails**. It does not report the property
  as holding over what it managed to examine.

### 5.3 Comparative

Vary what must not matter, and compare governed consequences.

- The demonstration MUST state **what was varied**, **what was held constant**, and **what
  equivalence was required**. Captured inputs are among what is held constant (Conceptual Model,
  *captured input*).
- **The variants MUST be genuinely independent.** Two runtimes that share the component under test,
  two protocols that share an adapter, or two environments that differ only in name establish
  nothing. The substitution did not substitute.
- Observational differences that are not governed consequences MUST be excluded from the comparison
  by the declared determinative/observational split (EV-5), not by ad-hoc filtering.

### 5.4 Derivational

Re-derive from what was supplied, and compare with what was recorded.

- The demonstration MUST re-derive **from the evidence, representation, or source representation the
  claim supplied**, and MUST NOT consult the producing system (EV-16).
- Where the re-derivation and the record differ, **the difference is the finding**. The demonstration
  MUST NOT reconcile them.

## 6. Fixtures

A **fixture** is material a demonstration is performed against.

- **A fixture MUST be declared and identified**, and MUST be part of what a claim supplies. A
  demonstration against material the evaluator cannot obtain is not a demonstration to that
  evaluator.
- **A negative demonstration needs a fixture that violates the obligation.** A fixture set of only
  well-formed material cannot exhibit a refusal. A claim whose fixtures are all valid has no negative
  demonstrations, however many it lists.
- **A fixture MUST NOT be repaired to make a demonstration pass.** Suppose a demonstration fails
  against a fixture believed correct. Then either the fixture or the subject is wrong, and the work is
  to determine which. Adjusting the fixture until the result turns green destroys the finding.
- Fixtures are versioned with the claim. A demonstration result stands against the fixtures that
  produced it.

## 7. Coverage

**Demonstration coverage** is the relation between the obligations binding a subject and the
demonstrations that establish them.

- **Every obligation binding a claimed subject MUST have at least one demonstration.**
- **An obligation with no demonstration MUST be reported** as part of the claim, not omitted. A claim
  that silently covers some obligations looks the same as one that covers all of them.
- **Coverage counts obligations, not demonstrations.** Ten demonstrations of one obligation cover one
  obligation.

### 7.1 What coverage does not establish

Full coverage establishes that every obligation was addressed. It does not establish that:

- the demonstrations were adequate (§4);
- the discharge classes were correct (CF-8);
- the fixtures could exhibit failure (§6).

**A claim with complete coverage, all-observational discharges and no failing fixtures has
established very little at considerable expense.** It will still present as more rigorous than a
claim with three structural demonstrations that could each have failed.

## 8. Demonstrations for a system instance

A system instance claim is discharged by discharging every applicable subject class (CF-3). Its
demonstrations are those of the applicable subjects, plus one class that exists only over the whole:

- **composition obligations** (GC-11): rules that quantify over the whole, agreement among copies of
  one identity, and composite identity. No part can demonstrate these. A claim that assembles
  part-level results has not addressed them.

## 9. Genesis demonstrations

The first transformation and the first snapshot are governed like any other, and MUST be demonstrated
like any other (TR-15a, SN-13).

Two demonstrations are specific to genesis:

- **that the claimed profile was not authored by what claims it** (NP-7, SN-7). This is a structural
  demonstration about authorship, not a check that a profile was named;
- **that the first baseline satisfies both conditions**: consistency with its own declared governance,
  and satisfaction of the claimed profile (Semantic Model §11). A demonstration that establishes only
  the first has shown self-consistency, and every vacuous genesis also satisfies that.

**A profile whose systems are constituted rather than inherited is the subject of both.** At genesis,
the claimed profile is the only constraint on the proposal (Normative Platform Profile §1, SM-11). So a
profile that supports a claim about a system it constitutes supports a claim about genesis, whether it
names one or not. Normative Platform Profile §7 requires it to decide what discharges that claim.
**Such a profile decides what its fixtures are**: which proposal, which authorship record and which
baseline. It does not decide which discharge class applies. The text above settles that, and it is
the evaluator's question (CF-8).

## 10. What a result establishes

- **A passing demonstration establishes its obligation for its subject, against its fixtures, under
  its discharge class.** It establishes nothing broader. A claim that generalizes from it has
  overclaimed.
- **A failing demonstration establishes a finding.** It is not a flaky result to re-run until it
  passes. A demonstration that passes on repetition after failing has established that something
  varies, and that is itself a finding (GC-10).
- **An unrun demonstration establishes nothing**, and MUST NOT be reported as anything other than
  unrun.

## 11. What this document does not specify

- **Any framework, harness, runner or language.**
- **Any test for any particular realization.** No demonstration here names an implementation.
- **How demonstrations are automated, scheduled or integrated.**
- **Who runs them.** A claimant may, and so may an evaluator. The result is what was established, not
  who established it.
- **Pass thresholds.** There are none. An obligation is discharged or it is not (CF-11).

## 12. Normative invariants

- **CD-1.** A demonstration MUST state the obligation it discharges, its subject, its discharge class,
  what must be shown, and what constitutes failure (§2).
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

The conformance subject of this document is a **demonstration set**: the demonstrations, fixtures and
results supplied to discharge a conformance claim.

A demonstration set conforms when all of the following hold:

- every demonstration names its obligation and class;
- every refusal obligation is exhibited;
- every demonstration has been shown capable of failing;
- negative demonstrations use violating fixtures;
- coverage is stated, including its gaps;
- no result claims more than it established.

**Apply to a demonstration set the test it applies to everything else: can it fail?** Picture a set
that has never failed, over a system that has never been wrong, examined by demonstrations none of
which has been shown able to reject anything. That is not evidence of conformance. It is evidence that
nothing has been checked. From outside, it looks exactly like the case where everything is correct.

That resemblance is the whole reason this document requires what it requires.
