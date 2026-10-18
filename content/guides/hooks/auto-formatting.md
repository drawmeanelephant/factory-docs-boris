---
id: guides/hooks/auto-formatting
title: "Auto-formatting Code"
status: published
summary: "Automatically format code after every file edit using hooks"
parent: guides/hooks/index
tags: [guides, formatting, prettier, black, gofmt, rustfmt, auto-format, code-style]
relations: [relates_to=jp/guides/hooks/auto-formatting]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Auto-formatting Code</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Automatically format code after every file edit using hooks</p>


This cookbook shows how to automatically format code after Droid edits files, ensuring consistent code style across your project without manual intervention.

## How it works {#how-it-works}

The hook:

1. **Triggers on file edits**: Runs after Write or Edit tool calls
2. **Detects file type**: Checks file extension to determine formatter
3. **Runs appropriate formatter**: Executes prettier, black, gofmt, rustfmt, etc.
4. **Provides feedback**: Reports formatting results to the user
5. **Handles errors gracefully**: Continues even if formatting fails

## Prerequisites {#prerequisites}

Install formatters for your language stack:



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



## Basic setup {#basic-setup}

### Single language project {#single-language-project}

For a JavaScript/TypeScript project, add this to your `.factory/hooks.json`:

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

### Multi-language project {#multi-language-project}

For projects with multiple languages, use a script to handle different file types.

Create `.factory/hooks/format.sh`:

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

Make the script executable:

```bash
chmod +x .factory/hooks/format.sh
```

Add to `.factory/hooks.json`:

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

## Advanced configurations {#advanced-configurations}

### Format with custom config {#format-with-custom-config}

Use project-specific prettier config:

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

### Format with linting {#format-with-linting}

Combine formatting with linting fixes.

Create `.factory/hooks/format-and-lint.sh`:

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

Make the script executable:

```bash
chmod +x .factory/hooks/format-and-lint.sh
```

Add to `.factory/hooks.json`:

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

### Conditional formatting {#conditional-formatting}

Only format files in specific directories.

Create `.factory/hooks/format-src-only.sh`:

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

Make the script executable:

```bash
chmod +x .factory/hooks/format-src-only.sh
```

Add to `.factory/hooks.json`:

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

## Real-world examples {#real-world-examples}

### Example 1: React component formatting {#example-1-react-component-formatting}



<div class="factory-tabs">

<div class="factory-tab-panel">

<div class="factory-tab-heading">Before Hook</div>

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

<div class="factory-tab-heading">After Hook</div>

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



### Example 2: Python import sorting {#example-2-python-import-sorting}



<div class="factory-tabs">

<div class="factory-tab-panel">

<div class="factory-tab-heading">Before Hook</div>

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

<div class="factory-tab-heading">After Hook</div>

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
Imports sorted into stdlib, third-party, and local groups
</Aside>



</div>

</div>



## Best practices {#best-practices}



<Aside kind="warning">
Formatters can sometimes introduce subtle bugs (e.g., changing string formats, line continuations). Always review changes before committing.
</Aside>





<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Start with read-only mode</div>

Test your formatter configuration manually first:
```bash
# Dry run to see what would change
prettier --check src/
black --check src/
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Use consistent config files</div>

Ensure formatter configs are committed:
```bash
# Add to version control
git add .prettierrc .prettierignore
git add pyproject.toml  # for black config
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Set appropriate timeouts</div>

Large files may need more time:
```json
{
  "timeout": 60  // Increase for large files
}
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Handle formatter errors gracefully</div>

Don't block Droid if formatting fails:
```bash
# Use || true to continue on errors
prettier --write "$file_path" 2>&1 || true
```

</div>


  
  

<div class="factory-step">

<div class="factory-step-title">Consider Git hooks integration</div>

Combine with pre-commit hooks for consistency:
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



## Troubleshooting {#troubleshooting}

### Formatter not found {#formatter-not-found}

**Problem**: `command not found` error

**Solution**: Install the formatter globally or use npx/project binaries:
```bash
# Install globally
npm install -g prettier

# Or use project version
npx prettier --write "$file_path"
```

### Formatting breaks code {#formatting-breaks-code}

**Problem**: Formatter introduces syntax errors

**Solution**: Add file validation after formatting:
```bash
# For TypeScript
prettier --write "$file_path"
tsc --noEmit "$file_path" || echo "⚠️ Type errors after formatting"
```

### Hook runs too slowly {#hook-runs-too-slowly}

**Problem**: Formatting takes too long

**Solution**: Only format changed files, use faster formatters:
```bash
# Skip files that haven't changed
if git diff --quiet "$file_path"; then
  exit 0
fi
```

### Conflicts with editor formatting {#conflicts-with-editor-formatting}

**Problem**: Editor and hook format differently

**Solution**: Use the same config for both:
```json
// .vscode/settings.json
{
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.formatOnSave": true,
  "prettier.configPath": ".prettierrc"
}
```

## See also {#see-also}

- [[reference/hooks-reference|Hooks reference]] - Complete hooks API documentation
- [[cli/configuration/hooks-guide|Get started with hooks]] - Basic hooks introduction
- [[guides/hooks/code-validation|Code validation hooks]] - Enforce code standards
- [[guides/hooks/git-workflows|Git workflow hooks]] - Integrate with Git
