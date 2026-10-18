---
id: api-reference/service-accounts/rotate-a-service-account-api-key
title: "Rotate a service account API key"
status: published
summary: "POST /api/v0/service-accounts/{serviceAccountId}/api-keys/{keyId}/rotate — Rotate a service account API key"
parent: api-reference/service-accounts/index
tags: [api-reference, service-accounts, post]
relations: [relates_to=jp/api-reference/service-accounts/rotate-a-service-account-api-key]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Rotate a service account API key</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/service-accounts/{serviceAccountId}/api-keys/{keyId}/rotate</span></div>

DESTRUCTIVE: atomically revokes the existing key and issues a replacement that inherits its name, returning the new one-time key value (shown only once). The previous key stops authenticating the instant this call succeeds, so any client still using it will immediately start failing with 401. Update every consumer with the new value before rotating, or set `gracePeriodMinutes` to keep the old key valid for a short overlap window.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/service-accounts/{serviceAccountId}/api-keys/{keyId}/rotate`
- **Category:** [[api-reference/service-accounts/index|Service Accounts API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `serviceAccountId` | `path` | `string` | Yes | - |
| `keyId` | `path` | `string` | Yes | - |

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `expiresAt` | `integer` | No | - |
| `gracePeriodMinutes` | `integer` | No | How long (0-10 minutes) the rotated-from key stays valid after rotation. Omit or 0 revokes it immediately. Rejected with a 400 if the key would expire before the grace window ends (the grace period never extends a key lifetime). |

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

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/service-accounts/{serviceAccountId}/api-keys/{keyId}/rotate" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
