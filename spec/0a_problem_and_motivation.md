# Problem and Motivation

*Non-normative. This document makes no requirement and confers no authority. It states the problem
Protocol-Governed Computing exists to address, for a reader who wants the case before the
specification. The arguments are developed at length elsewhere; §8 says where.*

## 1. Maintenance dominates, and that is a symptom

Most software money is spent sustaining systems rather than building them — consistently 60–80% of
expenditure, across two decades of measurement. The ratio is treated as normal.

It is a signal. A cost structure in which sustaining a system outgrows creating it says something
about how the system was built, not about how well it is being maintained. The useful question is
not *how do we maintain better* but **why does maintenance dominate**.

The answer is not people, process, or tooling. It is structural.

## 2. The expensive problem is not computation

There are two quite different software problems, and conflating them misplaces the entire cost.

| | Bounded by | Cost concentrated in |
|---|---|---|
| **computational software** — an algorithm, a transform, a kernel | its specification | getting it right once |
| **business software** — rules, workflows, authorization, exceptions, obligations, integrations | its accumulated history | keeping its meaning intact over decades |

The second is where organizational capital actually sits: business knowledge, policies, data
semantics, controls, compliance obligations, operational assumptions, and migration history — most
of it never written down as anything a machine can check.

**Replacing the code is not equivalent to replacing the software.** A rewrite reproduces the
computation and loses the accumulation, which is why rewrites of mature business systems fail in a
characteristic way: undocumented behavior is discovered in production, one exception at a time.

## 3. What accumulates is governance debt

The rules that constrain a mature system are real and load-bearing. They live in code paths, review
conventions, wiki pages, and the memories of long-serving engineers — everywhere except in a form
anything can validate.

That accumulation is **structural governance debt**: the cost of embedding governance decisions in
code rather than in explicit, checkable declarations. It is not technical debt and does not behave
like it.

- **It is invisible to code-level measures.** Test coverage, complexity, and static analysis do not
  see it.
- **It compounds superlinearly** as implicit relationships between components multiply.
- **It cannot be repaid by refactoring.** Rewrite every function to be clean and idiomatic and the
  debt is unchanged, because the constraints that should bind behavior to intent still do not exist
  as artifacts.

Its visible form is **fear of change** — which is not timidity but a rational response to a system
whose dependencies are implicit. Every change is a gamble whose odds nobody can compute.

Its organizational form is the machinery built to compensate: architecture review boards, change
advisory boards, cross-team synchronization. **These are human governance mechanisms substituting
for architectural ones.**

## 4. Existing remedies govern a layer and stop

Each of the industry's advances governs something real, and none reaches the semantic layer.

| Remedy | Governs | Cannot govern |
|---|---|---|
| CI/CD | build and deploy | behavioral semantics; inter-component contracts |
| microservices | boundaries and interface schemas | behavior *behind* interfaces; cross-service invariants |
| infrastructure-as-code | topology and provisioning | application logic; business rules |
| feature flags | activation state | the semantic consequences of activation |

Microservices are the instructive case: the governance gap does not shrink when a monolith is
decomposed. **It relocates** — from inside the monolith to between services, where it is harder to
see and harder to test. Shipping gets faster; shipping correctly does not.

High-assurance domains — aviation, telecom — do achieve structural governance, and they do it
*externally*: formal specification, certification regimes, and sustained human discipline at a cost
most software cannot bear. They establish that structural governance works. The open question is
whether it can be a property of the system rather than an institution around it.

## 5. AI removes the last throttle

The deficit predates AI. What is new is the rate.

```
code generation velocity        accelerating
governance establishment        bounded by human deliberation
```

The widening gap between them is the **generation–governance impedance mismatch**. Human coding
speed was the last natural throttle on the accumulation of governance debt, and it is being removed.

This is not an argument against machine-generated software. It is the observation that **when
producing code becomes cheap, establishing what the produced system means becomes the scarce
thing** — and that a model which cannot express meaning in checkable form gets worse, not better,
as generation gets faster.

## 6. The sweet spot, and what it is not

Protocol-Governed Computing is aimed at software where behavior is more than computation and lasts
longer than its authors: large, long-lived, rule-intensive systems in regulated or operationally
consequential settings — financial, industrial, clinical, governmental, supply-chain, enterprise
workflow, and anything carrying long-term traceability obligations.

**It is not aimed at** numerical algorithms, scientific computation, signal and image processing,
utility libraries, small computational functions, or performance-critical inner loops. Those are
bounded problems with a different cost structure, and a governance apparatus around them is
overhead without a return.

Stating this plainly matters, because a model presented as *how all software should be written* will
be judged — correctly — as overreach.

## 7. What would count as success

A mature realization of this idea would let an organization:

1. state business intent in a form a machine can consume;
2. express governing constraints explicitly rather than by convention;
3. construct a system from those declarations rather than from interpretation of them;
4. establish that what was constructed is what was declared;
5. run it without behavior arriving from anywhere undeclared;
6. ask it what it contains and what it decided;
7. change it through a governed act rather than an edit;
8. show, to someone who was not there, that it continued to conform; and
9. replace the implementation without losing the accumulated meaning.

The last is the point of the other eight. **The ambition is to make the software lifecycle itself
governable** — not to make execution safer at one moment, but to keep a system's meaning intact and
demonstrable from its first construction to its retirement.

Whether that ambition is realized is a question for the normative documents and for the systems
built against them. This document only claims that the problem is real, expensive, and structural.

## 8. Where this is developed

This is a summary. The argument is made in full elsewhere:

- **The diagnosis** — the application-centric model, its three structural properties, the failure
  categories, and structural governance debt with its formal definition: *Protocol-Governed
  Systems*, Chapter 1, "Why Software Breaks at Scale."
- **Where behavioral authority sits, and what follows from moving it**: Ganti, B.
  *Protocol-Governed Computing: An Architecture for Deterministic Declarative Execution.*
  <https://doi.org/10.5281/zenodo.21879516>
- **Why the specification is the load-bearing failure, and evolution as governed transformation**:
  Ganti, B. *Protocol-Governed Computing: An Architecture for Closed-Loop Governed Transformation.*
  <https://doi.org/10.5281/zenodo.21879948>
- **What a functioning platform requires in practice**: Ganti, B. *Protocol-Governed Computing:
  Realizing the Normative Platform and Its Governed Transformation.*
  <https://doi.org/10.5281/zenodo.21880155>

The next document states why the problem persists and what a solution would have to be true of. The
normative parts state what such a system must mean and do.
