---
id: api-reference/computers/retry-the-install-dependencies-step
title: "Retry the install-dependencies step"
status: published
summary: "POST /api/v0/computers/{computerId}/install-deps — Retry the install-dependencies step"
parent: api-reference/computers/index
tags: [api-reference, computers, post]
relations: [relates_to=jp/api-reference/computers/retry-the-install-dependencies-step]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Retry the install-dependencies step</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/computers/{computerId}/install-deps</span></div>

Starts a new dependency-installation attempt on a managed computer that was configured to install dependencies. Installation runs in the background; returns `202 Accepted` with the updated computer, or `409 Conflict` when an install is already in progress.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/computers/{computerId}/install-deps`
- **Category:** [[api-reference/computers/index|Computers API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `computerId` | `path` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `202` | Response for status 202 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `404` | Response for status 404 |
| `409` | Response for status 409 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/computers/{computerId}/install-deps" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
