---
id: jp/cli/account/droid-shield
title: "Droid Shield"
status: published
summary: "git commitやpushで認証情報が誤って公開されるのを防ぐ自動シークレット検出。"
parent: jp/cli/account/index
tags: [cli, droid-shield, secrets, credentials, api-keys, detection, security]
relations: [relates_to=cli/account/droid-shield]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Droid Shield</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">git commitやpushで認証情報が誤って公開されるのを防ぐ自動シークレット検出。</p>


## Droid Shieldとは？ {#what-is-droid-shield}

Droid Shieldは、コミットしてリモートにプッシュする前に、未コミットの変更を自動的にスキャンして潜在的なシークレットを検出する組み込みセキュリティ機能です。APIキー、トークン、パスワードなどの機密認証情報がバージョン管理履歴に誤って公開されることを防ぐセーフティネットとして機能します。



<Aside kind="tip">
**高度な保護をお探しですか？** [[jp/cli/account/droid-shield-plus|Droid Shield Plus]]は、プロンプトインジェクション検出、強化されたシークレット検出、機密データ保護を備えたAI搭載セキュリティスキャンを提供します。エンタープライズのお客様が利用できます。
</Aside>



---

## Droid Shieldの動作原理 {#how-droid-shield-works}

Droidを使用して`git commit`または`git push`操作を実行すると、Droid Shieldは自動的に以下を行います：

1. **差分をスキャン** - 追加される行のみを分析（削除や変更されていない行は対象外）
2. **シークレットを検出** - パターンマッチングを使用して潜在的な認証情報を識別
3. **実行をブロック** - シークレットが検出された場合、git操作を停止
4. **検出結果を報告** - 潜在的なシークレットが見つかった正確な場所を表示



<Aside kind="note">
Droid ShieldはDroid経由で実行されたgit操作のみをスキャンします。Droidの外で手動実行したgitコマンドには影響しません。
</Aside>



---

## Droid Shieldが検出する対象 {#what-droid-shield-detects}

Droid Shieldは、以下を含む幅広い認証情報パターンをスキャンします：



<div class="factory-card-group">

<div class="factory-card">

**APIキーとトークン**

Factory APIキー、GitHubトークン、GitLabトークン、npmトークン、AWS、Google Cloud、Stripe、SendGridなどのAPIキー。

</div>


  

<div class="factory-card">

**認証情報**

（JWT、OAuth、セッショントークンなど）と、認証情報が埋め込まれたURL。

</div>


  

<div class="factory-card">

**秘密鍵**

（SSH秘密鍵、PGP鍵、ageシークレットキー、OpenSSH鍵など）およびその他の暗号鍵形式。

</div>


  

<div class="factory-card">

**サービス固有のシークレット**

（Slack Webhookとトークン、Twilio認証情報、Mailchimpキー、Square OAuthシークレット、Azureストレージキーなど）。

</div>

</div>



### 検出アルゴリズム {#detection-algorithm}

Droid Shieldは、ランダム性検証を伴うスマートパターンマッチングを使用します：

- **パターンマッチング** - フォーマットによる認証情報の識別
- **ランダム性チェック** - キャプチャされた値が実際のシークレットのように見えるかを検証
- **コンテキスト認識** - 変数名と代入パターンを考慮して誤検出を減らす

---

## Droid Shield 2.0: 学習型シークレット検出 {#droid-shield-20-learned-secret-detection}

Droid Shield 2.0 は、パターンベース検出の上に意味的レイヤーを追加する 2 つのファインチューニング済み分類モデルによって、決定論的スキャナーを拡張します。すべての commit と push は引き続き最初に決定論的スキャナーを通過し、その後モデルが、スキャナーがフラグ付けした、または見逃した特定のコンテキストを分類します。



<Aside kind="note">
Droid Shield 2.0 はリサーチプレビューです。組織で有効にするには、[お問い合わせください](mailto:support@factory.ai)。
</Aside>



### 2 つの分類モデル {#the-two-classification-models}

これらのモデルは決定論的スキャナーの前後で機能し、それぞれ異なる失敗パターンに最適化されています。



<div class="factory-card-group">

<div class="factory-card">

**リスクモデル**

決定論的スキャナーが**検出しなかった**変更行のうち、周辺コンテキストから見てなおシークレットを含んでいそうな行に対して実行されます。パターンセットが見逃す実際のシークレットを捉えるため、再現率を重視して最適化されています。見逃された可能性のあるシークレットを検出すると、警告を生成します。

</div>


  

<div class="factory-card">

**ダウングレードモデル**

スキャナーが**検出した**行に対して実行されます。検出されたシークレットをマスクした周辺コンテキストを確認し、スキャナーのヒットが真陽性（ブロックを維持）か、誤検知（警告にダウングレード）かを判定します。

</div>

</div>



---

## Droid Shieldが起動するタイミング {#when-droid-shield-activates}

Droid Shieldは以下のgit操作中に自動的に起動します：

- **`git commit`** - コミット作成前にステージされた変更をスキャン
- **`git push`** - リモートにプッシュされるコミットをスキャン



<Aside kind="warning">
シークレットが検出された場合、認証情報の露出を防ぐためgit操作はブロックされます。続行する前にシークレットを削除する必要があります。
</Aside>



---

## Droid Shield設定の管理 {#managing-droid-shield-settings}

### CLIでの操作 {#in-the-cli}

設定メニューからDroid Shieldのオン/オフを切り替えることができます：

1. `droid`を実行
2. `/settings`を入力
3. **「Droid Shield」**設定を切り替え
4. 変更は即座に有効になります



<Aside kind="info">
Droid Shieldは保護のため**デフォルトで有効**です。有効のままにしておくことを強く推奨します。
</Aside>



---

## シークレットが検出された場合の対処法 {#what-to-do-if-secrets-are-detected}

Droid Shieldが潜在的なシークレットを検出すると、以下のようなエラーメッセージが表示されます：

```
Droid-Shield has detected potential secrets in 2 location(s) across files:
src/config.ts, .env.example

If you would like to override, you can either:
1. Perform the commit/push yourself manually
2. Disable Droid Shield by running /settings and toggling the "Droid Shield" option
```

### 推奨される対処方法 {#recommended-actions}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">検出結果を確認</div>

記載されたファイルと行を慎重に確認し、検出内容を特定します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">シークレットを削除</div>

- ハードコードされた認証情報の代わりに環境変数を使用する
  - シークレットを安全な認証情報ストアに移動する
  - 機密ファイルを`.gitignore`に追加する
  - シークレットがすでにコミットされている場合は、git filter-branchまたはBFG Repo-Cleanerを使用する

</div>


  

<div class="factory-step">

<div class="factory-step-title">操作を再試行</div>

シークレットを削除したら、Droid経由でgitコマンドを再度実行します。

</div>

</div>





<Aside kind="warning">
**チェックを回避するためだけにDroid Shieldを無効化しないでください。** 認証情報の露出は、セキュリティ侵害、不正アクセス、コンプライアンス違反につながる可能性があります。
</Aside>



### 誤検出の場合 {#if-you-get-a-false-positive}

Droid Shieldは慎重を期すために保守的なパターンを使用します。検出が誤検出だと思われる場合：

1. **実際のシークレットでないことを確認** - その値が機密情報でないことを再確認
2. **手動コミットを使用** - Droid以外でgit操作を直接実行
3. **パターンを報告** - 繰り返し発生する誤検出がある場合はsupport@factory.aiまでご連絡ください



<Aside kind="note">
Droid Shield 2.0 が有効な場合、ダウングレードモデルがスキャナーのヒットを自動的に確認し、明らかな誤検知（プレースホルダー、サンプル、テストフィクスチャ）を手動介入なしで除外できます。
</Aside>



---

## ベストプラクティス {#best-practices}





<Details summary="環境変数を使用">
すべてのシークレットを環境変数または安全な認証情報マネージャーに保存し、ソースファイルには絶対にハードコードしないでください。

```bash
# 良い例 - 環境変数を使用
const apiKey = process.env.FACTORY_API_KEY;

# 悪い例 - シークレットをハードコード
const apiKey = "YOUR_API_KEY_HERE";
```
</Details>



  

<Details summary="Droid Shieldを有効にしておく">
Droid Shieldは重要な安全レイヤーを提供します。特にチーム環境では常に有効にしておいてください。
</Details>



  

<Details summary="コミット前に確認">
Droid Shieldがあっても、コミット前に変更を手動で確認し、機密データが含まれていないことを確認してください。
</Details>



  

<Details summary="チームに周知">
すべてのチームメンバーがDroid Shieldの仕組みと、有効に保つ重要性を理解していることを確認してください。
</Details>





---

## 制限事項 {#limitations}



<Aside kind="note">
**Droid Shieldは検出ツールであり、保証ではありません。** 一般的なシークレットパターンの多くを検出できますが、決定論的スキャナー単体では以下を検出できません:
  - パターンデータベースにないカスタムシークレット形式
  - 認識可能なパターンに従わないシークレット
  - 難読化またはエンコードされた認証情報
  - ビジネスロジックの脆弱性やコードセキュリティの問題
</Aside>



---

## 関連リソース {#related-resources}



<div class="factory-card-group">

<div class="factory-card">

**[[jp/cli/account/security|セキュリティ概要]]**

Factoryの包括的なセキュリティ機能とベストプラクティスについて学びます。

</div>


  

<div class="factory-card">

**[[jp/cli/configuration/settings|設定]]**

Droid Shieldの設定を含むDroid設定を構成します。

</div>


  

<div class="factory-card">

**[Droid Shield 2.0 リサーチ記事](https://factory.ai/news/droid-shield-2-0)**

学習型分類モデル、トレーニングデータ、評価結果の技術的な詳細を紹介します。

</div>


  

<div class="factory-card">

**[[jp/enterprise/llm-safety-and-agent-controls|LLMの安全性とエージェント制御]]**

Droid Shieldがより広範なエンタープライズ向けセーフティモデルの中でどのような役割を果たすかを説明します。

</div>

</div>



---

## サポートが必要ですか？ {#need-help}



<div class="factory-card-group">

<div class="factory-card">

**セキュリティに関する質問**

セキュリティチームへのお問い合わせ: **security@factory.ai**

</div>


  

<div class="factory-card">

**誤検知**

継続的な誤検知パターンを報告するには、**support@factory.ai**までお問い合わせください。

</div>

</div>
