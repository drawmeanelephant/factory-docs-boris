---
id: jp/cli/byok/openrouter
title: "OpenRouter"
status: published
summary: "統一インターフェースから複数プロバイダーのモデルにアクセスする"
parent: jp/cli/byok/index
tags: [cli, openrouter, api-key, byok, multiple-providers, custom-model]
relations: [relates_to=cli/byok/openrouter]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">OpenRouter</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">統一インターフェースから複数プロバイダーのモデルにアクセスする</p>


単一のAPIインターフェースを通じて複数のプロバイダーのモデルにアクセスするため、OpenRouterに接続します。

## 設定 {#configuration}

`~/.factory/settings.json`に追加：

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

## はじめに {#getting-started}

1. [openrouter.ai](https://openrouter.ai)でサインアップ
2. ダッシュボードからAPIキーを取得
3. [openrouter.ai/models](https://openrouter.ai/models)で利用可能なモデルを閲覧
4. 希望するモデルを設定に追加

## 注意事項 {#notes}

- OpenRouterは`generic-chat-completion-api`プロバイダータイプを使用します
- 一部のモデルには使用制限があるか、追加の許可が必要な場合があります
