---
kind: phase_supplement
phase_code: P6
---

# Phase P6 — supplemental depth

### Agent frameworks

### Orchestration Patterns

**Looping & Conditional Workflows:** Agents often need to loop (retry until success, iterate until quality threshold) and branch (take different paths based on conditions). LangGraph implements loops as cycles in the state graph and branches as conditional edges. n8n implements these as loop nodes and IF/Switch nodes. Production systems need loop termination conditions (max iterations, timeout) to prevent infinite loops.

**Sub-Agent Parallelism:** Spawning multiple specialized sub-agents to work on independent subtasks simultaneously. Example: a research agent spawns three sub-agents in parallel — one searches arXiv, one searches GitHub, one searches news. Results are collected and synthesized by the parent agent. Dramatically reduces total execution time for parallelizable tasks. Implemented in LangGraph as parallel branches or via Python asyncio.

**Task Dispatch & Routing:** The orchestrator pattern where a central agent receives tasks and routes them to the most appropriate specialized sub-agent based on task type, required tools, or current load. Example: a customer support orchestrator routes billing questions to a billing agent, technical questions to a tech support agent, and escalations to a human agent. Routing logic can be rule-based or LLM-based.

**AutoGen Studio:** Microsoft's visual interface for building and testing AutoGen multi-agent workflows. Drag-and-drop agent configuration, visual conversation flow, built-in code execution. Useful for prototyping multi-agent systems before implementing them in code. Complements the AutoGen SDK (Module 48).

### Curriculum visual map — block E

### Image 7: 12 AI Skills — Skills 5-12 (Exact Descriptions)

**5. Prompt Engineering:** The art of designing structured prompts to guide AI effectively. When to use: whenever you need precision, creativity, or technical accuracy in outputs. Tools: ChatGPT, Claude, Gemini, Perplexity, PromptPerfect.

### Image 8: Claude Code Best Practices — From Prompts to Agentic Systems

**Section 1 — Complete Building Blocks:**
Claude Core connects to 7 building blocks:
- Subagents → isolated execution (fresh context)
- Commands → reusable prompts
- Skills → reusable knowledge/workflows
- MCP Servers → tools + APIs
- Memory → persistent context
- Settings → system control
- Workflows → orchestration layer

**Section 2 — System Flow:**
Execution pipeline: User Intent → Command Layer → Skills Injection (Memory feeds into all layers) → Subagent Execution (Hooks trigger on events) → MCP Tool Calls → Output (Workflows = scale)

**Section 3 — Context Engineering:**
- Bad: Big Prompt Chaos — cluttered commands, skills, messy summary, many items not structured
- Good: Structured Context — Commands, Skills, Memory, Subagents
- Key insight: "Smaller context = higher accuracy"

**Section 4 — Memory System:**
Three tiers: Session Context (temporary, persistent vs ephemeral) | Skills (playbooks, avoid noise) | CLAUDE.md (rules, architecture, store only long-term truth)

### Syllabus theme — day 14

**Day 14 — Lifecycle & Frameworks:** Agent lifecycle and planning loops. Frameworks: LangChain, LangGraph. Exercise: Build a simple agent using LangChain with memory and tools.

### Syllabus theme — day 15

**Day 15 — Multi-Agent Architectures & Frameworks:** Multi-agent coordination patterns (MCP). Frameworks: AI Foundry (Agent as a Service), OpenAI Agents, CrewAI (overview + deep dive). Exercise: Simulate MCP with task delegation and feedback loop; build CrewAI project (researcher + summarizer); compare AI Foundry vs CrewAI; design multi-agent workflow for domain use case.

### Syllabus theme — day 17

**Day 17 — Workflows:** Agent orchestration with AutoGen Studio and Semantic Kernel. Designing agent workflows and task delegation. Exercise: Build a multi-agent system using AutoGen Studio.

**Capstone 1: "My AI Called Me While I Was Driving"**
- Autonomous agent with HITL voice escalation
- Stack: LangGraph, Twilio Voice, Ollama, n8n, FastAPI, Redis, WebSocket
- Architecture: Task Trigger → Autonomous Execution → Decision Gate → Phone Call → Resume
- Full implementation with LangGraph StateGraph, Redis checkpointer, Twilio TTS, FastAPI webhook
- Difficulty: Advanced, 1-2 weeks


**Capstone 2: "AI-Powered Financial Risk Monitor"**
- Autonomous agent monitoring transactions, detecting anomalies, alerting in real-time
- Stack: LangGraph, n8n, Claude API, Pinecone, FastAPI, Twilio SMS, Redis Streams
- Architecture: Data Ingestion → Risk Scoring (Pinecone similarity) → LLM Analysis → Escalation (SMS/Slack/log)
- Fintech/payments consulting focused (AML/fraud monitoring)


- Human-in-the-loop voice escalation
- LangGraph state machine with Twilio Voice integration
- Ollama for local LLM inference
- Full trace logging for audit trail


- SearXNG meta-search engine (self-hosted via Docker)
- Ollama local LLM for answer synthesis
- Source cards with citations from search results
- Streamlit UI for search interface
- LangChain for orchestrating search → synthesize pipeline


- Exercise: Craft prompts for summarization, Q&A, classification using LangChain


- Anthropic: combine strong eval metrics with crisp demos (Streamlit/FastAPI)
- Hugging Face: ship clean cards, reproducible training, eval tables
- LangGraph: projects with traces, tests, and Dockerfile score highest


- Module 75: Orchestrator Design & Patterns [Core] | Tools: LangGraph, custom Pyth
- Module 77: Identity & Agent Security Layer [Core] | Tools: Teleport, cryptograph


- Self-hosted workflow automation with Docker
- Webhooks, AI nodes, LLM integration
- $0 cost with local Ollama integration
- Visual scenario builder with modules and connections
- + app integrations, conditional routing
- AI-enhanced automation scenarios
- Zaps: trigger → action workflows
- Enterprise-grade integrations, multi-step Zaps
- AI actions and natural language automation
- Directed Acyclic Graphs for workflow orchestration
- Event-based triggers: webhooks, schedules, file changes
- Tools: LangGraph, Airflow, n8n
- Conditional branching in automation workflows
- Validation gates, error handling, retry logic
- LangGraph conditional edges, n8n IF/Switch nodes


- Module 125: CAPSTONE 1: AI That Calls You [Core] | Tools: LangGraph, Twilio, Fas


- Designing instructions, formats, and examples for reliable model output
- Highest-ROI lever for many products
- Tools: Claude, GPT-4, PromptPerfect
- Emit intermediate reasoning steps before final answer
- Improves performance on math, logic, and multi-step tasks
- Everything visible to the model in one forward pass: system instructions, tool r
- Managing context for long conversations and large documents
- Tools: LangChain Memory, Claude 200K context
- Tools: CrewAI, AutoGen
- Iterative self-evaluation with score thresholds and automatic revision
- Reflexion pattern: generate → evaluate → reflect → regenerate
- Tools: LangGraph, custom Python
- Assigning roles and personas to guide model behavior
- Task decomposition through structured prompts
- Tools: Claude, GPT-4, Perplexity
- Sequential prompt pipelines where output of one becomes input of next
- LCEL (LangChain Expression Language) for composable chains
- Tools: LangChain, LangGraph, LCEL


- System combining model + tools + memory + control loop for multi-step goals
- Autonomous: full self-direction; Semi-autonomous: human checkpoints
- ReAct: Reasoning + Acting interleaved
- CAMEL: role-playing agent communication
- AutoGPT: recursive self-prompting autonomous agent
- Breaking complex goals into executable sub-tasks
- Custom planners, hierarchical task networks
- Tools: LangGraph, custom planners
- State machines for agent decision flow
- Policy selection based on context and constraints
- Tools: LangGraph, state machines
- ReAct pattern: Thought → Action → Observation → repeat
- Execution monitoring and error recovery
- Tools: LangGraph, ReAct pattern
- Reflexion: generate → evaluate → reflect → regenerate
- Score-based iteration with improvement thresholds
- Tools: Reflexion, LangGraph
- Sequential, parallel, hierarchical agent topologies
- Tools: CrewAI, AutoGen, LangGraph


- Module 34: Action Planning Loops & Execution [Core] | Tools: LangGraph, ReAct pa
- Module 35: Self-Reflection / Feedback Loops [Core] | Tools: Reflexion, LangGraph


- Designing tool interfaces for LLM consumption
- OpenAI tools parameter, LangChain tool decorators
- Schema design, error handling, tool selection strategies
- Short-term: conversation buffer within session
- Long-term: persistent storage across sessions (vector stores, databases)
- Episodic: event-based recall of past interactions
- Tools: LangChain Memory, mem0
- HTTP clients: requests, httpx for async
- Authentication, error handling, retry logic
- LangChain API chain patterns
- Python I/O for reading/writing files from agent context
- LangChain file tools, document loaders
- Security considerations for file system access
- Sandboxed code execution for agents
- E2B cloud sandboxes, Docker-based isolation
- Safety: never run untrusted code without sandboxing
- Tavily: AI-optimized search API
- SerpAPI: Google search results programmatically
- DuckDuckGo: privacy-focused search integration
- Playwright: headless browser automation
- Selenium: browser-based web scraping
- Firecrawl: AI-friendly web content extraction
- Use cases: data gathering, form filling, monitoring
- AEO: Answer Engine Optimization — optimizing for AI-driven search
- GEO: Generative Engine Optimization — appearing in ChatGPT/Perplexity results


- Module 37: Tool Use System Design [Core] | Tools: OpenAI tools, LangChain tools
- Module 39: External API Calling from Agents [Core] | Tools: requests, httpx, Lan
- Module 40: File Reader/Writer Tools [Core] | Tools: Python I/O, LangChain tools
- Module 42: Search & Retrieval Tools [Core] | Tools: Tavily, SerpAPI, DuckDuckGo
- Module 43: Web Browsing Tools for Agents [Core] | Tools: Playwright, Selenium, F
- Module 44: AI Search Optimisation (AEO/GEO) [Optional] | Tools: SearchAble, Outr


- Module 45: LangChain Deep Dive [Core] | Tools: LangChain, LCEL, chains
- Module 52: Semantic Kernel (Microsoft) [Optional] | Tools: Semantic Kernel, C#/P
- Module 54: LLM Management: W&B, Arize AI [Optional] | Tools: Weights & Biases, A


- Module 57: Document Chunking Strategies [Core] | Tools: LangChain splitters, cus
- Module 60: Query Refinement & Hybrid Search [Core] | Tools: BM25, dense retrieva
- Module 61: Knowledge Graphs for AI [Optional] | Tools: Neo4j, NetworkX, graph RA

