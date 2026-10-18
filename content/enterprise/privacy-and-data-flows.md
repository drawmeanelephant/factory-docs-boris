---
id: enterprise/privacy-and-data-flows
title: "Privacy, Data Flows & Governance"
status: published
summary: "How code, prompts, and telemetry move in cloud, hybrid, and fully airgapped Droid deployments, and how to control those flows."
parent: enterprise/index
tags: [enterprise]
relations: [relates_to=jp/enterprise/privacy-and-data-flows]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Privacy, Data Flows &amp; Governance</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">How code, prompts, and telemetry move in cloud, hybrid, and fully airgapped Droid deployments, and how to control those flows.</p>


High‑security organizations need precise answers to **what data goes where, when, and under whose control**.

Factory’s answer is simple: **data boundaries are determined by the models, gateways, and deployment pattern you choose**, and Droid is configurable to respect those boundaries.

---

## Overview: three main data flows {#overview-three-main-data-flows}

When you run Droid, there are three primary ways data can move:

1. **Code and files** – local reads and writes on your filesystem and git repositories.
2. **LLM traffic** – prompts and context sent to model providers or LLM gateways.
3. **Telemetry** – metrics, traces, and logs emitted via OpenTelemetry.

How far each flow travels depends on whether you are in a **cloud‑managed**, **hybrid**, or **fully airgapped** deployment.



<div class="factory-card-group">

<div class="factory-card">

**Cloud‑managed**

Droid runs on laptops and CI, talking to Factory’s cloud for orchestration
and (optionally) analytics. LLM requests go to your chosen model providers
or LLM gateways.

</div>


  

<div class="factory-card">

**Hybrid**

Droid runs entirely inside your infra. LLM and OTEL traffic terminate in
your network; Factory cloud may only see minimal metadata if you enable it.

</div>


  

<div class="factory-card">

**Fully airgapped**

Droid, models, and collectors all live inside an isolated network. No
runtime dependency on Factory cloud; **no traffic leaves the environment**.

</div>

</div>



---

## Code and file access {#code-and-file-access}

Droid is a filesystem‑native agent:

- It reads your code, configuration, and test files **directly from the local filesystem** at the moment they’re needed.
- It uses LLMs to analyze existing code and generate new code, then applies patches on disk, with git as the source of truth where available.
- It does **not** upload or index your codebase into a remote datastore; there is no static or “cold” copy of your repository stored in Factory cloud.

In all deployment patterns:

- The **agent loop and runtime execute entirely on the machine** where Droid runs (developer workstation, CI runner, VM, or container).
- File contents can be included in LLM requests as context, so the data path for code always follows the same LLM request pipeline described below.
- **File reads and writes remain local** to that environment; only the portions you choose to include in prompts leave the machine, and only to the model endpoints you configure.
- Hooks and Droid Shield run locally inside that agent loop. By default they behave like local SAST / policy checks; they only send data off the machine if you explicitly configure a hook to call an external service.

You control which files and directories Droid can see through standard OS permissions and your repository layout. See [[enterprise/llm-safety-and-agent-controls|LLM Safety & Agent Controls]] for additional file‑level protections.

---

## LLM requests and model‑specific guarantees {#llm-requests-and-modelspecific-guarantees}

When Droid needs model output, it sends prompts and context to **your configured models and LLM gateways**.

By default, Droid can target **enterprise‑grade endpoints** for providers like Azure OpenAI, AWS Bedrock, Google Vertex AI, OpenAI, Anthropic, and Gemini, using contracts that support zero data retention and enterprise privacy controls. In these configurations, Factory routes traffic **directly** to the provider’s official APIs; we do not proxy this traffic through third‑party services or store prompts and responses in Factory cloud.

If you instead configure your own endpoints—LLM gateways, self‑hosted models, or generic HTTP APIs—the privacy guarantees are entirely determined by those systems and your agreements with them; Factory does not add additional protections on top.

### Model and gateway options {#model-and-gateway-options}

- **Cloud model providers** – OpenAI, Anthropic, Google, and others via their enterprise offerings.
- **Cloud AI platforms** – AWS Bedrock, GCP Vertex, Azure OpenAI, using your cloud accounts.
- **On‑prem / self‑hosted models** – models served inside your network or airgapped environment via HTTP/gRPC gateways.
- **LLM gateways** – central gateways that normalize traffic, add authentication, enforce rate limits, and log usage.

### How Droid interacts with models {#how-droid-interacts-with-models}

- Org and project policies decide **which models and gateways are allowed**, and whether users can bring their own keys.
- In high‑security settings, orgs commonly:
  - Prefer direct enterprise endpoints (for example, Azure OpenAI, AWS Bedrock, Google Vertex AI, OpenAI Enterprise, Anthropic/Claude Enterprise, Gemini Enterprise) to get first‑party zero‑retention guarantees.
  - Disable ad‑hoc user‑supplied keys and generic internet endpoints.
  - Treat any LLM gateways or self‑hosted models as in‑scope security systems, subject to the same reviews and monitoring as other critical services.

See [[enterprise/models-llm-gateways-and-integrations|Models, LLM Gateways & Integrations]] for configuration details.

---

## Telemetry and analytics {#telemetry-and-analytics}

Telemetry is how you understand _what_ Droid is doing and _where_. Factory treats OpenTelemetry as the primary interface for this.

### OTEL as the source of truth {#otel-as-the-source-of-truth}

- Droid emits **OTLP signals** (metrics, traces, logs) to the endpoints you configure via environment variables or `.factory` settings.
- Typical destinations include OTEL collectors feeding **Prometheus, Datadog, New Relic, Splunk, Loki, Jaeger, Tempo**, and similar systems.
- High‑security customers commonly deploy OTEL collectors **inside their own networks** and never send telemetry to Factory.

### Optional Factory cloud analytics {#optional-factory-cloud-analytics}

In cloud‑managed deployments, you can opt into Factory’s own analytics dashboards, which may:

- Aggregate anonymized usage metrics to show adoption, model usage, and cost trends.
- Surface per‑org and per‑team insights for platform and leadership teams.

These analytics are optional; org administrators decide whether to enable them.

For more on signals and schema, see [[enterprise/usage-cost-and-analytics|Usage, Cost & Productivity Analytics]] and [[enterprise/compliance-audit-and-monitoring|Compliance, Audit & Monitoring]].

---

## Data retention and residency {#data-retention-and-residency}

### Factory‑hosted components {#factoryhosted-components}

In cloud‑managed mode, Factory may store limited operational logs and metrics for:

- Authentication and administrative actions (for example, org configuration changes).
- Service health and debugging.

Retention and residency for these logs are documented in the [Trust Center](https://trust.factory.ai) and can be tuned per customer engagement.

### Customer‑hosted components {#customerhosted-components}

For hybrid and airgapped deployments:

- **LLM traffic** is handled entirely by your providers and gateways; Factory does not see it.
- **Telemetry** is stored in your observability stack; retention is governed by your own policies.
- **Code, configuration, and secrets** never leave your environment unless you explicitly send them to external services via hooks or gateways.

In fully airgapped environments, Factory never receives any runtime data; you are responsible for all retention and residency decisions.

---

## Governance controls in practice {#governance-controls-in-practice}

To make these guarantees enforceable rather than aspirational, Factory exposes **governance levers** at the org and project levels:

- Model and gateway allow/deny lists.
- Policies for whether user‑supplied BYOK keys are allowed.
- Global and project‑specific hooks for DLP, redaction, and approval workflows.
- OTEL endpoint configuration (including requiring on‑prem collectors).
- Maximum autonomy level and other safety controls, especially in less‑trusted environments.

These levers are implemented through the **hierarchical settings** system described in [[enterprise/hierarchical-settings-and-org-control|Hierarchical Settings & Org Control]].
