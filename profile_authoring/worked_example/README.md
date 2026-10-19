# Worked examples

Four sheets, answered for real systems. Read them in this order.

| Example | What it is | Read it for |
|---|---|---|
| `reference_composition/` | A governance surface, one conformance workload, two tool domains. Single node, unsigned, nothing crossing a boundary. | **Start here.** A complete sheet, fully answered, with a note on why each decision went the way it did. |
| `governance_surface/` | The same surface with no workload and no business domain — written to be derived from. | What a profile asks for when it expects others to build on it: as little as a platform can coherently ask. |
| `federated_multinode/` | Many nodes under one authority, with external callers. **In progress.** | What an authoring session looks like mid-flight: what was asked, what was revised, and what is still open. |
| `signed_federated_multinode/` | The same shape carried through: signed, four node roles, a bounded retention window, a read surface reached across the boundary. | A sheet answered **forwards**, for a platform not yet built. The first example with a trust root, and the one where Section A decisions visibly constrain Section B and C. |

Each folder holds the `scope_sheet.md` that was answered. All but `federated_multinode` also hold the
documents the generator produced from it, in `profiles/`: one platform profile, one environment
profile, and one domain profile per declared domain. Only `signed_federated_multinode` has had its
gaps closed, so it is the one to read for what a finished profile's §2–§6 look like.

## Why answer backwards from a built system

Answering the sheet for a platform that already exists is the only way to check that the questions
reach what a real platform actually decided. Doing it found two defects that writing the questions
alone did not:

- an empty answer and an unanswered question looked identical to the validator, so a system that
  declared no environmental facts was reported as having skipped the question;
- the generator treated "kinds this platform allows" and "kinds a snapshot must actually contain" as
  one list. They are different questions, and requiring all of them failed a snapshot that was
  perfectly conforming — the failure read as the system's fault rather than the profile's.

The sheet now asks both questions separately.

## What the fourth example found

Answering forwards, for a platform that does not exist yet, reached three decisions the first three
never had to make — a trust root, a bounded retention window, and a read surface reachable from
outside the host. Each exposed a question the sheet was not asking:

- **where a Section A value is carried** — in the snapshot, or supplied by the environment. Every
  Section A axis can be answered completely while leaving this open, and under a trust root it is the
  difference between a signature that covers a rule and one that does not. Now `A15`.
- **what a partly applied transition leaves behind** — SM-7a binds whether a profile mentions it or
  not, and only Section B made the case visible. An author reaching it from there would settle what a
  result means by where it ran. Now `A16`.
- **whether the profile derives from another** — already noted as missing by `federated_multinode`.
  Now `D1`, and §5 of a platform profile is no longer a gap.

It also found six defects in the generator, four of them one mistake repeated: matching a word
without its polarity or position, so that an answer saying "node-to-node traffic is *not* a crossing"
read as declaring no boundary at all.
