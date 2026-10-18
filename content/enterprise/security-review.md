---
id: enterprise/security-review
title: "Security Review"
status: published
summary: "Run security-focused PR reviews and full-codebase audits with Droid using STRIDE, OWASP, and supply-chain methodology."
parent: enterprise/index
tags: [enterprise, security-review, security-audit, stride, owasp, owasp-llm-top-10, supply-chain, code-review]
relations: [relates_to=jp/enterprise/security-review]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Security Review</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Run security-focused PR reviews and full-codebase audits with Droid using STRIDE, OWASP, and supply-chain methodology.</p>


Droid security review is a dedicated security workflow for finding high-confidence vulnerabilities in pull requests or across an entire repository. It can run locally from the CLI or automatically in GitHub Actions.



<div class="factory-card-group">

<div class="factory-card">

**PR security review**

Review only the pull request diff, trace changed data flows, and post inline security findings with severity and suggested fixes.

</div>


  

<div class="factory-card">

**Full-codebase audit**

Audit every source file in the repository, group files for parallel review, and produce a structured report of validated findings.

</div>

</div>



## Run a full-codebase audit {#run-a-full-codebase-audit}

For the most thorough security results, run the audit inside a [[features/missions/overview|Mission]]. Missions plan the audit upfront, fan out work across orchestrated agents, and validate findings at each milestone, which produces dramatically deeper coverage than a single-session run.

From any Droid session, enter a mission and kick off the security review:

```text
/missions
/security-review deep audit
```

### Periodic scan in CI {#periodic-scan-in-ci}

Run the same mission-based audit on a schedule by invoking `droid exec --mission` from a workflow. The audit writes its full output under `~/security-audits/<slug>-<YYYYMMDD>/` on the runner, so add an `actions/upload-artifact` step to preserve findings after the runner exits:

```yaml
on:
  schedule:
    - cron: '0 6 * * 1'

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Droid CLI
        run: |
          curl -fsSL https://app.factory.ai/cli | sh
          echo "$HOME/.local/bin" >> "$GITHUB_PATH"
      - name: Run deep security review
        env:
          FACTORY_API_KEY: ${{ secrets.FACTORY_API_KEY }}
        run: |
          droid exec --mission --auto high -m claude-opus-4-7 \
            "/security-review across the entire repository"
      - name: Upload security review output
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: deep-security-review-${{ github.run_id }}
          path: ~/security-audits/
          if-no-files-found: warn
          retention-days: 90
```

## Run locally on a diff {#run-locally-on-a-diff}

To review the current diff in your working tree or branch from the CLI, run the built-in skill in any Droid session:

```text
/security-review local diff
```

When invoked on a diff, Droid traces changed data flows across authentication, authorization, validation, database, network, filesystem, and LLM boundaries, and reports validated findings inline with severity and suggested fixes.

## Run in GitHub CI on pull requests {#run-in-github-ci-on-pull-requests}

With [Droid Action](https://github.com/Factory-AI/droid-action), comment on a pull request to trigger an on-demand security review:

```text
@droid security
```

To run security review automatically on every non-draft PR, add `automatic_security_review: true` to your review workflow:

```yaml
- name: Run Droid Auto Review
  uses: Factory-AI/droid-action@main
  with:
    factory_api_key: ${{ secrets.FACTORY_API_KEY }}
    automatic_review: true
    automatic_security_review: true
```

When `automatic_review` and `automatic_security_review` are both enabled, Droid runs the security pass alongside the standard code review and includes the security summary in the PR feedback.

## Configuration {#configuration}

These are the Droid Action security inputs currently wired for the workflows documented on this page:

| Input | Default | Description |
| --- | --- | --- |
| `automatic_security_review` | `false` | Run security review automatically on PRs without requiring `@droid security`. |
| `security_model` | `""` | Override the model used for security review candidate generation and full-repository scans. Falls back to `review_model` if unset. |
| `security_severity_threshold` | `medium` | Full-repository scans only: minimum severity to include in the generated report. |
| `security_notify_team` | `""` | Full-repository scans only: GitHub team to cc in the generated scan PR body, such as `@org/security-team`. |

## Methodology {#methodology}

Security review uses the built-in `security-review` skill. In PR automation, Droid Action runs a dedicated `security-reviewer` subagent that loads this methodology before reading files, then traces changed data flows across authentication, authorization, validation, database, network, filesystem, and LLM boundaries.

The methodology applies multiple security frameworks together:

- **STRIDE threat modeling**: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege.
- **OWASP Top 10:2021**: Broken access control, cryptographic failures, injection, insecure design, misconfiguration, vulnerable components, authentication failures, integrity failures, logging failures, and SSRF.
- **OWASP Top 10 for LLM Applications:2025**: prompt injection, sensitive information disclosure, insecure LLM output handling, excessive agency, vector/embedding weaknesses, and other AI-specific risks when the codebase uses LLMs.
- **Supply-chain analysis**: dependency manifest and lockfile review, including typosquatting signals, install scripts, overly broad version ranges, and newly published packages.
- **Repository threat-model context**: if `.factory/threat-model.md` exists, Droid uses it as the attack-surface map.

### Review pipeline {#review-pipeline}

Security review uses a two-pass workflow:

1. **Candidate generation**: Droid reads the diff or codebase, identifies security-relevant areas, traces untrusted input across trust boundaries, and produces candidate vulnerabilities.
2. **Validation**: Droid re-checks each candidate for reachability, exploitability, existing controls, and false positives before reporting it.

Findings are reported only when there is a realistic exploit path, such as an injection vulnerability, missing authentication or authorization on a sensitive operation, hardcoded secret, data exposure, unsafe LLM output handling, or risky supply-chain change.

### Severity levels {#severity-levels}

| Severity | Priority | Examples |
| --- | --- | --- |
| Critical | `P0` | RCE, hardcoded production secret, auth bypass, unauthenticated admin endpoint |
| High | `P1` | SQL injection behind auth, stored XSS, sensitive-data IDOR, very new dependency |
| Medium | `P2` | CSRF on state-changing operations, information disclosure, prompt injection behind auth |
| Low | `P3` | Minor security hardening with a concrete but low-impact exploit path |

## See also {#see-also}

- [[features/missions/overview|Missions]]: Plan and orchestrate large multi-step work, including thorough audits.
- [[guides/droid-exec/code-review|Automated Code Review]]: Standard PR code review automation.
- [[cli/configuration/skills|Skills]]: How to invoke and customize skills.
- [[enterprise/github-integration-security|GitHub Integration Security]]: Security architecture for the GitHub App integration.
