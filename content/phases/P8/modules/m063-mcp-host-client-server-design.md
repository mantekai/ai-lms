---
journey_id: '8.2'
module_num: 63
phase_code: P8
title: 'MCP Host, Client & Server Design'
tools: 'mcp Python SDK, Claude Desktop'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 8.2 — MCP Host, Client & Server Design

**8.2 — MCP Host, Client & Server Design** [Core] | Tools: `mcp Python SDK, Claude Desktop`
- Learn: OverviewModule 63 (P8) — MCP Host, Client & Server Design. Tools focus: mcp Python SDK, Claude Desktop. Core path — prioritize in your sprint.Hosts (Claude Desktop, IDEs) spawn MCP clients; servers implement capabilities over stdio or HTTP+SSE. Lifecycle includes capability negotiation and stderr logging.
- Practice: Configure one MCP server in Claude Desktop JSON config.Verify the host lists tools/resources after restart.Inspect logs for handshake errors; fix path or command once.Document how you’d pin server version for teams.Threat-model: what data leaves the machine?
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `
