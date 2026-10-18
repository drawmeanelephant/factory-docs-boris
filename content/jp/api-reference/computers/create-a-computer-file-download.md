---
id: jp/api-reference/computers/create-a-computer-file-download
title: "Create a computer file download"
status: published
summary: "POST /api/v0/computers/{computerId}/files/{fileName}/create-download — Create a computer file download"
parent: jp/api-reference/computers/index
tags: [api-reference, computers, post]
relations: [relates_to=api-reference/computers/create-a-computer-file-download]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Create a computer file download</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/computers/{computerId}/files/{fileName}/create-download</span></div>

Creates a download for a file in the computer's workspace and returns a time-limited download URL.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/computers/{computerId}/files/{fileName}/create-download`
- **Category:** [[jp/api-reference/computers/index|Computers API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `computerId` | `path` | `string` | Yes | - |
| `fileName` | `path` | `string` | Yes | - |

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sessionId` | `string` | Yes | - |
| `cwd` | `string` | No | - |
| `filePath` | `string` | No | - |
| `contentType` | `string` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `424` | Response for status 424 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/computers/{computerId}/files/{fileName}/create-download" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
