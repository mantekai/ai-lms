---
journey_id: '10.2'
module_num: 76
phase_code: P10
title: 'Memory Layer Architecture (3-Tier)'
tools: 'mem0, Redis, PostgreSQL'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 10.2 — Memory Layer Architecture (3-Tier)

**10.2 — Memory Layer Architecture (3-Tier)** [Core] | Tools: `mem0, Redis, PostgreSQL`
- Learn: OverviewModule 76 (P10) — Memory Layer Architecture (3-Tier). Tools focus: mem0, Redis, PostgreSQL. Core path — prioritize in your sprint.Three-tier memory: hot session (Redis), warm structured (Postgres), cold semantic (vector). mem0 and similar libraries abstract policies but you still own PII and TTL law.
- Practice: Map one product’s memory to the three tiers with example keys.Define eviction when user deletes account (right to erasure).Prototype Redis TTL for session; Postgres row for preferences.Query vector tier with metadata filter by user_id.Estimate monthly cost at 10k MAU for your sketch.
- Code: `# Module 76 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 76, "topic": "Memory Layer Architecture (3-Tier)"`
