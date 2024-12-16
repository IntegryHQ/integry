---
hidden: true
icon: table-list
---

# Embed Flows (Coming soon)

In this guide, we will use the [Integry.JS SDK](../apis-and-sdks/js-sdk-reference/) to enable users to setup/run integrations of [Flows](broken-reference) with other apps (and connect those apps) from your SaaS application.

Before you proceed, please [sign up](https://app.integry.io/accounts/register/v3/signup/?product=functions) for a free trial (if you haven't).

## Set up the SDK

Follow the steps [here](../apis-and-sdks/js-sdk-reference/#setting-up).

## Show flows

Your users need a way to discover flows.

### Show Flows in the Integry marketplace

Call the [`showFlows()`](../apis-and-sdks/js-sdk-reference/#show-flows-coming-soon) method to show a list of flows. You can [configure the render mode, layout and styling](render-modes-layouts-and-styling.md).

<figure><img src="../.gitbook/assets/Screenshot 2024-11-12 at 8.13.04 PM.png" alt="" width="375"><figcaption></figcaption></figure>

Your users will simply click an app to connect. If the app has [Flows](broken-reference), they will then be able to setup/run those flows.

### Show apps in your own marketplace

If you're using Integry to add more apps to an existing integrations marketplace in your app, see [embed an app](add-integry-apps-to-an-existing-marketplace.md).

## Listen to events (optional)

### Integration created

If you are going to send data from your app to another app, you will need to capture (and store) the **unique callback URL** for the user's integration so you can trigger it from your app.

Subscribe to the `integration-created` event and get the `callbackURL`. This event will fire after your user creates an integration. It will not fire if they edit an existing integration.

```javascript
integry.eventEmitter.on('integration-created', (data) => {
    console.log("Callback URL: " + data.callbackUrl);
});
```
