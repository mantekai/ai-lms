---
kind: phase_supplement
phase_code: P3
---

# Phase P3 — supplemental depth

### LLMs and provider APIs

### Providers

**Free API Stack:** Zero-cost API options for prototyping and learning:
- Groq: 14,400 requests/day, 300+ tokens/second, supports LLaMA and Mixtral
- Google AI Studio: 1M tokens/minute free tier, Gemini 2.5 Flash
- Mistral: 1 billion tokens/month free on la Plateforme
- OpenRouter: 30+ free models from multiple providers via single API
- Cerebras: Ultra-fast inference (1,000+ tokens/second) on CS-3 wafer-scale chips
Building a comparison matrix of these providers (latency, context length, tool support, rate limits) is a required exercise in Module 6 (P0).

### API Skills

**Rate Limiting & Backoff:** Production API usage requires handling 429 (rate limit) and 529 (overloaded) errors gracefully. Implementation: exponential backoff with jitter (random delay to prevent thundering herd). The tenacity library provides retry decorators. Never retry non-idempotent POST requests blindly. Log HTTP status codes and request IDs, never log payloads containing PII.

**Function Calling / Toolformer:** The mechanism by which LLMs emit structured tool invocation requests instead of plain text. Define tools as JSON schemas with name, description, and parameters. The model decides when to call a tool based on the description quality. Tight schemas (enums, required fields, clear descriptions) reduce hallucinated tool calls.

**Streaming Responses:** Instead of waiting for the full response, stream tokens as they are generated using server-sent events. Implementation: `client.messages.stream()` in Anthropic SDK, `stream=True` in OpenAI SDK. Dramatically improves perceived latency for chat interfaces. Required for production chatbot UIs.

**Batch API:** Send up to 10,000 requests in a single batch job. Results returned within 24 hours. Cost: 50% reduction vs real-time API. Use cases: bulk document processing, offline evaluation runs, large-scale data enrichment. Not suitable for real-time user-facing applications.

**Vision API:** Send images alongside text to multimodal models. Supported formats: JPEG, PNG, GIF, WebP. Max size: 5MB per image, up to 20 images per request (Claude). Use cases: document analysis, chart interpretation, screenshot debugging, product image analysis. Base64 encoding or URL references both supported.

### Multimodal AI

**Text + Image + Audio + Video Pipelines:** Cross-modal AI workflows that combine multiple input/output types. Example pipeline: audio transcription (Whisper) → text analysis (Claude) → image generation (DALL-E) → video synthesis (Pika). Each modality has different latency, cost, and quality characteristics. Designing multimodal pipelines requires understanding the constraints of each modality.

**GPT-4V, Gemini Multimodal, Pika, ElevenLabs:** GPT-4V: OpenAI's vision-capable model for image understanding. Gemini 1.5 Pro: Google's multimodal model supporting text, images, audio, and video in a 1M token context. Pika: AI video generation from text or image prompts. ElevenLabs: text-to-speech with voice cloning, used for agent voice escalation in Capstone 1.

**Computer Vision:** AI systems that interpret and understand visual information from images and videos. Applications: document OCR, product defect detection, medical imaging, security surveillance. Models: GPT-4V, Gemini Vision, Claude 3.5 Sonnet (vision). Relevant for building agents that can "see" and interpret visual data.

**AI Content Generation Tools:** Descript (video/audio editing with AI transcription and voice cloning), ElevenLabs (text-to-speech, voice cloning, audio generation), Synthesia (AI avatar video generation), HeyGen (personalized video at scale), OpusClip (AI video clipping and repurposing). These tools are part of the AI Tool Stacking skill set.

### Curriculum visual map — block C

### Image 3: Top 40 AI Terms (Exact Definitions from Image)

**Core AI Concepts:**
1. AGI (Artificial General Intelligence) — AI with human-like reasoning
2. AI Model — Trained system for tasks
3. Machine Learning (ML) — AI learning from data
4. Deep Learning — ML using deep neural networks
5. Supervised Learning — AI trained on labeled data
6. Unsupervised Learning — AI finding patterns in unlabeled data
7. Reinforcement Learning — AI learning via rewards/penalties

**AI Processes & Functions:**
8. Inference — AI generating responses from data
9. Context — Information AI retains for relevance
10. Explainability — Understanding AI decisions
11. Hallucination — AI generating false information
12. RAG (Retrieval-Augmented Generation) — AI combining search + generation
13. CoT (Chain of Thought) — AI reasoning step-by-step
14. Context Window — Memory limit for AI's inputs
15. Cost per Token — Processing cost of AI usage

**AI Ethics & Safety:**
16. AI Alignment — Ensuring AI follows human values
17. Training Data — Source quality shaping AI behavior
18. Bias — AI producing unfair outcomes
19. Privacy — Protecting user data in AI
20. Regulation — AI laws and compliance

**AI Model Development:**
21. Fine-tuning — Adapting a pre-trained model for a task
22. Prompt Engineering — Optimizing inputs for better outputs
23. Tokenization — Splitting text into processable units
24. Parameters — Internal values shaping AI behavior
25. Weights — Values in a neural network that adjust during training
26. Embedding — Numeric representation of data
27. Quantization — Reducing model size for efficiency
28. Training Data — Data AI learns from

**AI Tools & Infrastructure:**
29. GPU (Graphics Processing Unit) — Hardware for AI acceleration
30. TPU (Tensor Processing Unit) — Google's AI-specialized chip
31. Compute — Processing power for AI
32. Transformer — AI architecture for language models
33. MCP (Model Context Protocol) — Standard for AI data access
34. API (Application Programming Interface) — AI integration via external requests

**Specialized AI Applications:**
35. Computer Vision — AI interpreting images/videos
36. NLP (Natural Language Processing) — AI understanding/generating language
37. Chatbots — AI simulating human conversation
38. Generative AI — AI creating text, images, etc.
39. Vibe Coding — AI-assisted programming
40. AI Agent — AI autonomously performing tasks

### Image 4: MCP Explained — The Protocol Connecting AI to Everything

**Definition:** The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools.

**MCP Host contains:** Claude Desktop | IDE | AI Tools

**Connection Pattern:**
- MCP Host → MCP Client → MCP Protocol → MCP Server A → Amazon S3
- MCP Host → MCP Client → MCP Protocol → MCP Server B → Airbnb
- MCP Host → MCP Client → MCP Protocol → MCP Server C → Stripe

**Key Points:**
- MCP Server A connects to AWS S3 for file storage
- MCP Server B connects to an Airbnb server (booking/availability)
- MCP Server C connects to the Stripe server (payments)
- MCP Host includes tools like Claude Desktop, IDEs, and AI tools

**How MCP Works:** MCP Client ↔ Transport Layer ↔ MCP Server — bidirectional communication via Transport Layer

**5 Key Components of MCP:**
1. Secure File Access — Ensures data security when interacting with files
2. Sampling — Retrieves relevant data samples
3. Prompt — Enables AI-based querying and processing
4. Resources — Provides access to knowledge sources
5. Tools & Functions — Offers additional computational tools
