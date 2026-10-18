---
id: cli/features/wiki/web-viewer
title: "AutoWiki in the Factory App"
status: published
summary: "Browse, search, and manage Wikis from the Factory App."
parent: cli/features/wiki/index
tags: [cli, autowiki, wiki, factory-app, browse, search, refresh, export]
relations: [relates_to=jp/cli/features/wiki/web-viewer]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">AutoWiki in the Factory App</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Browse, search, and manage Wikis from the Factory App.</p>


The AutoWiki view in the Factory App at [app.factory.ai/wiki](https://app.factory.ai/wiki) lets you browse, search, and manage generated Wikis for all your repositories in one place.

## What you'll see {#what-youll-see}

The top-level Wiki view lists every generated repository Wiki, with freshness indicators and controls for searching, filtering, and refreshing documentation.

<img src="../../../images/wiki/autowiki-list.png" alt="AutoWiki repository list in the Factory App" />

Open a repository to read generated pages with navigation, page outlines, search, export, and refresh controls.

<img src="../../../images/wiki/autowiki-reader.png" alt="AutoWiki reader showing generated architecture documentation" />

When GitHub Wiki sync is enabled, the same generated pages are also available from the repository's GitHub Wiki tab.

<img src="../../../images/wiki/github-wiki-sync.png" alt="Generated AutoWiki content synced to GitHub Wiki" />

## Browsing your Wikis {#browsing-your-wikis}

The main AutoWiki page shows a table of repositories with generated Wikis. Each row displays the repository name, last refresh date, and branch. Click a repository to open its Wiki.

### Wiki reader {#wiki-reader}

The Wiki reader provides:

- **Markdown rendering** -- Full-fidelity rendering of the generated documentation with syntax-highlighted code blocks
- **Table of contents** -- A sidebar outline of the current page for quick navigation
- **Breadcrumbs** -- Hierarchical navigation showing your position in the page tree
- **Search** -- Full-text search across all generated pages
- **Version history** -- A dropdown to browse previous Wiki generations and compare how documentation has evolved
- **Export** -- Download the generated documentation as markdown files

## Refreshing a Wiki {#refreshing-a-wiki}

Click the **Refresh** button on a Wiki page to regenerate documentation. A modal presents two options:



<div class="factory-card-group">

<div class="factory-card">

**One-time refresh**

Regenerate the Wiki once using the latest code on the default branch.

</div>


  

<div class="factory-card">

**Recurring (on push)**

Install a CI action that refreshes the Wiki on every push to the
default branch.

</div>

</div>



After choosing a mode, select how to run the generation:

| Method | Description |
|--------|-------------|
| **Local** | Copies the Droid CLI command (`/wiki` or `/install-wiki`) for you to paste into a local Droid session |
| **Cloud** | Runs the generation on a cloud template linked to the repository |

### Batch refresh {#batch-refresh}

From the top-level AutoWiki page at [app.factory.ai/wiki](https://app.factory.ai/wiki), you can refresh multiple repositories at once:

1. Click **Refresh** to enter selection mode
2. Select the repositories you want to refresh
3. Choose **One-time** or **Recurring**
4. Select a **Droid Computer** to run the work

<img src="../../../images/wiki/autowiki-batch-refresh.png" alt="Batch refresh selection mode in AutoWiki" />

Droid clones each repository on the selected Droid Computer and generates Wikis, or sets up recurring generation, running the jobs in parallel where possible.

## See also {#see-also}

- [[cli/features/wiki/generate|Generate a Wiki]] -- Produce a Wiki from the Droid CLI with `/wiki`
- [[cli/features/wiki/auto-refresh|Set up AutoWiki refresh]] -- Keep Wikis current with a CI action
- [[cli/features/wiki/overview|AutoWiki overview]] -- How all the pieces fit together
