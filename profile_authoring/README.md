# Profile authoring

This is the beginner-friendly path for turning a real system into a profile that speaks the standard's
language.

The job is simple in principle:

1. answer the business questions in plain language,
2. check that every deferred decision is actually decided,
3. generate the profile documents,
4. fix the remaining gaps before anyone treats the profile as a target.

**Nothing in this directory has authority.** It is not a standard document, it declares no part, it
discharges no membership condition, and it takes no part in revision or supersession. If anything here
appears to disagree with a `spec/` document, the specification wins. Where this material is absent from
the standard, this material is wrong.

---

## 1. Why this exists

A system built to this standard must decide a lot of things for itself: which kinds of governed thing
it has, what a checking party accepts as a trust root, how long evidence is kept, whether a domain is
an authority or a concern. The standard defers those decisions on purpose. Deciding them would turn it
into one platform's specification instead of a family's.

That is correct, but it leaves a new author with no front door:

- the standard tells you what decisions exist,
- it does not tell you how to make them in business terms,
- and a profile is only *the record of decisions already made*.

You cannot start building either. Building without those decisions means making them by accident, in
code, one at a time — discovered later by whoever has to check the result.

This folder supplies the missing step: make the decisions deliberately, in business language, then turn
them into profile documents mechanically.

---

## 2. What is in this folder

| File | What it is for |
|---|---|
| `scope_sheet.md` | The business questions, each with a default. This is the main working document. |
| `scope_axis_register.md` | The same decisions with citations, valid options, and target fields. Not for the author: it is what the sheet is written from, and where you check that a question is not an invention. |
| `profile_template.md` | The structure a profile should follow, based on the standard's own requirements. |
| `generate_profiles.py` | Reads a completed scope sheet and writes the profile documents. |
| `check_every_axis_decided.py` | Reads a finished profile back against the register and checks whether every deferred decision was actually answered. |
| `worked_example/` | Three sheets answered for real systems, with the profiles they produced. **Start here if you are new.** |

---

## 3. The first rule: a blank answer is not an answer

A scope sheet is not a form that fills itself in. It is the record of a conversation between two
parties:

- **the author answers.** Somebody who knows the business — what the system is for, who it answers to,
  what must never happen, what "done" means. Every answer is theirs.
- **the other party questions.** Somebody who knows the family — whose job is to say what each question
  is really asking, notice which ones have not been answered, and catch the reasonable-sounding answer
  that fails later.

**The second role decides nothing.** It cannot. A decision made by whoever holds the standard, rather
than by whoever owns the system, is the exact failure the standard names: a profile that has not decided
its own questions is one that two systems agreeing on nothing could both claim.

The first role cannot work unaided either. An author will not know that "we'll sign things eventually"
is not a trust root, or that calling a domain an authority means pointing at a decision no other part of
the business may make.

So nothing is defaulted. Examples of answers the sheet refuses:

- "whatever the system decides"
- "same as the reference implementation"
- an empty question, left for the tool to settle

Where the sheet says *if you have no view yet*, that is a suggestion to consider and then write down in
your own words. `none`, `not applicable`, `false`, and an empty list are all valid explicit answers.
Silence is not.

---

## 4. There are three passes, in order

The sheet is ordered because later questions assume earlier ones. The work is easier done in order.

### Pass one — what the platform means (Section A)

The meaning layer. It answers questions like:

- what kinds of governed thing exist,
- what a step is allowed to conclude,
- what a checking party trusts,
- how long evidence is kept,
- who may read what.

This is the slow pass. Expect a session of its own, and expect it to surface business disagreements
that were never written down.

Two items have no default and must be answered directly:

- when a design is too thin to build from,
- what makes the first build trustworthy.

Everything else has a default that is a real answer — but the default still has to be chosen.

### Pass two — where it runs (Section B)

This pass is about the environment, not meaning:

- how many machines are involved,
- what may sit next to what,
- what deadlines apply,
- what failure looks like.

**Nothing in this pass may change anything pass one decided.** The environment determines whether the
system runs, when, how fast, and where — never what its results mean. If an answer here seems to need a
new kind of governed thing, a new authority, or an exception to a rule, that answer belongs in pass one
and you have reached it from the wrong direction.

This is where the common mixture gets separated:

- "single-node moving to Kubernetes" is pass two.
- "unsigned moving to signed" is pass one, because it changes who vouches for evidence.
- "encrypted snapshot" is pass two, unless a governed result actually depends on the encryption, in
  which case it is pass one.
- "federated" is both, and must be answered in both places.

### Pass three — what it is made of (Section C)

The domains, and for each one the question that cannot be skipped:

**Is this an authority or a concern?**

A domain is an authority only if you can point to a declared act that created it and answer, from your
own declarations alone:

- who it is,
- what created it,
- what falls under it,
- what decision it may make that no other part of the system may make,
- and how it stands relative to what is above and beside it.

If you cannot answer all five, it is a concern — governed under the authority above it. That is the
ordinary case. A domain is not an authority just because it has its own name, repository, deployment,
or team.

> **Where this falls short of the design lifecycle.** The lifecycle elsewhere in this project gates each
> phase: a phase is evaluated and must be admissible before the next is attempted. This toolkit checks
> all the answers at the end, in one pass. The sheet is ordered and says later questions assume earlier
> ones, but nothing yet stops an author answering Section C before Section A. Per-section gating is a
> small change to the generator, and it has not been made.

---

## 5. What counts as a finished profile

There are two separate checks, and they answer different questions.

### 5.1 `open_gaps`

`generate_profiles.py` counts `open_gaps` by looking for sections the generator refused to fill in.

Three parts of a profile need the author's judgment:

- additional obligations,
- how each claim is discharged,
- whether the profile derives from another profile.

A generator can produce plausible text for those, and the result would read complete while being
nothing of the kind. So it marks them and counts them instead. When the author writes them in,
`open_gaps` becomes zero.

That says nothing about whether the decisions the family defers were made. A profile can carry
`open_gaps: 0` and still leave the trust root undecided, because the trust root is not a generated
section. It is a question on the sheet.

### 5.2 "every axis decided"

`check_every_axis_decided.py` compares the finished profile against the register and reports, per axis,
whether the field is:

- decided,
- absent,
- empty,
- or evasive.

`evasive` is the one worth having. `6a` §7 calls handing the question back the more dangerous failure,
precisely because it reads as a decision: "whatever the system declares" satisfies the form of §6 while
inverting its substance.

Run it like this:

```bash
python3 check_every_axis_decided.py path/to/PROFILE.md
```

It exits with:

- `0` when every axis is decided,
- `1` when any axis is not.

Run it before handing a profile to anyone. The profile's own precondition is that it be read against a
candidate snapshot; this is the cheaper check that comes first, and it catches the easy failures early.

Two limits matter:

- the register states an explicit target field for only three axes; the rest are matched by name, so a
  renamed field reports as absent rather than being followed,
- and the check establishes that a decision was made, never that it was sound.

---

## 6. How to generate the profiles

Run from this directory (`standards/profile_authoring`), or give full paths from anywhere:

```bash
python generate_profiles.py <your_scope_sheet.md> --check          # validate only; write nothing
python generate_profiles.py <your_scope_sheet.md> --out <dir>      # write the profile documents
```

You get one platform profile, one environment profile, and one domain profile per declared domain.

**Every one is titled a draft** and carries a machine-readable `completion` block saying so, because a
skeleton with the right headings is the thing most easily mistaken for a finished profile. The generator
also reads back every document it writes, so a profile that does not parse is a failed run rather than a
file you find unreadable months later. That failure mode is not hypothetical: a hand-written profile in
this project is unreadable for exactly this reason, and it reports as "profile not found" — pointing at
the claim rather than at the syntax error.

The generator refuses two kinds of answer, because they read as decisions and are not:

- *"Whatever the system decides."* This hands the question back to the party the profile is supposed to
  constrain. Two systems agreeing on nothing would both satisfy you.
- *"The same as the reference implementation."* Resembling a working system establishes nothing about
  yours.

---

## 7. What the generator will not do

The generated profiles come out with gaps, marked and counted. That is the point, not a shortcoming.

| Gap | Why a tool cannot write it |
|---|---|
| Which artifacts are required | They are identities in your system, and they do not exist until you author them. |
| Additional obligations | Each must say what would count as breaking it. An obligation nothing could ever refuse is not in force. |
| How each claim is settled | A demonstration has to be capable of failing. One that cannot fail supports a claim nobody can evaluate. |
| Whether the profile derives from another | This is a judgment about intent. |

A profile with an open gap is not yet something to hand anyone as a target.

There is one thing no automation can supply: **independence**. A profile is supposed to be written by
someone other than the system claiming it. A generator you ran, producing the profile for the system you
are building, is not external — whatever directory it ends up in. This material shortens the work; it
does not remove the requirement.

If you write both sides, say so. A recorded gap is worth more than a claim that will not survive being
checked.

---

## 8. Start with the worked examples

`worked_example/` holds three sheets answered for systems that already exist. Its own README says
which to read first; in short:

| Example | What it shows |
|---|---|
| `reference_composition/` | A complete sheet, fully answered — a governance surface, one workload, two tool domains, nothing crossing a boundary. **Read this one first.** |
| `governance_surface/` | The same surface with no workload, written to be derived from. |
| `federated_multinode/` | An authoring session in progress: many nodes, external callers, questions still open. |

The first two carry the generated profiles beside them, in each example's `profiles/` folder.

Read the notes, not just the answers. Each one records **why a decision went the way it did**, which
is the part worth reading.

These examples are also how the toolkit is tested, and they have earned their place. Running the
first one found two defects that writing the questions alone did not:

- an empty answer and an unanswered question looked identical to the validator, so a system that
  declared no environmental facts was reported as having skipped the question;
- the generator treated "kinds this platform allows" and "kinds a snapshot must actually contain" as
  the same list. Those are different questions. Requiring all of them failed a snapshot that was
  perfectly conforming, because it allows a kind it has no artifact for yet — and the failure read as
  the system's fault rather than the profile's.

The second is the more instructive one. It is a mistake an author would make, it produces a profile
that looks right, and it fails a conforming system. The sheet now asks both questions separately.

---

## 9. The practical workflow

Building a profile for the first time, do this in order:

1. Read the worked example (`worked_example/reference_composition/`).
2. Fill in the scope sheet in order, from pass one to pass three.
3. Check that every answer is explicit and not merely implied.
4. Run the generator in check mode.
5. Fix any invalid or evasive answer.
6. Generate the profiles into an output directory.
7. Review the gaps and decide whether they are really closed.
8. Run the axis check before handing the profile to anyone.

This is not a form-filling exercise. It is a decision-making process with a record, and the record is
what becomes the profile.

---

## 10. One writing rule to keep in mind

When a decision could reasonably have gone another way, write down why your system chose this route.

That one sentence turns a profile from something merely followed into something that can be reviewed.
