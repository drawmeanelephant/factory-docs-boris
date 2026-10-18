---
id: jp/enterprise/hierarchical-settings-and-org-control
title: "階層設定と組織管理"
status: published
summary: "組織、プロジェクト、フォルダ、ユーザー設定がどのように連携してDroidのモデル、ツール、安全ポリシー、テレメトリを制御するか。"
parent: jp/enterprise/index
tags: [enterprise]
relations: [relates_to=enterprise/hierarchical-settings-and-org-control]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">階層設定と組織管理</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">組織、プロジェクト、フォルダ、ユーザー設定がどのように連携してDroidのモデル、ツール、安全ポリシー、テレメトリを制御するか。</p>


Factoryのエンタープライズストーリーは、**単一で予測可能な設定階層**の上に構築されています。マシンごとのアドホックな設定の代わりに、組織はポリシーを一度表現し、ラップトップ、CI、VM、エアギャップ環境全体で一貫して適用させることができます。

このページでは、階層がどのように機能するか、そしてモデル、ツール、安全ポリシー、テレメトリを統制するためにそれをどのように使用するかを説明します。

---

## 4つのレベル {#the-four-levels}

設定は、4つのレベルで一貫した構造を持つ`.factory/`フォルダで定義されます：
```text
Org         → Central `.factory/` bundle (or config endpoint)
Folder      → <git-root>/.../subfolder/.factory/
Project     → <git-root>/.factory/
User        → ~/.factory/
```
各 `.factory/` フォルダには以下が含まれます：

- `settings.json` – 一般設定（モデル、安全性、環境設定、テレメトリ）
- `hooks.json` – フック定義
- `mcp.json` – MCP サーバー設定
- `droids/` – droid 定義
- `commands/` – カスタムコマンド
- `skills/` – スキル定義

すべてのレベルで**同じスキーマ**が適用されます。変わるのは**優先度**です。

---

## システム管理 `settings.json` ファイル {#system-managed-settings-file}

ユーザーがサインインする**前に**組織ポリシーを適用する必要があるデプロイメント — 管理対象ラップトップ、Factory に認証されていない CI ランナー、エアギャップ環境または制限付きネットワークのインストール — では、IT / MDM 管理者は各マシンのハードコードされた既知のパスに `settings.json` を配置できます：

| OS | パス |
| ------------ | ----------------------------------------------------- |
| macOS | `/Library/Application Support/Factory/settings.json` |
| Linux と WSL | `/etc/factory/settings.json` |
| Windows | `C:\Program Files\Factory\settings.json` |

このファイルは、このページの他の部分と同じ [[jp/enterprise/hierarchical-settings-and-org-control#settings-json-schema|Settings JSON スキーマ]] を使用します。

このファイルが存在する場合、そのマシンでは**組織レベル設定の正式な情報源**となり、組織設定に対する API 取得や開発者モードの環境変数オーバーライドは行われません。`factoryTier` シグナルは引き続きベストエフォートで Factory API に問い合わせられ（失敗しても致命的ではありません）、管理対象デプロイメントでもエンタープライズ限定の動作が維持されます。

このファイルが存在しない、または読み取れない場合、Droid は既存の組織設定フロー（Factory App / managed-settings エンドポイント）にフォールバックします。ファイルが存在しても形式が不正、またはスキーマ検証に失敗した場合、組織設定は空のポリシーとして解決され、失敗はログに記録されます。つまり、壊れた管理者デプロイメントが**黙ってバイパスされることはありません**。

これは、MDM イメージやインストーラーとともにベースポリシーを配布する推奨方法であり、ユーザーがこれを上書きしたり弱めたりすることはできません。

---

## Settings JSON スキーマ {#settings-json-schema}

以下は組織管理設定の完全なスキーマです。これらは Factory App の [Enterprise Controls](https://app.factory.ai) ページで組織管理者によって設定されます。すべてのプロパティはオプションです。設定する必要のないフィールドは省略してください。



<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">sessionDefaultSettings</span><span class="factory-rf-type">object</span></div>

セッションのデフォルト環境設定
  

<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">model</span><span class="factory-rf-type">string</span></div>

デフォルトモデル識別子（例：`claude-opus-4-6`、`gpt-5.3-codex`）

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">reasoningEffort</span><span class="factory-rf-type">string</span></div>

モデルが応答前にどれだけ思考するか。`none`、`dynamic`、`off`、`minimal`、`low`、`medium`、`high`、`xhigh`、`max` のいずれか

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">interactionMode</span><span class="factory-rf-type">string</span></div>

Droid インタラクションモード。`auto`、`spec`、`agi` のいずれか

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">autonomyMode</span><span class="factory-rf-type">string</span></div>

セッションの自律モード。`normal`、`spec`、`auto-low`、`auto-medium`、`auto-high` のいずれか

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">specModeModel</span><span class="factory-rf-type">string</span></div>

spec モードがアクティブな時に使用するモデル

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">specModeReasoningEffort</span><span class="factory-rf-type">string</span></div>

spec モード用の推論努力のオーバーライド。`reasoningEffort` と同じ値

</div>
</Details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">maxAutonomyLevel</span><span class="factory-rf-type">string</span></div>

任意のユーザーまたはプロジェクトが設定できる最大自律レベル。`off`、`low`、`medium`、`high` のいずれか

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">builtInToolAutonomyOverrides</span><span class="factory-rf-type">object</span></div>

組み込みネットワークツールを確認プロンプトなしで実行するために必要な、ツールごとの[[jp/cli/user-guides/auto-run|自律レベル]]。組み込みツール名を `low`、`medium`、`high` にマッピングします。ツールは、セッションの自律レベルが設定された要件以上の場合にのみ自動実行され、それ以外の場合は Droid が承認を求めます。エントリのないツールはデフォルトで `low` になります。組織管理設定からのみ適用されるため、ユーザーおよびプロジェクト設定で弱めることはできません。Enterprise Controls の **Built-in Tool Autonomy** で設定します。
  

<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">WebSearch</span><span class="factory-rf-type">string</span></div>

組み込みの Web Search ツールを実行するために必要な自律レベル。`low`、`medium`、`high` のいずれか。デフォルトは `low`。

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">FetchUrl</span><span class="factory-rf-type">string</span></div>

組み込みの Fetch URL ツールを実行するために必要な自律レベル。`low`、`medium`、`high` のいずれか。デフォルトは `low`。

</div>
</Details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">subagentAutonomyLevel</span><span class="factory-rf-type">string</span></div>

Task ツールによって起動されるサブエージェントに適用される自律レベル。`inherit`、`off`、`low`、`medium`、`high` のいずれか。デフォルトは `inherit` で、親セッションの自律レベルにフォールバックします。明示的なレベルは `maxAutonomyLevel` によって制限されるため、エンタープライズの上限を超えることはありません。

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">cloudSessionSync</span><span class="factory-rf-type">boolean</span></div>

セッションがクラウドに同期されるかどうか

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">wikiCloudSync</span><span class="factory-rf-type">boolean</span></div>

AutoWiki コンテンツを Factory App に保存し、GitHub wiki に同期できるかどうか

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">disableWeeklyUsageSummary</span><span class="factory-rf-type">boolean</span></div>

月間クレジット上限の80%以上に達したユーザーと有効なサービスアカウントを一覧にした週次メールを、組織のマネージャーおよびオーナーへ送信するかどうかを制御します。未設定または `false` の場合は送信され、`true` に設定すると停止します。

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">includeCoAuthoredByDroid</span><span class="factory-rf-type">boolean</span></div>

git コミットに `Co-authored-by: Droid` トレーラーを含めるかどうか

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">enableDroidShield</span><span class="factory-rf-type">boolean</span></div>

Droid Shield 安全性チェックを有効にするかどうか

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">ideAutoConnect</span><span class="factory-rf-type">boolean</span></div>

セッション開始時に IDE に自動接続するかどうか

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">commandAllowlist</span><span class="factory-rf-type">string[]</span></div>

常に許可されるシェルコマンドパターン（レベル間で累積）

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">commandDenylist</span><span class="factory-rf-type">string[]</span></div>

常に確認が必要なシェルコマンドパターン（レベル間で累積）。denylistのコマンドでも、ユーザーが明示的に承認すれば実行できます。ハードブロックには`commandBlocklist`を使用してください。

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">commandBlocklist</span><span class="factory-rf-type">string[]</span></div>

絶対に実行されないシェルコマンドパターン（レベル間で累積）。拒否リストとは異なり、ブロックされたコマンドには承認の手段がありません。完全自律、自動実行、`--skip-permissions-unsafe`のいずれの場合でもブロックが適用されます。droidは照合前に実際に呼び出されるプログラムを解決するため、ラッパーシェル、絶対パス、クォートのトリック、コマンド置換で回避することはできません。組織が義務付けるハードストップに使用してください。

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">allowManagedHooksOnly</span><span class="factory-rf-type">boolean</span></div>

`true` の場合、組織管理フックと、組織が有効にしたプラグイン由来のフックのみが読み込まれます。ユーザーレベルおよびプロジェクトレベルで定義されたフックは無視されます。デフォルトは `false` で、すべてのレベルのフックが通常どおりマージされます。[[jp/reference/hooks-reference#org-managed-hooks|組織管理フック]] を参照してください。

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">hooks</span><span class="factory-rf-type">object</span></div>

[[jp/reference/hooks-reference#hook-events|フックイベント]] をキーとする組織管理フック定義。組織が定義したフックは常に読み込まれ、下位レベルで削除することはできません。フックの完全なセマンティクスについては [[jp/reference/hooks-reference|フックリファレンス]] を参照してください。
  

<details class="boris-details">
<summary>properties</summary>

<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">field</span><span class="factory-rf-type">string</span></div>

" type="object[]">
フックイベントごとに1つのキー: `PreToolUse`、`PostToolUse`、`Notification`、`UserPromptSubmit`、`Stop`、`SubagentStop`、`PreCompact`、`SessionStart`、`SessionEnd`。各値はマッチャーグループの配列です。不明なイベントキーは許容されますが、読み込み時に警告が表示されます。


<details class="boris-details">
<summary>properties</summary>

<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">matcher</span><span class="factory-rf-type">string</span></div>

照合するツール名のパターン（`PreToolUse` と `PostToolUse` のみに適用）。

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">commandRegex</span><span class="factory-rf-type">string</span></div>

コマンドに対して照合される任意の正規表現。

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">hooks</span><span class="factory-rf-type">object[]</span><span class="factory-rf-required">required</span></div>

マッチャーが一致したときに実行するコマンド。


<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">type</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

`"command"` である必要があります。

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">command</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

実行するシェルコマンド。

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">timeout</span><span class="factory-rf-type">number</span></div>

コマンドごとのタイムアウト（秒）。

</div>

</details>



</div>

</details>



</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">hooksDisabled</span><span class="factory-rf-type">boolean</span></div>

セッションのすべてのフックを無効にします。

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">showHookOutput</span><span class="factory-rf-type">boolean</span></div>

セッションビューにフック出力を表示します。

</div>
</Details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">customModels</span><span class="factory-rf-type">object[]</span></div>

組織提供のカスタムモデル定義
  

<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">model</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

プロバイダー API に送信されるモデル名

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">id</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

このカスタムモデルエントリの一意識別子。`custom:` で始まる必要があります（例：`custom:my-internal-model-v1`）

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">index</span><span class="factory-rf-type">integer</span><span class="factory-rf-required">required</span></div>

表示順序インデックス

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">baseUrl</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

モデル API エンドポイントのベース URL

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">apiKey</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

プロバイダーとの認証用 API キー

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">provider</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

プロバイダータイプ。`anthropic`、`openai`、`generic-chat-completion-api`、`factory`、`google`、`xai`、`voyage` のいずれか

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">displayName</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

モデル選択画面に表示される人間が読める名前

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">maxContextLimit</span><span class="factory-rf-type">integer</span></div>

トークン単位での最大コンテキストウィンドウサイズ

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">enableThinking</span><span class="factory-rf-type">boolean</span></div>

拡張思考 / 思考の連鎖を有効にするかどうか

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">thinkingMaxTokens</span><span class="factory-rf-type">integer</span></div>

思考フェーズの最大トークン数

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">maxOutputTokens</span><span class="factory-rf-type">integer</span></div>

最大出力トークン数

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">extraHeaders</span><span class="factory-rf-type">object</span></div>

各リクエストで送信する追加 HTTP ヘッダー。ヘッダー名と値のマップ

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">extraArgs</span><span class="factory-rf-type">object</span></div>

API に渡される追加のプロバイダー固有引数

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">noImageSupport</span><span class="factory-rf-type">boolean</span><span class="factory-rf-required">required</span></div>

モデルが画像入力をサポートしない場合は `true` に設定

</div>
</Details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">modelPolicy</span><span class="factory-rf-type">object</span></div>

組織レベルのモデルアクセス制御
  

<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">allowedModelIds</span><span class="factory-rf-type">string[]</span></div>

明示的に許可されるモデル ID。以下の [[jp/enterprise/hierarchical-settings-and-org-control#supported-model-ids|サポートされるモデル ID]] を参照

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">blockedModelIds</span><span class="factory-rf-type">string[]</span></div>

明示的にブロックされるモデル ID

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">allowCustomModels</span><span class="factory-rf-type">boolean</span></div>

ユーザーが独自のカスタムモデルを追加できるかどうか

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">allowedBaseUrls</span><span class="factory-rf-type">string[]</span></div>

カスタムモデルが接続を許可されるベース URL

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">allowAllFactoryModels</span><span class="factory-rf-type">boolean</span></div>

許可/ブロックリストに関係なく、すべての Factory ホストモデルを許可するかどうか

</div>
</Details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">userModelPolicies</span><span class="factory-rf-type">object</span></div>

ユーザーごとのモデルオーバーライド。ユーザー ID からポリシーオブジェクトへのマップ
  

<Details summary="properties">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">allowedModelIds</span><span class="factory-rf-type">string[]</span></div>

このユーザーが使用を許可されるモデル ID

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">blockedModelIds</span><span class="factory-rf-type">string[]</span></div>

このユーザーが使用をブロックされるモデル ID

</div>
</Details>



</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">enabledPlugins</span><span class="factory-rf-type">object</span></div>

`plugin@marketplace` 形式のプラグイン名から `true`（有効）または `false`（無効）へのマップ。`true` に設定されたプラグインは、マーケットプレイスが利用可能になるとCLI起動時に自動的にインストールされます。

</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">extraKnownMarketplaces</span><span class="factory-rf-type">object</span></div>

追加のプラグインマーケットプレイス。マーケットプレイス名からソースオブジェクトへのマップ。ここにリストされたマーケットプレイスは、CLI起動時に自動的にクローンされ、登録されます。
  

<details class="boris-details">
<summary>properties</summary>

<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">source</span><span class="factory-rf-type">object</span><span class="factory-rf-required">required</span></div>

マーケットプレイスソース — `source` フィールドで区別される以下の形式のいずれか：


<details class="boris-details">
<summary>github</summary>

<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">source</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

`"github"` である必要があります。

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">repo</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

`owner/repo` 形式のGitHubリポジトリ。

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">ref</span><span class="factory-rf-type">string</span></div>

追跡するGitブランチまたはタグ（例：`"main"`、`"v1.2.0"`）

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">sha</span><span class="factory-rf-type">string</span></div>

オプションの40文字フルコミットSHA。設定すると、マーケットプレイスはこの正確なコミットに固定されます。

</div>

</details>




<Details summary="url">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">source</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

`"url"` である必要があります。

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">url</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

マーケットプレイスのGitリポジトリURL（例：`https://gitlab.com/company/plugins.git`）

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">ref</span><span class="factory-rf-type">string</span></div>

追跡するオプションのGitブランチまたはタグ

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">sha</span><span class="factory-rf-type">string</span></div>

固定先となるオプションの40文字フルコミットSHA

</div>
</Details>




<Details summary="local">
<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">source</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

`"local"` である必要があります。

</div>




<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">path</span><span class="factory-rf-type">string</span><span class="factory-rf-required">required</span></div>

マーケットプレイスへのローカルファイルシステムパス。

</div>
</Details>



</div>

</details>



</div>





<div class="factory-response-field">

<div class="factory-response-field-meta"><span class="factory-rf-name">strictKnownMarketplaces</span><span class="factory-rf-type">object[]</span></div>

厳格に強制されるマーケットプレイスソース。各エントリは、`extraKnownMarketplaces` の値のように `source` キーでラップされるのではなく、ソースオブジェクトを直接記述します（例：`{ "source": "github", "repo": "owner/repo" }`）。

</div>



### サポートされているモデルID {#supported-model-ids}

以下のモデル識別子は `allowedModelIds` と `blockedModelIds` で使用できます：

| プロバイダー | モデルID |
|---|---|
| **Anthropic** | `claude-sonnet-4-5-20250929`, `claude-sonnet-4-6`, `claude-opus-4-5-20251101`, `claude-opus-4-6`, `claude-opus-4-6-fast`, `claude-opus-4-7`, `claude-haiku-4-5-20251001` |
| **OpenAI** | `gpt-5.1`, `gpt-5.1-codex`, `gpt-5.1-codex-max`, `gpt-5.2`, `gpt-5.3-codex` |
| **Google** | `gemini-3.5-flash`, `gemini-3-flash-preview`, `gemini-3.1-pro-preview` |
| **XAI** | `grok-code-fast-1` |
| **オープンソース** | `glm-5`, `glm-5.1`, `glm-5.2`, `kimi-k2.5`, `kimi-k2.6`, `minimax-m2.7` |

---

## 拡張のみのセマンティクス {#extensiononly-semantics}

Factoryは、従来の「上書き」動作ではなく、**拡張のみ**のセマンティクスを使用します。

- 上位レベル（組織、プロジェクト）は、下位レベルによって**上書きされません**。
- 下位レベル（フォルダー、ユーザー）は、それらのフィールドが未設定の場合にのみ、上位レベルで定義されたものに**追加**できます。
- これにより、プロジェクトやユーザーが体験をカスタマイズしても、組織のポリシーがそのまま維持されます。

データ型に応じて3つのマージモードがあります。

### 1. 単純な値 – 最初の値が優先 {#1-simple-values-first-wins}

単純なスカラー値（文字列、数値、ブール値）の場合：

- 値を設定した最初のレベルが「優先」されます。
- 下位レベルはその値を変更または削除できません。

例：

- `sessionDefaultSettings.model`
- `sessionDefaultSettings.autonomyMode`
- `maxAutonomyLevel`
- `subagentAutonomyLevel`

これにより、組織の決定（どのモデルや自律レベルが許可されているかなど）が権威を保持することが保証されます。

### 2. 配列 – 統合、削除不可 {#2-arrays-union-cannot-remove}

配列フィールドはレベル間で蓄積されます：

- 組織エントリは常に存在し、**削除できません**。
- プロジェクトとフォルダーレベルは、より多くのエントリを追加できます。
- ユーザーレベルはより多くのエントリを追加できますが、上位レベルのエントリを削除または弱体化できません。

例：

- コマンドの**許可リスト**と**拒否リスト**。
- 有効なフックや機能のリスト。

このパターンは「これらのコマンドは常に拒否される」や「これらのフックは常に有効」などのポリシーに適しており、チームがリストを拡張することも可能です。

### 3. オブジェクト – キーはレベルごとにロック {#3-objects-keys-are-locked-per-level}

オブジェクトフィールドの場合：

- 上位レベルで定義されたキーは**ロック**され、その内容は下位レベルで変更できません。
- 下位レベルは新しいキーを追加できますが、既存のキーを変更または削除はできません。

例：

- `customModels` – 組織が `claude-enterprise` を定義し、プロジェクトが `payments-gpt` を追加し、ユーザーが `personal-experimental` を追加できますが、誰も `claude-enterprise` を変更または削除できません。
- MCPサーバー定義 – 組織がどのサーバーが存在し、どのように接続するかを定義し、プロジェクトがどれを使用するかを決定します。

これにより、重要な設定（モデルエンドポイントやMCPサーバーなど）が一元管理下に置かれます。

---

## 組織設定 {#org-configuration}

大規模組織は通常、以下を行う**組織レベルの `.factory` バンドル**または設定エンドポイントを管理します：

- 許可されたモデル、ゲートウェイ、BYOKポリシーを指定。
- グローバルなコマンド許可/拒否リストを定義。
- 自律性、推論努力、Droid Shieldなどの安全機能のデフォルトを設定。
- OTELのデフォルト（エンドポイント、サンプリング、属性）を設定。
- 組織標準のドロイド、コマンド、フックを公開。

このバンドルは、Droidが動作するすべての環境（開発者マシン、CI、VM、エアギャップクラスター）に配布されます。

組織ポリシーが基盤であり、プロジェクトとユーザーはその上に構築します。

---

## プロジェクトとフォルダー設定 {#project-and-folder-configuration}

プロジェクトとフォルダーは、バージョン管理にチェックインされた `.factory/` ディレクトリを使用して、特定のコードベースやチームに対する組織ポリシーを専門化します。

一般的な責任は以下の通りです：

- 許可されたセット内でプロジェクト固有のモデルとゲートウェイを追加。
- プロジェクト固有のドロイド（例：`/migrate-service`、`/refactor-module`）を定義。
- プロジェクトのテスト、リンター、デプロイメントプロセスを認識するフックを設定。
- 高リスクリポジトリの安全制御を強化。

フォルダーレベルの `.factory/` ディレクトリは、異なるサブシステムが異なるポリシーを持つモノレポで有用です。

---

## ユーザー設定 {#user-configuration}

開発者は、上位レベルが設定されていない場合の**個人設定のみ**に対して `~/.factory/` を設定できます。

例：

- 許可されたセットから好みのモデルを選択。
- 表示オプションとマイナーなUX設定のデフォルト動作を設定。
- 組織ポリシーと競合しない追加のフックやツールを有効化。
拡張専用のセマンティクスのため、ユーザーは以下のことができません：

- 組織またはプロジェクト設定で禁止されたモデルやツールを再度有効にする。
- コマンドの許可/拒否リストを緩める。
- 組織またはプロジェクトで設定された自律性や安全要件を軽減する。

---

## 例：モデルポリシーの強制 {#example-enforcing-a-model-policy}

あなたの組織が以下を求めているとします：

- 承認されたエンタープライズモデルのみを許可する。
- ユーザー提供のAPIキーを禁止する。
- すべてのプロンプトを特定のLLMゲートウェイ経由で強制する。

この場合、以下を行います：

1. 組織の`.factory/settings.json`で許可されたモデルとゲートウェイエンドポイントを定義する。
2. ユーザーBYOKを完全に無効にするためのポリシーフラグを設定する。
3. モデル選択やエンドポイント使用が組織承認済みセットと一致することを検証するフックを構成する。

プロジェクトとユーザーは異なるタスクで**承認されたモデルのうちどれを**使用するかを選択できますが、これらの保証を破ることはできません。

---

## 例：環境固有の自律性 {#example-environmentspecific-autonomy}

以下を求める組織を考えてみましょう：

- CIおよびサンドボックスコンテナで高い自律性を許可する。
- 開発者のラップトップで自律性を制限する。

以下のようにできます：

1. 組織レベルで`maxAutonomyLevel`を`high`に設定する。
2. プロジェクト設定で、以下を行う環境対応フックを定義する：
   - 環境タグを検査する（例：`environment.type=local|ci|sandbox`）。
   - ラップトップで実行時に`medium`を超える自律性レベルをダウングレードまたはブロックする。
3. 特に機密性の高いリポジトリについては、オプションでより厳しいフォルダレベルのポリシーを定義する。

繰り返しますが、ユーザーはこれらのルールを上書きできません。許可された範囲内でより安全な個人デフォルトを選択することのみ可能です。

---

## 例：完全な組織管理設定 {#example-full-org-managed-settings}
```json
{
  "sessionDefaultSettings": {
    "model": "claude-sonnet-4-6",
    "reasoningEffort": "high",
    "interactionMode": "auto",
    "autonomyMode": "auto-medium",
    "specModeModel": "claude-opus-4-6",
    "specModeReasoningEffort": "medium"
  },
  "maxAutonomyLevel": "high",
  "builtInToolAutonomyOverrides": {
    "WebSearch": "high",
    "FetchUrl": "medium"
  },
  "subagentAutonomyLevel": "inherit",
  "cloudSessionSync": true,
  "includeCoAuthoredByDroid": true,
  "enableDroidShield": true,
  "ideAutoConnect": true,
  "commandAllowlist": ["npm *", "yarn *", "pnpm *", "make *"],
  "commandDenylist": ["rm -rf /", "sudo *"],
  "commandBlocklist": ["shutdown", "mkfs", "curl"],
  "allowManagedHooksOnly": true,
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Execute",
        "hooks": [
          {
            "type": "command",
            "command": "\"$FACTORY_PROJECT_DIR\"/.factory/hooks/audit-command.sh",
            "timeout": 30
          }
        ]
      }
    ]
  },
  "customModels": [
    {
      "model": "my-internal-model",
      "id": "custom:my-internal-model-v1",
      "index": 0,
      "baseUrl": "https://llm-gateway.internal.example.com/v1",
      "apiKey": "${INTERNAL_MODEL_API_KEY}",
      "provider": "generic-chat-completion-api",
      "displayName": "Internal Model v1",
      "maxContextLimit": 128000,
      "enableThinking": true,
      "thinkingMaxTokens": 8192,
      "maxOutputTokens": 16384,
      "extraHeaders": {
        "X-Team": "platform"
      },
      "extraArgs": {},
      "noImageSupport": false
    }
  ],
  "modelPolicy": {
    "allowedModelIds": ["claude-opus-4-6", "claude-sonnet-4-6", "gpt-5.3-codex"],
    "blockedModelIds": [],
    "allowCustomModels": true,
    "allowedBaseUrls": ["https://llm-gateway.internal.example.com/v1"],
    "allowAllFactoryModels": false
  },
  "disableWeeklyUsageSummary": false,
  "userModelPolicies": {
    "user-abc-123": {
      "allowedModelIds": ["claude-opus-4-6"],
      "blockedModelIds": []
    }
  },
  "enabledPlugins": {
    "my-org-plugin@internal-marketplace": true,
    "experimental-plugin@internal-marketplace": false
  },
  "extraKnownMarketplaces": {
    "internal-marketplace": {
      "source": {
        "source": "github",
        "repo": "my-org/factory-plugins"
      }
    }
  },
  "strictKnownMarketplaces": [
    {
      "source": "github",
      "repo": "my-org/factory-plugins"
    }
  ]
}
```
---

## 機能別のエンタープライズ制御 {#featurespecific-enterprise-controls}

一般的な階層に加えて、いくつかの機能には下位レベルをすべて上書きする専用の組織レベル切り替えがあります：

- **AutoWiki Cloud Sync** (`wikiCloudSync`) – AutoWiki コンテンツを Factory App に生成・保存できるかどうかを制御します。無効にすると、すべての wiki API エンドポイントがブロックされ、CLI は Factory App への保存と GitHub wiki 同期をスキップします。デフォルトで有効です。詳しくは [[jp/cli/features/wiki/overview#autowiki-cloud-sync|AutoWiki]] を参照してください。
- **Cloud Session Sync** (`cloudSessionSync`) – セッションデータを Factory cloud に同期するかどうかを制御します。
- **Hooks Policy** (`allowManagedHooksOnly`, `hooks`) – 組織管理者が組織管理フックを定義でき、「管理/プラグインフックのみ」を有効にすると、すべてのユーザーレベルおよびプロジェクトレベルのフックが解決時に破棄されます。組織管理フックは権威があり、メンバーがそれらを削除したり独自のフックを再導入したりすることはできません。[[jp/reference/hooks-reference#org-managed-hooks|組織管理フック]] を参照してください。
- **Built-in Tool Autonomy** (`builtInToolAutonomyOverrides`) – 組み込みネットワークツール（Web Search、Fetch URL）を確認プロンプトなしで実行するために必要な[[jp/cli/user-guides/auto-run|自律レベル]]を設定します。エントリのないツールはデフォルトで `low` になります。組織設定からのみ適用されるため、ユーザーおよびプロジェクトで弱めることはできません。

これらの制御は、[app.factory.ai](https://app.factory.ai) の **Enterprise Controls** セクションで組織管理者が管理します。

---

## すべてをまとめる {#putting-it-all-together}

階層設定システムは、他のエンタープライズページで説明されているすべての基盤となります：

- [[jp/enterprise/identity-and-access|アイデンティティ・アクセス管理]] – 誰がどのレベルの設定を変更できるか。
- [[jp/enterprise/privacy-and-data-flows|プライバシー、データフロー・ガバナンス]] – データとテレメトリがどこに送信を許可されるか。
- [[jp/enterprise/network-and-deployment|ネットワーク・デプロイメント設定]] – Droidが実行できる環境とその接続方法。
- [[jp/enterprise/llm-safety-and-agent-controls|LLM安全性・エージェント制御]] – コマンド、ツール、Droid Shieldのポリシー。
- [[jp/enterprise/models-llm-gateways-and-integrations|モデル、LLMゲートウェイ・統合]] – モデル、ゲートウェイ、MCPサーバー、ドロイド、コマンドの制御。
- [[jp/enterprise/compliance-audit-and-monitoring|コンプライアンス、監査・モニタリング]] – コンプライアンス証明に使用される保証とテレメトリ。

適切なレベルでポリシーを一度定義することで、**マシンごとの設定のずれや一回限りの設定なしに**、クラウド、ハイブリッド、エアギャップ環境でDroidを実行できます。
