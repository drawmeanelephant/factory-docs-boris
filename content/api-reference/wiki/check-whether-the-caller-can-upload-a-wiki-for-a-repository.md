---
id: api-reference/wiki/check-whether-the-caller-can-upload-a-wiki-for-a-repository
title: "Check whether the caller can upload a wiki for a repository"
status: published
summary: "GET /api/v0/wiki/upload-access — Check whether the caller can upload a wiki for a repository"
parent: api-reference/wiki/index
tags: [api-reference, wiki, get]
relations: [relates_to=jp/api-reference/wiki/check-whether-the-caller-can-upload-a-wiki-for-a-repository]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Check whether the caller can upload a wiki for a repository</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/wiki/upload-access</span></div>

Check whether the caller can upload a wiki for a repository

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/wiki/upload-access`
- **Category:** [[api-reference/wiki/index|Wiki API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `repoUrl` | `query` | `string` | Yes | Repository URL that will be passed to POST /api/v0/wiki |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/wiki/upload-access" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
