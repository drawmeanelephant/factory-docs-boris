[Factory](https://www.factory.ai/news/legacy-bench) が提供する、COBOL、Java 7、BASIC、C89、Fortran、Assembly にまたがるレガシーエンジニアリングタスクでの AI エージェント性能を測定するベンチマークです。

### 結果 — 総合合格率 {#legacy-bench-sec-1-15b4b34c}
<div class="factory-chart">
  <div class="factory-chart-header"><span class="factory-chart-title">Legacy Bench</span><span class="factory-chart-axis">Accuracy (%)</span></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (GPT-5.3 Codex)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:42.5%"></div></div><div class="factory-chart-val">42.5%</div></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (GPT-5.4)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:40.7%"></div></div><div class="factory-chart-val">40.7%</div></div>
  <div class="factory-chart-row"><div class="factory-chart-label">Codex CLI (GPT-5.4)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:40.1%"></div></div><div class="factory-chart-val">40.1%</div></div>
  <div class="factory-chart-row"><div class="factory-chart-label">Codex CLI (GPT-5.3 Codex)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:39.4%"></div></div><div class="factory-chart-val">39.4%</div></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (Gemini 3.1 Pro)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:38.7%"></div></div><div class="factory-chart-val">38.7%</div></div>
  <div class="factory-chart-row"><div class="factory-chart-label">Gemini CLI (Gemini 3.1 Pro)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:36.0%"></div></div><div class="factory-chart-val">36.0%</div></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (Claude Opus 4.6)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:34.6%"></div></div><div class="factory-chart-val">34.6%</div></div>
  <div class="factory-chart-row"><div class="factory-chart-label">Claude Code (Claude Opus 4.6)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:33.0%"></div></div><div class="factory-chart-val">33.0%</div></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (GLM-5)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:32.2%"></div></div><div class="factory-chart-val">32.2%</div></div>
  <div class="factory-chart-row"><div class="factory-chart-label">Cursor (Composer 2)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:31.0%"></div></div><div class="factory-chart-val">31.0%</div></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (Gemini 3 Flash)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:27.2%"></div></div><div class="factory-chart-val">27.2%</div></div>
  <div class="factory-chart-row factory-chart-row--highlight"><div class="factory-chart-label">Factory Droid (Kimi K2.5)</div><div class="factory-chart-track"><div class="factory-chart-fill" style="width:16.9%"></div></div><div class="factory-chart-val">16.9%</div></div>
</div>

*最終更新: 2026年4月*

### 方法論 {#legacy-bench-sec-2-8892b68e}
| 項目 | 説明 |
|------|------|
| **タスクセット** | 6 つのレガシー言語ファミリーにまたがる数百件のタスクと、代表的な 10 件の公開サンプル |
| **タスク形式** | 自然言語の指示、コンテナ化されたソース環境、参照実装、非公開の検証テスト |
| **タスク種別** | バグ修正、実装、移行、その他のレガシーエンジニアリング作業 |
| **評価** | 仕様理解、動作するコードの生成、検証通過をエージェントに求める Harbor 互換タスク |
| **スコアリング** | 12 のモデル・エージェント組み合わせにおける非公開テストの合格率 |

### ベンチマーク構成 {#legacy-bench-sec-3-0d3a458a}
| 言語 | 割合 | 代表的な分野 |
|------|------|--------------|
| **COBOL** | 46% | 金融決済、給与処理、保険請求、通信課金、VSAM ファイル処理 |
| **Java 7** | 32% | エンタープライズミドルウェア、CDR 処理、倉庫物流、バイナリ解析、EJB パターン |
| **BASIC** | 6% | 業務アプリケーション、会計、データ処理 |
| **C89** | 5% | システムプログラミング、低レベルデバッグ、プロトコル実装 |
| **Fortran** | 5% | 科学技術計算、数値計算、物理シミュレーション |
| **Assembly** | 5% | x86 ファームウェア解析、プロトコルデコード、ハードウェアシミュレーション |

Java 7 のバグ修正では、コンパイラとランタイムのフィードバックによってエラーが表面化しやすいため、エージェントは最も高いスコアを記録しています。一方で最も難しいのは COBOL で、どのモデルも解けなかった 44 件のタスクのうち 31 件を COBOL が占めています。

<div class="factory-card">

**[Legacy-Bench](https://github.com/factory-ai/legacy-bench)**

GitHub でサンプルタスクと評価ハーネスを見る

</div>

<div class="factory-card">

**[解説を読む](https://www.factory.ai/news/legacy-bench)**

Legacy-Bench: AI エージェントは世界で最も重要なソフトウェアを保守できるのか？

</div>
