# Domain Profiles

## 1. Scope

This document specifies how a **domain** — a business or application region of a governed system —
declares what it governs, what it may do, and what it accepts by being part of a larger whole.

It closes Part VI. The Normative Platform Profile specifies what a profile is; Execution Environment
Profiles specify profiles whose subject is a substrate; this document specifies profiles whose
subject is a **region of the system itself**, and the boundary between what a platform governs and
what a domain does.

A domain profile is a **profile** in the sense the Normative Platform Profile specifies, and every
rule there applies unchanged: it narrows and never widens, redefines nothing, exempts nothing, and is
not authored by the system that claims it. It selects and constrains domain-level declarations; **it
extends neither the authority of the platform profile nor that of the family.**

**A domain is a subject of profiling.** Whether that subject is itself an authority is a
determination made under Governance Closure & Authority, not a consequence of calling it a domain
(§4).

This document introduces the term **domain profile**.

Keywords MUST, SHOULD, MAY per RFC 2119.

## 2. What a domain is

A **domain** is a bounded region of a governed system that owns its declarations and is responsible
for them (1a).

**A domain is a governance boundary.** It is not a directory, a package, a repository, a team, a
deployment unit, or a namespace. Where those coincide with a domain in some system, the coincidence
is that system's arrangement and not what makes the domain one.

- A domain is *bounded*: what belongs to it is determinable, and what does not is outside it.
- A domain *owns*: it is responsible for its declarations and answerable for them (CA §4).
- A domain is *within*: it exists inside a larger governed system whose governance reaches it.

**A domain boundary and an execution environment boundary are unrelated.** An environment boundary —
a cluster, a namespace, an account, a region — does not establish a domain, and a domain does not
establish an environment. Where they coincide, that is an arrangement; neither constitutes the other,
and neither constitutes an authority (6b §4, CA-2).

## 3. The ownership boundary

The central question this document answers is where platform governance ends and domain governance
begins.

| | Owns | Examples of what it settles |
|---|---|---|
| **platform** | how anything is governed, constructed, executed, and evidenced | the declaration surface, the kind vocabulary, the closure mechanism, the execution model, the boundary contracts |
| **domain** | what its own subjects are, and what may be done with them | its workflows, its capability contracts, its stores, its obligations over its own subjects |

The line is not where most systems draw it, and stating it precisely matters:

> **The platform governs the *form* of governance. The domain governs its own *subjects*.**

A domain does not get to decide *how* governance works — what a closure is, what refusal means,
whether evidence is produced. It decides *what its rules are* within a mechanism it does not own.

### 3.1 The domain does not weaken what reaches it

Platform governance **reaches into** a domain; domain governance does not reach out.

- A domain MUST NOT weaken, exempt itself from, or reinterpret any governance applicable to it
  (NP-4).
- A domain MUST NOT declare an obligation that contradicts one already applicable. Where its
  declarations and the platform's compose, they compose by dominance like any others (GS-8) — the
  domain can only add restriction.
- **A domain that could relax what governs it would be an authority over the platform**, which is
  the opposite of what a domain is.

## 4. Is a domain an authority?

**Sometimes. The standard supplies the test; it does not supply the answer for any system.**

A domain is a distinct governance authority only if it satisfies what Governance Closure & Authority
requires of one: a declared constituting act, and answers to all five questions — establishable from
declared artifacts alone — namely who the authority is, what constituted it, what subjects fall
within it, **what decision it may make that no other authority may**, and how it relates to the
authorities above and beside it (CA-3). It must additionally satisfy the independence test (CA-4).

A domain that does not satisfy them is not thereby illegitimate. **It is a concern, governed under
the authority above it** (2b §7.2) — organized, named, indexed, and governed, with no jurisdiction of
its own. That is an ordinary and correct arrangement.

What is not permitted is the third case:

- **A domain MUST NOT be treated as an authority without satisfying the test**, and MUST NOT acquire
  jurisdiction by being named, bounded, deployed separately, or owned by a different team (CA-2).
- **A concern classification MUST NOT constitute an authority** (CA-6).

Whether the domains of any particular system are authorities or concerns is a determination about
that system, made under its own governance. This document does not decide it, and a profile that
asserts it without discharging CA-3 has asserted rather than established it.

## 5. What a domain declares

A domain profile declares, for the domain it profiles:

| Declares | Meaning |
|---|---|
| **its subjects** | what the domain owns and is responsible for |
| **its governance** | the obligations applicable to its subjects under the governing authority — its own, where it has constituted authority (§4) |
| **its capabilities** | the contracts through which its work is reached (3d) |
| **its workflows** | the structures through which its work is ordered (3a) |
| **its stores** | the governed state it owns, and what may write to it (3a §6.2) |
| **its boundary exposure** | what of it is reachable from outside, and how (5a, 5b) |
| **its authority claim** | whether it claims to be an authority, and on what basis (§4) |

The last is not optional. **A domain profile that does not state whether the domain is an authority
or a concern has left the question to be answered by whoever needs an answer** — and it will be
answered differently by different parties, each reasonably.

## 6. What a domain accepts

By being part of a governed system, a domain accepts obligations it does not get to decline:

- **Its declarations are governed.** They are admitted, determined, and refused like any others; a
  domain has no private admission path (GC-4).
- **Its changes are transformations.** A domain evolves through governed transformation against a
  baseline, not by editing what it owns (TR-1, TR-15).
- **Its effects are enumerable.** Everything it can do to the world passes through declared effecting
  capabilities (CP-8), and its reach is part of what the composed system can state about itself.
- **Its state is owned and its writes are authorized** (3a §6.2). Ownership of a store means
  controlling what may write to it, not merely holding it.
- **It is subject to composition obligations.** Rules quantifying over the whole are determined over
  the whole, and a domain that is individually admissible may still make a composition inadmissible
  (GC-11).
- **It carries no exemption for being new, small, experimental, or internal.**

## 7. Between domains

A domain is bounded, and the boundary means something:

- **Reads across a boundary MAY be declared and permitted.** What one domain exposes to another is a
  declared surface, and what is not exposed is not reachable (1a, *surface*).
- **Writes across a boundary are authorized by the governance applicable to the store, never by
  reach** (3a §6.2). A domain able to address another domain's state has not thereby acquired the
  right to change it, and an owner that does not control its own writes does not own the state.
- **A domain MUST NOT depend on another domain's internals.** What it may depend on is what the
  other declares; what the other happens to do is not a dependency it is entitled to take.
- **Cross-domain dependence is declared and therefore visible.** A composition can state which
  domains depend on which, because every dependence passed through a declaration.

Where two domains are two authorities, the relation between them is **federation** (CA §9). Where
they are two concerns of one authority, it is not — they are that authority's concerns, and calling
the relation federation would assert two jurisdictions that were never constituted.

## 8. Domain kinds

A domain MAY **propose artifact kinds for admission** into the vocabulary its profile declares. It
does not create them: admission is the vocabulary's act, not the domain's (KV-3).

- Admitting one requires naming the semantic category it occupies and the provenance it carries
  (GO-3, 2b §8), and its kind contract.
- **Admitting a domain kind MUST NOT require an ontology revision** (GO-12). A domain kind that
  cannot be classified under an existing category has not revealed a gap in the ontology; it has more
  often revealed that the kind is two things, or that it is a concern rather than a classification.
- A domain kind is admitted into the vocabulary the system's profile declares (KV-6), and is subject
  to every rule that governs any kind. **A domain does not have a private vocabulary.**

## 9. Governance as subject matter

A domain's business may itself be governing something in the world — agents, transactions, licences,
access, people.

**Such a domain is an application built with this family. It is not the governance this family
defines**, and the two MUST NOT be conflated (1a §5).

| | Is | Governed by |
|---|---|---|
| the family's governance | what determines what the software may construct and execute | this family |
| a governance domain's rules | business declarations about a subject in the world | the platform, like any domain's declarations |

The distinction has a practical consequence that is easy to get wrong: **a domain that governs
something in the world has no more authority over the system than any other domain.** That its
subject matter is governance does not make its declarations governing elements of the platform, and
a system that let them become so would have a domain deciding how the platform governs — which §3.1
forbids.

## 10. Adding and removing a domain

- **Adding a domain is a governed transformation** of the system it joins (TR-1). The domain's
  declarations are candidates; they are determined admissible or refused like any others.
- **A domain MUST NOT claim genesis.** A system's first transformation is its only one without a
  baseline (TR-15a); a domain introduced afterwards — however whole, however self-contained — is
  introduced by transformation against a baseline that exists (4d §12.5).
- **Removing a domain is likewise a transformation**, and invalidates every reference to what it
  removed. A composition retaining a reference to a removed domain's subject is inadmissible, and
  the removal is what must be determined complete — not the absence noticed later.

## 11. What this document does not specify

- **What domains a system has**, or how many.
- **Whether any particular domain is an authority or a concern** (§4). The test is supplied; the
  determination is per system.
- **How domains are arranged** — in repositories, packages, or deployments. None of those is a
  domain (§2).
- **What a domain's business is**, or what subjects it governs.
- **Whether a domain is separately versioned, released, or operated.** Arrangement, not governance.

## 12. Normative invariants

- **DP-1.** A domain MUST NOT weaken, exempt itself from, or reinterpret governance applicable to it
  (§3.1).
- **DP-2.** A domain's declarations MUST compose with applicable governance by dominance; a domain
  MUST NOT declare an obligation that contradicts one already applicable (§3.1).
- **DP-3.** A domain MUST NOT be treated as an authority without satisfying the authority test, and
  MUST NOT acquire jurisdiction by being named, bounded, deployed separately, or separately owned
  (§4).
- **DP-4.** A domain profile MUST state whether the domain claims to be an authority or is a concern
  (§5).
- **DP-5.** A domain MUST have no private admission path; its declarations are admitted as any others
  are (§6).
- **DP-6.** A domain MUST change only through governed transformation against a baseline (§6, §10).
- **DP-7.** A write across a domain boundary MUST be authorized by the governance applicable to the
  store written, and MUST NOT be authorized by reach (§7).
- **DP-8.** A domain MUST NOT depend on another domain's internals; dependence MUST be on what the
  other declares (§7).
- **DP-9.** Admitting a domain kind MUST NOT require an ontology revision, and a domain MUST NOT
  hold a private vocabulary (§8).
- **DP-10.** A domain whose subject matter is governance MUST NOT thereby acquire authority over the
  platform (§9).
- **DP-11.** A domain MUST NOT claim genesis (§10).

## 13. Conformance

The conformance subject of this document is a **domain profile**: what a domain declares, what it
claims, and what it accepts.

A domain profile conforms when it declares its subjects, its governance, and its authority position;
adds restriction without relaxing anything; holds no private admission path or vocabulary; depends on
other domains only through what they declare; and accepts the obligations of §6 without exception.

**The failure to look for is authority acquired by arrangement.** A domain that is separately
repositoried, separately deployed, separately owned, and separately released looks like a sovereign
and will be treated as one — and none of those four facts is a constituting act (CA-2). The test is
CA-3's fourth question, and it is asked of the declarations rather than of the arrangement: **what
decision may this domain make that no other authority may?** A domain with no answer is a concern,
whatever its infrastructure suggests.

How this is required and evaluated belongs to the Conformance Model and the Conformance Test
Specification.
