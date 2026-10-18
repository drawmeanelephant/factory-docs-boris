---
id: jp/api-reference/organization/get-group-credits-limits
title: "Get group credits limits"
status: published
summary: "GET /api/v0/organization/usage/limits/groups — Get group credits limits"
parent: jp/api-reference/organization/index
tags: [api-reference, organization, get]
relations: [relates_to=api-reference/organization/get-group-credits-limits]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Get group credits limits</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/organization/usage/limits/groups</span></div>

Returns the directory-group credits limits mapped for the organization. Each mapping applies the mapped limit to every synced member of the group, between their individual override and the global limit. Members of several mapped groups get the highest mapped limit.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/organization/usage/limits/groups`
- **Category:** [[jp/api-reference/organization/index|Organization API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/organization/usage/limits/groups" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
