---
id: cli/byok/openrouter
title: "OpenRouter"
status: published
summary: "Access models from multiple providers through a unified interface"
parent: cli/byok/index
tags: [cli, openrouter, api-key, byok, multiple-providers, custom-model]
relations: [relates_to=jp/cli/byok/openrouter]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">OpenRouter</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Access models from multiple providers through a unified interface</p>


Connect to OpenRouter for access to models from multiple providers through a single API interface.

## Configuration {#configuration}

Add to `~/.factory/settings.json`:

```json
{
  "customModels": [
    {
      "model": "openai/gpt-oss-20b",
      "displayName": "GPT-OSS-20B [OpenRouter]",
      "baseUrl": "https://openrouter.ai/api/v1",
      "apiKey": "YOUR_OPENROUTER_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 32000
    }
  ]
}
```

## Getting Started {#getting-started}

1. Sign up at [openrouter.ai](https://openrouter.ai)
2. Get your API key from the dashboard
3. Browse available models at [openrouter.ai/models](https://openrouter.ai/models)
4. Add desired models to your configuration

## Notes {#notes}

- OpenRouter uses the `generic-chat-completion-api` provider type
- Some models may have usage restrictions or require additional permissions
