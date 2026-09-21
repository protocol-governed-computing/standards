# Worked example — a signed, federated, multinode platform

The scope sheet answered for a platform being built rather than one already standing: a governance
surface and a conformance workload, signed, running across several nodes, reachable from outside.
Where the other examples answer backwards from something built, this one answers forwards — which is
the harder direction, because nothing on disk settles an argument.

It is the first example here with a trust root, the first with a bounded retention window, and the
first whose read surface is reached across the interaction boundary rather than by an operator on the
host. Each of those turned out to change answers elsewhere.

**Read the notes, not just the answers.** Where a decision could have gone the other way, one
sentence on why it went this way is what makes a profile reviewable rather than merely followed.

## Answers

```yaml
scope_sheet:
  platform_name: Signed Federated Collatz Platform
  profile_identity: SIGNED_FEDERATED_MULTINODE_PROFILE_V0
  derives_from: GOVERNANCE_SURFACE_PROFILE_V0

  # A — meaning
  kinds:                      # A1
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
  aliases_accepted: false     # A1
  kinds_required_exercised:   # A1b
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
  outcomes: [succeeded, refused, not_applicable, failed]   # A2
  result_classes: accepted, refused, invalid, unavailable   # A3
  projections: [canonical_form, kind_index, identity_index, store_index]   # A4
  namespaces:                 # A5
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
  namespaces_closed: true     # A5
  trust_root: >               # A6
    A single operator-held signing key. A checking party accepts that key without asking for
    anything further, and every attestation chain terminates in it.

    The private half is held by the operator on the build machine and is never present on any
    node that executes workflows. Each node carries the public half only — enough to verify a
    snapshot manifest's signature and to refuse a copy that does not verify, and not enough to
    produce one. A node can therefore establish that the snapshot it holds is the one, and cannot
    mint one its peers would accept.

    Custody of that key is part of what every claim this platform makes rests on. It was chosen
    over per-node keys because per-node keys give each node something of its own to vouch with,
    which pulls toward the multiple-authority model this platform declined.
  evidence_retention: >       # A7
    A fixed window of five days, measured from the close of the trace the evidence belongs to.
    The clock is read through the platform's governed clock side effect, not off a host, so the
    origin of the period is itself an accounted act.

    What terminates it is an act, not a lapse: evidence past its window is deleted by a declared
    capability side effect. The record of that deletion is exempt from the window and retained
    indefinitely — otherwise the platform would eventually be unable to distinguish evidence that
    was deleted from evidence that was never written.

    An attestation expires with its subject. Nothing outlives what it vouches for, so the platform
    never retains a signed statement about a determination whose evidence is gone. The alternative
    was available and was declined: such a statement is a claim rather than a proof, and keeping
    one after its subject would invite it to be read as the evidence it is not.

    The consequence is stated plainly because it is the point of the answer: after five days a
    determination becomes unestablishable. It was governed when it was made and does not become
    ungoverned, but no claim about it can be checked thereafter. Any audit obligation longer than
    five days is not served by this platform.

    Evidence outlives the node that produced it. A worker writes to a store that survives it, so
    retiring or replacing a container destroys no evidence and shortens no window. This also means
    a single expiry process against a single clock: node-local traces would have given N expiry
    processes whose clock skew would make nodes disagree about what still exists.

    The window is declared in the snapshot, on the expiry side effect itself, and is not an
    environmental parameter. Changing it is therefore a recompile: a new snapshot identity and a
    declared supersession, never an operator editing a value. This follows from the trust root
    rather than from retention: a checking party who verifies a signed snapshot must be able to
    read off that same snapshot how long its evidence lives. Were the window environmental, the
    signature would cover the evidence but not the rule governing its life, and the audit reach
    could be shortened without any declared act.

    Evidence storage placement remains a constraint on the environment rather than on governance:
    the evidence store must be reachable, and a node that cannot reach it does not begin
    execution (see B1).
  read_openness: >            # A8
    Named classes of caller: operator, client, checking party.

    An operator may issue every declared read. A client may read its own submissions and their
    results, and nothing else. A checking party may read evidence, attestations and the snapshot
    manifest, and submits nothing — it exists because the trust root in A6 is addressed to
    somebody, and a platform whose evidence can only be verified from inside the host has a
    trust root that serves nobody outside it.

    Each read is decided when it is issued. Admitting a class fixes the policy; it does not
    dispense with the determination (5b §11), and a read this platform answers without
    determining it would be an ungoverned read path whatever this field says.
  reads_attributed: true      # A9
    # Attributed reads are evidence and fall under the same five-day window as determinations,
    # so the platform answers "who read what" over exactly the reach it answers "what was
    # determined". The window is what makes this affordable: under indefinite retention the
    # evidence store would have grown with read traffic rather than with determinations.
  sufficiency_criterion: >    # A10
    A design is sufficient to build from when all of the following are determinable from the
    declarations alone, without recourse to a convention, a default, or an implementation:

      - every capability contract declares its complete outcome vocabulary, and the traversal
        declares routing for every outcome in it;
      - every workflow reaches a terminal state on every declared outcome;
      - every reference resolves inside a declared namespace, the set of which is closed (A5);
      - every capability side effect names the state it writes and what else may write it;
      - an artifact of every kind required by A1b is present;
      - wherever the order of two effects matters, the declarations state that order.

    The last is here because of how this platform is deployed. Distribution introduces no
    ordering ambiguity; it reveals one already present (6b §8.2). An unstated ordering is
    invisible on a single node and becomes non-deterministic across worker nodes, so the
    construction boundary is the only place it can be caught before it becomes an intermittent
    defect nobody can reproduce.

    Refusal names the unmet criterion and the artifact that failed it, and nothing is built.
    Construction does not warn and proceed: a warning fills the gap with an assumption, which is
    the failure this criterion exists to prevent.
  interaction_forms_governed: >   # A11
    Yes. What arrives at the boundary is declared as a transport ingress artifact and admitted
    like any other, never whatever the receiving code happens to parse. TRANSPORT_INGRESS is
    required by A1b, so a snapshot without one is not this platform.
  protocol_bindings_governed: >   # A12
    Yes. HTTP is a declared binding rather than an assumption in code. Ingress and egress
    contracts are protocol-neutral: they state what crosses, not how it is carried, and
    substituting a different carrier is a change to a declaration rather than to an
    implementation. Answering no would have made HTTP this platform's semantics by accident —
    the same failure the result classes in A3 avoid by refusing status codes.
  read_surface_reach: >       # A13
    Not applicable — an interaction boundary is selected, and the read surface is reached across
    it. A checking party issues declared read operations remotely through governed ingress and
    egress, exactly as a client does; verification requires no access to the host and no operator
    tooling. This is what makes the trust root in A6 serve a party outside the platform rather
    than only its operators, and it requires the read surface itself to be present in the
    snapshot as governed ingress and egress contracts (see C1b).
  genesis_discharge: >        # A14
    Two parts, one discharged and one not.

    Integrity is discharged by the trust root. The first snapshot's manifest is signed under the
    operator key in A6, and every node verifies that signature before executing, so the platform
    can establish that the snapshot it runs is the one sealed and that no node holds a divergent
    copy under the same identity.

    Independence is not discharged, and this is recorded as a gap rather than argued away. This
    profile is written by the same party that authors the platform claiming it, and the
    governance surface it derives from has the same author. A self-signed genesis establishes
    that the operator vouches for the operator; per 3e §6.1 that transfers the question to the
    attesting party rather than answering it. Any checking party who requires the profile to
    have been written independently of what it governs is not served by this genesis, and that
    limit is stated here rather than discovered later.

  environment_supplied_values: none   # A15
    # The snapshot carries every Section A value. The retention window in A7 is the one that
    # tempted otherwise, and it is declared on the expiry side effect precisely so that it is
    # not here: a checking party verifying a signed snapshot must be able to read off that same
    # snapshot how long its evidence lives. A value outside the snapshot is outside what the
    # signature covers.
  partial_application: >      # A16
    No transition is resumed after partial application, so none is ever partly applied and then
    continued elsewhere. Work re-dispatched after a node is lost is work that had not begun
    (B1); begun work is not moved, and its run refuses.

    This is what makes the answer available rather than aspirational. A lost node is a
    realization applying a transition partly, and SM-7a would oblige this platform to determine
    the resulting state and SM-10 to hold across the re-execution. Neither obligation is engaged
    where nothing is resumed.

    The alternative was available and declined: making every reachable effect re-appliable
    without changed effect would let begun work move too. It would also be a change to the
    governance surface this platform derives from, which this profile does not undertake.

  # B — environment
  nodes: >                    # B1/B2
    A node group: at least four separately addressable nodes — one serving the interaction
    boundary, one coordinating, and at least two workers — sharing an evidence store reachable
    by all of them.

    The profile constrains roles, addressability and reachability. It does not constrain how
    nodes are realized, how many machines carry them, or how far apart they are. A deployment
    placing every node on one host and a deployment spanning several hosts both satisfy it.

    The reference deployment realizes this as four LXC containers on a single headless host on a
    local network. That is a narrowing a conforming deployment need not share, and it is
    recorded as a property of that deployment rather than of the environment this profile
    describes.
  availability: >             # B1
    Execution requires three things reachable, and the absence of any of them prevents execution
    rather than changing a result.

      - the snapshot, readable, whose manifest signature verifies against the public half of the
        trust root in A6;
      - the evidence store, reachable and writable, which is not node-local (A7);
      - for a worker, the coordinator that dispatches to it.

    A node that cannot reach all three does not begin execution. Unreachability is never a
    result: a dependency that is down makes the platform refuse to proceed, and never makes a
    step conclude differently (6b §8.1).

    When a worker is lost, work that has not begun is re-dispatched to the other worker; work
    already begun is not. The distinction is required rather than chosen. A dying container is a
    realization that can apply a transition partly, and SM-7a obliges such a realization to
    determine what state results — so re-dispatching a step that may already have written
    through a capability side effect would oblige this platform to declare that state and to
    hold SM-10 across the re-execution. Restricting re-dispatch to un-started work means no
    transition is ever partly applied and then resumed elsewhere, so neither obligation is
    engaged.

    The cost is stated rather than hidden: a worker lost mid-step refuses that run, and only an
    idle worker is lost for free. Making every reachable side effect re-executable without
    changed effect would remove that limit; it would also be a change to the governance surface
    this platform derives from, which is work this profile does not undertake.
  co_location_rules: >        # B2/B5
    Three rules, each following from a Section A decision rather than from convenience, and each
    stated so that any placement can be checked against it.

    The private half of the trust root is not co-located with any node that executes workflows.
    A node able to sign could mint a snapshot its peers would accept, which would defeat the
    single-authority model in A6.

    Only the node serving the interaction boundary is reachable from outside the node group.
    Workers and the coordinator are not addressable from beyond it. Without this the caller
    classes in A8 are decorative: a caller able to reach a worker directly has bypassed the
    admission the ingress contracts perform.

    Every node reaches the evidence store, and the store is held by none of them. This is what
    A7 requires in practice — evidence that outlives the node that produced it. Placing the
    store inside the coordinator would have made the coordinator's loss destroy evidence, which
    is node-local traces under another name.

  resource_guarantees: none stated   # B3
  deadlines: >                # B4
    None stated. No deadline is imposed on admission, execution or evidence write. This costs
    nothing that governance depends on: nothing this family requires may be traded away to
    obtain a performance property (3c §12), so declining to state deadlines forecloses no
    obligation.
  isolation: >                # B5
    Two mechanisms, both environmental.

    The container network is segmented so that only the boundary container is reachable from
    outside it (see B2).

    The snapshot is encrypted at rest. No governed result depends on that encryption:
    decrypting every copy and changing nothing else would change no determination this platform
    makes, which is the test that keeps it in Section B.

    Signature verification is deliberately not listed here. A node refuses a snapshot whose
    manifest signature does not verify, so a governed determination does depend on it — which is
    why it is a trust root in A6 and not an isolation mechanism.
  failure_visibility: >       # B6
    A step fails and the workflow refuses. Failure is a declared outcome with declared routing
    (3a §4.2); a failure the declarations did not route is an unrouted outcome and refuses
    (3a §4.3). Environmental failure — an unreachable store, a lost worker, a partition — is not
    an outcome at all, and resolves to refusal to proceed under B1.
  distribution: >             # B7
    Federated across nodes under a single governance authority. Each node is an LXC container with
    its own address on a local network. The federation is a placement and distribution fact: it
    constitutes no authority, and inter-node traffic is internal transport rather than a governed
    boundary.
  declared_environment_facts: []   # B8
    # Empty is the answer, not an omission. No determination this platform makes depends on
    # anything the environment reports. The near misses were each tested and each excluded: the
    # clock drives evidence expiry, and expiry renders a determination unestablishable rather
    # than different (3e §11); which node executed a step is observational evidence, which may
    # differ between nodes without either being wrong (3e §5); and the retention window is
    # declared in the snapshot precisely so that it is not an environmental input (A7).
  environment_excludes: >     # B9
    Any system requiring evidence to be establishable beyond five days, and any system requiring
    the loss of a worker mid-step to be survivable rather than refused.

    Both follow from Section A and hold in every placement. Limits belonging to a particular
    deployment — how many machines carry the nodes, whether they share a kernel, whether they
    share a failure domain — are not exclusions of this environment, and a deployment providing
    more than the reference one does still claims it.
  environment_claims:         # B10
    - no determination depends on the latency between nodes, or on any node sharing an operating
      system, kernel or runtime build with another
    # What would show it broken: a determination that changes when nodes are separated by a
    # slower link, or when one node runs a different operating system, with nothing else altered.
    #
    # Two limits on the evidence, both recorded rather than argued away. Latency: nodes placed on
    # one host always have a fast link, so a dependency on timing between them is invisible in
    # exactly the environment that satisfies it (6b §7, SN-4, 3b §15). Homogeneity, the stronger
    # of the two: containers on one host share that host's kernel, so every node in the reference
    # deployment runs the same operating system, kernel and runtime build, and a determination
    # depending on any of those would surface only on the first deployment that mixed them.
    #
    # The nodes do not share a filesystem: each holds its own root filesystem, and the evidence
    # store is reachable by all of them because the deployment mounts it deliberately, not
    # because containers share storage by nature.
    #
    # The claim is made and marked untested. A deployment that separates its nodes, or varies
    # their operating system, is what would discharge it.
  # C — composition
  domains:                    # C1: one entry per domain, each with an authority claim
    - name: platform
      owns: the governance surface — constitutions, invariants, structures, and the capability vocabulary
      governed_by: its own constitutions — this domain is the governing authority
      reached_by: [platform capability contracts]
      ordered_by: [platform workflows]
      state: [the compiled governance projections]
      exposed: nothing — reached by an operator without crossing the interaction boundary
      authority_claim: authority
      authority_note: >
        Its exclusive decision is admission: whether an artifact is admitted or refused against
        the constitutions. No other domain may make that determination, and every other domain
        is governed under it.
    - name: transformation
      owns: the design and construction lifecycle
      governed_by: its own design and construction constitutions, under the platform surface
      reached_by: [transformation capability contracts]
      ordered_by: [transformation workflows]
      state: [design phase records]
      exposed: nothing — reached by an operator without crossing the interaction boundary
      authority_claim: authority
      authority_note: >
        Its exclusive decision is sufficiency: whether a design is thin enough that construction
        refuses rather than building (A10). No other domain may make that determination. It is
        an authority nested under the platform surface, not beside it.
    - name: workload
      owns: one conformance workload and its results storage
      governed_by: the platform surface's constitutions and invariants
      reached_by: [workload capability contracts, workload transport ingress]
      ordered_by: [workload workflows]
      state: [workload results]
      exposed: its compute ingress and egress, reachable by the client caller class (A8)
      authority_claim: concern
    - name: inspection
      owns: read operations about a snapshot
      governed_by: the platform surface's constitutions, and the inspection boundary contracts
      reached_by: [inspection capability contracts, inspection transport ingress]
      ordered_by: [inspection workflows]
      state: []
      exposed: >
        its read ingress and egress, reachable by the checking party caller class (A8). This is
        what makes the trust root in A6 usable from outside the platform.
      authority_claim: concern
  required_domains: [platform, inspection]   # C1b
    # platform because nothing is governed without it. inspection because A13 places the read
    # surface across the interaction boundary, and without it the checking party admitted in A8
    # has no way to reach the evidence the trust root in A6 exists to let them verify.
    # workload is deliberately absent: the kinds a workload contributes are required by A1b, so
    # any workload supplying them satisfies this profile and the conformance workload is one
    # such supplier rather than a condition of conformance.
  excluded_domains: []        # C1c
  entry_points: []            # C3
    # None. The reasoning that first produced an answer here was sound and the mechanism was
    # wrong: requiring the inspection domain while not requiring its reads to work would require
    # a domain and not require it to function. But inspection carries no workflows — its reads
    # are transport ingress and egress pairs — so naming an inspection entry workflow names
    # something that cannot exist.
    #
    # The obligation is already carried. TRANSPORT_INGRESS and TRANSPORT_EGRESS are required by
    # A1b, and `inspection` is required by C1b, so a snapshot without a working read surface
    # fails on the kinds rather than on an entry point.
    #
    # No workload workflow is named either. Requiring one would contradict C1b, where the
    # conformance workload supplies required kinds rather than being a condition of conformance.
  boundary: >                 # C4
    Things cross. Callers reach this platform from outside it — a client submitting work through
    the workload's ingress, and a checking party issuing reads through the inspection ingress.

    Node-to-node traffic is not this. Nodes are internal to one authority (B7), so dispatch from
    a coordinator to a worker is internal transport and crosses no interaction boundary. The two
    were separated deliberately: conflating them would make every worker an admission point and
    would give the federation an authority it does not have.
  claims:                     # C5
    - SNAPSHOT_IMMUTABILITY
    - DETERMINISTIC_EXECUTION
    - COMPILED_INVOCATION_RESOLUTION
    - SIGNED_SNAPSHOT_VERIFICATION
    - EVIDENCE_EXPIRY
    # Each is settled by a demonstration capable of failing. SIGNED_SNAPSHOT_VERIFICATION is
    # settled by presenting a node a snapshot whose manifest signature does not verify: it must
    # refuse to execute. EVIDENCE_EXPIRY is settled by advancing the governed clock past the
    # window and finding the determination unestablishable and its deletion recorded.
    #
    # Protocol independence is deliberately not claimed. A12 holds that the binding to a wire
    # protocol is governed, which is a statement about how the binding is declared and not a
    # demonstration that a different carrier works. Only one carrier exists, so the substitution
    # that would test the claim cannot be performed, and claiming it would be claiming what
    # these answers make untestable.
    #
    # Every claim here is checkable for five days. A7 fixes that ceiling, and a claim outliving
    # the evidence that would settle it is the failure 3e §11 names.
```

## Why the answers went this way

**A6 trust root — one operator key, split by half.** The private half is on the build machine and on
no node that executes. A node that can sign can mint a snapshot its peers would accept, so possession
is the thing to control, not use. Per-node keys were the tempting alternative and were declined: they
give each node something of its own to vouch with, which pulls toward the multiple-authority model
this platform had already rejected.

**A7 retention — five days, and the window is in the snapshot.** The period was the easy half. The
hard half was where the number lives. Retention changes no result — discarding evidence makes a
determination unestablishable, never different — so it looks like a pure environment concern. It is
not, once there is a trust root: a window supplied by the environment is one the signature does not
cover, and an operator could shorten the audit reach with no declared act. Putting it in the snapshot
means changing it is a recompile and a supersession, which for a platform meant to exercise the
lifecycle is a feature rather than a cost.

**A7 again — the deletion record is exempt, and attestations are not.** Evidence past its window is
deleted by a declared side effect, because expiry is an act and not a lapse. Its record is kept
indefinitely: a platform that deletes the deletion cannot later distinguish evidence that was removed
from evidence never written. Attestations, by contrast, expire with their subjects. Keeping a signed
statement after the evidence supporting it is gone would leave exactly the thing the standard warns
not to mistake for evidence — a claim, not a proof.

**A9 reads attributed — affordable only because of A7.** Under indefinite retention, attributing
reads would have grown the evidence store with read traffic rather than with determinations. The
five-day window bounds it, and gives one audit reach rather than two: the platform answers "who read
this" over exactly the period it answers "what was determined".

**A8 read openness — three caller classes, and the third is the point.** Operator and client are
obvious. The checking party is not, and it is what makes A6 mean anything: a trust root is addressed
to somebody, and a platform whose evidence can only be verified from inside the host has one that
serves nobody outside it. Admitting that class is what later forced `inspection` into the required
domains.

**A1b required kinds — fifteen of sixteen.** The reference composition requires seven. This one
requires everything it admits except `ASSERT`, on the reasoning that a workflow, an actor and an
event are foundational to any usable platform whether a given workload exercises them or not. The
conformance workload was chosen to exercise them and could be replaced by another that does the
same — which is exactly why the kinds are required and the workload is not.

**A16 partial application — restricted rather than solved.** Re-dispatch is limited to work that had
not begun. The alternative, making every reachable effect re-appliable without changed effect, would
let begun work move too, and would be a change to the governance surface this platform derives from.
The cost is stated rather than hidden: a worker lost mid-step refuses its run, and only an idle
worker is lost for free.

**B — the environment describes a class, not the rig.** An earlier draft wrote "four LXC containers
on one headless host" into the profile itself. That was wrong. An environment profile bounds an
environment; the containers are one conforming deployment of it. The profile constrains roles,
addressability and reachability, and says nothing about how many machines carry them.

**B10 — the claim is made and marked untested.** No determination depends on inter-node latency or on
nodes sharing an operating system. Nothing in the reference deployment can demonstrate this:
containers on one host share that host's kernel, so every node runs the same OS, kernel and runtime
build, and a dependency on any of them is invisible in exactly the environment that satisfies it.
Recording the claim as untested is worth more than presenting it as demonstrated.

**C4 boundary — things cross, and node-to-node is not crossing.** This was the first question asked
and it decided the shape of everything after. One authority on many nodes puts federation entirely in
Section B; many authorities would have made every worker an admission point. Conflating inter-node
dispatch with a governed boundary would have given the federation an authority it does not have.

**C5 claims — five, and protocol independence deliberately absent.** Two claims are this example's
own: a node must refuse a snapshot whose signature does not verify, and a determination must become
unestablishable once its window closes. Both are settled by demonstrations capable of failing.
Protocol independence is not claimed even though A12 answers yes — A12 says the binding is
*declared*, which is not the same as showing a different carrier works, and only one carrier exists.

**§6 externality — recorded as failing.** The same party writes this profile, the platform claiming
it, and the governance surface it derives from. No wording fixes that. Every claim rests on a
demonstration the claimant designed, and closing it needs a second party to author the profile.

## What this example exposed in the toolkit

Four axes were missing or unguarded, and answering this sheet is what surfaced them. All four are now
in place.

**Where a Section A value is carried was not asked.** A7 could be answered completely — a period, a
terminating act, an exemption — and leave undecided whether the window lived in the snapshot or in
the environment. Every other Section A axis has the same blind spot; it only becomes visible under a
trust root, where the distinction is what the signature does and does not cover. Now **A15**, with a
cross-check against B8.

**Partial application was reachable only from the wrong direction.** Section A closed with no answer
to SM-7a, and Pass B surfaced it: a worker lost mid-step is a realization applying a transition
partly, and the obligation to determine the resulting state binds whether or not a profile mentions
it. The sheet had no question for it, so an author reaching it from Section B would either answer it
there — settling what a result means by where it ran — or not at all. Now **A16**, refusable when a
multinode platform holds that the case cannot arise.

**Derivation still had no axis**, as the in-progress federated example had already noted. The
judgement a generator must decline is the base's content; whether a profile derives at all, and from
which identity, is an ordinary answer. Now **D1**, and §5 is no longer a gap.

**Entry points were unguarded, and the register had no C axis at all.** C3 was answered here as "the
inspection read workflows" — a description. It passed every check in the toolkit, because a list of
strings is structurally valid, and would have failed at assembly as *"required workload entry point
absent: the inspection read workflows"*: a profile's defect presented as a snapshot's. Worse, the
thing it named cannot exist — the inspection domain carries eighteen transport ingress and eighteen
egress artifacts and **no workflow**, so a read surface can be required, reachable and working with no
workflow to name. The obligation was already carried by requiring the kinds in A1b and the domain in
C1b. C3 now requires identities of the form `namespace::ARTIFACT_IDENTITY`, and the register has a C3
entry recording both failure modes — and a note that the other C axes still have none.

## What this example exposed in the generator

Seven defects, six of the same family: the tool reporting something the document did not support.

- `boundary` was scanned for the substring `not`, so an answer saying "things cross" and then
  explaining that node-to-node traffic is *not* a crossing registered as no boundary at all —
  cascading into a refusal of `result_classes` for classifying callers it had decided did not exist.
- `REFUSED` matched the bare word `whatever`, flagging the two answers that most explicitly refused
  to hand the question back.
- `open_gaps` was a literal written beside the markers rather than derived from them: the platform
  profile declared five and emitted four, in checked-in files. §6 Externality asks for author text
  and carried no marker.
- A `LIST` axis answered `none` was rejected, contradicting the sheet's own rule that `none` and an
  empty list are both explicit answers.
- The new A15 cross-check iterated a string one character at a time.
- The new A16 cross-check matched `none` anywhere in the answer, so "none is ever partly applied"
  read as a dismissal — the same polarity flaw as `whatever`, written an hour after fixing it.
- `entry_points` accepted prose for a field the assembler resolves against artifact identities. This
  one is not a matching flaw: nothing was checking the field's shape at all, and the profile would
  have been handed to a build that reported the profile's mistake as the snapshot's.

The first two and the last two are one mistake made four times: matching a word without its polarity
or position. The boundary check, the evasion check and the A16 check now read the opening clause
through a shared helper, which is where an answer's decision sits.
