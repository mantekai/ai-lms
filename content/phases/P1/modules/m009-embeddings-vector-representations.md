---
journey_id: '1.3'
module_num: 9
phase_code: P1
title: 'Embeddings & Vector Representations'
tools: 'OpenAI Embeddings, SBERT'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 1.3 — Embeddings & Vector Representations

**1.3 — Embeddings & Vector Representations** [Core] | Tools: `OpenAI Embeddings, SBERT`
- Learn: OverviewModule 9 (P1) — Embeddings & Vector Representations. Tools focus: OpenAI Embeddings, SBERT. Core path — prioritize in your sprint.Embeddings map text (or images) into dense vectors so semantic similarity becomes geometry: cosine distance in vector space approximates related meaning. They power retrieval, clustering, and RAG front-ends.Contrast OpenAI-style embedding endpoints with open sentence-transformer models you can run locally. Understand normalization, dimensionality, and when to 
- Practice: Embed ten short phrases (two similar pairs, one opposite pair) using one API or local model.Compute cosine similarity between vectors; sanity-check that related phrases score higher.Change one word in a phrase and measure how much the vector shifts.Document embedding dimension and model version used — versioning matters for retrieval indexes.List one failure mode (polysemy, language mix) and a mit
- Code: `pip install chromadb sentence-transformers
import chromadb
c = chromadb.Client(); col = c.create_collection("m9")
col.add(documents=["RAG retrieves context before generation."], ids=["a"])
print(col.q`
