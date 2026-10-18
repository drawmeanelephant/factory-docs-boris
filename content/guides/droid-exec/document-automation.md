---
id: guides/droid-exec/document-automation
title: "Automated Documentation"
status: published
summary: "Automatically update documentation when code changes using CI/CD workflows"
parent: guides/droid-exec/index
tags: [guides, documentation, docs, automation, ci-cd, github-actions, droid-exec]
relations: [relates_to=jp/guides/droid-exec/document-automation]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Automated Documentation</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Automatically update documentation when code changes using CI/CD workflows</p>


This cookbook demonstrates how to use Droid Exec in GitHub Actions to automatically update documentation when code is merged to main. The workflow analyzes code changes, discovers relevant documentation, updates it, and creates a pull request for human review.

## How it works {#how-it-works}

End-to-end automated workflow:

1. **Trigger**: Code merged to main branch
2. **Explore**: Droid exec explores codebase structure (project type, tech stack)
3. **Analyze**: Identifies changed files and their purpose
4. **Discover**: Searches docs/ directory for relevant documentation
5. **Update**: Updates affected documentation sections
6. **Commit**: Workflow creates commit
7. **PR**: Bot opens pull request for team review

## Prerequisites {#prerequisites}

To get started, you'll need:
- Droid installed
- A Factory API key
- GitHub repository with Actions enabled
- `FACTORY_API_KEY` in repository secrets (Settings → Secrets → Actions)
- Existing documentation directory



<Aside kind="note">
See the Droid Exec setup [[cli/droid-exec/overview#installation|here]].
</Aside>



## Complete GitHub Actions workflow {#complete-github-actions-workflow}



<Aside kind="info">
This workflow will create pull requests automatically. Review the generated PRs carefully before merging to ensure accuracy.
</Aside>



Create `.github/workflows/update-docs.yml`:

```yaml
name: Auto-Update Documentation

on:
  push:
    branches: [main]
    paths:
      - 'src/**/*.ts'
      - 'src/**/*.tsx'
      - 'src/**/*.js'
      - 'src/**/*.py'

jobs:
  update-docs:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          token: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Set up the Droid CLI
        run: |
          curl -fsSL https://app.factory.ai/cli | sh
          echo "$HOME/.local/bin" >> $GITHUB_PATH
      
      - name: Get changed files
        id: changes
        run: |
          git diff --name-only HEAD^ HEAD > changed_files.txt
          echo "Files changed in last commit:"
          cat changed_files.txt
      
      - name: Update documentation
        env:
          FACTORY_API_KEY: ${{ secrets.FACTORY_API_KEY }}
        run: |
          droid exec --auto low "
          The following source files were just merged to main:
          $(cat changed_files.txt)
          
          Your task is to update the documentation to match these code changes.
          
          First, explore the codebase to understand context:
          1. Examine package.json, README, and main entry points
          2. Identify key directories and their purposes
          3. Note the tech stack (languages, frameworks, tools)
          4. Classify the project type:
             - **Library/SDK**: Exports functions/classes, has API docs, used as dependency
             - **Application**: Has routes/pages, domain models, user features
             - **Framework/Protocol**: Defines specs, client/server implementations
             - **Monorepo**: Multiple packages/apps in one repository
          
          Then, understand what changed:
          1. Read each changed file carefully
          2. Identify if changes are: API updates, new features, bug fixes, refactors
          3. Note breaking changes or new configuration options
          
          Next, find and update relevant documentation:
          1. Search the docs/ directory for files that reference:
             - The changed filenames or paths
             - Functions, classes, or APIs that were modified
             - Features or concepts affected by the changes
          2. Update the found documentation:
             - Update function signatures if they changed
             - Update code examples to match new APIs
             - Update configuration docs if options changed
             - Update explanations if behavior changed
             - Add notes about breaking changes if needed
          3. Preserve the existing doc structure and writing style
          4. Only modify sections that are actually affected
          
          DO NOT commit or push changes.
          
          Finally, create doc-update-summary.md with:
          - List of documentation files that were updated
          - Summary of changes made to each file
          - Any sections that may need human review or clarification
          "
      
      - name: Commit documentation updates
        run: |
          if [ -n "$(git status --porcelain)" ]; then
            git config user.name "github-actions[bot]"
            git config user.email "github-actions[bot]@users.noreply.github.com"
            git add -A
            git commit -m "docs: automated documentation updates"
          else
            echo "No documentation changes needed"
            exit 0
          fi
      
      - name: Create Pull Request
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          BRANCH="docs/auto-update-$(date +%Y%m%d-%H%M%S)"
          git checkout -b $BRANCH
          git push origin $BRANCH
          
          # Get summary or use default message
          SUMMARY=$(cat doc-update-summary.md 2>/dev/null || echo "Documentation updated to reflect recent code changes.")
          
          gh pr create \
            --title "📚 Automated documentation updates" \
            --body "## Automated Documentation Updates

$SUMMARY

### Review Checklist
- [ ] Documentation accurately reflects code changes
- [ ] Code examples are correct and runnable
- [ ] No unintended changes to other sections
- [ ] Formatting and style are consistent

---
This PR was automatically generated after code was merged to main." \
            --label "documentation,automated"
```

**Key workflow features:**
- Uses `--auto low` for file modifications only (following cookbook patterns)
- Explicit instruction: "DO NOT commit or push" (separation of concerns)
- Workflow handles git operations in separate step
- Droid autonomously explores codebase and discovers relevant docs (no mapping file needed)

## Best practices {#best-practices}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Scope triggers carefully</div>

Only trigger on meaningful code changes:
```yaml
paths:
  - 'src/**'
  - '!src/**/*.test.ts'
  - '!src/**/*.spec.ts'
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Use --auto low for safety</div>

Following cookbook patterns:
```bash
droid exec --auto low "..." # File changes only
# Workflow handles git operations separately
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Trust autonomous discovery</div>

Let droid explore and find relevant docs rather than maintaining manual mappings:
```bash
"Search the docs/ directory for files that reference the changed code"
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Always generate summaries</div>

Help reviewers understand changes:
```bash
"Create doc-update-summary.md explaining what was updated and why"
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Consider rate limits</div>

For high-frequency repos, use scheduled batch updates:
```yaml
schedule:
  - cron: '0 9 * * 1'  # Weekly on Monday
```

</div>

</div>



## Variations {#variations}

### Weekly comprehensive review {#weekly-comprehensive-review}

For repositories with frequent changes, batch updates into a weekly review:

```yaml
on:
  schedule:
    - cron: '0 9 * * 1'  # Monday 9 AM
  workflow_dispatch:  # Allow manual trigger
```

### Multiple documentation directories {#multiple-documentation-directories}

If your docs are spread across multiple locations:

```bash
droid exec --auto low "
Search docs/, guides/, and README.md for documentation to update
based on these code changes: $(cat changed_files.txt)
"
```

### Language-specific targeting {#language-specific-targeting}

Focus on specific file types:

```yaml
on:
  push:
    branches: [main]
    paths:
      - 'src/**/*.ts'
      - 'src/**/*.tsx'
      # TypeScript changes only
```

## Troubleshooting {#troubleshooting}



<Details summary="No PR created even though code changed">
Droid may have determined no docs needed updates. Check the workflow logs or add more specific search instructions in the prompt. You can also check if `doc-update-summary.md` was created to see what droid analyzed.
</Details>





<Details summary="Wrong sections get updated">
Improve the exploration prompt to be more specific about what to look for. Consider adding explicit instructions about which doc sections should or shouldn't be modified.
</Details>





<Details summary="Droid can't find relevant docs">
Make the search instructions more explicit by pointing Droid Exec at specific directories, filenames, or keywords. Providing a short list of likely docs can dramatically improve accuracy.
</Details>





<Details summary="Workflow times out">
For large repositories, consider:
  - Increasing the timeout in the workflow
  - Processing documentation updates in batches
  - Using scheduled updates instead of triggering on every merge
</Details>



## See also {#see-also}

- [[cli/droid-exec/overview|Droid Exec Overview]] - Autonomy levels and capabilities
- [[guides/droid-exec/github-actions|GitHub Actions Cookbook]] - More workflow examples
- [[guides/hooks/documentation-sync|Documentation Sync Hooks]] - Preventive approach
