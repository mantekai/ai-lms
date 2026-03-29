---
journey_id: '6.10'
module_num: 54
phase_code: P6
title: 'LLM Management: W&B, Arize AI'
tools: 'Weights & Biases, Arize'
priority: 'OPTIONAL'
source: content/curriculum/section-6-modules.md
---

# 6.10 — LLM Management: W&B, Arize AI

**6.10 — LLM Management: W&B, Arize AI** [Optional] | Tools: `Weights & Biases, Arize`
- Learn: OverviewModule 54 (P6) — LLM Management: W&B, Arize AI. Tools focus: Weights & Biases, Arize. Optional depth — revisit when you need this specialty.W&B tracks experiments; Arize/Phoenix targets LLM observability and embeddings drift. Pick tooling based on whether you optimise training or production inference.
- Practice: Log a small training or finetune run to W&B with hyperparameters.Create one dashboard chart you would show a client.Send a batch of prompts through Phoenix (or read tutorial); inspect traces.Define one drift metric for embeddings in production.Document cost of SaaS observability at your expected volume.
- Code: `# Module 54 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 54, "topic": "LLM Management: W&B, Arize AI", "st`

#### P7 — RAG & Knowledge
**Purpose:** Embeddings, chunking, vector DBs, hybrid search

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 55 | RAG Architecture & Pipeline Design | Core | LangChain, LlamaIndex |
| 56 | Embedding Models & Semantic Search | Core | OpenAI, Cohere, SBERT |
| 57 | Document Chunking Strategies | Core | LangChain splitters, custom logic |
| 58 | Custom Data Loaders & Document Ingestion | Core | LangChain loaders, Unstructured |
| 59 | Vector DBs: Pinecone, Weaviate, Chroma, FAISS | Core | Pinecone, Weaviate, Chroma |
| 60 | Query Refinement & Hybrid Search | Core | BM25, dense retrieval, rerankers |
| 61 | Knowledge Graphs for AI | Opt | Neo4j, NetworkX, graph RAG |
