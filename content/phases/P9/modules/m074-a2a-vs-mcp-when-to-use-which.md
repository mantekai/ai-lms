---
journey_id: '9.5'
module_num: 74
phase_code: P9
title: 'A2A vs MCP: When to Use Which'
tools: 'Architecture diagrams, code'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 9.5 — A2A vs MCP: When to Use Which

**9.5 — A2A vs MCP: When to Use Which** [Core] | Tools: `Architecture diagrams, code`
- Learn: OverviewModule 74 (P9) — A2A vs MCP: When to Use Which. Tools focus: Architecture diagrams, code. Core path — prioritize in your sprint.MCP excels at equipping a host with tools/resources; A2A excels at multi-agent tasking across trust boundaries. Many systems use both — draw boundaries deliberately.
- Practice: Draw a single architecture diagram placing MCP servers, your orchestrator, and A2A peers. Write a decision table: five criteria (latency, trust, UI surface, discoverability, state) × which protocol wins. Present a two-minute verbal summary to a peer and capture their questions as follow-ups.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `

#### P10 — Unified AI Systems
**Purpose:** Orchestration, identity, observability, 9-layer stack

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 75 | Orchestrator Design & Patterns | Core | LangGraph, custom Python |
| 76 | Memory Layer Architecture (3-Tier) | Core | mem0, Redis, PostgreSQL |
| 77 | Identity & Agent Security Layer | Core | Teleport, cryptographic identity |
| 78 | Observability: Logs, Traces, Metrics | Core | LangSmith, OpenTelemetry |
| 79 | Guardrails & Output Safety Systems | Core | NeMo Guardrails, custom filters |
| 80 | The 9-Layer Agentic AI Infrastructure Stack | Core | Architecture reference |
| 81 | RBAC & Securing AI Agents (Cryptographic ID) | Core | RBAC, Teleport, policy engines |
