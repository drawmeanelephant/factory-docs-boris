---
id: cli/features/wiki/generate
title: "Generate a Wiki"
status: published
summary: "Use the /wiki command to generate a comprehensive Wiki with AutoWiki from the Droid CLI."
parent: cli/features/wiki/index
tags: [cli, autowiki, wiki, generate, documentation, codebase-docs, slash-command, upload]
relations: [relates_to=jp/cli/features/wiki/generate]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Generate a Wiki</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Use the /wiki command to generate a comprehensive Wiki with AutoWiki from the Droid CLI.</p>


The `/wiki` command analyzes your repository and generates a structured Wiki covering architecture, modules, APIs, and conventions. Cloud Sync stores the Wiki in the Factory App, and AutoWiki can optionally sync it to GitHub Wiki.

## Quick start {#quick-start}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Open a Droid session in your repo</div>

Navigate to your project directory and start Droid:
```bash
cd /path/to/your/project
droid
```

</div>


  

<div class="factory-step">

<div class="factory-step-title">Run the wiki command</div>

```
> /wiki
```
Droid analyzes your codebase and generates markdown files into a local
`droid-wiki/` folder in your project directory. Once generation is
complete, Cloud Sync stores the contents in the Factory App.

</div>


  

<div class="factory-step">

<div class="factory-step-title">View the result</div>

After Cloud Sync completes, Droid prints a link to your Wiki:
```
Wiki uploaded successfully: https://app.factory.ai/wiki/{wikiRunId}
```
Open the link to browse your documentation, or visit
[app.factory.ai/wiki](https://app.factory.ai/wiki) to see all your Wikis.

</div>

</div>



## What happens during generation {#what-happens-during-generation}

When you run `/wiki`, Droid performs several steps:

1. **Codebase analysis** -- Reads source files, configuration, tests, and documentation to understand the project structure
2. **Page generation** -- Produces a set of structured markdown files organized by topic (architecture, modules, APIs, setup, etc.)
3. **Visual screenshots** -- If the repository has a [[guides/skills/automated-qa|QA skill]] installed, Droid launches the application and captures screenshots of web UIs and TUIs to include in the Wiki. Run `/install-qa` to set one up if your repo doesn't have one yet.
4. **Cloud Sync** -- Stores the pages and images in the Factory App
5. **GitHub Wiki sync** -- For GitHub repos, flattens pages and pushes to GitHub Wiki



<Aside kind="note">
Wiki generation uses your current branch and working directory state.
  For the most accurate documentation, run `/wiki` from a clean checkout
  of your default branch.
</Aside>





<Aside kind="tip">
The first Wiki generation for a repository can take a while -- Droid needs
  to analyze the entire codebase from scratch. Subsequent runs are
  significantly faster because they use incremental mode, only updating pages
  affected by code changes since the last generation.
</Aside>



## GitHub Wiki sync {#github-wiki-sync}

After Cloud Sync stores the Wiki in the Factory App, the Droid CLI automatically syncs it to GitHub Wiki for GitHub-hosted repositories. The sync:

<img src="../../../images/wiki/github-wiki-sync.png" alt="Generated AutoWiki content synced to GitHub Wiki" />

- Flattens the hierarchical page tree into GitHub Wiki's flat format (e.g., `overview/architecture.md` becomes `overview--architecture.md`)
- Rewrites internal links to use the flat filenames
- Generates `_Sidebar.md` with a navigable table of contents
- Generates `Home.md` from your Wiki root page
- Clones `{repo}.wiki.git`, replaces all content, and pushes

### Prerequisites for GitHub sync {#prerequisites-for-github-sync}

- Your repository must be hosted on GitHub
- GitHub Wiki must be initialized -- if you've never used it, create the first page at `https://github.com/{owner}/{repo}/wiki`
- Your Git credentials must have push access to the GitHub Wiki repository
- [[cli/features/wiki/overview#autowiki-cloud-sync|AutoWiki Cloud Sync]] must not be disabled for your organization

If GitHub Wiki isn't initialized, the Droid CLI prints a message with a link to create the first page and skips the sync without failing.

## Versioning {#versioning}

Each Wiki generation creates a new **Wiki Run** with metadata including:

- Commit hash and branch name
- Whether there were local uncommitted changes
- Droid CLI version used
- Timestamp

You can browse previous versions from the [[cli/features/wiki/web-viewer|AutoWiki page in the Factory App]] using the version dropdown.

## See also {#see-also}

- [[cli/features/wiki/auto-refresh|Set up AutoWiki refresh]] -- Keep Wikis current with a CI action
- [[cli/features/wiki/web-viewer|Browse Wikis]] -- Read, search, and export Wikis from the Factory App
- [[cli/features/wiki/overview|AutoWiki overview]] -- How all the pieces fit together
