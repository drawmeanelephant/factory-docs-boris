---
id: jp/enterprise/telemetry-export
title: "テレメトリエクスポート（OTEL）"
status: published
summary: "Droidから独自のOTLP互換コレクターへOpenTelemetryメトリクスをエクスポートし、既存のオブザーバビリティスタックで完全に可視化する。"
parent: jp/enterprise/index
tags: [enterprise]
relations: [relates_to=enterprise/telemetry-export]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">テレメトリエクスポート（OTEL）</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Droidから独自のOTLP互換コレクターへOpenTelemetryメトリクスをエクスポートし、既存のオブザーバビリティスタックで完全に可視化する。</p>


Droidは、OpenTelemetry (OTEL) メトリクスをお客様のOTLP対応コレクターにエクスポートすることができ、既存の可観測性スタック内でDroidアクティビティの完全な可視性を提供します。メトリクスは同じエクスポートサイクルでFactoryのコレクターとお客様のコレクター両方に送信されます。お客様のコレクターにアクセスできない場合でも、Factoryのエクスポートは影響を受けません。

---

## 設定 {#configuration}

Droidを起動する前に、以下の環境変数を設定してください：

```bash
export OTEL_TELEMETRY_ENDPOINT="https://your-collector.example.com:4318"
export OTEL_TELEMETRY_HEADERS="Authorization=Bearer <your-token>"
```

| Variable                  | 必須 | Description                                                                                                          |
| :------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------- |
| `OTEL_TELEMETRY_ENDPOINT` | Yes      | OTLP HTTPコレクターのベースURL。メトリクスは`{endpoint}/v1/metrics`に送信されます。                                   |
| `OTEL_TELEMETRY_HEADERS`  | No       | すべてのエクスポートでHTTPヘッダーとして送信されるカンマ区切りの`key=value`ペア。値には`=`を含めることができます（例：base64トークン）。 |

---

## 仕組み {#how-it-works}

- `OTEL_TELEMETRY_ENDPOINT`が設定されている場合、メトリクスはファンアウトエクスポーターを介して同じエクスポートサイクルでお客様のエンドポイントに送信されます。追加のタイマーやメトリクスリーダーの重複はありません。
- お客様のコレクターへの障害は、Factoryの独自エクスポートに影響しません。各エンドポイントは分離されています。
- メトリクスは**デルタテンポラリティ**を使用します。各エクスポートには、最後のフラッシュ以降の新しい値のみが含まれます（60秒間隔）。

---

## エクスポートされるメトリクス {#exported-metrics}

すべてのメトリクスは`droid.*`名前空間を使用します。

| Metric                            | Type      | Description                        |
| :-------------------------------- | :-------- | :--------------------------------- |
| `droid.code.files_modified`       | Counter   | セッション中に変更されたファイル数    |
| `droid.code.files_read`           | Counter   | セッション中に読み取られたファイル数        |
| `droid.code.lines_modified`       | Counter   | 変更されたコード行数             |
| `droid.git.commits`               | Counter   | 作成されたコミット数                    |
| `droid.git.pull_requests`         | Counter   | 作成されたプルリクエスト数              |
| `droid.tool.invocations`          | Counter   | ツール呼び出し数                   |
| `droid.tool.execution_time`       | Histogram | ツール実行時間（ミリ秒）       |
| `droid.mcp.tool_invocations`      | Counter   | MCPツール呼び出し数               |
| `droid.skill.invocations`         | Counter   | スキル呼び出し数                  |
| `droid.hook.invocations`          | Counter   | フック呼び出し数                   |
| `droid.slash_command.invocations` | Counter   | スラッシュコマンド呼び出し数          |
| `droid.auth.login_success`        | Counter   | ログイン成功数                  |
| `droid.repo.metadata`             | Gauge     | リポジトリメタデータスナップショット       |

---

## 共通属性 {#common-attributes}

すべてのデータポイントには、以下の属性が自動的に含まれます：

| Attribute         | Description              |
| :---------------- | :----------------------- |
| `user.id`         | 認証済みユーザーID    |
| `organization.id` | 組織ID          |
| `session.id`      | 現在のDroidセッションID |

ツール固有の属性（`tool.name`、`mcp.server`、`skill.name`など）は該当する場合に含まれます。リソース属性には`service.name`（`cli`）と`service.version`が含まれます。

---

## 設定例 {#message-content-logging}





<Details summary="Generic OTEL Collector / Grafana Alloy">
```bash
export OTEL_TELEMETRY_ENDPOINT="https://collector.example.com:4318"
```
</Details>



  

<Details summary="Datadog (via Agent OTLP ingestion)">
```bash
export OTEL_TELEMETRY_ENDPOINT="http://localhost:4318"
```
</Details>



  

<Details summary="Datadog (direct OTLP intake)">
```bash
export OTEL_TELEMETRY_ENDPOINT="https://otlp.datadoghq.com"
export OTEL_TELEMETRY_HEADERS="dd-api-key=<your-datadog-api-key>"
```
</Details>



  

<Details summary="New Relic">
```bash
export OTEL_TELEMETRY_ENDPOINT="https://otlp.nr-data.net:4318"
export OTEL_TELEMETRY_HEADERS="api-key=<your-new-relic-license-key>"
```
</Details>



  

<Details summary="Honeycomb">
```bash
export OTEL_TELEMETRY_ENDPOINT="https://api.honeycomb.io"
export OTEL_TELEMETRY_HEADERS="x-honeycomb-team=<your-api-key>,x-honeycomb-dataset=droid-metrics"
```
</Details>





---

## トラブルシューティング {#example-configurations}

- コレクターが`/v1/metrics`パスでOTLP HTTPを受け入れることを確認してください。
- `OTEL_TELEMETRY_HEADERS`に有効な認証クレデンシャルが含まれていることを確認してください。
- Droidを実行しているマシンからコレクターへのネットワーク接続を確保してください。
