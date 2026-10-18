---
id: api-reference/wiki/get-a-wiki-page
title: "Get a wiki page"
status: published
summary: "GET /api/v0/wiki/{wikiRunId}/pages/{pageId} — Get a wiki page"
parent: api-reference/wiki/index
tags: [api-reference, wiki, get]
relations: [relates_to=jp/api-reference/wiki/get-a-wiki-page]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Get a wiki page</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/wiki/{wikiRunId}/pages/{pageId}</span></div>

Get a wiki page

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/wiki/{wikiRunId}/pages/{pageId}`
- **Category:** [[api-reference/wiki/index|Wiki API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wikiRunId` | `path` | `string` | Yes | - |
| `pageId` | `path` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/wiki/{wikiRunId}/pages/{pageId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
