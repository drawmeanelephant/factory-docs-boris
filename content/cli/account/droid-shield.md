---
id: cli/account/droid-shield
title: "Droid Shield"
status: published
summary: "Automatic secret detection to prevent accidental exposure of credentials in your git commits and pushes."
parent: cli/account/index
tags: [cli, droid-shield, secrets, credentials, api-keys, detection, security]
relations: [relates_to=jp/cli/account/droid-shield]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Droid Shield</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Automatic secret detection to prevent accidental exposure of credentials in your git commits and pushes.</p>


## What is Droid Shield? {#what-is-droid-shield}

Droid Shield is a built-in security feature that automatically scans un-committed changes for potential secrets before committing and pushing them to remote. It acts as a safety net to prevent accidental exposure of sensitive credentials like API keys, tokens, and passwords in your version control history.



<Aside kind="tip">
**Looking for advanced protection?** [[cli/account/droid-shield-plus|Droid Shield Plus]] provides AI-powered security scanning with prompt injection detection, enhanced secrets detection, and sensitive data protection. Available for enterprise customers.
</Aside>



---

## How Droid Shield Works {#how-droid-shield-works}

When you use Droid to perform `git commit` or `git push` operations, Droid Shield automatically:

1. **Scans the diff** - Analyzes only the lines being added (not removed or unchanged)
2. **Detects secrets** - Uses pattern matching to identify potential credentials
3. **Blocks execution** - Stops the git operation if secrets are detected
4. **Reports findings** - Shows exactly where potential secrets were found



<Aside kind="note">
Droid Shield only scans git operations performed through Droid. Manual git commands run outside of Droid are not affected.
</Aside>



---

## What Droid Shield Detects {#what-droid-shield-detects}

Droid Shield scans for a wide range of credential patterns, including:



<div class="factory-card-group">

<div class="factory-card">

**API Keys & Tokens**

Factory API keys, GitHub tokens, GitLab tokens, npm tokens, and API keys from (e.g. AWS, Google Cloud, Stripe, SendGrid) and more.

</div>


  

<div class="factory-card">

**Authentication Credentials**

(e.g. JWT, OAuth, session tokens), and URLs with embedded credentials.

</div>


  

<div class="factory-card">

**Private Keys**

(e.g. SSH private keys, PGP keys, age secret keys, OpenSSH keys), and other cryptographic key formats.

</div>


  

<div class="factory-card">

**Service-Specific Secrets**

(e.g. Slack webhooks and tokens, Twilio credentials, Mailchimp keys, Square OAuth secrets, Azure storage keys).

</div>

</div>



### Detection Algorithm {#detection-algorithm}

Droid Shield uses smart pattern matching with randomness validation:

- **Pattern matching** - Identifies credentials by format
- **Randomness check** - Validates that captured values look like actual secrets
- **Context awareness** - Considers variable names and assignment patterns to reduce false positives

---

## Droid Shield 2.0: Learned Secret Detection {#droid-shield-20-learned-secret-detection}

Droid Shield 2.0 augments the deterministic scanner with two fine-tuned classification models that add a semantic layer on top of pattern-based detection. Every commit and push still passes through the deterministic scanner first; the models then classify specific contexts the scanner flagged or missed.



<Aside kind="note">
Droid Shield 2.0 is in research preview. To enable it for your organization, [contact us](mailto:support@factory.ai).
</Aside>



### The Two Classification Models {#the-two-classification-models}

The models sit on opposite sides of the deterministic scanner and are optimized for distinct failure modes:



<div class="factory-card-group">

<div class="factory-card">

**Risk model**

Runs on changed lines the deterministic scanner did **not** fire on, but that still look secret-bearing based on surrounding context. Optimized for recall to catch real secrets the pattern set would miss. Produces a warning when it flags a possible missed secret.

</div>


  

<div class="factory-card">

**Downgrade model**

Runs on lines where the scanner **did** fire. It reviews the surrounding context with the detected secret masked out, and decides whether the scanner hit is a true positive (keep blocking) or a false alarm (downgrade to a warning).

</div>

</div>



---

## When Droid Shield Activates {#when-droid-shield-activates}

Droid Shield automatically activates during these git operations:

- **`git commit`** - Scans staged changes before creating the commit
- **`git push`** - Scans commits that would be pushed to the remote



<Aside kind="warning">
If secrets are detected, the git operation is blocked to prevent credential exposure. You'll need to remove the secrets before proceeding.
</Aside>



---

## Managing Droid Shield Settings {#managing-droid-shield-settings}

### In the CLI {#in-the-cli}

You can toggle Droid Shield on or off through the settings menu:

1. Run `droid`
2. Enter `/settings`
3. Toggle **"Droid Shield"** setting
4. Changes take effect immediately



<Aside kind="info">
Droid Shield is **enabled by default** for your protection. We strongly recommend keeping it enabled.
</Aside>



---

## What to Do if Secrets are Detected {#what-to-do-if-secrets-are-detected}

When Droid Shield detects potential secrets, you'll see an error message like:

```
Droid-Shield has detected potential secrets in 2 location(s) across files:
src/config.ts, .env.example

If you would like to override, you can either:
1. Perform the commit/push yourself manually
2. Disable Droid Shield by running /settings and toggling the "Droid Shield" option
```

### Recommended Actions {#recommended-actions}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Review the findings</div>

Carefully examine the files and lines mentioned to identify what was detected.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Remove the secrets</div>

- Use environment variables instead of hardcoded credentials
  - Move secrets to secure credential stores
  - Add sensitive files to `.gitignore`
  - Use git filter-branch or BFG Repo-Cleaner if secrets were already committed

</div>


  

<div class="factory-step">

<div class="factory-step-title">Retry the operation</div>

Once secrets are removed, run the git command again through Droid.

</div>

</div>





<Aside kind="warning">
**Never disable Droid Shield just to bypass the check.** Exposed credentials can lead to security breaches, unauthorized access, and compliance violations.
</Aside>



### If You Get a False Positive {#if-you-get-a-false-positive}

Droid Shield uses conservative patterns to err on the side of caution. If you believe a detection is a false positive:

1. **Verify it's not a real secret** - Double-check that the value isn't sensitive
2. **Use a manual commit** - Perform the git operation yourself outside of Droid
3. **Report the pattern** - Contact support@factory.ai if you encounter recurring false positives



<Aside kind="note">
When Droid Shield 2.0 is enabled, the downgrade model automatically reviews scanner hits and can clear obvious false alarms (placeholders, examples, test fixtures) without manual intervention.
</Aside>



---

## Best Practices {#best-practices}





<Details summary="Use environment variables">
Store all secrets in environment variables or secure credential managers, never hardcode them in source files.

```bash
# Good - Using environment variable
const apiKey = process.env.FACTORY_API_KEY;

# Bad - Hardcoded secret
const apiKey = "YOUR_API_KEY_HERE";
```
</Details>


  
  

<Details summary="Keep Droid Shield enabled">
Droid Shield provides an essential safety layer. Keep it enabled at all times, especially in team environments.
</Details>


  
  

<Details summary="Review before committing">
Even with Droid Shield, manually review your changes before committing to ensure no sensitive data is included.
</Details>


  
  

<Details summary="Educate your team">
Make sure all team members understand how Droid Shield works and why it's important to keep it enabled.
</Details>





---

## Limitations {#limitations}



<Aside kind="note">
**Droid Shield is a detection tool, not a guarantee.** While it catches many common secret patterns, the deterministic scanner alone cannot detect:
  - Custom secret formats not in the pattern database
  - Secrets that don't follow recognizable patterns
  - Obfuscated or encoded credentials
  - Business logic vulnerabilities or code security issues
</Aside>



---

## Related Resources {#related-resources}



<div class="factory-card-group">

<div class="factory-card">

**[[cli/account/security|Security Overview]]**

Learn about Factory's comprehensive security features and best practices.

</div>


  

<div class="factory-card">

**[[cli/configuration/settings|Settings]]**

Configure Droid settings including Droid Shield preferences.

</div>


  

<div class="factory-card">

**[Droid Shield 2.0 Research Post](https://factory.ai/news/droid-shield-2-0)**

Technical deep dive on the learned classification models, training data, and evaluation results.

</div>


  

<div class="factory-card">

**[[enterprise/llm-safety-and-agent-controls|Agent Safety & Controls]]**

How Droid Shield fits into the broader enterprise safety model.

</div>

</div>



---

## Need Help? {#need-help}



<div class="factory-card-group">

<div class="factory-card">

**Security Questions**

Email our security team: **security@factory.ai**

</div>


  

<div class="factory-card">

**False Positives**

Contact **support@factory.ai** to report persistent false positive patterns.

</div>

</div>
