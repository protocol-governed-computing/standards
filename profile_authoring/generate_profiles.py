#!/usr/bin/env python3
"""Scope sheet in, profile skeletons out.

Reads the answers block of a completed scope sheet and emits a Normative Platform Profile, an
execution environment profile, and one domain profile per declared domain.

What it will not do is fill a section it cannot derive. Three parts of a profile require an author's
judgment — additional obligations, how each claim is discharged, and whether the profile derives from
another — and a generator that writes plausible text into them produces a profile that reads complete
and is not. Those are emitted as gaps, marked, and counted at the end of the run.

Everything emitted is parsed back before the run succeeds. A profile whose YAML does not load is not
a target anything can be judged against, and the failure is silent at the point it matters.

    generate_profiles.py <scope_sheet.md> --out <dir>
    generate_profiles.py <scope_sheet.md> --check      # validate answers, emit nothing
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

GAP = "> **GAP — to be written by the author.**"

# The answer schema. Every axis, its shape, and whether an empty collection is an answer.
#
# The sheet supplies no defaults and this refuses to invent any: an answer the author did not give is
# not the author's decision, and a profile assembled from unanswered questions is one two authors who
# agree on nothing could both claim (6a §7).
#
# What counts as answered is deliberately generous — `none`, `not_applicable`, `false` and `[]` are
# all answers. Absence is not, and neither is a blank or whitespace-only string: a value that reads as
# nothing becomes a silent default the moment it is projected.
TEXT, FLAG, LIST, DOMAINS = "text", "flag", "list", "domains"

SCHEMA: dict[str, str] = {
    "platform_name": TEXT, "profile_identity": TEXT,
    # A — meaning
    "kinds": LIST, "aliases_accepted": FLAG, "kinds_required_exercised": LIST, "outcomes": LIST,
    "result_classes": TEXT, "projections": LIST, "namespaces": LIST, "namespaces_closed": FLAG,
    "trust_root": TEXT, "evidence_retention": TEXT, "read_openness": TEXT, "reads_attributed": FLAG,
    "sufficiency_criterion": TEXT, "interaction_forms_governed": TEXT,
    "protocol_bindings_governed": TEXT, "read_surface_reach": TEXT, "genesis_discharge": TEXT,
    # B — environment
    "nodes": TEXT, "availability": TEXT, "co_location_rules": TEXT, "resource_guarantees": TEXT, "deadlines": TEXT,
    "isolation": TEXT, "failure_visibility": TEXT, "distribution": TEXT,
    "declared_environment_facts": LIST, "environment_excludes": TEXT, "environment_claims": LIST,
    # C — composition
    "domains": DOMAINS, "required_domains": LIST, "excluded_domains": LIST,
    "entry_points": LIST, "boundary": TEXT, "claims": LIST,
}

# Which pass each axis belongs to. A sheet is answered over several sessions, and "what is still
# open, by pass" is the question a facilitator actually has between them.
SECTIONS: dict[str, tuple[str, ...]] = {
    "identity": ("platform_name", "profile_identity"),
    "A — what the platform means": (
        "kinds", "aliases_accepted", "kinds_required_exercised", "outcomes", "result_classes",
        "projections", "namespaces", "namespaces_closed", "trust_root", "evidence_retention",
        "read_openness", "reads_attributed", "sufficiency_criterion", "interaction_forms_governed",
        "protocol_bindings_governed", "read_surface_reach", "genesis_discharge"),
    "B — where it runs": (
        "nodes", "availability", "co_location_rules", "resource_guarantees", "deadlines", "isolation",
        "failure_visibility", "distribution", "declared_environment_facts", "environment_excludes",
        "environment_claims"),
    "C — what it is made of": (
        "domains", "required_domains", "excluded_domains", "entry_points", "boundary", "claims"),
}

# Each declared domain answers all of these. 6c §5: the last is not optional.
DOMAIN_FIELDS = ("name", "owns", "governed_by", "reached_by", "ordered_by", "state", "exposed",
                 "authority_claim")

# Answers that read as decisions and are not. 6a §7 and NP-12; CF-5 for the third.
REFUSED = (
    (r"whatever|as declared by the system|system decides|up to the system",
     "defers the decision back to the system it constrains (6a §7, NP-12) — an item is not decided "
     "by requiring the system to decide it"),
    (r"same as the reference|as the reference (implementation|realization)|like the reference",
     "answers by resemblance (CF-5) — resembling a realization establishes nothing"),
    (r"^\s*(minimal|maximal|everything|all of them)\s*$",
     "minimality is relative to a profile and no profile is privileged (6a §8, §11)"),
)


def says_nothing(value) -> bool:
    """Whether an answer means "there is none of this".

    Authors do not write bare tokens. `none`, `none — no boundary is exercised`, and
    `not applicable, single node` are the same answer, and a check that matches only the bare token
    reads the qualified ones as substantive and refuses a correct sheet. Match the leading word.
    """
    if value in (None, False):
        return True
    if isinstance(value, (list, tuple, dict)):
        return not value
    return bool(re.match(r"\s*(none|no\b|n/a|not[ _]applicable|nothing)", str(value), re.I))


class SheetError(Exception):
    pass


def read_answers(path: Path) -> dict:
    blocks = re.findall(r"```yaml\n(.*?)```", path.read_text(encoding="utf-8"), re.S)
    for block in blocks:
        try:
            parsed = yaml.safe_load(block) or {}
        except yaml.YAMLError as exc:
            raise SheetError(f"the answers block does not parse: {exc}") from exc
        if isinstance(parsed, dict) and "scope_sheet" in parsed:
            return parsed["scope_sheet"] or {}
    raise SheetError(f"no `scope_sheet:` answers block found in {path}")


def validate(a: dict) -> tuple[list[str], list[str]]:
    """What is unanswered, and what is answered inadmissibly.

    Kept apart because they are different situations. A sheet mid-session is mostly unanswered and
    that is not a fault; an inadmissible answer is one, however few there are. Reporting them in one
    undifferentiated list buries the second in the first.
    """
    unanswered: list[str] = []
    problems: list[str] = []

    def blank(v) -> bool:
        return v is None or (isinstance(v, str) and not v.strip())

    for key, kind in SCHEMA.items():
        if key not in a or blank(a[key]):
            unanswered.append(key)
            continue
        value = a[key]
        if kind is LIST and not isinstance(value, list):
            problems.append(f"{key}: expected a list of answers, got {type(value).__name__}")
        elif kind is LIST and any(blank(x) for x in value):
            problems.append(f"{key}: contains a blank entry")
        elif kind is FLAG and not isinstance(value, bool):
            problems.append(f"{key}: expected true or false, got {value!r}")
        elif kind is TEXT and not isinstance(value, (str, int, float, bool)):
            problems.append(f"{key}: expected a single answer, got {type(value).__name__}")
        elif kind is DOMAINS:
            if not isinstance(value, list) or not value:
                problems.append("domains: expected a list of domains, each with its own answers")
                continue
            seen: set[str] = set()
            for i, d in enumerate(value):
                if not isinstance(d, dict):
                    problems.append(f"domains[{i}]: expected a mapping of answers, got "
                                    f"{type(d).__name__}")
                    continue
                label = d.get("name") or f"[{i}]"
                for field in DOMAIN_FIELDS:
                    if field not in d or blank(d[field]):
                        unanswered.append(f"domains[{label}].{field}")
                claim = str(d.get("authority_claim") or "").strip().lower()
                if claim and claim not in ("authority", "concern"):
                    problems.append(
                        f"domains[{label}].authority_claim: {d['authority_claim']!r} — must be "
                        "`authority` or `concern` (DP-4, 6c §5). A domain that has not stated it is "
                        "undeclared rather than defaulted")
                if label in seen:
                    problems.append(f"domains[{label}]: declared twice — a domain names one thing")
                seen.add(label)

    if not problems and not unanswered:
        declared = {d["name"] for d in a["domains"]}
        for key in ("required_domains", "excluded_domains"):
            for name in a[key]:
                if key == "required_domains" and name not in declared:
                    problems.append(f"{key}: {name!r} is required and not declared in `domains`")
                if key == "excluded_domains" and name in declared:
                    problems.append(
                        f"excluded_domains: {name!r} is both excluded and declared — a profile "
                        "cannot admit and refuse the same domain")

    for key, value in a.items():
        if not isinstance(value, str):
            continue
        for pattern, why in REFUSED:
            if re.search(pattern, value, re.I):
                problems.append(f"{key}: {why}")

    def answered(*keys: str) -> bool:
        return not any(k in unanswered for k in keys)

    # C4 governs A3, A11, A12, and constrains C5. A boundary nothing crosses cannot discharge a
    # claim about crossing it.
    boundary = str(a.get("boundary") or "").lower()
    exercised = "cross" in boundary and "not" not in boundary and "nothing" not in boundary
    if answered("boundary") and not exercised:
        if answered("result_classes") and not says_nothing(a.get("result_classes")):
            problems.append(
                "result_classes: declared while no boundary is exercised (C4) — result classes "
                "classify what a caller is told, and nothing calls")
        if answered("read_surface_reach") and not a.get("read_surface_reach"):
            problems.append(
                "read_surface_reach: unanswered, and no boundary is exercised (C4) — a platform "
                "nothing crosses still has to be readable (5b §10)")
        for claim in a.get("claims") or ():
            if re.search(r"protocol|wire|transport.*independen", str(claim), re.I):
                problems.append(
                    f"claims: {claim!r} asserts stability across protocols while none is exercised "
                    "— a claim discharged by a substitution that cannot be performed is not "
                    "discharged (CF-8)")

    distribution = str(a.get("distribution") or "")
    distributed = bool(distribution) and not says_nothing(distribution) \
        and not re.search(r"single[ -]node", distribution, re.I)
    if distributed and answered("declared_environment_facts") \
            and a.get("declared_environment_facts") is None:
        # An empty list is an answer — the system declares no environmental fact, so none may change
        # a result. Absent is not: it leaves 6b §2 with nothing to quantify over.
        problems.append(
            "declared_environment_facts: unanswered while distribution is selected (B7/B8) — what "
            "may not vary is anything the system did not declare (6b §2). An empty list is an "
            "answer; absence is not")

    admissible = set(a.get("kinds") or ())
    for kind in a.get("kinds_required_exercised") or ():
        if kind not in admissible:
            problems.append(
                f"kinds_required_exercised: {kind!r} is required to be exercised and is not in the "
                "admissible set (A1) — a snapshot cannot carry a kind the vocabulary refuses")

    return unanswered, problems


def _yaml(block: dict) -> str:
    return yaml.safe_dump(block, sort_keys=False, default_flow_style=False, allow_unicode=True).rstrip()


def _draft_block(gaps: int) -> str:
    """Every emitted document says it is a draft, in a form a reader and a tool both see.

    A skeleton that looks like a profile is the failure mode automation invites here: the shape is
    right, the sections are present, and nothing announces that several of them were never decided.
    """
    return f"""```yaml
completion:
  status: draft
  generated_from: scope sheet
  open_gaps: {gaps}
  usable_as_a_target: false   # a profile with an open gap is not yet something to hand anyone
```
"""


def platform_profile(a: dict) -> str:
    identity = a["profile_identity"]
    domains = a.get("domains") or []
    body = {
        "snapshot_profile": {
            "identity": identity,
            "supersedes": None,
            "derives_from": None,
            "description": a.get("platform_name"),
            # A profile states a floor, never an inventory: a snapshot may carry more than this
            # and still conform (6a §5, CF-5). The domains an author happens to have composed are
            # not thereby required of everyone claiming the profile.
            "required_domains": a.get("required_domains") or [],
            "excluded_domains": a.get("excluded_domains") or [],
            "declared_domains": [d["name"] for d in domains],
            "namespaces": {
                "form": "<namespace>::<ARTIFACT_IDENTITY>",
                "declared": a.get("namespaces") or [],
                "closed": bool(a.get("namespaces_closed", True)),
                "derives_concern": False,
                "derives_authority": False,
            },
            "declared_vocabulary": {
                "kinds": [{"kind": k, "governance_assertion": "required"}
                          for k in (a.get("kinds") or [])],
                "aliases_accepted": bool(a.get("aliases_accepted", False)),
            },
            "declared_outcomes": a.get("outcomes") or [],
            "result_classes": a.get("result_classes") or None,
            "projections": a.get("projections") or [],
            "trust_root": a.get("trust_root"),
            "evidence_retention": a.get("evidence_retention"),
            "read_surface": {
                "openness": a.get("read_openness"),
                "reads_attributed": bool(a.get("reads_attributed", False)),
                "reach": a.get("read_surface_reach"),
            },
            "sufficiency_criterion": a.get("sufficiency_criterion"),
            "interaction_forms_governed": a.get("interaction_forms_governed"),
            "protocol_bindings_governed": a.get("protocol_bindings_governed"),
            "genesis_discharge": a.get("genesis_discharge"),
            "required_governance": {
                # Admissible is not the same question as exercised. declared_vocabulary.kinds is the
                # closed set a snapshot MAY carry; this is the set it MUST. A profile that equates
                # them fails any snapshot that admits a kind it has no artifact for yet.
                "artifact_kinds": a.get("kinds_required_exercised") or [],
                "artifacts": [],   # GAP — see §2
            },
            "required_domain_profiles": [
                {"domain": d["name"], "claims": d.get("authority_claim")} for d in domains],
            "required_self_description": {
                "manifest_declares_profile": True,
                "manifest_declares_identity_coverage": True,
                "covered_set_excludes_the_value": True,
            },
            "required_workloads": {"entry_workflows": a.get("entry_points") or []},
            "required_claims": a.get("claims") or [],
        }
    }
    return f"""# {identity} — draft

{_draft_block(5)}
A snapshot profile is a conformance contract over an assembled snapshot. It states the properties a
snapshot SHALL satisfy — not an inventory of what any particular build contains. A snapshot may
contain more than this profile requires and still conform.

Generated from a scope sheet. Sections marked GAP were not generated and must be written before this
profile is handed to anyone as a target.

## 1. Profile

```yaml
{_yaml(body)}
```

## 2. Required governance artifacts

{GAP} `required_governance.artifacts` above is empty.

A profile references governed identities — namespaces and artifact identities — and never filesystem
paths, repository names, or module paths. The identities cannot be generated from a scope sheet
because they do not exist until the artifacts are authored. Name here the artifacts whose absence
would mean a snapshot is not this platform.

## 3. Additional obligations

{GAP}

For each obligation beyond what §1 selects, state **what would establish a breach**. An obligation
nothing could refuse is not in force, and one that restates a selection in §1 is not additional
(NP-6).

## 4. Claims and their discharge

{GAP} §1 names {len(a.get('claims') or [])} claim(s) and says nothing about what settles them.

For each: what discharges it, which discharge class that is, and a demonstration **capable of
failing** if the system were non-conforming (CD-4). A claim with no stated discharge is decorative.

## 5. Derivation

{GAP}

If this profile derives from another, name the base **by identity** and state that this profile does
not widen it (NP-10). If it derives from none, delete this section — an absent section is clearer
than one saying "none".

## 6. Externality

NP-7 requires a profile to be external to what it governs, and **externality is authorship, not
storage**. A profile written by the authority that builds the system is not external, whatever
directory it is kept in.

State which case applies here. Where the same authority wrote both, a conformance claim under this
profile must record that — a finding against the claim, not against the profile.

## 7. Scope rules

- Profile scope changes are new identities (`_V0` → `_V1`), never in-place edits (NP-9).
- A profile that has not been read against a candidate snapshot MUST NOT be handed to anyone as a
  target. Running the check is a precondition of use.
"""


def environment_profile(a: dict) -> str:
    identity = f"{a['profile_identity']}_ENVIRONMENT"
    body = {
        "environment_profile": {
            "identity": identity,
            "environment": a.get("nodes"),
            "execution_constraints": {
                "availability": a.get("availability"),
                "placement": a.get("co_location_rules"),
                "resource": a.get("resource_guarantees"),
                "timing": a.get("deadlines"),
                "isolation": a.get("isolation"),
                "failure_mode": a.get("failure_visibility"),
            },
            "distribution": a.get("distribution"),
            "declared_environment_facts": a.get("declared_environment_facts") or [],
            "excludes": a.get("environment_excludes"),
            "supported_claims": a.get("environment_claims") or [],
        }
    }
    return f"""# {identity} — draft

{_draft_block(1)}
An execution environment profile. It states where execution happens and under what constraints, and
it changes nothing about what execution means.

## 1. Profile

```yaml
{_yaml(body)}
```

## 2. What this profile may not do

An environment profile MUST NOT introduce a governance kind or semantic category, an authority, a
determination point, environment-derived behavior, or an exemption. An environment that cannot
satisfy an invariant has not earned relief from it.

**Governed consequences do not vary with the environment.** What may not vary is anything the system
did not declare; `declared_environment_facts` above is that list, and a fact absent from it must not
change a result.

## 3. Obligations and their breach

{GAP}

For each constraint in §1, state the obligation it places on a system claiming this profile and what
would establish a breach. A constraint stated as a description obliges nothing.

## 4. What this profile excludes

`excludes` in §1 carries the author's answer: systems whose requirements this environment cannot
meet. Stating this is what lets a reader tell in one pass whether the profile is theirs.
"""


def domain_profile(a: dict, d: dict) -> str:
    name = d["name"]
    identity = f"{a['profile_identity']}_DOMAIN_{name.upper()}"
    claim = d.get("authority_claim")
    body = {
        "domain_profile": {
            "identity": identity,
            "domain": name,
            "authority_claim": claim,
            "subjects": d.get("owns"),
            "governance": d.get("governed_by"),
            "capabilities": d.get("reached_by") or [],
            "workflows": d.get("ordered_by") or [],
            "stores": d.get("state") or [],
            "boundary_exposure": d.get("exposed"),
        }
    }
    if claim == "authority":
        authority_section = f"""## 2. The authority claim

This domain claims to be a distinct governance authority. That claim is established only by
answering all five, **from declared artifacts alone** (CA-3), plus the independence test (CA-4).

{GAP}

| | |
|---|---|
| who the authority is | |
| what constituted it — the declared constituting act | |
| what subjects fall within it | |
| **what decision it may make that no other authority may** | |
| how it relates to the authorities above and beside it | |

A domain acquires no jurisdiction by being named, bounded, deployed separately, or owned by a
different team (CA-2). Until the table is filled, this claim is asserted rather than established.
"""
    else:
        authority_section = """## 2. The authority claim

This domain is a **concern**: governed under the authority above it, with no jurisdiction of its own.
It is organized, named, indexed and governed — an ordinary and correct arrangement, and not a lesser
one.

A concern classification cannot constitute an authority (CA-6). If this domain later needs to make a
decision no other part of the system may make, that is a change of claim, discharged against CA-3.
"""
    return f"""# {identity} — draft

{_draft_block(1 if claim == "authority" else 0)}
## 1. Profile

```yaml
{_yaml(body)}
```

{authority_section}
## 3. What this domain accepts

By being part of a governed system this domain accepts obligations it does not get to decline: its
declarations are admitted, determined and refused like any others, with no private admission path;
its changes are transformations against a baseline rather than edits to what it owns; its effects
pass through declared effecting capabilities; its state is owned and its writes authorized; it is
subject to composition obligations; and it carries no exemption for being new, small, experimental,
or internal.
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("sheet", type=Path)
    ap.add_argument("--out", type=Path, help="directory to write profiles into")
    ap.add_argument("--check", action="store_true", help="validate the answers and emit nothing")
    args = ap.parse_args()

    try:
        answers = read_answers(args.sheet)
    except SheetError as exc:
        print(f"[scope] {exc}", file=sys.stderr)
        return 2

    unanswered, problems = validate(answers)

    if unanswered or problems:
        total = len(SCHEMA)
        answered = total - len([u for u in unanswered if "." not in u])
        print(f"[scope] {args.sheet}", file=sys.stderr)
        print(f"[scope] {answered} of {total} axes answered", file=sys.stderr)

    if unanswered:
        # Grouped by pass and named, not one repeated sentence per field. A sheet is answered over
        # several sessions and this is the between-sessions question: what is still open, and where.
        print("\n[scope] not yet answered — nothing is defaulted, so each needs an answer from the",
              file=sys.stderr)
        print("        author. `none`, `not_applicable`, `false` and `[]` all count; silence does not.",
              file=sys.stderr)
        per_domain = [u for u in unanswered if "." in u]
        for section, keys in SECTIONS.items():
            open_here = [k for k in keys if k in unanswered]
            if open_here:
                print(f"\n  {section} ({len(open_here)} of {len(keys)})", file=sys.stderr)
                for k in open_here:
                    print(f"      {k}", file=sys.stderr)
        if per_domain:
            print(f"\n  per-domain answers ({len(per_domain)})", file=sys.stderr)
            for k in per_domain:
                print(f"      {k}", file=sys.stderr)

    if problems:
        print(f"\n[scope] {len(problems)} answered inadmissibly — these are faults, not gaps:",
              file=sys.stderr)
        for p_ in problems:
            print(f"  - {p_}", file=sys.stderr)

    if unanswered or problems:
        return 1

    if args.check:
        print(f"[scope] {args.sheet}: answers complete and admissible")
        return 0
    if not args.out:
        print("[scope] --out is required unless --check", file=sys.stderr)
        return 2

    args.out.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    identity = answers["profile_identity"]
    for path, text in [
        (args.out / f"{identity}.md", platform_profile(answers)),
        (args.out / f"{identity}_ENVIRONMENT.md", environment_profile(answers)),
    ] + [
        (args.out / f"{identity}_DOMAIN_{d['name'].upper()}.md", domain_profile(answers, d))
        for d in (answers.get("domains") or [])
    ]:
        path.write_text(text, encoding="utf-8")
        written.append(path)

    # Everything emitted is read back. A profile whose YAML does not load resolves to nothing when a
    # checking party asks for it by identity, and the failure surfaces as "profile not found".
    for path in written:
        for block in re.findall(r"```yaml\n(.*?)```", path.read_text(encoding="utf-8"), re.S):
            try:
                yaml.safe_load(block)
            except yaml.YAMLError as exc:
                print(f"[scope] emitted YAML does not parse in {path}: {exc}", file=sys.stderr)
                return 3

    gaps = sum(p.read_text(encoding="utf-8").count(GAP) for p in written)
    for path in written:
        print(f"[scope] wrote {path}")
    print(f"[scope] {len(written)} profile(s), YAML verified, {gaps} gap(s) left for the author")
    print("[scope] a profile with an open gap is not yet a target — see §3–§6 of the platform profile")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
