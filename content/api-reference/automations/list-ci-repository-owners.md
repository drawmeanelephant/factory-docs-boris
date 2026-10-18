---
id: api-reference/automations/list-ci-repository-owners
title: "List CI repository owners"
status: published
summary: "GET /api/v0/automations/ci/repository-owners — List CI repository owners"
parent: api-reference/automations/index
tags: [api-reference, automations, get]
relations: [relates_to=jp/api-reference/automations/list-ci-repository-owners]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List CI repository owners</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/automations/ci/repository-owners</span></div>

List CI repository owners

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/automations/ci/repository-owners`
- **Category:** [[api-reference/automations/index|Automations API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/automations/ci/repository-owners" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
