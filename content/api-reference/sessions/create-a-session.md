---
id: api-reference/sessions/create-a-session
title: "Create a session"
status: published
summary: "POST /api/v0/sessions — Create a session"
parent: api-reference/sessions/index
tags: [api-reference, sessions, post]
relations: [relates_to=jp/api-reference/sessions/create-a-session]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Create a session</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/sessions</span></div>

Creates a new session with the specified configuration. This feature is enabled for selected organizations only.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/sessions`
- **Category:** [[api-reference/sessions/index|Sessions API]]

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `computerId` | `string` | Yes | Computer ID to connect |
| `cwd` | `string` | No | Working directory for the session on the computer. |
| `sessionSettings` | `object` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `201` | Response for status 201 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `429` | Response for status 429 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |
| `504` | Response for status 504 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/sessions" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
