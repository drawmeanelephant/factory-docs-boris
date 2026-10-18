---
id: api-reference/computers/list-available-computer-providers
title: "List available computer providers"
status: published
summary: "GET /api/v0/computers/providers — List available computer providers"
parent: api-reference/computers/index
tags: [api-reference, computers, get]
relations: [relates_to=jp/api-reference/computers/list-available-computer-providers]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List available computer providers</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/computers/providers</span></div>

Returns the managed compute providers currently available for new computers in the authenticated organization.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/computers/providers`
- **Category:** [[api-reference/computers/index|Computers API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/computers/providers" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
