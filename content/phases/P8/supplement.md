---
kind: phase_supplement
phase_code: P8
---

# Phase P8 — supplemental depth

### Model Context Protocol

### Building MCP Servers

**Configuring MCP Servers:** MCP servers are configured in `.claude/settings.json` (project-level, shared via git) or `~/.claude/settings.json` (global, personal). Configuration specifies the server command, arguments, environment variables, and permissions. Project-level config is preferred for team consistency. Each server entry includes: command (how to start the server), args (CLI arguments), env (environment variables for secrets).

### MCP Integrations

**Slack MCP:** An MCP server that exposes Slack capabilities as tools to Claude. Tools include: read_channel (fetch recent messages), send_message (post to a channel), search_messages (full-text search), schedule_message (post at a future time), create_canvas (create a Slack canvas document). Enables agents to monitor Slack for triggers and respond to messages autonomously.

**Google Calendar MCP:** An MCP server exposing Google Calendar as agent tools. Tools: list_events (fetch upcoming events), create_event (schedule a meeting), update_event (modify existing event), delete_event (cancel a meeting), find_free_time (find available slots for a given duration). Enables scheduling agents that can autonomously manage calendars.

**Jira & Confluence MCP:** MCP servers for Atlassian products. Jira tools: create_issue, search_issues (JQL queries), update_issue, add_comment. Confluence tools: create_page, search_pages, update_page. Enables agents to automatically create tickets from feedback, update issue status, and document decisions in Confluence.

**Google Cloud Vertex AI:** Running Claude models on Google Cloud Platform via Vertex AI. Benefits: data residency in GCP regions, integration with BigQuery for data analysis, GCS for document storage, IAM for access control, VPC for network isolation. Relevant for enterprise customers with existing GCP infrastructure and data governance requirements.

**Phase 5: MCP & A2A Protocols**
- Build MCP Server with 3 tools (database query, file read, API call) using FastMCP
- Connect to Claude Desktop via `claude_desktop_config.json`
- MCP architecture: 1:1 client-server mapping, Tools + Resources + Prompts
- A2A protocol understanding
- Certifications: Anthropic Advanced MCP Course (free), HuggingFace MCP Course (free)


- Different servers (A, B, C) handle different data sources
- Each MCP server interacts with a specific external system:


- Layer Agentic AI Infrastructure Stack (Module 80)
- Unified AI System: User → Orchestrator → Agents (A2A) → MCP Clients → MCP Server
- Cross-cutting concerns: Memory, Identity, Observability, Guardrails
- MCP = capability layer (tools); A2A = communication layer (agents); Together = p


- Phase 0 is mandatory first (Ollama, LM Studio, LiteLLM minimum)
- No module without working, copy-paste-ready code
- MCP (P8) + A2A (P9) must be deeply covered (13+ modules combined)
- Every phase produces a career artifact (LinkedIn post, resume bullet, demo)


### IMAGE 1 — MCP vs A2A vs Unified AI Architecture


### IMAGE 2 — MCP Explained (The Protocol Connecting AI to Everything)


- MCP Host: Claude Desktop, IDEs, AI Tools
- MCP Clients act as intermediaries following MCP Protocol
- MCP Server A → Amazon S3 (file storage)
- MCP Server B → Airbnb (booking/availability)
- MCP Server C → Stripe (payments)


- Section 1: Complete Building Blocks — Claude Core, Skills (reusable modules), Me
- Section 2: System Flow — Command Layer → Subagent Execution → Output with Workfl
- Section 3: Context Engineering — smaller context = higher accuracy
- Section 4: Memory System — in-context (temporary), in-cache (session), in-storag
- Section 5: Reusability Engine — stop rewriting; modularise workflows
- Section 6: MCP Integration — Claude ↔ MCP ↔ DB/S3/External tools
- Section 7: Hooks & Guardrails — Event → Hook → Action; listing, validation, noti
- Section 8: Settings & Extensions — model config, environment setup
- Section 9: Iteration System — test fast, fail fast, ship fast
- Foundation: Claude 101, AI Fluency Framework, AI Fluency for Students/Educators
- Developer: Claude Code in Action, Building with Claude API, Prompt Engineering
- Platform: Claude with Amazon Bedrock, Claude with Google Cloud Vertex AI
- Advanced: MCP Introduction, MCP Advanced Topics
- Agents: Introduction to Agent Skills, Claude Code (Coursera)


- What is Cowork Mode — desktop Claude app with Linux VM, file access, pre-loaded
- Installing & Using Plugins — bundles of MCPs + skills + commands


- Hugging Face smol-course** (HuggingFace) — Beginner → Intermediate
- MCP Servers** (Model Context Protocol) — Intermediate → Advanced
- Dify** (Community) — Intermediate


- Open protocol for seamless integration between LLM apps and external data/tools
- Host → Client → Protocol → Server → Data Source pattern
- :1 client-server mapping within a host
- Host: application containing MCP clients (Claude Desktop, IDEs, AI tools)
- Client: manages connection to one MCP server
- Server: exposes tools, resources, prompts to the client
- Tools: mcp Python SDK, Claude Desktop
- stdio transport: local process communication
- HTTP SSE transport: remote server communication
- Bidirectional messaging via transport layer
- Secure file access: controlled data security for file interactions
- Sampling: retrieving relevant data samples from sources
- Security boundaries and permission models
- Resources: access to knowledge sources and data
- Prompts: AI-based querying and processing templates
- Tools & Functions: computational capabilities exposed to the model
- mcp Python SDK for server implementation
- FastAPI integration for HTTP-based servers
- Tool registration, resource exposure, prompt templates
- boto3 for AWS S3 file storage access
- stripe SDK for payment processing integration
- psycopg2 for PostgreSQL database access
- Patterns for wrapping existing APIs as MCP servers
- Claude Desktop configuration for MCP servers
- mcp config JSON setup and server registration
- End-to-end workflow: config → connect → use tools


- Module 62: MCP Architecture & Core Concepts [Core] | Tools: MCP spec, Python
- Module 63: MCP Host, Client & Server Design [Core] | Tools: mcp Python SDK, Clau
- Module 66: MCP Resources, Prompts & Tools [Core] | Tools: MCP spec, tool definit
- Module 69: Claude Desktop + MCP Full Setup [Core] | Tools: Claude Desktop, mcp c

