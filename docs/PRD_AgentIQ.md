# AgentIQ — Product and learning specification

AgentIQ is an AI-native learning platform with a **living curriculum**. Learners move through **phases P0–P19** using **journey module ids** (`0.1`, `1.2`, … = phase index · order within phase). **What to study and in what order** is below. **Full module bodies** live under [`content/phases/<P*>/modules/`](../content/phases/P0/modules/) (see each phase’s **index** and **Extended depth** links).

---

## Part A — Context

### Executive summary

AgentIQ is an AI-native, enterprise-grade Learning Management System purpose-built for AI education. Unlike static course platforms, AgentIQ is a **living platform** — its content grows autonomously via AI agents that research, write, and update topics daily. Students learn AI by interacting with AI. The platform runs on AI agents, is maintained by AI agents, and teaches people how to build AI agents.

**Core differentiators:**
- Content grows automatically — AI agents add new topics, sections, and modules daily
- A module marked complete today may have new sections tomorrow — progress is dynamic and honest
- AI agents handle feedback, triage improvements, respond to students, and file internal tickets
- Enterprise/tenant model — colleges, bootcamps, and companies can onboard entire cohorts
- Gamification: 10 learner levels (L1–L10), 100+ badges, streaks, leaderboards
- AI Chatbot interprets natural language queries and maps them to the right course/module
- Live AI News Feed curated by an agent monitoring X, arXiv, GitHub, and AI blogs daily
- Every AI agent interaction is transparently labeled — learners always know they are talking to an AI

---

### Problem statement

AI education is broken in three fundamental ways:

1. **Static content** — courses go stale within months as the AI landscape shifts weekly. A course on LangChain from 6 months ago may reference deprecated APIs.
2. **No personalization** — one-size-fits-all paths ignore where a learner actually is. A senior developer and a career switcher need different entry points.
3. **No feedback loop** — student confusion and improvement ideas disappear into a void. Nobody reads the feedback form.

AgentIQ solves all three: content is always current (agents update it), paths are adaptive (AI recommends next steps), and every piece of feedback is acted on by an AI agent within hours.

---

### Learning model

This is the most important architectural concept of AgentIQ. Content is **never frozen**.

### Content Hierarchy
```
Platform
└── Phase (20 phases, P0–P19)
    └── Module (133+ modules, growing)
        └── Section (Learn · Practice · Code · Quiz · References)
            └── Topic (individual concept, tool, or exercise)
```

### The Living Contract
- Any Topic, Section, or Module can receive new content at any time via AI agents or admin
- When new content is added to a module a learner has already completed:
  - Module status → **"Needs Review"** (not "Incomplete" — XP is preserved)
  - In-app notification: *"Module X has new content — review to stay current"*
  - Learner sees a **"What changed?"** diff view showing new/updated/removed topics
  - Learner re-checks new topics to restore "Complete" status
  - Quiz re-attempt is NOT required unless admin explicitly flags it
- Learners are never penalized — XP and badges are preserved, but the module badge requires re-acknowledgment of new content

### Content Versioning
- Every Topic, Section, and Module has a `version` integer and `updated_at` timestamp
- Learner's Progress record stores `completed_at_module_version`
- On module page load: if `module.version > progress.completed_at_module_version` → show "Updated" banner
- Full version history per module: who changed what, when (human or which agent)
- Rollback to any previous version available to admins
- Scheduled publish: set future date/time for content to go live

### Module Completion Definition
- Completion = learner has checked off all topics in Learn + Practice tabs
- Quiz passing is NOT required for completion (quiz is for self-assessment and XP bonus)
- Learner can mark individual topics complete as they go
- Module is "Complete" when all topics are checked

---

## Part B — Curriculum by phase

# Phase P0 — Local AI Setup

**Purpose:** Full local AI environment before writing agent code

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `0.1` | 1 | Ollama Setup & Local Model Running | MUST DO | [`content/phases/P0/modules/m001-ollama-setup-local-model-running.md`](../content/phases/P0/modules/m001-ollama-setup-local-model-running.md) |
| `0.2` | 2 | LM Studio — GUI for Local LLMs | MUST DO | [`content/phases/P0/modules/m002-lm-studio-gui-for-local-llms.md`](../content/phases/P0/modules/m002-lm-studio-gui-for-local-llms.md) |
| `0.3` | 3 | Open WebUI — Local ChatGPT Interface | MUST DO | [`content/phases/P0/modules/m003-open-webui-local-chatgpt-interface.md`](../content/phases/P0/modules/m003-open-webui-local-chatgpt-interface.md) |
| `0.4` | 4 | vLLM — High-Performance Inference | OPTIONAL | [`content/phases/P0/modules/m004-vllm-high-performance-inference.md`](../content/phases/P0/modules/m004-vllm-high-performance-inference.md) |
| `0.5` | 5 | LiteLLM Routing & Load Balancing | MUST DO | [`content/phases/P0/modules/m005-litellm-routing-load-balancing.md`](../content/phases/P0/modules/m005-litellm-routing-load-balancing.md) |
| `0.6` | 6 | Free APIs: Groq, Gemini, Mistral, OpenRouter | MUST DO | [`content/phases/P0/modules/m006-free-apis-groq-gemini-mistral-openrouter.md`](../content/phases/P0/modules/m006-free-apis-groq-gemini-mistral-openrouter.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P0/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P1 — AI Foundations

**Purpose:** LLMs, transformers, embeddings, ML paradigms

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `1.1` | 7 | Top 40 AI Terms & Core Concepts | MUST DO | [`content/phases/P1/modules/m007-top-40-ai-terms-core-concepts.md`](../content/phases/P1/modules/m007-top-40-ai-terms-core-concepts.md) |
| `1.2` | 8 | How LLMs Work: Transformers & Tokenization | MUST DO | [`content/phases/P1/modules/m008-how-llms-work-transformers-tokenization.md`](../content/phases/P1/modules/m008-how-llms-work-transformers-tokenization.md) |
| `1.3` | 9 | Embeddings & Vector Representations | MUST DO | [`content/phases/P1/modules/m009-embeddings-vector-representations.md`](../content/phases/P1/modules/m009-embeddings-vector-representations.md) |
| `1.4` | 10 | Inference, Context Windows & Cost Optimisation | MUST DO | [`content/phases/P1/modules/m010-inference-context-windows-cost-optimisation.md`](../content/phases/P1/modules/m010-inference-context-windows-cost-optimisation.md) |
| `1.5` | 11 | Quantization & Model Efficiency | OPTIONAL | [`content/phases/P1/modules/m011-quantization-model-efficiency.md`](../content/phases/P1/modules/m011-quantization-model-efficiency.md) |
| `1.6` | 12 | GPU/TPU & Compute for AI | OPTIONAL | [`content/phases/P1/modules/m012-gputpu-compute-for-ai.md`](../content/phases/P1/modules/m012-gputpu-compute-for-ai.md) |
| `1.7` | 13 | ML Paradigms: Supervised, Unsupervised, RL | MUST DO | [`content/phases/P1/modules/m013-ml-paradigms-supervised-unsupervised-rl.md`](../content/phases/P1/modules/m013-ml-paradigms-supervised-unsupervised-rl.md) |
| `1.8` | 14 | Generative AI Pipeline (Input→Process→Output) | MUST DO | [`content/phases/P1/modules/m014-generative-ai-pipeline-inputprocessoutput.md`](../content/phases/P1/modules/m014-generative-ai-pipeline-inputprocessoutput.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P1/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P2 — Prompt Engineering

**Purpose:** The primary interface to models

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `2.1` | 15 | Prompt Engineering Fundamentals | MUST DO | [`content/phases/P2/modules/m015-prompt-engineering-fundamentals.md`](../content/phases/P2/modules/m015-prompt-engineering-fundamentals.md) |
| `2.2` | 16 | Chain-of-Thought (CoT) Prompting | MUST DO | [`content/phases/P2/modules/m016-chain-of-thought-cot-prompting.md`](../content/phases/P2/modules/m016-chain-of-thought-cot-prompting.md) |
| `2.3` | 17 | Context Management & Context Window | MUST DO | [`content/phases/P2/modules/m017-context-management-context-window.md`](../content/phases/P2/modules/m017-context-management-context-window.md) |
| `2.4` | 18 | Multi-Agent & Goal-Oriented Prompts | MUST DO | [`content/phases/P2/modules/m018-multi-agent-goal-oriented-prompts.md`](../content/phases/P2/modules/m018-multi-agent-goal-oriented-prompts.md) |
| `2.5` | 19 | Self-Critique, Retry Loops & Reflexion | MUST DO | [`content/phases/P2/modules/m019-self-critique-retry-loops-reflexion.md`](../content/phases/P2/modules/m019-self-critique-retry-loops-reflexion.md) |
| `2.6` | 20 | Task Planning Prompts & Role Prompting | MUST DO | [`content/phases/P2/modules/m020-task-planning-prompts-role-prompting.md`](../content/phases/P2/modules/m020-task-planning-prompts-role-prompting.md) |
| `2.7` | 21 | Prompt Chaining & Advanced Techniques | MUST DO | [`content/phases/P2/modules/m021-prompt-chaining-advanced-techniques.md`](../content/phases/P2/modules/m021-prompt-chaining-advanced-techniques.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P2/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P3 — LLMs & APIs

**Purpose:** Providers, auth, tools, multimodal

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `3.1` | 22 | OpenAI API Deep Dive (GPT-4, GPT-4o) | MUST DO | [`content/phases/P3/modules/m022-openai-api-deep-dive-gpt-4-gpt-4o.md`](../content/phases/P3/modules/m022-openai-api-deep-dive-gpt-4-gpt-4o.md) |
| `3.2` | 23 | Anthropic Claude API | MUST DO | [`content/phases/P3/modules/m023-anthropic-claude-api.md`](../content/phases/P3/modules/m023-anthropic-claude-api.md) |
| `3.3` | 24 | Google Gemini API | MUST DO | [`content/phases/P3/modules/m024-google-gemini-api.md`](../content/phases/P3/modules/m024-google-gemini-api.md) |
| `3.4` | 25 | Mistral & Open Source LLMs (LLaMA, DeepSeek) | MUST DO | [`content/phases/P3/modules/m025-mistral-open-source-llms-llama-deepseek.md`](../content/phases/P3/modules/m025-mistral-open-source-llms-llama-deepseek.md) |
| `3.5` | 26 | API Authentication & Rate Limiting | MUST DO | [`content/phases/P3/modules/m026-api-authentication-rate-limiting.md`](../content/phases/P3/modules/m026-api-authentication-rate-limiting.md) |
| `3.6` | 27 | Toolformer / Function Calling | MUST DO | [`content/phases/P3/modules/m027-toolformer-function-calling.md`](../content/phases/P3/modules/m027-toolformer-function-calling.md) |
| `3.7` | 28 | Tool Invocation & Output Parsing | MUST DO | [`content/phases/P3/modules/m028-tool-invocation-output-parsing.md`](../content/phases/P3/modules/m028-tool-invocation-output-parsing.md) |
| `3.8` | 29 | Multimodal AI (Text + Image + Audio + Video) | MUST DO | [`content/phases/P3/modules/m029-multimodal-ai-text-image-audio-video.md`](../content/phases/P3/modules/m029-multimodal-ai-text-image-audio-video.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P3/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P4 — Agent Fundamentals

**Purpose:** Architectures, planning, collaboration

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `4.1` | 30 | What Are AI Agents? Autonomous vs Semi-Auto | MUST DO | [`content/phases/P4/modules/m030-what-are-ai-agents-autonomous-vs-semi-auto.md`](../content/phases/P4/modules/m030-what-are-ai-agents-autonomous-vs-semi-auto.md) |
| `4.2` | 31 | Agent Architectures: ReAct, CAMEL, AutoGPT | MUST DO | [`content/phases/P4/modules/m031-agent-architectures-react-camel-autogpt.md`](../content/phases/P4/modules/m031-agent-architectures-react-camel-autogpt.md) |
| `4.3` | 32 | Goal Decomposition & Task Planning Algorithms | MUST DO | [`content/phases/P4/modules/m032-goal-decomposition-task-planning-algorithms.md`](../content/phases/P4/modules/m032-goal-decomposition-task-planning-algorithms.md) |
| `4.4` | 33 | Decision-Making Policies for Agents | MUST DO | [`content/phases/P4/modules/m033-decision-making-policies-for-agents.md`](../content/phases/P4/modules/m033-decision-making-policies-for-agents.md) |
| `4.5` | 34 | Action Planning Loops & Execution | MUST DO | [`content/phases/P4/modules/m034-action-planning-loops-execution.md`](../content/phases/P4/modules/m034-action-planning-loops-execution.md) |
| `4.6` | 35 | Self-Reflection / Feedback Loops | MUST DO | [`content/phases/P4/modules/m035-self-reflection-feedback-loops.md`](../content/phases/P4/modules/m035-self-reflection-feedback-loops.md) |
| `4.7` | 36 | Multi-Agent Collaboration Patterns | MUST DO | [`content/phases/P4/modules/m036-multi-agent-collaboration-patterns.md`](../content/phases/P4/modules/m036-multi-agent-collaboration-patterns.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P4/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P5 — Tool Use & Integration

**Purpose:** Memory, APIs, files, search, browsing

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `5.1` | 37 | Tool Use System Design | MUST DO | [`content/phases/P5/modules/m037-tool-use-system-design.md`](../content/phases/P5/modules/m037-tool-use-system-design.md) |
| `5.2` | 38 | Memory Integration (Short/Long-Term/Episodic) | MUST DO | [`content/phases/P5/modules/m038-memory-integration-shortlong-termepisodic.md`](../content/phases/P5/modules/m038-memory-integration-shortlong-termepisodic.md) |
| `5.3` | 39 | External API Calling from Agents | MUST DO | [`content/phases/P5/modules/m039-external-api-calling-from-agents.md`](../content/phases/P5/modules/m039-external-api-calling-from-agents.md) |
| `5.4` | 40 | File Reader/Writer Tools | MUST DO | [`content/phases/P5/modules/m040-file-readerwriter-tools.md`](../content/phases/P5/modules/m040-file-readerwriter-tools.md) |
| `5.5` | 41 | Python Execution Tools (Code Interpreter) | MUST DO | [`content/phases/P5/modules/m041-python-execution-tools-code-interpreter.md`](../content/phases/P5/modules/m041-python-execution-tools-code-interpreter.md) |
| `5.6` | 42 | Search & Retrieval Tools | MUST DO | [`content/phases/P5/modules/m042-search-retrieval-tools.md`](../content/phases/P5/modules/m042-search-retrieval-tools.md) |
| `5.7` | 43 | Web Browsing Tools for Agents | MUST DO | [`content/phases/P5/modules/m043-web-browsing-tools-for-agents.md`](../content/phases/P5/modules/m043-web-browsing-tools-for-agents.md) |
| `5.8` | 44 | AI Search Optimisation (AEO/GEO) | OPTIONAL | [`content/phases/P5/modules/m044-ai-search-optimisation-aeogeo.md`](../content/phases/P5/modules/m044-ai-search-optimisation-aeogeo.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P5/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P6 — Agent Frameworks

**Purpose:** LangChain, LangGraph, CrewAI, LlamaIndex…

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `6.1` | 45 | LangChain Deep Dive | MUST DO | [`content/phases/P6/modules/m045-langchain-deep-dive.md`](../content/phases/P6/modules/m045-langchain-deep-dive.md) |
| `6.2` | 46 | LangGraph — Stateful Agent Orchestration | MUST DO | [`content/phases/P6/modules/m046-langgraph-stateful-agent-orchestration.md`](../content/phases/P6/modules/m046-langgraph-stateful-agent-orchestration.md) |
| `6.3` | 47 | CrewAI — Multi-Agent Crews | MUST DO | [`content/phases/P6/modules/m047-crewai-multi-agent-crews.md`](../content/phases/P6/modules/m047-crewai-multi-agent-crews.md) |
| `6.4` | 48 | AutoGen — Conversational Multi-Agent | MUST DO | [`content/phases/P6/modules/m048-autogen-conversational-multi-agent.md`](../content/phases/P6/modules/m048-autogen-conversational-multi-agent.md) |
| `6.5` | 49 | Flowise — Visual Agent Builder | OPTIONAL | [`content/phases/P6/modules/m049-flowise-visual-agent-builder.md`](../content/phases/P6/modules/m049-flowise-visual-agent-builder.md) |
| `6.6` | 50 | AgentOps — Agent Monitoring & Observability | MUST DO | [`content/phases/P6/modules/m050-agentops-agent-monitoring-observability.md`](../content/phases/P6/modules/m050-agentops-agent-monitoring-observability.md) |
| `6.7` | 51 | Haystack — NLP Pipeline Framework | OPTIONAL | [`content/phases/P6/modules/m051-haystack-nlp-pipeline-framework.md`](../content/phases/P6/modules/m051-haystack-nlp-pipeline-framework.md) |
| `6.8` | 52 | Semantic Kernel (Microsoft) | OPTIONAL | [`content/phases/P6/modules/m052-semantic-kernel-microsoft.md`](../content/phases/P6/modules/m052-semantic-kernel-microsoft.md) |
| `6.9` | 53 | LlamaIndex — Data Framework for LLMs | MUST DO | [`content/phases/P6/modules/m053-llamaindex-data-framework-for-llms.md`](../content/phases/P6/modules/m053-llamaindex-data-framework-for-llms.md) |
| `6.10` | 54 | LLM Management: W&B, Arize AI | OPTIONAL | [`content/phases/P6/modules/m054-llm-management-wb-arize-ai.md`](../content/phases/P6/modules/m054-llm-management-wb-arize-ai.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P6/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P7 — RAG & Knowledge

**Purpose:** Embeddings, chunking, vector DBs, hybrid search

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `7.1` | 55 | RAG Architecture & Pipeline Design | MUST DO | [`content/phases/P7/modules/m055-rag-architecture-pipeline-design.md`](../content/phases/P7/modules/m055-rag-architecture-pipeline-design.md) |
| `7.2` | 56 | Embedding Models & Semantic Search | MUST DO | [`content/phases/P7/modules/m056-embedding-models-semantic-search.md`](../content/phases/P7/modules/m056-embedding-models-semantic-search.md) |
| `7.3` | 57 | Document Chunking Strategies | MUST DO | [`content/phases/P7/modules/m057-document-chunking-strategies.md`](../content/phases/P7/modules/m057-document-chunking-strategies.md) |
| `7.4` | 58 | Custom Data Loaders & Document Ingestion | MUST DO | [`content/phases/P7/modules/m058-custom-data-loaders-document-ingestion.md`](../content/phases/P7/modules/m058-custom-data-loaders-document-ingestion.md) |
| `7.5` | 59 | Vector DBs: Pinecone, Weaviate, Chroma, FAISS | MUST DO | [`content/phases/P7/modules/m059-vector-dbs-pinecone-weaviate-chroma-faiss.md`](../content/phases/P7/modules/m059-vector-dbs-pinecone-weaviate-chroma-faiss.md) |
| `7.6` | 60 | Query Refinement & Hybrid Search | MUST DO | [`content/phases/P7/modules/m060-query-refinement-hybrid-search.md`](../content/phases/P7/modules/m060-query-refinement-hybrid-search.md) |
| `7.7` | 61 | Knowledge Graphs for AI | OPTIONAL | [`content/phases/P7/modules/m061-knowledge-graphs-for-ai.md`](../content/phases/P7/modules/m061-knowledge-graphs-for-ai.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P7/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P8 — MCP Protocol

**Purpose:** Model Context Protocol depth

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `8.1` | 62 | MCP Architecture & Core Concepts | MUST DO | [`content/phases/P8/modules/m062-mcp-architecture-core-concepts.md`](../content/phases/P8/modules/m062-mcp-architecture-core-concepts.md) |
| `8.2` | 63 | MCP Host, Client & Server Design | MUST DO | [`content/phases/P8/modules/m063-mcp-host-client-server-design.md`](../content/phases/P8/modules/m063-mcp-host-client-server-design.md) |
| `8.3` | 64 | MCP Transport Layer & Communication | MUST DO | [`content/phases/P8/modules/m064-mcp-transport-layer-communication.md`](../content/phases/P8/modules/m064-mcp-transport-layer-communication.md) |
| `8.4` | 65 | Secure File Access & Sampling in MCP | MUST DO | [`content/phases/P8/modules/m065-secure-file-access-sampling-in-mcp.md`](../content/phases/P8/modules/m065-secure-file-access-sampling-in-mcp.md) |
| `8.5` | 66 | MCP Resources, Prompts & Tools | MUST DO | [`content/phases/P8/modules/m066-mcp-resources-prompts-tools.md`](../content/phases/P8/modules/m066-mcp-resources-prompts-tools.md) |
| `8.6` | 67 | Building a Custom MCP Server (Python) | MUST DO | [`content/phases/P8/modules/m067-building-a-custom-mcp-server-python.md`](../content/phases/P8/modules/m067-building-a-custom-mcp-server-python.md) |
| `8.7` | 68 | MCP Integrations: S3, Stripe, Databases | MUST DO | [`content/phases/P8/modules/m068-mcp-integrations-s3-stripe-databases.md`](../content/phases/P8/modules/m068-mcp-integrations-s3-stripe-databases.md) |
| `8.8` | 69 | Claude Desktop + MCP Full Setup | MUST DO | [`content/phases/P8/modules/m069-claude-desktop-mcp-full-setup.md`](../content/phases/P8/modules/m069-claude-desktop-mcp-full-setup.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P8/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P9 — A2A Protocol

**Purpose:** Agent-to-agent communication

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `9.1` | 70 | A2A Protocol Architecture | MUST DO | [`content/phases/P9/modules/m070-a2a-protocol-architecture.md`](../content/phases/P9/modules/m070-a2a-protocol-architecture.md) |
| `9.2` | 71 | Agent Cards & Agent Identity | MUST DO | [`content/phases/P9/modules/m071-agent-cards-agent-identity.md`](../content/phases/P9/modules/m071-agent-cards-agent-identity.md) |
| `9.3` | 72 | Task Delegation & Result Artifacts | MUST DO | [`content/phases/P9/modules/m072-task-delegation-result-artifacts.md`](../content/phases/P9/modules/m072-task-delegation-result-artifacts.md) |
| `9.4` | 73 | Multi-Agent Distributed Execution | MUST DO | [`content/phases/P9/modules/m073-multi-agent-distributed-execution.md`](../content/phases/P9/modules/m073-multi-agent-distributed-execution.md) |
| `9.5` | 74 | A2A vs MCP: When to Use Which | MUST DO | [`content/phases/P9/modules/m074-a2a-vs-mcp-when-to-use-which.md`](../content/phases/P9/modules/m074-a2a-vs-mcp-when-to-use-which.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P9/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P10 — Unified AI Systems

**Purpose:** Orchestration, identity, observability, 9-layer stack

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `10.1` | 75 | Orchestrator Design & Patterns | MUST DO | [`content/phases/P10/modules/m075-orchestrator-design-patterns.md`](../content/phases/P10/modules/m075-orchestrator-design-patterns.md) |
| `10.2` | 76 | Memory Layer Architecture (3-Tier) | MUST DO | [`content/phases/P10/modules/m076-memory-layer-architecture-3-tier.md`](../content/phases/P10/modules/m076-memory-layer-architecture-3-tier.md) |
| `10.3` | 77 | Identity & Agent Security Layer | MUST DO | [`content/phases/P10/modules/m077-identity-agent-security-layer.md`](../content/phases/P10/modules/m077-identity-agent-security-layer.md) |
| `10.4` | 78 | Observability: Logs, Traces, Metrics | MUST DO | [`content/phases/P10/modules/m078-observability-logs-traces-metrics.md`](../content/phases/P10/modules/m078-observability-logs-traces-metrics.md) |
| `10.5` | 79 | Guardrails & Output Safety Systems | MUST DO | [`content/phases/P10/modules/m079-guardrails-output-safety-systems.md`](../content/phases/P10/modules/m079-guardrails-output-safety-systems.md) |
| `10.6` | 80 | The 9-Layer Agentic AI Infrastructure Stack | MUST DO | [`content/phases/P10/modules/m080-the-9-layer-agentic-ai-infrastructure-stack.md`](../content/phases/P10/modules/m080-the-9-layer-agentic-ai-infrastructure-stack.md) |
| `10.7` | 81 | RBAC & Securing AI Agents (Cryptographic ID) | MUST DO | [`content/phases/P10/modules/m081-rbac-securing-ai-agents-cryptographic-id.md`](../content/phases/P10/modules/m081-rbac-securing-ai-agents-cryptographic-id.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P10/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P11 — Fine-Tuning

**Purpose:** LoRA, PEFT, data prep, evaluation

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `11.1` | 82 | Fine-Tuning Fundamentals & When to Use It | MUST DO | [`content/phases/P11/modules/m082-fine-tuning-fundamentals-when-to-use-it.md`](../content/phases/P11/modules/m082-fine-tuning-fundamentals-when-to-use-it.md) |
| `11.2` | 83 | LoRA & QLoRA (Efficient Fine-Tuning) | MUST DO | [`content/phases/P11/modules/m083-lora-qlora-efficient-fine-tuning.md`](../content/phases/P11/modules/m083-lora-qlora-efficient-fine-tuning.md) |
| `11.3` | 84 | PEFT: Parameter Efficient Fine-Tuning | MUST DO | [`content/phases/P11/modules/m084-peft-parameter-efficient-fine-tuning.md`](../content/phases/P11/modules/m084-peft-parameter-efficient-fine-tuning.md) |
| `11.4` | 85 | Training Data Preparation & Curation | MUST DO | [`content/phases/P11/modules/m085-training-data-preparation-curation.md`](../content/phases/P11/modules/m085-training-data-preparation-curation.md) |
| `11.5` | 86 | Domain Adaptation & Model Evaluation | OPTIONAL | [`content/phases/P11/modules/m086-domain-adaptation-model-evaluation.md`](../content/phases/P11/modules/m086-domain-adaptation-model-evaluation.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P11/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P12 — Vibe Coding

**Purpose:** AI-native development tools

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `12.1` | 87 | Vibe Coding Philosophy & Toolchain | MUST DO | [`content/phases/P12/modules/m087-vibe-coding-philosophy-toolchain.md`](../content/phases/P12/modules/m087-vibe-coding-philosophy-toolchain.md) |
| `12.2` | 88 | Claude Code: Setup, CLAUDE.md & Workflow | MUST DO | [`content/phases/P12/modules/m088-claude-code-setup-claudemd-workflow.md`](../content/phases/P12/modules/m088-claude-code-setup-claudemd-workflow.md) |
| `12.3` | 89 | Claude Code: Skills, Hooks & Memory System | MUST DO | [`content/phases/P12/modules/m089-claude-code-skills-hooks-memory-system.md`](../content/phases/P12/modules/m089-claude-code-skills-hooks-memory-system.md) |
| `12.4` | 90 | Claude Code: 4-Layer Architecture | MUST DO | [`content/phases/P12/modules/m090-claude-code-4-layer-architecture.md`](../content/phases/P12/modules/m090-claude-code-4-layer-architecture.md) |
| `12.5` | 91 | Claude Code: Project Structure (Agentic Setup) | MUST DO | [`content/phases/P12/modules/m091-claude-code-project-structure-agentic-setup.md`](../content/phases/P12/modules/m091-claude-code-project-structure-agentic-setup.md) |
| `12.6` | 92 | Cursor AI — AI-Native IDE | MUST DO | [`content/phases/P12/modules/m092-cursor-ai-ai-native-ide.md`](../content/phases/P12/modules/m092-cursor-ai-ai-native-ide.md) |
| `12.7` | 93 | GitHub Copilot for AI Development | MUST DO | [`content/phases/P12/modules/m093-github-copilot-for-ai-development.md`](../content/phases/P12/modules/m093-github-copilot-for-ai-development.md) |
| `12.8` | 94 | Lovable & Gamma (No-Code AI Builders) | OPTIONAL | [`content/phases/P12/modules/m094-lovable-gamma-no-code-ai-builders.md`](../content/phases/P12/modules/m094-lovable-gamma-no-code-ai-builders.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P12/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P13 — Automation

**Purpose:** n8n, Make, Zapier, DAGs, guardrails

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `13.1` | 95 | n8n — Open Source Workflow Automation | MUST DO | [`content/phases/P13/modules/m095-n8n-open-source-workflow-automation.md`](../content/phases/P13/modules/m095-n8n-open-source-workflow-automation.md) |
| `13.2` | 96 | Make.com (Integromat) — Visual Automation | MUST DO | [`content/phases/P13/modules/m096-makecom-integromat-visual-automation.md`](../content/phases/P13/modules/m096-makecom-integromat-visual-automation.md) |
| `13.3` | 97 | Zapier — Enterprise Integration Automation | MUST DO | [`content/phases/P13/modules/m097-zapier-enterprise-integration-automation.md`](../content/phases/P13/modules/m097-zapier-enterprise-integration-automation.md) |
| `13.4` | 98 | DAG Management & Event-Based Triggers | MUST DO | [`content/phases/P13/modules/m098-dag-management-event-based-triggers.md`](../content/phases/P13/modules/m098-dag-management-event-based-triggers.md) |
| `13.5` | 99 | Guardrails & Conditional Workflow Logic | MUST DO | [`content/phases/P13/modules/m099-guardrails-conditional-workflow-logic.md`](../content/phases/P13/modules/m099-guardrails-conditional-workflow-logic.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P13/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P14 — Production AI

**Purpose:** APIs, Docker, hosting, serverless

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `14.1` | 100 | FastAPI — Production API for AI Systems | MUST DO | [`content/phases/P14/modules/m100-fastapi-production-api-for-ai-systems.md`](../content/phases/P14/modules/m100-fastapi-production-api-for-ai-systems.md) |
| `14.2` | 101 | Streamlit & Gradio — AI UIs | MUST DO | [`content/phases/P14/modules/m101-streamlit-gradio-ai-uis.md`](../content/phases/P14/modules/m101-streamlit-gradio-ai-uis.md) |
| `14.3` | 102 | Serverless Functions for AI | MUST DO | [`content/phases/P14/modules/m102-serverless-functions-for-ai.md`](../content/phases/P14/modules/m102-serverless-functions-for-ai.md) |
| `14.4` | 103 | Docker for AI Systems | MUST DO | [`content/phases/P14/modules/m103-docker-for-ai-systems.md`](../content/phases/P14/modules/m103-docker-for-ai-systems.md) |
| `14.5` | 104 | Kubernetes for AI Scale | OPTIONAL | [`content/phases/P14/modules/m104-kubernetes-for-ai-scale.md`](../content/phases/P14/modules/m104-kubernetes-for-ai-scale.md) |
| `14.6` | 105 | Vector DB Hosting & Management | MUST DO | [`content/phases/P14/modules/m105-vector-db-hosting-management.md`](../content/phases/P14/modules/m105-vector-db-hosting-management.md) |
| `14.7` | 106 | Agent Hosting: Replit, Modal, Fly.io | MUST DO | [`content/phases/P14/modules/m106-agent-hosting-replit-modal-flyio.md`](../content/phases/P14/modules/m106-agent-hosting-replit-modal-flyio.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P14/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P15 — Monitoring & Eval

**Purpose:** RAGAS, LangSmith, OpenTelemetry

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `15.1` | 107 | Agent Evaluation Metrics & Benchmarks | MUST DO | [`content/phases/P15/modules/m107-agent-evaluation-metrics-benchmarks.md`](../content/phases/P15/modules/m107-agent-evaluation-metrics-benchmarks.md) |
| `15.2` | 108 | Human-in-the-Loop Feedback Systems | MUST DO | [`content/phases/P15/modules/m108-human-in-the-loop-feedback-systems.md`](../content/phases/P15/modules/m108-human-in-the-loop-feedback-systems.md) |
| `15.3` | 109 | LangSmith — Tracing & Debugging LLM Apps | MUST DO | [`content/phases/P15/modules/m109-langsmith-tracing-debugging-llm-apps.md`](../content/phases/P15/modules/m109-langsmith-tracing-debugging-llm-apps.md) |
| `15.4` | 110 | OpenTelemetry for AI Observability | MUST DO | [`content/phases/P15/modules/m110-opentelemetry-for-ai-observability.md`](../content/phases/P15/modules/m110-opentelemetry-for-ai-observability.md) |
| `15.5` | 111 | Auto-Evaluation Loops | MUST DO | [`content/phases/P15/modules/m111-auto-evaluation-loops.md`](../content/phases/P15/modules/m111-auto-evaluation-loops.md) |
| `15.6` | 112 | Prometheus & Grafana for AI Metrics | OPTIONAL | [`content/phases/P15/modules/m112-prometheus-grafana-for-ai-metrics.md`](../content/phases/P15/modules/m112-prometheus-grafana-for-ai-metrics.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P15/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P16 — Security & Governance

**Purpose:** Injection, secrets, RBAC, privacy

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `16.1` | 113 | Prompt Injection Detection & Protection | MUST DO | [`content/phases/P16/modules/m113-prompt-injection-detection-protection.md`](../content/phases/P16/modules/m113-prompt-injection-detection-protection.md) |
| `16.2` | 114 | API Key Management & Secret Rotation | MUST DO | [`content/phases/P16/modules/m114-api-key-management-secret-rotation.md`](../content/phases/P16/modules/m114-api-key-management-secret-rotation.md) |
| `16.3` | 115 | User Authentication & RBAC | MUST DO | [`content/phases/P16/modules/m115-user-authentication-rbac.md`](../content/phases/P16/modules/m115-user-authentication-rbac.md) |
| `16.4` | 116 | Output Filtering & Content Safety | MUST DO | [`content/phases/P16/modules/m116-output-filtering-content-safety.md`](../content/phases/P16/modules/m116-output-filtering-content-safety.md) |
| `16.5` | 117 | Red Team Testing for AI Systems | MUST DO | [`content/phases/P16/modules/m117-red-team-testing-for-ai-systems.md`](../content/phases/P16/modules/m117-red-team-testing-for-ai-systems.md) |
| `16.6` | 118 | Data Privacy, AI Alignment & Compliance | MUST DO | [`content/phases/P16/modules/m118-data-privacy-ai-alignment-compliance.md`](../content/phases/P16/modules/m118-data-privacy-ai-alignment-compliance.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P16/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P17 — Consultant Track

**Purpose:** Strategy, pricing, demos, 12 skills

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `17.1` | 119 | AI Strategy & Architecture Design | MUST DO | [`content/phases/P17/modules/m119-ai-strategy-architecture-design.md`](../content/phases/P17/modules/m119-ai-strategy-architecture-design.md) |
| `17.2` | 120 | The 12 AI Skills Matrix for 2026 | MUST DO | [`content/phases/P17/modules/m120-the-12-ai-skills-matrix-for-2026.md`](../content/phases/P17/modules/m120-the-12-ai-skills-matrix-for-2026.md) |
| `17.3` | 121 | Cost Optimisation for AI Systems | MUST DO | [`content/phases/P17/modules/m121-cost-optimisation-for-ai-systems.md`](../content/phases/P17/modules/m121-cost-optimisation-for-ai-systems.md) |
| `17.4` | 122 | Enterprise AI Implementation Playbook | MUST DO | [`content/phases/P17/modules/m122-enterprise-ai-implementation-playbook.md`](../content/phases/P17/modules/m122-enterprise-ai-implementation-playbook.md) |
| `17.5` | 123 | AI Consultant Positioning & Pricing | MUST DO | [`content/phases/P17/modules/m123-ai-consultant-positioning-pricing.md`](../content/phases/P17/modules/m123-ai-consultant-positioning-pricing.md) |
| `17.6` | 124 | Stakeholder Communication & Demos | MUST DO | [`content/phases/P17/modules/m124-stakeholder-communication-demos.md`](../content/phases/P17/modules/m124-stakeholder-communication-demos.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P17/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P18 — Capstones

**Purpose:** Three portfolio projects

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `18.1` | 125 | CAPSTONE 1: AI That Calls You | MUST DO | [`content/phases/P18/modules/m125-capstone-1-ai-that-calls-you.md`](../content/phases/P18/modules/m125-capstone-1-ai-that-calls-you.md) |
| `18.2` | 126 | CAPSTONE 2: AI Payment Risk Analyst | MUST DO | [`content/phases/P18/modules/m126-capstone-2-ai-payment-risk-analyst.md`](../content/phases/P18/modules/m126-capstone-2-ai-payment-risk-analyst.md) |
| `18.3` | 127 | CAPSTONE 3: Local Perplexity Clone | MUST DO | [`content/phases/P18/modules/m127-capstone-3-local-perplexity-clone.md`](../content/phases/P18/modules/m127-capstone-3-local-perplexity-clone.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P18/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

# Phase P19 — Certifications

**Purpose:** Vendor credentials roadmap

## Module index

Journey IDs use **phase index · sequence in phase** (e.g. `0.1`, `1.3`). Catalog `#` is the stable curriculum id for imports and data.

| Journey | Catalog # | Title | Priority | Core content |
|---------|------------|-------|----------|----------------|
| `19.1` | 128 | Google Cloud — Generative AI Leader & Vertex AI | MUST DO | [`content/phases/P19/modules/m128-google-cloud-generative-ai-leader-vertex-ai.md`](../content/phases/P19/modules/m128-google-cloud-generative-ai-leader-vertex-ai.md) |
| `19.2` | 129 | AWS Certified AI Practitioner & Gen AI on AWS | MUST DO | [`content/phases/P19/modules/m129-aws-certified-ai-practitioner-gen-ai-on-aws.md`](../content/phases/P19/modules/m129-aws-certified-ai-practitioner-gen-ai-on-aws.md) |
| `19.3` | 130 | NVIDIA Generative AI LLM Certifications | MUST DO | [`content/phases/P19/modules/m130-nvidia-generative-ai-llm-certifications.md`](../content/phases/P19/modules/m130-nvidia-generative-ai-llm-certifications.md) |
| `19.4` | 131 | Microsoft Azure AI Engineer (AI-102) | MUST DO | [`content/phases/P19/modules/m131-microsoft-azure-ai-engineer-ai-102.md`](../content/phases/P19/modules/m131-microsoft-azure-ai-engineer-ai-102.md) |
| `19.5` | 132 | IBM watsonx & Generative AI Engineering | OPTIONAL | [`content/phases/P19/modules/m132-ibm-watsonx-generative-ai-engineering.md`](../content/phases/P19/modules/m132-ibm-watsonx-generative-ai-engineering.md) |
| `19.6` | 133 | Hugging Face — LLM, Agents & Open Models | MUST DO | [`content/phases/P19/modules/m133-hugging-face-llm-agents-open-models.md`](../content/phases/P19/modules/m133-hugging-face-llm-agents-open-models.md) |

## Extended depth

- **Phase-wide** (maps, syllabus themes, topic glossaries): [`supplement.md`](../content/phases/P19/supplement.md) — present only when material was routed to this phase.
- **Per-module** addenda: `depth/mNNN.md` next to `modules/` (only generated for cited catalog ids).


---

## Part C — Hackathons

Narratives, judging patterns, and competition notes: [`content/categories/hackathons.md`](../content/categories/hackathons.md).

---

## Part D — Startup ideas

Extended idea specs: [`content/categories/startup-ideas.md`](../content/categories/startup-ideas.md).

---

## Part E — Platform specification (flows & requirements)

Part A states **core differentiators**; this part points to where each is **specified** (functional requirements, agents, and UX).

| Topic | Document |
|-------|----------|
| Vision & learner/admin personas | [`content/platform/vision-and-personas.md`](../content/platform/vision-and-personas.md) |
| Platform features — auth (incl. AI labeling), dashboard, navigation, module page, **topic feedback**, improvement suggestions, progress, certifications UI, capstones | [`content/platform/platform-features.md`](../content/platform/platform-features.md) |
| Gamification — levels L1–L10, XP, badges, streaks, leaderboards | [`content/platform/gamification.md`](../content/platform/gamification.md) |
| **AI agent system** — registry (content, feedback, news, triage, …), transparency rules, observability | [`content/platform/ai-agents.md`](../content/platform/ai-agents.md) |
| Enterprise & **multi-tenant** model | [`content/platform/enterprise-tenant.md`](../content/platform/enterprise-tenant.md) |
| **AI chatbot** (course navigator) | [`content/platform/ai-chatbot.md`](../content/platform/ai-chatbot.md) |
| **AI news feed** | [`content/platform/ai-news-feed.md`](../content/platform/ai-news-feed.md) |
| Notification system | [`content/platform/notifications.md`](../content/platform/notifications.md) |
| Admin & tenant admin panel | [`content/platform/admin-panel.md`](../content/platform/admin-panel.md) |
| Technical architecture | [`content/platform/technical-architecture.md`](../content/platform/technical-architecture.md) |
| **Content versioning & dynamic completion** (extends Part A learning model) | [`content/platform/content-versioning.md`](../content/platform/content-versioning.md) |
| Personalization & adaptive learning | [`content/platform/personalization.md`](../content/platform/personalization.md) |
| Certifications, capstones, catalogs, NFRs, metrics, roadmap (§18–§26) | [`content/platform/catalogs-and-roadmap.md`](../content/platform/catalogs-and-roadmap.md) |

**Layered specification (no duplicate curriculum text):**
- Platform + catalogs **§1–§5, §6 (pointer), §7–§26:** [`content/spec/agentiq_platform_spec.md`](../content/spec/agentiq_platform_spec.md)
- **§6 module archive** (split source): [`content/curriculum/section-6-modules.md`](../content/curriculum/section-6-modules.md)
- **§27–§73** topic / extract corpus: [`content/research/topic-and-extract-corpus.md`](../content/research/topic-and-extract-corpus.md)

**Canonical delivery** (per-module bodies): [`content/phases/`](../content/phases/) — `P*/modules/*.md`, plus `supplement.md` / `depth/` where generated.
