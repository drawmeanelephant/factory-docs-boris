---
id: api-reference/service-accounts/get-a-service-account
title: "Get a service account"
status: published
summary: "GET /api/v0/service-accounts/{serviceAccountId} — Get a service account"
parent: api-reference/service-accounts/index
tags: [api-reference, service-accounts, get]
relations: [relates_to=jp/api-reference/service-accounts/get-a-service-account]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Get a service account</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/service-accounts/{serviceAccountId}</span></div>

Returns a single service account by ID. Requires human authentication with a Manager role or higher; service account credentials are rejected.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/service-accounts/{serviceAccountId}`
- **Category:** [[api-reference/service-accounts/index|Service Accounts API]]

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
curl -X GET "https://api.factory.ai/api/v0/service-accounts/{serviceAccountId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
