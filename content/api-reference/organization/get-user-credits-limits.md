---
id: api-reference/organization/get-user-credits-limits
title: "Get user credits limits"
status: published
summary: "GET /api/v0/organization/usage/limits/users — Get user credits limits"
parent: api-reference/organization/index
tags: [api-reference, organization, get]
relations: [relates_to=jp/api-reference/organization/get-user-credits-limits]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Get user credits limits</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/organization/usage/limits/users</span></div>

Returns the global per-user credits limit and any individual user overrides for the organization.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/organization/usage/limits/users`
- **Category:** [[api-reference/organization/index|Organization API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/organization/usage/limits/users" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
