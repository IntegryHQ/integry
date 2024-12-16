---
icon: layer-plus
---

# Build a Flow

With Integry's low-code flow builder, you can create flows to sync data from/to (or both) [250+ apps](https://www.integry.ai/apps) and your app in minutes using ready-to-use triggers, queries and actions.

A flow moves your user’s data between your app and another app. Flows can sync data from another app to your app, to another app from your app, or both.

For example, lets create a flow that will trigger when a contact is created in Hubspot, look it up in Acme, update the contact in Acme (if it's found) or create a new contact in Acme.

### Create a Flow <a href="#h_01hrwa95dd8fh7mm8kjzpcjkc6" id="h_01hrwa95dd8fh7mm8kjzpcjkc6"></a>

Go to the Flows page and click **Create New Flow**. You can rename it by clicking the name at the top.

### Select a Trigger <a href="#h_01hrsqrvfjsx67c09bm5q5x420" id="h_01hrsqrvfjsx67c09bm5q5x420"></a>

A flow must have at least one trigger. The trigger can be a webhook, a scheduler, or when the integration is initialized by the user. The webhook can be from your app, or choose from 200+ events in other apps.&#x20;

A flow can have more than one trigger. This is useful if, let's say, you want the integration to sync when a Contact is Created or Updated.&#x20;

### Add a Step <a href="#h_01hrsqs8w3bpbn59n003k2w0mg" id="h_01hrsqs8w3bpbn59n003k2w0mg"></a>

You can add pre-built actions of 250+ apps (or make a custom HTTP call yourself), make an HTTP call to your app, execute custom code, add control steps, etc. For a full list of steps, go [here](https://docs.integry.io/hc/en-us/articles/30060054060953).

Click the **+ button** below (or above) a step in the flow to add a step.

### Map Fields (or get User Input) <a href="#h_01hrwaemdfhpttqbwcs7a1gbye" id="h_01hrwaemdfhpttqbwcs7a1gbye"></a>

A field in the output of one step can be used as the input of a field of a step downstream. Click the **+ button** to browse the output of upstream steps.

If you would rather have the user map the field, or input/select a value, add it to the setup form.

### Test the Flow <a href="#h_01hrwa95ddhqv1gbs7022tve3a" id="h_01hrwa95ddhqv1gbs7022tve3a"></a>

You can run and test all the steps in a trigger block by clicking **Test this trigger block**. We will send a test trigger with a sample payload to run the block. If you want, you can modify the test payload.

If the Flow has more than one trigger, you can switch to the other trigger(s) and test.

### Add the Flow to the Marketplace <a href="#h_01hs95wjrs3hcrg0ga7wypp427" id="h_01hs95wjrs3hcrg0ga7wypp427"></a>

Once you're happy with the flow, add it to the marketplace so your users can use it.
