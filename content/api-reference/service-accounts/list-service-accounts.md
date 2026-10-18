---
id: api-reference/service-accounts/list-service-accounts
title: "List service accounts"
status: published
summary: "GET /api/v0/service-accounts — List service accounts"
parent: api-reference/service-accounts/index
tags: [api-reference, service-accounts, get]
relations: [relates_to=jp/api-reference/service-accounts/list-service-accounts]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List service accounts</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/service-accounts</span></div>

Returns all service accounts in the authenticated organization. Requires human authentication with a Manager role or higher; service account credentials are rejected.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/service-accounts`
- **Category:** [[api-reference/service-accounts/index|Service Accounts API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `402` | Response for status 402 |
| `403` | Response for status 403 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/service-accounts" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
