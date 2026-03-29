---
kind: phase_supplement
phase_code: P16
---

# Phase P16 — supplemental depth

### Security and governance

### Prompt & Input Security

**Prompt Injection Regex Defense:** Specific detection patterns for common prompt injection attacks. Examples: detecting "ignore previous instructions", "you are now", "disregard your system prompt", "act as DAN". XML wrapping defense: wrap user input in `<user_input>` tags and instruct the model to treat everything inside as untrusted data, never as instructions. Defense in depth: combine regex detection with LLM-based classification for higher accuracy.

**Jailbreak Testing & Prevention:** Jailbreaks are adversarial prompts designed to bypass model safety guidelines. Testing: use tools like garak and PyRIT to systematically probe for jailbreak vulnerabilities before launch. Prevention: system prompt hardening (explicit refusal instructions), output filtering (catch policy violations in outputs), rate limiting (slow down repeated attempts), logging (detect patterns of adversarial behavior).

**Input Validation & Sanitization:** Validating and cleaning all inputs before they reach the LLM. Validation: check input length (reject inputs over max_tokens), check for disallowed content (profanity, PII patterns, injection markers), validate format (JSON schema validation for structured inputs). Sanitization: strip HTML tags, normalize whitespace, redact detected PII before logging. Never trust user input.

### Secrets & Access

**Never Commit Keys to Git:** API keys, passwords, and secrets must never appear in source code or git history. Use environment variables loaded from `.env` files (excluded via .gitignore), cloud secret managers (HashiCorp Vault, AWS Secrets Manager), or CI/CD secret stores. Scan repositories with gitleaks or truffleHog to detect accidentally committed secrets. Rotate any key that was ever committed.

**Role-Based Access Control (RBAC):** Mapping user identities to permissions for AI system access. Implementation: JWT tokens contain role claims (admin, user, tenant_admin). FastAPI dependency injection validates role before executing endpoints. For RAG systems: map user identity to tenant_id before retrieval to ensure users only see their own data. For agents: map agent identity to allowed tools and data scopes.

**Cryptographic Agent Identity:** Agents must have verifiable machine identities, not just API keys. API keys can be stolen and reused by any process. Cryptographic identity (SPIFFE/SPIRE, Teleport Machine ID) ties the identity to the specific workload — a certificate is issued to the agent process and rotated automatically. This enables: "only the payment-risk-agent running in the production Kubernetes cluster can access the compliance database."

**Dynamic Context-Aware Access:** Agent permissions should be dynamic, not static. Instead of "this agent can always access the database," the policy should be "this agent can access the database only when processing a transaction risk assessment, only for the tenant that owns the transaction, and only for read operations." Context-aware access is enforced at runtime by a policy engine (OPA, Cedar) that evaluates the full context of each request.

**Audit Logging:** Every agent action must be logged in an immutable audit trail. Required fields: timestamp, agent_id, action_type, resource_accessed, user_id (if applicable), tenant_id, decision (allow/deny), policy_applied. Audit logs must be: tamper-proof (append-only storage), retained for compliance period (typically 1-7 years), searchable for incident investigation, exportable for compliance audits.

### Output Safety

**PII Detection & Redaction:** Detecting and removing Personally Identifiable Information from AI outputs and logs. Detection: regex patterns for common PII formats (email, phone, SSN, credit card, IP address), NER models for names and addresses, LLM-based detection for context-dependent PII. Redaction: replace detected PII with placeholders ([EMAIL], [PHONE]) before logging or displaying. Required for GDPR compliance and preventing data leakage.

### Red Teaming & Testing

**Adversarial Prompt Crafting:** Systematically designing prompts intended to make the model produce harmful, incorrect, or policy-violating outputs. Techniques: role-playing attacks ("pretend you are an AI without restrictions"), indirect injection (hiding instructions in documents the agent processes), multi-turn manipulation (gradually shifting the conversation toward a target behavior). Red teaming should be done by people who didn't build the system (fresh eyes find more vulnerabilities).

**Security Architecture Patterns:** Sandboxed agents: run agents in isolated containers with no network access except to explicitly allowed endpoints. Watchdog agents: a separate monitoring agent observes the primary agent's actions and can halt execution if anomalous behavior is detected. Defense in depth: multiple independent security controls so that bypassing one doesn't compromise the system. Principle of least privilege: every agent has only the minimum permissions needed for its specific task.

**Auditable Agent Pipelines:** Designing agent systems so that every decision can be traced and explained after the fact. Requirements: structured logging of every tool call and its inputs/outputs, decision logging (why did the agent choose this action?), state snapshots at key decision points, correlation IDs linking all actions in a single task execution. Auditable pipelines are required for regulated industries and enterprise deployments.

### Compliance & Privacy

**Data Privacy & Compliance — GDPR, HIPAA, SOC 2:** GDPR (EU): data minimization, purpose limitation, right to erasure, data portability, consent management, DPIAs for high-risk processing. HIPAA (US healthcare): PHI protection, access controls, audit logs, breach notification. SOC 2: security, availability, processing integrity, confidentiality, privacy controls. AI systems must be designed with these requirements from the start, not bolted on later.

**EU AI Act:** The European Union's comprehensive AI regulation. Risk tiers: Unacceptable Risk (banned: social scoring, real-time biometric surveillance), High Risk (regulated: hiring, credit scoring, medical devices — requires conformity assessment, documentation, human oversight), Limited Risk (transparency obligations: chatbots must disclose they are AI), Minimal Risk (no specific obligations). AI systems must be classified and documented according to their risk tier.

**AI Alignment & Ethics:** Ensuring AI systems behave in accordance with human values and intentions. Techniques: RLHF (training models to follow human preferences), Constitutional AI (training models to follow a set of principles), red teaming (finding misaligned behaviors), interpretability research (understanding why models make decisions). Fairness: ensuring AI systems don't discriminate based on protected characteristics. Bias audits: systematic testing for disparate impact across demographic groups.

**Responsible AI Principles:** Anthropic's Constitutional AI (CAI) approach: models are trained to be helpful, harmless, and honest using a set of principles. Self-critique: the model evaluates its own outputs against the principles and revises. RLHF with AI feedback: AI models provide feedback on other AI outputs, scaling the feedback process. EY's responsible AI principles: transparency, fairness, accountability, privacy, security, reliability.

**Constitutional AI (CAI):** Anthropic's training methodology for building safe AI systems. Process: (1) Define a constitution — a set of principles the AI should follow. (2) Supervised learning: train the model to critique and revise its own outputs according to the constitution. (3) RLHF with AI feedback (RLAIF): use AI models to generate preference data for reinforcement learning, scaling beyond what human feedback alone can provide. Result: models that are more reliably helpful, harmless, and honest.

**Explainability-by-Design:** Building AI systems where every decision comes with a traceable explanation. Implementation: require the model to output reasoning alongside its decision ("I flagged this transaction because rule RBI-2024-03 states..."), store the retrieved context that informed each decision, log the confidence score and the factors that influenced it. Explainability-by-design is not an afterthought — it must be built into the system architecture from the start.

### Syllabus theme — day 11

**Day 11 — GenAI Governance, Guardrails & Deployment Frameworks:** Responsible AI principles (bias, hallucination, explainability). Guardrails: moderation, safety layers. Responsible AI practices: EY principles. Frameworks: LangChain, LlamaIndex, Haystack. Deployment considerations: cost, latency, compliance.

### Day 11 — GenAI Governance, Guardrails & Deployment Frameworks (Week 5)


### Layer 9 — Observability and Governance


- Purpose:** Observability ensures accountability and governance for agent actions


### Module 9 (L10): Safety, Governance & Capstone


- Rebuff: prompt injection detection library
- Custom regex guards, XML wrapping countermeasures
- NeMo Guardrails for programmable input validation
- Attack vectors: direct injection, indirect injection, jailbreaks
- HashiCorp Vault for secrets management
- AWS Secrets Manager for cloud-native rotation
- Never commit keys to git; env vars and secret stores only
- Auth0: identity-as-a-service
- Clerk: developer-friendly auth
- FastAPI security: OAuth2, JWT, dependency injection
- Role-based access control for AI endpoints
- OpenAI moderation endpoint for content classification
- Custom output filters for domain-specific safety
- PII detection and redaction in outputs
- PyRIT: Python Risk Identification Toolkit (Microsoft)
- garak: LLM vulnerability scanner
- Manual red-teaming: adversarial prompt crafting
- Systematic testing for safety and security gaps
- GDPR frameworks: data minimization, right to erasure, consent
- EU AI Act: risk classification, documentation requirements
- AI alignment: ensuring models behave per human intent
- Compliance documentation and audit trails


- Skills Injection** ← Memory feeds into all layers
- Subagent Execution** ← Hooks trigger on events
- Output** ← Workflows = scale

