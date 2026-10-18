---
id: jp/cli/getting-started/quickstart
title: "クイックスタート"
status: published
summary: "インタラクティブなターミナルUIでDroid CLIを5分で使い始める。"
parent: jp/cli/getting-started/index
tags: [quickstart, tutorial, getting-started, droid, cli, install-droid, setup, first-steps]
relations: [relates_to=cli/getting-started/quickstart]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">クイックスタート</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">インタラクティブなターミナルUIでDroid CLIを5分で使い始める。</p>


このクイックスタートガイドでは、わずか数分でFactory の開発エージェントとの協業を開始できます。Droidがあなたのコードベースを理解し、思慮深い変更を行い、既存のワークフローと統合する方法を体験できます。

## 始める前に {#before-you-begin}

以下をご用意ください：

- コードプロジェクト内で開いたターミナル
- Git リポジトリ（完全なワークフローデモンストレーションのため推奨）

## ステップ1: Droid CLIをインストールして開始 {#step-1-install-and-start-droid}



<div class="factory-codegroup">
<div class="factory-codegroup-bar"><button type="button" class="factory-codegroup-tab is-active" data-tab-idx="0">macOS/Linux</button><button type="button" class="factory-codegroup-tab" data-tab-idx="1">Homebrew</button><button type="button" class="factory-codegroup-tab" data-tab-idx="2">Windows</button><button type="button" class="factory-codegroup-tab" data-tab-idx="3">npm</button></div>

<div class="factory-codegroup-panel is-active" data-panel-idx="0">

```bash
curl -fsSL https://app.factory.ai/cli | sh
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="1">

```bash
brew install --cask droid
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="2">

```powershell
irm https://app.factory.ai/cli/windows | iex
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="3">

```bash
npm install -g droid
```

</div>

</div>





<Aside kind="note">
**Linuxユーザー:** 正しく動作させるには`xdg-utils`がインストールされていることを確認してください。インストール: `sudo apt-get install xdg-utils`
</Aside>



次に、プロジェクトに移動してDroid CLIを開始します。



<div class="factory-codegroup">

```bash
# Navigate to your project
cd /path/to/your/project

# Start interactive session
droid
```

</div>



<img
  src="../../../images/droid_tui_intro.png"
  alt="Droid CLI"
  height="450"
  class="rounded-lg"
/>

フルスクリーンのターミナルインターフェースでDroidのウェルカム画面が表示されます。プロンプトが表示された場合は、ブラウザ経由でサインインしてFactoryの開発エージェントに接続してください。

## ステップ2: コードベースを探索 {#step-2-explore-your-codebase}

まず、Droidにあなたのプロジェクトを理解してもらいましょう。以下の質問のいずれかを試してみてください：

```

> analyze this codebase and explain the overall architecture

```

```

> what technologies and frameworks does this project use?

```

```

> where are the main entry points and how is testing set up?

```

Droidはファイルを文脈的に読み取り、組織の知識を活用してプロジェクト構造と規約に関する包括的な洞察を提供します。

## ステップ3: 初回のコード変更を実行 {#step-3-make-your-first-code-change}

それでは、簡単な修正でDroidの動作を見てみましょう：

```

> add comprehensive logging to the main application startup

```

Droidは以下を実行します：

1. 現在のログ設定を分析
2. 明確な計画とともに具体的な変更を提案
3. 何が修正されるかを正確に表示
4. 変更を行う前にあなたの承認を待機

この透明なレビュープロセスにより、すべてのコード修正に対して完全な制御を維持できます。

## ステップ4: エンタープライズワークフローを体験 {#step-4-experience-enterprise-workflows}

Droidのエンタープライズ機能を示すより複雑なタスクを試してみてください：

```

> audit this codebase for security vulnerabilities and create a remediation plan

```

または、リンクを貼り付けてチームのツールからのコンテキストを提供してください：

```

> implement the feature described in this Jira ticket: https://company.atlassian.net/browse/PROJ-123

```

Factory App経由でこれらのプラットフォームを統合している場合、DroidはJira、Notion、Slack、その他のソースからコンテキストを自動的に読み取ることができます。DroidはMCP統合を介して追加のツールにも接続でき、さらなる機能を提供します。

## ステップ5: バージョン管理を処理 {#step-5-handle-version-control}

Droidは Git 操作を対話的で賢いものにします：

```

> review my uncommitted changes and suggest improvements before I commit

```

```

> create a well-structured commit with a descriptive message following our team conventions

```

```

> analyze the last few commits and identify any potential issues or patterns

```

## 基本的なコントロール {#essential-controls}

日常的に使用する主要な操作は以下の通りです：

| アクション           | 実行内容                                              | 使用方法                                     |
| -------------------- | ----------------------------------------------------- | -------------------------------------------- |
| メッセージ送信       | タスクまたは質問を送信                                | 入力して**Enter**を押す                      |
| 複数行入力           | より長いプロンプトを記述                              | **Shift\+Enter**で改行                       |
| 変更を承認           | 提案された修正を受け入れ                              | TUIで変更を受け入れ                          |
| 変更を拒否           | 提案された修正を拒否                                  | TUIで変更を拒否                              |
| モード切り替え       | モード間を切り替え                                    | **Shift\+Tab**                               |
| Bashモード           | AIの解釈なしでシェルコマンドを直接実行                | 入力が空の状態で`!`を押す；戻るには`Esc`     |
| トランスクリプト表示 | メッセージ詳細を含む詳細なトランスクリプトを切り替え  | **Ctrl+O**                                   |
| ミッションコントロール | Mission Control オーバーレイを切り替え（オーケストレーターセッション） | **Ctrl+T**                       |
| オーバーレイを閉じる | アクティブなオーバーレイまたはメニューを閉じる        | **Escape**                                   |
| トランスクリプトをスクロール | 過去のターンを移動                            | **Alt+Up** / **Alt+Down**                    |
| ショートカット表示   | 利用可能なコマンドをすべて表示                        | **?**を押す                                  |
| セッション終了       | Droidを終了                                           | **Ctrl\+C**または`exit`を入力                |

### 便利なスラッシュコマンド {#useful-slash-commands}

よく使う操作への簡単なショートカット：

- `/review` - AI搭載コードレビューワークフローを開始（[[jp/cli/features/code-review|learn more]]）
- `/settings` - Droidの動作、モデル、設定を構成
- `/model` - セッション中にAIモデルを切り替え
- `/sessions` - 過去のセッションを一覧表示し再開
- `/fork` - 現在のセッションを新しいブランチへフォーク
- `/compress` - 現在のセッションを圧縮してコンテキストを解放
- `/missions` - Missions メニューを開いてマルチエージェントプロジェクトを起動
- `/droids` - カスタム Droid（専門サブエージェント）を管理
- `/skills` - プロンプトベースのスキル（再利用可能な手順）を管理
- `/hooks` - ライフサイクル自動化のためのツール実行フックを管理
- `/plugins` - プラグインとマーケットプレイスを管理
- `/mcp` - Model Context Protocol サーバーを管理
- `/account` - ブラウザでFactory アカウント設定を開く
- `/billing` - 請求設定を表示・管理
- `/help` - 利用可能なコマンドをすべて表示

[[jp/cli/configuration/custom-slash-commands|カスタムスラッシュコマンドの作成方法を学ぶ →]]

## 協業のベストプラクティス {#collaboration-best-practices}

**コンテキストを具体的に：**
次の代わりに：「バグを修正して」
こう試してください：「設定された30分ではなく5分後にユーザーがログアウトされる認証タイムアウトの問題を修正して」

**複雑な機能には仕様モードを使用：**
より大きな機能については、[[jp/cli/user-guides/specification-mode|Specification Mode]]を使用してください。これは明示的に要求しなくても実装前に自動的に計画を提供します。

**組織の知識を活用：**

```

> following our team's coding standards, implement the user preferences feature described in ticket PROJ-123

```

**レビューワークフローを使用：**
承認前にDroidの提案された変更を常にレビューしてください。透明な差分表示により、何が修正されるかを正確に理解できます。

## エンタープライズチーム向けプロ・ティップス {#pro-tips-for-enterprise-teams}

**セキュリティファーストアプローチ：**
Droidは自動的にセキュリティへの影響を考慮し、コード生成時に潜在的な脆弱性にフラグを立てます。

**コンプライアンス統合：**
MCP を介してコンプライアンスツールを接続し、すべての変更が組織の標準を満たすようにします。

**チームの知識共有：**
Droidは組織のパターンから学習し、チームメンバーとプロジェクト間での一貫性を維持するのに役立ちます。

## 次のステップ {#whats-next}



<div class="factory-card-group">

<div class="factory-card">

**[[jp/cli/getting-started/common-use-cases|よくあるユースケース]]**

実践的なシナリオとワークフローを確認

</div>


  

<div class="factory-card">

**[[jp/cli/configuration/settings|設定]]**

チームのワークフローに合わせてDroidをカスタマイズする

</div>


  

<div class="factory-card">

**[[jp/cli/configuration/agents-md|AGENTS.mdガイド]]**

プロジェクトの規約とコマンドを文書化する

</div>


  

<div class="factory-card">

**[[jp/integrations/ide-integrations|IDE連携]]**

お気に入りのエディター内でDroidを使用する

</div>

</div>
