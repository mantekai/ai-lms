<!--
  Topic coverage, extracts, and patch-capture (former §27–§73). Manish.AI
-->

# Research & topic corpus

[`topic-and-extract-corpus.md`](topic-and-extract-corpus.md) holds **§27–§73**: domain topic glossaries, image extracts, external program notes, hackathon depth, module-level extracts, and gap-fill material.

`scripts/build_learner_phase_corpus.py` reads this file (together with the slim platform spec) to populate:

- `content/phases/P*/supplement.md`
- `content/phases/P*/depth/mNNN.md`
- `content/categories/*.md`

Do **not** duplicate this material inside `content/spec/agentiq_platform_spec.md` — the slim spec ends at §26.
