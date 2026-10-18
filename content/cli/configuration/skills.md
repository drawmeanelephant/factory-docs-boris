---
id: cli/configuration/skills
title: "Skills"
status: published
summary: "Reusable capabilities that your AI agent invokes on demand."
parent: cli/configuration/index
tags: [cli, skills, capabilities, tools, workflows, expertise, reusable, invoke]
relations: [relates_to=jp/cli/configuration/skills]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Skills</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Reusable capabilities that your AI agent invokes on demand.</p>

Skills are **reusable capabilities** that extend what your Droid can do. Create a `SKILL.md` file with instructions, and the Droid adds it to its toolkit. The Droid uses skills when relevant, or you can invoke one directly with `/skill-name`.



<Aside kind="tip">
Explore the [[guides/skills/frontend-ui-integration|skills guides]] for examples.
</Aside>





<Aside kind="note">
**Custom slash commands have been merged into skills.** A file at `.factory/commands/review.md` and a skill at `.factory/skills/review/SKILL.md` both create `/review` and work the same way. Your existing `.factory/commands/` files keep working. Skills add optional features: a directory for supporting files, frontmatter to [[cli/configuration/skills#control-who-invokes-a-skill|control who can invoke them]], and the ability for Droids to load them automatically when relevant.
</Aside>



**Key properties:**
- **Flexible invocation** – Both you and the Droid can invoke skills. Type `/skill-name` or let the Droid decide when to use them.
- **Composable** – can be chained together as part of larger workflows
- **Token-efficient** – lightweight and focused, not bloated with unused tools or repeated instructions

**A skill can be:**
- **A workflow** – step-by-step instructions (e.g., "navigate to URL, take screenshot, extract data")
- **Expertise** – domain knowledge and conventions (e.g., "how we implement frontend features with our design system")
- **Both** – instructions + tools + best practices bundled together

**Example skills:**
- `browser` – automate Chrome with CDP tools (navigate, screenshot, evaluate JS)
- `linear` – manage Linear issues with CLI tools (list, update status, move teams)
- `frontend-ui-integration` – implement typed React flows following team conventions

## What is a skill? {#what-is-a-skill}

A skill is a **directory** (e.g. `.factory/skills/frontend-ui-integration/`) containing:

- `SKILL.md` or `skill.mdx` with YAML frontmatter and markdown instructions
- Optional supporting files (scripts, schemas, checklists)

Each skill defines what problem it solves, what inputs it expects, and what success looks like. The Droid automatically invokes matching skills when they apply to the current task.

## Skill file format {#skill-file-format}

Skills are defined in Markdown with YAML frontmatter. A small, focused skill can be just a short `SKILL.md`:

```md
---
name: summarize-diff
description: Summarize the staged git diff in 3–5 bullets. Use when the user asks for a summary of pending changes.
---

# Summarize Diff

## Instructions

1. Run `git diff --staged`.
2. Summarize the changes in 3–5 bullets, focusing on user-visible behavior.
3. Call out any migrations, risky areas, or tests that should be run.
```

You can also include additional frontmatter fields to control behavior. See [[cli/configuration/skills#frontmatter-reference|Frontmatter reference]] for all available options.

## Where skills live {#where-skills-live}

Skills are discovered from a small set of well-known locations:

| Scope         | Location                            | Purpose                                                                 |
| ------------- | ----------------------------------- | ----------------------------------------------------------------------- |
| **Workspace** | `<repo>/.factory/skills/`           | Project skills shared with teammates; checked into git.                 |
| **Personal**  | `~/.factory/skills/`                | Private skills that follow you across projects on your machine.         |
| **Compatibility** | `<repo>/.agent/skills/`         | Discovered for compatibility with `.agent` folder conventions.          |

Each **skill** lives in its own directory under one of these roots:

- Workspace: `<repo>/.factory/skills/<skill-name>/SKILL.md`
- Personal: `~/.factory/skills/<skill-name>/SKILL.md`

In large monorepos, you can either:

- Keep a **single, shared** skills folder at the root:

  ```text
  .factory/skills/
    frontend/
      SKILL.md
    payments-service/
      SKILL.md
    data-warehouse-querying/
      SKILL.md
  ```

- Or add **per-project** `.factory` folders so skills live alongside each subproject:

  ```text
  services/payments/.factory/skills/
    payments-service/
      SKILL.md
  apps/frontend/.factory/skills/
    dashboard-ui/
      SKILL.md
  ```

Project skills are the primary way to share and standardize capabilities inside an engineering org; personal skills are ideal for individual workflows or experiments.

## Frontmatter reference {#frontmatter-reference}

Skills support YAML frontmatter fields between `---` markers at the top of your `SKILL.md` file:

```yaml
---
name: my-skill
description: What this skill does and when to use it
user-invocable: true
disable-model-invocation: false
---

Your skill instructions here...
```

| Field                      | Required    | Default | Description                                                                                                                                           |
| :------------------------- | :---------- | :------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                     | No          | Directory name | Display name for the skill. Lowercase letters, numbers, and hyphens only.                    |
| `description`              | Recommended | —       | What the skill does and when to use it. The Droid uses this to decide when to apply the skill. |
| `user-invocable`           | No          | `true`  | Set to `false` to hide from the `/` slash command menu. Use for background knowledge users shouldn't invoke directly. |
| `disable-model-invocation` | No          | `false` | Set to `true` to prevent the Droid from automatically loading this skill. Use for workflows you want to trigger manually with `/skill-name`. |

## Control who invokes a skill {#control-who-invokes-a-skill}

By default, both you and the Droid can invoke any skill. You can type `/skill-name` to invoke it directly, and the Droid can load it automatically when relevant to your conversation. Two frontmatter fields let you restrict this:

- **`disable-model-invocation: true`**: Only you can invoke the skill. Use this for workflows with side effects or that you want to control timing, like `/deploy` or `/send-notification`. You don't want the Droid deciding to deploy because your code looks ready.

- **`user-invocable: false`**: Only the Droid can invoke the skill. Use this for background knowledge that isn't actionable as a command. A `legacy-system-context` skill explains how an old system works. The Droid should know this when relevant, but `/legacy-system-context` isn't a meaningful action for users to take.

### Invocation summary {#invocation-summary}

| Frontmatter                      | User can `/invoke` | Droid can invoke |
| :------------------------------- | :----------------- | :--------------- |
| (default)                        | Yes                | Yes              |
| `disable-model-invocation: true` | Yes                | No               |
| `user-invocable: false`          | No                 | Yes              |

## Quickstart {#quickstart}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Create a skill folder</div>

Under your repo, create a directory in `.factory/skills/`, for example
`.factory/skills/frontend-ui-integration/`.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Add SKILL.md or skill.mdx</div>

Inside the folder, create `SKILL.md` or `skill.mdx` with YAML frontmatter
(`name`, `description`) and markdown instructions that define the
capability, inputs, and success criteria.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Add supporting files (optional)</div>

Co-locate any types, schemas, or checklists the Droid should use when the
skill is active (for example `types.ts`, `schemas/`, or
`rollout-checklist.md`).

</div>


  

<div class="factory-step">

<div class="factory-step-title">Restart and use</div>

Restart `droid` or your integration so it rescans skills, then describe
your task normally. The Droid will automatically invoke matching skills
when they apply.

</div>

</div>



## How skills differ from other configuration {#how-skills-differ-from-other-configuration}

Skills sit alongside other ways of shaping Droid behavior:

- **Custom droids** – define *which* model and tools to use and at what autonomy level; they are full agent configurations.
- **Legacy slash commands** (`.factory/commands/`) – user-invoked macros that still work but are now superseded by skills. Skills offer the same `/command` functionality plus optional Droid invocation and supporting files.
- **MCP servers** – expose external systems (APIs, databases, SaaS tools) as tools; they are about *connecting* resources, not encoding your workflow.

Skills are different because they:

- Package **how work should be done** (your engineering playbook) as reusable capabilities.
- Support **flexible invocation** – both you (via `/skill-name`) and the Droid can trigger them, with [[cli/configuration/skills#control-who-invokes-a-skill|fine-grained control]] over who can invoke what.
- Are **discoverable and composable** – the Droid can chain multiple skills inside a plan.
- Can sit on top of tools, custom droids, and MCP servers to orchestrate them safely.

In practice you might:

- Use MCP to expose your internal deployment API.
- Use a custom droid to define which tools/models are allowed in CI.
- Use a skill to encode "how to safely roll out a canary deployment" using that API and droid configuration.

## Why skills matter in enterprise codebases {#why-skills-matter-in-enterprise-codebases}

Skills are especially valuable in enterprise environments where you need to:

- Standardize how Droids do **frontend implementation, service integrations, data querying, and internal tools**.
- Encode **team conventions, safety rules, and SLAs** once, then reuse them across projects.
- Make automation **discoverable, auditable, and shareable** via git, not just "whatever happened in one chat".

You can create skills from scratch for Factory, or reuse existing skills you already invested in for other agents by importing them and wiring them into your droid configuration.


# Best practices {#best-practices}





<Details summary="Keep each skill narrow and outcome-focused">
Design skills around a **single responsibility** (e.g., "implement a typed
React UI for an existing endpoint"), not "build the whole feature".
Define a **crisp success criterion**: what artifacts should exist when the
skill finishes (files changed, tests added, docs updated, approvals
gathered). Prefer several small skills composed by a Droid over one giant
"do everything" skill.
</Details>



  

<Details summary="Make inputs explicit and structured">
Document required inputs: repo path, services involved, APIs, schemas,
feature flag names, etc. Use **structured fields** (JSON snippets, bullet
lists, tables) instead of long prose when describing APIs or data models.
For security-sensitive workflows, include explicit **"never do"**
constraints and escalation conditions.
</Details>



  

<Details summary="Encode team conventions and guardrails">
Bake in your **testing, observability, and rollout requirements** so the
skill always follows them. Reference your existing **AGENTS.md**, runbooks,
and design docs instead of inlining everything. Require **proof
artifacts**: tests, screenshots, log queries, or links to dashboards
depending on the domain.
</Details>



  

<Details summary="Design for enterprise constraints">
Assume **large monorepos, multiple services, and layered approvals**. Be
explicit about **which directories** Droids may touch, which
languages/frameworks are in-bounds, and which are not. Include guidance for
**cross-team dependencies** – when to stub, when to coordinate with
another team, and when to stop and ask.
</Details>



  

<Details summary="Make skills composable">
Prefer **idempotent** skills: safe to rerun on the same branch/PR. Design
skills to produce **machine-parseable output** where possible (for example,
a short summary block that other skills can consume). Keep skills
**stateless** beyond the current branch: no hidden assumptions about prior
runs.
</Details>



  

<Details summary="Operate with verification and safety">
Always include a **"Verification"** section that lists commands Droids
must run before completing the skill. Call out **fallbacks** when
verification fails (rollback steps, feature flags, or canary paths). For
production-adjacent skills, require that Droids **open PRs but never
merge** without human review.
</Details>






## Cookbook {#cookbook}

The cookbook provides opinionated skill templates aimed at common enterprise software workflows.

We focus on nine families of skills:

1. **[[guides/skills/frontend-ui-integration|Frontend implementation skills]]** – building UI surfaces that integrate with existing APIs
2. **[[guides/skills/service-integration|Integration skills for complex codebases]]** – extending or wiring together services in large monorepos
3. **[[guides/skills/data-querying|Internal data querying skills]]** – safe, auditable access to internal analytics or data services
4. **[[guides/skills/internal-tools|Internal tools skills]]** – building small but robust internal apps that improve developer and operator workflows
5. **[[guides/skills/vibe-coding|Vibe coding skills]]** – rapidly prototyping and building complete modern web applications from scratch (Lovable/Bolt/v0 replacement)
6. **[[guides/skills/ai-data-analyst|AI data analyst skills]]** – comprehensive data analysis, visualization, and statistical modeling (data analyst tool replacement)
7. **[[guides/skills/product-management|Product management skills]]** – assisting with PRDs, feature analysis, and PM workflows (PM tool augmentation)
8. **[[guides/skills/browser|Browser automation skills]]** – launching Chrome via CDP, navigating live tabs, evaluating DOM state, and collecting screenshots or selectors without running an MCP server
9. **[[guides/skills/automated-qa|Automated QA skills]]** – end-to-end quality assurance that tests your application as a real user would, with visual evidence, CI integration, and failure learning



<div class="factory-card-group">

<div class="factory-card">

**[[guides/skills/frontend-ui-integration|Frontend UI integration]]**

Implement typed, tested frontend flows against existing backend APIs using
your design system, routing, and testing conventions.

</div>


  

<div class="factory-card">

**[[guides/skills/service-integration|Service integration in complex codebases]]**

Extend or wire backend services in a shared monorepo while respecting
ownership boundaries, observability, and rollout requirements.

</div>


  

<div class="factory-card">

**[[guides/skills/data-querying|Internal data querying]]**

Safely query internal analytics and data services, producing reproducible
queries and shareable analysis artifacts.

</div>


  

<div class="factory-card">

**[[guides/skills/internal-tools|Internal tools]]**

Build or extend internal-facing tools (admin panels, consoles, utilities)
with strong RBAC, audit logging, and operational safeguards.

</div>


  

<div class="factory-card">

**[[guides/skills/vibe-coding|Vibe coding]]**

Rapidly prototype and build complete modern web applications from scratch
using React, Next.js, Vue, or other frameworks. Local-first alternative to
Lovable, Bolt, and v0.

</div>


  

<div class="factory-card">

**[[guides/skills/ai-data-analyst|AI data analyst]]**

Perform comprehensive data analysis, statistical modeling, and create
publication-quality visualizations using Python and the full data science
ecosystem.

</div>


  

<div class="factory-card">

**[[guides/skills/product-management|Product management]]**

Assist with product management workflows including writing PRDs, analyzing
features, synthesizing research, and planning roadmaps.

</div>


  

<div class="factory-card">

**[[guides/skills/browser|Browser automation]]**

Launch Chrome with remote debugging, drive tabs, evaluate DOM state, and
capture screenshots or selectors without deploying extra infrastructure.

</div>


  

<div class="factory-card">

**[[guides/skills/automated-qa|Automated QA]]**

End-to-end quality assurance that tests your app as a real user would --
across web, CLI, and API surfaces -- with visual evidence and CI integration.

</div>

</div>



In practice, each skill folder can also contain **supporting utilities** the agent may use alongside the core prompt template – for example:

- `SKILL.md` or `skill.mdx` – the main skill specification
- `references.md` – links and pointers to types, APIs, and modules that already exist in your codebase
- `schemas/` – JSON/YAML schemas or OpenAPI snippets referenced by the skill (not the source-of-truth service code)
- `checklists.md` – reusable validation or rollout checklists

These co-located files give the agent a predictable, structured bundle of context to work from when the skill is invoked, without duplicating or relocating production code.

Use these as starting points and adapt the inputs, constraints, and verification steps to match your stack and governance requirements.
