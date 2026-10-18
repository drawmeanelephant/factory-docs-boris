---
id: jp/api-reference/environments/update-a-factory-environment
title: "Update a Factory Environment"
status: published
summary: "PATCH /api/v0/environments/{environmentId} — Update a Factory Environment"
parent: jp/api-reference/environments/index
tags: [api-reference, environments, patch]
relations: [relates_to=api-reference/environments/update-a-factory-environment]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Update a Factory Environment</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">PATCH</span><span class="factory-openapi-path">/api/v0/environments/{environmentId}</span></div>

Update a Factory Environment

## Endpoint {#endpoint}

- **Method:** `PATCH`
- **Path:** `/api/v0/environments/{environmentId}`
- **Category:** [[jp/api-reference/environments/index|Environments API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `environmentId` | `path` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `409` | Response for status 409 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X PATCH "https://api.factory.ai/api/v0/environments/{environmentId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
