<!--
  Capstones: input/capstones.csv + Capstone 4 from PRD (not in CSV). Manish.AI
-->

# Capstone projects

Platform modules **125–127** are the three capstones in `input/modules.csv`. A fourth capstone is specified only in the PRD (§19 / §48.3); it is included here so nothing is lost.

## Capstone 1 — AI That Calls You

| Field | Value |
|-------|-------|
| ID | c1 |
| Difficulty | Advanced |
| Time | 1–2 weeks |
| Stack | LangGraph; Twilio Voice; FastAPI; Ollama; Redis |
| GitHub hint | Search: langgraph + twilio + human-in-the-loop |

**Description:** Autonomous agent pauses at risky decisions, places an outbound call, collects keypad input, resumes with full trace logging.

**Why it matters:** Demonstrates orchestration, human-in-the-loop, telephony integration, and production-style state persistence.

**PRD architecture:** Task Trigger → Autonomous Execution → Decision Gate → Phone Call (Twilio TTS + keypad) → Resume → Audit.

**Modules:** M125, M46, M100, M76, M77, M81

**Deliverables:** GitHub repo + README + architecture diagram; deployed FastAPI backend; 2-minute demo; LinkedIn post template.

---

## Capstone 2 — AI Payment Risk Analyst

| Field | Value |
|-------|-------|
| ID | c2 |
| Difficulty | Advanced |
| Time | 2–3 weeks |
| Stack | FastAPI; Vector DB; RAG; Streamlit; Claude or GPT-4 |
| GitHub hint | Search: rag + fraud + compliance + fastapi |

**Description:** Ingest policy and compliance text into a vector store; score synthetic transactions; produce explainable reports with cited clauses.

**Why it matters:** RAG, structured risk output, stakeholder-facing UI — typical enterprise consulting deliverable.

**Modules:** M126, M55, M59, M60, M100, M101

**Deliverables:** Repo, synthetic dataset + populated vector DB, public Streamlit demo, one-page architecture doc.

---

## Capstone 3 — Local Perplexity-style search

| Field | Value |
|-------|-------|
| ID | c3 |
| Difficulty | Intermediate |
| Time | 3–7 days |
| Stack | Ollama; SearXNG; Docker; Streamlit; LangChain |
| GitHub hint | Search: ollama + searxng + langchain |

**Description:** Self-hosted meta-search plus local LLM to synthesize answers with source cards — no paid LLM required.

**Why it matters:** Privacy-preserving research tooling on your own hardware.

**Modules:** M127, M1, M3, M95, M101, M103

**Deliverables:** Docker Compose (one command), repo + setup guide, 5-minute demo video.

---

## Capstone 4 — AI Financial Risk Monitor *(PRD only — not in `capstones.csv`)*

| Field | Value |
|-------|-------|
| Difficulty | Advanced |
| Time | 2–3 weeks |
| Stack | LangGraph; n8n; Claude API; Pinecone; FastAPI; Twilio SMS; Redis Streams |

**Description:** Real-time transaction monitoring via Redis Streams; Pinecone similarity search against fraud patterns; LLM explainable risk reasoning; multi-channel escalation (SMS / Slack / log).

**Architecture:** Data ingestion (Redis Streams) → Risk scoring (Pinecone) → LLM analysis → Escalation by threshold.

**Modules:** M46, M59, M95, M100, M76 (plus Twilio SMS, Redis Streams per PRD §49.4).

**Skills:** Fintech-style AML/fraud patterns, streaming ingestion, similarity search, multi-channel alerts, explainable outputs.

*Sources: `input/capstones.csv` (c1–c3); PRD §19, §48.3, §49.4.*
