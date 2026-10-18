---
id: api-reference/sessions/get-a-message-by-id
title: "Get a message by ID"
status: published
summary: "GET /api/v0/sessions/{sessionId}/messages/{messageId} — Get a message by ID"
parent: api-reference/sessions/index
tags: [api-reference, sessions, get]
relations: [relates_to=jp/api-reference/sessions/get-a-message-by-id]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Get a message by ID</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/sessions/{sessionId}/messages/{messageId}</span></div>

Returns a single message from the session by its ID. This feature is enabled for selected organizations only.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/sessions/{sessionId}/messages/{messageId}`
- **Category:** [[api-reference/sessions/index|Sessions API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `sessionId` | `path` | `string` | Yes | - |
| `messageId` | `path` | `string` | Yes | - |
| `computerId` | `query` | `string` | No | - |

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
curl -X GET "https://api.factory.ai/api/v0/sessions/{sessionId}/messages/{messageId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
