---
id: enterprise/hierarchical-settings-and-org-control
title: "Hierarchical Settings & Org Control"
status: published
summary: "How org, project, folder, and user settings combine to control models, tools, safety policies, and telemetry for Droid."
parent: enterprise/index
tags: [enterprise]
relations: [relates_to=jp/enterprise/hierarchical-settings-and-org-control]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Hierarchical Settings &amp; Org Control</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">How org, project, folder, and user settings combine to control models, tools, safety policies, and telemetry for Droid.</p>


Factory’s enterprise story is built on a **single, predictable settings hierarchy**. Instead of ad‑hoc per‑machine configuration, orgs express policy once and have it apply consistently across laptops, CI, VMs, and airgapped environments.

This page explains how the hierarchy works and how to use it to govern models, tools, safety policies, and telemetry.

---

## The four levels {#the-four-levels}

Settings are defined in `.factory/` folders with a consistent structure at four levels:

```text
Org         → Central `.factory/` bundle (or config endpoint)
Folder      → <git-root>/.../subfolder/.factory/
Project     → <git-root>/.factory/
User        → ~/.factory/
```

Each `.factory/` folder can contain:

- `settings.json` – general settings (models, safety, preferences, telemetry).
- `hooks.json` – hook definitions.
- `mcp.json` – MCP server configurations.
- `droids/` – droid definitions.
- `commands/` – custom commands.
- `skills/` – skill definitions.

The **same schema** applies at every level. What changes is **precedence**.

---

## System-managed settings file {#system-managed-settings-file}

For deployments where org policy must be applied **before any user signs in** — managed laptops, CI runners that aren’t authenticated to Factory, airgapped or restricted‑network installs — IT/MDM administrators can drop a `settings.json` at a hardcoded, well‑known path on each machine:

| OS           | Path                                                  |
| ------------ | ----------------------------------------------------- |
| macOS        | `/Library/Application Support/Factory/settings.json`  |
| Linux & WSL  | `/etc/factory/settings.json`                          |
| Windows      | `C:\Program Files\Factory\settings.json`              |

The file uses the same [[enterprise/hierarchical-settings-and-org-control#settings-json-schema|Settings JSON schema]] as the rest of this page.

When this file is present it is the **authoritative source for org‑level settings** on that machine — it short‑circuits any API fetch or developer‑mode environment overrides for org settings. The `factoryTier` signal is still queried from the Factory API on a best‑effort basis (failures are non‑fatal) so enterprise‑gated behaviors keep working for managed deployments.

If the file is absent or unreadable, Droid falls back to the existing org‑settings flow (Factory App / managed‑settings endpoint). If the file is present but malformed or fails schema validation, org settings resolve to an empty policy and the failure is logged — a broken admin deployment is **not** silently bypassed.

This is the recommended way to ship base policy with an MDM image or installer; users cannot override or weaken it.

---

## Settings JSON schema {#settings-json-schema}

Below is the full schema for org-managed settings. These are configured by org admins through the [Enterprise Controls](https://app.factory.ai) page in the Factory App. Every property is optional — omit any field you do not need to set.



<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">sessionDefaultSettings</span><span class="factory-rf-type">object</span></div>

Session default preferences.
  

<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">model</span><span class="factory-rf-type">string</span></div>

Default model identifier (e.g. `claude-opus-4-6`, `gpt-5.3-codex`).

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">reasoningEffort</span><span class="factory-rf-type">string</span></div>

How much thinking the model does before responding. One of `none`, `dynamic`, `off`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">interactionMode</span><span class="factory-rf-type">string</span></div>

Droid interaction mode. One of `auto`, `spec`, `agi`.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">autonomyMode</span><span class="factory-rf-type">string</span></div>

Autonomy mode for the session. One of `normal`, `spec`, `auto-low`, `auto-medium`, `auto-high`.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">specModeModel</span><span class="factory-rf-type">string</span></div>

Model to use when spec mode is active.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">specModeReasoningEffort</span><span class="factory-rf-type">string</span></div>

Reasoning effort override for spec mode. Same values as `reasoningEffort`.

</div>
</Details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">maxAutonomyLevel</span><span class="factory-rf-type">string</span></div>

Maximum autonomy level any user or project can set. One of `off`, `low`, `medium`, `high`.

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">builtInToolAutonomyOverrides</span><span class="factory-rf-type">object</span></div>

Per-tool [[cli/user-guides/auto-run|autonomy level]] required to run a built-in network tool without a confirmation prompt. Map of built-in tool name to `low`, `medium`, or `high`. A tool auto-runs only when the session's Autonomy Level is at or above its configured requirement; otherwise Droid asks for approval. Tools without an entry default to `low`. Enforced from org-managed settings only, so user and project settings cannot weaken it. Configured under **Built-in Tool Autonomy** in Enterprise Controls.
  

<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">WebSearch</span><span class="factory-rf-type">string</span></div>

Autonomy level required to run the built-in Web Search tool. One of `low`, `medium`, `high`. Defaults to `low`.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">FetchUrl</span><span class="factory-rf-type">string</span></div>

Autonomy level required to run the built-in Fetch URL tool. One of `low`, `medium`, `high`. Defaults to `low`.

</div>
</Details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">subagentAutonomyLevel</span><span class="factory-rf-type">string</span></div>

Autonomy level applied to subagents spawned by the Task tool. One of `inherit`, `off`, `low`, `medium`, `high`. Defaults to `inherit`, which falls back to the parent session's autonomy level. An explicit level is clamped to `maxAutonomyLevel` so it can never exceed the enterprise cap.

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">subagentModelSettings</span><span class="factory-rf-type">object</span></div>

Complexity→model routing for [[cli/configuration/custom-droids|subagents]]. Applies when a subagent's droid uses `model: inherit` and the parent passes a complexity tier.
  

<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">lightModel</span><span class="factory-rf-type">string</span></div>

Model used for `light` complexity tasks. A model identifier, or omit to inherit the spawning session's model.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">lightReasoningEffort</span><span class="factory-rf-type">string</span></div>

Reasoning effort for the light tier. Same values as `reasoningEffort`.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">mediumModel</span><span class="factory-rf-type">string</span></div>

Model used for `medium` complexity tasks. A model identifier, or omit to inherit the spawning session's model.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">mediumReasoningEffort</span><span class="factory-rf-type">string</span></div>

Reasoning effort for the medium tier. Same values as `reasoningEffort`.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">heavyModel</span><span class="factory-rf-type">string</span></div>

Model used for `heavy` complexity tasks. A model identifier, or omit to inherit the spawning session's model.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">heavyReasoningEffort</span><span class="factory-rf-type">string</span></div>

Reasoning effort for the heavy tier. Same values as `reasoningEffort`.

</div>
</Details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">cloudSessionSync</span><span class="factory-rf-type">boolean</span></div>

Whether sessions are synced to the cloud.

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">wikiCloudSync</span><span class="factory-rf-type">boolean</span></div>

Whether AutoWiki content can be stored in the Factory App and synced to GitHub wikis.

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">disableWeeklyUsageSummary</span><span class="factory-rf-type">boolean</span></div>

Controls the weekly email to organization Managers and Owners that lists users and active service accounts at or above 80% of their monthly credit cap. The summary is sent when this setting is omitted or `false`; set it to `true` to stop the summary.

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">includeCoAuthoredByDroid</span><span class="factory-rf-type">boolean</span></div>

Include a `Co-authored-by: Droid` trailer in git commits.

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">enableDroidShield</span><span class="factory-rf-type">boolean</span></div>

Enable Droid Shield safety checks.

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">ideAutoConnect</span><span class="factory-rf-type">boolean</span></div>

Automatically connect to the IDE on session start.

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">commandAllowlist</span><span class="factory-rf-type">string[]</span></div>

Shell command patterns that are always allowed (accumulated across levels).

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">commandDenylist</span><span class="factory-rf-type">string[]</span></div>

Shell command patterns that always require confirmation (accumulated across levels). A denylisted command can still run if the user explicitly approves it; use `commandBlocklist` for a hard block.

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">commandBlocklist</span><span class="factory-rf-type">string[]</span></div>

Shell command patterns that can never run (accumulated across levels). Unlike the denylist, blocked commands have no approval path: the block holds even under full autonomy, auto-run, or `--skip-permissions-unsafe`. droid resolves the actual program being invoked before matching, so a blocked command cannot be bypassed with a wrapper shell, an absolute path, quoting tricks, or command substitution. Use this for organization-mandated hard stops.

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">allowManagedHooksOnly</span><span class="factory-rf-type">boolean</span></div>

When `true`, only org-managed hooks and hooks from org-enabled plugins are loaded. Hooks defined at the user and project levels are ignored. Defaults to `false`, where hooks from every level participate as usual. See [[reference/hooks-reference#org-managed-hooks|Org-managed hooks]].

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">hooks</span><span class="factory-rf-type">object</span></div>

Org-managed hook definitions, keyed by [[reference/hooks-reference#hook-events|hook event]]. Org-defined hooks are always loaded and cannot be removed by lower levels. See the [[reference/hooks-reference|hooks reference]] for full hook semantics.
  

<details class="boris-details">
<summary>properties</summary>

<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">field</span><span class="factory-rf-type">string</span></div>

" type="object[]">
One key per hook event: `PreToolUse`, `PostToolUse`, `Notification`, `UserPromptSubmit`, `Stop`, `SubagentStop`, `PreCompact`, `SessionStart`, `SessionEnd`. Each value is an array of matcher groups. Unknown event keys are tolerated but warned about at load time.


<details class="boris-details">
<summary>properties</summary>

<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">matcher</span><span class="factory-rf-type">string</span></div>

Tool name pattern to match (only applies to `PreToolUse` and `PostToolUse`).

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">commandRegex</span><span class="factory-rf-type">string</span></div>

Optional regular expression matched against the command.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">hooks</span><span class="factory-rf-type">object[]</span><span class="factory-rf-required">required</span></div>

Commands to run when the matcher matches.


<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">type</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

Must be `"command"`.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">command</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

Shell command to execute.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">timeout</span><span class="factory-rf-type">number</span></div>

Per-command timeout in seconds.

</div>

</details>



</div>

</details>



</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">hooksDisabled</span><span class="factory-rf-type">boolean</span></div>

Disable all hooks for the session.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">showHookOutput</span><span class="factory-rf-type">boolean</span></div>

Show hook output in the session view.

</div>
</Details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">customModels</span><span class="factory-rf-type">object[]</span></div>

Org-provisioned custom model definitions.
  

<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">model</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

Model name sent to the provider API.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">id</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

Unique identifier for this custom model entry. Must start with `custom:` (e.g. `custom:my-internal-model-v1`).

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">index</span><span class="factory-rf-type">integer</span><span class="factory-rf-required">required</span></div>

Display order index.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">baseUrl</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

Base URL of the model API endpoint.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">apiKey</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

API key for authenticating with the provider.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">provider</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

Provider type. One of `anthropic`, `openai`, `generic-chat-completion-api`, `factory`, `google`, `xai`, `voyage`.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">displayName</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

Human-readable name shown in the model picker.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">maxContextLimit</span><span class="factory-rf-type">integer</span></div>

Maximum context window size in tokens.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">enableThinking</span><span class="factory-rf-type">boolean</span></div>

Enable extended thinking / chain-of-thought.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">thinkingMaxTokens</span><span class="factory-rf-type">integer</span></div>

Maximum tokens for the thinking phase.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">maxOutputTokens</span><span class="factory-rf-type">integer</span></div>

Maximum output tokens.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">extraHeaders</span><span class="factory-rf-type">object</span></div>

Additional HTTP headers to send with each request. Map of header name to value.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">extraArgs</span><span class="factory-rf-type">object</span></div>

Additional provider-specific arguments passed to the API.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">noImageSupport</span><span class="factory-rf-type">boolean</span><span class="factory-rf-required">required</span></div>

Set to `true` if the model does not support image inputs.

</div>
</Details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">modelPolicy</span><span class="factory-rf-type">object</span></div>

Org-level model access control.
  

<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">allowedModelIds</span><span class="factory-rf-type">string[]</span></div>

Model IDs that are explicitly allowed. See [[enterprise/hierarchical-settings-and-org-control#supported-model-ids|supported model IDs]] below.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">blockedModelIds</span><span class="factory-rf-type">string[]</span></div>

Model IDs that are explicitly blocked.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">allowCustomModels</span><span class="factory-rf-type">boolean</span></div>

Whether users may add their own custom models.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">allowedBaseUrls</span><span class="factory-rf-type">string[]</span></div>

Base URLs that custom models are allowed to connect to.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">allowAllFactoryModels</span><span class="factory-rf-type">boolean</span></div>

Allow all Factory-hosted models regardless of the allow/block lists.

</div>
</Details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">userModelPolicies</span><span class="factory-rf-type">object</span></div>

Per-user model overrides. Map of user ID to policy object.
  

<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">allowedModelIds</span><span class="factory-rf-type">string[]</span></div>

Model IDs this user is allowed to use.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">blockedModelIds</span><span class="factory-rf-type">string[]</span></div>

Model IDs this user is blocked from using.

</div>
</Details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">enabledPlugins</span><span class="factory-rf-type">object</span></div>

Map of plugin name in `plugin@marketplace` format to `true` (enabled) or `false` (disabled). Plugins set to `true` are automatically installed on CLI startup once their marketplace is available.

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">extraKnownMarketplaces</span><span class="factory-rf-type">object</span></div>

Additional plugin marketplaces. Map of marketplace name to a source object. Marketplaces listed here are automatically cloned and registered on CLI startup.
  

<details class="boris-details">
<summary>properties</summary>

<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">source</span><span class="factory-rf-type">object</span><span class="factory-rf-required">required</span></div>

Marketplace source — one of the following shapes, discriminated by the `source` field:


<details class="boris-details">
<summary>github</summary>

<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">source</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

Must be `"github"`.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">repo</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

GitHub repository in `owner/repo` format.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">ref</span><span class="factory-rf-type">string</span></div>

Optional Git branch or tag to track (e.g. `"main"`, `"v1.2.0"`).

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">sha</span><span class="factory-rf-type">string</span></div>

Optional full 40-character commit SHA. When set, the marketplace is pinned to this exact commit.

</div>

</details>




<Details summary="url">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">source</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

Must be `"url"`.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">url</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

Git repository URL of the marketplace (e.g. `https://gitlab.com/company/plugins.git`).

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">ref</span><span class="factory-rf-type">string</span></div>

Optional Git branch or tag to track.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">sha</span><span class="factory-rf-type">string</span></div>

Optional full 40-character commit SHA to pin to.

</div>
</Details>




<Details summary="local">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">source</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

Must be `"local"`.

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">path</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

Local filesystem path to the marketplace.

</div>
</Details>



</div>

</details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">strictKnownMarketplaces</span><span class="factory-rf-type">object[]</span></div>

Marketplace sources that are strictly enforced. Each entry is a source object directly (e.g. `{ "source": "github", "repo": "owner/repo" }`), not wrapped in a `source` key like `extraKnownMarketplaces` values.

</div>



### Supported model IDs {#supported-model-ids}

The following model identifiers can be used in `allowedModelIds` and `blockedModelIds`:

| Provider | Model IDs |
|---|---|
| **Anthropic** | `claude-sonnet-4-5-20250929`, `claude-sonnet-4-6`, `claude-opus-4-5-20251101`, `claude-opus-4-6`, `claude-opus-4-6-fast`, `claude-opus-4-7`, `claude-haiku-4-5-20251001` |
| **OpenAI** | `gpt-5.1`, `gpt-5.1-codex`, `gpt-5.1-codex-max`, `gpt-5.2`, `gpt-5.3-codex` |
| **Google** | `gemini-3.5-flash`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview` |
| **XAI** | `grok-code-fast-1` |
| **Open source** | `glm-5`, `glm-5.1`, `glm-5.2`, `kimi-k2.5`, `kimi-k2.6`, `minimax-m2.7` |

---

## Extension‑only semantics {#extensiononly-semantics}

Factory uses **extension‑only** semantics instead of traditional “override” behavior.

- Higher levels (org, project) **cannot be overridden** by lower levels.
- Lower levels (folder, user) can only **add** to what higher levels define when those fields are unset.
- This ensures org policies remain intact even as projects and users customize their experience.

There are three merge modes depending on the data type.

### 1. Simple values – first wins {#1-simple-values-first-wins}

For simple scalar values (strings, numbers, booleans):

- The first level that sets a value “wins.”
- Lower levels cannot change or remove that value.

Examples:

- `sessionDefaultSettings.model`
- `sessionDefaultSettings.autonomyMode`
- `maxAutonomyLevel`
- `subagentAutonomyLevel`
- `subagentModelSettings.*` (per-tier model and reasoning effort)

This guarantees that org decisions (such as which models or autonomy levels are allowed) remain authoritative.

### 2. Arrays – union, cannot remove {#2-arrays-union-cannot-remove}

Array fields accumulate across levels:

- Org entries are always present and **cannot be removed**.
- Project and folder levels can add more entries.
- User level can add more entries but cannot remove or weaken higher‑level entries.

Examples:

- Command **allow lists** and **deny lists**.
- Lists of enabled hooks or features.

This pattern is ideal for policies like “these commands are always denied” or “these hooks are always enabled,” while still allowing teams to extend the list.

### 3. Objects – keys are locked per level {#3-objects-keys-are-locked-per-level}

For object fields:

- Keys defined at a higher level are **locked**; their contents cannot be changed by lower levels.
- Lower levels can add new keys but not modify or delete existing ones.

Examples:

- `customModels` – org defines `claude-enterprise`; projects can add `payments-gpt`, users can add `personal-experimental`, but none can change or remove `claude-enterprise`.
- MCP server definitions – org defines which servers exist and how they connect; projects decide which to use.

This keeps critical configuration (like model endpoints and MCP servers) under centralized control.

---

## Org configuration {#org-configuration}

Large organizations typically manage an **org‑level `.factory` bundle** or config endpoint that:

- Specifies allowed models, gateways, and BYOK policies.
- Defines global command allow/deny lists.
- Sets defaults for autonomy, reasoning effort, and safety features like Droid Shield.
- Configures OTEL defaults (endpoints, sampling, and attributes).
- Publishes org‑standard droids, commands, and hooks.

This bundle is distributed to all environments where Droid runs—developer machines, CI, VMs, and airgapped clusters.

Org policy is the foundation; projects and users build on top of it.

---

## Project and folder configuration {#project-and-folder-configuration}

Projects and folders use `.factory/` directories checked into version control to specialize org policy for particular codebases and teams.

Common responsibilities include:

- Adding project‑specific models and gateways within the allowed set.
- Defining project‑specific droids (for example, `/migrate-service`, `/refactor-module`).
- Configuring hooks that know about the project’s tests, linters, and deployment processes.
- Tightening safety controls for high‑risk repositories.

Folder‑level `.factory/` directories are useful in monorepos where different subsystems have different policies.

---

## User configuration {#user-configuration}

Developers can configure `~/.factory/` for **personal preferences only** where higher levels are silent.

Examples:

- Choosing a preferred model from the allowed set.
- Setting default behavior for display options and minor UX preferences.
- Enabling additional hooks or tools that do not conflict with org policy.

Because of extension‑only semantics, users cannot:

- Re‑enable models or tools that org or project settings have disallowed.
- Loosen command allow/deny lists.
- Reduce autonomy or safety requirements set by org or project.

---

## Example: enforcing a model policy {#example-enforcing-a-model-policy}

Suppose your org wants to:

- Allow only approved enterprise models.
- Disallow user‑supplied API keys.
- Force all prompts through a particular LLM gateway.

You would:

1. Define the allowed models and gateway endpoints in the org `.factory/settings.json`.
2. Set a policy flag to disable user BYOK entirely.
3. Configure hooks to verify that any model selection or endpoint use matches the org‑approved set.

Projects and users can still choose **which of the approved models** to use for different tasks, but cannot break these guarantees.

---

## Example: environment‑specific autonomy {#example-environmentspecific-autonomy}

Consider an org that wants to:

- Allow high autonomy in CI and sandboxed containers.
- Limit autonomy on developer laptops.

You could:

1. At org level, set `maxAutonomyLevel` to `high`.
2. In project settings, define environment‑aware hooks that:
   - Inspect environment tags (for example, `environment.type=local|ci|sandbox`).
   - Downgrade or block autonomy levels above `medium` when running on laptops.
3. Optionally, define stricter folder‑level policies for particularly sensitive repos.

Again, users cannot override these rules; they can only choose safer personal defaults within the allowed space.

---

## Example: full org-managed settings {#example-full-org-managed-settings}

```json
{
  "sessionDefaultSettings": {
    "model": "claude-sonnet-4-6",
    "reasoningEffort": "high",
    "interactionMode": "auto",
    "autonomyMode": "auto-medium",
    "specModeModel": "claude-opus-4-6",
    "specModeReasoningEffort": "medium"
  },
  "maxAutonomyLevel": "high",
  "builtInToolAutonomyOverrides": {
    "WebSearch": "high",
    "FetchUrl": "medium"
  },
  "subagentAutonomyLevel": "inherit",
  "cloudSessionSync": true,
  "includeCoAuthoredByDroid": true,
  "enableDroidShield": true,
  "ideAutoConnect": true,
  "commandAllowlist": ["npm *", "yarn *", "pnpm *", "make *"],
  "commandDenylist": ["rm -rf /", "sudo *"],
  "commandBlocklist": ["shutdown", "mkfs", "curl"],
  "allowManagedHooksOnly": true,
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Execute",
        "hooks": [
          {
            "type": "command",
            "command": "\"$FACTORY_PROJECT_DIR\"/.factory/hooks/audit-command.sh",
            "timeout": 30
          }
        ]
      }
    ]
  },
  "customModels": [
    {
      "model": "my-internal-model",
      "id": "custom:my-internal-model-v1",
      "index": 0,
      "baseUrl": "https://llm-gateway.internal.example.com/v1",
      "apiKey": "${INTERNAL_MODEL_API_KEY}",
      "provider": "generic-chat-completion-api",
      "displayName": "Internal Model v1",
      "maxContextLimit": 128000,
      "enableThinking": true,
      "thinkingMaxTokens": 8192,
      "maxOutputTokens": 16384,
      "extraHeaders": {
        "X-Team": "platform"
      },
      "extraArgs": {},
      "noImageSupport": false
    }
  ],
  "modelPolicy": {
    "allowedModelIds": ["claude-opus-4-6", "claude-sonnet-4-6", "gpt-5.3-codex"],
    "blockedModelIds": [],
    "allowCustomModels": true,
    "allowedBaseUrls": ["https://llm-gateway.internal.example.com/v1"],
    "allowAllFactoryModels": false
  },
  "disableWeeklyUsageSummary": false,
  "userModelPolicies": {
    "user-abc-123": {
      "allowedModelIds": ["claude-opus-4-6"],
      "blockedModelIds": []
    }
  },
  "enabledPlugins": {
    "my-org-plugin@internal-marketplace": true,
    "experimental-plugin@internal-marketplace": false
  },
  "extraKnownMarketplaces": {
    "internal-marketplace": {
      "source": {
        "source": "github",
        "repo": "my-org/factory-plugins"
      }
    }
  },
  "strictKnownMarketplaces": [
    {
      "source": "github",
      "repo": "my-org/factory-plugins"
    }
  ]
}
```

---

## Feature‑specific enterprise controls {#featurespecific-enterprise-controls}

Beyond the general hierarchy, several features have dedicated org‑level toggles that override all lower levels:

- **AutoWiki Cloud Sync** (`wikiCloudSync`) – Controls whether Wikis can be generated and stored in the Factory App. When disabled, all AutoWiki API endpoints are blocked and the Droid CLI skips Cloud Sync and GitHub Wiki sync. Enabled by default. See [[cli/features/wiki/overview#autowiki-cloud-sync|AutoWiki]].
- **Cloud Session Sync** (`cloudSessionSync`) – Controls whether session data is synced to Factory's cloud.
- **Built-in Tool Autonomy** (`builtInToolAutonomyOverrides`) – Sets the [[cli/user-guides/auto-run|autonomy level]] required to run built-in network tools (Web Search, Fetch URL) without a confirmation prompt. Omitted tools default to `low`. Enforced from org settings only, so users and projects cannot weaken it.

These controls are managed by org administrators in the **Enterprise Controls** section at [app.factory.ai](https://app.factory.ai).

---

## Putting it all together {#putting-it-all-together}

The hierarchical settings system underpins everything described in the other enterprise pages:

- [[enterprise/identity-and-access|Identity & Access Management]] – who can change which level of settings.
- [[enterprise/privacy-and-data-flows|Privacy, Data Flows & Governance]] – where data and telemetry are allowed to go.
- [[enterprise/network-and-deployment|Network & Deployment Configuration]] – which environments Droid can run in and how it connects.
- [[enterprise/llm-safety-and-agent-controls|LLM Safety & Agent Controls]] – policies for commands, tools, and Droid Shield.
- [[enterprise/models-llm-gateways-and-integrations|Models, LLM Gateways & Integrations]] – control over models, gateways, MCP servers, droids, and commands.
- [[enterprise/compliance-audit-and-monitoring|Compliance, Audit & Monitoring]] – guarantees and telemetry used to prove compliance.

By expressing policy once at the right level, you can run Droid across cloud, hybrid, and airgapped environments **without per‑machine drift or one‑off configuration**.
