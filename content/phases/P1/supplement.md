---
kind: phase_supplement
phase_code: P1
---

# Phase P1 — supplemental depth

### AI foundations and terminology

### Core AI Concepts

**AGI (Artificial General Intelligence):** Hypothetical AI systems that match or exceed human-level reasoning across all domains. Contrasted with narrow AI (task-specific). Understanding AGI is foundational for framing where current LLMs and agents sit on the capability spectrum.

**AI Model:** A trained computational system that takes inputs and produces outputs based on learned patterns. Includes LLMs, vision models, embedding models, and multimodal models.

**Machine Learning (ML):** A subfield of AI where systems learn from data rather than explicit programming. Encompasses supervised, unsupervised, and reinforcement learning paradigms.

**Deep Learning:** ML using multi-layer neural networks (deep neural networks) to learn hierarchical representations. Foundation of modern LLMs, vision models, and speech systems.

**Supervised Learning:** Training on labeled input-output pairs to minimize prediction error. Used for classification, regression, and sequence labeling tasks. Tools: scikit-learn, PyTorch, TensorFlow.

**Unsupervised Learning:** Finding structure in unlabeled data — clustering, dimensionality reduction, anomaly detection, and next-token prediction (the basis of LLM pretraining).

**Reinforcement Learning (RL):** Agent learns by taking actions in an environment and receiving rewards or penalties. RLHF (Reinforcement Learning from Human Feedback) is used to align LLMs with human preferences.

**Neural Networks:** Computational graphs of interconnected nodes (neurons). Evolution: RNNs (sequential) → CNNs (spatial) → Transformers (attention-based, parallel). Transformers are the dominant architecture for LLMs.

**Deep Learning Frameworks:** PyTorch (research-first, dynamic graphs), TensorFlow (production-first, static graphs), Keras (high-level API over TensorFlow). All three used in fine-tuning and model training workflows.

**Evaluation Metrics:** MSE/MAE for regression; Precision, Recall, F1, ROC-AUC for classification; ROUGE for summarization; BLEU for translation; BERTScore for semantic similarity. Critical for comparing model versions and measuring fine-tuning success.

### LLM Internals

**Transformer Architecture:** The dominant neural network architecture for LLMs. Key mechanism: self-attention allows every token position to attend to every other position in parallel. Components: embedding layer, multi-head attention, feed-forward layers, positional encoding, layer normalization. Understanding transformers is required for Module 8 (P1).

**Tokenization:** Converting raw text into subword token IDs that models process. BPE (Byte Pair Encoding) is the most common algorithm. tiktoken is OpenAI's tokenizer. Token count directly determines API cost and context window usage. Learners must understand that "tokens != words" — 1 token ≈ 0.75 words in English.

**Embeddings:** Dense vector representations of text (or images) in a high-dimensional space where semantic similarity corresponds to geometric proximity. Used in RAG pipelines, semantic search, clustering, and recommendation. Models: OpenAI text-embedding-3, Cohere Embed, Sentence-BERT (SBERT), BAAI/bge-small.

**Parameters & Weights:** The numerical values inside a neural network that are adjusted during training. A 7B model has 7 billion parameters. Weights encode learned knowledge. Understanding parameter count helps learners reason about model capability, memory requirements, and fine-tuning cost.

**Inference:** Running a trained model on new inputs (forward pass only — no weight updates). Distinct from training. Inference cost = input tokens + output tokens × price per token. Optimization: smaller models, caching, batching, quantization.

**Context Window:** The maximum number of tokens a model can process in a single call — both input and output combined. GPT-4o: 128K tokens. Claude: 200K tokens. Gemini 1.5 Pro: 1M tokens. Exceeding the context window requires chunking, summarization, or sliding window strategies.

**Cost per Token:** API pricing model where you pay for input tokens + output tokens separately. Output tokens are typically 3-5x more expensive than input tokens. Cost optimization strategies: prompt compression, smaller models for easy tasks, caching repeated prompts, batching requests.

**Pretraining vs Fine-tuning:** Pretraining = training from scratch on massive datasets (done by AI labs). Fine-tuning = further training a pretrained model on a smaller domain-specific dataset to adapt style, format, or behavior. Fine-tuning is cheaper than pretraining but more expensive than prompt engineering.

**BERT (Bidirectional Encoder Representations from Transformers):** Google's encoder-only transformer model. Reads text bidirectionally (left and right context simultaneously). Used for classification, NER, question answering. Contrasted with GPT-style decoder-only models used for generation.

### Generative AI

**Generative AI Pipeline:** End-to-end flow: Input Collection → Feature Mapping → Pattern Learning (leveraging pretrained models) → Content Generation (decoding latent features) → Refinement & Filtering (quality control) → Output Rendering → User Feedback loop. Understanding this pipeline helps learners design reliable AI products.

**Types of Generative AI:** Text generation (GPT, Claude, Gemini), Image generation (DALL-E, Stable Diffusion, Midjourney), Audio generation (ElevenLabs, Stable Audio, MusicGen), Code generation (GitHub Copilot, Claude Code), Video generation (Pika, Sora, RunwayML). Each type has different latency, cost, and quality trade-offs.

**GANs & Diffusion Models:** GANs (Generative Adversarial Networks) — generator vs discriminator training loop, used in early image generation. Diffusion Models — iterative denoising process, current state-of-the-art for image/audio generation. Stable Diffusion is the leading open-source diffusion model. DALL-E 3 is OpenAI's image generation model integrated into ChatGPT.

**LLM vs GenAI vs AI Agents vs Agentic AI — 4-Stage Progression:**
- LLM: Text prediction only, no autonomy, no tools, no planning
- Generative AI: Content creation across modalities, user feedback loop, no autonomy
- AI Agents: Task execution, reactive, tool use (API/tool calls), task logging
- Agentic AI: Goal-driven autonomy, proactive, full reasoning and planning, sub-agent delegation, real-time monitoring and self-adjustment

**Hallucination:** When an AI model generates plausible-sounding but factually incorrect information. Causes: training data gaps, overconfident generation, lack of grounding. Mitigation: RAG (grounding in retrieved facts), output validation, citation requirements, human review. Detection: fact-checking agents, reference verification.

**Explainability (XAI):** The ability to understand and interpret AI model decisions. Techniques: attention visualization, SHAP values, LIME, chain-of-thought reasoning. Explainability-by-design means building systems where every AI decision comes with a traceable reason and cited source. Required for regulated industries (finance, healthcare, legal).

**Bias & Fairness:** AI models can produce unfair outcomes due to biased training data, biased labeling, or biased evaluation. Detection: fairness metrics (demographic parity, equalized odds), bias audits. Mitigation: diverse training data, debiasing techniques, human review of high-stakes outputs. Required for responsible AI deployment.

### Compute & Hardware

**Quantization & Pruning:** Quantization reduces weight precision (FP32 → FP16 → INT8 → 4-bit) to shrink model memory footprint and speed up inference. GGUF format bundles quantized weights for llama.cpp. GPTQ and bitsandbytes enable quantized training and inference in Python. Pruning removes low-importance weights to reduce model size. Together these techniques make large models deployable on consumer hardware.

**Knowledge Distillation:** Training a smaller "student" model to mimic the behavior of a larger "teacher" model. The student learns from the teacher's soft probability outputs rather than hard labels. Result: a lighter model that retains most of the teacher's capability. Used when production latency or cost constraints prevent using the full model. Example: DistilBERT is a distilled version of BERT.

### Programming and scripting

### Languages

**JavaScript / TypeScript:** Used for frontend AI applications (Next.js, React), Node.js backend services, and tooling (Claude Code CLI is Node.js-based). TypeScript adds static typing for safer large-scale AI application development. Required for building web-based AI UIs and integrating with browser-based tools.

**Shell / Bash:** Essential for scripting automation, running CLI tools (Ollama, Claude Code, Docker), writing deployment scripts, and chaining commands in CI/CD pipelines. Every AI engineer needs basic shell scripting to automate repetitive tasks and manage local AI environments.

### Python for AI

**Data Structures, Conditionals, Loops, Functions, Lambda:** Python fundamentals required before writing any AI code. Lists, dicts, sets, tuples for data handling. Conditional logic for agent decision branches. Loops for processing batches of documents or API responses. Lambda functions for concise transformations in data pipelines.

**Exception Handling, File Handling:** Try/except blocks for graceful API error handling (rate limits, timeouts, validation errors). File I/O for reading documents, writing logs, saving model outputs. Critical for building robust agent tools that don't crash on unexpected inputs.

**NumPy & Pandas:** NumPy for numerical array operations (embedding math, similarity calculations). Pandas for tabular data manipulation (loading CSVs, filtering datasets, preparing fine-tuning data). Both are prerequisites for data preparation and evaluation workflows.

**Async Programming:** asyncio for concurrent API calls, httpx for async HTTP requests. Essential for building agents that call multiple tools or APIs in parallel without blocking. Dramatically improves throughput in production AI systems that make many LLM calls.

**Web Scraping:** BeautifulSoup for parsing HTML, Playwright for headless browser automation, Firecrawl for AI-friendly content extraction. Used in agent tools that need to gather information from the web. Must respect robots.txt and rate limits.

**API Requests:** HTTP/JSON communication using the requests library (sync) and httpx (async). Understanding REST API patterns, headers, authentication, and response parsing is required for every agent tool that calls external services.

### Curriculum visual map — block A

### Image 1: MCP vs A2A vs Unified AI Architecture

**MCP Architecture (from image):**
- Client Agent → MCP Protocol → HOST (Transport Layer)
- HOST contains 1:1 client-server mapping:
  - MCP Client 1 → MCP Server 1 → DB (structured tool access)
  - MCP Client 2 → MCP Server 2 → API
  - MCP Client 3 → MCP Server 3 → Docs

**A2A Architecture (from image):**
- Client Agent → A2A Protocol → 3–4 Agents (with Agent Cards)
- Communication flow: Task Requests → 3–4 Remote Agents (with Agent Cards) → Result Artifacts returned
- Key concepts: distributed execution, task delegation, Agent Cards

**Unified AI System — Full Stack (from image):**
- User → Orchestrator → Agents Layer (agents communicate via A2A peer-to-peer) → MCP Clients → MCP Servers → Tools & Services (API, databases, external services, security/validation)
- Cross-cutting concerns (vertical):
  - Memory (left side, spanning all layers)
  - Identity / Agent Identity (right side)
  - Observability (Logs / Traces) (right side)
  - Guardrails (right side, bottom)

**Key Insights Table (from image):**
- MCP = tools | A2A = agents | Together = real AI systems
- Shift: Apps → Agents → Multi-Agent Systems → AI Infrastructure
- Design Principle: Communication layer + Capability layer = Production AI

### Image 2: Agentic AI Roadmap 2026

**Legend:** Must Do (Core) | Optional | Tools/Tech

**Programming Languages:**
- Python (Must Do) | JavaScript (Must Do) | TypeScript (Optional) | Shell/Bash (Optional)

**Scripting & Automation:**
- API Requests (HTTP/JSON) (Must Do) | File Handling (Must Do) | Async Programming (Optional) | Web Scraping (Optional)

**Prompting Concepts:**
- Prompt Engineering (Must Do) | Context Management (Must Do) | Chain-of-Thought Prompts (Must Do)
- Multi-Agent Prompts (Must Do) | Goal-Oriented Prompting (Must Do) | Self-Critique & Retry Loops (Must Do)
- Reflexion Looping (Must Do) | Task Planning Prompts (Must Do) | Role Prompting (Must Do)

**Basics of AI Agents:**
- What are AI Agents? (Must Do) | Autonomous vs. Semi-Autonomous Agents (Must Do)
- Agent Architectures (ReAct, CAMEL, AutoGPT) (Must Do)
- Model Context Protocol (MCP) (Must Do) | A2A Protocol (Agent-to-Agent) (Must Do)
- Goal Decomposition (Must Do) | Task Planning Algorithms (Must Do) | Decision-Making Policies (Must Do)
- Action Planning Loops (Must Do) | Multi-Agent Collaboration (Must Do) | Self-Reflection / Feedback Loops (Must Do)

**LLMs & APIs — Providers:**
- OpenAI (GPT-4, GPT-4o) (Must Do)

### Curriculum visual map — block B

### Agentic AI Roadmap 2026 — Full Categorized List

**LLMs & APIs — Providers (Must Do):**
- Claude (Must Do) | Gemini (Must Do) | Mistral (Must Do)
- Open Source LLMs (LLaMA, DeepSeek, Falcon) (Must Do)

**LLMs & APIs — API Skills:**
- API Authentication (Must Do) | Rate Limiting (Must Do)
- Toolformer / Function Calling (Must Do)
- Tool Invocation & Output Parsing (Must Do)
- Prompt Chaining via APIs (Must Do)

**Tool Use & Integration:**
- Tool Use System (Must Do) | Memory Integration (Must Do) | External API Calling (Must Do)
- File Reader / Writer Tools (Must Do) | Python Execution Tools (Must Do)
- Search & Retrieval Tools (Must Do) | Calculator & Code Interpreter (Must Do) | Web Browsing Tools (Must Do)

**Agent Frameworks:**
- LangChain (Must Do) | AutoGen (Must Do) | CrewAI (Must Do) | Flowise (Optional)
- AgentOps (Must Do) | Haystack (Optional) | Semantic Kernel (Optional) | Superagent (Optional) | LlamaIndex (Must Do)

**Orchestration & Automation:**
- n8n (Must Do) | Make.com (Optional) | Zapier (Optional) | LangGraph (Must Do)
- DAG Management (Must Do) | Event-Based Triggers (Must Do)
- Guardrails & Validations (Must Do) | Looping & Conditional Workflows (Must Do)

**Memory Management:**
- Short-Term Memory (Must Do) | Long-Term Memory (Must Do) | Episodic Memory (Must Do) | Vector Stores (Must Do)
- Pinecone (Tools/Tech) | Weaviate (Tools/Tech) | Chroma (Tools/Tech) | FAISS (Tools/Tech)

**Knowledge & RAG:**
- RAG (Retrieval-Augmented Generation) (Must Do) | Embedding Models (Must Do) | Custom Data Loaders (Must Do)
- Document Indexing (Must Do) | Query Refinement (Must Do) | Hybrid Search (Must Do)
- LangChain RAG (Tools/Tech) | LlamaIndex RAG (Tools/Tech)

**Deployment:**
- API Deployment (Must Do) | Serverless Functions (Must Do) | FastAPI / Streamlit / Gradio (Tools/Tech)
- Docker (Must Do) | Kubernetes (Optional) | Vector DB Hosting (Must Do)
- Agent Hosting Services (Replit, Modal, etc.) (Optional)

**Monitoring & Evaluation:**
- Agent Evaluation Metrics (Must Do) | Human-in-the-Loop Feedback (Must Do) | LangSmith (Tools/Tech)
- Logging / Tracing (Must Do) | Auto-Evaluation Loops (Must Do)
- OpenTelemetry (Tools/Tech) | Prometheus / Grafana (Tools/Tech) | Custom Dashboards (Optional)

**Security & Governance:**
- Prompt Injection Protection (Must Do) | API Key Management (Must Do) | User Authentication (Must Do)
- Role-Based Access Control (RBAC) (Must Do) | Output Filtering (Must Do)
- Red Team Testing (Must Do) | Data Privacy & Compliance (Must Do)

### Core concept refresher

### Core AI Concepts — Combined Reference

**AGI, AI Model, Machine Learning, Deep Learning:** These four terms form the conceptual foundation. AGI = hypothetical human-level AI. AI Model = any trained system producing outputs from inputs. Machine Learning = systems that learn from data. Deep Learning = ML using multi-layer neural networks. Every learner must be able to define all four in under 30 seconds before proceeding to later phases.

**Types: Text, Image, Audio, Code Generation:** The four primary output modalities of generative AI. Text: GPT-4, Claude, Gemini. Image: DALL-E 3, Stable Diffusion, Midjourney. Audio: ElevenLabs, Stable Audio, MusicGen. Code: GitHub Copilot, Claude Code, Cursor. Each modality has different latency, cost, quality, and use case characteristics. Multimodal models (Gemini 1.5 Pro, GPT-4o) handle multiple modalities in a single model.

**GPT-4V, Gemini Multimodal, Pika Video, ElevenLabs Audio:** The leading tools for each multimodal output type. GPT-4V: vision understanding (analyze images, charts, screenshots). Gemini 1.5 Pro: multimodal reasoning across text, images, audio, and video in a 1M token context. Pika: text-to-video and image-to-video generation. ElevenLabs: text-to-speech with voice cloning, used in Capstone 1 for agent voice escalation.

**In-Context Memory vs In-Cache vs In-Storage:** Three memory tiers in Claude Code's architecture. In-context (temporary): lives in the current prompt window, fastest access, lost when session ends, costs tokens every call. In-cache (session): stored via prompt caching, persists during a work session, 90% cost reduction for repeated content, cleared when cache expires. In-storage (long-term): written to CLAUDE.md or external database, persists across all sessions and all users, slowest to retrieve but permanent.

**Module 3 — The Pathway to GenAI:** Introduction to Generative AI, Discriminative vs Generative AI. History of GenAI, LLM models. How models understand text, how models predict the next word. Business problems to solve, applications in software development. Transformers for Generative AI: Introduction to Transformers, Sequential deep learning, Need for transformer models, Attention, self-attention, multi-head attention.


### Syllabus theme — day 1

**Day 1 — AI Basics:** Chronology of AI advancements: Machine Learning → Deep Learning → Computer Vision, NLP → LLMs. Evolution in Deep Learning Architectures: RNNs to Transformers. Deep Learning Frameworks: PyTorch, TensorFlow, and Keras introduction. Evaluation Metrics: MSE, MAE, Precision, Recall, ROC, AUC, F1 Score, ROUGE and BLEU for GenAI. Responsible AI and Explainability.

### Syllabus theme — day 6

**Day 6 — Introduction to Generative AI:** What is Generative AI? Types: Text, Image, Audio, Code generation. Key models: GPT, DALL·E, Codex, Stable Diffusion (Diffusion, GANs, Transformers). Applications in enterprise AI (use cases across industries).

### Syllabus theme — day 7

**Day 7 — LLM Fundamentals:** Anatomy of LLMs (GPT, BERT, LLaMA). Transformer architecture basics. Pretraining vs. fine-tuning. Tokenization, embeddings. Exercise: Explore GPT via playground or API.

**Phase 0: Local LLM Dev Lab**
- Ollama setup & local model running (llama4, gemma3, phi4, mistral)
- Ollama as OpenAI-compatible API (`http://localhost:11434/v1`)
- Python integration — drop-in OpenAI replacement (2-line change)
- LM Studio — visual model browser, quantization selection (Q4_K_M), local server
- LM Studio + LangChain integration
- Free Cloud API Stack: Groq (14,400 req/day, 300+ tok/sec), Google AI Studio (1M tokens/min, Gemini 2.5 Flash), Mistral (1B tokens/month free), OpenRouter (30+ free models), Cerebras (ultra-fast inference)
- LiteLLM routing with fallback between providers
- Certifications: NVIDIA DLI (Jetson Nano), HuggingFace LLM Course


- RAG pipeline: compliance docs (RBI, PCI-DSS) ingested into vector DB
- LLM: Claude or GPT-4 for risk reasoning and report generation
- Fraud detection: rule-based + LLM-based dual-layer analysis
- FastAPI REST endpoints + Streamlit dashboard
- Features: real-time risk scoring (0–100), compliance rule retrieval, explainable

