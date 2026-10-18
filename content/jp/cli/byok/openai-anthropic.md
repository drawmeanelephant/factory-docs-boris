---
id: jp/cli/byok/openai-anthropic
title: "OpenAIとAnthropic"
status: published
summary: "公式OpenAIおよびAnthropicモデルに自分のAPIキーを使用する"
parent: jp/cli/byok/index
tags: [cli, openai, anthropic, api-key, byok, gpt, claude, custom-model]
relations: [relates_to=cli/byok/openai-anthropic]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">OpenAIとAnthropic</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">公式OpenAIおよびAnthropicモデルに自分のAPIキーを使用する</p>


コストコントロールと請求の透明性のために、公式のOpenAIとAnthropic モデルで独自のAPI キーを使用してください。

## 設定 {#configuration}

`~/.factory/settings.json`に追加してください：

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

## API キーの取得 {#getting-api-keys}

### Anthropic {#anthropic}
1. [console.anthropic.com](https://console.anthropic.com)でサインアップしてください
2. API Keys セクションに移動してください
3. 新しいAPI キーを作成してください
4. コピーして設定で使用してください

### OpenAI {#openai}
1. [platform.openai.com](https://platform.openai.com)でサインアップしてください
2. API Keys セクションに移動してください
3. 新しいシークレットキーを作成してください
4. コピーして設定で使用してください

## 注意事項 {#notes}

- これらの設定は、完全なプロンプトキャッシュサポートを持つ公式APIを使用します
- Factory は利用可能な場合、プロンプトキャッシュを自動的に処理します
- CLIで`/cost`コマンドを使用して、コストの内訳とキャッシュヒット率を確認してください
