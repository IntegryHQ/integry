---
icon: grid-2-plus
---

# Add Integry Apps to an Existing  Marketplace

In this guide, we will use the [Integry.JS SDK](../apis-and-sdks/js-sdk-reference/) to add an app to an existing integrations marketplace in your app so your users can connect to that app and setup/run integrations with that app.

Before you proceed, please [sign up](https://app.integry.io/accounts/register/v3/signup/?product=functions) for a free trial (if you haven't).

## Set up the SDK

Follow the steps [here](../apis-and-sdks/js-sdk-reference/#setting-up).

## Add an app card in your marketplace

Add a card/button for each app powered by Integry. Your users will click that card/button to access the onwards experience powered by Integry.

## Show the Integry app page

Call the [`showApp()`](../apis-and-sdks/js-sdk-reference/#show-flows-coming-soon) method when a user clicks the card/button.

<pre class="language-javascript"><code class="lang-javascript"><strong>integry.showApp(
</strong><strong>  "hubspot"
</strong><strong>  IntegryJS.RenderModes.INLINE,
</strong>  "marketplace-container"
<strong>).then(() => {
</strong>  console.log("Showing Hubspot Flows!");
}).catch((error) => {
  console.error("Failed to launch Slack:", error);
});
</code></pre>

Your users will be asked to connect the app (if they haven't already) or select a connected account (if they have connected multiple accounts). They will then be able to setup/run integrations of Flows with that app.

## Listen to events

### App connected / disconnected

Subscribe to the `app-connected` and `app-disconnected` events that are respectively fired when the user connects or disconnects an app to be able to show the connection status on the card (like it's shown in the [Integry Apps Marketplace](embed-integry-apps-marketplace.md)).

```javascript
integry.eventEmitter.on('app-connected', (data) => {
    console.log("User connected:" + data.name);
});
```

### Integration created

If you are going to send data from your app to another app, you will need to capture (and store) the **unique callback URL** for the user's integration so you can trigger it from your app.

Subscribe to the `integration-created` event and get the `callbackURL`. This event will fire after your user creates an integration. It will not fire if they edit an existing integration.

```javascript
integry.eventEmitter.on('integration-created', (data) => {
    console.log("Callback URL: " + data.callbackUrl);
});
```
