---
id: api-reference/organization/list-organization-computer-secret-names
title: "List organization computer secret names"
status: published
summary: "GET /api/v0/organization/computer-secrets — List organization computer secret names"
parent: api-reference/organization/index
tags: [api-reference, organization, get]
relations: [relates_to=jp/api-reference/organization/list-organization-computer-secret-names]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">List organization computer secret names</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">GET</span><span class="factory-openapi-path">/api/v0/organization/computer-secrets</span></div>

Lists names of write-only secrets shared by managed computers in the authenticated organization. Persisted plaintext values are never returned.

## Endpoint {#endpoint}

- **Method:** `GET`
- **Path:** `/api/v0/organization/computer-secrets`
- **Category:** [[api-reference/organization/index|Organization API]]

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X GET "https://api.factory.ai/api/v0/organization/computer-secrets" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
