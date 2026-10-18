---
id: web/factory-router
title: "Factory Router"
status: published
summary: "Automatically select the best model for each task."
parent: web/index
tags: [web, auto-model-routing, factory-router, model-routing, models, enterprise-controls, cost-savings]
relations: [relates_to=jp/web/factory-router]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Factory Router</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Automatically select the best model for each task.</p>


Factory Router automatically chooses the best model for each Droid task. Instead of manually picking a single model for every session, Factory Router evaluates the task and routes work to the model that balances quality, latency, and cost.

Factory Router is available in the Factory CLI and App and works with the same enterprise controls as other models.

## Why use Factory Router? {#why-use-factory-router}

Factory Router is designed for teams that want strong results without manually changing model selection for every workflow.



<div class="factory-card-group">

<div class="factory-card">

**Best performance at lower cost**

In production, Factory Router delivers **43%** aggregate cost savings compared with pricing the same workload at top-tier model rates, while maintaining frontier-level performance in Factory evaluations.

</div>


  

<div class="factory-card">

**Improved model selection**

Droid can route routine steps to faster or lower-cost models and reserve stronger models for work that needs deeper reasoning.

</div>


  

<div class="factory-card">

**Enterprise-ready controls**

Factory Router respects the same org, project, and user-level model controls used across the Factory platform.

</div>

</div>




## Availability {#availability}

Factory Router is generally available in the Factory CLI and App model selector, with no setup required.

## Enterprise controls {#enterprise-controls}

Enterprise admins can manage Factory Router through the same model governance system used for other Factory-supported models, including allowing or restricting Factory Router at the organization level like any other model.

For more information on enterprise control of models, see [[enterprise/models-llm-gateways-and-integrations|Models, LLM Gateways & Integrations]].

## FAQ {#faq}

### How does model routing work? {#how-does-model-routing-work}

Factory Router is a per-task router that uses a mix of session and per-request routing. It strongly considers prompt cache maintenance and savings in its optimization.

### Can Factory Router be configured? {#can-factory-router-be-configured}

Factory Router can be enabled/disabled like any other model today. We also offer Enterprise Controls for Factory Router guidance.

### Are there benchmarks on Factory Router's performance? {#are-there-benchmarks-on-factory-routers-performance}

Yes. Factory Router maintains frontier-level performance on challenging benchmarks like Terminal Bench 2 and Legacy Bench, and provides the best balance of quality, latency, and cost.

### What are the cost benefits of Factory Router? {#what-are-the-cost-benefits-of-factory-router}

In production, measured as billed usage compared with the same workload priced at top-tier model rates, aggregate cost is 43% lower. The median session costs 81% less, and 61% of sessions are at least 80% cheaper. Factory Router maintains frontier-level performance throughout.
