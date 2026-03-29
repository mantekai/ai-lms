---
journey_id: '9.2'
module_num: 71
phase_code: P9
title: 'Agent Cards & Agent Identity'
tools: 'A2A agent cards, JSON'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 9.2 — Agent Cards & Agent Identity

**9.2 — Agent Cards & Agent Identity** [Core] | Tools: `A2A agent cards, JSON`
- Learn: OverviewModule 71 (P9) — Agent Cards & Agent Identity. Tools focus: A2A agent cards, JSON. Core path — prioritize in your sprint.Agent cards advertise skills, endpoints, and trust metadata — similar in spirit to OpenAPI for services. Accurate cards reduce unsafe trial-and-error discovery.
- Practice: Draft a JSON agent card for a fake internal agent (no real URLs with secrets).Validate the card against examples from the spec repo.Peer review: can another teammate integrate without asking you?Add authentication section: mTLS vs bearer — justify choice.Version the card; document breaking change policy.
- Code: `# Pseudocode: agent card JSON for discovery (follow latest A2A spec)
AGENT_CARD = {
  "name": "research-agent",
  "skills": [{"id": "web.search", "description": "Search and summarize"}],
  "endpoints"`
