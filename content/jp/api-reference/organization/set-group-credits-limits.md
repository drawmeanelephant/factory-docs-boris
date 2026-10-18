---
id: jp/api-reference/organization/set-group-credits-limits
title: "Set group credits limits"
status: published
summary: "PUT /api/v0/organization/usage/limits/groups — Set group credits limits"
parent: jp/api-reference/organization/index
tags: [api-reference, organization, put]
relations: [relates_to=api-reference/organization/set-group-credits-limits]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Set group credits limits</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">PUT</span><span class="factory-openapi-path">/api/v0/organization/usage/limits/groups</span></div>

Map synced directory groups to per-member credits limits (up to 100 per request). Identify each group by its stable WorkOS group id; renaming a group in your identity provider never changes the id, so mappings survive renames. Pass null for limit to unmap a group (members fall back to the global limit). Enforcement is read-time: members pick a mapping change up at their next request, with no per-user writes.

## Endpoint {#endpoint}

- **Method:** `PUT`
- **Path:** `/api/v0/organization/usage/limits/groups`
- **Category:** [[jp/api-reference/organization/index|Organization API]]

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `groups` | `array` | Yes | Array of group limit entries (up to 100). Each maps a synced directory group to a per-member credits limit. |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X PUT "https://api.factory.ai/api/v0/organization/usage/limits/groups" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
