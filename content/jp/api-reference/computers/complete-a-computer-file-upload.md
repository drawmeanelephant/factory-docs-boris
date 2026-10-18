---
id: jp/api-reference/computers/complete-a-computer-file-upload
title: "Complete a computer file upload"
status: published
summary: "POST /api/v0/computers/{computerId}/files/{fileName}/complete-upload — Complete a computer file upload"
parent: jp/api-reference/computers/index
tags: [api-reference, computers, post]
relations: [relates_to=api-reference/computers/complete-a-computer-file-upload]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Complete a computer file upload</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/computers/{computerId}/files/{fileName}/complete-upload</span></div>

Completes a file upload by writing the previously uploaded file into the computer's workspace. Returns `409 Conflict` if a file with that name already exists.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/computers/{computerId}/files/{fileName}/complete-upload`
- **Category:** [[jp/api-reference/computers/index|Computers API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `computerId` | `path` | `string` | Yes | - |
| `fileName` | `path` | `string` | Yes | - |

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `transferId` | `string` | Yes | - |
| `sessionId` | `string` | Yes | - |
| `destPath` | `string` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `409` | Response for status 409 |
| `424` | Response for status 424 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/computers/{computerId}/files/{fileName}/complete-upload" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
