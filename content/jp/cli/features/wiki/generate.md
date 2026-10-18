---
id: jp/cli/features/wiki/generate
title: "Wikiを生成する"
status: published
summary: "/wiki コマンドを使って、Droid CLI からAutoWikiの包括的なコードベースドキュメントを生成します。"
parent: jp/cli/features/wiki/index
tags: [cli, wiki, generate, documentation, codebase-docs, slash-command, upload, github-wiki-sync]
relations: [relates_to=cli/features/wiki/generate]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Wikiを生成する</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">/wiki コマンドを使って、Droid CLI からAutoWikiの包括的なコードベースドキュメントを生成します。</p>


`/wiki` コマンドはリポジトリを解析し、アーキテクチャ、モジュール、API、規約をカバーする構造化Wikiを生成します。Cloud Sync により、生成されたWikiはFactory Appに保存され、必要に応じて GitHub wiki タブにも同期されます。

## クイックスタート {#quick-start}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">リポジトリで Droid セッションを開く</div>

プロジェクトディレクトリに移動して Droid を開始します：
```bash
cd /path/to/your/project
droid
```

</div>


  

<div class="factory-step">

<div class="factory-step-title">wiki コマンドを実行する</div>

```
> /wiki
```
Droid はコードベースを解析し、プロジェクトディレクトリ内のローカル `droid-wiki/` フォルダに Markdown ファイルを生成します。生成が完了すると、Cloud Sync により内容をFactory Appに保存します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">結果を確認する</div>

アップロードが完了すると、Droid は wiki へのリンクを表示します：
```
Wiki uploaded successfully: https://app.factory.ai/wiki/{wikiRunId}
```
リンクを開いてドキュメントを閲覧するか、
[app.factory.ai/wiki](https://app.factory.ai/wiki) にアクセスして
すべての wiki を確認してください。

</div>

</div>



## 生成中に行われること {#what-happens-during-generation}

`/wiki` を実行すると、Droid は次の手順を実行します：

1. **コードベース解析** -- ソースファイル、設定、テスト、ドキュメントを読み取り、プロジェクト構造を把握します
2. **ページ生成** -- トピックごと（アーキテクチャ、モジュール、API、セットアップなど）に整理された Markdown ファイル群を生成します
3. **視覚的スクリーンショット** -- リポジトリに [[jp/guides/skills/automated-qa|QAスキル]] がインストールされている場合、Droid はアプリケーションを起動し、wiki に含める Web UI と TUI のスクリーンショットを取得します。まだ設定していない場合は `/install-qa` を実行して追加してください。
4. **Cloud Sync** -- ページと画像をFactory Appに保存します
5. **GitHub wiki sync** -- GitHub リポジトリでは、ページをフラット化してリポジトリの wiki タブへ push します



<Aside kind="note">
wiki の生成には、現在のブランチと作業ディレクトリの状態が使われます。最も正確なドキュメントにするには、デフォルトブランチのクリーンな checkout から `/wiki` を実行してください。
</Aside>





<Aside kind="tip">
リポジトリで最初の wiki 生成には時間がかかる場合があります。Droid はコードベース全体を一から解析する必要があるためです。2 回目以降は incremental mode を使い、前回の生成以降にコード変更の影響を受けたページだけを更新するため、かなり高速になります。
</Aside>



## GitHub wiki sync {#github-wiki-sync}

Cloud Sync でWikiがFactory Appに保存された後、Droid CLI は GitHub でホストされているリポジトリについて、生成されたWikiを GitHub の組み込み wiki タブへ自動同期します。この同期では次のことを行います：

<img src="../../../../images/wiki/github-wiki-sync.png" alt="GitHub Wikiに同期されたAutoWikiコンテンツ" />

- 階層型のページツリーを GitHub のフラットな wiki 形式に変換します（例：`overview/architecture.md` は `overview--architecture.md` になります）
- 内部リンクを書き換えてフラットなファイル名を使うようにします
- ナビゲーション可能な目次として `_Sidebar.md` を生成します
- wiki のルートページから `Home.md` を生成します
- `{repo}.wiki.git` を clone し、すべての内容を置き換えて push します

### GitHub 同期の前提条件 {#prerequisites-for-github-sync}

- リポジトリが GitHub でホストされていること
- wiki タブが初期化されていること（まだ使ったことがない場合は、`https://github.com/{owner}/{repo}/wiki` で最初のページを作成してください）
- Git の認証情報に wiki リポジトリへの push 権限があること
- 組織で [[jp/cli/features/wiki/overview#autowiki-cloud-sync|AutoWiki Cloud Sync]] が無効化されていないこと

wiki が初期化されていない場合、CLI は最初のページ作成用リンクを含むメッセージを表示し、失敗扱いにせず同期をスキップします。

## バージョン管理 {#versioning}

wiki を生成するたびに、次のメタデータを含む新しい **Wiki Run** が作成されます：

- コミットハッシュとブランチ名
- ローカルに未コミットの変更があったかどうか
- 使用した Droid CLI バージョン
- タイムスタンプ

過去のバージョンは、[[jp/cli/features/wiki/web-viewer|Factory App内のAutoWikiページ]] のバージョンドロップダウンから参照できます。

## 関連情報 {#see-also}

- [[jp/cli/features/wiki/auto-refresh|AutoWiki Refreshを設定する]] -- CI アクションでWikiを最新の状態に保つ
- [[jp/cli/features/wiki/web-viewer|Wikiを閲覧する]] -- Factory Appから閲覧、検索、エクスポートを行う
- [[jp/cli/features/wiki/overview|AutoWiki の概要]] -- 各要素がどのように連携するか
