---
journey_id: '8.8'
module_num: 69
phase_code: P8
title: 'Claude Desktop + MCP Full Setup'
tools: 'Claude Desktop, mcp config'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 8.8 — Claude Desktop + MCP Full Setup

**8.8 — Claude Desktop + MCP Full Setup** [Core] | Tools: `Claude Desktop, mcp config`
- Learn: OverviewModule 69 (P8) — Claude Desktop + MCP Full Setup. Tools focus: Claude Desktop, mcp config. Core path — prioritize in your sprint.Claude Desktop + MCP is the fastest way to feel the protocol. JSON config, absolute paths, and env vars are the usual friction points.
- Practice: Install Claude Desktop; locate MCP config file for your OS.Add one community server with narrow permissions.Restart; validate tools appear and run a harmless call.Snapshot working config (redacted) for teammates.Write troubleshooting FAQ from errors you actually saw.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

#### P9 — A2A Protocol
**Purpose:** Agent-to-agent communication

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 70 | A2A Protocol Architecture | Core | A2A spec, Python |
| 71 | Agent Cards & Agent Identity | Core | A2A agent cards, JSON |
| 72 | Task Delegation & Result Artifacts | Core | A2A tasks, Python SDK |
| 73 | Multi-Agent Distributed Execution | Core | A2A, LangGraph, Docker |
| 74 | A2A vs MCP: When to Use Which | Core | Architecture diagrams, code |
