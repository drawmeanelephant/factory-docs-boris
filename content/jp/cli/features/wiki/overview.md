---
id: jp/cli/features/wiki/overview
title: "AutoWiki"
status: published
summary: "AutoWikiは、リポジトリ向けに包括的で構造化されたWikiを生成します。"
parent: jp/cli/features/wiki/index
tags: [cli, autowiki, wiki, documentation, codebase, install-wiki, github-wiki, auto-refresh]
relations: [relates_to=cli/features/wiki/overview]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">AutoWiki</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">AutoWikiは、リポジトリ向けに包括的で構造化されたWikiを生成します。</p>


AutoWiki は、リポジトリ向けの包括的で構造化されたWikiを生成します。コードベースを解析し、アーキテクチャの概要、モジュールの内訳、相互リンクされたページを備えた閲覧可能なドキュメントを作成し、コードの変更に合わせて各Wikiの内容を最新に保ちます。

<img src="../../../../images/wiki/autowiki-list.png" alt="Factory App内のAutoWikiリポジトリ概要" />



<div class="factory-card-group">

<div class="factory-card">

**[[jp/cli/features/wiki/generate|生成]]**

Droid CLIで `/wiki` を実行して、任意のリポジトリからWikiを生成します

</div>


  

<div class="factory-card">

**[[jp/cli/features/wiki/auto-refresh|自動更新]]**

`/install-wiki` を実行して、push ごとにAutoWikiを更新します

</div>


  

<div class="factory-card">

**[[jp/cli/features/wiki/web-viewer|閲覧]]**

Factory AppでWikiを閲覧、検索、エクスポートできます

</div>

</div>



## 仕組み {#how-it-works}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">CLI から生成する</div>

Droid セッション内で `/wiki` を実行します。Droid はコードベースを解析し、アーキテクチャ、モジュール、API、規約をカバーする構造化されたMarkdownページ群を生成します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">Factory Appに保存する</div>

Cloud Sync により、生成されたWikiはFactory Appに保存され、
[app.factory.ai/wiki](https://app.factory.ai/wiki) で閲覧できるようになります。各アップロードにはバージョンが付き、時間の経過とともに変更を比較できます。

</div>


  

<div class="factory-step">

<div class="factory-step-title">GitHub wiki に同期する</div>

GitHub でホストされているリポジトリでは、AutoWiki が生成したWikiをリポジトリの組み込みwikiタブへ任意で push できます。内部リンクは書き換えられ、サイドバーが生成され、内容が `{repo}.wiki.git` に push されます。

</div>


  

<div class="factory-step">

<div class="factory-step-title">最新状態を保つ</div>

`/install-wiki` を実行すると、デフォルトブランチへの push ごとにWikiを再生成する CI ワークフロー（GitHub Actions または GitLab CI）が作成されます。必要に応じてFactory Appからいつでも更新をトリガーすることもできます。

</div>

</div>



## GitHub wiki sync {#github-wiki-sync}

GitHub でホストされているリポジトリでAutoWikiがWikiを生成すると、Factory は必要に応じてその内容を GitHub の組み込み wiki タブにも同期します。これにより、チームはFactory Appを開かなくてもリポジトリページから直接Wikiを閲覧できます。同期の仕組みの詳細は [[jp/cli/features/wiki/generate#github-wiki-sync|Wikiを生成する]] を参照してください。

<img src="../../../../images/wiki/github-wiki-sync.png" alt="GitHub Wikiに同期されたAutoWikiコンテンツ" />



<Aside kind="note">
Factory が同期する前に、GitHub 側で wiki を初期化しておく必要があります。まだ wiki タブを使ったことがない場合は、`https://github.com/{owner}/{repo}/wiki` で最初のページを手動で作成し、その後 `/wiki` を再実行してください。
</Aside>



## エンタープライズ制御 {#enterprise-controls}

### AutoWiki Cloud Sync {#autowiki-cloud-sync}

AutoWiki コンテンツをFactory Appに保存させたくない組織は、**AutoWiki Cloud Sync** を無効化できます。これは [app.factory.ai](https://app.factory.ai) の **Settings > Enterprise Controls** で利用できる組織レベルのエンタープライズ制御です。

<img src="../../../../images/wiki/autowiki-enterprise-controls.png" alt="Factory設定のAutoWiki Cloud Syncエンタープライズ制御" />

**AutoWiki Cloud Sync** が **無効** の場合：

- すべてのAutoWiki APIエンドポイントが組織に対して 403 を返します
- `/wiki` コマンドはコンテンツをFactory Appに保存しません
- CLI からの GitHub wiki 同期もスキップされます
- Factory App内のAutoWikiページにはコンテンツが表示されません

**AutoWiki Cloud Sync** は **デフォルトで有効** です。この設定を切り替えられるのは org manager のみです。

エンタープライズ制御の動作全体については、[[jp/enterprise/hierarchical-settings-and-org-control|階層設定と組織制御]] を参照してください。

## 次のステップ {#whats-next}



<div class="factory-card-group">

<div class="factory-card">

**[[jp/cli/features/wiki/generate|Wikiを生成する]]**

初めてのAutoWikiを生成するためのステップバイステップガイド

</div>


  

<div class="factory-card">

**[[jp/cli/features/wiki/auto-refresh|AutoWiki Refreshを設定する]]**

AutoWikiを最新状態に保つ CI アクションをインストールします

</div>


  

<div class="factory-card">

**[[jp/cli/features/wiki/web-viewer|Factory Appで閲覧する]]**

Wikiドキュメントを検索、閲覧、エクスポートします

</div>


  

<div class="factory-card">

**[[jp/enterprise/hierarchical-settings-and-org-control|エンタープライズ設定]]**

組織レベルの制御がAutoWikiや他の機能をどう統制するかを学びます

</div>

</div>
