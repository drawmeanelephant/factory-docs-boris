---
id: cli/features/readiness-report
title: "Readiness Report Command"
status: published
summary: "Evaluate your repository's autonomy maturity with the /readiness-report slash command."
parent: cli/features/index
tags: [cli]
relations: [relates_to=jp/cli/features/readiness-report]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Readiness Report Command</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Evaluate your repository&#x27;s autonomy maturity with the /readiness-report slash command.</p>


The `/readiness-report` slash command evaluates your current repository against the Autonomy Maturity Model, scoring it across five maturity levels and providing actionable recommendations to improve.

---

## Prerequisites {#prerequisites}

- Run the command from inside a git repository with an `origin` remote configured (the repository URL is used to associate the report with your project in the Factory App).

---

## Usage {#usage}

To use the command, navigate to the repo you'd like to evaluate and run:

```bash
droid
> /readiness-report
```

The evaluation runs against your current repo directory.

---

## What Happens {#what-happens}

When you run `/readiness-report`, the droid performs a comprehensive evaluation of the repository:

1. **Language Detection** — Identifies repository languages (JavaScript/TypeScript, Python, Rust, Go, Java, Ruby) based on configuration files and source code
2. **Sub-application Discovery** — Determines whether the repository is a mono-repo, or a single service/package/library. For mono-repos, this step identifies all independently deployable applications within the repo
3. **Criteria Evaluation** — Checks the criteria across all five maturity levels
4. **Report Storage** — Persists the evaluation results for visualization in the Factory App
5. **Summary Output** — Prints a human-readable report with results from the evaluation

---

## Understanding the Output {#understanding-the-output}

After evaluation, you'll see a structured report:

### Level Achieved {#level-achieved}

Your repository's current maturity level (1-5):

- **Level 1: Functional** — Basic tooling in place
- **Level 2: Documented** — Process and documentation established
- **Level 3: Standardized** — Security and observability configured
- **Level 4: Optimized** — Fast feedback and continuous measurement
- **Level 5: Autonomous** — Self-improving systems

### Applications Discovered {#applications-discovered}

For monorepos, the report lists each application found with a brief description:

```
Example:
1. apps/web - Main Next.js application for user interface
2. apps/api - Backend API service
```

### Criteria Results {#criteria-results}

Each evaluated criterion is assigned a score and rationale:

```
**Style & Validation**
- Linter Configuration: 2/2 - ESLint configured in both applications
- Type Checker: 2/2 - TypeScript strict mode enabled
- Pre-commit Hooks: 0/1 - No husky or lint-staged configuration found
```

The score for each criterion is formatted as `numerator/denominator`, where:

- **numerator:** The number of sub-applications that pass the criteria
- **denominator:** The number of sub-applications that were evaluated

### Action Items {#action-items}

The report concludes with 2-3 highest-impact recommendations to reach the next level:

```
Action Items:
- Add pre-commit hooks with husky to enforce linting and formatting
- Configure branch protection rules on the main branch
- Add AGENTS.md with setup and development instructions
```

---

## Viewing Historical Reports {#viewing-historical-reports}

All readiness reports are automatically saved and can be viewed in the [[web/agent-readiness/dashboard|web dashboard]]. This allows you to:

- Track readiness progression over time
- Compare scores across repositories
- Share results with your team



<Aside kind="tip">
Run `/readiness-report` periodically (e.g., after major infrastructure changes) to track your organization's
  progress toward higher readiness levels.
</Aside>



---

## Remediation with `/readiness-fix` {#remediation-with-readiness-fix}

Once you've generated a readiness report, the `/readiness-fix` slash command lets the droid automatically remediate the failing signals from the latest report — turning the report from a diagnostic tool into an automated improvement workflow.

### What it does {#what-it-does}

`/readiness-fix` fetches the most recent stored readiness report for your repository and starts an agent session that works through the failing criteria, implementing fixes such as adding pre-commit hooks, creating an `AGENTS.md`, configuring CI checks, or improving documentation.

### Usage {#usage-2}

Navigate to the same repository you ran `/readiness-report` against and run:

```bash
droid
> /readiness-fix
```

You can also pass additional natural-language instructions to focus the run:

```bash
> /readiness-fix prioritize style & validation; do not touch CI configuration
```

### What to expect {#what-to-expect}

1. **Report lookup** — The command resolves your repository from `git remote get-url origin` and fetches the latest readiness report stored for that repo.
2. **Agent session** — The droid plans and applies changes to address failing criteria, one at a time, just like a normal coding session. You can review and approve changes as they happen.
3. **Verification** — After fixes are applied, run `/readiness-report` again to re-score the repository and confirm signals have moved.



<Aside kind="note">
`/readiness-fix` requires that a readiness report has already been generated for the repo. If no prior report is found, run `/readiness-report` first.
</Aside>





<Aside kind="tip">
Treat `/readiness-fix` like any other agent run: review the proposed changes, run your tests, and commit only what looks good for your codebase.
</Aside>
