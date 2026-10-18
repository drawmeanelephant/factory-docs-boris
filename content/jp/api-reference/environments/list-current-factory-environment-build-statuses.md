---
id: jp/api-reference/environments/list-current-factory-environment-build-statuses
title: "List current Factory Environment build statuses"
status: published
summary: "GET /api/v0/environments/build-statuses — List current Factory Environment build statuses"
parent: jp/api-reference/environments/index
tags: [api-reference, environments, get]
relations: [relates_to=api-reference/environments/list-current-factory-environment-build-statuses]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List current Factory Environment build statuses</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/environments/build-statuses</span></div>

List current Factory Environment build statuses

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/environments/build-statuses`
- **Category:** [[jp/api-reference/environments/index|Environments API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `environmentIds` | `query` | `array` | Yes | - |
| `serviceAccountId` | `query` | `string` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/environments/build-statuses" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
