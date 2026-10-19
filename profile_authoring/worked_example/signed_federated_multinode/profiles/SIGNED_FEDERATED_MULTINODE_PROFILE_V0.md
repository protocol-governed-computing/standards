# SIGNED_FEDERATED_MULTINODE_PROFILE_V0 — draft

```yaml
completion:
  status: authored
  generated_from: scope sheet, gaps closed by the author
  open_gaps: 0
  usable_as_a_target: false   # gaps are closed; this profile has not yet been read against a
                              # candidate snapshot, which §7 makes a precondition of use
```

A snapshot profile is a conformance contract over an assembled snapshot. It states the properties a
snapshot SHALL satisfy — not an inventory of what any particular build contains. A snapshot may
contain more than this profile requires and still conform.

Generated from a scope sheet. Sections marked GAP were not generated and must be written before this
profile is handed to anyone as a target.

## 1. Profile

```yaml
snapshot_profile:
  identity: SIGNED_FEDERATED_MULTINODE_PROFILE_V0
  supersedes: null
  derives_from: GOVERNANCE_SURFACE_PROFILE_V0
  description: Signed Federated Collatz Platform
  required_domains:
  - platform
  - inspection
  excluded_domains: []
  declared_domains:
  - platform
  - transformation
  - workload
  - inspection
  namespaces:
    form: <namespace>::<ARTIFACT_IDENTITY>
    declared:
    - actor
    - artifact
    - authority
    - capability_contracts
    - capability_side_effects
    - capability_transforms
    - compiler
    - conformance
    - cryptographic_trust
    - event
    - execution
    - execution_placement
    - execution_scheduling
    - execution_topology
    - federation
    - governance
    - inspection
    - intent
    - lifecycle
    - runtime_binding
    - security_domain
    - structure
    - surface_contract
    - trace
    - transformation
    - transport
    - vocabulary
    - workflow
    - workload
    closed: true
    derives_concern: false
    derives_authority: false
  declared_vocabulary:
    kinds:
    - kind: CONSTITUTION
      governance_assertion: required
    - kind: INVARIANT
      governance_assertion: required
    - kind: ASSERT
      governance_assertion: required
    - kind: STRUCTURE
      governance_assertion: required
    - kind: VOCABULARY
      governance_assertion: required
    - kind: SURFACE_CONTRACT
      governance_assertion: required
    - kind: CAPABILITY_CONTRACT
      governance_assertion: required
    - kind: CAPABILITY_TRANSFORM
      governance_assertion: required
    - kind: CAPABILITY_SIDE_EFFECT
      governance_assertion: required
    - kind: RUNTIME_BINDING
      governance_assertion: required
    - kind: WORKFLOW
      governance_assertion: required
    - kind: INTENT
      governance_assertion: required
    - kind: ACTOR
      governance_assertion: required
    - kind: EVENT
      governance_assertion: required
    - kind: TRANSPORT_INGRESS
      governance_assertion: required
    - kind: TRANSPORT_EGRESS
      governance_assertion: required
    aliases_accepted: false
  declared_outcomes:
  - succeeded
  - refused
  - not_applicable
  - failed
  result_classes: accepted, refused, invalid, unavailable
  projections:
  - canonical_form
  - kind_index
  - identity_index
  - store_index
  trust_root: 'A single operator-held signing key. A checking party accepts that key
    without asking for anything further, and every attestation chain terminates in
    it.

    The private half is held by the operator on the build machine and is never present
    on any node that executes workflows. Each node carries the public half only —
    enough to verify a snapshot manifest''s signature and to refuse a copy that does
    not verify, and not enough to produce one. A node can therefore establish that
    the snapshot it holds is the one, and cannot mint one its peers would accept.

    Custody of that key is part of what every claim this platform makes rests on.
    It was chosen over per-node keys because per-node keys give each node something
    of its own to vouch with, which pulls toward the multiple-authority model this
    platform declined.

    '
  evidence_retention: 'A fixed window of five days, measured from the close of the
    trace the evidence belongs to. The clock is read through the platform''s governed
    clock side effect, not off a host, so the origin of the period is itself an accounted
    act.

    What terminates it is an act, not a lapse: evidence past its window is deleted
    by a declared capability side effect. The record of that deletion is exempt from
    the window and retained indefinitely — otherwise the platform would eventually
    be unable to distinguish evidence that was deleted from evidence that was never
    written.

    An attestation expires with its subject. Nothing outlives what it vouches for,
    so the platform never retains a signed statement about a determination whose evidence
    is gone. The alternative was available and was declined: such a statement is a
    claim rather than a proof, and keeping one after its subject would invite it to
    be read as the evidence it is not.

    The consequence is stated plainly because it is the point of the answer: after
    five days a determination becomes unestablishable. It was governed when it was
    made and does not become ungoverned, but no claim about it can be checked thereafter.
    Any audit obligation longer than five days is not served by this platform.

    Evidence outlives the node that produced it. A worker writes to a store that survives
    it, so retiring or replacing a container destroys no evidence and shortens no
    window. This also means a single expiry process against a single clock: node-local
    traces would have given N expiry processes whose clock skew would make nodes disagree
    about what still exists.

    The window is declared in the snapshot, on the expiry side effect itself, and
    is not an environmental parameter. Changing it is therefore a recompile: a new
    snapshot identity and a declared supersession, never an operator editing a value.
    This follows from the trust root rather than from retention: a checking party
    who verifies a signed snapshot must be able to read off that same snapshot how
    long its evidence lives. Were the window environmental, the signature would cover
    the evidence but not the rule governing its life, and the audit reach could be
    shortened without any declared act.

    Evidence storage placement remains a constraint on the environment rather than
    on governance: the evidence store must be reachable, and a node that cannot reach
    it does not begin execution (see B1).

    '
  read_surface:
    openness: 'Named classes of caller: operator, client, checking party.

      An operator may issue every declared read. A client may read its own submissions
      and their results, and nothing else. A checking party may read evidence, attestations
      and the snapshot manifest, and submits nothing — it exists because the trust
      root in A6 is addressed to somebody, and a platform whose evidence can only
      be verified from inside the host has a trust root that serves nobody outside
      it.

      Each read is decided when it is issued. Admitting a class fixes the policy;
      it does not dispense with the determination (5b §11), and a read this platform
      answers without determining it would be an ungoverned read path whatever this
      field says.

      '
    reads_attributed: true
    reach: 'Not applicable — an interaction boundary is selected, and the read surface
      is reached across it. A checking party issues declared read operations remotely
      through governed ingress and egress, exactly as a client does; verification
      requires no access to the host and no operator tooling. This is what makes the
      trust root in A6 serve a party outside the platform rather than only its operators,
      and it requires the read surface itself to be present in the snapshot as governed
      ingress and egress contracts (see C1b).

      '
  sufficiency_criterion: "A design is sufficient to build from when all of the following\
    \ are determinable from the declarations alone, without recourse to a convention,\
    \ a default, or an implementation:\n\n  - every capability contract declares its\
    \ complete outcome vocabulary, and the traversal\n    declares routing for every\
    \ outcome in it;\n  - every workflow reaches a terminal state on every declared\
    \ outcome;\n  - every reference resolves inside a declared namespace, the set\
    \ of which is closed (A5);\n  - every capability side effect names the state it\
    \ writes and what else may write it;\n  - an artifact of every kind required by\
    \ A1b is present;\n  - wherever the order of two effects matters, the declarations\
    \ state that order.\n\nThe last is here because of how this platform is deployed.\
    \ Distribution introduces no ordering ambiguity; it reveals one already present\
    \ (6b §8.2). An unstated ordering is invisible on a single node and becomes non-deterministic\
    \ across worker nodes, so the construction boundary is the only place it can be\
    \ caught before it becomes an intermittent defect nobody can reproduce.\nRefusal\
    \ names the unmet criterion and the artifact that failed it, and nothing is built.\
    \ Construction does not warn and proceed: a warning fills the gap with an assumption,\
    \ which is the failure this criterion exists to prevent.\n"
  interaction_forms_governed: 'Yes. What arrives at the boundary is declared as a
    transport ingress artifact and admitted like any other, never whatever the receiving
    code happens to parse. TRANSPORT_INGRESS is required by A1b, so a snapshot without
    one is not this platform.

    '
  protocol_bindings_governed: 'Yes. HTTP is a declared binding rather than an assumption
    in code. Ingress and egress contracts are protocol-neutral: they state what crosses,
    not how it is carried, and substituting a different carrier is a change to a declaration
    rather than to an implementation. Answering no would have made HTTP this platform''s
    semantics by accident — the same failure the result classes in A3 avoid by refusing
    status codes.

    '
  genesis_discharge: 'Two parts, one discharged and one not.

    Integrity is discharged by the trust root. The first snapshot''s manifest is signed
    under the operator key in A6, and every node verifies that signature before executing,
    so the platform can establish that the snapshot it runs is the one sealed and
    that no node holds a divergent copy under the same identity.

    Independence is not discharged, and this is recorded as a gap rather than argued
    away. This profile is written by the same party that authors the platform claiming
    it, and the governance surface it derives from has the same author. A self-signed
    genesis establishes that the operator vouches for the operator; per 3e §6.1 that
    transfers the question to the attesting party rather than answering it. Any checking
    party who requires the profile to have been written independently of what it governs
    is not served by this genesis, and that limit is stated here rather than discovered
    later.

    '
  environment_supplied_values: none
  partial_application: 'No transition is resumed after partial application, so none
    is ever partly applied and then continued elsewhere. Work re-dispatched after
    a node is lost is work that had not begun (B1); begun work is not moved, and its
    run refuses.

    This is what makes the answer available rather than aspirational. A lost node
    is a realization applying a transition partly, and SM-7a would oblige this platform
    to determine the resulting state and SM-10 to hold across the re-execution. Neither
    obligation is engaged where nothing is resumed.

    The alternative was available and declined: making every reachable effect re-appliable
    without changed effect would let begun work move too. It would also be a change
    to the governance surface this platform derives from, which this profile does
    not undertake.

    '
  required_governance:
    artifact_kinds:
    - CONSTITUTION
    - INVARIANT
    - STRUCTURE
    - VOCABULARY
    - SURFACE_CONTRACT
    - CAPABILITY_CONTRACT
    - CAPABILITY_TRANSFORM
    - CAPABILITY_SIDE_EFFECT
    - RUNTIME_BINDING
    - WORKFLOW
    - INTENT
    - ACTOR
    - EVENT
    - TRANSPORT_INGRESS
    - TRANSPORT_EGRESS
    artifacts: []
  required_domain_profiles:
  - domain: platform
    claims: authority
  - domain: transformation
    claims: authority
  - domain: workload
    claims: concern
  - domain: inspection
    claims: concern
  required_self_description:
    manifest_declares_profile: true
    manifest_declares_identity_coverage: true
    covered_set_excludes_the_value: true
  required_workloads:
    entry_workflows: []
  required_claims:
  - SNAPSHOT_IMMUTABILITY
  - DETERMINISTIC_EXECUTION
  - COMPILED_INVOCATION_RESOLUTION
  - SIGNED_SNAPSHOT_VERIFICATION
  - EVIDENCE_EXPIRY
```

## 2. Required governance artifacts

A snapshot missing any of the following is not this platform. Each is named by governed identity;
none is a path, a repository, or a module.

**The governing constitutions.**

- `governance::CONSTITUTION_GOVERNANCE_V0`
- `governance::CONSTITUTION_INVARIANTS_V0`
- `governance::INVARIANT_GOVERNANCE_DECLARATION_RESOLVES_V0`

Without these nothing is governed, and every other requirement below is unenforceable.

**The constitutions this platform's own decisions rest on.** Each is required because a decision in
§1 depends on it, and a snapshot carrying the decision without the constitution would assert
something nothing governs.

| Identity | The decision that requires it |
|---|---|
| `cryptographic_trust::CONSTITUTION_CRYPTOGRAPHIC_TRUST_V0` | the trust root, and the signature every node verifies before executing |
| `federation::CONSTITUTION_FEDERATION_BOUNDARY_V0` | one authority across many nodes, and the line between internal transport and a governed boundary |
| `execution_placement::CONSTITUTION_EXECUTION_PLACEMENT_V0` | nodes as placement rather than authority |
| `execution_topology::CONSTITUTION_EXECUTION_TOPOLOGY_V0` | the node roles and their reachability |
| `execution_scheduling::CONSTITUTION_EXECUTION_SCHEDULING_V0` | dispatch to workers, and re-dispatch restricted to un-started work |
| `transport::CONSTITUTION_ADMISSION_V0` | admission at the interaction boundary, on which the caller classes depend |

**One artifact this profile requires and no snapshot yet carries.**

- an identity in `capability_side_effects` that performs evidence expiry, declaring the five-day
  window, exempting its own deletion record, and expiring an attestation with its subject.

It is named as a requirement rather than as an existing artifact. Retention is a governed
consequence and its terminating act is an act: a platform that lets evidence lapse without a
declared side effect has discarded evidence by omission, and this profile would admit a snapshot
that did so. The requirement stands whether or not the artifact has been authored, which is what
makes this profile capable of refusing the platform its own author is building.

## 3. Additional obligations

Five obligations beyond what §1 selects. Each states what would establish a breach, because an
obligation nothing could refuse is not in force.

**OB-1 — No node executes an unverified snapshot.** Every node verifies the snapshot manifest's
signature against the public half of the trust root before executing anything from it, and refuses
where verification fails.
*Breach:* a node observed executing a workflow from a snapshot whose manifest signature does not
verify, or whose manifest carries no signature.

**OB-2 — No executing node can sign.** The private half of the trust root is absent from every node
that executes workflows.
*Breach:* the private half present on any node able to execute a workflow, whether or not it was
used. Possession is the breach; a node that can sign can mint a snapshot its peers would accept.

**OB-3 — Evidence is not held by the node that produced it.** The evidence store is reachable by
every node and held by none.
*Breach:* evidence for a determination readable only from the node that made it, or destroyed by
that node's removal.

**OB-4 — Re-dispatch never resumes a begun step.** Work re-dispatched after a node is lost is work
that had not begun.
*Breach:* a step re-executed on a second node after any part of its transition was applied on the
first. SM-7a then obliges this platform to determine the resulting state, and it declares none.

**OB-5 — Only the boundary node is externally reachable.** No node other than the one serving the
interaction boundary is addressable from outside the node group.
*Breach:* a caller reaching a worker, a coordinator, or the evidence store without passing the
declared ingress. Such a caller has bypassed admission, and the caller classes in §1 no longer
describe who reached what.

## 4. Claims and their discharge

Each claim below names a demonstration capable of failing. A demonstration that cannot fail supports
a claim nobody can evaluate.

**SNAPSHOT_IMMUTABILITY** — *discharge class: inspection.* Read the sealed snapshot, alter one
constituent, and read it again: the altered copy must be refused rather than accepted under the same
identity. *Fails if* a modified snapshot is admitted under the identity it claims.

**DETERMINISTIC_EXECUTION** — *discharge class: execution.* Execute the same workflow against the
same governed state on two different nodes and compare determinations. *Fails if* the
determinations differ. Note what this specifically tests here: SM-10 across nodes, not merely
across runs.

**COMPILED_INVOCATION_RESOLUTION** — *discharge class: construction.* Assemble a snapshot and
confirm every invocation resolves within it, then attempt execution with a reference resolvable
only at run time. *Fails if* anything routes at run time that was not resolved at build time.

**SIGNED_SNAPSHOT_VERIFICATION** — *discharge class: execution.* Present a node a snapshot whose
manifest signature does not verify against the trust root. *Fails if* the node executes from it.
This is the demonstration OB-1 and OB-2 exist to make possible, and no profile in this family that
declines a trust root can perform it.

**EVIDENCE_EXPIRY** — *discharge class: inspection.* Advance the governed clock past five days from
a trace's close and attempt to establish the determination that trace evidenced. *Fails if* the
determination remains establishable, **or** if no record of the deletion survives. Both halves
matter: evidence that outlives its window breaks the claim, and evidence that vanishes without a
record makes deletion indistinguishable from never having written.

**Every discharge above is itself checkable for five days only.** §1 fixes that window, and a claim
outliving the evidence that would settle it is not discharged but merely asserted.

## 5. Derivation

This profile derives from `GOVERNANCE_SURFACE_PROFILE_V0`, named by identity.

It **does not widen** that base (NP-10): every selection the base makes is made here, and this
profile only requires more. Where this profile and its base disagree about what a snapshot must
satisfy, this profile requires the stricter of the two, and a snapshot conforming here conforms
there.

Deriving does not make the base privileged and does not make this profile subordinate to it (6a
§11). The relation is declared by this profile, and the base makes no claim on profiles that have
not named it.

### 5.1 What was derived from, exactly

Naming a base profile by identity says which contract was derived from. It does not say which
*surface* — and a platform that clones a repository at whatever its development branch happens to be
has derived from something nobody can name twice. The four pins below are what make the ancestry
checkable rather than merely stated.

| Pin | Value | Why this one |
|---|---|---|
| toolchain | `protocol-governed-computing==4.0.0` | the published distribution; the implementations, not the declarations |
| governance surface | `software_governance` @ `v4` | the base profile's own surface — its constitutions and invariants are what deriving inherits |
| conformance workload | `conformance_workloads` @ `v4` | supplies required kinds, not a required domain (§1) |
| read surface | `snapshot_inspector` @ `v4` | required as a domain (§1); carries the ingress and egress a checking party reads through |

The three repositories are pinned to one tag rather than to three, because they compose. A wheel at
`4.0.0` against declarations from a later development branch is the incoherence pinning exists to
prevent: the implementations would be one composition's and the declarations another's, and nothing
would report the mismatch.

`v4` is named because it is the **published** tag, resolvable by anyone cloning the repositories. A
development tag that exists only on the machine that built the platform is not a pin: it names a
commit nobody else can reach, and a pin nobody can resolve records nothing.

**This platform does not track its base.** A fix or an addition made to the surface after this tag
does not reach a snapshot built from these pins, and reaching it is a deliberate act: a new pin, a
rebuild, a new snapshot identity. That is the cost of decoupling, accepted rather than regretted — a
platform that silently follows a branch has no reproducible ancestry to declare.

### 5.2 Derivation is not lineage

This profile derives from `GOVERNANCE_SURFACE_PROFILE_V0` and **supersedes nothing** (§1,
`supersedes: null`). The two relations hold between different objects and are easily confused:

- **Derivation** relates *profiles*: this one names a base and does not widen it.
- **Supersession** relates *claims*: a superseding profile states what it changes and what that
  invalidates (4e).

Superseding the base was considered and is incorrect, not merely undesirable. This profile
invalidates nothing about the platform that claims the base — that platform still requires it, and
replacing it would orphan a live claim. There is nothing to invalidate, so there is nothing to
supersede.

A snapshot built under this profile is therefore a **genesis snapshot**: it has no predecessor
snapshot, and its legitimacy is settled by §1 `genesis_discharge` rather than by comparison with one.
Carrying a governance ancestry and having no predecessor are consistent — ancestry is a relation
between profiles, lineage a relation between snapshots.


## 6. Externality

NP-7 requires a profile to be external to what it governs, and **externality is authorship, not
storage**. A profile written by the authority that builds the system is not external, whatever
directory it is kept in.

**The same authority wrote both, and this profile is therefore not external to what it governs.**

The party that authored this profile authors the platform claiming it and the governance surface it
derives from. NP-7 is not satisfied, and no wording here can satisfy it: externality is authorship,
and authorship is already settled.

The consequence is recorded rather than mitigated. Any conformance claim made under this profile
carries this as a finding against the claim — not against the profile, which is sound, and not
against the platform, which may well conform. What cannot be established is that the target was set
by someone other than the party meeting it.

Closing it requires a second party to author the profile against which this platform is checked.
Until then every claim in §4 rests on a demonstration the claimant designed.

## 7. Scope rules

- Profile scope changes are new identities (`_V0` → `_V1`), never in-place edits (NP-9).
- A profile that has not been read against a candidate snapshot MUST NOT be handed to anyone as a
  target. Running the check is a precondition of use.
