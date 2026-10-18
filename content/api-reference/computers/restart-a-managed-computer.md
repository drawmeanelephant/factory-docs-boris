---
id: api-reference/computers/restart-a-managed-computer
title: "Restart a managed computer"
status: published
summary: "POST /api/v0/computers/{computerId}/restart — Restart a managed computer"
parent: api-reference/computers/index
tags: [api-reference, computers, post]
relations: [relates_to=jp/api-reference/computers/restart-a-managed-computer]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Restart a managed computer</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/computers/{computerId}/restart</span></div>

Defaults to resume: resumes an offline computer and leaves a live daemon untouched (wasRestarted: false). Explicit reboot cold-boots from persisted files, stops all processes, and discards memory and unflushed writes. Reboot returns HTTP 200 only after the daemon reconnects. Unsupported provider modes are rejected. Not supported for computers connected through Remote Control. Errors use non-2xx HTTP status codes with status, title, and detail fields.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/computers/{computerId}/restart`
- **Category:** [[api-reference/computers/index|Computers API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `computerId` | `path` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `402` | Response for status 402 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `409` | Response for status 409 |
| `429` | Response for status 429 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/computers/{computerId}/restart" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
