# SIGNED_FEDERATED_MULTINODE_PROFILE_V0_ENVIRONMENT — draft

```yaml
completion:
  status: authored
  generated_from: scope sheet, gaps closed by the author
  open_gaps: 0
  usable_as_a_target: false   # gaps are closed; this profile has not yet been read against a
                              # candidate snapshot, which §7 makes a precondition of use
```

An execution environment profile. It states where execution happens and under what constraints, and
it changes nothing about what execution means.

## 1. Profile

```yaml
environment_profile:
  identity: SIGNED_FEDERATED_MULTINODE_PROFILE_V0_ENVIRONMENT
  environment: 'A node group: at least four separately addressable nodes — one serving
    the interaction boundary, one coordinating, and at least two workers — sharing
    an evidence store reachable by all of them.

    The profile constrains roles, addressability and reachability. It does not constrain
    how nodes are realized, how many machines carry them, or how far apart they are.
    A deployment placing every node on one host and a deployment spanning several
    hosts both satisfy it.

    The reference deployment realizes this as four LXC containers on a single headless
    host on a local network. That is a narrowing a conforming deployment need not
    share, and it is recorded as a property of that deployment rather than of the
    environment this profile describes.

    '
  execution_constraints:
    availability: "Execution requires three things reachable, and the absence of any\
      \ of them prevents execution rather than changing a result.\n\n  - the snapshot,\
      \ readable, whose manifest signature verifies against the public half of the\n\
      \    trust root in A6;\n  - the evidence store, reachable and writable, which\
      \ is not node-local (A7);\n  - for a worker, the coordinator that dispatches\
      \ to it.\n\nA node that cannot reach all three does not begin execution. Unreachability\
      \ is never a result: a dependency that is down makes the platform refuse to\
      \ proceed, and never makes a step conclude differently (6b §8.1).\nWhen a worker\
      \ is lost, work that has not begun is re-dispatched to the other worker; work\
      \ already begun is not. The distinction is required rather than chosen. A dying\
      \ container is a realization that can apply a transition partly, and SM-7a obliges\
      \ such a realization to determine what state results — so re-dispatching a step\
      \ that may already have written through a capability side effect would oblige\
      \ this platform to declare that state and to hold SM-10 across the re-execution.\
      \ Restricting re-dispatch to un-started work means no transition is ever partly\
      \ applied and then resumed elsewhere, so neither obligation is engaged.\nThe\
      \ cost is stated rather than hidden: a worker lost mid-step refuses that run,\
      \ and only an idle worker is lost for free. Making every reachable side effect\
      \ re-executable without changed effect would remove that limit; it would also\
      \ be a change to the governance surface this platform derives from, which is\
      \ work this profile does not undertake.\n"
    placement: 'Three rules, each following from a Section A decision rather than
      from convenience, and each stated so that any placement can be checked against
      it.

      The private half of the trust root is not co-located with any node that executes
      workflows. A node able to sign could mint a snapshot its peers would accept,
      which would defeat the single-authority model in A6.

      Only the node serving the interaction boundary is reachable from outside the
      node group. Workers and the coordinator are not addressable from beyond it.
      Without this the caller classes in A8 are decorative: a caller able to reach
      a worker directly has bypassed the admission the ingress contracts perform.

      Every node reaches the evidence store, and the store is held by none of them.
      This is what A7 requires in practice — evidence that outlives the node that
      produced it. Placing the store inside the coordinator would have made the coordinator''s
      loss destroy evidence, which is node-local traces under another name.

      '
    resource: none stated
    timing: 'None stated. No deadline is imposed on admission, execution or evidence
      write. This costs nothing that governance depends on: nothing this family requires
      may be traded away to obtain a performance property (3c §12), so declining to
      state deadlines forecloses no obligation.

      '
    isolation: 'Two mechanisms, both environmental.

      The container network is segmented so that only the boundary container is reachable
      from outside it (see B2).

      The snapshot is encrypted at rest. No governed result depends on that encryption:
      decrypting every copy and changing nothing else would change no determination
      this platform makes, which is the test that keeps it in Section B.

      Signature verification is deliberately not listed here. A node refuses a snapshot
      whose manifest signature does not verify, so a governed determination does depend
      on it — which is why it is a trust root in A6 and not an isolation mechanism.

      '
    failure_mode: 'A step fails and the workflow refuses. Failure is a declared outcome
      with declared routing (3a §4.2); a failure the declarations did not route is
      an unrouted outcome and refuses (3a §4.3). Environmental failure — an unreachable
      store, a lost worker, a partition — is not an outcome at all, and resolves to
      refusal to proceed under B1.

      '
  distribution: 'Federated across nodes under a single governance authority. Each
    node is an LXC container with its own address on a local network. The federation
    is a placement and distribution fact: it constitutes no authority, and inter-node
    traffic is internal transport rather than a governed boundary.

    '
  declared_environment_facts: []
  excludes: 'Any system requiring evidence to be establishable beyond five days, and
    any system requiring the loss of a worker mid-step to be survivable rather than
    refused.

    Both follow from Section A and hold in every placement. Limits belonging to a
    particular deployment — how many machines carry the nodes, whether they share
    a kernel, whether they share a failure domain — are not exclusions of this environment,
    and a deployment providing more than the reference one does still claims it.

    '
  supported_claims:
  - no determination depends on the latency between nodes, or on any node sharing
    an operating system, kernel or runtime build with another
```

## 2. What this profile may not do

An environment profile MUST NOT introduce a governance kind or semantic category, an authority, a
determination point, environment-derived behavior, or an exemption. An environment that cannot
satisfy an invariant has not earned relief from it.

**Governed consequences do not vary with the environment.** What may not vary is anything the system
did not declare; `declared_environment_facts` above is that list, and a fact absent from it must not
change a result.

## 3. Obligations and their breach

Each constraint in §1 places an obligation, and each obligation names what would establish a breach.
A constraint stated as a description obliges nothing.

**EO-1 — Node roles are present and distinct.** A system claiming this environment provides at least
four separately addressable nodes: one serving the interaction boundary, one coordinating, and at
least two workers.
*Breach:* fewer than four addressable nodes, or a role unfilled. Note what is **not** a breach: any
number of machines carrying them, any distance between them, any mix of operating systems. The
obligation is on roles and addressability, never on placement.

**EO-2 — The prerequisites of execution are reachable, or execution does not start.** A node begins
execution only with the snapshot readable and signature-verifying, the evidence store reachable and
writable, and — for a worker — its coordinator reachable.
*Breach:* a node beginning execution with any of the three unreachable. A system that proceeds
degraded has made unreachability change a result, which §2 forbids.

**EO-3 — The evidence store is external to every node.** It is reachable by all and held by none.
*Breach:* the store held inside any node, such that that node's removal removes evidence.

**EO-4 — Only the boundary node is externally reachable.** No other node is addressable from outside
the node group.
*Breach:* any external caller reaching a worker, the coordinator, or the store directly.

**EO-5 — Re-dispatch is limited to un-started work.** A lost node's un-started work may move to
another; its begun work may not.
*Breach:* a step resumed on a second node after any part of its transition applied on the first.

**EO-6 — No declared environmental input.** `declared_environment_facts` is empty, so nothing the
environment reports may change a determination.
*Breach:* a determination that differs between two nodes given the same governed state — by clock,
by node identity, by operating system, or by anything else the environment supplied.

**What this environment does not oblige.** No compute, memory or storage guarantee, and no deadline.
A system needing either is not served here, and nothing this family requires may be traded away to
obtain one.

## 4. What this profile excludes

`excludes` in §1 carries the author's answer: systems whose requirements this environment cannot
meet. Stating this is what lets a reader tell in one pass whether the profile is theirs.
