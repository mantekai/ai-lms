<!-- Extracted from content/spec/agentiq_platform_spec.md — run: python3 scripts/extract_platform_docs.py — Manish.AI -->

## 11. AI CHATBOT — COURSE NAVIGATOR

- FR-BOT-01: Persistent chat widget available on all pages (bottom-right)
- FR-BOT-02: Natural language query to course/module recommendation
  - Example: "I want to learn how to build an agent that can browse the web" -> recommends M43 (Web Browsing Tools), M34 (Action Planning Loops), M46 (LangGraph)
- FR-BOT-03: Diagnostic quiz mode — chatbot asks 3-5 questions to assess current level, then recommends a learning path
- FR-BOT-04: Topic search — "What is RAG?" returns definition + links to relevant modules
- FR-BOT-05: "What should I learn next?" — personalized recommendation based on completed modules and level
- FR-BOT-06: Certification guidance — "I want to get AWS AI Practitioner certified" returns study plan mapped to platform modules
- FR-BOT-07: Hackathon prep — "I want to enter the LangGraph hackathon" returns prep path and quick-start template
- FR-BOT-08: Full context of learner's progress, level, and completed modules
- FR-BOT-09: Can answer questions about module content (RAG over all module content)
- FR-BOT-10: Conversation history persisted per user
- FR-BOT-11: Escalation — if chatbot cannot answer, creates a feedback ticket for agent review
- FR-BOT-12: Always labeled "AI Chatbot" — learner always knows they are talking to an AI
- FR-BOT-13: Chatbot can explain the difference between any two topics (e.g. "What is the difference between MCP and A2A?")
- FR-BOT-14: Chatbot can generate a custom study plan for a stated goal and timeline

---
