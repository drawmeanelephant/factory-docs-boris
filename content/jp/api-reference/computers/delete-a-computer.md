---
id: jp/api-reference/computers/delete-a-computer
title: "Delete a computer"
status: published
summary: "DELETE /api/v0/computers/{computerId} — Delete a computer"
parent: jp/api-reference/computers/index
tags: [api-reference, computers, delete]
relations: [relates_to=api-reference/computers/delete-a-computer]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Delete a computer</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<div class="factory-openapi-endpoint"><span class="factory-openapi-method">DELETE</span><span class="factory-openapi-path">/api/v0/computers/{computerId}</span></div>

Permanently deletes a computer. Deleting a managed computer also shuts down its hosted environment and archives its sessions; deleting a computer connected through Remote Control removes the registration but leaves the machine and its sessions intact. Automations running on the computer are paused.

## Endpoint {#endpoint}

- **Method:** `DELETE`
- **Path:** `/api/v0/computers/{computerId}`
- **Category:** [[jp/api-reference/computers/index|Computers API]]

## Parameters {#parameters}

| Name | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `computerId` | `path` | `string` | Yes | - |

## Responses {#responses}

| Status | Description |
| --- | --- |
| `204` | Response for status 204 |
| `401` | Response for status 401 |
| `403` | Response for status 403 |
| `404` | Response for status 404 |
| `500` | Response for status 500 |
| `503` | Response for status 503 |

## Example Request {#example-request}

```bash
curl -X DELETE "https://api.factory.ai/api/v0/computers/{computerId}" \
  -H "Authorization: Bearer $FACTORY_API_KEY" \
  -H "Content-Type: application/json"
```
