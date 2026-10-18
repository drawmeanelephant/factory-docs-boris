---
id: cli/byok/lm-studio
title: "LM Studio"
status: published
summary: "Run OpenAI-compatible local models with LM Studio"
parent: cli/byok/index
tags: [cli, lm-studio, local, byok, openai-compatible, offline, self-hosted]
relations: [relates_to=jp/cli/byok/lm-studio]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">LM Studio</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Run OpenAI-compatible local models with LM Studio</p>


Run models locally on your hardware with LM Studio's OpenAI-compatible local server.



<Aside kind="note">
**Performance Notice**: Models below 30 billion parameters have shown significantly lower performance on agentic coding tasks. While smaller models can be useful for experimentation and learning, they are generally not recommended for production coding work or complex software engineering tasks.
</Aside>



## Configuration {#configuration}

Add to `~/.factory/settings.json`:

```json
{
  "customModels": [
    {
      "model": "google/gemma-4-e4b",
      "displayName": "Gemma 4 E4B [LM Studio]",
      "baseUrl": "http://localhost:1234/v1",
      "apiKey": "not-needed",
      "provider": "openai",
      "maxOutputTokens": 16000
    }
  ]
}
```

Replace `model` with the exact model identifier shown by your LM Studio local server.

## Setup {#setup}



<Aside kind="warning">
**Context Window Configuration**: For optimal performance with Factory, configure the model context window to at least 32,000 tokens in LM Studio before starting the server. Without adequate context, the experience will be significantly degraded.
</Aside>



1. Install LM Studio from [lmstudio.ai](https://lmstudio.ai)
2. Download a coding model, such as Qwen Coder or another OpenAI-compatible chat model
3. Open the **Developer** tab in LM Studio
4. Load your model and start the local server
5. Confirm the server is running at `http://localhost:1234/v1`
6. Add the configuration above to Factory config

## Finding Your Model ID {#finding-your-model-id}

LM Studio exposes loaded models through its OpenAI-compatible API:

```bash
curl http://localhost:1234/v1/models
```

Use the returned `id` value as the `model` in your Factory configuration.

## Troubleshooting {#troubleshooting}

### Local server not connecting {#local-server-not-connecting}
- Ensure the LM Studio local server is running from the Developer tab
- Check that the server port matches your `baseUrl`, usually `1234`
- Try `curl http://localhost:1234/v1/models` to test connectivity

### Model not found {#model-not-found}
- Load the model in LM Studio before using it from Factory
- Confirm the exact model ID with `curl http://localhost:1234/v1/models`

## Notes {#notes}

- LM Studio's local API does not require authentication, so use any placeholder value for `apiKey`
- Base URL format: `http://localhost:1234/v1`
- Use the `openai` provider with LM Studio's OpenAI-compatible endpoints
