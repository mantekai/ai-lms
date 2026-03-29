---
journey_id: '9.1'
module_num: 70
phase_code: P9
title: 'A2A Protocol Architecture'
tools: 'A2A spec, Python'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 9.1 — A2A Protocol Architecture

**9.1 — A2A Protocol Architecture** [Core] | Tools: `A2A spec, Python`
- Learn: OverviewModule 70 (P9) — A2A Protocol Architecture. Tools focus: A2A spec, Python. Core path — prioritize in your sprint.Google’s Agent2Agent (A2A) protocol focuses on discoverable agents, task messages, and artifacts — complementary to MCP’s tool/resource model. Study how remote agents authenticate and negotiate capabilities.
- Practice: Read A2A intro materials; contrast goals with MCP in one paragraph.List actors: client, remote agent, registry (if used).Sketch sequence diagram for a task submission and artifact return.Identify transport and auth questions unanswered by skimming docs.Note version skew risks between agent implementations.
- Code: `# Pseudocode: agent card JSON for discovery (follow latest A2A spec)
AGENT_CARD = {
  "name": "research-agent",
  "skills": [{"id": "web.search", "description": "Search and summarize"}],
  "endpoints"`
