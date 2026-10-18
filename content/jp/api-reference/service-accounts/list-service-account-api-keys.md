---
id: jp/api-reference/service-accounts/list-service-account-api-keys
title: "List service account API keys"
status: published
summary: "GET /api/v0/service-accounts/{serviceAccountId}/api-keys — List service account API keys"
parent: jp/api-reference/service-accounts/index
tags: [api-reference, service-accounts, get]
relations: [relates_to=api-reference/service-accounts/list-service-account-api-keys]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List service account API keys</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/service-accounts/{serviceAccountId}/api-keys</span></div>

Returns all API keys for a service account, active and inactive. Each item carries `isRevoked`, `expiresAt`, and `revokedAt` so clients can split them into active/inactive views.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/service-accounts/{serviceAccountId}/api-keys`
- **Category:** [[jp/api-reference/service-accounts/index|Service Accounts API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `serviceAccountId` | `path` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `402` | Response for status 402 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/service-accounts/{serviceAccountId}/api-keys" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
