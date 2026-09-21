# Worked examples

Three sheets, answered for real systems. Read them in this order.

| Example | What it is | Read it for |
|---|---|---|
| `reference_composition/` | A governance surface, one conformance workload, two tool domains. Single node, unsigned, nothing crossing a boundary. | **Start here.** A complete sheet, fully answered, with a note on why each decision went the way it did. |
| `governance_surface/` | The same surface with no workload and no business domain — written to be derived from. | What a profile asks for when it expects others to build on it: as little as a platform can coherently ask. |
| `federated_multinode/` | Many nodes under one authority, with external callers. **In progress.** | What an authoring session looks like mid-flight: what was asked, what was revised, and what is still open. |

Each folder holds the `scope_sheet.md` that was answered. The first two also hold the documents the
generator produced from it, in `profiles/`: one platform profile, one environment profile, and one
domain profile per declared domain.

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
