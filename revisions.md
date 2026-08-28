# Revision Record

The declared supersession relations between revisions of this family.

`4e` §9 governs: a revision of a document supersedes the revision it replaces, and **the relation is
declared rather than inferred from a number or a date.** `VERSION` carries the current revision's
identity; this document carries the relation, what it changes, and what it invalidates. A revision
that appears in `VERSION` and not here has not been declared.

**This record is not a document of the family.** It declares no part and states no requirement — it
is where the family's own supersession declarations live, in the same sense that a successor artifact
carries its `supersedes`.

---

## `v0` supersedes `draft-3`

**Predecessor:** `draft-3` — thirty-two documents, twenty-eight declared changes, frozen.

**`v0` is this family's first non-draft identity.** The version is a single number and it starts at
zero: **ground zero**, the first identity anyone may build against and name in a claim. It is not
a semantic version and carries no major, minor or patch — `4e` §9 holds that a revision is declared
rather than inferred from a number, so the number counts revisions and asserts nothing else.

**Worked under the identity `draft-4`, declared as `v0`.** `draft-4` was the working name while the
revision was open. It was never frozen and never tagged, no claim was made against it, and nothing
outside this repository named it. The single supersession is therefore `draft-3` → `v0`, and Change
1 below is its content.

**Occasioned by exposure, not by a defect.** No finding forced this. Four gates of independent
authoring, realization, execution and transformation produced no undeclared gap in the standard, and
the instruments that examine the text — the terminology and requirement projections — run clean.
**What the programme cannot manufacture is a reader who has not been part of it.** A draft identity
signals *provisional*, and that signal now costs more than it buys.

**It invalidates nothing.** Change 1 altered no obligation on a realization: it repaired
declarations,
moved a definition, declared five refinements, and added **CM-8**, which binds documents of this
family rather than systems. A realization conforming to `draft-3` conforms to `v0` unchanged.

**Five findings are carried into `v0` and are published with it**, each with what would settle it:
**B** (no demonstration for the specification subject class), **C** (`0z` states MUSTs and carries
no
invariants), **C-1** (a demonstration must be capable of failing; nothing requires showing which one
does), **C-2** (`3a` does not name the case that distinguishes read routing from hard-coded routing
that matches), and **C-3** (a profile exclusion bars comparability, and `7a` §10 does not say so).

**Two of those would change what conformance costs.** C-1 and C-2, if carried, may require evidence
a claimant does not need today. Systems claiming `v0` keep their claims — `0z` §5.1: a later
revision does not reach backwards into claims discharged against an earlier one — but a successor
may ask more. Said here rather than left to be discovered.

**Occasioned by the freeze itself.** `draft-3` closed with four findings recorded as outstanding
against it, and a frozen revision cannot absorb them — that is what freezing means. A successor must
exist to hold them, and it must exist before the first one is carried rather than being created to
accommodate it. Opening it now also settles a question that would otherwise be answered under
pressure: **where does the first external finding land?**

**This does not reopen `draft-3`.** The freeze holds. `draft-3`'s text is closed to change, and
nothing arriving after it amends that revision — a finding against `draft-3` is an occasion for a
change here, declared against `draft-3` as its named predecessor (`0z` §5.1, `4e` §9). Systems that
claimed `draft-3` claimed what they claimed; whether they satisfy this revision is a fresh question,
determined fresh (`6a` §9).

### Carried forward from `draft-3`

Four findings were recorded as outstanding at the freeze. **None is yet a change** — each is a
candidate, and each may end as a declared change, a narrowed concern, or a finding considered and
declined with the reason.

| | Finding | Why it was not carried into `draft-3` |
|---|---|---|
| **A** | Whether `6a` should tell a profile author what to notice is missing. Both authoring trials produced logs that under-reported: the family gives an author the list of what to decide (§7) and no way to tell a deliberate silence from an omission. | A new normative section, not a repair to one. |
| **B** | `7b` specifies no demonstration for the **specification** subject class. `7a` §3 names it; `7b` does not mention it. | Carried forward unchanged from `draft-3` Change 10. |
| **C** | `0z` states three MUSTs and carries no invariants. Whether a document governing the family's own construction should carry them is unresolved. | Different in kind from whether `1a` should, which Change 10 settled. |
| **D** | `4d` remains the document with the most vocabulary of its own and the largest invariant set. Narrowed by Change 8's re-review and by Change 26, and not closed. | A clause-by-clause re-review against `8a` §4.7 is what would settle it, and was not undertaken. |

### Recorded against this revision

Findings arising from work done here, on the same terms as those carried forward: a candidate, not
a change.

| | Finding | Why it is not carried |
|---|---|---|
| **E** | Nothing says when a word must become a term. CM-3 requires a document introducing a term to define it, and CM-8 requires the term to sit where its subject matter puts it, but neither says a word must be introduced at all — so nothing distinguishes a term the family needs from a word an author chose to bold. Six terms are declared, defined, and used nowhere afterward: `Promotion` (`1a`), `construction disposition` (`2c`), `projection source` (`4b`), `protocol adapter` (`5a`), `profile derivation` (`6a`), `demonstration coverage` (`7b`). | A new invariant, discharged by every document demonstrating that each term it introduces is used. Six of 167 may not justify one, and the obvious formulation — that family vocabulary must span documents — is contradicted by the evidence: 31 terms are local to one document and 15 of those carry that document's own invariants. |

| **F** | Whether the domain-neutral semantic spaces a runtime must recognize belong in the ontology as a third axis. The reference realization's development converged on nine such spaces, held to be orthogonal and canonically complete; the family names no such axis, and answers *"domain-neutral with respect to what?"* only through `2d`'s open kind vocabulary and a profile's closure over it. | An ontology revision under `2b` §9, which "invalidates every category contract, kind classification, and cross-cutting obligation stated in terms of the affected category". Three things in `2b` stand against it as posed: **Concern** is already defined (§7.2) as *what is being decided about* and stated there to be **not an ontology axis**; §7.1 rejects axes that are "the category restated as a verb", and several of the nine map onto existing categories — occurrence onto **Evidential**, exposed boundary onto **Contractual**, behavior onto **Operational**; and §9's criterion is whether admitting a genuinely new kind requires changing the ontology, where a set derived from one realization's kinds is the named failure. |

The evidence to settle **F** does not exist yet and is a by-product of NOVA **G0**: an independent
author, working from the standard alone and with no sight of the nine, must close a kind vocabulary
for the profile it authors. Convergence on a similar set is evidence the spaces are canonical;
divergence is evidence they were artifacts of one realization. Asserting them into `2b` first would
destroy the experiment that could justify them.

The evidence is in `projections/vocabulary_locality.md`, including its bearing on Finding **D**:
`4d` owns 11 terms, 4 are local to it, and all 4 are cited by a `4d` invariant. `4d` did not invent
vocabulary nothing uses, which narrows D to whether its subject requires that much — the `8a` §4.7
re-review, still not undertaken. `5a` and `2c` each carry 5 local terms and were never the subject
of a finding.

**Change 1 produced two instances of E and corrected them.** `6c`'s pair was reported by the first
harvest as declared and unused; the triage judged that §3 names the distinction and defined them
rather than striking them. They were then declared, defined, and still unused. They are struck in
Change 1 as first proposed — recorded because writing a definition is the tempting remedy for an
unused declaration, and it is the wrong one.

### G0 run `NPP-C`

The first authoring trial against this revision, run by an external worker at commit `e736800d`
under an honour-based firewall. Its integrity held: all 32 documents in the sandbox came back
byte-identical to the pinned commit.

**Finding A is ANSWERED. `6a` supports the distinction.** It took three runs to establish, and the
first two failed for the same reason in different forms.

Run `NPP-C` was handed a taxonomy naming the very distinction A says the family lacks; its clean log
showed the commission working and said nothing about `6a`. Run `NPP-D` ran under a repaired
commission but in the same worker's context, and carried the withdrawn vocabulary forward — a phrase
absent from the commission it was given, and present in the one before it. Run `NPP-E` ran fresh,
with no prior context, and separated the two cases from the text alone: eleven determinations
*expressly permitted by source*, eight *unresolved by family*.

**What rules out recall** is that `NPP-E` extended the claim-type vocabulary as `NPP-D` had, but
with different constructions for the same distinction. Recall reproduces phrasing; derivation
reproduces structure.

**The rule this established outlives G0:** an experiment may constrain the task, but it must not
supply the distinction whose derivability it is measuring — and a worker's memory of an earlier run
is the same contamination reached by a route no prohibition on handed-over material covers.

**Finding F is settled on the question it asked, and not in the way expected.** Three runs closed
three vocabularies from byte-identical text under one scope. `NPP-C` and `NPP-D` closed four kinds
each and match one another — which is the carry-over, not agreement. `NPP-E`, the run that could not
remember, closed five and diverged from both, reaching **workflow** and **capability contract**,
concepts neither earlier run touched.

The result is therefore not *four rather than nine*. It is that **the standard determines no
vocabulary at all**, and `2d` §1 says it must not: *"a family that named its kinds would admit
exactly one platform, and PGC admits as many as there are profiles."* Variation between closures is
the specified behaviour.

**A set the family deliberately declines to determine cannot be a canonical axis of its ontology.**
Where such a set belongs is a profile — which `2d` already says, and which the three runs
demonstrate by closing different ones. F is dispositioned: **not carried into `2b`.**

All three runs share one model, and a different reader would strengthen every line above. It would
not change the divergence, which was observed within one reader.

**One new finding.** The family uses `tenant` in `6b` and `5a` and defines it nowhere, load-bearing
in `6b` where tenants are named as an environmental constraint. The terminology projection is blind
to it by construction — it tracks terms a document declares, and nothing declares this one. It is
Finding **E** from the other side: E asks when a word must become a term; this is a word already
behaving like one.

Two matters the run recorded that are checkable and would matter if they hold: the family supplies
**no form for a profile artifact**, so a profile claim cannot be mechanically checked; and **no
claim vocabulary**, so claim names are not interoperable between profiles. Neither is dispositioned
yet.

The evaluation and the post-run reclassification are in `.github/doc/`.

### Two findings dispositioned, neither carried

**`0z` §2's ranges understate the family by six — declined.** The requirement projection's count
guard found that `SM-1 … SM-12` names twelve positions while `1b` carries fifteen identifiers, the
extra three being `SM-5a`, `SM-7a` and `SM-7b`; `4d` is the same by three more. Range notation
cannot express a suffixed identifier.

**It is not a defect, because the column is not a census.** `0z` §2 opens by stating that a file
identifier is *"an **address**, not an identity"*, and the invariant column is the same kind of
thing: it tells a reader which document to open for `SM-7a`, which it does correctly. Restating it
as counts would create a second statement of one fact that must be maintained in lockstep with the
documents, and would drift from them the first time it was not.

What the finding does establish is a constraint on **instruments**, not on the standard: a check
that treats the map as a count is wrong, and `tools/check_requirement_count.py` adds the suffixed
identifiers explicitly rather than absorbing the difference.

**`tenant` is used and never defined — declined, and an earlier characterization of it withdrawn.**
The term appears twice: `6b` §11 lists *"replication, reachability, bounded staleness, agreement
about which snapshot is current, isolation between tenants"* as things a distributed environment
profile **may** require, and `5a` §12 lists *"a version, a tenant, an authority context"* as scopes
one operation identity may resolve differently across.

**Both are illustrative lists, and `tenant` is ordinary English in them.** It sits beside
`replication`, `bounded staleness` and `authority context`, none of which the family defines either,
and for the same reason: they are examples of what a profile might constrain, not terms the family
requires anything of. `1a` §2 holds that a term not defined in Part I is not a PGC term — and
nothing here uses `tenant` as one.

**The earlier reading, that `6b` makes it load-bearing by naming tenants as an environmental
constraint, was wrong.** `6b` requires that whatever an environment profile constrains be *declared*
as an environmental constraint. That is a requirement about declaration, not about tenants.

### Seven findings dispositioned

Checked against the text rather than accepted as stated. `0z` §3: a finding may end as a declared
change, a narrowed concern, or a finding considered and declined with the reason.

**B — `7b` specifies no demonstration for the *specification* subject class. Carried.** Confirmed:
`7a` §3 names **specification** among seven subject classes, and `7b` refers to subject classes only
by pointing back at `7a` §3. Nothing in `7b` says what a demonstration of a specification looks
like. **This is a new normative section, not a repair to one** — which is why it was not carried
into
`draft-3` and is not carried here. What settles it is authoring that section, and the question it
must answer is what discharges a claim whose subject is a document rather than a running system.

**C — `0z` states MUSTs and carries no invariants. Carried, with its method named.** Confirmed: four
MUST statements, zero invariant identifiers. **This is the shape Change 10 already repaired once**,
when `1a` carried six MUSTs and a conformance clause that nothing could cite. The method is the same
— derive identifiers from the statements already in force, with no wording change and no requirement
that was not already stated. What makes it a decision rather than a formality is that `0z` governs
the family's own construction, so giving it citable requirements makes the family's structure
conformance-checkable against itself.

**D — `4d`'s vocabulary. Narrowed, and its original form closed.** The G0 terminology measurement
settles the concern as stated: `4d` owns eleven terms, four are local to it, and **all four are
cited by its own invariants.** It did not invent vocabulary nothing uses. `5a` and `2c` each carry
five local terms and were never the subject of a finding. **What survives is a different
question** —
whether `4d`'s subject requires that much vocabulary at all — and that is the `8a` §4.7
clause-by-clause re-review, still not undertaken. Carried in that narrowed form.

**E — nothing says when a word must become a term. Declined as an invariant, and its supporting
measurement corrected.** The obvious rule is contradicted by the evidence: 31 terms appear in no
document but the one defining them, and **fifteen of those carry a requirement in that document's
own invariants.** A rule that family vocabulary must span documents would break every one.

**The narrower claim that supported it was wrong.** Six terms were recorded as declared, defined,
and used nowhere afterward. Checking each against its document shows **five are used throughout
under a shortened name** — `construction disposition` as *disposition* ten times, `projection
source` as *source* fifty-nine, `protocol adapter` as *adapter* eighteen, `demonstration coverage`
as *coverage* nine, `profile derivation` as *derivation* three. Only `1a`'s **Promotion** is
genuinely unused, and removing a Part I definition is a revision under CM-7 rather than an editorial
tidy.

**What the measurement actually found is name drift** — the same pattern Change 1 repaired at `2d`
(`kind registry` marked as *registry*) and `3b` (`self-description` marked as *self-describing*).
A term declared in full and used in short is one term with two spellings, not a term nobody needs.

**And it is a stated limitation of the terminology projection**, recorded in
`projections/vocabulary_locality.md`: an occurrence count over the full term cannot distinguish
disuse from abbreviation, and reading it as disuse would have struck five live concepts.

**C-1 — a demonstration capable of failing is required; showing which one fails is not. Carried, and
it is the strongest candidate of the seven.** `7b` CD-4 requires that a demonstration could fail if
the system were non-conforming. It does not require the claimant to identify *which* demonstration
fails when a given guard is removed. NOVA found two guards, correctly implemented, whose removal
broke no test — invisible to a passing suite, to the author, and to a reading of the evidence, and
found only by mutation. **A clarification requiring each claimed normative guard to carry a
documented counterfactual would close it without prescribing tooling.** It is carried rather than
declared because it adds an obligation to every claimant, and that is a change to what conformance
costs.

**C-2 — `3a` §16 does not name the case that distinguishes reading routing from hard-coding it.
Carried.** Confirmed: §16 requires that every step was one the sealed representation contained,
*"reached by declared"* routing. An execution that hard-codes routing which happens to match its
declaration satisfies that sentence. The four cases differ in what they establish — a route
followed,
a route absent, a route retargeted, and **routing that ignores a changed declaration** — and only
the
fourth separates a traversal that reads from one that assumes. NOVA demonstrated exactly this and
had
to be asked for it; nothing in the text asks.

**C-3 — `7a` §10 addresses different profiles, not exclusion. Carried.** Confirmed: §10 says two
systems *under different profiles* are not comparable. A profile that **excludes** a system is a
different case — the system is not under that profile at all, and the sentence does not reach it.
`NPP-E` §12 excludes the reference realization by construction, which is why the comparative gate is
blocked, and the text does not say that an exclusion bars comparison rather than merely barring one
candidate's conformance.

**Five carried, one narrowed and closed in its original form, one declined.** None is repaired here:
four require authoring normative text, and the family's own rule is that a specification edit states
what it changes and what that invalidates before it is made.

### What this revision is waiting for

`draft-3`'s freeze named three tests it had not faced. Findings from any of them are the expected
occasion for changes here, and their absence is itself informative.

- **A claim attempt** — a system built independently of any profile in hand, attempting to claim
one.
- **A second independent realization** — every comparative discharge class in `7a` §7.3 is currently
  unexercised, and RT-12 is stated over exactly that.
- **An authoring trial for `6b` or `6c`** — both instruments so far have been pointed at `6a`.

**A finding is recorded whatever its source, and its source decides nothing** (`0z` §3).
Experience —
from a realization, a reviewer, or a claim attempt — occasions a ruling and is not one. **A finding
declined is recorded here with the reason**, because declining silently invites it again.


### Change 1 — every declared term has a definition, and refinement is exercised for the first time

**Documents:** `1a` §1, §8 (**Step** added), §12, §13 (**CM-8** added), §14; `0z` §2; `2b` §1, §6;
`2d` §3; `2e` §3; `3a` §1, §3; `3b` §1, §2; `3c` §1; `4a` §1, §2; `4c` §1, §6; `5a` §4, §9, §10;
`6a` §3; `6c` §3; `7a` §4.

**Occasioned by** a terminology index derived over the family and checked against `1a` §12 — the
first instrument pointed at the family's own vocabulary rather than at a realization. Its contract
is declared under `0z` §5.2 in `projections/`.

**Twenty-four documents declare the terms they introduce; twelve of those declarations were not
true.** A document would name a term in its declaration sentence and then never define it. The
vocabulary rules were in force the whole time — CM-3 requires a document introducing a term to
define it — and nothing could see that they were being broken, because nothing read the declaration
sentences against the documents that carry them.

**The instrument was wrong before the documents were.** Its first pass reported 124 defects, of
which 111 were its own blindness to conventions the family had used all along: a definition sited in
a section named for the term, a copula sentence, a table row, a definition sharing a line with the
declaration that introduces it. That is recorded here rather than omitted, because a derived index
that is trusted before it is calibrated produces exactly this class of false finding, and the
contract in `projections/terminology_projection_contract.md` now states the conventions it depends on.

**What changes.** Twelve terms, none of which alters an obligation:

- **Seven gained a definition** where their document already declared them: `jurisdiction` (`2e` §3),
  `evaluator` (`7a` §4), `external protocol` and `governed result` and `governed executable target`
  (`5a` §10, §9, §4), `extension point` (`6a` §3), and `kind registry` (`2d` §3). Each is written
  from what its own document already asserts, in the form that document already uses.
- **Four were struck from their declaration.** For two, defining them would have created the overlap
  CM-3 forbids: `3c` no longer introduces `execution agent`, because `1a` §8 defines **Runtime** as
  "the agent that performs execution" and a second name for one concept is the defect CM-3 names;
  `4a` no longer introduces `admissibility determination`, a transparent compound of
  **Admissibility** (`1a` §7) and **determination** (`1b` §4). For the other two, `6c` no longer
  introduces `platform-owned governance` or `domain-owned governance`: the document names the
  distinction in its §3 table and never uses either phrase, and defining them produced two
  definitions nothing read. §3 is unchanged from `draft-3`.
- **`step` moves to `1a` §8.** `1a` §8 defined **Workflow** as "a declared structure of governed
  steps" while `step` itself was owned by `3a` — a Part I definition resting on a Part III term,
  against `1a` §2. `1a` now defines it; `3a` refines it.

**Refinement is exercised for the first time.** CM-2 requires a document needing more of an
inherited concept to refine it and say what it is refining, and no document had ever done so. Five
now do: `3a` §3 over `step`, `3b` §2 over `snapshot`, `2b` §6 over `provenance`, `4c` §6 over
`resolution`, `4a` §2 over `candidate`. Four were already refinements in substance — `3b` §2 adds
five properties to `1a`'s snapshot, `2b` §6 adds the authored/derived/produced vocabulary, `4c` §6
states what resolution must do where an identity is what is resolved, and none of them restated what
the concept *is*. What each document did wrong was *declare* that it introduced the term, which
states the opposite of the relation CM-2 requires. In those four only the declaration changed.

**`4a`'s candidate was the one real duplication.** `4a` §2 opened "A **candidate** is a declaration
that has been produced but not yet admitted", which answers again what `1a` §10 already answers. The
second *is* clause is removed; what construction adds is kept — that the candidate is a declaration,
and that its non-existence holds until a determination admits it.

**Ownership was determined by semantic primacy, not by document order.** The rule applied, and
recorded here because the family does not yet state it: `1a` owns a term when the term is required
to understand several parts of the family and its identity does not depend on one later standard's
mechanism; a subject standard owns a term that exists principally because of that standard's subject
matter. A later document *refines* when it preserves the inherited identity and adds what its domain
requires, and *redefines* — violating CM-2 — when it answers again what the concept is.

Applying that to `candidate` was not obvious from wording. Near-verbatim duplication is evidence of
an accident, not of ownership, so the test was usage breadth: `candidate` appears in ten documents,
and `1b` §4 defines **proposal** as "a candidate change presented to a governed state". A Part I
document using the term to define one of its own settles it — the concept is family-wide, and the
alternative reading, that construction owns it, would leave `1b` resting on a Part IV term. That is
the same defect this change repaired for `step`.

**What it invalidates.** Nothing. No invariant is added, removed, or altered; no obligation changes
scope; no *distinguish from* is drawn or dropped. Every definition states what its document already
relied on, and a realization conforming to `draft-3` conforms to this unchanged.

**The ownership rule becomes CM-8.** It was applied four times in this change and stated nowhere
in the family: `1a` §12 carried the usage rules and CM-2 required refinement, but nothing said how
to decide which document owns a term in the first place. `1a` §12 now states it, §13 carries it as
**CM-8**, §14 adds the matching conformance condition, and `0z` §2's `1a` row reads `CM-1 … CM-8`.

This is the one part of the change that adds a requirement rather than repairing a declaration, and
it is stated as the rule that was already being followed: the family's terms sit where their subject
matter puts them, and `1a` §8 defining **Runtime** while `3c` specifies it is that rule in force
before it was written down. What CM-8 forbids is the contrary reading — that a term belongs to `1a`
because `1a` comes first — which would make the Conceptual Model a warehouse for whatever was
written down earliest.

**What CM-8 invalidates.** No existing definition. The four determinations this change made are the
first application of the rule, and every one of them left the term where the rule puts it. A document
of the family that placed a term wrongly would now be non-conforming under `1a` §14, and none is
known to.

**Also outstanding, smaller.** `2d` §3 labels its table row `**registry**` while the term it
declares is `kind registry`; `3b` marks `**self-describing**` where it declares `self-description`.
The definitions are now sited and the drift is cosmetic, but a family whose terms are load-bearing
should probably not mark them under two spellings.

---

## `draft-3` supersedes `draft-2`

**Predecessor:** `draft-2` — twenty-six documents, seven declared changes, frozen.

**Occasioned by** the family's own need, not by a realization. `draft-2` closed with a machine-
readable rendering of its requirements demonstrably producible — 315 requirements across 24
documents, mechanically extracted and verified — and with no rule in the family governing such a
rendering. **A family that specifies how derived representations behave, and then derives one of
itself under no rule, has placed its own derivation outside the standard it is asserting.**

**This does not reopen `draft-2`.** The freeze holds: `draft-2`'s text is closed to change in
response to the realization, and it has not changed. A revision is how this family moves (`4e` §9),
and it moves by supersession rather than by amendment — which is the same rule it applies to
everything else.

### Change 1 — a projection of this family is governed by the Projection Standard

**Document:** `0z` Document Set. **Section:** §5.2, added.

`0z` §1 already applies the family to itself twice: *"Part VII applies to all of the above, and to
itself,"* and Supersession *"governs how any governed thing is replaced — including the documents of
this family."* **Nothing subjected a derivation from these documents to `4b`.**

The consequence was reachable: a machine-readable index of the requirements is a projection in every
substantive sense — derived, lossy, deterministic, produced for a declared use — and **PJ-3 requires
every projection to be governed by a projection contract.** The family would have shipped a
projection of itself that its own PJ-3 refuses.

**What changes.** §5.2 states that a machine-readable rendering of this family is a projection in the
Projection Standard's sense and is governed by it: the documents are the source and govern where the
two disagree (PJ-7); a contract is required stating source, selection and derivation (PJ-3); the
projection is regenerable and never edited (PJ-9, PJ-8); and carrying less than the whole is faithful
where the contract says so (`4b` §4.1). A projection carries no authority of its own (PJ-11).

**What it does not require.** That any such projection exist. Where one does, it is governed as
above.

**What it invalidates.** No conformance claim — none has been discharged against `draft-2` or
`draft-3`. No normative requirement of any other document is added, relaxed or removed. The
requirement identifiers, their text and their references are untouched, so **a projection of
`draft-2` remains a projection of `draft-2`**: this revision governs how such a thing is made, and
changes nothing it would carry.

**The contract itself is not part of the family.** It is declared in
`projections/requirement_projection_contract.md`, outside the family, because a contract governing a
derivation from the family is not a document of it (`0z` §2).

---

### Change 2 — clause 4 bounds the result in both directions

**Document:** `1b` Semantic Model. **Invariant:** SM-7a added. **Section:** §8.

§8 clause 4 defined a governed transition as one where *"the resulting state is what that
determination permits, **and nothing more**."* The upper bound was explicit and the lower bound was
left to reading.

**The asymmetry is visible elsewhere in the family.** That a *refused* proposal must not partly
proceed is stated three times — SM-7, `2f` EN-10, and `2f` §7's *"no reduced form, no best-effort."*
That an *admitted* transition must not come to rest partly applied was stated nowhere, and was not
delegated either: `6b` §8.3's list of what a distributed environment profile may legitimately require
covers replication, reachability, staleness, snapshot agreement and tenant isolation, and does not
reach the durability of an applied transition.

**Occasioned by the family's own scope claim, not by the realization.** In a single-process
realization over one in-memory store, an admitted transition either completes or the process is gone;
partial application is unreachable. The family claims placement-neutrality, and in any placement with
a network write or a crash between two effects, partial application is the routine failure — and the
one distributed condition `6b` §8's table does not answer, being neither *unable to determine* nor
*determined and refused*, but determined, admitted, and incompletely applied.

**What changes.** §8 states that clause 4 bounds the result in both directions, and that a
realization able to apply a transition partly MUST determine what state results — by preventing the
partial application, by completing it, or by reducing it to a state some determination permits.
SM-7a carries it. **Which of the three, and by what mechanism — transactions, journalling,
compensation, idempotent replay — is not specified.**

**Blast radius, determined rather than discovered** (SU-9). `6b` §8.1's table argues that
distribution's characteristic failures already have determinations, and listed four. **Partial
application is the fifth and is the canonical distributed failure**; it now has a determination, so
the table gains a row citing SM-7a. That is the whole reach: `2f` §7 and `1c` AI-8 cite SM-7, which
is unchanged and remains about refusal, and `1c` requires no new invariant — SM-5a set the precedent
in `draft-2` that a sub-invariant needs no architectural counterpart.

**What it invalidates.** No conformance claim; none has been discharged against `draft-2` or
`draft-3`. SM-7 is unchanged and remains about refusal. **The realization needs no change**: it
cannot apply a transition partly, so it satisfies SM-7a by construction — which is exactly why the
gap was invisible.

### Change 3 — a closure is established for the state the transition applies to

**Document:** `1b` Semantic Model. **Invariant:** SM-7b added. **Section:** §8.

§8 clause 1 requires that *"a closure `C` was established for `(S, π)`"* — a determination is over a
**specific** state. It follows that a determination made against one state and applied to another
satisfies clause 1 for neither, and that where two proposals are determined against the same state
and both applied, at most one is a governed transition.

**The family already covered this, by derivation.** The change states it, for the same reason `6b` §8
exists: the answer is in the family, and stating it saves every implementer the same rediscovery. It
is the derivation a sequential realization never has to make, and the first one any concurrent
placement forces — arriving as a question about governance rather than about locking.

**What changes.** §8 states the binding and its consequence for two concurrent determinations. SM-7b
carries it.

**What it invalidates.** Nothing. No requirement is added in substance — clause 1 already entailed
it. **This is a clarity revision**, and it is recorded as a revision rather than as an editorial note
because `0z` §4 holds that terminology and meaning are load-bearing, and a reader who missed the
entailment was not reading carelessly.

### Change 4 — a profile does not decide an item by deferring it to what claims it

**Document:** `6a` Normative Platform Profile. **Sections:** §7, §12, §13.

**Occasioned by** an independent author, given the family and nothing else, who filled three of §7's
boxes with "the system declares its kind vocabulary," "its contracts declare their outcomes," "the
system declares its namespaces" — and believed the items decided. Each restates KV-1, CP-2 and ID-1.
Under such a profile two systems agreeing on nothing both conform.

**Nothing in `6a` forbade it.** §7's sentence — *"A profile that leaves one undecided yields systems
that cannot be checked on it"* — is descriptive, and NP-8 required that an item be decided without
saying whose decision it must be. The gap is §6's, arriving by a different door: the party the
profile constrains becomes the party that fixes the constraint, while NP-7 is untouched because the
profile's text is external.

**What changes.** §7 adds *"A decision MUST be the profile's own"* and what re-delegation looks like;
NP-12 carries it; §13 says *decides what its claims require rather than re-deferring it*.

**What it invalidates.** Any profile whose §7 decisions restate a family requirement. Nothing else —
no system's conformance to the family turns on this, only a profile's own conformance.

### Change 5 — the subject of a read is named

**Document:** `5b` Governed Inspection. **Sections:** §1, §3.1, §11, IN-12.

**Occasioned by** the same author, who needed a term for whom a read surface is open to, found none,
and invented "governed party" — a term the family does not contain.

`5b` used **caller** in a normative invariant (IN-8, *"MUST NOT delegate its derivation to the
caller"*) and in §8's heading without introducing it, and **party** at §1, §3.1 and §11 for what may
or may not be the same thing. §11 — *"does not establish that a given party may reach it"* — is the
sentence a profile deciding read-surface openness must act on, and its subject was unglossed. `3e`
introduces **attesting party**, not *party*.

**What changes.** §1 introduces **caller** and defines it as the party that issues a read operation.
§3.1 and §11 use it. IN-12 names it: governance applicable to the read *and to its caller*.

**What it invalidates.** Nothing. No obligation moves; the subject an existing obligation already had
is now nameable. A profile deciding read-surface openness now has a term to decide it over.

### Change 6 — a system instance is bounded by the snapshot it accepted

**Document:** `7a` Conformance Model. **Section:** §3.1.

**Occasioned by** the same author's profile, which parameterized evidence retention over "the
lifetime of the system instance." §3.1 defined a system instance — *"a governed system, composed
under a named profile, running"* — and said nothing about when one begins or ends. An obligation
anchored to an unbounded period cannot be breached, so the profile's retention decision was
undecidable while appearing decided.

**What changes.** §3.1 states the bound: acceptance (RT-3) to the next acceptance or to stopping. Two
snapshots are two instances; idleness does not end one. A first drafting had an instance end when the
system *"ceases to execute"* — which ends an instance between every two workflow runs and would have
made the retention period nearly nothing. Acceptance is the right boundary because it is the event
the family already governs.

**What it invalidates.** No claim already discharged — every such claim was about a period the
claimant named. It fixes what a profile may anchor to.

### Change 7 — four consequences of Changes 4–6, and one correction to Change 5

**Documents:** `5b` §1, IN-12; `6a` §5, §7; `7a` §3.1.

**Occasioned by** a review of the family by the same independent author, after Changes 4–6. Ten
observations were offered; five are carried, five are not, and the reasons for both are worth
recording because the pattern in what was declined is itself a finding about how the family is read.

**Correction to Change 5.** IN-12 was amended to read *"the governance applicable to it and to its
caller."* That was wrong and is reverted. Governance applies to governed subjects (`2e`); a caller is
not one, and the amendment asserted a relation between governance and an actor that this family does
not have. §1's gloss now says so directly — **a caller is identified, not governed** — which is what
the amendment was reaching for and states it where it belongs. The invariant returns to its
`draft-2` wording.

**Carried:**

- **`5b` §1.** The gloss states that being a caller confers nothing and requires nothing, and that
  there is no governed and ungoverned kind of caller. This is what forecloses the invented term the
  trial produced; the bare definition alone did not.
- **`6a` §7.** *"The test for whether an item is decided is whether two systems that disagree on it
  could both claim the profile."* NP-12 names the re-delegation failure; this states the criterion
  that catches its variants.
- **`6a` §7.** A profile MUST NOT support a claim no system under it could discharge. Which class
  establishes an obligation is the evaluator's question; whether a system under the profile can be
  subjected to that class is the profile's, and nothing said so.
- **`6a` §5.** An additional obligation must add something. One that restates a family requirement or
  the profile's own selection cannot be breached by anything that has not already breached what it
  restates, and under §9 every later adjustment to it costs a profile identity.
- **`7a` §3.1.** Which subject classes a system contains is a fact about the system, established at
  claim time. A profile enumerating classes states a floor. This settles what the trial got wrong in
  both directions — the profile under-enumerated, and the evaluation treated the enumeration as
  though the profile should have been exhaustive.

**Not carried, and why.** Five observations asked for guidance, examples, decision heuristics, or a
restatement of cited invariants inside the citing text. **The annex is where guidance lives** (`8a`),
and none of the five was addressed to it. Two further reasons apply:

- **Restating an invariant where it is cited** creates two statements of one requirement, which drift.
  The consolidated reference the observation asks for already exists and is governed — Change 1 of
  this revision put the family's requirement projection under `4b`.
- **Retention periods, sufficiency criteria, and the platform/domain line** are decisions the family
  delegates on purpose. Supplying "guidance" on them is the family deciding them quietly, which is
  what `6a` §1 says the deferral exists to prevent.

**What it invalidates.** IN-12 as published in Change 5 — a wording that stood for one revision cycle
and against which nothing was claimed. Nothing else.

### Change 8 — the `4d` re-review, and one invariant that had no document behind it

**Document:** `4d` Governed Transformation. **Sections:** §4, §13, §14, TR-20, TR-23.

**Occasioned by** the finding left outstanding against `draft-2`: *"`4d` remains the document with the
most vocabulary of its own and the largest invariant set, and a clause-by-clause re-review against
`8a` §4.7 is still what would settle it."* This is that review. It is carried in `draft-3` rather
than deferred again, because the changes it produced are small and a finding recorded as outstanding
across two revisions is a finding nobody intends to close.

**The test applied** is `8a` §4.7: a place where the document describes a mechanism while believing
it describes a meaning, such that an alternative model satisfying every semantic requirement is
nonetheless excluded.

**TR-23 had no document behind it.** *"A refusal the business declares MUST be discharged by the
design, the discharge MUST be stated, and it MUST be checked against what it does"* — the invariant
cited §14, and §14 said nothing of the kind. The requirement appeared nowhere in the document's body,
in any revision. **This is worse than over-specification: an invariant that derives from no stated
text is a requirement the family asserts without having said it**, and `0z` §3's derivation rule has
nothing to check it against. It was also being conformed to — the realization map records TR-23 as
*Demonstrated*, against text that did not exist.

The requirement is right and is kept; what was missing was its derivation. §14 now states it, as
§9.2's fabrication check applied to refusals: a design that declares a discharge has stated
something, and whether the artifacts it fixes actually refuse is the different question that is the
discharge. TR-23's wording is unchanged.

**Two over-specifications, both linearity where dependency was meant:**

- **§4** said a transformation is *"an ordered sequence of phases"* producing *"one dossier document"*
  each, while §1 of the same document says *"Nothing here requires a particular pipeline, tooling, or
  number of steps."* A transformation whose phases form a dependency graph with independent branches
  satisfies every requirement §4 goes on to state and was excluded by its opening sentence. §4 now
  says the order is a dependency order and not necessarily a line, and defines **dossier** as what
  the phases emit together with what was determined at each, rather than as one document per phase.
- **TR-20** required the realization order be *total*. Coverage and dependency-respect are what the
  section argues for; totality additionally orders artifacts that depend on each other not at all,
  which excludes a realizer that works independent artifacts concurrently and drops nothing. TR-20
  now requires gapless coverage and dependency-respect, and says the rest is unspecified.

**Considered and not carried.** TR-2 and TR-4 presume that governed content is grouped into
per-phase register documents, which excludes a model recording each decision as a separately
identified declaration. The requirement underneath — that governed content be field-addressable and
that a finding name a location — does not need the grouping. It is not carried because `draft-2`
Change 6 settled a finding's location as register, entry and field one revision ago, and reopening
it on review rather than on a claim would be revising a decision that has not yet been tested.
**Recorded as outstanding against `draft-3`.**

**What it invalidates.** Nothing discharged. TR-23's subject is unchanged, so no claim against it
moves; what changes is that the invariant can now be derived. A realization whose phases are a line
and whose realization order is total conforms exactly as before — both changes widen what conforms,
which is permitted of the family and would not have been permitted of a profile (`6a` §3.1).

### Change 9 — the document map states two invariant ranges the documents do not have

**Document:** `0z` Document Set. **Section:** §2.

**Occasioned by** a reader's question about `1a`'s scope, which prompted a mechanical check of every
invariant range in the map against the document it describes. Two disagreed:

- **`6a`** was listed as `NP-1 … NP-11`. Change 4 of this revision added NP-12 and did not update the
  map — a defect introduced by this revision and closed within it.
- **`4e` Supersession** was listed as carrying no invariants. It carries **SU-1 … SU-10**, and has
  since `draft-1`; `draft-2`'s own change record cites SU-5, SU-9 and SU-10 by identity. The map has
  understated the document for two revisions.

The second is the one worth noting. §2 opens by saying a file identifier is an address and that
**invariant identifiers carry their document's prefix** — so a map that omits a document's
invariants entirely says that document imposes nothing, about the document that governs how
everything in this family is replaced.

**What changes.** Two rows of §2. No normative text.

**What it invalidates.** Nothing. Every SU invariant was in force throughout; the map was wrong about
what the family contains, not the family.

### Change 10 — the Conceptual Model's requirements become citable

**Documents:** `1a` §1, §13 (new), §14; `0z` §2.

**Occasioned by** a reader noticing that `1a` carries no invariant identifiers, and asking whether
that made it non-normative. It did not — and that was the problem.

**`1a` stated requirements nothing could name.** §12 carries six MUST/MUST NOT rules over documents
of this family — use the terms as defined, do not redefine, do not overlap, preserve every
*distinguish from*, a profile alters no meaning, altering a definition is a revision — and §13 stated
a conformance test. None of it carried an identifier. **A finding that a document redefined a term
had nothing to cite**, in a family where every other requirement is named and where `0z` §2 asserts
that invariant identifiers carry their document's prefix.

**The layering does not excuse it.** `0z` §3 places `1a` at the concept layer, where requirements are
expected downstream. But §12's rules are not concept-layer content — they are requirements on
documents, and §14 is a conformance clause. Nothing in the derivation rule reaches them.

**What changes.** §13 states **CM-1 … CM-7**, derived from §3 and §12 with no wording change to
either and no requirement that was not already stated. The former §13 becomes §14; nothing in the
family referenced it. §1 names the invariants alongside the usage rules. `0z` §2's `1a` row now reads
`CM-1 … CM-7` rather than `—`.

**What it invalidates.** Nothing. Every rule was in force and unchanged; what changes is that a
document violating one can now be told which one.

**Recorded as outstanding.** `7a` §3 names **specification** as a conformance subject class evaluated
by the Conceptual Model and the Semantic Model, and `7b` — the document that specifies demonstrations
— **does not mention that subject class at all.** Half the class was already citable (`1b` carries
SM-1 … SM-12) and is now wholly so, but no demonstration is specified for any of it. That is a new
section in a normative document rather than a bookkeeping fix, and it is not carried here.

**Also outstanding, smaller.** `0z` itself states three MUSTs — including the derivation rule — and
carries no invariants. Whether a document governing the family's own construction should carry them
is a different question from whether `1a` should, and is left open.

### Change 11 — inspection is reached independently of the interaction boundary

**Documents:** `5b` Governed Inspection (§2.1 added, IN-15, IN-16); `5a` Governed Interaction
Boundary (§14); `6a` Normative Platform Profile (§7).

**Occasioned by** a second independent author, given the family and nothing else, writing a profile
whose scope excluded the interaction boundary and required inspection. They produced a universally
open read surface for a system nothing outside it can reach, and did not notice — because nothing in
the family says whether inspection is reached through the interaction boundary or independently of
it.

`5b` §2 already said inspection is *"a governed boundary of the same standing as the interaction
boundary,"* which settles standing and not reachability. `5a` §14 disclaims *"any external protocol,
or how one is spoken"* for its own boundary and says nothing about the other. A profile selecting no
interaction boundary therefore could not tell whether it had removed one boundary or two.

**What changes.** `5b` §2.1 states that the two boundaries are reached independently, that a read
operation is not an operation identity at the interaction boundary, that selecting no interaction
boundary leaves the read surface required, and that a profile making that selection MUST state how
its read surface is reached. IN-15 and IN-16 carry it. `5a` §14 records the same from its side. `6a`
§7 adds the deferred item and a third emphasis bullet on the reachability of what a selection leaves
standing.

**What it invalidates.** Any profile that selects no interaction boundary and does not say how its
read surface is reached. No system's family conformance turns on it; a realization that already
reaches inspection independently is unaffected.

### Change 12 — read-surface openness is a policy, and does not dispense with the determination

**Documents:** `5b` Governed Inspection (§11); `6a` Normative Platform Profile (§7).

**Occasioned by** the same author, who wrote that *"any caller may issue any declared read
operation"* and then hedged it — *"subject only to the family refusal rules"* — because `6a` §7
delegates read-surface openness to the profile while `5b` §11 makes every read a determination under
governance. The hedge was the author reconciling two documents the family had not reconciled.

**What changes.** `5b` §11 adds the split: the profile fixes the **policy** — which callers are
admitted to which declared read operations, up to and including all callers to all of them — and the
system's governance still makes the **determination**, per read, with evidence. A profile MAY fix
the first completely and MUST NOT dispense with the second; reading the open policy as permission to
answer without determining is widening that appeared to parameterize (NP-11). `6a` §7's read-openness
bullet carries the same distinction.

**What it invalidates.** No obligation moves. A profile that declared an open read surface is not
thereby non-conforming; a realization that took an open policy as licence to answer undetermined
reads was already in breach of IN-12 and is now visibly so.

### Change 13 — a closed vocabulary states what each kind may omit

**Documents:** `2d` Kind Vocabulary (§5.1 added, KV-10, §11); `6a` Normative Platform Profile (§13).

**Occasioned by** the same author, whose profile closed a kind vocabulary at ten kinds and gave, for
each, its name, its primary category, and what it declares — and not whether a governance assertion
is required for its admission. `6a` §13 already names this exact failure: *"A profile that admits a
small kind vocabulary while permitting one of those kinds to omit a governance assertion has narrowed
in the visible dimension and widened in the one that matters."*

**It was named and not checkable.** MB-10 requires each kind to declare the disposition; nothing
required a vocabulary to state it, so a vocabulary could be complete by KV-1 … KV-9 and silent on the
dimension `6a` §13 warns about. A warning in a conformance section is not an invariant.

**What changes.** `2d` §5.1 states that closure answers *which kinds may be used* and must also
answer *what each may omit*; KV-10 requires the vocabulary to state each admitted kind's
governance-assertion disposition; §11 adds it to what a conforming vocabulary carries. `6a` §13
points at KV-10 as the checkable form of the failure it describes.

**What it invalidates.** Any declared vocabulary that does not state the disposition — a declaration
defect, repaired by declaring it. No kind's semantics change and no artifact's admission changes.

### Change 14 — the line between a governed artifact and a declaration element

**Documents:** `2c` Machine Block (§7.1 added, MB-15); `4d` Governed Transformation (§5).

**Occasioned by** the same author, who closed a kind vocabulary admitting no kind for a
transformation rule, a register, a snapshot, or a genesis proposal, while supporting claims over
`TR-*`, `SN-*` and `GC-*` — and had no way to tell whether that was a hole. KV-9 requires no
particular kind; `4d` §1 says artifact kinds *"are free to vary"*; `4d` §5 calls a rule *"declared
data."* **Nothing said what makes something an artifact requiring a kind rather than a declaration
element inside one.**

The consequence runs both ways: a system may fragment one artifact into many kinds, or hide many
artifacts inside one, and the family gave no test to distinguish them.

**What changes.** `2c` §7.1 gives the test — **admission, not size or structure**: an element is an
artifact when it is determined in its own right, identified independently, referenced from outside a
container, and separately supersedable; anything else is a declaration element, governed by the
artifact carrying it and requiring no kind. MB-15 carries it. `4d` §5 applies it to registers, rules
and check kinds, and separates **check kind** from artifact kind explicitly, the two never appearing
in one registry.

**What it invalidates.** Any vocabulary admitting kinds for declaration elements, and any system
carrying separately-admitted elements without kinds. Both are declaration defects. The test is new
text for a question the family answered by silence, so a realization may find itself on either side
of it.

### Change 15 — an outcome named for refusal is not a refusal

**Documents:** `3a` Execution Model (§4.4 added, EX-16); `2f` Enforcement & Refusal (§6.1, EN-14);
`3d` Capability Standard (§3.2).

**Occasioned by** the same author, whose profile selected `completed | constrained | refused |
failed` as the outcome vocabulary for every capability contract. Outcomes are the only thing
traversal routes on (EX-2); EN-8 requires a refusal to establish **that nothing proceeded**. An
outcome named `refused` is routed on, and routing is proceeding.

**The family reserved nothing and said nothing.** Outcome names are a profile's or a contract's to
choose, and both `2f` and `3a` used *refusal* in their own senses without stating that the word does
not carry the semantics between them. A checking party reading evidence of a routed `refused`
outcome could not tell whether a determination had occurred.

**What changes.** `3a` §4.4 separates the two in a table and states that no evidence of the one is
evidence of the other; EX-16 carries it. `2f` §6.1 adds the converse — nothing becomes a refusal by
being called one, and a refusal MUST NOT be delivered as a value that is acted on — carried by EN-14.
`3d` §3.2 points a contract author at the distinction.

**What it invalidates.** No outcome name is forbidden and no vocabulary must change. What is
invalidated is any realization or evidence record in which a routed outcome stood in for a
determination.

### Change 16 — genesis is in scope wherever a first snapshot is

**Documents:** `6a` Normative Platform Profile (§7); `7b` Conformance Test Specification (§9).

**Occasioned by** the same author, whose profile scoped itself to *"one accepted snapshot"* — a
system constituted rather than inherited — and whose discharge table cited `7b` §8 and no `SM-*`
subject at all. Genesis was in scope and unaddressed.

`6a` §1 already says the claimed profile is *"the only thing constraining a system that has no
predecessor,"* and `7b` §9 already specifies the two genesis demonstrations. **Neither said that a
profile constituting systems thereby supports a claim about genesis**, so §7's deferral list — the
list a profile author works through — never raised it.

**What changes.** `6a` §7 adds the deferred item, and states that such a profile supports a genesis
claim whether it says so or not. `7b` §9 records the same from its side, and bounds it: what the
profile decides is **what its fixtures are**, not which discharge class applies, which remains the
evaluator's question (CF-8).

**What it invalidates.** Any profile constituting systems and supporting no genesis claim. It does
not invalidate a genesis that occurred — the demonstrations were already specified and already
required.

### Change 17 — bookkeeping for Changes 11–16

**Document:** `0z` Document Set. **Section:** §2.

The invariant ranges of `2c`, `2d`, `2f`, `3a` and `5b` are extended to MB-15, KV-10, EN-14, EX-16
and IN-16. No invariant was renumbered and none was removed; every identifier existing before this
revision means what it meant.

### Change 18 — a snapshot's whole-integrity value does not cover itself

**Document:** `3b` Snapshot. **Section:** §6, SN-14.

**Occasioned by** an external reviewer. §6 requires the self-description to carry integrity *"over
each constituent, and over the whole,"* and requires the self-description to be a constituent. **The
value over the whole therefore covers itself**, and a value computed over a set containing that value
has no determinate result. Two realizations resolving the circularity differently — excluding the
field, zeroing it, hashing a placeholder — produce incompatible snapshots that both appear to
conform.

**What changes.** §6 requires the covered set to be canonically determined, declared, and not to
contain the value; SN-14 carries it. The mechanism stays unspecified (§10): which function, which
serialization, which ordering are not this family's, and the reviewer's recommendation to fix a
canonical scheme is not taken.

**What it invalidates.** Any snapshot that does not declare what its integrity value covers. Existing
values are unaffected where the exclusion was already implicit and can be stated.

### Change 19 — evidence identifies what it is about

**Document:** `3e` Evidence, Attestation & Provenance. **Sections:** §3.1, §9, EV-17.

**Occasioned by** an external reviewer, who observed that `1b` §13 checks conformance by re-evaluating
the closure and rules recorded in the evidence, while §9 makes the reference from evidence to
snapshot identity permissive — *"each may reference the others."* **A record that does not name its
snapshot re-evaluates clean against itself and establishes nothing about any system.** A producer
supplying a permissive closure and a matching determination would pass, which is precisely the trust
EV-16 says a checking party must not have to extend.

**What changes.** §3.1 requires evidence to identify the sealed representation it was produced under
and the subject of the determination; §9 makes that one reference required; EV-17 carries it.

**The reviewer's remedy is not taken.** Mandating cryptographic binding, freshness, and key
revocation would put a mechanism in a family that defers all of them (§12) and would decide, for
every profile, what `6a` §7 gives each profile to decide. **That the record states what it is about
is semantics; how the statement is made unforgeable is not.**

**What it invalidates.** Any evidence record that does not name its snapshot and subject.

### Change 20 — evaluating a sealed obligation is not making a determination

**Document:** `3c` Runtime. **Section:** §7.1 added, RT-13.

**Occasioned by** both external reviewers independently — the only finding they both reached. §2
excludes the runtime from making *"no governing determination"*; §7 requires it to refuse on *"an
obligation, applicable and evaluated, that is not satisfied."* **The document never says who
evaluated it.** A realization could claim an incorrect refusal was outside the runtime's governing
role, and nothing in the text settles it.

**What changes.** §7.1 separates **determination** — establishing what governs, before sealing, by
governance (2e §10.1) — from **application** — evaluating a sealed assertion against sealed
declarations, at execution, by the runtime. It gives the checkable form: a runtime that *could have
refused differently* has made a determination; one that could only have refused as it did has applied
one. RT-13 carries it.

**What it invalidates.** Nothing. Both acts were already required and already bounded by RT-6 and
SN-10; neither moves. What was missing was the sentence saying they are two acts.

### Change 21 — EX-5 forbids admitting an undeclared result, not producing one

**Document:** `3a` Execution Model. **Sections:** §4.1, EX-5.

**Occasioned by** an external reviewer. EX-5 read *"An outcome a contract does not declare MUST NOT
occur"* while §4.1 states that a realization **can** produce one, *"which is why refusal exists."*
The invariant as written was an obligation on the physical world that nothing could refuse, and an
obligation nothing can refuse is not in force (EN-1).

**What changes.** EX-5 forbids **routing on, admitting, or recording** an undeclared result and
requires refusal. §4.1 adds the sentence the distinction needed: **detecting an undeclared result is
required; tolerating one is what is prohibited** — a realization that could not detect it could not
refuse it either.

**What it invalidates.** No realization's behavior; the intended obligation is unchanged. It
invalidates any conformance argument that read EX-5 as unsatisfiable, and any demonstration that
tried to establish non-production.

### Change 22 — what an amendment may change

**Document:** `4e` Supersession. **Section:** §7, SU-11.

**Occasioned by** both external reviewers. §7 calls amendment *"a whole redeclaration"* and *"the
ordinary case,"* and separately states that a change of declared semantics is a new identity (ID-5).
The two are consistent and were never joined, so the section read as licensing in-place semantic
change.

**What changes.** §7 states the consequence directly: amendment is available for everything that is
not declared semantics, and **an in-place change to declared semantics is not an amendment** but a new
identity written over an old one. It adds the test — not how much text moved: a whole redeclaration
leaving semantics identical is an amendment; a one-field change that alters meaning is not. SU-11
carries it.

**What it invalidates.** Any artifact amended in place through a semantic change, and every reference
admitted against its former meaning.

### Change 23 — the caller may compute; it may not substitute

**Document:** `5b` Governed Inspection. **Section:** §8.

**Occasioned by** an external reviewer, who read §8's *"A caller that computes relationships over what
inspection returned has become a second inspection engine"* and observed that, taken as written, it
forbids a report, a dashboard, or any downstream analysis of read results. **It also contradicts §12**,
which says observability is a *use* of the read surface and not a second kind of inspection.

**What changes.** §8 states the line as **substitution, not computation**: a caller may compute
whatever it likes for its own purposes; it MUST NOT present a client-derived result as the system's
answer, or supply one where a governed answer is required — to a checking party, an evidence record,
another governed system, or a determination. *"The line is not did the client calculate something but
whose answer is this held out to be."* Both consequences are stated, including the one that runs the
other way: a read operation MUST NOT be designed so the answer exists only once a client assembles it
(IN-8).

**What it invalidates.** No obligation moves and IN-8 is unchanged. It invalidates a reading, and the
reading was available.

### Change 24 — the applicable subject classes are read off the system, not asserted by the claimant

**Document:** `7a` Conformance Model. **Section:** §3.1, CF-14.

**Occasioned by** an external reviewer, and it is the conformance-side twin of this revision's Change
4. §3.1 says which classes a system contains is *"a fact about the system, established at claim
time"* — and does not say by whom. In practice the claimant enumerates, and **a claim whose scope the
constrained party sets is defeatable by omission**: leaving a class out is not a smaller claim made
honestly, it is the largest claim available with the failing part excluded, and nothing in the claim
shows it.

**What changes.** §3.1 derives the applicable set from the accepted snapshot's self-description —
already required to be total, with undeclared constituents refused at acceptance (SN-5, SN-8) —
together with the claimed profile. CF-14 carries it. **A class present in the system and absent from
the enumeration was already a defect at acceptance rather than a narrowing of the claim.**

**What it invalidates.** Any system-instance claim whose subject set was asserted rather than derived.

### Change 25 — a prohibition on structural possibility is discharged by absence, not by refusal

**Document:** `7b` Conformance Test Specification. **Sections:** §3, §3.2 added, CD-17.

**Occasioned by** an external reviewer. §3's table defined a negative demonstration as *"the subject
refuses what the obligation forbids"* — but the family's most important prohibitions forbid a
structural possibility rather than requiring a runtime refusal, and **no input elicits one**: the
demonstration that would exhibit a refusal is the demonstration that would exhibit the defect.

`7a` §8 already rules correctly — negative properties are discharged structurally or comparatively and
*"none is discharged by a system having worked"* — so the family was not wrong. **The document that
specifies demonstrations gave no form for half of them**, which is a defect in `7b` whatever `7a`
says.

**What changes.** §3's table splits the negative row into **refusal** and **absence** forms. §3.2
specifies the absence form: a stated search space, totality over it, and the space being the one the
obligation speaks of — *"an obligation about reachable execution paths is not discharged by searching
declared ones."* CD-4 applies unchanged: an absence demonstration must be shown to find the forbidden
thing when a fixture contains one. CD-17 carries it.

**What it invalidates.** Any discharge of a structural prohibition by refusal or by observation.

### Change 26 — a human answer is governed content

**Document:** `4d` Governed Transformation. **Sections:** §9, TR-13, TR-25.

**Occasioned by** an external reviewer. TR-13 — *"Given the same human answers, any worker MUST yield
the same admissible registers"* — is the invariant that makes workers interchangeable, and **"the same
human answers" was never typed.** Over free prose it is undecidable: two answers meaning the same
thing in different words are indistinguishable from two different answers, so the obligation could not
be refused and was not in force (EN-1).

**What changes.** §9 requires a human answer to be recorded as declared register content addressed by
the field of the register the question was opened against — *"an answer given in conversation and not
landed in a register has not been given."* TR-13 names the comparison it is stated over; TR-25 carries
the recording obligation. This is §5's existing line applied where it had not been: **governed content
lives in registers, and a human answer is governed content.**

**What it invalidates.** Any transformation whose human answers live outside its registers, and any
worker-equivalence claim demonstrated over prose.

### Change 27 — naming and revision metadata

**Documents:** `4c` Identity & Addressing, `6a` Normative Platform Profile; `0z` Document Set. Also
`README.md` and the repository rules, which are not family documents.

`4c` §2.4, `4c` §8 and `6a` §4 referred to **"Supersession & Family Evolution"**; `0z` §2 names the
document **"Supersession."** Documents reference one another by name, so a name that is not the name
resolves to nothing. All three now use `0z`'s.

`0z` §2's invariant ranges are extended to SN-14, RT-13, EV-17, SU-11, TR-25, CF-14 and CD-17. No
invariant was renumbered or removed.

`README.md` described the family as `draft-1` and *"not yet published as a numbered revision"* while
`VERSION` carried `draft-3` and this record declared the supersession — three reader-facing statements
of which revision governs, disagreeing. **A family requiring every conformance claim to name a
revision cannot be ambiguous about which one it is.** The README now names `draft-3` and points here.

### Change 28 — the family gains a figure document

**Documents:** `0d` Visual Representation of the Standard, added; `0z` Document Set (§2, §7). Also
the repository rules, which are not a family document.

**Occasioned by** two independently drawn conceptual diagrams of the family, neither of which is
adopted, and both of which were useful for the same reason: **each drew the family as a pipeline**,
and seeing the error drawn made it clear how easily the prose invites it. Both rendered the
interaction boundary as a stage between the snapshot and the determination — which `5a` §3 forbids
in its own heading, *"A boundary, not a stage"* — both placed inspection downstream of evidence as
an assurance activity rather than as a boundary of the same standing (`5b` §2, §2.1), both named
implementation stages the family does not have, and neither drew the profile as anything but one
declaration among several. **The single most load-bearing idea in the family — that the constraint
arrives from outside the system's authority — was absent from both.**

`0z` §1 already says the parts are *"a dependency order, not a pipeline."* Nothing said it of the
subjects, and a reader assembling a mental picture from thirty-one prose documents assembles a
pipeline unless something stops them.

**What changes.** `0d` is added to Part 0 as a non-normative reading aid: seven figures, each
carrying one idea — the seal and the two times it separates; the external profile that keeps
governance from closing on itself; the three paths by which applicability arises and the two refusals
that look alike and mean opposite things; the two boundaries and evidence's one-way flow; the
transformation loop; and where each part sits on the picture. `0z` §2 lists it and §7 points at it.

**It is commentary, not a projection.** `0z` §5.2 governs a *derived* rendering of this family; a
composed figure is not regenerable from the documents alone (PJ-9) and is authored rather than
derived (PJ-8), so it is not one and does not claim to be. The document says so in its own preamble
and states that where a figure and a document disagree, the document governs.

**What it invalidates.** Nothing. `0d` states no requirement, defines no term, and carries no
invariant; the document count in the repository rules moves from 31 to 32.

### Findings considered and not carried

Recorded because a finding declined is worth as much as one taken, and because declining silently
invites it again.

- **A canonical `GoverningRelation(A, S)` object** — raised as the single most important remaining
  issue. **`2e` §10.1 already is it**: it enumerates the conditions, states that direct declaration,
  inheritance and import are *"the only paths by which applicability arises,"* and says the closure
  *"is the result of resolving them, not a prior fact."* The family expresses the relation as an
  establishment procedure over a closed input set rather than as a named object. Naming it would add
  no constraint, and the finding does not identify a determination two implementations could make
  differently.
- **`2b`'s four open ontology questions must be resolved before shipping.** They are in §10, *What
  this ontology does not specify* — the section every document in this family carries — with a stated
  resolution criterion and an explicit warning not to confuse them with the minimality question.
  **Deliberate deferral recorded in the document's own deferral section is the discipline working**,
  not an omission. GO-1 … GO-12 close what conformance depends on.
- **A family-wide identity-vocabulary sweep** — semantic identity, representation identity, address.
  The distinction is stated and normatively carried: `4c` §4 separates all three, MB-3 defines equality
  and identity over the semantic object and integrity over the representation. The finding is about
  consistency of wording across 31 documents, which is a family-wide terminology revision under `0z`
  and is not undertaken as a set of local edits.
- **Cryptographic binding, freshness, and key revocation for evidence** — see Change 19. The defect is
  real and is fixed; the remedy would have decided for every profile what `6a` §7 gives each profile.
- **P1 and P2 editorial findings** across Parts 0, I, II and IV — sourcing an empirical claim in `0a`,
  terminology polish, sharper types for *constrain*, an admission/authorization/permission matrix.
  None identifies a decision two implementations could make differently, and this revision is already
  large.

### What this revision is occasioned by, recorded plainly

**Changes 11–17 come from one independent author's profile, and none from a finding that author
reported. Changes 18–26 come from two external reviewers reading the family directly.** Their questions log declared *"No missing semantic decision was required to write
this profile"* — and the six silences above are the ones they decided over without recognising them
as silences. Changes 4 and 5 of this revision came from the first such author, who did report theirs.

The instrument therefore reports two different things, and the second is worth stating: **a
zero-finding log is not evidence that the family is complete.** It is evidence that the family does
not signal where it is silent on purpose. What found these was reviewing the profile against the
documents, not reading the log.

**The two instruments find different defects, and neither substitutes for the other.** The authoring
trial finds what the family fails to *delegate clearly* — silences a profile author must fill and
cannot see. Direct review finds what the family fails to *say consistently* — two documents that are
each defensible and do not join. Changes 11–17 are all of the first kind; Changes 18–26 are all of the
second, and not one of them was reachable from a profile. Of the two reviewers' findings, roughly a
third were carried: the rest were either already answered in a section the reviewer had not read
against, or were remedies that would have put a mechanism where this family keeps a decision.

**Outstanding, not carried.** Whether `6a` should tell a profile author what to notice is missing —
a "what a profile must be able to tell it has not decided" note — is a section in a normative
document rather than a repair to one, and is left open.

## `draft-3` is frozen

Twenty-eight changes are declared above. **This revision is closed to further change.**

**What freezing means.** `draft-2` was frozen against one thing — the reference realization — because
that was the only source of findings it had faced. This revision faced two more, and closes against
all three. `0z` §3 forbids amending a document to match what was built; §5.1 holds that experience
*occasions* a revision and does not decide one. Findings arriving after this point are occasions for
its successor — declared as `v0` — and they are not amendments to this.

**What was established before freezing.** `draft-2`'s freeze named the test it had not faced: *"A
defect found by someone who did not build the realization. That is the next test and the only one
this revision has not faced."* This revision faced it, twice over, by two instruments that find
different things:

| Instrument | What it tests | What it found |
|---|---|---|
| **the authoring trial** | can a competent reader decide the family's delegated questions from the standard alone? | Changes 4–5 (first author), Changes 11–16 (second) — silences a profile author must fill and cannot see |
| **external review** | do two documents that are each defensible actually join? | Changes 18–26 — inconsistencies unreachable from any profile |
| **internal examination** | does the family hold against itself? | Changes 1–3, 7–10, 17, 27–28 |

Both authoring trials produced a profile that would survive NP-1 … NP-12 review. **Neither author had
to invent a facility the family has no home for**, and neither was blocked. The family now carries
338 invariants across 32 documents, no undefined cross-reference, and no invariant range in `0z` that
the documents do not have.

**The result that matters most is not a change.** The second author's questions log declared *"No
missing semantic decision was required to write this profile"* — and six of this revision's changes
come from silences that author decided over without recognising them as silences. **A zero-finding log
is not evidence that the family is complete.** What found those was reviewing the profile against the
documents, not reading the log, and the same is true of every finding an instrument does not know it
has made.

**What would reopen it.** Three tests this revision has not faced, in the order they are worth doing:

- **A claim attempt.** A system built independently of any profile in hand, attempting to claim one.
  Passing and failing are both informative; what is not informative is a profile written so that some
  particular system passes.
- **A second independent realization.** RT-12 and CF-* are stated over substitutability, and one
  realization cannot establish it. Every comparative discharge class in `7a` §7.3 is currently
  unexercised.
- **An authoring trial for `6b` or `6c`.** Both instruments so far have been pointed at `6a`. An
  execution-environment or domain profile written from the standard alone would test two documents
  that no independent reader has yet been made to use.

**What is not frozen.** The reference realization, whose findings are its own (`doc/realization_map.md`),
and `0d`, which states no requirement and may be redrawn without a revision — a figure that misleads is
corrected, not superseded.

### Outstanding against `draft-3`

Carried forward because declining a finding silently invites it again.

- **Whether `6a` should tell a profile author what to notice is missing.** Both authoring trials
  produced logs that under-reported: the family gives a profile author the list of what to decide
  (§7) and no way to tell a deliberate silence from an omission. A "what a profile must be able to
  tell it has not decided" section is a new normative section, not a repair to one.
- **`7b` specifies no demonstration for the specification subject class.** Carried forward from
  Change 10 unchanged. `7a` §3 names it; `7b` does not mention it.
- **`0z` states three MUSTs and carries no invariants.** Whether a document governing the family's own
  construction should carry them is unresolved.
- **`4d` remains the document with the most vocabulary of its own and the largest invariant set.**
  Narrowed twice — by Change 8's re-review and by Change 26 — and not closed. A clause-by-clause
  re-review against `8a` §4.7 is still what would settle it.

---

## `draft-2` supersedes `draft-1`

**Predecessor:** `draft-1` — 31 documents, marked and unedited.
**Occasioned by:** the realization map (`doc/realization_map.md`), which examined all twenty-five
normative documents against one realization and returned three findings against the documents. Two
were ruled to change a document; the rulings are in the workspace ruling record. Per `0z` §5.1,
experience from a realization may occasion a revision and may not decide one — each change below
rests on a ruling, not on what the realization does.

### Change 1 — SU-5 admits the declaration SU-3 requires

**Document:** `4e` Supersession. **Invariant:** SU-5. **Section:** §4.

SU-3 requires the successor to declare the supersession relation, which necessarily names the
predecessor's identity. SU-5 forbade anything in the governed system referencing the predecessor, and
§4 foreclosed the obvious narrowing — *"the requirement is strict: no reference, not no executable
reference."* Read literally the two could not both be satisfied, and **no supersession conformed.**

**What changes.** SU-5 now reads "nothing … MUST reference `Y` other than the supersession
declaration SU-3 requires". §4 gains a paragraph distinguishing a **dependency** on the predecessor
from the **record** of its retirement, and states that the exclusion is not a weakening: every other
mention remains forbidden, including a prose one.

**What it invalidates.** No conformance claim — none has been discharged against `draft-1`. No other
invariant cites SU-5. No document referred to SU-5's previous scope.

**Why this and not the alternative.** SU-3 could instead have been changed so the relation is
declared without naming the predecessor, but a relation between two identities cannot be declared
without naming both. SU-5 was the clause that had overshot.

### Change 2 — TR-17 states its requirement rather than a mechanism

**Document:** `4d` Governed Transformation. **Invariant:** TR-17. **Sections:** §13, §14, §16.

TR-17 required sufficiency "measured … as the proportion of required facts the design states" and
refusal "below the declared threshold" — a computation and a scalar. §13 states the requirement one
line later: *"a generator that supplies a fact the design omits is a second, ungoverned design
authority."* A realization determining **per-artifact determinability**, refusing on the first
artifact its design does not fix, satisfies that requirement more directly and did not conform.

Under `8a` §4.7 an alternative model that satisfies the semantics and is nonetheless excluded is
evidence of an over-specified document. This was one.

**It was also an inconsistency inside `4d`.** §1 already disclaims exactly what §13 specified: *"It
specifies a semantic contract, not a realization. Phase names, register shapes, rule identifiers, and
artifact kinds are free to vary. Nothing here requires a particular pipeline, tooling, or number of
steps."* §13's proportion and threshold were a mechanism in a document that says it names none. The
change brings §13 into line with §1 rather than imposing an outside view on either.

**What changes.** TR-17 now requires that sufficiency be **determined** before realization and that
realization refuse a design that does not fix every fact the realization needs, with the manner of
determination unconstrained. §13 names a proportion-and-threshold and a per-artifact test as
discharging it equally.

**Blast radius, determined rather than discovered** (SU-9): three references to the removed mechanism
were re-pointed — `4d` §14's "sufficiency at its threshold", `4d` §16's deferral of "the sufficiency
threshold", and **`6a` §7's deferred-items table**, where a profile is required to decide it (NP-8).
The deferral is unchanged in substance: a profile still decides the sufficiency criterion, and no
longer presumes it is a scalar.

**What it invalidates.** No conformance claim. TR-18 — a realized artifact is a function of the
design alone — is unaffected and carries the weight this clause was sharing.

### Change 3 — SU-9's blast radius is bounded by the composition

**Document:** `4e` Supersession. **Invariant:** SU-9. **Sections:** §5, §8, §10, §11.

SU-9 required a supersession to determine its blast radius and did not say over what. A realization
superseded a catalog boundary and the workflow that admits it, determined the radius over the
composition as SU-6 requires, and retained both predecessors as SU-2 and SU-8 require. A caller
outside the composition went on naming a predecessor and being refused by it — for as long as the
supersession existed. **Nothing was wrong with either the supersession or the refusal**, and nothing
in the document said so.

**What changes.** §8 states that a blast radius is determined over the composition, and that
superseding does not redirect a caller — the caller moves. §5 qualifies its reachability table as a
statement about the composition's own closure: a party outside it that names a superseded identity
directly is informed, not prevented. SU-9 is restated to say both. §10 adds informing external
parties to what this document does not specify.

**What it invalidates.** No conformance claim — none has been discharged against `draft-2`. SU-2,
SU-7 and SU-8 are unaffected. SU-5 is untouched: this is not about references within the composition,
which remain forbidden.

**Why this and not the alternative.** SU-9 could instead have required a superseded thing to become
**unreachable** rather than merely unprojected, which would have made the caller's dispatch fail. That
conflicts with SU-2, SU-8, and §5's *"it stops being reachable. It does not stop having existed."*
**Resolving an under-specification by contradicting three invariants of the same document is not a
revision of it.** The limit is real, and a document that states its limits is stronger than one that
implies a guarantee it cannot deliver.

**The realization needs no change.** Its behaviour was already the adopted reading. What was missing
was the document saying so — the same direction as Changes 1 and 2, and the third time in this
revision that the document moved rather than the system.

### Change 4 — constraints compose by conjunction

**Document:** `1b` Semantic Model. **Invariant:** SM-5, and SM-5a added. **Section:** §6.

§6 orders consequences `refuse` > `constrain` > `admit` and states that a rule set yielding several
consequences determines the dominant one. **That is an order over three consequence classes, not a
composition rule for two constraints.** `constrain` is defined as *"the proposal may proceed only in
a restricted form the rule states"* — the form is the rule's, and two applicable rules may state
different ones. Dominance establishes that the determination is `constrain` and left unstated which
restricted form applies.

**Nothing else in the family closed it, and the obvious fallback is forbidden.** `2e` §2 names
*"being first — precedence in resolution, loading, or authoring order"* as mechanism, and `2e` §10.2
and `2a` §7 require composition to be order-independent. An implementer reaching this point had to
invent, and two implementations could compose differently, satisfy every stated invariant, and admit
different proposals from the same closure.

**What changes.** §6 gains a paragraph: where several rules constrain, the constraints compose by
conjunction — a proposal satisfies the composed constraint only where it satisfies every constituent
constraint. SM-5a states it.

**Why conjunction and not another composition.** §6 already supplies the argument, applied to the
ordering rather than to this case: *"adding a rule to a closure could increase what the system may
do, and a governance closure that grows more permissive as it grows larger governs nothing."* Any
composition other than conjunction lets a proposal proceed in a form some applicable rule restricts,
which is that same failure one level down. **The change states a consequence of the document's
existing reasoning; it does not introduce a new principle.**

**What it invalidates.** No conformance claim — none has been discharged against `draft-2`. SM-5 is
unchanged and SM-5a is additive: no realization that already conjoined constraints becomes
non-conforming, and none that did otherwise was conforming to a stated rule, because there was none.

**Deliberately not done.** No general treatment of constraint algebra — no ordering over restricted
forms, no subsumption, no normalization. The gap was one unstated composition and the change is that
composition.

### Change 5 — `4d` states registers over declared fields, not columns

**Document:** `4d` Governed Transformation. **Invariants:** TR-5, TR-6. **Sections:** §5, §5.1, §6,
§8.

`4d` disclaims register shape twice — §1, *"register shapes … are free to vary"*, and §10's
does-not-specify list, *"the register shapes, column names, or document format"* — and then required
one. §5 read *"a phase document is registers — named tables with declared columns"*; TR-5 required
*"a constrained column's admissible values … declared with the register's shape"*; TR-6 required
grounding evidence to *"occupy a column declared for it"*.

**A column is a register shape.** A realization holding registers as typed records, as named
relations, or as any other representation has no columns, could not satisfy TR-5 or TR-6 as written,
and breached nothing this document means.

**What changes.** §5 states that a register is named with a declared field set, and that whether it
is realized as a table or otherwise is not specified. §5.1's two vacuity diagnostics are stated over
field names, which is what they were always about — a rule naming a field the register does not
declare, and a check resolving a field name by prefix. §6 is retitled *Declared fields* and its first
bullet constrains a **field**. §8's placeholder example says field. TR-5 and TR-6 say **field**.

**What it invalidates.** No conformance claim — none has been discharged against `draft-2`. **No
obligation is added, relaxed, or removed**: the requirements were, and remain, that a constrained
field's admissible values are declared with the register rather than elsewhere, that emptiness is
declared rather than inferred, and that grounding evidence occupies a declared place. **The
realization needs no change** — its registers are tables, which remains one conforming shape.

**How it was found, and what the search establishes.** By the same method as Change 2: an invariant
specifying what the document's own scope section disclaims. That method was then run across the whole
family — extract each document's does-not-specify list, keep only the **mechanism** words, and look
for them in that document's own invariants. **Three of nineteen documents flagged, and two are false
positives**: `4c` ID-1 and ID-3 name filename and representation in order to *subordinate* them to
identity, and `5a` IB-6 requires normalization *to* a canonical form whose shape §10 leaves open.
**`4d` is the family's only confirmed over-specification.** Recorded because a sweep that finds one
instance is a different fact from a sweep that was never run.

### Change 6 — a finding's location is register, entry and field

**Document:** `4d` Governed Transformation. **Invariants:** TR-4 restated, TR-5a added.
**Sections:** §5, §6.

TR-4 required a verdict to name *"the rule and location of each finding"*, and **nothing in the
family defined a location.** While §5 required *"named tables with declared columns"* the term had an
implicit reading — row and column — and **Change 5 removed that reading.** Registers were left with a
declared field set and no stated notion of an identified entry, so a location became inexpressible:
an implementer had to decide whether it meant the register, the register and field, or an entry
identifier the document never required entries to have.

**What changes.** §6 requires a register's entries to be individually addressable, and states that
*how* an entry is addressed — by declared key, by position, or otherwise — is not specified. §5
defines a location as identifying the register, the entry, and the field the finding concerns. TR-4
carries that; TR-5a states addressability.

**The split is the same one Change 5 made.** Required: an implementation can unambiguously identify
the particular governed register entry and field. Not required: a path syntax, pointer notation,
row/column scheme, filename convention, or database key.

**What it invalidates.** No conformance claim — none has been discharged against `draft-2`. **No
obligation is relaxed or removed:** TR-4's force is unchanged and becomes dischargeable, and TR-5a
states a property the document previously assumed through a representation it no longer requires.
The realization needs no change; its registers are tables, whose entries are addressable by position.

**Why addressability sits in §6 and not in TR-4.** It is a property of a register, not of a verdict.
Stating it inside TR-4 would make a reporting rule the place a structural property is declared, and
§6 is where register properties live.

**How it was found, and the lesson it carries.** By E4's A/B/C/D pass over `4d`'s twenty-six
invariants — the family's largest set — which returned 21 A, 4 B, 0 C and this one D. **Change 5
created it.** A change that removes a mechanism can strand a term that was relying on it, and the
remedy is procedural rather than textual: **after any over-specification fix, re-read the invariants
that used the removed vocabulary.**

### Change 7 — the sufficiency criterion is a profile's decision

**Document:** `4d` Governed Transformation. **Invariant:** TR-17, unchanged. **Section:** §16.

§16 deferred the sufficiency criterion to *"a profile **or** a governing element."* Two delegates were
offered for one question, and they differ in kind: a profile fixes a criterion for every system
claiming it, before any determination is made; a governing element fixes it inside one system, as a
governed determination. An implementer could not know which discipline applied, and an evaluator
could not know where to look — `7a` CF-7's condition.

**The family had already placed it.** `6a` §7's deferred-items table lists *"the sufficiency criterion
below which realization refuses"* among the decisions the family hands to profiles, alongside trust
roots, retention, admissible kinds and result classes. **NP-8 makes that binding:** *"a profile MUST
decide every deferred item bearing on a conformance claim it supports."*

**What changes.** §16 now reads *"which the applicable profile declares (6a §7),"* citing the
authoritative placement. TR-17 is unchanged — it never named a delegate.

**What it invalidates.** No conformance claim; none has been discharged against `draft-2`. No
obligation is added, relaxed or removed. A realization whose criterion came from a governing element
rather than a profile was never conforming to a stated rule, because two were stated.

**How it was found.** E4's classification pass, which examined every deferred item in the family by
whom it hands the question to: **twenty name a profile, one names another document, one names the
system's own governance, and this one named two.** It was the family's only ambiguous delegation.

## `draft-2` is frozen

Seven changes are declared above. **This revision is closed to further change in response to the
reference realization.**

**What freezing means.** `0z` §5.1 already holds that experience from a realization *"may occasion a
revision and may not decide one."* Freezing states the stronger position this revision has now
earned: **the realization's remaining findings are not occasions.** Fifteen RI absences, a
conformance profile with four unverifiable axes, and a realization that cannot make a conforming
genesis claim are all facts about one implementation, and `0z` §3 forbids amending a document to
match what was built.

**What was established before freezing.** Every normative document was read against the question an
independent implementer asks — *what would I have to invent?* — and classified. Twenty-six documents,
315 invariants, **zero missing semantic decisions and zero over-specifications**, after two were found
and corrected here as Changes 5 and 6. No unresolved cross-reference, and no ambiguous delegation: the
family's only one was Change 7.

**What would reopen it.** A defect found by someone who did not build the realization. That is the
next test and the only one this revision has not faced — internal examination reached its limit, and
the last defects it found were of a kind an outside reader would have seen sooner.

**What is not frozen.** The realization. Its findings are recorded in `doc/realization_map.md` §28.1
and belong to it.

### What is not changed, and why it is recorded here

Two findings against the documents were opened and **not** carried into this revision:

- **IN-13's scope** was ruled to be settled already by `5b` §2, §12 and IN-14 read together. The
  finding was the map misreading one invariant in isolation. No document changes; the realization has
  two violations to close.
- **Whether `4d` was derived from the realization** is not settled by finding one over-specified
  clause in it, and derivation is not itself a defect (`0z` §5.1). **Two things weigh against the
  concern and are recorded because they were found while making this change:** §1 states the
  disclaimer in the document's own voice, and TR-3a — the invariant that looked most like a
  transcribed lesson — carries a derivation, citing EN-5, of which it is the transformation-side
  form. A document that cites its own general case is deriving, not describing.

  The concern is **narrowed rather than closed**: `4d` remains the document with the most vocabulary
  of its own and the largest invariant set, and a clause-by-clause re-review against `8a` §4.7 is
  still what would settle it. **Recorded as outstanding against `draft-2`.**

### One thing worth noting about this revision

`draft-2`'s declaration above names `draft-1`, a superseded revision. Under `draft-1`'s own SU-5 that
reference was forbidden; it is permitted by the exception this revision adds. **The family's first
revision is licensed by the clause it revises** — which is `2a` §6's reflexivity working, and the
reason `4e` §9 says there is no outer mechanism governing this family's evolution: "there is this
document, applied to itself."
