# WORKED_EXAMPLE_PLATFORM_V0 — draft

```yaml
completion:
  status: draft
  generated_from: scope sheet
  open_gaps: 5
  usable_as_a_target: false   # a profile with an open gap is not yet something to hand anyone
```

A snapshot profile is a conformance contract over an assembled snapshot. It states the properties a
snapshot SHALL satisfy — not an inventory of what any particular build contains. A snapshot may
contain more than this profile requires and still conform.

Generated from a scope sheet. Sections marked GAP were not generated and must be written before this
profile is handed to anyone as a target.

## 1. Profile

```yaml
snapshot_profile:
  identity: WORKED_EXAMPLE_PLATFORM_V0
  supersedes: null
  derives_from: null
  description: 'A governance surface with one conformance workload and two tool domains,
    assembled without business domains. Single node, unsigned, locally stored. Declares
    the governed boundary contracts and exercises none of them.

    '
  required_domains:
  - platform
  excluded_domains: []
  declared_domains:
  - platform
  - workload
  - inspection
  - transformation
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
  result_classes: none
  projections:
  - canonical_form
  - kind_index
  - identity_index
  - store_index
  trust_root: 'None. Evidence is self-asserted and integrity is recomputed from constituent
    bytes at acceptance rather than compared to a recorded value. A checking party
    that requires more than self-assertion is not served by this platform, and that
    is a limit rather than an oversight.

    '
  evidence_retention: 'Indefinite. Evidence is written into the sealed snapshot and
    into per-run traces, and nothing removes either. The period a determination can
    be established is therefore unbounded, which is the cheap answer for a single-node
    platform with no storage pressure.

    '
  read_surface:
    openness: 'Nobody outside the system. Reads are issued by an operator tool running
      on the same host; there is no caller class to admit because there is no caller.

      '
    reads_attributed: false
    reach: 'A local read tool, run by an operator against the assembled snapshot on
      the same host. It reads projections and never internals.

      '
  sufficiency_criterion: 'A design is sufficient when every fact the construction
    step needs is fixed by a declaration rather than supplied at build time. Construction
    refuses — it does not fill, default, or infer — where a required field is unfixed,
    and the refusal names the field and the phase that should have fixed it.

    '
  interaction_forms_governed: not_applicable
  protocol_bindings_governed: not_applicable
  genesis_discharge: 'The first snapshot is discharged by recomputing its integrity
    from constituent bytes and by the composition conformance rules passing over the
    whole. What is NOT discharged is CD-14: this profile was authored by the same
    authority that built the system it governs, so the genesis claim''s externality
    demonstration fails and is recorded as failing.

    '
  required_governance:
    artifact_kinds:
    - CONSTITUTION
    - INVARIANT
    - STRUCTURE
    - VOCABULARY
    - SURFACE_CONTRACT
    - CAPABILITY_TRANSFORM
    - CAPABILITY_SIDE_EFFECT
    artifacts: []
  required_domain_profiles:
  - domain: platform
    claims: authority
  - domain: workload
    claims: concern
  - domain: inspection
    claims: concern
  - domain: transformation
    claims: authority
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
```

## 2. Required governance artifacts

> **GAP — to be written by the author.** `required_governance.artifacts` above is empty.

A profile references governed identities — namespaces and artifact identities — and never filesystem
paths, repository names, or module paths. The identities cannot be generated from a scope sheet
because they do not exist until the artifacts are authored. Name here the artifacts whose absence
would mean a snapshot is not this platform.

## 3. Additional obligations

> **GAP — to be written by the author.**

For each obligation beyond what §1 selects, state **what would establish a breach**. An obligation
nothing could refuse is not in force, and one that restates a selection in §1 is not additional
(NP-6).

## 4. Claims and their discharge

> **GAP — to be written by the author.** §1 names 3 claim(s) and says nothing about what settles them.

For each: what discharges it, which discharge class that is, and a demonstration **capable of
failing** if the system were non-conforming (CD-4). A claim with no stated discharge is decorative.

## 5. Derivation

> **GAP — to be written by the author.**

If this profile derives from another, name the base **by identity** and state that this profile does
not widen it (NP-10). If it derives from none, delete this section — an absent section is clearer
than one saying "none".

## 6. Externality

NP-7 requires a profile to be external to what it governs, and **externality is authorship, not
storage**. A profile written by the authority that builds the system is not external, whatever
directory it is kept in.

State which case applies here. Where the same authority wrote both, a conformance claim under this
profile must record that — a finding against the claim, not against the profile.

## 7. Scope rules

- Profile scope changes are new identities (`_V0` → `_V1`), never in-place edits (NP-9).
- A profile that has not been read against a candidate snapshot MUST NOT be handed to anyone as a
  target. Running the check is a precondition of use.
