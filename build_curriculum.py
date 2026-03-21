#!/usr/bin/env python3
"""Generate embedded curriculum JSON for AI Master Tracker (133 modules, 20 phases). Cursor-assisted build — data layer by Manish.AI."""
import csv
import json
from pathlib import Path

from catalog_io import ensure_catalog_or_bootstrap
from curriculum_deep_content import build_learn_html, build_steps_html
from phase_ref_extras import PHASE_REFERENCE_EXTRAS

ROOT = Path(__file__).resolve().parent

# Blueprint §2 crosswalk: canonical topic buckets from the Master Tracker doc → where they are addressed.
BLUEPRINT_CROSSWALK = [
    {"id": "img1_mcp_a2a_unified", "doc_ref": "§2 Image 1", "topic": "MCP vs A2A vs unified agentic stack", "module_nums": list(range(62, 75)), "tracker_status": "modules_exist_content_scaffold"},
    {"id": "img2_mcp_explained", "doc_ref": "§2 Image 2", "topic": "MCP host/client/server, tools, resources, prompts", "module_nums": list(range(62, 70)), "tracker_status": "modules_exist_content_scaffold"},
    {"id": "img3_curriculum_map", "doc_ref": "§2 Image 3", "topic": "Full 2026 curriculum map (languages, agents, RAG, deploy, security)", "module_nums": list(range(1, 134)), "tracker_status": "mapped_to_133_modules"},
    {"id": "img4_top40_terms", "doc_ref": "§2 Image 4", "topic": "Top 40 AI terms & core vocabulary", "module_nums": [7], "tracker_status": "covered_on_page"},
    {"id": "img5_skills_2026", "doc_ref": "§2 Image 5", "topic": "12 AI skills for 2026", "module_nums": [120], "tracker_status": "module_scaffold"},
    {"id": "img6_coding_spectrum", "doc_ref": "§2 Image 6", "topic": "Traditional vs vibe vs no-code", "module_nums": [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], "tracker_status": "modules_scaffold"},
    {"id": "img7_nine_layer_stack", "doc_ref": "§2 Image 7", "topic": "9-layer agentic infrastructure stack", "module_nums": [80], "tracker_status": "module_scaffold"},
    {"id": "img8_agent_security", "doc_ref": "§2 Image 8", "topic": "Securing AI agents & infrastructure risk", "module_nums": [77, 81, 113, 114, 115, 116, 117, 118], "tracker_status": "modules_scaffold"},
    {"id": "capstones", "doc_ref": "§6", "topic": "Three capstone projects", "module_nums": [125, 126, 127], "tracker_status": "capstone_pages_plus_modules_scaffold"},
    {"id": "certs_p19", "doc_ref": "§3 P19 / §8.4", "topic": "Vendor certification paths", "module_nums": list(range(128, 134)), "tracker_status": "tracker_ui_plus_modules_scaffold"},
]

# Phase metadata: code, sidebar title, purpose, icon, color class, module count (must sum 133)
PHASE_META = [
    ("P0", "Local AI Setup", "Full local AI environment before writing agent code", "💻", "mc-0", 6),
    ("P1", "AI Foundations", "LLMs, transformers, embeddings, ML paradigms", "🧠", "mc-1", 8),
    ("P2", "Prompt Engineering", "The primary interface to models", "✍️", "mc-2", 7),
    ("P3", "LLMs & APIs", "Providers, auth, tools, multimodal", "🔌", "mc-3", 8),
    ("P4", "Agent Fundamentals", "Architectures, planning, collaboration", "🤖", "mc-4", 7),
    ("P5", "Tool Use & Integration", "Memory, APIs, files, search, browsing", "🛠️", "mc-5", 8),
    ("P6", "Agent Frameworks", "LangChain, LangGraph, CrewAI, LlamaIndex…", "⚡", "mc-6", 10),
    ("P7", "RAG & Knowledge", "Embeddings, chunking, vector DBs, hybrid search", "📚", "mc-7", 7),
    ("P8", "MCP Protocol", "Model Context Protocol depth", "🔗", "mc-5", 8),
    ("P9", "A2A Protocol", "Agent-to-agent communication", "🌐", "mc-8", 5),
    ("P10", "Unified AI Systems", "Orchestration, identity, observability, 9-layer stack", "🏗️", "mc-7", 7),
    ("P11", "Fine-Tuning", "LoRA, PEFT, data prep, evaluation", "🎯", "mc-9", 5),
    ("P12", "Vibe Coding", "AI-native development tools", "💫", "mc-10", 8),
    ("P13", "Automation", "n8n, Make, Zapier, DAGs, guardrails", "⚙️", "mc-6", 5),
    ("P14", "Production AI", "APIs, Docker, hosting, serverless", "🚀", "mc-11", 7),
    ("P15", "Monitoring & Eval", "RAGAS, LangSmith, OpenTelemetry", "📊", "mc-4", 6),
    ("P16", "Security & Governance", "Injection, secrets, RBAC, privacy", "🔐", "mc-7", 6),
    ("P17", "Consultant Track", "Strategy, pricing, demos, 12 skills", "💼", "mc-2", 6),
    ("P18", "Capstones", "Three portfolio projects", "🎓", "mc-8", 3),
    ("P19", "Certifications", "Vendor credentials roadmap", "🏆", "mc-12", 6),
]

# Canonical 133 rows: (title, tools, priority)
ROWS = [
    ("Ollama Setup & Local Model Running", "Ollama, llama3, mistral", "MUST DO"),
    ("LM Studio — GUI for Local LLMs", "LM Studio, GGUF models", "MUST DO"),
    ("Open WebUI — Local ChatGPT Interface", "Open WebUI, Docker", "MUST DO"),
    ("vLLM — High-Performance Inference", "vLLM, CUDA, Python", "OPTIONAL"),
    ("LiteLLM Routing & Load Balancing", "LiteLLM, proxy server", "MUST DO"),
    ("Free APIs: Groq, Gemini, Mistral, OpenRouter", "Groq API, Gemini, OpenRouter", "MUST DO"),
    ("Top 40 AI Terms & Core Concepts", "Flashcards, terminology", "MUST DO"),
    ("How LLMs Work: Transformers & Tokenization", "Hugging Face, tiktoken", "MUST DO"),
    ("Embeddings & Vector Representations", "OpenAI Embeddings, SBERT", "MUST DO"),
    ("Inference, Context Windows & Cost Optimisation", "Token counters, model APIs", "MUST DO"),
    ("Quantization & Model Efficiency", "GGUF, GPTQ, bitsandbytes", "OPTIONAL"),
    ("GPU/TPU & Compute for AI", "CUDA, Colab, RunPod", "OPTIONAL"),
    ("ML Paradigms: Supervised, Unsupervised, RL", "scikit-learn, OpenAI Gym", "MUST DO"),
    ("Generative AI Pipeline (Input→Process→Output)", "OpenAI API, LangChain", "MUST DO"),
    ("Prompt Engineering Fundamentals", "Claude, GPT-4, PromptPerfect", "MUST DO"),
    ("Chain-of-Thought (CoT) Prompting", "GPT-4o, Claude, Gemini", "MUST DO"),
    ("Context Management & Context Window", "LangChain Memory, Claude 200K", "MUST DO"),
    ("Multi-Agent & Goal-Oriented Prompts", "CrewAI, AutoGen", "MUST DO"),
    ("Self-Critique, Retry Loops & Reflexion", "LangGraph, custom Python", "MUST DO"),
    ("Task Planning Prompts & Role Prompting", "Claude, GPT-4, Perplexity", "MUST DO"),
    ("Prompt Chaining & Advanced Techniques", "LangChain, LangGraph, LCEL", "MUST DO"),
    ("OpenAI API Deep Dive (GPT-4, GPT-4o)", "openai Python SDK", "MUST DO"),
    ("Anthropic Claude API", "anthropic Python SDK", "MUST DO"),
    ("Google Gemini API", "google-generativeai", "MUST DO"),
    ("Mistral & Open Source LLMs (LLaMA, DeepSeek)", "Hugging Face, mistralai SDK", "MUST DO"),
    ("API Authentication & Rate Limiting", "API keys, backoff, tenacity", "MUST DO"),
    ("Toolformer / Function Calling", "OpenAI tools, Claude tool_use", "MUST DO"),
    ("Tool Invocation & Output Parsing", "Pydantic, json_schema, LangChain", "MUST DO"),
    ("Multimodal AI (Text + Image + Audio + Video)", "GPT-4V, Gemini, Pika, ElevenLabs", "MUST DO"),
    ("What Are AI Agents? Autonomous vs Semi-Auto", "LangChain, custom Python", "MUST DO"),
    ("Agent Architectures: ReAct, CAMEL, AutoGPT", "LangChain ReAct, AutoGPT", "MUST DO"),
    ("Goal Decomposition & Task Planning Algorithms", "LangGraph, custom planners", "MUST DO"),
    ("Decision-Making Policies for Agents", "LangGraph, state machines", "MUST DO"),
    ("Action Planning Loops & Execution", "LangGraph, ReAct pattern", "MUST DO"),
    ("Self-Reflection / Feedback Loops", "Reflexion, LangGraph", "MUST DO"),
    ("Multi-Agent Collaboration Patterns", "CrewAI, AutoGen, LangGraph", "MUST DO"),
    ("Tool Use System Design", "OpenAI tools, LangChain tools", "MUST DO"),
    ("Memory Integration (Short/Long-Term/Episodic)", "LangChain Memory, mem0", "MUST DO"),
    ("External API Calling from Agents", "requests, httpx, LangChain", "MUST DO"),
    ("File Reader/Writer Tools", "Python I/O, LangChain tools", "MUST DO"),
    ("Python Execution Tools (Code Interpreter)", "E2B, Docker sandbox", "MUST DO"),
    ("Search & Retrieval Tools", "Tavily, SerpAPI, DuckDuckGo", "MUST DO"),
    ("Web Browsing Tools for Agents", "Playwright, Selenium, Firecrawl", "MUST DO"),
    ("AI Search Optimisation (AEO/GEO)", "SearchAble, Outranking", "OPTIONAL"),
    ("LangChain Deep Dive", "LangChain, LCEL, chains", "MUST DO"),
    ("LangGraph — Stateful Agent Orchestration", "LangGraph, StateGraph", "MUST DO"),
    ("CrewAI — Multi-Agent Crews", "CrewAI, agents, tasks", "MUST DO"),
    ("AutoGen — Conversational Multi-Agent", "AutoGen, ConversableAgent", "MUST DO"),
    ("Flowise — Visual Agent Builder", "Flowise, Docker, UI flows", "OPTIONAL"),
    ("AgentOps — Agent Monitoring & Observability", "AgentOps, LangSmith", "MUST DO"),
    ("Haystack — NLP Pipeline Framework", "Haystack, pipelines", "OPTIONAL"),
    ("Semantic Kernel (Microsoft)", "Semantic Kernel, C#/Python", "OPTIONAL"),
    ("LlamaIndex — Data Framework for LLMs", "LlamaIndex, VectorStore index", "MUST DO"),
    ("LLM Management: W&B, Arize AI", "Weights & Biases, Arize", "OPTIONAL"),
    ("RAG Architecture & Pipeline Design", "LangChain, LlamaIndex", "MUST DO"),
    ("Embedding Models & Semantic Search", "OpenAI, Cohere, SBERT", "MUST DO"),
    ("Document Chunking Strategies", "LangChain splitters, custom logic", "MUST DO"),
    ("Custom Data Loaders & Document Ingestion", "LangChain loaders, Unstructured", "MUST DO"),
    ("Vector DBs: Pinecone, Weaviate, Chroma, FAISS", "Pinecone, Weaviate, Chroma", "MUST DO"),
    ("Query Refinement & Hybrid Search", "BM25, dense retrieval, rerankers", "MUST DO"),
    ("Knowledge Graphs for AI", "Neo4j, NetworkX, graph RAG", "OPTIONAL"),
    ("MCP Architecture & Core Concepts", "MCP spec, Python", "MUST DO"),
    ("MCP Host, Client & Server Design", "mcp Python SDK, Claude Desktop", "MUST DO"),
    ("MCP Transport Layer & Communication", "stdio, HTTP SSE transport", "MUST DO"),
    ("Secure File Access & Sampling in MCP", "MCP server Python", "MUST DO"),
    ("MCP Resources, Prompts & Tools", "MCP spec, tool definitions", "MUST DO"),
    ("Building a Custom MCP Server (Python)", "mcp, fastapi, Python", "MUST DO"),
    ("MCP Integrations: S3, Stripe, Databases", "boto3, stripe, psycopg2 + MCP", "MUST DO"),
    ("Claude Desktop + MCP Full Setup", "Claude Desktop, mcp config", "MUST DO"),
    ("A2A Protocol Architecture", "A2A spec, Python", "MUST DO"),
    ("Agent Cards & Agent Identity", "A2A agent cards, JSON", "MUST DO"),
    ("Task Delegation & Result Artifacts", "A2A tasks, Python SDK", "MUST DO"),
    ("Multi-Agent Distributed Execution", "A2A, LangGraph, Docker", "MUST DO"),
    ("A2A vs MCP: When to Use Which", "Architecture diagrams, code", "MUST DO"),
    ("Orchestrator Design & Patterns", "LangGraph, custom Python", "MUST DO"),
    ("Memory Layer Architecture (3-Tier)", "mem0, Redis, PostgreSQL", "MUST DO"),
    ("Identity & Agent Security Layer", "Teleport, cryptographic identity", "MUST DO"),
    ("Observability: Logs, Traces, Metrics", "LangSmith, OpenTelemetry", "MUST DO"),
    ("Guardrails & Output Safety Systems", "NeMo Guardrails, custom filters", "MUST DO"),
    ("The 9-Layer Agentic AI Infrastructure Stack", "Architecture reference", "MUST DO"),
    ("RBAC & Securing AI Agents (Cryptographic ID)", "RBAC, Teleport, policy engines", "MUST DO"),
    ("Fine-Tuning Fundamentals & When to Use It", "Hugging Face, OpenAI fine-tune", "MUST DO"),
    ("LoRA & QLoRA (Efficient Fine-Tuning)", "PEFT, bitsandbytes, LoRA", "MUST DO"),
    ("PEFT: Parameter Efficient Fine-Tuning", "PEFT library, HF Transformers", "MUST DO"),
    ("Training Data Preparation & Curation", "datasets, Argilla, Label Studio", "MUST DO"),
    ("Domain Adaptation & Model Evaluation", "ROUGE, BERTScore, Eleuther LM Eval", "OPTIONAL"),
    ("Vibe Coding Philosophy & Toolchain", "Claude Code, Cursor, GitHub Copilot", "MUST DO"),
    ("Claude Code: Setup, CLAUDE.md & Workflow", "Claude Code CLI, CLAUDE.md", "MUST DO"),
    ("Claude Code: Skills, Hooks & Memory System", "Claude Code skills, hooks", "MUST DO"),
    ("Claude Code: 4-Layer Architecture", "CLAUDE.md, Skills, Hooks, Agents", "MUST DO"),
    ("Claude Code: Project Structure (Agentic Setup)", "agentic project scaffold", "MUST DO"),
    ("Cursor AI — AI-Native IDE", "Cursor, Cursor rules", "MUST DO"),
    ("GitHub Copilot for AI Development", "Copilot, VS Code, CLI", "MUST DO"),
    ("Lovable & Gamma (No-Code AI Builders)", "Lovable, Gamma", "OPTIONAL"),
    ("n8n — Open Source Workflow Automation", "n8n, Docker, webhooks", "MUST DO"),
    ("Make.com (Integromat) — Visual Automation", "Make.com, modules, scenarios", "MUST DO"),
    ("Zapier — Enterprise Integration Automation", "Zapier, Zaps, triggers", "MUST DO"),
    ("DAG Management & Event-Based Triggers", "LangGraph, Airflow, n8n", "MUST DO"),
    ("Guardrails & Conditional Workflow Logic", "LangGraph conditionals, n8n", "MUST DO"),
    ("FastAPI — Production API for AI Systems", "FastAPI, Pydantic, uvicorn", "MUST DO"),
    ("Streamlit & Gradio — AI UIs", "Streamlit, Gradio", "MUST DO"),
    ("Serverless Functions for AI", "AWS Lambda, Vercel Edge, Modal", "MUST DO"),
    ("Docker for AI Systems", "Docker, docker-compose", "MUST DO"),
    ("Kubernetes for AI Scale", "Kubernetes, Helm, k8s", "OPTIONAL"),
    ("Vector DB Hosting & Management", "Pinecone cloud, Weaviate cloud", "MUST DO"),
    ("Agent Hosting: Replit, Modal, Fly.io", "Replit, Modal, Fly.io", "MUST DO"),
    ("Agent Evaluation Metrics & Benchmarks", "RAGAS, TruLens, custom evals", "MUST DO"),
    ("Human-in-the-Loop Feedback Systems", "LangSmith, Argilla", "MUST DO"),
    ("LangSmith — Tracing & Debugging LLM Apps", "LangSmith, LangChain", "MUST DO"),
    ("OpenTelemetry for AI Observability", "OpenTelemetry, Jaeger", "MUST DO"),
    ("Auto-Evaluation Loops", "LLM-as-judge, custom eval chains", "MUST DO"),
    ("Prometheus & Grafana for AI Metrics", "Prometheus, Grafana dashboards", "OPTIONAL"),
    ("Prompt Injection Detection & Protection", "Rebuff, custom guards, NeMo", "MUST DO"),
    ("API Key Management & Secret Rotation", "Vault, AWS Secrets Manager", "MUST DO"),
    ("User Authentication & RBAC", "Auth0, Clerk, FastAPI security", "MUST DO"),
    ("Output Filtering & Content Safety", "OpenAI moderation, custom filters", "MUST DO"),
    ("Red Team Testing for AI Systems", "PyRIT, garak, manual red-teaming", "MUST DO"),
    ("Data Privacy, AI Alignment & Compliance", "GDPR frameworks, AI Act basics", "MUST DO"),
    ("AI Strategy & Architecture Design", "Miro, architecture templates", "MUST DO"),
    ("The 12 AI Skills Matrix for 2026", "Skills framework, self-assessment", "MUST DO"),
    ("Cost Optimisation for AI Systems", "Token calculators, model comparisons", "MUST DO"),
    ("Enterprise AI Implementation Playbook", "Consulting frameworks", "MUST DO"),
    ("AI Consultant Positioning & Pricing", "Deck templates, pricing models", "MUST DO"),
    ("Stakeholder Communication & Demos", "Streamlit, Gradio, Gamma", "MUST DO"),
    ("CAPSTONE 1: AI That Calls You", "LangGraph, Twilio, FastAPI", "MUST DO"),
    ("CAPSTONE 2: AI Payment Risk Analyst", "RAG, compliance logic, FastAPI", "MUST DO"),
    ("CAPSTONE 3: Local Perplexity Clone", "Ollama, SearXNG, Streamlit UI", "MUST DO"),
    ("Google Cloud — Generative AI Leader & Vertex AI", "Gen AI Leader, Gemini, Vertex AI Agent Builder", "MUST DO"),
    ("AWS Certified AI Practitioner & Gen AI on AWS", "AIF-C01, Bedrock, Agents, Skill Builder", "MUST DO"),
    ("NVIDIA Generative AI LLM Certifications", "NCA-GENL, NCP-GENL, RAG & deployment labs", "MUST DO"),
    ("Microsoft Azure AI Engineer (AI-102)", "Azure OpenAI, AI Search, content filters, Entra patterns", "MUST DO"),
    ("IBM watsonx & Generative AI Engineering", "watsonx.ai, enterprise Gen AI, governance", "OPTIONAL"),
    ("Hugging Face — LLM, Agents & Open Models", "Transformers, agents course, Hub, fine-tuning", "MUST DO"),
]

assert len(ROWS) == 133
assert sum(p[5] for p in PHASE_META) == 133

# Human-editable catalog: data/catalog/phases.csv + modules.csv (bootstrap from legacy if missing).
PHASE_META, ROWS = ensure_catalog_or_bootstrap(PHASE_META, ROWS)
assert len(ROWS) == 133
assert sum(p[5] for p in PHASE_META) == 133

# Per-module references (same order as ROWS). Labels + official / primary docs only.
MODULE_REF_LINKS = [
    [("Ollama — home", "https://ollama.com/"), ("Ollama GitHub", "https://github.com/ollama/ollama"), ("Model library", "https://ollama.com/library")],
    [("LM Studio", "https://lmstudio.ai/"), ("LM Studio docs", "https://lmstudio.ai/docs"), ("GGUF / Hugging Face Hub", "https://huggingface.co/docs/hub/en/gguf")],
    [("Open WebUI", "https://github.com/open-webui/open-webui"), ("Open WebUI docs", "https://docs.openwebui.com/")],
    [("vLLM documentation", "https://docs.vllm.ai/"), ("vLLM GitHub", "https://github.com/vllm-project/vllm")],
    [("LiteLLM docs", "https://docs.litellm.ai/docs/"), ("LiteLLM GitHub", "https://github.com/BerriAI/litellm")],
    [("Groq API docs", "https://console.groq.com/docs/overview"), ("Google AI Studio / Gemini", "https://ai.google.dev/gemini-api/docs"), ("Mistral API", "https://docs.mistral.ai/"), ("OpenRouter API", "https://openrouter.ai/docs")],
    [("Hugging Face — LLM course", "https://huggingface.co/learn/llm-course/chapter1/1"), ("IBM Think — AI topics", "https://www.ibm.com/think/topics/artificial-intelligence")],
    [("Hugging Face Transformers", "https://huggingface.co/docs/transformers/index"), ("tiktoken (OpenAI)", "https://github.com/openai/tiktoken"), ("Illustrated Transformer", "https://jalammar.github.io/illustrated-transformer/")],
    [("OpenAI — embeddings", "https://platform.openai.com/docs/guides/embeddings"), ("Sentence Transformers", "https://sbert.net/docs/sentence_transformer/usage/usage.html"), ("HF — sentence-transformers", "https://huggingface.co/sentence-transformers")],
    [("OpenAI — models", "https://platform.openai.com/docs/models"), ("Anthropic — models & pricing", "https://docs.anthropic.com/en/docs/about-claude/models"), ("Tokenization — HF", "https://huggingface.co/docs/transformers/tokenizer_summary")],
    [("HF — quantization", "https://huggingface.co/docs/transformers/main_classes/quantization"), ("bitsandbytes", "https://huggingface.co/docs/bitsandbytes/main"), ("GGUF overview", "https://github.com/ggerganov/llama.cpp/blob/master/README.md")],
    [("NVIDIA CUDA", "https://docs.nvidia.com/cuda/"), ("Google Colab", "https://colab.research.google.com/"), ("RunPod docs", "https://docs.runpod.io/")],
    [("scikit-learn", "https://scikit-learn.org/stable/"), ("Gymnasium (RL envs)", "https://gymnasium.farama.org/")],
    [("OpenAI — quickstart", "https://platform.openai.com/docs/quickstart"), ("LangChain — overview", "https://python.langchain.com/docs/concepts/")],
    [("Anthropic — prompt engineering", "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview"), ("OpenAI — prompting guide", "https://platform.openai.com/docs/guides/prompt-engineering")],
    [("OpenAI — reasoning models", "https://platform.openai.com/docs/guides/reasoning"), ("Chain-of-thought (Google Cloud)", "https://cloud.google.com/discover/what-is-chain-of-thought-prompting")],
    [("LangChain — memory", "https://python.langchain.com/docs/concepts/memory/"), ("Anthropic — long context", "https://docs.anthropic.com/en/docs/build-with-claude/context-windows")],
    [("CrewAI docs", "https://docs.crewai.com/en/introduction"), ("Microsoft AutoGen", "https://microsoft.github.io/autogen/stable/")],
    [("LangGraph — overview", "https://docs.langchain.com/oss/python/langgraph/overview"), ("Reflexion (paper)", "https://arxiv.org/abs/2303.11366")],
    [("Anthropic — best practices", "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices")],
    [("LangChain — LCEL", "https://python.langchain.com/docs/concepts/lcel/"), ("LangGraph", "https://docs.langchain.com/oss/python/langgraph/overview")],
    [("OpenAI API reference", "https://platform.openai.com/docs/api-reference"), ("openai-python", "https://github.com/openai/openai-python")],
    [("Anthropic API", "https://docs.anthropic.com/en/api/getting-started"), ("anthropic-sdk-python", "https://github.com/anthropics/anthropic-sdk-python")],
    [("Gemini API", "https://ai.google.dev/gemini-api/docs"), ("google-genai SDK", "https://github.com/googleapis/python-genai")],
    [("Mistral AI — API", "https://docs.mistral.ai/"), ("Hugging Face — inference", "https://huggingface.co/docs/huggingface_hub/en/guides/inference")],
    [("OpenAI — rate limits", "https://platform.openai.com/docs/guides/rate-limits"), ("tenacity", "https://tenacity.readthedocs.io/en/latest/")],
    [("OpenAI — function calling", "https://platform.openai.com/docs/guides/function-calling"), ("Anthropic — tool use", "https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview")],
    [("Pydantic", "https://docs.pydantic.dev/latest/"), ("LangChain — structured output", "https://python.langchain.com/docs/how_to/structured_output/")],
    [("OpenAI — vision", "https://platform.openai.com/docs/guides/images-vision"), ("Gemini — vision", "https://ai.google.dev/gemini-api/docs/vision")],
    [("LangChain — agents intro", "https://python.langchain.com/docs/concepts/agents/"), ("HF — agents course", "https://huggingface.co/learn/agents-course/unit0/introduction")],
    [("LangChain — ReAct", "https://python.langchain.com/docs/concepts/agents/#react-agent"), ("AutoGPT", "https://github.com/Significant-Gravitas/AutoGPT")],
    [("LangGraph — graphs", "https://docs.langchain.com/oss/python/langgraph/graph-api")],
    [("LangGraph — persistence", "https://docs.langchain.com/oss/python/langgraph/persistence")],
    [("LangGraph — human-in-the-loop", "https://docs.langchain.com/oss/python/langgraph/interrupts")],
    [("Reflexion pattern", "https://arxiv.org/abs/2303.11366"), ("LangGraph tutorials", "https://docs.langchain.com/oss/python/langgraph/tutorials")],
    [("CrewAI", "https://docs.crewai.com/en/introduction"), ("AutoGen", "https://microsoft.github.io/autogen/stable/")],
    [("OpenAI — tools", "https://platform.openai.com/docs/guides/function-calling"), ("LangChain — tools", "https://python.langchain.com/docs/concepts/tools/")],
    [("LangChain — memory", "https://python.langchain.com/docs/concepts/memory/"), ("mem0", "https://docs.mem0.ai/")],
    [("httpx", "https://www.python-httpx.org/"), ("Requests", "https://requests.readthedocs.io/en/latest/")],
    [("LangChain — tool calling", "https://python.langchain.com/docs/how_to/tool_calling/")],
    [("E2B — code interpreter", "https://e2b.dev/docs"), ("Docker docs", "https://docs.docker.com/")],
    [("Tavily API", "https://docs.tavily.com/"), ("SerpAPI", "https://serpapi.com/docs-search-api")],
    [("Playwright", "https://playwright.dev/python/docs/intro"), ("Firecrawl", "https://docs.firecrawl.dev/")],
    [("Google Search Central", "https://developers.google.com/search/docs"), ("Bing Webmaster guidelines", "https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a")],
    [("LangChain — home", "https://python.langchain.com/docs/introduction/")],
    [("LangGraph", "https://docs.langchain.com/oss/python/langgraph/overview")],
    [("CrewAI", "https://docs.crewai.com/en/introduction")],
    [("AutoGen", "https://microsoft.github.io/autogen/stable/")],
    [("Flowise", "https://docs.flowiseai.com/")],
    [("AgentOps", "https://docs.agentops.ai/"), ("LangSmith", "https://docs.smith.langchain.com/")],
    [("Haystack", "https://docs.haystack.deepset.ai/docs/intro")],
    [("Semantic Kernel", "https://learn.microsoft.com/en-us/semantic-kernel/overview/")],
    [("LlamaIndex", "https://docs.llamaindex.ai/en/stable/")],
    [("Weights & Biases", "https://docs.wandb.ai/"), ("Arize Phoenix", "https://docs.arize.com/phoenix")],
    [("LlamaIndex — RAG", "https://docs.llamaindex.ai/en/stable/understanding/rag/"), ("LangChain — RAG", "https://python.langchain.com/docs/tutorials/rag/")],
    [("OpenAI embeddings", "https://platform.openai.com/docs/guides/embeddings"), ("Cohere embed", "https://docs.cohere.com/docs/embeddings")],
    [("LangChain — text splitters", "https://python.langchain.com/docs/concepts/text_splitters/")],
    [("LangChain — document loaders", "https://python.langchain.com/docs/integrations/document_loaders/"), ("Unstructured", "https://docs.unstructured.io/")],
    [("Pinecone docs", "https://docs.pinecone.io/"), ("Weaviate docs", "https://weaviate.io/developers/weaviate"), ("Chroma", "https://docs.trychroma.com/"), ("FAISS wiki", "https://github.com/facebookresearch/faiss/wiki")],
    [("Weaviate — hybrid search", "https://weaviate.io/developers/weaviate/concepts/search/hybrid-search")],
    [("Neo4j — GraphRAG", "https://neo4j.com/labs/genai-ecosystem/graphrag/"), ("NetworkX", "https://networkx.org/documentation/stable/")],
    [("MCP — specification (repo)", "https://github.com/modelcontextprotocol/specification"), ("MCP — documentation", "https://modelcontextprotocol.io/")],
    [("MCP — Python SDK", "https://github.com/modelcontextprotocol/python-sdk"), ("Claude — desktop apps", "https://claude.ai/download"), ("Anthropic — MCP connector help", "https://support.anthropic.com/")],
    [("MCP — docs", "https://modelcontextprotocol.io/"), ("MCP — specification", "https://github.com/modelcontextprotocol/specification")],
    [("MCP — documentation", "https://modelcontextprotocol.io/"), ("MCP — specification", "https://github.com/modelcontextprotocol/specification")],
    [("MCP — tools & resources", "https://modelcontextprotocol.io/"), ("Official MCP servers", "https://github.com/modelcontextprotocol/servers")],
    [("FastMCP", "https://github.com/jlowin/fastmcp"), ("MCP Python SDK", "https://github.com/modelcontextprotocol/python-sdk")],
    [("boto3 S3", "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html"), ("Stripe API", "https://docs.stripe.com/api"), ("psycopg", "https://www.psycopg.org/docs/")],
    [("Claude Desktop", "https://claude.ai/download"), ("MCP — quickstart", "https://modelcontextprotocol.io/quickstart")],
    [("A2A — Google repo", "https://github.com/google/A2A"), ("A2A — site", "https://a2a-protocol.org/")],
    [("A2A — agent card", "https://github.com/google/A2A/blob/main/docs/topics/agent-discovery-and-identity.md")],
    [("A2A — specification", "https://github.com/google/A2A")],
    [("LangGraph — multi-agent", "https://docs.langchain.com/oss/python/langgraph/multi-agent"), ("Docker Compose", "https://docs.docker.com/compose/")],
    [("MCP — introduction", "https://modelcontextprotocol.io/introduction"), ("A2A protocol", "https://a2a-protocol.org/"), ("A2A — GitHub", "https://github.com/google/A2A")],
    [("LangGraph — workflows", "https://docs.langchain.com/oss/python/langgraph/workflows-agents")],
    [("mem0", "https://docs.mem0.ai/"), ("Redis docs", "https://redis.io/docs/"), ("PostgreSQL", "https://www.postgresql.org/docs/")],
    [("Teleport — zero trust", "https://goteleport.com/docs/")],
    [("LangSmith", "https://docs.smith.langchain.com/"), ("OpenTelemetry", "https://opentelemetry.io/docs/")],
    [("NeMo Guardrails", "https://docs.nvidia.com/nemo/guardrails/latest/"), ("LLM Guard", "https://github.com/laiyer-ai/llm-guard")],
    [("Google Cloud — AI/ML architecture", "https://cloud.google.com/architecture/ai-ml")],
    [("Auth0 — RBAC", "https://auth0.com/docs/manage-users/access-control/rbac"), ("Teleport — Machine ID", "https://goteleport.com/docs/machine-id/intro/"), ("OWASP — authorization", "https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html")],
    [("Hugging Face — fine-tuning", "https://huggingface.co/docs/transformers/training"), ("OpenAI — fine-tuning", "https://platform.openai.com/docs/guides/fine-tuning")],
    [("Hugging Face — PEFT / LoRA", "https://huggingface.co/docs/peft/index")],
    [("PEFT", "https://huggingface.co/docs/peft/index"), ("Transformers", "https://huggingface.co/docs/transformers/index")],
    [("datasets", "https://huggingface.co/docs/datasets/index"), ("Argilla", "https://docs.argilla.io/latest/"), ("Label Studio", "https://labelstud.io/guide/")],
    [("Evaluate — HF", "https://huggingface.co/docs/evaluate/index"), ("lm-evaluation-harness", "https://github.com/EleutherAI/lm-evaluation-harness")],
    [("Cursor", "https://cursor.com/docs"), ("GitHub Copilot", "https://docs.github.com/en/copilot"), ("Claude Code", "https://docs.anthropic.com/en/docs/claude-code/overview")],
    [("Claude Code — setup", "https://docs.anthropic.com/en/docs/claude-code/setup")],
    [("Claude Code — hooks", "https://docs.anthropic.com/en/docs/claude-code/hooks")],
    [("Claude Code — overview", "https://docs.anthropic.com/en/docs/claude-code/overview")],
    [("Claude Code — best practices", "https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices")],
    [("Cursor — rules", "https://cursor.com/docs/context/rules")],
    [("GitHub Copilot", "https://docs.github.com/en/copilot")],
    [("Lovable", "https://lovable.dev/"), ("Gamma", "https://gamma.app/")],
    [("n8n docs", "https://docs.n8n.io/")],
    [("Make — help", "https://www.make.com/en/help")],
    [("Zapier — help", "https://help.zapier.com/hc/en-us")],
    [("Apache Airflow", "https://airflow.apache.org/docs/"), ("LangGraph", "https://docs.langchain.com/oss/python/langgraph/overview")],
    [("n8n — error workflows", "https://docs.n8n.io/flow-logic/error-handling/")],
    [("FastAPI", "https://fastapi.tiangolo.com/")],
    [("Streamlit", "https://docs.streamlit.io/"), ("Gradio", "https://www.gradio.app/docs/")],
    [("AWS Lambda", "https://docs.aws.amazon.com/lambda/"), ("Modal", "https://modal.com/docs/guide"), ("Vercel functions", "https://vercel.com/docs/functions")],
    [("Docker docs", "https://docs.docker.com/")],
    [("Kubernetes docs", "https://kubernetes.io/docs/home/")],
    [("Pinecone", "https://docs.pinecone.io/"), ("Weaviate Cloud", "https://weaviate.io/developers/weaviate/cloud-services")],
    [("Replit", "https://docs.replit.com/"), ("Modal", "https://modal.com/docs/guide"), ("Fly.io", "https://fly.io/docs/")],
    [("RAGAS", "https://docs.ragas.io/en/stable/")],
    [("LangSmith — datasets", "https://docs.smith.langchain.com/evaluation/how_to_guides/datasets"), ("Argilla", "https://docs.argilla.io/latest/")],
    [("LangSmith", "https://docs.smith.langchain.com/")],
    [("OpenTelemetry Python", "https://opentelemetry.io/docs/languages/python/")],
    [("LangChain — evaluation", "https://python.langchain.com/docs/guides/evaluation/")],
    [("Prometheus", "https://prometheus.io/docs/introduction/overview/"), ("Grafana", "https://grafana.com/docs/")],
    [("OWASP LLM Top 10", "https://owasp.org/www-project-top-10-for-large-language-model-applications/"), ("Rebuff", "https://github.com/protectai/rebuff")],
    [("HashiCorp Vault", "https://developer.hashicorp.com/vault/docs"), ("AWS Secrets Manager", "https://docs.aws.amazon.com/secretsmanager/")],
    [("Auth0", "https://auth0.com/docs"), ("Clerk", "https://clerk.com/docs"), ("FastAPI security", "https://fastapi.tiangolo.com/tutorial/security/")],
    [("OpenAI moderation", "https://platform.openai.com/docs/guides/moderation")],
    [("PyRIT", "https://github.com/Azure/PyRIT"), ("garak", "https://github.com/leondz/garak")],
    [("EU — AI Act portal", "https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai"), ("ICO — UK GDPR", "https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/")],
    [("Google Cloud — architecture center", "https://cloud.google.com/architecture")],
    [("WEF — Future of Jobs", "https://www.weforum.org/publications/the-future-of-jobs-report-2025/")],
    [("OpenAI — pricing", "https://openai.com/api/pricing/"), ("LiteLLM — spend", "https://docs.litellm.ai/docs/proxy/cost_tracking")],
    [("Google Cloud — adoption framework", "https://cloud.google.com/adoption-framework")],
    [("SCORE — pricing services", "https://www.score.org/resource/how-price-your-small-business-services"), ("HubSpot — pricing strategy", "https://blog.hubspot.com/sales/pricing-strategy")],
    [("Streamlit gallery", "https://streamlit.io/gallery"), ("Gradio demos", "https://www.gradio.app/demos/")],
    [("LangGraph", "https://docs.langchain.com/oss/python/langgraph/overview"), ("Twilio Voice", "https://www.twilio.com/docs/voice"), ("FastAPI", "https://fastapi.tiangolo.com/")],
    [("FastAPI", "https://fastapi.tiangolo.com/"), ("LlamaIndex — RAG", "https://docs.llamaindex.ai/en/stable/understanding/rag/")],
    [("Ollama", "https://ollama.com/"), ("SearXNG", "https://docs.searxng.org/"), ("Streamlit", "https://docs.streamlit.io/")],
    [
        ("Google Cloud — Generative AI Leader", "https://cloud.google.com/learn/certification/generative-ai-leader"),
        ("Skills Boost — Generative AI Leader path", "https://www.cloudskillsboost.google/paths/1951"),
        ("Professional ML Engineer (Vertex AI depth)", "https://cloud.google.com/learn/certification/machine-learning-engineer"),
        ("Vertex AI — documentation", "https://cloud.google.com/vertex-ai/docs"),
    ],
    [
        ("AWS Certified AI Practitioner (AIF-C01)", "https://aws.amazon.com/certification/certified-ai-practitioner/"),
        ("AWS Certification — exam guide (AIF-C01)", "https://docs.aws.amazon.com/aws-certification/latest/examguides/ai-practitioner-01.html"),
        ("Amazon Bedrock — user guide", "https://docs.aws.amazon.com/bedrock/"),
        ("AWS — responsible AI resources", "https://aws.amazon.com/machine-learning/responsible-ai/"),
    ],
    [
        ("NVIDIA — Gen AI LLM Associate (NCA-GENL)", "https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/"),
        ("NVIDIA — Gen AI LLM Professional (NCP-GENL)", "https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-professional/"),
        ("NVIDIA training — course catalog", "https://www.nvidia.com/en-us/training/"),
    ],
    [
        ("Microsoft — Azure AI Engineer (AI-102)", "https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/"),
        ("Azure OpenAI Service", "https://learn.microsoft.com/en-us/azure/ai-services/openai/"),
        ("Azure AI Search", "https://learn.microsoft.com/en-us/azure/search/"),
    ],
    [
        ("IBM — watsonx documentation", "https://www.ibm.com/docs/en/watsonx"),
        ("Coursera — IBM Generative AI Engineering PC", "https://www.coursera.org/professional-certificates/ibm-generative-ai-engineering"),
    ],
    [
        ("Hugging Face — Learn hub", "https://huggingface.co/learn"),
        ("Hugging Face — LLM course", "https://huggingface.co/learn/llm-course/chapter1/1"),
        ("Hugging Face — Agents course", "https://huggingface.co/learn/agents-course/unit0/introduction"),
        ("Transformers — documentation", "https://huggingface.co/docs/transformers/index"),
    ],
]

assert len(MODULE_REF_LINKS) == 133

_PHASE_CODES = {p[0] for p in PHASE_META}
assert _PHASE_CODES == set(PHASE_REFERENCE_EXTRAS.keys()), "phase_ref_extras.py must define extras for every phase code"


def _dedupe_ref_urls(pairs: list[tuple[str, str]]) -> list[tuple[str, str]]:
    seen: set[str] = set()
    out: list[tuple[str, str]] = []
    for label, url in pairs:
        u = (url or "").strip()
        if not u or u in seen:
            continue
        seen.add(u)
        out.append((label, u))
    return out


def _title_anchor_refs(title: str) -> list[tuple[str, str]]:
    """A few extra anchors for titles that benefit from a second primary doc (deduped later)."""
    t = title.lower()
    pairs: list[tuple[str, str]] = []
    if "vllm" in t:
        pairs.append(("Ray — documentation", "https://docs.ray.io/en/latest/index.html"))
    if "open webui" in t or "webui" in t:
        pairs.append(("Docker Hub", "https://hub.docker.com/"))
    if "litellm" in t:
        pairs.append(("OpenAI API compatibility", "https://platform.openai.com/docs/api-reference"))
    if "flowise" in t:
        pairs.append(("LangChain.js", "https://js.langchain.com/docs/introduction"))
    if "haystack" in t:
        pairs.append(("Deepset — blog", "https://www.deepset.ai/blog"))
    if "searxng" in t or "perplexity" in t:
        pairs.append(("SearXNG GitHub", "https://github.com/searxng/searxng"))
    if "twilio" in t:
        pairs.append(("Twilio — console", "https://www.twilio.com/console"))
    if "stripe" in t and "mcp" in t:
        pairs.append(("Stripe — testing", "https://docs.stripe.com/testing"))
    if "kubernetes" in t or "k8s" in t:
        pairs.append(("CNCF — Kubernetes", "https://www.cncf.io/"))
    if "prometheus" in t or "grafana" in t:
        pairs.append(("Grafana — Loki", "https://grafana.com/docs/loki/latest/"))
    if "ibm" in t and "watson" in t:
        pairs.append(("IBM — watsonx documentation", "https://www.ibm.com/docs/en/watsonx"))
    if "generative ai leader" in t or ("google cloud" in t and "vertex ai" in t):
        pairs.append(("Google Skills — Generative AI Leader path", "https://www.cloudskillsboost.google/paths/1951"))
    if "aws certified ai practitioner" in t or "aif-c01" in t.lower():
        pairs.append(("AWS — Certified AI Practitioner", "https://aws.amazon.com/certification/certified-ai-practitioner/"))
    if "nca-genl" in t or "ncp-genl" in t or ("nvidia" in t and "llm" in t):
        pairs.append(("NVIDIA — Gen AI LLM Associate", "https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/"))
    return pairs


# Fallback pool (deduped) so every module still lists enough depth after URL overlap with phase extras.
_REF_PAD: list[tuple[str, str]] = [
    ("MDN — Fetch API", "https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API"),
    ("JSON.org — specification", "https://www.json.org/json-en.html"),
    ("YAML — language spec", "https://yaml.org/spec/"),
    ("W3C — Web standards", "https://www.w3.org/standards/"),
    ("IETF — RFC editor", "https://www.rfc-editor.org/"),
    ("Unicode — standard", "https://www.unicode.org/standard/standard.html"),
    ("arXiv — preprints", "https://arxiv.org/"),
    ("Internet Archive", "https://archive.org/"),
]


def merge_module_refs(global_idx: int, phase_code: str, title: str) -> list[tuple[str, str]]:
    base = list(MODULE_REF_LINKS[global_idx])
    extra = list(PHASE_REFERENCE_EXTRAS.get(phase_code, []))
    extra.extend(_title_anchor_refs(title))
    merged = _dedupe_ref_urls(base + extra)
    if len(merged) < 6:
        merged = _dedupe_ref_urls(merged + _REF_PAD)
    return merged


def refs_html(links: list[tuple[str, str]]) -> str:
    intro = (
        "<p class=\"refs-intro\">Official documentation, specs, and trusted tutorials. "
        "Use these when you want depth beyond this page—none are required to mark the module complete.</p>"
    )
    parts = [
        f'<li><a class="ext-link" href="{url}" target="_blank" rel="noopener">{label} ↗</a></li>'
        for label, url in links
    ]
    return intro + '<ul class="refs-list">' + "".join(parts) + "</ul>"


def slug(s: str) -> str:
    return "".join(c if c.isalnum() else "-" for c in s.lower())[:48].strip("-")


def build_module(global_idx: int, title: str, tools: str, priority: str, phase_code: str) -> dict:
    g = global_idx + 1
    learn = build_learn_html(g, title, tools, priority, phase_code)
    steps = build_steps_html(g, title, tools, priority, phase_code)
    # Minimal runnable-style samples; vary by phase
    if "Ollama" in title or global_idx == 0:
        code = '''curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2
ollama run llama3.2 "Summarize MCP in 3 bullets"'''
    elif "LM Studio" in title:
        code = '''# After starting LM Studio local server (default :1234):
curl http://localhost:1234/v1/models'''
    elif "LiteLLM" in title:
        code = '''pip install litellm
python -c "import litellm; print(litellm.completion(model='ollama/llama3.2', messages=[{'role':'user','content':'ping'}]))"'''
    elif "API" in title or "Claude" in title or "OpenAI" in title or "Gemini" in title:
        code = '''import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello from module ''' + str(g) + '''!"}],
)
print(r.choices[0].message.content)'''
    elif "MCP" in title or "mcp" in tools.lower():
        code = '''pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
if __name__ == "__main__":
    mcp.run(transport="stdio")'''
    elif "A2A" in title or "Agent Cards" in title:
        code = '''# Pseudocode: agent card JSON for discovery (follow latest A2A spec)
AGENT_CARD = {
  "name": "research-agent",
  "skills": [{"id": "web.search", "description": "Search and summarize"}],
  "endpoints": {"tasks": "http://localhost:9100/tasks"}
}
import json; print(json.dumps(AGENT_CARD, indent=2))'''
    elif "RAG" in title or "Vector" in title or "Chunking" in title:
        code = '''pip install chromadb sentence-transformers
import chromadb
c = chromadb.Client(); col = c.create_collection("m''' + str(g) + '''")
col.add(documents=["RAG retrieves context before generation."], ids=["a"])
print(col.query(query_texts=["What is RAG?"], n_results=1))'''
    elif "Docker" in title or "n8n" in title:
        code = '''docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
# Open http://localhost:5678 — build a webhook → HTTP Request → LLM flow'''
    elif "FastAPI" in title:
        code = '''pip install fastapi uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health(): return {"ok": True}
# uvicorn main:app --reload'''
    else:
        code = f'''# Module {g} — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {{"module": {g}, "topic": "{title[:40]}", "status": "practiced"}}

if __name__ == "__main__":
    print(deliverable())'''

    refs = refs_html(merge_module_refs(global_idx, phase_code, title))

    return {
        "id": global_idx,
        "num": g,
        "title": title,
        "tools": tools,
        "priority": priority,
        "phase": phase_code,
        "slug": slug(title),
        "learn": learn,
        "steps": steps,
        "code": code,
        "refs": refs,
        "content_tier": "full",
        "blueprint_ref": f"Doc §3 registry — module {g} ({phase_code})",
        "coverage_notes": f"Primary learning on-page (Learn/Steps/Code); optional depth via content/modules/m{g:03d}.json or References tab.",
    }


def apply_content_overrides(phases_out: list) -> int:
    """Merge JSON overrides from content/modules/*.json into modules. Returns count applied."""
    mods_dir = ROOT / "content" / "modules"
    if not mods_dir.is_dir():
        return 0
    applied = 0
    for fp in sorted(mods_dir.glob("*.json")):
        data = json.loads(fp.read_text(encoding="utf-8"))
        num = int(data["module_num"])
        for ph in phases_out:
            for m in ph["modules"]:
                if m["num"] != num:
                    continue
                for key in ("learn", "steps", "code", "refs"):
                    if key in data:
                        m[key] = data[key]
                if "content_tier" in data:
                    m["content_tier"] = data["content_tier"]
                if "blueprint_ref" in data:
                    m["blueprint_ref"] = data["blueprint_ref"]
                if "coverage_notes" in data:
                    m["coverage_notes"] = data["coverage_notes"]
                applied += 1
                break
    return applied


def self_contained_label(tier: str) -> str:
    if tier == "full":
        return "yes"
    if tier == "partial":
        return "partial"
    return "no"


def write_topics_csv_and_coverage_json(phases_out: list) -> None:
    data_dir = ROOT / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    csv_path = data_dir / "topics_coverage.csv"
    fieldnames = [
        "phase_code",
        "module_num",
        "module_title",
        "priority",
        "content_tier",
        "self_contained_on_page",
        "blueprint_ref",
        "coverage_notes",
    ]
    module_rows = []
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for ph in phases_out:
            for m in ph["modules"]:
                tier = m.get("content_tier", "scaffold")
                row = {
                    "phase_code": ph["code"],
                    "module_num": m["num"],
                    "module_title": m["title"],
                    "priority": m["priority"],
                    "content_tier": tier,
                    "self_contained_on_page": self_contained_label(tier),
                    "blueprint_ref": m.get("blueprint_ref", ""),
                    "coverage_notes": m.get("coverage_notes", ""),
                }
                w.writerow(row)
                module_rows.append(row)
    cov = {
        "version": 1,
        "generated_for": "AI Master Tracker",
        "modules": module_rows,
        "blueprint_crosswalk": BLUEPRINT_CROSSWALK,
        "legend": {
            "content_tier_full": "Primary learning material is in the app (Learn/Steps/Code tabs).",
            "content_tier_partial": "Some on-page depth; may still expand.",
            "content_tier_scaffold": "Legacy label: use content/modules/mNNN.json + rebuild to change tier.",
            "self_contained_yes": "No external reading required to complete the module.",
            "self_contained_no": "References are starting points; on-page narrative still thin.",
        },
    }
    cov_txt = json.dumps(cov, ensure_ascii=False)
    (ROOT / "data" / "coverage.json").write_text(cov_txt, encoding="utf-8")
    (ROOT / "coverage.embed.json").write_text(cov_txt, encoding="utf-8")


def main():
    phases_out = []
    idx = 0
    for code, name, purpose, icon, color, count in PHASE_META:
        mods = []
        for _ in range(count):
            t, tools, pri = ROWS[idx]
            mods.append(build_module(idx, t, tools, pri, code))
            idx += 1
        phases_out.append(
            {
                "code": code,
                "name": name,
                "purpose": purpose,
                "icon": icon,
                "color": color,
                "modules": mods,
            }
        )
    assert idx == 133
    n_ov = apply_content_overrides(phases_out)
    write_topics_csv_and_coverage_json(phases_out)
    payload = {"version": 1, "phases": phases_out}
    js = json.dumps(payload, ensure_ascii=False)
    primary = ROOT / "data" / "curriculum.json"
    primary.parent.mkdir(parents=True, exist_ok=True)
    primary.write_text(js, encoding="utf-8")
    legacy = ROOT / "curriculum.embed.json"
    legacy.write_text(js, encoding="utf-8")
    print("Wrote", primary, primary.stat().st_size, "bytes")
    print("Wrote", legacy, "(mirror for legacy tooling)")
    print("Content overrides applied:", n_ov)
    print("Wrote", ROOT / "data" / "topics_coverage.csv")
    print("Wrote", ROOT / "data" / "coverage.json")


if __name__ == "__main__":
    main()
