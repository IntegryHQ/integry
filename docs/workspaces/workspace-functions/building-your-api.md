# Building your API

If you're looking to push data to your app, you must provide an API that Integry will use to create, update, or delete objects at your end.

For example, if you want to import tasks from [Asana](https://integry.ai/apps/asana), you will need an equivalent API endpoint in your app for creating tasks (or tickets, todos, items, or the matching name in your app).&#x20;

There are many great articles on building Restful APIs. This document is only a subset of recommendations that are relevant to integrations.

### Authentication: API-Key <a href="#h_01haark85e2h01hw0793qxhhmk" id="h_01haark85e2h01hw0793qxhhmk"></a>

The key should ideally be scoped to a per-user level. Integry will use this key to make calls to your app's API on the user's behalf. You can also have API keys scoped at an app level. These keys are usually for admin APIs, where Integry can change any user's object.

### Don't make an Integry-specific endpoint <a href="#h_01haark85eydvabwq6jz2ptkts" id="h_01haark85eydvabwq6jz2ptkts"></a>

The number of API clients using your APIs will increase as you grow. Creating client-specific endpoints will quickly go out of hand. Instead, we recommend creating generic endpoints you can give anyone, not just Integry.&#x20;

🟢 good: /api/task

🔴 bad: /projects/integry

### Don't hardcode third-party apps <a href="#h_01haark85ejsg13p0vdmp06808" id="h_01haark85ejsg13p0vdmp06808"></a>

A key benefit of working with Integry is that it will allow you to pull data from any app. You may start with one app like Asana, but if you need to add another app, you will have to code another endpoint, which will quickly become unwieldy. So:

🟢 good: /api/task

🔴 bad: /api/asana

Ideally, your logic should be agnostic of the third-party app you're integrating with (unless you plan on building a product around the app). It shouldn't matter where the data comes from. However, if you need to track where it comes from, Integry can send its internal app ID and name in your API call.

### Return values <a href="#h_01haark85ed2vjt7cnqm79c4tr" id="h_01haark85ed2vjt7cnqm79c4tr"></a>

APIs that create objects should return the ID of the created object at the minimum and, ideally, the entire object. This is helpful for downstream steps in your integration.&#x20;
