---
kind: category_supplement
title: Startup ideas
---

# Startup ideas — supplemental depth

### Startup idea catalog

### YC-Style Ideas — Complete Specifications

**1. AI Policy Copilot for Regulated Orgs**
- Problem: Teams drown in internal policy updates — compliance officers spend hours manually checking if new policies affect existing processes
- Solution: RAG over policy corpuses with citation-only answers — the AI only answers from retrieved policy text, never hallucinating
- Stack: P7 RAG + P8 MCP + P14 FastAPI
- Market: Large governance/compliance software TAM (multi-billion dollar segment)
- 2-week MVP: Upload PDFs → query API → Slack bot that answers policy questions with citations

**2. Meeting → Action-Item Router**
- Problem: Action items die in notes after calls — nobody follows up, commitments are forgotten
- Solution: Transcript → structured tasks → Jira/Asana via agents — automatically creates tickets with assignees and due dates
- Stack: P4 Agents + P5 tools + P13 n8n
- Market: Productivity/collaboration segment — every knowledge worker has this problem
- 2-week MVP: Webhook receives transcript → LLM extracts action items → creates Jira tickets → sends Slack summary

**3. Sales Email Personalizer (Bounded)**
- Problem: Generic outreach converts poorly — sales teams send the same template to everyone
- Solution: Template-safe LLM filling only approved slots from CRM fields — personalization without hallucination risk
- Stack: P2 prompting + P16 safety + P3 APIs
- Market: GTM tooling — crowded but always in demand, clear ROI
- 2-week MVP: CSV in (contact list + CRM fields) → CSV out (personalized emails) with moderation filter

**4. Onboarding Assistant for Internal Wikis**
- Problem: New hires cannot find canonical docs — they ask the same questions repeatedly, wasting senior engineer time
- Solution: Agent answers from verified sources with links — RAG over Confluence/Notion with source citations
- Stack: P7 RAG + P10 unified stack + P14 hosting
- Market: Enterprise internal tools — every company with 50+ employees has this problem
- 2-week MVP: Single Confluence space indexed → chat UI → answers with page links

**5. Agent Observability Starter Pack**
- Problem: No tracing for ad-hoc LLM scripts — developers can't debug why their agent failed
- Solution: Drop-in OpenTelemetry + LangSmith-style dashboard template — add 3 lines of code to get full observability
- Stack: P15 monitoring + P10 observability layer
- Market: Developer tooling for AI teams — every team building agents needs this
- 2-week MVP: One FastAPI service with exemplar traces, Grafana dashboard, and setup guide

**6. AI Legal Document Review**
- Problem: Legal review is slow and expensive — lawyers charge $300-500/hour to review contracts that follow predictable patterns
- Solution: RAG over legal corpus + structured clause extraction + risk flagging — AI identifies non-standard clauses and flags risks with citations to standard practice
- Stack: P7 RAG + P8 MCP + P14 FastAPI + P16 compliance
- Market: Legal tech / enterprise compliance — $25B+ legal tech market, AI disrupting document review first
- 2-week MVP: Upload contract → extract key clauses → flag deviations from standard → risk summary with citations

**7. AI Meeting Note-Taker**
- Problem: Meeting notes are inconsistent and incomplete — different people capture different things, action items are buried in prose
- Solution: Transcript → structured summary → action items → calendar integration — consistent, structured output every time
- Stack: P4 Agents + P5 tools + P13 automation
- Market: Productivity tools — $50B+ market, Otter.ai and Fireflies prove the demand
- 2-week MVP: Audio upload → Whisper transcription → LLM structured summary → action items → Slack post with calendar links

**8. AI Compliance Checker for Fintech**
- Problem: Fintech teams manually check transactions against compliance rules — slow, error-prone, expensive
- Solution: RAG over RBI/PCI-DSS rules + LLM risk scoring + explainable output — automated compliance checking with cited rule references
- Stack: P7 RAG + P8 MCP + P14 FastAPI + P16 security
- Market: Fintech compliance — regulatory fines run into billions, compliance automation has clear ROI
- 2-week MVP: Synthetic transactions → risk score (0-100) → cited compliance rule → human review queue for high-risk items

**9. AI Onboarding Assistant**
- Problem: New employees overwhelmed by tools and processes — HR spends weeks answering the same questions
- Solution: Agent answers from verified HR/IT docs with source links — RAG over onboarding documentation with citation-only responses
- Stack: P7 RAG + P10 unified stack + P14 hosting
- Market: Enterprise HR tech — $30B+ HCM market, onboarding automation is a clear use case
- 2-week MVP: Single knowledge base (HR handbook + IT setup guide) → chat UI → answers with document links
