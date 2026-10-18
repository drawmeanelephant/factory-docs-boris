---
id: api-reference/computers/record-managed-computer-activity
title: "Record managed computer activity"
status: published
summary: "POST /api/v0/computers/{computerId}/activity — Record managed computer activity"
parent: api-reference/computers/index
tags: [api-reference, computers, post]
relations: [relates_to=jp/api-reference/computers/record-managed-computer-activity]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Record managed computer activity</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/computers/{computerId}/activity</span></div>

Advances the inactivity clock for an active managed computer without performing connection or restart work. Not supported for computers connected through Remote Control. Members of a shared session can record activity on the service-account computer that runs it by passing its ID as sharedSessionId.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/computers/{computerId}/activity`
- **Category:** [[api-reference/computers/index|Computers API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `computerId` | `path` | `string` | Yes | - |
| `sharedSessionId` | `query` | `string` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/computers/{computerId}/activity" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
