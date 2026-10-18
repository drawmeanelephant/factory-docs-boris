---
id: cli/getting-started/quickstart
title: "Quickstart"
status: published
summary: "Get productive with droid in 5 minutes using the interactive terminal UI."
parent: cli/getting-started/index
tags: [quickstart, tutorial, getting-started, droid, cli, install-droid, setup, first-steps]
relations: [relates_to=jp/cli/getting-started/quickstart]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Quickstart</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Get productive with droid in 5 minutes using the interactive terminal UI.</p>


This quickstart guide will have you collaborating with Factory's development agent in just a few minutes. You'll experience how droid understands your codebase, makes thoughtful changes, and integrates with your existing workflow.

## Before you begin {#before-you-begin}

Make sure you have:

- A terminal open in a code project
- Git repository (recommended for full workflow demonstration)

## Step 1: Install and start droid {#step-1-install-and-start-droid}



<div class="factory-codegroup">
<div class="factory-codegroup-bar"><button type="button" class="factory-codegroup-tab is-active" data-tab-idx="0">macOS/Linux</button><button type="button" class="factory-codegroup-tab" data-tab-idx="1">Homebrew</button><button type="button" class="factory-codegroup-tab" data-tab-idx="2">Windows</button><button type="button" class="factory-codegroup-tab" data-tab-idx="3">npm</button></div>

<div class="factory-codegroup-panel is-active" data-panel-idx="0">

```bash
curl -fsSL https://app.factory.ai/cli | sh
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="1">

```bash
brew install --cask droid
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="2">

```powershell
irm https://app.factory.ai/cli/windows | iex
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="3">

```bash
npm install -g droid
```

</div>

</div>





<Aside kind="note">
**Linux users:** Ensure `xdg-utils` is installed for proper functionality. Install with: `sudo apt-get install xdg-utils`
</Aside>



Then navigate to your project and start the Droid CLI.



<div class="factory-codegroup">

```bash
# Navigate to your project
cd /path/to/your/project

# Start interactive session
droid
```

</div>



<img
  src="../../images/droid_tui_intro.png"
  alt="Droid CLI"
  height="450"
  class="rounded-lg"
/>

You'll see droid's welcome screen in a full-screen terminal interface. If prompted, sign in via your browser to connect to Factory's development agent.

## Step 2: Explore your codebase {#step-2-explore-your-codebase}

Let's start by having droid understand your project. Try one of these questions:

```

> analyze this codebase and explain the overall architecture

```

```

> what technologies and frameworks does this project use?

```

```

> where are the main entry points and how is testing set up?

```

Droid reads your files contextually and leverages organizational knowledge to provide comprehensive insights about your project structure and conventions.

## Step 3: Make your first code change {#step-3-make-your-first-code-change}

Now let's see droid in action with a simple modification:

```

> add comprehensive logging to the main application startup

```

Droid will:

1. Analyze your current logging setup
2. Propose specific changes with a clear plan
3. Show you exactly what will be modified
4. Wait for your approval before making changes

This transparent review process ensures you maintain full control over all code modifications.

## Step 4: Experience enterprise workflows {#step-4-experience-enterprise-workflows}

Try a more complex task that showcases droid's enterprise capabilities:

```

> audit this codebase for security vulnerabilities and create a remediation plan

```

Or provide context from your team's tools by pasting a link:

```

> implement the feature described in this Jira ticket: https://company.atlassian.net/browse/PROJ-123

```

If you've integrated these platforms through Factory's dashboard, droid can automatically read context from Jira, Notion, Slack, and other sources. Droid can also connect to additional tools via MCP integrations for even more capabilities.

## Step 5: Handle version control {#step-5-handle-version-control}

Droid makes Git operations conversational and intelligent:

```

> review my uncommitted changes and suggest improvements before I commit

```

```

> create a well-structured commit with a descriptive message following our team conventions

```

```

> analyze the last few commits and identify any potential issues or patterns

```

## Essential controls {#essential-controls}

Here are the key interactions you'll use daily:

| Action            | What it does                                          | How to use                                   |
| ----------------- | ----------------------------------------------------- | -------------------------------------------- |
| Send message      | Submit a task or question                             | Type and press **Enter**                     |
| Multi-line input  | Write longer prompts                                  | **Shift\+Enter** for new lines               |
| Approve changes   | Accept proposed modifications                         | Accept change in the TUI                     |
| Reject changes    | Decline proposed modifications                        | Reject change in the TUI                     |
| Switch modes      | Toggle between modes                                  | **Shift\+Tab**                               |
| Bash mode         | Run shell commands directly without AI interpretation | Press `!` on an empty input; `Esc` to return |
| Transcript view   | Toggle detailed transcript with full message details  | **Ctrl+O**                                   |
| Mission control   | Toggle Mission Control overlay (orchestrator sessions)| **Ctrl+T**                                   |
| Close overlay     | Dismiss the active overlay or menu                    | **Escape**                                   |
| Scroll transcript | Navigate through previous turns                       | **Alt+Up** / **Alt+Down**                    |
| View shortcuts    | See all available commands                            | Press **?**                                  |
| Exit session      | Leave droid                                           | **Ctrl\+C** or type `exit`                   |

### Useful slash commands {#useful-slash-commands}

Quick shortcuts to common actions:

- `/review` - Start AI-powered code review workflow ([[cli/features/code-review|learn more]])
- `/settings` - Configure droid behavior, models, and preferences
- `/model` - Switch between AI models mid-session
- `/sessions` - List and resume previous sessions
- `/fork` - Fork the current session into a new branch
- `/compress` - Compress/compact the current session to free up context
- `/missions` - Open the Missions menu to launch multi-agent projects
- `/droids` - Manage custom Droids (specialized subagents)
- `/skills` - Manage prompt-based skills (reusable procedures)
- `/hooks` - Manage tool execution hooks for lifecycle automation
- `/plugins` - Manage plugins and marketplaces
- `/mcp` - Manage Model Context Protocol servers
- `/account` - Open your Factory account settings in browser
- `/billing` - View and manage your billing settings
- `/help` - See all available commands

[[cli/configuration/custom-slash-commands|Learn how to create custom slash commands →]]

## Collaboration best practices {#collaboration-best-practices}

**Be specific with context:**
Instead of: "fix the bug"
Try: "fix the authentication timeout issue where users get logged out after 5 minutes instead of the configured 30 minutes"

**Use spec mode for complex features:**
For larger features, use [[cli/user-guides/specification-mode|Specification Mode]] which automatically provides planning before implementation without needing to explicitly request it.

**Leverage organizational knowledge:**

```

> following our team's coding standards, implement the user preferences feature described in ticket PROJ-123

```

**Use the review workflow:**
Always review droid's proposed changes before approval. The transparent diff view helps you understand exactly what will be modified.

## Pro tips for enterprise teams {#pro-tips-for-enterprise-teams}

**Security-first approach:**
Droid automatically considers security implications and will flag potential vulnerabilities during code generation.

**Compliance integration:**
Connect your compliance tools through MCP to ensure all changes meet your organization's standards.

**Team knowledge sharing:**
Droid learns from your organization's patterns and can help maintain consistency across team members and projects.

## What's next? {#whats-next}



<div class="factory-card-group">

<div class="factory-card">

**[[cli/getting-started/common-use-cases|Common Use Cases]]**

Explore real-world scenarios and workflows

</div>


  

<div class="factory-card">

**[[cli/configuration/settings|Configuration]]**

Customize droid for your team's workflow

</div>


  

<div class="factory-card">

**[[cli/configuration/agents-md|AGENTS.md Guide]]**

Document your project conventions and commands

</div>


  

<div class="factory-card">

**[[integrations/ide-integrations|IDE Integration]]**

Use droid within your favorite editor

</div>

</div>
