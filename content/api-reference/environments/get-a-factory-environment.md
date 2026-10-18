---
id: api-reference/environments/get-a-factory-environment
title: "Get a Factory Environment"
status: published
summary: "GET /api/v0/environments/{environmentId} — Get a Factory Environment"
parent: api-reference/environments/index
tags: [api-reference, environments, get]
relations: [relates_to=jp/api-reference/environments/get-a-factory-environment]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Get a Factory Environment</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/environments/{environmentId}</span></div>

Get a Factory Environment

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/environments/{environmentId}`
- **Category:** [[api-reference/environments/index|Environments API]]

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
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/environments/{environmentId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
