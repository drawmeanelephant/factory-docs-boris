---
id: api-reference/computers/create-computers-in-bulk
title: "Create computers in bulk"
status: published
summary: "POST /api/v0/computers/bulk — Create computers in bulk"
parent: api-reference/computers/index
tags: [api-reference, computers, post]
relations: [relates_to=jp/api-reference/computers/create-computers-in-bulk]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Create computers in bulk</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/computers/bulk</span></div>

Creates up to 20 identical managed computers with server-assigned names (`<namePrefix>-<n>`, lowest free suffixes). Creation is fail-fast without rollback: on a mid-batch failure the response is still 201 with the computers created so far plus an `error` describing the failure.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/computers/bulk`
- **Category:** [[api-reference/computers/index|Computers API]]

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `quantity` | `integer` | Yes | Number of identical computers to create. |
| `namePrefix` | `string` | Yes | - |
| `provider` | `string` | No | - |
| `repos` | `array` | No | - |
| `autoInstallDeps` | `boolean` | No | - |
| `serviceAccountId` | `string` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `201` | Response for status 201 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `402` | Response for status 402 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `409` | Response for status 409 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/computers/bulk" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
