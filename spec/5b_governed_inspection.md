# Governed Inspection

## 1. Scope

This document specifies **governed inspection**: the boundary through which a governed system is
interrogated — asked what it contains and what governed determinations have been recorded — without
being altered and without anything being executed.

It closes Part V. The Governed Interaction Boundary specifies how a system is *acted upon*; this
document specifies how it is *asked about*. They are two boundaries of one system, and neither is a
special case of the other.

Inspection is the mechanism several earlier documents depend on. Governed Transformation grounds its
claims about an existing system by reading a baseline through it, and requires that it answer about a
named artifact rather than only enumerate (4d §11.2). The Projection Standard makes inspection a
consumer of projections and never an author of one (4b §9). Evidence, Attestation & Provenance
requires that records be checkable by a party with no access to the producing system (EV-16); the
read boundary is how such a party reaches them.

This document introduces the terms **read operation**, **read**, **query**, **read surface**, and
**caller**. A **caller** is the party that issues a read operation — the party a read operation must
answer rather than supply material to (§8), and the party a read is attributed to where a profile
requires attribution. **A caller is identified, not governed.** Being a caller confers nothing and
requires nothing; whether a read may proceed is determined by the governance applicable to the read
(§11), and there is no governed and ungoverned kind of caller.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. Inspection is a boundary, not a facility

**Inspection is a governed boundary of the same standing as the interaction boundary.**

It is not a debugging affordance, a developer convenience, an administrative back door, or a tool
that happens to read files. What may be asked is declared; what is not declared cannot be asked; and
adding a **read operation** is an authoring act on a governed artifact, not an edit to a mechanism.

The reason is the same one that makes the interaction boundary a boundary: **a read path that is not
governed is a path into the system that nothing determined.** It will be used — by tooling, by
operators, by other systems — and everything reached through it is reached outside the closure that
governs everything else.

> A governed system that cannot answer questions about itself is governed only in principle.

### 2.1 Inspection is reached independently of the interaction boundary

**The two boundaries are of the same standing and are not one boundary.** The interaction boundary
admits proposals that may change governed state (5a §3); inspection admits questions that change
nothing (§3.1). Neither is reached through the other.

Three consequences follow, and the third is the one profiles get wrong:

- **A read operation is not an operation identity at the interaction boundary.** It is not an
  ingress contract, it does not carry a result class, and it is not admitted by anything 5a
  specifies. A realization that routes reads through the interaction boundary has made every read
  subject to a contract that was written for proposals.
- **Selecting no interaction boundary does not remove the read surface.** A system with no ingress
  and no egress is still required to answer what it contains, what governs what, what it
  determined, and what it is (§10). Inspection is not an interaction in 5a's sense, and excluding
  interaction leaves it untouched.
- **Selecting no interaction boundary does not by itself say how the read surface is reached.**
  This family does not specify the means for either boundary — no protocol, no transport, no
  invocation form. A profile that selects no interaction boundary and says nothing further has
  required a read surface without saying by what means a checking party obtains an answer from it,
  and a read surface no party can reach discharges nothing (§10). **A profile that selects no
  interaction boundary MUST state how its read surface is reached** — that it is reached in
  process, by a party with direct access to the sealed representation, or by some other declared
  means. What that means is remains outside this family; that the profile has decided it does not.

**Reached is not permitted.** How a read surface is reached is a question about means; whether a
given read may proceed is a determination under governance (§11). Deciding the first does not
decide the second.

## 3. What inspection is

Three activities answer three different questions, and inspection is the third:

| Activity | Answers |
|---|---|
| construction | may this exist? |
| execution | what happens? |
| **inspection** | **what does this system contain, and what determinations are recorded?** |

### 3.1 Inspection alters nothing

**An inspection MUST NOT change governed state, produce an effect, or modify anything it reads.**

- The sealed representation is read-only to everything downstream (SN-1). Inspection reads it and
  writes nothing back.
- An inspection that recorded something into what it inspected would make the act of asking change
  the answer, and two callers asking the same question would receive different ones.
- Evidence *of* an inspection may of course be produced, as evidence of any determination is. What
  may not happen is that evidence entering the subject of inspection.

### 3.2 Inspection introduces no execution

**Answering a question MUST NOT run anything.**

An inspection that executed a workflow, invoked a capability, or produced an effect in order to
answer would be **an unbudgeted execution path**: execution reached without an interaction, without
an ingress contract, without the authority an interaction carries, and without the evidence an
execution produces.

This is the single most consequential requirement here. Every other governed path into the system
passes through a boundary that determines whether it may proceed; a read path that can execute has
opened one that does not.

Deriving an answer by traversing and evaluating declared structure is not execution (§5). Invoking a
governed executable target is. *Evaluating* here carries the Semantic Model's meaning — applying a
predicate to yield a value, total and free of effect (1b §5) — and never the invocation of anything.

## 4. Read operations are governed contracts

**Every question that may be asked is a declared read operation with its own identity.**

- A read operation identity is an identity in the sense Identity & Addressing specifies: declared,
  authoritative over position, not derived from any address that reaches it.
- Read operations are declared, admitted, constructed, and sealed like anything else. **Adding,
  renaming, or re-pointing one is an authoring act on a governed artifact**, never a change to a
  table inside a mechanism.
- A read operation declares its inputs, its answer shape, and its outcomes, as any contract does.
- **A read operation is not a capability and authorizes no execution.** It is reached to obtain an
  answer, never to cause anything; a read operation that could be invoked for its effect would be a
  capability declared at the wrong boundary.
- **Two systems may legitimately offer different questions.** What may be asked is a property of a
  system's declarations, not of the tooling that reaches it.

## 5. Reading and querying

Read operations divide into two classes, and **the division is load-bearing**:

| Class | Does | Authority it carries |
|---|---|---|
| **read** | projects published material — no traversal, no evaluation | returns what is already determined |
| **query** | derives an answer by traversing and evaluating declared structure | computes a relationship that was not already stated |

- **Every read operation MUST declare which class it is.**
- **A read MUST NOT quietly compute a relationship.** One that does is a query wearing a read's
  clothes: cheaper to call, casually used, and carrying authority it never declared.
- A query MUST derive its answer from declared structure only. Traversing a declared graph is
  permitted; invoking anything is not (§3.2).

The distinction matters because the two differ in what a caller is entitled to conclude. A read
returns something the system already determined. A query returns something the *inspection* derived,
and its correctness depends on the derivation as well as on the material.

## 6. Answering about a named thing

**The read surface MUST be able to answer about a named artifact, not only to enumerate.**

An inspection interface that produces only inventories cannot express a question of the form *what
does this particular thing currently declare?* — and every obligation that depends on such a
question becomes inexpressible where it belongs.

The consequence is concrete and was found by trying: a transformation that must compare a design
against one existing artifact cannot state that rule at design time if grounding can only list. The
rule migrates to a later, weaker check while the realization remains formally conforming (4d §11.2).
**That is a limitation of the interface, not of the rule.**

## 7. Inspection reads projections, not internals

**Inspection MUST read the governed system as it is, never the machinery that produced it.**

- It reads the sealed representation, the projections it carries, and the evidence record (4b §9).
- It MUST NOT reach into construction internals, intermediate state, or anything belonging to a
  mechanism rather than to the system.
- **Transient execution state is not a subject of inspection** unless it is declared governed state.
  That something exists in a running mechanism — a buffer, a cache, a working set — does not make it
  part of the governed system, and reading it is a read of internals like any other.
- A projection or an evidence record read through inspection **remains authoritative only according
  to the authority of its source** (PJ-7, PJ-11). Being returned by an inspection confers nothing;
  what an answer is worth is what its source was worth.

A consumer that reaches into construction internals has taken a dependency on **how the system was
made** rather than on **what it is** — and that dependency breaks whenever the mechanism changes,
while appearing to work until it does. It is also, straightforwardly, a read of something no closure
governs.

## 8. The caller does not derive

**A read operation returns an answer. It MUST NOT return raw material for a caller to compute the
answer from**, where the answer is what was asked for.

A caller that assembles the system's answer for itself has become **a second inspection engine**,
with answers of its own that no declaration governs and no evidence accounts for. Its answers will
diverge from the system's, and the divergence appears only when someone compares them.

**What is prohibited is substitution, not computation.** A caller may compute whatever it likes over
what it was returned, for its own purposes — that is a use of the read surface, and §12 says uses are
not a second kind of inspection. What it MUST NOT do is **present a client-derived result as the
system's answer**, or supply one where a governed answer is required: to a checking party, to an
evidence record, to another governed system, or to a determination. The line is not *did the client
calculate something* but *whose answer is this held out to be*.

Two consequences follow, and they run opposite ways:

- **A report, a dashboard, a spreadsheet, or an analysis built on read results is not a violation.**
  Forbidding downstream computation would forbid the read surface's ordinary purpose, and nothing
  here does.
- **A read operation MUST NOT be designed so that the answer only exists once a client has assembled
  it** (IN-8). Where the system's answer is what is wanted, the system answers; where a client's
  analysis is what is wanted, it is the client's and is not offered as the system's.

Where an answer is not available:

- **the correct remedy is to add a read operation** — a governed authoring act (§4);
- **the incorrect remedy is to assemble it in a client and hold it out as the system's**, which
  produces the answer without the governance.

Every consumer of the read surface is a peer. None holds a capability of its own, and none is
privileged — a surface whose primary client can answer things the surface cannot has already
divided into two.

## 9. Empty is not unanswerable

**An empty answer and an unanswerable question MUST be distinguishable.**

An inspection can be confidently empty and wrong: asked of the wrong material, or of material that
is malformed, it returns nothing and reports success. Nothing about the response says it failed —
and an empty answer is exactly what a correct response often looks like.

Therefore:

- **Malformed or unreadable material MUST produce a refusal**, never an empty answer.
- **A question that cannot be answered MUST be refused**, never answered emptily.
- **A read operation MUST NOT fall back** to a different source, a partial source, or a default when
  what it was asked to read is unavailable.

This is AI-6 at the read boundary: absence of an answer and inability to answer must not produce the
same result. It is stated separately because at this boundary the failure is silent in a way it is
not elsewhere — an execution that cannot proceed stops, while an inspection that cannot answer
returns something a caller will use.

## 10. Sufficiency of the read surface

A read surface MUST be sufficient for the obligations other documents place on it. At minimum, a
governed system MUST be able to answer:

- **what it contains** — its admitted artifacts, enumerably and individually (§6);
- **what governs what** — the closure applicable to a named subject;
- **what it determined** — the evidence of its determinations, sufficient for the checks Evidence,
  Attestation & Provenance requires;
- **what it is** — its identity, its constituents, and what it claims (SN-5).

A system unable to answer any of these has an obligation elsewhere in this family that cannot be
discharged against it. **Sufficiency is therefore not a quality of the read surface but a condition
of the system being checkable at all.**

## 11. Reading is governed

**Reachability is not permission** (CP-11). That a read operation exists and can be reached does not
establish that a given caller may reach it.

- Whether a read may proceed is determined by the governance applicable to that determination, like
  any other (2e).
- **What may be read is as much a governed question as what may be done.** A system whose read
  surface is universally open has decided that, and should have decided it deliberately.
- A refusal to answer is a determination and is evidenced like any other (EN-8).

**How this reconciles with a profile's decision.** 6a §7 defers *how open the read surface is* to a
profile, and this section requires that a read proceed only by determination. The two are not in
conflict, and the line between them is this:

| Decided by | What it fixes |
|---|---|
| **the profile** | the **policy** — which classes of caller the system's governance admits to which declared read operations, up to and including all callers to all of them |
| **the system's governance, per read** | the **determination** — that this read, now, under the applicable closure, proceeds or is refused |

A profile MAY fix the policy completely. **A profile MUST NOT dispense with the determination.** A
profile stating that every caller may issue every declared read has selected the most permissive
policy available; it has not established that any particular read proceeded without one, and a
realization that answers a read it never determined has an ungoverned read path (§2) whatever the
profile says. The distinction is observable: under an open policy the determination still produces
evidence, still distinguishes rule refusal from closure failure (2f §6.2), and still refuses a read
whose subject is unavailable or malformed (IN-9).

A profile that reads the open policy as permission to answer without determining has widened where
it appeared to parameterize (NP-11).

## 12. Observability is a use, not a semantics

Metrics, tracing, diagnostics, dashboards, and operational monitoring are **uses** of the read
surface and of the evidence record. They are not a second kind of inspection with rules of its own.

- **Nothing is admitted at the read boundary because a tool would find it convenient.** A question
  worth asking is worth declaring as a read operation; a question not worth declaring is not asked.
- An observability need that cannot be met by a declared read operation is a request for a new read
  operation, and is answered by authoring one (§8).
- A side channel opened for observation is an ungoverned read path, and §2 applies to it exactly as
  to any other.

## 13. Before anything can be inspected

Inspection presupposes something sealed to inspect. **Genesis precedes it**: the first snapshot is
constituted before any inspection of it is possible, and a transformation producing a first baseline
has no baseline to ground against (4d §12).

A realization MUST NOT resolve that by inspecting a partially constructed system. **There is nothing
to inspect until there is a sealed representation**, and a read of construction-in-progress is a read
of internals (§7) against material that no determination has yet admitted.

## 14. What this document does not specify

- **What questions a system offers.** A property of its declarations; two systems may differ.
- **The answer shapes**, their encoding, or how a response is carried.
- **How the read surface is reached** — a protocol, a library, a command line, or an external
  boundary binding (5a).
- **Whether reads are attributed**, retained, or rate-limited. Operational questions a profile may
  answer.
- **Authority evaluation for reads** (2e's subject; §11 requires only that reading be governed).

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
- **IN-8.** A read operation MUST return the answer asked for, and MUST NOT delegate its derivation
  to the caller (§8).
- **IN-9.** Malformed or unreadable material MUST produce a refusal, and an unanswerable question
  MUST be refused rather than answered emptily (§9).
- **IN-10.** A read operation MUST NOT fall back to another source, a partial source, or a default
  (§9).
- **IN-11.** A governed system MUST be able to answer what it contains, what governs what, what it
  determined, and what it is (§10).
- **IN-12.** Whether a read may proceed MUST be determined by the governance applicable to it;
  reachability MUST NOT constitute permission (§11).
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

A read surface conforms when every question it answers is a declared operation, no answer requires
execution, nothing it reads is altered, its classes are declared and honored, it can answer about
named things, it refuses rather than answering emptily, and no path reaches the system's contents
except through it.

**Two properties are established only negatively, and both are invisible from a working system.**
That inspection introduces no execution is shown by the absence of any reachable path from a read
operation to an executable target — not by observing reads that happened not to take one. That no
ungoverned read path exists is shown by the same kind of absence; a side channel used only by one
tool is used, and is a path.

**A third is established by comparison**: that the caller does not derive is shown by a second,
independently written client returning the same answers. A surface whose clients diverge has already
placed some of its answers outside itself.

How these are required and evaluated belongs to the Conformance Test Specification.
