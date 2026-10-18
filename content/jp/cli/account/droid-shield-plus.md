---
id: jp/cli/account/droid-shield-plus
title: "Droid Shield Plus"
status: published
summary: "プロンプトインジェクション、シークレット検出、機密データ保護のためのAI搭載セキュリティスキャン。Palo Alto Networks Prisma AIRSを利用するエンタープライズ機能。"
parent: jp/cli/account/index
tags: [cli, droid-shield-plus, prisma-airs, prompt-injection, secrets-detection, dlp, enterprise-security, ai-security]
relations: [relates_to=cli/account/droid-shield-plus]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Droid Shield Plus</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">プロンプトインジェクション、シークレット検出、機密データ保護のためのAI搭載セキュリティスキャン。Palo Alto Networks Prisma AIRSを利用するエンタープライズ機能。</p>




<Aside kind="info">
**エンタープライズ機能** — Droid Shield Plusはエンタープライズ顧客が利用できます。組織でこの機能を有効にするには[お問い合わせください](mailto:sales@factory.ai)。
</Aside>



## Droid Shield Plusとは？ {#what-is-droid-shield-plus}

Droid Shield Plusは、プロンプトインジェクション攻撃、機密データの露出、その他のセキュリティ脅威に対するリアルタイム保護を提供する高度なAI搭載セキュリティレイヤーです。パターンベースの検出を使用する標準的な[[jp/cli/account/droid-shield|Droid Shield]]とは異なり、Droid Shield Plusは**[Palo Alto Networks Prisma AIRS](https://docs.paloaltonetworks.com/ai-runtime-security)**（AI Runtime Security）を活用して、インテリジェントでコンテキストを認識するセキュリティスキャンを提供します。

---

## 主な機能 {#key-features}



<div class="factory-card-group">

<div class="factory-card">

**プロンプトインジェクション検出**

AIの動作を操作したりセキュリティ制御を回避したりする悪意あるプロンプトインジェクションの試みを特定してブロックします。

</div>


  

<div class="factory-card">

**高度なシークレットスキャン**

パターンマッチングより高い精度と少ない誤検知で、APIキー、トークン、パスワード、認証情報をAIで検出します。

</div>


  

<div class="factory-card">

**機密データ保護（DLP）**

個人識別情報（PII）、財務データ、その他の機密情報がプロンプトやコミットに含まれて公開される前に検出します。

</div>


  

<div class="factory-card">

**悪意あるコード検出**

セキュリティリスクとなり得る危険なコードパターンや疑わしいコンテンツを特定します。

</div>

</div>



---

## Droid Shield Plusの仕組み {#how-droid-shield-plus-works}

Droid Shield Plusは2層の保護を提供します：

### 1. プロンプトセキュリティスキャン {#1-prompt-security-scanning}

Droidに送信するすべてのプロンプトは、処理前に自動的にスキャンされます。脅威が検出された場合、プロンプトはブロックされ、通知されます：

```
Droid Shield Plus has blocked this prompt due to detected: prompt injection, sensitive data.

If you believe this is a false positive, you can disable Droid Shield Plus in settings.
```

**検出される脅威のカテゴリ：**
- **Prompt Injection** — AIの指示を操作しようとする試み
- **機密データ (DLP)** — PII、認証情報、または機密情報
- **有害コンテンツ** — 害のあるまたは不適切なコンテンツ
- **悪意のあるコード** — 疑わしいコードパターン

### 2. Git コミットスキャン {#2-git-commit-scanning}

Droid経由で`git commit`または`git push`操作を実行する際、Droid Shield PlusはAI搭載分析を使用してステージされた変更をスキャンします：

```
Droid Shield Plus has detected potential secrets in your staged changes.

If you would like to override, you can either:
1. Perform the commit/push yourself manually
2. Disable Droid Shield Plus in settings
```

これにより正規表現ベースのスキャンよりも大幅に高精度な検出が可能になり、以下をキャッチします：
- 難読化またはエンコードされたシークレット
- コンテキストを認識した認証情報の検出
- カスタムシークレット形式
- 複雑なコード構造に埋め込まれたシークレット

---

## Droid Shield vs Droid Shield Plus {#droid-shield-vs-droid-shield-plus}

| 機能 | Droid Shield | Droid Shield Plus |
|---------|--------------|-------------------|
| **検出方法** | パターン/正規表現マッチング | AI搭載分析 |
| **プロンプトスキャン** | なし | あり |
| **Git コミットスキャン** | あり | あり |
| **Prompt Injection 検出** | なし | あり |
| **機密データ (DLP)** | 限定的 | 包括的 |
| **有害コンテンツ検出** | なし | あり |
| **悪意のあるコード検出** | なし | あり |
| **偽陽性率** | 高い | 低い |
| **利用可能性** | 全ユーザー | Enterprise |
| **提供元** | 内蔵パターン | Palo Alto Networks Prisma AIRS |



<Aside kind="note">
Droid Shield Plusを有効にすると、git操作では標準のDroid Shieldに代わり、パターンベース検出ではなく強化されたAI搭載スキャンを提供します。
</Aside>



---

## Droid Shield Plusの有効化 {#enabling-droid-shield-plus}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Factoryに問い合わせる</div>

組織でDroid Shield Plusを有効にするには、[sales@factory.ai](mailto:sales@factory.ai)までお問い合わせください。

</div>


  

<div class="factory-step">

<div class="factory-step-title">設定で有効化</div>

組織で有効化されたら:
  1. `droid`を実行します
  2. `/settings`を入力します
  3. **Security**セクションに移動します
  4. **"Droid Shield Plus (AI-Powered)"**をオンにします

</div>


  

<div class="factory-step">

<div class="factory-step-title">有効化を確認</div>

確認用のサブタイトルとして、*"AI-powered security scanning for prompt injection, sensitive data, and toxic content. Powered by Palo Alto Networks Prisma AIRS."*が表示されます。

</div>

</div>



---

## ブロックされたプロンプトの処理 {#handling-blocked-prompts}

Droid Shield Plusがプロンプトやgit操作をブロックした場合：





<Details summary="検出内容を確認">
フラグが立った内容を慎重に確認します。エラーメッセージには脅威カテゴリ（プロンプトインジェクション、機密データ、有害コンテンツ、悪意のあるコード）が表示されます。
</Details>



  

<Details summary="機密コンテンツを削除">
機密データが検出された場合:
  - シークレットを環境変数に移動する
  - 安全な認証情報ストアを使用する
  - プロンプトからPIIを削除する
</Details>



  

<Details summary="必要に応じて言い換える">
プロンプトインジェクションが検出された場合は、操作の試みと誤解される可能性のあるパターンを避けるようにリクエストを言い換えます。
</Details>



  

<Details summary="誤検知を報告">
検出が誤っていると思われる場合は、誤検知の詳細を添えて[support@factory.ai](mailto:support@factory.ai)までお問い合わせください。
</Details>







<Aside kind="warning">
**セキュリティチェックを回避するためだけにDroid Shield Plusを無効化しないでください。** コンテンツがブロックされている場合、対処すべき正当なセキュリティ上の懸念がある可能性があります。
</Aside>



---

## セキュリティとプライバシー {#security-privacy}

Droid Shield Plusは業界をリードするAIランタイムセキュリティプラットフォームである**[Palo Alto Networks Prisma AIRS](https://docs.paloaltonetworks.com/ai-runtime-security)**によって駆動されています：

- **リアルタイム分析** — プロンプトとコードは最小限のレイテンシでリアルタイムスキャンされます
- **エンタープライズグレードセキュリティ** — Palo Alto Networksの業界をリードするセキュリティインフラストラクチャ上に構築
- **グレースフルデグラデーション** — セキュリティサービスが一時的に利用できない場合、Droidは問題をログに記録しながら動作を継続します

---

## 関連リソース {#related-resources}



<div class="factory-card-group">

<div class="factory-card">

**[[jp/cli/account/droid-shield|Droid Shield]]**

すべてのDroidアカウントに含まれる標準のパターンベースシークレット検出について学びます。

</div>


  

<div class="factory-card">

**[[jp/cli/account/security|セキュリティ概要]]**

Factoryのセキュリティ機能とプラクティスの包括的な概要。

</div>

</div>



### Prisma AIRS ドキュメント {#prisma-airs-documentation}



<div class="factory-card-group">

<div class="factory-card">

**[Prisma AIRS概要](https://docs.paloaltonetworks.com/ai-runtime-security)**

Prisma AIRS AI Runtime SecurityプラットフォームのPalo Alto Networks公式ドキュメント。

</div>


  

<div class="factory-card">

**[Prisma AIRS APIリファレンス](https://pan.dev/prisma-airs/api/airuntimesecurity/)**

Prisma AIRS AI Runtime Security APIの開発者向けドキュメント。

</div>

</div>



---

## Droid Shield Plusを入手 {#get-droid-shield-plus}



<div class="factory-card">

**[組織で有効化](mailto:sales@factory.ai)**

エンタープライズ組織でDroid Shield Plusを有効にするには、**sales@factory.ai**まで営業チームにお問い合わせください。

</div>
