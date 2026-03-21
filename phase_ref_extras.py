# Manish.AI — vetted supplemental links merged per phase (deduped with module-specific refs).
"""Extra reference tuples appended to every module in a phase for broader official depth."""

PHASE_REFERENCE_EXTRAS: dict[str, list[tuple[str, str]]] = {
    "P0": [
        ("Docker — get started", "https://docs.docker.com/get-started/"),
        ("Python — venv", "https://docs.python.org/3/library/venv.html"),
        ("NVIDIA — CUDA downloads", "https://developer.nvidia.com/cuda-downloads"),
        ("Homebrew (macOS)", "https://brew.sh/"),
    ],
    "P1": [
        ("Hugging Face — LLM course (full)", "https://huggingface.co/learn/llm-course"),
        ("3Blue1Brown — neural networks", "https://www.3blue1brown.com/topics/neural-networks"),
        ("Distill.pub", "https://distill.pub/"),
        ("Google — ML crash course", "https://developers.google.com/machine-learning/crash-course"),
    ],
    "P2": [
        ("OpenAI — cookbook (GitHub)", "https://github.com/openai/openai-cookbook"),
        ("Google Cloud — prompt design", "https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design"),
        ("Lilian Weng — LLM survey", "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/"),
        ("PromptingGuide.ai", "https://www.promptingguide.ai/"),
    ],
    "P3": [
        ("MDN — HTTP overview", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview"),
        ("OWASP — API security", "https://owasp.org/www-project-api-security/"),
        ("JSON Schema", "https://json-schema.org/"),
        ("OpenAPI specification", "https://swagger.io/specification/"),
    ],
    "P4": [
        ("HF — agents course", "https://huggingface.co/learn/agents-course"),
        ("Berkeley — RL book (Sutton & Barto)", "http://incompleteideas.net/book/the-book-2nd.html"),
        ("Microsoft — autonomous agents overview", "https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design"),
        ("ReAct paper", "https://arxiv.org/abs/2210.03629"),
    ],
    "P5": [
        ("Mozilla — HTTP caching", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching"),
        ("OWASP — SSRF", "https://owasp.org/www-community/attacks/Server_Side_Request_Forgery"),
        ("Python — pathlib", "https://docs.python.org/3/library/pathlib.html"),
        ("OWASP — secure coding", "https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/"),
    ],
    "P6": [
        ("Python — typing", "https://docs.python.org/3/library/typing.html"),
        ("PyPI", "https://pypi.org/"),
        ("GitHub — semantic versioning", "https://semver.org/"),
        ("12-factor app", "https://12factor.net/"),
    ],
    "P7": [
        ("Stanford IR book (intro)", "https://nlp.stanford.edu/IR-book/"),
        ("Elasticsearch — hybrid search concepts", "https://www.elastic.co/guide/en/elasticsearch/reference/current/hybrid-search.html"),
        ("Microsoft — RAG patterns", "https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide"),
        ("Anthropic — contextual retrieval", "https://www.anthropic.com/news/contextual-retrieval"),
    ],
    "P8": [
        ("Anthropic — MCP announcement", "https://www.anthropic.com/news/model-context-protocol"),
        ("JSON-RPC 2.0 spec", "https://www.jsonrpc.org/specification"),
        ("OWASP — LLM Top 10", "https://owasp.org/www-project-top-10-for-large-language-model-applications/"),
        ("CNCF — security landscape", "https://www.cncf.io/"),
    ],
    "P9": [
        ("Google Cloud — A2A blog", "https://cloud.google.com/blog/products/ai-machine-learning/a2a-a-new-era-of-agent-interoperability"),
        ("IETF — JSON Web Token", "https://datatracker.ietf.org/doc/html/rfc7519"),
        ("OWASP — API security top 10", "https://owasp.org/API-Security/editions/2023/en/0x11-t10/"),
        ("gRPC docs", "https://grpc.io/docs/"),
    ],
    "P10": [
        ("CNCF — OpenTelemetry", "https://opentelemetry.io/"),
        ("SRE — Google workbook", "https://sre.google/workbook/table-of-contents/"),
        ("NIST — cybersecurity framework", "https://www.nist.gov/cyberframework"),
        ("OWASP — ASVS", "https://owasp.org/www-project-application-security-verification-standard/"),
    ],
    "P11": [
        ("Hugging Face — datasets docs", "https://huggingface.co/docs/datasets/index"),
        ("Papers With Code — benchmarks", "https://paperswithcode.com/sota"),
        ("Google — responsible AI", "https://ai.google/responsibility/"),
        ("Weights & Biases — reports", "https://docs.wandb.ai/guides/reports"),
    ],
    "P12": [
        ("Git — book", "https://git-scm.com/book/en/v2"),
        ("GitHub — code review", "https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews"),
        ("pre-commit framework", "https://pre-commit.com/"),
        ("Conventional Commits", "https://www.conventionalcommits.org/"),
    ],
    "P13": [
        ("Zapier — automation basics", "https://help.zapier.com/hc/en-us/categories/200094917-Getting-Started-with-Zapier"),
        ("IFTTT (patterns)", "https://ifttt.com/explore"),
        ("Temporal — durable execution", "https://docs.temporal.io/"),
        ("AWS — event-driven architecture", "https://aws.amazon.com/event-driven-architecture/"),
    ],
    "P14": [
        ("Twelve-factor — logs", "https://12factor.net/logs"),
        ("Mozilla — CORS", "https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS"),
        ("Let's Encrypt", "https://letsencrypt.org/docs/"),
        ("OWASP — Docker security", "https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html"),
    ],
    "P15": [
        ("Google — SRE monitoring", "https://sre.google/sre-book/monitoring-distributed-systems/"),
        ("Prometheus — best practices", "https://prometheus.io/docs/practices/"),
        ("OpenTelemetry — traces", "https://opentelemetry.io/docs/concepts/signals/traces/"),
        ("Chaos engineering principles", "https://principlesofchaos.org/"),
    ],
    "P16": [
        ("NIST — AI RMF", "https://www.nist.gov/itl/ai-risk-management-framework"),
        ("ENISA — AI cybersecurity", "https://www.enisa.europa.eu/publications"),
        ("OWASP — cheat sheet series", "https://cheatsheetseries.owasp.org/"),
        ("CWE — top 25", "https://cwe.mitre.org/top25/"),
    ],
    "P17": [
        ("Harvard Law — negotiation overview", "https://www.pon.harvard.edu/tag/negotiation-skills/"),
        ("Wikipedia — business analysis", "https://en.wikipedia.org/wiki/Business_analysis"),
        ("Wikipedia — technology roadmap", "https://en.wikipedia.org/wiki/Technology_roadmap"),
        ("PMI — what is project management", "https://www.pmi.org/about/learn-about-pmi/what-is-project-management"),
    ],
    "P18": [
        ("Twilio — voice quickstarts", "https://www.twilio.com/docs/voice/quickstart"),
        ("OWASP — ASVS (for threat modelling)", "https://owasp.org/www-project-application-security-verification-standard/"),
        ("Stripe — testing", "https://docs.stripe.com/testing"),
        ("Postman — API platform", "https://learning.postman.com/docs/introduction/overview/"),
    ],
    "P19": [
        ("Google Cloud — certification catalog", "https://cloud.google.com/learn/certification"),
        ("AWS — Certified AI Practitioner", "https://aws.amazon.com/certification/certified-ai-practitioner/"),
        ("Coursera — professional certificates", "https://www.coursera.org/professional-certificates"),
        ("MIT OpenCourseWare — search", "https://ocw.mit.edu/search/?q=artificial+intelligence"),
        ("Pearson VUE — test taker", "https://home.pearsonvue.com/"),
        ("Credly — digital badges", "https://www.credly.com/"),
    ],
}
