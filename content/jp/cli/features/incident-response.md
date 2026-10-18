---
id: jp/cli/features/incident-response
title: "インシデント対応"
status: published
summary: "Slackで本番アラートに対応し、インシデントの解決や調査を自律的に行うようDroidを設定します。"
parent: jp/cli/features/index
tags: [cli]
relations: [relates_to=cli/features/incident-response]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">インシデント対応</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Slackで本番アラートに対応し、インシデントの解決や調査を自律的に行うようDroidを設定します。</p>


## 概要 {#overview}

設定済みのSlackチャンネルにアラートが届くと、Factoryは関連付けられたDroidセッションを自動で開始し、適切なコンテキスト、マシン、指示を使ってDroidがインシデントを調査できるようにします。

DroidはRCAの実施、必要に応じた修正PRの作成、将来同じ種類のアラートをより速く調査できるようにするインシデントrunbookの更新まで進められます。



<Aside kind="warning">
Factoryのチャネル自動実行を設定するには、Factoryの**Owner**または**Manager**ロールが必要です。
</Aside>



## クイックスタート: Factory App からセットアップする {#quickstart-set-up-from-the-factory-app}

すべてのSlackチャンネル設定を1か所で確認したい場合は、Web UIを使用してください。



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Slack Channels 設定を開く</div>

Factory Appで**設定 → Integrations → Slack**に移動します。まだSlackを接続していない場合は、先に[[jp/integrations/slack|Slack連携]]を設定してから、Slack管理画面を開き、**Channels**タブを選択してください。

</div>



  

<div class="factory-step">

<div class="factory-step-title">Factoryをインシデントチャンネルに招待する</div>

Slackで、アラートbotがインシデントを投稿するチャンネルを開き、次を実行します。

```text
/invite @Factory
```

チャンネル一覧には、Factoryが招待されているチャンネルだけが表示されます。

</div>



  

<div class="factory-step">

<div class="factory-step-title">チャンネルのAuto-Backlinkを有効にする</div>

**Select Auto-Backlinked Channels**でインシデントチャンネルを検索し、**Auto-Backlink**をオンにします。これにより、そのチャンネルのSlackメッセージがFactoryセッションにリンクされ、チャンネル設定が展開されます。

</div>



  

<div class="factory-step">

<div class="factory-step-title">チャンネルの実行主体を選ぶ</div>

**Run as** の行が表示される場合は、**Factory user** のままにするか、サービスアカウントを選択します。サービスアカウントは専用のコンピューターとそのアカウントのIDで実行されるため、共有の事前設定済みアカウントでインシデントセッションを実行したい場合に選択してください。

</div>



  

<div class="factory-step">

<div class="factory-step-title">セッションの実行先を選ぶ</div>

**Machine Type** と、Droidが使用する実行先を選択します。多くの組織では **Computer** を使いますが、組織によっては **Cloud** または **Computer** を選択できます。サービスアカウントを選択した場合、Machine Type は **Computer** に固定され、**Computer** ピッカーにはそのサービスアカウントが所有するコンピューターだけが表示されます。

</div>



  

<div class="factory-step">

<div class="factory-step-title">Auto-Runを有効にする</div>

**Auto-Run**を有効にします。これにより、インシデントアラートが届いたときにFactoryがDroidセッションを自動で開始できるようになります。Auto-Runを有効にできない場合は、先に必要なコンピューターまたはワークスペースを選択または作成してください。

</div>



  

<div class="factory-step">

<div class="factory-step-title">公開範囲、モデル、プロンプトを調整する</div>

**Factory user** を使用する場合はセッション所有者を選び、セッションを所有者限定にするか組織に表示するかを設定し、必要に応じてモデルを選択して、カスタムのインシデントプロンプトを設定します。

開始時のプロンプトとしては、次の内容が適しています。

```text
Use the `/incident` skill for Slack incidents and run an RCA if applicable.
If the thread message is an incident or asking for RCA/root-cause analysis, invoke the `incident` skill before investigating.
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">テストアラートを送信する</div>

実際のインシデント送信に使うのと同じ種類のbotから、トップレベルのテストアラートを投稿します。Factoryが自動実行のDroidセッションを開始し、Slackスレッドからそのリンクを確認できることを確かめてください。

</div>

</div>



## 別の方法: Droid CLIでセットアップする {#configuration-details}

すでにDroidを開いていて、ガイド付きでインシデントチャンネルを設定したい場合は、CLIフローを使用してください。



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">セットアップコマンドを実行する</div>

Droid CLIで次を実行します。

```text
/setup-incident-response
```

まだSlackが接続されていない場合、Droidは続行前にSlackのOAuthフローを開きます。

</div>



  

<div class="factory-step">

<div class="factory-step-title">インシデントチャンネルを選ぶ</div>

インシデントアラートを受信するSlackチャンネルを選択します。チャンネルが表示されない場合は、`/invite @Factory`でFactoryを招待してから、セットアップコマンドを再実行してください。

</div>



  

<div class="factory-step">

<div class="factory-step-title">コンピューターを選ぶ</div>

Droidがインシデント調査に使用するコンピューターを選択します。適切なリポジトリのチェックアウト、観測ツール、認証情報が揃った環境を選んでください。

</div>



  

<div class="factory-step">

<div class="factory-step-title">RCAプロンプトを受け入れるか編集する</div>

デフォルトのインシデント用プロンプトをそのまま使うか、どの runbook、ダッシュボード、リポジトリ、エスカレーションルールを優先的に確認するべきかなど、チャンネル固有の指示を追加します。

</div>



  

<div class="factory-step">

<div class="factory-step-title">適用して確認する</div>

設定を確定したら、Slackでテストアラートを送信し、Droidが自動で起動することを確認します。

</div>

</div>



## 設定の詳細 {#customizing-the-prompt}

### プロンプトをカスタマイズする {#channel-selection-and-trigger-source}

チャンネルプロンプトは、そのチャンネルのすべての自動実行セッションに注入されます。内容はインシデント対応に特化させてください。

- 適切な場合はRCAを実施し、`/incident`ワークフローを使うようにDroidに伝える
- そのチャンネルに対応する主要なサービスやリポジトリを示す
- runbook、ダッシュボード、一般的なアラートソースを案内する
- 不確実性を要約して共有するタイミングなど、エスカレーションの期待値を明示する

チャンネルを汎用的な自動化の入口にしてしまうようなプロンプトは避けてください。インシデント対応は、プロンプトが狭く運用に特化しているほど効果を発揮します。

### チャンネルの選択 {#session-privacy-and-model}

インシデント対応は、インシデントアラートがトップレベルのメッセージとして届くチャンネル向けに設計されています。スレッド返信は新しい自動実行セッションの開始には使われないため、通常の会話でDroidが繰り返し起動するのを防げます。

最良の結果を得るには、`#incidents`、`#alerts-production`、またはサービス固有のインシデントチャンネルのような専用チャンネルを使用してください。

Slack Channels 設定テーブルには、Factoryが招待されているチャンネルだけが表示されます。まずそのチャンネルで**Auto-Backlink**を有効にし、その後に行を展開してAuto-Runを設定してください。

### Run as {#managing-the-automation}

**Run as** ピッカーは、組織でサービスアカウントによるチャンネル委任が利用できる場合に表示されます。

- **Factory user** では、設定したセッション所有者のFactoryユーザーIDがAuto-Runセッションで使われます。
- サービスアカウントでは、そのサービスアカウントのIDとコンピューターが使われます。

サービスアカウントを選択すると、Factoryは**Machine Type**を**Computer**に固定し、セッション所有者の行を非表示にし、コンピューターピッカーをそのサービスアカウントが所有するコンピューターのみに制限します。チャンネルを常に同じ事前設定済みアカウントとマシンから実行したい共有のインシデント対応セットアップで使ってください。

### セッション所有者 {#how-the-incident-flow-works}

**Run as** が **Factory user** に設定されている場合、セッション所有者によって、Auto-Runセッションで使用されるFactoryユーザーIDが決まります。インシデント調査に必要な接続済みツールと組織権限を持つ所有者を選んでください。

所有者が見つからない、またはアクセス権が不足しているためにセッションが失敗する場合は、チャンネル設定を更新し、適切な権限を持つ現行ユーザーを使用してください。

### 実行先マシン {#troubleshooting}

選択したコンピューターまたはワークスペースは、Droidが調査を実行する場所です。チャンネル設定で**Machine Type**を選択し、対象の**Computer**または**Workspace**を指定します。Auto-Runを有効にするには、事前に実行先を選択しておく必要があります。

実行先は次の条件を満たしている必要があります。

- 関連するリポジトリにアクセスできる
- 必要なパッケージマネージャーや CLI がインストールされている
- 観測、インシデント管理、ソース管理システムへ認証済みでアクセスできる
- RCA中にDroidが実行する可能性のあるアクションに対して安全な権限が設定されている

インシデントワークフローが事前設定済みツールを備えた永続環境に依存する場合は、[[jp/cli/features/droid-computers|Droid Computers]] を使用してください。

Bring Your Own Machine (BYOM) のコンピューターを選択すると、マシン情報を含むセッション出力がSlackチャンネルに投稿される可能性があることをFactoryが警告します。

### 公開範囲とモデル {#see-also}

プライベートセッションはセッション所有者だけが閲覧できます。組織に表示されるセッションは他のメンバーも確認できるため、インシデントの引き継ぎやポストモーテムレビューに役立ちます。

チームでインシデント分析用に明確な好みがない限り、モデルはデフォルトのまま使ってください。複雑な本番インシデントでは、利用可能であればより推論能力の高いモデルを選んでください。

## インシデントフローの仕組み {#h11-21a75e40}

設定後、インシデント対応は次の流れで動作します。

1. アラートbotが、設定済みのSlackチャンネルにトップレベルのメッセージを投稿します。
2. Factoryが、そのチャンネルの実行主体、対象マシン、公開範囲、モデル、プロンプトを使ってDroidセッションを開始します。
3. DroidがSlackアラートのコンテキストを受け取り、一致する `incident-guidelines` runbookガイダンスがあるか確認します。
4. Droidは設定済みツールを使って調査し、RCAが適切な場合は `/incident` ワークフローを呼び出すべきです。
5. FactoryはステータスとセッションリンクをSlackに投稿し、Droidは類似インシデント向けに再利用可能な知見を保存できます。

`incident-guidelines` runbookは、チームで再利用する場合は `.factory/skills/incident-guidelines/SKILL.md`、個人で再利用する場合は `~/.factory/skills/incident-guidelines/SKILL.md` にローカルで保存されます。ここには再利用可能な調査ガイダンスを保存し、シークレットや単発のRCA詳細は保存しないでください。

## トラブルシューティング {#h12-9df83831}





<Details summary="SlackチャンネルがFactoryに表示されない">
`/invite @Factory`でFactoryをチャンネルに招待してから、Slack設定を更新するか `/setup-incident-response` を再実行してください。プライベートチャンネルでは、明示的にFactoryを招待する必要があります。
</Details>



  

<Details summary="チャンネル設定を有効化または編集できない">
Slack自動実行設定を構成するには、FactoryのManagerまたはOwnerロールが必要です。組織オーナーに依頼してロールを更新してもらうか、セットアップを代行してもらってください。
</Details>



  

<Details summary="Auto-Runを有効にできない">
チャンネルにコンピューターまたはワークスペースが選択されていることを確認してください。**Run as** がサービスアカウントに設定されている場合、そのサービスアカウントが少なくとも1台のコンピューターを所有している必要があります。
</Details>



  

<Details summary="テストメッセージ後にセッションが始まらない">
そのメッセージが、設定済みチャンネル内のトップレベルアラートであり、スレッド返信ではないことを確認してください。インシデントセットアップフローでは、アラートbotのメッセージが想定トリガーです。
</Details>



  

<Details summary="Droidは起動するが問題を調査できない">
選択したマシンに、適切なリポジトリ、ツール、認証情報があることを確認してください。Droidが最初に使うべきrunbookやダッシュボードへのリンクを、チャンネルプロンプトに追加してください。
</Details>



  

<Details summary="RCA が一般的すぎる">
サービス名、アラートソース、ダッシュボードリンク、ログクエリ例、リポジトリパス、期待する RCA 形式など、チャンネル固有の情報をプロンプトに追加してください。
</Details>





## 関連項目 {#h13-c98af9d0}

- [[jp/integrations/slack|Slack連携]] -- FactoryをSlackに接続し、チャンネルにFactoryを招待します。
- [[jp/cli/user-guides/auto-run|自律レベル]] -- 繰り返し承認なしでDroidがどのように動作するかを理解します。
- [[jp/cli/features/droid-computers|Droid Computers]] -- 調査用の永続環境を設定します。
- [[jp/cli/configuration/skills|スキル]] -- インシデント調査のような再利用可能ワークフローがDroidをどのように導くかを学びます。
