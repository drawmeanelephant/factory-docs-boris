---
id: enterprise/eu-deployment
title: "EU Deployment"
status: published
summary: "Architecture, data residency, and region enforcement for Factory's EU deployment."
parent: enterprise/index
tags: [enterprise]
relations: [relates_to=jp/enterprise/eu-deployment]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">EU Deployment</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Architecture, data residency, and region enforcement for Factory&#x27;s EU deployment.</p>


Factory operates a dedicated EU deployment, fully isolated from the Global (US) deployment, with its own backend, database, and LLM inference endpoints in Europe. Each Factory client (CLI, desktop app, and web app) ships as a single build that works in both regions; after login, the client detects the organization's region and routes all subsequent requests to the correct deployment.



<Aside kind="info">
**Enterprise Feature** — The EU deployment is available to enterprise customers with European data-residency requirements. [Contact us](mailto:sales@factory.ai) to provision an EU organization for your team.
</Aside>



---

## Infrastructure {#infrastructure}

The EU API backend is hosted on Vercel in Frankfurt (`fra1`), within the European Economic Area, and reachable at `api.eu.factory.ai`.

Customers should allowlist `*.factory.ai` hostnames. Outbound LLM traffic from the EU backend targets the EU-region endpoints of the providers listed under [[enterprise/eu-deployment#inference|Inference]].

---

## Data {#data}

**Stored in the EU (`europe-west1`, Belgium):**

- **Session content** (prompts, assistant messages, tool calls and results, Droid messages, Git AI notes, and Git AI checkpoints) lives in a managed database instance in Belgium, provisioned separately from the global database with its own credentials, backups, and access controls.
- Raw request and response bodies are never written to logs or object storage.

**Stored in the global deployment (US):**

- Organization records (a small pointer document with the org's region tag), user profiles, and billing data. These contain no user-generated content and are required for cross-region authentication and account management.

---

## Inference {#inference}

All LLM requests from EU organizations are dispatched to EU-region endpoints only; prompts and conversation history do not transit US infrastructure.



<div class="factory-card-group">

<div class="factory-card">

**Anthropic Claude**

Served via AWS Bedrock (Frankfurt, `eu-central-1`) and Google Vertex AI (`europe-west1`). Includes Claude Opus 4.5, Opus 4.6, Opus 4.7, Sonnet 4.5, Sonnet 4.6, and Haiku 4.5.

</div>


  

<div class="factory-card">

**OpenAI**

Served via the OpenAI direct API using a dedicated project configured for EU data residency. Includes the GPT-5 family (GPT-5.2, GPT-5.3 Codex, GPT-5.4, GPT-5.4 Mini, GPT-5.5, and GPT-5.5 Pro).

</div>

</div>



Models or providers not available in the EU are hidden in the model picker and rejected at the server.

---

## Enforcement {#enforcement}

Identity is global (WorkOS-based SSO), but each organization is pinned to a region at creation time. Region matching is enforced at multiple layers so traffic and data can never be served by the wrong backend.

**Server-side.** Session data access and LLM inference are both gated by region-aware checks on the backend. Requests for an organization whose region does not match the deployment fail closed with an error, and requests for ineligible models or providers are rejected before any traffic is dispatched. EU traffic cannot reach US-only data or providers, and Global traffic cannot reach EU-only routes.

**Client-side.** After login, each client reads the org's region and routes all subsequent API requests to the matching backend:

- **Web app:** Each canonical hostname (`app.factory.ai`, `app.eu.factory.ai`) is statically backed by exactly one regional backend. Users who land on the wrong region are shown a redirect page with a link to the correct origin; they are not signed out.
- **Desktop app:** Reads the org's region from the authenticated session and targets the matching API host on every request.
- **CLI:** The region is pinned to the user's local token cache on first login and used to resolve the API host for every request. Logout and re-login re-derive the region.
