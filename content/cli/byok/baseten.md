---
id: cli/byok/baseten
title: "Baseten"
status: published
summary: "Deploy and serve custom models with enterprise-grade infrastructure"
parent: cli/byok/index
tags: [cli, baseten, api-key, byok, enterprise, deploy, custom-model, ml-serving]
relations: [relates_to=jp/cli/byok/baseten]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Baseten</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Deploy and serve custom models with enterprise-grade infrastructure</p>


Deploy and serve custom models with Baseten's enterprise-grade infrastructure for ML model serving.

## Configuration {#configuration}

Add to `~/.factory/settings.json`:

```json
{
  "customModels": [
    {
      "model": "Qwen/Qwen3-Coder-480B-A35B-Instruct",
      "displayName": "Qwen3-Coder-480B [Baseten]",
      "baseUrl": "https://inference.baseten.co/v1",
      "apiKey": "YOUR_BASETEN_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 8192
    }
  ]
}
```

## Getting Started {#getting-started}

1. Sign up at [baseten.co](https://baseten.co)
2. Deploy a model from their model library or upload your own
3. Get your API key from the settings page
4. Find your model ID in the deployment dashboard
5. Add the configuration to your Factory config

## Notes {#notes}

- Base URL format: `https://inference.baseten.co/v1`
- Replace `YOUR_MODEL_ID` with your deployed model's ID from Baseten dashboard
- Supports OpenAI-compatible API format
- Contact Baseten for enterprise features and custom deployments
