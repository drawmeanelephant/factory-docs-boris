---
id: jp/cli/byok/google-gemini
title: "Google Gemini"
status: published
summary: "Gemini AI APIキーを使用してGoogleのGeminiモデルにアクセスする"
parent: jp/cli/byok/index
tags: [cli, google, gemini, api-key, byok, custom-model, multimodal]
relations: [relates_to=cli/byok/google-gemini]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Google Gemini</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Gemini AI APIキーを使用してGoogleのGeminiモデルにアクセスする</p>


Googleの Gemini モデルに接続して、マルチモーダルサポート付きの高度なAI機能を利用できます。

## 設定 {#configuration}

`~/.factory/settings.json` に追加してください：

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

## はじめに {#getting-started}

1. [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey) にアクセスしてください
2. 「Create API Key」をクリックしてください
3. API キーをコピーしてください
4. Factory の設定に追加してください

## 注意事項 {#notes}

- Base URL は `v1beta` API バージョンを使用します
- Gemini モデルは `generic-chat-completion-api` プロバイダータイプを使用します
