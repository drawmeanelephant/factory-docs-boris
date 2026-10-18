---
id: jp/web/missions
title: "Desktop/Webでの実行"
status: published
summary: "Factory MissionsをDesktopおよびWebアプリで使って、構造化されたオーケストレーションにより複数機能にまたがる大規模プロジェクトを計画・実行します。"
parent: jp/web/index
tags: [factory-missions, missions, web, desktop, orchestration]
relations: [relates_to=web/missions]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Desktop/Webでの実行</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Factory MissionsをDesktopおよびWebアプリで使って、構造化されたオーケストレーションにより複数機能にまたがる大規模プロジェクトを計画・実行します。</p>




<div class="factory-frame">

<div style="background-color:#f4f4f5; padding:0.25rem; border-radius:0.5rem">
<img src="../../images/mission-web.png" alt="Mission Controlのオーケストレーション画面" style="border-radius:0.25rem" />
  </div>

</div>



## Mission Control ダッシュボード {#the-mission-control-dashboard}

Missions は CLI から実行することもできますが、Factory Desktop と Web アプリケーションでは、視覚的で情報量の多い Mission Control ダッシュボードを利用できます。このインターフェースは、あなたがプロジェクトマネージャーとして動けるよう設計されており、オーケストレーター、ワーカー、バリデーターが何をしているのかをより明確に把握できます。

## ミッションの開始と再開 {#starting-and-resuming-missions}

- **新しいミッションを開始:** 新しいセッションを作成するときに **Mission mode** を選ぶか、Mission Control ページから直接ミッションを開始できます。
- **過去のミッションを続行:** [Mission Control タブ](https://app.factory.ai/missions)に移動すると、過去のミッションを見つけて現在の状態を確認し、中断した場所からそのまま実行を再開できます。
- **リモートマシンで実行:** ミッションの開始時に、ターゲット環境として **Droid Computer** を選択できます。これにより、長時間実行されるミッションを、ローカルのワークスペースを占有せず、永続的なリモートマシン上のバックグラウンドで安全に実行できます。

## UIの見方 {#navigating-the-ui}

Mission Control ダッシュボードでは、マルチエージェントのワークフローをリアルタイムで可視化できます。

- **進捗の追跡:** ここまでに何が行われたかを正確に確認できます。上部バーには全体の時間とクレジットが表示され、右サイドバーには各ワーカーとマイルストーンの進捗ログがリアルタイムで表示されます。
- **モデルの選択:** 右サイドバーのモデルドロップダウンを使って、オーケストレーター、ワーカー、バリデーターの各エージェントに異なるモデルをその場で設定できます。
- **機能の確認:** メインビューには、アクティブなマイルストーンの概要が表示されます。任意の機能を掘り下げて、個別の検証基準やコミットを確認できます。
- **ワーカーの確認:** 左サイドバーには、アクティブなワーカーと完了済みのワーカーが一覧表示されます。特定のワーカーを選択すると、詳細なターミナル出力、思考プロセス、完了したサブタスクを確認できます。
- **介入とリダイレクト:** ミッションが行き詰まっているように見える場合や優先順位が変わった場合は、UI から直接オーケストレーターを一時停止し、再評価や再計画を指示したうえで実行を再開できます。

## 関連項目 {#see-also}

- [[jp/features/missions/overview|Factory Missions 概要]] -- コンセプトと Factory Missions の動作の仕組み
- [[jp/features/missions/planning|計画と検証]] -- 事前プランを正しく組み立てる
- [[jp/cli/features/missions/running-cli|CLIでの実行]] -- ターミナルから実行を監視・操作する
- [[jp/features/missions/troubleshooting|トラブルシューティング]] -- 停止したミッション、詰まったワーカー、ブロックされたマイルストーンから復旧する
- [[jp/features/missions/reference|設定とリファレンス]] -- ヘッドレス実行、設定、組織ポリシー
