---
journey_id: '7.5'
module_num: 59
phase_code: P7
title: 'Vector DBs: Pinecone, Weaviate, Chroma, FAISS'
tools: 'Pinecone, Weaviate, Chroma'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 7.5 — Vector DBs: Pinecone, Weaviate, Chroma, FAISS

**7.5 — Vector DBs: Pinecone, Weaviate, Chroma, FAISS** [Core] | Tools: `Pinecone, Weaviate, Chroma`
- Learn: OverviewModule 59 (P7) — Vector DBs: Pinecone, Weaviate, Chroma, FAISS. Tools focus: Pinecone, Weaviate, Chroma. Core path — prioritize in your sprint.Vector databases differ on hybrid search, filtering, multi-tenancy, and ops model (serverless vs self-host). FAISS is a library; Pinecone/Weaviate/Chroma are services or servers.
- Practice: Create a collection/index; upsert 1k vectors with metadata.Run metadata-filtered queries; verify performance.Try hybrid (BM25 + vector) if supported.Snapshot backup/restore procedure.Rough TCO: self-host vs managed for one workload.
- Code: `pip install chromadb sentence-transformers
import chromadb
c = chromadb.Client(); col = c.create_collection("m59")
col.add(documents=["RAG retrieves context before generation."], ids=["a"])
print(col.`
