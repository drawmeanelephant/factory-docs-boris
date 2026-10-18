---
id: cli/getting-started/video-walkthrough
title: "Video Walkthrough"
status: published
summary: "A video tutorial covering installation, configuration, and all key features of the Droid CLI"
parent: cli/getting-started/index
tags: [cli, video, tutorial, walkthrough, demo, guide, learn, watch]
relations: [relates_to=jp/cli/getting-started/video-walkthrough]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Video Walkthrough</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">A video tutorial covering installation, configuration, and all key features of the Droid CLI</p>


<iframe
  class="w-full aspect-video rounded-xl"
  src="https://youtube.com/embed/aw0thMXwAMY"
  title="Factory Video Walkthrough"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
></iframe>

## Installation & Setup {#installation-setup}

Get started by installing the Droid CLI in your terminal of choice.



<div class="factory-codegroup">
<div class="factory-codegroup-bar"><button type="button" class="factory-codegroup-tab is-active" data-tab-idx="0">macOS/Linux</button><button type="button" class="factory-codegroup-tab" data-tab-idx="1">Windows</button></div>

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

</div>



Verify the installation:

```bash
which droid
```

Start the Droid CLI:

```bash
cd /path/to/your/project
droid
```

### First-Time Authentication {#first-time-authentication}

On your first run, you'll see an onboarding screen:

1. Choose to create an account or log in
2. Confirm the authentication code in your browser
3. Return to the terminal to start using droid

## Interface & Shortcuts {#interface-shortcuts}

### Help Menu {#help-menu}

Press `Shift + ?` to open the help menu, which shows:

- How to send messages and create new lines
- Available keyboard shortcuts
- Basic navigation commands
- Autonomy mode options



<Aside kind="note">
**Terminal-specific key bindings**: The default for new lines is `\` + `Enter`, but you can configure this to `Shift + Enter` or other combinations based on your terminal's key bindings. Check `/terminal-setup` in the CLI for configuration options.
</Aside>



### Essential Keyboard Shortcuts {#essential-keyboard-shortcuts}

| Shortcut | Action |
|----------|--------|
| `Enter` | Send message |
| `\` + `Enter` (or `Shift + Enter`) | New line in message |
| `Esc` (double tap) | Clear current input |
| `Shift + ?` | Open help menu |
| `Shift + Tab` | Cycle through autonomy modes |
| `!` on empty input | Toggle Bash mode for direct shell commands |
| `/` | Open command menu |
| `Cmd + Shift + H` | Show root directory |
| `Cmd + Shift + .` | Show hidden files/folders |
| `Ctrl + C` or `exit` | Exit droid |
| `Ctrl + V` | Paste image |



<Aside kind="note">
The paste image shortcut works across all terminals, though the specific key binding may vary based on your terminal configuration.
</Aside>





<Aside kind="note">
In Bash mode, the prompt changes to `$`. Type a shell command and press `Enter`, then press `Esc` to return to normal chat.
</Aside>



## Autonomy Modes {#autonomy-modes}

Cycle through different autonomy levels by pressing `Shift + Tab`:

[[cli/user-guides/specification-mode|Learn more about Specification Mode →]]





<Details summary="Spec Mode (Research & Plan Only)">
Droid will research and create a plan without making any changes. Perfect for understanding what will happen before execution.

  - No file edits
  - No command execution
  - Creates detailed specifications
  - Allows iteration on plans before proceeding
</Details>



  

<Details summary="Low Mode (Read-Only + Safe Commands)">
Allows reading files and executing low-risk, read-only commands.

  - File reading
  - Directory listing
  - Safe diagnostic commands
  - No modifications
</Details>



  

<Details summary="Medium Mode (File Edits Allowed)">
Enables file modifications and medium-risk commands that are easily reversible.

  - Create/edit/delete files
  - Run build commands
  - Execute tests
  - Reversible operations
</Details>



  

<Details summary="High Mode (All Commands with Safeguards)">
Allows all commands but still maintains safety through allow/deny lists.

  - Full command execution
  - File removal operations (with confirmation)
  - Git operations
  - Configurable via allow/deny lists
</Details>







<Aside kind="warning">
Even in High mode, certain dangerous operations (like removing files) will always require your approval unless you explicitly configure them in the allow list.
</Aside>



[[cli/configuration/settings|Configure autonomy settings →]]

## Slash Commands {#slash-commands}

Press `/` to access the command menu with options for:

- **Account & Billing** - Manage your Factory account
- **Model** - Switch between AI models and set reasoning levels
- **Sessions** - View and navigate previous sessions
- **Settings** - Configure CLI preferences
- **Terminal Setup** - Configure key bindings
- **Custom Commands** - Access your [[cli/configuration/custom-slash-commands|custom slash commands]]
- **Droids** - Manage [[cli/configuration/custom-droids|custom sub-agents]]
- **MCP** - Configure [[cli/configuration/mcp|Model Context Protocol integrations]]

### Switching Models {#switching-models}

Access the model menu with `/model`:

1. View available models
2. Switch between models for different tasks
3. Set reasoning level where applicable



<Aside kind="tip">
Different models excel at different tasks. Use reasoning models for complex planning and faster models for routine edits.
</Aside>



[[models|Learn about available models →]]

### Sessions Management {#sessions-management}

Access with `/sessions`:

- View all previous sessions
- Navigate to any past session
- Open sessions in the Factory App
- Continue work from where you left off

Cloud Sync must be enabled in settings for sessions to appear in the Factory App.

## Settings & Configuration {#settings-configuration}

Access settings via `/settings` to customize your experience:

[[cli/configuration/settings|Full settings documentation →]]

### Core Settings {#core-settings}



<div class="factory-card-group">

<div class="factory-card">

**Model & Reasoning**

Choose your default model and reasoning level for new sessions

</div>


  
  

<div class="factory-card">

**Diff Mode**

Configure how code changes are displayed

</div>


  
  

<div class="factory-card">

**GitHub Completion**

Enable/disable GitHub Copilot-style completions

</div>


  
  

<div class="factory-card">

**Cloud Sync**

Sync sessions to Factory web platform

</div>

</div>



### Advanced Settings {#advanced-settings}





<Details summary="Droid Co-Author on PRs">
When enabled, droid will be added as a co-author on pull requests it helps create. You can disable this if you prefer to be the sole author.
</Details>



  

<details class="boris-details">
<summary>Droid Shield</summary>

Protects environment variables and secrets in your code. Prevents accidental commits of sensitive information like API keys, passwords, and tokens.



<Aside kind="warning">
Keep this enabled to protect against security vulnerabilities.
</Aside>



[[cli/account/droid-shield|Learn more about Droid Shield →]]

</details>



  

<Details summary="Save Spec as Markdown">
Automatically saves specifications generated in Spec Mode as markdown files on your machine for reference and documentation.

[[cli/user-guides/specification-mode|Learn more about Specification Mode →]]
</Details>



  

<Details summary="Allow List & Deny List">
Configure which commands require approval even in High autonomy mode. Even on High, file removal operations require confirmation by default.

[[cli/user-guides/auto-run|Learn more about auto-run settings →]]
</Details>





### IDE Integration {#ide-integration}

Install the droid extension for VS Code, Cursor, and other IDEs directly from the settings menu.

[[integrations/ide-integrations|Learn more about IDE integration →]]

## Configuration Files {#configuration-files}

Access your configuration directory by pressing `Cmd + Shift + H` to show your root directory, then `Cmd + Shift + .` to reveal hidden files. Navigate to the `~/.factory/` folder.

### Directory Structure {#directory-structure}

```
~/.factory/
├── config.json          # Model configuration and BYOK
├── settings.json        # CLI settings and allow/deny lists
├── mcp.json            # MCP integrations
├── droids/             # Custom sub-agents
├── commands/           # Custom slash commands
├── logs/               # Session logs
└── bug-reports/        # Crash reports
```



<Aside kind="tip">
Learn more: [[cli/configuration/settings|Settings]] | [[cli/configuration/custom-slash-commands|Custom Slash Commands]] | [[cli/configuration/custom-droids|Custom Droids]] | [[cli/configuration/mcp|MCP Configuration]]
</Aside>



### config.json - Bring Your Own Key {#configjson---bring-your-own-key}

Configure custom models using your own API keys:

```json
{
  "models": [
    {
      "provider": "openrouter",
      "name": "anthropic/claude-3.5-sonnet",
      "apiKey": "your-api-key-here",
      "displayName": "Claude 3.5 Sonnet (OpenRouter)"
    }
  ]
}
```



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Find Provider Documentation</div>

Visit [[cli/byok/overview|Bring Your Own Key documentation]] and select your provider (OpenRouter, Fireworks, etc.)

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Copy Configuration Template</div>

Copy the JSON configuration for your chosen provider

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Add to config.json</div>

Paste the configuration into `~/.factory/config.json` and add your API key

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Select Model</div>

Use `/model` in the CLI to select your newly added model

</div>

</div>



[[cli/byok/overview|See all BYOK providers →]]

### settings.json - Allow & Deny Lists {#settingsjson---allow-deny-lists}

Configure which commands require approval in High autonomy mode:

```json
{
  "autoModeAllow": [],
  "autoModeDeny": [
    "git push",
    "rm -rf",
    "npm publish"
  ]
}
```

Even in High mode, commands in the `autoModeDeny` list will always require your explicit approval before execution.

### mcp.json - MCP Integrations {#mcpjson---mcp-integrations}

Enable or disable MCP tools individually:

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-api-key"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-playwright"],
      "disabled": true
    }
  }
}
```

Set `"disabled": true` to temporarily disable an MCP without removing its configuration.

[[cli/configuration/mcp|Learn more about MCP configuration →]]

## Custom Droids (Sub-Agents) {#custom-droids-sub-agents}

Custom droids are specialized AI agents that handle specific tasks. Access the droids menu with `/droids`:

### Managing Droids {#managing-droids}

- **Import** (`i`) - Import pre-built droids from other agents
- **Create** (`c`) - Create a new custom droid
- **Edit** - Modify existing droid configurations
- **Enable/Disable** - Toggle droids on or off

### Creating a Custom Droid {#creating-a-custom-droid}

[[cli/configuration/custom-droids|Learn more about custom droids →]]



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Choose Scope</div>

Decide if the droid should be **project-level** (specific repository) or **personal** (available across all projects)

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Generation Method</div>

Choose to create manually or generate with droid's help:

```
I want a code review droid that checks for security issues and coding standards
```

Droid will generate an appropriate description and configuration

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Configure Model</div>

- **Inherit**: Use the same model as the parent session
  - **Specific Model**: Choose a dedicated model for this droid (e.g., use a reasoning model for complex analysis)

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Enable Tools</div>

Select which tools and capabilities the droid should have access to

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Save &amp; Edit</div>

Confirm the configuration and optionally edit the details

</div>

</div>



### Example Use Cases {#example-use-cases}

- **Code Review Droid** - Automated code reviews for pull requests
- **Documentation Droid** - Generates and maintains documentation
- **Test Generation Droid** - Creates comprehensive test suites
- **Security Audit Droid** - Scans for vulnerabilities and security issues

## MCP Integrations {#mcp-integrations}

Model Context Protocol (MCP) allows droid to integrate with external tools and data sources.

### Adding MCPs via CLI {#adding-mcps-via-cli}

Use the `/mcp add` command:

```bash
/mcp add
```

Then provide the MCP details:
- **Name**: Identifier for the MCP
- **Command**: Executable command (e.g., `npx`, `python`)
- **Args**: Command arguments
- **Environment Variables**: API keys and configuration

### Listing Configured MCPs {#listing-configured-mcps}

```bash
/mcp list
```

This connects to each configured MCP server and reports its current connection status: **connected**, **connecting**, **needs authentication**, or **failed**. Servers that require OAuth show **needs authentication** until you complete the sign-in flow in the interactive `/mcp` manager.



<Aside kind="note">
After adding or modifying MCPs, you may need to restart the CLI for changes to take effect.
</Aside>



### Adding MCPs via Configuration File {#adding-mcps-via-configuration-file}

You can also directly edit `~/.factory/mcp.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token-here"
      }
    }
  }
}
```

### Popular MCP Integrations {#popular-mcp-integrations}

- **Brave Search** - Web search capabilities
- **Playwright** - Browser automation
- **GitHub** - Repository and issue management
- **Filesystem** - Extended file system access
- **Postgres** - Database queries
- **Slack** - Team communication

[[cli/configuration/mcp|Browse all MCP servers →]]

## Example Workflow: Spec Mode to Implementation {#example-workflow-spec-mode-to-implementation}

Here's a complete workflow demonstrating droid's capabilities:



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Start in Spec Mode</div>

Press `Shift + Tab` until you're in Spec mode

```
Create an authentication system with GitHub and Google OAuth
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Review the Plan</div>

Droid generates a detailed specification:
  - Architecture decisions
  - Files to create/modify
  - Dependencies needed
  - Implementation steps

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Iterate on the Spec</div>

Refine the plan before implementation:

```
Change the plan to only include Github auth and not Google auth
```

Droid updates the specification accordingly

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Approve and Proceed</div>

Once satisfied with the plan, proceed with High mode to implement

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Review Changes</div>

Droid shows exactly what will change and waits for your approval

</div>

</div>





<Aside kind="tip">
Spec mode is especially powerful for complex features. It allows you to validate the approach before any code is written.
</Aside>



[[cli/user-guides/specification-mode|Read the full Specification Mode guide →]]

[[cli/user-guides/implementing-large-features|Learn about implementing large features →]]

## Summary {#summary}

You've learned how to:

- Install and authenticate with the Droid CLI
- Navigate the interface and use keyboard shortcuts
- Understand and switch between autonomy modes
- Configure settings and preferences
- Add custom models with BYOK
- Create and manage custom droids (sub-agents)
- Integrate external tools via MCP
- Use spec mode for planning before implementation

## Next Steps {#next-steps}



<div class="factory-card-group">

<div class="factory-card">

**[[cli/getting-started/how-to-talk-to-a-droid|How to Talk to a Droid]]**

Learn best practices for communicating with droid

</div>


  
  

<div class="factory-card">

**[[cli/getting-started/common-use-cases|Common Use Cases]]**

Explore real-world workflows and scenarios

</div>


  
  

<div class="factory-card">

**[[cli/user-guides/become-a-power-user|Become a Power User]]**

Advanced techniques and productivity tips

</div>


  
  

<div class="factory-card">

**[[cli/configuration/agents-md|AGENTS.md Guide]]**

Document project-specific conventions

</div>

</div>
