# SIGNED_FEDERATED_MULTINODE_PROFILE_V0_DOMAIN_TRANSFORMATION — draft

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
  identity: SIGNED_FEDERATED_MULTINODE_PROFILE_V0_DOMAIN_TRANSFORMATION
  domain: transformation
  authority_claim: authority
  subjects: the design and construction lifecycle
  governance: its own design and construction constitutions, under the platform surface
  capabilities:
  - transformation capability contracts
  workflows:
  - transformation workflows
  stores:
  - design phase records
  boundary_exposure: nothing — reached by an operator without crossing the interaction
    boundary
```

## 2. The authority claim

This domain claims to be a distinct governance authority. That claim is established only by
answering all five, **from declared artifacts alone** (CA-3), plus the independence test (CA-4).

| | |
|---|---|
| who the authority is | the `transformation` domain — the design and construction lifecycle |
| what constituted it — the declared constituting act | its own design and construction constitutions, admitted under the platform surface |
| what subjects fall within it | designs, and the artifacts construction produces from them |
| **what decision it may make that no other authority may** | **sufficiency** — whether a design is too thin to build from, so that construction refuses and names the unmet criterion rather than filling the gap with an assumption. No other domain determines when construction refuses |
| how it relates to the authorities above and beside it | nested under the `platform` authority, not beside it. Its constitutions are admitted by that authority, and a transformation determination contradicting an invariant would be refused like any other artifact |

**Independence (CA-4).** Its criterion is declared and its refusal names the criterion that was not
met, so a party other than transformation can evaluate whether a refusal was correct. An authority
whose refusals could not be checked against a declared criterion would be asserting sufficiency
rather than determining it.

A domain acquires no jurisdiction by being named, bounded, deployed separately, or owned by a
different team (CA-2). Until the table is filled, this claim is asserted rather than established.

## 3. What this domain accepts

By being part of a governed system this domain accepts obligations it does not get to decline: its
declarations are admitted, determined and refused like any others, with no private admission path;
its changes are transformations against a baseline rather than edits to what it owns; its effects
pass through declared effecting capabilities; its state is owned and its writes authorized; it is
subject to composition obligations; and it carries no exemption for being new, small, experimental,
or internal.
