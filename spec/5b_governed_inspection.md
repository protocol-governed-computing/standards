# Governed Inspection

## 1. Scope

This document specifies **governed inspection**: the boundary through which a party questions a
governed system. The party asks what the system contains and what governed determinations it has
recorded. Inspection alters nothing and executes nothing.

This document closes Part V. The Governed Interaction Boundary specifies how a party *acts on* a
system. This document specifies how a party *asks about* it. They are two boundaries of one system,
and neither is a special case of the other.

Several earlier documents depend on inspection:

- Governed Transformation grounds its claims about an existing system by reading a baseline through
  inspection. It requires inspection to answer about a named artifact, not only enumerate (Governed
  Transformation §11.2).
- The Projection Standard makes inspection a consumer of projections, never an author of one
  (Projection Standard §9).
- Evidence, Attestation & Provenance requires that a party with no access to the producing system
  can check records (EV-16). The read boundary is how such a party reaches them.

This document introduces the terms **read operation**, **read**, **query**, **read surface**, and
**caller**. A **caller** is the party that issues a read operation. A read operation must answer the
caller, not supply it material (§8). Where a profile requires attribution, a read is attributed to its
caller. **A caller is identified, not governed.** Being a caller confers nothing and requires
nothing. The governance applicable to the read determines whether it may proceed (§11). There is no
governed and ungoverned kind of caller.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Inspection is a boundary, not a facility

**Inspection is a governed boundary of the same standing as the interaction boundary.**

It is not a debugging aid, a developer convenience, an administrative back door, or a tool that
happens to read files. What may be asked is declared. Only declared questions can be asked. Adding a
**read operation** is an authoring act on a governed artifact, not an edit to a mechanism.

The reason is the same one that makes the interaction boundary a boundary: **a read path that is not
governed is a path into the system that nothing determined.** Tooling, operators and other systems
will use it. Everything reached through it is reached outside the closure that governs everything
else.

> A governed system that cannot answer questions about itself is governed only in principle.

### 2.1 Inspection is reached independently of the interaction boundary

**The two boundaries have the same standing, and they are not one boundary.** The interaction
boundary admits proposals that may change governed state (Governed Interaction Boundary §3).
Inspection admits questions that change nothing (§3.1). Neither is reached through the other.

Three consequences follow. Profiles get the third one wrong:

- **A read operation is not an operation identity at the interaction boundary.** It is not an ingress
  contract. It carries no result class. Nothing the Governed Interaction Boundary specifies admits
  it. A realization that routes reads through the interaction boundary has subjected every read to a
  contract written for proposals.
- **A system that selects no interaction boundary still has its read surface.** A system with no
  ingress and no egress must still answer what it contains, what governs what, what it determined,
  and what it is (§10). Inspection is not an interaction in the Governed Interaction Boundary's
  sense, and excluding interaction leaves inspection untouched.
- **Selecting no interaction boundary does not, alone, say how the read surface is reached.** This
  family specifies no means for either boundary: no protocol, no transport, no invocation form.
  Suppose a profile selects no interaction boundary and says nothing more. It has required a read
  surface without saying how a checking party gets an answer from it. A read surface that no party
  can reach discharges nothing (§10). **A profile that selects no interaction boundary MUST state how
  its read surface is reached.** It may be reached in process, by a party with direct access to the
  sealed representation, or by some other declared means. Which means is outside this family. That
  the profile has decided is not.

**Reached is not permitted.** How a read surface is reached is a question about means. Whether a
given read may proceed is a determination under governance (§11). Deciding the first does not decide
the second.

## 3. What inspection is

Three activities answer three different questions. Inspection is the third:

| Activity | Answers |
|---|---|
| construction | may this exist? |
| execution | what happens? |
| **inspection** | **what does this system contain, and what determinations are recorded?** |

### 3.1 Inspection alters nothing

**An inspection MUST NOT change governed state, produce an effect, or modify anything it reads.**

- The sealed representation is read-only to everything downstream (SN-1). Inspection reads it and
  writes nothing back.
- Suppose an inspection recorded something into what it inspected. Asking would then change the
  answer, and two callers asking the same question would receive different answers.
- A system may of course produce evidence *of* an inspection, as it does of any determination. That
  evidence may not enter the subject of the inspection.

### 3.2 Inspection introduces no execution

**Answering a question MUST NOT run anything.**

Suppose an inspection executed a workflow, invoked a capability or produced an effect in order to
answer. It would be **an unbudgeted execution path**. Execution would be reached without an
interaction, without an ingress contract, without the authority an interaction carries, and without
the evidence an execution produces.

This is the most consequential requirement in this document. Every other governed path into the
system passes through a boundary that determines whether it may proceed. A read path that can execute
opens one that does not.

Deriving an answer by traversing and evaluating declared structure is not execution (§5). Invoking a
governed executable target is execution. *Evaluating* here carries the Semantic Model's meaning:
applying a predicate to yield a value, totally and without effect (Semantic Model §5). It never means
invoking anything.

## 4. Read operations are governed contracts

**Every question that may be asked is a declared read operation with its own identity.**

- A read operation identity is an identity in the sense Identity & Addressing specifies: declared,
  authoritative over position, and never derived from an address that reaches it.
- Read operations are declared, admitted, constructed and sealed like anything else. **Adding,
  renaming or re-pointing one is an authoring act on a governed artifact.** It is never a change to a
  table inside a mechanism.
- A read operation declares its inputs, its answer shape and its outcomes, as any contract does.
- **A read operation is not a capability, and it authorizes no execution.** A party reaches it to
  obtain an answer, never to cause anything. A read operation that could be invoked for its effect
  would be a capability declared at the wrong boundary.
- **Two systems may legitimately offer different questions.** What may be asked is a property of a
  system's declarations, not of the tooling that reaches it.

## 5. Reading and querying

Read operations divide into two classes, and **the division carries weight**:

| Class | Does | Authority it carries |
|---|---|---|
| **read** | projects published material — no traversal, no evaluation | returns what is already determined |
| **query** | derives an answer by traversing and evaluating declared structure | computes a relationship that was not already stated |

- **Every read operation MUST declare which class it is.**
- **A read MUST NOT quietly compute a relationship.** A read that does is a query in disguise: cheaper
  to call, casually used, and carrying authority it never declared.
- A query MUST derive its answer from declared structure only. It may traverse a declared graph. It
  may not invoke anything (§3.2).

The distinction matters because the two entitle a caller to different conclusions. A read returns
something the system already determined. A query returns something the *inspection* derived. Its
correctness depends on both the derivation and the material.

## 6. Answering about a named thing

**The read surface MUST be able to answer about a named artifact, not only enumerate.**

An inspection interface that produces only inventories cannot express a question of the form *what
does this particular thing currently declare?* Every obligation that depends on such a question then
becomes inexpressible where it belongs.

The consequence is concrete, and it was found by trying. A transformation that must compare a design
against one existing artifact cannot state that rule at design time if grounding can only list. The
rule migrates to a later, weaker check, while the realization stays formally conforming (Governed
Transformation §11.2). **That is a limitation of the interface, not of the rule.**

## 7. Inspection reads projections, not internals

**Inspection MUST read the governed system as it is, never the machinery that produced it.**

- It reads the sealed representation, the projections it carries, and the evidence record
  (Projection Standard §9).
- It MUST NOT reach into construction internals, intermediate state, or anything that belongs to a
  mechanism rather than to the system.
- **Transient execution state is not a subject of inspection** unless it is declared governed state.
  A buffer, a cache or a working set may exist in a running mechanism. That does not make it part of
  the governed system. Reading it is a read of internals like any other.
- A projection or an evidence record read through inspection **is authoritative only to the extent
  its source is** (PJ-7, PJ-11). Being returned by an inspection confers nothing. An answer is worth
  what its source was worth.

A consumer that reaches into construction internals has taken a dependency on **how the system was
made**, not on **what it is**. That dependency breaks whenever the mechanism changes, and it appears
to work until then. It is also, plainly, a read of something no closure governs.

## 8. The caller does not derive

**A read operation returns an answer. It MUST NOT return raw material for a caller to compute the
answer from**, where the answer is what was asked for.

A caller that assembles the system's answer for itself has become **a second inspection engine**. Its
answers are its own. No declaration governs them, and no evidence accounts for them. They will diverge
from the system's, and the divergence appears only when someone compares them.

**The rule prohibits substitution, not computation.** A caller may compute whatever it likes over what
it was returned, for its own purposes. That is a use of the read surface, and §12 says uses are not a
second kind of inspection. A caller MUST NOT **present a client-derived result as the system's
answer**. Nor may it supply one where a governed answer is required: to a checking party, to an
evidence record, to another governed system, or to a determination. The question is not *did the
client calculate something*. It is *whose answer is this held out to be*.

Two consequences follow, and they run in opposite directions:

- **A report, a dashboard, a spreadsheet or an analysis built on read results is not a violation.**
  Forbidding downstream computation would forbid the read surface's ordinary purpose, and nothing here
  does.
- **A read operation MUST NOT be designed so that the answer exists only once a client has assembled
  it** (IN-8). Where the system's answer is wanted, the system answers. Where a client's analysis is
  wanted, the analysis belongs to the client and is not offered as the system's.

Where an answer is not available:

- **the correct remedy is to add a read operation**, a governed authoring act (§4);
- **the incorrect remedy is to assemble the answer in a client and hold it out as the system's.** That
  produces the answer without the governance.

Every consumer of the read surface is a peer. None holds a capability of its own, and none is
privileged. If a surface's primary client can answer things the surface cannot, the surface has
already split in two.

## 9. Empty is not unanswerable

**An empty answer and an unanswerable question MUST be distinguishable.**

An inspection can be confidently empty and wrong. Asked of the wrong material, or of malformed
material, it returns nothing and reports success. Nothing in the response says it failed. And an
empty answer is exactly what a correct response often looks like.

Therefore:

- **Malformed or unreadable material MUST produce a refusal**, never an empty answer.
- **A question that cannot be answered MUST be refused**, never answered emptily.
- **A read operation MUST NOT fall back** to a different source, a partial source or a default when
  what it was asked to read is unavailable.

This is AI-6 at the read boundary: absence of an answer and inability to answer must not produce the
same result. This document states it separately because at this boundary the failure is silent in a
way it is not elsewhere. An execution that cannot proceed stops. An inspection that cannot answer
returns something a caller will use.

## 10. Sufficiency of the read surface

A read surface MUST be sufficient for the obligations other documents place on it. At minimum, a
governed system MUST be able to answer:

- **what it contains**: its admitted artifacts, enumerably and individually (§6);
- **what governs what**: the closure applicable to a named subject;
- **what it determined**: the evidence of its determinations, sufficient for the checks Evidence,
  Attestation & Provenance requires;
- **what it is**: its identity, its constituents, and what it claims (SN-5).

If a system cannot answer one of these, some obligation elsewhere in this family cannot be
discharged against it. **So sufficiency is not a quality of the read surface. It is a condition of
the system being checkable at all.**

## 11. Reading is governed

**Reachability is not permission** (CP-11). A read operation that exists and can be reached is not
thereby open to a given caller.

- The governance applicable to that determination decides whether a read may proceed, as with any
  other determination (Governance Closure & Authority).
- **What may be read is as much a governed question as what may be done.** A system whose read
  surface is open to everyone has decided that, and should have decided it deliberately.
- A refusal to answer is a determination, and it is evidenced like any other (EN-8).

**How this reconciles with a profile's decision.** Normative Platform Profile §7 leaves *how open the
read surface is* to a profile. This section requires that a read proceed only by determination. The
two do not conflict. The line between them is this:

| Decided by | What it fixes |
|---|---|
| **the profile** | the **policy** — which classes of caller the system's governance admits to which declared read operations, up to and including all callers to all of them |
| **the system's governance, per read** | the **determination** — that this read, now, under the applicable closure, proceeds or is refused |

A profile MAY fix the policy completely. **A profile MUST NOT dispense with the determination.** A
profile that lets every caller issue every declared read has selected the most permissive policy
available. It has not established that any particular read proceeded without a determination. A
realization that answers a read it never determined has an ungoverned read path (§2), whatever the
profile says. The difference is observable. Under an open policy, the determination still:

- produces evidence;
- distinguishes rule refusal from closure failure (Enforcement & Refusal §6.2);
- refuses a read whose subject is unavailable or malformed (IN-9).

A profile that reads the open policy as permission to answer without determining has widened where
it appeared only to parameterize (NP-11).

## 12. Observability is a use, not a semantics

Metrics, tracing, diagnostics, dashboards and operational monitoring are **uses** of the read surface
and of the evidence record. They are not a second kind of inspection with rules of its own.

- **Nothing is admitted at the read boundary because a tool would find it convenient.** A question
  worth asking is worth declaring as a read operation. A question not worth declaring is not asked.
- An observability need that no declared read operation meets is a request for a new read operation.
  The answer is to author one (§8).
- A side channel opened for observation is an ungoverned read path, and §2 applies to it exactly as to
  any other.

## 13. Before anything can be inspected

Inspection presupposes something sealed to inspect. **Genesis precedes it.** The first snapshot is
constituted before anyone can inspect it. A transformation that produces a first baseline has no
baseline to ground against (Governed Transformation §12).

A realization MUST NOT work around that by inspecting a partially constructed system. **There is
nothing to inspect until there is a sealed representation.** A read of construction in progress is a
read of internals (§7), against material that no determination has yet admitted.

## 14. What this document does not specify

- **What questions a system offers.** That is a property of its declarations, and two systems may
  differ.
- **The answer shapes**, their encoding, or how a response is carried.
- **How the read surface is reached**: a protocol, a library, a command line, or an external boundary
  binding (Governed Interaction Boundary).
- **Whether reads are attributed**, retained or rate-limited. These are operational questions a
  profile may answer.
- **Authority evaluation for reads.** That is the subject of Governance Closure & Authority. §11
  requires only that reading be governed.

## 15. Normative invariants

- **IN-1.** Inspection MUST NOT change governed state, produce an effect, or modify what it reads
  (§3.1).
- **IN-2.** Answering a read operation MUST NOT invoke a governed executable target or otherwise
  introduce execution (§3.2).
- **IN-3.** Every question that may be asked MUST be a declared read operation with a declared
  identity, admitted and sealed like any other artifact (§4).
- **IN-4.** A read operation MUST declare whether it reads or queries, and a read MUST NOT compute a
  relationship (§5).
- **IN-5.** A query MUST derive its answer from declared structure only (§5).
- **IN-6.** The read surface MUST be able to answer about a named artifact, not only to enumerate
  (§6).
- **IN-7.** Inspection MUST read the governed system and its projections, and MUST NOT read
  construction internals or mechanism state (§7).
- **IN-8.** A read operation MUST return the answer asked for, and MUST NOT delegate its derivation to
  the caller (§8).
- **IN-9.** Malformed or unreadable material MUST produce a refusal, and an unanswerable question MUST
  be refused rather than answered emptily (§9).
- **IN-10.** A read operation MUST NOT fall back to another source, a partial source, or a default
  (§9).
- **IN-11.** A governed system MUST be able to answer what it contains, what governs what, what it
  determined, and what it is (§10).
- **IN-12.** Whether a read may proceed MUST be determined by the governance applicable to it.
  Reachability MUST NOT constitute permission (§11).
- **IN-13.** No read path MUST exist that is not a declared read operation (§2, §12).
- **IN-14.** Inspection MUST NOT be performed against a representation that has not been sealed
  (§13).
- **IN-15.** Inspection MUST be reachable independently of the interaction boundary, and a read
  operation MUST NOT be admitted as an interaction at that boundary (§2.1).
- **IN-16.** An open read-surface policy MUST NOT dispense with the determination IN-12 requires
  (§11).

## 16. Conformance

The conformance subject of this document is a **read surface**: the read operations a governed system
declares, together with what they return and what they refuse.

A read surface conforms when all of the following hold:

- every question it answers is a declared operation;
- no answer requires execution;
- nothing it reads is altered;
- its classes are declared and honored;
- it can answer about named things;
- it refuses instead of answering emptily;
- no path reaches the system's contents except through it.

**Only absence can establish two of these properties, and a working system shows neither:**

- That inspection introduces no execution is shown by the absence of any reachable path from a read
  operation to an executable target. Observing reads that happened not to take such a path shows
  nothing.
- That no ungoverned read path exists is shown by the same kind of absence. A side channel that only
  one tool uses is still used, and it is still a path.

**Comparison establishes a third.** A second, independently written client that returns the same
answers shows that the caller does not derive. A surface whose clients diverge has already placed
some of its answers outside itself.

The Conformance Test Specification owns how these are required and evaluated.
