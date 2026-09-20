# Profile authoring

A way for someone building their own PGC system to say what platform they are building, and get back
the profile documents that say it in the standard's terms.

**None of this carries authority.** Nothing here is a document of the standard. It declares no part,
discharges no membership condition, and does not participate in revision or supersession. Where
anything here and a document in `spec/` appear to differ, the document governs — and where something
here is simply absent from the documents, it is this material that is wrong.

---

## 1. The problem this solves

Someone decides to build a system on this standard. They read it, and it tells them — correctly and
repeatedly — that a great many decisions are theirs to make. Which kinds of governed thing their
system has. What a checking party accepts as a trust root. How long evidence is kept. Whether a
domain is an authority or a concern.

The standard does this on purpose. It defers those decisions rather than deciding them, because
deciding them would make it one platform's specification instead of a family's.

But the effect on a new author is that there is no front door. They cannot start writing a profile,
because a profile is *the record of decisions already made*, and they have not made them yet. They
cannot start building either, because building without those decisions means making them by
accident, in code, one at a time, discovered later by whoever has to check the result.

**What was missing is the step before the profile: a way to make the decisions deliberately, in
business language, and then turn them into the profile mechanically.** That is what this folder is.

---

## 2. What is in here

| File | What it is |
|---|---|
| `scope_sheet.md` | The questions. Thirty of them, in business language, each with a default. This is what an author actually works through. |
| `scope_axis_register.md` | The same decisions with their citations, option sets, and target fields. Not for the author — it is the source the sheet is written from, and the place to check that a question is not an invention. |
| `profile_template.md` | The structure a platform profile takes, derived from the standard's own requirements. |
| `generate_profiles.py` | Reads a completed sheet, writes the profile documents. |
| `check_every_axis_decided.py` | Reads a finished profile back against the register: is every deferred decision actually decided? |
| `worked_example/` | The whole path run once, on a system that already exists. **Read this first.** |


### Checking a profile you have finished

`open_gaps` and *every axis decided* are different questions, and it is worth being clear which one
a number is answering.

`generate_profiles.py` writes `open_gaps` by counting the sections it refused to fill. Three parts of
a profile need an author's judgment — the additional obligations, how each claim is discharged, and
whether the profile derives from another — and a generator that writes plausible text into them
produces a profile that reads complete and is not. So it emits them marked, and counts them. When the
author has written them, `open_gaps` is zero.

That says nothing about whether the decisions the family defers were made. A profile can carry
`open_gaps: 0` and leave the trust root undecided, because the trust root was never a section the
generator left blank — it was a question on the sheet.

`check_every_axis_decided.py` reads the finished profile back against the register and reports, per
axis, whether the field is decided, absent, empty, or evasive. *Evasive* is the one worth having:
`6a` §7 calls handing the question back the more dangerous failure, because it reads as a decision.
"whatever the system declares" satisfies the form of §6 while inverting its substance.

```bash
python3 check_every_axis_decided.py path/to/PROFILE.md
```

Exit 0 when every axis is decided, 1 when any is not. Run it before handing a profile to anyone — the
profile's own precondition is that it be read against a candidate snapshot first, and this is the
cheaper check that comes before that one.

Two limits. The register states an explicit target field for only three axes; the rest are matched by
name, so a renamed field reports as absent rather than being followed. And the check establishes that
a decision was made, never that it was sound.

---

## 3. Authoring is a conversation, not a form

This is the part most easily missed, so it is stated plainly.

**The scope sheet is not a questionnaire to be filled in alone, and it is not a form the tooling
completes for you.** It is the *record* of a session in which the answers come from one side and the
questioning from the other:

- **the author answers.** Somebody who knows the business — what the system is for, who it answers
  to, what must never happen, what "done" means. Every answer in the sheet is theirs. None is
  supplied by anyone else, and none is assumed.
- **the other party extracts.** Somebody who knows the family — whose job is to draw the scope out
  fully: to say what each question is really asking, to notice which questions have not actually been
  answered, and to catch the reasonable-sounding answer that fails later.

The second role decides nothing. It cannot: a decision made by whoever holds the standard, rather
than by whoever owns the system, is the failure the standard names explicitly — a profile that has
not decided its own questions is one two systems agreeing on nothing could both claim.

But the first role cannot work unaided either. An author will not know that "we'll sign things
eventually" is not a trust root, or that calling a domain an authority requires pointing at a
decision no other part of the business may make. Left alone they answer the easy questions, skip the
hard ones, and discover in six months which ones they skipped.

**So: nothing is defaulted.** A question left blank is refused, not filled in. Where the sheet says
*if you have no view yet*, that is a suggestion to consider and then write down — the words still
have to be the author's. `none`, `not applicable`, `false` and an empty list are all answers; silence
is not.

The sheet exists so the conversation leaves a record, and so the record becomes a profile without
anyone rewriting it by hand.

This mirrors how the design lifecycle works elsewhere in this project — a problem stated in business
language is driven through ordered phases, each one checked before the next is attempted, until what
comes out is complete enough to build from. Profile authoring has the same shape and the same
reason: **the decisions are ordered, and later ones assume earlier ones.**

> **Where it currently falls short of that model.** The design lifecycle gates each phase — a phase
> is evaluated and must be admissible before the next is attempted. This toolkit checks all the
> answers at the end, in one pass. The sheet is ordered and says that later questions assume earlier
> ones, but nothing yet stops an author answering Section C before Section A. Adding per-section
> gating is a small change to the generator rather than a redesign, and it has not been made.

---

## 4. The three passes

### Pass one — what the platform means

Section A of the sheet, fourteen questions plus one. These are the decisions the standard explicitly
hands to a profile, and they are about **meaning**: what kinds of thing exist, what a step can
conclude, what a checking party trusts, how long evidence lives, who may read what.

Two of them have no default and must be answered: *when is a design too thin to build from*, and
*what makes your first build trustworthy*. Everything else has a default that is a real answer.

This pass is the slow one. Expect it to take a session on its own, and expect it to surface
disagreements inside the business that had never been made explicit.

### Pass two — where it runs

Section B, eight questions. How many machines, what may sit next to what, what deadlines apply, what
a failure looks like.

**Nothing in this pass may change anything pass one decided.** The environment determines whether
the system runs, when, how fast, and where — never what its results mean. If an answer here seems to
need a new kind of governed thing, or a new authority, or an exception to a rule, the answer belongs
in pass one and has been reached from the wrong direction.

This is where the common mixture gets separated. "Single-node moving to Kubernetes" is pass two.
"Unsigned moving to signed" is pass one — it is about who vouches for evidence, not about where the
code runs. "Encrypted snapshot" is pass two, unless some governed result actually depends on the
encryption, in which case it is pass one. "Federated" is both, and has to be answered twice.

### Pass three — what it is made of

Section C. The domains, and for each one the question that cannot be skipped: **is this an authority,
or a concern?**

A domain is an authority only if you can point at a declared act that created it and answer, from
your declarations alone: who it is, what created it, what falls under it, **what decision it may make
that no other part of the system may**, and how it stands relative to what is above and beside it.

If you cannot answer all five, it is a concern — governed under the authority above it. That is the
ordinary case. What is not available is calling something an authority because it has its own name,
its own repository, its own deployment, or its own team.

---

## 5. What comes out

Run the generator:

Run it from this directory (`standards/profile_authoring`), or give full paths from anywhere:

```
python generate_profiles.py <your_scope_sheet.md> --check          # validate, write nothing
python generate_profiles.py <your_scope_sheet.md> --out <dir>      # write the profiles
```

You get one platform profile, one environment profile, and one domain profile per domain you
declared. **Every one is titled a draft** and carries a machine-readable `completion` block saying so,
because a skeleton with the right shape and the right section headings is the thing most easily
mistaken for a finished profile. The generator reads back every document it writes, so a profile that does not parse is a
failed run rather than a file you discover is unreadable months later. That failure mode is not
hypothetical: a hand-written profile in this project is unreadable for exactly this reason, and it
reports as "profile not found" — pointing at the claim rather than at the syntax error.

**It also refuses two kinds of answer**, because they read as decisions and are not:

- *"Whatever the system decides."* This hands the question back to the party the profile is supposed
  to constrain. Two systems agreeing on nothing would both satisfy you.
- *"The same as the reference implementation."* Resembling a working system establishes nothing about
  yours.

---

## 6. What it deliberately will not do

The generated profiles come out with **gaps**, marked as gaps and counted at the end of the run. The
generator will not fill them, and this is the point rather than a shortcoming.

| Gap | Why no tool can write it |
|---|---|
| **Which artifacts are required** | They are identities in your system, and they do not exist until you author them. |
| **Additional obligations** | Each must say what would count as breaking it. An obligation nothing could ever refuse is not in force. |
| **How each claim is settled** | A demonstration has to be capable of failing. Naming one that cannot fail supports a claim nobody can evaluate. |
| **Whether the profile derives from another** | A judgment about intent. |

A profile with an open gap is not yet something to hand anyone as a target.

**And one thing no automation can supply.** A profile is supposed to be written by someone other than
the system claiming it. A generator you ran, producing the profile for the system you are building,
is not external — whatever directory it ends up in. What this material shortens is the work, not the
independence. If you write both, say so; a recorded gap is worth more than a claim that will not
survive being checked.

---

## 7. Start here

`worked_example/` answers the sheet backwards from a system that already exists — a governance
surface, one workload, two tool domains, nothing crossing a boundary. It carries a section on **why
each decision went the way it did**, which is the part worth reading. The generated profiles sit
beside it in `worked_example/profiles/`.

That example is also how the toolkit is tested, and it has already earned its place. Running it
found two defects that writing the questions alone did not:

- an empty answer and an unanswered question looked identical to the validator, so a system that
  declared no environmental facts was reported as having skipped the question;
- the generator treated "kinds this platform allows" and "kinds a snapshot must actually contain" as
  the same list. They are different questions. Requiring all of them failed a snapshot that was
  perfectly conforming, because it allows a kind it has no artifact for yet — and the failure read
  as the system's fault rather than the profile's.

The second is the more instructive: it is a mistake an author would make, it produces a profile that
looks right, and it fails a conforming system. The sheet now asks both questions separately.
