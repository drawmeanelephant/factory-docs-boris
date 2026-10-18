---
id: jp/guides/droid-exec/refactor-imports
title: "インポートの整理"
status: published
summary: "Droid Execを使ってコードベース全体のimportを自動整理する"
parent: jp/guides/droid-exec/index
tags: [guides, imports, organize-imports, refactor, automation, codebase, droid-exec]
relations: [relates_to=guides/droid-exec/refactor-imports]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">インポートの整理</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Droid Execを使ってコードベース全体のimportを自動整理する</p>


このチュートリアルでは、Droid Execを使用して数百のファイル全体でimport文を同時にリファクタリングする方法を説明します。このスクリプトはインポートを賢く分類、並び替え、最適化し、未使用の依存関係を削除してモジュール形式を変換します。

## 動作原理 {#how-it-works}

スクリプトは以下の処理を行います：

1. **ファイルを検索**: すべての`.js`、`.jsx`、`.ts`、`.tsx`ファイルを検索します
2. **スマートフィルタリング**: `node_modules`、`.git`、`dist`、`build`ディレクトリを除外します
3. **インポートをチェック**: import文を含むファイルのみを処理します
4. **インポートを分類**: 外部、内部、相対インポートに整理します
5. **アルファベット順に並び替え**: 各グループ内で一貫性を保ちます
6. **未使用を削除**: 参照されていないインポートを削除します
7. **構文を現代化**: `require()`をES6 `import`に変換します
8. **重複を統合**: 同じモジュールからの複数のインポートをマージします

## スクリプトを入手 {#get-the-script}



<Details summary="完全なスクリプトソースを表示">
```bash
#!/bin/bash

# Simplified Droid Import Refactoring Script
# A cookbook example of using AI to refactor imports across a codebase
#
# Usage: ./droid-refactor-imports.sh [directory]
# Example: ./droid-refactor-imports.sh src

set -e

# Configuration
CONCURRENCY=${CONCURRENCY:-5}
DRY_RUN=${DRY_RUN:-false}
TARGET_DIR="${1:-.}"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Temp files for tracking
TEMP_DIR=$(mktemp -d)
FILES_LIST="$TEMP_DIR/files.txt"
MODIFIED_COUNT=0
PROCESSED_COUNT=0

# Cleanup on exit
trap "rm -rf $TEMP_DIR" EXIT

# Function to process a single file
process_file() {
    local filepath="$1"
    local filename=$(basename "$filepath")

    # Check if file has imports
    if ! grep -qE "^import |^const .* = require\(|^export .* from" "$filepath" 2>/dev/null; then
        return 0
    fi

    echo -e "${BLUE}Processing: $filepath${NC}"

    # The AI prompt for refactoring imports
    local prompt="Refactor the imports in $filepath:

1. Group imports in this order with blank lines between:
   - External packages (node_modules)
   - Internal/absolute imports (@/ or src/)
   - Relative imports (./ or ../)

2. Sort alphabetically within each group
3. Remove unused imports
4. Convert require() to ES6 imports
5. Consolidate duplicate imports from same module

Only modify imports, preserve all other code exactly.
Return the complete refactored file."

    if [ "$DRY_RUN" = "true" ]; then
        echo -e "${YELLOW}  [DRY RUN] Would refactor imports${NC}"
        return 0
    fi

    # Get original file hash for comparison
    local original_hash=$(md5sum "$filepath" 2>/dev/null | cut -d' ' -f1 || md5 -q "$filepath")

    # Run droid to refactor the file
    if droid exec --auto low "$prompt" 2>/dev/null; then
        # Check if file was modified
        local new_hash=$(md5sum "$filepath" 2>/dev/null | cut -d' ' -f1 || md5 -q "$filepath")
        if [ "$original_hash" != "$new_hash" ]; then
            echo -e "${GREEN}  ✓ Refactored${NC}"
            ((MODIFIED_COUNT++))
        fi
        ((PROCESSED_COUNT++))
    else
        echo "  ✗ Failed to process"
    fi
}

# Export function and variables for parallel execution
export -f process_file
export DRY_RUN GREEN YELLOW BLUE NC

# Main execution
echo -e "${BLUE}=== Droid Import Refactoring ===${NC}"
echo -e "${BLUE}Directory: $TARGET_DIR${NC}"
echo -e "${BLUE}Concurrency: $CONCURRENCY${NC}"
[ "$DRY_RUN" = "true" ] && echo -e "${YELLOW}DRY RUN MODE${NC}"
echo ""

# Find JavaScript and TypeScript files
find "$TARGET_DIR" -type f \
    \( -name "*.js" -o -name "*.jsx" -o -name "*.ts" -o -name "*.tsx" \) \
    ! -path "*/node_modules/*" \
    ! -path "*/.git/*" \
    ! -path "*/dist/*" \
    ! -path "*/build/*" \
    > "$FILES_LIST"

FILE_COUNT=$(wc -l < "$FILES_LIST" | tr -d ' ')

if [ "$FILE_COUNT" -eq 0 ]; then
    echo -e "${YELLOW}No JavaScript/TypeScript files found${NC}"
    exit 0
fi

echo -e "${BLUE}Found $FILE_COUNT files to check${NC}\n"

# Process files in parallel
cat "$FILES_LIST" | xargs -n 1 -P "$CONCURRENCY" -I {} bash -c 'process_file "$@"' _ {}

# Show summary
echo -e "\n${BLUE}=== Summary ===${NC}"
echo -e "${GREEN}Files processed: $PROCESSED_COUNT${NC}"
[ "$DRY_RUN" = "false" ] && echo -e "${GREEN}Files modified: $MODIFIED_COUNT${NC}"

if [ "$DRY_RUN" = "false" ] && [ "$MODIFIED_COUNT" -gt 0 ]; then
    echo -e "\n${BLUE}Next steps:${NC}"
    echo "  git diff           # Review changes"
    echo "  git add -A         # Stage changes"
    echo "  git commit -m 'refactor: organize imports'"
fi
```
</Details>



## 前提条件 {#prerequisites}

開始する前に、[[jp/cli/droid-exec/overview#installation|Droid Exec installation]]を完了してください。

## 基本的な使用方法 {#basic-usage}

### 変更をプレビュー（ドライラン） {#preview-changes-dry-run}



<Aside kind="warning">
ファイルを変更する前に、変更をプレビューするため必ずドライランから始めます。これにより、適用される変換を把握できます。
</Aside>



ドライラン機能は`DRY_RUN`環境変数によって制御されます：

```bash
# Preview what would happen (no changes made)
DRY_RUN=true ./droid-refactor-imports.sh src

# Example output:
# === Droid Import Refactoring ===
# Directory: src
# Concurrency: 5
# DRY RUN MODE
#
# Found 25 files to check
#
# Processing: src/components/Button.tsx
#   [DRY RUN] Would refactor imports
# Processing: src/utils/api.ts
#   [DRY RUN] Would refactor imports
```

**ドライランの動作:**
- `DRY_RUN=true`の場合：スクリプトは処理が必要なすべてのファイルを検索し、リファクタリングが必要なインポートを持つファイルを表示しますが、ファイルは変更しません
- `DRY_RUN=false`（デフォルト）の場合：実際にAIリファクタリングを実行してファイルを変更します

これは以下の場合に特に有用です：
- 変更を理解するために小さなディレクトリで最初にテストする
- 大きなコードベースを処理する前に時間/コストを見積もる
- 変更をコミットする前にスクリプトが正しいファイルを見つけることを確認する

### リファクタリングを適用 {#apply-refactoring}

プレビューに満足したら、実際のリファクタリングを実行します：

```bash
# Actually refactor the imports (default behavior)
./droid-refactor-imports.sh packages/models

# Or explicitly set DRY_RUN=false
DRY_RUN=false ./droid-refactor-imports.sh packages/models

# Adjust concurrency for faster processing
CONCURRENCY=10 ./droid-refactor-imports.sh packages/models
```

実際の実行例：
```
=== Droid Import Refactoring ===
Directory: packages/models
Concurrency: 5

Found 78 files to check

Processing: packages/models/src/organization/test-utils/fixtures.ts
Processing: packages/models/src/organization/agentReadiness/types.ts
Processing: packages/models/src/organization/utils.ts
Processing: packages/models/src/organization/agentReadiness/handlers.ts
Processing: packages/models/jest.config.ts
Processing: packages/models/src/organization/user/defaultRepositories/handlers.ts
Perfect! I've successfully refactored the imports in the file...
## Summary

I've successfully refactored the imports in `packages/models/src/organization/test-utils/fixtures.ts`.
The imports are now properly organized with comments separating external packages from relative imports...
...
```

## 実世界での変換 {#real-world-transformations}

### 例1：CommonJSからES6への変換 {#example-1-commonjs-to-es6-conversion}



<div class="factory-tabs">

<div class="factory-tab-panel">

<div class="factory-tab-heading">変更前</div>

```typescript
// customers.ts
const getStripeInstance = require("./instance").getStripeInstance;
import dayjs from 'dayjs';  // unused import
import url from 'url';  // unused import
```

</div>



  

<div class="factory-tab-panel">

<div class="factory-tab-heading">変更後</div>

```typescript
// customers.ts
// Relative imports
import { getStripeInstance } from './instance';
```


<Aside kind="note">
CommonJS converted to ES6, unused imports removed
</Aside>



</div>

</div>



### 例2：重複インポートの統合 {#example-2-consolidating-duplicate-imports}



<div class="factory-tabs">

<div class="factory-tab-panel">

<div class="factory-tab-heading">変更前</div>

```typescript
// admin.ts
const { auth } = require('firebase-admin');
import { App } from "firebase-admin/app"
import { Firestore } from 'firebase-admin/firestore';
import dotenv from 'dotenv';  // unused import
const { FirebaseProjectName } = require("./enums");
import {
  getFirestoreInstanceForProject,
  getFirebaseAuthInstanceForProject,
} from './multi-admin';
const { initializeFirebaseAdminApp } = require('./multi-admin');
import {
  getFirestoreInstance as getDefaultFirestoreInstance,
  getFirestoreInstanceForTest as getDefaultFirestoreInstanceForTest,
  getFirebaseAuthInstance as getDefaultFirebaseAuthInstance,
} from "./multi-admin"
import express from 'express';  // unused import
```

</div>



  

<div class="factory-tab-panel">

<div class="factory-tab-heading">変更後</div>

```typescript
// admin.ts
// External packages
import { auth } from 'firebase-admin';
import { App } from 'firebase-admin/app';
import { Firestore } from 'firebase-admin/firestore';

// Relative imports
import { FirebaseProjectName } from './enums';
import {
  getFirestoreInstanceForProject,
  getFirebaseAuthInstanceForProject,
  initializeFirebaseAdminApp,
  getFirestoreInstance as getDefaultFirestoreInstance,
  getFirestoreInstanceForTest as getDefaultFirestoreInstanceForTest,
  getFirebaseAuthInstance as getDefaultFirebaseAuthInstance,
} from './multi-admin';
```


<Aside kind="note">
同じモジュールからの複数importを統合し、未使用を削除し、CommonJSを変換
</Aside>



</div>

</div>



## ベストプラクティス {#best-practices}



<Aside kind="note">
安全で効果的なimportリファクタリングのため、これらのベストプラクティスに従ってください。
</Aside>





<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">ドライランから始める</div>

ファイルを変更する前に必ず変更をプレビューします:
```bash
# Preview what would happen without making changes
DRY_RUN=true ./droid-refactor-imports.sh packages/models
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">まず小さな範囲でテストする</div>

コードベース全体を処理する前に、特定のサブディレクトリから始めます:
```bash
# Test on a single module first
./droid-refactor-imports.sh packages/models/src/utils

# Then expand to larger directories
./droid-refactor-imports.sh packages/models
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">段階的に処理する</div>

大規模なコードベースでは、レビューしやすいようにディレクトリを分けて処理します:
```bash
# Process each package separately
./droid-refactor-imports.sh packages/models
git add -A && git commit -m "refactor: organize imports in models"

./droid-refactor-imports.sh packages/services
git add -A && git commit -m "refactor: organize imports in services"
```

</div>

</div>
