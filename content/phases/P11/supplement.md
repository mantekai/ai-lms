---
kind: phase_supplement
phase_code: P11
---

# Phase P11 — supplemental depth

### Fine-tuning and optimization

### Fine-Tuning

**Hands-on Fine-Tuning — CLI and SDK Workflows:** OpenAI fine-tuning via CLI: `openai api fine_tuning.jobs.create -t training_file.jsonl -m gpt-3.5-turbo`. Hugging Face fine-tuning via Trainer API or SFTTrainer. Key steps: prepare JSONL dataset, upload to provider, launch job, monitor loss curves, evaluate on held-out set, deploy fine-tuned model. Always evaluate before and after fine-tuning to confirm improvement.

**JSON Output Fine-Tuning:** Fine-tuning a model specifically to produce consistent, valid JSON output for a given schema. Useful when structured output via prompting is unreliable. Training data: input prompts paired with perfect JSON outputs. Evaluation: JSON validity rate, schema compliance rate, field accuracy. Often more reliable than prompt-based structured output for complex schemas.

**Baseline Summarizer Fine-Tuning:** A common fine-tuning exercise: take a pretrained model and fine-tune it on domain-specific document-summary pairs. The fine-tuned model learns the organization's preferred summary style, length, and format. Evaluation: ROUGE scores vs baseline, human preference ratings. Demonstrates the full fine-tuning workflow from data prep to deployment.

### Data Preparation

**datasets Library:** Hugging Face's datasets library for loading, processing, and sharing datasets. Supports streaming for large datasets, built-in preprocessing functions, and integration with the Trainer API. Key operations: load_dataset, map (apply transformations), filter (remove examples), train_test_split, push_to_hub.

**Data Quality, Deduplication, Format Conversion:** High-quality training data beats raw scale. Deduplication: remove near-duplicate examples using MinHash or embedding similarity. Format conversion: normalize all examples to the same JSONL format with consistent field names. Quality filters: remove examples with toxic content, PII, or formatting errors. Inter-annotator agreement: measure consistency between human labelers.

**Preparing Datasets in JSON Format:** Fine-tuning datasets must be in JSONL format (one JSON object per line). For instruction fine-tuning: `{"messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}`. For completion fine-tuning: `{"prompt": "...", "completion": "..."}`. Validation: check all examples parse correctly, no empty fields, consistent schema.

**Processing Raw Data with LLMs:** Using LLMs to generate, clean, and augment training data. Applications: generating diverse question-answer pairs from documents, rewriting examples in different styles, identifying and removing low-quality examples, generating synthetic edge cases. Quality control: human review of a random sample (typically 5-10%) before using LLM-generated data for training.

### Evaluation

**BLEU (Bilingual Evaluation Understudy):** A metric for evaluating text generation quality by comparing n-gram overlap between generated text and reference text. Originally designed for machine translation. Range: 0-1 (higher is better). Limitations: doesn't capture semantic similarity, penalizes valid paraphrases. Used alongside ROUGE and BERTScore for comprehensive evaluation.

**Model Selection Trade-offs:** Choosing the right model involves balancing: Latency (response time), Cost (price per token), Accuracy (task performance), Context length (max input size), Domain specificity (general vs specialized), Availability (API uptime, rate limits). Decision framework: start with the cheapest model that meets quality requirements; upgrade only when quality is insufficient.

**GenAI Experimentation:** Systematic benchmarking of LLM capabilities. Process: define evaluation set (20+ diverse examples), run all candidate models, score outputs on defined metrics, create comparison table, track performance over time as models are updated. Tools: LangSmith for experiment tracking, custom eval scripts, W&B for visualization.

**Module 8 — Model Selection, Evaluation and Fine-Tuning:** Processing raw data with LLMs — preparing raw data for models, generating synthetic data, cleaning and preprocessing. Model selection trade-offs: latency, cost, accuracy, domain specificity. Knowledge Distillation: when to recommend lighter models for performance-sensitive environments. Quantization & Pruning: optimizing inference latency and model size. Fine-Tuning Models: Need for Parameter Efficient Fine-Tuning, Introduction to LoRA, QLoRA, Baseline summarizer, JSON output fine-tuning. Hands-on fine-tuning with Azure OpenAI CLI and SDK. RAG vs Fine-tuning decision framework. Preparing datasets in JSON format. Evaluating fine-tuned models with metrics: accuracy, F1-score, BLEU. Use-case decision trees for model and system choices.


### Syllabus theme — day 2

**Day 2 — MLOps:** Model Lifecycle — Development, Release, and Productionization. MLFlow: Evaluation Metrics, Model Logging, Registering, Experimentation, Tracking, Monitoring. Exercise: Install and run MLflow locally; train two models and log as separate experiments.

- Further training a pre-trained model on domain-specific data
- Cheaper than training from scratch; shifts style, format, or behavior
- When to fine-tune vs prompt engineering vs RAG decision framework
- LoRA: Low-Rank Adaptation — train small adapter matrices instead of full weights
- QLoRA: quantized base model + LoRA adapters for memory efficiency
- Tools: PEFT library, bitsandbytes for quantization
- PEFT library from Hugging Face
- Adapter methods: LoRA, prefix tuning, prompt tuning
- Integration with HF Transformers training loop
- datasets library for data loading and processing
- Argilla: annotation and labeling platform
- Label Studio: open-source data labeling
- ROUGE: recall-oriented understudy for gisting evaluation
- BERTScore: semantic similarity evaluation
- Eleuther LM Eval: standardized benchmark harness

