---
icon: comment-question
---

# Embedding FAQs

### Can the SDK be integrated in any framework of my choice? <a href="#h_01hndj40zvnw2bn8xcj7rx0cte" id="h_01hndj40zvnw2bn8xcj7rx0cte"></a>

Yes. The SDK package is framework-agnostic and can be installed in any framework that supports Javascript and HTML. It is also compatible with server-side rendering and can be used with frameworks such as NextJS and Nuxt.

### How do I embed Integry in different deployment environments?

You will embed the same code in all your environments. Integry will use the same base URL and use the same API key(s) when calling your API endpoints.

If you want different flows to show in different environments, you can tag the flows, and filter on the tag(s) in the embed code.

If you want Integry to consider each environment to be completely separate, you can create [additional workspaces](broken-reference). This feature is only available on the Enterprise license.

### How do I make the rendered HTML from SDK match my app's look and feel? <a href="#h_01hndm9ckdpr0kaq5ddhzbxw8y" id="h_01hndm9ckdpr0kaq5ddhzbxw8y"></a>

SDK returns a basic HTML structure that you have full control over. As the SDK's output becomes part of your app, so you can override the CSS styles to make any changes required to match your own app's look and feel.

### Can I customize the styling with my own CSS? <a href="#h_01hndj5mq95shgfm5cr129scbf" id="h_01hndj5mq95shgfm5cr129scbf"></a>

Of course! Go [here](render-modes-layouts-and-styling.md).

### How do I remove extra HTML elements being rendered by the SDK, e.g. a few headings that we don't need, etc.? <a href="#h_01hndma0wpkymrpkm7m1383zyd" id="h_01hndma0wpkymrpkm7m1383zyd"></a>

You can simply inspect the HTML returned by the SDK and set the elements to hidden which are not required.

### Why are my users being asked to provide an API key for my app? <a href="#h_01hndma508btdvrx515h651b5m" id="h_01hndma508btdvrx515h651b5m"></a>

Integry requires an API key to be able to call your app to make HTTP calls. If you pass an API key when you [initialize IntegryJS()](../apis-and-sdks/js-sdk-reference/#initializing-integryjs), the prompt will disappear.

### How do I edit an existing integration? <a href="#h_01hndm8da3nr42rkfyc1sk068y" id="h_01hndm8da3nr42rkfyc1sk068y"></a>

Call [editIntegration()](../apis-and-sdks/js-sdk-reference/#edit-an-integration-coming-soon).
