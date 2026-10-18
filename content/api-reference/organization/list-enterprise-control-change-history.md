---
id: api-reference/organization/list-enterprise-control-change-history
title: "List enterprise control change history"
status: published
summary: "GET /api/v0/organization/enterprise-controls/history — List enterprise control change history"
parent: api-reference/organization/index
tags: [api-reference, organization, get]
relations: [relates_to=jp/api-reference/organization/list-enterprise-control-change-history]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List enterprise control change history</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/organization/enterprise-controls/history</span></div>

Returns a paginated list of enterprise control setting changes for the organization, ordered by revision descending. Properties for the `settings` object may be added, removed, or renamed between API versions. Clients should parse it as a generic JSON object.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/organization/enterprise-controls/history`
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
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/organization/enterprise-controls/history" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
