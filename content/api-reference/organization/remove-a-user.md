---
id: api-reference/organization/remove-a-user
title: "Remove a user"
status: published
summary: "DELETE /api/v0/organization/users — Remove a user"
parent: api-reference/organization/index
tags: [api-reference, organization, delete]
relations: [relates_to=jp/api-reference/organization/remove-a-user]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Remove a user</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">DELETE</span><span class="factory-openapi-path">/api/v0/organization/users</span></div>

Removes a user from the organization by email. Works for both active members (deletes membership) and pending invitations (revokes the invite).

## Endpoint {#endpoint}

- **Method:** `DELETE`
- **Path:** `/api/v0/organization/users`
- **Category:** [[api-reference/organization/index|Organization API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `email` | `query` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `204` | Response for status 204 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `409` | Response for status 409 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X DELETE "https://api.factory.ai/api/v0/organization/users" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
