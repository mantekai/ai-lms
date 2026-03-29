---
kind: phase_supplement
phase_code: P7
---

# Phase P7 — supplemental depth

### RAG and knowledge systems

### RAG Architecture

**RAG vs Fine-tuning Decision Framework:** When to use RAG vs fine-tuning: Use RAG when knowledge changes frequently (news, policies, product catalogs), when you need citations, when data is too large for context window, or when you need to keep data private. Use fine-tuning when you need consistent style/format, when the task is highly specialized, or when latency is critical and RAG retrieval adds too much overhead. Most production systems use RAG first and fine-tune only when RAG is insufficient.

**Agentic RAG:** A RAG pattern where an agent actively decides how to retrieve information rather than using a fixed retrieval pipeline. The agent can: reformulate the query, choose between multiple retrieval sources, decide whether to retrieve at all, or chain multiple retrievals. More flexible than naive RAG but adds complexity and latency.

**Adaptive RAG:** A specific agentic RAG pattern with a router agent that classifies the query and selects the optimal retrieval strategy: direct retrieval for simple factual queries, iterative retrieval for complex multi-hop questions, or web search for time-sensitive queries. Improves retrieval quality by matching strategy to query type.

**RAGAS Evaluation Suite:** A framework for evaluating RAG pipeline quality. Key metrics: Faithfulness (does the answer only use retrieved context?), Answer Relevance (does the answer address the question?), Context Precision (are retrieved chunks relevant?), Context Recall (were all relevant chunks retrieved?). Used to benchmark RAG pipeline improvements and catch regressions.

### Embeddings & Search

**BM25 Keyword Search:** A classical information retrieval algorithm based on term frequency and inverse document frequency. Excels at exact keyword matching and rare term retrieval. Combined with dense vector search in hybrid search systems. BM25 handles cases where semantic search fails — proper nouns, product codes, technical terms that don't have semantic neighbors.

### Document Processing

**LangChain Text Splitters:** RecursiveCharacterTextSplitter (splits on paragraph → sentence → word boundaries, most versatile), TokenTextSplitter (splits by token count, precise for context window management), SemanticChunker (splits at semantic boundaries using embedding similarity, best quality but slower). Chunk size and overlap are the key parameters — larger chunks preserve context, smaller chunks improve retrieval precision.

**Unstructured Library:** Open-source library for parsing complex document formats — PDFs (including scanned), Word documents, PowerPoint, HTML, email, images with OCR. Handles table extraction, header/footer removal, and metadata extraction. Used when LangChain's built-in loaders produce poor quality output for complex documents.

**OCR & Document Intelligence:** Optical Character Recognition converts scanned images and PDFs into machine-readable text. Tools: PyMuPDF (fast PDF text extraction), Tesseract (open-source OCR engine), PyPDF (pure Python PDF parsing). Cloud services: Azure Document Intelligence (handles complex layouts, tables, forms). Required for processing legacy documents, invoices, contracts, and scanned records.

**Metadata Extraction & Enrichment:** Attaching structured metadata to document chunks during ingestion — source file, page number, section title, date, author, document type. Metadata enables filtered retrieval (e.g., "only search documents from 2024") and improves citation quality. Enrichment: using an LLM to extract additional metadata (key entities, topics, sentiment) from each chunk.

**Synthetic Data Generation:** Using LLMs to generate training data, evaluation sets, or test cases. Applications: generating question-answer pairs from documents for RAG evaluation, creating diverse examples for fine-tuning, augmenting small datasets. Tools: LangChain's QAGenerationChain, custom prompts. Quality control: human review of a sample, deduplication, diversity checks.

### Knowledge Graphs

**Entity Relationships, Ontologies, Graph Traversal:** Knowledge graphs model entities (people, places, concepts) and their relationships as nodes and edges. Ontologies define the schema — what types of entities exist and what relationships are valid. Graph traversal (BFS, DFS, shortest path) enables multi-hop reasoning: "Who are the colleagues of the author of this paper who also work on RAG?" Vector search cannot answer this; graph traversal can.

### Curriculum visual map — block F

### Image 8: Claude Code — Sections 6-9 (Exact from Image)

**Section 6 — MCP Integration:** Claude Core ↔ MCP Servers ↔ APIs / DB / Tools. Benefits: real-time data access, external grounding reduces hallucination, grounded AI responses.

**Section 7 — Hooks & Guardrails:** Event → Hook → Action. Use cases: linting, security checks, validation, policy enforcement. Key insight: "Hooks = safety."

**Section 9 — Iteration System:** Build → Review → Checkpoint → Rewind → Build... Safe experimentation through checkpoints and rewind capability.

### Image 9: The Complete Agentic AI Infrastructure Stack (2026) — Exact Layer Descriptions

**Layer 1 — User Layer:** Humans initiate tasks, but agents increasingly execute them autonomously. Components: Developer Copilots → AI Assistants → Enterprise Chat Systems → Automation Workflows.

**Layer 2 — AI Agent Layer:** Agents reason, plan, and take actions across infrastructure. Components: Research Agents → Coding Agents → Data Agents → Automation Agents → DevOps Agents.

**Layer 3 — Agent Orchestration:** Orchestration frameworks coordinate multi-agent workflows. Components: Task Planners → Workflow Engines → Agent Collaboration.

**Layer 4 — Model Layer:** Foundation models power reasoning and decision-making. Components: AI Model Infrastructure → LLMs → Reasoning Models → Embedding Models → Multimodal Models.

**Layer 5 — Context and Knowledge:** Agents retrieve context to make informed decisions. Components: Knowledge Infrastructure → Vector Databases → Knowledge Graphs → Document Stores → Search Systems.

**Layer 6 — Tooling Layer:** Agents perform real actions through tools and integrations. Components: Agents → APIs → Databases → Git Repositories → File Systems → Cloud Services.

**Layer 7 — Identity and Access Layer:** Secure identity ensures agents access infrastructure safely and transparently. Sub-sections: Cryptographic Identity | Policy Enforcement | Infrastructure Access. Flow: Agents → Identity Issuance → Access Authorization → Runtime Enforcement → Audit Logging. Note: "Teleport fits!" — this layer maps to Teleport's agentic identity framework.

**Layer 8 — Infrastructure Layer:** Infrastructure executes actions initiated by AI agents. Components: Kubernetes Clusters → Cloud Platforms → Databases → Storage Systems → Developer Tooling.

**Layer 9 — Observability and Governance:** Observability ensures accountability and governance for agent actions. Components: Agent Activity Logs → Policy Enforcement → Access Analytics.

### Image 10: Traditional Coding

**Traditional Coding (CODE):** Writing logic manually using programming languages, frameworks, and APIs. Key features: full control over logic, custom architectures, requires deep technical skill, high performance, unlimited flexibility. Used for: custom AI agents, backend services & APIs, building full SaaS products, complex integrations, high-performance systems.

### Week 4 — RAG and Multi-Agent Systems


### Syllabus theme — day 9

**Day 9 — RAG & Vector Databases:** RAG architecture and flow. Vector DBs: Pinecone, Weaviate, FAISS, Azure AI Search. Indexing, retrieval, and latency considerations. Exercise: Build a RAG pipeline using LangChain + Azure AI Search.

**Phase 4: RAG & Vector Databases**
- Full local RAG pipeline ($0): PyPDFLoader → RecursiveCharacterTextSplitter → HuggingFaceEmbeddings (BAAI/bge-small) → Chroma → Ollama → RetrievalQA
- Chunking strategy guide: fixed-size, semantic, hierarchical
- Hybrid search (BM25 + semantic, +23% accuracy)
- RAGAS evaluation suite
- Agentic RAG with router agents
- Certifications: DeepLearning.AI Building Systems with ChatGPT API (free), Weaviate Academy RAG (free)


**Platform Architecture:** Single HTML5 shell (`index.html`) loading data from `data/*.json` and `data/catalog/*.csv`. 9 navigation pages: Dashboard, Topic Coverage, All Phases, Capstones, Hackathons, Open Source, YC Ideas, Cert Tracker, Career. 5 themes: Dark, Light, Ocean, Mint, Sunset. Progress tracking via localStorage with JSON/CSV import/export. Each module has: Learn tab, Steps tab, Code tab, References tab. All 133 modules are self-contained on-page with full content tier.


- Document ingestion: policy PDFs → chunked → embedded → vector store
- Transaction scoring: synthetic transactions scored against compliance rules
- Explainable reports: cited clauses from source documents
- Streamlit dashboard for stakeholder review
- Claude or GPT-4 for reasoning, FastAPI for API layer


- Exercise: Detect biased outputs; test content moderation; build RAG app with saf


- Exercise: Upload image, PDF, JSON to Azure Blob Storage; explore Cosmos DB Data


- Exercise: Create Azure Storage Queue, write Python script to enqueue/dequeue; cr


- Supervised / Unsupervised / Reinforcement Learning
- Inference, Context, Explainability, Hallucination, RAG, Chain-of-Thought (CoT),
- Fine-tuning, Prompt Engineering, Tokenization, Parameters, Weights, Embedding, Q
- GPU, TPU, Compute, Transformer architecture
- MCP (Model Context Protocol), API, Computer Vision, NLP, Chatbots
- Generative AI, Vibe Coding, AI Agent
- AI Alignment, Training Data quality, Bias, Privacy, Regulation


- Cloud SDKs: AWS SDK, Azure SDK
- Used for: Custom AI agents, backend services, complex integrations, high-perform
- Tools: Claude Code, GitHub Copilot, Cursor AI, Replit AI, Tabnine, Codeium
- AI writes most of the code; human reviews + edits
- Tools: Zapier, Make.com, n8n, ServiceNow Flow Designer, Power Automate, Webflow,
- Zero coding required; drag-and-drop; AI handles logic


- Core AI: AGI, AI model, ML, Deep Learning, Supervised/Unsupervised Learning, RL
- Inference & Behaviour: Inference, Context, Explainability, Hallucination, RAG, C
- Training & Hardware: Fine-tuning, Prompt Engineering, Tokenization, Parameters,
- Tools & Protocols: MCP, API, Computer Vision, NLP, Chatbot, Generative AI, Vibe
- Ethics & Safety: AI Alignment, Training Data Quality, Bias, Privacy, Regulation
- Code sample: tiktoken tokenization demo
- Self-attention mechanism: every position attends to every other position in para
- Tools: Hugging Face ecosystem, tiktoken
- Dense vectors representing text in a space where similar meanings are closer
- Used for search, clustering, and RAG pipelines
- Tools: OpenAI Embeddings, Sentence-BERT (SBERT)
- Running trained models on new inputs (forward pass), no weight updates
- Context window = max tokens model can attend to in one call
- Cost = input tokens + output tokens; optimization via shorter prompts, smaller m
- Tools: Token counters, model APIs
- Representing weights/activations in lower precision (8-bit, 4-bit) to shrink mem
- Common for local deployment: GGUF, GPTQ, bitsandbytes
- GPU: parallel processor for matrix math in training/inference
- TPU: Google's ASIC for large matrix workloads
- Tools: CUDA, Google Colab, RunPod
- Supervised: labeled pairs (input, correct output), minimize prediction error
- Unsupervised: no labels — clustering, dimensionality reduction, next-token predi
- Reinforcement Learning: agent learns via actions/rewards; RLHF for LLM alignment
- Tools: scikit-learn, OpenAI Gym
- Systems that synthesize new content from learned patterns
- Full pipeline: input collection → feature mapping → pattern learning → content g
- Tools: OpenAI API, LangChain


- Async Python web framework with automatic OpenAPI docs
- Pydantic models for request/response validation
- uvicorn ASGI server for production deployment
- Streamlit: Python-first web apps for data/AI
- Gradio: quick ML demo interfaces with sharing
- Rapid prototyping for stakeholder demos
- AWS Lambda: event-driven compute
- Vercel Edge: edge-deployed functions
- Modal: serverless GPU compute for AI workloads
- Containerization for reproducible AI environments
- docker-compose for multi-service stacks
- GPU passthrough, volume mounts, networking
- Container orchestration at scale
- Helm charts for AI service deployment
- Auto-scaling, rolling updates, resource management
- Pinecone cloud: managed vector database service
- Weaviate cloud: managed open-source vector DB
- Scaling, indexing, backup, monitoring considerations
- Replit: browser-based development and hosting
- Modal: serverless Python with GPU support
- Fly.io: edge-deployed application hosting
- Choosing hosting based on latency, cost, GPU needs


- Human-in-the-loop voice escalation blueprint
- Demonstrates: orchestration, HitL, telephony integration, production-style state
- Stack: LangGraph + Twilio Voice + FastAPI + Ollama + Redis
- RAG + compliance reasoning + reporting
- Ingest policy/compliance text into vector store, score synthetic transactions, p
- Demonstrates: RAG, structured risk output, stakeholder-facing UI — common enterp
- Stack: FastAPI + Vector DB + RAG + Streamlit + Claude or GPT-4
- Ollama + SearXNG + cited answers
- Self-hosted meta-search plus local LLM to synthesize answers with source cards —
- Demonstrates: privacy-preserving research tooling entirely on your hardware
- Stack: Ollama + SearXNG + Docker + Streamlit + LangChain


- Chat completions, embeddings, speech endpoints
- openai Python SDK patterns, streaming, structured outputs
- anthropic Python SDK, tool_use, system prompts, long context
- Safety features and content policy handling
- google-generativeai SDK, multimodal inputs, Vertex AI integration
- Hugging Face ecosystem, mistralai SDK
- Running and comparing open-weight models
- API key management, exponential backoff, tenacity library
- Burst vs sustained rate limits across providers
- OpenAI tools parameter, Claude tool_use
- Defining function schemas for model invocation
- Pydantic models for structured output validation
- json_schema enforcement, LangChain output parsers
- GPT-4V vision, Gemini multimodal, Pika video, ElevenLabs audio
- Cross-modal pipelines and use cases


- Retrieve relevant chunks → inject into prompt → generate grounded answer
- Reduces hallucination by grounding in your data
- End-to-end pipeline: ingest → chunk → embed → store → retrieve → generate
- OpenAI embeddings, Cohere embed, Sentence-BERT
- Cosine similarity, nearest-neighbor search
- Choosing embedding dimensions and models for your use case
- LangChain text splitters: recursive character, token-based, semantic
- Chunk size vs overlap trade-offs
- Custom chunking logic for structured documents
- LangChain document loaders for PDF, HTML, CSV, databases
- Unstructured library for complex document parsing
- Metadata extraction and enrichment
- Pinecone: managed cloud vector DB
- Weaviate: open-source with hybrid search
- Chroma: lightweight local vector store
- FAISS: Facebook's similarity search library
- Comparison: managed vs self-hosted, filtering, scale
- BM25 (keyword) + dense retrieval (semantic) = hybrid search
- Rerankers: cross-encoder reranking for precision
- Query expansion, HyDE (Hypothetical Document Embeddings)
- Neo4j graph database, NetworkX for Python
- Graph RAG: combining knowledge graphs with retrieval


- Single HTML5 shell (`index.html`) loading data from `data/*.json` and `data/cata
- Single self-contained HTML file (Vanilla JS + CSS, no build tools)
- Claude-style left sidebar (collapsible, persistent), page-based SPA navigation
- tabs per module: Learn · Steps · Code · References
- themes (Light, Dark, Solarized, Dracula, High Contrast) via CSS variables
- Progress tracking via localStorage with CSV import/export
- Code highlighting via Prism.js; fonts: Inter + JetBrains Mono


- Single self-contained HTML file — all CSS, JavaScript, and content embedded inli
- Works offline, shareable as a single file, no installation required
- Claude-style left sidebar with collapsible phase groups
- Sidebar: logo + progress summary (X of 133 completed), scrollable phase list, ut
- Each module shows: module number, name, completion checkbox, priority tag
- Learn · Steps · Code · References
- Boolean completion state per module stored in localStorage
- Phase-level % complete shown as progress bar
- Global: total modules completed / 133
- Export/Import via CSV; one-click reset with confirmation


- Total Modules: 133
- Total Phases: 20 (P0–P19)
- MUST DO modules: 115
- OPTIONAL modules: 18
- Content Tier: All modules are "full" with self-contained on-page content
- Capstone Projects: 3 (Advanced to Intermediate)
- Hackathons: 7 recurring opportunities
- Open Source Projects: 5 contribution targets
- YC Startup Ideas: 5 concepts with MVP timelines
- Certifications: 7 paid credentials + 23 free learning paths
- Themes: 5 (Dark, Light, Ocean, Mint, Sunset)
- Navigation Pages: 9 (Dashboard, Coverage, Phases, Capstones, Hackathons, OSS, YC


- Two-column: 280px fixed sidebar + main content area
- Below 768px: sidebar collapses to hamburger menu
- built-in themes selectable via dropdown, persisted to localStorage
- Font: Inter (body), JetBrains Mono (code blocks)
- Sidebar: 280px fixed, collapses to 48px icon-only on toggle
- Module cards: 12px border-radius, subtle box-shadow, hover state
- Code blocks: dark background, Prism.js syntax highlighting, copy button


### Week 4 — RAG and Multi-Agent Systems

