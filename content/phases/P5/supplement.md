---
kind: phase_supplement
phase_code: P5
---

# Phase P5 — supplemental depth

### Tool use and integration

### Tool System Design

**Tool Decorators & Registration:** LangChain provides `@tool` decorator to convert any Python function into an agent-callable tool. The function's docstring becomes the tool description that the model uses to decide when to call it. OpenAI tools parameter accepts a list of JSON schema tool definitions. Tool description quality directly determines how reliably the model selects the right tool.

**Calculator & Code Interpreter:** A sandboxed Python execution environment that agents can use to perform calculations, data analysis, and code generation. E2B provides cloud-based sandboxes with network isolation. Docker-based local sandboxes provide full control. The code interpreter tool is what makes agents capable of solving math problems, analyzing data, and generating charts without hallucinating results.

### Memory Systems

**Short-Term Memory:** Conversation buffer stored in the current session context. Contains the recent message history. Limited by the context window. Managed by LangChain's ConversationBufferMemory or ConversationSummaryMemory (which summarizes older turns to save tokens). Cleared when the session ends.

**Long-Term Memory:** Persistent storage of facts, preferences, and knowledge across sessions. Stored in vector databases (for semantic retrieval) or relational databases (for structured facts). The agent retrieves relevant memories at the start of each session. Tools: mem0 (memory layer for AI agents), LangChain VectorStoreRetrieverMemory.

**Episodic Memory:** Storage of past task executions — what the agent did, what tools it called, what results it got, and what the outcome was. Enables agents to learn from past experience and avoid repeating mistakes. Stored as structured records with timestamps, task descriptions, and outcomes.

**3-Tier Memory Architecture:** Production memory design: Tier 1 (Hot) — Redis for session context, fast reads, TTL-based expiry. Tier 2 (Warm) — PostgreSQL for structured user preferences and task history, queryable. Tier 3 (Cold) — Vector database for semantic long-term memory, retrieved by similarity search. Each tier has different latency, cost, and retention characteristics.

**In-Context Memory vs In-Cache vs In-Storage:** Three memory locations in Claude Code's architecture. In-context: temporary, lives in the current prompt window, lost after session. In-cache: session-level, persisted during a work session via prompt caching, faster and cheaper than re-sending. In-storage: long-term, written to CLAUDE.md or external storage, persists across all sessions.

**Secure Memory Management:** Buffer vs summary memory trade-offs for security: buffer memory retains full conversation history (PII risk), summary memory compresses history (reduces PII exposure but loses detail). Session isolation: each user's memory must be strictly isolated — no cross-tenant memory leakage. Memory eviction on account deletion (GDPR right to erasure).

### Middleware & Infrastructure

**Message Queuing:** Decoupling agent components using message queues. Azure Queue Services and Service Bus (or equivalent: AWS SQS, RabbitMQ, Redis Streams) allow agents to communicate asynchronously without direct coupling. Producer agents write tasks to the queue; consumer agents pick them up when ready. Enables horizontal scaling and fault tolerance in multi-agent systems.

### Syllabus theme — day 16

**Day 16 — Tools, APIs & Middleware Integration:** Memory, tool orchestration, and agent chaining. Connecting agents to APIs, databases, and external tools. Middleware components: Redis, FastAPI, event queues. Exercise: Integrate an agent with a backend API and Redis memory.
