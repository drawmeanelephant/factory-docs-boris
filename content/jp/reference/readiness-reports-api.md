---
id: jp/reference/readiness-reports-api
title: "準備状況レポートAPI"
status: published
summary: "エージェント準備状況レポートへプログラムからアクセスするためのREST APIリファレンス。"
parent: jp/reference/index
tags: [reference]
relations: [relates_to=reference/readiness-reports-api]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">準備状況レポートAPI</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">エージェント準備状況レポートへプログラムからアクセスするためのREST APIリファレンス。</p>


準備状況レポートAPIは、組織のエージェント準備状況評価データへプログラムからアクセスする手段を提供します。

---

## 認証 {#authentication}

すべてのリクエストには`Authorization`ヘッダーにFactory APIキーが必要です：

```bash
Authorization: Bearer fk-your-api-key
```

APIキーは[app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys)で生成してください。

---

## ベースURL {#base-url}

```
https://app.factory.ai
```

---

## エンドポイント {#endpoints}

### 準備状況レポートの一覧取得 {#list-readiness-reports}

組織の準備状況レポートを取得します。

```
GET /api/organization/agent-readiness-reports
```

#### クエリパラメータ {#query-parameters}

| パラメータ    | 型    | 必須 | 説明                                            |
| :----------- | :------ | :------- | :----------------------------------------------------- |
| `repoId`     | string  | いいえ       | リポジトリIDでレポートをフィルタ                        |
| `limit`      | integer | いいえ       | 返すレポートの最大数（正の値である必要があります） |
| `startAfter` | string  | いいえ       | ページネーションカーソル用のレポートID                        |

#### レスポンス {#response}

```json
{
  "reports": [
    {
      "reportId": "550e8400-e29b-41d4-a716-446655440000",
      "createdAt": 1701792000000,
      "repoUrl": "https://github.com/org/repo",
      "apps": {
        "apps/web": {
          "description": "メインのNext.jsアプリケーション"
        },
        "apps/api": {
          "description": "バックエンドAPIサービス"
        }
      },
      "report": {
        "lint_config": {
          "numerator": 2,
          "denominator": 2,
          "rationale": "両方のアプリケーションでESLintが設定済み"
        },
        "type_check": {
          "numerator": 2,
          "denominator": 2,
          "rationale": "TypeScriptのstrictモードが有効"
        }
      },
      "commitHash": "abc123def456",
      "branch": "main",
      "hasLocalChanges": false,
      "hasNonRemoteCommits": false,
      "modelUsed": {
        "id": "claude-sonnet-4-5",
        "reasoningEffort": "high"
      },
      "droidVersion": "0.30.0"
    }
  ]
}
```

#### リクエスト例 {#example-request}

```bash
curl -X GET "https://app.factory.ai/api/organization/agent-readiness-reports?limit=10" \
  -H "Authorization: Bearer fk-your-api-key"
```

---

## 準備状況レポートスキーマ {#readiness-report-schema}

### レポートオブジェクト {#report-object}

| フィールド                 | 型     | 説明                                                |
| :-------------------- | :------- | :--------------------------------------------------------- |
| `reportId`            | string   | レポートの一意識別子（UUID）                    |
| `createdAt`           | number   | レポートが作成されたUnixタイムスタンプ（ミリ秒） |
| `repoUrl`             | string   | 評価されたリポジトリURL                          |
| `apps`                | object   | アプリケーションパスから説明オブジェクトへのマップ            |
| `report`              | object   | 基準IDから評価結果へのマップ                 |
| `commitHash`          | string?  | 評価時のGitコミットハッシュ                      |
| `branch`              | string?  | 評価時のGitブランチ名                      |
| `hasLocalChanges`     | boolean? | コミットされていない変更が存在したかどうか                        |
| `hasNonRemoteCommits` | boolean? | プッシュされていないコミットが存在したかどうか                           |
| `modelUsed`           | object?  | 評価に使用されたモデル設定                    |
| `droidVersion`        | string?  | レポートを生成したCLIバージョン                      |

### アプリ説明オブジェクト {#app-description-object}

| フィールド         | 型   | 説明                                    |
| :------------ | :----- | :--------------------------------------------- |
| `description` | string | アプリケーションの機能に関する簡潔な説明 |

### 基準評価オブジェクト {#criterion-evaluation-object}

| フィールド         | 型   | 説明                                                                 |
| :------------ | :----- | :-------------------------------------------------------------------------- |
| `numerator`   | number | 基準を満たしたサブアプリケーションの数（0からdenominatorまで）         |
| `denominator` | number | 基準が評価されたサブアプリケーションの数（最低1） |
| `rationale`   | string | 評価結果の説明                                        |

### 使用モデルオブジェクト {#model-used-object}

| フィールド             | 型   | 説明                                             |
| :---------------- | :----- | :------------------------------------------------------ |
| `id`              | string | モデル識別子                                        |
| `reasoningEffort` | string | 推論労力レベル（`low`、`medium`、`high`、`off`） |

---

## ページネーション {#pagination}

大きな結果セットに対しては、カーソルベースのページネーションを使用してください：

1. 希望する`limit`で初回リクエストを実行
2. レスポンスの最後のアイテムの`reportId`を取得
3. そのIDを次のリクエストで`startAfter`として渡す

```bash
# 最初のページ
curl "https://app.factory.ai/api/organization/agent-readiness-reports?limit=10"

# 次のページ（前回レスポンスの最後のreportIdを使用）
curl "https://app.factory.ai/api/organization/agent-readiness-reports?limit=10&startAfter=550e8400-e29b-41d4-a716-446655440000"
```

---

## 使用例 {#use-cases}

### CI/CD統合 {#cicd-integration}

各評価後にレポートを取得することで、時系列での準備状況スコアを追跡：

```bash
# 特定リポジトリの最新レポートを取得
curl "https://app.factory.ai/api/organization/agent-readiness-reports?repoId=123&limit=1" \
  -H "Authorization: Bearer $FACTORY_API_KEY"
```

### カスタムダッシュボード {#custom-dashboards}

すべてのレポートを取得し、集約メトリクスを計算することで内部ダッシュボードを構築：

```javascript
const response = await fetch(
  "https://app.factory.ai/api/organization/agent-readiness-reports",
  { headers: { Authorization: `Bearer ${apiKey}` } }
);
const { reports } = await response.json();

// 平均レベルを計算
const avgLevel =
  reports.reduce((sum, r) => sum + calculateLevel(r), 0) / reports.length;
```

### 自動アラート {#automated-alerting}

準備状況スコアが閾値を下回った際のアラートを設定：

```bash
# 最近のレポートを取得し、後退がないか確認
reports=$(curl -s "https://app.factory.ai/api/organization/agent-readiness-reports?limit=50" \
  -H "Authorization: Bearer $FACTORY_API_KEY")

# 後退を処理し、アラートを送信...
```

---

## エラーレスポンス {#error-responses}

| ステータス | 説明                |
| :----- | :------------------------- |
| `400`  | 無効なリクエストパラメータ |
| `401`  | APIキーが欠如または無効 |
| `500`  | 内部サーバーエラー      |
