# Migration and Adoption

*This document answers the question an organization asks once it understands the standard and sees
its merit: how do we get there from where we are? Read it after Part 0 and the normative parts you
need. It belongs to the annex and is non-normative. Its recommendations are advice, and they oblige
no one.*

## 1. What we mean by migration

Every organization that considers PGC already runs software. In that software, the rules that
matter live in code, in conventions and in the heads of experienced people. PGC asks for something
different: the rules live in declarations that a machine checks before anything runs.

| | Where the organization starts | Where migration leads |
|---|---|---|
| **Where the rules live** | in code paths, configuration, wiki pages and memory | in explicit, versioned declarations |
| **How anyone checks them** | by reading code and asking people | a machine checks them before the system runs |
| **How the system changes** | someone edits the code | a governed act transforms one sealed state into the next |
| **What a run leaves behind** | whatever logs someone remembered to write | evidence of what was admitted, decided and refused |

**Migration, in this document, means moving authority from the left column to the right.** The
authority to decide what the system does moves out of code and memory and into declarations. Code
still runs. It just stops being the place where the rules are decided.

The rest of this document explains how to make that move without stopping the business.

### The running example

A lender runs a loan-approval service. It is ten years old and works well. Its rules include:

- a minimum credit score, set in code;
- an exception for long-standing customers, added after a complaint years ago and documented
  nowhere;
- a manager override, which three managers describe in three different ways.

A web portal, a branch system and a partner's broker platform all call the service. One senior
engineer knows why the exception exists. The sections below return to this lender at each step.

## 2. Why migration cannot be a rewrite

Nobody starts from nothing. An organization that considers this model already has systems and data.
It has interfaces with outside consumers and operating procedures. It has people who know things that
nobody has written down.

**The migration path must work with what exists, not against it.** A model that demands a rewrite
before it delivers anything asks for the most expensive first step possible. It also asks the
organization to take that step on faith.

So the goal is not to translate a large body of business code into a different form. The goal is to
**recover and state the governed meaning of what exists**. A machine can then check that meaning.
When a new implementation arrives, the organization can then show that it preserves the meaning.

This change of goal is the whole migration story. A rewrite reproduces the computation and loses the
accumulated rules. An organization that recovers the meaning first keeps the accumulated rules. It
leaves the implementation choice open.

*The lender.* A rewrite of the loan service would reproduce the credit-score check in a week. It
would lose the exception for long-standing customers, because nobody wrote it down. The first
customer the new service wrongly refused would reveal the loss. Recovering the meaning works the
other way round. With the senior engineer's help, the lender states the exception as a declared rule
before any code changes.

## 3. How a governed system lives beside an old one

A governed system meets ungoverned systems in two places, called seams, and it declares both. That is
why an organization can adopt it step by step.

### 3.1 Wrapping inward

An existing service becomes an **effecting capability** behind a declared contract. Its
implementation, data, interface and deployment stay the same. What changes is that nothing calls it
directly any more.

| Changes | Does not change |
|---|---|
| invocation is governed — reached through a declared contract | the service's implementation |
| invocation is evidenced — what was invoked, with what, to what outcome | its data store |
| outcomes are classified — declared results, not ad-hoc exceptions | its interface |
| authority is declared rather than assumed | its deployment |

**A wrapper is not a refactoring. It lays governance over the service.** The wrapped system does not
know that anything governs it, and it keeps working exactly as before. The organization gains
control of how the service is invoked. It can state each invocation, refuse it, and keep evidence of
it.

*The lender.* The ten-year-old loan service keeps its code and its database. A declared contract now
stands in front of it. Every request reaches the service through that contract. Every outcome is
recorded as approved, declined or refused, with its reason.

### 3.2 Boundary outward

Ungoverned callers reach a governed system through a declared interaction boundary. Each caller keeps
the protocol it already uses. An adapter normalizes the call. The governed system never learns how
the call arrived.

This is coexistence in the other direction. **An organization can adopt a governed system without
changing the system's consumers.** Nothing outside needs to change before work begins.

*The lender.* The web portal, the branch system and the broker platform keep calling exactly as they
did. Nobody modifies them. Only the path behind the boundary changes.

## 4. The path, one step at a time

### 4.1 Three phases, with no point of no return

| Phase | Scope | What it establishes |
|---|---|---|
| **one capability** | weeks | that the model works here, and one person who can author governance |
| **one domain** | months | a governed region with evidence sufficient for compliance questions |
| **composition** | ongoing | the properties that only appear over a whole — closure, equivalence, reproducibility |

**Each phase pays off on its own.** An organization that stops after the first phase has proof and a
trained author. One that stops after the second has a governed domain and its evidence. Neither
needs the third phase to have gained something.

The organization never has to abandon its existing architecture. Each phase adds governance beside
what is already there.

*The lender.* The first capability is one decision, with one trained author. The domain is all of
lending. Composition comes later, if ever, when the lender must show that lending and its other
governed domains hold together.

### 4.2 Recovering meaning pays before anything is built

Adoption starts by stating what a system does, in a form something can check. **That work has value
even if nothing else follows.**

While doing it, most organizations find questions they cannot answer, though they assumed they
could. Which rules actually apply here? Who is entitled to this? What happens in this exception?
What was authoritative last year? The exercise does not create these questions. It **reveals that
nobody could answer them already**.

**You cannot govern what you cannot state.** The attempt to state it produces an artifact the
organization did not previously have.

*The lender.* To state the manager override, the lender must choose among the three managers'
versions. It now has one agreed rule where it had three habits. That rule has value even if the
lender never governs anything else.

## 5. Choosing the first step

- **Start where refusal is cheap.** People learn the discipline when the system refuses something.
  Learn it where a refusal costs a corrected declaration, not an incident.
- **Start where the meaning is contested.** The best first subject is often one that three people
  describe three different ways. The governance work settles the disagreement, and the settlement is
  the deliverable.
- **Do not start with the most critical system.** The model can carry it. But a first adoption is
  also a first misunderstanding.
- **Prefer a subject that will still exist in five years.** The returns come from change over time.
  A subject due for replacement will be gone before it yields them.

*The lender.* Final approval is the most critical decision, so the lender does not start there. It
starts with pre-qualification, the quick estimate a customer sees before applying. A wrong refusal
there costs a corrected declaration, not a lost loan. Pre-qualification also uses the contested
override, and the lender will still offer it in five years.

## 6. Deciding whether to migrate at all

> **If a system must stay correct as it changes over time, this model pays for itself. If the system
> is temporary, informal or owned by one person, the overhead is not justified.**

Problem and Motivation §6 lists the domains this model targets and the ones it does not. The rule
above is the short form. The overhead is real, and it comes first. A lifetime of change repays it. A
system without that lifetime never reaches repayment.

People misread two cases, in opposite directions:

- **Exploratory work is a fair exclusion, not a loss of nerve.** A prototype exists to discover a
  domain, not to govern one, and declaring first slows discovery. Govern the prototype when it stops
  being one. Make that decision explicitly, because most prototypes become production by default,
  not by decision.
- **"We'll add governance later" is exactly the case this model exists to refuse.** By "later", the
  rules have accumulated and their meaning is already implicit. The cost of stating meaning grows
  with the amount of it. Each postponement makes adoption more expensive.

*The lender.* Lending rules must stay correct for years, and regulators ask what was decided and
why. So lending qualifies. A spreadsheet that marketing built for one campaign does not.

## 7. What goes wrong, and what it costs

### 7.1 What makes adoption fail

- **Adopting the mechanism without the discipline.** Teams write declarations to satisfy a tool and
  keep the real decisions in code. The result is overhead with no governance.
- **Softening refusal.** The first inconvenient refusal shows whether an organization meant it. A
  fallback added to keep a demo working starts an ungoverned path.
- **Treating adoption as a platform project.** The deliverable is governed subjects, not a governed
  platform. A platform that governs no subject is infrastructure waiting for a purpose.
- **Beginning at composition scale.** The properties that appear only across a whole system are also
  the hardest to establish. A team that starts there must learn everything at once.

### 7.2 What it makes harder, on purpose

Honesty about the cost matters more than enthusiasm about the benefit.

- **Systems refuse where they used to degrade.** A conventional system limps on. A governed system
  stops and says why. That is the intended behavior, but it will look like a regression the first
  time.
- **There is no fallback, so teams fix causes.** This is slower at the moment of failure and faster
  over a year.
- **Declaration comes before execution.** The first delivery is slower. The tenth change is faster.
- **Nothing repairs your omissions for you.** A construction step that filled in what you left out
  would be deciding what you meant.
- **Every change is a transformation.** There are no quick fixes, not even the ones that would truly
  have been fine.

**An organization that wants these costs softened wants a different model**, and another model would
serve it better. These properties all follow from the same choices. Nobody can take some and leave
the rest.

*The lender.* One day pre-qualification meets a case that no declaration covers. The old service
would have guessed and carried on. The governed one stops and names the missing declaration. That
will feel like a step backwards. A month later, the lender can show a regulator every
pre-qualification decision and the rule behind it.

## 8. Where this is developed

- **Adoption patterns, phase detail, and the decision tree**: *Protocol-Governed Systems*,
  Chapter 18, "Adopting Protocol Governance Incrementally."
- **Why the returns are in change over time**: *Protocol-Governed Systems*, Chapter 15, "Structural
  Economics of Governance."
- **What a functioning platform requires in practice**: Ganti, B. *Protocol-Governed Computing:
  Realizing the Normative Platform and Its Governed Transformation.*
  <https://doi.org/10.5281/zenodo.21880155>
- **Operational doctrine for the reference realization**: Ganti, B. *Protocol-Governed Computing:
  Field Manual.* <https://doi.org/10.5281/zenodo.21898082>

The normative parts state what a governed system must mean and do. This document constrains none of
them. They require no particular path for getting there.
