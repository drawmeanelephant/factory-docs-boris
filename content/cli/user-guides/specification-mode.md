---
id: cli/user-guides/specification-mode
title: "Specification Mode"
status: published
summary: "Turn plain-English specifications into production-ready code with automatic planning and review."
parent: cli/user-guides/index
tags: [cli, spec-mode, specification, planning, plan, spec, feature-planning, implementation-plan]
relations: [relates_to=jp/cli/user-guides/specification-mode]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Specification Mode</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Turn plain-English specifications into production-ready code with automatic planning and review.</p>


Specification Mode transforms simple feature descriptions into working code with automatic planning and safety checks. You provide a brief description of what you want, and droid creates a detailed specification and implementation plan before making any changes.



<div class="factory-card-group">

<div class="factory-card">

**Simple Input**

Just 4-6 sentences describing what you want built

</div>


  

<div class="factory-card">

**Automatic Planning**

Droid creates detailed specs and implementation plans

</div>


  

<div class="factory-card">

**Safe Execution**

No code changes until you approve the complete plan

</div>


  

<div class="factory-card">

**Enterprise Ready**

Built-in security, compliance, and team standards

</div>

</div>



## How it works {#how-it-works}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Describe your feature</div>

Provide a simple description in 4-6 sentences. No need to write formal
specifications.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Droid creates the spec</div>

Droid analyzes your request and generates a complete specification with
acceptance criteria, implementation plan, and technical details. You can optionally use [[cli/configuration/mixed-models|mixed models]] to configure a different model for planning.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Review and approve</div>

You review the generated specification and implementation plan. Request
changes or approve as-is.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Implementation</div>

Only after approval does droid begin making actual code changes, showing
each modification for review.

</div>

</div>



## Example workflow {#example-workflow}

**Your input:**

```
Add a feature for users to export their personal data.
It should create a ZIP file with their profile, posts, and uploaded files.
Send them an email when it's ready. Make sure it follows GDPR requirements.
The export should work for accounts up to 2GB of data.
```

**Droid generates:**

- Complete specification with detailed acceptance criteria
- Technical implementation plan covering backend, frontend, and email
- File-by-file breakdown of changes needed
- Testing strategy and verification steps
- Security and compliance considerations

**You approve, then droid implements** the complete solution while showing each change for review.



<Aside kind="note">
Specification Mode must be manually activated using **Shift+Tab** in the CLI.
  It does not automatically activate.
</Aside>



## How to activate Specification Mode {#how-to-activate-specification-mode}

To enter Specification Mode, press **Shift+Tab** while in the CLI. This will enable the specification planning workflow for your next request.

## What happens during planning {#what-happens-during-planning}

**Analysis phase (read-only):**

- Examines your existing codebase and patterns
- Reviews related files and dependencies
- Studies your AGENTS.md conventions
- Gathers context from external sources

**Planning phase:**

- Develops comprehensive implementation strategy
- Identifies all files that need changes
- Plans sequence of modifications
- Considers testing and verification steps

**Safety guarantees:**

- Cannot edit files during analysis
- Cannot run commands that modify anything
- Cannot create, delete, or move files
- All exploration is read-only until you approve

## Writing effective requests {#writing-effective-requests}

**Focus on outcomes:** Describe what the software should accomplish, not how to build it.

```
Users need to be able to reset their passwords using email verification.
The reset link should expire after 24 hours for security.
Include rate limiting to prevent abuse.
```

**Include important constraints:**

```
Add user data export functionality that works for accounts up to 5GB.
Must comply with GDPR and include audit logging.
Should complete within 10 minutes and not impact application performance.
```

**Reference existing patterns:**

```
Add a notification system similar to how we handle email confirmations.
Use the same background job pattern as our existing report generation.
Follow the authentication patterns we use for other sensitive operations.
```

**Be specific about verification:** Tell droid how to confirm the implementation works correctly.

**Consider the full user journey:** Describe the complete experience, not just technical requirements.

**Include error scenarios:** Specify how failures should be handled and communicated to users.

**Think about scale:** Mention performance requirements and expected usage patterns.

## Enterprise integration {#enterprise-integration}

Reference external requirements by pasting links:

```
Implement the user management features described in this Jira ticket:
https://company.atlassian.net/browse/PROJ-123

Follow our security standards and include comprehensive error handling.
```

If you've integrated platforms through Factory's dashboard, droid can read context from tickets, documents, and specs during analysis.

## Benefits {#benefits}



<div class="factory-card-group">

<div class="factory-card">

**Safety First**

No accidental changes during exploration. See the complete plan before any
modifications.

</div>


  

<div class="factory-card">

**Thorough Planning**

Comprehensive analysis leads to better architecture decisions and fewer
surprises.

</div>


  

<div class="factory-card">

**Full Control**

Complete visibility into what will be done before any code changes happen.

</div>


  

<div class="factory-card">

**Better Outcomes**

Well-planned implementations are more likely to be correct, complete, and
maintainable.

</div>

</div>



## AGENTS.md integration {#agentsmd-integration}

Document your project conventions to enhance Specification Mode's planning. See [[cli/configuration/agents-md|AGENTS.md]] for more information.

Specification Mode automatically incorporates these conventions, ensuring consistency with your team's standards.

## Breaking down large features {#breaking-down-large-features}

For complex features spanning multiple components, break them into focused phases:

**Phase 1:**

```
Implement user data export backend API and job processing.
Focus only on the server-side functionality, not the UI yet.
```

**Phase 2:**

```
Add the frontend UI for data export using the API from Phase 1.
Include progress indicators and download management.
```

This approach allows you to validate each phase before proceeding to the next.

## Specification approval options {#specification-approval-options}

After droid presents the specification, choose how to continue:

1. **Proceed with implementation** – Approve the plan and keep normal (manual) execution controls.
2. **Proceed, and allow file edits and read-only commands (Low)** – Set Autonomy Level to Low so droid can edit files and run safe read-only commands automatically.
3. **Proceed, and allow reversible commands (Medium)** – Set Autonomy Level to Medium so droid can also run reversible commands without additional prompts.
4. **Proceed, and allow all commands (High)** – Set Autonomy Level to High for fully automated execution, including commands that are not easily reversible.
5. **No, keep iterating on spec** – Stay in Specification Mode to refine the plan before implementation.

Selecting any Autonomy Level option sets that level for the rest of the session. Choosing to keep iterating leaves Specification Mode active so you can continue shaping the plan.

## Saving your specifications as Markdown {#saving-your-specifications-as-markdown}

Specification Mode can automatically write the approved plan to disk. Open the CLI settings and enable **Save spec as Markdown** to turn this on.

- By default, plans are saved to `.factory/docs` inside the nearest project-level `.factory` directory. If none exists, the CLI falls back to `~/.factory/docs` in your home directory.
- Use the **Spec save directory** setting to pick between the project directory, your home directory, or a custom path. Custom values support absolute paths, `~` expansion, `.factory/...` shortcuts, and relative paths from the current workspace.
- The CLI creates the target directory if it does not exist and writes the Markdown exactly as shown in the approval dialog.
- Files are named `YYYY-MM-DD-slug.md`, where the slug comes from the spec title or first heading, and a counter is appended if a file with the same name already exists.

## What happens after approval {#what-happens-after-approval}

Once you approve a specification plan, droid systematically implements the changes while showing each modification for review. You maintain full control through the approval workflow, ensuring quality and alignment with requirements.

For simpler changes that don't need comprehensive planning, droid can proceed directly while still showing all modifications for approval.

Ready to try Specification Mode? Start with a simple description of what you want to build, and let droid handle the specification and planning complexity.
