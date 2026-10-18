---
id: jp/api-reference/environments/delete-a-factory-environment
title: "Delete a Factory Environment"
status: published
summary: "DELETE /api/v0/environments/{environmentId} — Delete a Factory Environment"
parent: jp/api-reference/environments/index
tags: [api-reference, environments, delete]
relations: [relates_to=api-reference/environments/delete-a-factory-environment]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Delete a Factory Environment</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">DELETE</span><span class="factory-openapi-path">/api/v0/environments/{environmentId}</span></div>

Delete a Factory Environment

## Endpoint {#endpoint}

- **Method:** `DELETE`
- **Path:** `/api/v0/environments/{environmentId}`
- **Category:** [[jp/api-reference/environments/index|Environments API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `environmentId` | `path` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `204` | Response for status 204 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `409` | Response for status 409 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X DELETE "https://api.factory.ai/api/v0/environments/{environmentId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
