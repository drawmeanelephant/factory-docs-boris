---
id: api-reference/computers/list-computers
title: "List computers"
status: published
summary: "GET /api/v0/computers — List computers"
parent: api-reference/computers/index
tags: [api-reference, computers, get]
relations: [relates_to=jp/api-reference/computers/list-computers]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List computers</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/computers</span></div>

Returns the computers owned by the authenticated client, ordered newest first. Provisioning steps are included only when `includeProvisioningSteps=true`.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/computers`
- **Category:** [[api-reference/computers/index|Computers API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `hostId` | `query` | `string` | No | - |
| `serviceAccountId` | `query` | `string` | No | - |
| `includeProvisioningSteps` | `query` | `string` | No | - |
| `includeUnlisted` | `query` | `string` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `402` | Response for status 402 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/computers" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
