# Genealogy explorer — draft UX and implementation plan

Prepared 17 September 2026 from the current local records. This is a product plan, not a genealogy source or a change to research conclusions.

## Recommended direction

Build a person-centered family graph with a persistent detail panel and an integrated document viewer. Use a stable generational layout for family browsing, with an optional research view for uncertain connections. Start with a private, local, read-only application generated from the existing files.

The main interaction is: select a person → read their facts and relationships → inspect the supporting claim → open its document. Selecting an edge should explain the relationship and its evidence just as selecting a person explains the person.

## What the data supports today

| Existing artifact | Observed structure | UX role |
|---|---|---|
| `people.jsonl` | 14 identities; IDs, aliases, identity notes, claim/census links, explicit non-merge boundaries | Initial person nodes and disambiguation |
| `claims.jsonl` | 210 claims; 34 have person IDs; all have source IDs | Facts, evidence, hypotheses, and historical conclusions |
| `sources.jsonl` | 204 citation bundles with claim links, URLs, and local evidence paths | Source cards and document navigation |
| `CATON_CENSUS_LEDGER.md` | Stable household IDs; raw readings, normalized observations, and interpretation kept separate | Household panels and census evidence |
| `discrepancies.jsonl` | 9 records: 5 resolved, 4 open/provisional/unresolved | Competing readings and identity questions |
| `searches.jsonl` | 27 searches; 25 legacy/unstructured, 2 structured | Research coverage and limitations |
| `evidence/` | Images, PDFs, Markdown notes, text, CSVs, ZIPs | Original records, crops, transcripts, and supporting notes |
| `BRIEF.md` | Current synthesis | Research context and orientation |

The registry is intentionally an identity-disambiguation list, not a complete family tree. Sarah, Julia, William Bramwell, and much of the documented direct line need person records before a complete family view is possible. There is no explicit relationship table. Relationships are embedded in claim text and narrative material.

The existing `TREE.md` and `tree.html` are identified as stale by `README.md`. The HTML's paper colors and serif typography can serve as a visual reference; its genealogy content must be regenerated. Current counts should come from parsed files: the brief still says 209 claims, while the file contains 210.

## Screen and interaction design

### Family canvas

- Open centered on Aaron, with immediate family and a visible “Parents unknown” annotation. Do not invent parent nodes.
- Person cards show name, supported lifespan, and a short locality or identity qualifier. Keep similarly named Aarons distinguishable at every zoom level.
- Use solid, labeled edges for reviewed established relationships. Dashed, explicitly labeled hypotheses appear only when “Show hypotheses” is enabled.
- Keep document nodes off the default family canvas. An optional evidence view can expose person → claim → source → file connections.
- Provide search by name/alias, expand relatives, zoom to selection, reset view, and a family/research view switch. Expand a small neighborhood instead of exposing the entire graph at once.
- Clicking selects without moving the graph; a separate “Focus here” action recenters it. Preserve position and expansion state when returning from a document.
- Keep unrelated candidate clusters separate. A shared claim, surname, household, or source does not create a kinship edge.

### Person detail panel

Use a right-side panel on desktop, with a full-page detail route on narrow screens. Make each person and source directly linkable.

1. **Overview:** supported vital facts, aliases, identity qualifier, and concise unresolved questions. Put “Parents unknown” near Aaron's name.
2. **Family:** relationships with explicit status and supporting evidence; distinguish established relatives from research candidates.
3. **Timeline:** reviewed dated life events, preserving approximate dates and conflicting values. Claim dates sometimes describe research activity, so do not automatically turn every dated claim into a life event.
4. **Documents:** thumbnails or file-type cards, citation, date if recorded, and a sentence explaining relevance. Label original record, transcript, and research note separately.
5. **Research:** claims, competing readings, identity boundaries, search coverage, and historical/superseded conclusions.

Show readable labels by default; expose claim/source IDs for traceability. Offer keyboard navigation and a synchronized people list so browsing does not depend on manipulating a graph. Do not communicate uncertainty with color alone.

### Relationship and document details

An edge opens its exact assertion, assessment, supporting and conflicting claim IDs, and rationale. Evidence grade and relationship certainty are separate concepts: a primary newspaper can support an inferred relationship without proving it.

Open images and PDFs in a larger viewer with zoom, available crop/full-page links, citation, source URL, and an adjacent transcript or note. Preserve a breadcrumb back to the person and claim. Show “No local image retained” or access restrictions explicitly when only a citation exists. Never represent a research note as the original record.

Deduplicate displayed files by normalized path, while preserving every citation bundle and its claim links. A source bundle can contain multiple citations; its count is not a count of independent documents. ZIPs can initially be download-only; CSVs can use a basic table preview.

## Minimum data work

1. **Audit coverage.** Report registered/unregistered people, unlinked claims, missing local files, legacy source bundles, and proposed relationship extractions. Use names to suggest matches for review, never to merge identities automatically.
2. **Register the first family cluster.** Assign stable IDs to Aaron's immediate family and the direct-line people needed for the first view; link reviewed claims to the correct subjects. Resolve both person-to-claim and claim-to-person references, preserving their origin and flagging disagreement.
3. **Add an explicit relationship registry.** Proposed fields: relationship ID, from/to person IDs, relationship type, assessment (`established`, `hypothesis`, `disputed`, `rejected`), lifecycle, supporting/conflicting claim IDs, rationale, and review date. Keep identity constraints in their own category. Being recorded in one household is not equivalent to parentage.
4. **Create a generated presentation dataset.** Compile people, reviewed relationships, selected profile facts/events, claims, sources, census records, conflicts, and asset references. Every displayed fact/event must retain claim/source provenance. Retain unlinked claims in a searchable research index rather than silently dropping them.
5. **Preserve ownership.** Existing canonical files continue to own their current information. Document the relationship registry's authority in `DATA_MODEL.md` when implementing it. Generated UI data must be reproducible and never become an alternate editable evidence store.

Do not derive conclusions solely from `status: active` or an A/B grade. Some active legacy claims contain old interpretations alongside later qualifications. Profile summaries and relationship assessments need review against current synthesis and discrepancy resolutions.

## Delivery sequence

### 1. Select the interaction treatment

Compare the references below using the same actions: locate a person, follow a relationship, inspect evidence, and return to the original view. Decide primarily on family layout, detail-panel behavior, and evidence depth. Produce two lightweight layouts using the same small reviewed dataset: a generational tree and a research network.

### 2. Build one complete browsing path

Use Aaron, Sarah, Julia, Joseph, and the elder Thomas as the initial slice. Demonstrate Aaron/Sarah's marriage using C005, Julia's parent information using C037 with its informant caveat, the Joseph sibling hypothesis using C110, and Thomas's possible parentage using C099/current synthesis. Include Julia's birthplace conflict to exercise conflicting evidence display. New person IDs and relationship assessments are proposed work, not already present data.

Deliver a working path from Aaron → Julia → supporting claim → death certificate, plus a clearly optional hypothesis view. This tests the useful experience before expanding to all people.

### 3. Expand and validate

Add the reviewed direct line, remaining registered candidates, document previews, search, filters, and historical claims. Add comparison of similarly named people after the basic browsing flow works. Defer maps, editing, collaboration, and public hosting to later scope.

At this scale, a graph database is unnecessary. A small web application with a generated JSON dataset and a local file-serving layer is sufficient. Choose the rendering library after selecting the layout treatment. Keep layout positions and interface state separate from evidence data. Record generation time and input fingerprints so stale displays are detectable.

### Acceptance checks

- Aaron has no established parent edge; enabling hypotheses never changes that assessment.
- Joseph remains an unproved sibling hypothesis despite the newspaper's evidence grade.
- Direct-line Aaron, elder Aaron, and Aaron F. remain separate identities.
- Julia's accepted birthplace and competing readings remain inspectable with provenance.
- Every displayed relationship and profile fact traces to reviewed claims; every document card identifies its source bundle and actual file availability.
- Superseded/reversed claims remain available in history and do not silently become current profile facts.
- Back navigation restores selection and graph position; people and documents have stable links.
- Registry changes pass the existing project validator; new relationship validation checks endpoint IDs and provenance. UI checks cover the browsing path and uncertainty controls.

## UX references

Links and feature descriptions checked against official pages on 17 September 2026; these are design references, not a migration recommendation or a hands-on usability evaluation.

| Reference | What to inspect | Relevance |
|---|---|---|
| [FamilySearch tree interaction](https://www.familysearch.org/en/help/helpcenter/article/new-landscape-and-pedigree-views) | Person selection opens a side sheet, with navigation to the full person page; compare portrait and landscape layouts | Strong starting pattern for approachable family browsing; help page previews the interaction without needing your tree |
| [Gramps Web demo](https://demo.grampsweb.org/) | Person-centered interactive charts and navigation across people, events, sources, citations, and media | Closest functional reference for evidence-rich genealogy; [official homepage](https://www.grampsweb.org/) lists demo login `owner` / `owner` |
| [Kumu gallery](https://kumu.io/gallery) and [profiles](https://docs.kumu.io/guides/profiles) | Relationship maps with detail profiles for both nodes and connections | Best reference for candidate clusters and explaining an edge; use neighborhood filtering to limit density |
| [Family Echo](https://www.familyecho.com/) | Compact family tree, person details, and navigation among parents, partners, children, and siblings | Useful comparison for a simpler tree-first experience |

Recommended combination: FamilySearch's selection/panel interaction, Gramps' source hierarchy, and Kumu's inspectable relationship profiles. Keep the existing paper/serif aesthetic as one visual option, independent of which interaction model wins.
