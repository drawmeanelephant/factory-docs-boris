---
id: features/missions/overview
title: "Factory Missions"
status: published
summary: "Use Factory Missions to plan and execute large, multi-feature projects with structured orchestration. Describe your goal, collaborate on the plan, and let Droid manage the work."
parent: features/missions/index
tags: [features, factory-missions, missions, mission, orchestration, multi-feature, milestones, skills]
relations: [relates_to=jp/features/missions/overview]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Factory Missions</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Use Factory Missions to plan and execute large, multi-feature projects with structured orchestration. Describe your goal, collaborate on the plan, and let Droid manage the work.</p>




<div class="factory-frame">

<img src="../../images/mission-control.png" alt="Mission Control orchestration view" />

</div>



## What Missions do {#what-missions-do}

Factory Missions are structured workflows for taking on large, multi-feature work with Droid. Instead of tackling everything in a single session, you collaborate with Droid upfront to build a plan -- features, milestones, and the skills needed to accomplish each part -- then hand off execution to an orchestration layer that manages the work.

Access Missions with the `/missions` command (also available via `/mission`).



<div class="factory-card-group">

<div class="factory-card">

**Collaborative Planning**

Work with Droid to define features, milestones, and success criteria before any code is written.

</div>


  

<div class="factory-card">

**Skill-Aware Execution**

Existing skills are leveraged and new specialized skills are developed for each part of the work.

</div>


  

<div class="factory-card">

**Structured Orchestration**

Mission Control manages execution across agents, tracking progress through your plan.

</div>


  

<div class="factory-card">

**Your Config Carries Over**

MCP integrations, skills, hooks, and custom droids all work inside Missions.

</div>

</div>



## For optimal outcomes {#for-optimal-outcomes}



<Aside kind="warning">
For the best results, your repository should be at [[web/agent-readiness/overview|Agent Readiness]] **Level 4 (Optimized) or above**.

  As a mission works, it runs user-facing QA testing against your application to validate each feature and self-correct as it goes. For this to work in an existing project, your codebase needs an automated, scriptable way to exercise the app the way a user would (for example, a script to stand up or mock all dependencies of the app to simulate all potential user flows). Without it, the mission cannot reliably verify its own work.

  Not there yet? Re-run your readiness evaluation with [[cli/features/readiness-report|/readiness-report]], then close the gaps with [[cli/features/readiness-report#remediation-with-readiness-fix|/readiness-fix]].
</Aside>



## How it works {#how-it-works}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Enter Missions</div>

Start by running `/missions` in any Droid session.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Collaborate on the plan</div>

Droid interacts with you back and forth to understand your goal. It asks clarifying questions, probes for constraints, and works with you to define what you actually want built. This is a conversation, not a one-shot prompt.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Build features and milestones</div>

Based on the conversation, Droid constructs a structured plan: a set of features organized into milestones. Each milestone represents a meaningful checkpoint in the work.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Skills are leveraged or developed</div>

Droid pulls in your existing skills where they apply, and develops specialized skills for parts of the work that need them. This means the execution is tailored to your project and workflow, not generic.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Enter Mission Control</div>

Once the plan is approved, Droid enters Mission Control -- the Missions orchestration view that manages execution of the plan. You can monitor progress, see which features are being worked on, and intervene when needed.

</div>

</div>



For details on getting the plan right, see [[features/missions/planning|Planning & Validation]]. To run and steer an approved mission, see [[cli/features/missions/running-cli|Running in the CLI]] or [[web/missions|Running in the Desktop/Web]].

## What Missions are good for {#what-missions-are-good-for}

We have built and tested Missions across a range of work:

- **Full-stack development** -- Building complete applications with frontend, backend, database, and deployment.
- **Research** -- Deep investigation tasks that require exploring multiple approaches, synthesizing findings, and producing structured output.
- **Brownfield migrations** -- Modernizing existing codebases, swapping frameworks, or restructuring large projects while preserving existing behavior.
- **Ambitious prototypes** -- Product experiments that need to be functional, not just sketched out.

The common thread: work that benefits from upfront planning and structured decomposition rather than ad-hoc prompting.

## Open questions {#open-questions}

Missions are early. We are shipping this as a research preview because there are fundamental questions we are still working through:

- **Is parallelization necessary?** Running multiple agents in parallel sounds good in theory, but does it actually produce better results than sequential execution? We are testing this.
- **How do you maximize correctness?** Long-running plans accumulate errors. What validation and correction strategies work best at each stage?
- **Cost vs. quality tradeoffs** -- How aggressive should the orchestrator be? More planning and validation means higher cost but potentially better output. Where is the right balance?

We want your feedback on these. Use Missions, push the workflow hard, and tell us what works and what does not.

## See also {#see-also}

- [[features/missions/planning|Planning & Validation]] -- Get the upfront plan right and tune validation frequency
- [[cli/features/missions/running-cli|Running in the CLI]] -- Monitor, intervene, and redirect from the terminal
- [[web/missions|Running in the Desktop/Web]] -- The visual Mission Control dashboard
- [[features/missions/troubleshooting|Troubleshooting]] -- Recover from frozen missions, stuck workers, and blocked milestones
- [[features/missions/reference|Configuration & Reference]] -- Headless execution, settings, and enterprise policy
- [[cli/user-guides/specification-mode|Specification Mode]] -- For well-scoped tasks that benefit from planning before implementation
- [[cli/user-guides/implementing-large-features|Implementing Large Features]] -- Manual workflow for multi-phase projects
- [[cli/configuration/custom-droids|Custom Droids]] -- Build specialized subagents that Missions can use
- [[cli/configuration/skills|Skills]] -- Create and manage skills that Missions can leverage
