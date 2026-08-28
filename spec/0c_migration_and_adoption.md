# Migration and Adoption

*Non-normative. Problem and Motivation states the problem; Diagnosis and Principles states why it
persists. This document addresses the question an organization asks next: how do I get there from
where I am. It requires nothing and recommends without obliging.*

## 1. The question

Nobody starts from nothing. An organization considering this model already has systems, data,
interfaces with external consumers, operational procedures, and people whose knowledge is not
written down anywhere.

**The migration path has to work with what exists, not against it.** A model that requires a rewrite
before it delivers anything has asked for the most expensive possible first step, and has asked for
it on faith.

## 2. It is not a rewrite

The objective is not to translate a large body of business code into a different form.

It is to **recover and state the governed meaning of what exists**, so that meaning becomes
something a machine can check — and so that a new implementation, when there is one, can be
established as preserving it.

This reframing is the whole of the migration story. A rewrite reproduces computation and loses
accumulation; recovering meaning captures the accumulation first, and leaves the question of
implementation open.

## 3. Two seams

Adoption is incremental because there are two places a governed system meets an ungoverned one, and
both are declared.

### 3.1 Wrapping inward

An existing service becomes an **effecting capability** behind a declared contract. Its
implementation, data, interface, and deployment are unchanged; what changes is that it is no longer
called directly.

| Changes | Does not change |
|---|---|
| invocation is governed — reached through a declared contract | the service's implementation |
| invocation is evidenced — what was invoked, with what, to what outcome | its data store |
| outcomes are classified — declared results, not ad-hoc exceptions | its interface |
| authority is declared rather than assumed | its deployment |

**Wrapping is not refactoring. It is governance overlay.** The wrapped system does not know it is
governed, and continues to function exactly as before. What the organization gains is that its
invocation is now something that can be stated, refused, and evidenced.

### 3.2 Boundary outward

A governed system is reached by ungoverned callers through a declared interaction boundary. The
caller speaks whatever protocol it already speaks; an adapter normalizes; the governed system never
learns how the call arrived.

This is the other direction of coexistence, and it means **a governed system can be adopted without
its consumers being adopted.** Nothing outside has to change to begin.

## 4. Incremental, with no point of no return

| Phase | Scope | What it establishes |
|---|---|---|
| **one capability** | weeks | that the model works here, and one person who can author governance |
| **one domain** | months | a governed region with evidence sufficient for compliance questions |
| **composition** | ongoing | the properties that only appear over a whole — closure, equivalence, reproducibility |

**Each phase is independently valuable.** An organization that stops after the first has proof and a
trained author; one that stops after the second has a governed domain and the evidence that comes
with it. Neither needs the third to have gained something.

There is no moment at which the existing architecture must be abandoned. Each phase adds governance
alongside what is already there.

## 5. Recovering meaning pays before anything is built

The first work of adoption is stating what a system does in a form something can check — and **that
work has value even if nothing further happens.**

Most organizations discover, in doing it, that they cannot answer questions they assumed were
answerable: what rules actually apply here, who is entitled to this, what happens in this exception,
what was authoritative last year. Those are not questions the exercise creates. They are questions
the exercise **reveals were already unanswerable**.

**You cannot govern what you cannot state.** The artifact produced by trying is the artifact the
organization never had.

## 6. Where to start

- **Start where refusal is cheap.** The discipline is learned by having something refused. Learn it
  where the cost of a refusal is a corrected declaration, not an incident.
- **Start where the meaning is contested.** The highest-value first subject is usually the one three
  people describe differently — the governance work resolves the disagreement, and the resolution is
  the deliverable.
- **Do not start with the most critical system.** Not because the model cannot carry it, but because
  a first adoption is also a first misunderstanding.
- **Prefer a subject that will still exist in five years.** The returns are in change over time; a
  subject due for replacement will not be around to yield them.

## 7. When it pays, and when it does not

> **If a system must remain correct under change over time, this model pays for itself. If it is
> temporary, informal, or individually owned, the overhead is not justified.**

Problem and Motivation §6 states the domains this is aimed at and the ones it is not. The decision
rule above is the compressed form: the overhead is real, it is front-loaded, and it is repaid over a
lifetime of change. A system without that lifetime does not reach repayment.

Two cases deserve naming because they are misread in opposite directions:

- **Exploratory work is a legitimate exclusion, not a failure of nerve.** A prototype exists to
  discover a domain, not to govern one, and declaration-first discipline slows discovery. Govern it
  when it stops being a prototype — which is a decision worth making explicitly, because most
  prototypes become production by default rather than by decision.
- **"We'll add governance later" is the case the model exists to refuse.** Later is when the
  accumulation has happened and the meaning is already implicit. The cost of stating meaning rises
  with the amount of it, and adoption postponed is adoption made more expensive.

## 8. What makes adoption fail

- **Adopting the mechanism without the discipline.** Declarations authored to satisfy a tool, with
  the real decisions still in code, produce overhead and no governance.
- **Softening refusal.** The first inconvenient refusal is where an organization decides whether it
  meant this. A fallback added to keep a demo working is the beginning of an ungoverned path.
- **Treating adoption as a platform project.** The deliverable is governed subjects, not a governed
  platform. A platform with no governed subject is infrastructure awaiting a purpose.
- **Beginning at composition scale.** The properties that only appear over a whole are also the
  hardest to establish, and beginning there means learning everything at once.

## 9. What it makes harder, on purpose

Honesty about the cost matters more than enthusiasm about the benefit.

- **Systems refuse where they used to degrade.** A conventional system limps; a governed one stops
  and says why. That is the intended behavior, and it will look like a regression the first time.
- **There is no fallback, so causes get fixed.** This is slower at the moment of failure and faster
  over a year.
- **Declaration precedes execution.** First delivery is slower. What is faster is the tenth change.
- **Nothing repairs on your behalf.** A construction that could complete what you omitted would be
  deciding what you meant.
- **Every change is a transformation.** There are no quick fixes, including the ones that would
  genuinely have been fine.

**An organization that wants these softened wants a different model**, and would be better served by
one. The properties are consequences of the same choices; they cannot be had selectively.

## 10. Where this is developed

- **Adoption patterns, phase detail, and the decision tree**: *Protocol-Governed Systems*,
  Chapter 18, "Adopting Protocol Governance Incrementally."
- **Why the returns are in change over time**: *Protocol-Governed Systems*, Chapter 15, "Structural
  Economics of Governance."
- **What a functioning platform requires in practice**: Ganti, B. *Protocol-Governed Computing:
  Realizing the Normative Platform and Its Governed Transformation.*
  <https://doi.org/10.5281/zenodo.21880155>
- **Operational doctrine for the reference realization**: Ganti, B. *Protocol-Governed Computing:
  Field Manual.* <https://doi.org/10.5281/zenodo.21898082>

The normative parts state what a governed system must mean and do. Nothing in this document
constrains them, and nothing in them requires any particular path to arriving.
