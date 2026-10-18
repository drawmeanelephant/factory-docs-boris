---
id: jp/api-reference/wiki/export-a-wiki-run-as-a-zip
title: "Export a wiki run as a zip"
status: published
summary: "GET /api/v0/wiki/{wikiRunId}/export — Export a wiki run as a zip"
parent: jp/api-reference/wiki/index
tags: [api-reference, wiki, get]
relations: [relates_to=api-reference/wiki/export-a-wiki-run-as-a-zip]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Export a wiki run as a zip</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/wiki/{wikiRunId}/export</span></div>

Export a wiki run as a zip

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/wiki/{wikiRunId}/export`
- **Category:** [[jp/api-reference/wiki/index|Wiki API]]

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
curl -X GET "https://api.factory.ai/api/v0/wiki/{wikiRunId}/export" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
