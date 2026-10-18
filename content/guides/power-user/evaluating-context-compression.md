---
id: guides/power-user/evaluating-context-compression
title: "Evaluating Context Compression"
status: published
summary: "Summary of Factory Research’s evaluation of context compression strategies for long-running AI agent sessions."
parent: guides/power-user/index
tags: [guides, context-compression, summarization, agents, memory, token-efficiency, evaluation]
relations: [relates_to=jp/guides/power-user/evaluating-context-compression]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Evaluating Context Compression</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Summary of Factory Research’s evaluation of context compression strategies for long-running AI agent sessions.</p>


This page summarizes Factory Research’s post: **[Evaluating Context Compression for AI Agents](https://factory.ai/news/evaluating-compression)** (Dec 16, 2025).



<Aside kind="info">
For the full methodology, charts, and examples, read the original post linked above.
</Aside>



---

## TL;DR {#tldr}

- Long-running agent sessions can exceed any model’s context window, so some form of **context compression** is required.
- The key metric isn’t *tokens per request*; it’s **tokens per task** (because missing details force costly re-fetching and rework).
- In Factory’s evaluation, **structured summarization** retained more “continue-the-task” information than OpenAI’s `/responses/compact` and Anthropic’s SDK compression, at similar compression rates.

---

## Why context compression matters {#why-context-compression-matters}

As agent sessions stretch into hundreds/thousands of turns, the full transcript can reach **millions of tokens**. If an agent loses critical state (e.g., the exact endpoint, file paths changed, or the current next step), it often:

- re-reads files it already read
- repeats debugging dead ends
- forgets what changed and where

That costs more time and tokens than the compression saved.

---

## How Factory evaluated “context quality” {#how-factory-evaluated-context-quality}

Instead of using summary similarity metrics (e.g., ROUGE), Factory used a **probe-based evaluation**:

1. Take real, long-running production sessions.
2. Compress the earlier portion.
3. Ask probes that require remembering specific, task-relevant details from the truncated history.
4. Grade the answers for functional usefulness.

### Probe types {#probe-types}

- **Recall**: factual retention (e.g., “What was the original error?”)
- **Artifact**: file tracking (e.g., “Which files did we modify and how?”)
- **Continuation**: task planning (e.g., “What should we do next?”)
- **Decision**: reasoning chain (e.g., “What did we decide and why?”)

### Scoring dimensions {#scoring-dimensions}

Responses were scored (0–5) by an LLM judge (**GPT-5.2**) across:

- Accuracy
- Context awareness
- Artifact trail
- Completeness
- Continuity
- Instruction following

The judge is blinded to which compression method produced the response.

---

## Compression approaches compared {#compression-approaches-compared}

| Approach      | What it produces                                                                                                                                                                                                                                      | Key trade-off                                                                                                      |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Factory**   | A **structured, persistent summary** with explicit sections (intent, file modifications, decisions, next steps). Updates by summarizing only the newly-truncated span and **merging** into the existing summary (“anchored iterative summarization”). | Slightly larger summaries than the most aggressive compression, but better retention of task-critical details.     |
| **OpenAI**    | `/responses/compact`: an **opaque** compressed representation optimized for reconstruction fidelity.                                                                                                                                                  | Highest compression, but low interpretability (you can’t inspect what was preserved).                              |
| **Anthropic** | Claude SDK built-in compression: detailed structured summaries (often 7–12k chars), regenerated on each compression.                                                                                                                                  | High-quality summaries, but regenerating the whole summary each time can cause drift across repeated compressions. |

---

## Results (high-level) {#results-high-level}

Factory reports evaluating **36,000+ messages** from production sessions across tasks like PR review, bug fixes, feature implementation, and refactoring.

### Overall scores (0–5) {#overall-scores-05}

| Method    | Overall  | Accuracy | Context  | Artifact | Completeness | Continuity | Instruction |
| --------- | --------: | --------: | --------: | --------: | ------------: | ----------: | -----------: |
| Factory   | **3.70** | **4.04** | **4.01** | **2.45** | **4.44**     | **3.80**   | **4.99**    |
| Anthropic | 3.44     | 3.74     | 3.56     | 2.33     | 4.37         | 3.67       | 4.95        |
| OpenAI    | 3.35     | 3.43     | 3.64     | 2.19     | 4.37         | 3.77       | 4.92        |

### Compression ratio vs. quality {#compression-ratio-vs-quality}

The post notes similar compression rates across methods:

- OpenAI: **99.3%** token removal
- Anthropic: **98.7%** token removal
- Factory: **98.6%** token removal

Factory retained ~0.7 percentage points more tokens than OpenAI (kept more context), and scored **+0.35** higher on overall quality.

---

## What Factory says it learned {#what-factory-says-it-learned}

- **Structure matters**: forcing explicit sections (files/decisions/next steps) reduces the chance that critical details “silently disappear” over time.
- **Compression ratio is a misleading target**: aggressive compression can “save tokens” but lose details that cause expensive rework; optimize for **tokens per task**.
- **Artifact tracking is still hard**: all methods scored low on tracking which files were created/modified/examined (Factory’s best was **2.45/5**), suggesting this may need dedicated state tracking beyond summarization.
- **Probe-based evaluation is closer to agent reality** than text similarity metrics, because it tests whether work can continue effectively.

---

## Related docs {#related-docs}

- [[guides/power-user/memory-management|Memory and Context Management]]
- [[guides/power-user/token-efficiency|Token Efficiency Strategies]]
