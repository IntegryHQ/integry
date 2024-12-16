---
icon: grid-2
---

# Overview

Integry support hundreds of apps. See the full list [here](https://www.integry.ai/apps).

### What can I do with a supported app?

#### Connect to the App

Your users can connect to the app. Integry manages the authentication process and refreshes tokens (if applicable). For more, see [Authentication](authentication/).

#### Call Functions

You can call functions to push/pull data to/from that app. Make a [`GET /functions?app=<app_name>`](https://integry.gitbook.io/docs/apis-and-sdks/api-reference#list-all-functions) call to find out what's possible. For more, see [Functions](../functions/overview.md).

#### Build Flows

You can build complex workflows that sync data one-way between your app and another app, or sync data bi-directionally. For more, see [Flows](../flows/overview.md).

#### Make Passthrough Requests

If you'd rather just consume the app's endpoints directly (while Integry manages auth), you can do that too! Simply make [Passthrough Requests](passthrough-requests.md).

### What if Integry does not have the app I need?

If we're able to access it, we'll be happy to add it! Our apps roadmap is entirely customer-driven. Tell us what you're looking for?
