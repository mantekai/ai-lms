---
kind: phase_supplement
phase_code: P4
---

# Phase P4 — supplemental depth

### AI agents

### Agent Fundamentals

**Autonomous vs Semi-Autonomous Agents:** Autonomous agents operate without human intervention — they plan, execute, and complete tasks independently. Semi-autonomous agents include human checkpoints at defined decision points (e.g., before irreversible actions, when confidence is below threshold). Most production systems are semi-autonomous for safety and compliance reasons.

**The Agent Loop:** The fundamental execution cycle of any AI agent: Perceive (gather inputs from environment/tools) → Think (reason about current state and next action) → Act (execute tool call or produce output) → Observe (process tool results) → Repeat until goal achieved or stop condition met. Understanding this loop is the foundation of all agent architectures.

### Agent Architectures

**Hierarchical Agents — Supervisor + Worker Pattern:** A supervisor agent decomposes a high-level goal into subtasks and delegates each to specialized worker agents. The supervisor monitors progress, handles failures, and synthesizes results. Used in complex multi-step workflows where different subtasks require different expertise. Example: supervisor delegates research to a web agent, writing to a content agent, and fact-checking to a validation agent.

**Sequential Pattern:** Agents execute in a fixed sequence where each agent's output becomes the next agent's input. Simple and predictable. Example: new employee onboarding crew — HR agent collects info → IT agent provisions accounts → Manager agent sends welcome message. Best for linear workflows with clear hand-off points.

**Reflection / Round Robin Group Chat:** Multiple agents take turns contributing to a shared task. Example: writer agent produces draft → critic agent provides feedback → writer agent revises → critic agent approves. The round-robin continues until quality threshold is met. Used for content creation, code review, and adversarial validation.

**Event-Driven Agents vs Always-On Workflows:** Event-driven agents wake up in response to triggers (webhook, schedule, queue message) and go dormant after completing their task. Always-on workflows run continuously, monitoring for conditions. Event-driven is more cost-efficient; always-on is better for real-time monitoring use cases.

### Planning & Decision Making

**Confidence-Based Branching:** Agents evaluate their confidence in a decision before proceeding. If confidence falls below a threshold, the agent takes a fallback action: escalate to human, request clarification, or choose a safer default. Implementation: the model outputs a confidence score alongside its decision; the orchestrator routes based on the score. Critical for production safety.

**A Decision Calculus for Multi-Agent Design:** A framework for deciding when to use multi-agent systems vs single agents. Factors: task complexity (can one agent handle it?), parallelism (can subtasks run concurrently?), specialization (do different subtasks need different expertise?), cost (multi-agent adds overhead), reliability (more agents = more failure points). Use multi-agent when the benefits outweigh the coordination cost.

### Multi-Agent Collaboration

**Role Assignment, Message Passing, Shared State:** In multi-agent systems, each agent has a defined role (researcher, writer, validator). Agents communicate via structured messages (not free-form chat). Shared state (a common data structure) allows agents to read each other's outputs without direct communication. LangGraph implements shared state as a typed dictionary passed through the graph.

**Adaptive RAG:** A multi-agent RAG pattern where a router agent decides which retrieval strategy to use based on the query type. Simple factual queries → direct vector search. Complex analytical queries → hybrid search + reranking. Ambiguous queries → query expansion first. The router improves retrieval quality by matching strategy to query characteristics.

### Human-in-the-Loop (HITL)

**HITL Design Patterns:** The principle that AI agents should operate independently for routine decisions but pause and involve humans at true decision points — irreversible actions, low-confidence situations, high-stakes outputs, or compliance-required approvals. Good HITL design minimizes human interruptions while maintaining safety. The agent serializes its state before pausing so it can resume exactly where it left off.

**Callback Architecture:** The technical implementation of HITL: (1) Agent reaches a decision point and serializes its full state to persistent storage (Redis, database). (2) Agent sends notification to human via preferred channel (Slack, email, SMS, phone call). (3) Human reviews and responds via a callback endpoint. (4) Agent deserializes state and resumes execution with the human's input. This pattern is demonstrated in Capstone 1 (AI That Calls You).

**Twilio Voice Integration:** Using Twilio's Voice API to place outbound phone calls from an AI agent. The agent generates TwiML (Twilio Markup Language) to define the call script — text-to-speech message, keypad input collection (Gather verb), and webhook callback URL. When the human presses 1 (approve) or 2 (reject), Twilio sends the keypad input to the FastAPI webhook, which resumes the agent. Used in Capstone 1.

**State Serialization & Async Resumption:** The technical challenge of pausing an agent mid-execution and resuming it later (potentially hours later after a human responds). Solution: LangGraph's checkpointing system serializes the full graph state (current node, all state variables, tool results so far) to a persistent store (SQLite, Redis, PostgreSQL). On resumption, the graph loads the checkpoint and continues from the exact pause point.

### Curriculum visual map — block D

### Image 5: LLM vs Generative AI vs AI Agents vs Agentic AI — 7-Step Pipelines

**LLM (Large Language Model) — 7 Steps:**
1. Choose Cloud Provider — Select infrastructure
2. Tokenization & Embedding — Convert text to numeric representations
3. Context Understanding — Process input context
4. Neural Inference — Apply transformer layers, use learned weights
5. Token Prediction — Predict next tokens
6. Output Construction — Build the response
7. Response Delivery — Return output to user

**Generative AI — 7 Steps:**
1. Input Collection — Gather input data
2. Feature Mapping — Map input features
3. Pattern Learning — Leverage trained models, identify latent space
4. Content Generation — Decode latent features, generate new content
5. Refinement & Filtering — Quality control
6. Output Rendering — Format final output
7. User Feedback — Collect feedback for improvement

**AI Agents — 7 Steps:**
1. Task Triggered — Receive a task
2. Intent Detection — Understand task type, classify intent
3. Rule/Model Execution — Apply rules or models
4. Tool or API Call — Interact with tools, retrieve information
5. Result Generation — Produce results
6. Response Handling — Process and format response
7. Task Logging — Log task execution

**Agentic AI — 7 Steps:**
1. Goal Initiation — Receive or define objective, understand context
2. Situation Awareness — Analyze environment, identify constraints
3. Reasoning & Planning — Create action plan, prioritize steps
4. Autonomous Execution — Act without instruction, call tools or sub-agents
5. Real-time Monitoring — Track progress, detect triggers
6. Strategy Adjustment — Adapt to changes, optimize approach
7. Outcome Evaluation — Assess results, decide next steps

### Image 6: Securing AI Agents in Infrastructure

**Traditional Access Model:** Human → Role → Infrastructure. Human-centric identities, static permissions (RBAC), perimeter-based security.

**Agentic AI Model (Current Problem):** AI Agent → APIs → Infrastructure. Risks: no unique agent identity, privilege escalation potential, undetected rogue behavior.

**Teleport's New Agentic Identity Framework (Solution):** Agent → Cryptographic Identity → Runtime Access → Auditable Actions. Key principles: machine-attestable identity, dynamic context-aware access, real-time policy enforcement.

**Key Takeaways:**
- Traditional RBAC is insufficient for AI agents — agents aren't humans
- Agents need cryptographic identity (not just API keys)
- Runtime access must be dynamic and context-aware, not static
- All agent actions must be auditable with full logging
- Real-time policy enforcement replaces perimeter-based security

### Image 7: 12 AI Skills — Skill 1: AI Agents

**AI Agents:** Autonomous systems that plan, act, and complete workflows without human help. When to use: automate research, scheduling, content creation, or customer engagement. Tools: CrewAI, LangChain, ChatGPT, OpenAI Agents, AutoGen.

**Agentic Architect — Session Plan:** 12-week instructor-led course (Saturdays & Sundays, 9:00 AM – 1:00 PM). Focus: Generative AI + Agentic AI on Azure.


### Week 1 — Python Fundamentals for GenAI and Agentic AI


### Week 5 — Multi-Agent Collaboration & Model Optimization


**Module 7 — Multi-Agent Collaboration & Agent Evaluation:** Multi-agent design patterns: Sequential pattern (new employee onboarding Crew), Supervisor pattern (sales analyst + market researcher), Reflection / Round Robin Group Chat (advertising copy creation with writer + critic agent). A decision calculus for multi-agent design. Workflow Orchestration using Azure Durable Functions and Logic Apps: state machine logic, coordinating decision points, retries, branching, event-driven triggers. Implementing generative AI workflows with multi-agent systems: Adaptive RAG. Evaluating agents: measuring tool call accuracy and goal accuracy. Safe interaction design and fallback routing. Observability basics: integrating Azure Monitor and Application Insights for agent workflows.


**Module 9 — Domain & Platform Awareness:** Overview of how agentic patterns apply in enterprise stacks. Illustrative patterns from enterprise applications such as Salesforce & ServiceNow. Awareness of domain challenges: regulated data, legacy systems.


### Syllabus theme — day 13

**Day 13 — Foundations of Agentic AI:** What is Agentic AI? How it differs from traditional AI and GenAI. Core capabilities: Perceive, Reason, Act, Learn. Single-agent vs. Multi-agent systems. Real-world applications: healthcare, mobility, customer service.

- **Twilio Integration Setup** — outbound calls with TTS, keypad response capture (1=approve, 2=reject). Complete Implementation: agent analyzes GitHub repo → hits ambiguous decision → serializes state → calls phone → resumes based on keypad input. Demonstrates: autonomous operation, HITL at decision points, state serialization, async resumption.
- **Constitutional AI (CAI)** — deep dive into Anthropic's training methodology (not a standalone module)
- **Claude Code 4-Layer Architecture** — CLAUDE.md → Skills → Hooks → Sub-Agents as a system design
- **Cowork Mode & Desktop Plugins** — document creation skills, plugin ecosystem, Email Copilot
- **Claude.ai Projects** — persistent context feature for Pro/Team/Enterprise users
- **Chrome Automation** — Claude in Chrome extension for browser automation
- **Scheduled Tasks & Dispatch** — cron-based AI workflows, task routing to specialized agents
- **HITL Callback Architecture** — state serialization + async notification + resume pattern
- **Twilio Voice Integration** — phone-based human-in-the-loop for agent decision points
- **Skill Auto-Activation Patterns** — description field engineering for reliable skill triggering
- **Context Injection Techniques** — template variables, hook-based injection, skill-level loading
- **Batch API** — 10K requests/batch at 50% cost reduction (not covered in current modules)
- **Plugin Development** — building custom .plugin bundles (MCPs + skills + commands)


**Phase 1: AI Concepts & Terminology**
- LLM vs GenAI vs AI Agents vs Agentic AI — 4-stage progression with 7-step pipelines each
- Top 40 AI Terms with precise definitions (AGI, tokenization, embedding, context window, hallucination, inference, parameters, quantization, temperature, RAG, CoT, fine-tuning, RLHF, LoRA, PEFT, MCP, A2A, GGUF, vector database, GPU, transformer, vibe coding, AI agent)
- Certifications: Google AI Essentials (free), LinkedIn Career Essentials in GenAI (free)


**Phase 3: AI Agents & Frameworks**
- ReAct Agent from scratch with LangGraph — StateGraph, conditional edges, tool binding
- CrewAI Multi-Agent Team — researcher + writer with sequential process
- Agent architectures: ReAct, CAMEL, Hierarchical, Self-reflecting
- Memory architecture emphasis: "agent with good memory + weak model beats brilliant model with no memory"
- Certifications: HuggingFace AI Agents Course (free), DeepLearning.AI AI Agents in LangGraph (free), IBM Agentic AI with LangGraph/CrewAI/AutoGen (paid)


**Phase 7: Production & Security**
- 9-Layer Agentic AI Infrastructure Stack (L1–L9)
- Prompt injection protection — regex-based detection patterns + XML wrapping defense
- AI agent identity, cryptographic access
- Observability, RBAC
- Agent security architecture
- Certifications: ISACA AI Governance Professional (paid), AWS AI Practitioner Security Module (paid)


- What it is:** Fully self-running workflows managed by AI agents and triggers
- When to use it:** For handling business operations or content pipelines with zer


- Flow:** AI Agent → APIs → Infrastructure
- Risks & Limitations:**


- L1 CLAUDE.md → L2 Skills → L3 Hooks → L4 Agents
- Key principle: Smaller context = higher accuracy; Memory = consistency; Hooks =


### Day 13 — Foundations of Agentic AI (Week 5 continued)


- Exercise: Create comparison table (Traditional AI vs GenAI vs Agentic AI); desig


- Client-Agent → MCP Protocol → MCP Servers (1:1 client-server mapping)
- Structured tool access; secure & governed API interaction
- HOST contains: MCP Client 1→Server 1, Client 2→Server 2, Client 3→Server 3
- Transport Layer: bidirectional communication between client and server
- Client Agent ↔ A2A Agents ↔ 3–4 Remote Agents
- Communication: Task Requests & Result Artifacts
- Distributed execution; task delegation across agents
- User → Orchestrator → Agents Layer (A2A) → MCP Clients → MCP Servers → Tools & S
- Memory layer (left side); Identity (Agent/Identity) layer (right side)
- Observability (Logs/Traces) and Guardrails layers wrap the full stack
- Key Insight: MCP = tools, A2A = agents, Together = real AI systems
- Shift: Apps → Agents → Multi-Agent → AI Infrastructure
- Design Principle: Communication layer + Production code


### IMAGE 3 — Agentic AI Roadmap 2026 (Full Curriculum Map)


- Languages: Python, JavaScript, TypeScript, Shell/Bash
- Scripting & Automation: API Requests (HTTP/JSON), File Handling, Async Programmi
- Prompting Concepts: Prompt Engineering, Context Management, Chain-of-Thought Pro
- Advanced Prompting: Self-Critique & Retry Loops, Reflexion Looping, Task Plannin
- What are AI Agents? Autonomous vs. Semi-Autonomous Agents
- Model Context Protocol (MCP), A2A Protocol (Agent-to-Agent)
- Goal Decomposition, Task Planning Algorithms, Decision-Making Policies
- Action Planning Loops, Multi-Agent Collaboration, Self-Reflection / Feedback Loo
- OpenAI (GPT-4, GPT-4o), Claude, Gemini, Mistral
- Open Source LLMs: LLaMA, DeepSeek, Falcon
- API Authentication, Rate Limiting, Toolformer / Function Calling
- Tool Invocation & Output Parsing, Prompt Chaining via APIs
- Tool Use System, Memory Integration, External API Calling
- File Reader/Writer Tools, Python Execution Tools, Search & Retrieval Tools
- Calculator & Code Interpreter, Web Browsing Tools
- LangChain, AutoGen, CrewAI, Flowise, AgentOps, Haystack
- Semantic Kernel, Superagent, LlamaIndex
- n8n, Make.com, Zapier, LangGraph
- Short-Term Memory, Long-Term Memory, Episodic Memory, Vector Stores
- RAG (Retrieval-Augmented Generation), Embedding Models, Custom Data Loaders
- Document Indexing, Query Refinement, Hybrid Search
- LangChain RAG, LlamaIndex RAG
- API Deployment, Serverless Functions, FastAPI / Streamlit / Gradio
- Docker, Kubernetes, Vector DB Hosting
- Agent Hosting Services: Replit, Modal, etc.
- Agent Evaluation Metrics, Human-in-the-Loop Feedback, LangSmith
- Logging / Tracing, Auto-Evaluation Loops, OpenTelemetry
- Prometheus / Grafana, Custom Dashboards
- Prompt Injection Protection, API Key Management, User Authentication
- Role-Based Access Control (RBAC), Output Filtering, Red Team Testing


### IMAGE 8 — Securing AI Agents in Infrastructure


- Agentic AI Model risks: No unique agent identity, Privilege escalation potential
- Teleport Agentic Identity Framework: Machine-attestable identity, Dynamic contex
- Key components: Cryptographic Identity, Runtime Access, Auditable Actions


### LLM vs Generative AI vs AI Agents vs Agentic AI


- LLM: Text prediction, no autonomy, no planning
- Generative AI: Content creation, no autonomy, user feedback loop
- AI Agents: Task execution, reactive autonomy, tool use, task logging
- Agentic AI: Goal-driven autonomy, full reasoning & planning, sub-agent delegatio


- Purpose:** Humans initiate tasks, but agents increasingly execute them autonomou


- Purpose:** Agents reason, plan, and take actions across infrastructure


- Purpose:** Orchestration frameworks coordinate multi-agent workflows


- Purpose:** Agents retrieve context to make informed decisions


- Purpose:** Agents perform real actions through tools and integrations


- Purpose:** Secure identity ensures agents access infrastructure safely and trans


- Purpose:** Infrastructure executes actions initiated by AI agents


- Core Capabilities (from whiteboard): Agentic Code Generation, Deep Context Reaso
- Agentic Coding Architecture: User Intent → Planner → Sub-Agents → Tools → Codeba


- Architecture: Claude agent loop + state persistence + Twilio Voice API + Ngrok w


- Central coordinator for multi-agent workflows
- Patterns: router, supervisor, hierarchical, peer-to-peer
- Tools: LangGraph, custom Python orchestrators
- Tier 1: Session context (temporary, within conversation)
- Tier 2: Working memory (cross-session, task-specific)
- Tier 3: Long-term memory (persistent knowledge base)
- Tools: mem0, Redis, PostgreSQL
- Cryptographic identity for agents (not just API keys)
- Real-time policy enforcement replacing perimeter security
- Tools: Teleport's agentic identity framework
- Structured logging for agent actions
- Distributed tracing across multi-agent workflows
- Metrics: latency, cost, success rates, token usage
- Tools: LangSmith, OpenTelemetry
- Input validation, output filtering, content safety
- NeMo Guardrails for programmable safety rails
- Custom filter chains for domain-specific constraints
- Layer 1: User Layer (copilots, assistants, chat, automation)
- Layer 2: AI Agent Layer (research, coding, data, automation, DevOps agents)
- Layer 3: Agent Orchestration (task planners, workflow engines, collaboration)
- Layer 4: Model Layer (LLMs, reasoning models, embedding models, multimodal)
- Layer 5: Context & Knowledge (vector DBs, knowledge graphs, document stores, sea
- Layer 6: Tooling Layer (APIs, databases, git repos, file systems, cloud services
- Layer 7: Identity & Access (cryptographic identity, policy enforcement, infrastr
- Layer 8: Infrastructure Layer (Kubernetes, cloud platforms, databases, storage,
- Layer 9: Observability & Governance (agent activity logs, policy enforcement, ac
- Traditional RBAC insufficient for AI agents — agents aren't humans
- Agents need cryptographic identity, not just API keys
- Tools: RBAC, Teleport, policy engines


- AI-assisted development: steer natural-language intent, model drafts code
- You still own review, tests, and security
- Spectrum: Traditional Coding → Vibe Coding → No-Code
- CLAUDE.md = persistent project memory loaded every session
- Contains: tech stack, directory map, architecture, build/test/lint commands, got
- Memory hierarchy: ~/.claude/CLAUDE.md (global) → ~/CLAUDE.md (parent) → ./CLAUDE
- Keep each file under 200 lines; subfolder files append context
- Daily workflow: cd project → claude → Plan Mode → describe intent → Auto Accept
- Project skill: `.claude/skills/<name>/SKILL.md`; Personal: `~/.claude/skills/<na
- Hooks = deterministic callbacks: PreToolUse, PostToolUse, Notification
- Exit codes: 0 → allow, 2 → block
- Memory system: Session Context (temporary) → Skills (playbooks) → CLAUDE.md (lon
- Key: "Don't use Claude like ChatGPT — Design it like a system"
- Full directory layout: CLAUDE.md, .claude/ (settings, hooks, skills, commands, a
- settings.json for CLI & model preferences
- hooks/ for automation guardrails
- skills/ for reusable AI workflows (review, refactor, testing)
- commands/ for reusable prompts
- agents/ for specialized sub-agent definitions
- AI-native code editor built on VS Code
- Cursor rules for project-specific AI behavior
- Tab completion, chat, composer, multi-file editing
- VS Code integration, CLI support
- Code completion, chat, PR descriptions
- Copilot Workspace for issue-to-PR workflows
- Lovable: AI-powered app builder from natural language
- Gamma: AI presentation and document creation
- Zero-code approach for rapid prototyping


- LCEL (LangChain Expression Language) for composable chains
- Chains, agents, tools, memory, callbacks
- Production patterns and anti-patterns
- StateGraph for defining agent workflows as directed graphs
- Nodes = functions, edges = transitions, state = shared context
- Checkpointing, human-in-the-loop, branching logic
- Define agents with roles, goals, backstories
- Sequential and hierarchical process types
- Task definitions with expected outputs
- ConversableAgent for multi-turn agent conversations
- Group chat patterns, code execution agents
- Microsoft Research framework
- Drag-and-drop UI for building LLM workflows
- Docker deployment, visual flow design
- Low-code approach to agent building
- Monitoring agent runs, costs, latency, errors
- Integration with LangSmith for tracing
- Production observability for agent systems
- Pipeline-based NLP framework by deepset
- Document stores, retrievers, readers, generators
- Modular pipeline composition
- Microsoft's SDK for AI orchestration
- Plugins, planners, memory in C# and Python
- Enterprise integration patterns
- Data connectors, indexes, query engines
- VectorStore index for RAG pipelines
- Document-centric LLM applications
- Weights & Biases: experiment tracking, model versioning
- Arize AI: model monitoring, drift detection
- Production LLM lifecycle management


- Client Agent → A2A Protocol → Remote Agents (with Agent Cards)
- Task requests sent, result artifacts returned
- Distributed execution model for agent-to-agent communication
- JSON-based identity documents for agents
- Capabilities, endpoints, authentication metadata
- Discovery and registration patterns
- Structured task requests between agents
- Result artifacts: typed outputs from delegated work
- Error handling and timeout patterns
- Running agents across multiple processes/containers
- Docker-based agent deployment
- LangGraph + A2A for orchestrated distributed workflows
- MCP = tools (connecting models to data/APIs)
- A2A = agents (connecting agents to each other)
- Together = real AI systems (full production stack)
- Decision framework: capability exposure vs peer communication


### Scenario: Hands-Free Agentic Development


- Traditional: Human → Role → Infrastructure (static RBAC, perimeter-based)
- Current Problem: AI Agent → APIs → Infrastructure (no unique identity, privilege
- Solution: Agent → Cryptographic Identity → Runtime Access → Auditable Actions (T


- Master full stack: LLM → Agents → Agentic AI → MCP → A2A → Production → Consulti
- Build 3 enterprise-grade capstone projects
- Qualify for AI Consultant / AI Architect / Agentic AI Engineer roles


### Teleport's New Agentic Identity Framework (Solution)


- Flow:** Agent → Cryptographic Identity → Runtime Access → Auditable Actions
- Dynamic, context-aware access


- Memory** (left side)
- Iservability / Agent Identity** (left side, spanning layers)


### Week 5 — Multi-Agent Collaboration & Model Optimization


- Multi-agent design patterns and use cases:
- Sequential pattern (application: new employee onboarding Crew)
- Supervisor pattern (application: sales analyst + market researcher reporting to
- Reflection / Round Robin Group Chat pattern (application: advertising copy creat
- Workflow Orchestration:
- Orchestrating multi-step agent workflows using Azure Durable Functions and Logic
- Model Selection and Evaluation — different models and solutions available, stren

