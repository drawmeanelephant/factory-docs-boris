---
id: jp/api-reference/automations/list-github-actions-runs-for-ci-automation-workflows
title: "List GitHub Actions runs for CI automation workflows"
status: published
summary: "GET /api/v0/automations/ci/runs — List GitHub Actions runs for CI automation workflows"
parent: jp/api-reference/automations/index
tags: [api-reference, automations, get]
relations: [relates_to=api-reference/automations/list-github-actions-runs-for-ci-automation-workflows]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List GitHub Actions runs for CI automation workflows</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/automations/ci/runs</span></div>

List GitHub Actions runs for CI automation workflows

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/automations/ci/runs`
- **Category:** [[jp/api-reference/automations/index|Automations API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/automations/ci/runs" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
