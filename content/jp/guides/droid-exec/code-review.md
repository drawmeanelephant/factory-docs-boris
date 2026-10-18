---
id: jp/guides/droid-exec/code-review
title: "自動コードレビュー"
status: published
summary: "Droidによる自動プルリクエストとマージリクエストレビューの設定"
parent: jp/guides/droid-exec/index
tags: [guides, code-review, pr-review, pull-request, github-actions, automation, droid-exec, github-app]
relations: [relates_to=guides/droid-exec/code-review]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">自動コードレビュー</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Droidによる自動プルリクエストとマージリクエストレビューの設定</p>


GitHubまたはGitLabリポジトリの自動コードレビューを設定します。Droidがプルリクエストとマージリクエストを分析し、問題を特定して、インラインコメントとしてフィードバックを投稿します。GitHubリポジトリでは、セットアップフローがレビュー自動化の設定の一部としてFactory Droid GitHub Appのインストールを確認します。

<div style="display:flex; gap:1rem; flex-wrap:wrap">
  <div style="flex:1; min-width:300px">
    <img src="../../../guides/droid-exec/code-review-picture-1.png" alt="見つかった問題を含むコードレビューサマリーを投稿するFactory Droidボット" />
  </div>
  <div style="flex:1; min-width:300px">
    <img src="../../../guides/droid-exec/code-review-picture-2.png" alt="特定の行にインラインコードレビューコメントを投稿するFactory Droidボット" />
  </div>
</div>

## セットアップ {#setup}

GitHubまたはGitLabの自動コードレビューを設定するには、`/install-code-review`コマンドを使用します：
```bash
droid
> /install-code-review
```
ガイド付きフローでは以下を行います：
1. SCMプラットフォーム（GitHubまたはGitLab）を検出
2. 前提条件（CLIツール、権限）を確認
3. レビュー設定（深度、セキュリティ、トリガー）の設定をガイド
4. ワークフローファイルとともにPR/MRを作成

## 動作の仕組み {#how-it-works}

有効化すると、Droid Reviewワークフローは：

1. プルリクエストイベント（開始、同期、再開、レビュー準備完了）でトリガー
2. 開発中のノイズを避けるため下書きPRをスキップ
3. PR差分と既存のコメントを取得
4. バグ、セキュリティ問題、正確性の問題についてコード変更を分析
5. 問題のある行にインラインコメントを投稿
6. 問題が見つからない場合は承認を送信

## 認証 {#authentication}

自動レビューには、Droidを実行する権限と、プルリクエストに投稿する権限という、2種類の別々のアクセスが必要です。これらはそれぞれ独立して設定します。

### 1. Factory API key（Droidを実行） {#1-factory-api-key-run-droid}

DroidはFactory API keyを使用して実行されます。[app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys)でキーを作成し、`FACTORY_API_KEY`という名前のシークレットとしてリポジトリまたは組織に追加してください。ワークフローでは次のように渡します：

```yaml
- uses: Factory-AI/droid-action@main
  with:
    factory_api_key: ${{ secrets.FACTORY_API_KEY }}
```

これはすべての実行で必須です。

### 2. GitHub access（レビューを投稿） {#2-github-access-post-reviews}

PRにコメントや承認を残すには、DroidにGitHub tokenが必要です。指定方法は2つあります：

- **Factory Droid GitHub App（デフォルト、推奨）**。tokenを指定しない場合、actionはインストール済みのFactory Droid GitHub App用のtokenを安全に要求します。ほとんどのチームではこれだけで十分です。[app.factory.ai/settings/organization](https://app.factory.ai/settings/organization)から対象のリポジトリにAppをインストールすれば完了です。actionがtokenを要求できるように、`id-token: write` 権限が必要です：

  ```yaml
  permissions:
    contents: write
    pull-requests: write
    issues: write
    id-token: write # GitHub App認証に必須
  ```

- **独自のtoken（オーバーライド）**。GitHub Enterpriseで利用する場合や、どのアカウントでコメントを投稿するかを制御したい場合など、personal access tokenや独自のGitHub Appを使いたいなら、`github_token`として渡します。設定すると、Droidはそのtokenを直接使用し、Appはスキップされます。このtokenにはpull requestとrepository contentsへの書き込み権限が必要です。

  ```yaml
  - uses: Factory-AI/droid-action@main
    with:
      factory_api_key: ${{ secrets.FACTORY_API_KEY }}
      github_token: ${{ secrets.MY_GITHUB_TOKEN }}
  ```



<Aside kind="note">
GitLabでも必要な要素は同じです。`FACTORY_API_KEY`と`GITLAB_TOKEN`をCI/CD変数として設定してください。`/install-code-review`フローが両方を設定します。
</Aside>



GitHub Appのセキュリティアーキテクチャについては、[[jp/enterprise/github-integration-security|GitHub統合セキュリティ]]を参照してください。

## レビューの深度 {#review-depth}

`review_depth` 入力は各レビューの徹底さとコストを制御します。`/install-code-review` セットアップ時に深度を選択するか、ワークフローで直接設定します。

- **`deep`**（デフォルト） — より高い推論努力による徹底的な分析。より微妙なバグを捉えますが、レビューあたりのコストが高くなります。本番コードやセキュリティ重要なリポジトリに最適。
- **`shallow`** — 表面的な問題をカバーする、より高速でコスト効率の良いレビュー。大量リポジトリ、下書きPR、または支出を監視するチームに適しています。
```yaml
with:
  automatic_review: true
  review_depth: deep  # or shallow
```
`review_model` と `reasoning_effort` を使用してモデルや推論の強度を直接オーバーライドすることもでき、これらは深度プリセットよりも優先されます。

## セキュリティレビュー {#security-review}

セキュリティレビューは、STRIDE、OWASP、OWASP LLM Top 10、およびサプライチェーン分析のための専用ワークフローです。自動 PR セキュリティレビュー、スケジュールスキャン、組み込みの `security-review` スキルによるローカルのコードベース全体監査については、[[jp/enterprise/security-review|セキュリティレビュー]]を参照してください。

## Droidがレビューする内容 {#what-droid-reviews}

自動レビューアーは明確なバグと問題に焦点を当てます：

- デッド/到達不能コード
- 制御フローの破綻（`break`の欠如、フォールスルーバグ）
- async/awaitの間違い
- null/undefined参照
- リソースリーク
- SQL/XSSインジェクション脆弱性
- エラーハンドリングの欠如
- オフバイワンエラー
- 競合状態

スタイルの問題、軽微な最適化、アーキテクチャの意見はスキップします。

## ワークフローのカスタマイズ {#customizing-the-workflow}

ワークフローが作成された後、リポジトリの`.github/workflows/droid-review.yml`を編集してカスタマイズできます。

### トリガー条件の変更 {#change-the-trigger-conditions}

レビューが実行されるタイミングを変更：
```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened, ready_for_review]
    paths:
      - 'src/**'  # Only review changes in src/
      - '!**/*.test.ts'  # Skip test files
```
### カスタムレビューガイドライン {#custom-review-guidelines}

リポジトリ固有のレビューガイドラインを追加するには、リポジトリ内に`.factory/skills/review-guidelines/SKILL.md`ファイルを作成します：
```markdown
<!-- .factory/skills/review-guidelines/SKILL.md -->

Additional checks for this codebase:
- React hooks rules violations
- Missing TypeScript types on public APIs
- Prisma query performance issues
```
これらのガイドラインは自動的に取得され、すべてのレビュー実行に注入されます。ワークフローの変更は必要ありません。

### モデルを変更する {#change-the-model}

レビューに異なるモデルを使用する：
```yaml
droid exec --auto high --model claude-sonnet-4-5-20250929 -f prompt.txt
# Or use a faster model for quicker feedback:
droid exec --auto high --model claude-haiku-4-5-20251001 -f prompt.txt
```
### 特定のPRをスキップする {#skip-certain-prs}

特定のケースでレビューをスキップするための条件を追加する：
```yaml
jobs:
  code-review:
    # Skip bot PRs and PRs with [skip-review] in title
    if: |
      github.event.pull_request.draft == false &&
      !contains(github.event.pull_request.user.login, '[bot]') &&
      !contains(github.event.pull_request.title, '[skip-review]')
```
### コメント数を制限する {#limit-comment-count}

プロンプト内のコメントの最大数を調整します：
```
Guidelines:
- Submit at most 5 comments total, prioritizing the most critical issues
```
## すべてのワークフロー入力 {#all-workflow-inputs}

| 入力 | デフォルト | 説明 |
|-------|---------|-------------|
| `automatic_review` | `false` | `@droid review`なしでPRを自動的にレビューする |
| `review_depth` | `deep` | レビュープリセット: `deep`（徹底的） または `shallow`（高速） |
| `review_model` | (depthから) | コードレビュー用のモデルをオーバーライド |
| `reasoning_effort` | (depthから) | 推論努力をオーバーライド |
| `include_suggestions` | `true` | コメントにコード提案ブロックを含める |

セキュリティレビュー関連の入力は[[jp/enterprise/security-review#configuration|セキュリティレビュー]]に記載しています。

## 関連項目 {#see-also}

- [[jp/enterprise/security-review|セキュリティレビュー]] - セキュリティ重視の PR レビューとコードベース全体の監査
- [[jp/enterprise/github-integration-security|GitHub統合セキュリティ]] - GitHub App統合のセキュリティアーキテクチャ
- [[jp/guides/droid-exec/github-actions|GitHub Actionsの例]] - その他の自動化ワークフロー
- [[jp/cli/droid-exec/overview|Droid Exec]] - CI/CD環境でのDroid実行
