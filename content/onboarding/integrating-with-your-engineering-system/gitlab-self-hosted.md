---
id: onboarding/integrating-with-your-engineering-system/gitlab-self-hosted
title: "GitLab Self-Hosted"
status: published
summary: "Comprehensive guide for connecting Factory with your self-hosted GitLab instance"
parent: onboarding/integrating-with-your-engineering-system/index
tags: [onboarding]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">GitLab Self-Hosted</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Comprehensive guide for connecting Factory with your self-hosted GitLab instance</p>


This guide provides detailed instructions for integrating Factory with your self-hosted GitLab instance, allowing the Factory platform to securely access and work with your on-premise repositories.

> Connecting to a self-hosted GitLab instance is only supported in the Enterprise plan.

## Prerequisites {#prerequisites}

- Admin access to your self-hosted GitLab instance
- A Factory account with an Enterprise plan and admin privileges

## Integration Process {#integration-process}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Create GitLab Application</div>

1. In your GitLab instance, go to Admin Area \> Applications.
  2. Click "Add new application" and fill in the details:
  - Name: `Factory Integration`
  - Redirect URI: `https://api.factory.ai/api/integrations/redirect/gitlab-sh/callback`
  - Trusted: yes
  - Confidential: yes
  - Scopes:
  - `api`
  - `read_api`
  - `read_user`
  - `read_repository`
  - `write_repository`
  - `read_observability`
  - `write_observability`
  3. Save the application and note the Application ID and Secret.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Create Factory Droid User Account</div>

1. In your GitLab instance, go to Admin Area \> Users.
  2. Click "New User" and fill in the details:
  - Name: `Factory Droid`
  - Username: `factory-droid`
  - Email: [any]
  3. Once the user is created, log in as or Impersonate the user before moving on to the next step.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Configure GitLab Self-Hosted in Factory</div>

1. Navigate to https://app.factory.ai/settings/integrations, click on "Connect" next to GitLab, and toggle "Self-Hosted" in the bottom left.
  2. In the Self-Hosted Setup panel, enter your GitLab Self-Hosted Application details:
  - **Domain:** the url of your GitLab instance, such as https://gitlab.example.com. If you have separate internal and external domains, enter your external domain.
  - **Application ID:** from the application created in the previous part.
  - **Secret:** from the application created in the previous part.
  3. Save the configuration.
  4. Click "Manage GitLab Self-Hosted Permissions" in the top right. This will open a pop-up window that will authorize the integration. IMPORTANT: you must be logged in as or impersonating the `factory-droid` user before performing this step.
  5. Your repositories should now appear in the Repository Selection panel. Navigate there and enable repositories for Factory.

</div>

</div>



## Support {#support}

For any specific issues or detailed support needs, contact the Factory team through your designated support channel.



<div class="factory-card">

**[Security and Compliance](https://trust.factory.ai)**

Visit Factory's Trust Center for compliance documents, certifications, and security resources

</div>
