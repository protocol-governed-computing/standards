# Vocabulary Triage

A reading of the 36 terms the first scan reported as declared-but-never-defined. Each was
checked against the text of its declaring document. The scan's model of a definition site was
wrong for two thirds of them; what survives is listed below with the remedy each needs.

## What the first scan got wrong

The family sites definitions in five forms, not the two the scan first knew:

| Form | Example |
|---|---|
| lead | `**Candidate.** A proposed part of a governed system...` |
| copula | `A **binding** associates a contract with a realization.` |
| section | `## 4. Faithfulness` — "Faithfulness is soundness, not completeness." |
| table | `\| **Authorization** \| this may exist or occur at all \|` |
| emphasis | the term bolded at first substantive use |

Twenty-four of the thirty-six were sited in the *section* form: a numbered section named for
the term, defining it in its opening prose. That is a deliberate editorial convention and needs
no change to any document. The scan now reads it.

Two further conventions caused false reports and are also read now: a definition may share a
line with the declaration sentence that introduces it (`5b` §1, `caller`), and a mark may carry
its article inside the bold (`**a claimant**`, `**one semantic owner**`).

## Genuine gaps

Twelve terms are declared as introduced by a document that then never defines them. They divide
by what it would take to close them.

### Declared and effectively unused — closed

Six terms were named in a declaration sentence and then barely or never used. The remedy differed by
term, and the difference matters: two of them should not have been declared at all.

**Struck from the declaration — 2.** Defining these would have created the overlap CM-3 forbids.

| Term | Document | Why |
|---|---|---|
| execution agent | 3c | `1a` §10 already defines **Runtime** as "the agent that performs execution" — a second name for one concept |
| admissibility determination | 4a | a transparent compound of **Admissibility** (`1a` §7) and **determination** (`1b` §4), both defined |

`3c` continues to use "agent" and "execution agency" as ordinary English for the runtime, which is
what `1a` Runtime already covers. Nothing else changed in either document.

**Defined — 4.** These name concepts their documents genuinely rest on.

| Term | Document | Sited at | Written from |
|---|---|---|---|
| platform-owned governance | 6c | §3, after the ownership table | §3 table, §1 |
| domain-owned governance | 6c | §3, alongside its counterpart | §3 table, §1 |
| governed executable target | 5a | §4, the third relationship | §4 table, §5 |
| extension point | 6a | §3, where a profile's room to add is stated | §3 block quote, §2 |

`extension point` was the one to watch: `6a` §3 permits a profile to add requirements "within an
explicitly permitted extension point", so the term carries the whole weight of what a profile may
add. The definition says an extension point exists only where a standard declares one — stated
descriptively, since asserting it as a MUST would add an obligation `6a` does not carry.

### Used freely, never defined — closed

Five terms carried real weight in the prose while no document said what they were. Each now has a
definition where it is declared, written from what that document already asserts. None adds an
obligation, so no invariant changed in any of the five.

| Term | Document | Sited at | Written from |
|---|---|---|---|
| step | 3a | §3, beside `traversal` | `1a` §10 Workflow; `3d` §2; AI-11 |
| jurisdiction | 2e | §3, beside `authority` | §3.2 item 3; CA-6 |
| evaluator | 7a | §4, opposite `claimant` | §2 claimant row; §4 discharge |
| external protocol | 5a | §10, beside `protocol adapter` | §2 protocol mechanics |
| governed result | 5a | §9, before `result class` | §1 term table; §2 outcome projection |

Two of these needed care beyond locating a sentence. `jurisdiction` cannot be defined as the
subjects an authority *reaches*: `2e` §2 separates **scope** from **authority** precisely because
"reaching a subject is read as being entitled to", so the definition says *entitled to govern* and
names scope, containment, and concern as the separate questions they are. `evaluator` is defined
against `claimant` without saying whether the two may be the same party — `7a` states no
independence requirement, and a definition should not introduce one.

### Name drift — 1

| Term | Document | Note |
|---|---|---|
| kind registry | 2d | declared as `kind registry`; §3 marks `**registry**` |

Two further cases of the same drift appear as warnings rather than gaps, because a definition
was found under the other name: `3b` declares `self-description` and marks `**self-describing**`;
`3e` declares `determinative content` under a section titled for both it and its counterpart.

## Ownership conflicts — closed

Four terms were defined twice or claimed by the wrong document. None was a gap, and none could be
closed by adding a definition: each required deciding which document owns the term.

| Term | Owner | Refines | Was |
|---|---|---|---|
| Snapshot | 1a §7 | 3b §2 | `3b` declared it introduced a term `1a` defines |
| Provenance | 1a §9 | 2b §6 | `2b` declared it introduced a term `1a` defines |
| Resolution | 1a §7 | 4c §6 | `4c` declared it introduced a term `1a` defines |
| Candidate | 1a §10 | 4a §2 | `4a` restated what `1a` already states |

Only the last was a real duplication. In the other three the later document had never restated what
the concept *is* — it added what its own subject requires, which is refinement. What each got wrong
was the declaration sentence, which said it *introduced* the term.

**Ownership followed semantic primacy, not document order.** `1a` owns a term required to understand
several parts of the family, whose identity does not depend on one later standard's mechanism; a
subject standard owns a term that exists principally because of its own subject matter. The rule
matters because the alternative — *`1a` owns it because `1a` is first* — turns the Conceptual Model
into a vocabulary warehouse.

`candidate` was the case that tested it, and wording could not settle it: near-verbatim duplication
is evidence of an accident, not of ownership. Usage breadth settled it instead. `candidate` appears
in ten documents, and `1b` §4 defines **proposal** as "a candidate change presented to a governed
state" — a Part I document using the term to define one of its own. Had construction owned it, `1b`
would rest on a Part IV term, which is the defect this same pass repaired for `step`.

That rule is applied here and stated nowhere in the family. Whether it belongs in `1a` §12 is
recorded as outstanding against `v0`.
