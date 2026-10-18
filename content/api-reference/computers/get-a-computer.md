---
id: api-reference/computers/get-a-computer
title: "Get a computer"
status: published
summary: "GET /api/v0/computers/{computerId} — Get a computer"
parent: api-reference/computers/index
tags: [api-reference, computers, get]
relations: [relates_to=jp/api-reference/computers/get-a-computer]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Get a computer</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/computers/{computerId}</span></div>

Returns a computer by ID. Callers can access their own computers; organization members with the manager role or higher can also access service-account-owned computers, and members of a shared session can access the service-account computer that runs it by passing its ID as sharedSessionId.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/computers/{computerId}`
- **Category:** [[api-reference/computers/index|Computers API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `computerId` | `path` | `string` | Yes | - |
| `sharedSessionId` | `query` | `string` | No | - |
| `includeProvisioningSteps` | `query` | `string` | No | - |

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
curl -X GET "https://api.factory.ai/api/v0/computers/{computerId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
