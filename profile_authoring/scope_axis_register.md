# Scope axis register

The engineering counterpart to the Scope Sheet. One entry per decision an author must make when
scoping a PGC system, with the citation that defers it, what a valid answer looks like, and which
artifact the answer lands in.

**This is not the author-facing document.** The Scope Sheet is generated from this register, so that
the questions an author answers and the obligations those answers create cannot drift apart. An
entry here without a citation is an invention and should be removed rather than filled.

## How to read an entry

| Field | Meaning |
|---|---|
| **Question** | the axis in business language, as the Scope Sheet asks it |
| **Answer** | *closed set* — choose from the listed options · *required shape* — free text that must contain the stated content |
| **Options** | marked **family-enumerated** where the standard states the set, **illustrative** where the set is composed here from practice and is not closed |
| **Defers from** | the document and section that hands this decision to a profile |
| **Lands in** | the artifact and field the answer becomes |
| **Watch** | the way this axis is commonly answered wrongly |

**The illustrative marking is load-bearing.** Where the standard states a set, an answer outside it
is inadmissible. Where this register composes one, the options are a starting point and an author
may answer outside them; treating an illustrative list as closed would make this document a second
vocabulary the family never declared.

---

# A — Semantic axes

The fourteen decisions `6a` §7 defers to a profile. They land in a **Normative Platform Profile**.

`6a` §7 governs all of them: *a decision MUST be the profile's own*, and the test is whether two
systems that disagree on the item could both claim the profile. **A profile need not decide every
item — but it MUST decide every item bearing on a conformance claim it supports.**

### A1 — Admissible kinds

- **Question.** What kinds of governed thing does this platform have?
- **Answer.** Closed set, plus an alias policy.
- **Options.** Illustrative — the family requires no kind and enumerates none (`6a` §7: *no kind is
  required by the family*). The reference set is a starting point, not the set. The alias policy is
  binary: aliases accepted at a boundary and normalized before conformance, or not accepted at all.
- **Defers from.** `2d` KV-9; `6a` §7.
- **Lands in.** NPP `declared_vocabulary.kinds`, one entry per kind, each stating whether ordinary
  admission requires a governance assertion (KV-10, MB-10); and `aliases_accepted`.
- **Watch.** `2d` KV-7 — an alias is never carried or emitted as an authoritative classification. A
  system that both accepts and emits a short form has two vocabularies, and they will stop agreeing.
  Closure is *within a revision* (`2d` §5): adding a kind is a vocabulary revision, not an edit.

### A1b — Kinds required to be exercised

- **Question.** Which of those kinds must actually be used for a snapshot to be this platform?
- **Answer.** Subset of A1; may be empty.
- **Options.** Not enumerable — a subset of the author's own A1 answer.
- **Defers from.** Not a `6a` §7 item. It is the distinction `6a` §5 rests on: a profile states
  requirements, never an inventory.
- **Lands in.** NPP `required_governance.artifact_kinds` — distinct from
  `declared_vocabulary.kinds`, which is the admissible set.
- **Watch.** Equating the two is the failure this axis exists to prevent: a profile requiring every
  kind it admits fails any snapshot that has admitted a kind it has no artifact for yet, and the
  failure reads as non-conformance rather than as a profile defect.

### A2 — Outcomes

- **Question.** What may a step conclude, such that the next step is chosen by it?
- **Answer.** Closed enumeration.
- **Options.** Illustrative. The family requires only that the set be closed.
- **Defers from.** `3a` §4 (outcome vocabulary, closed); Capability Standard.
- **Lands in.** NPP, and per-contract declarations.
- **Watch.** `3a` §4.1 — traversal advances on outcomes and nothing else. An "outcome" set that
  mirrors return values, error classes, or state inspections is not an outcome vocabulary; execution
  that routes on any of them has routed on something no contract declared.

### A3 — Result classes at the interaction boundary

- **Question.** What can a caller at the boundary be told?
- **Answer.** Closed enumeration; `n/a` where no interaction boundary is selected.
- **Options.** Illustrative. `5a` §14 leaves the members to a profile.
- **Defers from.** `5a` (Governed Interaction Boundary); `6a` §7.
- **Lands in.** NPP.
- **Watch.** `5a` IB-8 — a result class MUST carry no external representation semantics: no status
  code, no error number, no exit value. A set mirroring one protocol's status vocabulary has adopted
  that protocol as the semantics. An outcome whose meaning is domain-specific is a domain result,
  not a result class.

### A4 — Projections carried

- **Question.** What derived views of itself does the system carry?
- **Answer.** Closed enumeration, each with a derivation contract.
- **Options.** Illustrative — canonical forms, indexes, address-resolved forms, rendered forms
  (`4b` §1 names these as uses, not as a closed set).
- **Defers from.** `4b`; `6a` §7.
- **Lands in.** NPP, plus a `4b` PJ-3 contract per projection.
- **Watch.** `4b` §5, §6, PJ-7/PJ-11 — the source is authoritative, a projection is regenerated
  rather than edited, and where a projection and its source disagree the source governs. A
  projection carrying authority is a second specification.

### A5 — Namespaces and their arrangement

- **Question.** What namespaces does this system have, and may a reference name one not on the list?
- **Answer.** Closed set: the enumeration, plus open/closed, plus two explicit denials.
- **Options.** Illustrative for the enumeration; **family-enumerated** for the denials — a namespace
  carries identity and nothing else, and derives neither concern nor authority.
- **Defers from.** `4c` §8; `6a` §7.
- **Lands in.** NPP `namespaces` — `declared`, `closed`, `derives_concern: false`,
  `derives_authority: false`.
- **Watch.** `4c` §5, ID-12, GO-11 — that a namespace name coincides with a concern name is an
  arrangement, never a derivation. A namespace set settled after the artifacts exist is settled by
  rename; decide it first. Adding a namespace changes the profile's obligations and is therefore a
  new profile identity (NP-9).

### A6 — Trust root

- **Question.** What does a checking party accept without asking for anything further?
- **Answer.** Required shape: something nameable.
- **Options.** Illustrative — none/self-asserted · an operator-held key · an organizational PKI · a
  transparency log · a hardware root · an external registrar.
- **Defers from.** `3e` §6.2, EV-10; `6a` §7 (*this family does not supply a trust root*).
- **Lands in.** NPP.
- **Watch.** An integrity value is not a trust root. A content hash establishes that bytes did not
  change; it establishes nothing about who vouched for them. `3e` EV-10 requires an attestation
  chain to *terminate* in a nameable root, and "the snapshot hash" terminates nothing. This is one of
  the three `6a` §7 singles out as commonly assumed rather than decided.

### A7 — Evidence retention

- **Question.** How long is evidence kept, and what ends its life?
- **Answer.** Required shape: a period and what terminates it.
- **Options.** Illustrative — none beyond the run · a bounded window · until superseded · indefinite.
- **Defers from.** `3e` §11; `6a` §7.
- **Lands in.** NPP.
- **Watch.** `3e` §11 — the period over which a determination can be established *is* the period over
  which its evidence is retained. A profile supporting a claim about evidence while leaving retention
  undecided supports a claim nobody can evaluate.

### A15 — Where a Section A value is carried

- **Question.** Which Section A answers does the environment supply, rather than the snapshot
  carrying them?
- **Answer.** Required shape: the list, or `none`. Each listed value names the answer it qualifies.
- **Options.** Illustrative — none · a named retention window · a named policy value.
- **Defers from.** `3b` §15; `6b` §2, §6; `6a` §7.
- **Lands in.** NPP `environment_supplied_values`.
- **Watch.** This axis exists because every other Section A axis can be fully answered while leaving
  it open. A complete answer states what a value *means*, never where it is written, and the two come
  apart precisely where it matters: a value supplied by the environment can change with no declared
  act. Under a trust root (A6) the consequence is sharper — anything outside the snapshot is outside
  what the signature covers, so the signature vouches for the evidence and not for the rule governing
  it. **Cross-check:** every value listed here MUST also appear in `declared_environment_facts` (B8).
  One listed here and absent there is a governed consequence varying with something undeclared.

### A16 — Partial application

- **Question.** Where a transition can be applied partly, what state results?
- **Answer.** Required shape: the resulting state, or a statement that no admitted realization can
  apply a transition partly together with what makes that true.
- **Options.** Illustrative — no transition is resumed after partial application · a partly applied
  transition is determined not to have applied · every effect is re-appliable without changed effect.
- **Defers from.** `1b` §8 (SM-7a, SM-10); `6b` §8.1.
- **Lands in.** NPP `partial_application`.
- **Watch.** SM-7a binds whether or not a profile mentions it, so silence here is not neutrality —
  it is an undetermined state the declarations owe an answer for. **Cross-check:** where more than
  one node participates (B1/B7), a node lost mid-step *is* a realization applying a transition
  partly, so "cannot happen" is refusable rather than merely optimistic. Note the direction of the
  dependency: the environment produces the case, and Section A must answer it — answering it in
  Section B would settle what a result means by where it ran.

### A8 — Read surface openness

- **Question.** Who may read what this system contains?
- **Answer.** Required shape: which classes of caller are admitted to which declared read operations.
- **Options.** Illustrative — closed · named caller classes · every caller to every declared read.
- **Defers from.** `5b` §11; `6a` §7.
- **Lands in.** NPP.
- **Watch.** `5b` §11 draws the line precisely: **the profile fixes the policy; it MUST NOT dispense
  with the determination.** The most permissive policy available is still a policy, and a realization
  that answers a read it never determined has an ungoverned read path whatever the profile says
  (CP-11 — reachability is not permission). A refusal to answer is itself a determination and is
  evidenced (EN-8).

### A9 — Read attribution

- **Question.** Is a read attributed to whoever made it?
- **Answer.** Closed set — yes · no.
- **Defers from.** `5b`; `6a` §7.
- **Lands in.** NPP.
- **Watch.** Attribution interacts with A7: attributed reads are evidence, and evidence has a
  retention answer.

### A10 — The sufficiency criterion

- **Question.** When is a design too thin to build from, so construction refuses?
- **Answer.** Required shape: the criterion, and what refusal looks like when it is not met.
- **Options.** None enumerable — this is the profile's own statement.
- **Defers from.** `4d` §16 (*the sufficiency criterion — what counts as fixing every fact the
  realization needs*); `6a` §7.
- **Lands in.** NPP.
- **Watch.** `4d` — a design language that omits it is a second, ungoverned design authority, and
  sufficiency stops meaning anything. Note also `4d`: document admissibility, sufficiency, and
  realization at zero differences are **jointly insufficient** to establish that anything works — so
  this axis must not be answered as though it were a correctness criterion.

### A11 — Interaction-form elements as governed artifacts

- **Question.** Is the shape of what arrives at the boundary itself a governed thing?
- **Answer.** Closed set — yes · no · no boundary selected.
- **Defers from.** `5a`; `6a` §7.
- **Lands in.** NPP.

### A12 — External protocol bindings as governed artifacts

- **Question.** Is the binding to a wire protocol itself a governed thing?
- **Answer.** Closed set — yes · no · none selected.
- **Defers from.** `5a`; `6a` §7.
- **Lands in.** NPP.
- **Watch.** Answering `no` while claiming protocol independence is the trap in A-claims below: a
  claim discharged by a substitution the profile's systems cannot perform is not discharged.

### A13 — Reaching the read surface with no interaction boundary

- **Question.** If nothing crosses a boundary, how is the system read at all?
- **Answer.** Required shape; `n/a` where a boundary is selected.
- **Defers from.** `5b`; `6a` §7.
- **Lands in.** NPP.
- **Watch.** This is the axis a single-node, boundary-free platform most often skips, and it is
  exactly the one such a platform needs — the read surface still has to satisfy `5b` §10.

### A14 — Genesis discharge

- **Question.** What settles the claim that the first snapshot was legitimately made?
- **Answer.** Required shape; omit only where the profile's scope excludes a first snapshot.
- **Defers from.** `7b` §9; `6a` §7.
- **Lands in.** NPP.
- **Watch.** `7b` CD-14 — a genesis claim MUST demonstrate that the claimed profile was **not
  authored by what it governs**. This is where NP-7 stops being a remark and becomes a demonstration
  that can fail. `7b` §9 also warns that self-consistency at genesis is satisfied by every vacuous
  genesis.

---

# B — Environment axes

The constraints `6b` §3 admits. They land in an **execution environment profile**, which is a
separate artifact from the NPP.

**`6b` §4 bounds every entry below.** An environment profile MUST NOT introduce a governance kind, an
authority, a determination point, environment-derived behavior, or an exemption. If an answer here
would need any of those, the answer belongs in Section A and has been asked in the wrong place.

**`6b` §2 is the standing test.** Governed consequences MUST NOT vary with the environment. An
environment may determine whether execution happens, when, how fast, and where — and nothing about
what it means.

| Axis | Question | Concerns |
|---|---|---|
| **B1 availability** | What must be reachable for execution to proceed, and what happens when it is not? | whether a resource, node, or dependency can be reached |
| **B2 placement** | Where does a step run, and on what? | where a step is performed |
| **B3 resource** | What compute, memory, and storage are guaranteed, and to what? | how much is available |
| **B4 timing** | What deadlines apply, and what bounds latency? | how long things take |
| **B5 isolation** | What must be separated from what, and by what mechanism? | separation and its mechanism |
| **B6 failure mode** | What does a failure look like to this system? | how the substrate fails |

- **Answer.** Required shape for each: the obligation, and what would establish a breach.
- **Options.** Family-enumerated as *axes*; the answers are the profile's own.
- **Lands in.** Execution environment profile, per `6b` §9 — the environment it profiles, the
  constraints it requires, what it excludes, the claims it supports.

### B7 — Distribution and ordering

- **Question.** Does more than one node participate, and what ordering does the system require?
- **Answer.** Required shape where distribution is selected.
- **Defers from.** `6b` §8, §8.2.
- **Watch.** `6b` §8.1 — distribution's characteristic failures already have determinations; they are
  not a reason to invent new ones. A single-node answer is a legitimate environment answer, not the
  absence of one, and produces a profile with few obligations rather than no profile.

### B9 / B10 — What the environment excludes, and what it claims

- **Question.** Which systems can this environment not serve, and what does it claim about itself?
- **Answer.** Required shape for both; either may be *none*.
- **Defers from.** `6b` §9 — an environment profile declares what it excludes and the conformance
  claims it supports.
- **Lands in.** Environment profile `excludes`, `supported_claims`.
- **Watch.** `6b` §9 names both, so neither may be emitted unasked. An empty the generator asserted
  is a claim the author never made.

### B8 — Declared versus ambient environment

- **Question.** Which environmental facts does the system take as governed inputs, and which does it
  merely run within?
- **Answer.** Required shape: the enumeration of declared facts.
- **Defers from.** `6b` §6.
- **Watch.** `6b` §2 — what may not vary is anything the system did not declare. A declared
  environmental fact is part of *the same inputs*; an undeclared one that changes a consequence is
  environment-derived behavior and is forbidden (AI-12, EX-3).

---

# C — Domain axes

Asked once per domain. They land in a **domain profile**, one per domain (`6c` §5).

**These numbers are not the Scope Sheet's.** The sheet asks C1–C5 in author order; the register
numbers C1–C7 by axis. The map:

| Register | Scope Sheet |
|---|---|
| C1 subjects, C3 capabilities, C4 workflows, C5 stores, C6 boundary exposure | C1, one row of its table each |
| C2 governance | C1, the *obligations* row |
| C7 authority claim | C2 |

D1–D5 below are the sheet's C1b, C1c, C3, C4 and C5.

| Axis | Question | Answer |
|---|---|---|
| **C1 subjects** | What does this domain own and answer for? | required shape |
| **C2 governance** | What obligations apply to its subjects, under which authority? | required shape |
| **C3 capabilities** | Through which contracts is its work reached? | enumeration |
| **C4 workflows** | Through which structures is its work ordered? | enumeration |
| **C5 stores** | What governed state does it own, and what may write to it? | enumeration + writer set |
| **C6 boundary exposure** | What of it is reachable from outside, and how? | required shape |
| **C7 authority claim** | Is it an authority, or a concern? | closed set — authority · concern |

**C7 is not optional and has a test.** `6c` §4: a domain is an authority only if it satisfies CA-3 —
a declared constituting act and answers, from declared artifacts alone, to who the authority is, what
constituted it, what subjects fall within it, **what decision it may make that no other authority
may**, and how it relates to the authorities above and beside it — plus the CA-4 independence test.

- **Watch.** CA-2 — a domain acquires no jurisdiction by being named, bounded, deployed separately,
  or owned by a different team. CA-6 — a concern classification cannot constitute an authority. `6c`
  §4: a domain that is not an authority is not thereby illegitimate; being a concern governed under
  the authority above it is *the ordinary and correct arrangement*. A profile asserting an authority
  claim without discharging CA-3 has asserted rather than established it.

---

# D — Composition axes

Not deferred by `6a`, and needed anyway: these are what a checking party reads a manifest against.

| Axis | Question | Lands in |
|---|---|---|
| **D1 required domains** | Which domains must be present for this to be the platform it claims? | NPP `required_domains` |
| **D2 excluded domains** | Which domains does this profile not admit? | NPP `excluded_domains` |
| **D3 entry points** | Which workflows must resolve and be reachable? | NPP `required_workloads.entry_workflows` |
| **D4 boundary status** | Is the interaction boundary declared only, or exercised? | NPP, and the claims it permits |
| **D5 claims** | Which conformance claims does this profile support? | NPP `required_claims`, with §7 discharge |

- **Watch.** `6a` §5 and CF-5 — a profile states requirements, never an inventory. A snapshot may
  contain more than the profile requires and still conform; a check that fails a larger snapshot for
  being larger is testing resemblance. D4 constrains D5 directly: a claim asserting stability across
  wire protocols cannot be discharged by a platform that exercises none.

---

# E — Answers the Scope Sheet must not offer

Each of these reads as a decision and is not one.

- **"Whatever the system declares."** `6a` §7 and NP-12 — an item is not decided by requiring the
  system to decide it. This is the more dangerous failure, because it satisfies the form while
  inverting the substance, handing the constraint back to the party the profile constrains.
- **"Minimal" or "maximal."** `6a` §8 — minimality is relative to a profile, and no platform is
  minimal by nature. `6a` §11 — no profile is privileged. A profile requiring every facility forces
  obligations NP-6 says must not be declared where they cannot be enforced.
- **"As the reference realization does."** CF-5 — resembling a realization establishes nothing, and a
  conformance regime testing for resemblance tests a choice.

---

# F — What has no axis

These cannot be projected from answers, and a generator that fills them produces a profile that
reads complete and is not.

| Not an axis | Why | Required by |
|---|---|---|
| **Additional obligations** | each must state what would establish a breach; an obligation nothing could refuse is not in force, and one restating a selection is not additional | `6a` §5, NP-6, `2f` EN-1 |
| **Supported claims and their discharge** | a demonstration must be capable of failing; naming a substitution the profile's systems cannot perform supports a claim nobody can evaluate | Part VII, `7b` CD-4, CF-8 |
| **Derivation** | whether this profile derives from another, named by identity, is a judgment about intent | `6a` §10, NP-10 |
| **Externality** | a generator the author wrote, producing the profile the author's system claims, is not external | NP-7, `7b` CD-14 |

**Also not an axis: the read surface minimum.** `5b` §10 requires every system to answer what it
contains, what governs what, what it determined, and what it is. That is not a choice — it is the
condition of being checkable at all — so it is stated to the author as a floor, never asked.

### D1 — Derivation

- **Question.** Does this profile derive from another, and from which identity?
- **Answer.** Required shape: the base profile's identity, or `none`.
- **Options.** Illustrative — none · a named profile identity.
- **Defers from.** `6a` §10, §11 (NP-10).
- **Lands in.** NPP `derives_from`, and §5 of the platform profile.
- **Watch.** Derivation was previously treated as a judgement a generator must decline, and the
  judgement it declined was the base's *content*. That is not what this axis asks. Whether a profile
  derives at all, and from which identity, is an ordinary answer an author can give, and NP-10's
  obligation not to widen the base is the same sentence whatever the base says. The failure this
  catches is composition without acknowledgement: building on a governance surface whose
  constitutions and invariants the author did not write is deriving, whatever the repository layout
  suggests, and a profile claiming otherwise claims a surface it does not carry.

### C3 — Entry points

- **Question.** Which workflows must resolve and be reachable for this to be the platform claimed?
- **Answer.** Required shape: artifact identities of the form `namespace::ARTIFACT_IDENTITY`, or `[]`.
- **Options.** None enumerable — the identities are the author's own.
- **Defers from.** `6a` §5; `3b` SN-7.
- **Lands in.** NPP `required_workloads.entry_workflows`, which a realization matches against the
  identities a snapshot carries.
- **Watch.** This is the only axis in the register whose value is resolved rather than read, and two
  failures follow from that. A **description** passes every check in the toolkit and fails at
  assembly, where the message names the description as an absent artifact — the profile's defect
  presented as the snapshot's. And an identity that is not a `WORKFLOW` cannot be satisfied at all: a
  domain may be required, reachable and working while carrying no workflow, as a read surface built
  from transport ingress and egress pairs does. Where a domain's reach is the concern, requiring its
  kinds (A1b) and the domain itself (C1b) carries the obligation without naming an entry point.

---

## What this register does not cover

The C axes other than C3 — the domains themselves, which of them are required or excluded, whether
anything crosses a boundary, and what the profile claims — have no entries here, and the axis check
does not report them. They are asked by the sheet and validated by the generator, but a decision that
appears in neither this register nor that check is one nothing independently verifies was made.

C3 is entered because it resolves against a snapshot, which made its failure mode concrete. The
others are not less important for being absent.
