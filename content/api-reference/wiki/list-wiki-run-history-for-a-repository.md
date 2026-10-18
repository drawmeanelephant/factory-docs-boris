---
id: api-reference/wiki/list-wiki-run-history-for-a-repository
title: "List wiki run history for a repository"
status: published
summary: "GET /api/v0/wiki/history/{repoUrl} — List wiki run history for a repository"
parent: api-reference/wiki/index
tags: [api-reference, wiki, get]
relations: [relates_to=jp/api-reference/wiki/list-wiki-run-history-for-a-repository]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List wiki run history for a repository</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/wiki/history/{repoUrl}</span></div>

List wiki run history for a repository

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/wiki/history/{repoUrl}`
- **Category:** [[api-reference/wiki/index|Wiki API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `repoUrl` | `path` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/wiki/history/{repoUrl}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
