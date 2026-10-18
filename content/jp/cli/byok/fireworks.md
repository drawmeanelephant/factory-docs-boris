---
id: jp/cli/byok/fireworks
title: "Fireworks AI"
status: published
summary: "最適化された提供基盤によるオープンソースモデル向け高性能推論"
parent: jp/cli/byok/index
tags: [cli, fireworks, api-key, byok, inference, custom-model, high-performance]
relations: [relates_to=cli/byok/fireworks]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Fireworks AI</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">最適化された提供基盤によるオープンソースモデル向け高性能推論</p>


Fireworks AIの最適化されたサービングインフラストラクチャを使用して、オープンソースモデルの高性能推論にアクセスできます。

## 設定 {#configuration}

`~/.factory/settings.json`に追加してください：

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

## はじめに {#getting-started}

1. [fireworks.ai](https://fireworks.ai)でサインアップしてください
2. ダッシュボードからAPI keyを取得してください
3. [model catalog](https://fireworks.ai/models)で利用可能なモデルを閲覧してください
4. 設定に希望するモデルを追加してください

## 注意事項 {#notes}

- ベースURLの形式：`https://api.fireworks.ai/inference/v1`
- モデルIDは通常`accounts/fireworks/models/`で始まります
- 対応モデルではストリーミングレスポンスとfunction callingをサポートしています
