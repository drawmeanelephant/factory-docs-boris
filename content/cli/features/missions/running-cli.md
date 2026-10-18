---
id: cli/features/missions/running-cli
title: "Running in the CLI"
status: published
summary: "Once a plan is approved, Droid enters Mission Control. Monitor progress, unblock workers, and redirect the orchestrator from the terminal."
parent: cli/features/missions/index
tags: [factory-missions, missions, mission-control, orchestrator, intervene, redirect, cli]
relations: [relates_to=jp/cli/features/missions/running-cli]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Running in the CLI</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Once a plan is approved, Droid enters Mission Control. Monitor progress, unblock workers, and redirect the orchestrator from the terminal.</p>


## Working with Mission Control {#working-with-mission-control}

Once the plan is approved, Droid enters Mission Control -- the orchestration view that manages execution. From here you can track progress across features and milestones, see which agents are working on what, and intervene when things need adjustment.



<Aside kind="tip">
Prefer a visual dashboard? The Desktop and Web apps provide a richer Mission Control experience. See [[web/missions|Running in the Desktop/Web]].
</Aside>



## Intervening and redirecting {#intervening-and-redirecting}

Missions are not fire-and-forget. The orchestrator is an agent, and you can talk to it. The most effective way to use Missions is to treat yourself as the project manager -- monitoring progress, unblocking workers, and redirecting when the plan needs to change.

When something goes wrong -- the mission freezes, a worker or milestone gets stuck, or you need to change direction -- pause the orchestrator and tell it what you are seeing. See [[features/missions/troubleshooting|Troubleshooting]] for common scenarios and example prompts.

## A new kind of debugging {#a-new-kind-of-debugging}

The skillset for working with Missions looks less like traditional debugging and more like **project management of agents**. You are not stepping through code line by line -- you are monitoring a team of workers, unblocking them when they get stuck, redirecting them when priorities change, and making judgment calls about when to push through versus when to re-plan.

This is a meaningfully different way of working with AI. The core skill is knowing when and how to intervene, not writing the code yourself.

## See also {#see-also}

- [[web/missions|Running in the Desktop/Web]] -- The visual Mission Control dashboard
- [[features/missions/reference|Configuration & Reference]] -- Headless execution, settings, and enterprise policy
- [[features/missions/planning|Planning & Validation]] -- Get the upfront plan right
