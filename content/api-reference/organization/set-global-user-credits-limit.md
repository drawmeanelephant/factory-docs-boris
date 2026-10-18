---
id: api-reference/organization/set-global-user-credits-limit
title: "Set global user credits limit"
status: published
summary: "PUT /api/v0/organization/usage/limits/global — Set global user credits limit"
parent: api-reference/organization/index
tags: [api-reference, organization, put]
relations: [relates_to=jp/api-reference/organization/set-global-user-credits-limit]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Set global user credits limit</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">PUT</span><span class="factory-openapi-path">/api/v0/organization/usage/limits/global</span></div>

Set the global per-user credits limit for the organization. This limit applies to all users who do not have an individual override. Pass null to remove the global limit.

## Endpoint {#endpoint}

- **Method:** `PUT`
- **Path:** `/api/v0/organization/usage/limits/global`
- **Category:** [[api-reference/organization/index|Organization API]]

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | `integer` | Yes | Global per-user credits limit (minimum 1,000,000). Pass null to remove the global limit. |

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
curl -X PUT "https://api.factory.ai/api/v0/organization/usage/limits/global" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
