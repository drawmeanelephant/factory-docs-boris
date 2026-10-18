---
id: api-reference/sessions/add-a-message-to-a-session
title: "Add a message to a session"
status: published
summary: "POST /api/v0/sessions/{sessionId}/messages — Add a message to a session"
parent: api-reference/sessions/index
tags: [api-reference, sessions, post]
relations: [relates_to=jp/api-reference/sessions/add-a-message-to-a-session]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Add a message to a session</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/sessions/{sessionId}/messages</span></div>

Adds a user message and optionally waits for agent completion. Supports text, images, and file attachments. This feature is enabled for selected organizations only.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/sessions/{sessionId}/messages`
- **Category:** [[api-reference/sessions/index|Sessions API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `sessionId` | `path` | `string` | Yes | - |

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | `string` | Yes | Message text content |
| `images` | `array` | No | Optional base64-encoded images |
| `files` | `array` | No | Optional file attachments (PDFs, text files) |
| `computerId` | `string` | No | Computer ID to route the message to; falls back to the session.computerId if omitted |
| `sender` | `object` | No | The mission session sending this message (the orchestrator, or an agent by name), stored on the message so clients can attribute it and the model sees a [From …] header. Omit for human messages. |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `429` | Response for status 429 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |
| `504` | Response for status 504 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/sessions/{sessionId}/messages" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
