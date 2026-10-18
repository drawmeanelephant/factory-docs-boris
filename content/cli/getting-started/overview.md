---
id: cli/getting-started/overview
title: "Overview"
status: published
summary: "Meet `droid` — the power of Factory in your terminal"
parent: cli/getting-started/index
tags: [droid, cli, terminal, command-line, factory-cli, droid-cli, install, setup]
relations: [relates_to=jp/cli/getting-started/overview]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Overview</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Meet `droid` — the power of Factory in your terminal</p>

## Get started in 30 seconds {#get-started-in-30-seconds}



<div class="factory-codegroup">
<div class="factory-codegroup-bar"><button type="button" class="factory-codegroup-tab is-active" data-tab-idx="0">macOS/Linux</button><button type="button" class="factory-codegroup-tab" data-tab-idx="1">Windows</button><button type="button" class="factory-codegroup-tab" data-tab-idx="2">npm</button></div>

<div class="factory-codegroup-panel is-active" data-panel-idx="0">

```bash
curl -fsSL https://app.factory.ai/cli | sh
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="1">

```powershell
irm https://app.factory.ai/cli/windows | iex
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="2">

```bash
npm install -g droid
```

</div>

</div>



Then navigate to your project and start the Droid CLI.



<div class="factory-codegroup">

```bash
# Navigate to your project
cd /path/to/your/project

# Start interactive session
droid
```

</div>



You're now connected to Factory's development agent from your terminal. [[cli/getting-started/quickstart|Try the 5-minute quickstart →]]



<Aside kind="note">
**Quick tip:** Press `!` to toggle bash mode and run shell commands directly without AI interpretation. Press `Esc` to return to normal mode. See the [[reference/cli-reference#bash-mode|CLI Reference]] for details.
</Aside>



## Key capabilities {#key-capabilities}

- **Missions**: Launch multi-agent projects where an orchestrator coordinates specialized worker droids to plan, implement, and validate larger features. Start one with `/missions` or run headlessly with `droid exec --mission`. [[features/missions/overview|Learn more →]]
- **MCP**: Connect droid to external tools and data sources through the Model Context Protocol. Add servers with `droid mcp add` or manage them via `/mcp`. [[cli/configuration/mcp|Learn more →]]
- **Custom Droids**: Define specialized subagents with their own system prompts, tools, and models for delegated tasks. Manage them through `/droids`. [[cli/configuration/custom-droids|Learn more →]]
- **Skills**: Package reusable procedures and domain knowledge that droid can invoke on demand. Browse and create skills with `/skills` or `/create-skill`. [[cli/configuration/skills|Learn more →]]
- **Hooks**: Automate behavior around the agent lifecycle by running shell commands before or after specific tool events. Configure them with `/hooks`. [[cli/configuration/hooks-guide|Learn more →]]
- **Plugins**: Extend droid with installable bundles of slash commands, droids, skills, and hooks distributed through marketplaces. Install with `droid plugin install` or manage via `/plugins`. [[cli/configuration/plugins|Learn more →]]
- **Exec Mode**: Run droid headlessly for scripts, CI/CD pipelines, and automation. Use `droid exec` with structured input and output formats. [[cli/droid-exec/overview|Learn more →]]

## What `droid` brings to your workflow {#what-droid-brings-to-your-workflow}

- **End-to-end feature development**: From planning to implementation to testing - droid handles the complete development lifecycle while keeping you in control through transparent review workflows.
- **Deep codebase understanding**: Leverages your organization's shared knowledge across repositories, documentation, and issue tracking to provide contextually aware assistance that improves over time.
- **Engineering system integration**: Connects directly to your existing tools — with native integrations to Jira, Notion, Slack, and many more tools — so development work stays synchronized with your team's processes.
- **Production-ready automation**: Deploy the same workflows locally during development or in CI/CD pipelines, with enterprise security and compliance built-in from day one.

## Why teams choose Factory {#why-teams-choose-factory}

- **Built for enterprise**: On-premise deployment options, SOC-2 compliance, and air-gapped environments. We prioritize security and quality over racing to the lowest price point.
- **Your tools, enhanced**: Works within your existing terminal, IDE, and development environment. No need to switch editors or learn new interfaces — droid integrates where you're already productive.
- **Transparent and controllable**: Every decision droid makes is visible and reviewable. You maintain full oversight of code changes with our native diff viewer and approval workflows.
- **Model flexibility**: Not locked into a single AI provider. Factory allows you to route tasks to the best model for each job while maintaining consistent behavior and memory across your organization.

## Next steps {#next-steps}



<div class="factory-card-group">

<div class="factory-card">

**[[cli/getting-started/quickstart|Quickstart]]**

See droid in action with practical examples

</div>


  

<div class="factory-card">

**[[cli/getting-started/common-use-cases|Common Use Cases]]**

Step-by-step guides for common workflows

</div>


  

<div class="factory-card">

**[[integrations/ide-integrations|IDE Integration]]**

Add droid to your IDE

</div>


  

<div class="factory-card">

**[[cli/configuration/settings|Configuration]]**

Customize droid for your workflow

</div>

</div>



## Additional resources {#additional-resources}



<div class="factory-card-group">

<div class="factory-card">

**[[cli/configuration/agents-md|AGENTS.md Guide]]**

Configure project-specific guidance and conventions

</div>


  

<div class="factory-card">

**[[reference/cli-reference|CLI Reference]]**

Complete reference for droid commands

</div>

</div>
