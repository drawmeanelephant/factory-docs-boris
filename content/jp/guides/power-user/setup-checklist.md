---
id: jp/guides/power-user/setup-checklist
title: "パワーユーザーセットアップチェックリスト"
status: published
summary: "IDE連携、メモリ、スキル、自動化を使ってDroidを最大限活用するための完全チェックリスト。"
parent: jp/guides/power-user/index
tags: [guides, power-user, setup, checklist, configuration, optimization, productivity, best-practices]
relations: [relates_to=guides/power-user/setup-checklist]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">パワーユーザーセットアップチェックリスト</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">IDE連携、メモリ、スキル、自動化を使ってDroidを最大限活用するための完全チェックリスト。</p>


このチェックリストは、基本的なDroidインストールを完全に最適化された開発環境に変換します。各セクションは前のセクションをベースに構築されているため、最良の結果を得るためには順番通りに完了してください。



<Aside kind="note">
分けて進めたい場合は、各セクションを個別に実行できます。
</Aside>





<Aside kind="info">
**Factory Appを使用していますか？** このガイドの大部分はDroid CLIと[[jp/web/getting-started/overview|Factory App]]の両方に適用されます。体験が異なる箇所では、Factory App固有の方法を記載しています。
</Aside>



---

## レベル1：基本セットアップ {#level-1-essential-setup}

これらの基盤となる項目は、最大の即時効果をもたらします。



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Factory IDEプラグインをインストール</div>

IDEプラグインは、開いているファイル、エラー、選択範囲などのリアルタイムコンテキストを提供し、Droidがあなたと同じものを見られるようにします。

**VSCode/Cursor:**
  1. Extensionsを開きます（`Cmd+Shift+X`）
  2. Search "Factory"
  3. インストールして再読み込みします

**確認:** `droid`を実行し、ステータスバーに"IDE connected"が表示されることを確認します。

</div>



  

<div class="factory-step">

<div class="factory-step-title">AGENTS.mdを作成</div>

リポジトリルートに基本的な[[jp/cli/configuration/agents-md|AGENTS.md]]を作成します:

```markdown
# Project Guidelines

## Build & Test
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint`

## Code Style
- Use TypeScript strict mode
- Prefer functional components in React
- Write tests for new features
```

最小構成から始め、作業しながら拡張します。その他の例は[[jp/cli/configuration/agents-md|AGENTS.mdガイド]]を参照してください。

</div>



  

<div class="factory-step">

<div class="factory-step-title">デフォルトモデルを設定</div>

設定で使用するモデルを設定します:

**CLI:**
```bash
droid
> /settings
# Navigate to Model and select your default
```

**Factory App:** チャットインターフェースのモデルセレクタードロップダウンを使用します。

**推奨:** 複雑な作業ではClaude Opus 4.5（デフォルト）から始め、定型作業ではHaiku 4.5またはGPT-5.1-Codexに切り替えます。

</div>

</div>





<Aside kind="tip">
**チェックポイント:** これでIDE連携、基本的なプロジェクトコンテキスト、使用するモデルが設定されました。
</Aside>



---

## レベル2：メモリ＆コンテキスト {#level-2-memory-context}

永続的なメモリを構築し、Droidがセッション間であなたの設定を記憶できるようにします。



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">memoriesファイルを作成</div>

個人の好み用に`~/.factory/memories.md`を作成します:

```markdown
# My Development Preferences

## Code Style
- I prefer arrow functions over function declarations
- I like early returns over nested conditionals
- I use 2-space indentation

## Testing
- I use React Testing Library, not Enzyme
- I prefer integration tests over unit tests for components
- Mock external APIs, not internal modules

## Past Decisions
- [2024-01] Chose Zustand over Redux for state management
- [2024-02] Using Tailwind CSS for styling
```

Droidに同じ指示を繰り返していると気づいたら、このファイルを更新してください。

</div>



  

<div class="factory-step">

<div class="factory-step-title">AGENTS.mdでmemoriesを参照</div>

`AGENTS.md`に追加します:

```markdown
## Personal Preferences
Refer to `~/.factory/memories.md` for my coding preferences and past decisions.
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">プロジェクト固有のmemoriesを作成（任意）</div>

チームプロジェクトでは`.factory/memories.md`を作成します:

```markdown
# Project Memories

## Architecture Decisions
- We use the repository pattern for data access
- All API routes go through the /api/v1 prefix
- Feature flags are managed via LaunchDarkly

## Known Issues
- The auth service has a 5-second timeout issue (#123)
- Legacy users table uses snake_case columns
```

</div>

</div>





<Aside kind="tip">
**チェックポイント:** Droidは、あなたが繰り返さなくても好みとプロジェクト履歴にアクセスできるようになりました。
</Aside>





<Aside kind="tip">
**メモリ記録を自動化したいですか？** "remember this:"と言ったときにメモリを自動保存するフックを設定します。セットアップ手順は[[jp/guides/power-user/memory-management#automatic-memory-capture|メモリ管理]]を参照してください。
</Aside>



---

## レベル3：ルール＆規約 {#level-3-rules-conventions}

コーディング標準を整理し、Droidが一貫してそれらに従うようにします。



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">ルールディレクトリを作成</div>

プロジェクトに`.factory/rules/`を作成します:

```
.factory/
└── rules/
    ├── typescript.md
    ├── testing.md
    └── security.md
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">TypeScriptルールを追加</div>

`.factory/rules/typescript.md`を作成します:

```markdown
# TypeScript Conventions

## General
- Use `interface` for object types, `type` for unions/intersections
- Avoid `any` - use `unknown` with type guards instead
- Export types alongside their implementations

## React Components
- Use functional components with TypeScript FC type
- Props interfaces should be named `{ComponentName}Props`
- Use `React.ReactNode` for children, not `React.ReactChild`

## Imports
- Group imports: React, external libs, internal modules, types
- Use absolute imports from `@/` prefix
- Avoid barrel files (index.ts re-exports) for performance
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">テストルールを追加</div>

`.factory/rules/testing.md`を作成します:

```markdown
# Testing Conventions

## File Organization
- Test files live next to source: `Component.tsx` → `Component.test.tsx`
- Integration tests go in `__tests__/integration/`
- E2E tests go in `e2e/`

## Test Structure
- Use descriptive test names: "should [action] when [condition]"
- One assertion per test when possible
- Use `beforeEach` for common setup, not `beforeAll`

## Mocking
- Mock at the boundary (API calls, not internal functions)
- Use MSW for API mocking in integration tests
- Reset mocks in `afterEach`
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">AGENTS.mdでルールを参照</div>

`AGENTS.md`を更新します:

```markdown
## Coding Standards
Follow the conventions documented in:
- `.factory/rules/typescript.md` - TypeScript and React patterns
- `.factory/rules/testing.md` - Testing conventions
- `.factory/rules/security.md` - Security requirements
```

</div>

</div>





<Aside kind="tip">
**チェックポイント:** コーディング標準が文書化され、Droidが一貫して従うようになりました。
</Aside>





<Aside kind="tip">
**ルールを自動適用:** 編集後にリンターを実行するには[[jp/cli/configuration/hooks-guide|PostToolUseフック]]を使用します。例は[[jp/reference/hooks-reference|フックリファレンス]]を参照してください。
</Aside>



---

## レベル4：スキル＆自動化 {#level-4-skills-automation}

再利用可能なスキルと自動化フックを追加します。



<Aside kind="info">
**自動化する3つの方法:**
  - **[[jp/cli/configuration/skills|スキル]]** — Droidがタスクコンテキストに基づいて呼び出します
  - **[[jp/cli/configuration/hooks-guide|フック]]** — 特定イベントで自動実行されます
  - **[[jp/cli/configuration/custom-slash-commands|カスタムスラッシュコマンド]]** — `/command-name`で呼び出します
</Aside>





<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">プロンプト改善スキルを作成</div>

`~/.factory/skills/prompt-refiner/SKILL.md`を作成します:

```markdown
---
name: prompt-refiner
description: Improve prompts before sending them to get better results. Use when you want to refine a task description.
---

# Prompt Refiner

## Instructions

When the user wants to refine a prompt:

1. Ask for their draft prompt or task description
2. Analyze it for:
   - Clarity: Is the goal specific and measurable?
   - Context: Does it include relevant background?
   - Constraints: Are requirements and limitations stated?
   - 例: Would examples help clarify expectations?
3. Suggest an improved version with explanations
4. Offer to iterate if needed

## Good Prompt Patterns

- Start with the outcome: "Create a..." not "I want you to..."
- Include acceptance criteria: "The result should..."
- Specify format: "Return as JSON/markdown/code"
- Mention constraints: "Must be compatible with...", "Should not modify..."
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">自動整形フックを追加</div>

`/hooks`を実行し、自動整形用のPostToolUseフックを追加します:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Create|Edit|ApplyPatch",
        "hooks": [
          {
            "type": "command",
            "command": "cd \"$FACTORY_PROJECT_DIR\" && npx prettier --write \"$(jq -r '.tool_input.file_path' 2>/dev/null || echo '')\" 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
```

これにより、Droidが編集した後にファイルが自動整形されます。

</div>



  

<div class="factory-step">

<div class="factory-step-title">編集時テストフックを追加（任意）</div>

編集後に関連テストを実行します:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|ApplyPatch",
        "hooks": [
          {
            "type": "command",
            "command": "cd \"$FACTORY_PROJECT_DIR\" && jq -r '.tool_input.file_path' | xargs -I {} npm test -- --findRelatedTests {} --passWithNoTests 2>/dev/null || true"
          }
        ]
      }
    ]
  }
}
```

</div>

</div>





<Aside kind="tip">
**チェックポイント:** 再利用可能なスキルと自動整形/テストが設定されました。
</Aside>



---

## レベル5：トークン最適化 {#level-5-token-optimization}

品質を犠牲にすることなく、コスト効率を微調整します。



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">複雑な作業で仕様モードを有効化</div>

複数ファイルに触れる機能を始める前に`Shift+Tab`または`/spec`を使用します。これによりコストの高い手戻りを防げます。

</div>



  

<div class="factory-step">

<div class="factory-step-title">モデル切り替えを設定</div>

計画用に仕様モードモデルを設定します:

```bash
droid
> /settings
# Set Spec Mode Model to a reasoning-heavy model
```

計画にはOpus 4.5を使用し、実装にはSonnetまたはCodexを使用します。

</div>



  

<div class="factory-step">

<div class="factory-step-title">準備状況レポートを実行</div>

プロジェクトのAI準備状況を確認します:

**CLI:**
```bash
droid
> /readiness-report
```

**Factory App:** [[jp/web/agent-readiness/dashboard|Agent Readinessダッシュボード]]で準備状況スコアを確認します。

影響の大きい項目から対応します。lint、型チェック、高速テストはトークンの無駄を大幅に減らします。

</div>

</div>



---

## クイックリファレンス：ファイルの場所 {#quick-reference-file-locations}

| 目的 | 個人用 | プロジェクト用 |
|---------|----------|---------|
| **スキル** | `~/.factory/skills/<name>/SKILL.md` | `.factory/skills/<name>/SKILL.md` |
| **メモリ** | `~/.factory/memories.md` | `.factory/memories.md` |
| **ルール** | `~/.factory/rules/*.md` | `.factory/rules/*.md` |
| **設定** | `~/.factory/settings.json` | `.factory/settings.json` |
| **フック** | `~/.factory/hooks.json` | `.factory/hooks.json` |
| **エージェント指示** | `~/.factory/AGENTS.md` | `./AGENTS.md` |
| **カスタムdroid** | `~/.factory/droids/<name>.md` | `.factory/droids/<name>.md` |

---

## 検証チェックリスト {#verification-checklist}

セットアップを検証するために、このチェックリストを実行してください：

- [ ] Droid実行時にIDEプラグインが「接続済み」を表示する
- [ ] `AGENTS.md`がbuild/testコマンドと共に存在する
- [ ] あなたの設定を含むメモリファイルが作成されている
- [ ] 少なくとも1つのルールファイルがあるルールディレクトリが存在する
- [ ] 少なくとも1つのカスタムスキルが作成されている
- [ ] 自動フォーマットフックが設定されている
- [ ] 準備状況レポートがレベル2以上を表示する

---

## 次のステップ {#next-steps}



<div class="factory-card-group">

<div class="factory-card">

**[[jp/guides/power-user/prompt-crafting|プロンプト作成]]**

モデル別のプロンプト技法を学ぶ

</div>


  

<div class="factory-card">

**[[jp/guides/power-user/token-efficiency|トークン効率化]]**

トークン使用量を減らす戦略

</div>


  

<div class="factory-card">

**[[jp/guides/power-user/memory-management|メモリ管理]]**

高度なメモリとコンテキストのパターン

</div>


  

<div class="factory-card">

**[[jp/guides/power-user/rules-conventions|ルールガイド]]**

チーム規約を効果的に整理する

</div>

</div>
