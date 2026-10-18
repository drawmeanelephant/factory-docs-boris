---
id: jp/api-reference/environments/list-available-factory-environment-sources
title: "List available Factory Environment sources"
status: published
summary: "GET /api/v0/environments/source-options — List available Factory Environment sources"
parent: jp/api-reference/environments/index
tags: [api-reference, environments, get]
relations: [relates_to=api-reference/environments/list-available-factory-environment-sources]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List available Factory Environment sources</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/environments/source-options</span></div>

List available Factory Environment sources

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/environments/source-options`
- **Category:** [[jp/api-reference/environments/index|Environments API]]

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
curl -X GET "https://api.factory.ai/api/v0/environments/source-options" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
