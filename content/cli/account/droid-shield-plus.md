---
id: cli/account/droid-shield-plus
title: "Droid Shield Plus"
status: published
summary: "AI-powered security scanning for prompt injection, secrets detection, and sensitive data protection. Enterprise feature powered by Palo Alto Networks Prisma AIRS."
parent: cli/account/index
tags: [cli, droid-shield-plus, prisma-airs, prompt-injection, secrets-detection, dlp, enterprise-security, ai-security]
relations: [relates_to=jp/cli/account/droid-shield-plus]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Droid Shield Plus</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">AI-powered security scanning for prompt injection, secrets detection, and sensitive data protection. Enterprise feature powered by Palo Alto Networks Prisma AIRS.</p>




<Aside kind="info">
**Enterprise Feature** — Droid Shield Plus is available for enterprise customers. [Contact us](mailto:sales@factory.ai) to enable this feature for your organization.
</Aside>



## What is Droid Shield Plus? {#what-is-droid-shield-plus}

Droid Shield Plus is an advanced AI-powered security layer that provides real-time protection against prompt injection attacks, sensitive data exposure, and other security threats. Unlike the standard [[cli/account/droid-shield|Droid Shield]] which uses pattern-based detection, Droid Shield Plus leverages **[Palo Alto Networks Prisma AIRS](https://docs.paloaltonetworks.com/ai-runtime-security)** (AI Runtime Security) to provide intelligent, context-aware security scanning.

---

## Key Features {#key-features}



<div class="factory-card-group">

<div class="factory-card">

**Prompt Injection Detection**

Identifies and blocks malicious prompt injection attempts designed to manipulate AI behavior or bypass security controls.

</div>


  

<div class="factory-card">

**Advanced Secrets Scanning**

AI-powered detection of API keys, tokens, passwords, and credentials with higher accuracy and fewer false positives than pattern matching.

</div>


  

<div class="factory-card">

**Sensitive Data Protection (DLP)**

Detects personally identifiable information (PII), financial data, and other sensitive information before it's exposed in prompts or commits.

</div>


  

<div class="factory-card">

**Malicious Code Detection**

Identifies potentially dangerous code patterns and suspicious content that could pose security risks.

</div>

</div>



---

## How Droid Shield Plus Works {#how-droid-shield-plus-works}

Droid Shield Plus provides two layers of protection:

### 1. Prompt Security Scanning {#1-prompt-security-scanning}

Every prompt you send to Droid is automatically scanned before processing. If a threat is detected, the prompt is blocked and you're notified:

```
Droid Shield Plus has blocked this prompt due to detected: prompt injection, sensitive data.

If you believe this is a false positive, you can disable Droid Shield Plus in settings.
```

**Detected threat categories:**
- **Prompt Injection** — Attempts to manipulate AI instructions
- **Sensitive Data (DLP)** — PII, credentials, or confidential information
- **Toxic Content** — Harmful or inappropriate content
- **Malicious Code** — Suspicious code patterns

### 2. Git Commit Scanning {#2-git-commit-scanning}

When you perform `git commit` or `git push` operations through Droid, Droid Shield Plus scans your staged changes using AI-powered analysis:

```
Droid Shield Plus has detected potential secrets in your staged changes.

If you would like to override, you can either:
1. Perform the commit/push yourself manually
2. Disable Droid Shield Plus in settings
```

This provides significantly more accurate detection than regex-based scanning, catching:
- Obfuscated or encoded secrets
- Context-aware credential detection
- Custom secret formats
- Secrets embedded in complex code structures

---

## Droid Shield vs Droid Shield Plus {#droid-shield-vs-droid-shield-plus}

| Feature | Droid Shield | Droid Shield Plus |
|---------|--------------|-------------------|
| **Detection Method** | Pattern/Regex matching | AI-powered analysis |
| **Prompt Scanning** | No | Yes |
| **Git Commit Scanning** | Yes | Yes |
| **Prompt Injection Detection** | No | Yes |
| **Sensitive Data (DLP)** | Limited | Comprehensive |
| **Toxic Content Detection** | No | Yes |
| **Malicious Code Detection** | No | Yes |
| **False Positive Rate** | Higher | Lower |
| **Availability** | All users | Enterprise |
| **Powered By** | Built-in patterns | Palo Alto Networks Prisma AIRS |



<Aside kind="note">
When Droid Shield Plus is enabled, it replaces the standard Droid Shield for git operations, providing enhanced AI-powered scanning instead of pattern-based detection.
</Aside>



---

## Enabling Droid Shield Plus {#enabling-droid-shield-plus}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Contact Factory</div>

Reach out to [sales@factory.ai](mailto:sales@factory.ai) to enable Droid Shield Plus for your organization.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Enable in Settings</div>

Once enabled for your organization:
  1. Run `droid`
  2. Enter `/settings`
  3. Navigate to the **Security** section
  4. Toggle **"Droid Shield Plus (AI-Powered)"** to On

</div>


  

<div class="factory-step">

<div class="factory-step-title">Verify Activation</div>

You'll see a subtitle confirming: *"AI-powered security scanning for prompt injection, sensitive data, and toxic content. Powered by Palo Alto Networks Prisma AIRS."*

</div>

</div>



---

## Handling Blocked Prompts {#handling-blocked-prompts}

When Droid Shield Plus blocks a prompt or git operation:





<Details summary="Review the detection">
Carefully examine what was flagged. The error message will indicate the threat category (prompt injection, sensitive data, toxic content, or malicious code).
</Details>


  
  

<Details summary="Remove sensitive content">
If sensitive data was detected:
  - Move secrets to environment variables
  - Use secure credential stores
  - Remove PII from prompts
</Details>


  
  

<Details summary="Rephrase if needed">
If prompt injection was detected, rephrase your request to avoid patterns that could be misinterpreted as manipulation attempts.
</Details>


  
  

<Details summary="Report false positives">
If you believe the detection is incorrect, contact [support@factory.ai](mailto:support@factory.ai) with details about the false positive.
</Details>







<Aside kind="warning">
**Never disable Droid Shield Plus just to bypass security checks.** If content is being blocked, there's likely a legitimate security concern that should be addressed.
</Aside>



---

## Security & Privacy {#security-privacy}

Droid Shield Plus is powered by **[Palo Alto Networks Prisma AIRS](https://docs.paloaltonetworks.com/ai-runtime-security)**, a leading AI runtime security platform:

- **Real-time Analysis** — Prompts and code are scanned in real-time with minimal latency
- **Enterprise-Grade Security** — Built on Palo Alto Networks' industry-leading security infrastructure
- **Graceful Degradation** — If the security service is temporarily unavailable, Droid continues to function while logging the issue

---

## Related Resources {#related-resources}



<div class="factory-card-group">

<div class="factory-card">

**[[cli/account/droid-shield|Droid Shield]]**

Learn about the standard pattern-based secret detection included with all Droid accounts.

</div>


  

<div class="factory-card">

**[[cli/account/security|Security Overview]]**

Comprehensive overview of Factory's security features and practices.

</div>

</div>



### Prisma AIRS Documentation {#prisma-airs-documentation}



<div class="factory-card-group">

<div class="factory-card">

**[Prisma AIRS Overview](https://docs.paloaltonetworks.com/ai-runtime-security)**

Official Palo Alto Networks documentation for Prisma AIRS AI Runtime Security platform.

</div>


  

<div class="factory-card">

**[Prisma AIRS API Reference](https://pan.dev/prisma-airs/api/airuntimesecurity/)**

Developer documentation for the Prisma AIRS AI Runtime Security API.

</div>

</div>



---

## Get Droid Shield Plus {#get-droid-shield-plus}



<div class="factory-card">

**[Enable for Your Organization](mailto:sales@factory.ai)**

Contact our sales team at **sales@factory.ai** to enable Droid Shield Plus for your enterprise organization.

</div>
