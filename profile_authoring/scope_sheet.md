# Platform scope sheet

Answer these and you have said what platform you are building. The answers become a Normative
Platform Profile, an execution environment profile, and one domain profile per domain you declare.

**Answer in order.** Section A settles what your platform *means*, B where it runs, C what it is made
of. Later questions assume earlier answers, and B never changes anything A decided.

**Every answer is yours to give.** Nothing here is pre-filled and nothing is assumed: a question you
leave blank is refused, not defaulted. Where a question ends with *if you have no view yet*, that is
a suggestion to consider and then write down — never a value that applies because you said nothing.

The suggestions taken together describe a coherent small platform: one governance surface, one node,
nothing crossing a boundary, nothing signed. That is a real platform and a legitimate answer. It is
not a floor, and nothing about it is more basic than a larger one.

**Somebody has to ask you these.** The sheet is the record of a session, not a form to complete
alone — see the README. The answers are yours; the other party's job is to draw them out, to say what
each question is really asking, and to catch the reasonable-sounding answer that fails later.

**Two answers are never available.** "Whatever the system decides" is not a decision — it hands the
question back to the party the profile is supposed to constrain, and two systems that agree on
nothing would both satisfy you. "The same as the reference implementation" is not a decision either;
resembling a working system establishes nothing about yours.

**Where an option list says *from practice*, you may answer outside it.** Those lists are collected
experience, not a closed set. Where a list says *fixed*, an answer outside it is inadmissible.

---

## Answers

Fill this in as you go. The generator reads this block and nothing else.

```yaml
scope_sheet:
  platform_name:              # what you are building, in your own words
  profile_identity:           # the name your snapshots will claim, e.g. ACME_ORDERS_PLATFORM_V0
  derives_from:               # D1: the base profile's identity, or none

  # A — meaning
  kinds:                      # A1
  aliases_accepted:           # A1
  kinds_required_exercised:   # A1b
  outcomes:                   # A2
  result_classes:             # A3  (or: none — no boundary)
  projections:                # A4
  namespaces:                 # A5
  namespaces_closed:          # A5
  trust_root:                 # A6
  evidence_retention:         # A7
  read_openness:              # A8
  reads_attributed:           # A9
  sufficiency_criterion:      # A10
  interaction_forms_governed: # A11
  protocol_bindings_governed: # A12
  read_surface_reach:         # A13
  genesis_discharge:          # A14
  environment_supplied_values: # A15  (or: none — the snapshot carries every one)
  partial_application:        # A16

  # B — environment
  nodes:                      # B1/B2
  availability:               # B1
  co_location_rules:          # B2/B5
  resource_guarantees:        # B3
  deadlines:                  # B4
  isolation:                  # B5
  failure_visibility:         # B6
  distribution:               # B7
  declared_environment_facts: # B8
  environment_excludes:       # B9
  environment_claims:         # B10

  # C — composition
  domains:                    # C1: one entry per domain, each with an authority claim
  required_domains:           # C1b — which of them a snapshot MUST carry
  excluded_domains:           # C1c
  entry_points:               # C3
  boundary:                   # C4
  claims:                     # C5
```

---

# Section A — What your platform means

## A1. What kinds of governed thing does your platform have?

The closed list of categories every artifact in your system must fall into. An artifact whose kind
is not on the list is refused rather than filed under something close.

*From practice:* constitutions, invariants, structures, vocabularies, surface contracts, capability
contracts, capability transforms, capability side effects, runtime bindings, workflows, intents,
actors, events, boundary ingress, boundary egress.

**Also answer: do you accept short forms?** If a declaration may say `CT` where the kind is
`CAPABILITY_TRANSFORM`, you have two names for one thing, and one day they will disagree. The safe
answer is no.

> **If you have no view yet:** the list above; short forms not accepted.

## A1b. Which of those kinds must actually be used?

Admitting a kind is not the same as requiring it. The list in A1 is what your system *may* carry; this
list is what a snapshot *must* carry to count as your platform at all. A kind you admit but do not
yet use belongs in A1 and not here.

Answering this list with A1's is the common mistake, and it fails every snapshot that has admitted a
kind it has no artifact for yet.

> **If you have no view yet:** none — admitting a kind requires nothing to use it.

## A2. What may a step conclude?

The closed list of results a step can report, on which the next step is chosen. Nothing else steers
execution — not a return value, not an error, not a look at the state.

*From practice:* succeeded, refused, not applicable, failed.

> **If you have no view yet:** the four above.

## A3. What can a caller at the boundary be told?

Only if something calls in from outside. These are protocol-neutral: no status codes, no error
numbers. A list that looks like HTTP's has quietly made HTTP your semantics.

*From practice:* accepted, refused, invalid, unavailable.

> **If you have no view yet:** none — nothing crosses a boundary (see C4).

## A4. What derived views does your system carry?

Indexes, canonical forms, rendered forms — anything generated from your declarations rather than
authored. Each is regenerated, never edited, and where a view and its source disagree the source
wins.

*From practice:* a canonical form per artifact, a kind index, an identity index, a human-readable
rendering.

> **If you have no view yet:** canonical forms and a kind index.

## A5. What namespaces does your system have?

The naming compartments artifact identities live in. Decide this before you author anything — a
namespace set settled afterwards is settled by renaming everything.

**Also answer: is the list closed?** Closed means a reference into a namespace you did not declare is
refused rather than resolved.

**And note what a namespace is not.** It carries identity and nothing else. If one of your namespaces
is called `billing`, that does not make billing an authority or a concern; you say which in Section C
and the system never reads it off the name.

> **If you have no view yet:** closed, with whatever list your domains require.

## A6. What does a checking party accept without asking for anything further?

When someone verifies your evidence, the chain of vouching has to stop somewhere. What it stops at is
your trust root, and you have to be able to name it.

*From practice:* nothing — evidence is self-asserted · a key your operators hold · your
organization's PKI · a public transparency log · a hardware root · an external registrar.

**A content hash is not an answer.** It shows bytes did not change. It says nothing about who vouched
for them.

> **If you have no view yet:** nothing — self-asserted.

## A7. How long do you keep evidence, and what ends it?

However long you keep it is exactly how long you can prove what your system determined. Shorter than
your audit window means you cannot answer the question you kept it for.

*From practice:* only for the run · a fixed window · until superseded by a newer determination ·
indefinitely.

> **If you have no view yet:** until superseded.

## A8. Who may read what your system contains?

Which callers may issue which read operations.

*From practice:* nobody outside the system · named classes of caller · everyone, for every declared
read.

**Whatever you choose, each read is still decided when it happens.** The most open policy available
is still a policy; a system that answers a read it never decided has an ungoverned read path
regardless of what you wrote here.

> **If you have no view yet:** nobody outside the system.

## A9. Are reads attributed to whoever made them?

If yes, reads become evidence, and A7 applies to them too.

> **If you have no view yet:** no.

## A10. When is a design too thin to build from?

The point below which construction refuses rather than filling gaps with assumptions. State the
criterion, and state what refusal looks like when it is not met.

There is no list to choose from. If you leave this open, whoever writes the build step decides it,
and they become a second design authority nobody appointed.

> **If you have no view yet:** none — you must answer this one.

## A11. Is the shape of what arrives at your boundary itself governed?

Only if something crosses a boundary. Governed means the request shape is declared and admitted like
any other artifact, rather than being whatever the code happens to parse.

> **If you have no view yet:** not applicable — no boundary.

## A12. Is the binding to a wire protocol itself governed?

Same condition. If you answer no here but want to claim your system works the same over any protocol,
those two answers contradict each other.

> **If you have no view yet:** not applicable — no boundary.

## A13. If nothing crosses a boundary, how is your system read at all?

A platform with no boundary still has to answer what it contains and what it determined. Say how —
a local command, a mounted read surface, an operator tool.

> **If you have no view yet:** a local read tool run by an operator.

## A14. What settles that your first snapshot was legitimately made?

Your first build has no predecessor to be checked against, so say what makes it trustworthy.

**One part of this cannot be satisfied by you.** A genuine answer has to show the profile your system
claims was not written by your system's own authors. If you wrote both, say so — a recorded gap is
worth more than a claim that cannot survive being checked.

> **If you have no view yet:** none — you must answer this one.

## A15. Which of the answers above does the environment supply, rather than the snapshot carrying them?

Every answer in Section A means something. This asks a different question about each: **where is it
written down?** A value declared in the snapshot travels with it and can be read by anyone holding
it. A value supplied by the environment can change without any declared act.

The distinction is invisible until you look for it. "Evidence is kept five days" is a complete answer
either way — but if the window lives in a config file, an operator can shorten how long your
determinations can be established, and nothing records that they did.

**It matters most where you have a trust root (A6).** A checking party verifies a signed snapshot.
Anything not in that snapshot is outside what the signature covers, so a meaning-bearing value
supplied by the environment is one the signature does not vouch for.

**Anything you list here must also appear in B8.** A value a determination may depend on, supplied by
the environment, is an environmental input; one that is not declared as such is the leak B8 exists to
prevent.

> **If you have no view yet:** none — the snapshot carries every one.

## A16. If a transition can be applied partly, what state results?

A transition that comes to rest half-applied is one your declarations have to account for: SM-7a
forbids it coming to rest that way, and obliges a realization that *can* apply one partly to
determine what state results.

Answer either that no realization this profile admits can apply a transition partly — and say what
makes that true — or what state results when one does.

**More than one node makes this real rather than theoretical.** A node lost mid-step is exactly a
realization applying a transition partly, so a multinode platform answering "cannot happen" is
answering about a case its own environment produces.

*From practice:* no transition is resumed after partial application, so none is ever partly applied
and resumed · a partly applied transition is determined not to have applied, and is retried · every
effect is re-appliable without changed effect, so re-application is the same state.

> **If you have no view yet:** none available — answer from how your own effects behave.

---

# Section D — What this profile derives from

## D1. Does this profile derive from another, and which?

Deriving means naming a base **by identity** and requiring at least what it requires. A deriving
profile may require more and permit less; it may never widen its base (NP-10).

Deriving is not inheritance of privilege. No profile is privileged (6a §11), a base makes no claim on
profiles that have not named it, and the relation is declared by the profile that derives — never by
the one derived from.

**Answer this if you are building on somebody's governance surface.** Composing on a surface whose
constitutions and invariants you did not author *is* deriving, whatever the directory layout says.
The honest answer names it.

> **If you have no view yet:** none — this profile derives from nothing.

---

# Section B — Where it runs

Nothing here changes anything Section A decided. The environment can determine whether your system
runs, when, how fast, and where — never what its results mean. If an answer below seems to need a new
kind of governed thing, or a new authority, or an exception to a rule, it belongs in Section A and
you have reached it from the wrong direction.

## B1/B2. How many nodes, where, and what may sit next to what?

*From practice:* one machine · one container · a container group · an orchestrated cluster · several
regions.

> **If you have no view yet:** one machine.

## B1. What must be reachable for execution to proceed, and what happens when it is not?

The nodes, stores, and dependencies your system needs in order to run at all — and what your system
does when one of them cannot be reached.

Answering only *how many machines* leaves this unsaid. How many nodes there are and what must be
reachable are different facts: a single machine still has a snapshot to read and a place to write
evidence, and "the disk is unreachable" is not the same event as "a step failed".

**Unreachable is not a result.** Whatever you answer, it determines whether execution happens — never
what a result means. A dependency that is down makes the system refuse to proceed; it never makes a
step conclude differently.

> **If you have no view yet:** the snapshot and the local evidence store must be readable and
> writable; if either is not, execution does not start.

## B3. What compute, memory, and storage are guaranteed?

> **If you have no view yet:** none stated.

## B4. What deadlines apply?

> **If you have no view yet:** none stated.

## B5. What must be kept separate, and by what mechanism?

Encryption at rest, tenancy separation, network segmentation — all live here, not in Section A,
unless a governed result actually depends on one of them.

> **If you have no view yet:** none stated.

## B6. What does a failure look like to your system?

> **If you have no view yet:** a step fails and the workflow refuses.

## B7. If more than one node participates, what ordering do you require?

And what establishes that ordering.

> **If you have no view yet:** not applicable — single node.

## B8. Which environmental facts does your system treat as inputs?

Anything the environment tells your system that a result may depend on — a clock, a region, a feature
flag. Anything not on this list must not change a result. This is the list that keeps B from leaking
into A.

> **If you have no view yet:** none.

## B9. Which systems can this environment not serve?

Requirements this environment cannot meet — a workload needing more isolation than you provide, a
deadline you cannot hold to. Saying so is what lets a reader tell in one pass whether this is theirs.

> **If you have no view yet:** none stated.

## B10. What do you claim about the environment itself?

Availability, redundancy, bounded latency — obligations a system claiming this environment can hold
you to. Each needs something that would show it broken.

> **If you have no view yet:** none.

---

# Section C — What it is made of

## C1. What domains does your platform have?

For each, answer all of:

| | |
|---|---|
| **name** | |
| **what it owns** | the subjects it is responsible for |
| **how its work is reached** | its contracts |
| **how its work is ordered** | its workflows |
| **what obligations apply to it** | the rules its subjects are held to, and under whose authority |
| **what state it owns** | and what is allowed to write to that state |
| **what of it is reachable from outside** | |
| **authority or concern** | see C2 |

## C2. For each domain: is it an authority, or a concern?

**This is not optional and it has a test.** A domain is an authority only if you can point to a
declared act that constituted it and answer, from your declarations alone: who it is, what
constituted it, what falls under it, **what decision it may make that no other part of your system
may**, and how it stands relative to what is above and beside it.

If you cannot answer all five, it is a concern — governed under the authority above it. That is the
ordinary case and there is nothing lesser about it. What is not available is calling something an
authority because it has its own name, its own repository, its own deployment, or its own team.

> **If you have no view yet:** concern.

## C1b. Which of those domains must be present?

Not the same question as C1. C1 lists the domains you have; this lists the ones whose absence would
mean a snapshot is not your platform at all.

A profile states a floor, never an inventory — a system may carry more than you require and still be
yours. Listing everything you happen to have built turns your current composition into a requirement
on everyone, including your future self.

> **If you have no view yet:** the domains carrying your governance surface, and nothing else.

## C1c. Which domains does this profile refuse?

Domains that must *not* be present. Usually empty; worth answering when a domain would contradict
what the platform is for.

> **If you have no view yet:** none.

## C3. Which workflows must resolve and be reachable?

The entry points that must exist for this to be the platform you are claiming.

> **If you have no view yet:** none required.

## C4. Does anything cross an interaction boundary?

*Fixed choices:* nothing crosses, and the boundary contracts are declared but unexercised · things
cross.

Declaring the contracts without exercising them is a real answer: the contracts exist and govern in
advance, so a later composition that does admit something finds them already in force rather than
written under pressure.

> **If you have no view yet:** declared, not exercised.

## C5. What do you claim about this platform?

Each claim needs something that would settle it, and that something has to be capable of failing.

*From practice:* the sealed build admits no behavior that was not in it · the same input yields the
same result · every invocation resolves at build time, nothing is routed at run time.

**Do not claim what your answers make untestable.** If nothing crosses a boundary (C4), you cannot
claim your system behaves the same across protocols — the substitution that would test it cannot be
performed.

> **If you have no view yet:** the three above.

---

# Not asked

Four things are required of every system, so they are told to you rather than asked.

- **Your read surface must answer four questions:** what your system contains, what governs what,
  what it determined, and what it is. A system that cannot answer these has obligations elsewhere
  that cannot be discharged against it.
- **Every read is decided when it happens**, whatever A8 says.
- **Your declarations are governed like anyone's** — no private admission path for a domain because
  it is new, small, internal, or experimental.
- **Your changes are transformations against a baseline**, not edits to what you own.

# What this sheet cannot produce

Your answers become most of a profile. Three parts are yours to write.

- **Extra obligations** beyond what the answers imply — and each must say what would count as
  breaking it. An obligation nothing could ever refuse is not in force.
- **How each claim is settled**, in enough detail that a demonstration could fail.
- **Whether your profile derives from an existing one**, named explicitly.

And one thing nothing can produce: a profile is supposed to be written by someone other than the
system claiming it. If you write both, the generated profile is still usable — but a conformance
claim made under it has to record that, and the honest record is worth more than the claim.
