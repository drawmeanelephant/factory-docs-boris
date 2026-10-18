---
id: api-reference/wiki/create-a-wiki-video-upload-url
title: "Create a wiki video upload URL"
status: published
summary: "POST /api/v0/wiki/video-upload-url — Create a wiki video upload URL"
parent: api-reference/wiki/index
tags: [api-reference, wiki, post]
relations: [relates_to=jp/api-reference/wiki/create-a-wiki-video-upload-url]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Create a wiki video upload URL</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/wiki/video-upload-url</span></div>

Create a wiki video upload URL

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/wiki/video-upload-url`
- **Category:** [[api-reference/wiki/index|Wiki API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/wiki/video-upload-url" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
