---
journey_id: '1.2'
module_num: 8
phase_code: P1
title: 'How LLMs Work: Transformers & Tokenization'
tools: 'Hugging Face, tiktoken'
priority: 'MUST DO'
source: content/curriculum/section-6-modules.md
---

# 1.2 — How LLMs Work: Transformers & Tokenization

**1.2 — How LLMs Work: Transformers & Tokenization** [Core] | Tools: `Hugging Face, tiktoken`
- Learn: OverviewModule 8 (P1) — How LLMs Work: Transformers & Tokenization. Tools focus: Hugging Face, tiktoken. Core path — prioritize in your sprint.Transformers use self-attention so every position can attend to every other position in parallel — the architectural basis of modern LLMs. Tokenization turns text into subword IDs; context length and cost follow from token counts.Connect Hugging Face ecosystem concepts (configs, tokenizers) to what you see in API billing. Optional: load a small tokenizer 
- Practice: Skim the Illustrated Transformer or HF docs summary; draw a one-page diagram: embedding → layers → logits.Run a tokenizer (HF or tiktoken) on three prompt shapes: code, bullet list, long paragraph.Compare token counts for the same meaning in verbose vs concise English.Note how special tokens (BOS/EOS/pad) appear in your encoder output.Write five bullets linking attention to long-context cost in pr
- Code: `# Module 8 — hands-on checkpoint
def deliverable() -> dict:
    """Return a tiny artifact proving you practiced this module."""
    return {"module": 8, "topic": "How LLMs Work: Transformers & Tokeniz`
