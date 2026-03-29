<!--
  Machine-readable topic coverage registry from input/topics_coverage.csv. Manish.AI
-->

# Module coverage registry

The CSV `input/topics_coverage.csv` ties each module to **content tier**, **blueprint references**, and **coverage notes** (e.g. whether learning is self-contained on the module page).

- **Rows:** 133 (one per module 1–133), plus header.
- **Columns:** `phase_code`, `module_num`, `module_title`, `priority`, `content_tier`, `self_contained_on_page`, `blueprint_ref`, `coverage_notes`.

For a rendered table in-repo, open the CSV in a spreadsheet or run:

`python3 -c "import csv;print(open('input/topics_coverage.csv').read()[:2000])"`

Narrative topic glossaries and supporting depth are summarized in **[`docs/PRD_AgentIQ.md`](../docs/PRD_AgentIQ.md)**; routed text also lives under **`content/phases/<P*>/supplement.md`** and **`content/phases/<P*>/depth/`** (see each phase’s [`index.md`](phases/P0/index.md)). The full capture remains in **[`research/topic-and-extract-corpus.md`](research/topic-and-extract-corpus.md)** (§27+).
