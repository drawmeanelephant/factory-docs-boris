---
id: api-reference/computers/get-a-computer-by-name
title: "Get a computer by name"
status: published
summary: "GET /api/v0/computers/name/{name} — Get a computer by name"
parent: api-reference/computers/index
tags: [api-reference, computers, get]
relations: [relates_to=jp/api-reference/computers/get-a-computer-by-name]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Get a computer by name</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/computers/name/{name}</span></div>

Returns the caller's computer by name, or a service account's computer when requested by a human Manager or higher.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/computers/name/{name}`
- **Category:** [[api-reference/computers/index|Computers API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `name` | `path` | `string` | Yes | - |
| `serviceAccountId` | `query` | `string` | No | - |
| `includeProvisioningSteps` | `query` | `string` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `402` | Response for status 402 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/computers/name/{name}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
