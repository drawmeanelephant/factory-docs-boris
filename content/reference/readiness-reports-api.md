---
id: reference/readiness-reports-api
title: "Readiness Reports API"
status: published
summary: "REST API reference for programmatic access to agent readiness reports."
parent: reference/index
tags: [reference]
relations: [relates_to=jp/reference/readiness-reports-api]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Readiness Reports API</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">REST API reference for programmatic access to agent readiness reports.</p>


The Readiness Reports API provides programmatic access to your organization's agent readiness evaluation data.

---

## Authentication {#authentication}

All requests require a Factory API key in the `Authorization` header:

```bash
Authorization: Bearer fk-your-api-key
```

Generate API keys at [app.factory.ai/settings/api-keys](https://app.factory.ai/settings/api-keys).

---

## Base URL {#base-url}

```
https://app.factory.ai
```

---

## Endpoints {#endpoints}

### List Readiness Reports {#list-readiness-reports}

Retrieves readiness reports for your organization.

```
GET /api/organization/agent-readiness-reports
```

#### Query Parameters {#query-parameters}

| Parameter    | Type    | Required | Description                                            |
| :----------- | :------ | :------- | :----------------------------------------------------- |
| `repoId`     | string  | No       | Filter reports by repository ID                        |
| `limit`      | integer | No       | Maximum number of reports to return (must be positive) |
| `startAfter` | string  | No       | Report ID for pagination cursor                        |

#### Response {#response}

```json
{
  "reports": [
    {
      "reportId": "550e8400-e29b-41d4-a716-446655440000",
      "createdAt": 1701792000000,
      "repoUrl": "https://github.com/org/repo",
      "apps": {
        "apps/web": {
          "description": "Main Next.js application"
        },
        "apps/api": {
          "description": "Backend API service"
        }
      },
      "report": {
        "lint_config": {
          "numerator": 2,
          "denominator": 2,
          "rationale": "ESLint configured in both applications"
        },
        "type_check": {
          "numerator": 2,
          "denominator": 2,
          "rationale": "TypeScript strict mode enabled"
        }
      },
      "commitHash": "abc123def456",
      "branch": "main",
      "hasLocalChanges": false,
      "hasNonRemoteCommits": false,
      "modelUsed": {
        "id": "claude-sonnet-4-5",
        "reasoningEffort": "high"
      },
      "droidVersion": "0.30.0"
    }
  ]
}
```

#### Example Request {#example-request}

```bash
curl -X GET "https://app.factory.ai/api/organization/agent-readiness-reports?limit=10" \
  -H "Authorization: Bearer fk-your-api-key"
```

---

## Readiness Report Schema {#readiness-report-schema}

### Report Object {#report-object}

| Field                 | Type     | Description                                                |
| :-------------------- | :------- | :--------------------------------------------------------- |
| `reportId`            | string   | Unique identifier for the report (UUID)                    |
| `createdAt`           | number   | Unix timestamp in milliseconds when the report was created |
| `repoUrl`             | string   | Repository URL that was evaluated                          |
| `apps`                | object   | Map of application paths to description objects            |
| `report`              | object   | Map of criterion IDs to evaluation results                 |
| `commitHash`          | string?  | Git commit hash at time of evaluation                      |
| `branch`              | string?  | Git branch name at time of evaluation                      |
| `hasLocalChanges`     | boolean? | Whether uncommitted changes existed                        |
| `hasNonRemoteCommits` | boolean? | Whether unpushed commits existed                           |
| `modelUsed`           | object?  | Model configuration used for evaluation                    |
| `droidVersion`        | string?  | CLI version that generated the report                      |

### App Description Object {#app-description-object}

| Field         | Type   | Description                                    |
| :------------ | :----- | :--------------------------------------------- |
| `description` | string | Brief description of what the application does |

### Criterion Evaluation Object {#criterion-evaluation-object}

| Field         | Type   | Description                                                                 |
| :------------ | :----- | :-------------------------------------------------------------------------- |
| `numerator`   | number | Number of sub-applications passing the criterion (0 to denominator)         |
| `denominator` | number | Number of sub-applications on which the criterion was evaluated (minimum 1) |
| `rationale`   | string | Explanation of the evaluation result                                        |

### Model Used Object {#model-used-object}

| Field             | Type   | Description                                             |
| :---------------- | :----- | :------------------------------------------------------ |
| `id`              | string | Model identifier                                        |
| `reasoningEffort` | string | Reasoning effort level (`low`, `medium`, `high`, `off`) |

---

## Pagination {#pagination}

For large result sets, use cursor-based pagination:

1. Make initial request with desired `limit`
2. Get the `reportId` of the last item in the response
3. Pass that ID as `startAfter` in the next request

```bash
# First page
curl "https://app.factory.ai/api/organization/agent-readiness-reports?limit=10"

# Next page (using last reportId from previous response)
curl "https://app.factory.ai/api/organization/agent-readiness-reports?limit=10&startAfter=550e8400-e29b-41d4-a716-446655440000"
```

---

## Use Cases {#use-cases}

### CI/CD Integration {#cicd-integration}

Track readiness scores over time by fetching reports after each evaluation:

```bash
# Get latest report for a specific repository
curl "https://app.factory.ai/api/organization/agent-readiness-reports?repoId=123&limit=1" \
  -H "Authorization: Bearer $FACTORY_API_KEY"
```

### Custom Dashboards {#custom-dashboards}

Build internal dashboards by fetching all reports and calculating aggregate metrics:

```javascript
const response = await fetch(
  "https://app.factory.ai/api/organization/agent-readiness-reports",
  { headers: { Authorization: `Bearer ${apiKey}` } }
);
const { reports } = await response.json();

// Calculate average level
const avgLevel =
  reports.reduce((sum, r) => sum + calculateLevel(r), 0) / reports.length;
```

### Automated Alerting {#automated-alerting}

Set up alerts when readiness scores drop below thresholds:

```bash
# Fetch recent reports and check for regressions
reports=$(curl -s "https://app.factory.ai/api/organization/agent-readiness-reports?limit=50" \
  -H "Authorization: Bearer $FACTORY_API_KEY")

# Process and alert on regressions...
```

---

## Error Responses {#error-responses}

| Status | Description                |
| :----- | :------------------------- |
| `400`  | Invalid request parameters |
| `401`  | Missing or invalid API key |
| `500`  | Internal server error      |
