---
id: jp/cli/getting-started/video-walkthrough
title: "ビデオウォークスルー"
status: published
summary: "Droid CLIのインストール、設定、主要機能を説明する動画チュートリアル"
parent: jp/cli/getting-started/index
tags: [cli, video, tutorial, walkthrough, demo, guide, learn, watch]
relations: [relates_to=cli/getting-started/video-walkthrough]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">ビデオウォークスルー</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Droid CLIのインストール、設定、主要機能を説明する動画チュートリアル</p>


<iframe
  class="w-full aspect-video rounded-xl"
  src="https://youtube.com/embed/aw0thMXwAMY"
  title="Droid CLI動画ウォークスルー"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
></iframe>

## インストール & セットアップ {#installation-setup}

お好みのターミナルでDroid CLIをインストールして開始しましょう。



<div class="factory-codegroup">
<div class="factory-codegroup-bar"><button type="button" class="factory-codegroup-tab is-active" data-tab-idx="0">macOS/Linux</button><button type="button" class="factory-codegroup-tab" data-tab-idx="1">Windows</button></div>

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

</div>



インストールを確認します：

```bash
which droid
```

Droid CLIを開始します：

```bash
cd /path/to/your/project
droid
```

### 初回認証 {#first-time-authentication}

初回実行時には、オンボーディング画面が表示されます：

1. アカウントの作成またはログインを選択します
2. ブラウザで認証コードを確認します
3. ターミナルに戻ってdroidの使用を開始します

## インターフェース & ショートカット {#interface-shortcuts}

### ヘルプメニュー {#help-menu}

`Shift + ?`を押してヘルプメニューを開きます。表示される内容：

- メッセージの送信方法と改行の作成方法
- 利用可能なキーボードショートカット
- 基本的なナビゲーションコマンド
- 自律モードオプション



<Aside kind="note">
**ターミナル固有のキーバインド**: 改行のデフォルトは`\` + `Enter`ですが、ターミナルのキーバインドに応じて`Shift + Enter`などの組み合わせに設定できます。設定オプションはCLIの`/terminal-setup`で確認してください。
</Aside>



### 基本的なキーボードショートカット {#essential-keyboard-shortcuts}

| ショートカット | アクション |
|----------|--------|
| `Enter` | メッセージを送信 |
| `\` + `Enter` (または `Shift + Enter`) | メッセージ内で改行 |
| `Esc` (ダブルタップ) | 現在の入力をクリア |
| `Shift + ?` | ヘルプメニューを開く |
| `Shift + Tab` | 自律モードを切り替え |
| 入力が空の状態で`!` | 直接シェルコマンドを実行するBashモードを切り替え |
| `/` | コマンドメニューを開く |
| `Cmd + Shift + H` | ルートディレクトリを表示 |
| `Cmd + Shift + .` | 隠しファイル/フォルダを表示 |
| `Ctrl + C` または `exit` | droidを終了 |
| `Ctrl + V` | 画像を貼り付け |



<Aside kind="note">
画像貼り付けショートカットはすべてのターミナルで機能しますが、具体的なキーバインドはターミナル設定によって異なる場合があります。
</Aside>





<Aside kind="note">
Bashモードでは、プロンプトが`$`に変わります。シェルコマンドを入力して`Enter`を押し、通常のチャットに戻るには`Esc`を押します。
</Aside>



## 自律モード {#autonomy-modes}

`Shift + Tab`を押して異なる自律レベルを切り替えます：

[[jp/cli/user-guides/specification-mode|仕様モードについて詳しく見る →]]





<Details summary="仕様モード（調査と計画のみ）">
Droidは変更を加えずに調査して計画を作成します。実行前に何が起こるかを理解するのに最適です。

  - ファイル編集なし
  - コマンド実行なし
  - 詳細な仕様を作成
  - 進める前に計画を反復改善できます
</Details>



  

<Details summary="低モード（読み取り専用 + 安全なコマンド）">
ファイルの読み取りと、低リスクで読み取り専用のコマンド実行を許可します。

  - ファイル読み取り
  - ディレクトリ一覧
  - 安全な診断コマンド
  - 変更なし
</Details>



  

<Details summary="Mediumモード（ファイル編集を許可）">
ファイル変更と、簡単に戻せる中リスクのコマンドを有効にします。

  - ファイルの作成・編集・削除
  - ビルドコマンドの実行
  - テスト実行
  - 元に戻せる操作
</Details>



  

<Details summary="高モード（保護付きですべてのコマンド）">
すべてのコマンドを許可しつつ、許可/拒否リストで安全性を維持します。

  - 完全なコマンド実行
  - ファイル削除操作（確認付き）
  - Git操作
  - 許可/拒否リストで設定可能
</Details>







<Aside kind="warning">
高モードでも、ファイル削除のような危険な操作は、許可リストで明示的に設定しない限り常に承認が必要です。
</Aside>



[[jp/cli/configuration/settings|自律性設定を構成する →]]

## スラッシュコマンド {#slash-commands}

`/`を押してコマンドメニューにアクセスします。以下のオプションがあります：

- **Account & Billing** - Factoryアカウントを管理
- **Model** - AIモデルの切り替えと推論レベルの設定
- **Sessions** - 過去のセッションの表示とナビゲーション
- **Settings** - CLI設定の構成
- **Terminal Setup** - キーバインドの構成
- **Custom Commands** - [[jp/cli/configuration/custom-slash-commands|custom slash commands]]にアクセス
- **Droids** - [[jp/cli/configuration/custom-droids|custom sub-agents]]の管理
- **MCP** - [[jp/cli/configuration/mcp|Model Context Protocol integrations]]の構成

### モデルの切り替え {#switching-models}

`/model`でモデルメニューにアクセス：

1. 利用可能なモデルを表示
2. 異なるタスクに応じてモデルを切り替え
3. 該当する場合は推論レベルを設定



<Aside kind="tip">
モデルごとに得意なタスクは異なります。複雑な計画には推論モデルを、定型的な編集には高速なモデルを使用します。
</Aside>



[[jp/models|モデル選択について学ぶ →]]

### セッション管理 {#sessions-management}

`/sessions`でアクセス：

- すべての過去のセッションを表示
- 任意の過去のセッションにナビゲート
- Factory Appでセッションを開く
- 中断したところから作業を続行

セッションがFactory Appに表示されるには、設定でクラウド同期が有効になっている必要があります。

## 設定 & 構成 {#settings-configuration}

`/settings`で設定にアクセスし、エクスペリエンスをカスタマイズできます：

[[jp/cli/configuration/settings|設定ドキュメント全体 →]]

### コア設定 {#core-settings}



<div class="factory-card-group">

<div class="factory-card">

**モデルと推論**

新しいセッションのデフォルトモデルと推論レベルを選択する

</div>



  

<div class="factory-card">

**Diffモード**

コード変更の表示方法を設定する

</div>



  

<div class="factory-card">

**GitHub完了**

GitHub Copilot形式の補完を有効/無効にする

</div>



  

<div class="factory-card">

**クラウド同期**

セッションをFactory Appに同期

</div>

</div>



### 詳細設定 {#advanced-settings}





<Details summary="PR上のDroid共同作成者">
有効にすると、droidが作成を支援したプルリクエストに共同著者として追加されます。単独の著者にしたい場合は無効化できます。
</Details>



  

<details class="boris-details">
<summary>Droid Shield</summary>

コード内の環境変数とシークレットを保護します。APIキー、パスワード、トークンなどの機密情報の誤コミットを防ぎます。



<Aside kind="warning">
セキュリティ脆弱性から保護するため、有効のままにしてください。
</Aside>



[[jp/cli/account/droid-shield|Droid Shieldについて詳しく見る →]]

</details>



  

<Details summary="仕様をMarkdownとして保存">
仕様モードで生成された仕様を参照・ドキュメント用のMarkdownファイルとしてマシンに自動保存します。

[[jp/cli/user-guides/specification-mode|仕様モードについて詳しく見る →]]
</Details>



  

<Details summary="許可リストと拒否リスト">
高自律性モードでも承認が必要なコマンドを設定します。高モードでも、ファイル削除操作はデフォルトで確認が必要です。

[[jp/cli/user-guides/auto-run|自動実行設定について詳しく見る →]]
</Details>





### IDE統合 {#ide-integration}

設定メニューから直接VS Code、Cursor、その他のIDEのdroidエクステンションをインストールできます。

[[jp/integrations/ide-integrations|IDE連携について詳しく見る →]]

## 構成ファイル {#configuration-files}

`Cmd + Shift + H`を押してルートディレクトリを表示し、次に`Cmd + Shift + .`を押して隠しファイルを表示して構成ディレクトリにアクセスします。`~/.factory/`フォルダにナビゲートします。

### ディレクトリ構造 {#directory-structure}

```
~/.factory/
├── config.json          # Model configuration and BYOK
├── settings.json        # CLI settings and allow/deny lists
├── mcp.json            # MCP integrations
├── droids/             # Custom sub-agents
├── commands/           # Custom slash commands
├── logs/               # Session logs
└── bug-reports/        # Crash reports
```



<Aside kind="tip">
詳しく見る: [[jp/cli/configuration/settings|設定]] | [[jp/cli/configuration/custom-slash-commands|カスタムスラッシュコマンド]] | [[jp/cli/configuration/custom-droids|カスタムDroid]] | [[jp/cli/configuration/mcp|MCP設定]]
</Aside>



### config.json - 独自キーの使用 {#configjson---bring-your-own-key}

独自のAPIキーを使用してカスタムモデルを構成：

```json
{
  "models": [
    {
      "provider": "openrouter",
      "name": "anthropic/claude-3.5-sonnet",
      "apiKey": "your-api-key-here",
      "displayName": "Claude 3.5 Sonnet (OpenRouter)"
    }
  ]
}
```



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">プロバイダードキュメントを探す</div>

[[jp/cli/byok/overview|独自キーの使用ドキュメント]]にアクセスし、プロバイダー（OpenRouter、Fireworksなど）を選択します

</div>



  

<div class="factory-step">

<div class="factory-step-title">設定テンプレートをコピー</div>

選択したプロバイダーのJSON設定をコピーします

</div>



  

<div class="factory-step">

<div class="factory-step-title">config.jsonに追加</div>

設定を`~/.factory/config.json`に貼り付け、APIキーを追加します

</div>



  

<div class="factory-step">

<div class="factory-step-title">モデルを選択</div>

CLIで`/model`を使用して、新しく追加したモデルを選択します

</div>

</div>



[[jp/cli/byok/overview|すべてのBYOKプロバイダーを見る →]]

### settings.json - 許可 & 拒否リスト {#settingsjson---allow-deny-lists}

高自律モードで承認が必要なコマンドを構成：

```json
{
  "autoModeAllow": [],
  "autoModeDeny": [
    "git push",
    "rm -rf",
    "npm publish"
  ]
}
```

高モードでも、`autoModeDeny`リストのコマンドは常に実行前に明示的な承認が必要です。

### mcp.json - MCP統合 {#mcpjson---mcp-integrations}

MCPツールを個別に有効または無効にします：

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-api-key"
      }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-playwright"],
      "disabled": true
    }
  }
}
```

`"disabled": true`を設定して、構成を削除せずに一時的にMCPを無効にできます。

[[jp/cli/configuration/mcp|MCP設定について詳しく見る →]]

## カスタムDroid（サブエージェント） {#custom-droids-sub-agents}

カスタムdroidは特定のタスクを処理する専門的なAIエージェントです。`/droids`でdroidメニューにアクセス：

### Droidの管理 {#managing-droids}

- **Import** (`i`) - 他のエージェントからビルド済みdroidをインポート
- **Create** (`c`) - 新しいカスタムdroidを作成
- **Edit** - 既存のdroid構成を変更
- **Enable/Disable** - droidのオン/オフを切り替え

### カスタムDroidの作成 {#creating-a-custom-droid}

[[jp/cli/configuration/custom-droids|カスタムDroidについて詳しく見る →]]



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">スコープを選択</div>

droidを**プロジェクトレベル**（特定リポジトリ）にするか、**個人用**（すべてのプロジェクトで利用可能）にするかを決めます

</div>



  

<div class="factory-step">

<div class="factory-step-title">生成方法</div>

手動で作成するか、droidの支援で生成するかを選択します:

```
I want a code review droid that checks for security issues and coding standards
```

Droidが適切な説明と設定を生成します

</div>



  

<div class="factory-step">

<div class="factory-step-title">モデルを設定</div>

- **継承**: 親セッションと同じモデルを使用します
  - **特定モデル**: このdroid専用のモデルを選択します（例: 複雑な分析には推論モデルを使用）

</div>



  

<div class="factory-step">

<div class="factory-step-title">ツールを有効化</div>

droidがアクセスできるツールと機能を選択します

</div>



  

<div class="factory-step">

<div class="factory-step-title">保存して編集</div>

設定を確認し、必要に応じて詳細を編集します

</div>

</div>



### 使用例 {#example-use-cases}

- **コードレビュー Droid** - プルリクエストの自動コードレビュー
- **Documentation Droid** - ドキュメントの生成と保守
- **Test Generation Droid** - 包括的なテストスイートの作成
- **Security Audit Droid** - 脆弱性とセキュリティ問題のスキャン

## MCP統合 {#mcp-integrations}

Model Context Protocol (MCP)により、droidは外部ツールやデータソースと統合できます。

### CLI経由でのMCP追加 {#adding-mcps-via-cli}

`/mcp add`コマンドを使用：

```bash
/mcp add
```

次にMCPの詳細を提供：
- **Name**: MCPの識別子
- **Command**: 実行可能コマンド（例：`npx`、`python`）
- **Args**: コマンド引数
- **Environment Variables**: APIキーと構成

### 構成済みMCPのリスト表示 {#listing-configured-mcps}

```bash
/mcp list
```

これにより、構成済みの各MCPサーバーに接続し、現在の接続ステータス（**connected**、**connecting**、**needs authentication**、**failed**）が表示されます。OAuthが必要なサーバーは、インタラクティブな`/mcp`マネージャーでサインインを完了するまで**needs authentication**と表示されます。



<Aside kind="note">
MCPを追加または変更した後、変更を反映するためにCLIの再起動が必要な場合があります。
</Aside>



### 構成ファイル経由でのMCP追加 {#adding-mcps-via-configuration-file}

`~/.factory/mcp.json`を直接編集することもできます：

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token-here"
      }
    }
  }
}
```

### 人気のMCP統合 {#popular-mcp-integrations}

- **Brave Search** - Web検索機能
- **Playwright** - ブラウザ自動化
- **GitHub** - リポジトリと課題管理
- **Filesystem** - 拡張ファイルシステムアクセス
- **Postgres** - データベースクエリ
- **Slack** - チームコミュニケーション

[[jp/cli/configuration/mcp|すべてのMCPサーバーを見る →]]

## ワークフロー例：Specモードから実装まで {#example-workflow-spec-mode-to-implementation}

droidの機能を実演する完全なワークフローです：



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Spec Modeで開始</div>

仕様モードになるまで`Shift + Tab`を押します

```
Create an authentication system with GitHub and Google OAuth
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">計画を確認</div>

Droidが詳細な仕様を生成します:
  - アーキテクチャ上の判断
  - 作成・変更するファイル
  - 必要な依存関係
  - 実装手順

</div>



  

<div class="factory-step">

<div class="factory-step-title">仕様を反復改善</div>

実装前に計画を改善します:

```
Change the plan to only include Github auth and not Google auth
```

Droidがそれに応じて仕様を更新します

</div>



  

<div class="factory-step">

<div class="factory-step-title">承認して続行</div>

計画に満足したら、高モードで実装に進みます

</div>



  

<div class="factory-step">

<div class="factory-step-title">変更を確認</div>

Droidは変更内容を正確に表示し、承認を待ちます

</div>

</div>





<Aside kind="tip">
仕様モードは複雑な機能で特に強力です。コードを書く前にアプローチを検証できます。
</Aside>



[[jp/cli/user-guides/specification-mode|仕様モードの完全ガイドを読む →]]

[[jp/cli/user-guides/implementing-large-features|大規模機能の実装について学ぶ →]]

## まとめ {#summary}

以下を学習しました：

- Droid CLIのインストールと認証
- インターフェースのナビゲーションとキーボードショートカットの使用
- 自律モードの理解と切り替え
- 設定と設定の構成
- BYOKでカスタムモデルの追加
- カスタムdroid（サブエージェント）の作成と管理
- MCP経由での外部ツールの統合
- 実装前の計画のためのspecモードの使用

## 次のステップ {#next-steps}



<div class="factory-card-group">

<div class="factory-card">

**[[jp/cli/getting-started/how-to-talk-to-a-droid|Droidとの話し方]]**

droidとのコミュニケーションのベストプラクティスを学ぶ

</div>



  

<div class="factory-card">

**[[jp/cli/getting-started/common-use-cases|よくあるユースケース]]**

実践的なワークフローとシナリオを確認

</div>



  

<div class="factory-card">

**[[jp/cli/user-guides/become-a-power-user|パワーユーザーになる]]**

高度なテクニックと生産性向上のヒント

</div>



  

<div class="factory-card">

**[[jp/cli/configuration/agents-md|AGENTS.mdガイド]]**

プロジェクト固有の規約を文書化する

</div>

</div>
