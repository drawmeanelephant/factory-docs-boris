---
id: jp/integrations/slack
title: "Slack"
status: published
summary: "FactoryとSlackワークスペースを接続する手順ガイド"
parent: jp/integrations/index
tags: [integrations]
relations: [relates_to=integrations/slack]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Slack</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">FactoryとSlackワークスペースを接続する手順ガイド</p>


FactoryをSlackに接続すると、DroidがSlack上の会話やチームのコンテキストを利用できるようになります。



<Aside kind="warning">
Factory Slack appがすでにワークスペースにインストールされている場合でも、以下のSlackインストールフローを再実行してください。これにより、DroidがSlackスレッド内の画像をコンテキストとして取り込み、動画、生成されたアーティファクト、その他のファイルをSlackに投稿できるようになります。Slackワークスペースの設定によっては、Adminの承認が必要になる場合があります。
</Aside>



## 前提条件 {#prerequisites}

- 管理者権限を持つFactoryアカウント
- SlackワークスペースのAdmin権限
- Slackワークスペースでアプリをインストールする権限

## 統合手順 {#integration-steps}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Slack連携設定を開く</div>

[Factoryアカウントにログイン](https://app.factory.ai)し、[**Settings** → **Organization**](https://app.factory.ai/settings/organization) を開いて、**Org Integrations** の **Slack** を探します。



<div class="factory-frame">

<img src="../../images/slack-organization-settings.png" alt="Org Integrations の Slack を表示している Factory の Organization 設定ページ" />

<div class="factory-frame-caption">Organization設定のSlack</div>

</div>



</div>


  

<div class="factory-step">

<div class="factory-step-title">Slack連携を開始</div>

**Connect** をクリックします。Slackがすでにインストールされている場合は **Manage** をクリックして連携プロセスを開始します。既存のSlackインストールを最新の権限に更新する場合は、連携詳細の **Reconnect** をクリックしてインストールフローを再実行します。



<div class="factory-frame">

<img src="../../images/slack-reconnect-button.png" alt="Reconnect ボタンを表示している Factory の Slack 連携詳細画面" />

<div class="factory-frame-caption">権限を更新するためにSlackを再接続</div>

</div>



</div>


  

<div class="factory-step">

<div class="factory-step-title">FactoryのSlackアプリを認可</div>

Slackにリダイレクトされます。要求された権限を確認し、**Allow** をクリックしてFactoryにSlackワークスペースへのアクセスを許可します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">ワークスペースを選択</div>

複数のワークスペースに所属している場合は、Factoryに接続するワークスペースを選択します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">連携を確認</div>

認可後、Factoryに戻ります。連携ステータスが"Connected"と表示されていることを確認します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">チャンネルに追加</div>

Slackワークスペースで、各チャンネルに`/invite @Factory`と入力してFactoryアプリを関連チャンネルに追加します。

</div>

</div>



## 検証 {#verification}

統合が正しく動作していることを確認するには：

1. アプリが追加されたチャンネル内のスレッドで `@Factory` をメンションします。
2. Factoryが、その会話をFactoryで開くためのリンク付きで応答することを確認します。
3. リンクをクリックし、Slackスレッドの内容が新しいFactoryセッションに表示されることを確認します。
4. 最新の権限のためにインストールフローを再実行した場合は、画像添付を含むスレッドでテストし、Droidがそれをコンテキストとして利用できることを確認します。
5. ワークフローが結果をSlackに返す場合は、Droidが生成ファイルまたは短い結果動画をそのスレッドにアップロードできることを確認します。

## 機能 {#capabilities}

Slack連携では、次のことができます。



<div class="factory-frame">

<video controls preload="metadata">
<source src="../../images/marketing/slack-clone-scene.mp4" type="video/mp4" />
  </video>

<div class="factory-frame-caption">FactoryのSlack連携デモ</div>

</div>



- 任意のSlackスレッドで `@Factory` をメンションして、そのスレッドからDroidセッションを開始する
- WebまたはDesktopでセッションを継続する
- 提供されたリンクをクリックして、Slackスレッド全体のコンテキストをFactoryにインポートする
- Slackの対応画像添付をセッションのコンテキストとして含める
- Droidにメッセージ、生成ファイル、アーティファクト、結果動画をSlackへ投稿させる
- アクティブなDroidセッションに対して、Slackからフォローアップメッセージや添付ファイルを送る
- **好きなモデルを選べ、ロックインはありません。** Factoryはモデル非依存で、Claude、GPT、Gemini、オープンソース/Droid Core、その他30以上のサポート対象モデルから選べます
- セッション開始時にモデルを選択したり、Auto-Runやサービスアカウントのワークフロー向けにチャンネルごとのデフォルトの **Model** を設定したり、[[jp/web/factory-router|Factory Router]] に最適なモデル選択を自動で任せたりできます
- FactoryチャットにスレッドURLを貼り付けて、FactoryでSlackスレッドを参照する



<div class="factory-frame">

<img src="../../images/slack-model-selection.png" alt="Factory models を表示しているモデルピッカー付きの Factory Session Settings ダイアログ" />

<div class="factory-frame-caption">Slackから開始したセッションで、特定のモデルを選ぶか、Factory Routerに自動選択を任せる</div>

</div>



PRを作成する際、Slack連携はCIを処理するサブエージェントも利用するため、エージェントの応答が速くなります。

Slackスレッドがインポートされると、Factoryは会話履歴全体にアクセスできるため、コンテキストを考慮した支援を提供できます。

## Slack設定 {#slack-settings}

Slackを接続したら、[**Settings** → **Organization**](https://app.factory.ai/settings/organization) の **Manage** をクリックしてSlackチャンネル設定を構成します。これらの設定が必要なのはIncident Responseとサービスアカウントのワークフローだけで、通常の `@Factory` メンションはここでチャンネルを設定しなくても動作します。

チャンネル設定では、チャンネルを有効にして行を展開し、**Run as**、**Incident Response**、**Machine Type**、**Computer** または **Workspace**、**Session Visibility**、**Model**、**Custom Prompt** を設定できます。この一覧には、Factoryアプリが招待されているチャンネルだけが表示されます。

## サービスアカウント {#service-accounts}

Slackセッションを、`@Factory` をメンションしたSlackユーザーではなく、共有IDと事前設定済みのDroid Computerから実行したい場合は、[[jp/enterprise/service-accounts|サービスアカウント]] を使用します。これは、一貫した認証情報とツールアクセスが必要なインシデント、運用、リリース用チャンネルに便利です。

Slackでサービスアカウントを使う前に、次を確認してください。

- 組織でサービスアカウントが有効になっている。
- サービスアカウントが有効な状態である。
- サービスアカウントが少なくとも1台のDroid Computerを所有している。
- FactoryアプリがSlackチャンネルに招待されている。



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Slackチャンネル設定を開く</div>

Factoryで **Settings** → **Integrations** → **Slack** → **Channels** に移動します。チャンネルを有効にして、その設定を展開します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">実行主体を選ぶ</div>

**Run as** の行が表示されたら、サービスアカウントを選択します。サービスアカウントを選ぶと、そのチャンネルはそのサービスアカウントのIDとコンピューターで実行されます。

</div>


  

<div class="factory-step">

<div class="factory-step-title">コンピューターを選ぶ</div>

サービスアカウントのSlackセッションはDroid Computersで実行されます。サービスアカウントを選択すると、Factoryは実行先を **Computer** に固定し、そのサービスアカウントが所有するコンピューターだけを表示します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">必要に応じてAuto-Runを設定する</div>

チャンネルの自動ワークフローでは、**Auto-Run** を有効にし、そのチャンネルのプロンプト、モデル、公開範囲を設定します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">Slackからテストする</div>

チャンネルで `@Factory` をメンションするか、Auto-Runが有効ならテストアラートを送信します。Factoryは選択したサービスアカウントとしてセッションを開始します。

</div>

</div>



アドホックなSlackセッションでは、コンピューターピッカーにも **Run as** セレクターが表示されることがあります。サービスアカウントを選択し、そのサービスアカウントのコンピューターの1つを選び、必要に応じて今後のSlackメンションのデフォルトとして保存できます。

## ベストプラクティス {#best-practices}

- 開発に関する議論が行われるチャンネルにのみFactoryアプリを追加する。
- Factoryをメンションする際は、チャンネルメッセージではなくスレッドを使用する。
- Factoryをメンションする前に、Slackスレッドで十分なコンテキストを提供する。
- Slack設定でFactoryアプリに付与された権限を定期的に確認する。

## トラブルシューティング {#troubleshooting}

統合中に問題が発生した場合：

- FactoryとSlackワークスペースの両方で管理者権限を持っていることを確認する。
- メンションしようとしているチャンネルにFactoryアプリが追加されていることを確認する。
- Droidが画像添付を読み取れない、またはファイルや動画をアップロードできない場合は、上記のSlackインストールフローを再実行してFactory Slack appの権限を更新する。
- SlackスレッドURLを貼り付ける際に「not_in_channel」エラートーストが表示される場合、そのチャンネルにFactoryボットを招待する必要があります。この問題を解決するには、チャンネルで `/invite @Factory` を使用してください。
- 組織のファイアウォールがwebhook通信をブロックしていないか確認する。
- 問題が解決しない場合は、具体的なエラーメッセージと共にFactoryサポートに連絡する。



<div class="factory-card">

**[セキュリティとコンプライアンス](https://trust.factory.ai)**

FactoryのTrust Centerでコンプライアンス資料、認証、セキュリティリソースを確認する

</div>
