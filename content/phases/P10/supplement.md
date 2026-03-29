---
kind: phase_supplement
phase_code: P10
---

# Phase P10 — supplemental depth

### Unified agentic systems

### The 9-Layer Agentic AI Infrastructure Stack

**Layer 1 — User Layer:** The interface between humans and AI systems. Components: Developer Copilots (Claude Code, Cursor, GitHub Copilot), AI Assistants (Claude.ai, ChatGPT), Enterprise Chat Systems (Slack bots, Teams bots), Automation Workflows (n8n, Zapier). Humans initiate tasks here but agents increasingly execute them autonomously.

**Layer 2 — AI Agent Layer:** Where agents reason, plan, and take actions. Agent types: Research Agents (gather and synthesize information), Coding Agents (write and debug code), Data Agents (analyze and transform data), Automation Agents (execute workflows), DevOps Agents (manage infrastructure). Each agent type has specialized tools and memory.

**Layer 3 — Agent Orchestration:** Frameworks that coordinate multi-agent workflows. Components: Task Planners (decompose goals into subtasks), Workflow Engines (execute task graphs), Agent Collaboration (manage inter-agent communication). Tools: LangGraph (stateful graphs), CrewAI (role-based crews), AutoGen (conversational agents).

**Layer 4 — Model Layer:** Foundation models that power agent reasoning. Components: LLMs (Claude, GPT-4, Gemini), Reasoning Models (o1, o3 for complex multi-step reasoning), Embedding Models (text-embedding-3, SBERT for semantic search), Multimodal Models (GPT-4V, Gemini for vision/audio). Model selection affects capability, cost, and latency.

**Layer 5 — Context & Knowledge:** Where agents retrieve information to make informed decisions. Components: Vector Databases (Pinecone, Weaviate, Chroma for semantic search), Knowledge Graphs (Neo4j for relational knowledge), Document Stores (S3, GCS for raw documents), Search Systems (Elasticsearch, Azure AI Search for hybrid search).

**Layer 6 — Tooling Layer:** Where agents perform real actions. Components: APIs (REST/GraphQL endpoints), Databases (PostgreSQL, MongoDB for structured data), Git Repositories (GitHub, GitLab for code), File Systems (local and cloud storage), Cloud Services (AWS, GCP, Azure for compute and managed services).

**Layer 7 — Identity & Access:** Ensures agents access infrastructure safely. Sub-components: Cryptographic Identity (SPIFFE/SPIRE, Teleport Machine ID — agents have verifiable identities, not just API keys), Policy Enforcement (OPA, Cedar — what each agent is allowed to do), Infrastructure Access (short-lived credentials, just-in-time access), Runtime Enforcement (real-time policy checks on every action), Audit Logging (immutable record of every agent action).

**Layer 8 — Infrastructure Layer:** The physical and virtual compute that executes agent actions. Components: Kubernetes Clusters (container orchestration, GPU scheduling), Cloud Platforms (AWS, GCP, Azure), Databases (PostgreSQL, Redis, vector DBs), Storage Systems (S3, GCS, NFS), Developer Tooling (CI/CD, monitoring, secrets management).

**Layer 9 — Observability & Governance:** Ensures accountability for agent actions. Components: Agent Activity Logs (structured logs of every agent decision and action), Policy Enforcement (automated compliance checks), Access Analytics (who accessed what, when, and why). Tools: OpenTelemetry, LangSmith, Grafana, custom audit dashboards.

### Cross-Cutting Concerns

**Memory Layer (cross-cutting):** Memory spans all layers — session context at Layer 1, working memory at Layer 3, long-term knowledge at Layer 5. A unified memory architecture ensures agents have consistent access to relevant context regardless of which layer they operate in.

**Identity / Agent Identity (cross-cutting):** Agent identity must be enforced at every layer — from the user interface (which agent is responding?) to the infrastructure layer (which workload is making this API call?). Cryptographic identity replaces API keys as the trust anchor.

**Guardrails (cross-cutting):** Safety checks applied at multiple layers — input validation at Layer 1, output filtering at Layer 2, policy enforcement at Layer 7, compliance checks at Layer 9. Defense in depth: no single guardrail is sufficient; multiple overlapping checks are required.

### Curriculum visual map — block G

### Image 10: Coding vs Vibe-Coding vs No-Coding (Full Detail)

**Traditional Coding — Tools/Languages:** JavaScript, TypeScript, Python, Java, Go, C# | AWS SDK, Azure SDK | React, Next.js, FastAPI, Flask

**Vibe-Coding (AI-Assisted Coding):** You write logic with the help of AI — the AI generates code, fixes bugs, and builds functions based on natural language instructions. Key features: AI writes most of the code, human reviews + edits, very fast prototyping, lower effort higher speed, blends coding + prompting. Used for: AI agent development, API automation scripts, debugging & refactoring, MVPs & prototypes, data pipelines, integration scripts.

**No-Coding (Visual / Automation Tools):** Building workflows, automations, apps, or agents without writing code, using blocks, drag-and-drop tools, or prompt-based builders. Key features: zero coding required, drag-and-drop building, AI handles logic, great for everyday automation, fastest development speed. Used for: business automation, AI workflows, process automation, agent workflows without backend, internal tools, CRM/ERP integrations. Tools: Zapier, Make.com, n8n, Power Automate, ServiceNow Flow Designer, Webflow, Bubble.

### Image 11: Claude Code — Autonomous Coding Agent (Comic Strip)

**Scenario:** Developer is jogging in the park when Claude Code calls him via smartwatch. Conversation: "SQLite and Postgres are good, search which is better." → Claude searches → "Your app is simple so SQLite is a great start!" → Developer: "Use SQLite and implement the account creation backend flow." → Claude Code autonomously executes: implementing account creation with SQLite, building backend flow, creating tables (users, accounts), setting up authentication, backend build complete.

**Key Concepts:** Agentic coding — Claude Code works autonomously while the developer is away. Tool use — Claude searches for information, makes decisions, executes code. Hands-free development — developer gives high-level intent, agent handles implementation. Database selection reasoning — agent evaluates SQLite vs Postgres based on app complexity. End-to-end execution — from research → decision → implementation → completion notification.

### Image 12: What Claude Code Can Do

**12 Core Capabilities:**
1. Agentic Code Generation — AI writes code autonomously
2. Deep Context Reasoning — Understands full codebase context
3. Smart Debugging & Fixes — Identifies and resolves bugs
4. Native Git Operations — Built-in git workflow support
5. Sub-Agent Parallelism — Multiple agents working simultaneously
6. Auto Checkpoints & Recovery — Automatic save points and rollback
7. 200K+ Context Window — Massive context for large codebases
8. MCP Tool Integrations — Connect to external tools via MCP
9. CI/CD Automation Hooks — Integrate with deployment pipelines
10. Test Generation & Refactors — Auto-generate tests and refactor code
11. Task Planning & Execution — Break down and execute complex tasks
12. Run Anywhere (Local → Cloud) — Works on Mac, Windows, Linux, IDE, Terminal, Cloud, Slack

**Agentic Coding Architecture:** User Intent → Planner → Sub-Agents → Tools → Codebase → Tests → Deploy

**CLAUDE.md — Persistent Project Memory:** Stores architecture decisions, maintains task history, enables cross-session reasoning.

**5 Key Differentiators:** Terminal-Native Execution | Deep Reasoning + Deterministic Edits | Long-Horizon Agentic Workflows | Stateful Memory Across Sessions | Tool Use Without Prompt Chaining

**Feature Comparison (Claude Code vs Cursor vs Copilot vs ChatGPT):**
- Agentic execution: Strong ✓ | ✓ | ✓ | ✓
- Persistent memory: ✓ | Limited | — | —
- Multi-file refactors: ✓ | ✓ | No | ✓
- Parallel agents: ✓ | No | No | Partial
- Native terminal ops: ✓ | Partial | ✓ | No
- Context length: 200k+ | 200k+ | 200k+ | 200k+
- CI/CD automation: ✓ | ✓ | ✓ | —

**Engineering Use Cases:** Large-Scale Refactors | Greenfield System Builds | Legacy Codebase Navigation | Automated Code Review | Test Suite Generation | Stack-Wide PR Creation | Incident Hotfix Automation | Continuous Code Modernization

**Tagline:** "From autocomplete → to autonomous software execution." Mac · Windows · Linux · IDE · Terminal · Cloud · Slack

### Image 13: Claude Code Workflow Cheatsheet

**Getting Started:** Install Claude Code (Requires Node.js 18+): `curl -fsSL https://claude.ai/install.sh | bash` then `cd your_project && claude && /init`. Scans your codebase and creates a starter memory file.

**CLAUDE.md:** Claude's persistent memory about your project. Loaded automatically at the start of every session. WHAT: Tech stack, Directory map, Architecture. WHY: Purpose of each module, Design decisions. HOW: Build/test/lint commands, Workflows, Gotchas.

**Memory File Hierarchy:**
- `~/.claude/CLAUDE.md` → Global — all projects
- `~/CLAUDE.md` → Parent — monorepo root
- `./CLAUDE.md` → Project — shared on git
- `./frontend/CLAUDE.md` → Subfolder — scoped context

### Syllabus theme — day 19

**Day 19 — Build an Agentic AI System:** Building a multi-agent system (e.g., research + summarizer + notifier). Document architecture, workflows, and governance strategy. Exercise: Peer feedback — group review of all members' artifacts.
