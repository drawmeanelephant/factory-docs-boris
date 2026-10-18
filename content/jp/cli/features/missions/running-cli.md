---
id: jp/cli/features/missions/running-cli
title: "CLIでの実行"
status: published
summary: "プランが承認されると、Droid は Mission Control に入ります。ターミナルから進捗を監視し、ワーカーのブロックを解除し、オーケストレーターをリダイレクトします。"
parent: jp/cli/features/missions/index
tags: [factory-missions, missions, mission-control, orchestrator, intervene, redirect, cli]
relations: [relates_to=cli/features/missions/running-cli]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">CLIでの実行</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">プランが承認されると、Droid は Mission Control に入ります。ターミナルから進捗を監視し、ワーカーのブロックを解除し、オーケストレーターをリダイレクトします。</p>


## Mission Control での作業 {#working-with-mission-control}

プランが承認されると、Droid は実行を管理するオーケストレーションビューである Mission Control に入ります。ここから機能とマイルストーンの進捗を追跡し、どのエージェントが何に取り組んでいるかを確認し、調整が必要な時に介入できます。



<Aside kind="tip">
視覚的なダッシュボードをご希望ですか？ Desktop および Web アプリではより豊富な Mission Control 体験が利用できます。[[jp/web/missions|Desktop/Webでの実行]] を参照してください。
</Aside>



## 介入とリダイレクト {#intervening-and-redirecting}

Factory Missions は設定したら放置するものではありません。オーケストレーターはエージェントであり、会話することができます。Factory Missions を最も効果的に使用する方法は、自分をプロジェクトマネージャーとして扱うことです - 進捗を監視し、ワーカーのブロックを解除し、プランの変更が必要な時にリダイレクトします。

問題が起きたとき（ミッションが停止する、ワーカーやマイルストーンが詰まる、方向転換が必要になるなど）は、オーケストレーターを一時停止し、見えている状況を伝えます。よくあるシナリオと例文については [[jp/features/missions/troubleshooting|トラブルシューティング]] を参照してください。

## 新しい種類のデバッグ {#a-new-kind-of-debugging}

Factory Missions で作業するスキルセットは、従来のデバッグというよりも**エージェントのプロジェクト管理**に近いものです。コードを1行ずつステップ実行するのではなく、ワーカーチームを監視し、詰まった時にブロックを解除し、優先順位が変わった時にリダイレクトし、押し通すか再計画するかの判断を下します。

これは AI との意味的に異なる作業方法です。核となるスキルは、いつどのように介入するかを知ることであり、自分でコードを書くことではありません。

## 関連項目 {#see-also}

- [[jp/web/missions|Desktop/Webでの実行]] -- 視覚的な Mission Control ダッシュボード
- [[jp/features/missions/reference|設定とリファレンス]] -- ヘッドレス実行、設定、組織ポリシー
- [[jp/features/missions/planning|計画と検証]] -- 事前プランを正しく組み立てる
