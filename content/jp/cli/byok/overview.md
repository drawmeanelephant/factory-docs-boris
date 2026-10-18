---
id: jp/cli/byok/overview
title: "独自キーの使用（BYOK）"
status: published
summary: "自分のAPIキーを接続し、オープンソースモデルを使用するか、ローカルモデルを実行する"
parent: jp/cli/byok/index
tags: [cli, byok, bring-your-own-key, own-api-key, api-key, custom-models, local-models, open-source]
relations: [relates_to=cli/byok/overview]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">独自キーの使用（BYOK）</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">自分のAPIキーを接続し、オープンソースモデルを使用するか、ローカルモデルを実行する</p>


Droid CLIは、BYOK（Bring Your Own Key）を通じてカスタムモデル設定をサポートしています。独自のOpenAIやAnthropicキーを使用し、任意のオープンソースモデルプロバイダーに接続するか、お使いのハードウェア上でローカルにモデルを実行できます。設定完了後は、`/model`コマンドを使用してモデル間を切り替えることができます。

Factory管理モデルと倍率については、[[jp/models|利用可能なモデル]]を参照してください。



<Aside kind="note">
APIキーはローカルに保持され、Factoryサーバーにはアップロードされません。カスタムモデルはCLIでのみ利用可能で、Factory Appやモバイルプラットフォームには表示されません。
</Aside>



<img src="../../../images/custom_models.png" alt="カスタムモデルを表示するモデルセレクター" />

[[jp/cli/getting-started/quickstart|5分クイックスタートでCLIをインストールする →]]

---

## 設定リファレンス {#configuration-reference}

`~/.factory/settings.json`の`customModels`配列にカスタムモデルを追加してください：

```json
{
  "customModels": [
    {
      "model": "your-model-id",
      "displayName": "My Custom Model",
      "baseUrl": "https://api.provider.com/v1",
      "apiKey": "${PROVIDER_API_KEY}",
      "provider": "generic-chat-completion-api",
      "maxOutputTokens": 16384
    }
  ]
}
```



<Aside kind="tip">
`settings.json`（および`settings.local.json`）では、`apiKey`が`${VAR_NAME}`構文による環境変数参照をサポートします。たとえば、`"apiKey": "${PROVIDER_API_KEY}"`は`PROVIDER_API_KEY`という名前の環境変数から読み込みます（例: `export PROVIDER_API_KEY=your_key_here`）。
</Aside>





<Aside kind="note">
**レガシーサポート**: 後方互換性のため、`~/.factory/config.json`内でsnake_caseフィールド名（`custom_models`、`base_url`など）を使うカスタムモデルは引き続きサポートされます。両方のファイルが読み込まれてマージされ、`settings.json`が優先されます。`apiKey`の環境変数展開は`settings.json`/`settings.local.json`に適用され、レガシーの`config.json`には適用されません。
</Aside>



### サポートされているフィールド {#supported-fields}

| フィールド | タイプ | 必須 | 説明 |
|-------|------|----------|-------------|
| `model` | `string` | ✓ | API経由で送信されるモデル識別子（例：`claude-sonnet-4-5-20250929`、`gpt-5-codex`、`qwen3:4b`） |
| `displayName` | `string` | | モデルセレクターに表示される人間が読みやすい名前 |
| `baseUrl` | `string` | ✓ | APIエンドポイントのベースURL |
| `apiKey` | `string` | ✓ | プロバイダー用のAPIキー。空にはできません。`settings.json`/`settings.local.json`での`${VAR_NAME}`をサポートします（例：`${PROVIDER_API_KEY}`は`PROVIDER_API_KEY`環境変数を使用します）。 |
| `provider` | `string` | ✓ | 次のいずれか：`anthropic`、`openai`、または`generic-chat-completion-api` |
| `maxOutputTokens` | `number` | | モデルレスポンスの最大出力トークン数 |
| `noImageSupport` | `boolean` | | このモデルで画像入力を無効にするには`true`に設定 |
| `extraArgs` | `object` | | APIリクエストに含める追加のプロバイダー固有の引数 |
| `extraHeaders` | `object` | | リクエストと共に送信する追加のHTTPヘッダー |

### extraArgsの使用 {#using-extraargs}

temperatureやtop_pなどのプロバイダー固有のパラメータを渡します：

```json
{
  "customModels": [
    {
      "model": "your-model",
      "displayName": "Custom Model",
      "baseUrl": "https://your-provider.com/v1",
      "apiKey": "YOUR_API_KEY",
      "provider": "generic-chat-completion-api",
      "extraArgs": {
        "temperature": 0.7,
        "top_p": 0.9
      }
    }
  ]
}
```

### extraHeadersの使用 {#using-extraheaders}

APIリクエストにカスタムHTTPヘッダーを追加します：

```json
{
  "customModels": [
    {
      "model": "your-model",
      "displayName": "Custom Model",
      "baseUrl": "https://your-provider.com/v1",
      "apiKey": "YOUR_API_KEY",
      "provider": "generic-chat-completion-api",
      "extraHeaders": {
        "X-Custom-Header": "value",
        "Authorization": "Bearer YOUR_TOKEN"
      }
    }
  ]
}
```

---

## プロバイダーの理解 {#aws-bedrock}

FactoryはAPI互換性を決定する3つのプロバイダータイプをサポートしています：

| プロバイダー | API形式 | 使用目的 | ドキュメント |
|----------|------------|---------|---------------|
| `anthropic` | Anthropic Messages API (v1/messages) | 公式APIまたは互換プロキシ上のAnthropicモデル | [Anthropic Messages API](https://docs.claude.com/en/api/messages) |
| `openai` | OpenAI Responses API | 公式APIまたは互換プロキシ上のOpenAIモデル。GPT-5やGPT-5-Codexなどの最新モデルに必要。 | [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses) |
| `generic-chat-completion-api` | OpenAI Chat Completions API | OpenRouter、Fireworks、Together AI、Ollama、vLLM、およびほとんどのオープンソースプロバイダー | [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat) |



<Aside kind="warning">
Factoryは主要モデルでのDroidの性能を継続的に検証していますが、すべてのカスタムモデルがそのまま動作することは保証できません。公式API経由でアクセスするAnthropicおよびOpenAIモデルのみが完全にテストされ、ベンチマークされています。
</Aside>





<Aside kind="note">
**モデルサイズに関する考慮事項**: 300億パラメータ未満のモデルは、エージェント型コーディングタスクで大幅に低い性能を示しています。これらの小型モデルは実験や学習には役立ちますが、本番のコーディング作業や複雑なソフトウェアエンジニアリングタスクには一般的に推奨されません。
</Aside>



---

## プロンプトキャッシング {#bedrock-fields}

Droid CLIは利用可能な場合にプロンプトキャッシングを自動的に使用してAPIコストを削減します：

- **公式プロバイダー（`anthropic`、`openai`）**：Factoryは公式APIを通じてプロンプトキャッシングの使用を試みます。キャッシング動作は各プロバイダーの実装と要件に従います。
- **汎用プロバイダー（`generic-chat-completion-api`）**：プロンプトキャッシングサポートはプロバイダーによって異なり、保証されません。一部のプロバイダーはキャッシングをサポートする場合もあれば、そうでない場合もあります。

### プロンプトキャッシングの確認 {#environment-variable-interpolation}

カスタムモデルでプロンプトキャッシングが正しく動作しているかを確認するには：

1. カスタムモデルで会話を実行
2. Droid CLIで`/cost`コマンドを使用してコスト内訳を表示
3. 出力でキャッシュヒット率と節約額を確認

期待されるキャッシング節約が表示されない場合は、プロバイダーのプロンプトキャッシングサポートと要件についてのドキュメントを参照してください。

---

## クイックスタート {#region-resolution}

特定の設定例を表示するには、左ナビゲーションからプロバイダーを選択してください：

- **[[jp/cli/byok/baseten|Baseten]]** - カスタムモデルのデプロイと提供
- **[[jp/cli/byok/deepinfra|DeepInfra]]** - オープンソースモデル向けの費用対効果の高い推論
- **[[jp/cli/byok/fireworks|Fireworks AI]]** - オープンソースモデル向けの高性能推論
- **[[jp/cli/byok/google-gemini|Google Gemini]]** - GoogleのGeminiモデルへのアクセス
- **[[jp/cli/byok/groq|Groq]]** - GroqのLPU™ Inference Engineによる超高速推論
- **[[jp/cli/byok/huggingface|Hugging Face]]** - HF Inference API上のモデルへの接続
- **[[jp/cli/byok/ollama|Ollama]]** - ローカルまたはクラウドでのモデル実行
- **[[jp/cli/byok/openai-anthropic|OpenAI & Anthropic]]** - 公式モデル用の独自APIキーの使用
- **[[jp/cli/byok/openrouter|OpenRouter]]** - 単一インターフェース経由での複数プロバイダーへのアクセス

---

## カスタムモデルの使用 {#understanding-providers}

設定完了後、CLIでカスタムモデルにアクセスできます：

1. `/model`コマンドを使用
2. カスタムモデルはFactory提供モデルの下にある別の「カスタムモデル」セクションに表示されます
3. 任意のモデルを選択して使用開始

カスタムモデルは`displayName`で設定した名前で表示され、異なるプロバイダーと設定を簡単に識別できます。

---

## トラブルシューティング {#prompt-caching}

### セレクターにモデルが表示されない {#verifying-prompt-caching}
- `~/.factory/settings.json`（レガシー形式を使用している場合は`config.json`）でJSON構文を確認
- 設定変更はファイル監視により自動的に検出されます
- すべての必須フィールドが存在することを確認

### 「Invalid provider」エラー {#quick-start}
- プロバイダーは正確に`anthropic`、`openai`、または`generic-chat-completion-api`である必要があります
- タイプミスを確認し、適切な大文字小文字を確保

### 認証エラー {#using-custom-models}
- APIキーが有効で利用可能なクレジットがあることを確認
- APIキーに適切な権限があることを確認
- ベースURLがプロバイダーのドキュメントと一致することを確認

### ローカルモデルが接続できない {#troubleshooting}
- ローカルサーバーが実行中であることを確認（例：`ollama serve`）
- ベースURLが正しく、必要に応じて`/v1/`サフィックスが含まれていることを確認
- モデルがローカルでプルされ/利用可能であることを確認

### レート制限またはクォータエラー {#model-not-appearing-in-selector}
- プロバイダーのレート制限と使用クォータを確認
- プロバイダーのダッシュボードで使用量を監視

---

## 請求 {#invalid-provider-error}

- Factory のマークアップや使用料なしで、プロバイダーに直接お支払いいただきます
- プロバイダーのダッシュボードでコストと使用量を追跡
