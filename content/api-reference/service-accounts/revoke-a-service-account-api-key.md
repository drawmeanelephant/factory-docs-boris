---
id: api-reference/service-accounts/revoke-a-service-account-api-key
title: "Revoke a service account API key"
status: published
summary: "POST /api/v0/service-accounts/{serviceAccountId}/api-keys/{keyId}/revoke — Revoke a service account API key"
parent: api-reference/service-accounts/index
tags: [api-reference, service-accounts, post]
relations: [relates_to=jp/api-reference/service-accounts/revoke-a-service-account-api-key]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Revoke a service account API key</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/service-accounts/{serviceAccountId}/api-keys/{keyId}/revoke</span></div>

Revokes an API key for a service account. Once revoked, the key can no longer authenticate. Idempotent.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/service-accounts/{serviceAccountId}/api-keys/{keyId}/revoke`
- **Category:** [[api-reference/service-accounts/index|Service Accounts API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `serviceAccountId` | `path` | `string` | Yes | - |
| `keyId` | `path` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `204` | Response for status 204 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/service-accounts/{serviceAccountId}/api-keys/{keyId}/revoke" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
