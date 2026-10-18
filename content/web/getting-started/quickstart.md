---
id: web/getting-started/quickstart
title: "Quickstart"
status: published
summary: "Get up and running with the Factory App in 5 minutes"
parent: web/getting-started/index
tags: [web, quickstart, getting-started, factory-app, droid-cli, factory-bridge, bridge, cloud-templates]
relations: [relates_to=jp/web/getting-started/quickstart]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Quickstart</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Get up and running with the Factory App in 5 minutes</p>


## Step 1: Download and Install {#step-1-download-and-install}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Download the Factory App</div>

<div class="factory-card-group">

<div class="factory-card">

**[Mac (Apple Silicon)](https://app.factory.ai/api/desktop?platform=darwin&architecture=arm64)**

M1/M2/M3

</div>




<div class="factory-card">

**[Mac (Intel)](https://app.factory.ai/api/desktop?platform=darwin&architecture=x64)**

Intel

</div>




<div class="factory-card">

**[Windows (x64)](https://app.factory.ai/api/desktop?platform=win32)**

Windows x64

</div>




<div class="factory-card">

**[Windows (ARM64)](https://app.factory.ai/api/desktop?platform=win32&architecture=arm64)**

Windows ARM64

</div>

</div>

</div>



  

<div class="factory-step">

<div class="factory-step-title">Install</div>

- **Mac**: Open the `.dmg` file and drag Factory to Applications
  - **Windows**: Run the installer

</div>



  

<div class="factory-step">

<div class="factory-step-title">Sign In</div>

Launch the Factory App and sign in with your account.

</div>

</div>



## Step 2: Connect to Your Codebase {#step-2-connect-to-your-codebase}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Set Your Working Directory</div>

Set your working directory to your project folder. The Factory App connects directly to your local machine.

</div>



  

<div class="factory-step">

<div class="factory-step-title">Select Your Model</div>

Choose your preferred AI model from the model selector. You can change this anytime.

</div>

</div>



## Step 3: Start Building {#step-3-start-building}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Ask Droid Anything</div>

Start with something simple:

```
Analyze this codebase and explain the architecture
```

Or jump straight into coding:

```
Add error handling to the user authentication flow
```

Droid will analyze your codebase, propose changes, and show you exactly what will be modified before applying anything.

</div>

</div>



## Example Workflows {#example-workflows}

### Feature Development {#feature-development}
```
Implement a dark mode toggle following our existing theme patterns
```

### Bug Fixing {#bug-fixing}
```
Fix the authentication timeout issue where users get logged out after 5 minutes
```

### Code Review {#code-review}
```
Review this PR and suggest improvements for error handling and edge cases
```

### Security Audit {#security-audit}
```
Audit this codebase for security vulnerabilities and create a remediation plan
```

## Tips {#tips}

- **Be specific**: Include relevant details like file names, error messages, or ticket numbers
- **Use context**: Reference team tools with '@' mentions or paste links directly
- **Review changes**: Always review Droid's proposed changes before approval

## Next Steps {#next-steps}



<div class="factory-card-group">

<div class="factory-card">

**[[integrations/linear|Integrations]]**

Connect Slack, Linear, and other tools

</div>


  

<div class="factory-card">

**[[cli/getting-started/overview|Droid CLI]]**

Use Droid from your terminal

</div>

</div>
