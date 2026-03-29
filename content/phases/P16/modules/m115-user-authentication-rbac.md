---
journey_id: '16.3'
module_num: 115
phase_code: P16
title: 'User Authentication & RBAC'
tools: 'Auth0, Clerk, FastAPI security'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 16.3 — User Authentication & RBAC

**16.3 — User Authentication & RBAC** [Core] | Tools: `Auth0, Clerk, FastAPI security`
- Learn: OverviewModule 115 (P16) — User Authentication & RBAC. Tools focus: Auth0, Clerk, FastAPI security. Core path — prioritize in your sprint.User authentication (Auth0, Clerk) pairs with FastAPI OAuth2/JWT validation. Map identities to tenant IDs before RAG retrieval.
- Practice: Integrate OIDC login on a demo app.Enforce RBAC on one API route.Test token expiry and refresh behaviour.Log auth failures without leaking emails in public logs.Threat-model stolen refresh token.
- Code: `# Module 115 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 115, "topic": "User Authentication & RBAC", "sta`
