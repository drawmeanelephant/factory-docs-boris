---
id: jp/cli/account/security
title: "セキュリティ"
status: published
summary: "Droid CLIが組み込み保護とベストプラクティスでコードとデータを安全に保つ方法。"
parent: jp/cli/account/index
tags: [cli, security, authentication, permissions, encryption, data-protection, privacy, secure]
relations: [relates_to=cli/account/security]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">セキュリティ</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Droid CLIが組み込み保護とベストプラクティスでコードとデータを安全に保つ方法。</p>


## セキュリティファーストデザイン {#security-first-design}

Droid CLI はセキュリティを中核に据えて構築されています。暗号化された認証、厳格な権限管理、エンタープライズグレードの保護により、あなたのコードは安全に保たれます。

---

## 主要なセキュリティ機能 {#key-security-features}



<div class="factory-card-group">

<div class="factory-card">

**安全な認証**

暗号化されたトークン保存を備えたOAuthログイン。トークンは30日ごとに自動ローテーションされ、OSレベルのファイル権限で保存されます。

</div>


  

<div class="factory-card">

**権限制御**

リスクのある操作にはすべて明示的な承認が必要です。セキュリティ要件に応じて、ツール権限をallow/ask/rejectで設定します。

</div>


  

<div class="factory-card">

**データ暗号化**

すべてのデータは転送中（TLS 1.3）と保存時（AWS KMSによるAES-256）に暗号化されます。Factoryがコードを学習に使用することはありません。

</div>


  

<div class="factory-card">

**ローカル実行**

シェルコマンドとファイル編集はローカルで実行されます。必要なコンテキストとdiffのみがFactoryの安全なクラウドに送信されます。

</div>


  

<div class="factory-card">

**OSレベルのサンドボックス（Beta）**

ファイルシステムとネットワークアクセスに対して、オプションで有効化できるカーネル強制の分離を提供します。詳しくは[[jp/cli/configuration/sandbox|サンドボックス]]を参照してください。

</div>

</div>



---

## セキュリティベストプラクティス {#security-best-practices}



<Aside kind="warning">
承認前に提案されたコードとコマンドを必ず確認してください。Droidがアクセス・実行できる内容はあなたが制御します。
</Aside>



### 基本的なセキュリティガイドライン {#essential-security-guidelines}





<Details summary="承認前に確認">
特に、**提案されたコマンドとファイル変更を必ず確認してください**:
  - パッケージをインストールするコマンドやシステムファイルを変更するコマンド
  - 機密データや認証情報を扱う操作
  - 外部サービスへのネットワークリクエスト
  - プロジェクトディレクトリ外のファイル操作
</Details>



  

<Details summary="分離環境を使用">
以下を扱う場合は**コンテナまたはVMでDroidを実行してください**:
  - 信頼できないコードリポジトリ
  - 外部APIまたはWebサービス
  - 実験的またはリスクのある可能性がある操作
  - 共有開発環境
</Details>



  

<Details summary="権限を慎重に管理">
セキュリティ要件に合わせて**ツール権限を設定**します:
  - 高リスクコマンドはデフォルトで"reject"に設定する
  - 監督が必要な中リスク操作には"ask"を使用する
  - 完全に信頼できる低リスクコマンドのみ"allow"にする
  - Settingsメニューで権限を定期的に確認する
</Details>



  

<Details summary="機密データを保護する">
**プロンプトにシークレットを含めないでください:**
  - APIキーとトークンには環境変数を使用する
  - 認証情報を安全な認証情報マネージャーに保存する
  - Droidの作業ディレクトリから機密ファイルを除外する
  - CI/CDではFACTORY_TOKEN環境変数を使用する
</Details>





---

## 組み込み保護機能 {#built-in-protections}

Droid CLI には複数のセキュリティレイヤーが含まれています：

- **書き込みアクセス制限**: プロジェクトディレクトリとそのサブディレクトリ内のファイルのみ変更可能
- **コマンド承認**: リスクの高い操作には明示的なユーザー確認が必要
- **プロンプトインジェクション検出**: 潜在的に有害な指示がないかリクエストを分析
- **ネットワークリクエスト制御**: Web取得ツールはデフォルトで承認が必要
- **入力サニタイゼーション**: コマンドインジェクション攻撃を防止
- **セッション分離**: 各会話は個別の安全なコンテキストを維持

---

## エンタープライズセキュリティ {#enterprise-security}



<div class="factory-card-group">

<div class="factory-card">

**SSOとアイデンティティ**

SCIMプロビジョニングとロールベースアクセス制御を備えたSAML 2.0 / OIDCシングルサインオン。

</div>


  

<div class="factory-card">

**データガバナンス**

ゼロデータ保持モード、顧客管理の暗号化キー（BYOK）、プライベートクラウドデプロイ。

</div>


  

<div class="factory-card">

**コンプライアンス**

SOC 2 Type II認証、GDPR準拠、定期的な侵入テスト、サプライチェーンセキュリティ。

</div>


  

<div class="factory-card">

**監査とモニタリング**

完全なセッションログ、OpenTelemetryメトリクス、エンタープライズ管理のセキュリティポリシー。

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

**トラストセンター**

コンプライアンス文書、認証、セキュリティリソースは**[trust.factory.ai](https://trust.factory.ai)**を参照してください。

</div>

</div>





<Aside kind="note">
責任ある開示プログラムを通じてセキュリティ脆弱性を報告してください。詳細はsecurity@factory.aiまでお問い合わせください。
</Aside>
