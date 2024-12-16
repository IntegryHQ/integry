---
hidden: true
icon: list-radio
---

# Embed Functions (Coming soon)

In this guide, we will use the [Integry.JS SDK](../apis-and-sdks/js-sdk-reference/) to enable users to execute [Functions](broken-reference) in other apps (and connect those apps) from your SaaS application.

Before you proceed, please [sign up](https://app.integry.io/accounts/register/v3/signup/?product=functions) for a free trial (if you haven't).

## Set up the SDK

Follow the steps [here](../apis-and-sdks/js-sdk-reference/#setting-up).

## Show functions

Your users need a way to discover functions.

### Show Functions in the Integry marketplace

Call the [`showFunctions()`](../apis-and-sdks/js-sdk-reference/#show-functions-coming-soon) method to show a list of functions. You can [configure the render mode, layout and styling](render-modes-layouts-and-styling.md).

Your users will simply click an app to connect. If the app has [Flows](broken-reference), they will then be able to setup/run those flows.
