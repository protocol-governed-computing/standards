# Worked example — the reference composition

The scope sheet answered for a platform that already exists: the reference realization's governance
surface, one conformance workload, two tool domains, nothing crossing a boundary. Answering backwards
from a built system is the only way to check that the questions reach what a real platform actually
decided.

**Read the notes, not just the answers.** Where a decision could have gone the other way, one
sentence on why it went this way is what makes a profile reviewable rather than merely followed.

## Answers

```yaml
scope_sheet:
  platform_name: >
    A governance surface with one conformance workload and two tool domains, assembled without
    business domains. Single node, unsigned, locally stored. Declares the governed boundary
    contracts and exercises none of them.
  profile_identity: WORKED_EXAMPLE_PLATFORM_V0

  # A — meaning
  kinds:
    - CONSTITUTION
    - INVARIANT
    - ASSERT
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
  aliases_accepted: false
  kinds_required_exercised:
    - CONSTITUTION
    - INVARIANT
    - STRUCTURE
    - VOCABULARY
    - SURFACE_CONTRACT
    - CAPABILITY_TRANSFORM
    - CAPABILITY_SIDE_EFFECT
  outcomes: [succeeded, refused, not_applicable, failed]
  result_classes: none
  projections: [canonical_form, kind_index, identity_index, store_index]
  namespaces:
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
  namespaces_closed: true
  trust_root: >
    None. Evidence is self-asserted and integrity is recomputed from constituent bytes at
    acceptance rather than compared to a recorded value. A checking party that requires more than
    self-assertion is not served by this platform, and that is a limit rather than an oversight.
  evidence_retention: >
    Indefinite. Evidence is written into the sealed snapshot and into per-run traces, and nothing
    removes either. The period a determination can be established is therefore unbounded, which is
    the cheap answer for a single-node platform with no storage pressure.
  read_openness: >
    Nobody outside the system. Reads are issued by an operator tool running on the same host; there
    is no caller class to admit because there is no caller.
  reads_attributed: false
  sufficiency_criterion: >
    A design is sufficient when every fact the construction step needs is fixed by a declaration
    rather than supplied at build time. Construction refuses — it does not fill, default, or infer —
    where a required field is unfixed, and the refusal names the field and the phase that should
    have fixed it.
  interaction_forms_governed: not_applicable
  protocol_bindings_governed: not_applicable
  read_surface_reach: >
    A local read tool, run by an operator against the assembled snapshot on the same host. It reads
    projections and never internals.
  genesis_discharge: >
    The first snapshot is discharged by recomputing its integrity from constituent bytes and by the
    composition conformance rules passing over the whole. What is NOT discharged is CD-14: this
    profile was authored by the same authority that built the system it governs, so the genesis
    claim's externality demonstration fails and is recorded as failing.

  # B — environment
  nodes: One machine.
  co_location_rules: None stated. Everything runs in one process on one host.
  resource_guarantees: None stated.
  deadlines: None stated.
  isolation: >
    None stated. The snapshot is stored unencrypted on a local filesystem; no separation mechanism
    is required and none is claimed.
  failure_visibility: >
    A step fails, the workflow refuses, and the refusal is evidenced. There is no partial-failure
    mode because there is no second participant.
  distribution: None — single node.
  declared_environment_facts: []
  environment_excludes: >
    Any system requiring more than one participant, a bounded latency, or a separation mechanism.
    None of the three is provided and none is claimed.
  environment_claims: []

  # C — composition
  domains:
    - name: platform
      owns: the governance surface — constitutions, invariants, structures, and the capability vocabulary
      governed_by: its own constitutions — this domain is the governing authority
      reached_by: [platform capability contracts]
      ordered_by: [platform workflows]
      state: [the compiled governance projections]
      exposed: nothing — no boundary is exercised
      authority_claim: authority
    - name: workload
      owns: one conformance workload and its storage
      governed_by: the platform surface's constitutions and invariants
      reached_by: [workload capability contracts]
      ordered_by: [workload workflows]
      state: [workload results]
      exposed: nothing
      authority_claim: concern
    - name: inspection
      owns: read operations about a snapshot
      governed_by: the platform surface's constitutions, and the inspection boundary contracts
      reached_by: [inspection capability contracts]
      ordered_by: [inspection workflows]
      state: []
      exposed: nothing
      authority_claim: concern
    - name: transformation
      owns: the design and construction lifecycle
      governed_by: its own design and construction constitutions, under the platform surface
      reached_by: [transformation capability contracts]
      ordered_by: [transformation workflows]
      state: [design phase records]
      authority_claim: authority
      exposed: nothing
  required_domains: [platform]
  excluded_domains: []
  entry_points: []
  boundary: declared, nothing crosses
  claims:
    - SNAPSHOT_IMMUTABILITY
    - DETERMINISTIC_EXECUTION
    - COMPILED_INVOCATION_RESOLUTION
```

## Why the answers went this way

**A3 result classes — none.** Nothing calls in, so there is nothing to classify. Answering with a
list here would have been the commonest error the sheet is built to catch: a result-class set
authored in advance of any caller ends up mirroring whichever protocol is imagined, and the
imagined protocol becomes the semantics.

**A6 trust root — none.** The tempting answer is "the snapshot hash". It is wrong: a hash establishes
that bytes did not change and says nothing about who vouched for them. Naming the absence is the
honest answer and it costs a claim rather than hiding one.

**A14 genesis — discharged in part, and the failing part recorded.** The externality demonstration
cannot succeed here, because the same authority wrote the profile and the system. Recording that is
worth more than a claim that would not survive being checked.

**B5 isolation — none stated.** Encryption at rest would be tempting to write into Section A as a
governance property. It is not one: no governed result depends on whether the bytes at rest are
encrypted, so it is an environment constraint or it is nothing.

**C2 authority claims.** `platform` and `transformation` each make a decision no other domain may —
what is admitted, and what counts as sufficient to build. `workload` and `inspection` make none;
they are concerns governed under the surface, which is the ordinary arrangement and not a demotion.

**C3 entry points — none required.** The reference composition runs a conformance workload, but
requiring its workflow by identity would make the workload a condition of being this platform. That
is the coupling this profile deliberately does not create: a workload is composed like any other
domain, and a platform that requires one by name cannot admit a second without a new identity.

**A1b required kinds — seven of the sixteen.** The first answer given was all sixteen, and it was
wrong: the composition admits `ASSERT` and carries no artifact of that kind, so requiring it failed a
snapshot that was conforming. Admitting a kind and requiring it are different questions, and only the
seven above are ones whose absence would mean this is not the platform.

**C1b required domains — one, not four.** The composition has four domains; only `platform` is
required. A snapshot without the governance surface is not this platform; a snapshot without the
workload is this platform with nothing composed onto it. Listing all four would have turned one
build's inventory into everyone's requirement — the same mistake as A1b, in a second place.

**C5 claims — three, and a fourth deliberately absent.** Protocol independence is not claimed. It
asserts stability across wire protocols, and this platform exercises none; a claim discharged by a
substitution that cannot be performed is not discharged.
