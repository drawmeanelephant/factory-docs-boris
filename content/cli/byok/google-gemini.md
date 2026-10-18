---
id: cli/byok/google-gemini
title: "Google Gemini"
status: published
summary: "Access Google's Gemini models using your Gemini AI API key"
parent: cli/byok/index
tags: [cli, google, gemini, api-key, byok, custom-model, multimodal]
relations: [relates_to=jp/cli/byok/google-gemini]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Google Gemini</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Access Google&#x27;s Gemini models using your Gemini AI API key</p>


Connect to Google's Gemini models for advanced AI capabilities with multimodal support.

## Configuration {#configuration}

Add to `~/.factory/settings.json`:

```json
{
  "customModels": [
    {
      "model": "gemini-2.5-pro",
      "displayName": "Gemini 2.5 Pro [Google]",
      "baseUrl": "https://generativelanguage.googleapis.com/v1beta/",
      "apiKey": "YOUR_GEMINI_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 32000
    },
    {
      "model": "gemini-1.5-pro",
      "displayName": "Gemini 1.5 Pro [Google]",
      "baseUrl": "https://generativelanguage.googleapis.com/v1beta/",
      "apiKey": "YOUR_GEMINI_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 1048576
    },
    {
      "model": "gemini-1.5-flash",
      "displayName": "Gemini 1.5 Flash [Google]",
      "baseUrl": "https://generativelanguage.googleapis.com/v1beta/",
      "apiKey": "YOUR_GEMINI_API_KEY",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 1048576
    }
  ]
}
```

## Getting Started {#getting-started}

1. Go to [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key
4. Add it to your Factory configuration

## Notes {#notes}

- Base URL uses the `v1beta` API version
- Gemini models use the `generic-chat-completion-api` provider type
