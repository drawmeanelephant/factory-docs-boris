---
id: api-reference/service-accounts/update-a-service-account
title: "Update a service account"
status: published
summary: "PATCH /api/v0/service-accounts/{serviceAccountId} — Update a service account"
parent: api-reference/service-accounts/index
tags: [api-reference, service-accounts, patch]
relations: [relates_to=jp/api-reference/service-accounts/update-a-service-account]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Update a service account</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">PATCH</span><span class="factory-openapi-path">/api/v0/service-accounts/{serviceAccountId}</span></div>

Updates a service account description or status. Name is immutable. Requires human authentication with a Manager role or higher; service account credentials are rejected.

## Endpoint {#endpoint}

- **Method:** `PATCH`
- **Path:** `/api/v0/service-accounts/{serviceAccountId}`
- **Category:** [[api-reference/service-accounts/index|Service Accounts API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `serviceAccountId` | `path` | `string` | Yes | - |

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `description` | `string` | No | Service account description. Must contain well-formed Unicode and no U+0000 characters. |
| `status` | `string` | No | - |

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

## Example Request {#example-request}

```bash
curl -X PATCH "https://api.factory.ai/api/v0/service-accounts/{serviceAccountId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
