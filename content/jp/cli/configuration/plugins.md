---
id: jp/cli/configuration/plugins
title: "プラグイン"
status: published
summary: "Droidをスキル、コマンド、ツールの共有可能なパッケージで拡張する。"
parent: jp/cli/configuration/index
tags: [cli, plugins, extensions, marketplace, skills, commands, mcp, shareable]
relations: [relates_to=cli/configuration/plugins]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">プラグイン</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Droidをスキル、コマンド、ツールの共有可能なパッケージで拡張する。</p>


プラグインを使用すると、プロジェクトやチーム間で共有できるカスタム機能でDroidを拡張できます。プラグインは、スキル、スラッシュコマンド、エージェント、MCPサーバーを単一の配布可能なパッケージにバンドルします。

## プラグインとは？ {#what-are-plugins}

プラグインは、マニフェストファイル（`.factory-plugin/plugin.json`）とスキル、コマンド、エージェントなどのオプションコンポーネントを含むディレクトリです。`.factory/`内のスタンドアロン設定とは異なり、プラグインは共有と配布を目的として設計されています。

**プラグインコンポーネント:**

| コンポーネント | 目的 | 呼び出し |
|-----------|---------|------------|
| **スキル** | 指示とツールを含む再利用可能な機能 | タスクに基づいてモデルが自動的に呼び出し |
| **コマンド** | 特定のワークフロー用のスラッシュコマンド | `/command-name`でユーザーが呼び出し |
| **エージェント** | 特殊化されたサブエージェント定義 | Taskツールを介して呼び出し |
| **フック** | ライフサイクルイベントハンドラー | 一致するイベント時に自動 |
| **MCPサーバー** | 外部ツール統合 | プラグインがアクティブな際にツールとして利用可能 |

## プラグイン vs スタンドアロン設定を使用するタイミング {#when-to-use-plugins-vs-standalone-configuration}

| アプローチ | 最適な用途 |
|----------|----------|
| **スタンドアロン**（`.factory/`ディレクトリ） | 個人的なワークフロー、プロジェクト固有のカスタマイズ、クイック実験 |
| **プラグイン** | チームメイトとの共有、コミュニティへの配布、バージョン管理されたリリース、プロジェクト間での再利用 |

迅速な反復のためには`.factory/`でのスタンドアロン設定から始め、共有する準備ができたらプラグインに変換してください。

## プラグイン管理 {#managing-plugins}

Droidはプラグインを管理する2つの方法を提供します：

### インタラクティブUI（推奨） {#interactive-ui-recommended}

`/plugins`スラッシュコマンドを使用してプラグインマネージャーを開きます：
```
/plugins
```
これはタブ形式のインターフェイスが開きます：
- **Browse（閲覧）** - 登録されたマーケットプレイスからプラグインを表示・インストール
- **Installed（インストール済み）** - インストール済みプラグインを管理（情報表示、更新、アンインストール）
- **Marketplaces（マーケットプレイス）** - マーケットプレイスの追加、更新、削除

**ナビゲーション:**
- 左/右矢印: タブ間の切り替え
- 上/下矢印: タブ内のナビゲーション
- Enter: 選択/確認
- Escape: 戻る、または閉じる

### CLI コマンド（スクリプト用） {#cli-commands-for-scripting}

自動化には、シェルからCLI コマンドを使用してください（スラッシュコマンドではありません）：
```bash
# マーケットプレイス管理
droid plugin marketplace add <url>
droid plugin marketplace remove <name>
droid plugin marketplace list
droid plugin marketplace update [name]

# プラグイン管理
droid plugin install <plugin@marketplace> [--scope user|project]
droid plugin uninstall <plugin@marketplace> [--scope user|project]
droid plugin update [plugin@marketplace] [--scope user|project]
droid plugin list [--scope user|project]
```
プラグインIDは`pluginName@marketplaceName`の形式を使用します（例：`security-guidance@claude-plugins-official`）。

## プラグインの構造 {#plugin-structure}

すべてのプラグインは以下のディレクトリ構造に従います：
```
my-plugin/
├── .factory-plugin/
│   └── plugin.json          # プラグインマニフェスト（必須）
├── commands/                 # スラッシュコマンド（任意）
│   └── my-command.md
├── skills/                   # エージェントスキル（任意）
│   └── my-skill/
│       └── SKILL.md
├── droids/                   # Subagent definitions (optional)
│   └── my-agent.md
├── mcp.json                  # MCP server configs (optional)
└── README.md                 # ドキュメント
```


<Aside kind="warning">
`commands/`、`skills/`、`droids/`、または `hooks/` を `.factory-plugin/` ディレクトリ内に配置しないでください。`.factory-plugin/` 内に配置するのは `plugin.json` のみです。その他のディレクトリはすべてプラグインのルートレベルに配置する必要があります。
</Aside>



### プラグインフック {#plugin-hooks}

プラグインは特定のライフサイクルイベントで実行されるフックを含めることができます。`hooks/` ディレクトリを追加し、`hooks.json` ファイルを配置してください：
```
my-plugin/
├── .factory-plugin/
│   └── plugin.json
├── hooks/
│   ├── hooks.json         # フック設定
│   └── my-script.sh       # フックスクリプト
└── ...
```
**hooks/hooks.json の例:**
```json
{
  "PostToolUse": [
    {
      "matcher": "Create|Edit|ApplyPatch",
      "hooks": [
        {
          "type": "command",
          "command": "${DROID_PLUGIN_ROOT}/hooks/format.sh"
        }
      ]
    }
  ]
}
```
`${DROID_PLUGIN_ROOT}`を使用して、プラグインディレクトリ内のファイルを参照します。この変数は、フックが実行される際に実際のプラグインパスに展開されます。詳細については[[jp/reference/hooks-reference#plugin-hooks|フック リファレンス]]を参照してください。

### プラグインマニフェスト {#plugin-manifest}

`.factory-plugin/plugin.json`のマニフェストは、プラグインのアイデンティティを定義します：
```json
{
  "name": "my-plugin",
  "description": "A helpful description of what this plugin does",
  "version": "1.0.0",
  "author": {
    "name": "Your Name"
  }
}
```
| フィールド | 目的 |
|-------|---------|
| `name` | プラグインの一意識別子 |
| `description` | プラグインマネージャーでの閲覧やインストール時に表示される |
| `version` | セマンティックバージョニングを使用してリリースを追跡 |
| `author` | オプション。帰属表示に役立つ |

## プラグインスコープ {#plugin-scopes}

プラグインをインストールする際、インストールスコープを選択します：

| スコープ | 場所 | 可視性 |
|-------|----------|------------|
| **User** | `~/.factory/` | すべてのプロジェクトで利用可能 |
| **Project** | `<project>/.factory/` | gitを通じてチームメイトと共有 |



<Aside kind="note">
**Orgスコープ**: 組織管理設定を通じて有効化されたプラグインは、自動的に`org`スコープでインストールされます。手動でorgスコープを設定することはできません。
</Aside>



プラグインは1つのスコープにのみ存在できます。スコープを変更するには、まずアンインストールしてから再インストールしてください。

## バージョン追跡 {#version-tracking}

プラグインはセマンティックバージョンではなく、Gitコミットハッシュによってバージョニングされます。プラグインを更新すると、Droidはマーケットプレイスリポジトリから最新のコミットを取得します。

マーケットプレイスを特定のバージョンに固定するには、マーケットプレイスソースに `ref`（ブランチまたはタグ）または `sha`（40文字のフルコミットSHA）を設定します。下記の[[jp/cli/configuration/plugins#pinning-a-marketplace-to-a-ref-or-commit|マーケットプレイスをrefまたはコミットに固定する]]を参照してください。

## マーケットプレイス {#marketplaces}

マーケットプレイスは、閲覧やインストールが可能なプラグインのカタログです。

### マーケットプレイスの追加 {#adding-marketplaces}

UI経由：`/plugins` → マーケットプレイスタブ → "新しいマーケットプレイスを追加" → URLを入力

CLI経由：
```bash
# GitHubから
droid plugin marketplace add https://github.com/owner/repo

# その他のGitホストから
droid plugin marketplace add https://gitlab.com/company/plugins.git

# ローカルパスから（開発用）
droid plugin marketplace add /path/to/local/marketplace
```
### マーケットプレースの管理 {#managing-marketplaces}

UI経由: `/plugins` → マーケットプレースタブ → マーケットプレースを選択 → アクションを選択 (更新、自動更新を無効化、削除)

CLI経由:
```bash
droid plugin marketplace list
droid plugin marketplace update [marketplace-name]
droid plugin marketplace remove <marketplace-name>
```


<Aside kind="note">
マーケットプレイスを削除しても、そのマーケットプレイスからのプラグインはアンインストールされません。インストールされたプラグインはキャッシュから機能し続けます。
</Aside>



### チームマーケットプレイス {#team-marketplaces}

`.factory/settings.json`に追加して、自動マーケットプレイスおよびプラグインインストールを設定します：
```json
{
  "extraKnownMarketplaces": {
    "your-org-internal-plugins": {
      "source": {
        "source": "github",
        "repo": "your-org/internal-plugins"
      }
    }
  },
  "enabledPlugins": {
    "code-standards@your-org-internal-plugins": true
  }
}
```
Droidが起動すると、自動的に以下を実行します：
1. `extraKnownMarketplaces`から、まだ登録されていないマーケットプレースを登録
2. `enabledPlugins`から、まだインストールされていないプラグインをインストール

インストールスコープは設定が定義されている場所によって決まります：
- 組織管理設定 → `org`スコープ
- ユーザー設定 → `user`スコープ
- プロジェクト設定 → `project`スコープ

### マーケットプレイスをrefまたはコミットに固定する {#pinning-a-marketplace-to-a-ref-or-commit}

デフォルトでは、Droidはマーケットプレイスのデフォルトブランチを追跡し、更新時に最新のコミットを取得します。ソースオブジェクトに `ref` または `sha` を追加することで、マーケットプレイスを特定のGit refまたはコミットに固定できます。

| フィールド | 型 | 説明 |
|-------|------|-------------|
| `ref` | string | 追跡するブランチまたはタグ（例: `"main"`、`"v1.2.0"`、`"staging"`）。 |
| `sha` | string | 40文字のフルコミットSHA。設定すると、マーケットプレイスはこのコミットに固定され、`droid plugin marketplace update` は何も行いません。 |

`ref` と `sha` は `github`、`url`、`git-subdir` ソースタイプでサポートされています。ハードピンには `sha`、ブランチやタグを追跡するには `ref` を使用します。

```json
{
  "extraKnownMarketplaces": {
    "your-org-internal-plugins": {
      "source": {
        "source": "github",
        "repo": "your-org/internal-plugins",
        "ref": "v1.2.0"
      }
    },
    "your-org-frozen-plugins": {
      "source": {
        "source": "github",
        "repo": "your-org/internal-plugins",
        "sha": "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b"
      }
    }
  }
}
```

CLIからマーケットプレイスを追加する際は、`--ref` または `--sha` を渡します：

```bash
droid plugin marketplace add https://github.com/your-org/internal-plugins --ref v1.2.0
droid plugin marketplace add https://github.com/your-org/internal-plugins --sha 1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b
```

## プラグインの発見 {#discovering-plugins}

### 公式Factoryプラグイン {#official-factory-plugins}

Factoryは`Factory-AI/factory-plugins`で厳選されたプラグインを含む公式プラグインマーケットプレースを管理しています。

`/plugins` UIまたはCLIから追加：
```bash
droid plugin marketplace add https://github.com/Factory-AI/factory-plugins
```
**利用可能なプラグイン:**

| プラグイン | 説明 |
|--------|-------------|
| **[[jp/cli/features/droid-control|droid-control]]** | ターミナル、ブラウザ、コンピュータの自動化。デモの記録、動作主張の検証、QAフローの実行。 |
| **droid-evolved** | 継続学習のためのスキル: セッションナビゲーション、人間による執筆、スキル作成、ビジュアルデザイン、フロントエンドデザイン、ブラウザ自動化 |
| **security-engineer** | セキュリティレビュー、脅威モデリング、コミットスキャン、脆弱性検証 |

`/plugins` UIの（Browse（閲覧）タブ）またはCLI経由でインストール:
```bash
droid plugin install droid-control@factory-plugins
droid plugin install droid-evolved@factory-plugins
droid plugin install security-engineer@factory-plugins
```
### コミュニティプラグイン {#community-plugins}

| プラグイン | 説明 | ソース |
|--------|-------------|--------|
| **superpowers** | ブレインストーミング、プランニング、サブエージェント駆動の開発を含む完全なソフトウェア開発ワークフロー | `obra/superpowers` |

### エンタープライズプラグインレジストリ {#enterprise-plugin-registry}

承認済みプラグインの集中管理が必要な組織については、[[jp/enterprise/enterprise-plugin-registry|エンタープライズプラグインレジストリ]]を参照してください。これにより以下が可能になります：

- 承認済みプラグインのプライベートマーケットプレイスの維持
- 全ユーザー向けの必須プラグインの事前インストール
- チーム、役割、または機能によるプラグインの整理

### Claude Code互換性 {#claude-code-compatibility}

DroidはClaude Code向けに構築されたプラグインと互換性があります。使用したいClaude Codeプラグインを見つけた場合、直接インストールできます - プラグイン形式は相互運用可能です。詳細については[Claude Codeプラグインドキュメント](https://code.claude.com/docs/en/plugins)を参照してください。

## CLI コマンドリファレンス {#cli-command-reference}

`droid plugin` サブコマンドのクイックリファレンスです。すべてのコマンドは `--scope user|project`（エイリアス `-s`）を受け付け、プラグインのインストール先を指定できます。フラグを省略するとプロンプトが表示されます。

| コマンド | 目的 | 例 |
| :------- | :--- | :- |
| `droid plugin install <plugin@marketplace>` | 登録済みのマーケットプレイスからプラグインをインストール。エイリアス: `droid plugin i`。 | `droid plugin install droid-control@factory-plugins --scope project` |
| `droid plugin uninstall <plugin@marketplace>` | インストール済みのプラグインを削除。エイリアス: `droid plugin remove`。 | `droid plugin uninstall droid-control@factory-plugins` |
| `droid plugin update [plugin@marketplace]` | 特定のプラグインを更新。引数なしで呼び出すとすべてのプラグインを更新。 | `droid plugin update droid-control@factory-plugins` |
| `droid plugin list` | インストール済みのプラグインを一覧表示。スコープの指定も可能。 | `droid plugin list --scope user` |
| `droid plugin marketplace` | マーケットプレイスを管理（`add`、`remove`、`list`、`update`）。 | `droid plugin marketplace add https://github.com/Factory-AI/factory-plugins` |

**よくあるワークフロー：**

```bash
droid plugin marketplace add https://github.com/Factory-AI/factory-plugins
droid plugin install droid-control@factory-plugins
droid plugin list
droid plugin update
droid plugin uninstall droid-control@factory-plugins
```



<Aside kind="tip">
閲覧やワンオフのインストールにはインタラクティブな `/plugins` UI を推奨します。オンボーディングのスクリプト化、CI セットアップ、共有のドットファイルでは CLI を利用してください。
</Aside>



## 次のステップ {#next-steps}



<div class="factory-card-group">

<div class="factory-card">

**[[jp/guides/building/building-plugins|プラグインの構築]]**

スキルとコマンドを使用して独自のプラグインを作成する方法を学習します。

</div>


  

<div class="factory-card">

**[[jp/cli/configuration/skills|スキル]]**

スキルの動作方法と作成方法を理解します。

</div>


  

<div class="factory-card">

**[[jp/cli/configuration/custom-slash-commands|カスタムコマンド]]**

ユーザー呼び出し可能なスラッシュコマンドを作成します。

</div>


  

<div class="factory-card">

**[[jp/cli/configuration/custom-droids|カスタムDroid]]**

プラグイン用の専用サブエージェントを作成します。

</div>

</div>
