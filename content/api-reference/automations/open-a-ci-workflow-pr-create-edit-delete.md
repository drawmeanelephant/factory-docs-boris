---
id: api-reference/automations/open-a-ci-workflow-pr-create-edit-delete
title: "Open a CI workflow PR (create / edit / delete)"
status: published
summary: "POST /api/v0/automations/ci/edit — Open a CI workflow PR (create / edit / delete)"
parent: api-reference/automations/index
tags: [api-reference, automations, post]
relations: [relates_to=jp/api-reference/automations/open-a-ci-workflow-pr-create-edit-delete]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Open a CI workflow PR (create / edit / delete)</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/automations/ci/edit</span></div>

Open a CI workflow PR (create / edit / delete)

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/automations/ci/edit`
- **Category:** [[api-reference/automations/index|Automations API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/automations/ci/edit" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
