# WORKED_EXAMPLE_PLATFORM_V0_ENVIRONMENT — draft

```yaml
completion:
  status: draft
  generated_from: scope sheet
  open_gaps: 1
  usable_as_a_target: false   # a profile with an open gap is not yet something to hand anyone
```

An execution environment profile. It states where execution happens and under what constraints, and
it changes nothing about what execution means.

## 1. Profile

```yaml
environment_profile:
  identity: WORKED_EXAMPLE_PLATFORM_V0_ENVIRONMENT
  environment: One machine.
  execution_constraints:
    availability: 'The assembled snapshot must be readable and the local evidence
      store writable for execution to proceed. If either is unreachable the run does
      not start; nothing is retried and no step concludes. There is no remote dependency
      to be unreachable.

      '
    placement: None stated. Everything runs in one process on one host.
    resource: None stated.
    timing: None stated.
    isolation: 'None stated. The snapshot is stored unencrypted on a local filesystem;
      no separation mechanism is required and none is claimed.

      '
    failure_mode: 'A step fails, the workflow refuses, and the refusal is evidenced.
      There is no partial-failure mode because there is no second participant.

      '
  distribution: None — single node.
  declared_environment_facts: []
  excludes: 'Any system requiring more than one participant, a bounded latency, or
    a separation mechanism. None of the three is provided and none is claimed.

    '
  supported_claims: []
```

## 2. What this profile may not do

An environment profile MUST NOT introduce a governance kind or semantic category, an authority, a
determination point, environment-derived behavior, or an exemption. An environment that cannot
satisfy an invariant has not earned relief from it.

**Governed consequences do not vary with the environment.** What may not vary is anything the system
did not declare; `declared_environment_facts` above is that list, and a fact absent from it must not
change a result.

## 3. Obligations and their breach

> **GAP — to be written by the author.**

For each constraint in §1, state the obligation it places on a system claiming this profile and what
would establish a breach. A constraint stated as a description obliges nothing.

## 4. What this profile excludes

`excludes` in §1 carries the author's answer: systems whose requirements this environment cannot
meet. Stating this is what lets a reader tell in one pass whether the profile is theirs.
