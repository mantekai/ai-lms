---
journey_id: '8.3'
module_num: 64
phase_code: P8
title: 'MCP Transport Layer & Communication'
tools: 'stdio, HTTP SSE transport'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 8.3 — MCP Transport Layer & Communication

**8.3 — MCP Transport Layer & Communication** [Core] | Tools: `stdio, HTTP SSE transport`
- Learn: OverviewModule 64 (P8) — MCP Transport Layer & Communication. Tools focus: stdio, HTTP SSE transport. Core path — prioritize in your sprint.Transports carry JSON-RPC messages: stdio for local trust boundaries; HTTP+SSE for remote servers. Latency and auth differ materially.
- Practice: Run a stdio server; trace one request/response with debug logging.Read transport section of spec; note framing rules.Compare stdio vs remote transport for a corporate locked-down laptop.Add TLS and auth sketch for remote deployment.List failure modes: partial frames, timeouts, proxy interference.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `
