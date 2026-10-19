# WORKED_EXAMPLE_PLATFORM_V0_DOMAIN_INSPECTION — draft

```yaml
completion:
  status: draft
  generated_from: scope sheet
  open_gaps: 0
  usable_as_a_target: false   # a profile with an open gap is not yet something to hand anyone
```

## 1. Profile

```yaml
domain_profile:
  identity: WORKED_EXAMPLE_PLATFORM_V0_DOMAIN_INSPECTION
  domain: inspection
  authority_claim: concern
  subjects: read operations about a snapshot
  governance: the platform surface's constitutions, and the inspection boundary contracts
  capabilities:
  - inspection capability contracts
  workflows:
  - inspection workflows
  stores: []
  boundary_exposure: nothing
```

## 2. The authority claim

This domain is a **concern**: governed under the authority above it, with no jurisdiction of its own.
It is organized, named, indexed and governed — an ordinary and correct arrangement, and not a lesser
one.

A concern classification cannot constitute an authority (CA-6). If this domain later needs to make a
decision no other part of the system may make, that is a change of claim, discharged against CA-3.

## 3. What this domain accepts

By being part of a governed system this domain accepts obligations it does not get to decline: its
declarations are admitted, determined and refused like any others, with no private admission path;
its changes are transformations against a baseline rather than edits to what it owns; its effects
pass through declared effecting capabilities; its state is owned and its writes authorized; it is
subject to composition obligations; and it carries no exemption for being new, small, experimental,
or internal.
