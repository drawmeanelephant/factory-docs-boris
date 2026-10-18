---
id: jp/cli/features/droid-control
title: "Droid Control"
status: published
summary: "ターミナル、ブラウザ、デスクトップの自動化。デモの記録、動作検証、QAフローの実行。"
parent: jp/cli/features/index
tags: [cli, droid-control, automation, demo, verify, qa-test, terminal, browser]
relations: [relates_to=cli/features/droid-control]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Droid Control</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">ターミナル、ブラウザ、デスクトップの自動化。デモの記録、動作検証、QAフローの実行。</p>


Droid Controlは、Droidsがソフトウェアを*操作*できるようにします：アプリの起動、コマンドの入力、ボタンのクリック、動作の記録、そして洗練された動画証拠の生成を行います。Droidsによって、Droidsのために作られました。



<div class="factory-frame">

<video autoplay muted loop playsinline>
<source src="../../../images/features/droid-control-hero.mp4" type="video/mp4" />
  </video>

<div class="factory-frame-caption">この動画は完全にDroidによって計画、記録、レンダリングされました。</div>

</div>



## 提供される機能 {#what-you-get}



<div class="factory-card-group">

<div class="factory-card">

**主張の検証**

動作に関する主張が真実かどうかをテストし、いずれの場合も証拠を生成します。演出も偏見もなく、ただ調査のみを行います。

</div>


  

<div class="factory-card">

**QAフローの実行**

ターミナルCLI、Webアプリ、またはElectronアプリをエンドツーエンドフローで操作します。注釈付きスクリーンショットで合格/不合格を報告します。

</div>


  

<div class="factory-card">

**デモの記録**

タイトルカード、キーストロークオーバーレイ、ウィンドウクロームを含む、PRの洗練されたビフォーアフター比較動画を生成します。

</div>

</div>



## 始め方 {#get-started}



<div class="factory-tabs">

<div class="factory-tab-panel">

<div class="factory-tab-heading">UI</div>

Droidセッションで`/plugins`を実行し、**Browse**タブに移動して**droid-control**を見つけ、インストールしてください。

</div>


  

<div class="factory-tab-panel">

<div class="factory-tab-heading">CLI</div>

```bash
droid plugin marketplace add https://github.com/Factory-AI/factory-plugins
droid plugin install droid-control@factory-plugins --scope user
```

</div>

</div>



動画レンダリングの場合、プラグイン追加後にRemotionの依存関係を一度インストールする必要があります：
```bash
droid plugin list --scope user
cd <plugin-path>/remotion && npm install
```


<Aside kind="note">
使用ケースに応じてランタイムツール（tuistory、agent-browser、ffmpeg など）も必要です。使用ケース別のインストールコマンドについては[[jp/cli/features/droid-control#prerequisites|前提条件]]を参照してください。
</Aside>



## コマンド {#commands}

Droid Controlは3つのスラッシュコマンドを追加します。それぞれが計画、実行、記録、報告という全ワークフローをエンドツーエンドで処理します。



<div class="factory-tabs">

<div class="factory-tab-panel">

<div class="factory-tab-heading">/demo</div>

機能やPRのデモ動画を記録します。

```
    /demo pr-1847
```
PRの番号、GitHub URL、またはフリーテキストの説明を受け付けます。比較PRはデフォルトでサイドバイサイドレイアウトになり、新機能は単一ブランチになります。

追加の調整用フラグを追加します：
```
    /demo pr-1847 -- showcase, keys
```
| Flag | Effect |
|------|--------|
| `showcase` | 暖かい背景とフィルムグレインを使用したシネマティックプリセット |
| `keys` | ユーザーアクションを表示するキーストロークオーバーレイピル |

#### 仕組み {#how-it-works}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">変更を理解する</div>

PRの説明、差分、リンクされたチケットを取得します。各変更について、証明すべき内容と閲覧者が混乱する可能性のある要素を特定します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">インタラクションを計画する</div>

機能が動作することを可視的に証明するアクションシーケンスをスクリプト化します。両方のブランチで同じインタラクションを実行するため、動作のみが異なります。計画を提示し、録画前にあなたの承認を待ちます。

</div>


  

<div class="factory-step">

<div class="factory-step-title">両方のブランチをキャプチャする</div>

ワーカーサブエージェントを使用して、ベースラインブランチと候補ブランチで並行して録画セッションを開始します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">動画を合成する</div>

Remotionを使用してタイトルカード、ウィンドウクローム、エフェクトを含む洗練された動画をレンダリングします。シネマティック（`factory`）から実用的（`minimal`）まで6つのビジュアルプリセットがあります。

</div>


  

<div class="factory-step">

<div class="factory-step-title">出力を検証する</div>

配信前に最終動画が元のコミットメントに対して適合しているかチェックします。

</div>

</div>

</div>




<div class="factory-tab-panel">

<div class="factory-tab-heading">/verify</div>

特定の動作クレームをテストし、証拠とともに結果を報告します。
```
    /verify "ESC cancels streaming in bash mode"
```
PRリファレンスをオプションのクレームと共に受け付けます：
```
    /verify 11386 -- the fork flag creates a new session
```
PR番号のみが与えられた場合、DroidはPRを取得し、最も重要なテスト可能な主張を特定します。



<Aside kind="tip">
ドロイドは**調査官**として位置づけられており、擁護者ではありません。主張が偽である場合、それは有効な発見です。偽造防止ルールにより、期待される結果に合わせた証拠の演出は防がれています。
</Aside>



#### 動作の仕組み {#how-it-works-2}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">テスト内容を決定</div>

観察すべき特定の動作と必要な証拠のタイプを特定します：機能的な主張にはテキストスナップショット、視覚的な主張にはスクリーンショット、エンコーディングの主張には生バイトキャプチャを使用します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">証拠をキャプチャ</div>

アプリを起動し、動作を実証する最小限のインタラクションシーケンスを実行して、結果をキャプチャします。動作が主張と矛盾する場合、それは証拠であり、エラーではありません。

</div>


  

<div class="factory-step">

<div class="factory-step-title">発見を報告</div>

**CONFIRMED**、**REFUTED**、または**INCONCLUSIVE**の結論とともに、キャプチャされたすべての証拠をインラインで含む構造化されたレポートを提供します。

</div>

</div>

</div>




<div class="factory-tab-panel">

<div class="factory-tab-heading">/qa-test</div>

ターミナルCLI、Webアプリ、またはElectronアプリに対して自動化されたQAを実行します。
```
    /qa-test https://app.example.com -- login, create a project, invite a member
```
CLI コマンド、Electronアプリ名、PR参照、または自由記述も可能です。`--` 以降のテストステップは任意です。何も提供されない場合、Droidが適切なフローを設計します。

#### 仕組み {#how-it-works-3}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">テストプランを定義</div>

対象（ウェブ、ターミナル、またはElectron）を決定し、指示やアプリのUIからテストステップを設計し、各ステップで取得すべき証拠を特定します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">フローを実行</div>

アプリを起動して各ステップを実行し、スクリーンショット（ブラウザ）やテキストスナップショット（ターミナル）を途中で取得します。ステップが失敗した場合は、失敗を記録して最大限のカバレッジのために続行します。

</div>


  

<div class="factory-step">

<div class="factory-step-title">結果をレポート</div>

インライン証拠付きのステップレベルの合格/不合格テーブルと、発見された問題の要約を提供します。

</div>

</div>

</div>

</div>



### 出力例 {#example-output}

以下のビデオはすべてDroidによって計画、録画、レンダリングされました。



<div class="factory-tabs">

<div class="factory-tab-panel">

<div class="factory-tab-heading">CLI: シングルブランチ</div>



<div class="factory-frame">

<video autoplay muted loop playsinline>
<source src="../../../images/features/droid-control-demo-single.mp4" type="video/mp4" />
</video>

<div class="factory-frame-caption">/cwd コマンドのデモ。Factoryプリセット、シングルブランチレイアウト。</div>

</div>



</div>


  

<div class="factory-tab-panel">

<div class="factory-tab-heading">CLI: 変更前/後</div>



<div class="factory-frame">

<video autoplay muted loop playsinline>
<source src="../../../images/features/droid-control-demo-comparison.mp4" type="video/mp4" />
</video>

<div class="factory-frame-caption">bashモード出力リデザインの変更前/後比較。Factoryプリセット、サイドバイサイドレイアウト。</div>

</div>



</div>


  

<div class="factory-tab-panel">

<div class="factory-tab-heading">ウェブ: シングルブランチ</div>



<div class="factory-frame">

<video autoplay muted loop playsinline>
<source src="../../../images/features/droid-control-web-single.mp4" type="video/mp4" />
</video>

<div class="factory-frame-caption">ウェブアプリのブラウザ自動化デモ。Droidによって録画・レンダリング。</div>

</div>



</div>


  

<div class="factory-tab-panel">

<div class="factory-tab-heading">ウェブ: 変更前/後</div>



<div class="factory-frame">

<video autoplay muted loop playsinline>
<source src="../../../images/features/droid-control-web-comparison.mp4" type="video/mp4" />
</video>

<div class="factory-frame-caption">ウェブアプリ変更の変更前/後比較。サイドバイサイドレイアウト。</div>

</div>



</div>

</div>



## 自動化ドライバー {#automation-drivers}

Droid Controlは4つの自動化バックエンドをサポートしています。対象に基づいて適切なものが自動的に選択されます。



<div class="factory-card-group">

<div class="factory-card">

**tuistory**

**仮想PTY自動化。** ターミナル作業のデフォルト。asciinema録画と強制トゥルーカラー出力を備えたPlaywright風CLI。

</div>


  

<div class="factory-card">

**true-input**

**リアルターミナルエミュレーター。** ヘッドレスWaylandコンポジター（Linux）、KVM/QEMU（Windows）、またはQEMUモニター（macOS）。実際のレンダリング証拠が必要な場合に使用。

</div>


  

<div class="factory-card">

**agent-browser**

**ウェブとElectronアプリ。** Chrome DevTools Protocolサポートを備えたPlaywrightベースのCLI。ページをナビゲートし、フォームを記入し、ボタンをクリックし、スクリーンショットを取得。

</div>


  

<div class="factory-card">

**desktop-control**

**ネイティブデスクトップアプリ。** [trycua/cua](https://github.com/trycua/cua) の `cua-driver` によるアクセシビリティツリーのスナップショット、要素またはピクセル単位の操作、ウィンドウごとのスクリーンショットを、フォーカスを奪わずに実行できます。macOSとWindowsは本番対応、Linuxはプレリリースです。

</div>

</div>



## ビデオレンダリング {#video-rendering}

デモとショーケースビデオは、Reactベースのビデオエンジンである[Remotion](https://www.remotion.dev/)でレンダリングされます。プラグインには23の視覚コンポーネントと6つのプリセットが含まれています。





<Details summary="視覚プリセット">
| プリセット | 外観 | 最適な用途 |
|--------|------|----------|
| `factory` | 暖かい黒、信号機、アンバーグロー | 公式Factoryコンテンツ |
| `factory-hero` | 同上 + グラデーション背景 | ランディングページ、ソーシャル |
| `hero` | クールなグラデーション、余裕のあるマージン | Factory以外のマーケティング |
| `macos` | ダーク、クリーンなフレーム | 汎用デモ |
| `presentation` | 黒、余裕のあるマージン | スライドデッキ、発表 |
| `minimal` | ウィンドウバーなし、タイトなマージン | ドキュメント埋め込み、インラインクリップ |
</Details>


  

<Details summary="自動レイヤー（常に存在）">
- 暖かい放射状背景、浮遊パーティクル、フィルムグレインオーバーレイ、カラーグレーディング
  - 設定可能なタイトル-コンテンツ遷移（`motion-blur`, `flash`, `whip-pan`, `light-leak`, `glitch-lite`）
  - 信号機とガラスモーフィックボーダー付きアニメーションウィンドウクローム
  - 自動スケールタイトル/サブタイトルテキスト
</Details>


  

<Details summary="エフェクトレイヤー（合成時に選択）">
- 特定の領域をハイライトするスポットライトオーバーレイ
  - 小さなテキストや詳細のための指向性ズーム
  - ユーザーアクションを表示するキーストロークピル
  - セクションヘッダーと遷移スイープ
  - ソース変更オーバーレイのシンタックスハイライトされたコード注釈
</Details>





## アーキテクチャ {#architecture}

プラグインは3つのレイヤーからなる構成アーキテクチャを使用しています：

- **オーケストレーター** -- 各リクエストを3つの独立したルックアップ（対象、ステージ、アーティファクト）を通じてルーティングし、読み込むスキルを決定します。
- **11のアトムスキル** -- オンデマンドで読み込まれる自己完結型の背景知識で、ドライバー、対象、ステージ、ポリッシュに分割されています。
- **3つのコマンド** -- 引数をコミットメントに解析し、ハイブリッドハンドオフを介してアトムに委任します。

すべてのワークフローは**キャプチャ → 合成 → 検証**を通じて流れます。コマンドは*何を*生成するかを宣言し、アトムが*どのように*行うかを所有します。スキルはハードコードされたパイプラインではなく明示的なハンドオフを通じてチェーンするため、droidは自然にフローに従います。



<div class="factory-card">

**[アーキテクチャの詳細](https://github.com/Factory-AI/factory-plugins/blob/master/plugins/droid-control/ARCHITECTURE.md)**

設計の根拠：droidのためのUX、ウォーターフォールルーティング、タスク委任、ハイブリッドハンドオフ。

</div>



## 前提条件 {#prerequisites}

使用ケースに必要なもののみをインストールしてください。





<Details summary="ターミナルデモ（tuistory）">
```bash
npm install -g tuistory                                # virtual PTY driver
pip install asciinema                                   # terminal recording
cargo install --git https://github.com/asciinema/agg   # .cast → .gif converter
sudo apt-get install -y ffmpeg                          # video processing
```
</Details>


  

<Details summary="Web/Electronの自動化 (agent-browser)">
```bash
agent-browser install   # downloads Chromium
```
</Details>


  

<Details summary="ネイティブデスクトップアプリ（desktop-control）">
```bash
curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh | bash
cua-driver skills install   # upstream skill pack (deep tool reference)
```
WindowsではPowerShellで `irm https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.ps1 | iex` を実行してインストールします。macOSでは追加で `cua-driver permissions grant`（アクセシビリティ + 画面収録）が必要です。
</Details>


  

<Details summary="実際のターミナルエミュレータ（true-input）">
| プラットフォーム | 必要なツール |
|----------|----------------|
| Linux/Wayland | `cage`、`wtype`、Wayland対応ターミナル |
| Windows (KVM) | `libvirt`、`qemu`、SSH対応KVM VM |
| macOS (QEMU) | `qemu`、`socat`、SSH対応macOS VM |
</Details>


  

<Details summary="ビデオ合成（showcase）">
Node.js >= 18、Chrome/Chromium、`ffmpeg`、`ffprobe`、`agg`が必要です。
</Details>





## 関連項目 {#see-also}



<div class="factory-card-group">

<div class="factory-card">

**[ソースコード](https://github.com/Factory-AI/factory-plugins/tree/master/plugins/droid-control)**

完全なプラグインソース：スキル、コマンド、スクリプト、Remotionコンポーネント。

</div>


  

<div class="factory-card">

**[[jp/cli/configuration/plugins|プラグイン]]**

プラグインの仕組み、インストール方法、独自プラグインの構築方法を学ぶ。

</div>


  

<div class="factory-card">

**[[jp/guides/skills/automated-qa|自動QAスキル]]**

CI統合、障害学習、構造化レポートによる高度なQA自動化。

</div>


  

<div class="factory-card">

**[README](https://github.com/Factory-AI/factory-plugins/blob/master/plugins/droid-control/README.md)**

クイックスタート、コマンドリファレンス、前提条件。

</div>

</div>
