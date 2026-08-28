# PGC Normative Requirement Index

Derived from the documents of the family by `tools/requirement_index.py`, governed by
`requirement_projection_contract.md`. It is an index of requirement identities, not a
statement of the obligations themselves: it carries each requirement's text and the
references that text states, and never the sections those references reach.

**Authority.** None. Where this projection and the documents disagree, the documents govern
(`0z` §5.2, PJ-7).

356 requirements · 26 documents · 339 bullet · 17 heading

## 1a — Conceptual Model & Terminology

- **CM-1** (§13) A document of this family MUST use the terms defined here with the meanings defined here (§12). — *sections: §12*
- **CM-2** (§13) A document MUST NOT redefine a term defined here; where it needs more, it MUST refine the inherited concept and state what it is refining (§12). — *sections: §12*
- **CM-3** (§13) A document introducing a term not defined here MUST define it, and MUST NOT define it so as to overlap a term defined here (§12). — *sections: §12*
- **CM-4** (§13) A distinction drawn in §4–§11 as *distinguish from* MUST be preserved by every document that relies on it (§12). — *sections: §11, §12, §4*
- **CM-5** (§13) A profile MUST NOT alter the meaning of any term defined here (§12). — *sections: §12*
- **CM-6** (§13) A document MUST relate the concepts as §3 relates them, MUST introduce no relation §3 does not provide, and MUST NOT draw an inference between relations that §3.2 forbids (§3, §14). — *sections: §14, §3, §3.2*
- **CM-7** (§13) Adding, removing, or altering a definition here MUST be a revision of this document, and MUST require every document that used the affected term to be re-examined (§12). — *sections: §12*
- **CM-8** (§13) A term MUST be defined by the document whose subject matter principally establishes it, and ownership of a term MUST NOT be assigned by the order in which documents appear (§12). — *sections: §12*

## 1b — Semantic Model

- **SM-1** (§16) Every change to governed state MUST be a governed transition (§4). — *sections: §4*
- **SM-2** (§16) A determination MUST complete before the transition it governs occurs.
- **SM-3** (§16) A determination MUST be reached over the complete rule set the closure supplies; a partial evaluation MUST NOT yield a determination.
- **SM-4** (§16) Where a closure cannot be established, the determination MUST be `refuse` (§7.1). — *sections: §7.1*
- **SM-5** (§16) Consequences MUST compose by dominance, and no rule may admit what another refuses (§6). — *sections: §6*
- **SM-5a** (§16) Where several applicable rules constrain, their constraints MUST compose by conjunction: a proposal satisfies the composed constraint only where it satisfies every constituent constraint (§6). — *sections: §6*
- **SM-6** (§16) Predicate evaluation MUST NOT alter governed state.
- **SM-7** (§16) A refused proposal MUST NOT partly proceed (§9). — *sections: §9*
- **SM-7a** (§16) An admitted transition MUST NOT come to rest having applied part of what its determination permits; where a realization can apply a transition partly, it MUST determine what state results (§8). — *sections: §8*
- **SM-7b** (§16) A closure MUST be established for the state the transition applies to (§8). — *sections: §8*
- **SM-8** (§16) Every determination MUST produce evidence adequate by §13. — *sections: §13*
- **SM-9** (§16) Transformation of the declarations MUST itself be a governed transition (§10). — *sections: §10*
- **SM-10** (§16) The same `(S, π, C)` MUST yield the same determination, and the same determination applied to the same governed state MUST permit the same resulting state (§12). — *sections: §12*
- **SM-11** (§16) A genesis transition MUST be determined reflexively against the closure its proposal declares, MUST additionally satisfy the profile it claims, and MUST NOT be exempt from §8 (§11). — *sections: §11, §8*
- **SM-12** (§16) Conformance checking MUST re-evaluate the closure and rules recorded in evidence, and MUST NOT rediscover a closure from a live system or current environment (§14). — *sections: §14*

## 1c — Architectural Invariants

- **AI-1** (§4) Behavior originates in declaration
- **AI-2** (§4) No ambient authority
- **AI-3** (§4) The activities do not trade places
- **AI-4** (§5) Determination precedes effect
- **AI-5** (§5) Resolution completes before what depends on it
- **AI-6** (§5) Absence is not permission
- **AI-7** (§5) Refusal dominates
- **AI-8** (§5) Refusal leaves no residue
- **AI-9** (§5) Identity is derived, sealing is real
- **AI-10** (§6) Execution consumes a verified sealed representation
- **AI-11** (§6) Structure is complete before execution
- **AI-12** (§6) Nothing enters by discovery
- **AI-13** (§6) Effects occur only through declared surfaces
- **AI-14** (§7) Every determination is evidenced
- **AI-15** (§7) Evidence is output only
- **AI-16** (§7) Evidence is checkable without its producer
- **AI-17** (§8) Change occurs only by governed transformation

## 2a — Governance Standard

- **GS-1** (§9) The governing relation MUST be declared. It MUST NOT be established by containment, ordering, naming, defaulting, or proximity (§3.1). — *sections: §3.1*
- **GS-2** (§9) A conforming governance arrangement MUST establish the governing relation from both the governing-element and governed-subject perspectives, and MUST refuse where the two assertions disagree (§3.2). — *sections: §3.2*
- **GS-3** (§9) Governance MUST be positive: what is not authorized MUST NOT be admitted into the governed system, and MUST NOT require prohibition in order to be unavailable (§4.1). — *sections: §4.1*
- **GS-4** (§9) Authorization and prohibition MUST NOT be collapsed. Authorization governs existence; prohibition governs occurrence (§4.2). — *sections: §4.2*
- **GS-5** (§9) A governing element MUST be an artifact, admitted, identified, and superseded as any other artifact is (§5). — *sections: §5*
- **GS-6** (§9) Every governing element MUST itself be a governed subject. No element may be exempt from the governance it participates in (§6). — *sections: §6*
- **GS-7** (§9) Change to a governing element MUST be a governed transition (§6, SM-9). — *requirements: SM-9; sections: §6*
- **GS-8** (§9) Composition of applicable elements MUST be by dominance and MUST be order-independent (§7). — *sections: §7*
- **GS-9** (§9) An element's semantic category MUST NOT establish, extend, or limit what it governs (§8). — *sections: §8*

## 2b — Governance Semantic Ontology

- **GO-1** (§11) Every element MUST have exactly one primary semantic category (§3). — *sections: §3*
- **GO-2** (§11) Every semantic element MUST have exactly one provenance — authored, derived, or produced — describing how that element came into existence. Subsequent representations or materializations MUST NOT change it (§6). — *sections: §6*
- **GO-3** (§11) A kind MUST declare its semantic category and any provenance constraint its kind contract imposes. An element's provenance MUST be established explicitly, and neither category nor provenance MUST be inferred from an artifact's name, location, or content (§8). — *sections: §8*
- **GO-4** (§11) A secondary relationship MUST NOT alter, extend, or make ambiguous an element's primary category (§5). — *sections: §5*
- **GO-5** (§11) No element's declarations may violate its category contract (§4). — *sections: §4*
- **GO-6** (§11) An evidential element MUST NOT be referenced as a source of authority (§4.1). — *sections: §4.1*
- **GO-7** (§11) A participatory element MUST NOT carry behavior, and its identity MUST NOT constitute authority (§4.1). — *sections: §4.1*
- **GO-8** (§11) An operational element MUST NOT be a source of authority (§4.1). — *sections: §4.1*
- **GO-9** (§11) Derived and produced elements MUST NOT be sources of governance authority, and MUST carry provenance identifying their source or producing operation (§6). — *sections: §6*
- **GO-10** (§11) A semantic category MUST NOT establish, extend, or limit what an element governs (§1, §7.2). — *sections: §1, §7.2*
- **GO-11** (§11) Authority, concern, federation, and namespace MUST NOT be encoded in a single identifier (§7.2). — *sections: §7.2*
- **GO-12** (§11) Admitting a new kind MUST NOT require an ontology revision (§9). — *sections: §9*

## 2c — Machine Block

- **MB-1** (§15) An artifact MUST have exactly one bounded declaration surface, and nothing outside it MUST determine anything about the artifact (§2). — *sections: §2*
- **MB-2** (§15) A machine block's meaning MUST NOT depend on its location, its surroundings, or its serialized form (§2, §3). — *sections: §2, §3*
- **MB-3** (§15) Equality and identity MUST be defined over the semantic object. Integrity MUST be computed over a canonical form of the semantic object (§3). — *sections: §3*
- **MB-4** (§15) Every declaration element MUST have exactly one semantic owner (§5). — *sections: §5*
- **MB-5** (§15) The universal envelope MUST be closed, and a kind MUST NOT redefine or extend it (§6). — *sections: §6*
- **MB-6** (§15) Identity MUST be declared, MUST be authoritative over position, and MUST NOT be derived from a name or location (§6.1). — *sections: §6.1*
- **MB-7** (§15) Identity, authority, and concern MUST remain separately expressible at the declaration surface, and their representation MUST NOT collapse these distinctions (§6.1, GO-11). — *requirements: GO-11; sections: §6.1*
- **MB-8** (§15) Every block MUST declare exactly one artifact kind, and the kind MUST NOT be inferred (§7). — *sections: §7*
- **MB-9** (§15) An unregistered kind MUST be refused (§7). — *sections: §7*
- **MB-10** (§15) A kind MUST declare whether a governance assertion is required for its ordinary use. Omission MUST be permitted only where the applicable semantic model authorizes it, and MUST NOT constitute exemption from governance (§8). — *sections: §8*
- **MB-11** (§15) Every surface MUST be closed; no surface may admit undeclared elements (§11). — *sections: §11*
- **MB-12** (§15) Every normative declaration element MUST carry a semantic role and a construction disposition (§12). — *sections: §12*
- **MB-13** (§15) Every semantic element of a sealed representation MUST have a declared provenance to at least one of: a declared machine block, a governing artifact, a declared construction transformation, or a required integrity mechanism (§13). — *sections: §13*
- **MB-14** (§15) Admitting a kind MUST NOT require amending this document (§14). — *sections: §14*
- **MB-15** (§15) An element MUST carry a kind if and only if it is admitted as an artifact in its own right; a declaration element of an artifact MUST NOT carry one (§7.1). — *sections: §7.1*

## 2d — Kind Vocabulary

- **KV-1** (§10) A governed system MUST operate under a declared kind vocabulary, and MUST name it (§9). — *sections: §9*
- **KV-2** (§10) A kind vocabulary MUST be closed within its revision; an unrecognized kind MUST be refused (§5). — *sections: §5*
- **KV-3** (§10) A kind MUST be admitted by its vocabulary. A registry, a contract, or a mechanism MUST NOT constitute a kind (§3). — *sections: §3*
- **KV-4** (§10) A machine block MUST carry exactly one authoritative discriminator, whose value is the self-describing canonical kind name (§4). — *sections: §4*
- **KV-5** (§10) A kind MUST NOT be derived from a prefix, a naming convention, a location, or any other positional signal (§4). — *sections: §4*
- **KV-6** (§10) A vocabulary revision MUST be a governed transition, and MUST NOT require amending this document, the Machine Block Standard, or the Governance Semantic Ontology (§6). — *sections: §6*
- **KV-7** (§10) An accepted alias MUST be normalized to the canonical kind before the artifact is treated as conformant, and MUST NOT be carried or emitted as the authoritative classification (§7). — *sections: §7*
- **KV-8** (§10) A representation change MUST NOT increment an artifact's declared version (§8). — *sections: §8*
- **KV-9** (§10) No particular kind MUST be required of a governed system by this family (§9). — *sections: §9*
- **KV-10** (§10) A declared vocabulary MUST state, for each kind it admits, whether a governance assertion is required for that kind's ordinary admission (§5.1, MB-10). — *requirements: MB-10; sections: §5.1*

## 2e — Governance Closure & Authority

- **CA-1** (§11) Authority, ownership, scope, concern, admission, inheritance, and import MUST be separately determinable, and none MUST be inferred from another (§2). — *sections: §2*
- **CA-2** (§11) An authority MUST exist by a declared constituting act, and MUST NOT be constituted by need, precedence, containment, naming, or classification (§3.1). — *sections: §3.1*
- **CA-3** (§11) A purported authority MUST answer all five questions of §3.2 from declared artifacts alone, or MUST NOT be admitted as an authority. — *sections: §3.2*
- **CA-4** (§11) The authority constituting and exercising a jurisdiction MUST be distinguishable from the authority whose subjects it governs (§3.3). — *sections: §3.3*
- **CA-5** (§11) A delegation MUST be declared, MUST NOT exceed its source, and MUST NOT transfer answerability (§3.4). — *sections: §3.4*
- **CA-6** (§11) A concern classification MUST NOT constitute an authority or a jurisdiction (§5). — *sections: §5*
- **CA-7** (§11) A governing element MUST declare its scope as a set of subjects. Scope MUST NOT be represented by the absence of a boundary, or by an unbounded assertion of everything (§5.1). — *sections: §5.1*
- **CA-8** (§11) Inheritance MUST be declared; containment MUST NOT carry governance of itself (§7). — *sections: §7*
- **CA-9** (§11) Import MUST be declared by the receiving closure, MUST be enumerable, and MUST NOT extend the imported element's authority (§8). — *sections: §8*
- **CA-10** (§11) A closure MUST be fully established before any determination over its subject, and MUST be enumerable before evaluation begins (§10.1, §10.3). — *sections: §10.1, §10.3*
- **CA-11** (§11) No governing element may apply to a subject without having been established in that subject's closure (§10.3). — *sections: §10.3*
- **CA-12** (§11) Where a closure cannot be established, the determination MUST be `refuse`, and MUST be distinguishable from a rule refusal (§10.4). — *sections: §10.4*

## 2f — Enforcement & Refusal

- **EN-1** (§10) An obligation MUST be rendered as at least one assertion capable of refusing its violation, and an obligation without such coverage MUST be a finding (§4.1). — *sections: §4.1*
- **EN-2** (§10) An assertion MUST identify the obligation it enforces (§3.1). — *sections: §3.1*
- **EN-3** (§10) An assertion MUST NOT impose a normative consequence beyond its obligation, and MUST NOT be a source of authority (§3.1). — *sections: §3.1*
- **EN-4** (§10) Where an assertion and its obligation differ, the obligation MUST govern (§3.2). — *sections: §3.2*
- **EN-5** (§10) An assertion whose predicate has no admissible input yielding `refuse` MUST be a finding (§4.2). — *sections: §4.2*
- **EN-6** (§10) An obligation MUST be evaluated at every determination whose closure supplies it (§5). — *sections: §5*
- **EN-7** (§10) Enforcement MUST complete before the effect it governs (§5, AI-4). — *requirements: AI-4; sections: §5*
- **EN-8** (§10) A refusal MUST establish what was proposed, what refused it, under what closure and authority, and that nothing proceeded (§6.1). — *sections: §6.1*
- **EN-9** (§10) Rule refusal and closure failure MUST be distinguishable in the determination and in its evidence (§6.2, CA-12). — *requirements: CA-12; sections: §6.2*
- **EN-10** (§10) A refused proposal MUST NOT partly proceed, and no mechanism MUST exist by which a refusal is set aside (§6.3). — *sections: §6.3*
- **EN-11** (§10) An obligation whose violation produces only a report MUST NOT be declared as governance (§6.3). — *sections: §6.3*
- **EN-12** (§10) Refusals MUST be evidenced as fully as admissions (§8). — *sections: §8*
- **EN-13** (§10) Evidence MUST NOT be an input to a determination (§8, AI-15). — *requirements: AI-15; sections: §8*
- **EN-14** (§10) A determination MUST NOT be reported as a refusal unless it establishes what §6.1 requires, and a refusal MUST NOT be delivered as a value that is acted on (§6.1). — *sections: §6.1*

## 3a — Execution Model

- **EX-1** (§15) Execution MUST NOT originate behavior; every step MUST realize behavior the sealed representation already determined (§3). — *sections: §3*
- **EX-2** (§15) Traversal MUST advance only on declared outcomes, according to routing resolvable from the sealed representation alone (§3.2, §4.1). — *sections: §3.2, §4.1*
- **EX-3** (§15) Routing MUST NOT be computed from payload, environment, accumulated state, or caller identity (§3.2). — *sections: §3.2*
- **EX-4** (§15) The structure traversed MUST NOT be added to, removed from, or rerouted during a run (§3.2). — *sections: §3.2*
- **EX-5** (§15) A result a contract does not declare as an outcome MUST NOT be routed on, admitted into the governed transition, or recorded as an outcome, and MUST produce refusal; an outcome for which no routing is declared MUST produce refusal (§4.1, §4.3). — *sections: §4.1, §4.3*
- **EX-6** (§15) Failure paths MUST be declared outcomes with declared routing; no recovery, retry, fallback, or degraded path MUST exist that the declarations did not specify (§4.2). — *sections: §4.2*
- **EX-7** (§15) A step's inputs MUST be resolved from declared references, and MUST NOT be searched for or inferred (§5). — *sections: §5*
- **EX-8** (§15) Every change to governed state MUST be a transition the declarations determined, including its target and its permitting conditions (§6.1). — *sections: §6.1*
- **EX-9** (§15) A governed store MUST be written only through its owner's declarations (§6.2). — *sections: §6.2*
- **EX-10** (§15) The set of effects a system can produce MUST be closed and declared; no implicit effect path MUST exist (§7). — *sections: §7*
- **EX-11** (§15) An event MUST NOT trigger execution (§8). — *sections: §8*
- **EX-12** (§15) A step's result MUST conform to its governing contract's declared surface (§9). — *sections: §9*
- **EX-13** (§15) No property of how an interaction arrived MUST be observable to the traversal (§10). — *sections: §10*
- **EX-14** (§15) Where the declarations do not answer, execution MUST refuse, and MUST NOT default, improvise, or degrade (§11). — *sections: §11*
- **EX-15** (§15) An execution MUST produce sufficient evidence to permit the path taken to be independently checked against the sealed representation (§12). — *sections: §12*
- **EX-16** (§15) An outcome MUST NOT be treated as a governance refusal, whatever it is named, and a refusal MUST NOT be reported as a routable outcome (§4.4, EN-8). — *requirements: EN-8; sections: §4.4*

## 3b — Snapshot

- **SN-1** (§14) A snapshot MUST be immutable from the moment of sealing; any change MUST produce a different snapshot (§3). — *sections: §3*
- **SN-2** (§14) A snapshot's identity MUST be derived from its content, MUST cover every constituent, and MUST NOT be assigned (§4). — *sections: §4*
- **SN-3** (§14) Two snapshots bearing the same identity MUST have identical content (§4). — *sections: §4*
- **SN-4** (§14) A snapshot MUST have execution closure: nothing required to execute may be obtained from outside it (§5). — *sections: §5*
- **SN-5** (§14) A snapshot MUST carry a self-description enumerating its constituents, their integrity, its provenance, and the profile it claims (§6). — *sections: §6*
- **SN-6** (§14) The self-description MUST be a constituent and MUST be covered by the snapshot's identity (§6). — *sections: §6*
- **SN-7** (§14) The claimed profile MUST NOT be authored by the snapshot that claims it (§6, §11). — *sections: §11, §6*
- **SN-8** (§14) A snapshot MUST be verified for integrity, identity, totality, and claimed profile before anything executes against it (§7). — *sections: §7*
- **SN-9** (§14) A snapshot that fails any acceptance check MUST be refused whole; partial acceptance MUST NOT occur (§7). — *sections: §7*
- **SN-10** (§14) No behavior MUST enter execution from outside the accepted snapshot (§8). — *sections: §8*
- **SN-11** (§14) The same snapshot, inputs, and initial state MUST produce the same governed consequences on any conforming agent (§9). — *sections: §9*
- **SN-12** (§14) A snapshot MUST NOT be modified in place; change MUST proceed by constructing a successor (§10). — *sections: §10*
- **SN-13** (§14) A first snapshot MUST satisfy every requirement above; genesis MUST NOT relieve it of any (§11). — *sections: §11*
- **SN-14** (§14) A snapshot MUST declare what its whole-integrity value covers, and that covered set MUST NOT contain the value itself (§6). — *sections: §6*

## 3c — Runtime

- **RT-1** (§13) A runtime MUST originate no governed behavior, hold no domain meaning, make no governing determination, and add nothing to the representation it executes (§2). — *sections: §2*
- **RT-2** (§13) A runtime MUST consume only an accepted snapshot, an interaction, and declared governed state (§3). — *sections: §3*
- **RT-3** (§13) A runtime MUST establish every acceptance condition before executing against a snapshot, and MUST refuse the snapshot whole on any failure (§3.1). — *sections: §3.1*
- **RT-4** (§13) A runtime MUST NOT modify, extend, annotate, or repair an accepted snapshot (§3.1). — *sections: §3.1*
- **RT-5** (§13) A runtime MAY take a decision only where varying it cannot vary a governed consequence (§4). — *sections: §4*
- **RT-6** (§13) A runtime MUST NOT supply a default, select among ambiguous candidates, interpret an unexpected value, or retry an unrouted outcome (§5). — *sections: §5*
- **RT-7** (§13) A runtime MUST produce the governed consequences the snapshot determines and nothing beyond them (§6). — *sections: §6*
- **RT-8** (§13) A runtime MUST evidence every determination it makes, including every refusal (§6, §7). — *sections: §6, §7*
- **RT-9** (§13) A runtime MUST refuse wherever the declarations do not answer, and MUST NOT improvise, default, degrade, or continue (§7). — *sections: §7*
- **RT-10** (§13) A runtime MUST NOT carry behavioral state between executions or across snapshots, and MUST NOT consult prior evidence in a present determination (§9). — *sections: §9*
- **RT-11** (§13) A runtime MUST NOT expose an extension point through which domain behavior enters execution (§11). — *sections: §11*
- **RT-12** (§13) Replacing a conforming runtime with another MUST NOT change any governed consequence (§10). — *sections: §10*
- **RT-13** (§13) A runtime MUST NOT establish what governs a subject; it MUST evaluate obligations already determined and sealed, and MUST refuse rather than resolve what they leave open (§7.1). — *sections: §7.1*

## 3d — Capability

- **CP-1** (§12) A capability MUST be reachable only through its declared contract (§3.1). — *sections: §3.1*
- **CP-2** (§12) A contract MUST declare closed sets of inputs, outputs, and outcomes, and MUST declare its effect disposition (§3). — *sections: §3*
- **CP-3** (§12) Execution MUST NOT depend on anything beneath a contract (§3.1). — *sections: §3.1*
- **CP-4** (§12) A result that is not a declared outcome MUST NOT be routed on (§3.2). — *sections: §3.2*
- **CP-5** (§12) A capability MUST NOT acquire inputs other than through declared references (§4). — *sections: §4*
- **CP-6** (§12) A capability MUST NOT communicate with execution other than through its declared outcome and outputs (§4). — *sections: §4*
- **CP-7** (§12) A non-effecting capability MUST produce no effect and MUST NOT invoke an effecting capability, directly or transitively (§5.1). — *sections: §5.1*
- **CP-8** (§12) Every effect a system produces MUST pass through a declared effecting capability (§5.2). — *sections: §5.2*
- **CP-9** (§12) A binding MUST be declared, MUST resolve before dispatch, and MUST NOT alter what the contract declares (§6). — *sections: §6*
- **CP-10** (§12) Replacing a realization that satisfies a contract MUST NOT change a governed consequence and MUST NOT require a declaration to change (§8). — *sections: §8*
- **CP-11** (§12) A capability MUST NOT be a source of authority, and its reachability MUST NOT constitute permission to reach it (§9). — *sections: §9*

## 3e — Evidence, Attestation & Provenance

- **EV-1** (§13) Every determination MUST produce evidence sufficient to establish the five points of §3.1, and every execution MUST additionally establish its path (§3.1). — *sections: §3.1*
- **EV-2** (§13) Evidence MUST be produced as the determination is made, and MUST NOT be reconstructed afterwards (§4). — *sections: §4*
- **EV-3** (§13) Refusals MUST be evidenced as fully as admissions (§3.3). — *sections: §3.3*
- **EV-4** (§13) Evidence MUST NOT be an input to any determination (§3.2). — *sections: §3.2*
- **EV-5** (§13) Evidence MUST distinguish its determinative content from its observational content, and the distinction MUST be declared rather than inferred (§5.1). — *sections: §5.1*
- **EV-6** (§13) Determinative content MUST be identical across determinations over the same state, proposal, and closure (§5.1). — *sections: §5.1*
- **EV-7** (§13) Observational content MUST NOT participate in any determination (§5.1). — *sections: §5.1*
- **EV-8** (§13) An attestation MUST identify its attesting party, its subject, and the property asserted (§6). — *sections: §6*
- **EV-9** (§13) An attestation MUST NOT be treated as establishing the truth of what it asserts (§6.1). — *sections: §6.1*
- **EV-10** (§13) An attestation chain MUST terminate in a nameable trust root (§6.2). — *sections: §6.2*
- **EV-11** (§13) An attestation MUST NOT confer authority or admissibility on what it attests (§6.3). — *sections: §6.3*
- **EV-12** (§13) Every derived or produced element MUST carry provenance identifying its source and derivation (§7). — *sections: §7*
- **EV-13** (§13) Provenance MUST NOT confer authority, and MUST NOT be read as establishing correctness (§7.1). — *sections: §7.1*
- **EV-14** (§13) Evidence, attestation, and provenance MUST NOT be sources of governance authority (§8). — *sections: §8*
- **EV-15** (§13) Snapshot, evidence, attestation, and actor identities MUST be separately determinable (§9). — *sections: §9*
- **EV-16** (§13) Records MUST be checkable without access to, or trust in, the system that produced them (§10). — *sections: §10*
- **EV-17** (§13) Evidence MUST identify the sealed representation it was produced under and the subject of the determination it records (§3.1). — *sections: §3.1*

## 4a — Governed Construction

- **GC-1** (§14) Construction MUST determine admissibility, and MUST NOT determine adequacy (§4.1). — *sections: §4.1*
- **GC-2** (§14) Admissibility MUST be determinable from declarations and governance alone; construction MUST NOT execute a realization to determine it (§4.2). — *sections: §4.2*
- **GC-3** (§14) Every obligation of §5 MUST be discharged, and none MUST be discharged on the basis of something a later obligation was to establish (§5). — *sections: §5*
- **GC-4** (§14) Only admitted candidates MUST be considered; nothing MUST enter construction by discovery (§5.1). — *sections: §5.1*
- **GC-5** (§14) Nothing depending on a candidate's legality MUST precede that candidate's determination, and nothing after a determination MUST revisit it (§6). — *sections: §6*
- **GC-6** (§14) A refused construction MUST produce no usable output (§6.1). — *sections: §6.1*
- **GC-7** (§14) Construction MUST refuse rather than repair, complete, substitute, or default (§7). — *sections: §7*
- **GC-8** (§14) Construction MUST NOT originate meaning, and a derived element MUST NOT thereby become a source of authority (§8). — *sections: §8*
- **GC-9** (§14) The same declarations under the same closure MUST produce the same authorized representation and the same identity (§9). — *sections: §9*
- **GC-10** (§14) Construction MUST NOT depend on any undeclared input (§9). — *sections: §9*
- **GC-11** (§14) Composition obligations MUST be determined over the whole composition, against the governance that composition carries (§10). — *sections: §10*
- **GC-12** (§14) Copies of one identity within a composition MUST agree, or the composition MUST be refused (§10). — *sections: §10*
- **GC-13** (§14) What was materialized MUST be verified against what was determined, and a mismatch MUST be a refusal (§11). — *sections: §11*
- **GC-14** (§14) Attestation MUST NOT confer admissibility (§12). — *sections: §12*

## 4b — Projection

- **PJ-1** (§13) A projection MUST have a defined source and a declared derivation (§2, §3). — *sections: §2, §3*
- **PJ-2** (§13) A derivation MUST be deterministic and MUST consult nothing but its source (§3). — *sections: §3*
- **PJ-3** (§13) Every projection MUST be governed by a projection contract stating its source, its selection, and its derivation (§3.1). — *sections: §3.1*
- **PJ-4** (§13) A projection MUST make no claim its source does not entail (§4). — *sections: §4*
- **PJ-5** (§13) A projection MUST NOT supply a default, resolve an ambiguity, infer, or silently transform an unresolved condition into a resolved one; where its source does not determine what it would carry, the derivation MUST refuse (§4.2). — *sections: §4.2*
- **PJ-6** (§13) A projection MUST NOT omit anything its contract declares it carries (§4.1). — *sections: §4.1*
- **PJ-7** (§13) Where a projection and its source disagree, the source MUST govern (§5). — *sections: §5*
- **PJ-8** (§13) Nothing MUST be authored into a projection, and a projection MUST NOT be edited (§5). — *sections: §5*
- **PJ-9** (§13) A projection MUST be regenerable from its source (§6). — *sections: §6*
- **PJ-10** (§13) A projection MUST carry provenance identifying its source and derivation (§7). — *sections: §7*
- **PJ-11** (§13) Derivation MUST NOT confer authority on a projection (§7). — *sections: §7*
- **PJ-12** (§13) Projections of one source MUST NOT entail contradictory claims (§8). — *sections: §8*

## 4c — Identity & Addressing

- **ID-1** (§9) An identity MUST be declared and MUST be authoritative over filename, path, containment, position, convention, and manner of discovery (§2.1). — *sections: §2.1*
- **ID-2** (§9) Nothing MUST acquire identity by being found (§2.1). — *sections: §2.1*
- **ID-3** (§9) Identity MUST be defined over the semantic object, and a representation change preserving meaning MUST NOT change identity (§2.2). — *sections: §2.2*
- **ID-4** (§9) Two admitted things bearing one identity MUST be refused (§2.3). — *sections: §2.3*
- **ID-5** (§9) A change of declared semantics MUST be a new identity (§2.4). — *sections: §2.4*
- **ID-6** (§9) Identity MUST NOT carry ordering; supersession MUST be a declared relation (§2.4). — *sections: §2.4*
- **ID-7** (§9) An address MUST NOT be treated as an assertion of identity (§3.1). — *sections: §3.1*
- **ID-8** (§9) A change of address MUST NOT change identity (§3.2, §4.1). — *sections: §3.2, §4.1*
- **ID-9** (§9) Identity MUST NOT be derived from an address (§4.1). — *sections: §4.1*
- **ID-10** (§9) A resolution mechanism MUST NOT assign, alter, normalize, or complete an identity (§4.2). — *sections: §4.2*
- **ID-11** (§9) Where a resolved thing's declared identity differs from what was expected, the difference MUST be refused (§4.2). — *sections: §4.2*
- **ID-12** (§9) A namespace MUST NOT establish authority, concern, or federation, and MUST NOT encode them alongside identity (§5). — *sections: §5*
- **ID-13** (§9) References MUST be by declared identity, and resolution MUST complete before anything depending on it proceeds (§6). — *sections: §6*
- **ID-14** (§9) Resolution MUST NOT search, select among candidates, or fall back; an ambiguous or unresolvable reference MUST be refused (§6). — *sections: §6*
- **ID-15** (§9) A composite identity MUST be derived from its constituents' identities, and MUST change when any constituent changes (§7). — *sections: §7*

## 4d — Governed Transformation

- **TR-1** (§17) A transformation MUST be a governed transition, and its dossier MUST NOT be a member of the governed system (§2, §4). — *sections: §2, §4*
- **TR-2** (§17) Governed content MUST live in registers; a phase document's prose MUST NOT carry it (§5). — *sections: §5*
- **TR-3** (§17) Rules MUST be declared data; check kinds MUST be closed and MUST fail hard on the unknown; every declared rule MUST be evaluated (§5). — *sections: §5*
- **TR-3a** (§17) Every declared rule MUST be demonstrated capable of refusing; a rule set is not evidence that its rules can fail (§5.1). — *sections: §5.1*
- **TR-4** (§17) A verdict MUST name, for each finding, the rule and its location, where a location identifies the register, the entry, and the field concerned (§5). — *sections: §5*
- **TR-5** (§17) A constrained field's admissible values MUST be declared with the register's own declaration, and emptiness MUST be declared rather than inferred (§6). — *sections: §6*
- **TR-5a** (§17) A register's entries MUST be individually addressable; the addressing mechanism is not specified (§6). — *sections: §6*
- **TR-6** (§17) Each register MUST declare its rung; a business rung MUST NOT name a constructed identity; grounding evidence MUST occupy a field declared for it (§7). — *sections: §7*
- **TR-7** (§17) Where a capability is named before it is identified, provisional name and bound identity MUST be reconciled in both directions (§7). — *sections: §7*
- **TR-8** (§17) Admissibility MUST be decided by the rule set alone; a quality score MUST NOT gate, and MUST NOT score a value that admission refuses (§8). — *sections: §8*
- **TR-9** (§17) An unanswered question MUST be recorded as such, MUST NOT be filled in or hedged, and a blocking one MUST make its document inadmissible (§9.1). — *sections: §9.1*
- **TR-10** (§17) Human semantic content MUST enter once; later phases MUST preserve, reference, or declare supersession of it (§9.2). — *sections: §9.2*
- **TR-11** (§17) Preservation MUST be checked in both directions — nothing dropped, nothing invented (§9.2). — *sections: §9.2*
- **TR-12** (§17) Gates MUST be declared, and acceptance MUST NOT be inferred from admissibility (§9.3). — *sections: §9.3*
- **TR-13** (§17) Given the same human answers — the same declared field values (§9) — any worker MUST yield the same admissible registers (§9.4). — *sections: §9, §9.4*
- **TR-14** (§17) A phase determined by its prior MUST be projected, MUST refuse an inadmissible prior, and its verdict MUST NOT be read as evidence about the change (§10). — *sections: §10*
- **TR-15** (§17) A transformation MUST be validated against a named frozen baseline, and never against one containing its own output (§11). — *sections: §11*
- **TR-15a** (§17) Only the first transformation of a system MAY proceed without a baseline; it MUST name a profile it did not author, MUST declare its grounding registers empty rather than omitting them, and MUST satisfy every other requirement of this document. No later transformation MUST claim genesis (§12). — *sections: §12*
- **TR-16** (§17) Claims about the existing system MUST be grounded; truth, belief, and question MUST be kept in separate registers; grounding MUST be able to answer about a named artifact (§11.1, §11.2). — *sections: §11.1, §11.2*
- **TR-17** (§17) Sufficiency MUST be determined before realization, and realization MUST refuse a design that does not fix every fact the realization needs; how it is determined is unconstrained (§13). — *sections: §13*
- **TR-18** (§17) A realized artifact MUST be a function of the design alone (§13). — *sections: §13*
- **TR-19** (§17) An amendment MUST be a whole redeclaration and MUST NOT narrow what it replaces (§13). — *sections: §13*
- **TR-20** (§17) The realization order MUST be gapless over what it schedules and dependency-respecting; whether independent artifacts are ordered relative to one another is not specified (§13). — *sections: §13*
- **TR-21** (§17) Realization MUST cover both authored and amended artifacts, and MUST be checked in both directions against what was asked for (§13). — *sections: §13*
- **TR-22** (§17) Completion MUST require execution against real state, with criteria asserting state rather than returned status (§14). — *sections: §14*
- **TR-23** (§17) A refusal the business declares MUST be discharged by the design, the discharge MUST be stated, and it MUST be checked against what it does rather than only that it was stated (§14). — *sections: §14*
- **TR-24** (§17) Where a rule set has two readers, they MUST derive from one declaration, and divergence MUST be detectable (§15.1). — *sections: §15.1*
- **TR-25** (§17) A human answer MUST be recorded as declared register content addressed by field (§9). — *sections: §9*

## 4e — Supersession

- **SU-1** (§11) Supersession MUST be a declared relation between two exact identities, and MUST NOT cause any reference to resolve to a different identity (§2). — *sections: §2*
- **SU-2** (§11) Nothing MUST be treated as superseded by deletion, renaming, deprecation in prose, or disuse (§2). — *sections: §2*
- **SU-3** (§11) The relation MUST be declared once, on the successor; both sides MUST be established from that declaration (§3). — *sections: §3*
- **SU-4** (§11) A predecessor recorded as superseded by nothing MUST be refused (§3). — *sections: §3*
- **SU-5** (§11) Where `X` supersedes `Y`, nothing in the governed system MUST reference `Y` other than the supersession declaration SU-3 requires, and the closure MUST be determined during construction (§4). — *requirements: SU-3; sections: §4*
- **SU-6** (§11) Referential closure MUST be determined over the whole composition (§4). — *sections: §4*
- **SU-7** (§11) A superseded thing MUST be excluded from every projection execution consumes, and MUST be retained in the canonical record and reachable by inspection (§5). — *sections: §5*
- **SU-8** (§11) No mechanism MUST delete a superseded thing (§6). — *sections: §6*
- **SU-9** (§11) A supersession MUST determine its blast radius over the composition rather than leaving it to be discovered, and MUST NOT be treated as determining the state of parties the composition does not carry (§8). — *sections: §8*
- **SU-10** (§11) A superseded profile or family revision MUST NOT retroactively alter claims discharged against it (§8, §9). — *sections: §8, §9*
- **SU-11** (§11) An amendment MUST NOT change an artifact's declared semantics; such a change MUST be a new identity (§7, ID-5). — *requirements: ID-5; sections: §7*

## 5a — Governed Interaction Boundary

- **IB-1** (§15) No boundary contract MUST depend on any external protocol (§2). — *sections: §2*
- **IB-2** (§15) An operation identity MUST be uniquely resolvable and MUST NOT be the identity of an executable target (§5). — *sections: §5*
- **IB-3** (§15) The boundary MUST bind to a governed executable target without requiring it to carry any particular vocabulary classification (§6). — *sections: §6*
- **IB-4** (§15) Ingress and egress MUST be contracts at the edge and MUST NOT be modelled as execution stages (§3). — *sections: §3*
- **IB-5** (§15) Operation-to-target resolution, input-contract existence, and closure establishment MUST be determined before interaction time; execution MUST enforce the constructed boundary (§6, §12). — *sections: §12, §6*
- **IB-6** (§15) Ingress and egress MUST declare explicit normalization to and from the canonical form; raw passthrough of an inbound payload or a governed result MUST NOT occur (§8). — *sections: §8*
- **IB-7** (§15) An adapter MUST determine no governed or domain semantics (§10). — *sections: §10*
- **IB-8** (§15) A result class MUST carry no external representation semantics (§9). — *sections: §9*
- **IB-9** (§15) The mapping from result class to external representation MUST be adapter-owned and MUST NOT appear in an egress contract (§9). — *sections: §9*
- **IB-10** (§15) No boundary contract or adapter MUST introduce domain state-transition, resource, or result semantics; domain meaning MUST enter only through governed execution artifacts (§2, §10). — *sections: §10, §2*
- **IB-11** (§15) Applicability of boundary contracts MUST be determined within an applicable governance scope, and contracts from incompatible scopes MUST NOT be combined (§11). — *sections: §11*
- **IB-12** (§15) Within one governance scope, an operation identity MUST resolve to exactly one governed invocation contract (§5, §11). — *sections: §11, §5*
- **IB-13** (§15) An interaction with no applicable ingress contract MUST be refused (§6). — *sections: §6*
- **IB-14** (§15) Evidence leaving the boundary MUST be declared, not incidental (§7). — *sections: §7*
- **IB-15** (§15) A system MUST NOT be constituted through its own interaction boundary (§13). — *sections: §13*

## 5b — Governed Inspection

- **IN-1** (§15) Inspection MUST NOT change governed state, produce an effect, or modify what it reads (§3.1). — *sections: §3.1*
- **IN-2** (§15) Answering a read operation MUST NOT invoke a governed executable target or otherwise introduce execution (§3.2). — *sections: §3.2*
- **IN-3** (§15) Every question that may be asked MUST be a declared read operation with a declared identity, admitted and sealed like any other artifact (§4). — *sections: §4*
- **IN-4** (§15) A read operation MUST declare whether it reads or queries, and a read MUST NOT compute a relationship (§5). — *sections: §5*
- **IN-5** (§15) A query MUST derive its answer from declared structure only (§5). — *sections: §5*
- **IN-6** (§15) The read surface MUST be able to answer about a named artifact, not only to enumerate (§6). — *sections: §6*
- **IN-7** (§15) Inspection MUST read the governed system and its projections, and MUST NOT read construction internals or mechanism state (§7). — *sections: §7*
- **IN-8** (§15) A read operation MUST return the answer asked for, and MUST NOT delegate its derivation to the caller (§8). — *sections: §8*
- **IN-9** (§15) Malformed or unreadable material MUST produce a refusal, and an unanswerable question MUST be refused rather than answered emptily (§9). — *sections: §9*
- **IN-10** (§15) A read operation MUST NOT fall back to another source, a partial source, or a default (§9). — *sections: §9*
- **IN-11** (§15) A governed system MUST be able to answer what it contains, what governs what, what it determined, and what it is (§10). — *sections: §10*
- **IN-12** (§15) Whether a read may proceed MUST be determined by the governance applicable to it; reachability MUST NOT constitute permission (§11). — *sections: §11*
- **IN-13** (§15) No read path MUST exist that is not a declared read operation (§2, §12). — *sections: §12, §2*
- **IN-14** (§15) Inspection MUST NOT be performed against a representation that has not been sealed (§13). — *sections: §13*
- **IN-15** (§15) Inspection MUST be reachable independently of the interaction boundary, and a read operation MUST NOT be admitted as an interaction at that boundary (§2.1). — *sections: §2.1*
- **IN-16** (§15) An open read-surface policy MUST NOT dispense with the determination IN-12 requires (§11). — *requirements: IN-12; sections: §11*

## 6a — Normative Platform Profile

- **NP-1** (§12) A profile MUST NOT permit what the family forbids, and MUST NOT require less than the family requires (§3.1). — *sections: §3.1*
- **NP-2** (§12) A conforming system under any profile MUST be a conforming system under the family (§3.1). — *sections: §3.1*
- **NP-3** (§12) A profile MUST NOT redefine the semantics of a core facility or give a normative term an incompatible meaning (§4). — *sections: §4*
- **NP-4** (§12) A profile MUST NOT weaken, exempt from, or relax any invariant of this family (§4). — *sections: §4*
- **NP-5** (§12) A profile MUST NOT introduce a facility the family has no home for (§4). — *sections: §4*
- **NP-6** (§12) A profile's additional obligations MUST be enforceable, and an unenforceable one MUST NOT be declared as an obligation (§5). — *sections: §5*
- **NP-7** (§12) A profile MUST NOT be authored by a system that claims it (§6). — *sections: §6*
- **NP-8** (§12) A profile MUST decide every deferred item bearing on a conformance claim it supports (§7). — *sections: §7*
- **NP-9** (§12) A profile MUST have an identity, and a change to its obligations MUST be a new identity (§9). — *sections: §9*
- **NP-10** (§12) A derived profile MUST name its base by identity and MUST NOT widen it (§10). — *sections: §10*
- **NP-11** (§12) A profile MUST NOT use selection, parameterization, or an additional requirement to make a behavior the family prohibits appear permitted (§13). — *sections: §13*
- **NP-12** (§12) A profile MUST NOT decide a deferred item by deferring it to the system that claims the profile (§7). — *sections: §7*

## 6b — Execution Environment Profiles

- **EE-1** (§11) Governed consequences MUST NOT vary with the environment (§2). — *sections: §2*
- **EE-2** (§11) An environment profile MUST NOT introduce a governance kind, semantic category, authority, or determination point (§4). — *sections: §4*
- **EE-3** (§11) An environment profile MUST NOT exempt a system from any invariant of this family (§4). — *sections: §4*
- **EE-4** (§11) A governed consequence MUST NOT follow from an environmental property no declaration established (§6). — *sections: §6*
- **EE-5** (§11) An environment profile MUST NOT convert an ambient environmental property into a governed input; only the system may declare one (§6). — *sections: §6*
- **EE-6** (§11) Two conforming environments executing the same snapshot, inputs, and initial state MUST produce the same governed consequences (§7). — *sections: §7*
- **EE-7** (§11) Inability to establish governed state or an applicable closure MUST produce refusal, whatever the environmental cause (§8.1). — *sections: §8.1*
- **EE-8** (§11) A distributed environment MUST NOT relieve a system of any invariant a single-node system carries (§8.3). — *sections: §8.3*

## 6c — Domain Profiles

- **DP-1** (§12) A domain MUST NOT weaken, exempt itself from, or reinterpret governance applicable to it (§3.1). — *sections: §3.1*
- **DP-2** (§12) A domain's declarations MUST compose with applicable governance by dominance; a domain MUST NOT declare an obligation that contradicts one already applicable (§3.1). — *sections: §3.1*
- **DP-3** (§12) A domain MUST NOT be treated as an authority without satisfying the authority test, and MUST NOT acquire jurisdiction by being named, bounded, deployed separately, or separately owned (§4). — *sections: §4*
- **DP-4** (§12) A domain profile MUST state whether the domain claims to be an authority or is a concern (§5). — *sections: §5*
- **DP-5** (§12) A domain MUST have no private admission path; its declarations are admitted as any others are (§6). — *sections: §6*
- **DP-6** (§12) A domain MUST change only through governed transformation against a baseline (§6, §10). — *sections: §10, §6*
- **DP-7** (§12) A write across a domain boundary MUST be authorized by the governance applicable to the store written, and MUST NOT be authorized by reach (§7). — *sections: §7*
- **DP-8** (§12) A domain MUST NOT depend on another domain's internals; dependence MUST be on what the other declares (§7). — *sections: §7*
- **DP-9** (§12) Admitting a domain kind MUST NOT require an ontology revision, and a domain MUST NOT hold a private vocabulary (§8). — *sections: §8*
- **DP-10** (§12) A domain whose subject matter is governance MUST NOT thereby acquire authority over the platform (§9). — *sections: §9*
- **DP-11** (§12) A domain MUST NOT claim genesis (§10). — *sections: §10*

## 7a — Conformance Model

- **CF-1** (§13) A conformance claim MUST name its subject, its profile, its revision, and its claimant (§2). — *sections: §2*
- **CF-2** (§13) A claim MUST NOT be discharged by evidence about a different subject (§3.2). — *sections: §3.2*
- **CF-3** (§13) A system instance claim MUST be discharged by discharging every constituent class (§3.1). — *sections: §3.1*
- **CF-4** (§13) Discharge MUST NOT require the evaluator to trust the claimant; reliance on an assertion MUST be visible as an attestation (§4). — *sections: §4*
- **CF-5** (§13) Conformance MUST be established over semantic guarantees, and MUST NOT be established by resemblance to any realization (§5). — *sections: §5*
- **CF-6** (§13) An evaluation MUST derive from a stated obligation, and MUST NOT add to or relax one (§6). — *sections: §6*
- **CF-7** (§13) An obligation with no derivable evaluation MUST be a finding against the document stating it (§6). — *sections: §6*
- **CF-8** (§13) An evaluation MUST use a discharge class capable of establishing the obligation (§7.5). — *sections: §7.5*
- **CF-9** (§13) A negative property MUST NOT be discharged observationally (§7.2, §8). — *sections: §7.2, §8*
- **CF-10** (§13) An obligation about what must not vary MUST be discharged by substitution, and a subject exercised in one configuration MUST NOT be treated as having discharged it (§7.3). — *sections: §7.3*
- **CF-11** (§13) No conformance level denoting partial satisfaction of an obligation MUST be defined (§9). — *sections: §9*
- **CF-12** (§13) Two conforming systems under one profile and revision producing different governed consequences from the same inputs MUST be a finding against at least one (§10). — *sections: §10*
- **CF-13** (§13) A conformance claim MUST identify, for each discharge, whether it is observational, structural, comparative, or derivational (§7). — *sections: §7*
- **CF-14** (§13) The subject classes applicable to a system-instance claim MUST be determined from the accepted snapshot's self-description and its claimed profile, and MUST NOT be enumerated by the claimant (§3.1). — *sections: §3.1*

## 7b — Conformance Test Specification

- **CD-1** (§12) A demonstration MUST state the obligation it discharges, its subject, its discharge class, what must be shown, and what constitutes failure (§2). — *sections: §2*
- **CD-2** (§12) A demonstration stating no obligation MUST NOT form part of a conformance claim (§2). — *sections: §2*
- **CD-3** (§12) Every obligation whose consequence is refusal MUST have a demonstration exhibiting the refusal, its grounds, its cause, and that nothing partly proceeded (§3.1). — *sections: §3.1*
- **CD-4** (§12) Every demonstration MUST be shown capable of failing (§4). — *sections: §4*
- **CD-5** (§12) A demonstration MUST refuse where its subject is malformed, absent, or unreadable, and MUST NOT report success (§4). — *sections: §4*
- **CD-6** (§12) A structural demonstration MUST state what path was sought and over what its search was total, and MUST follow transitive reach where the obligation is transitive (§5.2). — *sections: §5.2*
- **CD-7** (§12) A comparative demonstration MUST use genuinely independent variants, and MUST state what was varied and held constant (§5.3). — *sections: §5.3*
- **CD-8** (§12) A derivational demonstration MUST re-derive from supplied material and MUST NOT consult the producing system (§5.4). — *sections: §5.4*
- **CD-9** (§12) A fixture MUST be declared, identified, and supplied with the claim (§6). — *sections: §6*
- **CD-10** (§12) A negative demonstration MUST use a fixture that violates the obligation (§6). — *sections: §6*
- **CD-11** (§12) A fixture MUST NOT be adjusted to make a demonstration pass (§6). — *sections: §6*
- **CD-12** (§12) Every obligation binding a claimed subject MUST have a demonstration, and any obligation without one MUST be reported (§7). — *sections: §7*
- **CD-13** (§12) A system instance claim MUST include demonstrations of composition obligations, which MUST NOT be assembled from part-level results (§8). — *sections: §8*
- **CD-14** (§12) A genesis claim MUST demonstrate that the claimed profile was not authored by what claims it (§9). — *sections: §9*
- **CD-15** (§12) A failing demonstration MUST be reported as a finding, and MUST NOT be discharged by repetition (§10). — *sections: §10*
- **CD-16** (§12) A demonstration MUST NOT be reported as establishing anything broader than its stated subject, obligation, fixtures, and discharge class (§10). — *sections: §10*
- **CD-17** (§12) An obligation forbidding a structural possibility MUST be discharged by an absence demonstration over a stated and totally searched space, and MUST NOT be discharged by a refusal or by observation (§3.2). — *sections: §3.2*
