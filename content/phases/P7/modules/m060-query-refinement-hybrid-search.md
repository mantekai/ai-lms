---
journey_id: '7.6'
module_num: 60
phase_code: P7
title: 'Query Refinement & Hybrid Search'
tools: 'BM25, dense retrieval, rerankers'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 7.6 — Query Refinement & Hybrid Search

**7.6 — Query Refinement & Hybrid Search** [Core] | Tools: `BM25, dense retrieval, rerankers`
- Learn: OverviewModule 60 (P7) — Query Refinement & Hybrid Search. Tools focus: BM25, dense retrieval, rerankers. Core path — prioritize in your sprint.Query refinement rewrites user questions; hybrid search blends lexical and dense signals; rerankers reorder top-k for better precision at small k.
- Practice: Log raw user queries vs rewritten queries; compare results.Tune BM25 vs vector weights on five test questions.Add a cross-encoder reranker; measure latency impact.Define when to skip reranking for cost reasons.Document fallback if rewriter hallucinates constraints.
- Code: `# Module 60 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 60, "topic": "Query Refinement & Hybrid Search", `
