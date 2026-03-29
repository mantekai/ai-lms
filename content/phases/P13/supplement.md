---
kind: phase_supplement
phase_code: P13
---

# Phase P13 — supplemental depth

### Workflow automation

**n8n + Ollama Local Integration:** Running n8n workflow automation with a local Ollama LLM as the AI backend — zero API cost. Configuration: n8n's HTTP Request node calls Ollama's OpenAI-compatible API at `http://localhost:11434/v1`. Use cases: local document processing, private data workflows, cost-free prototyping. Enables building production-grade AI automations without any external API dependencies.

**Production Automations — Real-World Patterns:**
- Email → AI Summary → Slack: Trigger on new email, extract content, summarize with LLM, post to Slack channel
- Lead → CRM → AI Scoring: New lead webhook, enrich with company data, score with LLM (1-10 fit score + reasoning), update CRM
- Invoice → AI Extraction → Accounting: PDF invoice received, extract line items with LLM, validate totals, push to accounting system
- Meeting → Transcript → Action Items → Jira: Meeting ends, transcription webhook, extract action items with LLM, create Jira tickets with assignees and due dates

**Azure Durable Functions & Logic Apps (Generic: Stateful Workflow Orchestration):** Stateful workflow orchestration for long-running processes. Durable Functions: serverless orchestration with built-in state persistence, fan-out/fan-in patterns, human approval workflows, and automatic retry. Logic Apps: visual workflow designer for enterprise integrations. Generic equivalent: LangGraph for agent workflows, Airflow for data pipelines, n8n for business automation.

**Phase 6: Workflow Automation**
- n8n self-host + first AI workflow
- n8n + Ollama local LLM integration ($0 API cost)
- Make.com, Zapier overview
- DAG management, event-based triggers, guardrails
- Production automations: Email→AI summary→Slack, Lead→CRM→AI scoring, Invoice→AI extraction→Accounting, Meeting→transcript→action items→Jira
- Certifications: n8n Official Certification (free), GreatLearning n8n Workflow Automation (free)

