---
id: integrations/ide-integrations
title: "IDE Integrations"
status: published
summary: "Run droid directly inside your editor for richer context and a smoother workflow."
parent: integrations/index
tags: [integrations]
relations: [relates_to=jp/integrations/ide-integrations]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">IDE Integrations</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Run droid directly inside your editor for richer context and a smoother workflow.</p>


Droid works great with any Integrated Development Environment (IDE) that has a terminal. Just run `droid`, and you're ready to go.

Droid also provides dedicated plugins for Visual Studio Code (including Cursor and Windsurf) and JetBrains IDEs. For JetBrains IDEs such as IntelliJ IDEA, PyCharm, Android Studio, WebStorm, PhpStorm, and GoLand, you can install the official Factory Droid plugin for enhanced integration, or just run `droid` in the integrated terminal.

## Features {#features}

- **Quick launch**: Use keyboard shortcuts to open Droid directly from your editor, or click the Droid button in the UI
- **Diff viewing**: Code changes can be displayed directly in the IDE diff viewer instead of the terminal
- **Selection context**: The current selection/tab in the IDE is automatically shared with Droid
- **File reference shortcuts**: Use keyboard shortcuts to insert file references
- **Diagnostic sharing**: Diagnostic errors (lint, syntax, etc.) from the IDE are automatically shared with Droid as you work

## Installation {#installation}

### VS Code {#vs-code}

To install Droid on VS Code and supported forks (Cursor, Windsurf):

1. Open VS Code
2. Open the integrated terminal
3. Run `droid` - the extension will auto-install



<Aside kind="note">
You can install the [VS Code Extension
  here](https://marketplace.visualstudio.com/items?itemName=Factory.factory-vscode-extension).
</Aside>



### Other IDEs {#other-ides}



<div class="factory-card-group">

<div class="factory-card">

**[[integrations/jetbrains|JetBrains IDEs]]**

Step-by-step setup and usage for IntelliJ IDEA, PyCharm, WebStorm, and other
JetBrains IDEs.

</div>


  

<div class="factory-card">

**[[integrations/zed|Zed]]**

Configure Factory Droid as a custom agent in Zed with MCP servers and Agent
Panel workflows.

</div>

</div>



## Usage {#usage}

### From your IDE {#from-your-ide}

Run `droid` from your IDE's integrated terminal, and all features will be active.

### The `/ide` Command {#the-ide-command}

Use the `/ide` command within droid to manage your IDE integrations:

```
/ide
```

This command will:

- Show the current extension version if installed
- Prompt to install the extension if not yet installed
- Works with VS Code, Cursor, and Windsurf

## Troubleshooting {#troubleshooting}

### VS Code extension not installing {#vs-code-extension-not-installing}

- Ensure you're running Droid from VS Code's integrated terminal
- Ensure that the CLI corresponding to your IDE is installed:
  - For VS Code: `code` command should be available
  - For Cursor: `cursor` command should be available
  - For Windsurf: `windsurf` command should be available
  - If not installed, use `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux) and search for "Shell Command: Install 'code' command in PATH" (or the equivalent for your IDE)
- Check that VS Code has permission to install extensions

### ESC key configuration {#esc-key-configuration}

If the ESC key doesn't interrupt Droid operations in JetBrains terminals:

1. Go to Settings → Tools → Terminal
2. Either:
   - Uncheck "Move focus to the editor with Escape", or
   - Click "Configure terminal keybindings" and delete the "Switch focus to Editor" shortcut
3. Apply the changes

This allows the ESC key to properly interrupt Droid operations.

### Common issues {#common-issues}

| Symptom                                   | Fix                                                                                          |
| ----------------------------------------- | -------------------------------------------------------------------------------------------- |
| **"Editor integration disabled" message** | Verify the VS Code extension is installed or update `editorIntegration` to match your editor |
| CLI cannot find Node/Bun                  | Ensure the `droid` binary is on the PATH VS Code/JetBrains uses (restart after install)      |
| Missing file context                      | Save files; unsaved buffers older than 500 KB are skipped for performance                    |
| Stale diagnostics                         | Run **↻ Refresh Diagnostics** command (VS Code Command Palette)                              |
| VS Code terminal closes immediately       | Check your shell's startup scripts: they must not auto-exit                                  |
| Network blocked in corporate proxy        | Configure proxy variables in settings or set `HTTP_PROXY`/`HTTPS_PROXY` env vars             |

For additional help, email support@factory.ai with logs from `~/.factory/logs/`

## Next steps {#next-steps}



<div class="factory-card-group">

<div class="factory-card">

**[[cli/configuration/settings|Settings]]**

Fine-tune thinking budget, tool permissions, and more.

</div>


  

<div class="factory-card">

**[[cli/user-guides/specification-mode|Specification Mode]]**

See how editor context improves feature delivery.

</div>

</div>
