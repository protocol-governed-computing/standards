"""Derive the PGC terminology index and vocabulary violations report from spec/.

Writes into projections/, governed by projections/terminology_projection_contract.md.

The index is derived, never authored. Two channels in the documents are read:

  declaration   "This document introduces the terms **x**, **y**, and **z**."
  definition    the site where the document says what the term is

The family sites a definition in four forms, all of which mark the term in bold:

  lead      a paragraph opening with "**Term.**"          (1a, throughout)
  copula    "A **constituent** is anything the snapshot..."
  table     "| **Authorization** | this may exist or occur at all | ..."
  section   a numbered section named for the term, defining it in its opening sentence
  emphasis  the term bolded at its first substantive use

A term is a PGC term because a document declares or defines it (1a Sec 2, Sec 12).
This tool asserts nothing the documents do not already say; where the two channels
disagree, that disagreement is reported as a defect against CM-2/CM-3.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
SECTION = re.compile(r"^##\s+(\d+[a-z]?)\.\s+(.*)$")
BOLD = re.compile(r"\*\*(.+?)\*\*", re.S)
INTRO = re.compile(
    r"introduces?\s+(?:the\s+)?terms?\b(.*?)(?:,?\s+and\s+refines\b|\.\s|\.$|$)", re.S | re.I
)
REFINES = re.compile(r"refines?\b(.*?)(?:\.\s|\.$|$)", re.S | re.I)
LEAD_DEFN = re.compile(r"^\*\*([^*]{2,80}?)\.\*\*")
DISTINGUISH = re.compile(r"\*Distinguish from ([^.*]+)\.\*")
ABBREV = re.compile(r"\s*\(([A-Z][A-Za-z0-9-]{1,12})\)\s*$")

# A bolded lead-in is a definition only if it names a thing. These reject the
# far more common use of paragraph-leading bold: an emphasised full sentence.
SENTENCE_MARKERS = re.compile(
    r"\b(is|are|was|were|be|been|has|have|had|does|do|must|may|shall|should|"
    r"can|cannot|will|would|not|never|always|no|nothing|every|each|MUST|MAY|SHOULD)\b"
)
LEADING_ARTICLE = re.compile(r"^(a|an|the)\s+", re.I)
MAX_TERM_WORDS = 6

LEAD, COPULA, SECTION_DEFN, TABLE, EMPHASIS = "lead", "copula", "section", "table", "emphasis"

# Forms that say what a term is. A table row or a bolded mention marks a term
# without defining it, and cannot carry a second definition of one.
DEFINING_FORMS = (LEAD, COPULA, SECTION_DEFN)


def normalize(term: str) -> str:
    return re.sub(r"\s+", " ", term.strip().lower())


def variants(term: str) -> list[str]:
    """Surface forms of a term: the term, and the term with its last word pluralized."""
    forms = {term}
    head, _, last = term.rpartition(" ")
    prefix = f"{head} " if head else ""
    if last.endswith("y") and len(last) > 2 and last[-2] not in "aeiou":
        forms.add(f"{prefix}{last[:-1]}ies")
    elif last.endswith(("s", "x", "z", "ch", "sh")):
        forms.add(f"{prefix}{last}es")
    else:
        forms.add(f"{prefix}{last}s")
    return sorted(forms, key=len, reverse=True)


@dataclass
class Site:
    doc: str
    line: int
    section: str
    form: str


@dataclass
class Term:
    name: str
    abbrev: str | None = None
    declared_in: list[str] = field(default_factory=list)
    refined_in: list[str] = field(default_factory=list)
    sites: list[Site] = field(default_factory=list)
    distinctions: list[str] = field(default_factory=list)
    occurrences: dict[str, list[int]] = field(default_factory=lambda: defaultdict(list))

    @property
    def definition(self) -> Site | None:
        """The authoritative site: a defining form outranks a mere marking."""
        for form in DEFINING_FORMS:
            for site in self.sites:
                if site.form == form:
                    return site
        return self.sites[0] if self.sites else None

    @property
    def home(self) -> str | None:
        site = self.definition
        if site:
            return site.doc
        return self.declared_in[0] if self.declared_in else None


@dataclass
class Doc:
    stem: str
    title: str
    path: Path
    lines: list[str]
    prose: list[bool]
    masked: list[str] = field(default_factory=list)  # lines, declaration sentences blanked


def load(spec_dir: Path) -> list[Doc]:
    docs = []
    for path in sorted(spec_dir.glob("*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        prose, in_fence = [], False
        for line in lines:
            if FENCE.match(line):
                in_fence = not in_fence
                prose.append(False)
                continue
            prose.append(not in_fence)
        title = next(
            (m.group(2).strip() for m in (HEADING.match(l) for l in lines[:5]) if m),
            path.stem,
        )
        docs.append(Doc(path.stem.split("_")[0], title, path, lines, prose, list(lines)))
    return docs


def sections_by_line(doc: Doc) -> dict[int, str]:
    """Map every line number to the numbered section heading it falls under."""
    mapping, current = {}, ""
    for i, line in enumerate(doc.lines, start=1):
        m = SECTION.match(line)
        if m:
            current = f"Sec {m.group(1)}"
        mapping[i] = current
    return mapping


def paragraphs(doc: Doc):
    """Yield (start_line_number, text) for each prose paragraph."""
    buf, start = [], 0
    for i, (line, is_prose) in enumerate(zip(doc.lines, doc.prose), start=1):
        if not is_prose:
            continue
        if line.strip():
            if not buf:
                start = i
            buf.append(line)
        elif buf:
            yield start, "\n".join(buf)
            buf = []
    if buf:
        yield start, "\n".join(buf)


def classify(line: str, term: str) -> str:
    """Which definition form does this line use for the term?"""
    stripped = line.strip()
    # Match the same marks the site search accepts: plural forms, article inside the bold.
    bolded = r"\s*(?:an?|the|one|exactly one)?\s*(?:%s)\s*" % "|".join(
        re.escape(v) for v in variants(term.lower())
    )
    if re.match(r"^\*\*%s\.?\*\*" % bolded, stripped, re.I):
        return LEAD
    if stripped.startswith("|"):
        return TABLE
    if re.search(r"\*\*%s\*\*\s+(?:is|are|means)\b" % bolded, stripped, re.I):
        return COPULA
    if re.search(r"(?:^|[.:;]\s|\s)(?:An?|The)\s+\*\*%s\*\*\s+[a-z]" % bolded, stripped, re.I):
        return COPULA
    return EMPHASIS


def mask_span(doc: Doc, start_line: int, text: str, span: tuple[int, int]) -> None:
    """Blank the characters of `text[span]` in the document's masked view."""
    blanked = list(text)
    for i in range(*span):
        if blanked[i] != "\n":
            blanked[i] = " "
    for offset, line in enumerate("".join(blanked).split("\n")):
        doc.masked[start_line - 1 + offset] = line


def harvest(docs: list[Doc]) -> dict[str, Term]:
    terms: dict[str, Term] = {}

    def get(name: str) -> Term:
        key = normalize(name)
        if key not in terms:
            terms[key] = Term(name=name.strip())
        return terms[key]

    # Channel 1: each document's declaration of the terms it introduces.
    # Channel 2: lead definition sites, "**Term.**" opening a paragraph.
    for doc in docs:
        sections = sections_by_line(doc)
        for start, text in paragraphs(doc):
            intro = INTRO.search(text)
            if intro:
                # A definition may share the declaration's line, so mask the
                # declaration sentence rather than skipping the lines it spans.
                mask_span(doc, start, text, (intro.start(), intro.end()))
                for bolded in BOLD.findall(intro.group(1)):
                    name = re.sub(r"\s+", " ", bolded.strip().rstrip(",.")).strip()
                    if name:
                        term = get(name)
                        if doc.stem not in term.declared_in:
                            term.declared_in.append(doc.stem)

            refines = REFINES.search(text)
            if refines:
                for bolded in BOLD.findall(refines.group(1)):
                    name = re.sub(r"\s+", " ", bolded.strip().rstrip(",.")).strip()
                    if name:
                        term = get(name)
                        if doc.stem not in term.refined_in:
                            term.refined_in.append(doc.stem)

            m = LEAD_DEFN.match(text)
            if not m:
                continue
            raw = re.sub(r"\s+", " ", m.group(1).strip())
            abbrev_match = ABBREV.search(raw)
            name = ABBREV.sub("", raw).strip()
            looks_like_sentence = (
                len(name.split()) > MAX_TERM_WORDS
                or SENTENCE_MARKERS.search(name)
                or LEADING_ARTICLE.match(name)
            )
            if not name or looks_like_sentence:
                continue
            term = get(name)
            term.abbrev = term.abbrev or (abbrev_match.group(1) if abbrev_match else None)
            term.sites.append(Site(doc.stem, start, sections.get(start, ""), LEAD))
            for d in DISTINGUISH.findall(text):
                d = re.sub(r"\s+", " ", d.strip())
                if d not in term.distinctions:
                    term.distinctions.append(d)

    # Outside 1a, a paragraph-leading bold is as often an emphasised sentence as a
    # definition ("**CD-4 applies unchanged.**"). No heuristic separates them
    # reliably, and none should: a term is a PGC term because a document declares
    # it (1a Sec 2), so an undeclared lead site outside 1a is not a term at all.
    for key in list(terms):
        term = terms[key]
        if term.declared_in:
            continue
        term.sites = [site for site in term.sites if site.doc == "1a"]
        if not term.sites:
            del terms[key]

    # Channel 4: a section named for the term, whose opening prose says what it is.
    by_stem_h = {d.stem: d for d in docs}
    for term in terms.values():
        if term.sites:
            continue
        for stem in term.declared_in:
            doc = by_stem_h.get(stem)
            if doc is None:
                continue
            # The heading names the term if it carries all the term's words:
            # "Determinative and observational content" names both its terms.
            words = [re.escape(w) for w in term.name.lower().split()]
            found = None
            for i, line in enumerate(doc.masked, start=1):
                m = HEADING.match(line)
                if not m:
                    continue
                heading = m.group(2).lower()
                if not all(re.search(r"(?<![\w-])%s" % w, heading) for w in words):
                    continue
                # A section named for the term is where a reader locates it. Its body
                # may use a shortened form ("obligations" under "Composition
                # obligations"), so the term need not recur verbatim.
                depth = len(m.group(1))
                for j in range(i + 1, len(doc.masked) + 1):
                    nxt = HEADING.match(doc.masked[j - 1])
                    if nxt and len(nxt.group(1)) <= depth:
                        break
                    if doc.prose[j - 1] and doc.masked[j - 1].strip():
                        found = j
                        break
                if found:
                    break
            if found:
                term.sites.append(
                    Site(stem, found, sections_by_line(doc).get(found, ""), SECTION_DEFN)
                )
                break

    # Channel 3: a declared term with no lead definition is sited at its first
    # bolded use in the declaring document, after the declaration sentence.
    by_stem = {d.stem: d for d in docs}
    for term in terms.values():
        for stem in term.declared_in:
            if any(s.doc == stem for s in term.sites):
                continue
            doc = by_stem.get(stem)
            if doc is None:
                continue
            sections = sections_by_line(doc)
            # The mark may carry an article inside the bold: "**a claimant**".
            pattern = re.compile(
                r"\*\*\s*(?:an?|the|one|exactly one)?\s*(?:%s)\s*\.?\s*\*\*"
                % "|".join(re.escape(v) for v in variants(term.name)),
                re.I,
            )
            for i, (line, is_prose) in enumerate(zip(doc.masked, doc.prose), start=1):
                if not is_prose or not pattern.search(line):
                    continue
                term.sites.append(Site(stem, i, sections.get(i, ""), classify(line, term.name)))
                break
    return terms


def count_occurrences(docs: list[Doc], terms: dict[str, Term]) -> None:
    patterns = [
        (
            key,
            re.compile(
                r"(?<![\w-])(?:%s)(?![\w-])" % "|".join(re.escape(v) for v in variants(key)),
                re.I,
            ),
        )
        for key in terms
    ]
    for doc in docs:
        for i, (line, is_prose) in enumerate(zip(doc.lines, doc.prose), start=1):
            if not is_prose or not line.strip():
                continue
            stripped = re.sub(r"`[^`]*`", " ", line)
            for key, pattern in patterns:
                if pattern.search(stripped):
                    terms[key].occurrences[doc.stem].append(i)


def find_defects(terms: dict[str, Term]) -> list[tuple[str, str, str]]:
    """Return (severity, invariant, message) for every disagreement found."""
    out = []
    for key in sorted(terms):
        term = terms[key]
        name = term.name
        lead_docs = sorted({s.doc for s in term.sites if s.form in DEFINING_FORMS})

        if len(lead_docs) > 1:
            out.append((
                "defect", "CM-2",
                f"'{name}' carries a definition in {', '.join(lead_docs)} — a term is defined "
                "once; a later document refines the concept, it does not redefine the term.",
            ))

        if term.declared_in and not term.sites:
            out.append((
                "defect", "CM-3",
                f"'{name}' is declared introduced by {', '.join(term.declared_in)} but the "
                "document never marks it at a definition site.",
            ))

        if lead_docs and term.declared_in:
            misplaced = [d for d in term.declared_in if d not in lead_docs]
            if misplaced:
                out.append((
                    "defect", "CM-3",
                    f"'{name}' is declared introduced by {', '.join(misplaced)} but defined in "
                    f"{', '.join(lead_docs)}.",
                ))

        site = term.definition
        if site and site.form == EMPHASIS and term.declared_in:
            out.append((
                "warning", "CM-3",
                f"'{name}' is introduced by {site.doc} but its site (line {site.line}) is bold "
                "emphasis rather than a definition — the document marks the term without saying "
                "what it is.",
            ))

        if term.sites and not term.declared_in and term.home != "1a":
            out.append((
                "warning", "CM-3",
                f"'{name}' is defined in {term.home} but that document does not declare it "
                "among the terms it introduces.",
            ))

        used_elsewhere = {d for d in term.occurrences if d != term.home}
        if term.home and not used_elsewhere:
            out.append((
                "warning", "-",
                f"'{name}' appears only in {term.home} — vocabulary carried by no other document.",
            ))
    return out


def render_index(terms: dict[str, Term], docs: list[Doc]) -> str:
    titles = {d.stem: d.title for d in docs}
    lines = [
        "# PGC Terminology Index",
        "",
        "Derived from the documents of the family by `tools/vocab_index.py`. It records where each",
        "PGC term is defined and where it is used. It is not a glossary: it states no meaning and",
        "carries no authority. The defining document is the only authority for a term, and this",
        "index is regenerated rather than edited — hand edits are discarded on the next run.",
        "",
        f"{len(terms)} terms across {len(docs)} documents.",
        "",
        "## Terms",
        "",
    ]
    for key in sorted(terms):
        term = terms[key]
        heading = term.name + (f" ({term.abbrev})" if term.abbrev else "")
        lines += [f"### {heading}", ""]
        site = term.definition
        if site:
            where = f"{site.section}, " if site.section else ""
            note = "" if site.form == LEAD else f" [{site.form}]"
            lines.append(
                f"- **Defined in** {site.doc} — {titles.get(site.doc, site.doc)} "
                f"({where}line {site.line}){note}"
            )
        elif term.declared_in:
            d = term.declared_in[0]
            lines.append(f"- **Declared by** {d} — {titles.get(d, d)} (no definition site)")
        if term.distinctions:
            lines.append(f"- **Distinguished from** {'; '.join(term.distinctions)}")
        if term.refined_in:
            lines.append(f"- **Refined in** {', '.join(term.refined_in)}")
        used = [d for d in sorted(term.occurrences) if d != term.home]
        if used:
            spread = ", ".join(f"{d} ({len(term.occurrences[d])})" for d in used)
            lines.append(f"- **Used in** {spread}")
        else:
            lines.append("- **Used in** no other document")
        lines.append("")

    lines += ["## By document", ""]
    for doc in docs:
        owned = [terms[k].name for k in sorted(terms) if terms[k].home == doc.stem]
        if owned:
            lines.append(f"- **{doc.stem}** {doc.title} — {', '.join(owned)}")
    lines.append("")
    return "\n".join(lines)


def render_violations(defects) -> str:
    by_kind = defaultdict(list)
    for severity, invariant, message in defects:
        by_kind[severity].append((invariant, message))
    lines = [
        "# Vocabulary Violations",
        "",
        "Derived from the documents by `tools/vocab_index.py`. Each entry is a disagreement",
        "between what a document declares it introduces and where terms are actually defined and",
        "used, tested against the usage rules of the Conceptual Model. A defect is a breach of a",
        "stated invariant; a warning is a condition worth examining that no invariant forbids.",
        "",
        f"{len(by_kind['defect'])} defects, {len(by_kind['warning'])} warnings.",
        "",
    ]
    for severity, title in (("defect", "Defects"), ("warning", "Warnings")):
        lines += [f"## {title}", ""]
        if not by_kind[severity]:
            lines += ["None.", ""]
            continue
        for invariant, message in sorted(by_kind[severity]):
            tag = f"**{invariant}** — " if invariant != "-" else ""
            lines.append(f"- {tag}{message}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", type=Path, default=root / "spec")
    ap.add_argument("--out", type=Path, default=root / "projections")
    ap.add_argument("--check", action="store_true", help="exit non-zero if any defect is found")
    args = ap.parse_args()

    docs = load(args.spec)
    if not docs:
        print(f"no documents found in {args.spec}", file=sys.stderr)
        return 2

    terms = harvest(docs)
    count_occurrences(docs, terms)
    defects = find_defects(terms)

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "terminology_index.md").write_text(render_index(terms, docs), encoding="utf-8")
    (args.out / "vocabulary_violations.md").write_text(render_violations(defects), encoding="utf-8")

    n_defects = sum(1 for s, _, _ in defects if s == "defect")
    print(f"{len(terms)} terms, {len(docs)} documents")
    print(f"{n_defects} defects, {len(defects) - n_defects} warnings")
    print(f"wrote {args.out / 'terminology_index.md'}")
    print(f"wrote {args.out / 'vocabulary_violations.md'}")
    return 1 if (args.check and n_defects) else 0


if __name__ == "__main__":
    raise SystemExit(main())
