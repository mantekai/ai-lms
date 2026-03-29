---
journey_id: '8.5'
module_num: 66
phase_code: P8
title: 'MCP Resources, Prompts & Tools'
tools: 'MCP spec, tool definitions'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 8.5 — MCP Resources, Prompts & Tools

**8.5 — MCP Resources, Prompts & Tools** [Core] | Tools: `MCP spec, tool definitions`
- Learn: OverviewModule 66 (P8) — MCP Resources, Prompts & Tools. Tools focus: MCP spec, tool definitions. Core path — prioritize in your sprint.Resources expose data; prompts are templates; tools execute actions. Naming and descriptions feed model routing quality.
- Practice: Implement one resource URI pattern; fetch via client.Register a tool with rich description + JSON schema.Add a prompt template with variables; render from host.Test model’s ability to pick correct tool among three.Version schemas when breaking changes occur.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `
