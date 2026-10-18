---
id: api-reference/environments/retry-a-factory-environment-build
title: "Retry a Factory Environment Build"
status: published
summary: "POST /api/v0/environments/{environmentId}/builds — Retry a Factory Environment Build"
parent: api-reference/environments/index
tags: [api-reference, environments, post]
relations: [relates_to=jp/api-reference/environments/retry-a-factory-environment-build]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Retry a Factory Environment Build</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/environments/{environmentId}/builds</span></div>

Retry a Factory Environment Build

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/environments/{environmentId}/builds`
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
| `409` | Response for status 409 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/environments/{environmentId}/builds" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
