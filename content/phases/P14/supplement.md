---
kind: phase_supplement
phase_code: P14
---

# Phase P14 — supplemental depth

### Production deployment

### APIs & UIs

**CI/CD for AI:** Continuous Integration and Continuous Deployment pipelines for AI systems. Key stages: code commit → automated tests (unit, integration, eval) → Docker build → security scan → staging deployment → eval regression check → production deployment. Tools: GitHub Actions, GitLab CI. AI-specific additions: prompt regression tests, model evaluation gates, A/B deployment for model versions.

### Containerization & Hosting

**Deployment to Cloud:** Deploying containerized AI applications to cloud platforms. Options: managed container services (equivalent to Azure Container Apps, AWS ECS, Google Cloud Run), virtual machines with Docker, Kubernetes clusters. Key considerations: GPU availability for inference, cold start latency, auto-scaling policies, cost per request, data residency requirements.

### MLOps

**MLOps / MLflow:** MLOps is the practice of applying DevOps principles to machine learning. MLflow is the leading open-source MLOps platform. Key capabilities: Experiment Tracking (log parameters, metrics, artifacts for each training run), Model Registry (version and stage models: Staging → Production), Model Serving (deploy models as REST APIs), Monitoring (track model performance in production). Essential for teams managing multiple model versions.

**Model Lifecycle:** The stages a model goes through: Development (experimentation, training, evaluation) → Release (packaging, versioning, documentation) → Productionization (deployment, monitoring, A/B testing) → Retirement (deprecation, migration to new model). MLflow manages this lifecycle with model stages and transition workflows.

**CI/CD Pipeline for AI:** Automated pipeline: code push → lint/format check → unit tests → integration tests → Docker build → push to registry → deploy to staging → run eval suite → if eval passes → deploy to production → monitor metrics → alert on regression. The eval suite is the AI-specific addition — it runs a set of golden examples through the model and checks that quality metrics haven't degraded.

**Hallucination & Drift Detection:** Monitoring production AI systems for quality degradation. Hallucination detection: compare model outputs against known facts using a judge model or fact-checking pipeline. Drift detection: track output distribution over time — if the model starts producing different types of outputs for the same inputs, it may indicate prompt injection, model updates, or data distribution shift. Tools: Arize AI, Evidently, custom monitoring pipelines.

### Cloud platforms and credentials

**Cloud-Native Deployment Patterns:** Containerization (Docker), serverless (Lambda/Cloud Functions/Modal), managed container services (ECS/Cloud Run/Container Apps), Kubernetes for orchestration. Key patterns: microservices (each agent as a separate service), event-driven (agents triggered by queue messages), serverless-first (scale to zero when idle). Choose based on: latency requirements, GPU needs, cost sensitivity, operational complexity tolerance.

**Unstructured Data Storage:** Object stores (S3-compatible: AWS S3, GCS, MinIO) for storing raw documents, images, audio, and video. Key concepts: bucket organization, access control (IAM policies, presigned URLs for temporary access), SAS links (Shared Access Signatures for time-limited access), versioning (keep previous versions of documents), lifecycle policies (auto-archive or delete old files). Used in RAG pipelines for storing source documents.

**NoSQL / Document Databases:** JSON document stores (MongoDB, Cosmos DB, Firestore) for flexible schema data. Key concepts: JSON data modelling (embed vs reference), partition keys (for horizontal scaling), Request Units (RUs — Cosmos DB's capacity model), consistency levels (strong vs eventual), CRUD operations. Used for storing agent state, user preferences, and semi-structured data that doesn't fit a relational schema.

**Load Balancing & Application Gateway:** Distributing traffic across multiple instances of an AI service. Layer 4 (TCP) vs Layer 7 (HTTP) load balancing. Health checks: automatically remove unhealthy instances from the pool. SSL termination: decrypt HTTPS at the load balancer. Rate limiting at the gateway level: protect backend services from traffic spikes. Relevant for production AI APIs that need high availability.

**Serverless Functions & App Services:** Event-driven compute that scales automatically and charges per execution. Use cases: lightweight AI API endpoints, webhook handlers, scheduled jobs, file processing triggers. Limitations: cold start latency (100ms-2s), execution time limits (15 min for Lambda), payload size limits, no persistent state. Best for: stateless AI operations, infrequent workloads, cost-sensitive deployments.

**AI Platform Services — Agent as a Service:** Managed platforms for deploying AI agents without managing infrastructure. Examples: Azure AI Foundry (Microsoft's agent hosting platform), AWS Bedrock Agents, Google Vertex AI Agent Builder. Benefits: managed scaling, built-in monitoring, integrated security, pay-per-use pricing. Trade-offs: less control, vendor lock-in, higher cost at scale vs self-hosted.

**Full-Stack Capstone Structure:** The complete architecture for a production-ready AI application: Backend (FastAPI — REST API, authentication, business logic) + Frontend (Streamlit or React — user interface) + Vector DB (Chroma/Pinecone — semantic search) + Relational DB (PostgreSQL — structured data) + Cache (Redis — sessions, queues) + Docker (containerization) + Cloud deployment (managed container service) + CI/CD (GitHub Actions). This full stack is demonstrated in the N-1 25-day capstone project (Days 21-25).

### Additional tools and stacks

### Infrastructure & Networking

**WebSocket:** A full-duplex communication protocol over a single TCP connection. Used in AgentIQ for real-time features: live progress updates as an agent executes, streaming module content, real-time notification delivery, live capstone review status. Implementation: FastAPI WebSocket endpoints, Next.js client-side WebSocket hooks. Essential for the HITL callback architecture in Capstone 1 where the agent must notify the frontend when a phone call is initiated.

**Ngrok:** A tool for exposing local development servers to the internet via secure tunnels. Used in Capstone 1 development: Twilio needs a publicly accessible webhook URL to send keypad responses back to the FastAPI server. Ngrok creates a temporary public URL (e.g., `https://abc123.ngrok.io`) that tunnels to `localhost:8000`. Essential for testing webhook-based integrations during local development.

**Google Colab:** Google's free cloud-based Jupyter notebook environment with GPU access. Used for: running fine-tuning experiments without local GPU, testing embedding models, exploring Hugging Face models, running RAGAS evaluations. Free tier provides T4 GPU access. Pro tier provides A100 access. Essential for learners without local GPU hardware who need to complete fine-tuning modules (P11).

**Ollama CLI Commands:** The essential Ollama command-line interface:
- `ollama pull llama3.2` — download a model from the Ollama registry
- `ollama run llama3.2` — start an interactive chat session with a model
- `ollama list` — show all downloaded models with size and modification date
- `ollama serve` — start the Ollama API server (runs automatically on most systems)
- `ollama ps` — show currently running models
- `ollama rm llama3.2` — remove a downloaded model
- `ollama show llama3.2` — display model information and parameters

**PagedAttention (vLLM):** vLLM's memory management innovation for GPU inference. Traditional inference allocates a fixed KV cache per request (wasteful). PagedAttention manages KV cache memory like OS virtual memory — allocating pages on demand and sharing pages between requests with the same prefix. Result: 2-4x higher throughput than naive inference, enabling more concurrent requests on the same GPU hardware.

### No-Code & Automation Tools

**Power Automate:** Microsoft's enterprise workflow automation platform (formerly Microsoft Flow). Part of the Microsoft 365 ecosystem. Integrates natively with SharePoint, Teams, Outlook, Dynamics 365. AI Builder add-on enables AI-powered flows: document processing, form recognition, prediction models. Relevant for enterprise learners working in Microsoft-heavy organizations.

**Bardeen:** AI-powered browser automation tool that runs directly in the browser. Capabilities: scrape web data, automate repetitive browser tasks, connect web apps without APIs, trigger automations from natural language. Use cases: lead enrichment, competitive research, data collection, form filling. Positioned between Zapier (API-based) and Playwright (code-based) in the automation spectrum.

**PromptLayer:** A platform for prompt versioning, logging, and analytics. Capabilities: log every LLM API call with full prompt and response, version prompts with tags and metadata, A/B test prompt variants, track cost and latency per prompt version, search historical prompts. Integrates with OpenAI, Anthropic, and other providers via a drop-in SDK wrapper. Essential for teams managing many prompt variants in production.

### AI Content & Multimodal Tools

**DALL-E:** OpenAI's image generation model integrated into ChatGPT and available via API. DALL-E 3 generates high-quality images from text descriptions. API: `openai.images.generate(model="dall-e-3", prompt="...", size="1024x1024")`. Use cases: generating diagrams for documentation, creating visual assets for presentations, prototyping UI mockups. Part of the multimodal AI skill set (Module 29, P3).

**Stable Audio:** Stability AI's text-to-audio generation model. Generates music, sound effects, and ambient audio from text descriptions. Use cases: background music for video demos, sound effects for AI-generated videos, audio content creation. Part of the broader multimodal AI ecosystem alongside ElevenLabs (voice) and Pika (video).

**OpusClip:** AI-powered video clipping tool that automatically identifies the most engaging moments in long-form video and creates short clips optimized for social media. Use cases: repurposing webinar recordings into LinkedIn clips, creating course preview videos, generating social media content from long demos. Part of the AI Content Generation skill set.

### AEO/GEO Tools

**Screaming Frog:** A website crawler used for SEO and AEO (Answer Engine Optimization) audits. Crawls websites to identify: missing metadata, broken links, duplicate content, page structure issues. For AEO: audits structured data markup (schema.org), identifies pages that could be optimized for AI search engine citations, analyzes content structure for featured snippet eligibility.

### AI Tool Stacking

**ClickUp AI:** AI-enhanced project management platform. Features: AI-generated task summaries, automated status updates, AI writing assistant for task descriptions, smart task prioritization. Part of the AI Tool Stacking skill — combining ClickUp AI with Make.com automations and Claude for a fully AI-powered project management workflow.

### Additional Agent Frameworks

**Superagent:** Open-source framework for building and deploying AI agents as APIs. Features: agent templates, tool integrations, memory management, API deployment. Positioned as a simpler alternative to LangChain for teams that want to deploy agents quickly without deep framework knowledge.

**ChatDev:** A multi-agent framework that simulates a software development company. Agents take on roles: CEO, CTO, programmer, reviewer, tester. Given a software requirement, the agents collaborate to design, implement, test, and document a software project. Demonstrates how multi-agent systems can tackle complex, multi-phase tasks through role specialization.

### Monitoring & Tracing

**Sentence-BERT (SBERT):** A modification of BERT that produces semantically meaningful sentence embeddings. Unlike BERT (which requires comparing two sentences simultaneously), SBERT produces independent embeddings for each sentence that can be compared with cosine similarity. Much faster for large-scale semantic search. Models: `all-MiniLM-L6-v2` (fast, small), `all-mpnet-base-v2` (higher quality). Used in RAG pipelines and semantic search systems.

**Module 2 — Foundation of Azure Ecosystem:** Azure AI services and capabilities. Overview of Azure OpenAI Service, Azure Cognitive Search, Azure AI Foundry. Introduction to Azure security, compliance, and governance frameworks. Cloud-native deployment patterns on Azure.


**Module 6 — Azure-Native Agent Development & RAG:** Taxonomy of agents: autonomous, tool-using, collaborative. Planning, memory, and tool orchestration patterns. Semantic Kernel, AutoGen, CrewAI, LangChain: architectural differences. Introduction to Azure-native agent architectures. Designing modular agents with separation of planning, reasoning, and tool-use. Event-driven agents vs always-on workflows. Creating fallback strategies and confidence-based branching. Semantic search and RAG fundamentals using Azure AI Search and Azure OpenAI embeddings. Tokenization, embedding types, vector databases (Azure Cognitive Search, FAISS). Building and managing vector databases with Azure-native tools. Assessment: Graded Quiz 1, Graded Project 1.


**Module 10 — GenAI Cloud Platforms and Implementations:** Building APIs and integrations using Azure Functions, Azure API Management, and FastAPI on Azure. Integration of agents with data pipelines and tool endpoints. Deployment: Dockerizing LLM applications for Azure Container Apps. Observability: Logging, tracing, monitoring, cost & latency dashboards using Azure Monitor and Application Insights. Alert configuration. Agent Development Basics with Azure AI Services. Agent Orchestration. End-to-end Monitoring. Detecting hallucinations and drift. Assessment: Graded Quiz 2, Graded Project 2.


**Module 12 — Security, Compliance and Responsible AI:** Data Privacy & Governance — GDPR, HIPAA, SOC 2 compliance in Azure. AI Safety — prompt injection, jailbreaks, data leakage, guardrails for GenAI. Responsible AI — fairness, bias detection, explainability. Security architecture patterns: sandboxed agents, watchdogs. Integration with enterprise security and Azure Security Center.


### Syllabus theme — day 3

**Day 3 — Unstructured/Semi-Structured Data (Part 1):** Understanding options for storing unstructured/semi-structured data: Azure Storage & Cosmos DB. What is Azure Cosmos DB? Key Features (Global Distribution, Low Latency). Understanding Request Units (RUs). Data Modelling with JSON Documents. Partition Key Basics. CRUD Operations in Cosmos DB.

### Syllabus theme — day 4

**Day 4 — Unstructured/Semi-Structured Data (Part 2):** Querying with SQL API. Consistency Levels. Using Azure Portal for Cosmos DB. Basic Security and Access Control. Introduction to OCR. Azure Document Intelligence. Accessing Blob storage through SDK and SAS links. Reading PDFs through open-source libraries: PyMuPDF, Tesseract, PyPDF.

### Syllabus theme — day 5

**Day 5 — Core Azure Services: Compute, Messaging, Load Balancing & Databricks:** Azure Queue Services & Service Bus for Decoupling. Azure Load Balancer & Application Gateway Basics. Application of Azure Functions & Azure App Services.

### Syllabus theme — day 12

**Day 12 — Putting It All Together: GenAI Use Case & Deployment:** GenAI API Example: Calling Azure OpenAI / HuggingFace APIs (simple RAG without vector DB). Best Practices, CI/CD Overview. Exercise: Build complete pipeline — Input Queue → Processing → Store → API Serve (FastAPI/Flask) → Containerize with Docker → Deploy to Azure App Services / Container Instances.

### Cloud and data engineering patterns

N-1 Curriculum — Unique Topics (Gap Analysis)

- **Azure Cosmos DB** — JSON data modelling, partition keys, RUs, consistency levels, CRUD operations
- **Azure Blob Storage** — SDK access, SAS links, unstructured data storage
- **OCR & Document Intelligence** — Azure Document Intelligence, PyMuPDF, Tesseract, PyPDF for PDF processing
- **Azure Queue Services & Service Bus** — decoupling patterns, message queuing
- **Azure Load Balancer & Application Gateway** — infrastructure basics
- **Redis as middleware** — agent memory with Redis, event queues
- **Streamlit UI** — frontend for AI apps (current curriculum doesn't cover frontend frameworks)
- **AutoGen Studio** — visual agent orchestration (vs AutoGen SDK which is covered)
- **AI Foundry — Agent as a Service** — Azure-native agent hosting
- **Full-stack capstone structure** — backend (FastAPI) + frontend (Streamlit) + vector DB + Docker + Azure deployment + CI/CD

- commit messages
- docker-deploy
- codebase-visualizer
- api-design


- LangGraph stateful agent graph with human-in-the-loop node
- FastAPI REST API backend
- Twilio for programmatic phone calls + SMS escalation
- Tool layer: email reader, calendar API, Slack notifier, decision logger
- Flow: Trigger → Planning → Execution → Decision gate → Escalation → Resume → Log
- Deliverables: GitHub repo, deployed FastAPI backend (Railway/Fly.io), 2-min vide


- Ollama: runs LLaMA 3 or Mistral locally
- SearXNG: self-hosted meta-search engine (Docker)
- LangChain: agent that queries SearXNG → retrieves pages → synthesises answer
- Streamlit: clean chat UI with source citations
- Features: NL query → web search → answer with citations, follow-up support, sour
- Deliverables: Docker Compose file, GitHub repo + setup guide, 5-min demo video


- Exercise: Azure Document Intelligence deep dive (markdown and JSON extract, anal


### Day 5 — Core Azure Services: Compute, Messaging, Load Balancing & Databricks


- Module 102: Serverless Functions for AI [Core] | Tools: AWS Lambda, Vercel Edge,
- Module 103: Docker for AI Systems [Core] | Tools: Docker, docker-compose
- Module 104: Kubernetes for AI Scale [Optional] | Tools: Kubernetes, Helm, k8s
- Module 105: Vector DB Hosting & Management [Core] | Tools: Pinecone cloud, Weavi


- Module 115: User Authentication & RBAC [Core] | Tools: Auth0, Clerk, FastAPI sec
- Module 117: Red Team Testing for AI Systems [Core] | Tools: PyRIT, garak, manual


- Architecture design for enterprise AI systems
- Miro for visual architecture diagrams
- Strategy frameworks for AI adoption roadmaps
- Self-assessment framework for skill gaps
- Career positioning based on skill combinations
- Token calculators for budget planning
- Model comparison: cost vs quality vs latency trade-offs
- Caching, batching, model routing for cost reduction
- Smaller models for easy tasks, larger for complex ones
- Consulting frameworks for enterprise AI adoption
- Stakeholder alignment, risk assessment, phased rollout
- Change management and training programs
- Deck templates for client presentations
- Pricing models: hourly, project-based, retainer, value-based
- Positioning as AI architect vs implementer vs strategist
- Streamlit/Gradio for live demos to stakeholders
- Gamma for AI-generated presentations
- Communication frameworks for technical and non-technical audiences


- Architectural constraints integrating Azure OpenAI models into workflows


- Overview of Azure cloud platform capabilities, cost, and deployment options

