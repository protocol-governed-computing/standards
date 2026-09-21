# SIGNED_FEDERATED_MULTINODE_PROFILE_V0_DOMAIN_PLATFORM — draft

```yaml
completion:
  status: authored
  generated_from: scope sheet, gaps closed by the author
  open_gaps: 0
  usable_as_a_target: false   # gaps are closed; this profile has not yet been read against a
                              # candidate snapshot, which §7 makes a precondition of use
```

## 1. Profile

```yaml
domain_profile:
  identity: SIGNED_FEDERATED_MULTINODE_PROFILE_V0_DOMAIN_PLATFORM
  domain: platform
  authority_claim: authority
  subjects: the governance surface — constitutions, invariants, structures, and the
    capability vocabulary
  governance: its own constitutions — this domain is the governing authority
  capabilities:
  - platform capability contracts
  workflows:
  - platform workflows
  stores:
  - the compiled governance projections
  boundary_exposure: nothing — reached by an operator without crossing the interaction
    boundary
```

## 2. The authority claim

This domain claims to be a distinct governance authority. That claim is established only by
answering all five, **from declared artifacts alone** (CA-3), plus the independence test (CA-4).

| | |
|---|---|
| who the authority is | the `platform` domain — the governance surface, named by the constitutions and invariants it carries |
| what constituted it — the declared constituting act | `governance::CONSTITUTION_GOVERNANCE_V0`, with `governance::CONSTITUTION_INVARIANTS_V0` declaring what holds under it |
| what subjects fall within it | every artifact in every namespace this platform declares, including those of the other three domains |
| **what decision it may make that no other authority may** | **admission** — whether an artifact is admitted or refused against the constitutions. No other domain determines what is admissible, and an artifact no constitution admits is refused rather than filed under something close |
| how it relates to the authorities above and beside it | nothing stands above it within this platform; `transformation` is an authority nested under it, and `workload` and `inspection` are concerns governed under it |

**Independence (CA-4).** The authority is constituted by declared artifacts that are not its own
subject matter: the constitutions above are read by the compiler and the assembler, neither of which
the platform domain authors. The federation constitutes nothing here — nodes are placement, and no
node holds authority of its own.

A domain acquires no jurisdiction by being named, bounded, deployed separately, or owned by a
different team (CA-2). Until the table is filled, this claim is asserted rather than established.

## 3. What this domain accepts

By being part of a governed system this domain accepts obligations it does not get to decline: its
declarations are admitted, determined and refused like any others, with no private admission path;
its changes are transformations against a baseline rather than edits to what it owns; its effects
pass through declared effecting capabilities; its state is owned and its writes authorized; it is
subject to composition obligations; and it carries no exemption for being new, small, experimental,
or internal.
