---
id: api-reference/sessions/list-a-sessions-child-sessions
title: "List a session's child sessions"
status: published
summary: "GET /api/v0/sessions/{sessionId}/children — List a session's child sessions"
parent: api-reference/sessions/index
tags: [api-reference, sessions, get]
relations: [relates_to=jp/api-reference/sessions/list-a-sessions-child-sessions]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List a session&#x27;s child sessions</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/sessions/{sessionId}/children</span></div>

Returns the caller's sessions spawned under one parent session (Task subagents, mission agents) with their last reported status and the state of the computer each runs on, oldest first. Computer details are only included for computers the caller owns. Artifacts are included only when `includeArtifacts=true`; what each session is waiting on only when `includeAttention=true`; token usage and Factory Standard Credits, rolled up with each session's Task subagents, only when `includeUsage=true`.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/sessions/{sessionId}/children`
- **Category:** [[api-reference/sessions/index|Sessions API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `sessionId` | `path` | `string` | Yes | - |
| `includeArtifacts` | `query` | `string` | No | - |
| `includeAttention` | `query` | `string` | No | - |
| `includeUsage` | `query` | `string` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/sessions/{sessionId}/children" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
