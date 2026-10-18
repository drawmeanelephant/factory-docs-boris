---
id: enterprise/service-accounts
title: "Service Accounts"
status: published
summary: "Non-human identities for running Factory automation in CI/CD pipelines, scripts, and Droid Computers."
parent: enterprise/index
tags: [enterprise]
relations: [relates_to=jp/enterprise/service-accounts]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Service Accounts</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Non-human identities for running Factory automation in CI/CD pipelines, scripts, and Droid Computers.</p>


Service accounts are non-human identities that automate work on behalf of your organization. Use them when a workload should belong to your organization instead of a specific teammate, such as CI/CD pipelines, scripts, Slack automations, or Droid Computers.



<Aside kind="info">
**Enterprise Feature** — Service accounts are available to enterprise customers. [Contact us](mailto:sales@factory.ai) to learn more.
</Aside>



---

## Start with the basics {#start-with-the-basics}



<div class="factory-card-group">

<div class="factory-card">

**Create a service account**

Add a stable identity from the API keys section in Settings. Give it a clear name and optional description so teammates know what it runs. Only managers and owners can create or edit a service account.

</div>


  

<div class="factory-card">

**Generate API keys**

Create keys for scripts, CI jobs, and other automated workloads. Key values are shown only once, so copy them and store them securely.

</div>


  

<div class="factory-card">

**Attach Droid Computers**

Create computers owned by the service account so long-running work can continue under the same identity.

</div>


  

<div class="factory-card">

**Configure Git access**

Use your organization's GitHub App installation for GitHub. For GitLab Cloud, add a service-account GitLab token in Settings.

</div>

</div>



---

## How service accounts work {#how-service-accounts-work}

A service account authenticates with a Factory API key and runs as its own principal. Sessions, computers, billing events, and audit surfaces are attributed to the service account instead of a human user.

Service accounts must be active to authenticate. If you mark one inactive or delete it, new requests using its keys fail, and workloads depending on that identity should be moved or restarted with another account.

---

## Manage access safely {#manage-access-safely}





<Details summary="Use short-lived keys when possible">
Set expiration dates for keys that are used in temporary automation. Short-lived keys limit the blast radius if a key is accidentally exposed.
</Details>



  

<Details summary="Rotate keys regularly">
Create a new key, update the workload, then revoke the old key. Regular rotation reduces the risk of compromised credentials.
</Details>



  

<Details summary="Keep names stable">
Service account names are immutable identifiers. Create a new service account if you need a different name.
</Details>



  

<Details summary="Delete when finished">
Deleting a service account revokes its access and cleans up owned Factory resources where possible.
</Details>





---

## Common use cases {#common-use-cases}



<div class="factory-card-group">

<div class="factory-card">

**CI/CD**

Run release, testing, or deployment workflows without depending on one engineer's account.

</div>


  

<div class="factory-card">

**Slack automation**

Configure channels or workflows to run Droid as a shared team identity.

</div>


  

<div class="factory-card">

**Repository automation**

Clone, push, and operate on repositories with credentials managed for the service account.

</div>


  

<div class="factory-card">

**Persistent computers**

Keep Droid Computers tied to an automation identity instead of a teammate's personal account.

</div>

</div>
