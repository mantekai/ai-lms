---
journey_id: '8.1'
module_num: 62
phase_code: P8
title: 'MCP Architecture & Core Concepts'
tools: 'MCP spec, Python'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 8.1 — MCP Architecture & Core Concepts

**8.1 — MCP Architecture & Core Concepts** [Core] | Tools: `MCP spec, Python`
- Learn: OverviewModule 62 (P8) — MCP Architecture & Core Concepts. Tools focus: MCP spec, Python. Core path — prioritize in your sprint.MCP standardises how hosts expose tools, resources, and prompts to models. It complements (not replaces) your HTTP APIs — think structured capability contracts.
- Practice: Read the MCP intro + spec outline; list three primitives.Contrast MCP with ad-hoc REST tools you already built.Sketch a host → client → server diagram for your desktop assistant.List security questions (filesystem, network) MCP must answer.Pick one sample server from official repos to run read-only.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `
