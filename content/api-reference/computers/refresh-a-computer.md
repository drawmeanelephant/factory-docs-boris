---
id: api-reference/computers/refresh-a-computer
title: "Refresh a computer"
status: published
summary: "POST /api/v0/computers/{computerId}/refresh — Refresh a computer"
parent: api-reference/computers/index
tags: [api-reference, computers, post]
relations: [relates_to=jp/api-reference/computers/refresh-a-computer]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Refresh a computer</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/computers/{computerId}/refresh</span></div>

Refreshes the Git credentials and user-owned computer secrets on a managed computer. Computers connected through Remote Control are not modified and return zero counts.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/computers/{computerId}/refresh`
- **Category:** [[api-reference/computers/index|Computers API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `computerId` | `path` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/computers/{computerId}/refresh" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
