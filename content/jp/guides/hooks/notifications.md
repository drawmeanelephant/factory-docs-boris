---
id: jp/guides/hooks/notifications
title: "カスタム通知"
status: published
summary: "デスクトップ通知、サウンド、SlackなどでDroidが対応を必要とするときに通知を受ける"
parent: jp/guides/hooks/index
tags: [guides, notifications, alerts, slack, desktop, sounds, webhook, hook]
relations: [relates_to=guides/hooks/notifications]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">カスタム通知</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">デスクトップ通知、サウンド、SlackなどでDroidが対応を必要とするときに通知を受ける</p>


このクックブックでは、Droidがあなたの入力を必要としている時や、セッション中に重要なイベントが発生した時に知ることができるカスタム通知の設定方法を説明します。

## 仕組み {#how-it-works}

通知フックは以下のことができます：

1. **複数のイベントでトリガー**: 通知、停止、サブエージェント停止、セッション終了
2. **複数のチャンネルに対応**: デスクトップ通知、システム音、Slack、メール、webhook
3. **コンテキストを提供**: セッション詳細、タスク完了状況、エラーメッセージを含む
4. **インテリジェントフィルタリング**: 重要なイベントのみを通知
5. **クロスプラットフォーム対応**: macOS、Linux、Windows

## 前提条件 {#prerequisites}

お使いのプラットフォーム用の通知ツールをインストール：



<div class="factory-codegroup">
<div class="factory-codegroup-bar"><button type="button" class="factory-codegroup-tab is-active" data-tab-idx="0">macOS</button><button type="button" class="factory-codegroup-tab" data-tab-idx="1">Linux</button><button type="button" class="factory-codegroup-tab" data-tab-idx="2">Windows (PowerShell)</button></div>

<div class="factory-codegroup-panel is-active" data-panel-idx="0">

```bash
# Built-in commands (no installation needed)
which osascript  # For display notifications
which afplay     # For sounds
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="1">

```bash
# Install notify-send
sudo apt-get install libnotify-bin  # Ubuntu/Debian
sudo dnf install libnotify           # Fedora
sudo pacman -S libnotify             # Arch
```

</div>

<div class="factory-codegroup-panel" data-panel-idx="2">

```bash
# BurntToast for Windows notifications
Install-Module -Name BurntToast -Scope CurrentUser
```

</div>

</div>



Slack通知については、[api.slack.com/messaging/webhooks](https://api.slack.com/messaging/webhooks)でwebhookを作成してください。

## 基本的な通知 {#basic-notifications}

### Droidが待機している時のデスクトップ通知 {#desktop-notification-when-droid-waits}

Droidがあなたの入力を待っている時に通知を受け取ります。

`.factory/hooks/notify-wait.sh`を作成：

```bash
#!/bin/bash

input=$(cat)
message=$(echo "$input" | jq -r '.message // "Droid needs your attention"')
hook_event=$(echo "$input" | jq -r '.hook_event_name')

# Only notify on actual wait events
if [ "$hook_event" != "Notification" ]; then
  exit 0
fi

# Platform-specific notification
if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS
  osascript -e "display notification \"$message\" with title \"Droid\" sound name \"Ping\""
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  # Linux
  notify-send "Droid" "$message" -i dialog-information -u normal
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
  # Windows
  powershell -Command "New-BurntToastNotification -Text 'Droid', '$message'"
fi

exit 0
```

```bash
chmod +x .factory/hooks/notify-wait.sh
```

`~/.factory/hooks.json`に追加（ユーザー全体）：

```json
{
  "Notification": [
    {
      "hooks": [
        {
          "type": "command",
          "command": "~/.factory/hooks/notify-wait.sh",
          "timeout": 5
        }
      ]
    }
  ]
}
```

### タスク完了時の音声アラート {#sound-alert-when-task-completes}

Droidが終了した時に音を再生します。

`.factory/hooks/completion-sound.sh`を作成：

```bash
#!/bin/bash

input=$(cat)
hook_event=$(echo "$input" | jq -r '.hook_event_name')

# Only alert on completion events
if [ "$hook_event" != "Stop" ]; then
  exit 0
fi

# Platform-specific sound
if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS - use system sounds
  afplay /System/Library/Sounds/Glass.aiff
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
  # Linux - use system bell or speaker-test
  paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null || \
    echo -e '\a'  # Fallback to terminal bell
fi

exit 0
```

```bash
chmod +x .factory/hooks/completion-sound.sh
```

`~/.factory/hooks.json`に追加：

```json
{
  "Stop": [
    {
      "hooks": [
        {
          "type": "command",
          "command": "~/.factory/hooks/completion-sound.sh",
          "timeout": 3
        }
      ]
    }
  ]
}
```

## 高度な通知 {#advanced-notifications}

### Slack連携 {#slack-integration}

Droidがタスクを完了した時にSlackメッセージを送信します。

`.factory/hooks/slack-notify.sh`を作成：

```bash
#!/bin/bash
set -e

# Configure your Slack webhook URL
SLACK_WEBHOOK_URL="${SLACK_WEBHOOK_URL:-}"

if [ -z "$SLACK_WEBHOOK_URL" ]; then
  echo "SLACK_WEBHOOK_URL not set, skipping Slack notification"
  exit 0
fi

input=$(cat)
hook_event=$(echo "$input" | jq -r '.hook_event_name')
session_id=$(echo "$input" | jq -r '.session_id')
cwd=$(echo "$input" | jq -r '.cwd')

# Build message based on event type
case "$hook_event" in
  "Stop")
    title="✅ Droid Task Completed"
    color="good"
    ;;
  "SessionEnd")
    title="🏁 Droid Session Ended"
    color="#808080"
    reason=$(echo "$input" | jq -r '.reason')
    ;;
  "SubagentStop")
    title="🤖 Subagent Task Completed"
    color="good"
    ;;
  *)
    exit 0
    ;;
esac

# Send to Slack
curl -X POST "$SLACK_WEBHOOK_URL" \
  -H 'Content-Type: application/json' \
  -d @- << EOF
{
  "attachments": [
    {
      "color": "$color",
      "title": "$title",
      "fields": [
        {
          "title": "Project",
          "value": "$(basename "$cwd")",
          "short": true
        },
        {
          "title": "Session",
          "value": "${session_id:0:8}...",
          "short": true
        }
      ],
      "footer": "Droids",
      "ts": $(date +%s)
    }
  ]
}
EOF

exit 0
```

```bash
chmod +x .factory/hooks/slack-notify.sh
```

webhook URLを設定：

```bash
# Add to ~/.bashrc or ~/.zshrc
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
```

`~/.factory/hooks.json`に追加：

```json
{
  "Stop": [
    {
      "hooks": [
        {
          "type": "command",
          "command": "~/.factory/hooks/slack-notify.sh",
          "timeout": 10
        }
      ]
    }
  ],
  "SessionEnd": [
    {
      "hooks": [
        {
          "type": "command",
          "command": "~/.factory/hooks/slack-notify.sh",
          "timeout": 10
        }
      ]
    }
  ]
}
```

### メール通知 {#email-notifications}

重要なイベントのメールアラートを送信します。

`.factory/hooks/email-notify.sh`を作成：

```bash
#!/bin/bash
set -e

# Configure email settings
EMAIL_TO="${DROID_NOTIFY_EMAIL:-your-email@example.com}"
EMAIL_FROM="${DROID_FROM_EMAIL:-droid@factory.ai}"

input=$(cat)
hook_event=$(echo "$input" | jq -r '.hook_event_name')

# Only notify on session end with errors
if [ "$hook_event" != "SessionEnd" ]; then
  exit 0
fi

reason=$(echo "$input" | jq -r '.reason')
session_id=$(echo "$input" | jq -r '.session_id')
cwd=$(echo "$input" | jq -r '.cwd')

# Check if session ended due to error
if [ "$reason" != "error" ] && [ "$reason" != "other" ]; then
  exit 0
fi

# Send email using sendmail or mail command
subject="Droid Session Ended: $(basename "$cwd")"
body="Session $session_id ended with reason: $reason

Project: $cwd
Time: $(date)

Check the logs for more details."

# Try sendmail first, fallback to mail command
if command -v sendmail &> /dev/null; then
  echo -e "Subject: $subject\nFrom: $EMAIL_FROM\nTo: $EMAIL_TO\n\n$body" | sendmail -t
elif command -v mail &> /dev/null; then
  echo "$body" | mail -s "$subject" "$EMAIL_TO"
else
  echo "No email command available (sendmail or mail)"
  exit 1
fi

exit 0
```

```bash
chmod +x .factory/hooks/email-notify.sh
```

環境を設定：

```bash
# Add to ~/.bashrc or ~/.zshrc
export DROID_NOTIFY_EMAIL="your-email@example.com"
```


### アクション付きリッチデスクトップ通知 {#rich-desktop-notifications-with-actions}

アクションボタン付きのmacOS通知。

`.factory/hooks/rich-notify-macos.sh`を作成：

```bash
#!/bin/bash

input=$(cat)
hook_event=$(echo "$input" | jq -r '.hook_event_name')
message=$(echo "$input" | jq -r '.message // "Droid needs your attention"')
session_id=$(echo "$input" | jq -r '.session_id')

# Only for macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
  exit 0
fi

case "$hook_event" in
  "Notification")
    # Notification with action buttons
    osascript << EOF
tell application "System Events"
  display notification "$message" with title "Droid Waiting" subtitle "Session: ${session_id:0:8}" sound name "Ping"
end tell
EOF
    ;;

  "Stop")
    # Success notification
    osascript << EOF
tell application "System Events"
  display notification "Task completed successfully" with title "Droid Complete" subtitle "$(basename "$PWD")" sound name "Glass"
end tell
EOF
    ;;

  "SessionEnd")
    reason=$(echo "$input" | jq -r '.reason')
    # Different sound based on reason
    sound="Purr"
    if [ "$reason" == "error" ]; then
      sound="Basso"
    fi

    osascript << EOF
tell application "System Events"
  display notification "Session ended: $reason" with title "Droid Session" subtitle "$(basename "$PWD")" sound name "$sound"
end tell
EOF
    ;;
esac

exit 0
```

```bash
chmod +x .factory/hooks/rich-notify-macos.sh
```


### Webhook連携 {#webhook-integration}

カスタムwebhookに通知を送信：



`.factory/hooks/webhook-notify.sh`を作成：

```bash
#!/bin/bash
set -e

WEBHOOK_URL="${DROID_WEBHOOK_URL:-}"

if [ -z "$WEBHOOK_URL" ]; then
  exit 0
fi

input=$(cat)

# Forward the entire hook input to webhook
curl -X POST "$WEBHOOK_URL" \
  -H 'Content-Type: application/json' \
  -d "$input" \
  --max-time 5 \
  --silent \
  --show-error

exit 0
```

```bash
chmod +x .factory/hooks/webhook-notify.sh
export DROID_WEBHOOK_URL="https://your-webhook-url.com/droid-events"
```


## 実際の使用例 {#real-world-examples}

### 例1: フォーカスモード通知 {#example-1-focus-mode-notifications}

デスクから離れている時のみ通知：



`.factory/hooks/smart-notify.sh`を作成：

```bash
#!/bin/bash

input=$(cat)

# Check if user is idle (macOS)
if [[ "$OSTYPE" == "darwin"* ]]; then
  idle_time=$(ioreg -c IOHIDSystem | awk '/HIDIdleTime/ {print int($NF/1000000000)}')

  # Only notify if idle for more than 60 seconds
  if [ "$idle_time" -lt 60 ]; then
    exit 0
  fi
fi

# Send notification
message=$(echo "$input" | jq -r '.message // "Droid needs your attention"')
osascript -e "display notification \"$message\" with title \"Droid\" sound name \"Ping\""

exit 0
```


### 例2: チーム通知ダッシュボード {#example-2-team-notification-dashboard}

すべてのイベントを共有ダッシュボードに記録：



`.factory/hooks/team-logger.sh`を作成：

```bash
#!/bin/bash
set -e

# Central logging endpoint
LOG_ENDPOINT="${TEAM_LOG_ENDPOINT:-}"

if [ -z "$LOG_ENDPOINT" ]; then
  exit 0
fi

input=$(cat)
hook_event=$(echo "$input" | jq -r '.hook_event_name')
session_id=$(echo "$input" | jq -r '.session_id')
cwd=$(echo "$input" | jq -r '.cwd')

# Add metadata
payload=$(echo "$input" | jq -c ". + {
  user: \"$USER\",
  hostname: \"$HOSTNAME\",
  timestamp: \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",
  project: \"$(basename "$cwd")\"
}")

# Send to logging service
curl -X POST "$LOG_ENDPOINT" \
  -H 'Content-Type: application/json' \
  -d "$payload" \
  --max-time 3 \
  --silent

exit 0
```


## ベストプラクティス {#best-practices}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">通知スクリプトを高速に保つ</div>

Droidをブロックしないよう短いタイムアウトを使用します:
```json
{
  "timeout": 5  // 5 seconds max for notifications
}
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">失敗を適切に処理する</div>

通知に失敗しても実行をブロックしないでください:
```bash
# Continue even if curl fails
curl -X POST "$URL" ... || true
exit 0
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">ユーザー設定を尊重する</div>

オプトアウト用の環境変数を確認します:
```bash
if [ "$DROID_DISABLE_NOTIFICATIONS" = "true" ]; then
  exit 0
fi
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">通知をテストする</div>

テストのために手動でフックをトリガーします:
```bash
# Test notification script
echo '{"hook_event_name":"Notification","message":"Test"}' | .factory/hooks/notify-wait.sh
```

</div>



  

<div class="factory-step">

<div class="factory-step-title">適切な通知レベルを使用</div>

イベントごとに適切な緊急度は異なります:
  - Notification: 緊急度高（Droidが待機中）
  - Stop: 緊急度中（タスク完了）
  - SessionEnd: 緊急度低（参考情報のみ）

</div>

</div>



## トラブルシューティング {#troubleshooting}



    **問題**: 通知が表示されない

    **解決策**: 通知の権限を確認：
    ```bash
    # macOS - check System Settings > Notifications
    # Linux - verify notify-send works
    notify-send "Test" "This is a test"

    # Check if hooks are executing
    droid --debug
    ```



    **問題**: Slackメッセージが送信されない

    **解決策**: webhookを直接テスト：
    ```bash
    curl -X POST "$SLACK_WEBHOOK_URL" \
      -H 'Content-Type: application/json' \
      -d '{"text":"Test from curl"}'
    ```



    **問題**: アラートスパムを受け取る

    **解決策**: レート制限を追加：
    ```bash
    # Only notify once every 5 minutes
    LAST_NOTIFY_FILE="/tmp/droid-last-notify"

    if [ -f "$LAST_NOTIFY_FILE" ]; then
      last_time=$(cat "$LAST_NOTIFY_FILE")
      current_time=$(date +%s)
      if [ $((current_time - last_time)) -lt 300 ]; then
        exit 0
      fi
    fi

    date +%s > "$LAST_NOTIFY_FILE"
    # ... send notification
    ```



    **問題**: 音声アラートが鳴らない

    **解決策**: 音声システムを確認：
    ```bash
    # macOS - list available sounds
    ls /System/Library/Sounds/

    # Test sound
    afplay /System/Library/Sounds/Glass.aiff

    # Linux - check audio
    paplay /usr/share/sounds/freedesktop/stereo/complete.oga
    ```



## 関連項目 {#see-also}

- [[jp/reference/hooks-reference|フックリファレンス]] - 完全なフックAPI文書
- [[jp/cli/configuration/hooks-guide|Get started with hooks]] - 基本的なhooksの紹介
- [[jp/guides/hooks/session-automation|Session automation]] - セッション設定の自動化
- [[jp/guides/hooks/logging-analytics|Logging and analytics]] - Droid使用状況の追跡
