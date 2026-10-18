---
id: api-reference/service-accounts/create-a-service-account
title: "Create a service account"
status: published
summary: "POST /api/v0/service-accounts — Create a service account"
parent: api-reference/service-accounts/index
tags: [api-reference, service-accounts, post]
relations: [relates_to=jp/api-reference/service-accounts/create-a-service-account]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Create a service account</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/service-accounts</span></div>

Creates a new service account in the authenticated organization. Requires human authentication with a Manager role or higher; service account credentials are rejected.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/service-accounts`
- **Category:** [[api-reference/service-accounts/index|Service Accounts API]]

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | - |
| `description` | `string` | No | Service account description. Must contain well-formed Unicode and no U+0000 characters. |
| `status` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `201` | Response for status 201 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `402` | Response for status 402 |
| `403` | Response for status 403 |
| `409` | Response for status 409 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/service-accounts" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
