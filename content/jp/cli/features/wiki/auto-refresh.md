---
id: jp/cli/features/wiki/auto-refresh
title: "AutoWiki Refresh"
status: published
summary: "/install-wiki を使って、デフォルトブランチへの push ごとにAutoWikiを再生成する CI アクションを設定します。"
parent: jp/cli/features/wiki/index
tags: [cli, wiki, install-wiki, auto-refresh, github-actions, gitlab-ci, ci, recurring]
relations: [relates_to=cli/features/wiki/auto-refresh]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">AutoWiki Refresh</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">/install-wiki を使って、デフォルトブランチへの push ごとにAutoWikiを再生成する CI アクションを設定します。</p>


`/install-wiki` コマンドは、デフォルトブランチにコードが push されるたびにWikiを自動的に再生成する CI ワークフローを作成します。CI フレームワーク（GitHub Actions または GitLab CI）を検出し、適切な設定を生成します。これにより、手動の介入なしでAutoWikiをコードベースと同期した状態に保てます。

## クイックスタート {#quick-start}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">リポジトリで Droid セッションを開く</div>

```bash
cd /path/to/your/project
droid
```

</div>


  

<div class="factory-step">

<div class="factory-step-title">インストールコマンドを実行する</div>

```
> /install-wiki
```
Droid はワークフローファイルを作成し、レビュー用の PR を開きます。

</div>


  

<div class="factory-step">

<div class="factory-step-title">Factory API キーを追加する</div>

CI 設定で `FACTORY_API_KEY` をシークレットとして追加します：
  - **GitHub**: リポジトリの **Settings > Secrets and variables > Actions**（または組織レベルの **Organization Settings > Secrets and variables > Actions**）
  - **GitLab**: リポジトリの **Settings > CI/CD > Variables**（またはグループレベルの **Group Settings > CI/CD > Variables**）

キーは [app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys) で生成できます。

</div>


  

<div class="factory-step">

<div class="factory-step-title">PR をマージする</div>

シークレットを設定したら、ワークフローの PR をマージします。これで、デフォルトブランチへの push ごとに wiki が自動更新されます。

</div>

</div>



## 生成されるワークフロー {#generated-workflows}

Droid は CI フレームワークを検出し、適切な設定を作成します。

### GitHub Actions {#github-actions}

`.github/workflows/droid-wiki-refresh.yml` を作成します（異なる場合は `main` をデフォルトブランチ名に置き換えてください）：

```yaml
name: Droid AutoWiki Refresh

on:
  push:
    branches: [main] # change to your default branch if not main

jobs:
  wiki-refresh:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Factory Droid
        run: curl -fsSL https://app.factory.ai/cli | sh

      - name: Generate wiki
        run: droid exec --auto high "/wiki"
        env:
          FACTORY_API_KEY: ${{ secrets.FACTORY_API_KEY }}
```

### GitLab CI {#gitlab-ci}

既存の `.gitlab-ci.yml` にジョブを追記します：

```yaml
droid-wiki-refresh:
  stage: deploy
  before_script:
    - curl -fsSL https://app.factory.ai/cli | sh
  script:
    - droid exec --auto high "/wiki"
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  variables:
    FACTORY_API_KEY: $FACTORY_API_KEY
```

どちらのワークフローも以下を行います：

- デフォルトブランチへの **push をトリガー** にする
- 公式インストーラーで **Droid CLI をインストール** する
- 高い自律性の headless モードで **`/wiki` を実行** し、Wikiを生成してFactory AppにCloud Syncで保存する



<Aside kind="tip">
インストール後にワークフローをカスタマイズすることもできます。たとえば、トリガーブランチを変更したり、ソースファイルが変わった時だけ再生成するようにパスフィルターを追加したり、タイムアウトを調整したりできます。
</Aside>



## 前提条件 {#prerequisites}

- GitHub または GitLab でホストされているリポジトリ
- Factory API キー（[app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys) で生成）
- 対象リポジトリでシークレットを追加し、PR をマージする権限

## Web から更新する {#refreshing-from-the-factory-app}

Factory Appから定期更新を設定することもできます：

1. [app.factory.ai/wiki](https://app.factory.ai/wiki) に移動する
2. AutoWikiページで **Refresh** をクリックする
3. **Recurring (on push)** を選択する
4. **Local** または **Cloud** の方法を選ぶ：
   - **Local** -- ローカル clone で実行するための `/install-wiki` コマンドをコピーします
   - **Cloud** -- セットアップをリモート実行する cloud template または Droid Computer を選択します

複数のリポジトリをまとめて操作する場合、Factory App では複数の repo を選択し、1 回の操作で Droid Computer 上でセットアップを実行できます。

Factory Appインターフェースの詳細は [[jp/cli/features/wiki/web-viewer|Factory App内のAutoWiki]] を参照してください。

## トラブルシューティング {#troubleshooting}





<Details summary="認証エラーでワークフローが失敗する">
リポジトリの **Settings > Secrets and variables > Actions** に
`FACTORY_API_KEY` シークレットが正しく設定されていることを確認してください。必要に応じて、
[app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys)
で新しいキーを生成してください。
</Details>



  

<Details summary="push 後にAutoWikiが更新されない">
`.github/workflows/droid-wiki-refresh.yml` にワークフローファイルが存在し、
ブランチトリガーがデフォルトブランチと一致していることを確認してください。ワークフロー実行ログは
リポジトリの Actions タブで確認できます。
</Details>



  

<Details summary="GitHub wiki が同期されない">
Factory が push する前に GitHub wiki タブを初期化しておく必要があります。
`https://github.com/{owner}/{repo}/wiki` で最初のページを手動で作成してください。あわせて、
組織で [[jp/cli/features/wiki/overview#autowiki-cloud-sync|AutoWiki Cloud Sync]] が無効化されていないことも確認してください。
</Details>





## 関連情報 {#see-also}

- [[jp/cli/features/wiki/generate|Wikiを生成する]] -- `/wiki` を使った一度きりのAutoWiki生成
- [[jp/cli/features/wiki/web-viewer|Wikiを閲覧する]] -- Factory Appから閲覧と検索を行う
- [[jp/guides/droid-exec/code-review|自動コードレビュー]] -- コードレビュー自動化向けの類似ワークフロー
- [[jp/cli/droid-exec/overview|Droid Exec]] -- 生成されたワークフローで使用される headless モード
