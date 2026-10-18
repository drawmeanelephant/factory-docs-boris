---
id: jp/cli/getting-started/overview
title: "概要"
status: published
summary: "`droid`へようこそ — ターミナルでDroid CLIの力を活用する"
parent: jp/cli/getting-started/index
tags: [droid, cli, terminal, command-line, factory-cli, droid-cli, install, setup]
relations: [relates_to=cli/getting-started/overview]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">概要</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">`droid`へようこそ — ターミナルでDroid CLIの力を活用する</p>

## 30秒で始める {#get-started-in-30-seconds}



<div class="factory-codegroup">
<div class="factory-codegroup-bar"><button type="button" class="factory-codegroup-tab is-active" data-tab-idx="0">macOS/Linux</button><button type="button" class="factory-codegroup-tab" data-tab-idx="1">Windows</button><button type="button" class="factory-codegroup-tab" data-tab-idx="2">npm</button></div>

<div class="factory-codegroup-panel is-active" data-panel-idx="0">

```bash
curl -fsSL https://app.factory.ai/cli | sh
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="1">

```powershell
irm https://app.factory.ai/cli/windows | iex
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="2">

```bash
npm install -g droid
```

</div>

</div>



次に、プロジェクトに移動してDroid CLIを開始します。



<div class="factory-codegroup">

```bash
# Navigate to your project
cd /path/to/your/project

# Start interactive session
droid
```

</div>



これでターミナルからFactory の開発エージェントに接続されました。[[jp/cli/getting-started/quickstart|5分クイックスタートを試す →]]



<Aside kind="note">
**クイックヒント:** `!`を押すとbashモードに切り替わり、AIの解釈なしでシェルコマンドを直接実行できます。通常モードに戻るには`Esc`を押します。詳しくは[[jp/reference/cli-reference#bash-mode|CLIリファレンス]]を参照してください。
</Aside>



## 主な機能 {#key-capabilities}

- **Missions**: オーケストレーターが専門のワーカー Droid を編成し、より大きな機能の計画・実装・検証を行うマルチエージェントプロジェクトを起動します。`/missions` で開始するか、`droid exec --mission` でヘッドレス実行できます。[[jp/features/missions/overview|詳細 →]]
- **MCP**: Model Context Protocol を通じて droid を外部のツールやデータソースに接続します。`droid mcp add` でサーバーを追加するか、`/mcp` で管理します。[[jp/cli/configuration/mcp|詳細 →]]
- **カスタム Droid**: 独自のシステムプロンプト、ツール、モデルを持つ専門サブエージェントを定義し、タスクを委任します。`/droids` から管理できます。[[jp/cli/configuration/custom-droids|詳細 →]]
- **Skills**: 再利用可能な手順やドメイン知識をパッケージ化し、droid がオンデマンドで呼び出せるようにします。`/skills` または `/create-skill` でスキルを閲覧・作成します。[[jp/cli/configuration/skills|詳細 →]]
- **Hooks**: 特定のツールイベントの前後にシェルコマンドを実行することで、エージェントのライフサイクル周辺の動作を自動化します。`/hooks` で設定します。[[jp/cli/configuration/hooks-guide|詳細 →]]
- **Plugins**: マーケットプレイスを通じて配布されるスラッシュコマンド、droid、スキル、フックの導入可能なバンドルで droid を拡張します。`droid plugin install` でインストールするか、`/plugins` で管理します。[[jp/cli/configuration/plugins|詳細 →]]
- **Exec モード**: スクリプト、CI/CD パイプライン、自動化のために droid をヘッドレスで実行します。構造化された入出力形式で `droid exec` を使用します。[[jp/cli/droid-exec/overview|詳細 →]]

## `droid` がワークフローにもたらすもの {#what-droid-brings-to-your-workflow}

- **エンドツーエンドの機能開発**: 計画から実装、テストまで - Droidは透明性のあるレビューワークフローを通じてあなたのコントロール下を保ちながら、完全な開発ライフサイクルを処理します。
- **コードベースの深い理解**: リポジトリ、ドキュメント、課題追跡にわたる組織の共有知識を活用し、時間と共に改善される文脈を意識したサポートを提供します。
- **エンジニアリングシステムとの統合**: 既存のツールに直接接続し、Jira、Notion、Slackなどの多くのツールとのネイティブ統合により、開発作業をチームのプロセスと同期させ続けます。
- **本番環境対応の自動化**: 開発中またはCI/CDパイプラインで同じワークフローをローカルにデプロイし、初日からエンタープライズセキュリティとコンプライアンスが組み込まれています。

## チームがFactoryを選ぶ理由 {#why-teams-choose-factory}

- **エンタープライズ向けに構築**: オンプレミスデプロイメントオプション、SOC-2コンプライアンス、エアギャップ環境。私たちは最低価格帯への競争よりもセキュリティと品質を優先しています。
- **あなたのツールを強化**: 既存のターミナル、IDE、開発環境内で動作します。エディタを切り替えたり新しいインターフェースを学ぶ必要はありません — Droidはあなたがすでに生産性を発揮している場所で統合されます。
- **透明性と制御可能性**: Droidが行うすべての決定は可視化され、レビュー可能です。私たちのネイティブdiffビューアと承認ワークフローにより、コード変更の完全な監視を維持できます。
- **モデルの柔軟性**: 単一のAIプロバイダーにロックインされません。Factoryでは、組織全体で一貫した動作とメモリを維持しながら、各ジョブに最適なモデルにタスクをルーティングできます。

## 次のステップ {#next-steps}



<div class="factory-card-group">

<div class="factory-card">

**[[jp/cli/getting-started/quickstart|クイックスタート]]**

実践的な例でDroidの動作を見る

</div>


  

<div class="factory-card">

**[[jp/cli/getting-started/common-use-cases|よくあるユースケース]]**

一般的なワークフローのステップごとのガイド

</div>


  

<div class="factory-card">

**[[jp/integrations/ide-integrations|IDE連携]]**

IDEにDroidを追加する

</div>


  

<div class="factory-card">

**[[jp/cli/configuration/settings|設定]]**

ワークフローに合わせてDroidをカスタマイズする

</div>

</div>



## 追加リソース {#additional-resources}



<div class="factory-card-group">

<div class="factory-card">

**[[jp/cli/configuration/agents-md|AGENTS.mdガイド]]**

プロジェクト固有のガイダンスと規約を設定する

</div>


  

<div class="factory-card">

**[[jp/reference/cli-reference|CLIリファレンス]]**

droidコマンドの完全なリファレンス

</div>

</div>
