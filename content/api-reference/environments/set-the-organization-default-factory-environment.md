---
id: api-reference/environments/set-the-organization-default-factory-environment
title: "Set the organization default Factory Environment"
status: published
summary: "PUT /api/v0/environments/default — Set the organization default Factory Environment"
parent: api-reference/environments/index
tags: [api-reference, environments, put]
relations: [relates_to=jp/api-reference/environments/set-the-organization-default-factory-environment]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Set the organization default Factory Environment</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">PUT</span><span class="factory-openapi-path">/api/v0/environments/default</span></div>

Set the organization default Factory Environment

## Endpoint {#endpoint}

- **Method:** `PUT`
- **Path:** `/api/v0/environments/default`
- **Category:** [[api-reference/environments/index|Environments API]]

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `environmentId` | `string` | Yes | - |

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
curl -X PUT "https://api.factory.ai/api/v0/environments/default" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
