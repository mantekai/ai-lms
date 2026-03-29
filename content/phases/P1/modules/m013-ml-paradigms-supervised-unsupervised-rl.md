---
journey_id: '1.7'
module_num: 13
phase_code: P1
title: 'ML Paradigms: Supervised, Unsupervised, RL'
tools: 'scikit-learn, OpenAI Gym'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 1.7 — ML Paradigms: Supervised, Unsupervised, RL

**1.7 — ML Paradigms: Supervised, Unsupervised, RL** [Core] | Tools: `scikit-learn, OpenAI Gym`
- Learn: OverviewModule 13 (P1) — ML Paradigms: Supervised, Unsupervised, RL. Tools focus: scikit-learn, OpenAI Gym. Core path — prioritize in your sprint.Supervised learning fits labeled pairs; unsupervised structure learns without per-example labels; RL optimizes policies via rewards. Generative models (including LLMs) are often pretrained with self-supervised next-token objectives.Place LLM fine-tuning and RLHF in this map so you can explain trade-offs to non-specialists.
- Practice: For each paradigm, write one real-world example (not toy XOR) relevant to business data.Run a minimal sklearn supervised example; note fit/predict vs generative “generate” APIs.Explain why RLHF is related to RL but not the same as classic game-playing RL.List where unsupervised embeddings appear in your RAG or search roadmap.Create a comparison table: data needs, evaluation, and typical risk for e
- Code: `# Module 13 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 13, "topic": "ML Paradigms: Supervised, Unsupervi`
