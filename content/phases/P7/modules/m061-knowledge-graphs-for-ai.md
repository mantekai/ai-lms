---
journey_id: '7.7'
module_num: 61
phase_code: P7
title: 'Knowledge Graphs for AI'
tools: 'Neo4j, NetworkX, graph RAG'
priority: 'OPTIONAL'
source: content/curriculum/section-6-modules.md
---

# 7.7 — Knowledge Graphs for AI

**7.7 — Knowledge Graphs for AI** [Optional] | Tools: `Neo4j, NetworkX, graph RAG`
- Learn: OverviewModule 61 (P7) — Knowledge Graphs for AI. Tools focus: Neo4j, NetworkX, graph RAG. Optional depth — revisit when you need this specialty.Knowledge graphs model entities and relations; GraphRAG combines graph traversal with LLM summarisation. Higher setup cost, strong for multi-hop reasoning over structured domains.
- Practice: Model ten triples from a tiny domain (manual OK).Run one multi-hop question requiring two edges.Compare graph answer vs vector-only answer on same question.List maintenance cost when facts change frequently.Identify one client vertical where graphs pay off.
- Code: `# Module 61 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 61, "topic": "Knowledge Graphs for AI", "status":`

#### P8 — MCP Protocol
**Purpose:** Model Context Protocol depth

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 62 | MCP Architecture & Core Concepts | Core | MCP spec, Python |
| 63 | MCP Host, Client & Server Design | Core | mcp Python SDK, Claude Desktop |
| 64 | MCP Transport Layer & Communication | Core | stdio, HTTP SSE transport |
| 65 | Secure File Access & Sampling in MCP | Core | MCP server Python |
| 66 | MCP Resources, Prompts & Tools | Core | MCP spec, tool definitions |
| 67 | Building a Custom MCP Server (Python) | Core | mcp, fastapi, Python |
| 68 | MCP Integrations: S3, Stripe, Databases | Core | boto3, stripe, psycopg2 + MCP |
| 69 | Claude Desktop + MCP Full Setup | Core | Claude Desktop, mcp config |
