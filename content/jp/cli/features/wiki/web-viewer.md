---
id: jp/cli/features/wiki/web-viewer
title: "Factory App内のAutoWiki"
status: published
summary: "Factory Appから、生成したWikiを閲覧、検索、管理します。"
parent: jp/cli/features/wiki/index
tags: [cli, wiki, web, viewer, browse, search, refresh, export]
relations: [relates_to=cli/features/wiki/web-viewer]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Factory App内のAutoWiki</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Factory Appから、生成したWikiを閲覧、検索、管理します。</p>


[app.factory.ai/wiki](https://app.factory.ai/wiki) のFactory App内にあるAutoWikiビューでは、すべてのリポジトリで生成されたAIドキュメントを1か所で閲覧、検索、管理できます。

## 表示される内容 {#what-youll-see}

トップレベルのWikiビューには、生成済みの各リポジトリWikiが表示され、鮮度インジケーターと、ドキュメントの検索、フィルタリング、更新のための操作が用意されています。

<img src="../../../../images/wiki/autowiki-list.png" alt="Factory App内のAutoWikiリポジトリ一覧" />

リポジトリを開くと、ナビゲーション、ページアウトライン、検索、エクスポート、更新操作とともに生成ページを閲覧できます。

<img src="../../../../images/wiki/autowiki-reader.png" alt="生成されたアーキテクチャドキュメントを表示するAutoWiki reader" />

GitHub Wiki syncが有効な場合、同じ生成ページをリポジトリのGitHub Wikiタブからも利用できます。

<img src="../../../../images/wiki/github-wiki-sync.png" alt="GitHub Wikiに同期されたAutoWikiコンテンツ" />

## wiki の閲覧 {#browsing-your-wikis}

メインのAutoWikiページには、Wikiが生成済みのリポジトリ一覧が表で表示されます。各行にはリポジトリ名、最終更新日、ブランチが表示されます。リポジトリをクリックすると、そのWikiが開きます。

### Wiki Reader {#wiki-reader}

Wiki Readerでは次の機能を利用できます：

- **Markdown レンダリング** -- 構文ハイライト付きコードブロックを含む、生成ドキュメントの高忠実度な表示
- **目次** -- 現在のページをすばやく移動するためのサイドバーアウトライン
- **パンくずリスト** -- ページツリー内の現在位置を示す階層ナビゲーション
- **検索** -- wiki 内の全ページを対象にした全文検索
- **バージョン履歴** -- 過去の wiki 生成を参照し、ドキュメントの変化を比較できるドロップダウン
- **エクスポート** -- wiki を Markdown ファイルとしてダウンロード

## Wikiを更新する {#refreshing-a-wiki}

Wikiページの **Refresh** ボタンをクリックすると、ドキュメントを再生成できます。モーダルには 2 つのオプションが表示されます：



<div class="factory-card-group">

<div class="factory-card">

**一度だけ更新**

デフォルトブランチ上の最新コードを使って wiki を 1 回だけ再生成します。

</div>


  

<div class="factory-card">

**定期更新（push ごと）**

デフォルトブランチへの push ごとに wiki を更新する CI アクションをインストールします。

</div>

</div>



モードを選んだ後、生成の実行方法を選択します：

| 方法 | 説明 |
|--------|-------------|
| **Local** | ローカルの Droid セッションに貼り付けられるよう、CLI コマンド（`/wiki` または `/install-wiki`）をコピーします |
| **Cloud** | リポジトリに紐付いた cloud template 上で生成を実行します |

### 一括更新 {#batch-refresh}

[app.factory.ai/wiki](https://app.factory.ai/wiki) のトップレベルAutoWikiページから、複数のリポジトリを一度に更新することもできます：

1. **Refresh** をクリックして選択モードに入る
2. 更新したいリポジトリを選択する
3. **One-time** または **Recurring** を選択する
4. 実行先の **Droid Computer** を選択する

<img src="../../../../images/wiki/autowiki-batch-refresh.png" alt="AutoWikiの一括更新選択モード" />

Droid は選択したコンピュータ上で各リポジトリを clone し、可能な範囲で並列に wiki を生成します（または定期生成のセットアップを行います）。

## 関連情報 {#see-also}

- [[jp/cli/features/wiki/generate|Wikiを生成する]] -- CLI で `/wiki` を使ってAutoWikiを生成する
- [[jp/cli/features/wiki/auto-refresh|AutoWiki Refreshを設定する]] -- CI アクションでWikiを最新状態に保つ
- [[jp/cli/features/wiki/overview|AutoWiki の概要]] -- 各要素がどのように連携するか
