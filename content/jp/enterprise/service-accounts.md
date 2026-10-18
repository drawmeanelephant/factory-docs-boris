---
id: jp/enterprise/service-accounts
title: "サービスアカウント"
status: published
summary: "CI/CDパイプライン、スクリプト、Droid ComputersでFactoryの自動化を実行するための人以外のID。"
parent: jp/enterprise/index
tags: [enterprise]
relations: [relates_to=enterprise/service-accounts]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">サービスアカウント</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">CI/CDパイプライン、スクリプト、Droid ComputersでFactoryの自動化を実行するための人以外のID。</p>


サービスアカウントは、組織に代わって作業を自動化する人以外のIDです。CI/CDパイプライン、スクリプト、Slack自動化、Droid Computersなど、特定のチームメイトではなく組織にワークロードを紐づけるべき場合に使用します。



<Aside kind="info">
**Enterprise機能** — サービスアカウントはエンタープライズ顧客が利用できます。詳細については[お問い合わせください](mailto:sales@factory.ai)。
</Aside>



---

## まずは基本から {#start-with-the-basics}



<div class="factory-card-group">

<div class="factory-card">

**サービスアカウントを作成**

SettingsのAPIキーセクションから安定したIDを追加します。実行内容がチームに分かるよう、明確な名前と必要に応じた説明を付けてください。サービスアカウントを作成または編集できるのは、マネージャーとオーナーのみです。

</div>


  

<div class="factory-card">

**APIキーを生成**

スクリプト、CIジョブ、その他の自動化ワークロード用のキーを作成します。キーの値は一度しか表示されないため、コピーして安全に保管してください。

</div>


  

<div class="factory-card">

**Droid Computersを関連付ける**

サービスアカウントが所有するコンピューターを作成し、長時間実行される作業を同じIDのまま継続できるようにします。

</div>


  

<div class="factory-card">

**Gitアクセスを設定**

GitHubには組織のGitHub Appインストールを使用します。GitLab Cloudでは、Settingsにサービスアカウント用のGitLabトークンを追加します。

</div>

</div>



---

## サービスアカウントの仕組み {#how-service-accounts-work}

サービスアカウントはFactory APIキーで認証され、独立したプリンシパルとして実行されます。セッション、コンピューター、課金イベント、監査関連の情報は、人間のユーザーではなくサービスアカウントに紐づけられます。

サービスアカウントが認証に使用されるには、有効である必要があります。無効にしたり削除したりすると、そのキーを使う新しいリクエストは失敗し、そのIDに依存するワークロードは別のアカウントへ移行するか、別のアカウントで再起動する必要があります。

---

## アクセスを安全に管理する {#manage-access-safely}





<Details summary="可能なら短命なキーを使う">
一時的な自動化で使うキーには有効期限を設定します。誤ってキーが漏えいしても、短命なキーであれば影響範囲を抑えられます。
</Details>



  

<Details summary="キーを定期的にローテーションする">
新しいキーを作成し、ワークロードを更新してから古いキーを失効させます。定期的なローテーションにより、認証情報が侵害された場合のリスクを減らせます。
</Details>



  

<Details summary="名前は固定して使う">
サービスアカウント名は変更できない識別子です。別の名前が必要な場合は、新しいサービスアカウントを作成してください。
</Details>



  

<Details summary="不要になったら削除する">
サービスアカウントを削除するとアクセス権が取り消され、可能な範囲でそのアカウントが所有するFactoryリソースも整理されます。
</Details>





---

## 一般的なユースケース {#common-use-cases}



<div class="factory-card-group">

<div class="factory-card">

**CI/CD**

あるエンジニア1人のアカウントに依存せず、リリース、テスト、デプロイのワークフローを実行します。

</div>


  

<div class="factory-card">

**Slack自動化**

チャンネルやワークフローを設定して、Droidをチーム共有のIDとして実行します。

</div>


  

<div class="factory-card">

**リポジトリ自動化**

サービスアカウントで管理される認証情報を使って、リポジトリのclone、push、各種操作を行います。

</div>


  

<div class="factory-card">

**永続的なコンピューター**

Droid Computersを、チームメイト個人のアカウントではなく自動化用IDに紐づけたまま維持します。

</div>

</div>
