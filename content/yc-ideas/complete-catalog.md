<!--
  Nine YC-style ideas: items 1–5 from yc_ideas.csv + 6–9 from the source PRD. Manish.AI
-->

# YC-style startup ideas (complete set of nine)

## From `input/yc_ideas.csv` (ideas 1–5)

| Title | Problem | Solution | Stack | Market | MVP |
|-------|---------|----------|-------|--------|-----|
| AI policy copilot for regulated orgs | Teams drown in internal policy updates. | RAG over policy corpuses with citation-only answers. | P7 RAG, P8 MCP, P14 FastAPI | Large governance / compliance software TAM. | Upload PDFs → query API → Slack bot in 2 weeks. |
| Meeting → action-item router | Action items die in notes after calls. | Transcript → structured tasks → Jira/Asana via agents. | P4 Agents, P5 tools, P13 n8n | Productivity / collaboration. | Webhook + single integration + reviewer UI. |
| Sales email personalizer (bounded) | Generic outreach converts poorly. | Template-safe LLM that only fills approved slots from CRM fields. | P2 prompting, P16 safety, P3 APIs | GTM tooling. | CSV in → CSV out with moderation filter. |
| Onboarding assistant for internal wikis | New hires cannot find canonical docs. | Agent answers from verified sources with links. | P7 RAG, P10 unified stack, P14 hosting | Enterprise internal tools. | Single Confluence space + chat UI. |
| Agent observability starter pack | No tracing for ad-hoc LLM scripts. | Drop-in OpenTelemetry + LangSmith-style dashboard template. | P15 monitoring, P10 observability | Developer tooling for AI teams. | One FastAPI service with exemplar traces. |

---

## From the source PRD only (ideas 6–9) — expanded specifications

### 6. AI legal document review

- **Problem:** Legal review is slow and expensive; many contracts follow predictable patterns.
- **Solution:** RAG over a legal corpus + structured clause extraction + risk flagging; cite standard practice.
- **Stack:** P7 RAG + P8 MCP + P14 FastAPI + P16 compliance.
- **Market:** Legal tech / enterprise compliance.
- **2-week MVP:** Upload contract → extract key clauses → flag deviations → risk summary with citations.

### 7. AI meeting note-taker

- **Problem:** Notes are inconsistent; action items are buried in prose.
- **Solution:** Transcript → structured summary → action items → calendar integration.
- **Stack:** P4 Agents + P5 tools + P13 automation.
- **Market:** Productivity tools.
- **2-week MVP:** Audio upload → transcription → structured summary → action items → Slack post with calendar links.

### 8. AI compliance checker for fintech

- **Problem:** Manual checks against compliance rules are slow and error-prone.
- **Solution:** RAG over regulatory corpora + LLM risk scoring + explainable, cited output.
- **Stack:** P7 RAG + P8 MCP + P14 FastAPI + P16 security.
- **Market:** Fintech compliance.
- **2-week MVP:** Synthetic transactions → risk score (0–100) → cited rule → human review queue for high-risk items.

### 9. AI onboarding assistant (HR)

- **Problem:** New employees overwhelmed by tools and processes; HR repeats the same answers.
- **Solution:** Agent grounded in verified HR/IT docs with source links (citation-only).
- **Stack:** P7 RAG + P10 unified stack + P14 hosting.
- **Market:** Enterprise HR tech.
- **2-week MVP:** Single knowledge base (handbook + IT setup) → chat UI → answers with document links.

---

**Reconciliation:** The overview table in the source PRD claimed “9 YC ideas” while `yc_ideas.csv` contains **5** rows. All **nine** distinct concepts are listed above.
