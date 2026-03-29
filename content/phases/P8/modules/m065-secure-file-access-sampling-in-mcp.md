---
journey_id: '8.4'
module_num: 65
phase_code: P8
title: 'Secure File Access & Sampling in MCP'
tools: 'MCP server Python'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 8.4 — Secure File Access & Sampling in MCP

**8.4 — Secure File Access & Sampling in MCP** [Core] | Tools: `MCP server Python`
- Learn: OverviewModule 65 (P8) — Secure File Access & Sampling in MCP. Tools focus: MCP server Python. Core path — prioritize in your sprint.Sampling and filesystem rules gate model access to local resources. Least privilege defaults beat “allow all” demos.
- Practice: Enable directory allowlist in a sample server config.Attempt disallowed path access; confirm denial.Review sampling callbacks — when human approval triggers.Document audit log fields you would ship.Red-team prompt injection via malicious file contents.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `
