---
id: api-reference/organization/update-organization-computer-secrets
title: "Update organization computer secrets"
status: published
summary: "PATCH /api/v0/organization/computer-secrets — Update organization computer secrets"
parent: api-reference/organization/index
tags: [api-reference, organization, patch]
relations: [relates_to=jp/api-reference/organization/update-organization-computer-secrets]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Update organization computer secrets</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">PATCH</span><span class="factory-openapi-path">/api/v0/organization/computer-secrets</span></div>

Atomically upserts and deletes write-only secrets shared by managed computers in the authenticated organization. Responses include names only.

## Endpoint {#endpoint}

- **Method:** `PATCH`
- **Path:** `/api/v0/organization/computer-secrets`
- **Category:** [[api-reference/organization/index|Organization API]]

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `createOnly` | `boolean` | No | - |
| `upsert` | `array` | Yes | - |
| `delete` | `array` | Yes | - |

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
curl -X PATCH "https://api.factory.ai/api/v0/organization/computer-secrets" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
