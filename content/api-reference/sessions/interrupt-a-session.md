---
id: api-reference/sessions/interrupt-a-session
title: "Interrupt a session"
status: published
summary: "POST /api/v0/sessions/{sessionId}/interrupt — Interrupt a session"
parent: api-reference/sessions/index
tags: [api-reference, sessions, post]
relations: [relates_to=jp/api-reference/sessions/interrupt-a-session]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Interrupt a session</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/sessions/{sessionId}/interrupt</span></div>

Interrupts a running agent loop. Idempotent if already idle. This feature is enabled for selected organizations only.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/sessions/{sessionId}/interrupt`
- **Category:** [[api-reference/sessions/index|Sessions API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `sessionId` | `path` | `string` | Yes | - |

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
curl -X POST "https://api.factory.ai/api/v0/sessions/{sessionId}/interrupt" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
