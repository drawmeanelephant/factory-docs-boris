---
id: guides/power-user/setup-checklist
title: "Power User Setup Checklist"
status: published
summary: "Complete checklist to configure Droid for maximum effectiveness with IDE integration, memory, skills, and automation."
parent: guides/power-user/index
tags: [guides, power-user, setup, checklist, configuration, optimization, productivity, best-practices]
relations: [relates_to=jp/guides/power-user/setup-checklist]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Power User Setup Checklist</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Complete checklist to configure Droid for maximum effectiveness with IDE integration, memory, skills, and automation.</p>


This checklist transforms a basic Droid installation into a fully optimized development environment. Each section builds on the previous one—complete them in order for best results.



<Aside kind="note">
Each section can be done independently if you prefer to spread it out.
</Aside>





<Aside kind="info">
**Using Factory App?** Most of this guide applies to both the Droid CLI and the [[web/getting-started/overview|Factory App]]. Where the experience differs, we've noted the Factory App-specific approach.
</Aside>



---

## Level 1: Essential Setup {#level-1-essential-setup}

These foundational items give you the biggest immediate impact.



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Install the Factory IDE Plugin</div>

The IDE plugin provides real-time context—open files, errors, selections—so Droid sees what you see.

**VSCode/Cursor:**
  1. Open Extensions (`Cmd+Shift+X`)
  2. Search "Factory"
  3. Install and reload

**Verify:** Run `droid` and check for "IDE connected" in the status bar.

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Create your AGENTS.md</div>

Create a basic [[cli/configuration/agents-md|AGENTS.md]] at your repository root:

```markdown
# Project Guidelines

## Build & Test
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint`

## Code Style
- Use TypeScript strict mode
- Prefer functional components in React
- Write tests for new features
```

Start minimal—you'll expand this as you work. See the [[cli/configuration/agents-md|AGENTS.md guide]] for more examples.

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Configure your default model</div>

Set your preferred model in settings:

**CLI:**
```bash
droid
> /settings
# Navigate to Model and select your default
```

**Factory App:** Use the model selector dropdown in the chat interface.

**Recommendation:** Start with Claude Opus 4.5 (default) for complex work, switch to Haiku 4.5 or GPT-5.1-Codex for routine tasks.

</div>

</div>





<Aside kind="tip">
**Checkpoint:** You should now have IDE integration, basic project context, and your preferred model configured.
</Aside>



---

## Level 2: Memory & Context {#level-2-memory-context}

Build persistent memory so Droid remembers your preferences across sessions.



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Create a memories file</div>

Create `~/.factory/memories.md` for personal preferences:

```markdown
# My Development Preferences

## Code Style
- I prefer arrow functions over function declarations
- I like early returns over nested conditionals
- I use 2-space indentation

## Testing
- I use React Testing Library, not Enzyme
- I prefer integration tests over unit tests for components
- Mock external APIs, not internal modules

## Past Decisions
- [2024-01] Chose Zustand over Redux for state management
- [2024-02] Using Tailwind CSS for styling
```

Update this file whenever you find yourself repeating instructions to Droid.

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Reference memories in AGENTS.md</div>

Add to your `AGENTS.md`:

```markdown
## Personal Preferences
Refer to `~/.factory/memories.md` for my coding preferences and past decisions.
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Create project-specific memories (optional)</div>

For team projects, create `.factory/memories.md`:

```markdown
# Project Memories

## Architecture Decisions
- We use the repository pattern for data access
- All API routes go through the /api/v1 prefix
- Feature flags are managed via LaunchDarkly

## Known Issues
- The auth service has a 5-second timeout issue (#123)
- Legacy users table uses snake_case columns
```

</div>

</div>





<Aside kind="tip">
**Checkpoint:** Droid now has access to your preferences and project history without you repeating them.
</Aside>





<Aside kind="tip">
**Want automated memory capture?** Set up a hook to automatically save memories when you say "remember this:". See [[guides/power-user/memory-management#automatic-memory-capture|Memory Management]] for setup instructions.
</Aside>



---

## Level 3: Rules & Conventions {#level-3-rules-conventions}

Organize your coding standards so Droid follows them consistently.



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Create a rules directory</div>

Create `.factory/rules/` in your project:

```
.factory/
└── rules/
    ├── typescript.md
    ├── testing.md
    └── security.md
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Add TypeScript rules</div>

Create `.factory/rules/typescript.md`:

```markdown
# TypeScript Conventions

## General
- Use `interface` for object types, `type` for unions/intersections
- Avoid `any` - use `unknown` with type guards instead
- Export types alongside their implementations

## React Components
- Use functional components with TypeScript FC type
- Props interfaces should be named `{ComponentName}Props`
- Use `React.ReactNode` for children, not `React.ReactChild`

## Imports
- Group imports: React, external libs, internal modules, types
- Use absolute imports from `@/` prefix
- Avoid barrel files (index.ts re-exports) for performance
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Add testing rules</div>

Create `.factory/rules/testing.md`:

```markdown
# Testing Conventions

## File Organization
- Test files live next to source: `Component.tsx` → `Component.test.tsx`
- Integration tests go in `__tests__/integration/`
- E2E tests go in `e2e/`

## Test Structure
- Use descriptive test names: "should [action] when [condition]"
- One assertion per test when possible
- Use `beforeEach` for common setup, not `beforeAll`

## Mocking
- Mock at the boundary (API calls, not internal functions)
- Use MSW for API mocking in integration tests
- Reset mocks in `afterEach`
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Reference rules in AGENTS.md</div>

Update your `AGENTS.md`:

```markdown
## Coding Standards
Follow the conventions documented in:
- `.factory/rules/typescript.md` - TypeScript and React patterns
- `.factory/rules/testing.md` - Testing conventions
- `.factory/rules/security.md` - Security requirements
```

</div>

</div>





<Aside kind="tip">
**Checkpoint:** Your coding standards are now documented and Droid will follow them consistently.
</Aside>





<Aside kind="tip">
**Enforce rules automatically:** Use [[cli/configuration/hooks-guide|PostToolUse hooks]] to run linters after edits. See [[reference/hooks-reference|Code Validation hooks]] for examples.
</Aside>



---

## Level 4: Skills & Automation {#level-4-skills-automation}

Add reusable skills and automation hooks.



<Aside kind="info">
**Three ways to automate:** 
  - **[[cli/configuration/skills|Skills]]** — Droid invokes them based on task context
  - **[[cli/configuration/hooks-guide|Hooks]]** — Run automatically on specific events
  - **[[cli/configuration/custom-slash-commands|Custom Slash Commands]]** — You invoke with `/command-name`
</Aside>





<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Create a prompt refiner skill</div>

Create `~/.factory/skills/prompt-refiner/SKILL.md`:

```markdown
---
name: prompt-refiner
description: Improve prompts before sending them to get better results. Use when you want to refine a task description.
---

# Prompt Refiner

## Instructions

When the user wants to refine a prompt:

1. Ask for their draft prompt or task description
2. Analyze it for:
   - Clarity: Is the goal specific and measurable?
   - Context: Does it include relevant background?
   - Constraints: Are requirements and limitations stated?
   - Examples: Would examples help clarify expectations?
3. Suggest an improved version with explanations
4. Offer to iterate if needed

## Good Prompt Patterns

- Start with the outcome: "Create a..." not "I want you to..."
- Include acceptance criteria: "The result should..."
- Specify format: "Return as JSON/markdown/code"
- Mention constraints: "Must be compatible with...", "Should not modify..."
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Add an auto-formatting hook</div>

Run `/hooks` and add a PostToolUse hook for automatic formatting:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Create|Edit|ApplyPatch",
        "hooks": [
          {
            "type": "command",
            "command": "cd \"$FACTORY_PROJECT_DIR\" && npx prettier --write \"$(jq -r '.tool_input.file_path' 2>/dev/null || echo '')\" 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
```

This automatically formats files after Droid edits them.

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Add a test-on-edit hook (optional)</div>

Run related tests after edits:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|ApplyPatch",
        "hooks": [
          {
            "type": "command",
            "command": "cd \"$FACTORY_PROJECT_DIR\" && jq -r '.tool_input.file_path' | xargs -I {} npm test -- --findRelatedTests {} --passWithNoTests 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
```

</div>

</div>





<Aside kind="tip">
**Checkpoint:** You now have reusable skills and automatic formatting/testing.
</Aside>



---

## Level 5: Token Optimization {#level-5-token-optimization}

Fine-tune for cost efficiency without sacrificing quality.



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Enable Spec Mode for complex work</div>

Use `Shift+Tab` or `/spec` before starting features that touch multiple files. This prevents expensive false starts.

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Configure model switching</div>

Set up a spec mode model for planning:

```bash
droid
> /settings
# Set Spec Mode Model to a reasoning-heavy model
```

Use Opus 4.5 for planning, then Sonnet or Codex for implementation.

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Run the readiness report</div>

Check your project's AI-readiness:

**CLI:**
```bash
droid
> /readiness-report
```

**Factory App:** View your readiness score in the [[web/agent-readiness/dashboard|Agent Readiness Dashboard]].

Address high-impact items first—linting, type checking, and fast tests dramatically reduce token waste.

</div>

</div>



---

## Quick Reference: File Locations {#quick-reference-file-locations}

| Purpose                | Personal                            | Project                           |
| ---------------------- | ----------------------------------- | --------------------------------- |
| **Skills**             | `~/.factory/skills/<name>/SKILL.md` | `.factory/skills/<name>/SKILL.md` |
| **Memory**             | `~/.factory/memories.md`            | `.factory/memories.md`            |
| **Rules**              | `~/.factory/rules/*.md`             | `.factory/rules/*.md`             |
| **Settings**           | `~/.factory/settings.json`          | `.factory/settings.json`          |
| **Hooks**              | `~/.factory/hooks.json`             | `.factory/hooks.json`             |
| **Agent instructions** | `~/.factory/AGENTS.md`              | `./AGENTS.md`                     |
| **Custom droids**      | `~/.factory/droids/<name>.md`       | `.factory/droids/<name>.md`       |

---

## Verification Checklist {#verification-checklist}

Run through this checklist to verify your setup:

- [ ] IDE plugin shows "connected" when running Droid
- [ ] `AGENTS.md` exists with build/test commands
- [ ] Memories file created with your preferences
- [ ] Rules directory with at least one rules file
- [ ] At least one custom skill created
- [ ] Auto-formatting hook configured
- [ ] Readiness report shows Level 2 or higher

---

## Next Steps {#next-steps}



<div class="factory-card-group">

<div class="factory-card">

**[[guides/power-user/prompt-crafting|Prompt Crafting]]**

Learn model-specific prompting techniques

</div>


  

<div class="factory-card">

**[[guides/power-user/token-efficiency|Token Efficiency]]**

Strategies for reducing token usage

</div>


  

<div class="factory-card">

**[[guides/power-user/memory-management|Memory Management]]**

Advanced memory and context patterns

</div>


  

<div class="factory-card">

**[[guides/power-user/rules-conventions|Rules Guide]]**

Organizing team conventions effectively

</div>

</div>
