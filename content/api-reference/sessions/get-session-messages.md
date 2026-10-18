---
id: api-reference/sessions/get-session-messages
title: "Get session messages"
status: published
summary: "GET /api/v0/sessions/{sessionId}/messages — Get session messages"
parent: api-reference/sessions/index
tags: [api-reference, sessions, get]
relations: [relates_to=jp/api-reference/sessions/get-session-messages]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Get session messages</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/sessions/{sessionId}/messages</span></div>

Returns paginated message history with optional role filtering. This feature is enabled for selected organizations only.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/sessions/{sessionId}/messages`
- **Category:** [[api-reference/sessions/index|Sessions API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `sessionId` | `path` | `string` | Yes | - |
| `limit` | `query` | `string` | No | - |
| `cursor` | `query` | `string` | No | - |
| `computerId` | `query` | `string` | No | - |
| `role` | `query` | `string` | No | - |

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
| `504` | Response for status 504 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/sessions/{sessionId}/messages" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
