# Parked Rulings & Items — Open PGC Standard

Rulings made about the standard family, and items considered for it and deliberately not admitted
yet. An item is here because it is not driven by a use case, not because it is wrong.

## Governed Transformation — comparison run records

Carried forward from the transformation specification fragment when that fragment was subsumed into
the Governed Transformation standard. The standard itself excludes review history; these records are
kept because a recorded gap that later closes is evidence about the method, and deleting it would
leave the method unfalsifiable.

Section references below are to the **retired fragment**, not to the current standard. The mapping
for the two that still matter: fragment §12 grounding → standard §11.1–§11.2; fragment §14 "a rule
that passes because a value is absent has not passed" → standard §5.1 and TR-3a; fragment §15.23
declared refusal and discharge → standard TR-23.

**One realization gap remains open across both runs**: nothing checks that a contract preserves
state another contract wrote.

### First run

**Gaps in the realization, not in this model.** Nothing checks that a contract preserves state
another contract wrote (§13). Human content entering once (§10) is enforced at two handoffs and not
at the rest. "A rule that passes because a value is absent has not passed" (§14) is stated by this
fragment and enforced nowhere — a live instance was found the day it was written.

**A gap this model had, now closed.** Grounding was specified as an interface without saying what it
must answer. A realization able only to enumerate cannot express a rule that compares a design
against one named existing artifact, and will migrate such rules to later, weaker checks while
remaining formally conformant. §12 now requires it.

**Correctly absent, and deliberately so.** How a realization derives its test fixtures, where a
dossier is stored relative to the system it changes, and how change requests are named are method and
convention. They belong to a realization and would not survive contact with a second one.

### Second run

**Two of the first run's three realization gaps have closed, and neither closure was recorded until
this run.** Preservation is now enforced at every handoff, not two: each of the eight carries at
least one rule reconciling what it received against what it passes on. And §14 is no longer enforced
nowhere — the realization made every rule identifier it declares fail on a document written to
violate it, and the pass found two rules that could not fire at all, nine registers whose missing
column was undetectable, and one live defect in a fixture that had never been reported.

**A gap in the realization, unchanged.** Nothing checks that a contract preserves state another
contract wrote (§13). It was the first run's first finding and is the only one still open.

**What §14 turned out to mean, which the first run did not know.** A rule passes because a value is
absent in more than one way, and only one of them is about the document. A rule whose parameters name
a column the register does not have reads every cell as empty and reports clean; a check that
resolves a column name by prefix is satisfied by a longer sibling, so a register can lose a column and
report clean. Both were live, in a realization that reported green, and neither was reachable by
reading the rule. **A rule set is not evidence that its rules can fail.** §14 states the principle;
what a realization must do about it is demonstrate refusal, not declare intent.

**A gap in this model, found by this run and closed by it — §15.23.** The realization carries a
governance mechanism this fragment had no home for: **a refusal the business declares and the design
must discharge.** A business states an operation the system must refuse; the design carries the
refusal out. Until now this fragment used "refuse" only of documents and rules, and said nothing
about a refusal that is *subject matter*, travelling from a business statement to a design that must
account for it. It is not realization detail: any transformation whose business can say *"the system
must never do X"* faces it, and it presumes no host capability beyond the three §16 already requires.

**What §15.23 deliberately does not say.** It does not enumerate the forms a discharge may take. The
realization admits three — performed by a step, deferred to a named owner under a stated condition,
or discharged by the governance surface — and a fourth, prohibition by absence, is designed and
unbuilt. Enumerating them would specify one realization's taxonomy as though it were the model, and
would make the reference realization non-conformant against a fragment written from it, which is not
how an invariant should arrive.

**Why the second clause is there.** A discharge can be declared, accurate in every cell, and still
not discharge anything: the realization's sharpest probe names an outcome the step really reports and
routes it to the ending that *completes* the act. Nothing that reads the declaration alone can see
it. So the invariant requires the discharge to be checked against what it does — the same distinction
§14 draws for rules, applied to a design's own statements.

**Correctly absent, confirmed against a second body of evidence.** Register identity — which
registers exist, what each is called, what a phase names them — remains realization detail; a
comparison by register name finds fourteen concepts with no home here and every one of them is a
register name. So is the quality score's shape (§8 governs its use, not its scale), so is how a
realization decides a phase has said enough. And **cross-subdomain reach** — that a subdomain owns
what it holds and another may read it and never write it — is correctly absent too, but for a
different reason worth stating: it presumes a host with subdomains and stores, and §16 requires only
three host capabilities, none of which is that.


## Specification plan — residue

The planning artifact `specification_plan.md` was retired when the specification it planned was
written. It carried twelve unresolved questions (U-01 … U-12). Every question it raised at
*specification* level is now answered:

| Was | Answered by |
|---|---|
| U-02 where canonicalization lives | required to exist, scheme unspecified — `4c` §2.2, MB-3 |
| U-03 what a snapshot address means | identity derived from content — `3b` §4, `4c` |
| U-04 conformance model and tiers | `7a` — and **tiers refused**, CF-11 |
| U-05 the snapshot boundary | constituents and construction obligations — `3b` §2, `4a` §5 |
| U-06 when transformation is specified | `4d` |
| U-07 inspection and assembly as tooling | inspection is a first-class boundary (`5b`); assembly is construction (`4a`) |
| U-09 numbering scheme | `0z` §2 |
| U-11 house style | `0z` §4 |
| U-12 conformance test kit | `7b` |

What remains from that list is not specification: U-01 (which components a platform has), U-08 and
U-10 (repository naming and staging). Those are arrangement questions a profile or an organization
answers, and the family declines to (`6a` §7, `6c` §11).


## Rejected framings of the same item

- **"Bootstrap Profile" / "Minimal Conformance Profile."** Proposed as a normative floor: the
  smallest set of declarations that constructs, seals, and executes a governed no-op. Rejected
  as premature — fixing a conformance floor before the Conformance Model exists decides what
  conformance is by accident. A floor is derived from the model, not the other way round.
- **"Getting Started" / "Hello World."** A tutorial. Belongs with the reference realization's
  own documentation, not in the standard family.


---

## Canonical kind enumeration — the trigger has fired

The Kind Vocabulary specifies the vocabulary *mechanism* and deliberately enumerates no kinds; which
kinds a system admits belongs to its profile. That much is settled and stated in `2d` §1.

What was parked with it is the enumeration itself. The canonical-kind list remains working material
in `kind_vocabulary.md`, held there **until a normative platform profile exists**, at which point it
is the candidate content for that profile's declared vocabulary.

**That condition is now met.** `GOVERNANCE_SURFACE_PROFILE_V0` is the profile in force and declares
`required_governance.artifact_kinds`. So the question is live rather than hypothetical: does the
profile's declared kind set become the canonical enumeration, and does `kind_vocabulary.md` then stop
being working material?

Parked rather than ruled because nothing yet depends on the answer — the profile's kind list is read
by the assembler today and the working list is read by no one. It is recorded here so the trigger is
not discovered by someone wondering why two lists of kinds exist.
