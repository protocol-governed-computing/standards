# Realization Map

*Non-normative. This document is evidence about one realization. It requires nothing, relaxes
nothing, and establishes nothing about any other implementation — Implementation Guidance §2 governs
what such evidence is worth, notably that resembling the reference realization establishes nothing.
Where this map and a normative document appear to differ, the document governs.*

## 0. Subject

**This map is not a document of the standard family.** It declares no part, derives nothing along
the derivation rule, and states no conformance obligation — it satisfies none of the membership
conditions of the Document Set, by design. It carries no file identifier, appears in no document
map, and **does not participate in revision or supersession.** A finding closed here changes this
map and nothing else; it is not a revision of anything.

That matters because a map inside the revision unit would let a change in a codebase move the
standard's revision identity — inverting the direction of authority the family exists to protect.

Like any evidence, it is stated against a named subject:

| | |
|---|---|
| **Realization** | the Protocol-Governed Computing reference realization |
| **Snapshot** | `94e9b9ddffdc5d854c1f540169a864b9d55b1d8c4d30bbe9b2602dced0aa8643` |
| **Composition** | 7 domains, 394 artifacts, composition conformance PASSED over 5 rules |
| **Standard revision** | `draft-2` |

**This is the second measurement.** The first was stated against snapshot `7b6f2699…` under
`draft-1`, before Tasks B and C. **§28 carries the disposition of every finding** — what closed, what
was revised, what a change request carries, what is deferred and on what ground. Read it before
reopening anything here; the entries below record what was found, and only §28 records what became
of it.

**This map is retired.** Task D is closed and the map is not extended. Its value was the attempt
rather than the document: the three defects it found against the standard — SU-5, TR-17, SU-9 — were
each found by trying to conform and failing, and that mechanism needs no map. The findings §28 leaves
open are absences rather than falsehoods, each a change request when somebody wants one.

**The map is true of that subject and of nothing else.** It does not age into being wrong; it stays
about an older snapshot, which is a different and honest thing. Reading it against a later
composition establishes nothing until the subject above is restated and the entries rechecked.

**The subject has two axes and only one has moved.** The realization is unchanged at
`7b6f2699…`. The standard moved from `draft-1` to `draft-2`, which supersedes two entries of this
map — the rulings on SU-5, TR-17 and SU-9 changed the documents those entries were about. All three
are marked **closed by revision** below, with the declarations in `revisions.md`. The other
twenty-three normative documents are unchanged, so every other entry stands against `draft-2` as
written.

## 1. What this map is

Implementation Guidance §6 states the map's two purposes: to save every implementer the
rediscovery of reading the code, and to make visible that **a normative document with no
demonstration is either unimplemented or unimplementable**.

For each normative invariant this map records **where the reference realization demonstrates it** —
which declarations, which construction path, which region of the sealed representation, which
evidence — and where nothing does, which of the two that is.

It is a partial map. Documents are covered as they are worked; §27 collects the findings, §28
records what became of each, and §29 states what is covered so far.

## 2. How to read an entry

Each entry carries a **class**:

| Class | Meaning |
|---|---|
| **Demonstrated** | a named mechanism establishes the invariant, and its failure is observable |
| **Partial** | some clause of the invariant is established and some is not; the entry says which |
| **Unimplemented** | nothing demonstrates it, and nothing prevents a realization from doing so |
| **Unimplementable** | the invariant cannot be demonstrated as stated — a finding against the document |
| **Over-specified** | the document names a mechanism while believing it names a meaning (`8a` §4.7) — a finding against the document |
| **Vacuous** | the mechanism the invariant constrains does not exist here, so it cannot be violated |
| **Violated** | a mechanism demonstrably does what the invariant forbids |

**Partial, Unimplemented and Vacuous entries are findings**, and a finding is resolved by ruling —
never by editing a normative document to match what was built (Document Set §3).

Locations are repository-relative paths in the reference realization. They are addresses in one
codebase, not part of the standard.

## 3. Snapshot — SN-1 … SN-13

The realized snapshot is the directory produced by `snapshot_assembler` and consumed unchanged by
`protocol_runtime`. Its self-description is `snapshot/manifest.json`; its sealing act is
`assembler/core.py::assemble`; its acceptance is `runtime/boot.py::warm_boot`.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **SN-1** immutable from sealing | `assemble` writes the manifest once and never rewrites it; `verify_snapshot` and `warm_boot` both refuse a domain set that has moved | Partial — §3.1 |
| **SN-2** identity derived, covering every constituent, never assigned | `core.py::compute_composite_hash` over `_identity_view` — sha256 of canonical JSON, timestamp-free and path-free | Partial — §3.2 |
| **SN-3** same identity ⇒ identical content | follows from SN-2's derivation over the identity view, for the constituents that view covers | Partial — §3.2 |
| **SN-4** execution closure | `runtime/loader.py` loads dispatch, handlers and vocabulary from the snapshot only; the compiler's static handler registry admits no path that reaches outside it | Demonstrated |
| **SN-5** self-description enumerates constituents, integrity, provenance, claimed profile | `manifest.json` carries `snapshot_id`, `composite_hash`, `domains[]` with a hash per projection, and `provenance` | Partial — §3.3 |
| **SN-6** self-description is a constituent covered by the identity | — | Unimplemented — §3.4 |
| **SN-7** claimed profile not self-authored | no snapshot claims a profile | Vacuous — §3.3 |
| **SN-8** verified for integrity, identity, totality, profile before execution | `warm_boot` recomputes the composite and refuses a mismatch; `loader.py` anchors each domain to the manifest's tokenized hash | Partial — §3.5 |
| **SN-9** refused whole; no partial acceptance | `warm_boot` raises before any domain becomes resident; there is no per-domain admission path | Demonstrated |
| **SN-10** no behavior enters from outside the snapshot | `runtime/api.py` resolves every handler through the snapshot's dispatch table; an operation the table does not name has no path to an implementation | Demonstrated |
| **SN-11** same snapshot, inputs and state ⇒ same governed consequences | one conforming agent exists, so the invariant's subject — agreement between two — has never been exercised | Unimplemented — §3.6 |
| **SN-12** change by successor, never in place | the assembler has no incremental mode; every build reruns `assemble` over all domains | Demonstrated |
| **SN-13** genesis relieves the first snapshot of nothing | genesis produces its snapshot through the same `assemble` path as any other | Demonstrated |

### 3.1 SN-1 — sealing is detected, not enforced

Nothing renders the sealed directory immutable. What exists is detection, and it is narrower than
the invariant: `verify_snapshot` and `warm_boot` recompute the composite over `domains[]`, so a
change to the *domain set or its recorded hashes* is refused. A change to a file **inside** a
projection is not, because no recorded hash is recomputed from content at that point (§3.5).

The finding is not that immutability is unenforced — the standard requires that a sealed snapshot
not change, not that a filesystem prevent it. The finding is that the realization's detection does
not cover every way it can change.

### 3.2 SN-2, SN-3 — the identity does not cover every constituent

`_identity_view` is six values per domain: the domain name, the `tokenized`, `vocabulary` and
`canonical` projection hashes, the trust attestation hash, and the graph address hash. The snapshot
carries constituents outside that view:

| Constituent | Read by |
|---|---|
| `artifact_index/index.json`, `kind_index/index.json`, `store_index/index.json` | the inspection surface |
| `behavior_logic/<domain>/` | `si.behavior_logic.*`, `protocol_runtime examine` |
| `conformance/composition.json` | the composition conformance result |
| `evidence/<domain>/` | provenance and attestation readers |

Each is part of what the snapshot carries as itself, and each is outside the identity. **A changed
index answers a different question under an unchanged snapshot identity** — which is exactly what
SN-2's totality clause exists to prevent, and what SN-3 rests on.

That the indexes are *derivable* from covered projections does not discharge it. Derivability makes
a divergence repairable; it does not make it detectable, and the snapshot is the thing a party who
did not build it must be able to check.

### 3.3 SN-5, SN-7 — no claimed profile, and a partial enumeration

The manifest carries identity, integrity and provenance. It carries **no profile claim**. Profiles
exist in the realization — `.github/snapshot_profiles/` holds two — but a snapshot does not name one,
so no acceptance can evaluate clause 4 of §7 and SN-7 has no claim to constrain.

The enumeration is also not total in SN-5's sense: `domains[]` enumerates the per-domain projections
and nothing enumerates the constituents listed in §3.2. Under §6 that material is undeclared content
and MUST be refused at acceptance; it is instead read normally.

### 3.4 SN-6 — the self-description is outside its own identity

`compute_composite_hash` reads `manifest.json`'s `domains[]` and hashes that. The manifest as a whole
— including `provenance`, and including the `snapshot_id` it bears — is not itself covered. The
standard's reasoning applies directly: claims made about the snapshot can change without the
snapshot's identity changing.

This is **unimplemented rather than unimplementable**. A self-description covering itself is
constructible in the ordinary way — hash the description with the identity field held at a fixed
placeholder, then write the result in — and nothing in the realization forecloses it.

### 3.5 SN-8 — integrity is a chain of recorded values, not a content check

This is the map's sharpest finding so far, and it is invisible from a snapshot that verified.

At construction, integrity **is** computed from content: `compiler/graph/hashing.py::compute_projection_hash`
produces each projection hash, and `stages/s8_verify.py` round-trips what was materialized against
what was determined. Those values are then written into each projection's `metadata.json`.

At acceptance, nothing recomputes them. `verify_snapshot` compares `metadata.json`'s **recorded**
`projection_hash` against the manifest's, and `loader.py`'s manifest anchor compares the same
recorded value against the manifest's claim. Every comparison is between two copies of a number that
was computed elsewhere, at another time.

The consequence is precise: **editing a file inside a projection, and touching nothing else, passes
acceptance.** The recorded hash still matches the manifest, the composite still recomputes, the
snapshot is accepted, and execution proceeds against content that is not what was determined. What
the realization has is a *provenance chain* — a demonstration that the manifest, the metadata and the
attestation all agree about what was built. SN-8 clause 1 asks for something else: that each
constituent match the integrity value the self-description carries **for it**.

Clause 3 (totality) is likewise not established at acceptance, though the analogous check exists at
construction — `s8_verify.py::_check_undeclared_files` and `_check_undeclared_directories` refuse
material no declaration accounts for. The check has a home; it is on the wrong side of the seal.

Clause 4 (profile) has no subject (§3.3).

### 3.6 SN-11 — one agent cannot demonstrate agreement between two

Determinism is exercised: a clean rebuild reproduces the snapshot identity. That is GC-9, and it is
a property of construction. SN-11 is a property of *execution* across conforming agents, and its
demonstration requires a second agent — which is not a defect in the realization so much as a
statement of what a single-implementation family can establish. It is recorded here so that the
absence is not mistaken for coverage.

## 4. Governed Construction — GC-1 … GC-14

The realized construction is `protocol_compiler`, whose nine stages `s1_extract` … `s9_attest`
correspond one-to-one with the nine obligations of §5. **That correspondence is an accident of this
realization and the map's most misleading feature** — §5 states obligations with dependency
constraints, explicitly not stages, and a reader who takes the stage list as the standard's shape has
read an architecture into a semantic requirement. §4.1 states what the correspondence does and does
not license.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **GC-1** determines admissibility, not adequacy | `s4_govern` evaluates declared rules and yields admitted / refused — with one exception found later, at `2f`: `assert_cc_no_unused_outputs_v0` detects "code smell" and "optimization opportunities" | **Violated** — §13.2 |
| **GC-2** admissibility from declarations and governance alone | every stage reads artifacts and the governance closure; no stage invokes a capability transform | Demonstrated |
| **GC-3** every obligation discharged, none on a successor's basis | the nine stages, each consuming only its predecessors' `State` | Demonstrated — §4.1 |
| **GC-4** only admitted candidates; nothing by discovery | `s1_extract` admits from the build configuration's declared `artifact_types` and roots; `STRUCTURE_BUILD_*_CONFIG` is the admission authority | Demonstrated |
| **GC-5** nothing precedes a candidate's determination; nothing revisits it | stage ordering, and `s4_govern` writing a determination that no later stage reopens | Demonstrated |
| **GC-6** a refused construction produces no usable output | a stage raising aborts the pipeline before `s7_materialize` writes | Partial — §4.2 |
| **GC-7** refuse rather than repair, complete, substitute or default | the fail-hard doctrine, enforced by review rather than by a mechanism | Partial — §4.2 |
| **GC-8** construction originates no meaning | derived elements carry `derived_from`; `s5_construct` builds structure over the resolved graph and adds no declaration | Demonstrated |
| **GC-9** same declarations, same closure ⇒ same representation and identity | a clean rebuild of the platform and every domain reproduces the snapshot identity | Demonstrated |
| **GC-10** no undeclared input | `pgc_env_check.py` asserts the interpreter and that no foreign package is reachable; roots are environment-provisioned, never synthesized | Demonstrated |
| **GC-11** composition obligations over the whole | `assembler/conformance.py` evaluates the composition rule set over every artifact of every domain, after assembly | Demonstrated |
| **GC-12** copies of one identity must agree | `assembler/core.py::_verify_copies_agree` compares every copy of each identity across domains and refuses disagreement | Demonstrated |
| **GC-13** materialized verified against determined | `s8_verify.py::_verify_roundtrip`, `_verify_tokenized_integrity`, `_verify_evidence_integrity`, `_verify_canonical_references` | Demonstrated |
| **GC-14** attestation confers no admissibility | `s9_attest` runs after `s8_verify` and writes an attestation; no stage reads an attestation to decide admission | Demonstrated |

Two mechanisms outside the compiler are load-bearing here and are worth naming, because an
implementer reading only `compiler/` would not find them:
`assembler/core.py::_verify_governance_provenance` refuses a domain compiled against a governance
closure other than the one being assembled, which is what makes GC-9's "same closure" checkable
rather than assumed; and `_verify_copies_agree` is the whole of GC-12.

### 4.1 The stage correspondence, and what it licenses

`s1_extract` ↔ admission, `s2_canonicalize` ↔ normalization, `s3_semantic_addressing` ↔ resolution,
`s4_govern` ↔ governance determination, `s5_construct` ↔ structure construction, `s6_project` ↔
projection, `s7_materialize` ↔ materialization, `s8_verify` ↔ verification, `s9_attest` ↔
attestation.

This establishes that the obligations are **discharged** and that the dependency constraints among
them are **satisfiable in one order**. It establishes nothing about the obligations being stages,
and a conformance regime reading the correspondence as the requirement would reject a realization
discharging several in one operation — which §5 explicitly permits.

### 4.2 GC-6, GC-7 — refusal is doctrine, not a mechanism

A refused construction produces no usable output because the pipeline aborts before the writing
stage, not because output is staged and discarded. The two coincide today. They come apart the moment
an obligation is discharged after materialization, or materialization is incremental — and nothing in
the realization would notice.

GC-7 is the same shape and weaker. "Refuse rather than repair" is stated in the repositories'
authoring rules and observed by review; no check refuses a repair. This is the hazard Implementation
Guidance §5 names last, in its general form: a property everyone believes holds, that nothing has
been made to demonstrate.

## 5. Governed Inspection — IN-1 … IN-14

The realized read surface is `snapshot_inspector`: eighteen operations under the `si.` identity
space, each declared by a Transport Ingress contract in `snapshot_inspector/transport/`, implemented
in `inspector/reads/`, and resolved through the closed registry `inspector/registry.py`.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **IN-1** inspection changes nothing | every `reads/` module opens the snapshot read-only and returns a value; no write path exists in the package | Demonstrated |
| **IN-2** answering invokes no governed target | contracts declare `handler.kind: SNAPSHOT_READ`, which selects the inspector's static entry point rather than the runtime's; the engine routes by kind and stops | Demonstrated |
| **IN-3** every question is a declared, sealed operation | `TI_SI_*_V0.md` — one contract per operation, carrying its identity, input contract and implementation binding, compiled and sealed like any artifact | Demonstrated |
| **IN-4** a read operation declares read or query; a read computes no relationship | no contract carries the classification | Unimplemented — §5.1 |
| **IN-5** a query derives only from declared structure | `si.topology.impact` and `si.artifact.refs` traverse the sealed graph and nothing else | Demonstrated |
| **IN-6** can answer about a named artifact | `si.artifact.show`, `si.store.show`, `si.behavior_logic.show`, `si.vocab.resolve` each take an identity | Demonstrated |
| **IN-7** reads the governed system, not construction internals | every operation resolves against the snapshot root; none reads compiler `State`, a working tree, or a source repository | Demonstrated |
| **IN-8** returns the answer asked for, delegating no derivation | `si.capability.surface` and `si.rule_set.list` were each added rather than left to a client join | Demonstrated — §5.2 |
| **IN-9** malformed or unreadable material refuses; unanswerable is refused, not empty | `reads/artifact_show.py` returns `NOT_FOUND` with a reason for both a malformed identity and an absent one | Demonstrated |
| **IN-10** no fallback to another source, a partial source, or a default | the registry is statically imported and closed; an unnamed implementation cannot be reached | Demonstrated |
| **IN-11** can answer what it contains, what governs what, what it determined, what it is | `si.artifact.list` / `si.artifact.refs` / `si.snapshot.summary` / `si.snapshot.topology` | Partial — §5.3 |
| **IN-12** governance determines whether a read may proceed | `context_requirements: []` in every contract — the field exists and is inert | Unimplemented — §5.4 |
| **IN-13** no read path that is not a declared operation | — | Unimplemented — §5.5 |
| **IN-14** no inspection against an unsealed representation | operations take a snapshot root, and the assembler's output is the only root any surface is given | Partial — §5.5 |

### 5.1 IN-4 — the read/query distinction is not declared

A contract's `catalog.category` (`ARTIFACTS`, `BEHAVIOR`, `SNAPSHOT`, `STORES`, `VOCABULARY`) is
presentation — what a client groups a menu by. It is not the read/query classification, and no field
carries one.

The distinction exists in fact: `si.artifact.show` returns what is stored, `si.topology.impact`
computes a relationship over it. Nothing declares which is which, so nothing can enforce the second
half of IN-4 — that a *read* must not compute a relationship. An operation could quietly acquire a
derivation and no mechanism would object.

**Unimplemented, and cheaply.** The contract is the authority for everything else about an operation;
one declared field would put the classification where the rest of its identity already lives.

### 5.2 IN-8 — the invariant that shaped two operations

Worth recording because it is the map's clearest case of a normative requirement changing what was
built rather than describing it. `si.capability.surface` and `si.rule_set.list` both exist because
the answer was otherwise one join away in a client — the exact hazard Implementation Guidance §5
lists. `si.rule_set.list` in particular was added when a check needed the sealed rule set and the
alternative was for the caller to assemble it from `si.artifact.show`.

### 5.3 IN-11 — three of four

"What it contains", "what governs what" and "what it is" are answered. **"What it determined" is
not, from the read surface.** Determinations are carried in `evidence/<domain>/` and in the
composition conformance result, and no `si.` operation publishes either; they are read by opening
the files. Under IN-13 that is a read path outside the surface (§5.5), and under IN-11 it is a
question the surface cannot answer.

### 5.4 IN-12 — reachability is currently permission

Every contract declares `context_requirements: []`, reserved and inert. Whether a read may proceed
is therefore determined by whether the caller can reach the surface — which IN-12 names exactly as
what must not constitute permission.

This is unimplemented rather than unimplementable: the field exists, the boundary evaluates
declared input contracts before reaching a handler, and the governance to evaluate is declarable.
What is absent is any determination on the path.

### 5.5 IN-13, IN-14 — the surface is not the only path

IN-13 requires that no read path exist outside the declared operations. Several do. The snapshot is
a directory of JSON; `protocol_runtime examine`, the assembler's own verification, the transformation
compiler's `design/sealed.py`, and every check in `.github/process/` read it directly. Each is a
legitimate consumer, and each is a path.

**Ruled: `5b` settles it and the scope is broad.** §2 names "a tool that happens to read files" as
not exempt; §12 says a side channel opened for observation is an ungoverned read path. IN-14 bounds
it — inspection cannot be performed against an unsealed representation, so construction reading its
own in-flight state is outside `5b` entirely, and acceptance (`3b` §7) is a determination *about* a
snapshot rather than a question asked *of* it.

Under that reading the direct readers separate cleanly:

| Reader | Disposition |
|---|---|
| `s8_verify` reading what it materialized | pre-seal — Part IV, not inspection |
| `verify_snapshot`, `warm_boot` | acceptance under `3b` §7 |
| `transformation/design/sealed.py` | **compliant** — routes through `si.artifact.show` |
| `protocol_runtime examine` | **violation** — its own locator/parser/reporter over a sealed snapshot |
| `.github/process/frontmatter_fidelity.py` | **violation** — reads `snapshot/` directly |

`runtime examine` is the larger of the two: it is a whole read surface answering questions about a
sealed snapshot to a person, and it should be expressed as `si.` operations.

IN-14 inherits the same question. Every `si.` operation reads a sealed root, so the read surface
satisfies it; the direct readers above include ones that read pre-seal material by design — the
compiler's own verification stages read what has not been sealed yet, correctly. If those are read
paths under IN-13, IN-14 is violated by them; if they are not, both are satisfied. One ruling settles
both.

## 6. Projection — PJ-1 … PJ-12

The realization derives **six** projections from one source. `compiler/stages/s6_project.py` states
the arrangement in its own words: "Each projection is a deterministic derivation of the Graph — the
sole semantic authority. **No projection derives from another projection.**" The six are `canonical`,
`vocabulary`, `tokenized`, `evidence`, `dispatch` and `handlers`; each is a module under
`compiler/projections/`, each returns content plus a trace of `TraceEvent`s, and `s7_materialize`
writes them with a sibling `metadata.json`.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **PJ-1** defined source, declared derivation | the Graph is the sole source, stated in `s6_project`; the derivation is a named module per projection | Partial — §6.1 |
| **PJ-2** deterministic, consults nothing but its source | each generator takes `state.graph` and nothing else — no clock, no environment, no prior projection; a clean rebuild reproduces every projection hash | Demonstrated |
| **PJ-3** governed by a projection contract stating source, selection, derivation | — | Unimplemented — §6.1 |
| **PJ-4** makes no claim its source does not entail | `s8_verify::_verify_tokenized_integrity` resolves every projected node and edge back into `graph.reverse_table`; `_verify_canonical_references` does the same for canonical | Partial — §6.2 |
| **PJ-5** no default, no ambiguity resolved, refuse where the source does not determine | the fail-hard doctrine; `s6` generators raise rather than substitute | Partial — §6.2 |
| **PJ-6** omits nothing its contract declares | no contract exists, so no declared carriage can be omitted | Vacuous — §6.1 |
| **PJ-7** source governs where they disagree | the Graph is rebuilt from declarations every compile; no stage writes back into it from a projection | Demonstrated |
| **PJ-8** nothing authored into a projection; never edited | — | Unimplemented — §6.3 |
| **PJ-9** regenerable from its source | a clean rebuild of the platform and every domain reproduces every projection hash and the snapshot identity | Demonstrated |
| **PJ-10** carries provenance identifying source and derivation | each `metadata.json` carries `projection_type`, `projection_class`, `graph_address_hash`, `graph_topology_hash`, `compiler_version`, `structure_id` | Demonstrated |
| **PJ-11** derivation confers no authority | governance reads artifacts, never projections; `s4_govern` runs before `s6_project` and cannot see one | Demonstrated |
| **PJ-12** projections of one source entail no contradiction | tokenized metadata carries `vocabulary_hash`, tying two projections to one build | Partial — §6.4 |

### 6.1 PJ-1, PJ-3, PJ-6 — the derivation is code, and there is no contract

**The source is declared and the derivation is not.** That the Graph is the sole source is stated
plainly and enforced by construction — a generator receives `state.graph` and has nothing else to
consult. What is absent is the other half of PJ-1 and the whole of PJ-3: **no projection contract
exists.** There is no `PROJECTION` artifact kind, no governed declaration of what a projection
carries, and no statement of selection anywhere outside the Python that performs it.

`4b` §3.1 states exactly what this costs, and the realization is the illustration: *"Without it, an
absent element is ambiguous between deliberately not projected and lost, and no examination can tell
which."* Six projections are lossy by design and nothing declares what each one drops. PJ-6 has no
subject in consequence — a projection that declares no carriage cannot omit what it declared — so
the invariant is vacuous rather than satisfied, which is the weaker result of the two.

**Unimplemented, and the shape of the fix is already present elsewhere.** The inspection surface
solved the same problem: `si.` operations were once implementations with metadata in code, and
`TI_SI_*_V0` contracts moved the declaration into governed artifacts where "adding, renaming or
re-pointing an operation is an authoring act … it cannot happen silently in code." A projection
contract is that move, applied to `compiler/projections/`.

### 6.2 PJ-4, PJ-5 — faithfulness is checked for two projections of six

`4b` §14 is explicit that **faithfulness is established by regeneration, not by inspection**, and
regeneration is demonstrated (PJ-9). What the realization additionally has is structural
verification, and its coverage is uneven. `s8_verify::_verify_roundtrip` gates on
`projection_class`, verifying only `CANONICAL_ARTIFACT` files and skipping every other class with
the comment that they "have dedicated structural checks elsewhere." Two do —
`_verify_tokenized_integrity` and `_verify_evidence_integrity`. **`dispatch`, `handlers`, and the
vocabulary lookup tables have no dedicated check**, and `forward.json` / `reverse.json` are skipped
by name rather than by class, which the same function elsewhere calls out as the ad-hoc pattern it
replaced.

That matters more for `dispatch` and `handlers` than for the rest: they are what the runtime reads
to route execution, so an unfaithful claim in either is a behavioral claim nothing derived.

PJ-5's refusal requirement holds by the fail-hard doctrine rather than by a mechanism — the same
class as GC-7, and recorded here for the same reason.

### 6.3 PJ-8 — the same gap as SN-1, one level down

Nothing prevents or detects a projection edited in place. This is SN-1's finding restated at the
constituent level, and the two close together: an acceptance check that recomputed each projection
hash from content (finding 2) would detect an edited projection as a side effect.

### 6.4 PJ-12 — consistency is by construction, not by check

All six projections derive from one Graph in one pass, so they cannot disagree about a build. That
is a strong guarantee and it is not the invariant: PJ-12 is a property of the projections **as
carried**, and once carried, nothing rechecks that they still agree. `_verify_copies_agree` compares
copies of one *identity* across domains, which is GC-12 and a different relation.

## 7. Evidence, Attestation & Provenance — EV-1 … EV-16

**The realization's `snapshot/evidence/` is not evidence in this document's sense.** It carries
`nodes`, `edges`, `event_catalog` and declares `projection_class: evidence_substrate` — it is a
*projection of what the system could evidence*, which `4b` §10 names as an evidence view. It records
no determination. Actual records live in two other places: **construction** attests through
`trust/<domain>/structure_attestation.json`, and **execution** writes a JSONL trace through
`runtime/evidence.py::TraceWriter`. The name collision is worth stating first because it makes the
map read as better-covered than it is.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **EV-1** evidence establishes closure, rules, predicate results, consequence, resulting state; execution additionally its path | the trace records the path — `wf_start`, `cc_start`, `cc_step`, `cc_complete`, `wf_complete`, each with addresses and `result_status` | Partial — §7.1 |
| **EV-2** produced as the determination is made, never reconstructed | `TraceWriter._emit` writes and flushes per event, inline with execution | Demonstrated |
| **EV-3** refusals evidenced as fully as admissions | at runtime, `TraceWriter.error` records a failure into the trace | Partial — §7.2 |
| **EV-4** evidence is never an input to a determination | nothing reads a trace back; the runtime opens a trace write-only and no stage or handler consults `traces/` | Demonstrated |
| **EV-5** determinative and observational content distinguished, and the distinction declared | — | Unimplemented — §7.3 |
| **EV-6** determinative content identical across the same `(S, π, C)` | the differential and e2e harnesses compare rule outcomes across runs; nothing compares trace content | Partial — §7.3 |
| **EV-7** observational content participates in no determination | no handler reads `ts_ns` or a trace id | Demonstrated |
| **EV-8** attestation identifies party, subject, property | subject `structure_id` and property `tokenized_projection_hash` are carried; the party is not | Partial — §7.4 |
| **EV-9** an attestation is not treated as establishing truth | the assembler independently recomputes the governance closure rather than accepting the attestation's word — `_verify_governance_provenance` | Demonstrated |
| **EV-10** an attestation chain terminates in a nameable trust root | — | Unimplemented — §7.4 |
| **EV-11** attestation confers no authority or admissibility | `s9_attest` runs after `s8_verify`; no stage reads an attestation to admit anything | Demonstrated |
| **EV-12** every derived element carries provenance identifying source and derivation | projection `metadata.json`; the attestation's `imported_governance` naming the closure a domain was compiled against | Demonstrated |
| **EV-13** provenance confers no authority and establishes no correctness | `imported_governance` is used to *refuse* a stale domain, never to accept one | Demonstrated |
| **EV-14** none of the three is a source of governance authority | governance reads artifacts only | Demonstrated |
| **EV-15** snapshot, evidence, attestation and actor identities separately determinable | `snapshot_id`, `trace_id`, `attestation_hash` are distinct; actor is carried on `wf_start` | Partial — §7.5 |
| **EV-16** checkable without access to, or trust in, the producer | — | Unimplemented — §7.4 |

### 7.1 EV-1 — the path is evidenced; the determination is not

The trace establishes **what happened**: which workflow, which capability contract, which step, what
each step returned, in order. That satisfies the execution clause — the path can be checked against
the sealed representation.

It does not establish the five points of §3.1. **Which closure applied, which rules that closure
supplied, and what each predicate yielded are absent from the record.** A reader of a trace learns
that a step returned `result_status`; they cannot learn what governed that step or why the outcome
was the one permitted. `3e` §3.1 states the consequence directly: evidence recording outcomes
without the closure and rules that produced them "establishes that something happened, not that it
was governed — and those are the two things the family exists to separate."

**This is the map's confirmation of AI-14 as a real gap**, and it is narrower than the document-level
comparison suggested: the runtime evidences its path faithfully and evidences no determination.

### 7.2 EV-3 — construction refuses without evidence

At runtime a refusal is traced. **At construction it is not.** `compiler/cli.py` catches
`CompilerError`, writes a message to stderr, increments a failure count and exits 1. Nothing is
recorded. The determination "this candidate is inadmissible under this closure" — the exact subject
of §3.3 — leaves no checkable record anywhere.

**This is not GC-6 in tension with EV-3.** GC-6 forbids *usable output* from a refused construction;
an evidence record of the refusal is not usable output, and `3e` §3.3 requires it to establish "what
was proposed, what refused it, under what closure and authority, and that nothing proceeded." The
realization produces a diagnostic for a human reader and treats the two requirements as one.

`4a` §5 lists attestation as the ninth obligation and evidence nowhere, which is consistent with
this: the realization's construction was built to attest a success, not to evidence a determination.

### 7.3 EV-5, EV-6 — the distinction this document exists to settle is undeclared

`3e` §5 says of itself that it settles what earlier documents left open. **The realization does not
carry the distinction at all.** A trace event is a flat record:

```
trace_schema_version, trace_id, event_type, domain, wf_addr, cc_addr,
step_addr, step_op, result_status, detail, ts_ns
```

`ts_ns` is observational; `wf_addr`, `step_op` and `result_status` are determinative; `detail` is
whichever the caller put in it. Nothing declares which is which, so **EV-6 cannot be checked even in
principle** — a checker comparing two traces of one transition fails on `ts_ns` and on `trace_id`,
whose generator is documented as "not purely deterministic (timestamp advances each call)."

`3e` §5.2 describes precisely the three ways a checker then fails, and the realization has no way to
avoid all three. **This is the sharpest finding in `3e`** and the one with the widest reach: EV-6,
EV-16 and SN-11 all depend on it, and none can be demonstrated until it exists.

### 7.4 EV-8, EV-10, EV-16 — the attestation names no party

```json
"public_key_ref":    "STUB",
"signature":         "STUB_NOT_CRYPTOGRAPHICALLY_SIGNED",
"signing_algorithm": "STUB"
```

The attestation identifies its subject and its asserted property and **does not identify the
attesting party**. EV-8 is therefore two-thirds satisfied by a record whose remaining third is a
literal placeholder.

EV-10 follows: a chain that names no party terminates in nothing, and no trust root is nameable.
`3e` §6.2 requires that a system "be able to state what its chains terminate in," on the grounds
that "a trust root that cannot be named is being relied upon without being acknowledged." Here it is
acknowledged — by the string `STUB` — which is more honest than most and still not a root.

EV-16 is the consequence rather than a separate gap. A party with no access to the producer can
recompute the composite hash and the governance closure, which is real; they cannot establish who
vouched for anything, and they cannot compare determinative content (§7.3). **The realization is
independently checkable for integrity and not for determination.**

### 7.5 EV-15 — three of four identities are distinct

`snapshot_id`, `attestation_hash` and `trace_id` are separately determinable and never substituted.
The fourth is thinner: actor is an optional argument on `wf_start` and is absent from every other
event, so a determination made partway through an execution carries no actor identity. That is
enough to satisfy "separately determinable" and not enough to reach `3e` §9's point — that naming
who acted says nothing about entitlement — because for most events nobody is named.

## 8. Identity & Addressing — ID-1 … ID-15

The realization identifies artifacts by a fully qualified name declared in the machine block:
`<namespace>::<CODE>`. `s1_extract._resolve_identity` is unambiguous about the direction — *"The
filesystem location has no semantic authority over identity. Path derivation is fully retired:
identity is the artifact's own declaration"* — and an artifact declaring no `fqdn` is refused with
`E104_INVALID_FQDN`.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **ID-1** declared, authoritative over filename, path, containment, position, convention, discovery | `_resolve_identity` reads the declared `fqdn`; `artifact_kind` in the machine block is "the SOLE authoritative discriminator … the filename prefix is a naming convention only" | Partial — §8.2 |
| **ID-2** nothing acquires identity by being found | a discovered file with no declared `fqdn` is refused, not named after itself | Demonstrated |
| **ID-3** identity over the semantic object; meaning-preserving representation change does not alter it | `s2_canonicalize` establishes the normal form over which identity is determined | Demonstrated |
| **ID-4** two admitted things bearing one identity refused | `INVARIANT_UNIQUE_ARTIFACT_ID_V0` — "each fqdn_id must be unique across compilation graph" | Demonstrated |
| **ID-5** a change of declared semantics is a new identity | the `_V<n>` suffix is part of the declared FQDN, so a version is a distinct identity | Demonstrated |
| **ID-6** identity carries no ordering; supersession is declared | `superseded_by` is a declared relation; nothing derives order from `_V<n>` | Demonstrated |
| **ID-7** an address is not an assertion of identity | — | Partial — §8.3 |
| **ID-8** a change of address does not change identity | identity survives relocation; **admission does not** | Partial — §8.1 |
| **ID-9** identity is not derived from an address | path derivation is retired, by name, in the function that would do it | Demonstrated |
| **ID-10** resolution assigns, alters, normalizes or completes no identity | `s3_semantic_addressing` allocates addresses over declared identities and writes none back | Demonstrated |
| **ID-11** a resolved thing whose declared identity differs from what was expected is refused | — | Violated — §8.3 |
| **ID-12** a namespace establishes no authority, concern or federation, and encodes none alongside identity | — | Violated — §8.4 |
| **ID-13** references by declared identity; resolution completes before dependents | references are FQDNs; `s3` completes before `s4`, `s5` and `s6` | Demonstrated |
| **ID-14** resolution does not search, select among candidates, or fall back | — | Violated — §8.3 |
| **ID-15** composite identity derived from constituents' identities, changing when any changes | `compute_composite_hash` over `_identity_view` | Partial — §8.5 |

### 8.1 ID-8 and the relocation test — run, not reasoned

`4c` §10 gives the settling test: *"Move a governed thing — change its path, its container, its
address, the order in which it is encountered — and nothing about its identity, its governance, or
the composite identity of anything containing it may change."*

**The test was run** (§29.2). The realization passes it for identity and fails it for composite
identity, by a mechanism narrower and more concrete than reading suggested.

**What holds.** Moving `WF_COLLATZ_CONJECTURE_V0.md` from `registry/workflows/` to
`registry/intents/`, with the filename and every declaration untouched, leaves `fqdn_id` unchanged,
`content_hash` unchanged, and the graph address hash, graph topology hash, tokenized projection hash
and attestation hash **byte-identical**. Identity is declared, and the semantic layer is genuinely
insensitive to location. The canonical artifact is even written to the same output path, because that
path is derived from the artifact's kind rather than from where its source sat.

**What fails.** The canonical projection hash **changes**, because the canonical artifact carries a
`module_path` field derived from the source directory:

```
module_path   workload.registry.workflows   →   workload.registry.intents
```

`_identity_view` includes `canonical_projection_hash` — deliberately, per its own docstring, so that
a STRUCTURE artifact cannot change inside a sealed snapshot without the identity moving. The
consequence is that **a pure relocation changes the composite identity of the snapshot containing
it**, which is exactly the clause `4c` §10 names last.

**The changed hash is the symptom. `module_path` is the defect, and it is larger than a hash.**

### 8.1.0 Governance follows directory location

`module_path` is not diagnostic. Two consumers derive a **governed ownership fact** from it by
splitting on `.` and taking the third segment:

| Consumer | What it derives | What it does with it |
|---|---|---|
| `projections/artifact_index.py::_owner_subdomain` | `owner_subdomain` on every index entry | published to the read surface |
| `assertions/handlers/assert_rb_storage_subdomain_owned_v0.py::_owning_subdomain` | the subdomain owning a runtime binding | **refuses** a binding describing another subdomain's storage |

So a governance determination — whether this binding may describe that storage — is made from the
directory an artifact's source file sits in. `4c` §4.1 names this failure and its consequence in one
sentence: *"governance follows identity — so a thing whose identity changed by being moved has
silently changed what governs it, with no determination anywhere recording the change."* Here it is
one step more direct: governance follows **location**, without passing through identity at all.

**The realization has already ruled on this, in the opposite direction, in a comment:**

> `owner_subdomain` … IMMUTABLE once emitted: it is a pure function of `module_path` … re-homing to
> another subdomain changes `module_path` and therefore **requires a NEW version**.

That is a deliberate, coherent design position — ownership is declared by module organization, and
moving a thing is a semantic change requiring a new version. It is also the exact inverse of `4c`
§4.1: *"A change of identity requires a governed determination, never a change of location."* The
standard and the realization disagree about a settled question, and under `0z` §3 the document
governs and the disagreement is resolved by ruling.

**It is also a `4b` violation, and the more serious of the two.** No artifact declares a subdomain.
`owner_subdomain` is therefore a claim the projection's source does not entail — PJ-4 — and `4b`
§4.2 describes precisely what makes it dangerous: *"a declaration that nobody authored and no closure
admitted — reaching consumers as though it were derived fact … the added meaning arrives with the
authority of everything around it."* It reaches a consumer with authority: an assertion handler that
refuses on it.

`_owner_subdomain`'s docstring says it reads the path "with zero inference," which is true of the
parse and not of the fact. The parse is total; the fact was never declared.

**Removing `module_path` from the canonical projection is therefore not the fix**, and would break
two live consumers. The question the finding poses is whether subdomain ownership should be
**declared in the machine block** — where MB-1 says every determining fact already belongs. That is
`2c`'s subject and is flagged for it.

### 8.1.1 The silent-drop hazard is real and currently unreachable

A second reading of `s1_extract` suggested a sharper failure: discovery is `root_path.rglob("*.md")`
filtered by a `filename_pattern`, and a file whose name does not match is `continue`d silently, with
no diagnostic. Renaming an artifact out of the pattern would then drop it from the composition with
its identity intact and nothing refusing.

**Probed, and it does not happen** (§29.3). Renaming `CT_PURE_TERMINATION_CHECK_V0.md` to
`ct_pure_termination_check.md` is refused at `S2_CANONICALIZE`:

```
E104_INVALID_FQDN: Dangling reference: workload::CC_VERIFY_TERMINATION_V0
    → workload::CT_PURE_TERMINATION_CHECK_V0 (target not found in graph or imported surface)
```

Referential closure catches it. And it catches every case available to test: **every artifact in the
workload is referenced by at least one other**, and every platform invariant is named by its
constitution — which is the relation `governance_chain_closure.py` exists to prove.

So the silent `continue` is a **latent hazard rather than a live defect**, and the condition that
would expose it is nameable: an artifact class that nothing references. The realization currently has
none, and the check that keeps it that way is a different check from the one that would catch the
rename. Recorded here so that admitting such a class is recognized as removing a guard.

### 8.2 ID-1 — the prefix is doctrine in one place and authority in another

`s1_extract` states the rule correctly at line 722 and breaks it at line 500. Resolving imported
capabilities, it decides an artifact's kind by splitting the identifier:

```python
if artifact_code.split("_")[0] not in ("CS", "CT"):
    continue   # only capabilities are carried
```

That is a kind determination read from a naming convention — the fifth row of `4c` §2.1's table,
*"a convention describes; it does not constitute."* The consequence is bounded (the branch selects
what to carry, and a mis-split skips rather than mis-types) and the mechanism is exactly the one the
same file declares non-authoritative twenty lines of doctrine later.

### 8.3 ID-7, ID-11, ID-14 — resolution searches, selects, and falls back

The same block is the map's clearest violation, and it breaches three invariants in four lines:

```python
matches = list(canon_root.rglob(fqdn.replace("::", "__") + ".json"))
if not matches:
    continue          # not a compiled imported capability — leave to S2 tolerance
raw = json.loads(matches[0].read_text(encoding="utf-8"))
```

- **It searches.** `rglob` walks the tree looking for a filename derived from the identity. ID-14:
  "Resolution MUST NOT search."
- **It selects among candidates.** `matches[0]` takes the first of a list that may hold several,
  with no comparison and no refusal. ID-14: "no best match, no most likely candidate."
- **It falls back.** No match `continue`s to a downstream tolerance rather than refusing. ID-14 and
  AI-6 both forbid it; `4c` §6 states that an unresolvable reference "means something references a
  thing that is not in the system."
- **It never checks what it found.** The file's own declared `fqdn` is not compared against the one
  searched for, so a file whose name matches and whose declaration does not is accepted. That is
  ID-11, and it is what makes the address an assertion of identity here — ID-7.

**Deriving the address from the identity is not the problem** — ID-9 forbids the reverse direction
and is satisfied. The problem is that the derived address is then trusted, searched for, and
resolved to whatever turns up first.

### 8.4 ID-12 — the standing namespace violation, stated in this document's terms

Every artifact declares a namespace of the form `fb.<concern>`, where `fb` denotes a federation
boundary. ID-12 forbids exactly this: a namespace "MUST NOT establish authority, concern, or
federation, and MUST NOT encode them alongside identity," because "an identifier that carries two of
these makes them indistinguishable to any check, whatever is declared elsewhere."

The realization's own analysis reached the same conclusion independently and by a different route —
applying the federation constitution's test to all 26 declared boundaries and finding no survivor.
**The map adds one thing to that record: the reason no predicate can currently be written.** ID-12's
final clause is the operative one — a check cannot distinguish an unlisted namespace from an
illegitimate one while both are the same string.

This is a ruled finding already, so it is recorded here rather than reopened.

### 8.5 ID-15 — the composite is a function of five values per domain

Demonstrated for what `_identity_view` covers and failing ID-15's second clause for what it does
not. This is finding 1 seen from `4c`: a composite identity that does not change when a constituent
changes is not a composite identity over those constituents. The two documents state the same
requirement — SN-2's totality clause and ID-15's "MUST change when any constituent changes" — and
the realization satisfies neither for the six constituents outside the view.

## 9. Architectural Invariants — AI-1 … AI-17

`1c` states what must remain true of any realization, and its entries carry a **Shown by** clause
naming the observable signature of a breach. That makes it the one document where the map can record
what was *looked for* as well as what was found.

Most of AI-1…17 are restated by the documents already mapped and are not re-derived here; this
section records the four the plan asks about, plus the three whose signature was checked directly.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **AI-4** determination precedes effect | at construction, `s4_govern` completes before `s7_materialize` writes; at runtime, the one live determination — the reach read-only check in `dispatcher._execute_cs_step` — returns `VIOLATION` **before** the capability runs | Demonstrated — §9.1 |
| **AI-6** absence is not permission | `s4_govern` raises `E702_UNKNOWN_ASSERT` when an obligation resolves to no handler and `E701` when a handler raises; both fail the build. An unresolvable governing element is never an empty one | Demonstrated |
| **AI-7** refusal dominates | violations from every assertion accumulate into one error list, and any error fails the build. There is no combination step at which an allowance could outrank a refusal | Demonstrated — §9.2 |
| **AI-8** refusal leaves no residue | the pipeline aborts before the writing stage — **but** `1c` carves out "except for the evidence that it was refused," and that evidence does not exist (§7.2) | Partial — §9.3 |
| **AI-12** nothing enters by discovery | statically imported handler registry; environment-provisioned roots; no reflective loading | Demonstrated |
| **AI-14** every determination is evidenced | runtime path only | Partial — §7.1, §7.2 |
| **AI-16** evidence checkable without its producer | integrity yes, determination no | Partial — §7.4 |

### 9.1 AI-4 — satisfied largely by having moved determination out of runtime

The realization satisfies AI-4 mostly by architecture rather than by ordering: nearly every
determination happens at construction and is sealed, so at execution there is almost nothing left to
determine and therefore almost no ordering to get wrong. That is a legitimate way to hold the
invariant and it is worth naming, because it means **AI-4's failure mode is barely reachable here** —
a system with no runtime determinations cannot apply one late.

The one runtime determination that does exist is correctly ordered, and the code states the reason
in the same terms the invariant does:

> Refused before the capability runs, because a write that has happened cannot be unhappened.

### 9.2 AI-7 — held, and held trivially

Every assertion handler returns `violations`; none returns a permission. The determination is
"admitted unless something refused," so combining consequences permissively — AI-7's stated failure
mode — has no mechanism through which to occur.

**This is a real property obtained by a design choice, not a demonstration that the invariant is
enforced.** A realization whose rules could admit would need the combination rule AI-7 states; this
one has no such rule because it has no such rules. Recorded so that admitting a permitting rule is
recognized as requiring the combination semantics along with it.

### 9.3 AI-8 — the carve-out is the part that fails

`1c` states the invariant with one exception: after refusal the governed state is as though the
proposal had not been made, **"except for the evidence that it was refused."** The realization holds
the rule and drops the exception. A refused construction leaves no residue *and no evidence* (§7.2),
which satisfies the clause about state and defeats what the exception exists to preserve.

## 10. Governance Semantic Ontology — GO-1 … GO-12

The realization classifies its kinds in `compiler/governance_engine/artifact_kinds.py`, which cites
this document by section: `semantic_category` is annotated *"Governance Ontology §4 primary
category; None = kind not authorized"*, and `runtime_disposition` *"Ontology §7 — derived from the
category, never stored."* Twenty-one kind descriptors carry the classification:

```
semantic_category   Operational 5 · Contractual 4 · Normative 3 · Definitional 2
                    Evidential 1 · Participatory 1 · None 5 (kind not authorized)
provenance          authored 15 · derived 1 · None 5
```

| Invariant | Where demonstrated | Class |
|---|---|---|
| **GO-1** exactly one primary semantic category | one `semantic_category` per descriptor, single-valued, no kind carrying two | Partial — §10.1 |
| **GO-2** exactly one provenance, unchanged by later representation | `provenance` per descriptor; ASSERT is the one `derived` kind, and `s4_govern` records its source invariant | Partial — §10.2 |
| **GO-3** a kind declares its category and provenance constraint; neither inferred from name, location or content | declared per kind — **in code** | Partial — §10.1 |
| **GO-4** a secondary relationship does not alter the primary category | `governed_by` and `superseded_by` are edges; neither writes back a category | Demonstrated |
| **GO-5** no declarations violate the category contract | — | Unimplemented — §10.3 |
| **GO-6** an evidential element is not referenced as a source of authority | `s4_govern` runs before evidence exists; no handler reads an attestation or trace | Demonstrated |
| **GO-7** a participatory element carries no behavior and its identity is not authority | ACTOR is the one Participatory kind; it declares attributes and no steps | Demonstrated |
| **GO-8** an operational element is not a source of authority | governance reads INVARIANT and CONSTITUTION only | Demonstrated |
| **GO-9** derived and produced elements are not authority sources and carry provenance | ASSERT is derived from its invariant and is never itself cited as governing | Demonstrated |
| **GO-10** a category does not establish, extend or limit what an element governs | `runtime_disposition` derives from category and governs topology participation, never jurisdiction | Demonstrated |
| **GO-11** authority, concern, federation and namespace not in one identifier | — | **Violated** — §8.4 |
| **GO-12** admitting a kind requires no ontology revision | adding a descriptor is a registry entry; the category vocabulary is untouched | Demonstrated |

### 10.1 GO-1, GO-3 — the classification is real and lives in code

This is the fourth instance of the map's recurring shape, and the most defensible of them. The
classification exists, is single-valued, cites the document it implements, and refuses an
unauthorized kind by carrying `None`. What it is not is a **declaration**: no artifact and no
governed registry states a kind's category, so GO-3's requirement that a kind *declare* its category
is met by a Python module rather than by a declaration surface.

Whether that satisfies GO-3 depends on whether "a kind declares" means the kind contract as authored
or the kind contract as realized — and `2c` MB-1 answers it for the realization's own terms (§11.1).

### 10.2 GO-2 — provenance is per kind, not per element

GO-2 is about **elements**: every semantic element has exactly one provenance. The realization
declares provenance **per kind** — every ACTOR is `authored`, the one ASSERT kind is `derived`.
That is a sound default and it is not the invariant: an element authored by a generator and an
element authored by hand carry the same kind and therefore the same recorded provenance.

The realization knows the difference and enforces it elsewhere — `emit_rule_sets --check` and
`author_transport_contracts --check` both exist because generated artifacts must not be hand-edited
— but that knowledge is in a script, not in the element's provenance.

### 10.3 GO-5 — category contracts are not checked

Each category carries a contract in `2b` §4 — what an element of that category may and may not do.
Nothing evaluates an artifact against its category's contract; the prohibitions that *are* enforced
(GO-6 … GO-9) hold because of how the pipeline is arranged rather than because a check reads a
category and applies its contract. Unimplemented, and the shape of the fix is an assertion per
category rather than per kind.

**One place the realization has decided a question this document leaves open.** `2b` §11 records as
deliberately open whether **Evidential** is a peer semantic category. The kind registry already
carries `Evidential` as one, applied to one kind. That is a realization committing to an answer the
standard has parked — harmless today, and exactly the material `0z` §5.1 says may occasion a
revision. Recorded rather than ruled.

## 11. Machine Block — MB-1 … MB-14

The machine block is the fenced `yaml` region of each artifact, parsed by `s1_extract` and validated
against a per-kind JSON schema in `software_governance/registry/schema/`. It is the realization's
declaration surface and, by MB-1, is meant to be the only thing that determines anything.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **MB-1** exactly one bounded declaration surface; nothing outside it determines anything | one fenced block per artifact, parsed once | **Violated** — §11.1 |
| **MB-2** meaning does not depend on location, surroundings, or serialized form | — | **Violated** — §11.1, §11.2 |
| **MB-3** equality and identity over the semantic object; integrity over a **canonical form** of it | — | **Violated, proved** — §11.2 |
| **MB-4** every declaration element has exactly one semantic owner | schema per kind owns its properties; no property is defined by two schemas | Demonstrated |
| **MB-5** the universal envelope is closed; a kind does not redefine or extend it | `fqdn`, `artifact_kind`, `version`, `governed_by` are read by `s1_extract` from every kind alike | Demonstrated |
| **MB-6** identity declared, authoritative over position, not derived from name or location | `_resolve_identity` — "path derivation is fully retired" | Demonstrated |
| **MB-7** identity, authority and concern separately expressible | — | **Violated** — §8.4 |
| **MB-8** exactly one artifact kind per block, never inferred | `artifact_kind` is "the SOLE authoritative discriminator … the filename prefix is a naming convention only" | Partial — §8.2 |
| **MB-9** an unregistered kind is refused | `REGISTRY.node_kind_for_kind` returns `None` → `E103_TYPE_MISMATCH`; a kind carrying no `semantic_category` is "not authorized" | Demonstrated |
| **MB-10** a kind declares whether governance assertion is required for ordinary use | `governed_by` is declared by 163 artifacts | Partial — §11.3 |
| **MB-11** every surface closed; no surface admits undeclared elements | 19 of 24 schemas set `additionalProperties: false` | Partial — §11.3 |
| **MB-12** every normative declaration element carries a semantic role and a construction disposition | `disposition` is declared per **kind**, not per element | Partial — §11.4 |
| **MB-13** every semantic element of a sealed representation has declared provenance | projection `metadata.json`, `imported_governance`, and the ASSERT derivation cover most of it | Partial — §11.4 |
| **MB-14** admitting a kind requires no amendment to this document | a kind is a registry descriptor plus a schema | Demonstrated |

### 11.1 MB-1 — the invariant that adjudicates findings 6, 8, 12 and 19

MB-1 is the reason `2c` was taken next, and it answers all four the same way:

> An artifact MUST have exactly one bounded declaration surface, and **nothing outside it MUST
> determine anything about the artifact.**

- **Finding 19 is a breach, not a gap.** `owner_subdomain` is determined by the source directory, and
  a directory is outside the declaration surface. It then refuses a runtime binding. Something
  outside the machine block determines something about the artifact and refuses on the result. `2e`
  CA-8 says it a third way — *"containment MUST NOT carry governance of itself."*
- **Findings 6, 8 and 12 are gaps, not breaches.** A projection contract, a read/query class, and a
  determinative/observational split are all absent from the declaration surface — but nothing outside
  it is determining them either. They are undeclared, not externally determined. MB-1 is silent on
  material that no surface carries; it prohibits a *second* surface, not an empty one.

That distinction matters for what each costs. Findings 6, 8 and 12 are additions to a surface.
Finding 19 is the removal of a second, undeclared one — and the realization's stated position
(§8.1.0) has to be overturned first.

**Discovery is the same breach at a different scale.** Admission is decided by a filename matching
`filename_pattern`, and `artifact_code` is assembled from the filename's captured groups. The
realization contains the doctrine and the breach in one file: `s1_extract:722` says "the filename
prefix is a naming convention only" twenty lines after `s1_extract:500` reads a kind out of it.

### 11.2 MB-3 — integrity is computed over the serialization, not over the semantic object

**Proved by probe** (§29.4). MB-3 requires integrity over *a canonical form of the semantic object*.
`s1_extract:717` computes it over the raw file text:

```python
content_hash = hashlib.sha256(content_raw.encode("utf-8")).hexdigest()
```

Swapping two sibling keys in a machine block — a YAML mapping is unordered, so the parsed object is
unchanged — was recompiled and compared:

```
frontmatter (the parsed semantic object)   SAME
content_hash                               CHANGED
graph_topology_hash                        CHANGED
canonical_projection_hash                  CHANGED   →  composite snapshot identity moves
```

`4c` ID-3 and `2d` KV-8 state the same requirement from their own subjects — a representation change
preserving meaning MUST NOT change identity — and all three fail together.

**This is the second independent way the composite identity moves while governed content does not.**
Finding 15 was *location*; this is *representation*. They share a cause: values that are properties
of a file rather than of a semantic object ride into a projection the identity covers.

**It also puts a false-positive under GC-12.** `_verify_copies_agree` compares copies of one identity
by `content_hash`; two copies differing only in whitespace would be reported as disagreeing when they
carry identical meaning.

### 11.3 MB-10, MB-11 — closure holds for most kinds and not for the ones that decide

Nineteen of twenty-four schemas close their top-level surface with `additionalProperties: false`, and
the diagnostic's own note is right that "for schema-closed kinds an unconsumed key cannot silently
survive." **Five do not close**, and the selection is unfortunate:

```
OPEN   SCHEMA_STRUCTURE_V0            the build-configuration authority
OPEN   SCHEMA_AUTHORITY_REGISTRY_V0   } the authority surface
OPEN   SCHEMA_AUTHORITY_STATE_V0      }
OPEN   SCHEMA_AUTHENTICATED_AUTHORITY_STATE_V0
OPEN   SCHEMA_TRACE_EVENT_V0          evidence records
```

STRUCTURE is the artifact that declares what may be admitted, which roots are searched, and the
filename pattern §11.1 turns on. The assembler's `_identity_view` docstring calls it "the
configuration authority for the whole system." Its surface is open.

**And two kinds have no schema at all.** `TRANSPORT_INGRESS` and `TRANSPORT_EGRESS` appear in no
schema file and in no `schema_index.json` entry, so the thirty-six `TI_`/`TE_` contracts carrying the
entire inspection read surface — input contracts, handler bindings, `context_requirements` — are
validated by no closed surface. This is why finding 8 (an undeclared read/query class) had nowhere
obvious to be declared: the kind has no schema to add it to.

MB-10 is partial for a related reason: `governed_by` is declared by 163 artifacts and nothing states,
per kind, whether a governance assertion is *required* for that kind's ordinary use. Omission is
therefore indistinguishable from a kind for which none is required — which MB-10's second sentence
exists to prevent.

### 11.4 MB-12, MB-13 — declared per kind, required per element

Both invariants quantify over **elements**; the realization declares over **kinds**. `disposition`
(EXECUTABLE / DECLARATIVE) is a descriptor field, so every element of a kind carries the same role
and the same construction disposition, and an element that differs from its kind's default has no way
to say so. Same shape as GO-2 (§10.2), and recorded separately because the fix differs: GO-2 needs a
provenance field per artifact, MB-12 needs role and disposition per declaration element.

MB-13 is the best-covered of the three. Every projection carries `graph_address_hash` and
`graph_topology_hash`; every domain attestation carries `imported_governance`; every ASSERT records
the invariant it derives from. What is uncovered is the material §3.2 already names — the indexes,
`behavior_logic/`, `conformance/` and `evidence/` — which carry no provenance and sit outside the
identity, finding 1 seen once more.

## 12. Governance Closure & Authority — CA-1 … CA-12

The realization's closure is the set of invariants and constitutions imported into a build, recorded
as `imported_governance` on each domain's attestation: an `import_domain`, a
`governance_closure_hash`, and a `closure_member_count` — 75 for the platform surface today.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **CA-1** authority, ownership, scope, concern, admission, inheritance and import separately determinable, none inferred from another | — | **Violated** — §12.2 |
| **CA-2** an authority exists by a declared constituting act, never by need, precedence, containment, naming or classification | each boundary declares a `CONSTITUTION_*`; **two declare none** | **Violated** — §12.2 |
| **CA-3** a purported authority answers all five questions of §3.2 from declared artifacts alone | applied to all 26 boundaries by the realization's own audit; **no survivor** | **Violated** — §12.2 |
| **CA-4** the authority constituting a jurisdiction distinguishable from the authority whose subjects it governs | `CONSTITUTION_GOVERNANCE_V0` declares itself "the root authority … supreme" while sitting as one boundary among peers | **Violated** — §12.2 |
| **CA-5** a delegation is declared, does not exceed its source, and does not transfer answerability | no delegation construct exists | Vacuous |
| **CA-6** a concern classification does not constitute an authority or a jurisdiction | `fb.<concern>` is exactly a concern classification constituting a boundary | **Violated** — §12.2 |
| **CA-7** a governing element declares its scope as a set of subjects; scope is never the absence of a boundary | `applies_to_kinds` on 88 invariants — a stated set, never empty-means-all | Partial — §12.1 |
| **CA-8** inheritance is declared; containment does not carry governance of itself | — | **Violated** — §11.1, §8.1.0 |
| **CA-9** import is declared by the receiving closure, enumerable, and does not extend the imported element's authority | `imported_governance.import_domain` is declared by the receiver; `closure_member_count` makes it enumerable | Demonstrated |
| **CA-10** a closure is fully established before any determination, and enumerable before evaluation | the closure is assembled, counted and hashed before `s4_govern` evaluates anything | Demonstrated — §12.1 |
| **CA-11** no governing element applies without having been established in the subject's closure | `_DOMAIN_INSTANTIATED` gates which kinds enter a domain build; an invariant outside the closure is never evaluated | Demonstrated |
| **CA-12** where a closure cannot be established the determination is `refuse`, distinguishable from a rule refusal | `E702_UNKNOWN_ASSERT` vs `E701_ASSERTION_FAILURE` | Partial — §13.3 |

### 12.1 CA-10 — the map's strongest single demonstration

CA-10 asks that a closure be established and enumerable *before* evaluation begins, and the
realization does more than satisfy it: it records the enumeration, hashes it, carries the hash in the
attestation, and **re-verifies it at assembly** — `_verify_governance_provenance` refuses a domain
compiled against a closure other than the one being assembled, naming the recorded member count and
the recomputed one.

That is a closure that is established, enumerable, recorded, and independently checkable. It is worth
naming plainly because most of this map is findings: **CA-10 is demonstrated better than the
invariant requires.**

CA-7 is partial for one reason only — scope is declared as a set of **kinds** rather than of
subjects. For the realization's purposes those coincide, and the invariant's actual prohibition
(scope as the absence of a boundary, or an unbounded assertion of everything) is not breached: two
boundaries do enumerate all 16 kinds, which is an unbounded assertion spelled out rather than
implied, and three declare no `applies_to_kinds` at all — the absence CA-7 names. Both are inside
finding 16's scope and are not counted twice.

### 12.2 CA-1 … CA-6 — the ruling the realization already reached, stated in this document's terms

The realization's `AUTHORITY_VS_CONCERN_RULING` applied the federation constitution's own test to all
26 declared boundaries and found no survivor. `2e` supplies the vocabulary for what that audit found,
and the correspondence is close enough to be worth setting out:

| The audit found | `2e` names it |
|---|---|
| 9 boundaries whose name **is** an artifact kind | CA-6 — a classification constituting a jurisdiction |
| 6 contesting one jurisdiction, 4 contesting the snapshot | CA-3 — §3.2's five questions unanswerable from declarations |
| 2 with no constituting act | CA-2 — authority not constituted by a declared act |
| 3 exercising no jurisdiction | CA-7 — scope as the absence of a boundary |
| `fb.governance` as root authority among peers | CA-4 — constituting authority not distinguished from governed subjects |

**The realization reached this independently and by a different route**, before these documents were
drafted, and recorded it as a ruled finding. The map adds two things: that `2e` names each variant
separately rather than as one modeling error, and that **CA-1 is the requirement Task B's step 2 has
to satisfy** — authority, ownership, scope, concern, admission, inheritance and import each
separately determinable. The current identifier carries at least three of the seven.

## 13. Enforcement & Refusal — EN-1 … EN-13

The realization's enforcement arrangement is 85 assertion handlers under
`compiler/governance_engine/assertions/handlers/`, each derived from a declared INVARIANT and
resolved through a closed registry keyed by the invariant's declared implementation module.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **EN-1** every obligation rendered as at least one assertion capable of refusing; a gap is a finding | `governance_closure.py` proves every compiler handler is named by an invariant; `implementation_closure.py` proves every named module is on disk | Partial — §13.1 |
| **EN-2** an assertion identifies its obligation | the ASSERT is derived from its INVARIANT by `s4_govern`; the handler's own `rule` field names the invariant FQDN | Demonstrated |
| **EN-3** an assertion imposes no consequence beyond its obligation and is no source of authority | handlers read artifacts and return violations; none writes, and none is consulted for admission | Demonstrated |
| **EN-4** where assertion and obligation differ, the obligation governs | — | Unimplemented — §13.1 |
| **EN-5** an assertion whose predicate can never refuse is a finding | — | **Violated** — §13.2 |
| **EN-6** an obligation evaluated at every determination whose closure supplies it | governance closure is recomputed per domain build and its digest verified by `_verify_governance_provenance` | Demonstrated |
| **EN-7** enforcement completes before the effect it governs | AI-4's mapping (§9.1) | Demonstrated |
| **EN-8** a refusal establishes what was proposed, what refused it, under what closure and authority, and that nothing proceeded | a `CompilerError` carries the assert code, the FQDN and the violations — to stderr, not to a record | Partial — §7.2 |
| **EN-9** rule refusal and closure failure distinguishable | `E701_ASSERTION_FAILURE` vs `E702_UNKNOWN_ASSERT` distinguish them by code | Partial — §13.3 |
| **EN-10** a refused proposal does not partly proceed, and no mechanism sets a refusal aside | the pipeline aborts; no override flag exists | Demonstrated |
| **EN-11** an obligation whose violation produces only a report MUST NOT be declared as governance | — | **Violated** — §13.2 |
| **EN-12** refusals evidenced as fully as admissions | — | Unimplemented — §7.2 |
| **EN-13** evidence is not an input to a determination | no handler reads a trace, an attestation, or a prior build's output | Demonstrated |

### 13.1 EN-1, EN-4 — coverage is proved in one direction

`governance_closure.py` proves that no handler exists without an invariant naming it. **EN-1 asks the
opposite question**: that every *obligation in force* has an assertion capable of refusing it. The
first prevents orphan mechanisms; the second prevents unenforced obligations, and only the first is
checked.

EN-4 has no mechanism at all: nothing compares what an assertion does against what its invariant
says, so a handler that has drifted from its obligation is indistinguishable from one that has not.
This is the same class as the `MACHINE_BLOCK_CLOSURE.md` defect the realization already carries —
prose about machine behavior with nothing checking that it still describes the machine.

### 13.2 EN-5 and EN-11 — one obligation that cannot refuse, declared as governance

`INVARIANT_CC_NO_UNUSED_OUTPUTS_V0` is declared as an INVARIANT — as governance — and its handler
cannot refuse its obligation. `assert_cc_no_unused_outputs_v0.py` returns:

```python
return {
    "assert_count": wf_count,
    "violations": [],   # No violations - warnings are not blocking
    "warnings": all_warnings,
    "status": "PASSED"  # PASSED with warnings
}
```

Its only `violations` path is a guard for missing compilation context — a **closure failure**, not a
refusal of the obligation. The obligation itself has no admissible input yielding refuse, which is
EN-5's definition of a finding, and it produces only a report while being declared as governance,
which is EN-11 stated exactly. The declared invariant carries `"severity": "WARNING"`.

**And its docstring states the deeper problem plainly:**

> Detects unused CC outputs as code smell indicator — Potential optimization opportunities

That is **adequacy, not admissibility**. `4a` GC-1 requires construction to determine admissibility
and *not* to determine adequacy, and §4 of this map records GC-1 as Demonstrated on the strength of
"no stage evaluates whether a candidate is good." **That entry is corrected here**: one of 85 does,
and its being non-blocking is why it went unnoticed — it evaluates goodness and then declines to act
on the answer, which is the least visible form of the breach.

**One instance in 85.** The scale matters for the ruling and not for the finding: EN-11 admits no
severity dimension, and an obligation that only reports is not governance whether one or many.

### 13.3 EN-9 — distinguishable by code, conflated in one handler

`E701` and `E702` separate rule refusal from closure failure at the error-code level, which is what
EN-9 asks for. The handler in §13.2 defeats it locally by returning its closure failure — missing
compilation context — through the `violations` channel, where it surfaces as `E701`. A checker
reading the error stream sees a rule refusal where a closure failed.

## 14. Governance Standard — GS-1 … GS-9

| Invariant | Where demonstrated | Class |
|---|---|---|
| **GS-1** the governing relation is declared, never established by containment, ordering, naming, defaulting or proximity | `governed_by` on 163 artifacts | **Violated** — §11.1 (containment governs via `module_path`) |
| **GS-2** the relation established from both perspectives, with disagreement refused | subject-side `governed_by`; governing-side rules in constitutions; `governance_chain_closure.py` proves both directions | Partial — §14.1 |
| **GS-3** governance is positive — what is not authorized is not admitted, and needs no prohibition to be unavailable | `artifact_types` allow-lists per build config; a kind with no `semantic_category` is "not authorized"; the handler registry is closed | Demonstrated |
| **GS-4** authorization and prohibition not collapsed | admission (what may exist) is `artifact_types` and closure membership; refusal (what may occur) is the assertion set — separate mechanisms | Demonstrated |
| **GS-5** a governing element is an artifact, admitted, identified and superseded as any other | INVARIANT and CONSTITUTION are ordinary kinds carrying `fqdn`, `governed_by`, `superseded_by` | Demonstrated |
| **GS-6** every governing element is itself a governed subject; no element is exempt | every constitution declares `governed_by`; 46 artifacts name `CONSTITUTION_INVARIANTS_V0` and it in turn is governed | Demonstrated — §14.2 |
| **GS-7** change to a governing element is a governed transition | a governance edit moves the closure digest, and `_verify_governance_provenance` refuses every domain not recompiled against it | Demonstrated |
| **GS-8** composition of applicable elements is by dominance and order-independent | violations accumulate into a set; no rule's position affects the outcome | Demonstrated — §9.2 |
| **GS-9** a semantic category does not establish, extend or limit what an element governs | `runtime_disposition` derives from category and governs topology participation only | Demonstrated |

### 14.1 GS-2 — both perspectives exist; disagreement is not refused at build time

The subject declares `governed_by` and the constitution declares its rules over subjects, so the
relation is established from both ends. `governance_chain_closure.py` proves the correspondence —
**but it is a process script in the runbook, not a build gate.** A subject naming a constitution that
does not name it back compiles.

GS-2's operative clause is "MUST refuse where the two assertions disagree." The realization detects
disagreement in a check somebody has to run.

### 14.2 GS-6 settles the `governed_by` cycle — Open Issue 3 is not a defect

The realization carries an unruled finding: a literal two-node cycle,
`fb.governance::CONSTITUTION_GOVERNANCE_V0 ⇄ fb.vocabulary::CONSTITUTION_VOCABULARY_V0`, both edges
declared. It turned on whether `governed_by` means *authority derivation* (a defect) or *governed
subject* (no contradiction), and the surface does not say.

**`2a` §6 answers it.** "A governing element is a governed subject … there is no privileged element
that governs without being governed," and reflexivity "is the property that makes governance real
rather than declarative." Under GS-6 the mutual relation is not merely permitted — a vocabulary
constitution that governed the governance constitution *without being governed by it* would be the
privileged element GS-6 forbids.

**The reading is settled by which one makes the arrangement conformant**: `governed_by` denotes the
governed-subject relation, and the cycle is GS-6 working. The narrower reading was already the
better-supported one — 46 artifacts name `CONSTITUTION_INVARIANTS_V0`, which is incoherent as
authority derivation — and GS-6 now supplies the reason rather than the weight of evidence.

### 14.3 GS-6's escape clause is the one thing the realization does not have

`2a` §6.1 states where the regress stops, and it is the same sentence twice:

> In genesis the closure is composed from the proposal's own declared governance together with an
> **externally claimed profile the proposal does not author** … **The claimed profile is what
> prevents reflexivity from becoming circularity** — without it, a system could declare governance
> that approves of itself and be, by its own account, perfectly governed.

**No snapshot claims a profile** (finding 4). The realization is reflexive exactly as GS-6 requires
and lacks the external term that keeps reflexivity from being self-approval.

This substantially escalates finding 4. It had been recorded as an acceptance check with no subject —
SN-8 clause 4 evaluating nothing. `2a` §6.1 makes it structural: the profile is not one condition
among four, it is **the only thing standing between reflexive governance and a system that certifies
itself.** Two profile documents exist in `.github/snapshot_profiles/` and nothing claims either.

## 15. Kind Vocabulary — KV-1 … KV-9

| Invariant | Where demonstrated | Class |
|---|---|---|
| **KV-1** the system operates under a declared kind vocabulary and names it | `CONSTITUTION_VOCABULARY_V0` exists as the vocabulary authority | Partial — §15.1 |
| **KV-2** the vocabulary is closed; an unrecognized kind is refused | `REGISTRY.node_kind_for_kind` → `None` → `E103_TYPE_MISMATCH`; `semantic_category: None` = "kind not authorized" | Demonstrated |
| **KV-3** a kind is admitted by its vocabulary — **a registry, a contract, or a mechanism MUST NOT constitute a kind** | — | **Violated** — §15.1 |
| **KV-4** exactly one authoritative discriminator carrying the self-describing canonical kind name | `artifact_kind` in the machine block | Demonstrated |
| **KV-5** a kind is never derived from a prefix, naming convention, location, or positional signal | `s1_extract:722` states the rule; `s1_extract:500` reads a kind from `artifact_code.split("_")[0]` | **Violated** — §8.2 |
| **KV-6** a vocabulary revision is a governed transition requiring no amendment to `2c`, `2b` or this document | adding a descriptor plus a schema; no ontology or machine-block change | Demonstrated |
| **KV-7** an accepted alias is normalized to the canonical kind and never emitted as authoritative | no alias mechanism exists | Vacuous |
| **KV-8** a representation change MUST NOT increment an artifact's declared version | `version` is declared and never computed; nothing increments it | Demonstrated — §15.2 |
| **KV-9** no particular kind is required by this family | the realization's 21 kinds are its own | Demonstrated |

### 15.1 KV-1, KV-3 — the registry constitutes the vocabulary

KV-3 is unusually direct: *"A kind MUST be admitted by its vocabulary. **A registry, a contract, or a
mechanism MUST NOT constitute a kind.**"*

In the realization, `compiler/governance_engine/artifact_kinds.py` **is** what constitutes a kind. A
descriptor added there makes the kind real; a kind absent from it is refused. `CONSTITUTION_VOCABULARY_V0`
exists and is the declared authority in name, but the enumeration that decides admission is the Python
registry, and nothing checks the two against each other.

This is the same shape as findings 6, 8, 12 and 25 — declared in code rather than in an artifact —
and it is the sharpest instance, because KV-3 names the mechanism-as-constitution failure explicitly
rather than leaving it to MB-1's general form. It also explains finding 24: `TRANSPORT_INGRESS` is a
kind because a descriptor says so, and no schema was required to make it one.

### 15.2 KV-8 — a correction to this map

An earlier entry cited KV-8 alongside MB-3 and ID-3 for finding 23, on the reading that it forbids a
meaning-preserving representation change from changing identity. **It does not.** KV-8 governs the
*declared version*: an artifact "that means exactly what it meant before has not become a new version
by being written differently." The realization never computes a version, so KV-8 is satisfied.

`2d` §8 goes further and is worth quoting, because it looks like it exonerates finding 23 and does
the opposite:

> What a conforming system does regenerate from the normalized representation is everything derived
> from it: canonical projections, integrity values, and attestations. **Those follow the canonical
> form (MB-3)**, so they change when the representation changes, and they must.

Integrity values are *supposed* to move when the representation changes — **when they follow a
canonical form**. Under a correct MB-3 the YAML key swap normalizes away before hashing and nothing
moves. The realization hashes raw bytes in `s1_extract`, one stage **before** the stage named
`s2_canonicalize`, and `s2_canonicalize` normalizes edges rather than the declaration. Finding 23
stands on MB-3 and ID-3; the KV-8 citation is withdrawn.

## 16. Execution Model — EX-1 … EX-15

The realized execution is `runtime/scheduler.py` traversing a workflow topology, with
`runtime/dispatcher.py` executing each contract's steps. Routing comes from `dispatch.routing`,
compiled at S2/S3 and sealed.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **EX-1** execution originates no behavior | the scheduler's own statement: "No domain logic, no semantic inference, no path construction" | Demonstrated |
| **EX-2** traversal advances only on declared outcomes, routing resolvable from the sealed representation alone | `dispatch.routing[wf_addr][cc_addr]` → next node; nothing else consulted | Demonstrated |
| **EX-3** routing not computed from payload, environment, accumulated state or caller identity | routing keys are `(cc_addr, condition)`; payload reaches `_resolve_step_inputs` and never the routing table | Demonstrated |
| **EX-4** the structure traversed is not added to, removed from, or rerouted during a run | the dispatch table is loaded at boot and never written | Demonstrated |
| **EX-5** an undeclared outcome must not occur; an outcome with no declared routing must **refuse** | — | **Violated** — §16.1 |
| **EX-6** failure paths are declared outcomes with declared routing; no recovery, retry, fallback or degraded path | no retry logic exists; `VIOLATION` is a declared outcome that routes | Partial — §16.1 |
| **EX-7** a step's inputs are resolved from declared references, never searched for or inferred | `_resolve_value` over a declared path grammar (`$.payload.…`, `$.results.<addr>.…`); an unresolvable path raises | Demonstrated |
| **EX-8** every change to governed state is a transition the declarations determined | CS operations are declared per binding with declared `effect` | Demonstrated |
| **EX-9** a governed store is written only through its owner's declarations | the reach read-only check refuses a write to a consulted entity (§9.1) | Demonstrated |
| **EX-10** the set of effects is closed and declared; no implicit effect path | CS handlers resolve through the sealed handlers table; an unnamed implementation is unreachable | Demonstrated |
| **EX-11** an event must not trigger execution | no subscriber, listener or trigger exists anywhere in the runtime; emission announces and nothing consumes | Demonstrated |
| **EX-12** a step's result conforms to its governing contract's declared surface | `_apply_outputs` maps declared outputs; `result_status_values` is declared per operation | Partial — §16.2 |
| **EX-13** no property of how an interaction arrived is observable to the traversal | the engine receives a payload built from the TI `payload_template`; no transport metadata crosses | Demonstrated |
| **EX-14** where the declarations do not answer, execution refuses and does not default, improvise or degrade | — | **Violated** — §16.1, §16.3 |
| **EX-15** an execution produces evidence sufficient to check the path independently against the sealed representation | the trace records every node, address and outcome in order | Demonstrated — §16.4 |

### 16.1 EX-5, EX-14 — an unrouted outcome ends the run instead of refusing

The scheduler states its rule plainly: *"Traversal ends when no routing entry exists for the current
`(cc_addr, condition)`."* And `_condition_addr` returns a sentinel when the outcome is unknown to the
vocabulary:

```python
    Returns -1 if the status has no registered address (no routing will match).
```

EX-5 requires that an outcome with no declared routing **produce refusal**, and EX-14 that execution
refuse where the declarations do not answer. The realization **terminates the traversal and returns
the last contract's `result_status` as the workflow's outcome** — a completion, not a refusal.

For `EXIT_` nodes this is correct and intended: an exit node has no routing because it is an ending.
The defect is that a non-exit node with an unrouted outcome is **indistinguishable from an exit**. The
two cases share one mechanism, and the mechanism reports success.

**The compiler makes this hard to reach** — routing completeness is checked at construction, which is
why the runtime path has probably never been taken. That is the standing concern in its usual form: a
runtime branch that cannot be shown to refuse, guarded by a construction-time check, is a branch
nobody has seen.

### 16.2 EX-12 — a two-namespace fallback in outcome resolution

`_condition_addr` resolves a `result_status` in a declared order:

```
1. transition::<result_status>   (primary — WF routing namespace)
2. outcome::<result_status>      (fallback — CC outcome namespace)
```

The code calls the second a fallback. It is milder than finding 14 — two declared namespaces in a
fixed order, fully deterministic, no filesystem search — but it is resolution proceeding to a second
source when the first does not answer, which AI-6 and RT-6 both name. A status registered in both
namespaces with different addresses would resolve by precedence rather than by declaration.

### 16.3 The IN_ admission gate admits everything

Every workflow topology carries `IN_` boundary nodes, and the scheduler says what they do:

```python
    # Boundary node (IN_, EXIT_) — no pipeline
    # admission_snapshot not yet integrated; IN_ nodes pass as ACK
    result_status = "ACK"
```

**A declared admission point that determines nothing and admits unconditionally.** The comment is
honest that this is unfinished, which is the right way to carry it, and the invariant it breaches is
the one whose breach is least visible: AI-6 — inability to determine producing the same outcome as
governance that permits. A workflow whose `IN_` node was intended to refuse an inadmissible
interaction admits it and routes forward on `ACK`.

This is the third mechanism in the map declared and inert, after `context_requirements` (finding 9)
and `INVARIANT_CC_NO_UNUSED_OUTPUTS_V0` (finding 20). The three differ in honesty — this one says so
in a comment — and not in effect.

### 16.4 EX-15 — the one place the trace is sufficient

EX-15 asks only that the path be independently checkable against the sealed representation, and the
trace carries `wf_addr`, `cc_addr`, `step_addr`, `step_op` and `result_status` per event, in order,
all of them addresses resolvable in the sealed vocabulary. **A party holding the snapshot can replay
the traversal and confirm every hop.**

This is worth stating because §7.1 records the trace as insufficient for EV-1, and both are true: the
trace is sufficient for the *path* and insufficient for the *determination*. EX-15 asks for the
former only, and gets it.

## 17. Runtime — RT-1 … RT-12

| Invariant | Where demonstrated | Class |
|---|---|---|
| **RT-1** originates no governed behavior, holds no domain meaning, makes no governing determination, adds nothing | the scheduler and dispatcher contain no domain vocabulary; every identifier is an address | Demonstrated |
| **RT-2** consumes only an accepted snapshot, an interaction, and declared governed state | `warm_boot` + payload + `data_root` | Demonstrated |
| **RT-3** establishes every acceptance condition before executing, and refuses the snapshot whole on failure | acceptance compares recorded values and never recomputes content | **Violated** — §3.5, §29.1 |
| **RT-4** does not modify, extend, annotate or repair an accepted snapshot | the runtime opens the snapshot read-only; all mutable output is scoped to `data_root` | Demonstrated |
| **RT-5** may take a decision only where varying it cannot vary a governed consequence | trace ids and file layout vary; no governed consequence depends on either | Demonstrated |
| **RT-6** supplies no default, selects among no ambiguous candidates, interprets no unexpected value, retries no unrouted outcome | the `transition::` → `outcome::` fallback, and the unrouted outcome ending the run | Partial — §16.1, §16.2 |
| **RT-7** produces the governed consequences the snapshot determines and nothing beyond | effects reach the world only through declared CS operations | Demonstrated |
| **RT-8** evidences every determination it makes, including every refusal | the path is evidenced; determinations are not | Partial — §7.1 |
| **RT-9** refuses wherever the declarations do not answer; does not improvise, default, degrade or continue | — | **Violated** — §16.1, §16.3 |
| **RT-10** carries no behavioral state between executions or across snapshots, and consults no prior evidence | each run boots the snapshot and opens a fresh trace; nothing reads `traces/` | Demonstrated |
| **RT-11** exposes no extension point through which domain behavior enters execution | handler resolution is a closed statically imported registry; `implementation_closure.py` proves every module is named by an artifact and present | Demonstrated |
| **RT-12** replacing a conforming runtime with another changes no governed consequence | one runtime exists | Unimplemented — §3.6 |

**RT-3 is the sharpest restatement of finding 2 in the family**, and it is worth recording that three
documents now state it independently: `3b` SN-8 as an acceptance obligation, `1c` AI-10 as an
architectural invariant, and RT-3 as a runtime obligation. The realization satisfies the *ordering*
all three require and the *content* none of them gets — acceptance completes before execution and
establishes agreement among recorded values rather than integrity over content (§29.1).

**RT-11 is the best-enforced invariant in the runtime.** A closed statically imported registry, plus a
check proving every named module exists and every existing module is named, is a demonstration that
no extension point exists — which `5b` §16 notes is otherwise establishable only negatively.

## 18. Normative Platform Profile — NP-1 … NP-11

**This is the section the map was expecting.** Part VI specifies a subject the realization approached
without a specification: two profile documents exist in `.github/snapshot_profiles/`, written before
these documents were drafted, and **no snapshot claims either** (finding 4). The result is not a
profile that falls short — it is an instrument that has been running unattached.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **NP-1** a profile permits nothing the family forbids and requires no less than it requires | both profiles state additional requirements over a family-conformant base; neither relaxes | Demonstrated |
| **NP-2** a conforming system under any profile is conforming under the family | no system conforms under either, because none claims one | Vacuous — §18.1 |
| **NP-3** a profile does not redefine core semantics or give a normative term an incompatible meaning | both use the realization's own vocabulary consistently | Demonstrated |
| **NP-4** a profile does not weaken, exempt from, or relax any invariant | neither carries an exemption clause | Demonstrated |
| **NP-5** a profile introduces no facility the family has no home for | `required_governance`, `artifact_kinds`, `artifacts`, claims — all have homes | Demonstrated |
| **NP-6** a profile's additional obligations are enforceable, and an unenforceable one is not declared | **every obligation in both profiles is unenforced**, because nothing evaluates a profile | **Violated** — §18.1 |
| **NP-7** a profile is not authored by a system that claims it | storage is fine; authorship is not | **Violated** — §18.3 |
| **NP-8** a profile decides every deferred item bearing on a conformance claim it supports | both name claims; neither decides the family's deferred items, none of which existed when they were written | Unimplemented |
| **NP-9** a profile has an identity, and a change to its obligations is a new identity | `identity: NORMATIVE_PLATFORM_PROFILE_BASELINE_V0`, `version: V0` | Partial — §18.2 |
| **NP-10** a derived profile names its base by identity and does not widen it | no derivation relation is declared between the two | Unimplemented |
| **NP-11** no selection or parameterization makes a prohibited behavior appear permitted | neither profile parameterizes anything | Demonstrated |

### 18.1 NP-6 — the obligations are unenforced, and one profile has quietly stopped naming the system

Nothing reads a profile. `verify_snapshot`, `warm_boot` and the composition conformance check make no
reference to `.github/snapshot_profiles/`, and the manifest carries no profile field (§3.3). Every
obligation both documents state is therefore declared and unenforced — the fourth instance of the
map's declared-and-inert pattern, after findings 9, 20 and 29, and by far the largest in scope.

**And the consequence is not hypothetical.** Resolving every artifact FQDN the baseline profile names
against the sealed snapshot:

```
NORMATIVE_PLATFORM_PROFILE_BASELINE_V0    35 FQDNs   23 do not resolve
REFERENCE_PLATFORM_PROFILE_V1             35 FQDNs    0 do not resolve
```

Two whole namespaces the baseline profile requires — `fb.constitution::` and `fb.topology::` — do not
exist. The artifacts do; they were reorganized:

```
fb.constitution::CONSTITUTION_GOVERNANCE_V0   →   fb.governance::CONSTITUTION_GOVERNANCE_V0
fb.constitution::STRUCTURE_DISCOVERY_V0       →   fb.structure::STRUCTURE_DISCOVERY_V0
fb.topology::CONSTITUTION_WORKFLOW_V0         →   fb.workflow::CONSTITUTION_WORKFLOW_V0
fb.topology::CONSTITUTION_EXECUTION_V0        →   fb.execution::CONSTITUTION_EXECUTION_V0
```

**A conformance contract requiring twenty-three artifacts that are not there, alongside one requiring
thirty-five that are, and nothing tells them apart** — because nothing reads either. This is
`2a` §6's second bullet arriving by a route it did not anticipate: not a system relaxing its own
profile, but a system reorganizing underneath a profile that then constrains nothing while appearing
to constrain everything.

**It also forecasts a cost for Task B.** The namespace migration moves 1,407 `fb.*` occurrences.
`REFERENCE_PLATFORM_PROFILE_V1` is currently sound and names thirty-five of them; nothing will notice
when it breaks.

### 18.2 NP-9 — identity without a change relation

Both profiles carry an identity. Neither records what its obligations were previously or what changed,
and `REFERENCE_PLATFORM_PROFILE_V1` is a `V1` whose `V0` is not present — so NP-9's second clause,
that a change to obligations is a new identity, has nothing to check against. Whether `V1` supersedes
the baseline or is a peer is undeclared, which is also NP-10.

### 18.3 NP-7 — externality is authorship, and the realization has one authority

`6a` §6 is explicit that this is not about storage:

> Externality is a property of **authorship**, not of storage. A profile may be carried anywhere,
> including within a system's own repository; what matters is that **changing it is not within the
> authority of the system that claims it.**

The profiles live in `.github`, which is legitimate. What is not is that changing them is the same
act, by the same authority, through the same release process, as changing the platform they
constrain. There is no separate authority over `.github/snapshot_profiles/`.

**This matters for how finding 5b gets closed.** The obvious fix — have the assembler claim
`REFERENCE_PLATFORM_PROFILE_V1` — would satisfy SN-5's enumeration and **would not** supply the
reflexivity term `2a` §6.1 requires, because the profile it claimed would still be one the claiming
system can change. Claiming a self-authored profile is the failure §6's first bullet describes: *"a
system declaring the standard it will be judged against — and it will pass."*

**This is a finding no code change closes.** It is a question about who may amend a document, which
is a property of the project rather than of the build, and the map records it because `6a` says the
instrument does not work without it.

## 19. Execution Environment Profiles — EE-1 … EE-8

**No execution environment profile exists.** The realization runs in one environment — a single
process, a local filesystem, one machine — and has never declared what that environment guarantees.
Most of `6b` therefore has no subject, and the invariants that survive are the ones stated over the
system rather than over a profile.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **EE-1** governed consequences do not vary with the environment | one environment; never tested against a second | Unimplemented — §19.1 |
| **EE-2** an environment profile introduces no governance kind, category, authority or determination point | no environment profile exists | Vacuous |
| **EE-3** an environment profile exempts a system from no invariant | no environment profile exists | Vacuous |
| **EE-4** a governed consequence does not follow from an environmental property no declaration established | roots are environment-provisioned and never synthesized; `pgc_env_check.py` asserts the interpreter and that no foreign package is reachable | Demonstrated — §19.2 |
| **EE-5** an environment profile does not convert an ambient property into a governed input | `PGC_SNAPSHOT_ROOT`, `PGC_DATA_ROOT`, `PGC_IMPL_ROOTS` supply *locations*; no declaration reads an environment value as a governed input | Demonstrated |
| **EE-6** two conforming environments produce the same governed consequences | one environment | Unimplemented — §19.1 |
| **EE-7** inability to establish governed state or an applicable closure refuses, whatever the environmental cause | a missing store, an unreadable snapshot and an unresolvable closure all raise; none degrades | Demonstrated |
| **EE-8** a distributed environment relieves a system of nothing | no distributed environment exists | Vacuous |

### 19.1 EE-1, EE-6 — the third statement of the same untested claim

EE-6 is SN-11 and RT-12 again, from the environment's side: the same snapshot, inputs and state must
produce the same governed consequences across two conforming environments. Three documents now state
it — `3b` for agents, `3c` for runtimes, `6b` for environments — and none can be demonstrated,
for one reason: **there is one of everything.**

This is recorded once and counted once (§3.6). What `6b` adds is the observation that the realization
has never had to *say* what its environment guarantees, so the properties EE-4 and EE-5 protect are
held by discipline rather than by a declared boundary. The discipline is real and visible —
`protocol_transport/CLAUDE.md`'s absolute-FQDN, no-fallback, env-provisioned-roots doctrine, and
`pgc_env_check.py` enforcing part of it — but a doctrine in a CLAUDE.md is not an environment profile,
and `8a` §3 already warns that a technique is not the property it serves.

### 19.2 EE-4 — the best-served invariant in Part VI

`pgc_env_check.py` asserts that the active interpreter is the workspace venv, that every PGC package
imports, and that **no legacy package is reachable** — an explicit check that an ambient environmental
property cannot reach a governed consequence. Combined with environment-provisioned roots and no path
synthesis, EE-4 is demonstrated positively rather than by absence, which is unusual in this map.

## 20. Domain Profiles — DP-1 … DP-11

Six domains are compiled into the composition — `ai_governance`, `blockchain`, `book_library_mgmt`,
`transformation`, `inspection`, `workload`. **No domain profile exists for any of them.**

| Invariant | Where demonstrated | Class |
|---|---|---|
| **DP-1** a domain does not weaken, exempt itself from, or reinterpret applicable governance | the platform governance closure is imported whole and its digest verified per domain | Demonstrated |
| **DP-2** a domain's declarations compose by dominance and contradict no applicable obligation | domain artifacts are evaluated against the imported closure; a contradiction is a violation | Demonstrated |
| **DP-3** a domain is not an authority by being named, bounded, deployed separately or separately owned | each domain is a separate root and repository, and none is treated as an authority | Demonstrated — §20.1 |
| **DP-4** a domain profile states whether the domain claims to be an authority or is a concern | — | Unimplemented — §20.1 |
| **DP-5** a domain has no private admission path | every domain compiles through the same nine stages against the same imported closure | Partial — §20.2 |
| **DP-6** a domain changes only through governed transformation against a baseline | the `transformation` compiler's nine phases, pinned to a named composition | Demonstrated |
| **DP-7** a write across a domain boundary is authorized by the governance applicable to the store written, and **never by reach** | `dispatcher._execute_cs_step` refuses a write to a `consulted` entity, "before the capability runs" | Demonstrated — §20.3 |
| **DP-8** a domain does not depend on another domain's internals | cross-domain reference is by declared FQDN into the import surface | Demonstrated |
| **DP-9** admitting a domain kind requires no ontology revision, and a domain holds no private vocabulary | every `artifact_types` list draws from the platform vocabulary; no domain introduces a kind | Demonstrated |
| **DP-10** a domain whose subject matter is governance does not thereby acquire authority over the platform | `ai_governance` and `transformation` both take governance as subject matter and neither governs the platform | Demonstrated — §20.4 |
| **DP-11** a domain does not claim genesis | genesis is the platform's; domains compile against an existing surface | Demonstrated |

**Part VI's one clear result: `6c` is the best-satisfied document in the map.** Nine of eleven
demonstrated, including the two that matter most (DP-7 and DP-10). The realization got domain
boundaries substantially right without a specification — which is worth stating as plainly as the
findings are, because `8a` §2 cuts both ways: resembling the reference realization establishes
nothing, and neither does the map's preponderance of findings establish that the realization is
mostly wrong.

### 20.1 DP-4 — the authority-or-concern question, one level down

DP-4 requires a domain profile to **state** whether the domain claims to be an authority or is a
concern. No domain states it, because no domain profile exists.

This is finding 16 at domain scale, and the realization has already been through the argument once:
the authority/concern ruling found that 26 federation boundaries conflated exactly these two things.
DP-4's answer is that the distinction is **declared, per domain, in a profile** — which is the
representation question Task B step 2 has to solve, arriving from a second direction.

**DP-3 is satisfied and DP-4 is not, and the gap between them is the finding.** Nothing treats a
domain as an authority, so no breach has occurred; nothing declares that it isn't, so nothing would
notice if one began to.

### 20.2 DP-5 — admission is shared, scope is per domain

Every domain compiles through the same stages against the same imported closure — there is no private
admission path in the sense DP-5 forbids. What each domain does carry is its own
`STRUCTURE_BUILD_*_CONFIG` declaring `artifact_types`: the kinds it may author.

That is a domain deciding its own admission *scope*, in a governed artifact, evaluated by the shared
pipeline. It is not a private path, and it is worth recording because Open Issue 7 — domain invariant
authority, ruled yes and unbuilt — sits exactly here. **`6c` neither requires nor forbids a domain
authoring governance**, so that ruling was a design choice rather than a conformance obligation, and
nothing in Part VI obliges the realization to build it.

### 20.3 DP-7 — reach is read-only, and the realization built it before reading the requirement

DP-7's second clause is unusually specific: a cross-boundary write "MUST NOT be authorized by reach."
The realization has exactly that mechanism and exactly that prohibition — an act that declared a reach
may read a consulted entity and may not write it, refused before the capability runs on two declared
facts, inferring nothing.

**This is the clearest case in the map of the realization independently reaching a requirement the
family states.** `0z` §3 says a realization "informs this family by exposing concepts that were
missing"; this is the same convergence in the other direction, and it is evidence that DP-7 names a
real distinction rather than an invented one.

### 20.4 DP-10 — two domains take governance as subject matter, neither acquires authority

`ai_governance` governs agent actions and AI licensing; `transformation` governs the design pipeline
that produces artifacts. Both have governance as subject matter, and DP-10 exists because that is
tempting to confuse with governing the platform.

Neither does. `ai_governance`'s workflows determine outcomes about agents, not about artifacts.
`transformation`'s rule sets judge design documents, and the artifacts a design determines are
admitted through the ordinary compile path with no special standing — which is why its dossiers are
pinned to a composition and judged against a sealed rule set rather than against the working tree.

## 21. Governed Transformation — TR-1 … TR-24

The realized transformation is `transformation/` — the Design Compiler (P0–P8) and the Construction
Compiler. It is the correspondence the map has to handle most carefully, for a reason stated in
§21.1 before any entry.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **TR-1** a transformation is a governed transition; its dossier is not a member of the governed system | 38 `transformation::` artifacts are in the composition; **zero dossiers are** | Demonstrated |
| **TR-2** governed content lives in registers; prose carries none | the P0–P8 templates are register tables; `template_reader` parses rows, never prose | Demonstrated |
| **TR-3** rules are declared data; check kinds closed and fail hard on the unknown; every declared rule evaluated | 820 rules over 57 check kinds, generated into `WF_P*` artifacts and **sealed into the composition**; `meta_test` proves every rule resolves to a mechanism | Demonstrated |
| **TR-3a** every declared rule demonstrated capable of refusing | **222 of 229 rule identifiers observed to fire — 96.9%** | Partial — §21.2 |
| **TR-4** a verdict names the rule and location of each finding | each finding carries rule id and register/row | Demonstrated |
| **TR-5** a constrained column's admissible values declared with the register's shape; emptiness declared not inferred | vocabulary columns declared per register; `| NONE IDENTIFIED |` is a declared sentinel read by `is_sentinel` | Demonstrated |
| **TR-6** each register declares its rung; a business rung names no constructed identity; grounding evidence occupies a declared column | rungs declared per register; `Source Finding` columns carry grounding | Demonstrated |
| **TR-7** provisional name and bound identity reconciled in both directions | P5→P7 capability reconciliation rules | Demonstrated |
| **TR-8** admissibility decided by the rule set alone; a quality score does not gate | `cli.py:221` — *"merit says how good the document is. A document may be admissible and imperfect"* | Demonstrated |
| **TR-9** an unanswered question recorded as such, never filled in or hedged; a blocking one makes its document inadmissible | the open-questions register and its sentinel | Demonstrated |
| **TR-10** human semantic content enters once; later phases preserve, reference, or declare supersession | prior-carriage rules across P1–P8 | Demonstrated |
| **TR-11** preservation checked in both directions — nothing dropped, nothing invented | — | Partial — §21.3 |
| **TR-12** gates declared; acceptance not inferred from admissibility | Gate 1 and Gate 2 are declared and human; a dossier reads ADMISSIBLE without being accepted | Demonstrated |
| **TR-13** the same human answers yield the same admissible registers for any worker | the phase pipeline is deterministic over its inputs | Demonstrated |
| **TR-14** a phase determined by its prior is projected, refuses an inadmissible prior, and its verdict is not evidence about the change | `PRIORS` per phase; a declared prior not supplied "reports the handoff unchecked rather than passing quietly" | Demonstrated |
| **TR-15** validated against a named frozen baseline, never one containing its own output | dossiers pin a composition; `design/sealed.py` reads the pinned rule set, never the working tree | Demonstrated — §21.4 |
| **TR-15a** only the first transformation may proceed without a baseline; it must name a profile it did not author | genesis names no profile | **Violated** — §18.3, finding 4 |
| **TR-16** claims about the existing system grounded; truth, belief and question in separate registers | separate grounding, belief and open-question registers | Demonstrated |
| **TR-17** sufficiency measured before realization; realization refuses below the declared threshold | `tc construction emit --require`, default **100.0** — *"Measured before anything is written. A design below the threshold does not determine its artifacts"* | Demonstrated |
| **TR-18** a realized artifact is a function of the design alone | `construction_acceptance` — 93/93 artifacts across two domains, 0 field differences | Demonstrated |
| **TR-19** an amendment is a whole redeclaration and does not narrow what it replaces | `tc construction check --snapshot` refuses a narrowing amendment | Partial — §21.5 |
| **TR-20** the realization order is total, gapless and dependency-respecting | the P8 authoring mandate declares a total order | Demonstrated |
| **TR-21** realization covers authored and amended artifacts, checked in both directions | `construction_acceptance` compares both ways | Partial — §21.5 |
| **TR-22** completion requires execution against real state, with criteria asserting state rather than returned status | the domain `execution_validation` suites run into a real data root and assert stored state | Demonstrated |
| **TR-23** a declared refusal is discharged by the design, the discharge is stated, and it is checked against what it does | §18/§19/§20 registers, and `GOVERNING_RULE_NOT_IN_FORCE` resolving a cited rule in the pinned composition | Demonstrated |
| **TR-24** where a rule set has two readers, they derive from one declaration and divergence is detectable | `differential.py` — 83 documents, two paths, both must agree | Demonstrated |

### 21.1 This document and this realization are not independent, and the map must say so

`4d` introduces eleven terms — **dossier, phase, register, check kind, verdict, gate, worker, rung,
grounding, sufficiency, realization**. None is defined by Part I. All eleven are the vocabulary of
`transformation/`. It carries twenty-four invariants, the largest set in the family, several of which
correspond to specific lessons this workspace learned and recorded: TR-3a to the rule-fire coverage
measurement, TR-24 to the differential harness, TR-15 to the pinning discipline, TR-11 to the
fabrication check, TR-19 to the narrowing-amendment guard.

**`0z` §5 permits a document to introduce terms it defines**, so membership is satisfied. `0z` §3
forbids something else: *"describing what an implementation does and declaring the description to be
the standard."*

**The map cannot settle which this is, and it would be improper for it to try** — it is evidence
about the realization, and the question is about the document. What it can do is record the test
`8a` §4.7 supplies: *where this annex cannot show how an alternative model conforms, that is evidence
of an over-specified normative document.* So the question for a ruling is concrete:

> Can a transformation system that has no "registers" and no "rungs" — one that carries governed
> content in some other bounded form — be shown to satisfy `4d`? If it cannot, `4d` names a
> mechanism while believing it names a meaning.

**Ruled** (`.github/doc/parked_rulings.md`): **the general concern does not survive its own test, and
one clause does.**

Applying `8a` §4.7 to the introduced terms, an alternative conforms in every case — a **register** is
any bounded declared surface carrying governed content rather than prose; a **rung** is any level in
a ladder from business language to bound identity; a system with one **phase** makes TR-14 vacuous
rather than violated. Each names a real distinction, and renaming is not an escape from the
requirement.

**TR-17 fails the test.** §13 requires sufficiency "measured … **as the proportion of required facts
the design states**" and refusal "below the declared threshold" — a computation and a scalar — where
the meaning is stated one line later: *"A generator that supplies a fact the design omits is a second,
ungoverned design authority."* A realization checking **per-artifact determinability** — does the
design fix every field this artifact needs? — satisfies that requirement more directly than a ratio,
and does not conform to `4d` as written.

**The realization is the evidence.** `tc construction emit --require` defaults to **100.0**, the point
at which a proportion carries no information. The scalar is not load-bearing in the only system that
implements it.

**What stays open.** Finding one over-specified clause does not settle whether `4d` was derived from
the realization, and derivation is not itself a defect — `0z` §5.1 permits experience to *occasion* a
revision, only not to decide one. `4d` carries the highest inverse-derivation risk in the family and
is the document to re-review clause-by-clause against §4.7. TR-17 is the demonstrated instance; the
review is what would establish whether it is the only one.

### 21.2 TR-3a — measured, and seven short

TR-3a is the invariant the realization arrived at independently and stated in its own words: *"a rule
set is not evidence that its rules can fail."* It then measured itself:

```
229 distinct rule identifiers
 63 ever observed to fire   (27.5%)   →   222 (96.9%)
```

**Seven rule identifiers have never been observed to refuse.** TR-3a admits no threshold — *every*
declared rule must be demonstrated capable of refusing — so 96.9% is partial, not passing. The
realization's own close-out records why each of the ten then-remaining is not a document, and two of
them need a dossier that does not exist (its specification is written).

This is the healthiest partial in the map: the obligation is understood, the gap is measured, the
number is published, and the remaining work is specified.

### 21.3 TR-11 — the direction that is checked, and the one that is not

TR-11 requires preservation checked **in both directions**: nothing dropped, nothing invented.
`4d` §18 names the second as one of two demonstrations distinguishing a conforming transformation
from one that merely completed — *"a fabrication check: a phase that states something its prior does
not, passing a pipeline that checks only for loss. Both failures report success."*

The realization's prior-carriage rules check **loss**: a P7 that fails to restate a P5 row reports
"restated nowhere here." The map found no rule that refuses a phase for stating something its prior
does not contain. The document names the hazard precisely and the realization implements one side.

### 21.4 TR-15 — the pin, and why it is stronger than the invariant asks

A dossier is validated against the composition it was designed against, never one containing its own
output, and `design/sealed.py` exists so that the pin — not the working tree — names the rule set.
The realization goes further than TR-15 in one respect worth recording: `GOVERNING_RULE_NOT_IN_FORCE`
resolves a cited rule **in the pinned composition**, so a design cannot discharge a refusal by citing
a rule its own change is adding. That is TR-15's principle applied to a case TR-15 does not mention.

### 21.5 TR-19, TR-21 — checked against the design, not against the renderer

`construction_acceptance` compares rendered artifacts against the designs that determine them, both
ways, 93/93 with zero field differences. What has no equivalent check is the **renderer** itself:
`emit_rule_sets --check` and `author_transport_contracts --check` exist for their generators, and
`tc construction emit` has none. The realization already knows this and carries it as an open item.

TR-19's narrowing guard is likewise scoped: `tc construction check --snapshot` refuses a narrowing
amendment **against the dossier's own baseline**, so two in-flight dossiers each amending one
artifact are invisible to it — a limit the realization has recorded.

## 22. Supersession — SU-1 … SU-10

Two artifacts in the composition are superseded, both in `blockchain`:

```
WF_RECORD_VERIFICATION_DECISION_V0  →  WF_ACCEPT_ACTOR_V0, WF_REJECT_ACTOR_V0
IN_ACTOR_VERIFIED_V0                →  IN_ACTOR_ACCEPTANCE_V0, IN_ACTOR_REJECTION_V0
```

| Invariant | Where demonstrated | Class |
|---|---|---|
| **SU-1** a declared relation between two exact identities, causing no reference to resolve differently | both sides name full FQDNs; nothing rewrites a reference | Demonstrated |
| **SU-2** nothing treated as superseded by deletion, renaming, deprecation in prose, or disuse | supersession is a machine-block field; both superseded artifacts remain present | Demonstrated |
| **SU-3** the relation declared **once, on the successor**; both sides established from that declaration | declared **twice** — `supersedes` on each successor and `superseded_by` on the predecessor | **Violated** — §22.1 |
| **SU-4** a predecessor recorded as superseded by nothing is refused | both predecessors name their successors | Demonstrated |
| **SU-5** where `X` supersedes `Y`, nothing references `Y`; closure determined during construction | the only machine-block references to `Y` are the SU-3 declarations themselves | — §22.2 |
| **SU-6** referential closure determined over the whole composition | `INVARIANT_SUPERSEDED_NOT_REFERENCED_V0` exists and is evaluated over the composition | Demonstrated |
| **SU-7** a superseded thing excluded from every projection execution consumes, retained in the canonical record, reachable by inspection | **both are absent from the vocabulary projection and present in `canonical/`** | Demonstrated |
| **SU-8** no mechanism deletes a superseded thing | nothing deletes; `construction_acceptance` excludes `superseded_by` from comparison because it is written by standing an artifact down | Demonstrated |
| **SU-9** a supersession determines its blast radius rather than leaving it to be discovered | the P8 authoring mandate declares the amendment set; a caller outside the composition is not in it | Partial — §21.5, §22.3 |
| **SU-10** a superseded profile or revision does not retroactively alter claims discharged against it | no claim has been discharged | Vacuous |

### 22.1 SU-3 — the relation is declared twice

The successors carry `supersedes` in their machine blocks; the predecessors carry `superseded_by` in
theirs. SU-3 requires it **once, on the successor**, with "both sides established from that
declaration" — that is, the predecessor's status **derived**, not separately asserted.

Two independent assertions of one relation can disagree, and nothing in the realization compares
them. This is the same shape as GO-2's per-kind provenance and MB-3's second copy of an integrity
value: a fact stated twice where the standard asks for it stated once and derived.

**It also corrects a standing open issue.** The workspace records that "`blockchain` carries three
references to a superseded workflow" which "under SU-5 will not compile once referential closure is
enforced." Measured: there are **two** superseded artifacts, not one; the machine-block references to
them are **exactly the SU-3 supersession declarations**; and no artifact carries a live dependency on
either. **SU-7 is already satisfied** — both are excluded from the vocabulary projection execution
consumes. The composition is not carrying stale dependencies; it is carrying its supersession
declarations twice.

### 22.2 SU-5 and SU-3 cannot both be satisfied as written

`4e` §4 is emphatic about SU-5's scope:

> The requirement is **strict**: *no* reference, not *no executable reference*. **A system that
> mentions a retired identity has not finished retiring it.**

SU-3 requires the successor to declare the relation, and a declaration of the form
`supersedes: <predecessor identity>` **is** a reference to the retired identity. Read together and
literally, **a conforming supersession is impossible**: SU-3 mandates the one reference SU-5
forbids.

§4 plainly intends "reference" to mean a dependency rather than the supersession declaration itself,
and it does not say so — while going out of its way to say the requirement admits no such narrowing.

**Ruled and upheld** (`.github/doc/parked_rulings.md`): SU-5's subject is **dependency**, not mention,
and it gains the exception SU-3 creates.

**The decisive evidence is not textual.** The realization enforces SU-5 with a handler that walks an
artifact's entire machine block for references — deliberately total, because "a handler that looked
only where references are *expected* would miss the one place a design put an identity nobody
anticipated." That handler carries:

```python
DECLARATION_KEYS = {"supersedes", "superseded_by"}
...
if key in DECLARATION_KEYS:
    continue
```

An independent implementer, enforcing SU-5 as written, hit the contradiction and carved out exactly
this exception — because without it nothing can ever be superseded. That is `0z` §3's case precisely:
a realization exposing a requirement that could not be met. **The realization needs no change; the
document does.**

### 22.3 SU-9 — a supersession is complete inside the composition and silent outside it

**Finding 44.**

`cr_04_catalog` withdrew three requirements from a catalog boundary. A boundary is rendered whole, so
saying less than its predecessor said is a supersession rather than an amendment, and because an act
names the boundary that admits it, the workflow was superseded with it. Both predecessors remain in
the composition, as SU-2 and SU-8 require.

**Both predecessors also remain live.** They are still admitted, still reachable, and still refuse
exactly the requests their successors accept. The domain's own end-to-end exercise invoked the
predecessor and was turned away — and had been for as long as the supersession existed, which was
correct behaviour by an artifact nobody had told it was retired.

**Nothing informs a caller.** SU-7 excludes a superseded artifact from every projection *execution*
consumes, and that is satisfied. But a caller naming the predecessor by identity is not executing a
projection; it is dispatching a workflow, and dispatch resolves. The blast radius SU-9 asks a
supersession to determine is determined over the composition — the P8 mandate names the amendment set
— and a caller is outside it. The exercise moved to the successor because a person read the dossier
and changed a line.

This is not SU-5: nothing in the composition *references* the predecessor. It is SU-9, and it is the
shape the map keeps finding. The supersession is declared, the declaration is governed, the closure is
determined, and the one party that had to act on it learned by prose.

**The realization needs no change here that the standard does not ask for first.** SU-9 says a
supersession determines its blast radius; it does not say whose. A composition that cannot enumerate
its callers cannot determine a radius that includes them — which is either a limit the document should
state, or a requirement that a superseded thing become unreachable rather than merely unprojected.
The second reading conflicts with SU-2 and SU-8 and would need `4e` to say which wins.

## 23. Governed Interaction Boundary — IB-1 … IB-15

The realized boundary is `protocol_transport` plus the 36 `TI_`/`TE_` contracts in
`snapshot_inspector/transport/`. Phase 1 of the workspace's own transport standard is frozen, and
its doctrine — TI and TE as first-class protocol-neutral governed boundary contracts, "not execution
stages, not protocol implementations" — is IB-1 and IB-4 stated in the realization's own words.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **IB-1** no boundary contract depends on any external protocol | no `TI_`/`TE_` contract names HTTP, a status code, a header, or a URL; the family shares one HTTP route as "a protocol convenience" | Demonstrated |
| **IB-2** an operation identity is uniquely resolvable and is not the identity of an executable target | `si.artifact.show` is an operation identity; the target is named separately under `handler.implementation` | Demonstrated |
| **IB-3** the boundary binds to a governed executable target without requiring a particular vocabulary classification | `handler.kind: SNAPSHOT_READ` selects an entry point; the engine "routes by KIND and stops there" | Demonstrated |
| **IB-4** ingress and egress are contracts at the edge, not execution stages | TI/TE are compiled artifact kinds, absent from the execution topology | Demonstrated |
| **IB-5** operation-to-target resolution, input-contract existence and closure validity determined before interaction time | all three are compiled and sealed; "it cannot happen silently in code" | Demonstrated |
| **IB-6** explicit normalization to and from the canonical form; no raw passthrough | `payload_template` maps declared inputs into the canonical payload | Partial — §23.1 |
| **IB-7** an adapter determines no governed or domain semantics | the resolver and adapters are boundary-only, fail-hard, no fallbacks | Demonstrated |
| **IB-8** a result class carries no external representation semantics | `NOT_FOUND` is a result class carrying no status code | Demonstrated |
| **IB-9** result-class-to-external-representation mapping is adapter-owned and absent from the egress contract | no `TE_` contract names an HTTP status | Demonstrated |
| **IB-10** no boundary contract or adapter introduces domain state-transition, resource or result semantics | contracts declare inputs, presentation and a handler binding; no domain meaning | Demonstrated |
| **IB-11** applicability of boundary contracts determined within an applicable governance closure | TI/TE are governed by `CONSTITUTION_TRANSPORT_INGRESS_V0` / `_EGRESS_V0` | Demonstrated |

**`5a` is the best-corresponded document in the map after `6c`**, and for an identifiable reason: it
is the one subject the realization stopped and specified *before* building. `protocol_transport`'s
Phase 1 was frozen as a standard first, with constitutions, compiler kinds and adapters explicitly
deferred until it was accepted. The result is a boundary that satisfies IB-1 through IB-11 by
construction.

### 23.1 IB-6 — normalization inbound, less clearly outbound

`payload_template` declares the inbound mapping explicitly, so no raw payload reaches a handler.
Outbound, a read operation returns a Python structure that the adapter serializes; what a `TE_`
contract declares is the result's shape, and the map found no equivalent of `payload_template` for
egress. Whether that is raw passthrough of a governed result or a declared identity normalization
depends on a `TE_` reading the map did not complete, and it is recorded as open rather than as a
finding.

## 24. Conformance Model — CF-1 … CF-13

**No conformance claim exists.** Nothing in the realization names a subject, a profile, a revision
and a claimant, so most of `7a` has no subject — which is the correct state for a system whose
profile is unclaimed (finding 4) and whose family revision is `draft-1`.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **CF-1** a claim names subject, profile, revision and claimant | no claim exists | Vacuous |
| **CF-2** a claim is not discharged by evidence about a different subject | the map states its own subject explicitly (§0) | Demonstrated — §24.1 |
| **CF-3** a system instance claim is discharged by discharging every constituent class | no claim exists | Vacuous |
| **CF-4** discharge does not require trusting the claimant; reliance on an assertion is visible as an attestation | the attestation names no party (finding 13), so reliance is not visible as one | Partial — §7.4 |
| **CF-5** conformance established over semantic guarantees, never by resemblance to a realization | cited throughout this map; the realization asserts nothing about its own conformance | Demonstrated |
| **CF-6** an evaluation derives from a stated obligation and neither adds to nor relaxes one | each map entry names its invariant | Demonstrated |
| **CF-7** an obligation with no derivable evaluation is a finding against the document stating it | — | §24.1 |
| **CF-8** an evaluation uses a discharge class capable of establishing the obligation | the map records where a class is incapable — SN-11, IN-2, IN-13 | Demonstrated |
| **CF-9** a negative property is not discharged observationally | stated at every negative property in this map | Demonstrated |
| **CF-10** an obligation about what must not vary is discharged by substitution; one configuration does not discharge it | one agent, one runtime, one environment | Unimplemented — §3.6 |
| **CF-11** no conformance level denoting partial satisfaction is defined | the realization defines none; **this map's "Partial" class is not one** — §24.2 | Demonstrated |
| **CF-12** two conforming systems producing different consequences from one input is a finding against at least one | one system | Unimplemented — §3.6 |

### 24.1 CF-7 and CD-12 describe this document

CF-7 — *an obligation with no derivable evaluation MUST be a finding against the document stating
it* — and CD-12 — *every obligation binding a claimed subject MUST have a demonstration, and any
obligation without one MUST be reported* — together describe exactly what this map produces.

**This map is not a conformance claim and must not be read as one.** It has no claimant, names no
profile, and discharges nothing (`8a` §7: following the annex discharges no claim). What it is, in
Part VII's vocabulary, is the **report CD-12 requires** — an enumeration of obligations without
demonstrations — produced in advance of any claim rather than as part of one.

That distinction matters because CF-2 forbids discharging a claim with evidence about a different
subject, and this map's subject is one snapshot of one realization (§0). Its findings are evidence
about that subject and nothing else.

### 24.2 CF-11 — "Partial" is a finding class, not a conformance level

CF-11 forbids defining a conformance level denoting partial satisfaction of an obligation. This map
uses **Partial** extensively, and it is worth stating plainly that the two are different things:
CF-11 governs *conformance regimes*, which may not offer a rank between conforming and not. A
finding class in an evidence document records *which clause of a multi-clause invariant is
demonstrated and which is not* — it grants nothing.

Every Partial entry in this map names the clause that fails. None of them is a claim that the
invariant is partly satisfied.

## 25. Conformance Test Specification — CD-1 … CD-16

**The realization has no conformance claim and an extensive demonstration practice**, and the two
facts are worth holding together: `7b` is substantially satisfied by a system that has never claimed
anything.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **CD-1** a demonstration states its obligation, subject, discharge class, what must be shown, and what constitutes failure | the check suite states expected results in the runbook; discharge class is not named | Partial |
| **CD-2** a demonstration stating no obligation is not part of a claim | no claim exists | Vacuous |
| **CD-3** every obligation whose consequence is refusal has a demonstration exhibiting the refusal, its grounds, its cause, and that nothing partly proceeded | 222/229 design rules; 85 assertion handlers with **no equivalent measurement** | Partial — §25.1 |
| **CD-4** every demonstration shown capable of failing | **the realization's own doctrine** — proved by tampering, 14 negative probes, 6 dev/7 probes each authored to fail and observed to | Demonstrated — §25.2 |
| **CD-5** a demonstration refuses where its subject is malformed, absent or unreadable, and does not report success | `NOT_FOUND` with a reason for a malformed identity; checks raise rather than skip | Demonstrated |
| **CD-6** a structural demonstration states what path was sought and over what its search was total | `implementation_closure`, `governance_closure`, `governance_chain_closure` each state their relation and their domain | Demonstrated |
| **CD-7** a comparative demonstration uses genuinely independent variants and states what was varied | `differential.py` — two readers of one declaration; the domain-neutrality rewrite stated what was varied | Demonstrated |
| **CD-8** a derivational demonstration re-derives from supplied material and does not consult the producing system | `_verify_governance_provenance` recomputes the closure rather than accepting the attestation | Demonstrated |
| **CD-9** a fixture is declared, identified and supplied with the claim | fixtures live in `scripts/testbed/fixture_dossiers/` and are named per case | Demonstrated |
| **CD-10** a negative demonstration uses a fixture that violates the obligation | 31 negative corpus documents, each naming the rules it must fire | Demonstrated |
| **CD-11** a fixture is not adjusted to make a demonstration pass | **"a fixture is not evidence — never edit the originals"**, carried as a standing rule | Demonstrated |
| **CD-12** every obligation binding a claimed subject has a demonstration; any without one is reported | this map is that report | — §24.1 |
| **CD-13** a system instance claim includes composition-obligation demonstrations, not assembled from part-level results | composition conformance evaluates 5 rules over 398 artifacts **after** assembly, not per domain | Demonstrated |
| **CD-14** a genesis claim demonstrates the claimed profile was not authored by what claims it | no profile is claimed; and if one were, it is self-authored | **Violated** — §18.3 |

### 25.1 CD-3 — refusal is demonstrated for one rule system and not the other

The realization has **two** rule systems, and they are in very different states.

- **The design rules** — 229 identifiers across nine phases — have been measured against negative
  documents authored to fire them: 222 observed to refuse, each probe naming the rules it must fire.
- **The compiler's 85 assertion handlers** have **no equivalent measurement.** Some have been proved
  by probe individually — the dev/7 probes, the schema conformance pair, the domain-wiring
  before/after — but no census exists of which assertions have ever been observed to refuse.

CD-3 binds both. **The obvious next measurement is the one the design compiler already ran, applied
to the governance surface**: how many of 85 handlers have ever been seen to fail? Finding 20 —
one handler that *cannot* refuse — was found by reading, not by measuring, which is exactly how the
seven silent design rules were found before the corpus pass.

### 25.2 CD-4 — the invariant the realization states in its own words

CD-4 is *"every demonstration MUST be shown capable of failing."* The realization arrived at the
same requirement independently and repeats it as a standing architectural concern: **a check nobody
has seen fail is a check nobody has seen.** It is enforced in practice — `author_transport_contracts
--check` is proved by editing a real contract and asserting exit 1, then restoring it; every negative
probe is authored to fail one named rule; the dev/7 probes were built, observed to fail, and
reverted.

This is the third independent convergence the map has recorded, after DP-7 and TR-3a, and the
strongest of them: the realization did not merely satisfy CD-4, it derived it, wrote it down as
doctrine, and applied it to its own checks before any of these documents existed.

## 26. Capability — CP-1 … CP-11

The realized capability surface is two kinds: **CT** (capability transform, non-effecting) and **CS**
(capability side effect, effecting). Both are declared as artifacts, bound to a `{module, callable}`
implementation, and resolved through the sealed handlers table.

| Invariant | Where demonstrated | Class |
|---|---|---|
| **CP-1** a capability is reachable only through its declared contract | `dispatcher` resolves CT and CS through `pkg.handlers`, keyed by address; no other path reaches an implementation | Demonstrated |
| **CP-2** closed sets of inputs, outputs and outcomes, and a declared effect disposition | each operation declares `input`, `output`, `result_status_values` and **`effect: read \| write`** | Demonstrated |
| **CP-3** execution does not depend on anything beneath a contract | the dispatcher calls `execute(op, payload)` and reads the declared outcome; nothing inspects the implementation | Demonstrated |
| **CP-4** a result that is not a declared outcome is not routed on | an unregistered status resolves to `-1` and matches no routing | Demonstrated — §26.1 |
| **CP-5** a capability acquires inputs only through declared references | `_resolve_step_inputs` over a declared path grammar; an unresolvable path raises | Demonstrated |
| **CP-6** a capability communicates with execution only through its declared outcome and outputs | the dispatcher reads `(result_status, raw_result)` and `_apply_outputs` maps declared outputs only | Demonstrated |
| **CP-7** a non-effecting capability produces no effect and invokes no effecting capability, directly or transitively | CT modules import only `typing` and `runtime.ct_executor`; the CT surface allow-list is enforced by invariant | Partial — §26.2 |
| **CP-8** every effect passes through a declared effecting capability | CS is the only path to a store; `implementation_closure` proves the CS surface is closed | Demonstrated |
| **CP-9** a binding is declared, resolves before dispatch, and does not alter what the contract declares | `RB` artifacts declare per-binding policy; resolution happens at boot from the sealed table | Demonstrated |
| **CP-10** replacing a realization satisfying a contract changes no governed consequence and requires no declaration change | the contract declares `{module, callable}`, so replacing the *body* is free and replacing the *module* is a declaration change | Partial — §26.3 |
| **CP-11** a capability is no source of authority, and reachability does not constitute permission | reachability is permission — a step invokes what its topology declares, with no separate determination | Partial — §26.4 |

### 26.1 CP-4 and EX-5 are adjacent and only one is breached

Both concern an outcome the declarations do not answer for. **CP-4 is satisfied**: an unregistered
`result_status` resolves to `-1` and no routing matches, so an undeclared outcome is never routed on.
**EX-5 is breached** (finding 28) because *not routed on* is implemented as *traversal ends* rather
than as *refusal*.

Recorded together because the distinction is easy to lose: the realization correctly refuses to act
on an undeclared outcome and incorrectly treats the resulting dead end as completion.

### 26.2 CP-7 — the property holds; its enforcement was withdrawn for one domain

No CT in the realization imports or invokes a CS, and the CT surface allow-list is enforced by
`INVARIANT_CT_SURFACE_CLOSED_V1` on the platform. **The workload's equivalent was deleted** when the
governance chain was closed (its authorship was withdrawn because no constitution named it), and the
platform invariant cannot substitute — importing it into a domain asserts the platform's allow-list
against that domain's artifacts.

So for `conformance_workloads/workloads/collatz`, CP-7 holds as a fact and **nothing would refuse a
third CT being added**. The realization recorded this at the time as a cost paid deliberately. `3d`
gives it a name: the invariant is satisfied and unenforced for one domain.

### 26.3 CP-10 — realization substitution is free; module substitution is a declaration change

CP-10 asks that replacing a realization satisfying a contract require no declaration to change. The
realization's binding names `{module, callable}`, so a body rewrite is invisible and a *different*
module is an authoring act.

**Whether that breaches CP-10 depends on what "a realization" names.** If it names the code behind a
contract, the realization satisfies it. If it names a substitutable implementation unit — the reading
`8a` §3's substitutability property suggests — then naming the module in the declaration couples the
contract to one implementation. The map records it as partial rather than deciding, because `3d` §8
does not say which, and the same question governs whether `implementation_closure.py` is enforcing a
contract or a coupling.

### 26.4 CP-11 — the same finding as IN-12, one layer down

CP-11's second clause — *reachability MUST NOT constitute permission to reach it* — is finding 9
restated for capabilities. A workflow step invokes the capability its topology names, and there is no
determination of whether *this* execution may reach *that* capability. The topology is the permission.

The one exception is the reach read-only check (§9.1), which is a genuine per-execution determination
about whether a capability may be used a particular way — and it is the only one. Recorded under the
same finding rather than counted twice.

## 27. Findings

Forty-four, grouped by what would close them. §28 records what became of each.

### 9.1 The identity story is half-built — one defect, five entries

| # | Finding | Class |
|---|---|---|
| 1 | The snapshot identity does not cover every constituent — indexes, behavior logic, conformance result and evidence sit outside `_identity_view` (§3.2, §8.5) | unimplemented |
| 2 | Integrity at acceptance compares recorded values and never recomputes from content; a projection can be edited and still accepted (§3.5) | unimplemented, **proved** (§29.1) |
| 3 | The self-description is not covered by the identity it carries (§3.4) | unimplemented |
| 4 | No snapshot claims a profile, so acceptance cannot evaluate one; SN-7 has no subject (§3.3) | unimplemented |
| 5 | Nothing prevents or detects a sealed projection edited in place (§3.1, §6.3) | unimplemented |

**These are one defect seen five times.** The realization built its manifest as a *provenance record*
— a chain establishing that the compiler, the assembler and the attestation agree about what was
built — and both `3b` and `4c` require a *self-description whose identity is total over what it
carries*. Finding 2 closes finding 5 as a side effect. Closing any one alone leaves a snapshot whose
identity story is half-migrated.

### 9.2 Declaration surfaces that stop short of the mechanism

| # | Finding | Class |
|---|---|---|
| 6 | No projection contract exists; six lossy projections declare no selection, so omission is uncheckable and PJ-6 is vacuous (§6.1) | unimplemented |
| 7 | `dispatch`, `handlers` and the vocabulary lookup tables have no structural verification — and `dispatch` and `handlers` are what the runtime routes on (§6.2) | unimplemented |
| 8 | The read/query classification IN-4 requires is undeclared; `catalog.category` is presentation (§5.1) | unimplemented |
| 9 | Reads are permitted by reachability; `context_requirements` is declared and inert (§5.4) | unimplemented |

Findings 6 and 8 have the same shape and the same fix, already demonstrated once in this codebase:
the `TI_SI_*` contracts moved the inspection surface's metadata out of code into governed artifacts,
so that "adding, renaming or re-pointing an operation is an authoring act … it cannot happen
silently in code." Projections and read classes are the same move, not yet made.

### 9.3 Evidence records the path and not the determination

| # | Finding | Class |
|---|---|---|
| 10 | A trace establishes the path taken and none of §3.1's five points — no closure, no rules supplied, no predicate results (§7.1) | unimplemented |
| 11 | Construction refuses without evidence: `CompilerError` produces a stderr diagnostic and exit 1, and no record of the determination (§7.2) | unimplemented |
| 12 | Evidence does not distinguish determinative from observational content, and the distinction is undeclared — so EV-6 cannot be checked even in principle (§7.3) | unimplemented |
| 13 | The attestation names no attesting party (`public_key_ref: "STUB"`), so no chain terminates in a nameable trust root (§7.4) | unimplemented |

**Finding 12 has the widest reach in the map.** EV-6, EV-16 and SN-11 all rest on it, and none can be
demonstrated until it exists. Finding 10 and finding 11 together are the map's confirmation of the
plan's known gap **AI-14**, and they narrow it usefully: the runtime evidences its path faithfully
and evidences no determination; construction evidences nothing at all on refusal. **AI-16** is
confirmed as partial — integrity is independently checkable, determination is not (§7.4).

### 9.4 Resolution and admission

| # | Finding | Class |
|---|---|---|
| 14 | Imported-capability resolution **searches** (`rglob`), **selects** (`matches[0]`), **falls back** (`continue`), and **never compares the found artifact's declared identity against the one sought** — ID-14, ID-11, ID-7 (§8.3) | **violated** |
| 15 | A pure relocation changes the composite snapshot identity: the canonical artifact carries a `module_path` derived from its source directory, and `_identity_view` covers the canonical projection hash — the relocation test of `4c` §10 fails (§8.1) | **violated, proved** |
| 16 | **CLOSED by Task B** — zero `fb.*` namespaces remain; `authority` and `concern` are declared carriers. Was: A namespace of the form `fb.<concern>` encodes concern alongside identity — ID-12 (§8.4) | **violated**, already ruled |
| 19 | **CLOSED by Task B** — all three derivation sites read the declared `concern`; the two `_owner_subdomain` functions are deleted. Was: **`owner_subdomain` — a governed ownership fact that a governance assertion refuses on — is derived from the source directory** via `module_path`, and no artifact declares it. PJ-4 and `4c` §4.1 (§8.1.0) | **violated, proved** |

Findings 14 and 15 are the only places so far where a mechanism demonstrably does what an invariant
forbids, rather than failing to demonstrate that it does not. **Finding 15 is one field deep**: the
semantic layer is wholly insensitive to location — identity, content hash, graph address, graph
topology, tokenized projection and attestation are all byte-identical across the move — and a single
location-derived field rides into a projection the identity covers.

**Finding 19 is the one to read.** Finding 15 is its symptom — a hash that moves — and 19 is the
mechanism: a governance determination made from a directory name, over a fact no artifact declares.
It is the only finding so far where the realization holds a **stated, deliberate position contrary to
a normative document** rather than an unimplemented obligation, which makes it the first that needs a
ruling rather than a work item.

**One claim was withdrawn on probing.** An earlier reading held that admission is filename-driven and
that a renamed artifact is *silently dropped*. It is not: referential closure refuses the rename at
`S2_CANONICALIZE`, and every artifact available to test is referenced by something (§8.1.1). The
silent `continue` in discovery remains a latent hazard whose exposure condition is nameable — an
artifact class nothing references — and it is recorded as a hazard rather than counted as a finding.

### 9.5 Refusal, and the one finding against a document

| # | Finding | Against |
|---|---|---|
| 17 | Refusal leaving no residue holds by pipeline shape, not by mechanism, and would not survive a materialization that is incremental or precedes an obligation (§4.2, §6.2) | the realization |
| 18 | **RULED, and reversed.** `5b` §2 forecloses the tooling exemption by name and §12 closes the observability route; IN-14 bounds the scope at the seal. IN-13 is **violated by the realization** — `protocol_runtime examine` and `.github/process/frontmatter_fidelity.py` read the sealed snapshot outside the `si.` surface (§5.5) | **violated** |

### 27.6 Enforcement — an obligation that cannot refuse

| # | Finding | Class |
|---|---|---|
| 20 | **`INVARIANT_CC_NO_UNUSED_OUTPUTS_V0` is declared as governance and cannot refuse.** Its handler returns `"violations": []` with `"status": "PASSED"`; its only violation path is a missing-context guard. EN-5, EN-11 — and its stated subject is "code smell" and "optimization opportunities", which is **adequacy**, breaching GC-1 (§13.2) | **violated** |
| 21 | Coverage is proved in one direction only: `governance_closure.py` proves no handler lacks an invariant, and nothing proves no *obligation* lacks an assertion capable of refusing it. EN-1 (§13.1) | unimplemented |
| 22 | Nothing compares what an assertion does against what its invariant says, so a drifted handler is indistinguishable from a faithful one. EN-4 (§13.1) | unimplemented |

### 27.7 Part II — declaration, classification, and authority

| # | Finding | Class |
|---|---|---|
| 23 | **Integrity is computed over the serialization, not over a canonical form of the semantic object.** Swapping two sibling YAML keys leaves the parsed object identical and moves `content_hash`, `graph_topology_hash` and `canonical_projection_hash` — so the composite snapshot identity moves. MB-3, ID-3, KV-8 (§11.2, §29.4) | **violated, proved** |
| 24 | **Five schemas do not close their surface** — STRUCTURE (the build-configuration authority), the three AUTHORITY kinds, and TRACE_EVENT — and **`TRANSPORT_INGRESS`/`TRANSPORT_EGRESS` have no schema at all**, so 36 contracts carrying the read surface are validated by no closed surface. MB-11 (§11.3) | violated |
| 25 | Semantic category and provenance are declared **per kind, in code**, where GO-1/GO-3 ask a kind to declare and GO-2/MB-12/MB-13 quantify over **elements** (§10.1, §10.2, §11.4) | unimplemented |
| 26 | Nothing evaluates an artifact against its category's contract; GO-6…GO-9 hold by pipeline arrangement rather than by a check reading a category. GO-5 (§10.3) | unimplemented |
| 27 | No kind states whether a governance assertion is required for its ordinary use, so omission is indistinguishable from a kind requiring none. MB-10 (§11.3) | unimplemented |

### 27.8 Execution, vocabulary, and the reflexivity term

| # | Finding | Class |
|---|---|---|
| 28 | **An outcome with no declared routing ends the run instead of refusing.** A non-exit node with an unrouted outcome is indistinguishable from an exit, and the workflow reports the last contract's status as its own. EX-5, EX-14, RT-9 (§16.1) | **violated** |
| 29 | **The `IN_` admission gate admits unconditionally** — `result_status = "ACK"`, with "admission_snapshot not yet integrated" stated in the code. A declared admission point determining nothing. AI-6, EX-14, RT-9 (§16.3) | **violated** |
| 30 | **The kind registry constitutes the vocabulary.** KV-3 forbids a registry, contract or mechanism from constituting a kind; `artifact_kinds.py` is what makes a kind real, and nothing checks it against the declared vocabulary authority (§15.1) | **violated** |
| 31 | Outcome resolution falls back from `transition::` to `outcome::`. Milder than finding 14 — two declared namespaces, fixed order — but resolution proceeding to a second source when the first does not answer. AI-6, RT-6 (§16.2) | violated |
| 32 | GS-2 requires refusing where subject-side and governing-side assertions disagree; `governance_chain_closure.py` detects it in a runbook script, not at build (§14.1) | unimplemented |

**Finding 29 is the third declared-and-inert mechanism**, after `context_requirements` (finding 9)
and `INVARIANT_CC_NO_UNUSED_OUTPUTS_V0` (finding 20). They differ in how plainly the code admits it
and not at all in effect: a governance point that determines nothing produces the same outcome as one
that permits, which is AI-6's least visible form.

**Finding 28 is guarded by a construction-time check, which is why it has never been reached.** That
is the standing concern in its usual shape — a runtime branch nobody has seen refuse.

### 27.10 Profiles — the instrument that was never attached

| # | Finding | Class |
|---|---|---|
| 33 | **The baseline profile has rotted and nothing noticed.** 23 of its 35 required artifact FQDNs do not resolve; `fb.constitution::` and `fb.topology::` no longer exist. `REFERENCE_PLATFORM_PROFILE_V1` resolves 35 of 35. **Nothing distinguishes them, because nothing reads either.** NP-6 (§18.1) | **violated, measured** |
| 34 | **NP-7 is breached in substance and no code change closes it.** Externality is authorship, not storage: changing `.github/snapshot_profiles/` is the same act, by the same authority, through the same release process, as changing the platform it constrains (§18.3) | **violated** |
| 35 | No execution environment profile exists; EE-2, EE-3 and EE-8 have no subject, and what EE-4/EE-5 protect is held by doctrine in a `CLAUDE.md` rather than by a declared boundary (§19.1) | unimplemented |
| 36 | No domain profile exists for any of six domains, so DP-4 — state whether the domain claims to be an authority or is a concern — is undeclared everywhere. Finding 16 at domain scale (§20.1) | unimplemented |

**Finding 33 is finding 5b's consequence, measured.** An unclaimed profile is an unverified profile,
and an unverified conformance contract decays silently: the platform was reorganized and the document
requiring the old arrangement went on looking authoritative. `2a` §6 anticipated a system relaxing its
own profile; this is the same outcome reached by not looking at it.

**It also prices Task B.** The migration moves 1,407 `fb.*` occurrences.
`REFERENCE_PLATFORM_PROFILE_V1` is sound today and names thirty-five of them; nothing will notice when
it breaks. **Add the profile to the migration's blast radius, and add a resolution check to the
runbook — that check is three lines and would have caught finding 33 years ago.**

**Finding 34 changes how finding 5b should be closed.** The obvious fix — have the assembler claim
`REFERENCE_PLATFORM_PROFILE_V1` — satisfies SN-5's enumeration and **does not** supply the reflexivity
term, because the profile claimed would still be one the claiming system can change. `6a` §6: *"a
system declaring the standard it will be judged against — and it will pass."* Closing 5b properly is
two acts, not one: **claim a profile, and place its amendment under an authority the composition does
not hold.**

**Part VI is where the ratio finally inverted, and not how the map expected.** The prediction was that
documents specifying subjects the realization approached without a specification would yield findings
against the *documents*. Instead `6c` came out the **best-satisfied document in the map** — nine of
eleven demonstrated, including DP-7, where the realization independently built the exact prohibition
the family states — while `6a` produced the two most consequential findings in it. The realization got
domain boundaries right and profiles wrong, and nothing about "approached without a specification"
predicted which would be which.

### 27.11 Transformation, supersession, and the boundary

| # | Finding | Class |
|---|---|---|
| 37 | **CLOSED BY REVISION.** Ruled and narrowed: the vocabulary concern does not survive `8a` §4.7. One clause was over-specified — TR-17's proportion-and-threshold — and `draft-2` restates it over the requirement. `4d`'s own §1 already disclaimed what §13 specified (§21.1, `revisions.md`) | **closed** |
| 38 | **CLOSED BY REVISION.** Ruled and upheld: SU-5's subject is *dependency*, not mention. `draft-2` adds the exception SU-3 creates. The realization already implemented the corrected rule (§22.2, `revisions.md`) | **closed** |
| 39 | Supersession is declared **twice** — `supersedes` on the successor and `superseded_by` on the predecessor — where SU-3 requires it once with the other side derived. Two assertions of one relation can disagree and nothing compares them (§22.1) | violated |
| 40 | TR-3a admits no threshold and **seven of 229 design rules have never been observed to refuse** (§21.2) | partial, measured |
| 41 | TR-11 requires preservation checked both ways; the realization checks **loss** and not **fabrication** — the exact failure `4d` §18 names as reporting success (§21.3) | unimplemented |
| 42 | **No census exists of which of the 85 compiler assertion handlers have ever been observed to refuse.** CD-3 binds them as it binds the design rules, which were measured at 96.9% (§25.1) | unimplemented |

**Findings 37 and 38 both come from Part IV, and neither could have been found by mapping a document
against code alone**: 37 required noticing that the correspondence was *too* good, and 38 required
reading two invariants of one document against each other.

**Both are now ruled** (`.github/doc/parked_rulings.md`). 38 is upheld and SU-5 is narrowed to
dependency rather than mention — with the realization's own handler, which already exempts the
declaration keys, as the evidence that an implementer enforcing SU-5 as written hits the contradiction
immediately. 37 is **narrowed**: the vocabulary concern fails its own test, and what survives is one
clause — TR-17's proportion-and-threshold, where §13 states the meaning one line later and the
realization's default of `100.0` sits at the point where the proportion carries no information.

**Two of the map's three findings against a document survive the ruling pass, and one reversed
against the map.** Finding 18 was the map misreading `5b`; findings 37 and 38 hold, 37 in narrowed
form. **Finding 44 became the fourth after this pass**, and is the third to change a document —
`4e` SU-9, bounded to the composition in `draft-2` Change 3.

**Finding 42 is the actionable one.** The design compiler measured its own rule system and found
seven rules that could not fire and two that were silent at a whole phase. The governance surface has
had no such measurement, and finding 20 — an obligation declared as governance that *cannot* refuse —
was found by reading rather than by measuring. **The same census, applied to 85 handlers, is the next
measurement worth running.**

**A standing open issue is corrected.** The workspace records that `blockchain` "carries three
references to a superseded workflow" which "under SU-5 will not compile." Measured: **two** superseded
artifacts; the machine-block references to them are **exactly the SU-3 supersession declarations**;
no artifact carries a live dependency; and **SU-7 is already satisfied** — both are absent from the
vocabulary projection execution consumes and present in the canonical record. The composition is not
carrying stale dependencies.

| # | Finding | Class |
|---|---|---|
| 43 | The workload's CT surface closure invariant was withdrawn when the governance chain was closed, so **CP-7 holds as a fact and nothing would refuse a third CT** in that domain. The platform invariant cannot substitute — it carries the platform's allow-list (§26.2) | unimplemented, known |

### 27.12 Three convergences, recorded as evidence about the documents

The map has now found three places where the realization independently reached a requirement the
family states, before these documents existed:

| | The realization built | The family requires |
|---|---|---|
| **DP-7** | reach is read-only; a write to a consulted entity is refused before the capability runs | a cross-boundary write MUST NOT be authorized by reach |
| **TR-3a** | "a rule set is not evidence that its rules can fail" — then measured 63/229 → 222/229 | every declared rule MUST be demonstrated capable of refusing |
| **CD-4** | "a check nobody has seen fail is a check nobody has seen" — proved by tampering | every demonstration MUST be shown capable of failing |

**This is the one kind of evidence a single-realization map can offer about the documents rather than
about the code.** Convergence is weak evidence — one group, one set of habits — but it is not nothing:
each of these was reached under pressure from a defect, written down as doctrine, and only later found
to match a normative requirement. Recorded because the map's thirty-nine findings against the
realization would otherwise be its only visible result.

### 27.9 Two adjudications and one correction

**Open Issue 3 is settled, and it is not a defect.** `2a` GS-6 requires that every governing element
be a governed subject and that no privileged element govern without being governed. The
`CONSTITUTION_GOVERNANCE_V0 ⇄ CONSTITUTION_VOCABULARY_V0` cycle is that requirement working:
`governed_by` denotes the governed-subject relation, and a vocabulary constitution governing the
governance constitution *without being governed by it* would be the privileged element GS-6 forbids
(§14.2).

**Finding 4 is escalated from an unevaluated check to the missing reflexivity term.** `2a` §6.1: the
regress terminates at genesis because the closure includes "an externally claimed profile the
proposal does not author," and **"the claimed profile is what prevents reflexivity from becoming
circularity — without it, a system could declare governance that approves of itself and be, by its
own account, perfectly governed."** No snapshot claims a profile. The realization is reflexive
exactly as GS-6 requires and lacks the only external term (§14.3).

**A citation is withdrawn.** Finding 23 cited KV-8 alongside MB-3 and ID-3. KV-8 governs the
*declared version*, not identity, and the realization never computes a version — KV-8 is satisfied.
`2d` §8 in fact says integrity values *must* change when the representation changes, **when they
follow a canonical form**; the realization has no canonical form, hashing raw bytes in `s1_extract`
one stage before the stage named `s2_canonicalize`. Finding 23 stands on MB-3 and ID-3 (§15.2).

**Finding 23 is finding 15's twin and the pair is one defect.** Both move the composite identity
while governed content is unchanged; one on the *location* axis, one on the *representation* axis.
Both have the same cause — a value that is a property of a **file** rather than of a **semantic
object** riding into a projection the identity covers. `module_path` and `content_hash` are the two
values, and closing either without the other leaves the test failing.

**MB-1 adjudicated four open findings and split them two ways** (§11.1). Finding 19 is a **breach** —
a directory determines subdomain ownership and refuses on it, which is something outside the
declaration surface determining something about the artifact, and `2e` CA-8 names it a third time.
Findings 6, 8 and 12 are **gaps** — undeclared, but nothing outside the surface is determining them
either. MB-1 prohibits a second surface, not an empty one.

**CA-10 is the map's strongest demonstration and is recorded as such** (§12.1). The governance
closure is assembled, enumerated, counted, hashed, carried in the attestation, and re-verified at
assembly by a check that refuses a domain compiled against a different closure. It exceeds what the
invariant asks.

**Finding 20 corrected an earlier entry in this map.** §4 recorded GC-1 as Demonstrated on the
strength of "no stage evaluates whether a candidate is good." One of 85 does. It went unnoticed
precisely because it is non-blocking — it evaluates goodness and then declines to act on the answer,
which is the least visible form of the breach and the reason `2f` exists to name it.

**It is also the map's first case of a later document correcting an earlier entry**, which is the
behavior `0z` §3 predicts of a realization examined against a family rather than against one
document: `4a` alone could not see it, because GC-1's breach here is legible only once EN-11 supplies
the test.

**Finding 18 was ruled and reversed** (`.github/doc/parked_rulings.md`). The map read IN-13 in
isolation; read with `5b` §2, §12 and IN-14 the document is unambiguous and answers *against* the
convenient reading. §2 forecloses the tooling exemption by name — inspection "is not … a tool that
happens to read files" — and §12 calls a side channel opened for observation an ungoverned read path.
**IN-14 supplies the boundary**: a pre-seal read is not inspection at all, so construction is outside
`5b` without needing an exemption, and everything reading a *sealed* representation is inspection
whoever performs it.

Two instances follow, and the realization already demonstrates the correct pattern in a third place —
`transformation/design/sealed.py` needed a sealed rule set and went through
`inspector.api.query("si.artifact.show", …)`, and when the observation pipeline could not supply what
a check needed the answer was to author `si.rule_set.list` rather than open a side channel.

**Worth stating because it is uncomfortable: the reading that exonerated the realization was the one
this map reached first, and it was wrong.**

**Three absences are deliberately not findings.** SN-11 needs a second conforming agent (§3.6).
IN-2's and IN-13's negative properties are established by the absence of a path rather than by any
observation, which `5b` §16 says plainly. And PJ-12 holds by construction — all six projections
derive from one Graph in one pass — which is a stronger guarantee than the invariant asks for and
still not a check on what was carried (§6.4).

## 28. Resolution register

Forty-four findings, and what has become of each. **The map records what was found; without this it
records nothing about what was done, which is the defect it keeps finding in the realization applied
to itself.**

A finding is resolved by ruling, by a change, or by being deferred with its ground stated. It is
never resolved by editing a normative document to match what was built (Document Set §3) — except
where the finding is *against the document*, which three of these are.

| Status | Meaning |
|---|---|
| **CLOSED** | the finding no longer holds, and something demonstrates that |
| **PARTIAL** | some of it is closed and the entry says which |
| **REVISED** | the finding was against the document; the document changed |
| **IN CR** | a dossier carries it; the dossier's state says how far |
| **DEFERRED** | not being closed, with the ground recorded |
| **OPEN** | no disposition |
| **UNASSESSED** | nobody has looked since the map was written |

**Every UNASSESSED row is an admission, not a category.** The register was added after the fact and
its first job is to stop having any.

| # | Status | Where |
|---|---|---|
| 1 | CLOSED | D5-A — identity total over enumerated constituents |
| 2 | CLOSED | D5-A — integrity recomputed from bytes; probe §29.1 re-run |
| 3 | CLOSED | D5-A — self-description covered by the identity it carries |
| 4 | CLOSED | D5-A — `profile` is required at assembly |
| 5 | CLOSED | D5-A — closed as a side effect of 2 |
| 6 | OPEN | projection contract; CR-shaped, not raised |
| 7 | OPEN | structural declaration for dispatch and lookup tables |
| 8 | OPEN | read/query classification; CR-shaped, not raised |
| 9 | OPEN | reads permitted by reachability; CR-shaped, not raised |
| 10 | CLOSED | `WF_ROUTE` and the determination record establish §3.1's five points |
| 11 | CLOSED | construction determination records written for ADMITTED and REFUSED |
| 12 | CLOSED | `VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V0`, read from the sealed composition |
| 13 | DEFERRED | `composition_identity` §12 — making the signature real is its own change; the attestation's constitutes/accompanies division is now declared and read |
| 14 | OPEN | imported-capability resolution searches and selects |
| 15 | CLOSED | `module_path` removed from the canonical projection |
| 16 | CLOSED | Task B — zero `fb.*` namespaces remain |
| 17 | OPEN | refusal residue holds by pipeline shape, not by mechanism |
| 18 | REVISED | ruled and reversed; became two realization violations, both closed |
| 19 | CLOSED | Task B — all three derivation sites read the declared carrier |
| 20 | IN CR | `enforcement_capability` — authored; the obligation that judges quality is named for `capability_contracts` |
| 21 | OPEN | coverage proved in one direction only |
| 22 | IN CR | `enforcement_capability` — `INVARIANT_ASSERT_CAPABLE_OF_REFUSING_V0` authored, carrying `declared_not_enforced` until the seventeen owners restate |
| 23 | CLOSED | `content_hash` computed over a canonical form |
| 24 | IN CR | `schema_governance`, P0–P8, gates closed. Worse than stated and narrower: six kinds were dispatched to nothing, three descriptions had drifted, two kinds have none — and four of the five open surfaces describe runtime data, not declarations, so they were never this finding's subject |
| 25 | OPEN | semantic category and provenance declared per kind, in code |
| 26 | OPEN | nothing evaluates an artifact against its category's contract |
| 27 | OPEN | no kind states whether a governance assertion is required |
| 28 | CLOSED | `UnroutedOutcomeError` — an unrouted outcome refuses |
| 29 | CLOSED | the `IN_` gate determines admission from its declared contract |
| 30 | OPEN | the kind registry constitutes the vocabulary |
| 31 | OPEN | outcome resolution falls back |
| 32 | OPEN | GS-2 two-sided assertion refusal |
| 33 | CLOSED | the claimed profile is evaluated at assembly; the rotted one is refused |
| 34 | **RULED, standing limitation** | NP-7 breached in substance; no code change closes it. **Re-derived independently by E4's reading pass from `1b` §11, which supplies the ground the original entry did not state: reflexive determination is vacuous without a condition the proposal did not author, so this is not a formality but the clause the whole instrument rests on. `6a` §6 settles the test — externality is authorship, not storage. **RULED:** the realization makes no genesis claim and says so. `7b` CD-14 requires a genesis claim to *demonstrate* the separation, and the thing to be demonstrated is not true — so no check closes it and none should be written. An externally authored profile is pursued in parallel, because E5 requires one regardless. A separation of authority declared inside the project was refused as appearance without substance.** |
| 35 | OPEN | no execution environment profile exists |
| 36 | OPEN | no domain profile exists for any of six domains |
| 37 | REVISED | `4d` TR-17 restated as requirement rather than mechanism |
| 38 | REVISED | `4e` SU-5 narrowed to dependency; the exception SU-3 creates |
| 39 | CLOSED | both sides compared by a process check; the closure handler normalizes a scalar `superseded_by` |
| 40 | OPEN | seven of 229 design rules have never fired |
| 41 | OPEN | TR-11 preservation checked one way |
| 42 | IN CR | `enforcement_capability` — the census exists; the two obligations `conformance` owns now declare the stage that matches what their checks do |
| 43 | CLOSED | `INVARIANT_CT_SURFACE_DERIVED_CLOSED_V0` closes a domain surface by `declared == invoked`; a third transform added to the workload was refused |
| 44 | REVISED | `4e` SU-9's blast radius bounded to the composition; §5, §8, §10, §11 |

**Tally: 17 closed, 4 revised, 5 in a change request, 2 deferred, 16 open, 0 unassessed.**

**All five in-CR findings now have their governance authored as well as designed.** A
composition's identity no longer counts when it was built — three recompiles of unchanged source
yield one identity, and a pin survives a rebuild for the first time. A domain's transform surface is
closed by derivation. Schema dispositions are declared per kind and a description that describes
nothing is refused.

Two dispositions carry no finding number because they are not findings against this realization:
`composition_identity` and `construction_determinacy` were raised from defects found *while resolving*
these, and belong to the workspace's dossier record rather than to this map.

### 28.1 Standard-side disposition of the seventeen open findings

**A status says what became of a finding; it does not say whose problem it is.** Seventeen rows read
OPEN, and nothing distinguished a requirement this realization has not built from a position the
standard leaves to a profile that does not exist, from a defect in the document itself. That
distinction decides what the next action even is, so it is recorded here rather than re-derived.

Each open finding is exactly one of:

| | |
|---|---|
| **RI absence** | the requirement is sound and applicable; this realization does not realize it |
| **Profile absence** | the standard requires the position to be established by a profile, and none exists |
| **Document defect** | the normative document itself needs revision |

**The classification is not a re-opening of the finding.** Where this map differs from a normative
document, the document governs; a row below that reads *RI absence* is recording that the document
was right, not that the finding was wrong.

| # | Disposition | Next action |
|---|---|---|
| 6 | RI absence | declare a projection contract; PJ-6 is vacuous until one exists |
| 7 | RI absence | structural verification for `dispatch`, `handlers` and the lookup tables the runtime routes on |
| 8 | RI absence | declare the read/query classification IN-4 requires |
| 9 | RI absence | make `context_requirements` determinative instead of inert |
| 14 | RI absence | resolution must compare the found artifact's declared identity against the one sought — ID-7, ID-11, ID-14 |
| 17 | RI absence | give refusal-leaves-no-residue a mechanism rather than a pipeline shape |
| 21 | RI absence | prove the second direction — that no obligation lacks an assertion capable of refusing it |
| 25 | RI absence | move semantic category and provenance from code into per-element declarations |
| 26 | RI absence | evaluate an artifact against its category's contract; GO-5 |
| 27 | RI absence | let a kind state whether a governance assertion is required for ordinary use |
| 30 | RI absence | the kind registry constitutes the vocabulary, which KV-3 forbids; check the registry against the declared vocabulary authority |
| 31 | RI absence | remove the `transition::` → `outcome::` fallback |
| 32 | RI absence | move GS-2's two-sided disagreement check from a runbook script to the build |
| 41 | RI absence | check preservation both ways — the realization checks loss and not fabrication |
| 40 | RI absence | seven of 229 design rules have never been observed to refuse; a rule never observed refusing is a demonstration gap, not evidence that TR-3a is defective |
| 35 | **Profile absence** | no execution environment profile exists; EE-2, EE-3 and EE-8 have no subject |
| 36 | **Profile absence** | no domain profile exists for any of six domains; DP-4 is undeclared everywhere |
| 44 | **Document defect** | **RESOLVED** — SU-9's blast radius bounded to the composition, `draft-2` Change 3 |

**One finding raised after this register was written**, by E4's reading pass rather than by the map:

| # | Disposition | Where |
|---|---|---|
| 45 | **RI absence** | **The conformance profile declares four axes nothing can verify.** `REFERENCE_PLATFORM_PROFILE_V1` §3 marks `required_compiler`, `required_assembler`, `required_runtime` and `required_transport` capabilities **verifiable: No**, because *"no component declares its capabilities into the snapshot."* The profile states them as contract terms and records that they are *"declared but unverified … they state intent for a conformance checker that cannot yet enforce them."* **Declared ≠ enforced, inside the conformance contract itself** — the cycle's central pattern reproduced by the artifact whose job is to prevent it. Next action: each component emits a capability declaration that assembly records in the manifest, making the four axes contract terms rather than commentary. |

**Fifteen RI absences, two profile absences, one document defect — the last now resolved.**

**That the ratio is this lopsided is the map's own result.** Forty-four findings against a document
family produced four document defects, and the sixteen that remain open are almost entirely work
this realization has not done. A map that had been quietly amending the standard to match the
realization would not look like this.

**The two profile absences are the same absence at two scales**, and they are where the standard's
intentional degrees of freedom have nowhere to be stated. They are also the first concrete instances
of profile-defined territory — until a profile exists, a position the standard delegates to one is
indistinguishable from a position the standard forgot.

## 29. Coverage

| Document | Invariants | Mapped | Findings |
|---|---|---|---|
| `1c` Architectural Invariants | AI-1 … AI-17 | the 7 checked directly | 11 (via AI-8) |
| `2a` Governance Standard | GS-1 … GS-9 | all | 4 (escalated), 19, 32 |
| `2b` Governance Semantic Ontology | GO-1 … GO-12 | all | 16, 25, 26 |
| `2c` Machine Block | MB-1 … MB-14 | all | 16, 19, 23, 24, 25, 27 |
| `2d` Kind Vocabulary | KV-1 … KV-9 | all | 30 |
| `2e` Governance Closure & Authority | CA-1 … CA-12 | all | 16, 19 |
| `2f` Enforcement & Refusal | EN-1 … EN-13 | all | 20, 21, 22 |
| `3a` Execution Model | EX-1 … EX-15 | all | 28, 29, 31 |
| `3b` Snapshot | SN-1 … SN-13 | all | 1, 2, 3, 4, 5 |
| `3c` Runtime | RT-1 … RT-12 | all | 2, 28, 29, 31 |
| `3d` Capability | CP-1 … CP-11 | all | 9, 43 |
| `3e` Evidence, Attestation & Provenance | EV-1 … EV-16 | all | 10, 11, 12, 13 |
| `4a` Governed Construction | GC-1 … GC-14 | all | 17, 20 |
| `4b` Projection | PJ-1 … PJ-12 | all | 5, 6, 7 |
| `4c` Identity & Addressing | ID-1 … ID-15 | all | 1, 14, 15, 16, 19, 23 |
| `4d` Governed Transformation | TR-1 … TR-24 | all | 4, 37, 40, 41 |
| `4e` Supersession | SU-1 … SU-10 | all | 38, 39 |
| `5a` Governed Interaction Boundary | IB-1 … IB-15 | all | — |
| `5b` Governed Inspection | IN-1 … IN-14 | all | 8, 9, 18 |
| `6a` Normative Platform Profile | NP-1 … NP-11 | all | 4, 33, 34 |
| `6b` Execution Environment Profiles | EE-1 … EE-8 | all | 35 |
| `6c` Domain Profiles | DP-1 … DP-11 | all | 36 |
| `7a` Conformance Model | CF-1 … CF-13 | all | — |
| `7b` Conformance Test Specification | CD-1 … CD-16 | all | 42 |

**The map is complete over every normative document of the family** — twenty-five documents,
roughly 280 invariants. Part 0 is non-normative and states no requirement of a governed system; `8a`
and this document are the annex.

`1c` is recorded as partial deliberately: ten of its seventeen invariants are restated by documents
mapped elsewhere, and re-deriving them here would put one fact in two places. `1c` is recorded as partial deliberately: ten of its
seventeen invariants are restated by documents already mapped, and re-deriving them here would put
one fact in two places.

**Part II changed the character of the map.** Its documents produced few new findings and
**adjudicated** many existing ones — MB-1 splitting 6/8/12 from 19, CA-8 confirming 19 a third time,
GO-11 and CA-6 supplying the requirement finding 16 rests on, GS-6 settling the `governed_by` cycle,
and `2a` §6.1 escalating finding 4 into the reflexivity term. A document that settles what an earlier
finding *is* earns its place as much as one that finds something new, and by Part II most of what was
left to learn was of that kind.

**Thirty-six findings, thirty-five against the realization and one against a document.** The
prediction on opening the second batch was that documents specifying subjects the realization
approached *without* a specification would begin yielding findings against the documents instead.
**That prediction was wrong twice, in opposite directions.**

- `3e` Evidence was the strongest candidate and did not invert: its four findings are all things the
  realization could carry and does not. What it exposed instead was a **naming collision** —
  `snapshot/evidence/` is an evidence *view* under `4b` §10 and contains no evidence under `3e` §3 —
  the "distinctions that were conflated" case `0z` §3 describes, resolved in the realization's
  vocabulary rather than the standard's.
- Part VI was the second candidate. `6c` Domain Profiles came out the **best-satisfied document in
  the map** — nine of eleven demonstrated, including DP-7, where the realization independently built
  the exact prohibition the family states. `6a` in the same part produced the two most consequential
  findings in the whole map.

**What that leaves is a caution about the map's own method.** "Approached without a specification"
does not predict where a realization will be found wanting; the realization got domain boundaries
right and profiles wrong, and nothing about the absence of a specification distinguished the two in
advance. The findings are worth what the evidence behind each one is worth, and no more.

**One finding against a document in thirty-six is itself a result, and it should be read carefully.**
It is weak evidence that the documents are sound and strong evidence that this map is examining the
realization rather than the family — which is its stated direction (`0z` §3) and also its limitation.
A second, independent realization is what would test the documents, and `8a` §2 says as much.

## 30. Probes

Findings read out of code are hypotheses. These were run against copies; no repository and no sealed
snapshot was modified, and the composition verified unchanged afterwards at `7b6f2699…`.

**One of the three changed a finding and one withdrew a claim.** That is the reason to run them:
`4b` §14 and `3b` §15 both say the same thing in their own subjects — the property is established by
doing the thing, not by reading the mechanism that was supposed to prevent it.

### 29.1 Tamper — finding 2

A copy of the sealed snapshot; one canonical artifact's `content` rewritten so that the workflow
declares a governing constitution that does not exist; `content_hash` and every `metadata.json` left
untouched.

```
sha256(content) == recorded content_hash     True before, False after
verify_snapshot(tampered)                    ACCEPTED — snapshot_id 7b6f2699… unchanged
runtime boot                                 "Warm reboot complete — snapshot resident + hash-verified"
                                             "✓ Snapshot healthy … No issues."
```

A second tamper, on the projection the runtime actually routes on — a capability transform's
`handler_ref.module` in `tokenized/workload/handlers.json` rewritten to a module that does not exist
— was likewise accepted, boot-verified and reported healthy. Executing the workflow then returned
`VIOLATION` at the step that reached the missing module.

**Confirmed as stated, with one qualification worth carrying.** The runtime refused; acceptance did
not. `3b` §7 requires integrity to be established *before anything executes against* the snapshot,
and here execution began, produced a trace, and failed partway. The tamper chosen names a module that
does not exist; one naming a different **admitted** transform would resolve and run, and nothing in
acceptance distinguishes the two cases.

### 29.2 Relocation — finding 15

Two copies of the collatz workload, compiled by `compile_domain.sh` into their own roots. In one,
`WF_COLLATZ_CONJECTURE_V0.md` moved from `registry/workflows/` to `registry/intents/` — filename and
declaration untouched. Both builds: 27 artifacts materialized, verified, attested.

```
graph_address_hash          SAME      b4928bc4af541c70…
graph_topology_hash         SAME      57187e3af3041601…
tokenized_projection_hash   SAME      169a22fd3ed46d9d…
attestation_hash            SAME      a40dc71272a97398…
canonical_projection_hash   CHANGED   312ecf9de1694f23…  →  5a8688718750bb88…

fqdn_id       workload::WF_COLLATZ_CONJECTURE_V0   unchanged
content_hash  5004ff30ea43302a…                    unchanged
module_path   workload.registry.workflows          →  workload.registry.intents
```

**The finding was sharpened by the probe.** What had been written as a discovery-filter defect is one
location-derived field, and the probe located it exactly.

### 29.3 Rename — the claim that was withdrawn

Same workload, `CT_PURE_TERMINATION_CHECK_V0.md` renamed to `ct_pure_termination_check.md`, out of
the discovery `filename_pattern`, declaration untouched.

```
S2_CANONICALIZE failed with 1 error(s):
  E104_INVALID_FQDN: Dangling reference: workload::CC_VERIFY_TERMINATION_V0
      → workload::CT_PURE_TERMINATION_CHECK_V0 (target not found in graph or imported surface)
Build Summary: 0 succeeded, 1 failed
```

**Refused.** The claim that a renamed artifact is silently dropped does not survive: referential
closure catches it, and there is no artifact in the workload — and no platform invariant — that
nothing references. The claim is withdrawn and the hazard recorded in §8.1.1 with its exposure
condition.

### 29.4 Representation — finding 23

Same workload. Two sibling keys swapped inside one artifact's machine block:

```yaml
version: v0                                              governed_by: fb.actor::CONSTITUTION_…
governed_by: fb.actor::CONSTITUTION_…        →           version: v0
```

A YAML mapping is unordered, so this is a representation change that preserves meaning exactly —
verified by parsing both and comparing: `parsed YAML identical: True`.

```
frontmatter (the parsed semantic object)   SAME
fqdn_id                                    SAME
graph_address_hash                         SAME
tokenized_projection_hash                  SAME
attestation_hash                           SAME

content_hash                 CHANGED   50ebd849b9609505… -> 5a96684ae1b93708…
graph_topology_hash          CHANGED   57187e3af3041601… -> c5427043d1f53209…
canonical_projection_hash    CHANGED   312ecf9de1694f23… -> 431339a51c2ed3f0…
```

The build succeeded and reported 27 artifacts materialized, verified and attested — as it should:
nothing is wrong with the artifact. What moved is the identity of the composition containing it.

**Three documents fail on one observation** — MB-3 (integrity over a canonical form of the semantic
object), ID-3 and KV-8 (a meaning-preserving representation change must not change identity). The
semantic object is provably unchanged in the same output that shows the hash moving.
