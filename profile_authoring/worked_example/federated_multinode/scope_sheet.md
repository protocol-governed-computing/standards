# Federated multinode platform — scope sheet

**In progress. Only the answers below were given; every other field is blank because it has not been
asked or has not been answered.** Nothing here is inferred, and nothing is defaulted.

Intended to derive from `GOVERNANCE_SURFACE_PROFILE_V0`, which the generator cannot yet express —
see the note at the end.

## Answers

```yaml
scope_sheet:
  platform_name:
  profile_identity:

  # A — meaning
  kinds:
  aliases_accepted:
  kinds_required_exercised:
  outcomes:
  result_classes:
  projections:
  namespaces:
  namespaces_closed:
  trust_root: >
    An operator-held signing key. A checking party accepts that key without asking for anything
    further, and every attestation chain terminates in it.
  evidence_retention:
  read_openness:
  reads_attributed:
  sufficiency_criterion:
  interaction_forms_governed:
  protocol_bindings_governed:
  read_surface_reach:
  genesis_discharge:

  # B — environment
  nodes: Several. Multinode.
  availability:
  co_location_rules:
  resource_guarantees:
  deadlines:
  isolation: >
    The snapshot is encrypted at rest. No governed result depends on the encryption: decrypting
    everything and changing nothing else would change no determination the system makes.
  failure_visibility:
  distribution: >
    Federated across nodes under a single governance authority. The federation is a placement and
    distribution fact; it constitutes no new authority, and inter-node traffic is internal transport
    rather than a governed boundary.
  declared_environment_facts:
  environment_excludes:
  environment_claims:

  # C — composition
  domains:
  required_domains:
  excluded_domains:
  entry_points:
  boundary: >
    Things cross. External callers reach the system from outside it. This is distinct from the
    inter-node traffic above, which is internal.
  claims:
```

## The session so far

| Asked | Answered | Consequence |
|---|---|---|
| What is federated — the authority or the machines? | One authority, many nodes *(revised from "multiple authorities")* | Federation moves entirely to Section B. Nothing new discharges CA-3. |
| Does anything cross from outside the whole system? | Yes — external callers | Result classes, interaction forms and protocol bindings become real answers rather than `not_applicable`. |
| What does a checking party accept without asking further? | An operator-held key | The key's custody is part of what every claim rests on. |
| Does any governed result depend on the encryption? | No — data at rest | Isolation is a Section B constraint, not a governance property. |
| What ordering do the nodes require? | None | **Holds only if no determination reads state another node may be writing.** Retest against what each part owns. |

## Open

Four questions outstanding, none of which can be answered by anyone but the author: what the platform
is for; what its parts are and what each owns; who calls in from outside; and what such a caller can
be told.

## Two things this sheet has already exposed

**A revision invalidated an earlier answer, and nothing would have caught it.** Changing federation
from "multiple authorities" to "one authority, many nodes" made the earlier boundary answer
ambiguous — "things cross" may have meant node-to-node, which is no longer a boundary at all. It was
re-asked and re-answered. No dependency of that kind is recorded in the register, and the generator's
cross-checks do not cover it: a facilitator who missed it would have carried a stale answer into the
profile, and every check would have passed.

**The generator cannot express derivation.** This platform is meant to derive from
`GOVERNANCE_SURFACE_PROFILE_V0` — requiring more and permitting less. The sheet has no question for
it and the generator emits `derives_from: null` with §5 as a gap. Derivation is a decision about
intent, which is why it was left to the author; but *whether a profile derives at all, and from
which identity*, is an ordinary answer an author can give. It should be an axis.
