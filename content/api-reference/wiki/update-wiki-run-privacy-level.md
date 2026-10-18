---
id: api-reference/wiki/update-wiki-run-privacy-level
title: "Update wiki run privacy level"
status: published
summary: "POST /api/v0/wiki/{wikiRunId}/privacy — Update wiki run privacy level"
parent: api-reference/wiki/index
tags: [api-reference, wiki, post]
relations: [relates_to=jp/api-reference/wiki/update-wiki-run-privacy-level]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Update wiki run privacy level</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/wiki/{wikiRunId}/privacy</span></div>

Update wiki run privacy level

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/wiki/{wikiRunId}/privacy`
- **Category:** [[api-reference/wiki/index|Wiki API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wikiRunId` | `path` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/wiki/{wikiRunId}/privacy" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
