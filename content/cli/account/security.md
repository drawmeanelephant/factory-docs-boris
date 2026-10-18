---
id: cli/account/security
title: "Security"
status: published
summary: "How the Droid CLI keeps your code and data secure with built-in protections and best practices."
parent: cli/account/index
tags: [cli, security, authentication, permissions, encryption, data-protection, privacy, secure]
relations: [relates_to=jp/cli/account/security]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Security</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">How the Droid CLI keeps your code and data secure with built-in protections and best practices.</p>


## Security-First Design {#security-first-design}

The Droid CLI is built with security at its core. Your code stays secure through encrypted authentication, strict permissions, and enterprise-grade protections.

---

## Key Security Features {#key-security-features}



<div class="factory-card-group">

<div class="factory-card">

**Secure Authentication**

OAuth login with encrypted token storage. Tokens auto-rotate every 30 days and are stored with OS-level file permissions.

</div>


  

<div class="factory-card">

**Permission Controls**

All risky operations require explicit approval. Configure tool permissions from allow/ask/reject per your security needs.

</div>


  

<div class="factory-card">

**Data Encryption**

All data encrypted in transit (TLS 1.3) and at rest (AES-256 with AWS KMS). Factory never trains on your code.

</div>


  

<div class="factory-card">

**Local Execution**

Shell commands and file edits run locally. Only necessary context and diffs are sent to Factory's secure cloud.

</div>


  

<div class="factory-card">

**OS-Level Sandbox (Beta)**

Optional kernel-enforced isolation for filesystem and network access. See [[cli/configuration/sandbox|Sandbox]].

</div>

</div>



---

## Security Best Practices {#security-best-practices}



<Aside kind="warning">
Always review suggested code and commands before approval. You control what Droid can access and execute.
</Aside>



### Essential Security Guidelines {#essential-security-guidelines}





<Details summary="Review before approving">
**Always verify proposed commands and file changes**, especially:
  - Commands that install packages or modify system files
  - Operations involving sensitive data or credentials  
  - Network requests to external services
  - File operations outside your project directory
</Details>


  
  

<Details summary="Use isolated environments">
**Run Droid in containers or VMs** when working with:
  - Untrusted code repositories
  - External APIs or web services
  - Experimental or potentially risky operations
  - Shared development environments
</Details>


  
  

<Details summary="Manage permissions carefully">
**Configure tool permissions** to match your security requirements:
  - Set high-risk commands to "reject" by default
  - Use "ask" for medium-risk operations requiring oversight
  - Only "allow" low-risk commands you trust completely
  - Review permissions regularly with the Settings menu
</Details>


  
  

<Details summary="Protect sensitive data">
**Never include secrets in prompts:**
  - Use environment variables for API keys and tokens
  - Store credentials in secure credential managers
  - Exclude sensitive files from Droid's working directory
  - Use the FACTORY_TOKEN environment variable for CI/CD
</Details>





---

## Built-in Protections {#built-in-protections}

The Droid CLI includes multiple layers of security:

- **Write access restriction**: Can only modify files in the project directory and subdirectories
- **Command approval**: Risky operations require explicit user confirmation
- **Prompt injection detection**: Analyzes requests for potentially harmful instructions
- **Network request controls**: Web-fetching tools require approval by default
- **Input sanitization**: Prevents command injection attacks
- **Session isolation**: Each conversation maintains separate, secure context

---

## Enterprise Security {#enterprise-security}



<div class="factory-card-group">

<div class="factory-card">

**SSO & Identity**

SAML 2.0 / OIDC single sign-on with SCIM provisioning and role-based access controls.

</div>


  

<div class="factory-card">

**Data Governance**

Zero data retention mode, customer-managed encryption keys (BYOK), and private cloud deployments.

</div>


  

<div class="factory-card">

**Compliance**

SOC 2 Type II certified, GDPR compliant, with regular penetration testing and supply chain security.

</div>


  

<div class="factory-card">

**Audit & Monitoring**

Complete session logging, OpenTelemetry metrics, and enterprise-managed security policies.

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

**Trust Center**

Visit **[trust.factory.ai](https://trust.factory.ai)** for compliance documents, certifications, and security resources.

</div>

</div>





<Aside kind="note">
Report security vulnerabilities through our responsible disclosure program. Contact security@factory.ai for details.
</Aside>
