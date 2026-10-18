---
id: jp/api-reference/sessions/delete-a-session
title: "Delete a session"
status: published
summary: "DELETE /api/v0/sessions/{sessionId} — Delete a session"
parent: jp/api-reference/sessions/index
tags: [api-reference, sessions, delete]
relations: [relates_to=api-reference/sessions/delete-a-session]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Delete a session</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">DELETE</span><span class="factory-openapi-path">/api/v0/sessions/{sessionId}</span></div>

Deletes a session (can be restored within retention period). This feature is enabled for selected organizations only.

## Endpoint {#endpoint}

- **Method:** `DELETE`
- **Path:** `/api/v0/sessions/{sessionId}`
- **Category:** [[jp/api-reference/sessions/index|Sessions API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `sessionId` | `path` | `string` | Yes | - |
| `computerId` | `query` | `string` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `204` | Response for status 204 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X DELETE "https://api.factory.ai/api/v0/sessions/{sessionId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
