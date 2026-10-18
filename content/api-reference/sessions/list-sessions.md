---
id: api-reference/sessions/list-sessions
title: "List sessions"
status: published
summary: "GET /api/v0/sessions — List sessions"
parent: api-reference/sessions/index
tags: [api-reference, sessions, get]
relations: [relates_to=jp/api-reference/sessions/list-sessions]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List sessions</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/sessions</span></div>

Returns a paginated list of sessions for the authenticated user. This feature is enabled for selected organizations only.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/sessions`
- **Category:** [[api-reference/sessions/index|Sessions API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `limit` | `query` | `string` | No | - |
| `cursor` | `query` | `string` | No | - |
| `computerId` | `query` | `string` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/sessions" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
