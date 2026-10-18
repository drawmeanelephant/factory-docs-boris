---
id: integrations/slack
title: "Slack"
status: published
summary: "Step-by-step guide to connect Factory with your Slack workspace"
parent: integrations/index
tags: [integrations]
relations: [relates_to=jp/integrations/slack]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Slack</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Step-by-step guide to connect Factory with your Slack workspace</p>


Connect Factory to Slack so Droid can work with Slack conversations and team context.



<Aside kind="warning">
If the Factory Slack app is already installed in your workspace, rerun the Slack install flow below to enable Droid to ingest images from Slack threads and post videos, generated artifacts, and other files back to Slack. An admin may have to approve this depending on your Slack workspace settings.
</Aside>



## Prerequisites {#prerequisites}

- A Factory account with admin privileges
- Admin access to your Slack workspace
- Ability to install apps in your Slack workspace

## Integration Steps {#integration-steps}



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Access Slack integration settings</div>

[Log in to your Factory account](https://app.factory.ai), open [**Settings** → **Organization**](https://app.factory.ai/settings/organization), then find **Slack** under **Org Integrations**.



<div class="factory-frame">

<img src="../images/slack-organization-settings.png" alt="Factory Organization settings page showing Slack under Org Integrations" />

<div class="factory-frame-caption">Slack in Organization settings</div>

</div>



</div>


  

<div class="factory-step">

<div class="factory-step-title">Initiate Slack Integration</div>

Click **Connect**, or **Manage** if Slack is already installed, to start the integration process. If you are updating an existing Slack install for the latest permissions, click **Reconnect** from the integration details to rerun the install flow.



<div class="factory-frame">

<img src="../images/slack-reconnect-button.png" alt="Factory Slack integration details showing the Reconnect button" />

<div class="factory-frame-caption">Reconnect Slack to refresh permissions</div>

</div>



</div>


  

<div class="factory-step">

<div class="factory-step-title">Authorize Factory&#x27;s Slack Application</div>

You'll be redirected to Slack. Review the requested permissions and click "Allow" to authorize Factory access to your Slack workspace.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Select Workspace</div>

If you belong to multiple workspaces, select the workspace you want to connect to Factory.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Confirm Integration</div>

After authorization, you'll be redirected back to Factory. Verify that the integration status shows as "Connected".

</div>


  

<div class="factory-step">

<div class="factory-step-title">Add to Channels</div>

In your Slack workspace, add the Factory app to relevant channels by typing `/invite @Factory` in each channel.

</div>

</div>



## Verification {#verification}

To ensure the integration is working correctly:

1. Mention `@Factory` in a thread within a channel where the app has been added.
2. Verify that Factory responds with a link to open the conversation in Factory.
3. Click the link and confirm that the Slack thread content appears in your new Factory session.
4. If you reran the install flow for the latest permissions, test with a thread that includes an image attachment and confirm Droid can use it as context.
5. If your workflow posts results back to Slack, confirm Droid can upload a generated file or short result video to the thread.


## Capabilities {#capabilities}

With the Slack integration, you can:



<div class="factory-frame">

<video controls preload="metadata">
<source src="../images/marketing/slack-clone-scene.mp4" type="video/mp4" />
  </video>

<div class="factory-frame-caption">Factory Slack integration demo</div>

</div>



- Mention `@Factory` in any Slack thread to start a Droid session from that thread
- Continue the session on Web or Desktop
- Import full Slack thread context into Factory by clicking the provided link
- Include supported image attachments from Slack as session context
- Have Droid post messages, generated files, artifacts, and result videos back to Slack
- Send follow-up messages and attachments from Slack into an active Droid session
- **Use any model you want, no lock-in.** Factory is model-agnostic: choose Claude, GPT, Gemini, open-source/Droid Core, or any of 30+ supported models
- Pick the model when you start a session, set a default **model** per channel for Auto-Run and service-account workflows, or let [[web/factory-router|Factory Router]] pick the best model automatically
- Reference Slack threads in Factory by pasting a thread URL into a Factory chat



<div class="factory-frame">

<img src="../images/slack-model-selection.png" alt="Factory Session Settings dialog showing the model picker with Factory models" />

<div class="factory-frame-caption">Pick a specific model, or let Factory Router choose automatically, for a Slack-started session</div>

</div>



When creating a PR, the Slack integration will also use a subagent to handle CI so the agent can respond faster.

When a Slack thread is imported, Factory has access to the entire conversation history, allowing it to provide context-aware assistance.

## Slack settings {#slack-settings}

After Slack is connected, click **Manage** from [**Settings** → **Organization**](https://app.factory.ai/settings/organization) to configure Slack channel settings. These settings are only needed for Incident Response and service-account workflows; standard `@Factory` mentions work without configuring channels here.

In channel settings, you can enable a channel, expand it, and configure **Run as**, **Incident Response**, **Machine Type**, **Computer** or **Workspace**, **Session Visibility**, **Model**, and **Custom Prompt**. Only channels where the Factory app has been invited appear in this list.

## Service accounts {#service-accounts}

Use [[enterprise/service-accounts|service accounts]] when Slack sessions should run from a shared identity and a preconfigured Droid Computer instead of the Slack user who mentions Factory. This is useful for incident, operations, or release channels that need consistent credentials and tool access.

Before using a service account with Slack, make sure:

- Service accounts are enabled for your organization.
- The service account is active.
- The service account owns at least one Droid Computer.
- The Factory app has been invited to the Slack channel.



<div class="factory-steps">

<div class="factory-step">

<div class="factory-step-title">Open Slack channel settings</div>

In Factory, go to **Settings** → **Integrations** → **Slack** → **Channels**. Enable the channel and expand its settings.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Choose the run identity</div>

If the **Run as** row appears, select the service account. Selecting a service account makes the channel run with that service account's identity and computers.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Choose the computer</div>

Service account Slack sessions run on Droid Computers. When a service account is selected, Factory locks the target to **Computer** and only shows computers owned by that service account.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Configure Auto-Run if needed</div>

For automated channel workflows, turn on **Auto-Run** and configure the prompt, model, and visibility settings for that channel.

</div>


  

<div class="factory-step">

<div class="factory-step-title">Test from Slack</div>

Mention `@Factory` in the channel, or send a test alert if Auto-Run is enabled. Factory starts the session as the selected service account.

</div>

</div>



For ad hoc Slack sessions, the computer picker can also show a **Run as** selector. Choose a service account, pick one of its computers, and optionally save it as your default for future Slack mentions.

## Best Practices {#best-practices}

- Add the Factory app only to channels where development discussions occur.
- Use threads rather than channel messages when mentioning Factory.
- Provide sufficient context in the Slack thread before mentioning Factory.
- Regularly review the permissions granted to the Factory app in your Slack settings.

## Troubleshooting {#troubleshooting}

If you encounter issues during integration:

- Ensure you have admin rights in both Factory and your Slack workspace.
- Verify that the Factory app has been added to the channel where you're mentioning it.
- If Droid cannot read image attachments or upload files/videos, rerun the Slack install flow above to refresh the Factory Slack app's permissions.
- If you see a "not_in_channel" error toast when trying to paste a Slack thread URL, it means the Factory bot needs to be invited to that channel. Use `/invite @Factory` in the channel to resolve this issue.
- Check that your organization's firewall isn't blocking webhook communications.
- For persistent issues, contact Factory support with specific error messages.



<div class="factory-card">

**[Security and Compliance](https://trust.factory.ai)**

Visit Factory's Trust Center for compliance documents, certifications, and security resources

</div>
