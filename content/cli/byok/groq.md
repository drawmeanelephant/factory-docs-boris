---
id: cli/byok/groq
title: "Groq"
status: published
summary: "Ultra-fast inference with Groq's LPU™ Inference Engine"
parent: cli/byok/index
tags: [cli, groq, api-key, byok, fast-inference, lpu, custom-model]
relations: [relates_to=jp/cli/byok/groq]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Groq</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Ultra-fast inference with Groq&#x27;s LPU™ Inference Engine</p>


Access ultra-fast inference powered by Groq's LPU™ (Language Processing Unit) Inference Engine for various open-source models.

## Configuration {#configuration}

Add to `~/.factory/settings.json`:

```json
{
  "customModels": [
    {
      "model": "moonshotai/kimi-k2-instruct-0905",
      "displayName": "Kimi K2 [Groq]",
      "baseUrl": "https://api.groq.com/openai/v1",
      "apiKey": "YOUR_GROQ_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    }
  ]
}
```

## Getting Started {#getting-started}

1. Sign up at [groq.com](https://groq.com)
2. Get your API key from [console.groq.com](https://console.groq.com)
3. Browse available models in the [Groq documentation](https://console.groq.com/docs/overview.md)
4. Add desired models to your configuration

## Notes {#notes}

- Base URL format: `https://api.groq.com/openai/v1`
- Groq uses the `generic-chat-completion-api` provider type
- Known for extremely fast inference speeds thanks to LPU architecture
- Supports streaming responses for compatible models
