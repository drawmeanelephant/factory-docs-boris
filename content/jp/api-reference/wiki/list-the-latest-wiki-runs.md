---
id: jp/api-reference/wiki/list-the-latest-wiki-runs
title: "List the latest wiki runs"
status: published
summary: "GET /api/v0/wiki — List the latest wiki runs"
parent: jp/api-reference/wiki/index
tags: [api-reference, wiki, get]
relations: [relates_to=api-reference/wiki/list-the-latest-wiki-runs]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List the latest wiki runs</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/wiki</span></div>

List the latest wiki runs

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/wiki`
- **Category:** [[jp/api-reference/wiki/index|Wiki API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/wiki" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
