---
id: jp/api-reference/sessions/update-a-session
title: "Update a session"
status: published
summary: "PATCH /api/v0/sessions/{sessionId} — Update a session"
parent: jp/api-reference/sessions/index
tags: [api-reference, sessions, patch]
relations: [relates_to=api-reference/sessions/update-a-session]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Update a session</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">PATCH</span><span class="factory-openapi-path">/api/v0/sessions/{sessionId}</span></div>

Updates session configuration such as model and reasoning effort. This feature is enabled for selected organizations only.

## Endpoint {#endpoint}

- **Method:** `PATCH`
- **Path:** `/api/v0/sessions/{sessionId}`
- **Category:** [[jp/api-reference/sessions/index|Sessions API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `sessionId` | `path` | `string` | Yes | - |

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sessionSettings` | `object` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X PATCH "https://api.factory.ai/api/v0/sessions/{sessionId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
