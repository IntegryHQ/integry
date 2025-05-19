---
icon: left-to-bracket
---

# Sync data TO another app from your app

In this tutorial, we will:

* [Create a flow **from your app** **to another app**](sync-data-to-another-app-from-your-app.md#h_01hev188pb696nwg83zdnc0e1n)
* [Set up an integration of that flow (like your users would)](sync-data-to-another-app-from-your-app.md#h_01hev2zavgk1s46ekb4mgvr37g)
* [Run the integration by calling a URL from an HTTP client](sync-data-to-another-app-from-your-app.md#h_01hev4chz4zw5bwp9z0jhthvb1)

If you'd like, you can also [create a flow that syncs data FROM another app](sync-data-from-another-app-to-your-app.md) to get started.

It will only take 5 minutes. Let's begin.

### Build a Flow <a href="#h_01hev188pb696nwg83zdnc0e1n" id="h_01hev188pb696nwg83zdnc0e1n"></a>

1. Click [Create a Flow](https://app.integry.io/platform/flow/create)
2.  Select a Trigger. In this example, we will select "Webhook" by Integry. This will let us invoke this Flow by calling the Webhook URL, more on that later.\
    \


    <figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>
3.  Select your app in the App field. Paste a sample json of the object that we will push from your app to Integry. Lastly, give this json payload a name.\
    \


    <figure><img src="../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>
4.  Add a step to perform an action in another app. In this example, we will select "Add Subscriber" in Mailchimp.\
    \


    <figure><img src="../../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>
5. Rename the flow and click Save.

That's it! The flow is ready for you to try. For that, head back to the Flows list.

### Set up an integration of the flow <a href="#h_01hev2zavgk1s46ekb4mgvr37g" id="h_01hev2zavgk1s46ekb4mgvr37g"></a>

1. Click Embed.
2. Click Generate Code.
3. Open the downloaded HTML file in the browser.
4. You'll see the flow you created. In this example, that's "Sync new contacts to Mailchimp". Click Setup and enable.
5. Login to Mailchimp.
6. Configure Mailchimp.
   1. Select the audience in which the subscriber will be created.
   2. Map the email field.
   3. Select the default subscriber status.
   4. Map any other fields and click Next.
7. Before we click Save to complete the setup, we need to do one small thing so we can access the URL we'll have to call to run this integration. Assuming you're using Chrome... click View > Developer > Javascript Console.
8. Now, click Save to initialize the integration.

Almost there! The integration is now live and ready to be triggered.

### Run the integration <a href="#h_01hev4chz4zw5bwp9z0jhthvb1" id="h_01hev4chz4zw5bwp9z0jhthvb1"></a>

1.  Right-click the URL shown in the console, and click Copy link address.\


    <figure><img src="../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>
2. Open Postman.
3. Set the method to POST.
4. Paste this URL.
5. Go to Body, select 'raw', click Text and switch that to JSON.
6. In the Integry app, go to Account Settings > Objects.
7. Select the object you selected while creating the flow. In this example, we selected "Contact".
8. Copy the JSON payload.
9. Paste the payload in the body in Postman.
   * If you want, you can modify any of the values.
10. Click Send to run it.

We're done! Head over to Mailchimp to see the new subscriber you just created.

Recap: You created a new flow, set up an integration of that flow, triggered it, and it ran.

You can now see how the run executed by clicking the count of users against this flow (in the flows list) and drilling down to runs.

Next, let's [Embed the Flows widget](broken-reference) so your users can set up integrations from within your app.
