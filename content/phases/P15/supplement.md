---
kind: phase_supplement
phase_code: P15
---

# Phase P15 — supplemental depth

### Monitoring and evaluation

**Logging / Tracing:** Structured logging records every agent action with a consistent schema: timestamp, trace_id, agent_id, action_type, tool_name, input_summary (no PII), output_summary, latency_ms, token_count, cost_usd. Distributed tracing links all log entries from a single user request across multiple agents and services using a shared trace_id. Essential for debugging non-deterministic agent failures.

**Cost Observability:** Tracking and attributing LLM API costs at a granular level. Implementation: tag every API call with feature_flag, user_segment, agent_id, and module_id. Aggregate costs by tag in a dashboard. Set budget alerts (e.g., alert if daily cost exceeds $50). Identify the most expensive operations and optimize them first. Cost observability is required for sustainable production AI systems.

**Observability: Azure Monitor & Application Insights (Generic: Cloud Observability):** Cloud-native observability platforms that collect logs, metrics, and traces from deployed applications. Generic equivalents: Datadog, New Relic, Grafana Cloud. Key capabilities: distributed tracing across microservices, custom dashboards for AI-specific metrics (token usage, latency, error rates), alerting on SLO violations, cost attribution by service.

### Syllabus theme — day 10

**Day 10 — GenAI Experimentation:** Experimentation — Metrics Evaluation, Understanding Benchmarks, Understanding Model Capabilities. Tracking model performance. Logging outcomes and feedback loops. Exercise: Evaluate LLM responses using BLEU, ROUGE, cosine similarity; create benchmark table; simulate prompt refinement loop.

### Syllabus theme — day 18

**Day 18 — Monitoring & Governance:** Observability: tracing, logging, feedback loops. Governance: safety, guardrails, compliance. Exercise: Implement feedback loop and basic guardrails on agent.

- Evaluation Metrics: regression & classification metrics — MSE, MAE, Precision, R
- Exercise: Map AI applications to type of AI and evaluation metric with reasoning


- tests/** = both evaluation and unit tests


- RAGAS: RAG Assessment framework (faithfulness, relevance, context recall)
- TruLens: LLM app evaluation and feedback
- Custom eval metrics for domain-specific quality
- LangSmith annotation queues for human review
- Argilla: collaborative data annotation
- Feedback loops: collect → analyze → improve
- End-to-end tracing of LangChain/LangGraph runs
- Debugging failed chains, latency analysis
- Dataset management and evaluation runs
- Vendor-neutral observability framework
- Traces, metrics, logs for AI pipelines
- Jaeger for distributed trace visualization
- LLM-as-judge: using one model to evaluate another
- Custom eval chains for automated quality checks
- Continuous evaluation in production pipelines
- Prometheus: time-series metrics collection
- Grafana: dashboard visualization
- AI-specific metrics: token usage, latency percentiles, error rates


- Module 111: Auto-Evaluation Loops [Core] | Tools: LLM-as-judge, custom eval chai


- Evaluation Metrics depth** — MSE, MAE, Precision, Recall, ROC, AUC, F1 Score, RO

