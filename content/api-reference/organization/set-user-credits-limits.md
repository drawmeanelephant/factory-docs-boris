---
id: api-reference/organization/set-user-credits-limits
title: "Set user credits limits"
status: published
summary: "PUT /api/v0/organization/usage/limits/users — Set user credits limits"
parent: api-reference/organization/index
tags: [api-reference, organization, put]
relations: [relates_to=jp/api-reference/organization/set-user-credits-limits]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Set user credits limits</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">PUT</span><span class="factory-openapi-path">/api/v0/organization/usage/limits/users</span></div>

Set individual per-user credits limits for one or more users. Supports bulk updates (up to 100 users per request). Identify each user by email. Pass null for limit to remove an individual override.

## Endpoint {#endpoint}

- **Method:** `PUT`
- **Path:** `/api/v0/organization/usage/limits/users`
- **Category:** [[api-reference/organization/index|Organization API]]

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `users` | `array` | Yes | Array of user limit entries (up to 100). Each identifies a user by email. |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X PUT "https://api.factory.ai/api/v0/organization/usage/limits/users" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
