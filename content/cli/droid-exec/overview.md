---
id: cli/droid-exec/overview
title: "Droid Exec (Headless)"
status: published
summary: "Non-interactive execution mode for CI/CD pipelines and automation scripts."
parent: cli/droid-exec/index
tags: [cli, droid-exec, headless, ci-cd, automation, pipeline, github-actions, scripts]
relations: [relates_to=jp/cli/droid-exec/overview]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Droid Exec (Headless)</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Non-interactive execution mode for CI/CD pipelines and automation scripts.</p>


Droid Exec is Factory's headless execution mode designed for automation workflows. Unlike the interactive CLI, `droid exec` runs as a one-shot command that completes a task and exits, making it ideal for CI/CD pipelines, shell scripts, and batch processing.



<Aside kind="tip">
Explore the [[guides/droid-exec/code-review|Droid Exec cookbooks]].
</Aside>



## Summary and goals {#summary-and-goals}

Droid Exec is a one-shot task runner designed to:

- Produce readable logs, and structured artifacts when requested
- Enforce opt-in for mutations/command execution (secure-by-default)
- Fail fast on permission violations with clear errors
- Support simple composition for batch and parallel work



<div class="factory-card-group">

<div class="factory-card">

**Non-Interactive**

Single run execution that writes to stdout/stderr for CI/CD integration

</div>


  

<div class="factory-card">

**Secure by Default**

Read-only by default with explicit opt-in for mutations via autonomy levels

</div>


  

<div class="factory-card">

**Composable**

Designed for shell scripting, parallel execution, and pipeline integration

</div>


  

<div class="factory-card">

**Clean Output**

Structured output formats and artifacts for automated processing

</div>

</div>



## Execution model {#execution-model}

- Non-interactive single run that writes to stdout/stderr.
- Default is spec-mode: the agent is only allowed to execute read-only operations.
- Add `--auto` to enable edits and commands; risk tiers gate what can run.

CLI help (excerpt):

```
Usage: droid exec [options] [prompt]

Execute a single command (non-interactive mode)

Arguments:
  prompt                          The prompt to execute

Options:
  -o, --output-format <format>          Output format (default: "text")
  --input-format <format>               Input format: stream-jsonrpc for multi-turn sessions
  -f, --file <path>                     Read prompt from file
  --auto <level>                        Autonomy level: low|medium|high
  --skip-permissions-unsafe             Skip ALL permission checks - allows all permissions (unsafe)
  -s, --session-id <id>                 Existing session to continue (requires a prompt)
  --fork <id>                           Fork an existing session and continue from it
  -m, --model <id>                      Model ID to use
  -r, --reasoning-effort <level>        Reasoning effort (defaults per model)
  --spec-model <id>                     Model ID to use for spec mode
  --spec-reasoning-effort <level>       Reasoning effort for spec mode
  --use-spec                            Start in spec mode
  --restrict-tools <ids>                Restrict the run to only the specified tools (comma or space separated list)
  --additional-tools <ids>              Enable additional tools beyond the defaults (comma or space separated list)
  --disabled-tools <ids>                Disable specific tools (comma or space separated list)
  --disable-builtin-skills              Disable Factory-provided builtin skills for this session
  --list-tools                          List available tools for the selected model and exit
  --cwd <path>                          Working directory path
  -w, --worktree [name]                 Run in a git worktree
  --worktree-dir <path>                 Directory for worktree creation
  --tag <spec>                          Session tag (name or JSON, repeatable)
  --log-group-id <id>                   Log group ID for filtering logs
  --append-system-prompt <text>         Append custom text to end of system prompt
  --append-system-prompt-file <path>    Append file contents to end of system prompt
  --mission                             Run in mission mode (multi-agent orchestration)
  --worker-model <id>                   Model for mission workers
  --worker-reasoning-effort <level>     Reasoning effort for mission workers
  --validator-model <id>                Model for mission validators
  --validator-reasoning-effort <level>  Reasoning effort for mission validators
  -h, --help                            display help for command
```

Use any [[models|available model ID]] with `--model` or `--spec-model`. For custom models, see [[cli/byok/overview|Bring Your Own Key (BYOK)]].

## Installation {#installation}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Install the Droid CLI</div>



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



</div>



  

<div class="factory-step">

<div class="factory-step-title">Get Factory API Key</div>

Generate your API key from the [Factory Settings Page](https://app.factory.ai/settings/api-keys)

</div>



  

<div class="factory-step">

<div class="factory-step-title">Set Environment Variable</div>

Export your API key as an environment variable:
```bash
export FACTORY_API_KEY=fk-...
```

</div>

</div>



## Quickstart {#quickstart}

- Direct prompt:
  - `droid exec "analyze code quality"`
  - `droid exec "fix the bug in src/main.js" --auto low`
- From file:
  - `droid exec -f prompt.md`
- Pipe:
  - `echo "summarize repo structure" | droid exec`
- Session continuation:
  - `droid exec --session-id <session-id> "continue with next steps"`

## Autonomy Levels {#autonomy-levels}

Droid exec uses a tiered autonomy system to control what operations the agent can perform. By default, it runs in read-only mode, requiring explicit flags to enable modifications.

### DEFAULT (no flags) - Read-only Mode {#default-no-flags---read-only-mode}
The safest mode for reviewing planned changes without execution:
- ✅ Reading files or logs: cat, less, head, tail, systemctl status
- ✅ Display commands: echo, pwd
- ✅ Information gathering: whoami, date, uname, ps, top
- ✅ Git read operations: git status, git log, git diff
- ✅ Directory listing: ls, find (without -delete or -exec)
- ❌ No modifications to files or system
- **Use case:** Safe for reviewing what changes would be made

```bash
# Analyze and plan refactoring without making changes
droid exec "Analyze the authentication system and create a detailed plan for migrating from session-based auth to OAuth2. List all files that would need changes and describe the modifications required."

# Review code quality and generate report
droid exec "Review the codebase for security vulnerabilities, performance issues, and code smells. Generate a prioritized list of improvements needed."

# Understand project structure
droid exec "Analyze the project architecture and create a dependency graph showing how modules interact with each other."
```

### `--auto low` - Low-risk Operations {#auto-low---low-risk-operations}
Enables basic file operations while blocking system changes:
- ✅ File creation/editing in project directories
- ❌ No system modifications or package installations
- **Use case:** Documentation updates, code formatting, adding comments

```bash
# Safe file operations
droid exec --auto low "add JSDoc comments to all functions"
droid exec --auto low "fix typos in README.md"
```

### `--auto medium` - Development Operations {#auto-medium---development-operations}
Operations that may have significant side effects, but these side effects are typically harmless and straightforward to recover from.
Adds common development tasks to low-risk operations:
- Installing packages from trusted sources: npm install, pip install (without sudo)
- Network requests to trusted endpoints: curl, wget to known APIs
- Git operations that modify local repositories: git commit, git checkout, git pull (but not git push)
- Building code with tools like make, npm run build, mvn compile
- ❌ No git push, sudo commands, or production changes
- **Use case:** Local development, testing, dependency management

```bash
# Development tasks
droid exec --auto medium "install deps, run tests, fix issues"
droid exec --auto medium "update packages and resolve conflicts"
```

### `--auto high` - Production Operations {#auto-high---production-operations}
Commands that may have security implications such as data transfers between untrusted sources or execution of unknown code, or major side effects such as irreversible data loss or modifications of production systems/deployments.
- Running arbitrary/untrusted code: curl | bash, eval, executing downloaded scripts
- Exposing ports or modifying firewall rules that could allow external access
- Git push operations that modify remote repositories: git push, git push --force
- Irreversible actions to production deployments, database migrations, or other sensitive operations
- Commands that access or modify sensitive information like passwords or keys
- ❌ Still blocks: sudo rm -rf /, system-wide changes
- **Use case:** CI/CD pipelines, automated deployments

```bash
# Full workflow automation
droid exec --auto high "fix bug, test, commit, and push to main"
droid exec --auto high "deploy to staging after running tests"
```

### `--skip-permissions-unsafe` - Bypass All Checks {#skip-permissions-unsafe---bypass-all-checks}


<Aside kind="warning">
DANGEROUS: This mode allows ALL operations without confirmation. Only use in completely isolated environments like Docker containers or throwaway VMs.
</Aside>



- ⚠️ Allows ALL operations without confirmation
- ⚠️ Can execute irreversible operations
- Cannot be combined with --auto flags
- **Use case:** Isolated environments

```bash
# In a disposable Docker container for CI testing
docker run --rm -v $(pwd):/workspace alpine:latest sh -c "
  apk add curl bash &&
  curl -fsSL https://app.factory.ai/cli | sh &&
  droid exec --skip-permissions-unsafe 'Install all system dependencies, modify system configs, run integration tests that require root access, and clean up test databases'
"

# In ephemeral GitHub Actions runner for rapid iteration
# where the runner is destroyed after each job
droid exec --skip-permissions-unsafe "Modify /etc/hosts for test domains, install custom kernel modules, run privileged container tests, and reset network interfaces"

# In a temporary VM for security testing
droid exec --skip-permissions-unsafe "Run penetration testing tools, modify firewall rules, test privilege escalation scenarios, and generate security audit reports"
```

### Fail-fast Behavior {#fail-fast-behavior}

If a requested action exceeds the current autonomy level, droid exec will:
1. Stop immediately with a clear error message
2. Return a non-zero exit code
3. Not perform any partial changes

This ensures predictable behavior in automation scripts and CI/CD pipelines.

## Output formats and artifacts {#output-formats-and-artifacts}

Droid exec supports three output formats for different use cases:

### text (default) {#text-default}
Human-readable output for direct consumption or logs:

```bash
$ droid exec --auto low "create a python file that prints 'hello world'"
Perfect! I've created a Python file named `hello_world.py` in your home directory that prints 'hello world' when executed.
```

### json {#json}
Structured JSON output for parsing in scripts and automation:

```bash
$ droid exec "summarize this repository" --output-format json
{
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "duration_ms": 5657,
  "num_turns": 1,
  "result": "This is a Factory documentation repository containing guides for CLI tools, web platform features, and onboarding procedures...",
  "session_id": "8af22e0a-d222-42c6-8c7e-7a059e391b0b"
}
```

Use JSON format when you need to:
- Parse the result in a script
- Check success/failure programmatically
- Extract session IDs for continuation
- Process results in a pipeline

### Build custom flows on raw JSON-RPC {#build-custom-flows-on-raw-json-rpc}

For custom integrations, you can run Droid as a long-lived subprocess and drive the full JSON-RPC control surface over stdin/stdout:

```bash
droid exec --input-format stream-jsonrpc --output-format stream-jsonrpc
```

In this long-lived JSON-RPC mode, CLI flags such as `--auto`, `--model`,
`--reasoning-effort`, and `--disable-builtin-skills` are validated but do not
configure sessions. Set autonomy, model, reasoning effort, and skill settings
in your JSON-RPC session requests instead. In particular, adding `--auto low`
to the launch command does not limit the session's permissions.

This is the lowest-level integration path for building your own interaction model around Droid. Your process can send turns, stream assistant output, handle permissions, update settings, manage MCP/tools, interrupt work, and resume or fork sessions.

Each stdin line is one JSON-RPC request. Each stdout line is a JSON-RPC response, server request, or notification. A custom client typically:

- Spawns `droid exec` with the project `cwd` and desired flags
- Writes newline-delimited JSON-RPC requests with unique IDs
- Starts with `droid.initialize_session` or `droid.load_session`
- Sends turns with `droid.add_user_message`
- Reads stdout line-by-line and matches responses by `id`
- Handles `droid.session_notification` events for assistant text deltas, tool events, token usage, errors, and turn completion
- Responds to server-to-client requests such as `droid.request_permission` and `droid.ask_user`
- Calls other session methods to interrupt work, update settings, manage MCP servers/tools, inspect context, fork sessions, or compact history
- Implements timeouts, process cleanup, and session persistence

You can build on top of raw stdin/stdout to create custom interaction flows such as:

- Web, desktop, or IDE agent experiences with your own UX and controls
- Chat or copiloting surfaces that route user actions into Droid turns
- CI and workflow runners that execute Droid tasks and surface progress in build logs
- Orchestrators that queue work, resume sessions, fork conversations, and persist results
- Policy layers that approve, deny, transform, or audit tool permission requests
- Bridges from Droid events into your own protocol, message bus, telemetry, or storage layer

To disable Factory-provided builtin skills, set `disableBuiltinSkills` when initializing or loading the session:

```json
{"jsonrpc":"2.0","id":"1","method":"droid.initialize_session","params":{"machineId":"my-machine","cwd":"/workspace","disableBuiltinSkills":true}}
{"jsonrpc":"2.0","id":"2","method":"droid.load_session","params":{"sessionId":"session-123","disableBuiltinSkills":true}}
```

In stream JSON-RPC mode, use the request field instead of the `--disable-builtin-skills` CLI flag. The TypeScript SDK exposes the same option through `createSession({ disableBuiltinSkills: true })` and `resumeSession(sessionId, { disableBuiltinSkills: true })`.

For protocol reference and implementation patterns, see the low-level client and process transport in the [TypeScript SDK](https://github.com/Factory-AI/droid-sdk-typescript).

Prefer an SDK when possible:

- **TypeScript**: [`@factory/droid-sdk`](https://github.com/Factory-AI/droid-sdk-typescript) for Node.js apps, streaming, multi-turn sessions, structured output, permissions, tool controls, and SDK-backed MCP tools
- **Python**: [`droid-sdk`](https://github.com/Factory-AI/droid-sdk-python) for asyncio apps, streaming, direct client control, notifications, permissions, and typed event handling

For automated pipelines, you can also direct the agent to write specific artifacts:

```bash
droid exec --auto low "Analyze dependencies and write to deps.json"
droid exec --auto low "Generate metrics report in CSV format to metrics.csv"
```

## Working directory {#working-directory}

- Use `--cwd` to scope execution:

```
droid exec --cwd /home/runner/work/repo "Map internal packages and dump graphviz DOT to deps.dot"
```

- Use `-w, --worktree [name]` to run the task inside an isolated [[reference/cli-reference#git-worktrees|git worktree]] on its own branch. This is useful for fanning out parallel `droid exec` jobs against the same repo without file conflicts:

```bash
droid exec --worktree codemod-a --auto medium "apply codemod A" &
droid exec --worktree codemod-b --auto medium "apply codemod B" &
wait
```

Clean worktrees are auto-removed on exit; dirty ones are preserved so you can review and push the work.

## Models and reasoning effort {#models-and-reasoning-effort}

Choose a model with `-m` and adjust reasoning with `-r`. See the [[models|Available Models]] for available models.

```bash
droid exec -m claude-sonnet-4-5-20250929 -r medium -f plan.md
```

Use `--use-spec` to start in specification mode, where the agent plans before executing:

```bash
droid exec --use-spec --auto low "refactor the auth module"
```

You can also use a different model for the spec phase:

```bash
droid exec --use-spec --spec-model claude-haiku-4-5-20251001 --auto medium "implement feature X"
```

### Tool controls {#tool-controls}

List available tools for a model:

```bash
droid exec --list-tools
droid exec --model gpt-5-codex --list-tools --output-format json
```

Enable or disable specific tools:

```bash
# Restrict to only specific tools
droid exec --restrict-tools ApplyPatch "refactor files"

# Enable additional tools
droid exec --additional-tools ApplyPatch "refactor files"

# Disable specific tools
droid exec --auto medium --disabled-tools execute-cli "run edits only"
```

### Skill controls {#skill-controls}

Use `--disable-builtin-skills` when an interactive or non-interactive session should expose only skills supplied outside the Droid CLI:

```bash
# Start the interactive TUI without builtin skills
droid --disable-builtin-skills

# Run one non-interactive session without builtin skills
droid exec --disable-builtin-skills "analyze this repository"
```

This removes Factory-provided builtin skills while preserving user, project, plugin, automation, mission, runtime, and dynamically supplied skills. For an interactive launch, the restriction remains active when you create, resume, or switch sessions. It is also inherited by child sessions, including subagents and mission workers.



<Aside kind="note">
The flag is not supported in Agent Client Protocol (ACP) mode. Use it with standard `droid` or `droid exec`, or set `disableBuiltinSkills` on `droid.initialize_session` and `droid.load_session` requests in stream JSON-RPC mode.
</Aside>



### Custom models {#custom-models}

You can configure custom models to use with droid exec by adding them to your `~/.factory/settings.json` file:

```json
{
  "customModels": [
    {
      "model": "gpt-5.1-codex-custom",
      "displayName": "My Custom Model",
      "baseUrl": "https://api.openai.com/v1",
      "apiKey": "your-api-key-here",
      "provider": "openai"
    }
  ]
}
```

To use a custom model, use the `custom:` prefix followed by the display name (with spaces replaced by dashes) and the index:

```bash
droid exec --model "custom:My-Custom-Model-0" "analyze this codebase"
```

If you have multiple custom models configured:

```json
{
  "customModels": [
    {
      "model": "kimi-k2",
      "displayName": "Kimi K2 [Groq]",
      "baseUrl": "https://api.groq.com/openai/v1",
      "apiKey": "your-groq-key",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    },
    {
      "model": "openai/gpt-oss-20b",
      "displayName": "GPT-OSS-20B [OpenRouter]",
      "baseUrl": "https://openrouter.ai/api/v1",
      "apiKey": "YOUR_OPENROUTER_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 32000
    }
  ]
}
```

You would reference them as:
- `--model "custom:Kimi-K2-[Groq]-0"`
- `--model "custom:GPT-OSS-20B-[OpenRouter]-1"`

The index corresponds to the position in the `customModels` array (0-based).



<Aside kind="note">
Reasoning effort (`-r` / `--reasoning-effort`) is not yet supported for custom models, but coming soon.
</Aside>



## Sessions, tagging, and logs {#sessions-tagging-and-logs}

Forking lets you branch off an existing session without disturbing the original; the new run starts from the forked session's history and is assigned a fresh session ID.

```bash
# Continue a session in-place
droid exec --session-id <session-id> "next steps"

# Branch off a session into a new run
droid exec --fork <session-id> --auto low "try an alternative refactor"
```

Use `--tag` to attach searchable labels to a run. The flag is repeatable and accepts either a plain name or a JSON object for structured metadata. Pair it with `--log-group-id` to bucket logs from related runs together for easier filtering and aggregation downstream.

```bash
droid exec \
  --tag release-v2 \
  --tag '{"name":"team","value":"platform"}' \
  --log-group-id ci-nightly \
  --auto low "run nightly checks and write report.md"
```

## Customizing the system prompt {#customizing-the-system-prompt}

Use `--append-system-prompt` to append additional text to the end of the system prompt for a single run, or `--append-system-prompt-file` to append the contents of a file. Both flags can be combined and are useful for injecting project-specific guidance, style guides, or invariants without modifying global settings.

```bash
droid exec \
  --append-system-prompt "Always prefer functional React components." \
  --auto low "review src/components for class-based components"

droid exec \
  --append-system-prompt-file ./docs/style-guide.md \
  --auto low "lint prose in README.md against the style guide"
```

## Mission mode {#mission-mode}

Mission mode runs `droid exec` as a multi-agent orchestrator that plans work, delegates to worker agents, and validates results. Enable it with `--mission` and optionally select dedicated models and reasoning effort levels for the worker and validator roles.

```bash
droid exec --mission \
  --worker-model claude-sonnet-4-5-20250929 \
  --worker-reasoning-effort medium \
  --validator-model claude-sonnet-4-5-20250929 \
  --validator-reasoning-effort high \
  --auto medium \
  "ship the new billing webhook end-to-end"
```

### Mission mode flags {#mission-mode-flags}

| Flag | Description |
|------|-------------|
| `--mission` | Run in mission mode (multi-agent orchestration). |
| `--worker-model <id>` | Model ID used by mission worker agents. |
| `--worker-reasoning-effort <level>` | Reasoning effort for mission workers. |
| `--validator-model <id>` | Model ID used by mission validator agents. |
| `--validator-reasoning-effort <level>` | Reasoning effort for mission validators. |

The top-level `-m, --model` and `-r, --reasoning-effort` flags still apply to the orchestrator itself; the worker and validator overrides only affect the agents the orchestrator spawns.

## Batch and parallel patterns {#batch-and-parallel-patterns}

Shell loops (bounded concurrency):

```bash
# Process files in parallel (GNU xargs -P)
find src -name "*.ts" -print0 | xargs -0 -P 4 -I {} \
  droid exec --auto low "Refactor file: {} to use modern TS patterns"
```

Background job parallelization:

```bash
# Process multiple directories in parallel with job control
for path in packages/ui packages/models apps/factory-app; do
  (
    cd "$path" &&
    droid exec --auto low "Run targeted analysis and write report.md"
  ) &
done
wait  # Wait for all background jobs to complete
```

Chunked inputs:

```bash
# Split large file lists into manageable chunks
git diff --name-only origin/main...HEAD | split -l 50 - /tmp/files_
for f in /tmp/files_*; do
  list=$(tr '\n' ' ' < "$f")
  droid exec --auto low "Review changed files: $list and write to review.json"
done
rm /tmp/files_*  # Clean up temporary files
```

Workflow Automation (CI/CD):

```yaml
# Dead code detection and cleanup suggestions
name: Code Cleanup Analysis
on:
  schedule:
    - cron: '0 1 * * 0' # Weekly on Sundays
  workflow_dispatch:
jobs:
  cleanup-analysis:
    strategy:
      matrix:
        module: ['src/components', 'src/services', 'src/utils', 'src/hooks']
    steps:
      - uses: actions/checkout@v4
      - run: droid exec --cwd "${{ matrix.module }}" --auto low "Identify unused exports, dead code, and deprecated patterns. Generate cleanup recommendations in cleanup-report.md"
```

## Unique usage examples {#unique-usage-examples}

License header enforcer:

```bash
git ls-files "*.ts" | xargs -I {} \
  droid exec --auto low "Ensure {} begins with the Apache-2.0 header; add it if missing"
```

API contract drift check (read-only):

```bash
droid exec "Compare openapi.yaml operations to our TypeScript client methods and write drift.md with any mismatches"
```

Security sweep:

```bash
droid exec --auto low "Run a quick audit for sync child_process usage and propose fixes; write findings to sec-audit.csv"
```

## Exit behavior {#exit-behavior}

- 0: success
- Non-zero: failure (permission violation, tool error, unmet objective). Treat non-zero as failed in CI.

## Best practices {#best-practices}

- Favor `--auto low`; keep mutations minimal and commit/push in scripted steps.
- Avoid `--skip-permissions-unsafe` unless fully sandboxed.
- Ask the agent to emit artifacts your pipeline can verify.
- Use `--cwd` to constrain scope in monorepos.
