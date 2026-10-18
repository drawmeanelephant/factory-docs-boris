---
id: cli/byok/openai-anthropic
title: "OpenAI & Anthropic"
status: published
summary: "Use your own API keys for official OpenAI and Anthropic models"
parent: cli/byok/index
tags: [cli, openai, anthropic, api-key, byok, gpt, claude, custom-model]
relations: [relates_to=jp/cli/byok/openai-anthropic]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">OpenAI &amp; Anthropic</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Use your own API keys for official OpenAI and Anthropic models</p>


Use your own API keys for cost control and billing transparency with official OpenAI and Anthropic models.

## Configuration {#configuration}

Add to `~/.factory/settings.json`:

```json
{
  "customModels": [
    {
      "model": "claude-sonnet-4-5-20250929",
      "displayName": "Sonnet 4.5 [Custom]",
      "baseUrl": "https://api.anthropic.com",
      "apiKey": "YOUR_ANTHROPIC_KEY",
      "provider": "anthropic",
      "maxOutputTokens": 8192
    },
    {
      "model": "gpt-5-codex",
      "displayName": "GPT5-Codex [Custom]",
      "baseUrl": "https://api.openai.com/v1",
      "apiKey": "YOUR_OPENAI_KEY",
      "provider": "openai",
      "maxOutputTokens": 16384
    }
  ]
}
```

## Getting API Keys {#getting-api-keys}

### Anthropic {#anthropic}
1. Sign up at [console.anthropic.com](https://console.anthropic.com)
2. Navigate to API Keys section
3. Create a new API key
4. Copy and use in your configuration

### OpenAI {#openai}
1. Sign up at [platform.openai.com](https://platform.openai.com)
2. Go to API Keys section
3. Create a new secret key
4. Copy and use in your configuration

## Notes {#notes}

- These configurations use the official APIs with full prompt caching support
- Factory automatically handles prompt caching when available
- Use `/cost` command in CLI to view cost breakdowns and cache hit rates
