---
id: jp/guides/hooks/auto-formatting
title: "コードの自動フォーマット"
status: published
summary: "フックを使ってファイル編集後にコードを自動整形する"
parent: jp/guides/hooks/index
tags: [guides, formatting, prettier, black, gofmt, rustfmt, auto-format, code-style]
relations: [relates_to=guides/hooks/auto-formatting]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">コードの自動フォーマット</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">フックを使ってファイル編集後にコードを自動整形する</p>


このクックブックは、Droidがファイルを編集した後に自動的にコードをフォーマットし、手動での介入なしにプロジェクト全体で一貫したコードスタイルを確保する方法を示します。

## 動作原理 {#how-it-works}

フック：

1. **ファイル編集時にトリガー**: WriteまたはEditツールコール後に実行
2. **ファイル種別を検出**: ファイル拡張子をチェックしてフォーマッターを決定
3. **適切なフォーマッターを実行**: prettier、black、gofmt、rustfmtなどを実行
4. **フィードバックを提供**: フォーマット結果をユーザーに報告
5. **エラーを適切に処理**: フォーマットが失敗しても継続

## 前提条件 {#prerequisites}

あなたの言語スタックに対応するフォーマッターをインストールしてください：



<div class="factory-codegroup">
<div class="factory-codegroup-bar"><button type="button" class="factory-codegroup-tab is-active" data-tab-idx="0">JavaScript/TypeScript</button><button type="button" class="factory-codegroup-tab" data-tab-idx="1">Python</button><button type="button" class="factory-codegroup-tab" data-tab-idx="2">Go</button><button type="button" class="factory-codegroup-tab" data-tab-idx="3">Rust</button></div>

<div class="factory-codegroup-panel is-active" data-panel-idx="0">

```bash
npm install -D prettier
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="1">

```bash
pip install black isort
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="2">

```bash
# gofmt is included with Go installation
go version
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="3">

```bash
rustup component add rustfmt
```

</div>

</div>



## 基本セットアップ {#basic-setup}

### 単一言語プロジェクト {#single-language-project}

JavaScript/TypeScriptプロジェクトの場合、`.factory/hooks.json`に以下を追加してください：

```json
{
  "PostToolUse": [
    {
      "matcher": "Create|Edit|ApplyPatch",
      "hooks": [
        {
          "type": "command",
          "command": "jq -r '.tool_input.file_path' | { read file_path; if echo \"$file_path\" | grep -qE '\\.(ts|tsx|js|jsx)$'; then npx prettier --write \"$file_path\" 2>&1 && echo \"✓ Formatted $file_path\"; fi; }",
          "timeout": 30
        }
      ]
    }
  ]
}
```

### 多言語プロジェクト {#multi-language-project}

複数の言語を使用するプロジェクトでは、異なるファイル種別を処理するスクリプトを使用します。

`.factory/hooks/format.sh`を作成してください：

```bash
#!/bin/bash
set -e

# Read the hook input
input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path')

# Skip if file doesn't exist
if [ ! -f "$file_path" ]; then
  exit 0
fi

# Determine formatter based on file extension
case "$file_path" in
  *.ts|*.tsx|*.js|*.jsx|*.json|*.css|*.scss|*.md|*.mdx)
    if command -v prettier &> /dev/null; then
      prettier --write "$file_path" 2>&1
      echo "✓ Formatted with Prettier: $file_path"
    fi
    ;;
  *.py)
    if command -v black &> /dev/null; then
      black "$file_path" 2>&1
      echo "✓ Formatted with Black: $file_path"
    fi
    if command -v isort &> /dev/null; then
      isort "$file_path" 2>&1
      echo "✓ Sorted imports with isort: $file_path"
    fi
    ;;
  *.go)
    if command -v gofmt &> /dev/null; then
      gofmt -w "$file_path" 2>&1
      echo "✓ Formatted with gofmt: $file_path"
    fi
    ;;
  *.rs)
    if command -v rustfmt &> /dev/null; then
      rustfmt "$file_path" 2>&1
      echo "✓ Formatted with rustfmt: $file_path"
    fi
    ;;
  *.java)
    if command -v google-java-format &> /dev/null; then
      google-java-format -i "$file_path" 2>&1
      echo "✓ Formatted with google-java-format: $file_path"
    fi
    ;;
  *)
    # No formatter for this file type
    exit 0
    ;;
esac

exit 0
```

スクリプトを実行可能にします：

```bash
chmod +x .factory/hooks/format.sh
```

`.factory/hooks.json`に追加してください：

```json
{
  "PostToolUse": [
    {
      "matcher": "Create|Edit|ApplyPatch",
      "hooks": [
        {
          "type": "command",
          "command": "\"$DROID_PROJECT_DIR\"/.factory/hooks/format.sh",
          "timeout": 30
        }
      ]
    }
  ]
}
```

## 高度な設定 {#advanced-configurations}

### カスタム設定でフォーマット {#format-with-custom-config}

プロジェクト固有のprettier設定を使用：

```json
{
  "PostToolUse": [
    {
      "matcher": "Create|Edit|ApplyPatch",
      "hooks": [
        {
          "type": "command",
          "command": "jq -r '.tool_input.file_path' | { read file_path; if echo \"$file_path\" | grep -qE '\\.(ts|tsx|js|jsx)$'; then npx prettier --config \"$DROID_PROJECT_DIR\"/.prettierrc --write \"$file_path\" 2>&1; fi; }",
          "timeout": 30
        }
      ]
    }
  ]
}
```

### リントとフォーマット {#format-with-linting}

フォーマットとリント修正を組み合わせます。

`.factory/hooks/format-and-lint.sh`を作成してください：

```bash
#!/bin/bash
set -e

input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path')

if [ ! -f "$file_path" ]; then
  exit 0
fi

case "$file_path" in
  *.ts|*.tsx|*.js|*.jsx)
    # Format with prettier
    if command -v prettier &> /dev/null; then
      prettier --write "$file_path" 2>&1
      echo "✓ Formatted: $file_path"
    fi

    # Fix lint issues
    if command -v eslint &> /dev/null; then
      eslint --fix "$file_path" 2>&1 || true
      echo "✓ Linted: $file_path"
    fi
    ;;
  *.py)
    # Format with black
    if command -v black &> /dev/null; then
      black "$file_path" 2>&1
      echo "✓ Formatted with Black: $file_path"
    fi

    # Sort imports
    if command -v isort &> /dev/null; then
      isort "$file_path" 2>&1
      echo "✓ Sorted imports: $file_path"
    fi

    # Run flake8 for style issues
    if command -v flake8 &> /dev/null; then
      flake8 "$file_path" 2>&1 || true
      echo "✓ Checked with flake8: $file_path"
    fi
    ;;
esac

exit 0
```

スクリプトを実行可能にします：

```bash
chmod +x .factory/hooks/format-and-lint.sh
```

`.factory/hooks.json`に追加してください：

```json
{
  "PostToolUse": [
    {
      "matcher": "Create|Edit|ApplyPatch",
      "hooks": [
        {
          "type": "command",
          "command": "\"$DROID_PROJECT_DIR\"/.factory/hooks/format-and-lint.sh",
          "timeout": 45
        }
      ]
    }
  ]
}
```

### 条件付きフォーマット {#conditional-formatting}

特定のディレクトリ内のファイルのみをフォーマットします。

`.factory/hooks/format-src-only.sh`を作成してください：

```bash
#!/bin/bash
set -e

input=$(cat)
file_path=$(echo "$input" | jq -r '.tool_input.file_path')

# Only format files in src/ or packages/ directories
if ! echo "$file_path" | grep -qE '^(src/|packages/)'; then
  exit 0
fi

case "$file_path" in
  *.ts|*.tsx|*.js|*.jsx)
    if command -v prettier &> /dev/null; then
      prettier --write "$file_path" 2>&1
      echo "✓ Formatted: $file_path"
    fi
    ;;
esac

exit 0
```

スクリプトを実行可能にします：

```bash
chmod +x .factory/hooks/format-src-only.sh
```

`.factory/hooks.json`に追加してください：

```json
{
  "PostToolUse": [
    {
      "matcher": "Create|Edit|ApplyPatch",
      "hooks": [
        {
          "type": "command",
          "command": "\"$DROID_PROJECT_DIR\"/.factory/hooks/format-src-only.sh",
          "timeout": 30
        }
      ]
    }
  ]
}
```

## 実例 {#real-world-examples}

### 例1: Reactコンポーネントのフォーマット {#example-1-react-component-formatting}



<div class="factory-tabs">

<div class="factory-tab-panel">

<div class="factory-tab-heading">フック前</div>

```typescript
// Droid creates this file
import React from 'react';
import {useState} from 'react';

export const Button = ({onClick,label}:{onClick:()=>void;label:string})=>{
const [loading,setLoading]=useState(false);
return <button onClick={onClick} disabled={loading}>{label}</button>
}
```

</div>



  

<div class="factory-tab-panel">

<div class="factory-tab-heading">フック後</div>

```typescript
// Automatically formatted by prettier
import React, { useState } from 'react';

export const Button = ({
  onClick,
  label,
}: {
  onClick: () => void;
  label: string;
}) => {
  const [loading, setLoading] = useState(false);
  return (
    <button onClick={onClick} disabled={loading}>
      {label}
    </button>
  );
};
```


<Aside kind="note">
Imports consolidated, spacing fixed, formatting applied
</Aside>



</div>

</div>



### 例2: Pythonインポートソート {#example-2-python-import-sorting}



<div class="factory-tabs">

<div class="factory-tab-panel">

<div class="factory-tab-heading">フック前</div>

```python
# Droid creates this file
from typing import Optional
import sys
from django.db import models
import os
from myapp.utils import helper

def process_data(data: Optional[str]) -> None:
    if data:
        helper(data)
```

</div>



  

<div class="factory-tab-panel">

<div class="factory-tab-heading">フック後</div>

```python
# Automatically formatted by black and isort
import os
import sys
from typing import Optional

from django.db import models

from myapp.utils import helper


def process_data(data: Optional[str]) -> None:
    if data:
        helper(data)
```


<Aside kind="note">
importを標準ライブラリ、サードパーティ、ローカルグループに整理
</Aside>



</div>

</div>



## ベストプラクティス {#best-practices}



<Aside kind="warning">
フォーマッターは、文字列形式や行継続の変更など、微妙なバグを混入させることがあります。コミット前に必ず変更を確認してください。
</Aside>





<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">読み取り専用モードから始める</div>

まずフォーマッター設定を手動でテストします:
```bash
# Dry run to see what would change
prettier --check src/
black --check src/
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">一貫した設定ファイルを使用</div>

フォーマッター設定がコミットされていることを確認します:
```bash
# Add to version control
git add .prettierrc .prettierignore
git add pyproject.toml  # for black config
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">適切なタイムアウトを設定</div>

大きなファイルにはより長い時間が必要な場合があります:
```json
{
  "timeout": 60  // Increase for large files
}
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">フォーマッターエラーを適切に処理する</div>

フォーマットに失敗してもDroidをブロックしないようにします:
```bash
# Use || true to continue on errors
prettier --write "$file_path" 2>&1 || true
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">Gitフック連携を検討する</div>

一貫性のためpre-commitフックと組み合わせます:
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v3.0.0
    hooks:
      - id: prettier
```

</div>

</div>



## トラブルシューティング {#troubleshooting}

### フォーマッターが見つからない {#formatter-not-found}

**問題**: `command not found`エラー

**解決策**: フォーマッターをグローバルにインストールするか、npx/プロジェクトバイナリを使用してください：
```bash
# Install globally
npm install -g prettier

# Or use project version
npx prettier --write "$file_path"
```

### フォーマットによりコードが破損 {#formatting-breaks-code}

**問題**: フォーマッターが構文エラーを引き起こす

**解決策**: フォーマット後にファイル検証を追加してください：
```bash
# For TypeScript
prettier --write "$file_path"
tsc --noEmit "$file_path" || echo "⚠️ Type errors after formatting"
```

### フックの実行が遅い {#hook-runs-too-slowly}

**問題**: フォーマットに時間がかかりすぎる

**解決策**: 変更されたファイルのみをフォーマットし、より高速なフォーマッターを使用してください：
```bash
# Skip files that haven't changed
if git diff --quiet "$file_path"; then
  exit 0
fi
```

### エディターのフォーマットと競合 {#conflicts-with-editor-formatting}

**問題**: エディターとフックが異なるフォーマットを行う

**解決策**: 両方で同じ設定を使用してください：
```json
// .vscode/settings.json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "prettier.configPath": ".prettierrc"
}
```

## 関連情報 {#see-also}

- [[jp/reference/hooks-reference|フックリファレンス]] - 完全なフックAPI文書
- [[jp/cli/configuration/hooks-guide|Get started with hooks]] - 基本的なフックの紹介
- [[jp/guides/hooks/code-validation|Code validation hooks]] - コード標準の強制
- [[jp/guides/hooks/git-workflows|Git workflow hooks]] - Gitとの統合
