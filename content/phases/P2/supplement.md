---
kind: phase_supplement
phase_code: P2
---

# Phase P2 — supplemental depth

### Prompt engineering depth

### Fundamentals

**Prompt Anatomy — Role + Context + Task + Format:** The four pillars of a well-structured prompt. Role: who the model should act as ("You are a senior Python engineer"). Context: background information the model needs. Task: the specific instruction. Format: how the output should be structured (JSON, bullet list, markdown). Mastering this structure is the highest-ROI skill for most AI products.

**System Prompts:** Instructions placed in the system message that define the model's persona, constraints, and behavior for the entire conversation. Used to set tone, restrict topics, enforce output formats, and inject domain knowledge. XML tags (Anthropic method) improve structure: `<role>`, `<context>`, `<instructions>`, `<output_format>`.

**Zero-Shot Prompting:** Asking the model to perform a task with no examples — relying entirely on its pretrained knowledge. Works well for common tasks. Fails on domain-specific formats or unusual output structures. Starting point before adding few-shot examples.

**Few-Shot Prompting:** Providing 2-5 input→output example pairs in the prompt to demonstrate the desired format and behavior. Reduces format errors by approximately 60%. Critical for structured output tasks where zero-shot produces inconsistent results.

**Goal-Oriented Prompting:** Framing prompts around the desired outcome rather than the process. "Produce a risk assessment with score, rationale, and recommended action" rather than "analyze this transaction." Forces the model to work backward from the goal.

### Advanced Techniques

**Tree-of-Thought (ToT):** Extension of Chain-of-Thought where the model explores multiple reasoning branches simultaneously and selects the best path. Useful for complex planning and optimization problems where a single reasoning chain may miss better solutions.

**Rephrase & Respond:** A prompt reformulation technique where the model first rephrases the question in its own words before answering. Improves comprehension of ambiguous or complex questions. Reduces misinterpretation errors.

**Self-Critique & Retry Loops:** The model generates an output, then critiques it against a rubric, then revises. Implemented as a loop with a maximum iteration count (typically 2-3 revisions). Improves output quality without human intervention. Tools: LangGraph for stateful loops, custom Python for simple cases.

**Reflexion Loop:** A specific self-critique pattern: Generate → Evaluate (score 1-10) → Reflect (what was wrong) → Regenerate. Loop continues until score meets threshold (e.g., ≥8) or max iterations reached. Produces measurably better outputs on writing, code, and analysis tasks.

**Multi-Agent Prompts:** Designing prompts that coordinate multiple agents toward a shared goal. Each agent has a specific role (researcher, writer, critic, validator). Hand-off prompts define what each agent receives and what it must produce. Frameworks: CrewAI, AutoGen.

**Dynamic XML Templates:** Function-based prompt construction where variables are injected into XML-structured templates at runtime. Example: a document analysis template that accepts `{document_type}`, `{jurisdiction}`, `{analysis_depth}` as parameters. Enables reusable, parameterized prompts across different use cases.

**XML Tags for Structure:** Anthropic's recommended approach for structuring complex prompts. Tags like `<context>`, `<task>`, `<format>`, `<example>`, `<thinking>` help the model parse and respond to different sections of a long prompt. Reduces confusion in multi-part instructions.

**LLM as a Judge:** Using one LLM to evaluate the output of another LLM. The judge model scores outputs on dimensions like accuracy, relevance, tone, and format. Used in auto-evaluation loops, A/B testing of prompts, and continuous quality monitoring in production.

**Prompt Tuning:** A parameter-efficient technique where a small set of learnable "soft prompt" tokens are prepended to the input and trained while the base model weights remain frozen. Different from prompt engineering (no training required). Used when consistent behavior is needed across many similar tasks.

### Optimization

**Temperature & Model Selection:** Temperature controls output randomness (0 = deterministic, 1 = creative). Model selection trade-offs: Claude Haiku (fast, cheap, simple tasks) → Claude Sonnet (balanced, most use cases) → Claude Opus (most capable, complex reasoning). Choosing the right model for each task is a key cost optimization skill.

**Rate Limits & Cost Management:** Every API provider enforces rate limits (requests per minute, tokens per minute, requests per day). Strategies: exponential backoff with jitter for 429 errors, request queuing, caching repeated prompts, using smaller models for high-volume low-complexity tasks, monitoring spend with dashboards.

**Prompt Evaluation & Debugging:** Systematic testing of prompts using evaluation sets (golden examples with expected outputs). Tools: LangSmith for tracing, PromptLayer for versioning, custom eval scripts. Process: write prompt → test on 20+ examples → measure pass rate → iterate → version control the prompt.

### Week 2 — GenAI Solution Design and Prompt Engineering


### Week 3 — Client Discovery & Prompt Engineering


**Module 5 — Prompt Engineering with Azure OpenAI:** Best practices for structuring prompts. Important prompt templates: Zero-shot, Few-shot, Chain-of-thought, Tree-of-thought, Self-consistency, Rephrase & Respond. Designing prompts to evaluate LLM outputs (LLM as a judge). Role-based and context-aware prompt design using Azure OpenAI SDK. Managing API rate limits, cost, and latency trade-offs. Building prompt chains and dynamic prompts with conditional logic.


**Module 11 — Designing for Governance & Reliability:** Risk mitigation in agent design: guardrails, output filtering, human-in-loop checkpoints. Designing for observability: telemetry hooks, prompt logging. Explainability-by-design principles. Safe interaction design and fallback routing.


### Syllabus theme — day 8

**Day 8 — Prompt Engineering & Model APIs:** Prompt types: zero-shot, few-shot, chain-of-thought. Prompt tuning. Prompt design principles. Prompt evaluation & debugging. Tools: LangChain, PromptLayer. Using OpenAI, Azure OpenAI, Anthropic APIs.

**Phase 2: Prompt Engineering**
- XML Tags & Structured Prompts (Anthropic method) — `<role>`, `<context>`, `<instructions>`, `<output_format>`
- Dynamic XML with variables — template functions for document analysis
- Chain-of-Thought + Self-Critique pattern — `<thinking_process>` + `<self_critique>` tags
- Reflexion Loop — iterative quality improvement with score threshold (rate 1-10, DONE if ≥8)
- Certifications: Anthropic Prompt Engineering (free), Google Prompting Essentials (free), NVIDIA Prompt Engineering with LLMs (free), DeepLearning.AI Prompt Engineering for Developers (free)


**Topics Unique to This Roadmap:**
- LiteLLM routing with fallback — multi-provider routing with automatic failover
- Cerebras — ultra-fast inference provider
- Reflexion Loop implementation — iterative self-critique with score threshold and automatic revision
- Dynamic XML prompt templates — function-based prompt construction with variable injection
- n8n + Ollama local integration — $0 workflow automation with local LLM
- Prompt injection regex defense — specific detection patterns and XML wrapping countermeasures
- Financial Risk Monitor capstone — fintech-specific agent with Redis Streams, Pinecone similarity, AML/fraud detection
- Certification ROI rankings — salary uplift percentages and job placement rates for each cert
- HITL voice escalation — Twilio Voice + LangGraph + Redis checkpointer for phone-based agent decisions
- Free tier comparison table — Groq (14,400 req/day), Google AI Studio (1M tok/min), Mistral (1B tok/month), OpenRouter (30+ free models)


- What it is:** The art of designing structured prompts to guide AI effectively
- When to use it:** Whenever you need precision, creativity, or technical accuracy


- Organiser: Anthropic
- Prep modules: Complete P2 Prompting + P16 Security modules first
- Quick-start template: Guardrailed agent + eval harness + short policy doc
- Past winners: Winning teams often combine strong eval metrics with crisp demos (


### Day 8 — Prompt Engineering & Model APIs


### IMAGE 9 — Claude Code Best Practices: Prompts → Agentic Systems


- Module 15: Prompt Engineering Fundamentals [Core] | Tools: Claude, GPT-4, Prompt
- Module 16: Chain-of-Thought (CoT) Prompting [Core] | Tools: GPT-4o, Claude, Gemi


- ❌ **Big Prompt Chaos** — Big prompt chaos, leadabert commands, skills, messy sum
- ✅ **Structured Context** — Commands, Skills, Memory, Subagents


- Use cases: code review, debugging, documentation, architecture
- Key insight: "Stop rewriting prompts every time"


- Tree-of-Thought prompting** — not explicitly covered in current prompt engineeri
- Self-consistency prompting** — not explicitly covered
- PII Redaction** — logging, tracing, and redacting PII in agent pipelines


### Week 2 — GenAI Solution Design and Prompt Engineering

