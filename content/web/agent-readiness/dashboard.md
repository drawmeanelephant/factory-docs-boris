---
id: web/agent-readiness/dashboard
title: "Readiness Dashboard"
status: published
summary: "Track and analyze your organization's Agent Readiness scores in the Factory App."
parent: web/agent-readiness/index
tags: [web]
relations: [relates_to=jp/web/agent-readiness/dashboard]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Readiness Dashboard</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Track and analyze your organization&#x27;s Agent Readiness scores in the Factory App.</p>


The Agent Readiness dashboard provides a centralized view of your organization's readiness scores across all repositories, with historical trends and detailed breakdowns.

<img src="../../images/web/readiness-dashboard.png" alt="Agent Readiness Dashboard" />

---

## Accessing the Dashboard {#accessing-the-dashboard}

Navigate to **Settings → Analytics → Agent Readiness** in the Factory App.

---

## Main Dashboard View {#main-dashboard-view}

The dashboard shows an organization-level overview with three main sections:

### Summary Cards {#summary-cards}

At the top, you'll see key metrics:

| Metric                   | Description                                                                 |
| :----------------------- | :-------------------------------------------------------------------------- |
| **Organization Score**   | Average readiness level across all measured repositories (rounded down)      |
| **Repositories Tracked** | Number of repositories with readiness reports vs. total enabled repositories |
| **Last Updated**         | Time since the most recent readiness evaluation                              |

### Progress Graph {#progress-graph}

A time-series chart showing your organization's readiness level over time. Use the period filters to view different time ranges:

- **7d** — Last 7 days
- **1m** — Last month
- **6m** — Last 6 months
- **1y** — Last year
- **all** — All time

### Repositories Table {#repositories-table}

A searchable, paginated table of all repositories showing:

- **Repository name** — Click to view details
- **Level** — Current readiness level (1-5)
- **Progress** — Percentage complete toward next level
- **Last Update** — When the repository was last evaluated

Use the search bar to filter repositories by name or URL.

---

## Repository Detail Page {#repository-detail-page}

Click any repository row to view its detailed readiness breakdown.

<img src="../../images/web/readiness-criteria.png" alt="Repository Detail Page" />

### Header {#header}

Shows the repository name, current level achieved, last evaluation time, and a **Refresh** button to trigger a new evaluation.

### Level Accordions {#level-accordions}

Each readiness level (Functional through Autonomous) has an expandable accordion section showing:

- **Percentage complete** — How much of that level's criteria are passing
- **Lock status** — Levels are locked until the previous level reaches 80%

### Criterion Rows {#criterion-rows}

Within each level, individual criteria display:

| Element       | Description                                        |
| :------------ | :------------------------------------------------- |
| **Name**      | The criterion being evaluated                      |
| **Score**     | Format `[X/Y]` — numerator/denominator             |
| **Status**    | Pass (green) or fail (red) indicator               |
| **Rationale** | Click to expand and see the evaluation explanation |

### Remediation (Coming Soon) {#remediation-coming-soon}

Soon, failing criteria will display a **Fix** button that triggers automated remediation. Select the criteria you want to fix, and the system will implement the necessary changes to your repository.

---

## Triggering a Refresh {#triggering-a-refresh}

There are two ways to refresh a readiness evaluation:

### From the Factory App dashboard {#from-the-factory-app-dashboard}

1. Navigate to the repository detail page
2. Click the **Refresh** button in the header
3. A new session starts to evaluate the repository
4. Once done, the dashboard will update with results from the latest report

### From the Droid CLI {#from-the-droid-cli}

Run the `/readiness-report` [[cli/features/readiness-report|slash command]] in the Droid CLI while in the repository directory:

```bash
droid
> /readiness-report
```



<Aside kind="note">
Re-evaluations run the full readiness assessment against the current state of
  your repository. This is useful after making infrastructure improvements or
  merging changes that can affect a readiness criterion.
</Aside>



---

## Understanding the Metrics {#understanding-the-metrics}

### Organization Level Calculation {#organization-level-calculation}

The organization-level score is calculated as the **average of all repository levels, rounded down**. For example:

- Repo A: Level 3
- Repo B: Level 2
- Repo C: Level 3

Organization Level = floor((3 + 2 + 3) / 3) = floor(2.67) = **Level 2**

### Repository Level Calculation {#repository-level-calculation}

A repository's level is determined by the **80% threshold system**:

1. Start at Level 1
2. If 80% of Level 1 criteria pass → achieve Level 2
3. If 80% of Level 2 criteria pass → achieve Level 3
4. Continue through Level 5

The percentage shown for each level indicates progress toward completing that level's criteria.

---

## Best Practices {#best-practices}

- **Regular evaluations:** Run readiness reports after significant infrastructure changes
- **Focus on current level:** Address failing criteria in your current level before jumping ahead to focus on foundational improvements first
- **Track trends:** Use the progress graph to monitor improvement over time
- **Prioritize high-impact fixes:** The action items in CLI reports highlight the most impactful improvements
