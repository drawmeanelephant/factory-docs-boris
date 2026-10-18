---
id: jp/web/getting-started/quickstart
title: "クイックスタート"
status: published
summary: "Factory Appを5分で使い始める"
parent: jp/web/getting-started/index
tags: [web, quickstart, getting-started, factory-app, desktop-app, droid, factory-bridge, bridge]
relations: [relates_to=web/getting-started/quickstart]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">クイックスタート</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Factory Appを5分で使い始める</p>


## ステップ1: ダウンロードとインストール {#step-1-download-and-install}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Factory Appをダウンロード</div>

<div class="factory-card-group">

<div class="factory-card">

**[Mac (Apple Silicon)](https://app.factory.ai/api/desktop?platform=darwin&architecture=arm64)**

M1/M2/M3

</div>




<div class="factory-card">

**[Mac (Intel)](https://app.factory.ai/api/desktop?platform=darwin&architecture=x64)**

Intel

</div>




<div class="factory-card">

**[Windows (x64)](https://app.factory.ai/api/desktop?platform=win32)**

Windows x64

</div>




<div class="factory-card">

**[Windows (ARM64)](https://app.factory.ai/api/desktop?platform=win32&architecture=arm64)**

Windows ARM64

</div>

</div>

</div>



  

<div class="factory-step">

<div class="factory-step-title">インストール</div>

- **Mac**: `.dmg`ファイルを開き、Factory AppをApplicationsにドラッグします
  - **Windows**: インストーラーを実行します

</div>



  

<div class="factory-step">

<div class="factory-step-title">サインイン</div>

Factory Appを起動し、アカウントでサインインします。

</div>

</div>



## ステップ2: コードベースに接続 {#step-2-connect-to-your-codebase}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">作業ディレクトリを設定</div>

作業ディレクトリをプロジェクトフォルダに設定します。Factory Appはローカルマシンに直接接続します。

</div>



  

<div class="factory-step">

<div class="factory-step-title">モデルを選択</div>

モデルセレクターから使用するAIモデルを選択します。これはいつでも変更できます。

</div>

</div>



## ステップ3: 構築を開始 {#step-3-start-building}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Droidに何でも質問</div>

まずは簡単なことから始めます:

```
Analyze this codebase and explain the architecture
```

またはすぐにコーディングを始めます:

```
Add error handling to the user authentication flow
```

Droidはコードベースを分析し、変更を提案し、適用前に何が変更されるかを正確に表示します。

</div>

</div>



## ワークフローの例 {#example-workflows}

### 機能開発 {#feature-development}
```
Implement a dark mode toggle following our existing theme patterns
```

### バグ修正 {#bug-fixing}
```
Fix the authentication timeout issue where users get logged out after 5 minutes
```

### コードレビュー {#code-review}
```
Review this PR and suggest improvements for error handling and edge cases
```

### セキュリティ監査 {#security-audit}
```
Audit this codebase for security vulnerabilities and create a remediation plan
```

## ヒント {#tips}

- **具体的に記述する**: ファイル名、エラーメッセージ、チケット番号などの関連する詳細を含める
- **コンテキストを活用する**: '@'メンションでチームツールを参照するか、リンクを直接貼り付ける
- **変更を確認する**: 承認前にDroidが提案した変更を必ず確認する

## 次のステップ {#next-steps}



<div class="factory-card-group">

<div class="factory-card">

**[[jp/integrations/linear|インテグレーション]]**

Slack、Linear、その他のツールを接続する

</div>


  

<div class="factory-card">

**[[jp/cli/getting-started/overview|CLI]]**

ターミナルからDroidを使用する

</div>

</div>
