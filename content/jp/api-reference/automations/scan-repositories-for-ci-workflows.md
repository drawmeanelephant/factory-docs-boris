---
id: jp/api-reference/automations/scan-repositories-for-ci-workflows
title: "Scan repositories for CI workflows"
status: published
summary: "GET /api/v0/automations/ci/scan — Scan repositories for CI workflows"
parent: jp/api-reference/automations/index
tags: [api-reference, automations, get]
relations: [relates_to=api-reference/automations/scan-repositories-for-ci-workflows]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Scan repositories for CI workflows</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/automations/ci/scan</span></div>

Scan repositories for CI workflows

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/automations/ci/scan`
- **Category:** [[jp/api-reference/automations/index|Automations API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/automations/ci/scan" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
