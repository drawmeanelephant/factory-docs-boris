---
id: api-reference/computers/update-a-computer
title: "Update a computer"
status: published
summary: "PATCH /api/v0/computers/{computerId} — Update a computer"
parent: api-reference/computers/index
tags: [api-reference, computers, patch]
relations: [relates_to=jp/api-reference/computers/update-a-computer]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Update a computer</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">PATCH</span><span class="factory-openapi-path">/api/v0/computers/{computerId}</span></div>

Updates a computer's name, remote user, or relay identity. A host ID can be assigned to a computer that does not have one; host IDs are immutable once set and must be unique among the owner's computers.

## Endpoint {#endpoint}

- **Method:** `PATCH`
- **Path:** `/api/v0/computers/{computerId}`
- **Category:** [[api-reference/computers/index|Computers API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `computerId` | `path` | `string` | Yes | - |

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No | - |
| `hostId` | `string` | No | - |
| `computerIdentity` | `object` | No | - |
| `remoteUser` | `string` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `409` | Response for status 409 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X PATCH "https://api.factory.ai/api/v0/computers/{computerId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
