---
id: jp/web/agent-readiness/dashboard
title: "準備状況ダッシュボード"
status: published
summary: "Factory Appで組織のAgent Readinessスコアを追跡・分析する。"
parent: jp/web/agent-readiness/index
tags: [web]
relations: [relates_to=web/agent-readiness/dashboard]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">準備状況ダッシュボード</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Factory Appで組織のAgent Readinessスコアを追跡・分析する。</p>


Agent Readinessダッシュボードは、組織のすべてのリポジトリにわたる準備状況スコアの一元化されたビューを提供し、履歴トレンドと詳細な内訳を表示します。

<img src="../../../images/web/readiness-dashboard.png" alt="Agent Readinessダッシュボード" />

---

## ダッシュボードへのアクセス {#accessing-the-dashboard}

Factory Appで**Settings → Analytics → Agent Readiness**に移動します。

---

## メインダッシュボードビュー {#main-dashboard-view}

ダッシュボードは、3つの主要セクションで構成された組織レベルの概要を表示します：

### サマリーカード {#summary-cards}

上部には、主要な指標が表示されます：

| 指標                      | 説明                                                                        |
| :----------------------- | :-------------------------------------------------------------------------- |
| **組織スコア**   | 測定対象の全リポジトリにおける平均準備レベル（切り下げ）                             |
| **Repositories Tracked** | 準備状況レポートのあるリポジトリ数 vs 有効化された総リポジトリ数                     |
| **Last Updated**         | 最新の準備状況評価からの経過時間                                                |

### 進捗グラフ {#progress-graph}

組織の準備レベルの時系列推移を示すグラフです。期間フィルターを使用して異なる時間範囲を表示できます：

- **7d** — 過去7日間
- **1m** — 過去1か月
- **6m** — 過去6か月
- **1y** — 過去1年
- **all** — 全期間

### リポジトリテーブル {#repositories-table}

検索・ページネーション機能付きの全リポジトリテーブルで、以下を表示します：

- **Repository name** — クリックして詳細を表示
- **Level** — 現在の準備レベル（1-5）
- **Progress** — 次のレベルまでの完了率
- **Last Update** — リポジトリが最後に評価された日時

検索バーを使用してリポジトリを名前またはURLでフィルタリングできます。

---

## リポジトリ詳細ページ {#repository-detail-page}

任意のリポジトリ行をクリックすると、詳細な準備状況の内訳が表示されます。

<img src="../../../images/web/readiness-criteria.png" alt="リポジトリ詳細ページ" />

### ヘッダー {#header}

リポジトリ名、現在達成しているレベル、最終評価時刻、および新しい評価をトリガーする**Refresh**ボタンが表示されます。

### レベルアコーディオン {#level-accordions}

各準備レベル（FunctionalからAutonomousまで）には展開可能なアコーディオンセクションがあり、以下が表示されます：

- **Percentage complete** — そのレベルの条件のうち合格している割合
- **Lock status** — 前のレベルが80%に達するまでレベルはロックされます

### 条件行 {#criterion-rows}

各レベル内で、個別の条件は以下を表示します：

| 要素          | 説明                                               |
| :------------ | :------------------------------------------------- |
| **Name**      | 評価される条件                                      |
| **Score**     | 形式`[X/Y]` — 分子/分母                      |
| **Status**    | 合格（緑）または不合格（赤）のインジケーター            |
| **Rationale** | クリックして展開し、評価の説明を確認                  |

### 修復（近日公開） {#remediation-coming-soon}

近日中に、不合格の条件には自動修復をトリガーする**Fix**ボタンが表示されます。修正したい条件を選択すると、システムがリポジトリに必要な変更を実装します。

---

## 更新のトリガー {#triggering-a-refresh}

準備状況評価を更新する方法は2つあります：

### Webダッシュボードから {#from-the-factory-app-dashboard}

1. リポジトリ詳細ページに移動
2. ヘッダーの**Refresh**ボタンをクリック
3. リポジトリを評価する新しいセッションが開始
4. 完了後、最新レポートの結果でダッシュボードが更新されます

### CLIから {#from-the-droid-cli}

リポジトリディレクトリ内でDroid CLIの`/readiness-report` [[jp/cli/features/readiness-report|slash command]]を実行します：

```bash
droid
> /readiness-report
```



<Aside kind="note">
再評価では、現在の状態に対して完全な準備状況評価を実行します
  リポジトリに対して実行されます。インフラ改善を行った後や、
  準備状況基準に影響する変更をマージした後に役立ちます。
</Aside>



---

## 指標の理解 {#understanding-the-metrics}

### 組織レベルの計算 {#organization-level-calculation}

組織レベルのスコアは、**全リポジトリレベルの平均を切り下げ**して計算されます。例：

- リポジトリA: レベル3
- リポジトリB: レベル2
- リポジトリC: レベル3

組織レベル = floor((3 + 2 + 3) / 3) = floor(2.67) = **Level 2**

### リポジトリレベルの計算 {#repository-level-calculation}

リポジトリのレベルは**80%閾値システム**によって決定されます：

1. Level 1から開始
2. Level 1の条件の80%が合格 → Level 2達成
3. Level 2の条件の80%が合格 → Level 3達成
4. Level 5まで継続

各レベルに表示される割合は、そのレベルの条件完了に向けた進捗を示しています。

---

## ベストプラクティス {#best-practices}

- **定期的な評価：** インフラストラクチャの重要な変更後に準備状況レポートを実行
- **現在のレベルに集中：** 先に進む前に現在のレベルの不合格条件に対処し、基盤的改善を優先
- **トレンドの追跡：** 進捗グラフを使用して時間経過に伴う改善を監視
- **高インパクトの修正を優先：** CLIレポートのアクション項目は最もインパクトの大きい改善を強調表示
