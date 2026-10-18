---
id: onboarding/integrating-with-your-engineering-system/github-enterprise-server
title: "GitHub Enterprise Server"
status: published
summary: "Comprehensive guide for connecting Factory with your GitHub Enterprise Server instance"
parent: onboarding/integrating-with-your-engineering-system/index
tags: [onboarding]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">GitHub Enterprise Server</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Comprehensive guide for connecting Factory with your GitHub Enterprise Server instance</p>


Factory can connect to a self-hosted GitHub Enterprise Server (GHES) instance using OAuth, making your organization's GHES repositories available inside Factory. Setup is self-service: an admin registers an OAuth App on the GHES instance and enters its credentials in Factory. 

This guide covers both the one-time **admin setup** and **day-to-day usage** for end users.

> Connecting to a GitHub Enterprise Server instance is only supported in the Enterprise plan.

## Part 1: Admin Setup (one-time) {#part-1-admin-setup-one-time}

### Prerequisites {#prerequisites}

- You are an **Owner/Manager** in your Factory organization (a privileged role is required to configure the integration).
- You have access to create an **OAuth App** on your GHES instance.
- Your GHES instance must have a **publicly reachable domain** and be accessible over the public internet. Factory validates that the server domain resolves to a public IP address. *(Note: If your instance is behind a proxy or firewall, please contact Factory Support to obtain the specific Factory IP addresses you will need to allowlist.)*

### Step 1: Create an OAuth App on GHES {#step-1-create-an-oauth-app-on-ghes}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Navigate to Developer Settings</div>

In GHES, go to **Settings \> Developer settings \> OAuth Apps \> New OAuth App** (you may create it under your personal account or under an organization you own).

</div>


  

<div class="factory-step">

<div class="factory-step-title">Fill in Application Details</div>

- **Application name**: e.g. `Factory Integration`
  - **Homepage URL**: your Factory URL (e.g., `https://app.factory.ai`)
  - **Authorization callback URL**: `https://<your-factory-api-domain>/api/integrations/redirect/github-es/callback`
*(Note: If you use the Factory control plane, your API domain will be `api.factory.ai`)*

</div>


  

<div class="factory-step">

<div class="factory-step-title">Generate Credentials</div>

Register the app, then copy the **Client ID** and generate a **Client Secret**. Securely store the Client Secret.

</div>

</div>



### Step 2: Configure the integration in Factory {#step-2-configure-the-integration-in-factory}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Enter Server Details</div>

In Factory, open **Settings \> Integrations** and choose **GitHub Enterprise Server**. Enter your GHES details:
  - **Server domain** (e.g. `https://github.your-company.com`)
  - **Client ID**
  - **Client Secret**

</div>


  

<div class="factory-step">

<div class="factory-step-title">Save Configuration</div>

Save the configuration. Factory will normalize and validate the domain.

</div>

</div>



### Step 3: Authorize {#step-3-authorize}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Start the Connection</div>

Click to authorize the integration. You are redirected to your GHES instance to authorize the OAuth App. 
*(Requested scopes: **`repo`** and **`read:org`**)*

</div>


  

<div class="factory-step">

<div class="factory-step-title">Import Repositories</div>

After you approve, Factory imports the repositories the authorizing account can access. Note that Factory **only exposes org-level repositories**, not user-level (personal) repositories.

</div>

</div>



### Important security notes for admins {#important-security-notes-for-admins}

- **One authorization serves the whole org.** The connecting admin's OAuth authorization is stored at the organization level and used for all of your org's GHES operations in Factory.
- **Use a dedicated service account** as the connecting admin rather than a personal employee account. This avoids tying org-wide access to one person's account lifecycle and lets you bound which repositories are exposed.
- **Repository scope.** Factory only exposes organization-level repositories. Personal (user-level) repositories accessible to the authorizing account are not imported into Factory.
- **Token lifecycle.** If your OAuth App issues expiring tokens, Factory refreshes them automatically. If it issues non-expiring tokens, the authorization is long-lived. Revoking the authorization or rotating the client secret disconnects the integration for the whole org.
- **Network reachability.** Factory validates and pins the resolved public IP for GHES requests (SSRF protection), so the instance must have a publicly reachable domain and be publicly resolvable. If your organization uses a proxy, contact Factory support for the IP addresses you need to allowlist.

---

## Part 2: End-User Guide {#part-2-end-user-guide}

### What you get {#what-you-get}

Once your admin has connected GHES, your organization's GHES repositories appear in Factory alongside your other repositories, and you can use them in sessions like any other repo.

### Accessing GHES repos {#accessing-ghes-repos}

- GHES access is enabled **at the organization level**. You do **not** need to authorize GHES individually.
- Repositories are available to members of your Factory org for whom the GHES integration is enabled.

### Troubleshooting {#troubleshooting}

- **A repo I expect is missing.** It may be excluded because its owner/org is not part of the connected account's visibility, or because it is a personal (user-level) repository, which Factory does not expose. Confirm with your admin.
- **GHES repos suddenly disappeared or auth is failing.** The organization's GHES authorization may have expired or been revoked. Ask your admin to reconnect the integration.

---

## FAQ {#faq}

**Does each user authorize GHES separately?** 
No. One admin authorization is shared org-wide; access is gated at the organization level.

**What permissions does Factory request?** 
The `repo` and `read:org` OAuth scopes.



<div class="factory-card">

**[Security and Compliance](https://trust.factory.ai)**

Visit Factory's Trust Center for compliance documents, certifications, and security resources

</div>
