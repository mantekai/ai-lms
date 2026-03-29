---
kind: phase_supplement
phase_code: P18
---

# Phase P18 — supplemental depth

### Portfolio capstone specifications

### Capstone Projects — Complete Structured Specifications

**Capstone 1 — AI That Calls You**
- Type: Advanced | Time: 1–2 weeks
- Stack: LangGraph · Twilio Voice · FastAPI · Ollama · Redis · WebSocket · Ngrok
- What: Autonomous agent pauses at risky decisions, places outbound call, collects keypad input (1=approve, 2=reject), resumes with full trace logging
- Architecture: Task Trigger → Autonomous Execution (tools + memory, confidence scored) → Decision Gate (below-threshold opens voice flow) → Phone Call (Twilio TTS + keypad) → Resume (agent continues based on human input) → Audit (structured logs)
- Key skills demonstrated: LangGraph StateGraph with checkpointing, Redis checkpointer for state persistence, Twilio Voice API with TwiML, FastAPI webhook endpoints, HITL design patterns, state serialization and async resumption, audit trail logging
- Modules: M125, M46, M100, M76, M77, M81
- Deliverables: GitHub repo with README and architecture diagram, deployed FastAPI backend (Railway or Fly.io), 2-minute demo recording, LinkedIn post template

**Capstone 2 — AI Payment Risk Analyst**
- Type: Advanced | Time: 2–3 weeks
- Stack: FastAPI · Vector DB · RAG · Streamlit · Claude or GPT-4
- What: Ingest compliance docs into vector store, score synthetic transactions, produce explainable reports with cited clauses from source documents
- Architecture: Ingest (chunk + embed policy docs) → Retrieve (hybrid search for relevant rules) → Reason (LLM outputs risk score 0-100, summary, cited rule IDs) → Review UI (Streamlit dashboard for risk officers)
- Key skills demonstrated: RAG pipeline design, structured risk output with citations, explainable AI (every decision has a cited source), stakeholder-facing Streamlit UI, batch processing of synthetic transactions
- Modules: M126, M55, M59, M60, M100, M101
- Deliverables: GitHub repo, synthetic dataset + populated vector DB, public Streamlit demo, 1-page architecture document

**Capstone 3 — Local Perplexity Clone**
- Type: Intermediate | Time: 3–7 days
- Stack: Ollama · SearXNG · Docker · Streamlit · LangChain
- What: Self-hosted meta-search + local LLM synthesizes answers with source cards — zero paid API cost, fully private
- Architecture: Search (SearXNG returns ranked URLs + snippets) → Fetch (optional light fetch for top hits, respect robots.txt) → Synthesize (local Ollama model cites sources) → Chat UI (Streamlit with history and model picker)
- Key skills demonstrated: local-first stack design, privacy-preserving AI (no external API calls), Docker Compose orchestration, source citation in LLM outputs, LangChain search-to-synthesis pipeline
- Modules: M127, M1, M3, M95, M101, M103
- Deliverables: Docker Compose file (one command to run everything), GitHub repo with setup guide, 5-minute demo video

**Capstone 4 — AI Financial Risk Monitor**
- Type: Advanced | Time: 2–3 weeks
- Stack: LangGraph · n8n · Claude API · Pinecone · FastAPI · Twilio SMS · Redis Streams
- What: Autonomous agent monitoring transactions in real-time, detecting anomalies, alerting via SMS/Slack/log based on risk threshold
- Architecture: Data Ingestion (Redis Streams for real-time transaction feed) → Risk Scoring (Pinecone similarity search against known fraud patterns) → LLM Analysis (Claude/GPT-4 for explainable risk reasoning) → Escalation (SMS/Slack/log based on risk score threshold)
- Key skills demonstrated: fintech-specific agent design, AML/fraud detection patterns, Redis Streams for real-time data, Pinecone similarity search, multi-channel escalation, explainable risk output
- Modules: M46, M59, M95, M100, M76

### Syllabus theme — day 21

**Day 21 — Capstone: Project Setup & Architecture:** Define problem statement. Choose project type (chatbot, summarizer, recommender). Draft architecture diagram. Select tech stack. Team formation and role assignment. Setup GitHub repo, Azure Services, and documentation structure.

### Syllabus theme — day 22

**Day 22 — Capstone: Backend & AI Integration:** Setup backend (FastAPI). Integrate LLM APIs (OpenAI). Setup vector DB (FAISS/Pinecone). Implement embedding and retrieval logic. Test API endpoints.

### Syllabus theme — day 23

**Day 23 — Capstone: Frontend & Middleware:** Build UI (Streamlit). Connect frontend to backend. Add middleware (logging, error handling). Implement basic user interaction flow. UI testing and feedback loop.

### Syllabus theme — day 24

**Day 24 — Capstone: Deployment & Testing:** Containerize app with Docker. Deploy to cloud (Azure). Setup CI/CD pipeline. Perform unit, integration, and load testing. Finalize documentation.

### Syllabus theme — day 25

**Day 25 — Capstone: Demo & Documentation:** Prepare documentation (problem, architecture, demo, runbook, learnings). Conduct live demo in groups. Peer review and feedback. Submit final GitHub repo.


---
