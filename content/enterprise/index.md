---
id: enterprise/index
title: "Enterprise Overview"
status: published
summary: "How to deploy, secure, and operate Droids in the world’s highest‑security environments."
parent: index
tags: [enterprise]
relations: [relates_to=jp/enterprise/index]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Enterprise Overview</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">How to deploy, secure, and operate Droids in the world’s highest‑security environments.</p>


Factory’s enterprise platform is designed for the **highest‑security customers**—systemically important banks, governments, healthcare, national security, and other regulated organizations.

Instead of forcing you into a single cloud IDE, Droid is a **CLI and agent runtime that runs anywhere**:

- On developer laptops, in any terminal or IDE
- In CI/CD pipelines (GitHub, GitLab, internal runners)
- In VMs, Kubernetes clusters, and hardened devcontainers
- In **fully airgapped environments** with no outbound internet access

This section explains how to deploy Droid safely, govern which models and tools it can use, and observe its behavior at enterprise scale.

---

## What this section covers {#what-this-section-covers}

Use these pages together as your enterprise playbook for Droids:



<div class="factory-card-group">

<div class="factory-card">

**Identity & Access**

How orgs, projects, folders, and users are identified; how SSO/SCIM and RBAC determine who can run Droid
and with which permissions. See [[enterprise/identity-and-access|Identity & Access Management]].

</div>


  

<div class="factory-card">

**Privacy & Data Flows**

Exact data flows for code, prompts, and telemetry across cloud, hybrid, and fully airgapped deployments.
See [[enterprise/privacy-and-data-flows|Privacy, Data Flows & Governance]].

</div>


  

<div class="factory-card">

**Network & Deployment**

Reference architectures for cloud‑managed, hybrid, and fully airgapped deployments, plus proxy and mTLS
configuration. See [[enterprise/network-and-deployment|Network & Deployment Configuration]].

</div>


  

<div class="factory-card">

**LLM Safety & Controls**

How Droid classifies command risk, enforces allow/deny lists, uses Droid Shield for secret scanning, and
integrates hooks and sandboxes. See [[enterprise/llm-safety-and-agent-controls|LLM Safety & Agent Controls]].

</div>


  

<div class="factory-card">

**Models & Integrations**

Hierarchical model allow/deny, LLM gateways, BYOK, MCP servers, droids, commands, and how Droid plugs into
your existing AI stack. See [[enterprise/models-llm-gateways-and-integrations|Models, LLM Gateways & Integrations]].

</div>


  

<div class="factory-card">

**Analytics & Compliance**

OTEL‑native telemetry, analytics, audit logging, and how Factory supports SOC2, ISO 27001, ISO 42001 and
internal regulatory reviews. See [[enterprise/usage-cost-and-analytics|Usage, Cost & Productivity Analytics]] and [[enterprise/compliance-audit-and-monitoring|Compliance, Audit & Monitoring]].

</div>

</div>



---

## Enterprise foundations {#enterprise-foundations}

### Multi‑deployment by design {#multideployment-by-design}

Factory supports three deployment patterns for Droid, all built on the same core binary and configuration model:

1. **Cloud‑managed** – Droid runs on developer machines and CI but uses Factory’s cloud for coordination and optional analytics. Models are either Factory‑brokered or brought by you.
2. **Hybrid enterprise** – Droid runs entirely in your infrastructure (VMs, CI runners, containers), optionally connecting to Factory cloud for UX while all LLMs and telemetry terminate inside your network.
3. **Fully airgapped** – Droid runs in a network with **no outbound internet access**. Models and OTEL collectors are hosted entirely inside this environment; Factory never receives traffic.

You can start in cloud‑managed mode, then migrate critical workloads to hybrid or airgapped environments without changing how developers talk to Droid.

### Hierarchical control, not per‑device drift {#hierarchical-control-not-perdevice-drift}

Enterprise policy is expressed through a **hierarchical settings model**:

- **Org** → global defaults and hard security policies
- **Project** → repo‑level settings committed to `.factory/`
- **Folder** → narrower team or subsystem overrides inside a repo
- **User** → personal preferences only where higher levels are silent

Higher levels **cannot be overridden** by lower ones. Org and project settings extend downward; users can opt into stricter controls but never weaken them. This hierarchy governs models, tools, MCP servers, droids, commands, autonomy levels, and telemetry destinations.

Learn more in [[enterprise/hierarchical-settings-and-org-control|Hierarchical Settings & Org Control]].

### Defense‑in‑depth agent safety {#defenseindepth-agent-safety}

LLMs are probabilistic; Factory treats them as powerful but untrusted components. Droid’s safety story combines:

- **Deterministic controls** – command risk classification, allow/deny lists, file and repo protections, and sandbox boundaries
- **Droid Shield** – secret scanning and DLP‑style checks across prompts, files, and commands
- **Hooks** – programmable enforcement points (pre‑prompt, pre‑tool, pre‑command, pre‑git, post‑edit) to integrate with your own security systems
- **Sandboxed runtimes** – running Droid inside devcontainers and hardened VMs for high‑risk work

These layers are independent of which LLM or IDE a developer prefers.

### OTEL‑native observability {#otelnative-observability}

All serious enterprise deployments need to answer: _“What are agents doing, where, and at what cost?”_

Droid emits **OpenTelemetry metrics, traces, and logs** so you can:

- Send telemetry directly to existing collectors (Prometheus, Datadog, Splunk, Jaeger, etc.)
- Track sessions, LLM usage, code edits, tool invocations, and errors per org/team/user
- Correlate Droid activity with SDLC metrics you already use

Factory’s own cloud analytics are **optional**; high‑security customers can route all telemetry exclusively to their own infrastructure.

See [[enterprise/usage-cost-and-analytics|Usage, Cost & Productivity Analytics]] and [[enterprise/compliance-audit-and-monitoring|Compliance, Audit & Monitoring]].

---

## Trust & compliance {#trust-compliance}

Factory maintains a security and compliance posture suitable for the most demanding organizations:

- **SOC 2**
- **ISO 27001**
- **ISO 42001**

You can find the latest reports, sub‑processor lists, and security architecture details in our **[Trust Center](https://trust.factory.ai)**.

For a deeper dive into how Droid fits your regulatory and audit requirements, start with [[enterprise/compliance-audit-and-monitoring|Compliance, Audit & Monitoring]].


## Section Directory {#section-directory}

- [[enterprise/audit-log|Audit Log]]
- [[enterprise/compliance-audit-and-monitoring|Compliance, Audit & Monitoring]]
- [[enterprise/enterprise-plugin-registry|Enterprise Plugin Registry]]
- [[enterprise/eu-deployment|EU Deployment]]
- [[enterprise/github-integration-security|GitHub Integration Security]]
- [[enterprise/hierarchical-settings-and-org-control|Hierarchical Settings & Org Control]]
- [[enterprise/identity-and-access|Identity & Access Management]]
- [[enterprise/identity-sso-and-scim|Identity, Domains, SSO, and SCIM]]
- [[enterprise/llm-safety-and-agent-controls|LLM Safety & Agent Controls]]
- [[enterprise/models-llm-gateways-and-integrations|Models, LLM Gateways & Integrations]]
- [[enterprise/network-and-deployment|Network & Deployment Configuration]]
- [[enterprise/privacy-and-data-flows|Privacy, Data Flows & Governance]]
- [[enterprise/security-review|Security Review]]
- [[enterprise/service-accounts|Service Accounts]]
- [[enterprise/telemetry-export|Telemetry Export (OTEL)]]
- [[enterprise/usage-cost-and-analytics|Usage, Cost & Productivity Analytics]]
