---
id: jp/cli/byok/baseten
title: "Baseten"
status: published
summary: "エンタープライズグレードのインフラでカスタムモデルをデプロイして提供する"
parent: jp/cli/byok/index
tags: [cli, baseten, api-key, byok, enterprise, deploy, custom-model, ml-serving]
relations: [relates_to=cli/byok/baseten]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Baseten</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">エンタープライズグレードのインフラでカスタムモデルをデプロイして提供する</p>


Baseten の ML モデル配信用エンタープライズグレードインフラストラクチャを使用して、カスタムモデルをデプロイして提供します。

## 設定 {#configuration}

`~/.factory/settings.json` に追加します:

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

## はじめに {#getting-started}

1. [baseten.co](https://baseten.co) でサインアップします
2. モデルライブラリからモデルをデプロイするか、独自のモデルをアップロードします
3. 設定ページから API キーを取得します
4. デプロイメントダッシュボードでモデル ID を確認します
5. Factory 設定に設定を追加します

## 注意事項 {#notes}

- ベース URL 形式: `https://inference.baseten.co/v1`
- `YOUR_MODEL_ID` を Baseten ダッシュボードからデプロイされたモデルの ID に置き換えてください
- OpenAI 互換 API 形式をサポートしています
- エンタープライズ機能とカスタムデプロイメントについては Baseten にお問い合わせください
