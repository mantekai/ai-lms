## 6. FULL CURRICULUM SPECIFICATION

### 6.1 Overview

| Stat | Value |
|------|-------|
| Total Phases | 20 (P0–P19) |
| Total Modules | 133 (growing via AI agents) |
| Core Modules | ~110 (MUST DO) |
| Optional Modules | ~23 (depth tracks) |
| Capstone Projects | 4 |
| Certifications tracked | 42+ |
| Hackathons | 7 |
| YC-Style Ideas | 9 |
| Open Source Targets | 8 |

### 6.2 The 20 Phases



### 6.3 Detailed Phase & Module Specifications

> Every module below includes: purpose, full module list with priority and tools, learn content, practice steps, and starter code.


#### P0 — Local AI Setup
**Purpose:** Full local AI environment before writing agent code

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 1 | Ollama Setup & Local Model Running | Core | Ollama, llama3, mistral |
| 2 | LM Studio — GUI for Local LLMs | Core | LM Studio, GGUF models |
| 3 | Open WebUI — Local ChatGPT Interface | Core | Open WebUI, Docker |
| 4 | vLLM — High-Performance Inference | Opt | vLLM, CUDA, Python |
| 5 | LiteLLM Routing & Load Balancing | Core | LiteLLM, proxy server |
| 6 | Free APIs: Groq, Gemini, Mistral, OpenRouter | Core | Groq API, Gemini, OpenRouter |


**Module 1: Ollama Setup & Local Model Running** [Core] | Tools: `Ollama, llama3, mistral`
- Learn: OverviewModule 1 (P0) — Ollama Setup & Local Model Running. Tools focus: Ollama, llama3, mistral. Core path — prioritize in your sprint.Ollama runs open-weight models locally with a simple CLI and HTTP API. Models ship as downloadable blobs; you pull once and run offline-capable inference on CPU or GPU depending on size.Practice the full loop: install, pull a 7–8B-class model, run interactive chat, then call the HTTP API from a script. Note RAM/VRAM limits — if generation is slow, that is expect
- Practice: Install Ollama from the official site for your OS; confirm `ollama --version`.Run `ollama pull` for a small chat model (e.g. llama3.2 or mistral) and wait for completion.Use `ollama run <model>` with three prompts: factual, reasoning, and code generation.From another terminal, hit the local HTTP API with curl or httpx using the same model.Document hardware (RAM/GPU), model size, and tokens/sec in 
- Code: `curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2
ollama run llama3.2 "Summarize MCP in 3 bullets"`

**Module 2: LM Studio — GUI for Local LLMs** [Core] | Tools: `LM Studio, GGUF models`
- Learn: OverviewModule 2 (P0) — LM Studio — GUI for Local LLMs. Tools focus: LM Studio, GGUF models. Core path — prioritize in your sprint.LM Studio provides a desktop UI for discovering GGUF checkpoints, loading them with configurable context and GPU layers, and exposing an OpenAI-compatible local server (often on port 1234).Learn when GUI workflows beat CLI-only runners: comparing quantizations (Q4_K_M vs Q8), toggling GPU offload, and debugging tokenizer mismatches when copying prompts from hosted AP
- Practice: Install LM Studio; download one GGUF model appropriate for your machine.Start a local server; verify `GET /v1/models` returns your loaded model.From Python or curl, send a chat completion to the local OpenAI-compatible endpoint.Experiment with GPU layer count: note speed vs quality trade-offs in a short table.Export your server settings screenshot + one sample request/response (redact any sensitiv
- Code: `# After starting LM Studio local server (default :1234):
curl http://localhost:1234/v1/models`

**Module 3: Open WebUI — Local ChatGPT Interface** [Core] | Tools: `Open WebUI, Docker`
- Learn: OverviewModule 3 (P0) — Open WebUI — Local ChatGPT Interface. Tools focus: Open WebUI, Docker. Core path — prioritize in your sprint.Open WebUI is a browser front-end for many backends (Ollama, OpenAI-compatible proxies). Docker is the common install path; you get multi-user patterns, model switching, and optional RAG plugins depending on build.Focus on operational concerns: volume mounts for persistence, upgrading images, and separating internal vs external network exposure if you demo on a lap
- Practice: Run Open WebUI via the documented Docker command; confirm the UI loads on localhost.Connect the UI to your local Ollama or LM Studio backend; send test chats through both.Create two model presets (e.g. fast vs quality) and document when you would use each.Back up or note the Docker volume path so you can recreate the environment.List one limitation you hit (auth, plugins, model list) and how you w
- Code: `# Module 3 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 3, "topic": "Open WebUI — Local ChatGPT Interface"`

**Module 4: vLLM — High-Performance Inference** [Optional] | Tools: `vLLM, CUDA, Python`
- Learn: OverviewModule 4 (P0) — vLLM — High-Performance Inference. Tools focus: vLLM, CUDA, Python. Optional depth — revisit when you need this specialty.vLLM targets high-throughput GPU serving with PagedAttention and continuous batching. It is the layer beneath many internal model-serving stacks when latency under load matters more than a desktop GUI.Understand CUDA/driver expectations, batching knobs, and when vLLM is overkill vs Ollama for solo development.
- Practice: Read the official installation prerequisites (CUDA version, GPU memory).Launch a minimal OpenAI-compatible server with a documented quickstart model.Send concurrent requests (simple script) and observe throughput vs single-threaded local runners.Capture one error from misconfigured CUDA or OOM and document the fix path.Write two sentences: when you would choose vLLM vs a simpler local runner for a
- Code: `# Module 4 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 4, "topic": "vLLM — High-Performance Inference", "`

**Module 5: LiteLLM Routing & Load Balancing** [Core] | Tools: `LiteLLM, proxy server`
- Learn: OverviewModule 5 (P0) — LiteLLM Routing & Load Balancing. Tools focus: LiteLLM, proxy server. Core path — prioritize in your sprint.LiteLLM is a unified router: one interface to many providers and local endpoints, with optional proxy features for budgets, fallbacks, and load balancing. It fits teams that standardize on OpenAI-style request bodies.Practice routing the same prompt to a local model and a hosted model; compare responses and failure modes when a backend is down.
- Practice: Install LiteLLM; configure at least two backends (e.g. Ollama + one hosted key).Send a completion through LiteLLM using the unified model string format.Simulate a failing backend; configure a fallback model and verify the request succeeds.Enable or inspect spend logging (if using proxy mode) with synthetic requests only.Document your routing table and when each backend is chosen.
- Code: `pip install litellm
python -c "import litellm; print(litellm.completion(model='ollama/llama3.2', messages=[{'role':'user','content':'ping'}]))"`

**Module 6: Free APIs: Groq, Gemini, Mistral, OpenRouter** [Core] | Tools: `Groq API, Gemini, OpenRouter`
- Learn: OverviewModule 6 (P0) — Free APIs: Groq, Gemini, Mistral, OpenRouter. Tools focus: Groq API, Gemini, OpenRouter. Core path — prioritize in your sprint.Free or low-cost hosted APIs (Groq LPU-style inference, Gemini developer tier, Mistral keys, OpenRouter aggregation) let you prototype without training models. Each has different rate limits, safety filters, and JSON/tooling support.Build a comparison matrix: latency, max context, function-calling support, and pricing unit. Never ship production t
- Practice: Create sandbox keys for at least two listed providers; store them only in env vars.Run the same three prompts through each; log latency and rough quality notes.Check each vendor's rate-limit headers or dashboard; note burst vs sustained limits.Identify which provider supports tool calling for your SDK version — try one tool call if available.Summarize in one page which provider you would default t
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

#### P1 — AI Foundations
**Purpose:** LLMs, transformers, embeddings, ML paradigms

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 7 | Top 40 AI Terms & Core Concepts | Core | Flashcards, terminology |
| 8 | How LLMs Work: Transformers & Tokenization | Core | Hugging Face, tiktoken |
| 9 | Embeddings & Vector Representations | Core | OpenAI Embeddings, SBERT |
| 10 | Inference, Context Windows & Cost Optimisation | Core | Token counters, model APIs |
| 11 | Quantization & Model Efficiency | Opt | GGUF, GPTQ, bitsandbytes |
| 12 | GPU/TPU & Compute for AI | Opt | CUDA, Colab, RunPod |
| 13 | ML Paradigms: Supervised, Unsupervised, RL | Core | scikit-learn, OpenAI Gym |
| 14 | Generative AI Pipeline (Input→Process→Output) | Core | OpenAI API, LangChain |


**Module 7: Top 40 AI Terms & Core Concepts** [Core] | Tools: `Flashcards, terminology`
- Learn: How to use this moduleStudy every term below until you can define it in your own words in under 30 seconds. References at the end are optional for deeper reading—not required to complete the module.1 — Core AI conceptsAGI (Artificial General Intelligence)Hypothetical systems that match or exceed human ability across the full range of cognitive tasks, not just a narrow skill. Today’s products are narrow AI; AGI remains a research and safety discussion, not a shipped product category.AI modelA lea
- Practice: Read all 40 definitions without skipping. Highlight any term you cannot paraphrase.Make a two-column sheet: Term | Your one-sentence definition — fill it from memory, then self-check against this page.Pick five terms that matter most to your target role (e.g. RAG, MCP, hallucination, context window, fine-tuning) and write a short scenario where each appears in a product decision.Optional: pair eac
- Code: `# Tokenisation demo — ties to: token, context window, cost per token
# pip install tiktoken
import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")
text = "RAG reduces hallucinations when retrieva`

**Module 8: How LLMs Work: Transformers & Tokenization** [Core] | Tools: `Hugging Face, tiktoken`
- Learn: OverviewModule 8 (P1) — How LLMs Work: Transformers & Tokenization. Tools focus: Hugging Face, tiktoken. Core path — prioritize in your sprint.Transformers use self-attention so every position can attend to every other position in parallel — the architectural basis of modern LLMs. Tokenization turns text into subword IDs; context length and cost follow from token counts.Connect Hugging Face ecosystem concepts (configs, tokenizers) to what you see in API billing. Optional: load a small tokenizer 
- Practice: Skim the Illustrated Transformer or HF docs summary; draw a one-page diagram: embedding → layers → logits.Run a tokenizer (HF or tiktoken) on three prompt shapes: code, bullet list, long paragraph.Compare token counts for the same meaning in verbose vs concise English.Note how special tokens (BOS/EOS/pad) appear in your encoder output.Write five bullets linking attention to long-context cost in pr
- Code: `# Module 8 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 8, "topic": "How LLMs Work: Transformers & Tokeniz`

**Module 9: Embeddings & Vector Representations** [Core] | Tools: `OpenAI Embeddings, SBERT`
- Learn: OverviewModule 9 (P1) — Embeddings & Vector Representations. Tools focus: OpenAI Embeddings, SBERT. Core path — prioritize in your sprint.Embeddings map text (or images) into dense vectors so semantic similarity becomes geometry: cosine distance in vector space approximates related meaning. They power retrieval, clustering, and RAG front-ends.Contrast OpenAI-style embedding endpoints with open sentence-transformer models you can run locally. Understand normalization, dimensionality, and when to 
- Practice: Embed ten short phrases (two similar pairs, one opposite pair) using one API or local model.Compute cosine similarity between vectors; sanity-check that related phrases score higher.Change one word in a phrase and measure how much the vector shifts.Document embedding dimension and model version used — versioning matters for retrieval indexes.List one failure mode (polysemy, language mix) and a mit
- Code: `pip install chromadb sentence-transformers
import chromadb
c = chromadb.Client(); col = c.create_collection("m9")
col.add(documents=["RAG retrieves context before generation."], ids=["a"])
print(col.q`

**Module 10: Inference, Context Windows & Cost Optimisation** [Core] | Tools: `Token counters, model APIs`
- Learn: OverviewModule 10 (P1) — Inference, Context Windows & Cost Optimisation. Tools focus: Token counters, model APIs. Core path — prioritize in your sprint.Inference is the forward pass at serving time — distinct from training. Context windows cap how much text fits in one call; providers bill input and output tokens separately, and long prompts hit latency and cost cliffs.Practice measuring tokens before send, trimming history, summarizing threads, and choosing smaller models for easy subtasks.
- Practice: Pick a tokenizer or API metadata; measure tokens for a long thread before and after summarization.Call a chat model with the same task using a large vs small model; compare cost and latency.Implement a simple token budget guard that refuses or compresses when over a threshold.Read provider docs for max context and output limits; note what happens on overflow.Write a stakeholder-friendly paragraph 
- Code: `# Module 10 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 10, "topic": "Inference, Context Windows & Cost O`

**Module 11: Quantization & Model Efficiency** [Optional] | Tools: `GGUF, GPTQ, bitsandbytes`
- Learn: OverviewModule 11 (P1) — Quantization & Model Efficiency. Tools focus: GGUF, GPTQ, bitsandbytes. Optional depth — revisit when you need this specialty.Quantization reduces weight precision (e.g. FP16 → INT8 → 4-bit) to shrink memory and speed inference. GGUF bundles for llama.cpp, GPTQ, and bitsandbytes QLoRA during training are common touchpoints.Understand accuracy vs size trade-offs and why quantized models behave slightly differently on code or math.
- Practice: Read one official guide each for GGUF inference vs training-time quantization (QLoRA).Run one pre-quantized model locally; note RAM/VRAM vs full precision expectations.List three metrics you would monitor if you switched quantization in production (latency, perplexity, task evals).Identify a task where low-bit quantization might fail (e.g. long arithmetic) and test informally.Summarize when you wo
- Code: `# Module 11 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 11, "topic": "Quantization & Model Efficiency", "`

**Module 12: GPU/TPU & Compute for AI** [Optional] | Tools: `CUDA, Colab, RunPod`
- Learn: OverviewModule 12 (P1) — GPU/TPU & Compute for AI. Tools focus: CUDA, Colab, RunPod. Optional depth — revisit when you need this specialty.GPUs parallelize matrix multiply for training and inference; TPUs are Google’s ASIC line for large matmul workloads. Colab and cloud pods abstract hardware, but data movement and memory bandwidth still dominate.Map a simple training or inference job to GPU memory usage — batch size, sequence length, and precision interact.
- Practice: List differences between latency-sensitive inference and throughput-heavy training on GPUs.Spin up one GPU notebook or pod; run a tiny matmul or model forward pass; note device name and memory.Read vendor docs for one TPU offering; compare programming model to CUDA briefly.Estimate rough VRAM needs for a model size you care about (parameters × precision heuristic).Document one operational issue: d
- Code: `# Module 12 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 12, "topic": "GPU/TPU & Compute for AI", "status"`

**Module 13: ML Paradigms: Supervised, Unsupervised, RL** [Core] | Tools: `scikit-learn, OpenAI Gym`
- Learn: OverviewModule 13 (P1) — ML Paradigms: Supervised, Unsupervised, RL. Tools focus: scikit-learn, OpenAI Gym. Core path — prioritize in your sprint.Supervised learning fits labeled pairs; unsupervised structure learns without per-example labels; RL optimizes policies via rewards. Generative models (including LLMs) are often pretrained with self-supervised next-token objectives.Place LLM fine-tuning and RLHF in this map so you can explain trade-offs to non-specialists.
- Practice: For each paradigm, write one real-world example (not toy XOR) relevant to business data.Run a minimal sklearn supervised example; note fit/predict vs generative “generate” APIs.Explain why RLHF is related to RL but not the same as classic game-playing RL.List where unsupervised embeddings appear in your RAG or search roadmap.Create a comparison table: data needs, evaluation, and typical risk for e
- Code: `# Module 13 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 13, "topic": "ML Paradigms: Supervised, Unsupervi`

**Module 14: Generative AI Pipeline (Input→Process→Output)** [Core] | Tools: `OpenAI API, LangChain`
- Learn: OverviewModule 14 (P1) — Generative AI Pipeline (Input→Process→Output). Tools focus: OpenAI API, LangChain. Core path — prioritize in your sprint.A generative pipeline moves from prompt or UI input through preprocessing, model call, optional tools/RAG, post-processing, and logging. Reliability comes from contracts at each hop — schemas, timeouts, and fallbacks.Sketch your own diagram for a support-bot vs a batch summariser; identify different bottlenecks.
- Practice: Draw input→process→output for one product idea; annotate trust boundaries and PII touchpoints.Implement a toy pipeline in Python: validate input → call model → validate output JSON.Add structured logging at each stage without logging secrets or user content raw.Identify two stages where caching would help and what invalidation policy you need.Write acceptance criteria for “done” that include laten
- Code: `# Module 14 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 14, "topic": "Generative AI Pipeline (Input→Proce`

#### P2 — Prompt Engineering
**Purpose:** The primary interface to models

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 15 | Prompt Engineering Fundamentals | Core | Claude, GPT-4, PromptPerfect |
| 16 | Chain-of-Thought (CoT) Prompting | Core | GPT-4o, Claude, Gemini |
| 17 | Context Management & Context Window | Core | LangChain Memory, Claude 200K |
| 18 | Multi-Agent & Goal-Oriented Prompts | Core | CrewAI, AutoGen |
| 19 | Self-Critique, Retry Loops & Reflexion | Core | LangGraph, custom Python |
| 20 | Task Planning Prompts & Role Prompting | Core | Claude, GPT-4, Perplexity |
| 21 | Prompt Chaining & Advanced Techniques | Core | LangChain, LangGraph, LCEL |


**Module 15: Prompt Engineering Fundamentals** [Core] | Tools: `Claude, GPT-4, PromptPerfect`
- Learn: OverviewModule 15 (P2) — Prompt Engineering Fundamentals. Tools focus: Claude, GPT-4, PromptPerfect. Core path — prioritize in your sprint.Prompt engineering is the highest-ROI lever before changing models: clarity, format, examples (few-shot), and role framing steer behaviour more cheaply than fine-tunes for many tasks.Practice rewriting vague prompts into instructions with constraints, output format (JSON/Markdown), and evaluation rubrics you can automate later.
- Practice: Take one business task; write a bad prompt, then two improved iterations with explicit format.Add a negative constraint (“do not”) and verify the model respects it on five trials.Compare zero-shot vs two-shot for a structured extraction task; score with a simple checklist.Document temperature and max-tokens choices and why they fit this task.Peer-review another learner’s prompt for ambiguity; revi
- Code: `# Module 15 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 15, "topic": "Prompt Engineering Fundamentals", "`

**Module 16: Chain-of-Thought (CoT) Prompting** [Core] | Tools: `GPT-4o, Claude, Gemini`
- Learn: OverviewModule 16 (P2) — Chain-of-Thought (CoT) Prompting. Tools focus: GPT-4o, Claude, Gemini. Core path — prioritize in your sprint.Chain-of-thought elicits intermediate reasoning before answers, improving multi-step math and logic when the model is instructed to show steps — but increases tokens and can leak verbose internals.Learn when to keep reasoning hidden from end users vs when to display it for auditability.
- Practice: Solve five numeric word problems with and without CoT; compare accuracy.Ask for explicit “final answer in a box” after reasoning to separate UI from chain.Measure token increase from CoT; decide if cost is justified per task.Try a self-consistency variant (multiple chains, vote) on one hard puzzle.Note one failure mode (overconfident wrong chain) and a guardrail.
- Code: `# Module 16 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 16, "topic": "Chain-of-Thought (CoT) Prompting", `

**Module 17: Context Management & Context Window** [Core] | Tools: `LangChain Memory, Claude 200K`
- Learn: OverviewModule 17 (P2) — Context Management & Context Window. Tools focus: LangChain Memory, Claude 200K. Core path — prioritize in your sprint.Context management is how you fit history, documents, and tool results under a finite window: summarization, sliding windows, and structured memory objects. Long-context models reduce pressure but not cost.Implement a policy for what stays verbatim vs summarized in a conversational agent.
- Practice: Simulate a 20-turn chat; count tokens cumulatively with a tokenizer.Apply a summarise-every-N-turns policy; check information retention on a quiz.Compare “full history” vs “summary + last K turns” on task success.Read provider notes on prompt caching where applicable; note billing impact.Write rules for when to reset context vs fork a new session.
- Code: `# Module 17 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 17, "topic": "Context Management & Context Window`

**Module 18: Multi-Agent & Goal-Oriented Prompts** [Core] | Tools: `CrewAI, AutoGen`
- Learn: OverviewModule 18 (P2) — Multi-Agent & Goal-Oriented Prompts. Tools focus: CrewAI, AutoGen. Core path — prioritize in your sprint.Multi-agent prompting assigns roles (researcher, critic, writer) and coordinates hand-offs. Frameworks like CrewAI or AutoGen encode patterns, but the design principles are delegation, clear interfaces, and stop conditions.Focus on avoiding infinite chatter: budgets for rounds and explicit termination.
- Practice: Design three roles for one task; specify inputs/outputs per role as JSON fields.Run a minimal two-agent exchange in code or a framework; cap at three rounds.Log each hand-off; verify no duplicate work or contradictory assumptions.Add a critic step that checks format before final user-visible output.Retrospective: when would a single-agent prompt be simpler and safer?
- Code: `# Module 18 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 18, "topic": "Multi-Agent & Goal-Oriented Prompts`

**Module 19: Self-Critique, Retry Loops & Reflexion** [Core] | Tools: `LangGraph, custom Python`
- Learn: OverviewModule 19 (P2) — Self-Critique, Retry Loops & Reflexion. Tools focus: LangGraph, custom Python. Core path — prioritize in your sprint.Self-critique and reflexion patterns ask the model to evaluate its draft and revise. LangGraph and custom loops implement retries with state — production needs limits to avoid runaway spend.
- Practice: Implement generate→critique→revise for one writing task; stop after two revisions max.Compare single-pass vs two-pass quality using a rubric you define.Instrument token usage per revision; plot cost vs gain.Handle critique refusal or empty output gracefully in code.Document when reflexion is inappropriate (latency-sensitive chat).
- Code: `# Module 19 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 19, "topic": "Self-Critique, Retry Loops & Reflex`

**Module 20: Task Planning Prompts & Role Prompting** [Core] | Tools: `Claude, GPT-4, Perplexity`
- Learn: OverviewModule 20 (P2) — Task Planning Prompts & Role Prompting. Tools focus: Claude, GPT-4, Perplexity. Core path — prioritize in your sprint.Task planning prompts decompose goals into ordered steps; role prompting sets expertise and tone. Combine with explicit tool lists when the model should choose actions.
- Practice: Write a planner prompt that outputs a numbered plan only (no execution).Feed the plan to an executor prompt; check step adherence on a simple project.Swap roles (junior vs principal) and note behaviour changes.Add a checklist the model must tick before claiming completion.Capture one derailment (skipped step) and tighten the prompt.
- Code: `# Module 20 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 20, "topic": "Task Planning Prompts & Role Prompt`

**Module 21: Prompt Chaining & Advanced Techniques** [Core] | Tools: `LangChain, LangGraph, LCEL`
- Learn: OverviewModule 21 (P2) — Prompt Chaining & Advanced Techniques. Tools focus: LangChain, LangGraph, LCEL. Core path — prioritize in your sprint.Prompt chaining composes LCEL or LangGraph nodes so each stage has a contract. Advanced techniques include routing, parallel branches, and structured outputs between hops.
- Practice: Build a three-node chain: extract → transform → generate; validate JSON between nodes.Add a conditional branch on extracted intent; test two paths.Measure end-to-end latency vs monolithic prompt.Version prompts separately per node; document compatibility.List failure modes per hop and corresponding fallbacks.
- Code: `# Module 21 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 21, "topic": "Prompt Chaining & Advanced Techniqu`

#### P3 — LLMs & APIs
**Purpose:** Providers, auth, tools, multimodal

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 22 | OpenAI API Deep Dive (GPT-4, GPT-4o) | Core | openai Python SDK |
| 23 | Anthropic Claude API | Core | anthropic Python SDK |
| 24 | Google Gemini API | Core | google-generativeai |
| 25 | Mistral & Open Source LLMs (LLaMA, DeepSeek) | Core | Hugging Face, mistralai SDK |
| 26 | API Authentication & Rate Limiting | Core | API keys, backoff, tenacity |
| 27 | Toolformer / Function Calling | Core | OpenAI tools, Claude tool_use |
| 28 | Tool Invocation & Output Parsing | Core | Pydantic, json_schema, LangChain |
| 29 | Multimodal AI (Text + Image + Audio + Video) | Core | GPT-4V, Gemini, Pika, ElevenLabs |


**Module 22: OpenAI API Deep Dive (GPT-4, GPT-4o)** [Core] | Tools: `openai Python SDK`
- Learn: OverviewModule 22 (P3) — OpenAI API Deep Dive (GPT-4, GPT-4o). Tools focus: openai Python SDK. Core path — prioritize in your sprint.OpenAI's API is the reference stack for chat completions, structured outputs, embeddings, and tool calls in many production systems. You learn authentication, model selection, streaming vs batch, and how errors surface (rate limits, context length, content policy).Compare latency and cost across models in the same family (e.g. mini vs full) for your own prompt shap
- Practice: Create a project API key in the OpenAI console; store it as an environment variable only.Install the official SDK for your language; run a minimal chat completion against a small model.Add structured logging: model name, latency, input/output token counts (no raw PII in logs).Call the same prompt with two model sizes; compare quality, latency, and documented pricing.Write a short openai Python SDK
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

**Module 23: Anthropic Claude API** [Core] | Tools: `anthropic Python SDK`
- Learn: OverviewModule 23 (P3) — Anthropic Claude API. Tools focus: anthropic Python SDK. Core path — prioritize in your sprint.Anthropic's API is the reference stack for chat completions, structured outputs, embeddings, and tool calls in many production systems. You learn authentication, model selection, streaming vs batch, and how errors surface (rate limits, context length, content policy).Compare latency and cost across models in the same family (e.g. mini vs full) for your own prompt shapes. Log re
- Practice: Create a project API key in the Anthropic console; store it as an environment variable only.Install the official SDK for your language; run a minimal chat completion against a small model.Add structured logging: model name, latency, input/output token counts (no raw PII in logs).Call the same prompt with two model sizes; compare quality, latency, and documented pricing.Write a short anthropic Pyth
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

**Module 24: Google Gemini API** [Core] | Tools: `google-generativeai`
- Learn: OverviewModule 24 (P3) — Google Gemini API. Tools focus: google-generativeai. Core path — prioritize in your sprint.Google’s Gemini API exposes multimodal and long-context models with a distinct SDK surface from OpenAI. You learn API keys via AI Studio, model IDs, safety settings, and quota dashboards.Compare request/response shapes to OpenAI for the same task; note tool and JSON schema support per model generation.Store keys in GOOGLE_API_KEY or the env var your SDK expects.Log model id + laten
- Practice: Create a key in Google AI Studio; export it to your shell environment only.Install google-genai or google-generativeai per current docs; list models available to your project.Run text and (if available) one image+text call; capture latency.Try structured output or function calling if supported on your chosen model.Write integration notes: differences vs OpenAI that would affect a shared abstractio
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

**Module 25: Mistral & Open Source LLMs (LLaMA, DeepSeek)** [Core] | Tools: `Hugging Face, mistralai SDK`
- Learn: OverviewModule 25 (P3) — Mistral & Open Source LLMs (LLaMA, DeepSeek). Tools focus: Hugging Face, mistralai SDK. Core path — prioritize in your sprint.Mistral’s hosted API and open-weights families (e.g. LLaMA-class, DeepSeek-class on Hugging Face) span commercial keys and self-hosted inference. Understand license tags, gated models, and HF tokens for downloads.Practice one hosted completion and one local or HF inference path so you can advise clients on lock-in vs control.
- Practice: Create a Mistral API key or HF token; never commit either.Call a Mistral chat model via official SDK or HTTP.Pull a small open model card on Hugging Face; read license and use restrictions.Run a minimal generate call locally or via inference endpoint if feasible.Summarize when you would recommend API vs self-host for a regulated client.
- Code: `# Module 25 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 25, "topic": "Mistral & Open Source LLMs (LLaMA, `

**Module 26: API Authentication & Rate Limiting** [Core] | Tools: `API keys, backoff, tenacity`
- Learn: OverviewModule 26 (P3) — API Authentication & Rate Limiting. Tools focus: API keys, backoff, tenacity. Core path — prioritize in your sprint.Production API usage requires key rotation, least privilege keys, exponential backoff on 429/5xx, and idempotency for retried writes. Centralize secrets in vaults or managed stores.Practice reading Retry-After headers and structuring tenacity (or equivalent) policies.
- Practice: Implement retries with jitter; never retry non-idempotent POSTs blindly without design.Log HTTP status and request id only — not payloads with PII.Simulate rate limits with a mock server or tiny limit in a test key.Document key rotation procedure for your team (who, how often, blast radius).Add a circuit breaker sketch: after N failures, fail fast and alert.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

**Module 27: Toolformer / Function Calling** [Core] | Tools: `OpenAI tools, Claude tool_use`
- Learn: OverviewModule 27 (P3) — Toolformer / Function Calling. Tools focus: OpenAI tools, Claude tool_use. Core path — prioritize in your sprint.Tool / function calling lets models emit structured actions the runtime executes. Schemas must be tight: enums, descriptions, and required fields reduce hallucinated arguments.
- Practice: Define one JSON schema tool; register it with the provider SDK you use.Handle tool_calls in a loop until the model returns user-visible content.Test three successful calls and two invalid-args paths; verify error handling.Compare parallel vs serial tool execution for your use case.Document trust boundaries: which tools can touch production data?
- Code: `# Module 27 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 27, "topic": "Toolformer / Function Calling", "st`

**Module 28: Tool Invocation & Output Parsing** [Core] | Tools: `Pydantic, json_schema, LangChain`
- Learn: OverviewModule 28 (P3) — Tool Invocation & Output Parsing. Tools focus: Pydantic, json_schema, LangChain. Core path — prioritize in your sprint.Parsing tool outputs into Pydantic models (or equivalent) enforces types before side effects. LangChain structured output helpers wrap similar ideas with retries.
- Practice: Return tool output as JSON; validate with Pydantic v2 models.Add a repair pass: on ValidationError, ask the model to fix shape.Unit-test parsers with golden files (no live API).Measure how often repair passes trigger in a 50-call sample.List schemas you would never auto-parse without human review.
- Code: `# Module 28 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 28, "topic": "Tool Invocation & Output Parsing", `

**Module 29: Multimodal AI (Text + Image + Audio + Video)** [Core] | Tools: `GPT-4V, Gemini, Pika, ElevenLabs`
- Learn: OverviewModule 29 (P3) — Multimodal AI (Text + Image + Audio + Video). Tools focus: GPT-4V, Gemini, Pika, ElevenLabs. Core path — prioritize in your sprint.Multimodal models accept images, audio, or video alongside text. Constraints include resolution limits, MIME handling, latency of uploads, and safety filters on media.
- Practice: Call a vision-capable model with three image types: chart, screenshot, photo.Compare text-only vs image+text answers on a diagram question.Handle oversized images: resize/compress pipeline with tests.Read provider limits on frames or duration for video inputs.Write privacy rules for user-uploaded media in logs and retention.
- Code: `# Module 29 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 29, "topic": "Multimodal AI (Text + Image + Audio`

#### P4 — Agent Fundamentals
**Purpose:** Architectures, planning, collaboration

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 30 | What Are AI Agents? Autonomous vs Semi-Auto | Core | LangChain, custom Python |
| 31 | Agent Architectures: ReAct, CAMEL, AutoGPT | Core | LangChain ReAct, AutoGPT |
| 32 | Goal Decomposition & Task Planning Algorithms | Core | LangGraph, custom planners |
| 33 | Decision-Making Policies for Agents | Core | LangGraph, state machines |
| 34 | Action Planning Loops & Execution | Core | LangGraph, ReAct pattern |
| 35 | Self-Reflection / Feedback Loops | Core | Reflexion, LangGraph |
| 36 | Multi-Agent Collaboration Patterns | Core | CrewAI, AutoGen, LangGraph |


**Module 30: What Are AI Agents? Autonomous vs Semi-Auto** [Core] | Tools: `LangChain, custom Python`
- Learn: OverviewModule 30 (P4) — What Are AI Agents? Autonomous vs Semi-Auto. Tools focus: LangChain, custom Python. Core path — prioritize in your sprint.Agents combine a language model with a control loop, tools, and memory to pursue multi-step goals. Semi-autonomous systems keep humans in the loop for approvals; fully autonomous loops need budgets and kill switches.
- Practice: Define “agent” vs “workflow script” for one use case in your words.List tools your agent would need; classify read vs write risk.Sketch state: what variables persist across turns?Identify stop conditions and max spend per task.Note one scenario where agents are the wrong abstraction.
- Code: `# Module 30 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 30, "topic": "What Are AI Agents? Autonomous vs S`

**Module 31: Agent Architectures: ReAct, CAMEL, AutoGPT** [Core] | Tools: `LangChain ReAct, AutoGPT`
- Learn: OverviewModule 31 (P4) — Agent Architectures: ReAct, CAMEL, AutoGPT. Tools focus: LangChain ReAct, AutoGPT. Core path — prioritize in your sprint.ReAct interleaves reasoning traces with tool calls; CAMEL-style role play coordinates two LLMs; AutoGPT popularized goal stacks. All share the risk of runaway loops without caps.
- Practice: Implement a minimal ReAct loop in pseudocode or LangChain with one tool.Log each thought/action/observation triplet for debugging.Compare CAMEL two-agent setup vs single-agent for the same task.Read AutoGPT architecture summary; list three production hazards.Write termination rules you would enforce in code, not prompts only.
- Code: `# Module 31 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 31, "topic": "Agent Architectures: ReAct, CAMEL, `

**Module 32: Goal Decomposition & Task Planning Algorithms** [Core] | Tools: `LangGraph, custom planners`
- Learn: OverviewModule 32 (P4) — Goal Decomposition & Task Planning Algorithms. Tools focus: LangGraph, custom planners. Core path — prioritize in your sprint.Goal decomposition turns vague objectives into ordered subtasks. Planners can be classical algorithms, LLM-generated plans, or hybrid graphs in LangGraph.
- Practice: Generate a plan for a multi-step research task; validate dependencies manually.Detect cyclic or impossible dependencies in the plan.Convert the plan into a LangGraph-style node list with edges.Simulate one failed subtask; define replanning policy.Estimate token cost of planning vs execution for your example.
- Code: `# Module 32 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 32, "topic": "Goal Decomposition & Task Planning `

**Module 33: Decision-Making Policies for Agents** [Core] | Tools: `LangGraph, state machines`
- Learn: OverviewModule 33 (P4) — Decision-Making Policies for Agents. Tools focus: LangGraph, state machines. Core path — prioritize in your sprint.Policies decide which tool or transition fires given state — epsilon-greedy exploration is rare in LLM agents; instead you use classifiers, routers, or scored choices. State machines keep behaviour auditable.
- Practice: Model agent state as an enum + small dict; document transitions.Implement if/match routing vs LLM-chosen tool once; compare failure rates on five cases.Add a default safe action when confidence is low.Log policy decisions with reasons (structured JSON).Describe how you would unit-test a policy without calling live models.
- Code: `# Module 33 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 33, "topic": "Decision-Making Policies for Agents`

**Module 34: Action Planning Loops & Execution** [Core] | Tools: `LangGraph, ReAct pattern`
- Learn: OverviewModule 34 (P4) — Action Planning Loops & Execution. Tools focus: LangGraph, ReAct pattern. Core path — prioritize in your sprint.Action planning loops execute tools, observe results, and continue until success criteria. Reliability requires timeouts, partial progress checkpoints, and idempotent tools where possible.
- Practice: Run a five-step synthetic task with mocked tools; verify ordering.Inject a tool timeout; ensure the loop surfaces a recoverable error.Persist partial results to disk or DB between steps.Measure wall-clock vs model time vs tool time.Define success predicates that code checks — not vibes.
- Code: `# Module 34 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 34, "topic": "Action Planning Loops & Execution",`

**Module 35: Self-Reflection / Feedback Loops** [Core] | Tools: `Reflexion, LangGraph`
- Learn: OverviewModule 35 (P4) — Self-Reflection / Feedback Loops. Tools focus: Reflexion, LangGraph. Core path — prioritize in your sprint.Self-reflection asks the model to critique prior outputs; multi-agent collaboration splits expertise. Combine with evaluation harnesses so reflection improves measurable scores.
- Practice: Pair generator and critic agents; cap at two critique rounds.Score outputs with a rubric before/after critique.Log whether critiques are actionable vs generic.Try a third agent as tie-breaker; note coordination overhead.Decide when human review replaces automated critique.
- Code: `# Module 35 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 35, "topic": "Self-Reflection / Feedback Loops", `

**Module 36: Multi-Agent Collaboration Patterns** [Core] | Tools: `CrewAI, AutoGen, LangGraph`
- Learn: OverviewModule 36 (P4) — Multi-Agent Collaboration Patterns. Tools focus: CrewAI, AutoGen, LangGraph. Core path — prioritize in your sprint.Tool-use system design covers discovery, schemas, authentication to backends, and principle of least privilege. Treat tools like microservices with contracts and audit trails.
- Practice: Inventory tools by data sensitivity (public, internal, PII).Draft OpenAPI-style descriptions for two tools; map to provider tool JSON.Implement auth per tool (API key, OAuth) without sharing one global secret.Add allowlists for domains or file paths.Red-team: what could a malicious prompt ask your tool to do?
- Code: `# Module 36 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 36, "topic": "Multi-Agent Collaboration Patterns"`

#### P5 — Tool Use & Integration
**Purpose:** Memory, APIs, files, search, browsing

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 37 | Tool Use System Design | Core | OpenAI tools, LangChain tools |
| 38 | Memory Integration (Short/Long-Term/Episodic) | Core | LangChain Memory, mem0 |
| 39 | External API Calling from Agents | Core | requests, httpx, LangChain |
| 40 | File Reader/Writer Tools | Core | Python I/O, LangChain tools |
| 41 | Python Execution Tools (Code Interpreter) | Core | E2B, Docker sandbox |
| 42 | Search & Retrieval Tools | Core | Tavily, SerpAPI, DuckDuckGo |
| 43 | Web Browsing Tools for Agents | Core | Playwright, Selenium, Firecrawl |
| 44 | AI Search Optimisation (AEO/GEO) | Opt | SearchAble, Outranking |


**Module 37: Tool Use System Design** [Core] | Tools: `OpenAI tools, LangChain tools`
- Learn: OverviewModule 37 (P5) — Tool Use System Design. Tools focus: OpenAI tools, LangChain tools. Core path — prioritize in your sprint.Memory types: short-term (conversation buffer), long-term (vector store of facts), episodic (past task traces). Stale memory hurts — TTLs and provenance matter.
- Practice: Choose one memory backend; store three synthetic “facts” with metadata.Retrieve with a natural-language query; verify precision.Expire or update one fact; confirm retrieval changes.Log memory writes with source and timestamp.List privacy implications of long-term user memory.
- Code: `# Module 37 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 37, "topic": "Tool Use System Design", "status": `

**Module 38: Memory Integration (Short/Long-Term/Episodic)** [Core] | Tools: `LangChain Memory, mem0`
- Learn: OverviewModule 38 (P5) — Memory Integration (Short/Long-Term/Episodic). Tools focus: LangChain Memory, mem0. Core path — prioritize in your sprint.Calling HTTP APIs from agents requires URL validation, SSRF protection, timeouts, and response size limits. Prefer typed clients (httpx) over ad-hoc requests in prompts.
- Practice: Wrap httpx calls with timeout + max bytes read.Block private IP ranges in a URL validator unittest.Parse JSON safely; handle HTML error pages.Add redaction of auth headers in logs.Document retry policy for idempotent GETs only.
- Code: `# Module 38 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 38, "topic": "Memory Integration (Short/Long-Term`

**Module 39: External API Calling from Agents** [Core] | Tools: `requests, httpx, LangChain`
- Learn: OverviewModule 39 (P5) — External API Calling from Agents. Tools focus: requests, httpx, LangChain. Core path — prioritize in your sprint.File tools read/write user or system files — highest risk surface. Sandboxed paths, extension allowlists, and size caps reduce exfiltration and destructive writes.
- Practice: Constrain reads to a single workspace directory in code.Reject symlinks escaping the workspace.Implement write with backup or dry-run mode.Test with oversized file and binary file edge cases.Describe how you’d add virus scanning for uploads in production.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

**Module 40: File Reader/Writer Tools** [Core] | Tools: `Python I/O, LangChain tools`
- Learn: OverviewModule 40 (P5) — File Reader/Writer Tools. Tools focus: Python I/O, LangChain tools. Core path — prioritize in your sprint.Code interpreter tools execute arbitrary code — use containers (E2B, Docker) with network disabled by default, CPU/memory limits, and short TTLs.
- Practice: Run hello-world in an isolated container or sandbox service.Disable outbound network in sandbox config; verify blocked.Set CPU and RAM limits; observe OOM behaviour.Whitelist allowed pip packages or base images.Write incident response if user code escapes sandbox (theoretical tabletop).
- Code: `# Module 40 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 40, "topic": "File Reader/Writer Tools", "status"`

**Module 41: Python Execution Tools (Code Interpreter)** [Core] | Tools: `E2B, Docker sandbox`
- Learn: OverviewModule 41 (P5) — Python Execution Tools (Code Interpreter). Tools focus: E2B, Docker sandbox. Core path — prioritize in your sprint.Search tools ground agents in fresh web data. Choose APIs with clear ToS; cache results; deduplicate snippets before stuffing context.
- Practice: Integrate one search API; fetch top five results for a query.Normalize titles/snippets; measure token cost to inject into prompt.Add query length limits and profanity filters if required by policy.Compare search-augmented vs non-search answer on a time-sensitive fact.Log query hashes instead of raw queries if PII is possible.
- Code: `# Module 41 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 41, "topic": "Python Execution Tools (Code Interp`

**Module 42: Search & Retrieval Tools** [Core] | Tools: `Tavily, SerpAPI, DuckDuckGo`
- Learn: OverviewModule 42 (P5) — Search & Retrieval Tools. Tools focus: Tavily, SerpAPI, DuckDuckGo. Core path — prioritize in your sprint.Browsing tools (Playwright, Firecrawl) render pages and extract content — fragile vs layout changes and heavy on resources. Prefer structured APIs when available.
- Practice: Fetch one static page and one SPA; note differences in extraction quality.Set navigation timeouts and user-agent responsibly.Strip scripts and ads before sending text to the model.Respect robots.txt for public projects; note legal nuance.Fallback path when page load fails mid-task.
- Code: `# Module 42 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 42, "topic": "Search & Retrieval Tools", "status"`

**Module 43: Web Browsing Tools for Agents** [Core] | Tools: `Playwright, Selenium, Firecrawl`
- Learn: OverviewModule 43 (P5) — Web Browsing Tools for Agents. Tools focus: Playwright, Selenium, Firecrawl. Core path — prioritize in your sprint.AEO/GEO optimises how brands appear in AI-generated answers vs classic blue-link SEO. Signals include factual consistency, structured data, and citation-friendly sources.
- Practice: There is no universal install checklist. Study how answer engines synthesise snippets, audit your public facts for consistency across pages, propose a measurement plan (branded queries in major assistants), and document three content changes you would pilot. Mark complete when your one-pager is reviewed by a peer.
- Code: `# Module 43 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 43, "topic": "Web Browsing Tools for Agents", "st`

**Module 44: AI Search Optimisation (AEO/GEO)** [Optional] | Tools: `SearchAble, Outranking`
- Learn: OverviewModule 44 (P5) — AI Search Optimisation (AEO/GEO). Tools focus: SearchAble, Outranking. Optional depth — revisit when you need this specialty.LangChain standardises chains, tools, retrievers, and LCEL composition. Learn when abstraction helps vs when raw SDK calls are clearer for small services.
- Practice: Build RunnableSequence with prompt | model | parser.Add a retriever + stuff chain for three documents.Swap LLM provider using LangChain adapters.Profile import time and cold start — note operational cost.List one feature you would not use in production and why.
- Code: `# Module 44 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 44, "topic": "AI Search Optimisation (AEO/GEO)", `

#### P6 — Agent Frameworks
**Purpose:** LangChain, LangGraph, CrewAI, LlamaIndex…

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 45 | LangChain Deep Dive | Core | LangChain, LCEL, chains |
| 46 | LangGraph — Stateful Agent Orchestration | Core | LangGraph, StateGraph |
| 47 | CrewAI — Multi-Agent Crews | Core | CrewAI, agents, tasks |
| 48 | AutoGen — Conversational Multi-Agent | Core | AutoGen, ConversableAgent |
| 49 | Flowise — Visual Agent Builder | Opt | Flowise, Docker, UI flows |
| 50 | AgentOps — Agent Monitoring & Observability | Core | AgentOps, LangSmith |
| 51 | Haystack — NLP Pipeline Framework | Opt | Haystack, pipelines |
| 52 | Semantic Kernel (Microsoft) | Opt | Semantic Kernel, C#/Python |
| 53 | LlamaIndex — Data Framework for LLMs | Core | LlamaIndex, VectorStore index |
| 54 | LLM Management: W&B, Arize AI | Opt | Weights & Biases, Arize |


**Module 45: LangChain Deep Dive** [Core] | Tools: `LangChain, LCEL, chains`
- Learn: OverviewModule 45 (P6) — LangChain Deep Dive. Tools focus: LangChain, LCEL, chains. Core path — prioritize in your sprint.LangChain unifies prompts, models, tools, retrievers, and LCEL Runnable chains. The goal is composable pipelines with clear I/O contracts — not every app needs the full framework surface.Deepen LCEL, structured output parsers, and retrieval chains; profile cold start and dependency weight before committing in latency-sensitive services.
- Practice: Build RunnableSequence: prompt | chat model | StrOutputParser.Add a retriever + stuff_documents chain on three local text files.Swap model provider via LangChain integration; keep the same interface.Write two unit tests with mocked LLM for deterministic CI.List which LangChain layers you would keep thin in production vs raw SDK.
- Code: `# Module 45 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 45, "topic": "LangChain Deep Dive", "status": "pr`

**Module 46: LangGraph — Stateful Agent Orchestration** [Core] | Tools: `LangGraph, StateGraph`
- Learn: OverviewModule 46 (P6) — LangGraph — Stateful Agent Orchestration. Tools focus: LangGraph, StateGraph. Core path — prioritize in your sprint.LangGraph adds persistence, interrupts, and cyclic graphs for agents. State reducers and checkpointing enable human-in-the-loop and crash recovery.
- Practice: Model a three-node graph with one conditional edge.Enable checkpointing to sqlite or memory; restart mid-run.Trigger an interrupt before a destructive tool; resume after approval.Draw your graph for stakeholders (boxes and arrows).Compare LangGraph complexity vs a plain Python loop for the same task.
- Code: `# Module 46 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 46, "topic": "LangGraph — Stateful Agent Orchestr`

**Module 47: CrewAI — Multi-Agent Crews** [Core] | Tools: `CrewAI, agents, tasks`
- Learn: OverviewModule 47 (P6) — CrewAI — Multi-Agent Crews. Tools focus: CrewAI, agents, tasks. Core path — prioritize in your sprint.CrewAI encodes crews, agents, and tasks with role descriptions. Good for demos; watch for hidden sequential coupling and unclear hand-offs.
- Practice: Define two agents with non-overlapping responsibilities.Create tasks with expected_output strings; run once end-to-end.Log each task completion artifact.Tighten prompts when output format drifts.Note licensing and dependency weight for deployment.
- Code: `# Module 47 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 47, "topic": "CrewAI — Multi-Agent Crews", "statu`

**Module 48: AutoGen — Conversational Multi-Agent** [Core] | Tools: `AutoGen, ConversableAgent`
- Learn: OverviewModule 48 (P6) — AutoGen — Conversational Multi-Agent. Tools focus: AutoGen, ConversableAgent. Core path — prioritize in your sprint.AutoGen uses conversable agents with code execution hooks. Learn group chat patterns and safety around code_runner.
- Practice: Spin up two-agent chat solving a coding puzzle.Constrain code execution to a sandbox if available.Stop the chat after N messages programmatically.Capture one failure where agents talk past each other; fix prompts.Summarize when AutoGen beats simpler orchestration.
- Code: `# Module 48 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 48, "topic": "AutoGen — Conversational Multi-Agen`

**Module 49: Flowise — Visual Agent Builder** [Optional] | Tools: `Flowise, Docker, UI flows`
- Learn: OverviewModule 49 (P6) — Flowise — Visual Agent Builder. Tools focus: Flowise, Docker, UI flows. Optional depth — revisit when you need this specialty.Flowise is a low-code node UI on top of chains. Useful for prototyping; export and version flows for staging promotions.
- Practice: Deploy Flowise via Docker locally.Build a flow: input → LLM → output parser.Export JSON; reload in a second environment.Identify secrets in nodes; move to env vars.List gaps vs code-first CI/CD for your org.
- Code: `# Module 49 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 49, "topic": "Flowise — Visual Agent Builder", "s`

**Module 50: AgentOps — Agent Monitoring & Observability** [Core] | Tools: `AgentOps, LangSmith`
- Learn: OverviewModule 50 (P6) — AgentOps — Agent Monitoring & Observability. Tools focus: AgentOps, LangSmith. Core path — prioritize in your sprint.AgentOps and LangSmith-class tools trace spans per model/tool call. You need consistent run IDs, cost attribution, and PII scrubbing.
- Practice: Instrument one agent with tracing SDK; view a waterfall.Tag traces with user_session anonymized.Add eval scores to a traced run manually.Configure retention policy appropriate for test data.Document who can access traces in your team RBAC model.
- Code: `# Module 50 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 50, "topic": "AgentOps — Agent Monitoring & Obser`

**Module 51: Haystack — NLP Pipeline Framework** [Optional] | Tools: `Haystack, pipelines`
- Learn: OverviewModule 51 (P6) — Haystack — NLP Pipeline Framework. Tools focus: Haystack, pipelines. Optional depth — revisit when you need this specialty.Haystack builds retrieval and QA pipelines with a document store abstraction. Compare to LangChain when teams already standardise on Haystack nodes.
- Practice: Run a minimal indexing + query pipeline from docs.Swap retriever component once (e.g. BM25 vs dense).Measure recall@k on five hand-made questions.Note deployment story for their pipeline runner.Decide Haystack vs LlamaIndex for one sample project.
- Code: `# Module 51 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 51, "topic": "Haystack — NLP Pipeline Framework",`

**Module 52: Semantic Kernel (Microsoft)** [Optional] | Tools: `Semantic Kernel, C#/Python`
- Learn: OverviewModule 52 (P6) — Semantic Kernel (Microsoft). Tools focus: Semantic Kernel, C#/Python. Optional depth — revisit when you need this specialty.Semantic Kernel is Microsoft’s SDK for planners, plugins, and memory across .NET/Python. Relevant when integrating with Azure AI services.
- Practice: Install SK for Python or .NET per your stack.Register one native plugin with two functions.Run a planner that selects functions automatically.Connect to an Azure OpenAI deployment if you have access; otherwise mock.Map SK concepts to LangChain terminology in a cheat sheet.
- Code: `# Module 52 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 52, "topic": "Semantic Kernel (Microsoft)", "stat`

**Module 53: LlamaIndex — Data Framework for LLMs** [Core] | Tools: `LlamaIndex, VectorStore index`
- Learn: OverviewModule 53 (P6) — LlamaIndex — Data Framework for LLMs. Tools focus: LlamaIndex, VectorStore index. Core path — prioritize in your sprint.LlamaIndex focuses on data connectors, indexes, and query engines over heterogeneous sources. Strong for RAG-centric products.
- Practice: Load ten docs; build VectorStoreIndex.Try query_engine vs chat_engine for the same question.Add metadata filters to a query.Persist index to disk; reload in a new process.Profile indexing time vs query latency.
- Code: `# Module 53 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 53, "topic": "LlamaIndex — Data Framework for LLM`

**Module 54: LLM Management: W&B, Arize AI** [Optional] | Tools: `Weights & Biases, Arize`
- Learn: OverviewModule 54 (P6) — LLM Management: W&B, Arize AI. Tools focus: Weights & Biases, Arize. Optional depth — revisit when you need this specialty.W&B tracks experiments; Arize/Phoenix targets LLM observability and embeddings drift. Pick tooling based on whether you optimise training or production inference.
- Practice: Log a small training or finetune run to W&B with hyperparameters.Create one dashboard chart you would show a client.Send a batch of prompts through Phoenix (or read tutorial); inspect traces.Define one drift metric for embeddings in production.Document cost of SaaS observability at your expected volume.
- Code: `# Module 54 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 54, "topic": "LLM Management: W&B, Arize AI", "st`

#### P7 — RAG & Knowledge
**Purpose:** Embeddings, chunking, vector DBs, hybrid search

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 55 | RAG Architecture & Pipeline Design | Core | LangChain, LlamaIndex |
| 56 | Embedding Models & Semantic Search | Core | OpenAI, Cohere, SBERT |
| 57 | Document Chunking Strategies | Core | LangChain splitters, custom logic |
| 58 | Custom Data Loaders & Document Ingestion | Core | LangChain loaders, Unstructured |
| 59 | Vector DBs: Pinecone, Weaviate, Chroma, FAISS | Core | Pinecone, Weaviate, Chroma |
| 60 | Query Refinement & Hybrid Search | Core | BM25, dense retrieval, rerankers |
| 61 | Knowledge Graphs for AI | Opt | Neo4j, NetworkX, graph RAG |


**Module 55: RAG Architecture & Pipeline Design** [Core] | Tools: `LangChain, LlamaIndex`
- Learn: OverviewModule 55 (P7) — RAG Architecture & Pipeline Design. Tools focus: LangChain, LlamaIndex. Core path — prioritize in your sprint.RAG combines retrieval with generation: chunk documents, embed, index, retrieve top-k, inject into prompt, generate with citations. Failure modes include wrong chunk boundaries and stale corpora.
- Practice: Diagram your target RAG pipeline with trust boundaries.List five ways retrieval can fail; pair each with a mitigation.Prototype ingest → chunk → embed → store with ten docs.Run five queries; log precision qualitatively.Define refresh policy when source docs change.
- Code: `pip install chromadb sentence-transformers
import chromadb
c = chromadb.Client(); col = c.create_collection("m55")
col.add(documents=["RAG retrieves context before generation."], ids=["a"])
print(col.`

**Module 56: Embedding Models & Semantic Search** [Core] | Tools: `OpenAI, Cohere, SBERT`
- Learn: OverviewModule 56 (P7) — Embedding Models & Semantic Search. Tools focus: OpenAI, Cohere, SBERT. Core path — prioritize in your sprint.Embedding model choice affects recall: multilingual, domain fit (legal, medical), and MRL dimensions. Re-embedding is expensive — version indexes.
- Practice: Compare two embedding models on the same ten-query set.Measure index build time and query latency.Test cross-language if relevant to your users.Store model name + dimension in index metadata.Plan A/B procedure before swapping embeddings live.
- Code: `# Module 56 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 56, "topic": "Embedding Models & Semantic Search"`

**Module 57: Document Chunking Strategies** [Core] | Tools: `LangChain splitters, custom logic`
- Learn: OverviewModule 57 (P7) — Document Chunking Strategies. Tools focus: LangChain splitters, custom logic. Core path — prioritize in your sprint.Chunking trades context coherence vs specificity: fixed size, sentence-aware, semantic splits, and late chunking techniques. Headers and metadata improve filtering.
- Practice: Chunk one long policy doc three ways; compare retrieval hits.Attach section titles as metadata on chunks.Tune overlap; observe redundancy in retrieved sets.Find a case where small chunks win vs large chunks.Document recommended chunk strategy per document type you serve.
- Code: `pip install chromadb sentence-transformers
import chromadb
c = chromadb.Client(); col = c.create_collection("m57")
col.add(documents=["RAG retrieves context before generation."], ids=["a"])
print(col.`

**Module 58: Custom Data Loaders & Document Ingestion** [Core] | Tools: `LangChain loaders, Unstructured`
- Learn: OverviewModule 58 (P7) — Custom Data Loaders & Document Ingestion. Tools focus: LangChain loaders, Unstructured. Core path — prioritize in your sprint.Loaders ingest PDFs, HTML, Notion exports, etc. Unstructured and vendor loaders differ on OCR quality and table handling — always validate samples.
- Practice: Ingest PDF + HTML + CSV samples; inspect extracted text quality.Handle encoding errors explicitly in pipeline code.Strip boilerplate footers/headers where they harm retrieval.Quarantine files that fail parse; alert operators.Estimate end-to-end ingest time per GB.
- Code: `# Module 58 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 58, "topic": "Custom Data Loaders & Document Inge`

**Module 59: Vector DBs: Pinecone, Weaviate, Chroma, FAISS** [Core] | Tools: `Pinecone, Weaviate, Chroma`
- Learn: OverviewModule 59 (P7) — Vector DBs: Pinecone, Weaviate, Chroma, FAISS. Tools focus: Pinecone, Weaviate, Chroma. Core path — prioritize in your sprint.Vector databases differ on hybrid search, filtering, multi-tenancy, and ops model (serverless vs self-host). FAISS is a library; Pinecone/Weaviate/Chroma are services or servers.
- Practice: Create a collection/index; upsert 1k vectors with metadata.Run metadata-filtered queries; verify performance.Try hybrid (BM25 + vector) if supported.Snapshot backup/restore procedure.Rough TCO: self-host vs managed for one workload.
- Code: `pip install chromadb sentence-transformers
import chromadb
c = chromadb.Client(); col = c.create_collection("m59")
col.add(documents=["RAG retrieves context before generation."], ids=["a"])
print(col.`

**Module 60: Query Refinement & Hybrid Search** [Core] | Tools: `BM25, dense retrieval, rerankers`
- Learn: OverviewModule 60 (P7) — Query Refinement & Hybrid Search. Tools focus: BM25, dense retrieval, rerankers. Core path — prioritize in your sprint.Query refinement rewrites user questions; hybrid search blends lexical and dense signals; rerankers reorder top-k for better precision at small k.
- Practice: Log raw user queries vs rewritten queries; compare results.Tune BM25 vs vector weights on five test questions.Add a cross-encoder reranker; measure latency impact.Define when to skip reranking for cost reasons.Document fallback if rewriter hallucinates constraints.
- Code: `# Module 60 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 60, "topic": "Query Refinement & Hybrid Search", `

**Module 61: Knowledge Graphs for AI** [Optional] | Tools: `Neo4j, NetworkX, graph RAG`
- Learn: OverviewModule 61 (P7) — Knowledge Graphs for AI. Tools focus: Neo4j, NetworkX, graph RAG. Optional depth — revisit when you need this specialty.Knowledge graphs model entities and relations; GraphRAG combines graph traversal with LLM summarisation. Higher setup cost, strong for multi-hop reasoning over structured domains.
- Practice: Model ten triples from a tiny domain (manual OK).Run one multi-hop question requiring two edges.Compare graph answer vs vector-only answer on same question.List maintenance cost when facts change frequently.Identify one client vertical where graphs pay off.
- Code: `# Module 61 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 61, "topic": "Knowledge Graphs for AI", "status":`

#### P8 — MCP Protocol
**Purpose:** Model Context Protocol depth

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 62 | MCP Architecture & Core Concepts | Core | MCP spec, Python |
| 63 | MCP Host, Client & Server Design | Core | mcp Python SDK, Claude Desktop |
| 64 | MCP Transport Layer & Communication | Core | stdio, HTTP SSE transport |
| 65 | Secure File Access & Sampling in MCP | Core | MCP server Python |
| 66 | MCP Resources, Prompts & Tools | Core | MCP spec, tool definitions |
| 67 | Building a Custom MCP Server (Python) | Core | mcp, fastapi, Python |
| 68 | MCP Integrations: S3, Stripe, Databases | Core | boto3, stripe, psycopg2 + MCP |
| 69 | Claude Desktop + MCP Full Setup | Core | Claude Desktop, mcp config |


**Module 62: MCP Architecture & Core Concepts** [Core] | Tools: `MCP spec, Python`
- Learn: OverviewModule 62 (P8) — MCP Architecture & Core Concepts. Tools focus: MCP spec, Python. Core path — prioritize in your sprint.MCP standardises how hosts expose tools, resources, and prompts to models. It complements (not replaces) your HTTP APIs — think structured capability contracts.
- Practice: Read the MCP intro + spec outline; list three primitives.Contrast MCP with ad-hoc REST tools you already built.Sketch a host → client → server diagram for your desktop assistant.List security questions (filesystem, network) MCP must answer.Pick one sample server from official repos to run read-only.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `

**Module 63: MCP Host, Client & Server Design** [Core] | Tools: `mcp Python SDK, Claude Desktop`
- Learn: OverviewModule 63 (P8) — MCP Host, Client & Server Design. Tools focus: mcp Python SDK, Claude Desktop. Core path — prioritize in your sprint.Hosts (Claude Desktop, IDEs) spawn MCP clients; servers implement capabilities over stdio or HTTP+SSE. Lifecycle includes capability negotiation and stderr logging.
- Practice: Configure one MCP server in Claude Desktop JSON config.Verify the host lists tools/resources after restart.Inspect logs for handshake errors; fix path or command once.Document how you’d pin server version for teams.Threat-model: what data leaves the machine?
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `

**Module 64: MCP Transport Layer & Communication** [Core] | Tools: `stdio, HTTP SSE transport`
- Learn: OverviewModule 64 (P8) — MCP Transport Layer & Communication. Tools focus: stdio, HTTP SSE transport. Core path — prioritize in your sprint.Transports carry JSON-RPC messages: stdio for local trust boundaries; HTTP+SSE for remote servers. Latency and auth differ materially.
- Practice: Run a stdio server; trace one request/response with debug logging.Read transport section of spec; note framing rules.Compare stdio vs remote transport for a corporate locked-down laptop.Add TLS and auth sketch for remote deployment.List failure modes: partial frames, timeouts, proxy interference.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `

**Module 65: Secure File Access & Sampling in MCP** [Core] | Tools: `MCP server Python`
- Learn: OverviewModule 65 (P8) — Secure File Access & Sampling in MCP. Tools focus: MCP server Python. Core path — prioritize in your sprint.Sampling and filesystem rules gate model access to local resources. Least privilege defaults beat “allow all” demos.
- Practice: Enable directory allowlist in a sample server config.Attempt disallowed path access; confirm denial.Review sampling callbacks — when human approval triggers.Document audit log fields you would ship.Red-team prompt injection via malicious file contents.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `

**Module 66: MCP Resources, Prompts & Tools** [Core] | Tools: `MCP spec, tool definitions`
- Learn: OverviewModule 66 (P8) — MCP Resources, Prompts & Tools. Tools focus: MCP spec, tool definitions. Core path — prioritize in your sprint.Resources expose data; prompts are templates; tools execute actions. Naming and descriptions feed model routing quality.
- Practice: Implement one resource URI pattern; fetch via client.Register a tool with rich description + JSON schema.Add a prompt template with variables; render from host.Test model’s ability to pick correct tool among three.Version schemas when breaking changes occur.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `

**Module 67: Building a Custom MCP Server (Python)** [Core] | Tools: `mcp, fastapi, Python`
- Learn: OverviewModule 67 (P8) — Building a Custom MCP Server (Python). Tools focus: mcp, fastapi, Python. Core path — prioritize in your sprint.Custom Python MCP servers often use FastMCP or official SDK. Package as CLI entrypoints; pin dependencies for reproducibility.
- Practice: Scaffold a server exposing two tools (read-only).Add unit tests mocking transport.Dockerfile optional: non-root user, read-only FS where possible.Publish README with install + config snippet.Peer review tool descriptions for ambiguity.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `

**Module 68: MCP Integrations: S3, Stripe, Databases** [Core] | Tools: `boto3, stripe, psycopg2 + MCP`
- Learn: OverviewModule 68 (P8) — MCP Integrations: S3, Stripe, Databases. Tools focus: boto3, stripe, psycopg2 + MCP. Core path — prioritize in your sprint.Integrations (S3, Stripe, Postgres) mean secrets, idempotency, and least privilege IAM. Never pass raw credentials through the model; server holds keys.
- Practice: Design IAM policy for S3 read-only prefix.Sketch Stripe flow with idempotency keys on writes.Use parameterized SQL only against Postgres tool.Log request metadata without card or PII payloads.Tabletop abuse: refund fraud prompt scenario.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `

**Module 69: Claude Desktop + MCP Full Setup** [Core] | Tools: `Claude Desktop, mcp config`
- Learn: OverviewModule 69 (P8) — Claude Desktop + MCP Full Setup. Tools focus: Claude Desktop, mcp config. Core path — prioritize in your sprint.Claude Desktop + MCP is the fastest way to feel the protocol. JSON config, absolute paths, and env vars are the usual friction points.
- Practice: Install Claude Desktop; locate MCP config file for your OS.Add one community server with narrow permissions.Restart; validate tools appear and run a harmless call.Snapshot working config (redacted) for teammates.Write troubleshooting FAQ from errors you actually saw.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

#### P9 — A2A Protocol
**Purpose:** Agent-to-agent communication

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 70 | A2A Protocol Architecture | Core | A2A spec, Python |
| 71 | Agent Cards & Agent Identity | Core | A2A agent cards, JSON |
| 72 | Task Delegation & Result Artifacts | Core | A2A tasks, Python SDK |
| 73 | Multi-Agent Distributed Execution | Core | A2A, LangGraph, Docker |
| 74 | A2A vs MCP: When to Use Which | Core | Architecture diagrams, code |


**Module 70: A2A Protocol Architecture** [Core] | Tools: `A2A spec, Python`
- Learn: OverviewModule 70 (P9) — A2A Protocol Architecture. Tools focus: A2A spec, Python. Core path — prioritize in your sprint.Google’s Agent2Agent (A2A) protocol focuses on discoverable agents, task messages, and artifacts — complementary to MCP’s tool/resource model. Study how remote agents authenticate and negotiate capabilities.
- Practice: Read A2A intro materials; contrast goals with MCP in one paragraph.List actors: client, remote agent, registry (if used).Sketch sequence diagram for a task submission and artifact return.Identify transport and auth questions unanswered by skimming docs.Note version skew risks between agent implementations.
- Code: `# Pseudocode: agent card JSON for discovery (follow latest A2A spec)
AGENT_CARD = {
  "name": "research-agent",
  "skills": [{"id": "web.search", "description": "Search and summarize"}],
  "endpoints"`

**Module 71: Agent Cards & Agent Identity** [Core] | Tools: `A2A agent cards, JSON`
- Learn: OverviewModule 71 (P9) — Agent Cards & Agent Identity. Tools focus: A2A agent cards, JSON. Core path — prioritize in your sprint.Agent cards advertise skills, endpoints, and trust metadata — similar in spirit to OpenAPI for services. Accurate cards reduce unsafe trial-and-error discovery.
- Practice: Draft a JSON agent card for a fake internal agent (no real URLs with secrets).Validate the card against examples from the spec repo.Peer review: can another teammate integrate without asking you?Add authentication section: mTLS vs bearer — justify choice.Version the card; document breaking change policy.
- Code: `# Pseudocode: agent card JSON for discovery (follow latest A2A spec)
AGENT_CARD = {
  "name": "research-agent",
  "skills": [{"id": "web.search", "description": "Search and summarize"}],
  "endpoints"`

**Module 72: Task Delegation & Result Artifacts** [Core] | Tools: `A2A tasks, Python SDK`
- Learn: OverviewModule 72 (P9) — Task Delegation & Result Artifacts. Tools focus: A2A tasks, Python SDK. Core path — prioritize in your sprint.Task delegation passes structured work items between agents; artifacts carry results (files, JSON, structured reports). Idempotency and correlation IDs matter across hops.
- Practice: Define task schema fields you would require (id, deadline, inputs).Simulate two-agent handoff with mocked HTTP; log correlation IDs.Handle partial failure: who retries, who compensates?Store artifacts in object storage vs inline JSON — decide per size.Write SLO for end-to-end task latency.
- Code: `# Module 72 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 72, "topic": "Task Delegation & Result Artifacts"`

**Module 73: Multi-Agent Distributed Execution** [Core] | Tools: `A2A, LangGraph, Docker`
- Learn: OverviewModule 73 (P9) — Multi-Agent Distributed Execution. Tools focus: A2A, LangGraph, Docker. Core path — prioritize in your sprint.Distributed execution spans containers or regions; combine A2A messages with orchestrators like LangGraph for local state while remote specialists handle subsets.
- Practice: Docker-compose two dummy agent services; send ping tasks.Introduce network partition; observe timeout behaviour.Centralise structured logs from both agents.Scale one agent replica; ensure task routing stays safe.Document blast radius if one agent is compromised.
- Code: `# Module 73 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 73, "topic": "Multi-Agent Distributed Execution",`

**Module 74: A2A vs MCP: When to Use Which** [Core] | Tools: `Architecture diagrams, code`
- Learn: OverviewModule 74 (P9) — A2A vs MCP: When to Use Which. Tools focus: Architecture diagrams, code. Core path — prioritize in your sprint.MCP excels at equipping a host with tools/resources; A2A excels at multi-agent tasking across trust boundaries. Many systems use both — draw boundaries deliberately.
- Practice: Draw a single architecture diagram placing MCP servers, your orchestrator, and A2A peers. Write a decision table: five criteria (latency, trust, UI surface, discoverability, state) × which protocol wins. Present a two-minute verbal summary to a peer and capture their questions as follow-ups.
- Code: `pip install mcp
# FastMCP minimal pattern (stdio server)
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("demo")
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return `

#### P10 — Unified AI Systems
**Purpose:** Orchestration, identity, observability, 9-layer stack

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 75 | Orchestrator Design & Patterns | Core | LangGraph, custom Python |
| 76 | Memory Layer Architecture (3-Tier) | Core | mem0, Redis, PostgreSQL |
| 77 | Identity & Agent Security Layer | Core | Teleport, cryptographic identity |
| 78 | Observability: Logs, Traces, Metrics | Core | LangSmith, OpenTelemetry |
| 79 | Guardrails & Output Safety Systems | Core | NeMo Guardrails, custom filters |
| 80 | The 9-Layer Agentic AI Infrastructure Stack | Core | Architecture reference |
| 81 | RBAC & Securing AI Agents (Cryptographic ID) | Core | RBAC, Teleport, policy engines |


**Module 75: Orchestrator Design & Patterns** [Core] | Tools: `LangGraph, custom Python`
- Learn: OverviewModule 75 (P10) — Orchestrator Design & Patterns. Tools focus: LangGraph, custom Python. Core path — prioritize in your sprint.Orchestrators coordinate subgraphs, retries, and human approvals. Patterns include supervisor, handoff, and parallel fan-out — each trades complexity vs observability.
- Practice: Implement supervisor routing three specialist stubs.Add pause/resume for human approval on high-risk branch.Export metrics: tasks started, succeeded, failed.Compare orchestrator code size vs prompts-only baseline.Document rollback story for partially applied side effects.
- Code: `# Module 75 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 75, "topic": "Orchestrator Design & Patterns", "s`

**Module 76: Memory Layer Architecture (3-Tier)** [Core] | Tools: `mem0, Redis, PostgreSQL`
- Learn: OverviewModule 76 (P10) — Memory Layer Architecture (3-Tier). Tools focus: mem0, Redis, PostgreSQL. Core path — prioritize in your sprint.Three-tier memory: hot session (Redis), warm structured (Postgres), cold semantic (vector). mem0 and similar libraries abstract policies but you still own PII and TTL law.
- Practice: Map one product’s memory to the three tiers with example keys.Define eviction when user deletes account (right to erasure).Prototype Redis TTL for session; Postgres row for preferences.Query vector tier with metadata filter by user_id.Estimate monthly cost at 10k MAU for your sketch.
- Code: `# Module 76 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 76, "topic": "Memory Layer Architecture (3-Tier)"`

**Module 77: Identity & Agent Security Layer** [Core] | Tools: `Teleport, cryptographic identity`
- Learn: OverviewModule 77 (P10) — Identity & Agent Security Layer. Tools focus: Teleport, cryptographic identity. Core path — prioritize in your sprint.Agent identity ties to machine IDs, SPIFFE/SPIRE concepts, or vendor features like Teleport Machine ID — goal is cryptographic proof of which workload spoke.
- Practice: Read high-level zero-trust agent identity blog/docs.List three attacks weak identity enables (spoof, replay).Sketch rotation for agent credentials (short-lived certs).Map identity to audit logs for tool calls.Tabletop: stolen agent credential response.
- Code: `# Module 77 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 77, "topic": "Identity & Agent Security Layer", "`

**Module 78: Observability: Logs, Traces, Metrics** [Core] | Tools: `LangSmith, OpenTelemetry`
- Learn: OverviewModule 78 (P10) — Observability: Logs, Traces, Metrics. Tools focus: LangSmith, OpenTelemetry. Core path — prioritize in your sprint.Observability triad: structured logs, traces, metrics. LLM apps add prompt/response spans, token counters, and evaluator scores — scrub PII before export.
- Practice: Emit JSON logs with trace_id on one multi-step run.View trace in LangSmith or Jaeger tutorial.Add three RED metrics definitions for your API.Test log sampling under load.Document retention aligned to compliance policy.
- Code: `# Module 78 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 78, "topic": "Observability: Logs, Traces, Metric`

**Module 79: Guardrails & Output Safety Systems** [Core] | Tools: `NeMo Guardrails, custom filters`
- Learn: OverviewModule 79 (P10) — Guardrails & Output Safety Systems. Tools focus: NeMo Guardrails, custom filters. Core path — prioritize in your sprint.Guardrails span input classifiers, output validators, topic allowlists, and NeMo-style policy YAML. Combine deterministic checks with model-based judges sparingly (cost).
- Practice: Implement regex + length guard on user input.Add LLM moderation or policy call on flagged subset only.Unit-test guard with adversarial prompts (synthetic).Measure latency impact of each layer.Define escalation path when guards disagree.
- Code: `# Module 79 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 79, "topic": "Guardrails & Output Safety Systems"`

**Module 80: The 9-Layer Agentic AI Infrastructure Stack** [Core] | Tools: `Architecture reference`
- Learn: OverviewModule 80 (P10) — The 9-Layer Agentic AI Infrastructure Stack. Tools focus: Architecture reference. Core path — prioritize in your sprint.The nine-layer stack is a reference lens: models, tools, memory, identity, observability, orchestration, data, security, UX — not a literal product diagram. Use it to gap-analyze proposals.
- Practice: Redraw the nine layers for one client scenario (e.g. internal copilot vs external support bot). Highlight three layers that are immature in their design and one concrete improvement per layer. No install steps — completion is the annotated diagram plus a short narrative in your portfolio notes.
- Code: `# Module 80 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 80, "topic": "The 9-Layer Agentic AI Infrastructu`

**Module 81: RBAC & Securing AI Agents (Cryptographic ID)** [Core] | Tools: `RBAC, Teleport, policy engines`
- Learn: OverviewModule 81 (P10) — RBAC & Securing AI Agents (Cryptographic ID). Tools focus: RBAC, Teleport, policy engines. Core path — prioritize in your sprint.RBAC for agents binds roles to tool permissions and data scopes. Cryptographic identity ties policy enforcement to workloads, not just API keys in env vars.
- Practice: Write RBAC matrix: roles × tools × data classes.Map Auth0/Clerk-style JWT claims to agent permissions.Test deny path when role lacks a tool.Integrate short-lived identity document for agent pod.Review OWASP authorization cheat sheet; note two gaps you will close.
- Code: `# Module 81 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 81, "topic": "RBAC & Securing AI Agents (Cryptogr`

#### P11 — Fine-Tuning
**Purpose:** LoRA, PEFT, data prep, evaluation

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 82 | Fine-Tuning Fundamentals & When to Use It | Core | Hugging Face, OpenAI fine-tune |
| 83 | LoRA & QLoRA (Efficient Fine-Tuning) | Core | PEFT, bitsandbytes, LoRA |
| 84 | PEFT: Parameter Efficient Fine-Tuning | Core | PEFT library, HF Transformers |
| 85 | Training Data Preparation & Curation | Core | datasets, Argilla, Label Studio |
| 86 | Domain Adaptation & Model Evaluation | Opt | ROUGE, BERTScore, Eleuther LM Eval |


**Module 82: Fine-Tuning Fundamentals & When to Use It** [Core] | Tools: `Hugging Face, OpenAI fine-tune`
- Learn: OverviewModule 82 (P11) — Fine-Tuning Fundamentals & When to Use It. Tools focus: Hugging Face, OpenAI fine-tune. Core path — prioritize in your sprint.Fine-tuning adapts a pretrained model to style, format, or domain with smaller curated datasets. Prefer prompting + RAG first; tune when you need consistent behaviour cheaper at inference than giant prompts.
- Practice: List go/no-go criteria: when tuning beats prompt/RAG for your use case.Sketch data card: source, license, PII scrubbing method.Run a toy HF Trainer or API fine-tune on public data only.Evaluate before/after on ten held-out prompts with a rubric.Document rollback: how to revert to base model serving.
- Code: `# Module 82 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 82, "topic": "Fine-Tuning Fundamentals & When to `

**Module 83: LoRA & QLoRA (Efficient Fine-Tuning)** [Core] | Tools: `PEFT, bitsandbytes, LoRA`
- Learn: OverviewModule 83 (P11) — LoRA & QLoRA (Efficient Fine-Tuning). Tools focus: PEFT, bitsandbytes, LoRA. Core path — prioritize in your sprint.LoRA/QLoRA train low-rank adapters while freezing most weights — feasible on consumer GPUs with bitsandbytes quant. Watch for catastrophic forgetting on edge tasks.
- Practice: Read PEFT LoRA guide; note rank and alpha defaults.Configure one QLoRA training job on a tiny dataset.Compare adapter-only checkpoint size vs full weights.Merge adapters vs load at runtime — decide for deployment.Run qualitative eval on domain jargon the base model mishandled.
- Code: `# Module 83 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 83, "topic": "LoRA & QLoRA (Efficient Fine-Tuning`

**Module 84: PEFT: Parameter Efficient Fine-Tuning** [Core] | Tools: `PEFT library, HF Transformers`
- Learn: OverviewModule 84 (P11) — PEFT: Parameter Efficient Fine-Tuning. Tools focus: PEFT library, HF Transformers. Core path — prioritize in your sprint.PEFT umbrella covers LoRA, prefix tuning, adapters. Pick method based on framework support and serving constraints (some hosts only merge LoRA).
- Practice: Tabulate three PEFT methods with memory and inference trade-offs.Implement one non-LoRA PEFt method tutorial if hardware allows.Export config YAML used for reproducibility.Version training code + data hash in experiment log.Identify failure: overfitting on tiny data — show metric.
- Code: `# Module 84 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 84, "topic": "PEFT: Parameter Efficient Fine-Tuni`

**Module 85: Training Data Preparation & Curation** [Core] | Tools: `datasets, Argilla, Label Studio`
- Learn: OverviewModule 85 (P11) — Training Data Preparation & Curation. Tools focus: datasets, Argilla, Label Studio. Core path — prioritize in your sprint.Data curation beats raw scale: dedupe, toxicity filters, format normalization, and human review for high-stakes labels. Argilla/Label Studio structure feedback loops.
- Practice: Ingest 100 rows; profile duplicates and label imbalance.Define annotation guidelines for one task; run 20 double-labels.Compute inter-annotator agreement roughly.Export JSONL for training; scrub PII with regex + manual spot check.Write data versioning plan (DVC or simple manifest).
- Code: `# Module 85 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 85, "topic": "Training Data Preparation & Curatio`

**Module 86: Domain Adaptation & Model Evaluation** [Optional] | Tools: `ROUGE, BERTScore, Eleuther LM Eval`
- Learn: OverviewModule 86 (P11) — Domain Adaptation & Model Evaluation. Tools focus: ROUGE, BERTScore, Eleuther LM Eval. Optional depth — revisit when you need this specialty.Domain adaptation evaluation uses task metrics (ROUGE, BERTScore) plus human eval for tone. lm-evaluation-harness standardises many benchmarks — know limits of automatic scores.
- Practice: Pick one optional evaluation harness tutorial; run on a public task; log scores and cost. Write a critique: where automatic metrics misalign with business quality. If GPU access is limited, document the exact commands you would run in cloud and stop after planning — still mark complete with written eval plan.
- Code: `# Module 86 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 86, "topic": "Domain Adaptation & Model Evaluatio`

#### P12 — Vibe Coding
**Purpose:** AI-native development tools

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 87 | Vibe Coding Philosophy & Toolchain | Core | Claude Code, Cursor, GitHub Copilot |
| 88 | Claude Code: Setup, CLAUDE.md & Workflow | Core | Claude Code CLI, CLAUDE.md |
| 89 | Claude Code: Skills, Hooks & Memory System | Core | Claude Code skills, hooks |
| 90 | Claude Code: 4-Layer Architecture | Core | CLAUDE.md, Skills, Hooks, Agents |
| 91 | Claude Code: Project Structure (Agentic Setup) | Core | agentic project scaffold |
| 92 | Cursor AI — AI-Native IDE | Core | Cursor, Cursor rules |
| 93 | GitHub Copilot for AI Development | Core | Copilot, VS Code, CLI |
| 94 | Lovable & Gamma (No-Code AI Builders) | Opt | Lovable, Gamma |


**Module 87: Vibe Coding Philosophy & Toolchain** [Core] | Tools: `Claude Code, Cursor, GitHub Copilot`
- Learn: OverviewModule 87 (P12) — Vibe Coding Philosophy & Toolchain. Tools focus: Claude Code, Cursor, GitHub Copilot. Core path — prioritize in your sprint.Vibe coding means steering AI assistants with intent while you review diffs, tests, and security. The toolchain spans Claude Code, Cursor, Copilot — each differs in rules, memory, and IDE integration.
- Practice: List your non-negotiables before accepting AI-generated patches (tests, types, secrets).Try one feature end-to-end with heavy AI assistance; capture diff review notes.Measure time saved vs bugs introduced (honest retro).Define branch protection + CI checks that AI cannot bypass.Teach a teammate your prompt patterns for refactors.
- Code: `# Module 87 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 87, "topic": "Vibe Coding Philosophy & Toolchain"`

**Module 88: Claude Code: Setup, CLAUDE.md & Workflow** [Core] | Tools: `Claude Code CLI, CLAUDE.md`
- Learn: OverviewModule 88 (P12) — Claude Code: Setup, CLAUDE.md & Workflow. Tools focus: Claude Code CLI, CLAUDE.md. Core path — prioritize in your sprint.Claude Code CLI uses project context files (CLAUDE.md), skills, and hooks to standardise behaviour across sessions — treat it like onboarding docs for a junior dev.
- Practice: Install Claude Code per vendor docs; create CLAUDE.md with stack + commands.Add repo map: directories, owners, test entrypoints.Run one guided task: fix lint + add test using the tool.Document which files the tool may edit vs forbid.Snapshot lessons learned in team wiki (redacted).
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

**Module 89: Claude Code: Skills, Hooks & Memory System** [Core] | Tools: `Claude Code skills, hooks`
- Learn: OverviewModule 89 (P12) — Claude Code: Skills, Hooks & Memory System. Tools focus: Claude Code skills, hooks. Core path — prioritize in your sprint.Hooks intercept tool lifecycle events; skills package repeatable workflows. Together they reduce drift between developers using the same repo.
- Practice: Configure one hook (pre-tool or post-edit) with safe logging only.Author one skill file for a repetitive task (e.g. migration checklist).Share skill with peer; gather usability feedback.Version skills in git; review changes via PR.List hook failure modes and fallbacks if hook crashes.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

**Module 90: Claude Code: 4-Layer Architecture** [Core] | Tools: `CLAUDE.md, Skills, Hooks, Agents`
- Learn: OverviewModule 90 (P12) — Claude Code: 4-Layer Architecture. Tools focus: CLAUDE.md, Skills, Hooks, Agents. Core path — prioritize in your sprint.Four-layer mental model: project memory (CLAUDE.md), skills, hooks, subagents/specialists. Align layers so instructions do not contradict.
- Practice: Produce a single-page diagram of the four layers for your main repo. Highlight one contradiction you resolved between CLAUDE.md and a skill, and how you fixed it. Completion = diagram + short write-up; no extra install beyond your existing Claude Code setup.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

**Module 91: Claude Code: Project Structure (Agentic Setup)** [Core] | Tools: `agentic project scaffold`
- Learn: OverviewModule 91 (P12) — Claude Code: Project Structure (Agentic Setup). Tools focus: agentic project scaffold. Core path — prioritize in your sprint.Agentic project structure separates prompts, tools, evals, and runtime config. Scaffold early so AI assistants do not sprawl files randomly.
- Practice: Create directories: prompts/, tools/, eval/, config/.Add README explaining boundaries.Move one messy script into proper module + tests.Add pre-commit for format + lint.Have another human navigate the tree without help — time them.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

**Module 92: Cursor AI — AI-Native IDE** [Core] | Tools: `Cursor, Cursor rules`
- Learn: OverviewModule 92 (P12) — Cursor AI — AI-Native IDE. Tools focus: Cursor, Cursor rules. Core path — prioritize in your sprint.Cursor is an AI-native IDE: rules files, codebase indexing, and inline edits. Learn to scope context windows deliberately to reduce wrong-file edits.
- Practice: Author .cursor/rules or project rules per docs.Use @file and @folder references intentionally in prompts.Disable overly broad context for a sensitive subfolder.Run tests after each AI edit batch; note flaky failures.Compare Cursor workflow vs plain VS Code + Copilot for one bugfix.
- Code: `# Module 92 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 92, "topic": "Cursor AI — AI-Native IDE", "status`

**Module 93: GitHub Copilot for AI Development** [Core] | Tools: `Copilot, VS Code, CLI`
- Learn: OverviewModule 93 (P12) — GitHub Copilot for AI Development. Tools focus: Copilot, VS Code, CLI. Core path — prioritize in your sprint.GitHub Copilot spans editor, CLI, and PR suggestions. Policies in org settings govern which models and repos participate — align with compliance.
- Practice: Enable Copilot for a sandbox repo; complete three small tasks.Try Copilot CLI for a refactor; review diff carefully.Check org policy on code suggestions for internal repos.Log one unsafe suggestion you rejected and why.Pair with tests-first workflow; measure coverage delta.
- Code: `# Module 93 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 93, "topic": "GitHub Copilot for AI Development",`

**Module 94: Lovable & Gamma (No-Code AI Builders)** [Optional] | Tools: `Lovable, Gamma`
- Learn: OverviewModule 94 (P12) — Lovable & Gamma (No-Code AI Builders). Tools focus: Lovable, Gamma. Optional depth — revisit when you need this specialty.Lovable and Gamma accelerate UI and slide generation from prompts. Outputs still need brand, accessibility, and content review before client-facing use.
- Practice: Generate one landing page draft; check a11y basics (contrast, headings).Export or hand off to code repo; diff against handcrafted baseline.List three limitations (layout control, data binding, SEO).Run content fact-check on generated copy.Decide when you would ban no-code for regulated clients.
- Code: `# Module 94 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 94, "topic": "Lovable & Gamma (No-Code AI Builder`

#### P13 — Automation
**Purpose:** n8n, Make, Zapier, DAGs, guardrails

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 95 | n8n — Open Source Workflow Automation | Core | n8n, Docker, webhooks |
| 96 | Make.com (Integromat) — Visual Automation | Core | Make.com, modules, scenarios |
| 97 | Zapier — Enterprise Integration Automation | Core | Zapier, Zaps, triggers |
| 98 | DAG Management & Event-Based Triggers | Core | LangGraph, Airflow, n8n |
| 99 | Guardrails & Conditional Workflow Logic | Core | LangGraph conditionals, n8n |


**Module 95: n8n — Open Source Workflow Automation** [Core] | Tools: `n8n, Docker, webhooks`
- Learn: OverviewModule 95 (P13) — n8n — Open Source Workflow Automation. Tools focus: n8n, Docker, webhooks. Core path — prioritize in your sprint.n8n is fair-code workflow automation with self-host option. Nodes connect triggers, HTTP, databases, and AI steps — version flows as JSON in git when possible.
- Practice: Run n8n via Docker; create admin user.Build webhook → function → HTTP request flow.Add error workflow or retry policy.Export workflow JSON to git.Secrets: use credential store; never hardcode in nodes.
- Code: `docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
# Open http://localhost:5678 — build a webhook → HTTP Request → LLM flow`

**Module 96: Make.com (Integromat) — Visual Automation** [Core] | Tools: `Make.com, modules, scenarios`
- Learn: OverviewModule 96 (P13) — Make.com (Integromat) — Visual Automation. Tools focus: Make.com, modules, scenarios. Core path — prioritize in your sprint.Make.com (Integromat) uses scenarios, modules, and data stores — great for SaaS glue. Understand operation billing and rate limits per plan.
- Practice: Create scenario with two modules + router.Map data mapping between modules explicitly.Test error path with invalid payload.Estimate monthly operations for expected volume.Document when you would migrate scenario to code (n8n/FastAPI).
- Code: `# Module 96 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 96, "topic": "Make.com (Integromat) — Visual Auto`

**Module 97: Zapier — Enterprise Integration Automation** [Core] | Tools: `Zapier, Zaps, triggers`
- Learn: OverviewModule 97 (P13) — Zapier — Enterprise Integration Automation. Tools focus: Zapier, Zaps, triggers. Core path — prioritize in your sprint.Zapier targets business users with Zaps and multi-step paths. Enterprise features include SAML and admin controls — evaluate before automating sensitive data.
- Practice: Build a Zap with filter + formatter steps.Test delay and throttle behaviour.Review audit logs if available on your tier.Compare Zapier vs Make pricing for same workload sketch.List data residency questions for EU clients.
- Code: `# Module 97 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 97, "topic": "Zapier — Enterprise Integration Aut`

**Module 98: DAG Management & Event-Based Triggers** [Core] | Tools: `LangGraph, Airflow, n8n`
- Learn: OverviewModule 98 (P13) — DAG Management & Event-Based Triggers. Tools focus: LangGraph, Airflow, n8n. Core path — prioritize in your sprint.DAGs express dependencies; event triggers react to webhooks, queues, or schedules. Mixing LangGraph with external schedulers is common in hybrid systems.
- Practice: Draw DAG for nightly ETL + morning LLM summary job.Implement one cron + one event trigger in n8n or Airflow tutorial.Define idempotency keys for downstream writes.Handle backlog: what if LLM step slows down?Alerting: PagerDuty/webhook on DAG failure.
- Code: `# Module 98 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 98, "topic": "DAG Management & Event-Based Trigge`

**Module 99: Guardrails & Conditional Workflow Logic** [Core] | Tools: `LangGraph conditionals, n8n`
- Learn: OverviewModule 99 (P13) — Guardrails & Conditional Workflow Logic. Tools focus: LangGraph conditionals, n8n. Core path — prioritize in your sprint.Conditional logic and guardrails in automation prevent runaway AI calls — caps on tokens, approvals on writes, and circuit breakers on error rates.
- Practice: Add branch on HTTP status in a flow.Cap OpenAI node max tokens and concurrency.Insert human approval email/Slack before payment action (mock).Simulate 5xx storm; verify breaker stops spam.Document rollback for partially executed scenario.
- Code: `# Module 99 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 99, "topic": "Guardrails & Conditional Workflow L`

#### P14 — Production AI
**Purpose:** APIs, Docker, hosting, serverless

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 100 | FastAPI — Production API for AI Systems | Core | FastAPI, Pydantic, uvicorn |
| 101 | Streamlit & Gradio — AI UIs | Core | Streamlit, Gradio |
| 102 | Serverless Functions for AI | Core | AWS Lambda, Vercel Edge, Modal |
| 103 | Docker for AI Systems | Core | Docker, docker-compose |
| 104 | Kubernetes for AI Scale | Opt | Kubernetes, Helm, k8s |
| 105 | Vector DB Hosting & Management | Core | Pinecone cloud, Weaviate cloud |
| 106 | Agent Hosting: Replit, Modal, Fly.io | Core | Replit, Modal, Fly.io |


**Module 100: FastAPI — Production API for AI Systems** [Core] | Tools: `FastAPI, Pydantic, uvicorn`
- Learn: OverviewModule 100 (P14) — FastAPI — Production API for AI Systems. Tools focus: FastAPI, Pydantic, uvicorn. Core path — prioritize in your sprint.FastAPI gives typed routes, OpenAPI docs, and async I/O — a common shell for LLM backends. Pair with Pydantic models for request/response contracts.
- Practice: Scaffold app with /health and /v1/chat proxy route (mock LLM).Add dependency-injected settings from env.Write pytest with TestClient covering 200 + validation error.Add request ID middleware; log structured JSON.Dockerfile non-root; pin base image digest.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

**Module 101: Streamlit & Gradio — AI UIs** [Core] | Tools: `Streamlit, Gradio`
- Learn: OverviewModule 101 (P14) — Streamlit & Gradio — AI UIs. Tools focus: Streamlit, Gradio. Core path — prioritize in your sprint.Streamlit and Gradio ship demos fast; they differ in layout models and auth story. Neither replaces hardened multi-tenant auth without extra work.
- Practice: Build Streamlit chat UI calling your FastAPI mock.Add Gradio variant with same backend.Compare session state handling.Host locally with HTTPS tunnel (e.g. cloudflared) for demo only.List production gaps: auth, rate limits, logging.
- Code: `# Module 101 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 101, "topic": "Streamlit & Gradio — AI UIs", "st`

**Module 102: Serverless Functions for AI** [Core] | Tools: `AWS Lambda, Vercel Edge, Modal`
- Learn: OverviewModule 102 (P14) — Serverless Functions for AI. Tools focus: AWS Lambda, Vercel Edge, Modal. Core path — prioritize in your sprint.Serverless (Lambda, Vercel, Modal) scales to zero but has cold starts and payload limits. Modal suits GPU jobs; Lambda suits thin orchestration.
- Practice: Deploy hello function to one serverless platform.Measure cold start p95 with simple load test.Set env vars + secrets via platform mechanism.Define max payload and timeout appropriate for LLM proxy.Cost estimate for 1M invocations/month at your memory setting.
- Code: `# Module 102 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 102, "topic": "Serverless Functions for AI", "st`

**Module 103: Docker for AI Systems** [Core] | Tools: `Docker, docker-compose`
- Learn: OverviewModule 103 (P14) — Docker for AI Systems. Tools focus: Docker, docker-compose. Core path — prioritize in your sprint.Docker packages dependencies reproducibly; multi-stage builds shrink images. For AI images, watch CUDA base sizes and layer caching for model weights.
- Practice: Write Dockerfile for FastAPI app; run locally.Add docker-compose with depends_on + healthcheck.Use .dockerignore to skip models and secrets.Scan image with trivy or docker scout; patch criticals.Document promote path: dev → staging tags.
- Code: `docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
# Open http://localhost:5678 — build a webhook → HTTP Request → LLM flow`

**Module 104: Kubernetes for AI Scale** [Optional] | Tools: `Kubernetes, Helm, k8s`
- Learn: OverviewModule 104 (P14) — Kubernetes for AI Scale. Tools focus: Kubernetes, Helm, k8s. Optional depth — revisit when you need this specialty.Kubernetes schedules GPU workloads, autoscaling, and config maps — operational overhead is real. Helm charts help but require cluster expertise.
- Practice: Read pod/resource requests vs limits for GPU pods.Sketch Deployment + Service + Ingress for your API.Plan config via ConfigMap vs Secret for keys.Understand HPA signals beyond CPU (custom metrics).Write when you would stay on VMs vs k8s for a client MVP.
- Code: `# Module 104 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 104, "topic": "Kubernetes for AI Scale", "status`

**Module 105: Vector DB Hosting & Management** [Core] | Tools: `Pinecone cloud, Weaviate cloud`
- Learn: OverviewModule 105 (P14) — Vector DB Hosting & Management. Tools focus: Pinecone cloud, Weaviate cloud. Core path — prioritize in your sprint.Managed vector hosting offloads replicas, backups, and upgrades. Still define namespaces/tenants and backup RPO for customer indexes.
- Practice: Create serverless index; upsert test vectors.Test failover/read replica behaviour from docs.Estimate monthly $ for 1M vectors at your dimension.Define restore drill quarterly.Map IAM roles for ingest vs query workloads.
- Code: `pip install chromadb sentence-transformers
import chromadb
c = chromadb.Client(); col = c.create_collection("m105")
col.add(documents=["RAG retrieves context before generation."], ids=["a"])
print(col`

**Module 106: Agent Hosting: Replit, Modal, Fly.io** [Core] | Tools: `Replit, Modal, Fly.io`
- Learn: OverviewModule 106 (P14) — Agent Hosting: Replit, Modal, Fly.io. Tools focus: Replit, Modal, Fly.io. Core path — prioritize in your sprint.Agent hosting platforms (Replit, Modal, Fly.io) differ in GPU access, sleep policies, and outbound network. Pick based on workload wake latency and compliance.
- Practice: Deploy stub agent HTTP service to one platform.Measure cold start and keep-warm trade-offs.Configure secrets and environment promotion.Test outbound allowlist if required by security.Document egress data paths for privacy review.
- Code: `# Module 106 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 106, "topic": "Agent Hosting: Replit, Modal, Fly`

#### P15 — Monitoring & Eval
**Purpose:** RAGAS, LangSmith, OpenTelemetry

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 107 | Agent Evaluation Metrics & Benchmarks | Core | RAGAS, TruLens, custom evals |
| 108 | Human-in-the-Loop Feedback Systems | Core | LangSmith, Argilla |
| 109 | LangSmith — Tracing & Debugging LLM Apps | Core | LangSmith, LangChain |
| 110 | OpenTelemetry for AI Observability | Core | OpenTelemetry, Jaeger |
| 111 | Auto-Evaluation Loops | Core | LLM-as-judge, custom eval chains |
| 112 | Prometheus & Grafana for AI Metrics | Opt | Prometheus, Grafana dashboards |


**Module 107: Agent Evaluation Metrics & Benchmarks** [Core] | Tools: `RAGAS, TruLens, custom evals`
- Learn: OverviewModule 107 (P15) — Agent Evaluation Metrics & Benchmarks. Tools focus: RAGAS, TruLens, custom evals. Core path — prioritize in your sprint.RAGAS and similar frameworks score faithfulness, answer relevance, and context precision — useful for regression suites, not perfect truth.
- Practice: Install RAGAS; run quickstart on synthetic QA pairs.Log metric distributions across five prompts.Identify one metric that misfires; explain why.Wire metrics export to CSV or W&B.Define pass threshold for CI gating.
- Code: `# Module 107 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 107, "topic": "Agent Evaluation Metrics & Benchm`

**Module 108: Human-in-the-Loop Feedback Systems** [Core] | Tools: `LangSmith, Argilla`
- Learn: OverviewModule 108 (P15) — Human-in-the-Loop Feedback Systems. Tools focus: LangSmith, Argilla. Core path — prioritize in your sprint.Human-in-the-loop feedback (Argilla, LangSmith datasets) closes the gap between automatic scores and user satisfaction — design lightweight rubrics.
- Practice: Create 20-row eval set with binary thumbs up/down reason codes.Run blind comparison two model versions; aggregate preference.Ensure annotators see identical prompts (counter bias).Export labeled set for fine-tune or prompt iteration.Document inter-rater drift over time.
- Code: `# Module 108 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 108, "topic": "Human-in-the-Loop Feedback System`

**Module 109: LangSmith — Tracing & Debugging LLM Apps** [Core] | Tools: `LangSmith, LangChain`
- Learn: OverviewModule 109 (P15) — LangSmith — Tracing & Debugging LLM Apps. Tools focus: LangSmith, LangChain. Core path — prioritize in your sprint.LangSmith traces show LLM spans, tool calls, and retries — essential for debugging non-deterministic failures in staging.
- Practice: Enable tracing on one chain; reproduce a bug twice.Filter traces by tags and latency.Share trace link internally with redaction checklist.Add evaluators on a dataset run.Set retention and access controls per environment.
- Code: `# Module 109 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 109, "topic": "LangSmith — Tracing & Debugging L`

**Module 110: OpenTelemetry for AI Observability** [Core] | Tools: `OpenTelemetry, Jaeger`
- Learn: OverviewModule 110 (P15) — OpenTelemetry for AI Observability. Tools focus: OpenTelemetry, Jaeger. Core path — prioritize in your sprint.OpenTelemetry standardises traces/metrics/logs export to Jaeger, Grafana, etc. Auto-instrument HTTP clients/servers first.
- Practice: Add OTel SDK to FastAPI service.Export traces to local Jaeger or Grafana stack.Create span around LLM HTTP call with attributes (model, not content).Add metric counter for tool errors.Verify sampling rate under load test.
- Code: `# Module 110 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 110, "topic": "OpenTelemetry for AI Observabilit`

**Module 111: Auto-Evaluation Loops** [Core] | Tools: `LLM-as-judge, custom eval chains`
- Learn: OverviewModule 111 (P15) — Auto-Evaluation Loops. Tools focus: LLM-as-judge, custom eval chains. Core path — prioritize in your sprint.Auto-evaluation loops run nightly evals, open PRs when regressions detected, or gate deploys — beware feedback loops where the judge model drifts.
- Practice: Design nightly job: sample prod queries → judge → dashboard.Choose judge model separate from production model.Add human spot-check percentage.Define rollback trigger thresholds.Document ethical limits on using user data in eval.
- Code: `# Module 111 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 111, "topic": "Auto-Evaluation Loops", "status":`

**Module 112: Prometheus & Grafana for AI Metrics** [Optional] | Tools: `Prometheus, Grafana dashboards`
- Learn: OverviewModule 112 (P15) — Prometheus & Grafana for AI Metrics. Tools focus: Prometheus, Grafana dashboards. Optional depth — revisit when you need this specialty.Prometheus scrapes metrics; Grafana dashboards visualize SLOs. LLM-specific panels might track tokens, latency, error codes, and judge scores.
- Practice: Stand up or follow a tutorial stack with Prometheus + Grafana; import a starter dashboard; add one custom panel for LLM proxy latency p95. If you cannot run Docker locally, complete the module with a written dashboard spec and PromQL queries you would use.
- Code: `# Module 112 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 112, "topic": "Prometheus & Grafana for AI Metri`

#### P16 — Security & Governance
**Purpose:** Injection, secrets, RBAC, privacy

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 113 | Prompt Injection Detection & Protection | Core | Rebuff, custom guards, NeMo |
| 114 | API Key Management & Secret Rotation | Core | Vault, AWS Secrets Manager |
| 115 | User Authentication & RBAC | Core | Auth0, Clerk, FastAPI security |
| 116 | Output Filtering & Content Safety | Core | OpenAI moderation, custom filters |
| 117 | Red Team Testing for AI Systems | Core | PyRIT, garak, manual red-teaming |
| 118 | Data Privacy, AI Alignment & Compliance | Core | GDPR frameworks, AI Act basics |


**Module 113: Prompt Injection Detection & Protection** [Core] | Tools: `Rebuff, custom guards, NeMo`
- Learn: OverviewModule 113 (P16) — Prompt Injection Detection & Protection. Tools focus: Rebuff, custom guards, NeMo. Core path — prioritize in your sprint.Prompt injection attempts to override system instructions via untrusted content — defenses include privilege separation, tool allowlists, and output policies.
- Practice: Reproduce a benign injection in a sandbox prompt.Move secrets and policies to system messages the user cannot edit.Add delimiter markers for untrusted document sections.Test Rebuff/regex guard if applicable.Write incident runbook if injection leads to data leak.
- Code: `# Module 113 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 113, "topic": "Prompt Injection Detection & Prot`

**Module 114: API Key Management & Secret Rotation** [Core] | Tools: `Vault, AWS Secrets Manager`
- Learn: OverviewModule 114 (P16) — API Key Management & Secret Rotation. Tools focus: Vault, AWS Secrets Manager. Core path — prioritize in your sprint.API keys belong in vaults (Vault, cloud secret managers) with rotation, audit, and least privilege paths. Never log secret values.
- Practice: Store one secret in Vault or cloud SM; read from app at boot.Rotate key; verify zero-downtime reload strategy.grep/scan repo for accidental keys (gitleaks).Define break-glass access procedure.Document quarterly rotation calendar.
- Code: `import os
# Use env vars — never commit keys
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
r = client.chat.completions.create(
    model="gpt-4o-mini",
    messag`

**Module 115: User Authentication & RBAC** [Core] | Tools: `Auth0, Clerk, FastAPI security`
- Learn: OverviewModule 115 (P16) — User Authentication & RBAC. Tools focus: Auth0, Clerk, FastAPI security. Core path — prioritize in your sprint.User authentication (Auth0, Clerk) pairs with FastAPI OAuth2/JWT validation. Map identities to tenant IDs before RAG retrieval.
- Practice: Integrate OIDC login on a demo app.Enforce RBAC on one API route.Test token expiry and refresh behaviour.Log auth failures without leaking emails in public logs.Threat-model stolen refresh token.
- Code: `# Module 115 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 115, "topic": "User Authentication & RBAC", "sta`

**Module 116: Output Filtering & Content Safety** [Core] | Tools: `OpenAI moderation, custom filters`
- Learn: OverviewModule 116 (P16) — Output Filtering & Content Safety. Tools focus: OpenAI moderation, custom filters. Core path — prioritize in your sprint.Output filtering blocks PII leaks, toxic content, or policy violations — combine provider moderation APIs with local regex for formats.
- Practice: Call moderation API on five synthetic outputs.Add local redact for credit-card-like patterns.Define fallback message when content blocked.Measure added latency.Human review queue for borderline cases.
- Code: `# Module 116 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 116, "topic": "Output Filtering & Content Safety`

**Module 117: Red Team Testing for AI Systems** [Core] | Tools: `PyRIT, garak, manual red-teaming`
- Learn: OverviewModule 117 (P16) — Red Team Testing for AI Systems. Tools focus: PyRIT, garak, manual red-teaming. Core path — prioritize in your sprint.Red teaming uses tools like PyRIT/garak plus manual creativity to find jailbreaks and data exfil paths — schedule before major launches.
- Practice: Run garak or PyRIT quick scan on a test model endpoint.Document five findings with severity and repro steps.Track fixes in issue tracker with retest dates.Invite non-author to attempt jailbreak (fresh eyes).Define sign-off criteria for GA.
- Code: `# Module 117 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 117, "topic": "Red Team Testing for AI Systems",`

**Module 118: Data Privacy, AI Alignment & Compliance** [Core] | Tools: `GDPR frameworks, AI Act basics`
- Learn: OverviewModule 118 (P16) — Data Privacy, AI Alignment & Compliance. Tools focus: GDPR frameworks, AI Act basics. Core path — prioritize in your sprint.Privacy, alignment, and compliance intersect: DPIAs, AI Act risk tiers, logging minimisation, and vendor DPAs. Legal review beats guesswork.
- Practice: Draft a one-page DPIA outline for a hypothetical AI feature: purpose, data categories, retention, automated decision impact, mitigations. Link each mitigation to modules you completed (RAG, auth, logging). No separate numbered lab — peer-review the outline and iterate once.
- Code: `# Module 118 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 118, "topic": "Data Privacy, AI Alignment & Comp`

#### P17 — Consultant Track
**Purpose:** Strategy, pricing, demos, 12 skills

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 119 | AI Strategy & Architecture Design | Core | Miro, architecture templates |
| 120 | The 12 AI Skills Matrix for 2026 | Core | Skills framework, self-assessment |
| 121 | Cost Optimisation for AI Systems | Core | Token calculators, model comparisons |
| 122 | Enterprise AI Implementation Playbook | Core | Consulting frameworks |
| 123 | AI Consultant Positioning & Pricing | Core | Deck templates, pricing models |
| 124 | Stakeholder Communication & Demos | Core | Streamlit, Gradio, Gamma |


**Module 119: AI Strategy & Architecture Design** [Core] | Tools: `Miro, architecture templates`
- Learn: OverviewModule 119 (P17) — AI Strategy & Architecture Design. Tools focus: Miro, architecture templates. Core path — prioritize in your sprint.AI strategy workshops align business outcomes, data readiness, and risk appetite. Architecture diagrams should separate hype from feasible 90-day milestones.
- Practice: Facilitate mock discovery: interview notes → problem tree.Draft current vs target architecture (as-is / to-be).Prioritise use cases by value × feasibility matrix.Identify data blockers early (access, quality, legal).Present executive summary in five slides without jargon walls.
- Code: `# Module 119 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 119, "topic": "AI Strategy & Architecture Design`

**Module 120: The 12 AI Skills Matrix for 2026** [Core] | Tools: `Skills framework, self-assessment`
- Learn: OverviewModule 120 (P17) — The 12 AI Skills Matrix for 2026. Tools focus: Skills framework, self-assessment. Core path — prioritize in your sprint.The twelve-skills framing maps technical depth (RAG, agents) to consulting skills (storytelling, pricing, change management). Self-assess honestly quarterly.
- Practice: Score yourself 1–5 on twelve skills (define the twelve from your framework notes). Pick the lowest two; tie each to two specific modules in this tracker to restudy. Write a 90-day improvement plan — completion is the scored matrix plus plan, not a software install.
- Code: `# Module 120 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 120, "topic": "The 12 AI Skills Matrix for 2026"`

**Module 121: Cost Optimisation for AI Systems** [Core] | Tools: `Token calculators, model comparisons`
- Learn: OverviewModule 121 (P17) — Cost Optimisation for AI Systems. Tools focus: Token calculators, model comparisons. Core path — prioritize in your sprint.Cost optimisation blends model routing, caching, prompt compression, and batching. Translate token math into monthly invoices stakeholders understand.
- Practice: Build spreadsheet: models × RPM × tokens × price.Simulate 30% traffic shift to smaller model; note quality guardrails.Evaluate prompt caching where providers support it.Add observability cost tags per feature flag.Present one slide CFO-friendly summary.
- Code: `# Module 121 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 121, "topic": "Cost Optimisation for AI Systems"`

**Module 122: Enterprise AI Implementation Playbook** [Core] | Tools: `Consulting frameworks`
- Learn: OverviewModule 122 (P17) — Enterprise AI Implementation Playbook. Tools focus: Consulting frameworks. Core path — prioritize in your sprint.Enterprise playbooks cover governance, landing zones, MLOps, and support models — adapt public cloud adoption frameworks to GenAI specifics.
- Practice: Read a cloud adoption framework chapter; map to AI workstreams.Define RACI for data science, security, platform, legal.Draft pilot exit criteria (accuracy, latency, incidents).Plan handover from pilot to BAU operations.Identify vendor lock-in risks and mitigations.
- Code: `# Module 122 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 122, "topic": "Enterprise AI Implementation Play`

**Module 123: AI Consultant Positioning & Pricing** [Core] | Tools: `Deck templates, pricing models`
- Learn: OverviewModule 123 (P17) — AI Consultant Positioning & Pricing. Tools focus: Deck templates, pricing models. Core path — prioritize in your sprint.Positioning and pricing tie outcomes to fees: value-based where possible, time-and-materials for discovery, retainers for advisory. Document assumptions explicitly.
- Practice: Write positioning statement for one niche (one sentence).Model three pricing scenarios with risk buffers.Create SOW outline: scope, exclusions, acceptance tests.Role-play negotiation objection on timeline.Define payment milestones tied to deliverables.
- Code: `# Module 123 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 123, "topic": "AI Consultant Positioning & Prici`

**Module 124: Stakeholder Communication & Demos** [Core] | Tools: `Streamlit, Gradio, Gamma`
- Learn: OverviewModule 124 (P17) — Stakeholder Communication & Demos. Tools focus: Streamlit, Gradio, Gamma. Core path — prioritize in your sprint.Stakeholder demos pair crisp narrative with working UI (Streamlit/Gradio/Gamma). Rehearse timing, backup offline slides, and Q&A on failure modes.
- Practice: Build five-minute demo script with click path.Record dry run; trim to timebox.Prepare three anticipated questions with evidence-backed answers.Add live failure demo (graceful) to show resilience.Collect feedback form; iterate once.
- Code: `# Module 124 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 124, "topic": "Stakeholder Communication & Demos`

#### P18 — Capstones
**Purpose:** Three portfolio projects

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 125 | CAPSTONE 1: AI That Calls You | Core | LangGraph, Twilio, FastAPI |
| 126 | CAPSTONE 2: AI Payment Risk Analyst | Core | RAG, compliance logic, FastAPI |
| 127 | CAPSTONE 3: Local Perplexity Clone | Core | Ollama, SearXNG, Streamlit UI |


**Module 125: CAPSTONE 1: AI That Calls You** [Core] | Tools: `LangGraph, Twilio, FastAPI`
- Learn: OverviewModule 125 (P18) — CAPSTONE 1: AI That Calls You. Tools focus: LangGraph, Twilio, FastAPI. Core path — prioritize in your sprint.Capstone 1: outbound voice or call experience using LangGraph orchestration, Twilio (or similar) telephony, and FastAPI webhooks — focus on state machine for call flows and PCI-adjacent caution.
- Practice: Define user story: who is called, when, and with what consent.Sketch call state machine (ringing, in-progress, escalate).Prototype webhook → LLM → TwiML response in dev environment.Add logging without recording sensitive audio in clear text.Document compliance checklist (consent, opt-out, retention).
- Code: `# Module 125 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 125, "topic": "CAPSTONE 1: AI That Calls You", "`

**Module 126: CAPSTONE 2: AI Payment Risk Analyst** [Core] | Tools: `RAG, compliance logic, FastAPI`
- Learn: OverviewModule 126 (P18) — CAPSTONE 2: AI Payment Risk Analyst. Tools focus: RAG, compliance logic, FastAPI. Core path — prioritize in your sprint.Capstone 2: payment risk analyst blends RAG over policy docs, structured rules, and human escalation — emphasise audit trails and non-hallucinated citations.
- Practice: Ingest policy corpuses with metadata (version, jurisdiction).Force citation snippets in model answers; validate existence.Implement risk score + threshold routing to human review.Add eval set of historical cases (synthetic if needed).Threat-model data leakage between tenants.
- Code: `# Module 126 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 126, "topic": "CAPSTONE 2: AI Payment Risk Analy`

**Module 127: CAPSTONE 3: Local Perplexity Clone** [Core] | Tools: `Ollama, SearXNG, Streamlit UI`
- Learn: OverviewModule 127 (P18) — CAPSTONE 3: Local Perplexity Clone. Tools focus: Ollama, SearXNG, Streamlit UI. Core path — prioritize in your sprint.Capstone 3: local Perplexity-style search combines SearXNG (or similar) results with local Ollama generation — optimise snippet stuffing and source display.
- Practice: Run SearXNG or alternative metasearch locally or docker.Pipe top snippets to Ollama with strict citation format.Build Streamlit UI with query + sources list.Handle search timeout and empty results gracefully.Compare answer quality with/without snippets on five questions.
- Code: `# Module 127 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 127, "topic": "CAPSTONE 3: Local Perplexity Clon`

#### P19 — Certifications
**Purpose:** Vendor credentials roadmap

| # | Module | Priority | Tools |
|---|--------|----------|-------|
| 128 | Google Cloud — Generative AI Leader & Vertex AI | Core | Gen AI Leader, Gemini, Vertex AI Agent Builder |
| 129 | AWS Certified AI Practitioner & Gen AI on AWS | Core | AIF-C01, Bedrock, Agents, Skill Builder |
| 130 | NVIDIA Generative AI LLM Certifications | Core | NCA-GENL, NCP-GENL, RAG & deployment labs |
| 131 | Microsoft Azure AI Engineer (AI-102) | Core | Azure OpenAI, AI Search, content filters, Entra patterns |
| 132 | IBM watsonx & Generative AI Engineering | Opt | watsonx.ai, enterprise Gen AI, governance |
| 133 | Hugging Face — LLM, Agents & Open Models | Core | Transformers, agents course, Hub, fine-tuning |


**Module 128: Google Cloud — Generative AI Leader & Vertex AI** [Core] | Tools: `Gen AI Leader, Gemini, Vertex AI Agent Builder`
- Learn: OverviewModule 128 (P19) — Google Cloud — Generative AI Leader & Vertex AI. Tools focus: Gen AI Leader, Gemini, Vertex AI Agent Builder. Core path — prioritize in your sprint.Vendor certifications structure how enterprises buy and govern AI. They complement — not replace — shipping agents, RAG systems, and the hands-on modules in this tracker.Generative AI Leader is Google Cloud’s business- and product-level credential: gen-AI concepts, Gemini and Vertex AI services, responsible use, and adoptio
- Practice: Download the official Google Cloud Generative AI Leader + Vertex AI exam guide and domain weights; highlight gaps vs your experience.Complete one instructor-led or self-paced course path; take notes in your own words.Run every hands-on lab twice: once following steps, once from memory with a checklist.Take a full practice exam; review every wrong answer against documentation.Book the exam; add a c
- Code: `# Module 128 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 128, "topic": "Google Cloud — Generative AI Lead`

**Module 129: AWS Certified AI Practitioner & Gen AI on AWS** [Core] | Tools: `AIF-C01, Bedrock, Agents, Skill Builder`
- Learn: OverviewModule 129 (P19) — AWS Certified AI Practitioner & Gen AI on AWS. Tools focus: AIF-C01, Bedrock, Agents, Skill Builder. Core path — prioritize in your sprint.AWS Certified AI Practitioner (AIF-C01) targets AI literacy on AWS: fundamentals of ML and generative AI, foundation models, responsible AI, and governance — aligned with product and engineering roles that touch Bedrock and agents.Study Bedrock, Agents, and IAM guardrails alongside this tracker’s API and security modules; scenario q
- Practice: Download the official AWS Certified AI Practitioner (AIF-C01) exam guide and domain weights; highlight gaps vs your experience.Complete one instructor-led or self-paced course path; take notes in your own words.Run every hands-on lab twice: once following steps, once from memory with a checklist.Take a full practice exam; review every wrong answer against documentation.Book the exam; add a calenda
- Code: `# Module 129 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 129, "topic": "AWS Certified AI Practitioner & G`

**Module 130: NVIDIA Generative AI LLM Certifications** [Core] | Tools: `NCA-GENL, NCP-GENL, RAG & deployment labs`
- Learn: OverviewModule 130 (P19) — NVIDIA Generative AI LLM Certifications. Tools focus: NCA-GENL, NCP-GENL, RAG & deployment labs. Core path — prioritize in your sprint.NVIDIA’s Generative AI LLM credentials (Associate NCA-GENL and Professional NCP-GENL) focus on LLM application design, prompting, data preparation, RAG-style workflows, deployment, evaluation, and responsible AI — closer to shipping assistants than to classical tabular ML.DLI workshops on RAG agents, deployment, and performance compleme
- Practice: Download the official NVIDIA Generative AI LLM (NCA-GENL / NCP-GENL) exam guide and domain weights; highlight gaps vs your experience.Complete one instructor-led or self-paced course path; take notes in your own words.Run every hands-on lab twice: once following steps, once from memory with a checklist.Take a full practice exam; review every wrong answer against documentation.Book the exam; add a 
- Code: `# Module 130 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 130, "topic": "NVIDIA Generative AI LLM Certific`

**Module 131: Microsoft Azure AI Engineer (AI-102)** [Core] | Tools: `Azure OpenAI, AI Search, content filters, Entra patterns`
- Learn: OverviewModule 131 (P19) — Microsoft Azure AI Engineer (AI-102). Tools focus: Azure OpenAI, AI Search, content filters, Entra patterns. Core path — prioritize in your sprint.The Azure AI Engineer (AI-102) exam emphasises Azure OpenAI, knowledge retrieval (including AI Search), content safety, and identity patterns you see in enterprise copilots and line-of-business agents.Cross-reference your LangChain, RAG, and governance modules: implementation choices on Azure mirror the same concerns (ground
- Practice: Download the official Microsoft Azure AI Engineer (AI-102) exam guide and domain weights; highlight gaps vs your experience.Complete one instructor-led or self-paced course path; take notes in your own words.Run every hands-on lab twice: once following steps, once from memory with a checklist.Take a full practice exam; review every wrong answer against documentation.Book the exam; add a calendar b
- Code: `# Module 131 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 131, "topic": "Microsoft Azure AI Engineer (AI-1`

**Module 132: IBM watsonx & Generative AI Engineering** [Optional] | Tools: `watsonx.ai, enterprise Gen AI, governance`
- Learn: OverviewModule 132 (P19) — IBM watsonx & Generative AI Engineering. Tools focus: watsonx.ai, enterprise Gen AI, governance. Optional depth — revisit when you need this specialty.IBM’s watsonx and Generative AI Engineering professional programs stress enterprise Gen AI patterns, tooling, and governance rather than notebook-only classical ML.Names and weights change — confirm the live curriculum and any exam blueprint before locking a date.
- Practice: Download the official IBM watsonx / Generative AI Engineering exam guide and domain weights; highlight gaps vs your experience.Complete one instructor-led or self-paced course path; take notes in your own words.Run every hands-on lab twice: once following steps, once from memory with a checklist.Take a full practice exam; review every wrong answer against documentation.Book the exam; add a calenda
- Code: `# Module 132 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 132, "topic": "IBM watsonx & Generative AI Engin`

**Module 133: Hugging Face — LLM, Agents & Open Models** [Core] | Tools: `Transformers, agents course, Hub, fine-tuning`
- Learn: OverviewModule 133 (P19) — Hugging Face — LLM, Agents & Open Models. Tools focus: Transformers, agents course, Hub, fine-tuning. Core path — prioritize in your sprint.Hugging Face is the hub for open models, datasets, and the ecosystem around Transformers. The LLM and Agents courses map directly to modules on fine-tuning, tool use, and open-weight deployment.Treat course certificates and skill badges as structured learning milestones; the practical proof remains repos and demos you ship with the
- Practice: Download the official Hugging Face LLM & Agents learning paths exam guide and domain weights; highlight gaps vs your experience.Complete one instructor-led or self-paced course path; take notes in your own words.Run every hands-on lab twice: once following steps, once from memory with a checklist.Take a full practice exam; review every wrong answer against documentation.Book the exam; add a calend
- Code: `# Module 133 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 133, "topic": "Hugging Face — LLM, Agents & Open`

---
