# Cursor-assisted curriculum narrative layer — Manish.AI
"""Per-module Learn/Steps HTML for all 133 modules (replaces generic scaffold)."""
from __future__ import annotations


def _e(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _ol(items: list[str]) -> str:
    return "<ol><li>" + "</li><li>".join(items) + "</li></ol>"


def _wrap(num: int, phase: str, title: str, tools: str, priority: str, inner: str) -> str:
    pri = (
        "Core path — prioritize in your sprint."
        if priority == "MUST DO"
        else "Optional depth — revisit when you need this specialty."
    )
    t, to = _e(title), _e(tools)
    head = (
        f"<div class='content-block'><div class='cb-label'>Overview</div><div class='cb-text'>"
        f"<p><strong>Module {num} ({phase})</strong> — {t}. "
        f"Tools focus: <em>{to}</em>. {pri}</p>{inner}</div></div>"
    )
    return head


# --- Shared templates (provider / pattern modules) ---------------------------------

def _api_learn_inner(vendor: str, env: str) -> str:
    return _inner(
        f"<p>{vendor}'s API is the reference stack for chat completions, structured outputs, embeddings, and tool calls in many production systems. You learn authentication, model selection, streaming vs batch, and how errors surface (rate limits, context length, content policy).</p>",
        "<p>Compare latency and cost across models in the same family (e.g. mini vs full) for your own prompt shapes. Log request IDs and token usage so you can explain spend to stakeholders.</p>",
        f"<ul><li>Configure <code>{_e(env)}</code> from the environment — never commit keys.</li><li>Use the official SDK; handle retries with exponential backoff.</li><li>Document which model you chose and why (quality, speed, price).</li></ul>",
    )


def _steps_openai_style(first_tool: str, vendor: str) -> str:
    return _ol(
        [
            f"Create a project API key in the {vendor} console; store it as an environment variable only.",
            "Install the official SDK for your language; run a minimal chat completion against a small model.",
            "Add structured logging: model name, latency, input/output token counts (no raw PII in logs).",
            "Call the same prompt with two model sizes; compare quality, latency, and documented pricing.",
            f"Write a short {first_tool} integration note: error codes you saw and how you handled them.",
        ]
    )


def _steps_cert(track: str) -> str:
    return _ol(
        [
            f"Download the official {track} exam guide and domain weights; highlight gaps vs your experience.",
            "Complete one instructor-led or self-paced course path; take notes in your own words.",
            "Run every hands-on lab twice: once following steps, once from memory with a checklist.",
            "Take a full practice exam; review every wrong answer against documentation.",
            "Book the exam; add a calendar block for final cram on weak domains only.",
        ]
    )


def _narrative_steps(text: str) -> str:
    return f"<p class='cb-text'>{text}</p>"


# --- Per-module learn bodies (module_num -> HTML fragment inside Overview already wrapped uses _wrap) ---
# We store inner HTML only (without outer wrap) for flexibility, then wrap in build_learn_html.

def _inner(*parts: str) -> str:
    return "".join(parts)


# Module number -> inner learn HTML (will be wrapped with title/tools in builder)
L_INNER: dict[int, str] = {}
S_STEPS: dict[int, str] = {}


def _add(n: int, learn_inner: str, steps: str) -> None:
    L_INNER[n] = learn_inner
    S_STEPS[n] = steps


# P0 — Local AI (1–6)
_add(
    1,
    _inner(
        "<p>Ollama runs open-weight models locally with a simple CLI and HTTP API. Models ship as downloadable blobs; you pull once and run offline-capable inference on CPU or GPU depending on size.</p>",
        "<p>Practice the full loop: install, pull a 7–8B-class model, run interactive chat, then call the HTTP API from a script. Note RAM/VRAM limits — if generation is slow, that is expected on CPU-only machines.</p>",
        "<ul><li>Distinguish <em>pull</em> vs <em>run</em> vs serving multiple models.</li><li>Know how to list installed models and free disk space.</li></ul>",
    ),
    _ol(
        [
            "Install Ollama from the official site for your OS; confirm `ollama --version`.",
            "Run `ollama pull` for a small chat model (e.g. llama3.2 or mistral) and wait for completion.",
            "Use `ollama run &lt;model&gt;` with three prompts: factual, reasoning, and code generation.",
            "From another terminal, hit the local HTTP API with curl or httpx using the same model.",
            "Document hardware (RAM/GPU), model size, and tokens/sec in NOTES.md for your portfolio.",
        ]
    ),
)
_add(
    2,
    _inner(
        "<p>LM Studio provides a desktop UI for discovering GGUF checkpoints, loading them with configurable context and GPU layers, and exposing an OpenAI-compatible local server (often on port 1234).</p>",
        "<p>Learn when GUI workflows beat CLI-only runners: comparing quantizations (Q4_K_M vs Q8), toggling GPU offload, and debugging tokenizer mismatches when copying prompts from hosted APIs.</p>",
    ),
    _ol(
        [
            "Install LM Studio; download one GGUF model appropriate for your machine.",
            "Start a local server; verify `GET /v1/models` returns your loaded model.",
            "From Python or curl, send a chat completion to the local OpenAI-compatible endpoint.",
            "Experiment with GPU layer count: note speed vs quality trade-offs in a short table.",
            "Export your server settings screenshot + one sample request/response (redact any sensitive text).",
        ]
    ),
)
_add(
    3,
    _inner(
        "<p>Open WebUI is a browser front-end for many backends (Ollama, OpenAI-compatible proxies). Docker is the common install path; you get multi-user patterns, model switching, and optional RAG plugins depending on build.</p>",
        "<p>Focus on operational concerns: volume mounts for persistence, upgrading images, and separating internal vs external network exposure if you demo on a laptop hotspot.</p>",
    ),
    _ol(
        [
            "Run Open WebUI via the documented Docker command; confirm the UI loads on localhost.",
            "Connect the UI to your local Ollama or LM Studio backend; send test chats through both.",
            "Create two model presets (e.g. fast vs quality) and document when you would use each.",
            "Back up or note the Docker volume path so you can recreate the environment.",
            "List one limitation you hit (auth, plugins, model list) and how you would address it in production.",
        ]
    ),
)
_add(
    4,
    _inner(
        "<p>vLLM targets high-throughput GPU serving with PagedAttention and continuous batching. It is the layer beneath many internal model-serving stacks when latency under load matters more than a desktop GUI.</p>",
        "<p>Understand CUDA/driver expectations, batching knobs, and when vLLM is overkill vs Ollama for solo development.</p>",
    ),
    _ol(
        [
            "Read the official installation prerequisites (CUDA version, GPU memory).",
            "Launch a minimal OpenAI-compatible server with a documented quickstart model.",
            "Send concurrent requests (simple script) and observe throughput vs single-threaded local runners.",
            "Capture one error from misconfigured CUDA or OOM and document the fix path.",
            "Write two sentences: when you would choose vLLM vs a simpler local runner for a client project.",
        ]
    ),
)
_add(
    5,
    _inner(
        "<p>LiteLLM is a unified router: one interface to many providers and local endpoints, with optional proxy features for budgets, fallbacks, and load balancing. It fits teams that standardize on OpenAI-style request bodies.</p>",
        "<p>Practice routing the same prompt to a local model and a hosted model; compare responses and failure modes when a backend is down.</p>",
    ),
    _ol(
        [
            "Install LiteLLM; configure at least two backends (e.g. Ollama + one hosted key).",
            "Send a completion through LiteLLM using the unified model string format.",
            "Simulate a failing backend; configure a fallback model and verify the request succeeds.",
            "Enable or inspect spend logging (if using proxy mode) with synthetic requests only.",
            "Document your routing table and when each backend is chosen.",
        ]
    ),
)
_add(
    6,
    _inner(
        "<p>Free or low-cost hosted APIs (Groq LPU-style inference, Gemini developer tier, Mistral keys, OpenRouter aggregation) let you prototype without training models. Each has different rate limits, safety filters, and JSON/tooling support.</p>",
        "<p>Build a comparison matrix: latency, max context, function-calling support, and pricing unit. Never ship production traffic on keys committed to git.</p>",
    ),
    _ol(
        [
            "Create sandbox keys for at least two listed providers; store them only in env vars.",
            "Run the same three prompts through each; log latency and rough quality notes.",
            "Check each vendor's rate-limit headers or dashboard; note burst vs sustained limits.",
            "Identify which provider supports tool calling for your SDK version — try one tool call if available.",
            "Summarize in one page which provider you would default to for prototyping vs demos.",
        ]
    ),
)

# P1 — Foundations (7–14) — m007 overridden by JSON
_add(
    7,
    _inner(
        "<p>This row is the blueprint vocabulary module. On-page definitions for forty terms appear when you use the enriched build; treat this block as a fallback if overrides are missing.</p>",
        "<p>Goal: explain each term to a peer in under thirty seconds without reading the slide.</p>",
    ),
    _ol(
        [
            "Read every term definition on the Learn tab; flag any you cannot paraphrase.",
            "Build a two-column sheet: term vs your one-sentence definition; self-check against the page.",
            "Pick five terms most relevant to your target role; tie each to a product decision.",
            "Run the tokenisation code sample and relate tokens to context windows and cost.",
        ]
    ),
)
_add(
    8,
    _inner(
        "<p>Transformers use self-attention so every position can attend to every other position in parallel — the architectural basis of modern LLMs. Tokenization turns text into subword IDs; context length and cost follow from token counts.</p>",
        "<p>Connect Hugging Face ecosystem concepts (configs, tokenizers) to what you see in API billing. Optional: load a small tokenizer and inspect how whitespace and punctuation split.</p>",
    ),
    _ol(
        [
            "Skim the Illustrated Transformer or HF docs summary; draw a one-page diagram: embedding → layers → logits.",
            "Run a tokenizer (HF or tiktoken) on three prompt shapes: code, bullet list, long paragraph.",
            "Compare token counts for the same meaning in verbose vs concise English.",
            "Note how special tokens (BOS/EOS/pad) appear in your encoder output.",
            "Write five bullets linking attention to long-context cost in production APIs.",
        ]
    ),
)
_add(
    9,
    _inner(
        "<p>Embeddings map text (or images) into dense vectors so semantic similarity becomes geometry: cosine distance in vector space approximates related meaning. They power retrieval, clustering, and RAG front-ends.</p>",
        "<p>Contrast OpenAI-style embedding endpoints with open sentence-transformer models you can run locally. Understand normalization, dimensionality, and when to re-embed after model upgrades.</p>",
    ),
    _ol(
        [
            "Embed ten short phrases (two similar pairs, one opposite pair) using one API or local model.",
            "Compute cosine similarity between vectors; sanity-check that related phrases score higher.",
            "Change one word in a phrase and measure how much the vector shifts.",
            "Document embedding dimension and model version used — versioning matters for retrieval indexes.",
            "List one failure mode (polysemy, language mix) and a mitigation (metadata, rerankers).",
        ]
    ),
)
_add(
    10,
    _inner(
        "<p>Inference is the forward pass at serving time — distinct from training. Context windows cap how much text fits in one call; providers bill input and output tokens separately, and long prompts hit latency and cost cliffs.</p>",
        "<p>Practice measuring tokens before send, trimming history, summarizing threads, and choosing smaller models for easy subtasks.</p>",
    ),
    _ol(
        [
            "Pick a tokenizer or API metadata; measure tokens for a long thread before and after summarization.",
            "Call a chat model with the same task using a large vs small model; compare cost and latency.",
            "Implement a simple token budget guard that refuses or compresses when over a threshold.",
            "Read provider docs for max context and output limits; note what happens on overflow.",
            "Write a stakeholder-friendly paragraph explaining why “bigger context” is not free.",
        ]
    ),
)
_add(
    11,
    _inner(
        "<p>Quantization reduces weight precision (e.g. FP16 → INT8 → 4-bit) to shrink memory and speed inference. GGUF bundles for llama.cpp, GPTQ, and bitsandbytes QLoRA during training are common touchpoints.</p>",
        "<p>Understand accuracy vs size trade-offs and why quantized models behave slightly differently on code or math.</p>",
    ),
    _ol(
        [
            "Read one official guide each for GGUF inference vs training-time quantization (QLoRA).",
            "Run one pre-quantized model locally; note RAM/VRAM vs full precision expectations.",
            "List three metrics you would monitor if you switched quantization in production (latency, perplexity, task evals).",
            "Identify a task where low-bit quantization might fail (e.g. long arithmetic) and test informally.",
            "Summarize when you would quantize for edge deployment vs keep FP16 in cloud.",
        ]
    ),
)
_add(
    12,
    _inner(
        "<p>GPUs parallelize matrix multiply for training and inference; TPUs are Google’s ASIC line for large matmul workloads. Colab and cloud pods abstract hardware, but data movement and memory bandwidth still dominate.</p>",
        "<p>Map a simple training or inference job to GPU memory usage — batch size, sequence length, and precision interact.</p>",
    ),
    _ol(
        [
            "List differences between latency-sensitive inference and throughput-heavy training on GPUs.",
            "Spin up one GPU notebook or pod; run a tiny matmul or model forward pass; note device name and memory.",
            "Read vendor docs for one TPU offering; compare programming model to CUDA briefly.",
            "Estimate rough VRAM needs for a model size you care about (parameters × precision heuristic).",
            "Document one operational issue: driver mismatch, OOM, or cold start — and the fix.",
        ]
    ),
)
_add(
    13,
    _inner(
        "<p>Supervised learning fits labeled pairs; unsupervised structure learns without per-example labels; RL optimizes policies via rewards. Generative models (including LLMs) are often pretrained with self-supervised next-token objectives.</p>",
        "<p>Place LLM fine-tuning and RLHF in this map so you can explain trade-offs to non-specialists.</p>",
    ),
    _ol(
        [
            "For each paradigm, write one real-world example (not toy XOR) relevant to business data.",
            "Run a minimal sklearn supervised example; note fit/predict vs generative “generate” APIs.",
            "Explain why RLHF is related to RL but not the same as classic game-playing RL.",
            "List where unsupervised embeddings appear in your RAG or search roadmap.",
            "Create a comparison table: data needs, evaluation, and typical risk for each paradigm.",
        ]
    ),
)
_add(
    14,
    _inner(
        "<p>A generative pipeline moves from prompt or UI input through preprocessing, model call, optional tools/RAG, post-processing, and logging. Reliability comes from contracts at each hop — schemas, timeouts, and fallbacks.</p>",
        "<p>Sketch your own diagram for a support-bot vs a batch summariser; identify different bottlenecks.</p>",
    ),
    _ol(
        [
            "Draw input→process→output for one product idea; annotate trust boundaries and PII touchpoints.",
            "Implement a toy pipeline in Python: validate input → call model → validate output JSON.",
            "Add structured logging at each stage without logging secrets or user content raw.",
            "Identify two stages where caching would help and what invalidation policy you need.",
            "Write acceptance criteria for “done” that include latency and error-rate SLOs.",
        ]
    ),
)

# P2 — Prompt engineering (15–21)
_add(
    15,
    _inner(
        "<p>Prompt engineering is the highest-ROI lever before changing models: clarity, format, examples (few-shot), and role framing steer behaviour more cheaply than fine-tunes for many tasks.</p>",
        "<p>Practice rewriting vague prompts into instructions with constraints, output format (JSON/Markdown), and evaluation rubrics you can automate later.</p>",
    ),
    _ol(
        [
            "Take one business task; write a bad prompt, then two improved iterations with explicit format.",
            "Add a negative constraint (“do not”) and verify the model respects it on five trials.",
            "Compare zero-shot vs two-shot for a structured extraction task; score with a simple checklist.",
            "Document temperature and max-tokens choices and why they fit this task.",
            "Peer-review another learner’s prompt for ambiguity; revise together.",
        ]
    ),
)
_add(
    16,
    _inner(
        "<p>Chain-of-thought elicits intermediate reasoning before answers, improving multi-step math and logic when the model is instructed to show steps — but increases tokens and can leak verbose internals.</p>",
        "<p>Learn when to keep reasoning hidden from end users vs when to display it for auditability.</p>",
    ),
    _ol(
        [
            "Solve five numeric word problems with and without CoT; compare accuracy.",
            "Ask for explicit “final answer in a box” after reasoning to separate UI from chain.",
            "Measure token increase from CoT; decide if cost is justified per task.",
            "Try a self-consistency variant (multiple chains, vote) on one hard puzzle.",
            "Note one failure mode (overconfident wrong chain) and a guardrail.",
        ]
    ),
)
_add(
    17,
    _inner(
        "<p>Context management is how you fit history, documents, and tool results under a finite window: summarization, sliding windows, and structured memory objects. Long-context models reduce pressure but not cost.</p>",
        "<p>Implement a policy for what stays verbatim vs summarized in a conversational agent.</p>",
    ),
    _ol(
        [
            "Simulate a 20-turn chat; count tokens cumulatively with a tokenizer.",
            "Apply a summarise-every-N-turns policy; check information retention on a quiz.",
            "Compare “full history” vs “summary + last K turns” on task success.",
            "Read provider notes on prompt caching where applicable; note billing impact.",
            "Write rules for when to reset context vs fork a new session.",
        ]
    ),
)
_add(
    18,
    _inner(
        "<p>Multi-agent prompting assigns roles (researcher, critic, writer) and coordinates hand-offs. Frameworks like CrewAI or AutoGen encode patterns, but the design principles are delegation, clear interfaces, and stop conditions.</p>",
        "<p>Focus on avoiding infinite chatter: budgets for rounds and explicit termination.</p>",
    ),
    _ol(
        [
            "Design three roles for one task; specify inputs/outputs per role as JSON fields.",
            "Run a minimal two-agent exchange in code or a framework; cap at three rounds.",
            "Log each hand-off; verify no duplicate work or contradictory assumptions.",
            "Add a critic step that checks format before final user-visible output.",
            "Retrospective: when would a single-agent prompt be simpler and safer?",
        ]
    ),
)
_add(
    19,
    _inner(
        "<p>Self-critique and reflexion patterns ask the model to evaluate its draft and revise. LangGraph and custom loops implement retries with state — production needs limits to avoid runaway spend.</p>",
    ),
    _ol(
        [
            "Implement generate→critique→revise for one writing task; stop after two revisions max.",
            "Compare single-pass vs two-pass quality using a rubric you define.",
            "Instrument token usage per revision; plot cost vs gain.",
            "Handle critique refusal or empty output gracefully in code.",
            "Document when reflexion is inappropriate (latency-sensitive chat).",
        ]
    ),
)
_add(
    20,
    _inner(
        "<p>Task planning prompts decompose goals into ordered steps; role prompting sets expertise and tone. Combine with explicit tool lists when the model should choose actions.</p>",
    ),
    _ol(
        [
            "Write a planner prompt that outputs a numbered plan only (no execution).",
            "Feed the plan to an executor prompt; check step adherence on a simple project.",
            "Swap roles (junior vs principal) and note behaviour changes.",
            "Add a checklist the model must tick before claiming completion.",
            "Capture one derailment (skipped step) and tighten the prompt.",
        ]
    ),
)
_add(
    21,
    _inner(
        "<p>Prompt chaining composes LCEL or LangGraph nodes so each stage has a contract. Advanced techniques include routing, parallel branches, and structured outputs between hops.</p>",
    ),
    _ol(
        [
            "Build a three-node chain: extract → transform → generate; validate JSON between nodes.",
            "Add a conditional branch on extracted intent; test two paths.",
            "Measure end-to-end latency vs monolithic prompt.",
            "Version prompts separately per node; document compatibility.",
            "List failure modes per hop and corresponding fallbacks.",
        ]
    ),
)

# P3 — LLMs & APIs (22–25)
_add(
    22,
    _api_learn_inner("OpenAI", "OPENAI_API_KEY"),
    _steps_openai_style("openai Python SDK", "OpenAI"),
)
_add(
    23,
    _api_learn_inner("Anthropic", "ANTHROPIC_API_KEY"),
    _steps_openai_style("anthropic Python SDK", "Anthropic"),
)
_add(
    24,
    _inner(
        "<p>Google’s Gemini API exposes multimodal and long-context models with a distinct SDK surface from OpenAI. You learn API keys via AI Studio, model IDs, safety settings, and quota dashboards.</p>",
        "<p>Compare request/response shapes to OpenAI for the same task; note tool and JSON schema support per model generation.</p>",
        "<ul><li>Store keys in <code>GOOGLE_API_KEY</code> or the env var your SDK expects.</li><li>Log model id + latency; avoid logging user media bytes.</li></ul>",
    ),
    _ol(
        [
            "Create a key in Google AI Studio; export it to your shell environment only.",
            "Install google-genai or google-generativeai per current docs; list models available to your project.",
            "Run text and (if available) one image+text call; capture latency.",
            "Try structured output or function calling if supported on your chosen model.",
            "Write integration notes: differences vs OpenAI that would affect a shared abstraction.",
        ]
    ),
)
_add(
    25,
    _inner(
        "<p>Mistral’s hosted API and open-weights families (e.g. LLaMA-class, DeepSeek-class on Hugging Face) span commercial keys and self-hosted inference. Understand license tags, gated models, and HF tokens for downloads.</p>",
        "<p>Practice one hosted completion and one local or HF inference path so you can advise clients on lock-in vs control.</p>",
    ),
    _ol(
        [
            "Create a Mistral API key or HF token; never commit either.",
            "Call a Mistral chat model via official SDK or HTTP.",
            "Pull a small open model card on Hugging Face; read license and use restrictions.",
            "Run a minimal generate call locally or via inference endpoint if feasible.",
            "Summarize when you would recommend API vs self-host for a regulated client.",
        ]
    ),
)

# P3 continued 26–29
_add(
    26,
    _inner(
        "<p>Production API usage requires key rotation, least privilege keys, exponential backoff on 429/5xx, and idempotency for retried writes. Centralize secrets in vaults or managed stores.</p>",
        "<p>Practice reading Retry-After headers and structuring tenacity (or equivalent) policies.</p>",
    ),
    _ol(
        [
            "Implement retries with jitter; never retry non-idempotent POSTs blindly without design.",
            "Log HTTP status and request id only — not payloads with PII.",
            "Simulate rate limits with a mock server or tiny limit in a test key.",
            "Document key rotation procedure for your team (who, how often, blast radius).",
            "Add a circuit breaker sketch: after N failures, fail fast and alert.",
        ]
    ),
)
_add(
    27,
    _inner(
        "<p>Tool / function calling lets models emit structured actions the runtime executes. Schemas must be tight: enums, descriptions, and required fields reduce hallucinated arguments.</p>",
    ),
    _ol(
        [
            "Define one JSON schema tool; register it with the provider SDK you use.",
            "Handle tool_calls in a loop until the model returns user-visible content.",
            "Test three successful calls and two invalid-args paths; verify error handling.",
            "Compare parallel vs serial tool execution for your use case.",
            "Document trust boundaries: which tools can touch production data?",
        ]
    ),
)
_add(
    28,
    _inner(
        "<p>Parsing tool outputs into Pydantic models (or equivalent) enforces types before side effects. LangChain structured output helpers wrap similar ideas with retries.</p>",
    ),
    _ol(
        [
            "Return tool output as JSON; validate with Pydantic v2 models.",
            "Add a repair pass: on ValidationError, ask the model to fix shape.",
            "Unit-test parsers with golden files (no live API).",
            "Measure how often repair passes trigger in a 50-call sample.",
            "List schemas you would never auto-parse without human review.",
        ]
    ),
)
_add(
    29,
    _inner(
        "<p>Multimodal models accept images, audio, or video alongside text. Constraints include resolution limits, MIME handling, latency of uploads, and safety filters on media.</p>",
    ),
    _ol(
        [
            "Call a vision-capable model with three image types: chart, screenshot, photo.",
            "Compare text-only vs image+text answers on a diagram question.",
            "Handle oversized images: resize/compress pipeline with tests.",
            "Read provider limits on frames or duration for video inputs.",
            "Write privacy rules for user-uploaded media in logs and retention.",
        ]
    ),
)

# P4 — Agent fundamentals (30–36)
_add(
    30,
    _inner(
        "<p>Agents combine a language model with a control loop, tools, and memory to pursue multi-step goals. Semi-autonomous systems keep humans in the loop for approvals; fully autonomous loops need budgets and kill switches.</p>",
    ),
    _ol(
        [
            "Define “agent” vs “workflow script” for one use case in your words.",
            "List tools your agent would need; classify read vs write risk.",
            "Sketch state: what variables persist across turns?",
            "Identify stop conditions and max spend per task.",
            "Note one scenario where agents are the wrong abstraction.",
        ]
    ),
)
_add(
    31,
    _inner(
        "<p>ReAct interleaves reasoning traces with tool calls; CAMEL-style role play coordinates two LLMs; AutoGPT popularized goal stacks. All share the risk of runaway loops without caps.</p>",
    ),
    _ol(
        [
            "Implement a minimal ReAct loop in pseudocode or LangChain with one tool.",
            "Log each thought/action/observation triplet for debugging.",
            "Compare CAMEL two-agent setup vs single-agent for the same task.",
            "Read AutoGPT architecture summary; list three production hazards.",
            "Write termination rules you would enforce in code, not prompts only.",
        ]
    ),
)
_add(
    32,
    _inner(
        "<p>Goal decomposition turns vague objectives into ordered subtasks. Planners can be classical algorithms, LLM-generated plans, or hybrid graphs in LangGraph.</p>",
    ),
    _ol(
        [
            "Generate a plan for a multi-step research task; validate dependencies manually.",
            "Detect cyclic or impossible dependencies in the plan.",
            "Convert the plan into a LangGraph-style node list with edges.",
            "Simulate one failed subtask; define replanning policy.",
            "Estimate token cost of planning vs execution for your example.",
        ]
    ),
)
_add(
    33,
    _inner(
        "<p>Policies decide which tool or transition fires given state — epsilon-greedy exploration is rare in LLM agents; instead you use classifiers, routers, or scored choices. State machines keep behaviour auditable.</p>",
    ),
    _ol(
        [
            "Model agent state as an enum + small dict; document transitions.",
            "Implement if/match routing vs LLM-chosen tool once; compare failure rates on five cases.",
            "Add a default safe action when confidence is low.",
            "Log policy decisions with reasons (structured JSON).",
            "Describe how you would unit-test a policy without calling live models.",
        ]
    ),
)
_add(
    34,
    _inner(
        "<p>Action planning loops execute tools, observe results, and continue until success criteria. Reliability requires timeouts, partial progress checkpoints, and idempotent tools where possible.</p>",
    ),
    _ol(
        [
            "Run a five-step synthetic task with mocked tools; verify ordering.",
            "Inject a tool timeout; ensure the loop surfaces a recoverable error.",
            "Persist partial results to disk or DB between steps.",
            "Measure wall-clock vs model time vs tool time.",
            "Define success predicates that code checks — not vibes.",
        ]
    ),
)
_add(
    35,
    _inner(
        "<p>Self-reflection asks the model to critique prior outputs; multi-agent collaboration splits expertise. Combine with evaluation harnesses so reflection improves measurable scores.</p>",
    ),
    _ol(
        [
            "Pair generator and critic agents; cap at two critique rounds.",
            "Score outputs with a rubric before/after critique.",
            "Log whether critiques are actionable vs generic.",
            "Try a third agent as tie-breaker; note coordination overhead.",
            "Decide when human review replaces automated critique.",
        ]
    ),
)
_add(
    36,
    _inner(
        "<p>Tool-use system design covers discovery, schemas, authentication to backends, and principle of least privilege. Treat tools like microservices with contracts and audit trails.</p>",
    ),
    _ol(
        [
            "Inventory tools by data sensitivity (public, internal, PII).",
            "Draft OpenAPI-style descriptions for two tools; map to provider tool JSON.",
            "Implement auth per tool (API key, OAuth) without sharing one global secret.",
            "Add allowlists for domains or file paths.",
            "Red-team: what could a malicious prompt ask your tool to do?",
        ]
    ),
)

# P5 — Tool use & integration (37–44)
_add(
    37,
    _inner(
        "<p>Memory types: short-term (conversation buffer), long-term (vector store of facts), episodic (past task traces). Stale memory hurts — TTLs and provenance matter.</p>",
    ),
    _ol(
        [
            "Choose one memory backend; store three synthetic “facts” with metadata.",
            "Retrieve with a natural-language query; verify precision.",
            "Expire or update one fact; confirm retrieval changes.",
            "Log memory writes with source and timestamp.",
            "List privacy implications of long-term user memory.",
        ]
    ),
)
_add(
    38,
    _inner(
        "<p>Calling HTTP APIs from agents requires URL validation, SSRF protection, timeouts, and response size limits. Prefer typed clients (httpx) over ad-hoc requests in prompts.</p>",
    ),
    _ol(
        [
            "Wrap httpx calls with timeout + max bytes read.",
            "Block private IP ranges in a URL validator unittest.",
            "Parse JSON safely; handle HTML error pages.",
            "Add redaction of auth headers in logs.",
            "Document retry policy for idempotent GETs only.",
        ]
    ),
)
_add(
    39,
    _inner(
        "<p>File tools read/write user or system files — highest risk surface. Sandboxed paths, extension allowlists, and size caps reduce exfiltration and destructive writes.</p>",
    ),
    _ol(
        [
            "Constrain reads to a single workspace directory in code.",
            "Reject symlinks escaping the workspace.",
            "Implement write with backup or dry-run mode.",
            "Test with oversized file and binary file edge cases.",
            "Describe how you’d add virus scanning for uploads in production.",
        ]
    ),
)
_add(
    40,
    _inner(
        "<p>Code interpreter tools execute arbitrary code — use containers (E2B, Docker) with network disabled by default, CPU/memory limits, and short TTLs.</p>",
    ),
    _ol(
        [
            "Run hello-world in an isolated container or sandbox service.",
            "Disable outbound network in sandbox config; verify blocked.",
            "Set CPU and RAM limits; observe OOM behaviour.",
            "Whitelist allowed pip packages or base images.",
            "Write incident response if user code escapes sandbox (theoretical tabletop).",
        ]
    ),
)
_add(
    41,
    _inner(
        "<p>Search tools ground agents in fresh web data. Choose APIs with clear ToS; cache results; deduplicate snippets before stuffing context.</p>",
    ),
    _ol(
        [
            "Integrate one search API; fetch top five results for a query.",
            "Normalize titles/snippets; measure token cost to inject into prompt.",
            "Add query length limits and profanity filters if required by policy.",
            "Compare search-augmented vs non-search answer on a time-sensitive fact.",
            "Log query hashes instead of raw queries if PII is possible.",
        ]
    ),
)
_add(
    42,
    _inner(
        "<p>Browsing tools (Playwright, Firecrawl) render pages and extract content — fragile vs layout changes and heavy on resources. Prefer structured APIs when available.</p>",
    ),
    _ol(
        [
            "Fetch one static page and one SPA; note differences in extraction quality.",
            "Set navigation timeouts and user-agent responsibly.",
            "Strip scripts and ads before sending text to the model.",
            "Respect robots.txt for public projects; note legal nuance.",
            "Fallback path when page load fails mid-task.",
        ]
    ),
)
_add(
    43,
    _inner(
        "<p>AEO/GEO optimises how brands appear in AI-generated answers vs classic blue-link SEO. Signals include factual consistency, structured data, and citation-friendly sources.</p>",
    ),
    _narrative_steps(
        "There is no universal install checklist. Study how answer engines synthesise snippets, audit your public facts for consistency across pages, "
        "propose a measurement plan (branded queries in major assistants), and document three content changes you would pilot. Mark complete when your one-pager is reviewed by a peer."
    ),
)
_add(
    44,
    _inner(
        "<p>LangChain standardises chains, tools, retrievers, and LCEL composition. Learn when abstraction helps vs when raw SDK calls are clearer for small services.</p>",
    ),
    _ol(
        [
            "Build RunnableSequence with prompt | model | parser.",
            "Add a retriever + stuff chain for three documents.",
            "Swap LLM provider using LangChain adapters.",
            "Profile import time and cold start — note operational cost.",
            "List one feature you would not use in production and why.",
        ]
    ),
)

# P6 — Frameworks (45–54) — order matches ROWS: LangChain, LangGraph, CrewAI, …
_add(
    45,
    _inner(
        "<p>LangChain unifies prompts, models, tools, retrievers, and LCEL Runnable chains. The goal is composable pipelines with clear I/O contracts — not every app needs the full framework surface.</p>",
        "<p>Deepen LCEL, structured output parsers, and retrieval chains; profile cold start and dependency weight before committing in latency-sensitive services.</p>",
    ),
    _ol(
        [
            "Build RunnableSequence: prompt | chat model | StrOutputParser.",
            "Add a retriever + stuff_documents chain on three local text files.",
            "Swap model provider via LangChain integration; keep the same interface.",
            "Write two unit tests with mocked LLM for deterministic CI.",
            "List which LangChain layers you would keep thin in production vs raw SDK.",
        ]
    ),
)
_add(
    46,
    _inner(
        "<p>LangGraph adds persistence, interrupts, and cyclic graphs for agents. State reducers and checkpointing enable human-in-the-loop and crash recovery.</p>",
    ),
    _ol(
        [
            "Model a three-node graph with one conditional edge.",
            "Enable checkpointing to sqlite or memory; restart mid-run.",
            "Trigger an interrupt before a destructive tool; resume after approval.",
            "Draw your graph for stakeholders (boxes and arrows).",
            "Compare LangGraph complexity vs a plain Python loop for the same task.",
        ]
    ),
)
_add(
    47,
    _inner(
        "<p>CrewAI encodes crews, agents, and tasks with role descriptions. Good for demos; watch for hidden sequential coupling and unclear hand-offs.</p>",
    ),
    _ol(
        [
            "Define two agents with non-overlapping responsibilities.",
            "Create tasks with expected_output strings; run once end-to-end.",
            "Log each task completion artifact.",
            "Tighten prompts when output format drifts.",
            "Note licensing and dependency weight for deployment.",
        ]
    ),
)
_add(
    48,
    _inner(
        "<p>AutoGen uses conversable agents with code execution hooks. Learn group chat patterns and safety around code_runner.</p>",
    ),
    _ol(
        [
            "Spin up two-agent chat solving a coding puzzle.",
            "Constrain code execution to a sandbox if available.",
            "Stop the chat after N messages programmatically.",
            "Capture one failure where agents talk past each other; fix prompts.",
            "Summarize when AutoGen beats simpler orchestration.",
        ]
    ),
)
_add(
    49,
    _inner(
        "<p>Flowise is a low-code node UI on top of chains. Useful for prototyping; export and version flows for staging promotions.</p>",
    ),
    _ol(
        [
            "Deploy Flowise via Docker locally.",
            "Build a flow: input → LLM → output parser.",
            "Export JSON; reload in a second environment.",
            "Identify secrets in nodes; move to env vars.",
            "List gaps vs code-first CI/CD for your org.",
        ]
    ),
)
_add(
    50,
    _inner(
        "<p>AgentOps and LangSmith-class tools trace spans per model/tool call. You need consistent run IDs, cost attribution, and PII scrubbing.</p>",
    ),
    _ol(
        [
            "Instrument one agent with tracing SDK; view a waterfall.",
            "Tag traces with user_session anonymized.",
            "Add eval scores to a traced run manually.",
            "Configure retention policy appropriate for test data.",
            "Document who can access traces in your team RBAC model.",
        ]
    ),
)
_add(
    51,
    _inner(
        "<p>Haystack builds retrieval and QA pipelines with a document store abstraction. Compare to LangChain when teams already standardise on Haystack nodes.</p>",
    ),
    _ol(
        [
            "Run a minimal indexing + query pipeline from docs.",
            "Swap retriever component once (e.g. BM25 vs dense).",
            "Measure recall@k on five hand-made questions.",
            "Note deployment story for their pipeline runner.",
            "Decide Haystack vs LlamaIndex for one sample project.",
        ]
    ),
)
_add(
    52,
    _inner(
        "<p>Semantic Kernel is Microsoft’s SDK for planners, plugins, and memory across .NET/Python. Relevant when integrating with Azure AI services.</p>",
    ),
    _ol(
        [
            "Install SK for Python or .NET per your stack.",
            "Register one native plugin with two functions.",
            "Run a planner that selects functions automatically.",
            "Connect to an Azure OpenAI deployment if you have access; otherwise mock.",
            "Map SK concepts to LangChain terminology in a cheat sheet.",
        ]
    ),
)
_add(
    53,
    _inner(
        "<p>LlamaIndex focuses on data connectors, indexes, and query engines over heterogeneous sources. Strong for RAG-centric products.</p>",
    ),
    _ol(
        [
            "Load ten docs; build VectorStoreIndex.",
            "Try query_engine vs chat_engine for the same question.",
            "Add metadata filters to a query.",
            "Persist index to disk; reload in a new process.",
            "Profile indexing time vs query latency.",
        ]
    ),
)
_add(
    54,
    _inner(
        "<p>W&B tracks experiments; Arize/Phoenix targets LLM observability and embeddings drift. Pick tooling based on whether you optimise training or production inference.</p>",
    ),
    _ol(
        [
            "Log a small training or finetune run to W&B with hyperparameters.",
            "Create one dashboard chart you would show a client.",
            "Send a batch of prompts through Phoenix (or read tutorial); inspect traces.",
            "Define one drift metric for embeddings in production.",
            "Document cost of SaaS observability at your expected volume.",
        ]
    ),
)

# P7 — RAG (55–61)
_add(
    55,
    _inner(
        "<p>RAG combines retrieval with generation: chunk documents, embed, index, retrieve top-k, inject into prompt, generate with citations. Failure modes include wrong chunk boundaries and stale corpora.</p>",
    ),
    _ol(
        [
            "Diagram your target RAG pipeline with trust boundaries.",
            "List five ways retrieval can fail; pair each with a mitigation.",
            "Prototype ingest → chunk → embed → store with ten docs.",
            "Run five queries; log precision qualitatively.",
            "Define refresh policy when source docs change.",
        ]
    ),
)
_add(
    56,
    _inner(
        "<p>Embedding model choice affects recall: multilingual, domain fit (legal, medical), and MRL dimensions. Re-embedding is expensive — version indexes.</p>",
    ),
    _ol(
        [
            "Compare two embedding models on the same ten-query set.",
            "Measure index build time and query latency.",
            "Test cross-language if relevant to your users.",
            "Store model name + dimension in index metadata.",
            "Plan A/B procedure before swapping embeddings live.",
        ]
    ),
)
_add(
    57,
    _inner(
        "<p>Chunking trades context coherence vs specificity: fixed size, sentence-aware, semantic splits, and late chunking techniques. Headers and metadata improve filtering.</p>",
    ),
    _ol(
        [
            "Chunk one long policy doc three ways; compare retrieval hits.",
            "Attach section titles as metadata on chunks.",
            "Tune overlap; observe redundancy in retrieved sets.",
            "Find a case where small chunks win vs large chunks.",
            "Document recommended chunk strategy per document type you serve.",
        ]
    ),
)
_add(
    58,
    _inner(
        "<p>Loaders ingest PDFs, HTML, Notion exports, etc. Unstructured and vendor loaders differ on OCR quality and table handling — always validate samples.</p>",
    ),
    _ol(
        [
            "Ingest PDF + HTML + CSV samples; inspect extracted text quality.",
            "Handle encoding errors explicitly in pipeline code.",
            "Strip boilerplate footers/headers where they harm retrieval.",
            "Quarantine files that fail parse; alert operators.",
            "Estimate end-to-end ingest time per GB.",
        ]
    ),
)
_add(
    59,
    _inner(
        "<p>Vector databases differ on hybrid search, filtering, multi-tenancy, and ops model (serverless vs self-host). FAISS is a library; Pinecone/Weaviate/Chroma are services or servers.</p>",
    ),
    _ol(
        [
            "Create a collection/index; upsert 1k vectors with metadata.",
            "Run metadata-filtered queries; verify performance.",
            "Try hybrid (BM25 + vector) if supported.",
            "Snapshot backup/restore procedure.",
            "Rough TCO: self-host vs managed for one workload.",
        ]
    ),
)
_add(
    60,
    _inner(
        "<p>Query refinement rewrites user questions; hybrid search blends lexical and dense signals; rerankers reorder top-k for better precision at small k.</p>",
    ),
    _ol(
        [
            "Log raw user queries vs rewritten queries; compare results.",
            "Tune BM25 vs vector weights on five test questions.",
            "Add a cross-encoder reranker; measure latency impact.",
            "Define when to skip reranking for cost reasons.",
            "Document fallback if rewriter hallucinates constraints.",
        ]
    ),
)
_add(
    61,
    _inner(
        "<p>Knowledge graphs model entities and relations; GraphRAG combines graph traversal with LLM summarisation. Higher setup cost, strong for multi-hop reasoning over structured domains.</p>",
    ),
    _ol(
        [
            "Model ten triples from a tiny domain (manual OK).",
            "Run one multi-hop question requiring two edges.",
            "Compare graph answer vs vector-only answer on same question.",
            "List maintenance cost when facts change frequently.",
            "Identify one client vertical where graphs pay off.",
        ]
    ),
)

# P8 — MCP (62–69)
_add(
    62,
    _inner(
        "<p>MCP standardises how hosts expose tools, resources, and prompts to models. It complements (not replaces) your HTTP APIs — think structured capability contracts.</p>",
    ),
    _ol(
        [
            "Read the MCP intro + spec outline; list three primitives.",
            "Contrast MCP with ad-hoc REST tools you already built.",
            "Sketch a host → client → server diagram for your desktop assistant.",
            "List security questions (filesystem, network) MCP must answer.",
            "Pick one sample server from official repos to run read-only.",
        ]
    ),
)
_add(
    63,
    _inner(
        "<p>Hosts (Claude Desktop, IDEs) spawn MCP clients; servers implement capabilities over stdio or HTTP+SSE. Lifecycle includes capability negotiation and stderr logging.</p>",
    ),
    _ol(
        [
            "Configure one MCP server in Claude Desktop JSON config.",
            "Verify the host lists tools/resources after restart.",
            "Inspect logs for handshake errors; fix path or command once.",
            "Document how you’d pin server version for teams.",
            "Threat-model: what data leaves the machine?",
        ]
    ),
)
_add(
    64,
    _inner(
        "<p>Transports carry JSON-RPC messages: stdio for local trust boundaries; HTTP+SSE for remote servers. Latency and auth differ materially.</p>",
    ),
    _ol(
        [
            "Run a stdio server; trace one request/response with debug logging.",
            "Read transport section of spec; note framing rules.",
            "Compare stdio vs remote transport for a corporate locked-down laptop.",
            "Add TLS and auth sketch for remote deployment.",
            "List failure modes: partial frames, timeouts, proxy interference.",
        ]
    ),
)
_add(
    65,
    _inner(
        "<p>Sampling and filesystem rules gate model access to local resources. Least privilege defaults beat “allow all” demos.</p>",
    ),
    _ol(
        [
            "Enable directory allowlist in a sample server config.",
            "Attempt disallowed path access; confirm denial.",
            "Review sampling callbacks — when human approval triggers.",
            "Document audit log fields you would ship.",
            "Red-team prompt injection via malicious file contents.",
        ]
    ),
)
_add(
    66,
    _inner(
        "<p>Resources expose data; prompts are templates; tools execute actions. Naming and descriptions feed model routing quality.</p>",
    ),
    _ol(
        [
            "Implement one resource URI pattern; fetch via client.",
            "Register a tool with rich description + JSON schema.",
            "Add a prompt template with variables; render from host.",
            "Test model’s ability to pick correct tool among three.",
            "Version schemas when breaking changes occur.",
        ]
    ),
)
_add(
    67,
    _inner(
        "<p>Custom Python MCP servers often use FastMCP or official SDK. Package as CLI entrypoints; pin dependencies for reproducibility.</p>",
    ),
    _ol(
        [
            "Scaffold a server exposing two tools (read-only).",
            "Add unit tests mocking transport.",
            "Dockerfile optional: non-root user, read-only FS where possible.",
            "Publish README with install + config snippet.",
            "Peer review tool descriptions for ambiguity.",
        ]
    ),
)
_add(
    68,
    _inner(
        "<p>Integrations (S3, Stripe, Postgres) mean secrets, idempotency, and least privilege IAM. Never pass raw credentials through the model; server holds keys.</p>",
    ),
    _ol(
        [
            "Design IAM policy for S3 read-only prefix.",
            "Sketch Stripe flow with idempotency keys on writes.",
            "Use parameterized SQL only against Postgres tool.",
            "Log request metadata without card or PII payloads.",
            "Tabletop abuse: refund fraud prompt scenario.",
        ]
    ),
)
_add(
    69,
    _inner(
        "<p>Claude Desktop + MCP is the fastest way to feel the protocol. JSON config, absolute paths, and env vars are the usual friction points.</p>",
    ),
    _ol(
        [
            "Install Claude Desktop; locate MCP config file for your OS.",
            "Add one community server with narrow permissions.",
            "Restart; validate tools appear and run a harmless call.",
            "Snapshot working config (redacted) for teammates.",
            "Write troubleshooting FAQ from errors you actually saw.",
        ]
    ),
)

# P9 — A2A (70–74)
_add(
    70,
    _inner(
        "<p>Google’s Agent2Agent (A2A) protocol focuses on discoverable agents, task messages, and artifacts — complementary to MCP’s tool/resource model. Study how remote agents authenticate and negotiate capabilities.</p>",
    ),
    _ol(
        [
            "Read A2A intro materials; contrast goals with MCP in one paragraph.",
            "List actors: client, remote agent, registry (if used).",
            "Sketch sequence diagram for a task submission and artifact return.",
            "Identify transport and auth questions unanswered by skimming docs.",
            "Note version skew risks between agent implementations.",
        ]
    ),
)
_add(
    71,
    _inner(
        "<p>Agent cards advertise skills, endpoints, and trust metadata — similar in spirit to OpenAPI for services. Accurate cards reduce unsafe trial-and-error discovery.</p>",
    ),
    _ol(
        [
            "Draft a JSON agent card for a fake internal agent (no real URLs with secrets).",
            "Validate the card against examples from the spec repo.",
            "Peer review: can another teammate integrate without asking you?",
            "Add authentication section: mTLS vs bearer — justify choice.",
            "Version the card; document breaking change policy.",
        ]
    ),
)
_add(
    72,
    _inner(
        "<p>Task delegation passes structured work items between agents; artifacts carry results (files, JSON, structured reports). Idempotency and correlation IDs matter across hops.</p>",
    ),
    _ol(
        [
            "Define task schema fields you would require (id, deadline, inputs).",
            "Simulate two-agent handoff with mocked HTTP; log correlation IDs.",
            "Handle partial failure: who retries, who compensates?",
            "Store artifacts in object storage vs inline JSON — decide per size.",
            "Write SLO for end-to-end task latency.",
        ]
    ),
)
_add(
    73,
    _inner(
        "<p>Distributed execution spans containers or regions; combine A2A messages with orchestrators like LangGraph for local state while remote specialists handle subsets.</p>",
    ),
    _ol(
        [
            "Docker-compose two dummy agent services; send ping tasks.",
            "Introduce network partition; observe timeout behaviour.",
            "Centralise structured logs from both agents.",
            "Scale one agent replica; ensure task routing stays safe.",
            "Document blast radius if one agent is compromised.",
        ]
    ),
)
_add(
    74,
    _inner(
        "<p>MCP excels at equipping a host with tools/resources; A2A excels at multi-agent tasking across trust boundaries. Many systems use both — draw boundaries deliberately.</p>",
    ),
    _narrative_steps(
        "Draw a single architecture diagram placing MCP servers, your orchestrator, and A2A peers. "
        "Write a decision table: five criteria (latency, trust, UI surface, discoverability, state) × which protocol wins. "
        "Present a two-minute verbal summary to a peer and capture their questions as follow-ups."
    ),
)

# P10 — Unified systems (75–81)
_add(
    75,
    _inner(
        "<p>Orchestrators coordinate subgraphs, retries, and human approvals. Patterns include supervisor, handoff, and parallel fan-out — each trades complexity vs observability.</p>",
    ),
    _ol(
        [
            "Implement supervisor routing three specialist stubs.",
            "Add pause/resume for human approval on high-risk branch.",
            "Export metrics: tasks started, succeeded, failed.",
            "Compare orchestrator code size vs prompts-only baseline.",
            "Document rollback story for partially applied side effects.",
        ]
    ),
)
_add(
    76,
    _inner(
        "<p>Three-tier memory: hot session (Redis), warm structured (Postgres), cold semantic (vector). mem0 and similar libraries abstract policies but you still own PII and TTL law.</p>",
    ),
    _ol(
        [
            "Map one product’s memory to the three tiers with example keys.",
            "Define eviction when user deletes account (right to erasure).",
            "Prototype Redis TTL for session; Postgres row for preferences.",
            "Query vector tier with metadata filter by user_id.",
            "Estimate monthly cost at 10k MAU for your sketch.",
        ]
    ),
)
_add(
    77,
    _inner(
        "<p>Agent identity ties to machine IDs, SPIFFE/SPIRE concepts, or vendor features like Teleport Machine ID — goal is cryptographic proof of which workload spoke.</p>",
    ),
    _ol(
        [
            "Read high-level zero-trust agent identity blog/docs.",
            "List three attacks weak identity enables (spoof, replay).",
            "Sketch rotation for agent credentials (short-lived certs).",
            "Map identity to audit logs for tool calls.",
            "Tabletop: stolen agent credential response.",
        ]
    ),
)
_add(
    78,
    _inner(
        "<p>Observability triad: structured logs, traces, metrics. LLM apps add prompt/response spans, token counters, and evaluator scores — scrub PII before export.</p>",
    ),
    _ol(
        [
            "Emit JSON logs with trace_id on one multi-step run.",
            "View trace in LangSmith or Jaeger tutorial.",
            "Add three RED metrics definitions for your API.",
            "Test log sampling under load.",
            "Document retention aligned to compliance policy.",
        ]
    ),
)
_add(
    79,
    _inner(
        "<p>Guardrails span input classifiers, output validators, topic allowlists, and NeMo-style policy YAML. Combine deterministic checks with model-based judges sparingly (cost).</p>",
    ),
    _ol(
        [
            "Implement regex + length guard on user input.",
            "Add LLM moderation or policy call on flagged subset only.",
            "Unit-test guard with adversarial prompts (synthetic).",
            "Measure latency impact of each layer.",
            "Define escalation path when guards disagree.",
        ]
    ),
)
_add(
    80,
    _inner(
        "<p>The nine-layer stack is a reference lens: models, tools, memory, identity, observability, orchestration, data, security, UX — not a literal product diagram. Use it to gap-analyze proposals.</p>",
    ),
    _narrative_steps(
        "Redraw the nine layers for one client scenario (e.g. internal copilot vs external support bot). "
        "Highlight three layers that are immature in their design and one concrete improvement per layer. "
        "No install steps — completion is the annotated diagram plus a short narrative in your portfolio notes."
    ),
)
_add(
    81,
    _inner(
        "<p>RBAC for agents binds roles to tool permissions and data scopes. Cryptographic identity ties policy enforcement to workloads, not just API keys in env vars.</p>",
    ),
    _ol(
        [
            "Write RBAC matrix: roles × tools × data classes.",
            "Map Auth0/Clerk-style JWT claims to agent permissions.",
            "Test deny path when role lacks a tool.",
            "Integrate short-lived identity document for agent pod.",
            "Review OWASP authorization cheat sheet; note two gaps you will close.",
        ]
    ),
)

# P11 — Fine-tuning (82–86)
_add(
    82,
    _inner(
        "<p>Fine-tuning adapts a pretrained model to style, format, or domain with smaller curated datasets. Prefer prompting + RAG first; tune when you need consistent behaviour cheaper at inference than giant prompts.</p>",
    ),
    _ol(
        [
            "List go/no-go criteria: when tuning beats prompt/RAG for your use case.",
            "Sketch data card: source, license, PII scrubbing method.",
            "Run a toy HF Trainer or API fine-tune on public data only.",
            "Evaluate before/after on ten held-out prompts with a rubric.",
            "Document rollback: how to revert to base model serving.",
        ]
    ),
)
_add(
    83,
    _inner(
        "<p>LoRA/QLoRA train low-rank adapters while freezing most weights — feasible on consumer GPUs with bitsandbytes quant. Watch for catastrophic forgetting on edge tasks.</p>",
    ),
    _ol(
        [
            "Read PEFT LoRA guide; note rank and alpha defaults.",
            "Configure one QLoRA training job on a tiny dataset.",
            "Compare adapter-only checkpoint size vs full weights.",
            "Merge adapters vs load at runtime — decide for deployment.",
            "Run qualitative eval on domain jargon the base model mishandled.",
        ]
    ),
)
_add(
    84,
    _inner(
        "<p>PEFT umbrella covers LoRA, prefix tuning, adapters. Pick method based on framework support and serving constraints (some hosts only merge LoRA).</p>",
    ),
    _ol(
        [
            "Tabulate three PEFT methods with memory and inference trade-offs.",
            "Implement one non-LoRA PEFt method tutorial if hardware allows.",
            "Export config YAML used for reproducibility.",
            "Version training code + data hash in experiment log.",
            "Identify failure: overfitting on tiny data — show metric.",
        ]
    ),
)
_add(
    85,
    _inner(
        "<p>Data curation beats raw scale: dedupe, toxicity filters, format normalization, and human review for high-stakes labels. Argilla/Label Studio structure feedback loops.</p>",
    ),
    _ol(
        [
            "Ingest 100 rows; profile duplicates and label imbalance.",
            "Define annotation guidelines for one task; run 20 double-labels.",
            "Compute inter-annotator agreement roughly.",
            "Export JSONL for training; scrub PII with regex + manual spot check.",
            "Write data versioning plan (DVC or simple manifest).",
        ]
    ),
)
_add(
    86,
    _inner(
        "<p>Domain adaptation evaluation uses task metrics (ROUGE, BERTScore) plus human eval for tone. lm-evaluation-harness standardises many benchmarks — know limits of automatic scores.</p>",
    ),
    _narrative_steps(
        "Pick one optional evaluation harness tutorial; run on a public task; log scores and cost. "
        "Write a critique: where automatic metrics misalign with business quality. "
        "If GPU access is limited, document the exact commands you would run in cloud and stop after planning — still mark complete with written eval plan."
    ),
)

# P12 — Vibe coding (87–94)
_add(
    87,
    _inner(
        "<p>Vibe coding means steering AI assistants with intent while you review diffs, tests, and security. The toolchain spans Claude Code, Cursor, Copilot — each differs in rules, memory, and IDE integration.</p>",
    ),
    _ol(
        [
            "List your non-negotiables before accepting AI-generated patches (tests, types, secrets).",
            "Try one feature end-to-end with heavy AI assistance; capture diff review notes.",
            "Measure time saved vs bugs introduced (honest retro).",
            "Define branch protection + CI checks that AI cannot bypass.",
            "Teach a teammate your prompt patterns for refactors.",
        ]
    ),
)
_add(
    88,
    _inner(
        "<p>Claude Code CLI uses project context files (CLAUDE.md), skills, and hooks to standardise behaviour across sessions — treat it like onboarding docs for a junior dev.</p>",
    ),
    _ol(
        [
            "Install Claude Code per vendor docs; create CLAUDE.md with stack + commands.",
            "Add repo map: directories, owners, test entrypoints.",
            "Run one guided task: fix lint + add test using the tool.",
            "Document which files the tool may edit vs forbid.",
            "Snapshot lessons learned in team wiki (redacted).",
        ]
    ),
)
_add(
    89,
    _inner(
        "<p>Hooks intercept tool lifecycle events; skills package repeatable workflows. Together they reduce drift between developers using the same repo.</p>",
    ),
    _ol(
        [
            "Configure one hook (pre-tool or post-edit) with safe logging only.",
            "Author one skill file for a repetitive task (e.g. migration checklist).",
            "Share skill with peer; gather usability feedback.",
            "Version skills in git; review changes via PR.",
            "List hook failure modes and fallbacks if hook crashes.",
        ]
    ),
)
_add(
    90,
    _inner(
        "<p>Four-layer mental model: project memory (CLAUDE.md), skills, hooks, subagents/specialists. Align layers so instructions do not contradict.</p>",
    ),
    _narrative_steps(
        "Produce a single-page diagram of the four layers for your main repo. "
        "Highlight one contradiction you resolved between CLAUDE.md and a skill, and how you fixed it. "
        "Completion = diagram + short write-up; no extra install beyond your existing Claude Code setup."
    ),
)
_add(
    91,
    _inner(
        "<p>Agentic project structure separates prompts, tools, evals, and runtime config. Scaffold early so AI assistants do not sprawl files randomly.</p>",
    ),
    _ol(
        [
            "Create directories: prompts/, tools/, eval/, config/.",
            "Add README explaining boundaries.",
            "Move one messy script into proper module + tests.",
            "Add pre-commit for format + lint.",
            "Have another human navigate the tree without help — time them.",
        ]
    ),
)
_add(
    92,
    _inner(
        "<p>Cursor is an AI-native IDE: rules files, codebase indexing, and inline edits. Learn to scope context windows deliberately to reduce wrong-file edits.</p>",
    ),
    _ol(
        [
            "Author .cursor/rules or project rules per docs.",
            "Use @file and @folder references intentionally in prompts.",
            "Disable overly broad context for a sensitive subfolder.",
            "Run tests after each AI edit batch; note flaky failures.",
            "Compare Cursor workflow vs plain VS Code + Copilot for one bugfix.",
        ]
    ),
)
_add(
    93,
    _inner(
        "<p>GitHub Copilot spans editor, CLI, and PR suggestions. Policies in org settings govern which models and repos participate — align with compliance.</p>",
    ),
    _ol(
        [
            "Enable Copilot for a sandbox repo; complete three small tasks.",
            "Try Copilot CLI for a refactor; review diff carefully.",
            "Check org policy on code suggestions for internal repos.",
            "Log one unsafe suggestion you rejected and why.",
            "Pair with tests-first workflow; measure coverage delta.",
        ]
    ),
)
_add(
    94,
    _inner(
        "<p>Lovable and Gamma accelerate UI and slide generation from prompts. Outputs still need brand, accessibility, and content review before client-facing use.</p>",
    ),
    _ol(
        [
            "Generate one landing page draft; check a11y basics (contrast, headings).",
            "Export or hand off to code repo; diff against handcrafted baseline.",
            "List three limitations (layout control, data binding, SEO).",
            "Run content fact-check on generated copy.",
            "Decide when you would ban no-code for regulated clients.",
        ]
    ),
)

# P13 — Automation (95–99)
_add(
    95,
    _inner(
        "<p>n8n is fair-code workflow automation with self-host option. Nodes connect triggers, HTTP, databases, and AI steps — version flows as JSON in git when possible.</p>",
    ),
    _ol(
        [
            "Run n8n via Docker; create admin user.",
            "Build webhook → function → HTTP request flow.",
            "Add error workflow or retry policy.",
            "Export workflow JSON to git.",
            "Secrets: use credential store; never hardcode in nodes.",
        ]
    ),
)
_add(
    96,
    _inner(
        "<p>Make.com (Integromat) uses scenarios, modules, and data stores — great for SaaS glue. Understand operation billing and rate limits per plan.</p>",
    ),
    _ol(
        [
            "Create scenario with two modules + router.",
            "Map data mapping between modules explicitly.",
            "Test error path with invalid payload.",
            "Estimate monthly operations for expected volume.",
            "Document when you would migrate scenario to code (n8n/FastAPI).",
        ]
    ),
)
_add(
    97,
    _inner(
        "<p>Zapier targets business users with Zaps and multi-step paths. Enterprise features include SAML and admin controls — evaluate before automating sensitive data.</p>",
    ),
    _ol(
        [
            "Build a Zap with filter + formatter steps.",
            "Test delay and throttle behaviour.",
            "Review audit logs if available on your tier.",
            "Compare Zapier vs Make pricing for same workload sketch.",
            "List data residency questions for EU clients.",
        ]
    ),
)
_add(
    98,
    _inner(
        "<p>DAGs express dependencies; event triggers react to webhooks, queues, or schedules. Mixing LangGraph with external schedulers is common in hybrid systems.</p>",
    ),
    _ol(
        [
            "Draw DAG for nightly ETL + morning LLM summary job.",
            "Implement one cron + one event trigger in n8n or Airflow tutorial.",
            "Define idempotency keys for downstream writes.",
            "Handle backlog: what if LLM step slows down?",
            "Alerting: PagerDuty/webhook on DAG failure.",
        ]
    ),
)
_add(
    99,
    _inner(
        "<p>Conditional logic and guardrails in automation prevent runaway AI calls — caps on tokens, approvals on writes, and circuit breakers on error rates.</p>",
    ),
    _ol(
        [
            "Add branch on HTTP status in a flow.",
            "Cap OpenAI node max tokens and concurrency.",
            "Insert human approval email/Slack before payment action (mock).",
            "Simulate 5xx storm; verify breaker stops spam.",
            "Document rollback for partially executed scenario.",
        ]
    ),
)

# P14 — Production AI (100–106)
_add(
    100,
    _inner(
        "<p>FastAPI gives typed routes, OpenAPI docs, and async I/O — a common shell for LLM backends. Pair with Pydantic models for request/response contracts.</p>",
    ),
    _ol(
        [
            "Scaffold app with /health and /v1/chat proxy route (mock LLM).",
            "Add dependency-injected settings from env.",
            "Write pytest with TestClient covering 200 + validation error.",
            "Add request ID middleware; log structured JSON.",
            "Dockerfile non-root; pin base image digest.",
        ]
    ),
)
_add(
    101,
    _inner(
        "<p>Streamlit and Gradio ship demos fast; they differ in layout models and auth story. Neither replaces hardened multi-tenant auth without extra work.</p>",
    ),
    _ol(
        [
            "Build Streamlit chat UI calling your FastAPI mock.",
            "Add Gradio variant with same backend.",
            "Compare session state handling.",
            "Host locally with HTTPS tunnel (e.g. cloudflared) for demo only.",
            "List production gaps: auth, rate limits, logging.",
        ]
    ),
)
_add(
    102,
    _inner(
        "<p>Serverless (Lambda, Vercel, Modal) scales to zero but has cold starts and payload limits. Modal suits GPU jobs; Lambda suits thin orchestration.</p>",
    ),
    _ol(
        [
            "Deploy hello function to one serverless platform.",
            "Measure cold start p95 with simple load test.",
            "Set env vars + secrets via platform mechanism.",
            "Define max payload and timeout appropriate for LLM proxy.",
            "Cost estimate for 1M invocations/month at your memory setting.",
        ]
    ),
)
_add(
    103,
    _inner(
        "<p>Docker packages dependencies reproducibly; multi-stage builds shrink images. For AI images, watch CUDA base sizes and layer caching for model weights.</p>",
    ),
    _ol(
        [
            "Write Dockerfile for FastAPI app; run locally.",
            "Add docker-compose with depends_on + healthcheck.",
            "Use .dockerignore to skip models and secrets.",
            "Scan image with trivy or docker scout; patch criticals.",
            "Document promote path: dev → staging tags.",
        ]
    ),
)
_add(
    104,
    _inner(
        "<p>Kubernetes schedules GPU workloads, autoscaling, and config maps — operational overhead is real. Helm charts help but require cluster expertise.</p>",
    ),
    _ol(
        [
            "Read pod/resource requests vs limits for GPU pods.",
            "Sketch Deployment + Service + Ingress for your API.",
            "Plan config via ConfigMap vs Secret for keys.",
            "Understand HPA signals beyond CPU (custom metrics).",
            "Write when you would stay on VMs vs k8s for a client MVP.",
        ]
    ),
)
_add(
    105,
    _inner(
        "<p>Managed vector hosting offloads replicas, backups, and upgrades. Still define namespaces/tenants and backup RPO for customer indexes.</p>",
    ),
    _ol(
        [
            "Create serverless index; upsert test vectors.",
            "Test failover/read replica behaviour from docs.",
            "Estimate monthly $ for 1M vectors at your dimension.",
            "Define restore drill quarterly.",
            "Map IAM roles for ingest vs query workloads.",
        ]
    ),
)
_add(
    106,
    _inner(
        "<p>Agent hosting platforms (Replit, Modal, Fly.io) differ in GPU access, sleep policies, and outbound network. Pick based on workload wake latency and compliance.</p>",
    ),
    _ol(
        [
            "Deploy stub agent HTTP service to one platform.",
            "Measure cold start and keep-warm trade-offs.",
            "Configure secrets and environment promotion.",
            "Test outbound allowlist if required by security.",
            "Document egress data paths for privacy review.",
        ]
    ),
)

# P15 — Monitoring & eval (107–112)
_add(
    107,
    _inner(
        "<p>RAGAS and similar frameworks score faithfulness, answer relevance, and context precision — useful for regression suites, not perfect truth.</p>",
    ),
    _ol(
        [
            "Install RAGAS; run quickstart on synthetic QA pairs.",
            "Log metric distributions across five prompts.",
            "Identify one metric that misfires; explain why.",
            "Wire metrics export to CSV or W&B.",
            "Define pass threshold for CI gating.",
        ]
    ),
)
_add(
    108,
    _inner(
        "<p>Human-in-the-loop feedback (Argilla, LangSmith datasets) closes the gap between automatic scores and user satisfaction — design lightweight rubrics.</p>",
    ),
    _ol(
        [
            "Create 20-row eval set with binary thumbs up/down reason codes.",
            "Run blind comparison two model versions; aggregate preference.",
            "Ensure annotators see identical prompts (counter bias).",
            "Export labeled set for fine-tune or prompt iteration.",
            "Document inter-rater drift over time.",
        ]
    ),
)
_add(
    109,
    _inner(
        "<p>LangSmith traces show LLM spans, tool calls, and retries — essential for debugging non-deterministic failures in staging.</p>",
    ),
    _ol(
        [
            "Enable tracing on one chain; reproduce a bug twice.",
            "Filter traces by tags and latency.",
            "Share trace link internally with redaction checklist.",
            "Add evaluators on a dataset run.",
            "Set retention and access controls per environment.",
        ]
    ),
)
_add(
    110,
    _inner(
        "<p>OpenTelemetry standardises traces/metrics/logs export to Jaeger, Grafana, etc. Auto-instrument HTTP clients/servers first.</p>",
    ),
    _ol(
        [
            "Add OTel SDK to FastAPI service.",
            "Export traces to local Jaeger or Grafana stack.",
            "Create span around LLM HTTP call with attributes (model, not content).",
            "Add metric counter for tool errors.",
            "Verify sampling rate under load test.",
        ]
    ),
)
_add(
    111,
    _inner(
        "<p>Auto-evaluation loops run nightly evals, open PRs when regressions detected, or gate deploys — beware feedback loops where the judge model drifts.</p>",
    ),
    _ol(
        [
            "Design nightly job: sample prod queries → judge → dashboard.",
            "Choose judge model separate from production model.",
            "Add human spot-check percentage.",
            "Define rollback trigger thresholds.",
            "Document ethical limits on using user data in eval.",
        ]
    ),
)
_add(
    112,
    _inner(
        "<p>Prometheus scrapes metrics; Grafana dashboards visualize SLOs. LLM-specific panels might track tokens, latency, error codes, and judge scores.</p>",
    ),
    _narrative_steps(
        "Stand up or follow a tutorial stack with Prometheus + Grafana; import a starter dashboard; "
        "add one custom panel for LLM proxy latency p95. If you cannot run Docker locally, complete the module with a written dashboard spec and PromQL queries you would use."
    ),
)

# P16 — Security & governance (113–118)
_add(
    113,
    _inner(
        "<p>Prompt injection attempts to override system instructions via untrusted content — defenses include privilege separation, tool allowlists, and output policies.</p>",
    ),
    _ol(
        [
            "Reproduce a benign injection in a sandbox prompt.",
            "Move secrets and policies to system messages the user cannot edit.",
            "Add delimiter markers for untrusted document sections.",
            "Test Rebuff/regex guard if applicable.",
            "Write incident runbook if injection leads to data leak.",
        ]
    ),
)
_add(
    114,
    _inner(
        "<p>API keys belong in vaults (Vault, cloud secret managers) with rotation, audit, and least privilege paths. Never log secret values.</p>",
    ),
    _ol(
        [
            "Store one secret in Vault or cloud SM; read from app at boot.",
            "Rotate key; verify zero-downtime reload strategy.",
            "grep/scan repo for accidental keys (gitleaks).",
            "Define break-glass access procedure.",
            "Document quarterly rotation calendar.",
        ]
    ),
)
_add(
    115,
    _inner(
        "<p>User authentication (Auth0, Clerk) pairs with FastAPI OAuth2/JWT validation. Map identities to tenant IDs before RAG retrieval.</p>",
    ),
    _ol(
        [
            "Integrate OIDC login on a demo app.",
            "Enforce RBAC on one API route.",
            "Test token expiry and refresh behaviour.",
            "Log auth failures without leaking emails in public logs.",
            "Threat-model stolen refresh token.",
        ]
    ),
)
_add(
    116,
    _inner(
        "<p>Output filtering blocks PII leaks, toxic content, or policy violations — combine provider moderation APIs with local regex for formats.</p>",
    ),
    _ol(
        [
            "Call moderation API on five synthetic outputs.",
            "Add local redact for credit-card-like patterns.",
            "Define fallback message when content blocked.",
            "Measure added latency.",
            "Human review queue for borderline cases.",
        ]
    ),
)
_add(
    117,
    _inner(
        "<p>Red teaming uses tools like PyRIT/garak plus manual creativity to find jailbreaks and data exfil paths — schedule before major launches.</p>",
    ),
    _ol(
        [
            "Run garak or PyRIT quick scan on a test model endpoint.",
            "Document five findings with severity and repro steps.",
            "Track fixes in issue tracker with retest dates.",
            "Invite non-author to attempt jailbreak (fresh eyes).",
            "Define sign-off criteria for GA.",
        ]
    ),
)
_add(
    118,
    _inner(
        "<p>Privacy, alignment, and compliance intersect: DPIAs, AI Act risk tiers, logging minimisation, and vendor DPAs. Legal review beats guesswork.</p>",
    ),
    _narrative_steps(
        "Draft a one-page DPIA outline for a hypothetical AI feature: purpose, data categories, retention, automated decision impact, mitigations. "
        "Link each mitigation to modules you completed (RAG, auth, logging). No separate numbered lab — peer-review the outline and iterate once."
    ),
)

# P17 — Consultant (119–124)
_add(
    119,
    _inner(
        "<p>AI strategy workshops align business outcomes, data readiness, and risk appetite. Architecture diagrams should separate hype from feasible 90-day milestones.</p>",
    ),
    _ol(
        [
            "Facilitate mock discovery: interview notes → problem tree.",
            "Draft current vs target architecture (as-is / to-be).",
            "Prioritise use cases by value × feasibility matrix.",
            "Identify data blockers early (access, quality, legal).",
            "Present executive summary in five slides without jargon walls.",
        ]
    ),
)
_add(
    120,
    _inner(
        "<p>The twelve-skills framing maps technical depth (RAG, agents) to consulting skills (storytelling, pricing, change management). Self-assess honestly quarterly.</p>",
    ),
    _narrative_steps(
        "Score yourself 1–5 on twelve skills (define the twelve from your framework notes). "
        "Pick the lowest two; tie each to two specific modules in this tracker to restudy. "
        "Write a 90-day improvement plan — completion is the scored matrix plus plan, not a software install."
    ),
)
_add(
    121,
    _inner(
        "<p>Cost optimisation blends model routing, caching, prompt compression, and batching. Translate token math into monthly invoices stakeholders understand.</p>",
    ),
    _ol(
        [
            "Build spreadsheet: models × RPM × tokens × price.",
            "Simulate 30% traffic shift to smaller model; note quality guardrails.",
            "Evaluate prompt caching where providers support it.",
            "Add observability cost tags per feature flag.",
            "Present one slide CFO-friendly summary.",
        ]
    ),
)
_add(
    122,
    _inner(
        "<p>Enterprise playbooks cover governance, landing zones, MLOps, and support models — adapt public cloud adoption frameworks to GenAI specifics.</p>",
    ),
    _ol(
        [
            "Read a cloud adoption framework chapter; map to AI workstreams.",
            "Define RACI for data science, security, platform, legal.",
            "Draft pilot exit criteria (accuracy, latency, incidents).",
            "Plan handover from pilot to BAU operations.",
            "Identify vendor lock-in risks and mitigations.",
        ]
    ),
)
_add(
    123,
    _inner(
        "<p>Positioning and pricing tie outcomes to fees: value-based where possible, time-and-materials for discovery, retainers for advisory. Document assumptions explicitly.</p>",
    ),
    _ol(
        [
            "Write positioning statement for one niche (one sentence).",
            "Model three pricing scenarios with risk buffers.",
            "Create SOW outline: scope, exclusions, acceptance tests.",
            "Role-play negotiation objection on timeline.",
            "Define payment milestones tied to deliverables.",
        ]
    ),
)
_add(
    124,
    _inner(
        "<p>Stakeholder demos pair crisp narrative with working UI (Streamlit/Gradio/Gamma). Rehearse timing, backup offline slides, and Q&A on failure modes.</p>",
    ),
    _ol(
        [
            "Build five-minute demo script with click path.",
            "Record dry run; trim to timebox.",
            "Prepare three anticipated questions with evidence-backed answers.",
            "Add live failure demo (graceful) to show resilience.",
            "Collect feedback form; iterate once.",
        ]
    ),
)

# P18 — Capstones (125–127)
_add(
    125,
    _inner(
        "<p>Capstone 1: outbound voice or call experience using LangGraph orchestration, Twilio (or similar) telephony, and FastAPI webhooks — focus on state machine for call flows and PCI-adjacent caution.</p>",
    ),
    _ol(
        [
            "Define user story: who is called, when, and with what consent.",
            "Sketch call state machine (ringing, in-progress, escalate).",
            "Prototype webhook → LLM → TwiML response in dev environment.",
            "Add logging without recording sensitive audio in clear text.",
            "Document compliance checklist (consent, opt-out, retention).",
        ]
    ),
)
_add(
    126,
    _inner(
        "<p>Capstone 2: payment risk analyst blends RAG over policy docs, structured rules, and human escalation — emphasise audit trails and non-hallucinated citations.</p>",
    ),
    _ol(
        [
            "Ingest policy corpuses with metadata (version, jurisdiction).",
            "Force citation snippets in model answers; validate existence.",
            "Implement risk score + threshold routing to human review.",
            "Add eval set of historical cases (synthetic if needed).",
            "Threat-model data leakage between tenants.",
        ]
    ),
)
_add(
    127,
    _inner(
        "<p>Capstone 3: local Perplexity-style search combines SearXNG (or similar) results with local Ollama generation — optimise snippet stuffing and source display.</p>",
    ),
    _ol(
        [
            "Run SearXNG or alternative metasearch locally or docker.",
            "Pipe top snippets to Ollama with strict citation format.",
            "Build Streamlit UI with query + sources list.",
            "Handle search timeout and empty results gracefully.",
            "Compare answer quality with/without snippets on five questions.",
        ]
    ),
)

# P19 — Certifications (128–133)
_add(
    128,
    _inner(
        "<p>Vendor certifications structure how enterprises buy and govern AI. They complement — not replace — shipping agents, RAG systems, and the hands-on modules in this tracker.</p>",
        "<p><strong>Generative AI Leader</strong> is Google Cloud’s business- and product-level credential: gen-AI concepts, Gemini and Vertex AI services, responsible use, and adoption strategy — ideal if you brief stakeholders or shape roadmaps.</p>",
        "<p><strong>Professional ML Engineer</strong> remains the depth path for practitioners: Vertex AI pipelines, evaluation, RAG-style patterns, and production operations. Pair the Leader guide with PMLE labs when you also build.</p>",
        "<ul><li>Map exam domains to modules you finished (prompting, APIs, RAG, monitoring, security).</li><li>Complete the official Skills Boost path for Generative AI Leader, then add Vertex AI hands-on labs.</li></ul>",
    ),
    _steps_cert("Google Cloud Generative AI Leader + Vertex AI"),
)
_add(
    129,
    _inner(
        "<p><strong>AWS Certified AI Practitioner (AIF-C01)</strong> targets AI literacy on AWS: fundamentals of ML and generative AI, foundation models, responsible AI, and governance — aligned with product and engineering roles that touch Bedrock and agents.</p>",
        "<p>Study Bedrock, Agents, and IAM guardrails alongside this tracker’s API and security modules; scenario questions often mirror how you scope access, logging, and safe use of third-party models.</p>",
        "<p>For deeper ML engineering later, consider AWS’s advanced ML specialty as a separate milestone — it is not required to validate strong generative-AI solution skills.</p>",
    ),
    _steps_cert("AWS Certified AI Practitioner (AIF-C01)"),
)
_add(
    130,
    _inner(
        "<p>NVIDIA’s <strong>Generative AI LLM</strong> credentials (Associate NCA-GENL and Professional NCP-GENL) focus on LLM application design, prompting, data preparation, RAG-style workflows, deployment, evaluation, and responsible AI — closer to shipping assistants than to classical tabular ML.</p>",
        "<p>DLI workshops on RAG agents, deployment, and performance complement this phase; use them to connect local inference modules (Ollama, vLLM) with production GPU serving stories.</p>",
    ),
    _steps_cert("NVIDIA Generative AI LLM (NCA-GENL / NCP-GENL)"),
)
_add(
    131,
    _inner(
        "<p>The <strong>Azure AI Engineer (AI-102)</strong> exam emphasises Azure OpenAI, knowledge retrieval (including AI Search), content safety, and identity patterns you see in enterprise copilots and line-of-business agents.</p>",
        "<p>Cross-reference your LangChain, RAG, and governance modules: implementation choices on Azure mirror the same concerns (grounding, PII, auditability).</p>",
    ),
    _steps_cert("Microsoft Azure AI Engineer (AI-102)"),
)
_add(
    132,
    _inner(
        "<p>IBM’s <strong>watsonx</strong> and <strong>Generative AI Engineering</strong> professional programs stress enterprise Gen AI patterns, tooling, and governance rather than notebook-only classical ML.</p>",
        "<p>Names and weights change — confirm the live curriculum and any exam blueprint before locking a date.</p>",
    ),
    _steps_cert("IBM watsonx / Generative AI Engineering"),
)
_add(
    133,
    _inner(
        "<p>Hugging Face is the hub for open models, datasets, and the ecosystem around <strong>Transformers</strong>. The <strong>LLM</strong> and <strong>Agents</strong> courses map directly to modules on fine-tuning, tool use, and open-weight deployment.</p>",
        "<p>Treat course certificates and skill badges as structured learning milestones; the practical proof remains repos and demos you ship with the rest of this curriculum.</p>",
    ),
    _steps_cert("Hugging Face LLM & Agents learning paths"),
)


def build_learn_html(module_num: int, title: str, tools: str, priority: str, phase_code: str) -> str:
    inner = L_INNER[module_num]
    return _wrap(module_num, phase_code, title, tools, priority, inner)


def build_steps_html(module_num: int, *_unused: str) -> str:
    """Signature accepts title/tools/priority/phase for callers; only module_num is used."""
    return S_STEPS[module_num]


# Sanity: every module 1..133 registered
assert len(L_INNER) == 133 and len(S_STEPS) == 133
assert set(L_INNER.keys()) == set(range(1, 134))
