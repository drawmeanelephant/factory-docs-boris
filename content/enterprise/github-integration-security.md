---
id: enterprise/github-integration-security
title: "GitHub Integration Security"
status: published
summary: "Security architecture, data flows, and controls for the Factory Droid GitHub Action integration."
parent: enterprise/index
tags: [enterprise]
relations: [relates_to=jp/enterprise/github-integration-security]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">GitHub Integration Security</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Security architecture, data flows, and controls for the Factory Droid GitHub Action integration.</p>


The Factory Droid GitHub Action enables automated code review and PR assistance directly within your GitHub workflows. This page explains the security architecture, data flows, and controls that govern how the integration operates.

---

## Overview {#overview}

The Droid GitHub Action (`Factory-AI/droid-action`) runs **entirely inside GitHub Actions** using your own runners. It does not require a separate hosted service or persistent connection to Factory infrastructure beyond standard API authentication.



<div class="factory-card-group">

<div class="factory-card">

**Runs in your environment**

The action executes on GitHub‑hosted or self‑hosted runners you control. No
external compute resources are provisioned.

</div>


  

<div class="factory-card">

**No persistent code storage**

Code is checked out transiently for the workflow run and discarded
afterward. Factory does not store your source code.

</div>


  

<div class="factory-card">

**Scoped permissions**

The action requests only the GitHub permissions it needs and tokens are
automatically revoked after each run.

</div>


  

<div class="factory-card">

**Standard Factory authentication**

Uses your Factory API key, subject to your org's existing model allowlists,
rate limits, and policies.

</div>

</div>



---

## Architecture and data flows {#architecture-and-data-flows}

When a workflow runs, the following sequence occurs:

1. **Trigger detection** – The action detects `@droid` mentions in PR comments, descriptions, or review comments.
2. **Permission verification** – Before executing, the action verifies the triggering user has write access to the repository.
3. **Context gathering** – Droid collects PR metadata, changed files, and existing comments from the checked‑out repository.
4. **Droid Exec** – The CLI runs with GitHub MCP tools pre‑registered, allowing it to interact with the PR via GitHub APIs.
5. **LLM requests** – Prompts are sent to your configured model providers through Factory's standard routing.
6. **Results** – Droid posts inline comments or updates the PR description directly via GitHub APIs.
7. **Token revocation** – GitHub App tokens are automatically revoked at the end of the workflow.

### Data boundaries {#data-boundaries}

| Data type           | Where it flows                     | Retention                                |
| ------------------- | ---------------------------------- | ---------------------------------------- |
| Source code         | GitHub runner (transient checkout) | Discarded after workflow                 |
| PR metadata         | GitHub APIs                        | GitHub's retention policies              |
| Prompts and context | Configured LLM providers           | Per your model provider agreements       |
| Workflow logs       | GitHub Actions                     | Your repository's log retention settings |
| Debug artifacts     | GitHub Actions artifacts           | 7 days (configurable)                    |

---

## Authentication and authorization {#authentication-and-authorization}

### Factory API key {#factory-api-key}

The action requires a Factory API key (`FACTORY_API_KEY`) stored as a GitHub secret. This key:

- Authenticates Droid Exec sessions with Factory's API.
- Is subject to your org's model allowlists, rate limits, and policies.
- Should be rotated regularly following your organization's key management practices.



<Aside kind="warning">
Never commit API keys directly to your repository. Always use GitHub Actions
  secrets.
</Aside>



### GitHub App tokens {#github-app-tokens}

When using the Factory Droid GitHub App:

- The app requests an installation token scoped to the specific repository.
- Tokens are short‑lived and automatically revoked after the workflow completes.
- The app only requests permissions necessary for its operation (contents, pull requests, issues).

If you prefer not to use the GitHub App, you can provide a custom `github_token` input with appropriate permissions.

### User permission verification {#user-permission-verification}

Before executing any `@droid` command, the action verifies:

1. The triggering user has **write access** to the repository.
2. The user is not a bot (unless explicitly allowed via `allowed_bots` input).
3. The comment or trigger matches the expected format.

This prevents unauthorized users from invoking Droid.

---

## Security controls {#security-controls}

### Permission scoping {#permission-scoping}

The action requests only the GitHub permissions it needs:

```yaml
permissions:
  contents: write # Read code, write for fixes
  pull-requests: write # Comment on and update PRs
  issues: write # Comment on issues
  id-token: write # OIDC token for secure auth
  actions: read # Read workflow run metadata
```

You can further restrict permissions in your workflow file based on your security requirements.

### Bot and user filtering {#bot-and-user-filtering}

Control who can trigger the action:

| Input                     | Purpose                                                                                  |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| `allowed_bots`            | Comma‑separated list of bot usernames allowed to trigger, or `*` for all. Default: none. |
| `allowed_non_write_users` | Usernames to allow without write permissions. Use with extreme caution.                  |

### Network restrictions (experimental) {#network-restrictions-experimental}

For enhanced security, you can restrict network access during Droid execution:

```yaml
- uses: Factory-AI/droid-action@main
  with:
    factory_api_key: ${{ secrets.FACTORY_API_KEY }}
    experimental_allowed_domains: |
      api.factory.ai
      api.anthropic.com
      api.openai.com
```

This limits outbound connections to only the specified domains.

### Secrets protection {#secrets-protection}

The action follows security best practices for secrets handling:

- API keys are passed via environment variables from GitHub secrets.
- The `show_full_output` option is disabled by default to prevent accidental exposure of sensitive data in logs.
- Debug artifacts are retained for only 7 days by default.



<Aside kind="warning">
Enabling `show_full_output` may expose sensitive information in publicly
  visible workflow logs. Only enable for debugging in non‑sensitive
  environments.
</Aside>



---

## Audit and monitoring {#audit-and-monitoring}

### Workflow logs {#workflow-logs}

All Droid activity is logged in GitHub Actions workflow runs, providing:

- Timestamps for all operations.
- Command inputs and outputs (unless containing sensitive data).
- Success/failure status for each step.
- Links to any comments or changes made.

### Debug artifacts {#debug-artifacts}

The action uploads debug artifacts including:

- Droid session logs.
- Console output.
- Session metadata.

These artifacts are retained for 7 days by default and can be used for troubleshooting or audit purposes.

### Integration with Factory telemetry {#integration-with-factory-telemetry}

If your organization uses Factory's OTEL telemetry, Droid Exec sessions from GitHub Actions are included in your telemetry data, providing:

- Session metrics tagged with repository and workflow context.
- LLM usage and cost attribution.
- Tool invocation tracking.

See [[enterprise/compliance-audit-and-monitoring|Compliance, Audit & Monitoring]] for details on Factory's telemetry capabilities.

---

## Deployment recommendations {#deployment-recommendations}





<Details summary="For security‑conscious organizations">
1. **Use repository secrets** – Store `FACTORY_API_KEY` as a repository or organization secret.
  2. **Review workflow permissions** – Ensure the workflow file requests only necessary permissions.
  3. **Restrict bot access** – Keep `allowed_bots` empty unless you have a specific need.
  4. **Enable branch protection** – Require PR reviews before merging Droid‑assisted changes.
  5. **Monitor workflow runs** – Review Droid activity in your GitHub Actions logs regularly.
  6. **Consider network restrictions** – Use `experimental_allowed_domains` to limit network access.
</Details>



  

<Details summary="For regulated environments">
- **Self‑hosted runners** – Run the action on self‑hosted runners in your controlled environment.
  - **Model allowlists** – Configure Factory org policies to restrict which models Droid can use.
  - **Audit retention** – Adjust artifact retention periods to meet your compliance requirements.
  - **Integrate with SIEM** – Export GitHub Actions logs and Factory telemetry to your security monitoring tools.
</Details>





---

## Comparison with other deployment patterns {#comparison-with-other-deployment-patterns}

| Aspect                | GitHub Action       | CLI on developer machine  | Droid Exec in CI            |
| --------------------- | ------------------- | ------------------------- | --------------------------- |
| Execution environment | GitHub runners      | Local workstation         | Your CI runners             |
| Code access           | Transient checkout  | Full local access         | Transient checkout          |
| Authentication        | Factory API key     | Factory API key           | Factory API key             |
| Trigger               | PR events, comments | Manual invocation         | CI pipeline events          |
| Audit trail           | GitHub Actions logs | Local + Factory telemetry | CI logs + Factory telemetry |

All deployment patterns use the same underlying Droid Exec runtime and are subject to the same Factory org policies.
