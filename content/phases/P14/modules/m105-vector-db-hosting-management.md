---
journey_id: '14.6'
module_num: 105
phase_code: P14
title: 'Vector DB Hosting & Management'
tools: 'Pinecone cloud, Weaviate cloud'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 14.6 — Vector DB Hosting & Management

**14.6 — Vector DB Hosting & Management** [Core] | Tools: `Pinecone cloud, Weaviate cloud`
- Learn: OverviewModule 105 (P14) — Vector DB Hosting & Management. Tools focus: Pinecone cloud, Weaviate cloud. Core path — prioritize in your sprint.Managed vector hosting offloads replicas, backups, and upgrades. Still define namespaces/tenants and backup RPO for customer indexes.
- Practice: Create serverless index; upsert test vectors.Test failover/read replica behaviour from docs.Estimate monthly $ for 1M vectors at your dimension.Define restore drill quarterly.Map IAM roles for ingest vs query workloads.
- Code: `pip install chromadb sentence-transformers
import chromadb
c = chromadb.Client(); col = c.create_collection("m105")
col.add(documents=["RAG retrieves context before generation."], ids=["a"])
print(col`
