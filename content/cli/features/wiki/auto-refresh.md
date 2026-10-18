---
id: cli/features/wiki/auto-refresh
title: "AutoWiki Refresh"
status: published
summary: "Use /install-wiki to set up a CI action that regenerates a Wiki on every push to the default branch."
parent: cli/features/wiki/index
tags: [cli, autowiki, wiki, install-wiki, auto-refresh, github-actions, gitlab-ci, ci]
relations: [relates_to=jp/cli/features/wiki/auto-refresh]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">AutoWiki Refresh</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Use /install-wiki to set up a CI action that regenerates a Wiki on every push to the default branch.</p>


The `/install-wiki` command creates a CI workflow that automatically regenerates a Wiki every time code is pushed to the default branch. It detects your CI framework -- GitHub Actions or GitLab CI -- and generates the appropriate configuration. This keeps your documentation in sync with your codebase without manual intervention.

## Quick start {#quick-start}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Open a Droid session in your repo</div>

```bash
cd /path/to/your/project
droid
```

</div>


  

<div class="factory-step">

<div class="factory-step-title">Run the install command</div>

```
> /install-wiki
```
Droid creates a workflow file and opens a pull request for you to review.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Add the Factory API key</div>

Add `FACTORY_API_KEY` as a secret in your CI settings:
  - **GitHub**: Repository **Settings > Secrets and variables > Actions** (or at the organization level under **Organization Settings > Secrets and variables > Actions**)
  - **GitLab**: Repository **Settings > CI/CD > Variables** (or at the group level under **Group Settings > CI/CD > Variables**)

Generate a key at [app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys).

</div>


  

<div class="factory-step">

<div class="factory-step-title">Merge the PR</div>

Once the secret is configured, merge the workflow PR. The Wiki will now
refresh automatically on every push to the default branch.

</div>

</div>



## Generated workflows {#generated-workflows}

Droid detects your CI framework and creates the appropriate configuration.

### GitHub Actions {#github-actions}

Creates `.github/workflows/droid-wiki-refresh.yml` (replace `main` with your default branch if different):

```yaml
name: Droid AutoWiki Refresh

on:
  push:
    branches: [main] # change to your default branch if not main

jobs:
  wiki-refresh:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Factory Droid
        run: curl -fsSL https://app.factory.ai/cli | sh

      - name: Generate Wiki
        run: droid exec --auto high "/wiki"
        env:
          FACTORY_API_KEY: ${{ secrets.FACTORY_API_KEY }}
```

### GitLab CI {#gitlab-ci}

Appends a job to your existing `.gitlab-ci.yml`:

```yaml
droid-wiki-refresh:
  stage: deploy
  before_script:
    - curl -fsSL https://app.factory.ai/cli | sh
  script:
    - droid exec --auto high "/wiki"
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  variables:
    FACTORY_API_KEY: $FACTORY_API_KEY
```

Both workflows:

- **Trigger on push** to the default branch
- **Install the Droid CLI** using the official installer
- **Run `/wiki`** in headless mode with high autonomy, generating the Wiki and storing it in the Factory App with Cloud Sync



<Aside kind="tip">
You can customize the workflow after installation. For example, change the
  trigger branch, add path filters to only regenerate when source files change,
  or adjust the timeout.
</Aside>



## Prerequisites {#prerequisites}

- A GitHub or GitLab hosted repository
- A Factory API key -- generate one at [app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys)
- Permission to add secrets and merge PRs in the target repository

## Refreshing from the Factory App {#refreshing-from-the-factory-app}

You can also set up recurring refreshes from the Factory App:

1. Go to [app.factory.ai/wiki](https://app.factory.ai/wiki)
2. Click **Refresh** on the Wiki page
3. Select **Recurring (on push)**
4. Choose a **Local** or **Cloud** method:
   - **Local** -- Copies the `/install-wiki` command for you to run in a local clone
   - **Cloud** -- Selects a cloud template or Droid Computer to run the setup remotely

For batch operations across multiple repositories, the Factory App lets you select several repos and run the setup on a Droid Computer in a single operation.

See [[cli/features/wiki/web-viewer|AutoWiki in the Factory App]] for more on the Factory App interface.

## Troubleshooting {#troubleshooting}





<Details summary="Workflow fails with authentication error">
Verify the `FACTORY_API_KEY` secret is set correctly in your repository's
**Settings > Secrets and variables > Actions**. Generate a new key at
[app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys)
if needed.
</Details>



  

<Details summary="AutoWiki not updating after push">
Check that the workflow file exists at `.github/workflows/droid-wiki-refresh.yml`
and that the branch trigger matches your default branch. View the Actions
tab in your repository to see workflow run logs.
</Details>



  

<Details summary="GitHub Wiki not syncing">
The GitHub Wiki tab must be initialized before Factory can push to it. Create
the first page manually at `https://github.com/{owner}/{repo}/wiki`. Also
verify that your organization hasn't disabled
[[cli/features/wiki/overview#autowiki-cloud-sync|AutoWiki Cloud Sync]].
</Details>





## See also {#see-also}

- [[cli/features/wiki/generate|Generate a Wiki]] -- One-time Wiki generation with `/wiki`
- [[cli/features/wiki/web-viewer|Browse Wikis]] -- Read and search Wikis from the Factory App
- [[guides/droid-exec/code-review|GitHub App installation]] -- Similar workflow for code review automation
- [[cli/droid-exec/overview|Droid Exec]] -- Headless mode used by the generated workflow
