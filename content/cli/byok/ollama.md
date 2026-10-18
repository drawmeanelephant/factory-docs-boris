---
id: cli/byok/ollama
title: "Ollama"
status: published
summary: "Run models locally on your hardware or use Ollama Cloud"
parent: cli/byok/index
tags: [cli, ollama, local, self-hosted, byok, llama, offline, on-premise]
relations: [relates_to=jp/cli/byok/ollama]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Ollama</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Run models locally on your hardware or use Ollama Cloud</p>


Run models locally on your hardware with Ollama, or use Ollama Cloud for hosted inference.



<Aside kind="note">
**Performance Notice**: Models below 30 billion parameters have shown significantly lower performance on agentic coding tasks. While smaller models (7B, 13B) can be useful for experimentation and learning, they are generally not recommended for production coding work or complex software engineering tasks.
</Aside>




## Local Ollama {#local-ollama}

Run models entirely on your machine with no internet required.

### Configuration {#configuration}

Add to `~/.factory/settings.json`:

```json
{
  "customModels": [
    {
      "model": "qwen2.5-coder:32b",
      "displayName": "Qwen 2.5 Coder 32B [Local]",
      "baseUrl": "http://localhost:11434/v1",
      "apiKey": "not-needed",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16000
    },
    {
      "model": "qwen2.5-coder:7b",
      "displayName": "Qwen 2.5 Coder 7B [Local]",
      "baseUrl": "http://localhost:11434/v1",
      "apiKey": "not-needed",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 4000
    }
  ]
}
```

### Setup {#setup}



<Aside kind="warning">
**Context Window Configuration**: For optimal performance with Factory, ensure you set the context window to at least 32,000 tokens. You can either:
  - Use the context window slider in the Ollama app (set to 32k minimum)
  - Set environment variable before starting: `OLLAMA_CONTEXT_LENGTH=32000 ollama serve`
  
  Without adequate context, the experience will be significantly degraded.
</Aside>



1. Install Ollama from [ollama.com/download](https://ollama.com/download)
2. Pull desired models:
   ```bash
   # Recommended models
   ollama pull qwen2.5-coder:32b
   ollama pull qwen2.5-coder:7b
   ```
3. Start the Ollama server with extra context:
   ```bash
   OLLAMA_CONTEXT_LENGTH=32000 ollama serve
   ```
4. Add configurations to Factory config


### Approximate Hardware Requirements {#approximate-hardware-requirements}

| Model Size | RAM Required | VRAM (GPU) |
|-----------|--------------|------------|
| 3B params | 4GB | 3GB |
| 7B params | 8GB | 6GB |
| 13B params | 16GB | 10GB |
| 30B params | 32GB | 20GB |
| 70B params | 64GB | 40GB |

## Ollama Cloud {#ollama-cloud}

Use Ollama's cloud service for hosted model inference without local hardware requirements

### Recommended Cloud Model {#recommended-cloud-model}

The best performance for agentic coding has been observed with **qwen3-coder:480b**. 

For a full list of available cloud models, visit: [ollama.com/search?c=cloud](https://ollama.com/search?c=cloud)

### Configuration {#configuration-2}

```json
{
  "customModels": [
    {
      "model": "qwen3-coder:480b-cloud",
      "displayName": "qwen3-coder [Online]",
      "baseUrl": "http://localhost:11434/v1/",
      "apiKey": "not-needed",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 128000
    }
  ]
}
```

### Getting Started with Cloud Models {#getting-started-with-cloud-models}

1. Ensure Ollama is installed and running locally
2. Cloud models are accessed through your local Ollama instance - no API key needed
3. Add the configuration above to your Factory config
4. The model will automatically use cloud compute when requested

## Troubleshooting {#troubleshooting}

### Local server not connecting {#local-server-not-connecting}
- Ensure Ollama is running: `ollama serve`
- Check if port 11434 is available
- Try `curl http://localhost:11434/api/tags` to test

### Model not found {#model-not-found}
- Pull the model first: `ollama pull model-name`
- Check exact model name with `ollama list`

## Notes {#notes}

- Local API doesn't require authentication (use any placeholder for `api_key`)
- Models are stored in `~/.ollama/models/`
