---
id: jp/api-reference/environments/provision-the-organization-default-factory-environment-if-none-exists
title: "Provision the organization default Factory Environment if none exists"
status: published
summary: "POST /api/v0/environments/default — Provision the organization default Factory Environment if none exists"
parent: jp/api-reference/environments/index
tags: [api-reference, environments, post]
relations: [relates_to=api-reference/environments/provision-the-organization-default-factory-environment-if-none-exists]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Provision the organization default Factory Environment if none exists</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/environments/default</span></div>

Provision the organization default Factory Environment if none exists

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/environments/default`
- **Category:** [[jp/api-reference/environments/index|Environments API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `204` | Response for status 204 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/environments/default" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
