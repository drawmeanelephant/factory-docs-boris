---
id: api-reference/wiki/delete-a-wiki-run
title: "Delete a wiki run"
status: published
summary: "DELETE /api/v0/wiki/{wikiRunId} — Delete a wiki run"
parent: api-reference/wiki/index
tags: [api-reference, wiki, delete]
relations: [relates_to=jp/api-reference/wiki/delete-a-wiki-run]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Delete a wiki run</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">DELETE</span><span class="factory-openapi-path">/api/v0/wiki/{wikiRunId}</span></div>

Delete a wiki run

## Endpoint {#endpoint}

- **Method:** `DELETE`
- **Path:** `/api/v0/wiki/{wikiRunId}`
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
curl -X DELETE "https://api.factory.ai/api/v0/wiki/{wikiRunId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
