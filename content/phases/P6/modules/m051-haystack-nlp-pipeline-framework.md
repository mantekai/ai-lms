---
journey_id: '6.7'
module_num: 51
phase_code: P6
title: 'Haystack — NLP Pipeline Framework'
tools: 'Haystack, pipelines'
priority: 'OPTIONAL'
source: content/curriculum/section-6-modules.md
---

# 6.7 — Haystack — NLP Pipeline Framework

**6.7 — Haystack — NLP Pipeline Framework** [Optional] | Tools: `Haystack, pipelines`
- Learn: OverviewModule 51 (P6) — Haystack — NLP Pipeline Framework. Tools focus: Haystack, pipelines. Optional depth — revisit when you need this specialty.Haystack builds retrieval and QA pipelines with a document store abstraction. Compare to LangChain when teams already standardise on Haystack nodes.
- Practice: Run a minimal indexing + query pipeline from docs.Swap retriever component once (e.g. BM25 vs dense).Measure recall@k on five hand-made questions.Note deployment story for their pipeline runner.Decide Haystack vs LlamaIndex for one sample project.
- Code: `# Module 51 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 51, "topic": "Haystack — NLP Pipeline Framework",`
