<!--
  Open source: input/opensource.csv + PRD additions. Manish.AI
-->

# Open-source contribution targets

## Primary list (`input/opensource.csv`)

| Icon | Title | Org | Difficulty | Tags | Link |
|------|-------|-----|------------|------|------|
| 🤗 | Hugging Face smol-course | HuggingFace | Beginner → Intermediate | Python; PyTorch | [github.com/huggingface/smol-course](https://github.com/huggingface/smol-course) |
| 🔗 | LangGraph | LangChain | Intermediate | Python; TS | [github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) |
| 🦙 | Ollama | Ollama | Beginner-friendly | Go | [github.com/ollama/ollama](https://github.com/ollama/ollama) |
| 🔌 | MCP Servers | Model Context Protocol | Intermediate → Advanced | Python; TypeScript | [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| 🚀 | Dify | Community | Intermediate | Python; Vue | [github.com/langgenius/dify](https://github.com/langgenius/dify) |

## Extended suggestions (from the source PRD)

The source PRD adds contribution guidance for:

- **LangGraph** — docs, tools, StateGraph edge cases, HITL examples, tests.
- **Ollama** — Modelfiles, docs, integration examples (no Go required for doc PRs).
- **LlamaIndex** — connectors, query engines, RAG examples, VectorStore fixes.
- **CrewAI** — agent templates, tools, sequential/hierarchical demos.
- **AutoGen** — multi-agent patterns, provider integrations, enterprise deployment docs.

Narrative detail is merged into [`docs/PRD_AgentIQ.md`](../../docs/PRD_AgentIQ.md) under the phases that cover agents, RAG, and local inference (for example P0, P6, P7).

The PRD overview historically cited “8 OSS targets”; the **canonical CSV row count is 5**, with the remainder documented in the PRD-derived corpus above.
