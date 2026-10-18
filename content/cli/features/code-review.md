---
id: cli/features/code-review
title: "Local Code Review"
status: published
summary: "Use the /review command to analyze local code changes with AI-powered review workflows"
parent: cli/features/index
tags: [cli, local-code-review, code-review, review, slash-command, pr-review, pull-request, commit-review]
relations: [relates_to=jp/cli/features/code-review]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Local Code Review</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Use the /review command to analyze local code changes with AI-powered review workflows</p>


## Overview {#overview}

The `/review` command provides a local workflow for analyzing code changes with AI-powered insights. It offers multiple review modes to fit different development scenarios—from reviewing uncommitted changes to analyzing full branches or specific commits.

When you run `/review`, droid guides you through selecting a review type, configuring parameters, and then performs a comprehensive analysis of your code changes based on industry-standard review guidelines.

## Quick start {#quick-start}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Start the review flow</div>

In a local droid session, type:
```bash
/review
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">Select a review type</div>

Choose from four review presets:
  - **Review against a base branch** - PR-style review comparing your branch to a base branch
  - **Review uncommitted changes** - Analyze working directory changes (staged, unstaged, and untracked)
  - **Review a commit** - Examine a specific commit from history
  - **Custom review instructions** - Define your own review criteria

</div>



  

<div class="factory-step">

<div class="factory-step-title">Configure parameters</div>

Depending on your selection:
  - For **base branch reviews**: Select the target branch (e.g., `main`, `develop`)
  - For **commit reviews**: Choose a commit from the interactive list
  - For **custom reviews**: Enter your review instructions

</div>



  

<div class="factory-step">

<div class="factory-step-title">Review the findings</div>

Droid analyzes the code changes and provides:
  - Prioritized findings with severity levels [P0-P3]
  - Specific file locations and line numbers
  - Suggested fixes with code suggestions
  - Overall assessment of the changes

</div>

</div>



## Review types {#review-types}

### Review against a base branch {#review-against-a-base-branch}

Compare your current branch against a base branch (like a pull request review). This is ideal for pre-PR reviews or checking what changes would be merged.

**How it works:**
1. Select "Review against a base branch"
2. Choose your target base branch from the list (local and remote branches shown)
3. Droid finds the merge base and reviews the diff

**Use cases:**
- Pre-commit PR reviews
- Checking branch changes before creating a pull request
- Validating feature branch against main/develop

**Example workflow:**
```bash
> /review
# Select: Review against a base branch
# Choose: origin/main
# Droid reviews all changes that would be merged
```

### Review uncommitted changes {#review-uncommitted-changes}

Analyze all current working directory changes—staged files, unstaged modifications, and untracked files.

**Use cases:**
- Quick sanity check before committing
- Reviewing work in progress
- Finding issues early in development

**Example workflow:**
```bash
> /review
# Select: Review uncommitted changes
# Droid immediately reviews all working directory changes
```

### Review a commit {#review-a-commit}

Examine the changes introduced by a specific commit in your repository history.

**How it works:**
1. Select "Review a commit"
2. Browse commits with hash, message, author, and date
3. Select a commit to review

**Use cases:**
- Reviewing recent commits for issues
- Understanding changes in a specific commit
- Post-merge review of teammate's work

**Example workflow:**
```bash
> /review
# Select: Review a commit
# Browse and select: abc1234 - "Add user authentication"
# Droid reviews that specific commit's changes
```

### Custom review instructions {#custom-review-instructions}

Define your own review criteria for specialized analysis.

**Use cases:**
- Performance analysis
- Checking specific coding standards
- Domain-specific validations

**Example workflow:**
```bash
> /review
# Select: Custom review instructions
# Enter: "Focus on performance regressions and unnecessary re-renders"
# Droid performs a targeted review
```

## Review guidelines {#review-guidelines}

All code reviews follow a structured rubric designed to provide actionable, high-quality feedback:

### Severity levels {#severity-levels}

Reviews categorize findings using priority levels:

- **[P0]** - Critical issues blocking release or operations
- **[P1]** - Urgent issues that should be addressed in the next cycle
- **[P2]** - Normal priority issues to fix eventually
- **[P3]** - Low priority nice-to-have improvements

### Bug detection criteria {#bug-detection-criteria}

The AI only flags issues as bugs when they meet ALL of these criteria:

1. **Meaningful impact** - Affects accuracy, performance, security, or maintainability
2. **Discrete and actionable** - Clear, specific issue with a clear fix
3. **Appropriate rigor** - Fix doesn't demand more rigor than the rest of the codebase
4. **Introduced in changes** - Bug was added in the reviewed changes (not pre-existing)
5. **Worth fixing** - Author would likely fix if made aware
6. **No unstated assumptions** - Based on verifiable facts, not speculation
7. **Provably affected** - Can identify specific affected code, not theoretical
8. **Not intentional** - Clearly not a deliberate design choice

### Comment style {#comment-style}

Review comments follow these principles:

- **Clear reasoning** - Explains why something is an issue
- **Appropriate severity** - Communicates impact accurately
- **Brief** - Maximum 1 paragraph per finding
- **Minimal code** - Code chunks limited to 3 lines in markdown
- **Scenario-specific** - Describes affected environments/conditions
- **Matter-of-fact tone** - Avoids accusatory language
- **Immediately graspable** - Easy for the author to understand
- **No excessive flattery** - Focuses on actionable feedback

### Output format {#output-format}

Each finding includes:

- **Clear title** (≤80 characters, imperative mood)
- **Explanation** of why this is a problem
- **File path and line numbers** where applicable
- **Priority level** [P0-P3]
- **Suggested fix** (when concrete replacement code is available)

Plus an **overall assessment**:
- Whether changes are correct or incorrect
- 1-3 sentence summary

## Tips and best practices {#tips-and-best-practices}





<Details summary="When to use each review type">
- **Uncommitted changes**: During active development, before staging commits
  - **Base branch review**: Before creating PRs, to catch issues early
  - **Commit review**: After merging, to understand historical changes or review teammate's commits
  - **Custom instructions**: When you need focused analysis (security, performance, specific patterns)
</Details>



  

<Details summary="Making the most of reviews">
- Run reviews frequently during development, not just before commits
  - Use custom instructions for domain-specific concerns your team cares about
  - Treat P0/P1 findings seriously—they represent real issues worth addressing
  - Review the overall assessment for context on whether changes are sound
</Details>



  

<Details summary="Navigating the review UI">
- Press **Esc** to go back at any step in the review flow
  - From the preset selection, **Esc** closes the review overlay
  - Use arrow keys to navigate branch/commit lists
  - Type to filter branches by name in real-time
</Details>



  

<Details summary="Integration with workflows">
The `/review` command is meant for local CLI sessions. For automated reviews in CI/CD, use:
```bash
droid exec "Review the changes in this PR for correctness and performance regressions"
```
See the [[guides/droid-exec/code-review|Automated Code Review guide]] for automation setup.
</Details>





## Examples {#examples}

### Pre-PR review {#pre-pr-review}

```bash
# Before creating a pull request
> /review
# Select: Review against a base branch
# Choose: origin/main
# Review findings, fix issues, then create PR
```

### Quick WIP check {#quick-wip-check}

```bash
# Check work in progress
> /review
# Select: Review uncommitted changes
# Get immediate feedback on current changes
```

### Post-merge review {#post-merge-review}

```bash
# Review a teammate's recent commit
> /review
# Select: Review a commit
# Choose the recent commit to understand changes
```

## Automated reviews in CI {#automated-reviews-in-ci}

For automated PR reviews, use the [[guides/droid-exec/code-review|Automated Code Review]] workflow. It supports:

- **Automatic PR reviews** triggered by pull request events or comments
- **Review depth** (`deep` or `shallow`) to control thoroughness and cost
- **Custom review guidelines** for repository-specific checks

Set up with:

```bash
droid
> /install-code-review
```

See the [[guides/droid-exec/code-review|Automated Code Review guide]] for full configuration options.

## See also {#see-also}

- [[reference/cli-reference|CLI Reference]] - Complete command reference including `/review`
- [[guides/droid-exec/code-review|Automated Code Review guide]] - Set up automated PR reviews with deep/shallow modes
- [[cli/getting-started/common-use-cases|Common use cases]] - Other workflows and patterns
- [[cli/getting-started/how-to-talk-to-a-droid|How to talk to a droid]] - Getting better results from AI reviews
