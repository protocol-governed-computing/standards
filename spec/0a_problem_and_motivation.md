# Problem and Motivation

*This document explains the problem that Protocol-Governed Computing exists to solve. Read it first
if you want the case before the specification. It is non-normative: only the normative documents
state requirements and confer authority. §8 lists the works that develop the argument in full.*

## 1. Maintenance dominates, and that is a symptom

Organizations spend most of their software budget keeping systems running, not building them.
Across two decades of measurement, maintenance has taken 60–80% of the money. The industry treats
that ratio as normal.

The ratio is a warning. Suppose a system costs more to keep alive than it cost to create. The cause
then lies in how the system was built, not in how well people maintain it. So the useful question is not "how do
we maintain better?" It is **"why does maintenance dominate?"**

The cause is structural. People, process and tools do not explain it.

## 2. The expensive problem is not computation

Software solves two different kinds of problem. Anyone who treats them as one misses where the cost
lies.

| | Bounded by | Cost concentrated in |
|---|---|---|
| **computational software** — an algorithm, a transform, a kernel | its specification | getting it right once |
| **business software** — rules, workflows, authorization, exceptions, obligations, integrations | its accumulated history | keeping its meaning intact over decades |

Business software holds an organization's real capital. That capital includes business knowledge,
policies, the meaning of data, controls, compliance obligations, operating assumptions and migration
history. Most of it exists in no form a machine can check.

**New code does not replace the software.** A rewrite reproduces the computation and loses
the accumulated rules. That is why rewrites of mature business systems fail in a familiar way. The
team discovers undocumented behavior in production, one exception at a time.

## 3. What accumulates is governance debt

Real rules constrain every mature system, and the system depends on them. Those rules live in code
paths, review habits, wiki pages and the memories of long-serving engineers. None of those places
lets anything check the rules.

We call this accumulation **structural governance debt**. It is the cost of embedding governance
decisions in code instead of in explicit, checkable declarations. It is not technical debt, and it
behaves differently.

- **Code-level measures cannot see it.** Test coverage, complexity metrics and static analysis all
  miss it.
- **It grows faster than the system.** Each new component adds implicit relationships with the
  others, so the debt compounds.
- **Refactoring cannot repay it.** You can rewrite every function to be clean and idiomatic, and the
  debt stays the same. The constraints that should tie behavior to intent still exist nowhere as
  artifacts.

The debt shows itself as **fear of change**. That fear is rational, not timid. The system's
dependencies are implicit, so nobody can calculate the risk of a change.

Organizations then build machinery to compensate: architecture review boards, change advisory
boards and cross-team coordination. **People are doing the governing that the architecture should
do.**

## 4. Existing remedies govern one layer and stop

Each advance in the industry governs something real. None reaches the layer where the software's
meaning lives.

| Remedy | Governs | Cannot govern |
|---|---|---|
| CI/CD | build and deploy | behavioral semantics; inter-component contracts |
| microservices | boundaries and interface schemas | behavior *behind* interfaces; cross-service invariants |
| infrastructure-as-code | topology and provisioning | application logic; business rules |
| feature flags | activation state | the semantic consequences of activation |

Microservices show the pattern most clearly. When a team splits a monolith, the governance gap does
not shrink.
**It moves the gap** from inside the monolith to the spaces between services, where it is harder to
see and harder to test. Teams ship faster, but they do not ship more correctly.

Some high-assurance fields, such as aviation and telecom, do achieve structural governance. They
achieve it *from outside the system*, through formal specification, certification and sustained
human discipline. Most software cannot afford that cost. These fields prove that structural
governance works. The open question is whether the system itself can carry that governance, instead
of an institution built around it.

## 5. AI removes the last brake

The governance gap existed before AI. What AI changes is the speed at which it grows.

```
code generation velocity        accelerating
governance establishment        bounded by human deliberation
```

We call the widening gap between these two rates the **generation–governance impedance mismatch**.
The speed of human coding used to limit how fast governance debt could accumulate. AI is removing
that limit.

This is not an argument against machine-generated software. It is an observation. **When code
becomes cheap to produce, knowing what the produced system means becomes the scarce resource.** A
way of building software that cannot state meaning in a checkable form gets worse as generation gets
faster.

## 6. Where it fits, and where it does not

Protocol-Governed Computing targets software whose behavior is more than computation and outlives
its authors. Such systems are large, long-lived and full of rules, and they run where mistakes carry
regulatory or operational consequences. Examples include financial, industrial, clinical,
governmental, supply-chain and enterprise-workflow systems, and any system with long-term
traceability obligations.

**It does not target** numerical algorithms, scientific computing, signal and image processing,
utility libraries, small computational functions or performance-critical inner loops. Those are
bounded problems with a different cost structure. Governance around them adds overhead and returns
nothing.

This limit matters. Readers would rightly judge a model presented as *how all software should be
written* as overreach.

## 7. What success would look like

A mature realization of this idea would let an organization:

1. state business intent in a form a machine can consume;
2. declare its governing constraints explicitly, not leave them to convention;
3. build a system from those declarations, not from someone's interpretation of them;
4. show that what it built is what it declared;
5. run the system with no behavior coming from anywhere undeclared;
6. ask the system what it contains and what it decided;
7. change the system through a governed act, not an edit;
8. show someone who was not there that the system kept conforming; and
9. replace the implementation without losing the accumulated meaning.

The last item is the purpose of the other eight. **The goal is to make the software lifecycle itself
governable.** Safer execution at one moment is not enough. The system's meaning must stay intact, and
provably so, from its first construction to its retirement.

This document does not claim that any system achieves this goal. The normative documents, and the
systems built against them, answer that question. This document claims only that the problem is
real, expensive and structural.

## 8. Where this is developed

This document summarizes. The following works make the full argument:

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

The next document explains why the problem persists and what any solution must satisfy. The
normative documents then state what such a system must mean and do.
