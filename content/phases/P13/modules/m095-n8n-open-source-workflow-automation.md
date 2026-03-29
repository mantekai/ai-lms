---
journey_id: '13.1'
module_num: 95
phase_code: P13
title: 'n8n — Open Source Workflow Automation'
tools: 'n8n, Docker, webhooks'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 13.1 — n8n — Open Source Workflow Automation

**13.1 — n8n — Open Source Workflow Automation** [Core] | Tools: `n8n, Docker, webhooks`
- Learn: OverviewModule 95 (P13) — n8n — Open Source Workflow Automation. Tools focus: n8n, Docker, webhooks. Core path — prioritize in your sprint.n8n is fair-code workflow automation with self-host option. Nodes connect triggers, HTTP, databases, and AI steps — version flows as JSON in git when possible.
- Practice: Run n8n via Docker; create admin user.Build webhook → function → HTTP request flow.Add error workflow or retry policy.Export workflow JSON to git.Secrets: use credential store; never hardcode in nodes.
- Code: `docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
# Open http://localhost:5678 — build a webhook → HTTP Request → LLM flow`
