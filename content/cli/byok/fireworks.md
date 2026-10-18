---
id: cli/byok/fireworks
title: "Fireworks AI"
status: published
summary: "High-performance inference for open-source models with optimized serving"
parent: cli/byok/index
tags: [cli, fireworks, api-key, byok, inference, custom-model, high-performance]
relations: [relates_to=jp/cli/byok/fireworks]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Fireworks AI</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">High-performance inference for open-source models with optimized serving</p>


Access high-performance inference for open-source models with Fireworks AI's optimized serving infrastructure.

## Configuration {#configuration}

Add to `~/.factory/settings.json`:

```json
{
  "customModels": [
    {
      "model": "accounts/fireworks/models/glm-4p5",
      "displayName": "GLM 4.5 [Fireworks]",
      "baseUrl": "https://api.fireworks.ai/inference/v1",
      "apiKey": "YOUR_FIREWORKS_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    },
    {
      "model": "accounts/fireworks/models/deepseek-v3p1-terminus",
      "displayName": "Deepseek V3.1 Terminus [Fireworks]",
      "baseUrl": "https://api.fireworks.ai/inference/v1",
      "apiKey": "YOUR_FIREWORKS_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 20480
    }
  ]
}
```

## Getting Started {#getting-started}

1. Sign up at [fireworks.ai](https://fireworks.ai)
2. Get your API key from the dashboard
3. Browse available models in their [model catalog](https://fireworks.ai/models)
4. Add desired models to your configuration

## Notes {#notes}

- Base URL format: `https://api.fireworks.ai/inference/v1`
- Model IDs typically start with `accounts/fireworks/models/`
- Supports streaming responses and function calling for compatible models
