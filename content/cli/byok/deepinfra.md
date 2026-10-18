---
id: cli/byok/deepinfra
title: "DeepInfra"
status: published
summary: "Cost-effective inference for a wide variety of open-source models"
parent: cli/byok/index
tags: [cli, deepinfra, api-key, byok, open-source, inference, custom-model]
relations: [relates_to=jp/cli/byok/deepinfra]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">DeepInfra</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Cost-effective inference for a wide variety of open-source models</p>


Access cost-effective inference for a wide variety of open-source models with DeepInfra's optimized infrastructure.

## Configuration {#configuration}

Add to `~/.factory/settings.json`:

```json
{
  "customModels": [
    {
      "model": "zai-org/GLM-4.7",
      "displayName": "GLM-4.7 [DeepInfra]",
      "baseUrl": "https://api.deepinfra.com/v1/openai",
      "apiKey": "YOUR_DEEPINFRA_TOKEN",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    },
    {
      "model": "deepseek-ai/DeepSeek-V3.1-Terminus",
      "displayName": "DeepSeek V3.1 Terminus [DeepInfra]",
      "baseUrl": "https://api.deepinfra.com/v1/openai",
      "apiKey": "YOUR_DEEPINFRA_TOKEN",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    },
    {
      "model": "moonshotai/Kimi-K2-Instruct-0905",
      "displayName": "Kimi K2 Instruct [DeepInfra]",
      "baseUrl": "https://api.deepinfra.com/v1/openai",
      "apiKey": "YOUR_DEEPINFRA_TOKEN",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 32768
    },
    {
      "model": "Qwen/Qwen3-Coder-480B-A35B-Instruct-Turbo",
      "displayName": "Qwen3 Coder 480B [DeepInfra]",
      "baseUrl": "https://api.deepinfra.com/v1/openai",
      "apiKey": "YOUR_DEEPINFRA_TOKEN",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 32768
    }
  ]
}
```

## Getting Started {#getting-started}

1. Sign up at [deepinfra.com](https://deepinfra.com)
2. Get your API token from the dashboard
3. View available models at their [model list](https://deepinfra.com/models)
4. Add desired models to your configuration

## Notes {#notes}

- Base URL format: `https://api.deepinfra.com/v1/openai`
- Model names match Hugging Face repository format
- Supports OpenAI-compatible API
- Automatic model updates when new versions are released
