#!/usr/bin/env python3
"""Check a profile against the scope axis register: is every deferred decision actually decided?

This answers a question `open_gaps` does not. The generator writes `open_gaps` by counting the
sections it refused to fill — additional obligations, claim discharge, derivation — so `open_gaps: 0`
means the author finished what the generator left blank. It says nothing about whether the decisions
`6a` §7 defers to a profile were made at all. A profile can carry `open_gaps: 0` and leave the trust
root undecided.

What this reads is the register: one axis per decision the family defers, and the profile field the
answer lands in. For each, it applies the standard's own test (`6a` §7) — an item is decided only if
two systems that disagree on it could not both claim the profile. So an answer that hands the
question back is reported as a failure, not a pass:

    DECIDED   an answer of the profile's own, including an explicit null
    ABSENT    the field is not there
    EMPTY     present and carrying nothing
    EVASIVE   "whatever the system declares", "same as the reference implementation", TBD

The last is the one worth having. `6a` §7 calls it the more dangerous failure because it reads as a
decision: it satisfies the form while handing the constraint back to the party the profile is
supposed to constrain.

Usage:
    python3 check_every_axis_decided.py <profile.md>

Exit 0 if every axis is decided, 1 if any is not, 2 if the file carries no profile block.

Two limits, stated so the result is read correctly. The register names an explicit NPP field for
only three axes; for the rest the field is matched by name here, so a profile that renames a field
will report ABSENT rather than following it. And this checks that a decision was *made*, never that
it was *right* — an author can decide badly and score full marks.
"""
import re, sys, yaml
from pathlib import Path

# axis -> NPP field path, from the register's "Lands in" lines
AXES = {
    "A1":  ("Admissible kinds",                      "declared_vocabulary.kinds"),
    "A1b": ("Kinds required to be exercised",        "required_governance.artifact_kinds"),
    "A2":  ("Outcomes",                              "declared_outcomes"),
    "A3":  ("Result classes at the boundary",        "result_classes"),
    "A4":  ("Projections carried",                   "projections"),
    "A5":  ("Namespaces and arrangement",            "namespaces"),
    "A6":  ("Trust root",                            "trust_root"),
    "A7":  ("Evidence retention",                    "evidence_retention"),
    "A8":  ("Read surface openness",                 "read_surface.openness"),
    "A9":  ("Read attribution",                      "read_surface.reads_attributed"),
    "A10": ("Sufficiency criterion",                 "sufficiency_criterion"),
    "A11": ("Interaction forms as artifacts",        "interaction_forms_governed"),
    "A12": ("Protocol bindings as artifacts",        "protocol_bindings_governed"),
    "A13": ("Reaching the read surface",             "read_surface.reach"),
    "A14": ("Genesis discharge",                     "genesis_discharge"),
}

EVASIONS = [
    r"whatever the system", r"whatever its contracts", r"whatever .* declares",
    r"same as the reference", r"as the reference implementation", r"to be (written|decided|determined)",
    r"\bTBD\b", r"\bTODO\b",
]

def get(d, path):
    cur = d
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None, False
        cur = cur[part]
    return cur, True

def verdict(value, present):
    if not present:                       return "ABSENT",   "field not in profile"
    if value is None:                     return "DECIDED",  "explicit null — a decision"
    if isinstance(value, bool):           return "DECIDED",  repr(value)
    s = str(value).strip()
    if s == "" or s == "[]" or s == "{}": return "EMPTY",    "present but carries nothing"
    for pat in EVASIONS:
        if re.search(pat, s, re.I):       return "EVASIVE",  "hands the question back (6a §7)"
    if isinstance(value, (list, dict)) and len(value) == 0:
        return "EMPTY", "present but carries nothing"
    return "DECIDED", (s.replace("\n", " ")[:58] + ("…" if len(s) > 58 else ""))

def main(path):
    t = Path(path).read_text()
    blocks = re.findall(r"```yaml\n(.*?)```", t, re.S)
    completion, prof = {}, None
    for b in blocks:
        try:
            d = yaml.safe_load(b)
        except Exception:
            continue
        if not isinstance(d, dict):
            continue
        if "completion" in d:
            completion = d["completion"]
        if "snapshot_profile" in d:
            prof = d["snapshot_profile"]
    if prof is None:
        print("no snapshot_profile block found"); return 2
    if not completion:
        print("  (no completion block — this profile predates the completeness discipline)")

    print(f"profile      : {prof.get('identity')}")
    print(f"declared     : status={completion.get('status')}  open_gaps={completion.get('open_gaps')}  "
          f"usable={completion.get('usable_as_a_target')}\n")

    counts = {}
    for aid, (title, field) in AXES.items():
        val, present = get(prof, field)
        v, why = verdict(val, present)
        counts[v] = counts.get(v, 0) + 1
        mark = {"DECIDED": "  ok  ", "ABSENT": " MISS ", "EMPTY": " EMPTY", "EVASIVE": "EVADE!"}[v]
        print(f"  {mark} {aid:4s} {title:34s} {field:38s} {why}")

    print(f"\n  decided {counts.get('DECIDED',0)}/{len(AXES)}"
          f"   absent {counts.get('ABSENT',0)}"
          f"   empty {counts.get('EMPTY',0)}"
          f"   evasive {counts.get('EVASIVE',0)}")
    undecided = len(AXES) - counts.get("DECIDED", 0)
    print(f"  declared open_gaps: {completion.get('open_gaps')}   undecided axes: {undecided}")
    if undecided and completion.get("open_gaps") == 0:
        print("\n  NOTE: open_gaps is 0 while axes remain undecided. The two count different things:")
        print("        open_gaps = prose sections the generator left for the author;")
        print("        this check = axes the family defers to a profile (6a §7).")
    return 1 if undecided else 0

EXAMPLE = ("    python3 check_every_axis_decided.py "
           "../../.github/snapshot_profiles/GOVERNANCE_SURFACE_PROFILE_V0.md")


def _help() -> int:
    """Asked for. Goes to stdout, exits clean."""
    print(__doc__.strip())
    print("\nFor example:\n" + EXAMPLE)
    return 0


def _no_profile() -> int:
    """Not asked for. Goes to stderr, exits 2."""
    print("name the profile to check:\n" + EXAMPLE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        sys.exit(_help())
    if len(sys.argv) != 2:
        sys.exit(_no_profile())
    target = Path(sys.argv[1])
    if not target.is_file():
        print(f"no such profile: {target}", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(target))
