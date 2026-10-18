---
id: api-reference/automations/list-ci-automation-jobs
title: "List CI automation jobs"
status: published
summary: "GET /api/v0/automations/ci/jobs — List CI automation jobs"
parent: api-reference/automations/index
tags: [api-reference, automations, get]
relations: [relates_to=jp/api-reference/automations/list-ci-automation-jobs]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List CI automation jobs</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/automations/ci/jobs</span></div>

List CI automation jobs

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/automations/ci/jobs`
- **Category:** [[api-reference/automations/index|Automations API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/automations/ci/jobs" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
