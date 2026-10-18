---
id: jp/api-reference/environments/create-a-factory-environment
title: "Create a Factory Environment"
status: published
summary: "POST /api/v0/environments — Create a Factory Environment"
parent: jp/api-reference/environments/index
tags: [api-reference, environments, post]
relations: [relates_to=api-reference/environments/create-a-factory-environment]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Create a Factory Environment</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/environments</span></div>

Create a Factory Environment

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/environments`
- **Category:** [[jp/api-reference/environments/index|Environments API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `201` | Response for status 201 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `405` | Response for status 405 |
| `409` | Response for status 409 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/environments" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
