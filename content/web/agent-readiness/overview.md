---
id: web/agent-readiness/overview
title: "Overview"
status: published
summary: "Understand the Agent Readiness Model across Droid CLI, dashboard, and API surfaces."
parent: web/agent-readiness/index
tags: [web]
relations: [relates_to=jp/web/agent-readiness/overview]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Overview</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Understand the Agent Readiness Model across Droid CLI, dashboard, and API surfaces.</p>


Autonomous software organizations build systems that maintain and improve themselves with minimal human intervention. Developers describe what they want built through whatever medium makes sense, and the system executes that vision with quality and precision.

The **Agent Readiness Model** measures how close your organization is to this state, and helps remediate gaps to get you there faster.

---

## Getting Started {#getting-started}

There are four ways to interact with Agent Readiness:

1. **Droid CLI:** Run the `/readiness-report` [[cli/features/readiness-report|slash command]] to evaluate a repository's readiness level
2. **Factory App dashboard:** View your organization's readiness scores in the [[web/agent-readiness/dashboard|Agent Readiness dashboard]]
3. **API:** Programmatically access readiness reports via the [[reference/readiness-reports-api|Readiness Reports API]]
4. **Remediation (Coming Soon):** Automatically fix failing criteria directly from the Droid CLI or dashboard

---

## What Autonomous Development Looks Like {#what-autonomous-development-looks-like}

What does it look like when an organization reaches high agent readiness? Here are concrete examples of workflows that become possible when the technical foundation is in place.

### Code from Conversation {#code-from-conversation}

A developer describes what they need built, and the system executes through deployment.

**Input:** "Refactor the authentication module to support OAuth2 with PKCE, maintaining backward compatibility."

**The system:**

- Generates idiomatic code following established patterns
- Validates against linters, type checkers, and test suites
- Handles the pull request and code review process
- Updates documentation and notifies stakeholders
- Deploys and monitors for issues

### Design to Implementation {#design-to-implementation}

A designer shares a mockup, and the system implements it without handoffs.

**Input:** Figma mockup of a new dashboard.

**The system:**

- Interprets the visual specification and design system
- Implements UI components with proper styling and responsiveness
- Connects to existing APIs or creates new endpoints
- Adds loading states, error handling, and accessibility
- Generates tests for user interactions
- Deploys to staging for design review

### Bug to Deployed Fix {#bug-to-deployed-fix}

A customer reports an issue, and the system diagnoses, fixes, and deploys autonomously.

**Input:** Bug report through support system.

**The system:**

- Triages based on error logs and impact
- Creates a ticket with reproduction steps and diagnostic context
- Identifies the root cause from code analysis
- Generates a fix and comprehensive tests
- Opens a PR and assigns a developer for review
- Notifies support when the fix is deployed

---

## The 5 Readiness Levels {#the-5-readiness-levels}

Repositories progress through five distinct levels, each representing a qualitative shift in how autonomous agents can operate within your codebase.

| Level | Name         | Description                                                                                                                            | Example Criteria                                                     |
| :---- | :----------- | :------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------- |
| **1** | Functional   | Code runs, but requires manual setup and lacks automated validation. Basic tooling that every repository should have.                  | README, linter, type checker, unit tests                             |
| **2** | Documented   | Basic documentation and process exist. Workflows are written down and some automation is in place.                                     | AGENTS.md, devcontainer, pre-commit hooks, branch protection         |
| **3** | Standardized | Clear processes are defined, documented, and enforced through automation. Development is standardized across the organization.         | Integration tests, secret scanning, distributed tracing, metrics     |
| **4** | Optimized    | Fast feedback loops and data-driven improvement. Systems are designed for productivity and measured continuously.                      | Fast CI feedback, regular deployment frequency, flaky test detection |
| **5** | Autonomous   | Systems are self-improving with sophisticated orchestration. Complex requirements decompose automatically into parallelized execution. | Self-improving systems                                               |

---

## How Scoring Works {#how-scoring-works}

### Level Progression {#level-progression}

To unlock a level, you must pass **80% of the criteria** from the previous level. This creates a gated progression system:

1. All repositories start at Level 1
2. Pass 80% of Level 1 criteria → Unlock Level 2
3. Pass 80% of Level 2 criteria → Unlock Level 3
4. And so on...

### Evaluation Scopes {#evaluation-scopes}

Criteria are evaluated at two different scopes:

- **Repository Scope:** Evaluated once for the entire repository (e.g., CODEOWNERS file exists, branch protection enabled)
- **Application Scope:** Evaluated per application in monorepos (e.g., linter configured, unit tests exist for each app)

For monorepos with multiple applications, application-scoped criteria show scores like `3 / 4` (3 out of 4 apps pass).

---

## The Technical Pillars {#the-technical-pillars}

The Agent Readiness Model organizes criteria into nine technical pillars that form the foundation for autonomous operation.

### Style & Validation {#style-validation}

Linters, type checkers, and formatters catch obvious errors instantly. Agents avoid wasting cycles on syntax errors, style inconsistencies, and type mismatches.

- **Example criteria:** Linter configuration, type checker, code formatter, pre-commit hooks

### Build System {#build-system}

Clear, deterministic build commands let agents verify their changes compile and run before committing. No guessing about which commands to run or which flags to pass.

- **Example criteria:** Build command documented, dependencies pinned, VCS CLI tools

### Testing {#testing}

Fast unit and integration tests create tight feedback loops. Agents learn whether their changes work correctly by running tests, seeing failures, and iterating.

- **Example criteria:** Unit tests exist, integration tests exist, tests runnable locally

### Documentation {#documentation}

Explicit instructions house the tribal knowledge that "everyone just knows." How to set up the environment, run tests, deploy changes, debug issues. Agents need written instructions that are discoverable, accurate, and maintained.

- **Example criteria:** AGENTS.md, README, documentation freshness

### Development Environment {#development-environment}

Reproducible environments ensure consistency. When developers and agents work in identical environments, entire classes of problems disappear. No more "works on my machine."

- **Example criteria:** Devcontainer, environment template, local services setup

### Debugging & Observability {#debugging-observability}

Structured logging, tracing, and metrics give agents runtime visibility into what code actually does. Good observability turns "it failed" into "it failed because X was null when calling Y after receiving Z."

- **Example criteria:** Structured logging, distributed tracing, metrics collection

### Security {#security}

Branch protection, secret scanning, and code owners prevent agents from introducing security issues or bypassing required reviews. Agents move fast—automated guardrails ensure they move fast safely.

- **Example criteria:** Branch protection, secret scanning, CODEOWNERS

### Task Discovery {#task-discovery}

Infrastructure for agents to find and scope work autonomously. Well-structured issues and templates help agents understand what needs to be done.

- **Example criteria:** Issue templates, issue labeling system, PR templates

### Product & Experimentation {#product-experimentation}

Tools for measuring impact, running experiments, and understanding user behavior. Agents can see whether features are actually used and measure the impact of their changes.

- **Example criteria:** Product analytics instrumentation, experiment infrastructure
