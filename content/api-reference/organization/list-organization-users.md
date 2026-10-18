---
id: api-reference/organization/list-organization-users
title: "List organization users"
status: published
summary: "GET /api/v0/organization/users — List organization users"
parent: api-reference/organization/index
tags: [api-reference, organization, get]
relations: [relates_to=jp/api-reference/organization/list-organization-users]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List organization users</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/organization/users</span></div>

Returns a paginated list of users in the Factory organization.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/organization/users`
- **Category:** [[api-reference/organization/index|Organization API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `limit` | `query` | `string` | No | - |
| `cursor` | `query` | `string` | No | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/organization/users" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
