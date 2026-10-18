---
id: cli/features/droid-control
title: "Droid Control"
status: published
summary: "Terminal, browser, and desktop automation. Record demos, verify behavior claims, and run QA flows."
parent: cli/features/index
tags: [cli, droid-control, automation, demo, verify, qa-test, terminal, browser]
relations: [relates_to=jp/cli/features/droid-control]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Droid Control</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Terminal, browser, and desktop automation. Record demos, verify behavior claims, and run QA flows.</p>


Droid Control lets Droids *operate* software: launch apps, type commands, click buttons, record what happens, and produce polished video evidence of it. Built by Droids, for Droids.



<div class="factory-frame">

<video autoplay muted loop playsinline>
<source src="../../images/features/droid-control-hero.mp4" type="video/mp4" />
  </video>

<div class="factory-frame-caption">This video was planned, recorded, and rendered entirely by a Droid.</div>

</div>



## What you get {#what-you-get}



<div class="factory-card-group">

<div class="factory-card">

**Verify claims**

Test whether a behavior claim is true and produce evidence either way. No staging, no advocacy -- just investigation.

</div>


  

<div class="factory-card">

**Run QA flows**

Drive terminal CLIs, web apps, or Electron apps through end-to-end flows. Report pass/fail with annotated screenshots.

</div>


  

<div class="factory-card">

**Record demos**

Generate polished before/after comparison videos of PRs, complete with title cards, keystroke overlays, and window chrome.

</div>

</div>



## Get started {#get-started}



<div class="factory-tabs">

<div class="factory-tab-panel">

<div class="factory-tab-heading">UI</div>

Run `/plugins` in a Droid session, go to the **Browse** tab, find **droid-control**, and install it.

</div>


  

<div class="factory-tab-panel">

<div class="factory-tab-heading">CLI</div>

```bash
droid plugin marketplace add https://github.com/Factory-AI/factory-plugins
droid plugin install droid-control@factory-plugins --scope user
```

</div>

</div>



For video rendering, Remotion dependencies need a one-time install after adding the plugin:

```bash
droid plugin list --scope user
cd <plugin-path>/remotion && npm install
```



<Aside kind="note">
You also need the runtime tools for your use case (tuistory, agent-browser, ffmpeg, etc.). See [[cli/features/droid-control#prerequisites|Prerequisites]] for per-use-case install commands.
</Aside>



## Commands {#commands}

Droid Control adds three slash commands. Each handles the full workflow end-to-end: planning, execution, recording, and reporting.



<div class="factory-tabs">

<div class="factory-tab-panel">

<div class="factory-tab-heading">/demo</div>

Record a demo video of a feature or PR.

```
/demo pr-1847
```

Accepts a PR number, GitHub URL, or free-text description. Comparison PRs get side-by-side layout by default; new features get single-branch.

Add flags for extra polish:

```
/demo pr-1847 -- showcase, keys
```

| Flag | Effect |
|------|--------|
| `showcase` | Cinematic preset with warm backgrounds and film grain |
| `keys` | Keystroke overlay pills showing user actions |

#### How it works {#how-it-works}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Understands the change</div>

Fetches the PR description, diff, and linked ticket. For each change, identifies what needs to be proven and what a viewer could confuse it with.

</div>




<div class="factory-step">

<div class="factory-step-title">Plans the interaction</div>

Scripts a sequence of actions that produces visible evidence the feature works. Both branches run identical interactions so only the behavior differs. Presents the plan and waits for your approval before recording.

</div>




<div class="factory-step">

<div class="factory-step-title">Captures both branches</div>

Launches recorded sessions on the baseline and candidate branches in parallel using worker subagents.

</div>




<div class="factory-step">

<div class="factory-step-title">Composes the video</div>

Renders a polished video via Remotion with title cards, window chrome, and effects. Six visual presets range from cinematic (`factory`) to utilitarian (`minimal`).

</div>




<div class="factory-step">

<div class="factory-step-title">Verifies the output</div>

Checks the final video against the original commitments before delivering.

</div>

</div>

</div>


  

<div class="factory-tab-panel">

<div class="factory-tab-heading">/verify</div>

Test a specific behavior claim and report findings with evidence.

```
/verify "ESC cancels streaming in bash mode"
```

Also accepts a PR reference with an optional claim:

```
/verify 11386 -- the fork flag creates a new session
```

If given a PR number alone, Droid fetches the PR and identifies the most important testable claim.



<Aside kind="tip">
The droid is framed as an **investigator**, not an advocate. If the claim is false, that's a valid finding. Anti-fabrication rules prevent staging evidence to match expected outcomes.
</Aside>



#### How it works {#how-it-works-2}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Determines what to test</div>

Identifies the specific behavior to observe and what evidence type is needed: text snapshots for functional claims, screenshots for visual claims, or raw byte captures for encoding claims.

</div>




<div class="factory-step">

<div class="factory-step-title">Captures the evidence</div>

Launches the app, runs the minimal interaction sequence that demonstrates the behavior, and captures the result. If the behavior contradicts the claim, that is evidence -- not an error.

</div>




<div class="factory-step">

<div class="factory-step-title">Reports the finding</div>

Delivers a structured report with a **CONFIRMED**, **REFUTED**, or **INCONCLUSIVE** conclusion, along with all captured evidence inline.

</div>

</div>

</div>


  

<div class="factory-tab-panel">

<div class="factory-tab-heading">/qa-test</div>

Run automated QA against terminal CLIs, web apps, or Electron apps.

```
/qa-test https://app.example.com -- login, create a project, invite a member
```

Also accepts a CLI command, Electron app name, PR reference, or free-text description. Test steps after `--` are optional -- Droid designs a reasonable flow if none are provided.

#### How it works {#how-it-works-3}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Defines the test plan</div>

Determines the target (web, terminal, or Electron), designs test steps from your instructions or the app's UI, and identifies what evidence to capture at each step.

</div>




<div class="factory-step">

<div class="factory-step-title">Drives the flow</div>

Launches the app and executes each step, capturing screenshots (browser) or text snapshots (terminal) along the way. If a step fails, it records the failure and continues for maximum coverage.

</div>




<div class="factory-step">

<div class="factory-step-title">Reports results</div>

Delivers a step-level pass/fail table with inline evidence and a summary of any issues found.

</div>

</div>

</div>

</div>



### Example output {#example-output}

Every video below was planned, recorded, and rendered entirely by a Droid.



<div class="factory-tabs">

<div class="factory-tab-panel">

<div class="factory-tab-heading">CLI: single-branch</div>



<div class="factory-frame">

<video autoplay muted loop playsinline>
<source src="../../images/features/droid-control-demo-single.mp4" type="video/mp4" />
</video>

<div class="factory-frame-caption">Demo of the /cwd command. Factory preset, single-branch layout.</div>

</div>



</div>


  

<div class="factory-tab-panel">

<div class="factory-tab-heading">CLI: before/after</div>



<div class="factory-frame">

<video autoplay muted loop playsinline>
<source src="../../images/features/droid-control-demo-comparison.mp4" type="video/mp4" />
</video>

<div class="factory-frame-caption">Before/after comparison of a bash mode output redesign. Factory preset, side-by-side layout.</div>

</div>



</div>


  

<div class="factory-tab-panel">

<div class="factory-tab-heading">Web: single-branch</div>



<div class="factory-frame">

<video autoplay muted loop playsinline>
<source src="../../images/features/droid-control-web-single.mp4" type="video/mp4" />
</video>

<div class="factory-frame-caption">Browser automation demo of a web app. Recorded and rendered by a Droid.</div>

</div>



</div>


  

<div class="factory-tab-panel">

<div class="factory-tab-heading">Web: before/after</div>



<div class="factory-frame">

<video autoplay muted loop playsinline>
<source src="../../images/features/droid-control-web-comparison.mp4" type="video/mp4" />
</video>

<div class="factory-frame-caption">Before/after comparison of a web app change. Side-by-side layout.</div>

</div>



</div>

</div>



## Automation drivers {#automation-drivers}

Droid Control supports four automation backends. The right one is selected automatically based on what you're targeting.



<div class="factory-card-group">

<div class="factory-card">

**tuistory**

**Virtual PTY automation.** Default for terminal work. Playwright-style CLI with asciinema recording and forced truecolor output.

</div>


  

<div class="factory-card">

**true-input**

**Real terminal emulator.** Headless Wayland compositor (Linux), KVM/QEMU (Windows), or QEMU monitor (macOS). For when you need real rendering evidence.

</div>


  

<div class="factory-card">

**agent-browser**

**Web and Electron apps.** Playwright-backed CLI with Chrome DevTools Protocol support. Navigates pages, fills forms, clicks buttons, captures screenshots.

</div>


  

<div class="factory-card">

**desktop-control**

**Native desktop apps.** Accessibility-tree snapshots, element or pixel actions, and per-window screenshots via [trycua/cua](https://github.com/trycua/cua) `cua-driver` -- all without stealing focus. macOS and Windows are production tier; Linux is pre-release.

</div>

</div>



## Video rendering {#video-rendering}

Demo and showcase videos are rendered with [Remotion](https://www.remotion.dev/), a React-based video engine. The plugin includes 23 visual components and 6 presets.





<Details summary="Visual presets">
| Preset | Look | Best for |
|--------|------|----------|
| `factory` | Warm black, traffic lights, amber glow | Official Factory content |
| `factory-hero` | Same + gradient background | Landing pages, social |
| `hero` | Cool gradient, generous margins | Non-Factory marketing |
| `macos` | Dark, clean frame | General-purpose demos |
| `presentation` | Black, generous margins | Slide decks, talks |
| `minimal` | No window bar, tight margins | Docs embeds, inline clips |
</Details>


  

<Details summary="Automatic layers (always present)">
- Warm radial backgrounds, floating particles, film grain overlay, color grading
  - Configurable title-to-content transition (`motion-blur`, `flash`, `whip-pan`, `light-leak`, `glitch-lite`)
  - Animated window chrome with traffic lights and glassmorphic borders
  - Auto-scaled title/subtitle text
</Details>


  

<Details summary="Effect layers (selected at compose time)">
- Spotlight overlays to highlight specific regions
  - Directed zoom for small text or details
  - Keystroke pills showing user actions
  - Section headers and transition sweeps
  - Syntax-highlighted code annotations for source-change overlays
</Details>





## Architecture {#architecture}

The plugin uses a composition architecture with three layers:

- **Orchestrator** -- Routes each request through three independent lookups (target, stage, artifact) to determine which skills to load.
- **11 atom skills** -- Self-contained background knowledge loaded on demand, split into drivers, targets, stages, and polish.
- **3 commands** -- Parse arguments into commitments, then delegate to atoms via hybrid handoffs.

Every workflow flows through **capture → compose → verify**. Commands declare *what* to produce; atoms own *how*. Skills chain through explicit handoffs rather than hardcoded pipelines, so the droid follows the flow naturally.



<div class="factory-card">

**[Architecture deep dive](https://github.com/Factory-AI/factory-plugins/blob/master/plugins/droid-control/ARCHITECTURE.md)**

Design rationale: UX for droids, waterfall routing, task delegation, and hybrid handoffs.

</div>



## Prerequisites {#prerequisites}

Only install what you need for your use case.





<Details summary="Terminal demos (tuistory)">
```bash
npm install -g tuistory                                # virtual PTY driver
pip install asciinema                                   # terminal recording
cargo install --git https://github.com/asciinema/agg   # .cast → .gif converter
sudo apt-get install -y ffmpeg                          # video processing
```
</Details>


  

<Details summary="Web/Electron automation (agent-browser)">
```bash
agent-browser install   # downloads Chromium
```
</Details>


  

<Details summary="Native desktop apps (desktop-control)">
```bash
curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh | bash
cua-driver skills install   # upstream skill pack (deep tool reference)
```
Windows installs via PowerShell: `irm https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.ps1 | iex`. macOS additionally needs `cua-driver permissions grant` (Accessibility + Screen Recording).
</Details>


  

<Details summary="Real terminal emulator (true-input)">
| Platform | Required tools |
|----------|----------------|
| Linux/Wayland | `cage`, `wtype`, a Wayland-compatible terminal |
| Windows (KVM) | `libvirt`, `qemu`, KVM VM with SSH |
| macOS (QEMU) | `qemu`, `socat`, macOS VM with SSH |
</Details>


  

<Details summary="Video composition (showcase)">
Requires Node.js >= 18, Chrome/Chromium, `ffmpeg`, `ffprobe`, and `agg`.
</Details>





## See also {#see-also}



<div class="factory-card-group">

<div class="factory-card">

**[Source code](https://github.com/Factory-AI/factory-plugins/tree/master/plugins/droid-control)**

Full plugin source: skills, commands, scripts, and Remotion components.

</div>


  

<div class="factory-card">

**[[cli/configuration/plugins|Plugins]]**

Learn how plugins work, how to install them, and how to build your own.

</div>


  

<div class="factory-card">

**[[guides/skills/automated-qa|Automated QA skill]]**

Deeper QA automation with CI integration, failure learning, and structured reports.

</div>


  

<div class="factory-card">

**[README](https://github.com/Factory-AI/factory-plugins/blob/master/plugins/droid-control/README.md)**

Quick start, command reference, and prerequisites.

</div>

</div>
