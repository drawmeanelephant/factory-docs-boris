---
id: jp/web/factory-router
title: "Factory Router"
status: published
summary: "各タスクに最適なモデルを自動的に選択します。"
parent: jp/web/index
tags: [web, factory-router]
relations: [relates_to=web/factory-router]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Factory Router</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">各タスクに最適なモデルを自動的に選択します。</p>


Factory Routerは、各Droidタスクに最適なモデルを自動的に選択します。セッションごとに単一のモデルを毎回手動で選ぶ代わりに、Factory Routerがタスクを評価し、品質、レイテンシ、コストのバランスが最もよいモデルに作業をルーティングします。

Factory RouterはFactory CLIとFactory Appで利用でき、他のモデルと同じエンタープライズ制御で動作します。

## Factory Routerを使う理由 {#why-use-factory-router}

Factory Routerは、ワークフローごとにモデル選択を手動で切り替えなくても高い成果を得たいチーム向けに設計されています。



<div class="factory-card-group">

<div class="factory-card">

**高性能をより低コストで**

Factory Routerは本番環境において、同じワークロードを最上位モデルの料金で換算した場合と比べて、Factoryの評価でフロンティア級の性能を維持しながら、集計ベースで **43%** のコスト削減を実現します。

</div>


  

<div class="factory-card">

**モデル選択の改善**

Droidは定型的なステップを高速または低コストのモデルにルーティングし、より深い推論が必要な作業には高性能なモデルを確保できます。

</div>


  

<div class="factory-card">

**エンタープライズ対応の制御**

Factory Routerは、Factoryプラットフォーム全体で使われている組織、プロジェクト、ユーザーレベルの同じモデル制御に従います。

</div>

</div>



## 提供状況 {#availability}

Factory Routerは、設定不要でFactory CLIとFactory Appのモデルセレクターから一般提供されています。

## エンタープライズ制御 {#enterprise-controls}

エンタープライズ管理者は、他のFactory対応モデルと同じモデルガバナンスシステムを通じてFactory Routerを管理でき、他のモデルと同様に組織レベルでFactory Routerを許可または制限できます。

モデルのエンタープライズ制御の詳細については、[[jp/enterprise/models-llm-gateways-and-integrations|モデル、LLM ゲートウェイ、インテグレーション]]を参照してください。

## FAQ {#faq}

### モデルルーティングはどのように動作しますか？ {#how-does-model-routing-work}

Factory Routerはタスク単位のルーターで、セッション単位のルーティングとリクエスト単位のルーティングを組み合わせて使用します。最適化では、プロンプトキャッシュの維持とコスト削減を強く考慮します。

### Factory Routerは設定できますか？ {#can-factory-router-be-configured}

Factory Routerは現在、他のモデルと同様に有効化または無効化できます。また、Factory Router向けのガイダンスとして Enterprise Controls も提供しています。

### Factory Routerのパフォーマンスに関するベンチマークはありますか？ {#are-there-benchmarks-on-factory-routers-performance}

はい。Factory Routerは、Terminal Bench 2 や Legacy Bench のような難易度の高いベンチマークでフロンティア級の性能を維持し、品質、レイテンシ、コストの最良のバランスを実現します。

### Factory Routerのコスト面での利点は何ですか？ {#what-are-the-cost-benefits-of-factory-router}

本番環境では、請求対象の利用量を同じワークロードの最上位モデル料金と比較すると、総コストは43%低くなります。中央値のセッションコストは81%低く、61%のセッションでは少なくとも80%安価です。その間も、Factory Routerは一貫してフロンティア級の性能を維持します。
