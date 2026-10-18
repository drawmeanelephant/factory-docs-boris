---
id: cli/features/wiki/overview
title: "AutoWiki"
status: published
summary: "AutoWiki generates comprehensive, structured Wikis for your repositories."
parent: cli/features/wiki/index
tags: [cli, autowiki, wiki, documentation, codebase, install-wiki, github-wiki, auto-refresh]
relations: [relates_to=jp/cli/features/wiki/overview]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">AutoWiki</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">AutoWiki generates comprehensive, structured Wikis for your repositories.</p>


AutoWiki generates comprehensive, structured Wikis for your repositories. It analyzes each codebase and produces browsable documentation with architecture overviews, module breakdowns, and cross-linked pages -- then keeps each Wiki current as your code changes.

<img src="../../../images/wiki/autowiki-list.png" alt="AutoWiki repository overview in the Factory App" />



<div class="factory-card-group">

<div class="factory-card">

**[[cli/features/wiki/generate|Generate]]**

Run `/wiki` in the Droid CLI to produce a Wiki for any repo

</div>


  

<div class="factory-card">

**[[cli/features/wiki/auto-refresh|Auto-refresh]]**

Run `/install-wiki` to refresh Wikis on every push

</div>


  

<div class="factory-card">

**[[cli/features/wiki/web-viewer|Browse]]**

Read, search, and export Wikis in the Factory App

</div>

</div>



## How it works {#how-it-works}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Generate from the Droid CLI</div>

Run `/wiki` inside a Droid session. Droid analyzes the codebase and produces
a set of structured markdown pages covering architecture, modules, APIs,
and conventions.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Store in the Factory App</div>

Cloud Sync stores the generated Wiki in the Factory App, where it becomes
browsable at [app.factory.ai/wiki](https://app.factory.ai/wiki). Each
sync is versioned so you can compare changes over time.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Sync to GitHub Wiki</div>

For GitHub-hosted repositories, AutoWiki can push generated Wikis to the
repo's built-in GitHub Wiki tab. Internal links are rewritten, a sidebar is
generated, and the content is pushed to `{repo}.wiki.git`.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Keep it current</div>

Run `/install-wiki` to create a CI workflow (GitHub Actions or GitLab CI)
that regenerates the Wiki on every push to the default branch -- or
trigger a refresh from the Factory App at any time.

</div>

</div>



## GitHub Wiki sync {#github-wiki-sync}

When AutoWiki generates a Wiki for a GitHub-hosted repository, Factory can optionally sync the content to GitHub Wiki. Your team can browse the same documentation directly from the repository page without visiting the Factory App. For details on how the sync works, see [[cli/features/wiki/generate#github-wiki-sync|Generate a Wiki]].

<img src="../../../images/wiki/github-wiki-sync.png" alt="Generated AutoWiki content synced to GitHub Wiki" />



<Aside kind="note">
GitHub requires GitHub Wiki to be initialized before Factory can sync to it.
  If you haven't used GitHub Wiki before, create the first page manually at
  `https://github.com/{owner}/{repo}/wiki`, then re-run `/wiki`.
</Aside>



## Enterprise controls {#enterprise-controls}

### AutoWiki Cloud Sync {#autowiki-cloud-sync}

Organizations that need to prevent AutoWiki content from being stored in the Factory App can disable **AutoWiki Cloud Sync**. This is an org-level enterprise control available at [app.factory.ai](https://app.factory.ai) under **Settings > Enterprise Controls**.

<img src="../../../images/wiki/autowiki-enterprise-controls.png" alt="AutoWiki Cloud Sync enterprise control in Factory settings" />

When AutoWiki Cloud Sync is **disabled**:

- All AutoWiki API endpoints return 403 for your organization
- The `/wiki` command will not store content in the Factory App
- GitHub Wiki sync is also skipped from the Droid CLI
- The AutoWiki page in the Factory App shows no content

AutoWiki Cloud Sync is **enabled by default**. Only org managers can toggle this setting.

For more on how enterprise controls work, see [[enterprise/hierarchical-settings-and-org-control|Hierarchical Settings & Org Control]].

## What's next {#whats-next}



<div class="factory-card-group">

<div class="factory-card">

**[[cli/features/wiki/generate|Generate a Wiki]]**

Step-by-step guide to producing your first Wiki

</div>


  

<div class="factory-card">

**[[cli/features/wiki/auto-refresh|Set Up AutoWiki Refresh]]**

Install a CI action that keeps Wikis current

</div>


  

<div class="factory-card">

**[[cli/features/wiki/web-viewer|Browse in the Factory App]]**

Search, read, and export Wikis

</div>


  

<div class="factory-card">

**[[enterprise/hierarchical-settings-and-org-control|Enterprise Settings]]**

Learn how org-level controls govern AutoWiki and other features

</div>

</div>
