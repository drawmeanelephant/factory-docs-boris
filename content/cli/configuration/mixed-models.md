---
id: cli/configuration/mixed-models
title: "Mixed Models"
status: published
summary: "Use a different AI model for Specification Mode planning than your default model for maximum flexibility and optimization."
parent: cli/configuration/index
tags: [cli, mixed-models, spec-mode-model, model-configuration, multiple-models, planning-model, default-model]
relations: [relates_to=jp/cli/configuration/mixed-models]
---
<div class="factory-page-title-row"><h1 class="factory-page-title">Mixed Models</h1><button class="factory-copy-page-btn" type="button">Copy page ▾</button></div>

<p class="factory-page-subtitle">Use a different AI model for Specification Mode planning than your default model for maximum flexibility and optimization.</p>


## What are mixed models? {#what-are-mixed-models}

Mixed models allow you to use a different AI model specifically for Specification Mode planning while keeping a separate default model for regular coding sessions. This gives you the flexibility to optimize both planning and implementation phases independently.

For example, you might want to use a more powerful model for comprehensive specification planning, while using a faster model for day-to-day implementation work.

---

## Why use mixed models? {#why-use-mixed-models}

Different models excel at different tasks. Separating your spec mode model from your default model lets you:



<div class="factory-card-group">

<div class="factory-card">

**Optimize for Planning**

Use a more thorough, analytical model for specification planning that considers edge cases and architectural decisions.

</div>


  

<div class="factory-card">

**Balance Speed & Cost**

Keep a faster, more economical model for regular coding while reserving powerful models for critical planning phases.

</div>


  

<div class="factory-card">

**Match Task Complexity**

Complex features benefit from advanced reasoning during planning, while simpler tasks can use standard models.

</div>


  

<div class="factory-card">

**Flexible Workflows**

Switch between different model combinations to find what works best for your specific use cases.

</div>

</div>



---

## How to configure mixed models {#how-to-configure-mixed-models}

### Accessing the Configuration {#accessing-the-configuration}

1. Run `droid` to start the CLI
2. Enter `/model` to open the model selector
3. Navigate to **"Configure Spec Mode Model"** (first option in the list)
4. Press **Enter** to begin configuration

### Configuration Options {#configuration-options}

When you open the configurator, you'll see three options:

- **Yes, configure spec mode model** - Select a different model for Specification Mode
- **No, keep using [current configuration/main model]** - Exit without making changes
- **Clear spec mode model (use main model)** - Remove the spec mode model and use your default model for everything *(only shown if you already have a spec mode model configured)*

### Selecting a Model {#selecting-a-model}

1. Choose **"Yes, configure spec mode model"**
2. Browse the list of available models
3. Select your preferred model for Specification Mode
4. If the model supports reasoning, choose your reasoning effort level
5. The configuration is saved automatically



<Aside kind="note">
Only compatible models will be available in the selector based on your current default model. See [[cli/configuration/mixed-models#model-compatibility|Model Compatibility]] below.
</Aside>



---

## Model Compatibility {#model-compatibility}

Not all model combinations work together due to how different AI providers handle reasoning traces and context. Here are the compatibility rules:

### Compatibility Rules {#compatibility-rules}





<Details summary="OpenAI Models">
**OpenAI models can only pair with other OpenAI models**

  - Main model: GPT-5 → Spec model: GPT-5-Codex ✅
  - Main model: GPT-5 → Spec model: Sonnet 4.5 ❌

OpenAI's internal reasoning format is encrypted and is incompatible with other model providers.
</Details>


  
  

<Details summary="Anthropic Models with Reasoning">
**Anthropic models with reasoning enabled can only pair with other Anthropic models**

  - Main model: Sonnet 4.5 (reasoning on) → Spec model: Sonnet 4.5 ✅
  - Main model: Sonnet 4.5 (reasoning on) → Spec model: GPT-5 ❌

When extended thinking is active, reasoning traces must stay within the same provider.
</Details>


  
  

<Details summary="Anthropic Models without Reasoning">
**Anthropic models with reasoning off can pair with non-OpenAI models**

  - Main model: Sonnet 4.5 (reasoning off) → Spec model: Any non-OpenAI model ✅
  - Main model: Sonnet 4.5 (reasoning off) → Spec model: DeepSeek ✅

Without reasoning enabled, cross-provider compatibility is possible.
</Details>







<Aside kind="info">
**Why these restrictions?** Model providers encrypt their reasoning traces differently. When reasoning is active, the spec model must be able to read and continue the reasoning chain from the main model, which requires matching providers.
</Aside>



---

## Reasoning Effort Configuration {#reasoning-effort-configuration}

If you select an Anthropic model that supports reasoning (like Sonnet 4.5), you'll be prompted to choose a reasoning effort level:

- **Off** - No extended thinking, faster responses
- **Low** - Brief consideration, balanced speed and depth
- **Medium** - Moderate thinking time for complex decisions
- **High** - Deep analysis for critical architectural choices

The reasoning effort for your spec mode model is independent of your default model's reasoning setting, giving you complete control over each phase.



<Aside kind="tip">
For specification planning, **Medium** or **High** reasoning effort often produces better results since thorough analysis during planning prevents issues during implementation.
</Aside>



---

## Common Configurations {#common-configurations}

Here are some effective model combinations for different scenarios:

### Anthropic Models {#anthropic-models}

**Best for:** Most development workflows, flexible reasoning control

- **Default model:** Haiku 4.5 or Sonnet 4.5 (select reasoning of your choice if supported)
- **Spec mode model:** Opus 4.8 (reasoning: high) or Sonnet 4.5 (reasoning: high)
- **Benefits:** Fast implementation with deep planning analysis. Opus 4.8 offers **Max** reasoning for the most thorough planning.

### OpenAI Models {#openai-models}

**Best for:** Teams using OpenAI models exclusively, cost-conscious projects

- **Default model:** GPT-5-Codex
- **Spec mode model:** GPT-5 (high reasoning)
- **Benefits:** Consistent reasoning format, specialized coding model for specs

---

## How It Works {#how-it-works}

Once configured, Droid automatically uses your spec mode model whenever you enter Specification Mode:

1. **Activate Specification Mode** with **Shift+Tab**
2. **Provide your feature description**
3. **Droid uses your spec mode model** to analyze, plan, and generate the specification
4. **Review and approve** the generated spec
5. **Implementation uses your default model** to write the actual code



<Aside kind="note">
Your default model is always used for regular coding sessions and implementation work. The spec mode model is only active during the planning phase of Specification Mode.
</Aside>



---

## Checking Your Configuration {#checking-your-configuration}

To see which models you're currently using:

1. Enter `/model` in the CLI
2. Your current default model is highlighted
3. If you have a spec mode model configured, it's displayed at the top of the selector

---

## Clearing your mixed models configuration {#clearing-your-mixed-models-configuration}

If you want to go back to using a single model for everything:

1. Enter `/model` in the CLI
2. Navigate to **"Configure Spec Mode Model"**
3. Press **Enter**
4. Select **"Clear spec mode model (use main model)"**
5. Confirm by pressing **Enter**

Your default model will now be used for both regular coding and Specification Mode.

---

## Best Practices {#best-practices}





<Details summary="Start with the same model">
If you're new to Specification Mode, start by using your default model for both modes. Once you're comfortable, experiment with different spec mode models to see if it improves your planning quality.
</Details>


  
  

<Details summary="Consider your project complexity">
Simple projects may not need separate models. For complex systems with intricate dependencies, using a more powerful spec mode model can prevent costly mistakes during implementation.
</Details>


  
  

<Details summary="Match reasoning to task importance">
Use higher reasoning effort for architectural decisions and lower effort for routine feature additions. Adjust both your default and spec mode reasoning independently.
</Details>


  
  

<Details summary="Respect compatibility rules">
Don't try to force incompatible model combinations. The restrictions exist for good technical reasons and violations will be prevented by the CLI.
</Details>


  
  

<Details summary="Monitor your usage">
More powerful models and higher reasoning efforts increase cost. Balance quality needs with budget constraints by using premium configurations selectively.
</Details>





---

## Troubleshooting {#troubleshooting}





<Details summary="Can't select the model I want">
**Cause:** The model is incompatible with your current default model.

**Solution:** Check the [[cli/configuration/mixed-models#model-compatibility|Model Compatibility]] rules above. You may need to change your default model first, or adjust reasoning settings to enable compatibility.
</Details>


  
  

<Details summary="Spec mode model was automatically cleared">
**Cause:** You changed your default model to one that's incompatible with your configured spec mode model.

**Solution:** This is expected behavior. Configure a new spec mode model that's compatible with your new default model, or continue using the default model for both modes.
</Details>


  
  

<Details summary="Reasoning effort selector doesn't appear">
**Cause:** The selected model doesn't support reasoning, or you're using a non-Anthropic model combination.

**Solution:** This is normal. Not all models support reasoning configuration. The model will use its default behavior.
</Details>





---

## Related Resources {#related-resources}



<div class="factory-card-group">

<div class="factory-card">

**[[cli/user-guides/specification-mode|Specification Mode]]**

Learn how to use Specification Mode for planning and implementing features.

</div>


  

<div class="factory-card">

**[[cli/configuration/settings|Settings]]**

Configure other aspects of how Droid behaves and integrates with your workflow.

</div>


  

<div class="factory-card">

**[[models|Available Models]]**

Understand the differences between available models and how to choose the right one.

</div>


  

<div class="factory-card">

**[[cli/byok/overview|BYOK]]**

Bring your own API keys to use custom models with Factory.

</div>

</div>



---
