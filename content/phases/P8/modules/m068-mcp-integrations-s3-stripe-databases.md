---
journey_id: '8.7'
module_num: 68
phase_code: P8
title: 'MCP Integrations: S3, Stripe, Databases'
tools: 'boto3, stripe, psycopg2 + MCP'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 8.7 — MCP Integrations: S3, Stripe, Databases

**8.7 — MCP Integrations: S3, Stripe, Databases** [Core] | Tools: `boto3, stripe, psycopg2 + MCP`
- Learn: OverviewModule 68 (P8) — MCP Integrations: S3, Stripe, Databases. Tools focus: boto3, stripe, psycopg2 + MCP. Core path — prioritize in your sprint.Integrations (S3, Stripe, Postgres) mean secrets, idempotency, and least privilege IAM. Never pass raw credentials through the model; server holds keys.
- Practice: Design IAM policy for S3 read-only prefix.Sketch Stripe flow with idempotency keys on writes.Use parameterized SQL only against Postgres tool.Log request metadata without card or PII payloads.Tabletop abuse: refund fraud prompt scenario.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `
