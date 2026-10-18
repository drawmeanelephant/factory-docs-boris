---
id: api-reference/organization/invite-or-update-a-user
title: "Invite or update a user"
status: published
summary: "POST /api/v0/organization/users/invite — Invite or update a user"
parent: api-reference/organization/index
tags: [api-reference, organization, post]
relations: [relates_to=jp/api-reference/organization/invite-or-update-a-user]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Invite or update a user</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">POST</span><span class="factory-openapi-path">/api/v0/organization/users/invite</span></div>

Sends an invitation to a user to join the organization. If the user is already a member, updates their role to the specified value. If the user has a pending invite, returns the current status without changes. If the organization has reached its seat limit, returns status "error" with a descriptive error message.

## Endpoint {#endpoint}

- **Method:** `POST`
- **Path:** `/api/v0/organization/users/invite`
- **Category:** [[api-reference/organization/index|Organization API]]

## Request Body {#request-body}

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `email` | `string` | Yes | Email address to invite |
| `role` | `string` | No | Role to assign (defaults to user) |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `200` | Response for status 200 |
| `400` | Response for status 400 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `409` | Response for status 409 |
| `500` | Response for status 500 |

## Example Request {#example-request}

```bash
curl -X POST "https://api.factory.ai/api/v0/organization/users/invite" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
