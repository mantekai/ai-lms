<!--
  Per-phase curriculum tree. Manish.AI
-->

# Phases (content layout)

Each phase **`P0` … `P19`** is a folder with the same shape:

| Path | Role |
|------|------|
| `P*/index.md` | Journey table + links (regenerated with `scripts/build_learner_phase_corpus.py`) |
| `P*/modules/*.md` | Core Learn / Practice / Code per catalog module (`scripts/split_modules_one_file_each.py`) |
| `P*/supplement.md` | Phase-wide supplemental depth (optional; generated when routed content exists) |
| `P*/depth/mNNN.md` | Extra notes tied to catalog module `NNN` (optional) |

Global phase metadata table: [`overview.md`](overview.md).

**§6 single-file archive** (same module text before splitting): [`../curriculum/section-6-modules.md`](../curriculum/section-6-modules.md).
