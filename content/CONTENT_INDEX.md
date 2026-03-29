<!--
  Index of LMS content: layered spec, curriculum, research, phases.
  Manish.AI
-->

# Content library index

Material is **layered** so curriculum and research text are **not duplicated** inside the slim platform spec:

| Layer | Path | Contents |
|--------|------|----------|
| **Platform spec** | [`spec/agentiq_platform_spec.md`](spec/agentiq_platform_spec.md) | §1–§5, §6 **pointer**, §7–§26 |
| **Curriculum §6 archive** | [`curriculum/section-6-modules.md`](curriculum/section-6-modules.md) | Full module definitions (split → `phases/P*/modules/`) |
| **Research corpus** | [`research/topic-and-extract-corpus.md`](research/topic-and-extract-corpus.md) | §27–§73 (topic depth, extracts, routed to `supplement.md` / `depth/`) |

CSV registries: **`input/*.csv`**.

## Platform slices

| Path | Description |
|------|-------------|
| [`platform/`](platform/) | Extracts from slim spec (vision, FRs, gamification, agents, …) |
| [`platform/catalogs-and-roadmap.md`](platform/catalogs-and-roadmap.md) | Certifications, capstones, hackathons catalog, NFRs, metrics, roadmap (§18–§26) |

## Primary tree: `phases/` → `modules/` → `depth/`

| Path | Description |
|------|-------------|
| [`phases/P0` … `phases/P19`](phases/) | **`index.md`**, **`modules/`**, optional **`supplement.md`**, optional **`depth/mNNN.md`** |
| [`phases/overview.md`](phases/overview.md) | Summary table from `input/phases.csv` |

**Journey ids** (`0.1`, `1.2`, …) = phase index · order within phase. **Catalog #** = `module_num` 1–133.

## Other folders

| Folder | Description |
|--------|-------------|
| [`categories/`](categories/) | Hackathon / startup depth (generated) |
| [`topics-coverage-from-registry.md`](topics-coverage-from-registry.md) | Pointer to `input/topics_coverage.csv` |
| [`navigation/`](navigation/) | App nav pages |
| [`capstones/`](capstones/) | Capstone specs |
| [`certifications/`](certifications/) | Certification catalog |
| [`hackathons/`](hackathons/) | Hackathon rows + detail |
| [`opensource/`](opensource/) | OSS targets |
| [`yc-ideas/`](yc-ideas/) | Startup ideas |

**Product overview:** [`docs/PRD_AgentIQ.md`](../docs/PRD_AgentIQ.md)

**Regenerate:**

- `python3 scripts/split_modules_one_file_each.py` — from [`curriculum/section-6-modules.md`](curriculum/section-6-modules.md) → `phases/P*/modules/`
- `python3 scripts/build_learner_phase_corpus.py` — `spec/` + `research/` → PRD, indexes, supplements
- `python3 scripts/extract_platform_docs.py` — `spec/` → `platform/`
- `python3 scripts/split_spec_into_layers.py` — only if re-splitting a monolithic spec into layers
- `python3 scripts/rebuild_content_from_input.py` — optional `content/modules/` rollup
