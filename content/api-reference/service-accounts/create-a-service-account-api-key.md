---
id: api-reference/service-accounts/create-a-service-account-api-key
title: "Create a service account API key"
status: published
summary: "POST /api/v0/service-accounts/{serviceAccountId}/api-keys — Create a service account API key"
parent: api-reference/service-accounts/index
tags: [api-reference, service-accounts, post]
relations: [relates_to=jp/api-reference/service-accounts/create-a-service-account-api-key]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Create a service account API key</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/service-accounts/{serviceAccountId}/api-keys</span></div>

Mints a new API key for a service account and returns the one-time key value. The value is shown only once and cannot be retrieved later.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/service-accounts/{serviceAccountId}/api-keys`
- **Category:** [[api-reference/service-accounts/index|Service Accounts API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `serviceAccountId` | `path` | `string` | Yes | - |

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | - |
| `expiresAt` | `integer` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `201` | Response for status 201 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `402` | Response for status 402 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `409` | Response for status 409 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/service-accounts/{serviceAccountId}/api-keys" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
