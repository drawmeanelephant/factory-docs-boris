---
id: enterprise/network-and-deployment
title: "Network & Deployment Configuration"
status: published
summary: "Reference architectures and network requirements for cloud, hybrid, and fully airgapped Droid deployments."
parent: enterprise/index
tags: [enterprise]
relations: [relates_to=jp/enterprise/network-and-deployment]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Network &amp; Deployment Configuration</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Reference architectures and network requirements for cloud, hybrid, and fully airgapped Droid deployments.</p>


Droids are designed to run anywhere: on laptops, in CI pipelines, on VMs and Kubernetes clusters, and in fully airgapped environments.

This page describes the **supported deployment patterns**, their **network requirements**, and how to combine Droid with proxies, custom CAs, mTLS, and sandboxed containers.

---

## Deployment patterns {#deployment-patterns}

Factory supports three canonical patterns. You can mix patterns across teams and environments.

### 1. Cloud‑managed deployment {#1-cloudmanaged-deployment}

In this pattern, Droid runs on developer machines and build infrastructure, while **Factory cloud** provides orchestration and optional analytics.



<div class="factory-card-group">

<div class="factory-card">

**Where Droid runs**

- Developer laptops and workstations
  - CI/CD runners (GitHub, GitLab, internal)
  - Optional devcontainers or remote development environments

</div>


  

<div class="factory-card">

**What lives in Factory cloud**

- Control plane and org metadata
  - Optional usage analytics dashboards
  - Authentication and access control for the web UI

</div>

</div>



LLM traffic can still be routed through **your own gateways and providers**; Factory does not need to broker model access.

Cloud‑managed deployments are ideal for organizations that allow well‑scoped cloud usage but want strong governance over models, keys, and telemetry.

### 2. Hybrid enterprise deployment {#2-hybrid-enterprise-deployment}

In hybrid deployments, Droid runs entirely within your infrastructure, while you may still use Factory cloud selectively for user experience and coordination.

- Droid processes run on **your VMs, containers, CI runners, and remote dev environments**.
- LLM traffic goes through **your LLM gateways or cloud providers** under your accounts.
- OTEL telemetry is sent to **your collectors and observability stack**.
- Factory cloud may see limited metadata (for example, org and project identifiers) if you enable cloud features.

This pattern is common for large enterprises and critical infrastructure where **network segmentation** and **central governance** are mandatory.

### 3. Fully airgapped deployment {#3-fully-airgapped-deployment}

In fully airgapped deployments:

- Droid runs in an isolated network with **no outbound internet connectivity**.
- Models are served from **on‑prem or in‑network endpoints**.
- OTEL collectors and observability tooling are hosted entirely inside the airgap.
- Factory cloud is not reachable at runtime; any artifacts (binaries, configuration) are imported via offline processes.

This is the default pattern for national security, defense, and other highly classified workloads.

---

## Network requirements {#network-requirements}

Network requirements vary per pattern.

### Cloud‑managed {#cloudmanaged}

In addition to your model providers and OTEL collector endpoints, Droid typically needs:

- Access to Factory cloud endpoints (for example, `*.factory.ai` and related domains).
- Outbound access to any configured LLM providers or LLM gateways.
- Outbound access to OTEL collectors if they are hosted outside the local network.

Your security team can tighten access by:

- Restricting outbound hosts to the minimum set of domains.
- Using HTTPS proxies and custom CAs as described below.
- Routing all LLM traffic through a central gateway and monitoring.

### Hybrid {#hybrid}

In hybrid mode, Droid generally needs only:

- Access to your **internal LLM gateways and model endpoints**.
- Access to your **internal OTEL collectors and SIEM/observability stack**.
- Optional, tightly scoped access to Factory cloud endpoints for specific features.

You can run Droid within private subnets, VPNs, and Kubernetes clusters, inheriting all existing firewall and network controls.

### Fully airgapped {#fully-airgapped}

In fully airgapped environments:

- Droid traffic is entirely **contained inside your network**.
- No external domains are required at runtime.
- Updates to Droid and configuration bundles are handled through your own artifact repositories or offline processes.

---

## Proxies, custom CAs, and mTLS {#proxies-custom-cas-and-mtls}

Enterprise networks frequently require HTTP(S) proxies, organization‑specific certificate authorities, and mutual TLS.

### HTTP(S) proxy support {#https-proxy-support}

Droid respects standard proxy environment variables:

```bash
export HTTPS_PROXY="https://proxy.example.com:8080"
export HTTP_PROXY="http://proxy.example.com:8080"

# Bypass proxy for specific hosts
export NO_PROXY="localhost,127.0.0.1,internal.example.com,.corp.example.com"
```

Use these to route traffic from Droid to LLM gateways and any Factory cloud endpoints through your corporate proxy.

### Custom certificate authorities {#custom-certificate-authorities}

If your organization uses custom CAs for HTTPS inspection or internal endpoints, configure the runtime environment so Droid trusts those CAs (for example, via `NODE_EXTRA_CA_CERTS` or OS‑level trust stores).

### Mutual TLS (mTLS) {#mutual-tls-mtls}

For environments that require client certificates when calling gateways or internal APIs, configure your containers, VMs, or runners with the appropriate certificate, key, and passphrase. These settings are usually handled at the HTTP client or proxy layer that Droid uses.

---

## Running in secure containers and VMs {#running-in-secure-containers-and-vms}

Running Droid inside hardened containers and VMs is one of the most effective ways to **bound the blast radius** of any agent mistakes or misconfigurations.

Recommended patterns include:

- **Devcontainers for untrusted code**
  - Use locked‑down devcontainers with restricted filesystem mounts and outbound network rules.
  - Run Droid with higher autonomy only inside these containers, never directly on the host.

- **Isolated VMs for sensitive operations**
  - Create dedicated VMs for production‑adjacent work (for example, migration tooling).
  - Use OS policies to restrict which repos, secrets, and networks those VMs can access.

- **CI/CD pipelines**
  - Run Droid in ephemeral CI jobs with short‑lived credentials and minimal privileges.
  - Combine with hooks and Droid Shield to prevent leaks and enforce approval workflows.

See [[enterprise/llm-safety-and-agent-controls|LLM Safety & Agent Controls]] for how autonomy, allow/deny lists, and Droid Shield interact with these environments.

---

## Configuration surfaces {#configuration-surfaces}

Network and deployment configuration is expressed through:

- **Environment variables** – proxies, gateways, OTEL endpoints, custom certificates.
- **Org and project `.factory/settings.json`** – hierarchical policies about where Droid may run, which models and gateways are allowed, and default telemetry destinations.
- **Org config endpoints** – for large organizations, a central configuration service can distribute a standard `.factory` bundle to all environments.
- **System-managed `settings.json`** – for MDM-deployed and airgapped fleets, drop a settings file at a hardcoded platform path so org policy is in effect before any user authenticates. See [[enterprise/hierarchical-settings-and-org-control#system-managed-settings-file|Hierarchical Settings & Org Control]].

For details on the hierarchy and merge behavior, see [[enterprise/hierarchical-settings-and-org-control|Hierarchical Settings & Org Control]].
