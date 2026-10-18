---
id: guides/power-user/prompt-crafting
title: "Prompt Crafting for Different Models"
status: published
summary: "Model-specific prompting techniques to get better results from Claude, GPT, and other models."
parent: guides/power-user/index
tags: [guides, prompts, prompting, claude, gpt, opus, sonnet, techniques]
relations: [relates_to=jp/guides/power-user/prompt-crafting]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Prompt Crafting for Different Models</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Model-specific prompting techniques to get better results from Claude, GPT, and other models.</p>


Different AI models respond better to different prompting styles. This guide covers model-specific techniques and provides ready-to-use prompt refiner skills.



<Aside kind="info">
**Works everywhere:** These prompting techniques apply to both the Droid CLI and the [[web/getting-started/overview|Factory App]].
</Aside>



---

## Universal Prompting Principles {#universal-prompting-principles}

These principles work across all models:





<Details summary="Be specific about the outcome">
**Weak:** "Fix the bug in auth"

**Strong:** "Fix the login timeout bug where users get logged out after 5 minutes of inactivity. The session should persist for 24 hours."
</Details>


  
  

<Details summary="Provide context before instructions">
**Weak:** "Add error handling"

**Strong:** "This API endpoint handles payment processing. It currently crashes silently on network errors. Add error handling that logs the error, returns a user-friendly message, and triggers an alert."
</Details>


  
  

<Details summary="Include acceptance criteria">
**Weak:** "Make it faster"

**Strong:** "Optimize the search query. Success criteria: query time under 100ms for 10k records, no change to result accuracy, passes existing tests."
</Details>


  
  

<Details summary="Specify constraints explicitly">
**Weak:** "Refactor this code"

**Strong:** "Refactor this code to use the repository pattern. Constraints: don't change the public API, maintain backward compatibility, keep the same test coverage."
</Details>





---

## Claude Models (Opus, Sonnet, Haiku) {#claude-models-opus-sonnet-haiku}

Claude models excel with structured, explicit instructions and respond particularly well to certain formatting patterns.

### Key Techniques for Claude {#key-techniques-for-claude}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Use XML tags for structure</div>

Claude responds exceptionally well to XML-style tags for organizing complex prompts:

```
<context>
This is a React application using TypeScript and Zustand for state management.
The auth module handles user sessions and JWT tokens.
</context>

<task>
Add a "remember me" checkbox to the login form that extends session duration to 30 days.
</task>

<requirements>
- Store preference in localStorage
- Update JWT expiration accordingly
- Add unit tests for the new functionality
</requirements>
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Put examples in dedicated sections</div>

When you want specific output formats, show examples:

```
<example>
Input: "user not found"
Output: { code: "USER_NOT_FOUND", message: "The specified user does not exist", httpStatus: 404 }
</example>

Now handle these error cases following the same pattern:
- Invalid password
- Account locked
- Session expired
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Use thinking prompts for complex reasoning</div>

For complex decisions, ask Claude to think through options:

```
Before implementing, analyze:
1. What are the tradeoffs between approach A and B?
2. Which approach better fits our existing patterns?
3. What edge cases should we consider?

Then implement the better approach.
```

</div>

</div>





<Aside kind="tip">
Copy the prompt refiner skills below to `~/.factory/skills/` to use them. Learn more about skills in the [[cli/configuration/skills|Skills documentation]].
</Aside>



### Claude Prompt Refiner Skill {#claude-prompt-refiner-skill}

Create `~/.factory/skills/prompt-refiner-claude/SKILL.md`:

````markdown
---
name: prompt-refiner-claude
description: Refine prompts for Claude models (Opus, Sonnet, Haiku) using Anthropic's best practices. Use when preparing complex tasks for Claude.
---

# Claude Prompt Refiner

## When to Use
Invoke this skill when you have a task for Claude that:
- Involves multiple steps or files
- Requires specific output formatting
- Needs careful reasoning or analysis
- Would benefit from structured context

## Refinement Process

### 1. Analyze the Draft Prompt
Review the user's prompt for:
- [ ] Clear outcome definition
- [ ] Sufficient context
- [ ] Explicit constraints
- [ ] Success criteria

### 2. Apply Claude-Specific Patterns

**Structure with XML tags:**
- `<context>` - Background information, codebase state
- `<task>` - The specific action to take
- `<requirements>` - Must-have criteria
- `<constraints>` - Limitations and boundaries
- `<examples>` - Sample inputs/outputs if helpful

**Ordering matters:**
1. Context first (what exists)
2. Task second (what to do)
3. Requirements third (how to do it)
4. Examples last (clarifying edge cases)

### 3. Enhance for Reasoning
For complex tasks, add:
- "Think through the approach before implementing"
- "Consider these edge cases: ..."
- "Explain your reasoning for key decisions"

### 4. Output the Refined Prompt
Present the improved prompt with:
- Clear section headers
- XML tags where beneficial
- Specific, measurable criteria

## Example Transformation

**Before:**
"Add caching to the API"

**After:**
```
<context>
The /api/products endpoint currently queries the database on every request.
Average response time is 200ms. We use Redis for other caching in the app.
</context>

<task>
Add Redis caching to the /api/products endpoint to reduce database load.
</task>

<requirements>
- Cache TTL of 5 minutes
- Cache invalidation when products are updated
- Graceful fallback to database if Redis is unavailable
- Add cache hit/miss metrics logging
</requirements>

<constraints>
- Don't change the response format
- Must pass existing integration tests
- Use our existing Redis connection from src/lib/redis.ts
</constraints>
```
````

---

## GPT Models (GPT-5, GPT-5.1, Codex) {#gpt-models-gpt-5-gpt-51-codex}

GPT models excel with clear system-level context and benefit from explicit role framing.

### Key Techniques for GPT {#key-techniques-for-gpt}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Frame the role explicitly</div>

GPT models respond well to clear role definitions:

```
You are a senior TypeScript developer reviewing code for a production e-commerce platform.
Focus on: type safety, error handling, and performance.

Review this checkout flow implementation...
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Use numbered steps for procedures</div>

GPT follows numbered instructions reliably:

```
Complete these steps in order:
1. Read the current implementation in src/auth/
2. Identify all places where tokens are validated
3. Create a centralized token validation utility
4. Update all call sites to use the new utility
5. Add unit tests for the utility
6. Run the test suite and fix any failures
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Be explicit about output format</div>

Specify exactly what you want:

```
Return your analysis as a markdown document with these sections:
## Summary (2-3 sentences)
## Issues Found (bulleted list)
## Recommended Changes (numbered, in priority order)
## Code Examples (if applicable)
```

</div>

</div>



### GPT Prompt Refiner Skill {#gpt-prompt-refiner-skill}

Create `~/.factory/skills/prompt-refiner-gpt/SKILL.md`:

````markdown
---
name: prompt-refiner-gpt
description: Refine prompts for GPT models (GPT-5, GPT-5.1, Codex) using OpenAI's best practices. Use when preparing complex tasks for GPT.
---

# GPT Prompt Refiner

## When to Use
Invoke this skill when you have a task for GPT that:
- Requires a specific persona or expertise
- Involves procedural steps
- Needs structured output
- Benefits from explicit examples

## Refinement Process

### 1. Analyze the Draft Prompt
Review for:
- [ ] Clear role/persona definition
- [ ] Step-by-step breakdown (if procedural)
- [ ] Output format specification
- [ ] Concrete examples

### 2. Apply GPT-Specific Patterns

**Role framing:**
Start with "You are a [specific role] working on [specific context]..."

**Numbered procedures:**
Break complex tasks into numbered steps that build on each other.

**Output specification:**
Be explicit: "Return as JSON", "Format as markdown with headers", etc.

**Chain of thought:**
For reasoning tasks, add: "Think through this step by step."

### 3. Structure the Prompt

**Effective order for GPT:**
1. Role definition (who/what)
2. Context (background info)
3. Task (what to do)
4. Steps (how to do it, if procedural)
5. Output format (what to return)
6. Examples (optional clarification)

### 4. Output the Refined Prompt
Present with:
- Clear role statement
- Numbered steps where applicable
- Explicit output requirements

## Example Transformation

**Before:**
"Review this code for security issues"

**After:**
```
You are a senior security engineer conducting a security audit of a Node.js payment processing service.

Context: This service handles credit card transactions and communicates with Stripe's API. It runs in AWS ECS.

Task: Review the code in src/payments/ for security vulnerabilities.

Steps:
1. Check for proper input validation on all endpoints
2. Verify secrets are not hardcoded or logged
3. Review authentication and authorization logic
4. Check for SQL injection and XSS vulnerabilities
5. Verify proper error handling that doesn't leak sensitive info

Output format:
Return a security report in markdown with:
- **Critical**: Issues that must be fixed before deployment
- **High**: Significant risks that should be addressed soon
- **Medium**: Improvements to consider
- **Recommendations**: General security enhancements

For each issue, include:
- File and line number
- Description of the vulnerability
- Recommended fix with code example
```
````

---

## Gemini Models {#gemini-models}

Gemini models handle long context well and work effectively with structured reasoning.

### Key Techniques for Gemini {#key-techniques-for-gemini}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Leverage long context</div>

Gemini can handle extensive context—don't be afraid to include more background:

```
Here's the full module structure for context:
[include relevant files]

Based on these patterns, implement a new service that...
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Use reasoning levels effectively</div>

Gemini supports Low and High reasoning. Use High for:
  - Architecture decisions
  - Complex debugging
  - Multi-step planning

Use Low for:
  - Straightforward implementations
  - Code generation from specs
  - Routine refactoring

</div>

</div>



---

## Model Selection Strategy {#model-selection-strategy}

Match the model to the task:

| Task Type                   | Recommended Model           | Reasoning Level |
| --------------------------- | --------------------------- | --------------- |
| **Complex architecture**    | Opus 4.8 or Opus 4.7        | High-Max        |
| **Feature implementation**  | Sonnet 4.5 or GPT-5.1-Codex | Medium          |
| **Quick edits, formatting** | Haiku 4.5                   | Off/Low         |
| **Code review**             | GPT-5.1-Codex-Max           | High            |
| **Bulk automation**         | GLM-5 (Droid Core)          | None            |
| **Research/analysis**       | Gemini 3 Pro                | High            |

---

## Creating Your Own Prompt Refiner {#creating-your-own-prompt-refiner}

For team-specific needs, create a custom prompt refiner:

````markdown
---
name: prompt-refiner-team
description: Refine prompts using our team's conventions and project context.
---

# Team Prompt Refiner

## Our Conventions
- We use the repository pattern
- All services have interfaces defined first
- Tests use our custom test utilities from @/test-utils

## Checklist for Prompts
1. [ ] References relevant existing code
2. [ ] Specifies which layer (API, service, repository)
3. [ ] Mentions related tests to update
4. [ ] Includes acceptance criteria

## Template
```
Context: [What exists, what module/layer]
Task: [Specific action]
Patterns to follow: [Reference existing similar code]
Tests: [What tests to add/update]
Done when: [Acceptance criteria]
```
````

---

## Quick Reference Card {#quick-reference-card}

### Claude (Opus/Sonnet/Haiku) {#claude-opussonnethaiku}
- ✅ XML tags for structure
- ✅ Context before instructions
- ✅ Examples in dedicated sections
- ✅ "Think through..." for reasoning

### GPT (GPT-5/Codex) {#gpt-gpt-5codex}
- ✅ Role framing ("You are a...")
- ✅ Numbered step procedures
- ✅ Explicit output format
- ✅ "Step by step" for reasoning

### Gemini {#gemini}
- ✅ Extensive context inclusion
- ✅ Low/High reasoning levels
- ✅ Structured output requests

---

## Next Steps {#next-steps}



<div class="factory-card-group">

<div class="factory-card">

**[[guides/power-user/setup-checklist|Setup Checklist]]**

Complete power user configuration

</div>


  

<div class="factory-card">

**[[guides/power-user/token-efficiency|Token Efficiency]]**

Reduce costs while maintaining quality

</div>

</div>
