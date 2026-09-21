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
| `worked_example/` | Four sheets answered for real systems, with the profiles they produced. **Start here if you are new.** |

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

### Pass three — what it is made of (Section C), and what it derives from (Section D)

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

`generate_profiles.py` counts `open_gaps` by looking for sections the generator refused to fill in,
and derives the number from the markers it emitted rather than asserting it beside them.

Four parts of a profile need the author's judgment:

- which artifacts are required,
- additional obligations,
- how each claim is discharged,
- whether the same authority wrote the profile and the system it governs.

A generator can produce plausible text for those, and the result would read complete while being
nothing of the kind. So it marks them and counts them instead. When the author writes them in,
`open_gaps` becomes zero.

Derivation used to be a fifth. It is now an ordinary answer on the sheet (`D1`): what a generator
cannot supply is the base's *content*, and it does not need to, because NP-10's obligation not to
widen a base is the same sentence whatever the base says.

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

- the register states an explicit target field for only some axes; the rest are matched by name, so a
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

A profile with an open gap is not yet something to hand anyone as a target.

There is one thing no automation can supply: **independence**. A profile is supposed to be written by
someone other than the system claiming it. A generator you ran, producing the profile for the system you
are building, is not external — whatever directory it ends up in. This material shortens the work; it
does not remove the requirement.

If you write both sides, say so. A recorded gap is worth more than a claim that will not survive being
checked.

---

## 8. Start with the worked examples

`worked_example/` holds four sheets. Its own README says
which to read first; in short:

| Example | What it shows |
|---|---|
| `reference_composition/` | A complete sheet, fully answered — a governance surface, one workload, two tool domains, nothing crossing a boundary. **Read this one first.** |
| `governance_surface/` | The same surface with no workload, written to be derived from. |
| `federated_multinode/` | An authoring session in progress: many nodes, external callers, questions still open. |
| `signed_federated_multinode/` | The same shape carried through and finished, answered forwards for a platform not yet built. The only example whose gaps are closed. |

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
9. Optionally, build a platform that claims it and read the result back — the cookbook in §10.

This is not a form-filling exercise. It is a decision-making process with a record, and the record is
what becomes the profile.

---

## 10. Cookbook: build a platform that claims your profile

You have a finished profile. This builds a platform that claims it, in a sandbox, in eight steps.

The rest of this folder is portable — the questions come from the standard, and any system can answer
them. This section is not. The commands are the PGC reference toolchain's, and they can drift with
it. Another realization would do all of this differently.

**Read this first, and note what it does and does not say.** The assembler *does* read your profile.
It resolves the `snapshot_profile` block by identity — not by filename, because a profile is named by
what it declares itself to be — and refuses to seal a snapshot that claims a profile whose required
artifacts and required kinds it does not carry. A claim nobody can read is not a claim (3b SN-7), and
a snapshot asserting a conformance it does not have is worse.

What it checks is a floor, and a narrow one: the identities and kinds §1 requires. It does not read
your trust root, your retention window, your obligations, or your claim discharges — and no compiler,
runtime or inspector reads any of it. **Everything the profile says beyond that floor is checked by
reading, by hand.** Finding out how much that is, and what it costs, is the whole point of the
exercise.

Below, `MY_PLATFORM_V0` is your profile's identity. Substitute your own.

### Step 1 — Make a sandbox

```bash
mkdir -p ~/pgc_sandbox && cd ~/pgc_sandbox
python3.12 -m venv .venv && source .venv/bin/activate
pip install protocol-governed-computing
pgc
```

`pgc` lists what is installed and what is missing. It will say no platform root is set. Step 2 fixes
that.

### Step 2 — Clone the declarations

The install gives you the tools and the implementation modules. It does not give you the
declarations. The wheels leave `registry/` out on purpose, so that nobody ends up with a second
governance surface hiding inside a package. You clone the repositories that carry it.

```bash
git clone https://github.com/protocol-governed-computing/software_governance.git
git clone https://github.com/protocol-governed-computing/conformance_workloads.git
```

**Note what you just did.** Your platform's governance surface is now that surface, with its
constitutions and its invariants. That is a derivation. Name the profile you derive from, by
identity, in §6 of your profile. If you want a platform that owes nothing to this one, author your
own surface instead.

### Step 3 — Point the tools at it

```bash
export PGC_PLATFORM_ROOT=~/pgc_sandbox/software_governance
export PGC_SNAPSHOT_ROOT=$PGC_PLATFORM_ROOT/snapshot
pgc
```

`pgc` should now resolve the platform root. If it says `no registry/ here`, you pointed at the wrong
directory.

### Step 4 — Compile the governance surface

```bash
protocol_compiler compile --structure STRUCTURE_BUILD_PLATFORM_CONFIG_V1
```

Name the structure. There is no default, because a governance surface is whatever a build config
says it is.

### Step 5 — Assemble your first snapshot

```bash
snapshot_assembler assemble \
  --source ~/pgc_sandbox/software_governance/snapshot/compiled \
  --out    ~/pgc_sandbox/snapshot_surface \
  --profile MY_PLATFORM_V0
```

`--profile` is where your profile enters. There is no default here either. A profile comes from
outside the system being built, so the assembler will not supply one for you.

Three things to know about what you just built:

- **This is a surface with no workload and no business domain.** It is not a snapshot with no
  domains. The surface *is* domains. Strip those and there are no constitutions and no invariants, so
  nothing governs whatever you add next.
- **It has no predecessor, so it is your genesis.** Genesis is a claim, though, not a file the
  assembler writes. Your A14 answer is what settles it.
- **A genesis claim has to show the profile was not written by what it governs.** If you wrote both,
  that demonstration fails. Record it as failing.

### Step 6 — Compile a workload

There is no separate command for this. It is the same `compile`, with the anchors moved to the domain
and the platform left where it is.

```bash
DOMAIN=~/pgc_sandbox/conformance_workloads/workloads/collatz

PGC_DOMAIN_ROOTS=$DOMAIN \
PGC_SNAPSHOT_ROOT=$DOMAIN/snapshot \
protocol_compiler compile --structure <the domain's own STRUCTURE_BUILD_*_CONFIG code>
```

Find the structure code in the domain's `registry/structures/` folder. Step 4 has to have run first:
the domain resolves its references against the compiled surface.

### Step 7 — Assemble a second snapshot

```bash
snapshot_assembler assemble \
  --source ~/pgc_sandbox/software_governance/snapshot/compiled \
  --source $DOMAIN/snapshot/compiled \
  --out    ~/pgc_sandbox/snapshot_with_workload \
  --profile MY_PLATFORM_V0
```

You are not adding the workload to the first snapshot. A snapshot is sealed. The assembler builds a
whole new one from the sources you name, so this is a separate snapshot with its own identity. Keep
both.

Do both conform to your profile? That depends on your answers, not on the tool. If your required
domains name the workload, the first one does not conform and the second does. If they name only the
surface, both conform — a profile sets a floor, and a snapshot may carry more than the floor.

### Step 8 — Read it back

```bash
snapshot_assembler verify --out ~/pgc_sandbox/snapshot_with_workload
python3 check_every_axis_decided.py ~/pgc_sandbox/profiles/MY_PLATFORM_V0.md
```

The first checks the snapshot against its own manifest. The second checks your profile against the
register.

Neither one checks the snapshot against your profile. You do that yourself, by reading. That reading
is what tells you whether the profile you wrote says anything a checking party could act on — which
is the answer this whole exercise exists to get.

---

## 11. One writing rule to keep in mind

When a decision could reasonably have gone another way, write down why your system chose this route.

That one sentence turns a profile from something merely followed into something that can be reviewed.
