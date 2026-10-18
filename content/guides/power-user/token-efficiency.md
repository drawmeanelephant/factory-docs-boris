---
id: guides/power-user/token-efficiency
title: "Token Efficiency Strategies"
status: published
summary: "Reduce token usage while maintaining quality through project setup, model selection, and workflow optimization."
parent: guides/power-user/index
tags: [guides, tokens, efficiency, cost, optimization, usage, pricing, performance]
relations: [relates_to=jp/guides/power-user/token-efficiency]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Token Efficiency Strategies</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Reduce token usage while maintaining quality through project setup, model selection, and workflow optimization.</p>


Token usage isn't just about cost—it's about feedback loop speed and context window limits. This guide shows you how to get more done with fewer tokens through project optimization, smart model selection, and workflow patterns.



<Aside kind="info">
**Using Factory App?** These strategies apply to both the Droid CLI and the [[web/getting-started/overview|Factory App]]. You can view your project's readiness score in the [[web/agent-readiness/dashboard|Agent Readiness Dashboard]].
</Aside>



---

## Understanding Token Usage {#understanding-token-usage}

Tokens are consumed in three main areas:

```
┌──────────────────────────────────────────────────────────┐
│                    Token Consumption                      │
├────────────────┬────────────────┬────────────────────────┤
│   Context      │   Tool Calls   │   Model Output         │
│   (Input)      │   (Overhead)   │   (Response)           │
├────────────────┼────────────────┼────────────────────────┤
│ • AGENTS.md    │ • Read files   │ • Explanations         │
│ • Memories     │ • Grep/search  │ • Generated code       │
│ • Conversation │ • Execute cmds │ • Analysis             │
│ • File content │ • Each retry   │ • Thinking tokens      │
└────────────────┴────────────────┴────────────────────────┘
```

**High token usage often means:**
- Too much exploration (unclear instructions)
- Multiple attempts (missing context or failing tests)
- Verbose output (no format constraints)

---

## Project Setup for Efficiency {#project-setup-for-efficiency}

The biggest token savings come from project configuration that prevents wasted cycles.

### 1. Fast, Reliable Tests {#1-fast-reliable-tests}



<Aside kind="warning">
Slow or flaky tests are the #1 cause of wasted tokens. Each retry costs a full response cycle.
</Aside>



| Test Characteristic | Impact on Tokens                                     |
| ------------------- | ---------------------------------------------------- |
| Fast tests (< 30s)  | Droid verifies changes immediately                   |
| Slow tests (> 2min) | Droid may skip verification or waste context waiting |
| Flaky tests         | False failures cause debugging cycles                |
| No tests            | Droid can't verify changes, more back-and-forth      |

**Action items:**
```markdown
## In your AGENTS.md

## Testing
- Run single file: `npm test -- path/to/file.test.ts`
- Run fast smoke tests: `npm test -- --testPathPattern=smoke`
- Full suite takes ~3 minutes, use `--bail` for early exit on failure
```

### 2. Linting and Type Checking {#2-linting-and-type-checking}

When Droid can catch errors immediately, it fixes them in the same turn instead of waiting for you to report them.

```markdown
## In your AGENTS.md

## Validation Commands
- Lint (auto-fix): `npm run lint:fix`
- Type check: `npm run typecheck`
- Full validation: `npm run validate` (lint + typecheck + test)

Always run `npm run lint:fix` after making changes.
```

### 3. Clear Project Structure {#3-clear-project-structure}

Document your file organization so Droid doesn't waste tokens exploring:

```markdown
## In your AGENTS.md

## Project Structure
- `src/components/` - React components (one per file)
- `src/hooks/` - Custom React hooks
- `src/services/` - API and business logic
- `src/types/` - TypeScript type definitions
- `tests/` - Test files mirror src/ structure

When adding a new component:
1. Create component in `src/components/ComponentName/`
2. Add index.ts for exports
3. Add ComponentName.test.tsx in same directory
```

---

## Agent Readiness Checklist {#agent-readiness-checklist}

The [[cli/features/readiness-report|Agent Readiness Report]] evaluates your project against criteria that directly impact token efficiency.

### High-Impact Criteria {#high-impact-criteria}

| Criterion                       | Token Impact | Why It Matters                                  |
| ------------------------------- | ------------ | ----------------------------------------------- |
| **Linter Configuration**        | 🟢 High       | Catches errors immediately, no debugging cycles |
| **Type Checker**                | 🟢 High       | Prevents runtime errors, clearer code           |
| **Unit Tests Runnable**         | 🟢 High       | Verification in same turn                       |
| **AGENTS.md**                   | 🟢 High       | Context upfront, less exploration               |
| **Build Command Documentation** | 🟡 Medium     | No guessing, fewer failed attempts              |
| **Dependencies Pinned**         | 🟡 Medium     | Reproducible builds                             |
| **Pre-commit Hooks**            | 🟡 Medium     | Automatic quality enforcement                   |

Run the readiness report to identify gaps:

```bash
droid
> /readiness-report
```

---

## Model Selection Strategy {#model-selection-strategy}

Different models have different cost multipliers and capabilities. Match the model to the task:

### Cost Multipliers {#cost-multipliers}

See [[models|Available Models]] for current model multipliers.

### Task-Based Model Selection {#task-based-model-selection}

```
Simple edit, formatting      → Haiku 4.5 (0.4×)
Implement feature from spec  → GPT-5.3-Codex (0.7×)
Debug complex issue          → Sonnet 4.5 (1.2×)
Architecture planning        → Opus 4.8 (2×) or Opus 4.7 (2×)
Bulk file processing         → Droid Core (MiniMax M2.7 at 0.12× or Kimi K2.6 at 0.4×)
```

### Reasoning Effort Impact {#reasoning-effort-impact}

Higher reasoning = more "thinking" tokens but often fewer retries.

| Reasoning | When to Use              | Token Trade-off                      |
| --------- | ------------------------ | ------------------------------------ |
| Off/None  | Simple, clear tasks      | Lowest per-turn, may need more turns |
| Low       | Standard implementation  | Good balance                         |
| Medium    | Complex logic, debugging | Higher per-turn, fewer retries       |
| High      | Architecture, analysis   | Highest per-turn, best first-attempt |

**Rule of thumb:** Use higher reasoning for tasks where a wrong first attempt would be expensive to fix.



<Aside kind="tip">
**Configure mixed models** to automatically use different models for planning vs implementation. See [[cli/configuration/mixed-models|Mixed Models]] for setup.
</Aside>



---

## Workflow Patterns for Efficiency {#workflow-patterns-for-efficiency}

### Pattern 1: Spec Mode for Complex Work {#pattern-1-spec-mode-for-complex-work}

Use [[cli/user-guides/specification-mode|Specification Mode]] (`Shift+Tab` or `/spec`) to plan before implementing.

**Without Spec Mode:**
```
Turn 1: Start implementing → wrong approach → wasted tokens
Turn 2: Undo and try different approach → more tokens
Turn 3: Finally get it right
Total: 3 turns of implementation tokens
```

**With Spec Mode:**
```
Turn 1: Plan with exploration → correct approach identified
Turn 2: Implement correctly
Total: 1 turn of planning + 1 turn of implementation
```



<Aside kind="tip">
Use Spec Mode (`Shift+Tab` or `/spec`) for any task that:
  - Touches more than 2 files
  - Requires understanding existing patterns
  - Has unclear requirements
  - Is security-sensitive
</Aside>



### Pattern 2: IDE Plugin for Context {#pattern-2-ide-plugin-for-context}

Without IDE plugin, Droid must read files to understand context:

```
Read file A → Read file B → Read file C → Understand context → Work
(4 tool calls before actual work)
```

With IDE plugin, context is immediate:

```
Work (IDE provides open files, errors, selection)
(0 extra tool calls for context)
```

### Pattern 3: Specific Over General {#pattern-3-specific-over-general}

**Expensive prompt:**
```
"Fix the bug in the auth module"
```
→ Droid reads multiple files to find the bug, explores different possibilities

**Efficient prompt:**
```
"Fix the timeout bug in src/auth/session.ts line 45 where the session expires after 5 minutes instead of 24 hours"
```
→ Droid goes directly to the issue

### Pattern 4: Batch Similar Work {#pattern-4-batch-similar-work}

**Expensive:**
```
Turn 1: "Add logging to userService"
Turn 2: "Add logging to orderService"
Turn 3: "Add logging to paymentService"
(3 turns, context rebuilt each time)
```

**Efficient:**
```
Turn 1: "Add structured logging to all services in src/services/. Use the pattern from src/lib/logger.ts. Services: user, order, payment."
(1 turn, pattern established once)
```

---

## Reducing Token Waste {#reducing-token-waste}

### Common Waste Patterns {#common-waste-patterns}

| Pattern                     | Cause                | Fix                    |
| --------------------------- | -------------------- | ---------------------- |
| Multiple exploration cycles | Unclear requirements | Be specific upfront    |
| Repeated file reads         | Missing IDE context  | Install IDE plugin     |
| Failed attempts             | No tests/linting     | Add validation tools   |
| Verbose explanations        | No format constraint | Ask for concise output |
| Wrong architecture          | Missing context      | Use Spec Mode          |

### Format Constraints {#format-constraints}

Ask for specific output formats to reduce verbosity:

```
"Add the feature. Return only the changed code, no explanations unless something is unclear."
```

```
"Review this code. Format: bullet list of issues only, no preamble."
```

```
"Debug this test failure. Show me the fix, then explain in 2-3 sentences."
```

---

## Monitoring Your Usage {#monitoring-your-usage}

### Check Current Session Cost {#check-current-session-cost}

```bash
droid
> /cost
```

This shows usage for the current session.

### Track Over Time {#track-over-time}

Review your usage patterns:

1. **After each session**, note the `/cost` output
2. **Identify expensive sessions**: What made them expensive?
3. **Refine approach**: More context? Different model? Better prompts?

### Usage Red Flags {#usage-red-flags}

Watch for these patterns:

- 🚩 **High read count**: Droid is exploring too much (add AGENTS.md context)
- 🚩 **Multiple grep/search calls**: Unclear what to look for (be more specific)
- 🚩 **Repeated similar edits**: Failed attempts (check tests/linting)
- 🚩 **Very long conversations**: Scope creep (break into smaller tasks)

---

## Quick Wins Checklist {#quick-wins-checklist}

Implement these for immediate token savings:

- [ ] **Install IDE plugin** - Eliminates context-gathering tool calls
- [ ] **Create AGENTS.md** - Droid knows build/test commands upfront
- [ ] **Configure linting** - Errors caught immediately
- [ ] **Fast test command** - Verification in same turn
- [ ] **Use Spec Mode** - Prevents expensive false starts
- [ ] **Be specific** - Reduces exploration cycles
- [ ] **Match model to task** - Don't use Opus for simple edits

---

## Token Budget Guidelines {#token-budget-guidelines}

Rough guidelines for common tasks:

| Task Type              | Typical Token Range | Notes                           |
| ---------------------- | ------------------- | ------------------------------- |
| Quick edit             | 5k-15k              | Simple, specific changes        |
| Feature implementation | 30k-80k             | With Spec Mode planning         |
| Complex debugging      | 50k-150k            | May need multiple attempts      |
| Architecture planning  | 20k-50k             | High-reasoning model            |
| Code review            | 30k-60k             | Depends on PR size              |
| Bulk refactoring       | 50k-200k            | Many files, use efficient model |

If you're significantly exceeding these ranges, review the waste patterns above.

---

## Summary: The Token-Efficient Workflow {#summary-the-token-efficient-workflow}

```
1. Set up your project
   └─ AGENTS.md with commands
   └─ Fast tests
   └─ Linting configured
   └─ IDE plugin installed

2. Start each task right
   └─ Use Spec Mode for complex work
   └─ Be specific about the goal
   └─ Reference existing patterns

3. Choose the right model
   └─ Simple → Haiku/Droid Core
   └─ Standard → Codex/Sonnet
   └─ Complex → Opus (with reasoning)

4. Monitor and adjust
   └─ Check /cost periodically
   └─ Identify expensive patterns
   └─ Refine your approach
```

---

## Next Steps {#next-steps}



<div class="factory-card-group">

<div class="factory-card">

**[[guides/power-user/setup-checklist|Setup Checklist]]**

Complete power user configuration

</div>


  

<div class="factory-card">

**[[cli/features/readiness-report|Readiness Report]]**

Evaluate your project's AI-readiness

</div>

</div>
