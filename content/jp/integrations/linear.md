---
id: jp/integrations/linear
title: "Linear"
status: published
summary: "FactoryとLinearワークスペースを接続するガイド"
parent: jp/integrations/index
tags: [integrations]
relations: [relates_to=integrations/linear]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Linear</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">FactoryとLinearワークスペースを接続するガイド</p>


このガイドでは、FactoryとLinearの統合プロセスを順を追って説明し、FactoryとLinearプロジェクト間のシームレスな連携を可能にします。

## 前提条件 {#prerequisites}

- Linearワークスペースへの管理者アクセス権
- 管理者権限を持つFactoryアカウント

## 統合手順 {#integration-steps}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Factoryインテグレーションにアクセス</div>

Factoryアカウントにログインし、SettingsのIntegrationsセクションに移動します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">Linear連携を開始</div>

Linear連携オプションを見つけて選択します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">FactoryのLinearアプリケーションを認可</div>

Linearにリダイレクトされます。要求された権限を確認し、"Authorize"をクリックしてFactoryにLinearワークスペースへのアクセスを許可します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">チームとプロジェクトアクセスを設定</div>

Factoryと連携させるチームとプロジェクトを選択します。必要に応じて後から設定を調整できます。

</div>


  

<div class="factory-step">

<div class="factory-step-title">権限を設定</div>

Factoryが課題の表示・作成、ワークフロー管理、関連プロジェクトデータへのアクセスに必要な権限を持っていることを確認します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">連携を確認</div>

権限を付与するとFactoryに戻ります。連携ステータスが"Connected"と表示されていることを確認します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">新しいセッションを作成</div>

"🔗 Factory - Open in Factory"リンクをクリックすると、このチケットをコンテキストに含めてLinearから直接新しいセッションを作成できます

  - このリンクをクリックすると常に**新しいセッション**が作成されます。

</div>

</div>



## 検証 {#verification}

統合が正しく動作していることを確認するには：

1. 認証されたLinearプロジェクトの1つでテスト用のissueを作成します。
2. Factoryを使用してこのissueと連携します（例：コメントを追加したり、ステータスを変更したりする）。
3. 変更がLinearに反映されていることを確認します。

## ベストプラクティス {#best-practices}

- Factoryに付与された権限を定期的に確認・監査する。
- Linearのチームレベル設定を使用してアクセスを効率的に管理する。
- Linearワークスペースのセキュリティ設定を最新の状態に保つ。

## トラブルシューティング {#troubleshooting}

統合中に問題が発生した場合：

- FactoryとLinearの両方で必要な管理者権限があることを確認する。
- 権限関連の問題がないかLinearの監査ログを確認する。
- 統合が意図したチームとプロジェクトにアクセスできることを確認する。

問題が解決しない場合は、具体的なエラーメッセージやスクリーンショットと共にFactoryサポートにお問い合わせください。



<div class="factory-card">

**[セキュリティとコンプライアンス](https://trust.factory.ai)**

FactoryのTrust Centerでコンプライアンス資料、認証、セキュリティリソースを確認する

</div>
