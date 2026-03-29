---
journey_id: '8.6'
module_num: 67
phase_code: P8
title: 'Building a Custom MCP Server (Python)'
tools: 'mcp, fastapi, Python'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 8.6 — Building a Custom MCP Server (Python)

**8.6 — Building a Custom MCP Server (Python)** [Core] | Tools: `mcp, fastapi, Python`
- Learn: OverviewModule 67 (P8) — Building a Custom MCP Server (Python). Tools focus: mcp, fastapi, Python. Core path — prioritize in your sprint.Custom Python MCP servers often use FastMCP or official SDK. Package as CLI entrypoints; pin dependencies for reproducibility.
- Practice: Scaffold a server exposing two tools (read-only).Add unit tests mocking transport.Dockerfile optional: non-root user, read-only FS where possible.Publish README with install + config snippet.Peer review tool descriptions for ambiguity.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `
