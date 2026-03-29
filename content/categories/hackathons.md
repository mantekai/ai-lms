---
kind: category_supplement
title: Hackathons
---

# Hackathons — supplemental depth

### Hackathon judging patterns

### Hackathon Winning Patterns — Full Detail

**Anthropic AI Safety Hackathon — Winning Pattern:** Strong eval metrics + crisp Streamlit/FastAPI demo. Winning teams combine: a well-defined safety or interpretability problem, measurable evaluation metrics (not just "it works"), a clean demo that non-technical judges can understand, and a short policy document explaining the safety implications. Prep: complete P2 (Prompting) + P16 (Security) modules first.

**Hugging Face Open-Source Sprint — Winning Pattern:** Clean model cards, reproducible training, eval tables. Top entries ship: a model card with full training details (dataset, hyperparameters, evaluation results), a reproducible training script (anyone can re-run it), an evaluation table comparing the submission to baselines, and a Gradio Space demo. Prep: P1 (Foundations) + P6 (Frameworks) + P7 (RAG).

**Devpost AI Hackathons — Winning Pattern:** Clear problem statement + live demo + public repo fork. Judges evaluate: does the problem statement make sense to a non-technical person? Is there a live demo that works during the judging period? Is the GitHub repo public and forkable? Does the README explain how to run it? Prep: P3 (LLM APIs) + P14 (Production deployment).

**LangGraph Build Challenge — Winning Pattern:** Traces, tests, and Dockerfile score highest. Projects that include: LangSmith traces showing the agent's reasoning, a test suite with at least 5 test cases, a Dockerfile that builds and runs without modification, and a clear README with architecture diagram consistently score in the top tier. Prep: P4 (Agents) + P6 (LangGraph depth).

**Google AI Hackathon (Gemini) — Winning Pattern:** Creative multimodal UX with latency under control. Winning projects use Gemini's multimodal capabilities in a genuinely creative way (not just text chat), keep response latency under 3 seconds for the demo, and have a polished UI. Judges are impressed by novel use of vision, audio, or long-context capabilities. Prep: P3 (Multimodal) + P14 (FastAPI/Streamlit).

**CrewAI Multi-Agent Challenge — Winning Pattern:** Clear agent boundaries and measurable task success. Winning crews have: clearly defined agent roles with non-overlapping responsibilities, measurable task success criteria (not just "the agent ran"), a demonstration of agents catching each other's errors, and clean task output artifacts. Prep: P4 (Agent collaboration) + P6 (CrewAI module).

**n8n Automation Hackathon — Winning Pattern:** Reusable templates published to marketplace. Top entries build workflows that other n8n users can immediately use — published as templates to the n8n marketplace. The template must work out of the box with minimal configuration, include clear documentation, and solve a real business problem. Prep: P13 (Automation modules).

### Multi-week sprint and hackathon format

### AGA Weeks 8-12

**Week 8 — Capstone (Module 13):** Architect a full-stack agentic AI solution for a client scenario. Document choices, trade-offs, fallback strategies, and deployment readiness. Present solution in business + technical terms.

**Weeks 9–12 — Hackathon:** Week 9: Preparation / buffer. Week 10 — Hackathon 1: Build an end-to-end solution to a business problem. Week 11 — Hackathon 2: Build an end-to-end solution to a business problem. Week 12 — Hackathon 3: Build an end-to-end solution to a business problem.

### Competition and hackathon notes

### Hackathon Full Details (from HTML extraction)

**Hugging Face Open-Source Sprint**
- Organiser: HuggingFace | Prize: Hub credits + visibility | Deadline: Quarterly sprints | Theme: Models, datasets, Spaces
- Description: 48-hour style sprints for Hub-ready artifacts.
- Prep modules: P1 foundations + P6 frameworks + P7 RAG
- Quick-start template: Gradio Space + dataset card + small model or adapter
- Past winners: Top entries ship clean cards, reproducible training, and eval tables.

**Devpost AI Hackathons**
- Organiser: Devpost | Prize: $10K–$100K depending on sponsor | Deadline: Rolling calendar | Theme: Sponsor-specific (Gemini, AWS, Azure)
- Description: Filter by AI; many enterprise-sponsored challenges.
- Prep modules: P3 LLM APIs + P14 deployment
- Quick-start template: MVP API + minimal UI + 90-second demo video
- Past winners: Clear problem statement + live demo + public repo fork win most tracks.

**LangGraph Build Challenge**
- Organiser: LangChain | Prize: Credits + ecosystem visibility | Deadline: Periodic announcements | Theme: Production agents
- Description: Focus on durable, deployable LangGraph apps.
- Prep modules: P4 Agents + P6 LangGraph depth
- Quick-start template: StateGraph + tool routing + LangSmith traces
- Past winners: Projects with traces, tests, and Dockerfile score highest.

**Google AI Hackathon (Gemini)**
- Organiser: Google | Prize: Large pooled prizes (see site) | Deadline: Annual / regional | Theme: Gemini API apps
- Description: Build on Gemini with mentor office hours.
- Prep modules: P3 multimodal + P14 FastAPI/Streamlit
- Quick-start template: Gemini tool use + OAuth + hosted demo
- Past winners: Creative multimodal UX with latency under control.

**CrewAI Multi-Agent Challenge**
- Organiser: CrewAI | Prize: Cash + enterprise intros | Deadline: Periodic | Theme: Multi-agent crews
- Description: Enterprise-flavored multi-agent builds.
- Prep modules: P4 collaboration + P6 CrewAI module
- Quick-start template: Defined roles + sequential process + task outputs
- Past winners: Clear agent boundaries and measurable task success.

**n8n Automation Hackathon**
- Organiser: n8n | Prize: ~$5K (see rules) | Deadline: Quarterly | Theme: Workflow + AI nodes
- Description: AI-powered automations in n8n.
- Prep modules: P13 automation modules
- Quick-start template: Webhook → LLM → CRM/Slack with error branch
- Past winners: Reusable templates published to marketplace trend well.
