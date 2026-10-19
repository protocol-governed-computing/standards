# Governance surface — scope sheet

A platform that is a governance surface and its tool domains, and nothing else. No conformance
workload, no business domain, nothing crossing a boundary, one machine.

**It is written to be derived from.** A profile derived from this one may require more and permit
less, never the reverse — so this one asks for as little as a platform can coherently ask for. Adding
a workload here would make the workload a requirement on everything that derives from it, which is
the coupling this profile exists to avoid.

**It is not a floor and it is not privileged.** Minimality is relative to a profile and no profile is
more basic than another. This is one platform, stated plainly, that happens to be undemanding.

## Answers

```yaml
scope_sheet:
  platform_name: >
    A governance surface with its two tool domains — inspection and transformation — assembled with
    no conformance workload and no business domain. One machine, unsigned, locally stored. The
    governed boundary contracts are declared and none is exercised.
  profile_identity: GOVERNANCE_SURFACE_PROFILE_V0
  derives_from: none

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
  result_classes: none — no boundary is exercised
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
  namespaces_closed: true
  trust_root: >
    None. Evidence is self-asserted, and integrity is recomputed from constituent bytes at
    acceptance rather than compared against a recorded value. A checking party requiring more than
    self-assertion is not served by this platform. A derived profile may name a real root; this one
    does not, so that it does not oblige every derivation to have one.
  evidence_retention: >
    Indefinite. Evidence is written into the sealed snapshot and into per-run traces, and nothing
    removes either.
  read_openness: >
    Nobody outside the system. Reads are issued by an operator tool on the same host; there is no
    caller class to admit because there is no caller.
  reads_attributed: false
  sufficiency_criterion: >
    A design is sufficient when every fact construction needs is fixed by a declaration rather than
    supplied at build time. Construction refuses — it does not fill, default, or infer — where a
    required field is unfixed, and the refusal names the field and the phase that should have fixed
    it.
  interaction_forms_governed: not_applicable — no boundary is exercised
  protocol_bindings_governed: not_applicable — no boundary is exercised
  read_surface_reach: >
    A local read tool run by an operator against the assembled snapshot on the same host. It reads
    projections and never internals.
  genesis_discharge: >
    Recomputing the snapshot's integrity from constituent bytes, and the composition conformance
    rules passing over the whole. The externality demonstration is NOT discharged: this profile was
    authored by the same authority that built the system it governs, so the genesis claim fails on
    that point and is recorded as failing.

  environment_supplied_values: none
  partial_application: >
    No transition is resumed after partial application. Execution is single-node and a run that
    does not complete is refused rather than continued, so nothing that came to rest partly
    applied is ever picked up — by this node or another. What is written before a refusal is
    evidence of the refusal, not a partly applied transition admitted as complete.

  # B — environment
  nodes: One machine.
  availability: >
    The assembled snapshot must be readable and the local evidence store writable. If either is
    unreachable the run does not start. Nothing else has to be reachable — the surface has no
    workload and no remote dependency.
  co_location_rules: None stated — everything runs in one process on one host.
  resource_guarantees: None stated.
  deadlines: None stated.
  isolation: >
    None stated. The snapshot is stored unencrypted on a local filesystem; no separation mechanism is
    required and none is claimed.
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
      exposed: nothing
      authority_claim: authority
  required_domains: [platform, inspection]
  excluded_domains: []
  entry_points: []
  boundary: declared, nothing crosses
  claims:
    - SNAPSHOT_IMMUTABILITY
    - DETERMINISTIC_EXECUTION
    - COMPILED_INVOCATION_RESOLUTION
```

## Why the answers went this way

**C1b required domains — two, not three.** `platform` is required because a snapshot without the
governance surface is not this platform. `inspection` is required for a reason found by trying it:
assembling the surface alone fails a composition invariant that requires at least one composed
inspection boundary contract. `transformation` is declared and not required — a snapshot without the
design lifecycle is still this platform, holding fewer tools.

**C3 entry points — none.** This is the whole point of the profile. Naming a workload workflow here
would make that workload a condition of being this platform, and every derived profile would inherit
it. A workload composes like any other domain, and a platform that names one cannot admit a second
without a new identity.

**A6 trust root — none, deliberately, at this level.** A derived profile may require a real root.
This one names none so that derivation is not obliged to.

**B — everything undemanding.** A derived profile narrows: it may require more machines, more
isolation, tighter deadlines. It cannot require fewer. So the base states almost no environment
obligation, and the advanced profile that derives from it states them all.

**A14 genesis — discharged in part, and the failing part recorded.** The externality demonstration
cannot succeed while the same authority writes both the profile and the system. Recording it is worth
more than a claim that would not survive being checked.
