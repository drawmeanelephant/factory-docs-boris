---
id: api-reference/computers/create-a-computer
title: "Create a computer"
status: published
summary: "POST /api/v0/computers — Create a computer"
parent: api-reference/computers/index
tags: [api-reference, computers, post]
relations: [relates_to=jp/api-reference/computers/create-a-computer]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Create a computer</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/computers</span></div>

Creates a computer. Managed computers are returned in a provisioning state and set up asynchronously; computers registered through Remote Control use an existing machine and are active immediately. Replaying a saved Software Factory Draft receipt returns its existing computer without provisioning another.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/computers`
- **Category:** [[api-reference/computers/index|Computers API]]

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | - |
| `provider` | `string` | No | - |
| `hostId` | `string` | No | - |
| `remoteUser` | `string` | No | - |
| `repos` | `array` | No | - |
| `autoInstallDeps` | `boolean` | No | - |
| `serviceAccountId` | `string` | No | - |
| `source` | `object` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
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
curl -X POST "https://api.factory.ai/api/v0/computers" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
