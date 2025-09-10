---
icon: square-js
---

# JS SDK Reference

This reference documents every object and method available in Integry’s browser-side JavaScript library, Integry.js.

## Setting Up

### Including Integry.js

To use the Integry JS SDK, you need to include it in your project. You can install it via npm:

```bash
npm install @integry/sdk
```

Or include it via a script tag:

```html
<script src="https://unpkg.com/@integry/sdk/dist/umd/index.umd.js"></script>
```

### Authentication

The Integry JS SDK requires an `App-Key` and a hash of `App-Secret` and `User-ID` to authenticate calls.

You can view and copy your `App-Key` and `App-Secret` from [the Integry app](https://app.integry.io/platform/workspace/security/).

`User-ID` is a unique string identifier for a user in your app. Function Calls and Integrations are associated to a user ID.

{% hint style="info" %}
If your app has workspaces/accounts and you want integrations to be shared across all users in a workspace/account, use the workspace/account ID as the user ID.
{% endhint %}

#### **Calculating the hash**

Calculate the hash server-side using HMAC SHA256.

{% tabs %}
{% tab title="JS" %}
```javascript
const crypto = require("crypto");

const userId = "";
const appSecret = "";

const hash = crypto
.createHmac("sha256", appSecret)
.update(userId)
.digest("hex");
```
{% endtab %}

{% tab title="Python" %}
```python
import hmac
import hashlib

app_secret = b"<app_secret>"
user_id = b"<user_id>"

hash = hmac.new(app_secret, user_id, hashlib.sha256).hexdigest()
```
{% endtab %}

{% tab title="PHP" %}
```php
<?php

$appSecret = '<APP_SECRET>';
$userId = '<USER_ID>';
$hash = hash_hmac('sha256', $userId, $appSecret);
```
{% endtab %}
{% endtabs %}

### Initializing IntegryJS()

Call `IntegryJS(authentication)` with the`App-Key`, [computed hash](./#calculating-the-hash) and `User-ID` to create an instance of the Integry object.

```javascript
const userId = "USER_ID"; // Your user's ID
const appKey = "YOUR_INTEGRY_APP_KEY";
const hash = "YOUR_GENERATED_HASH";

const integry = new IntegryJS({
    appKey,
    hash,
    user: {
        userId: userId,
    },
    lang: 'en', // Supported values: 'en', 'es', 'fr', 'ja'
    options: { 
        title: "Apps", // Only relevant if you call showApps()
        tags: [],
        debug: false,
    },
    payloads: {
    },
});
```

### Language Support (`lang`)

> Available in SDK v4.8.1 and above (Enterprise plan only).

The Integry JS SDK now supports setting a **UI language** through the `lang` parameter in the initialization options. This controls the language used for all SDK-rendered UI elements such as buttons, labels, menus, and prompts.

**Usage**

You can pass `lang` alongside `appKey`, `hash`, and `user` when initializing the SDK. See example above.

**Supported Languages**

Currently, the following languages are available:

* `en` – English (default)
* `es` – Spanish
* `fr` – French
* `ja` – Japanese
* `pt-BR` – Brazilian Portuguese

If no `lang` is provided, the SDK defaults to **English**.

**Notes on Translations**

* The `lang` parameter applies only to **SDK UI strings** (e.g., placeholders, error messages, action buttons).
* Content loaded dynamically from Integry **backend** (such as integration names, descriptions, or flow data) is **not automatically translated**.
* For backend translations of new flows or content, please reach out to **hello@integry.io**.
* If you need SDK UI translations in a language other than the supported ones, contact us at **hello@integry.io** to request additional support.



### Listening to Events

Some SDK methods emit events (eg. [`ready`](./#emits-event), [`app-connected`](./#emits-events)) that you can leverage to manipulate the user journey.

#### Subscribe to an event

Call `eventEmitter.on('<event_name>')` method​.

```javascript
integry.eventEmitter.on('app-connected', (data) => {
    //do something here
});
```

{% hint style="info" %}
Events emitted by the SDK are scoped to the instance on which the `eventEmitter` object is configured. There is no possibility of naming collision with global events, or even with the same event subscribed on multiple SDK instances.
{% endhint %}

#### Unsubscribe from an event

Call `eventEmitter.unsub('<event_name>')` method.

```javascript
integry.eventEmitter.on('app-disconnected', (data) => {
    //do something here
});
```

### Error Handling

All methods in the Integry JS SDK return `Promises`. It is recommended to always include `.catch()` to handle errors gracefully. Here is an example:

```javascript
integry.connectApp("slack").then((connectedAccountId) => {
  console.log("Connected to Slack with account ID:", connectedAccountId);
}).catch((error) => {
  console.error("An error occurred:", error);
});
```

## Apps

Integry supports [many apps](https://www.integry.ai/apps) like Slack, Hubspot, or Jira.

### Show apps

`showApps(renderMode, containerID, layout, fetchAll, useLoadMoreButton)`

Renders a marketplace-style listing of apps. You can customize the [render mode, layouts and styling](../../embedded-ui/render-modes-layouts-and-styling.md).

<figure><img src="../../.gitbook/assets/Screenshot 2024-12-09 at 10.43.54 AM.png" alt="" width="563"><figcaption></figcaption></figure>

_Note: If you want to directly connect an app, use_ [_`connectApp()`_](./#connect-appname)_._

```javascript
integry.showApps(
  IntegryJS.RenderModes.INLINE,
  "marketplace-container"
).then(() => {
  console.log("Marketplace rendered in-line.");
}).catch((error) => {
  console.error("Error rendering filtered marketplace:", error);
});
```

#### Method parameters

<table><thead><tr><th width="182.77734375">Name</th><th width="92">Type</th><th width="320">Description</th><th>Required</th></tr></thead><tbody><tr><td><code>renderMode</code></td><td>string</td><td>Specifies the mode in which the marketplace will be rendered. Allowed values: <code>IntegryJS.RenderModes.MODAL</code>, <code>IntegryJS.RenderModes.INLINE</code>. Defaults to <code>MODAL</code> if not specified.</td><td>false</td></tr><tr><td><code>containerId</code></td><td>string</td><td>The ID of the HTML container in which the marketplace content will be rendered.</td><td>true if <code>renderMode=IntegryJS.RenderModes.INLINE</code></td></tr><tr><td><code>layout</code></td><td>string</td><td>Specifies the layout. Allowed values: <code>IntegryJS.Layouts.WIDE</code>, <code>IntegryJS.Layouts.NARROW</code>. Defaults to <code>WIDE</code> if not specified.</td><td>false</td></tr><tr><td><code>fetchAll</code></td><td>boolean</td><td><p></p><p>Determines whether all apps should be fetched at once or retrieved using pagination.</p><ul><li><strong>Default:</strong> <code>false</code> (uses pagination).</li><li><strong>When <code>true</code></strong>, the method fetches all available apps in a single request instead of making paginated API calls.</li><li><strong>Use case:</strong> Set <code>fetchAll: true</code> if you need to load all the apps at once.</li></ul></td><td>false</td></tr><tr><td><code>useLoadMoreButton</code></td><td>boolean</td><td>If set to <code>true</code>, the app list will disable infinite scroll and instead display a <strong>"Load More"</strong> button at the bottom. Users will need to manually click this button to fetch additional apps.<br>When <code>false</code>, more results will be automatically loaded as the user scrolls to the end of the list.</td><td>false</td></tr></tbody></table>

#### Emits events

`app-connected`

Fired when the user successfully connects an app. It includes the app details along with an array of `connected_accounts` sorted by `modified_at` in descending order.

```json
{
    "id": 410,
    "name": "pipedrive",
    "title": "Pipedrive",
    "icon_url": "https://storage.googleapis.com/app-services-prod--bucket/public/c07f082e-33d2-499f-b67a-d98722ab367b.png",
    "docs_url": "",
    "connected_account_id": "1234",
    "connected_accounts": [
        {
            "id": 247714,
            "display_name": "663----------8b1",
            "modified_at": "2024-11-10T23:28:58Z"
        }
    ]
}
```

`app-disconnected`

Fired when the user disconnects an app. It includes the app details along with an array of remaining `connected_accounts`(if any) sorted by `modified_at` in descending order.

```json
{
    "id": 410,
    "name": "pipedrive",
    "title": "Pipedrive",
    "icon_url": "https://storage.googleapis.com/app-services-prod--bucket/public/c07f082e-33d2-499f-b67a-d98722ab367b.png",
    "docs_url": "",
    "connected_account_id": "1234",
    "connected_accounts": []
}
```

### Show an app

`showApp(appName, renderMode, containerID, layout)`

Renders the app page with connected accounts and flows. You can customize the [render mode, layouts and styling](../../embedded-ui/render-modes-layouts-and-styling.md).

<figure><img src="../../.gitbook/assets/Screenshot 2024-12-09 at 10.38.21 AM.png" alt="" width="375"><figcaption></figcaption></figure>

```javascript
integry.showApp(
  "mailchimp"
  IntegryJS.RenderModes.INLINE,
  "marketplace-container"
).then(() => {
  console.log("Showing Mailchimp Flows!");
}).catch((error) => {
  console.error("Failed to launch Mailchimp:", error);
});
```

#### Method parameters

<table><thead><tr><th width="162">Name</th><th width="92">Type</th><th width="320">Description</th><th>Required</th></tr></thead><tbody><tr><td><code>appName</code></td><td>string</td><td>Name of the app to show. Eg. Hubspot</td><td>true</td></tr><tr><td><code>renderMode</code></td><td>string</td><td>Specifies the mode in which the marketplace will be rendered. Allowed values: <code>IntegryJS.RenderModes.MODAL</code>, <code>IntegryJS.RenderModes.INLINE</code>. Defaults to <code>MODAL</code> if not specified.</td><td>false</td></tr><tr><td><code>containerId</code></td><td>string</td><td>The ID of the HTML container in which the marketplace content will be rendered.</td><td>true if <code>renderMode=IntegryJS.RenderModes.INLINE</code></td></tr><tr><td><code>layout</code></td><td>string</td><td>Specifies the layout. Allowed values: <code>IntegryJS.Layouts.WIDE</code>, <code>IntegryJS.Layouts.NARROW</code>. Defaults to <code>WIDE</code> if not specified.</td><td>false</td></tr></tbody></table>

#### Emits events

`app-connected`

Fired when the user successfully connects an app. It includes the app details along with an array of `connected_accounts` sorted by `modified_at` in descending order.

```json
{
    "id": 410,
    "name": "pipedrive",
    "title": "Pipedrive",
    "icon_url": "https://storage.googleapis.com/app-services-prod--bucket/public/c07f082e-33d2-499f-b67a-d98722ab367b.png",
    "docs_url": "",
    "connected_account_id": "1234",
    "connected_accounts": [
        {
            "id": 247714,
            "display_name": "663----------8b1",
            "modified_at": "2024-11-10T23:28:58Z"
        }
    ]
}
```

`app-disconnected`

Fired when the user disconnects an app. It includes the app details along with an array of remaining `connected_accounts`(if any) sorted by `modified_at` in descending order.

```json
{
    "id": 410,
    "name": "pipedrive",
    "title": "Pipedrive",
    "icon_url": "https://storage.googleapis.com/app-services-prod--bucket/public/c07f082e-33d2-499f-b67a-d98722ab367b.png",
    "docs_url": "",
    "connected_account_id": "1234",
    "connected_accounts": []
}
```

### Connect an app

`connectApp(appName)`

Invokes a UI flow to prompt the user to authenticate with the specified app. After the user connects, Integry verifies that it can access their account. It also refreshes the token, if needed.

Use this to connect apps if you are not using [showApps()](./#renderapps-options-object) .

<pre class="language-javascript"><code class="lang-javascript"><strong>integry.connectApp("slack").then((connectedAccountId) => {
</strong>  console.log("Connected to Slack with account ID:", connectedAccountId);
}).catch((error) => {
  console.error("Failed to connect to Slack:", error);
});
</code></pre>

#### Method parameters

<table><thead><tr><th>Name</th><th width="76">Type</th><th width="306">Description</th><th width="103">Example</th><th>Required</th></tr></thead><tbody><tr><td><code>appName</code></td><td>string</td><td>The name of the app you want the user to connect.</td><td>slack</td><td>true</td></tr></tbody></table>

#### Returns

This method returns a `connectedAccountId` (string).

If you use `connectApp()`to enable your users to connect multiple accounts for an app, you will need to use this ID when you [disconnectApp()](./#disconnectapp-appname-connectedaccountid), [showFunctionUI() ](./#showfunctionui-functionname-params-connectedaccountid)and [invokeFunction()](./#invokefunction-functionname-params-connectedaccountid).

### Disconnect an app

`disconnectApp(appName, connectedAccountId)`

Disconnects the user's connected account for an app.

<pre class="language-javascript"><code class="lang-javascript"><strong>integry.disconnectApp("slack").then(() => {
</strong>  console.log("Successfully disconnected from Slack");
}).catch((error) => {
  console.error("Failed to disconnect from Slack:", error);
});
</code></pre>

#### Method parameters

<table><thead><tr><th width="146">Name</th><th width="76">Type</th><th width="198">Description</th><th width="103">Example</th><th>Required</th></tr></thead><tbody><tr><td><code>appName</code></td><td>string</td><td>The name of the app to disconnect.</td><td>slack</td><td>true</td></tr><tr><td><code>connectedAccountId</code></td><td>string</td><td>The ID of the connected account to delete.</td><td>1234</td><td>true if the user has multiple connected accounts of this app</td></tr></tbody></table>

#### Returns

This method returns a `Promise` which resolves if the account is disconnected.

### Check if app is connected

`isAppConnected(appName)`

Checks if the user has connected the specified app.

<pre class="language-javascript"><code class="lang-javascript"><strong>integry.isAppConnected("slack").then((result) => {
</strong>  if(result) {
    console.log("User has connected Slack.");
  } else {
    console.log("User has not connected Slack.");
  }
  
}).catch((error) => {
  console.error("Failed to determine auth status:", error);
});
</code></pre>

#### Method parameters

<table><thead><tr><th>Name</th><th width="76">Type</th><th width="306">Description</th><th width="103">Example</th><th>Required</th></tr></thead><tbody><tr><td><code>appName</code></td><td>string</td><td>The name of the app.</td><td>slack</td><td>true</td></tr></tbody></table>

#### Returns

This method returns a boolean `result`. It will be true if the user has one (or more) connected account(s) with this app.

If your users have connected multiple accounts, use [getConnectedAccounts()](./#getconnectedaccounts-appname) to get their IDs.

### Get connected accounts of an app

`getConnectedAccounts(appName)`

Returns a user's connected accounts for an app.

#### Method parameters

<table><thead><tr><th>Name</th><th width="76">Type</th><th width="306">Description</th><th width="103">Example</th><th>Required</th></tr></thead><tbody><tr><td><code>appName</code></td><td>string</td><td>The name of the app.</td><td>slack</td><td>true</td></tr></tbody></table>

#### Returns

This method returns an array of `connected_accounts`.

```json
{
    "connected_accounts": [
        {
            "id": 247714,
            "display_name": "663----------8b1",
            "modified_at": "2024-11-10T23:28:58Z"
        }
    ]
}
```

### Show connected accounts of an app (Coming soon)

`showConnectedAccounts(appName, renderMode, containerID, layout)`

Renders a user's connected accounts for an app. Coming soon!

## Functions

### Show functions (Coming soon)

`showFunctions(renderMode, containerID, layout, appName)`

Renders a list of functions. You can filter by app. Coming soon!

### Show a function

`showFunction(functionName, options)`

Shows a function's parameters (with pre-filled values, if provided). The user can provide/modify the values. Take the output of this method to [call the function](./#call-a-function).

<figure><img src="../../.gitbook/assets/Screenshot 2024-12-09 at 10.52.35 AM.png" alt="" width="375"><figcaption></figcaption></figure>

```javascript
const params = {
  channel: "general",
  message: "Hello, team!"
};

integry.showFunctionUI("slack-post-message", {
  params: params
}).then((result) => {
  console.log("Function parameters filled-in by the user:", result);
}).catch((error) => {
  console.error("Failed to load function UI:", error);
});
```

#### Method parameters

<table><thead><tr><th width="140">Name</th><th width="83">Type</th><th width="381">Description</th><th width="156">Example</th><th>Required</th></tr></thead><tbody><tr><td><code>functionName</code></td><td>string</td><td>The name of the function to render.</td><td>slack-post-message</td><td>true</td></tr><tr><td><code>options</code></td><td>object</td><td>An object containing the function options.</td><td></td><td>false</td></tr><tr><td><code>options.params</code></td><td>object</td><td>An object containing the function parameters.</td><td><pre><code>{
  channel: "general",
  message: "Hello, team!"
}
</code></pre></td><td>false</td></tr><tr><td><code>options.payload</code></td><td>object</td><td>An object containing data from your app that users can map to function fields.</td><td><pre><code>{
  first_name: "John",
  last_name: "Doe"
}
</code></pre></td><td>false</td></tr><tr><td><code>options.autoMapPayload</code></td><td>boolean</td><td>An option to predict arguments by using the payload you pass.</td><td>false</td><td>false</td></tr><tr><td><code>options.connectedAccountId</code></td><td>string</td><td>An optional parameter to pass connected account id to use to make function calls.</td><td>12345</td><td>false</td></tr></tbody></table>

#### Returns

This method returns a `result` object with the filled-in arguments.

<pre class="language-json"><code class="lang-json">{
<strong>        "channel":"random",
</strong>        "text":"hello world from the other side"
}
</code></pre>

Use it as `params` to [invokeFunction()](./#invokefunction-functionname-params-connectedaccountid).

### Call a function

`invokeFunction(functionName, params, connectedAccountId)`

Invokes the specified function of an app with the provided parameters. Integry will automatically include your user's authentication credentials when making the onwards API call.

Integry will execute the function if the user has already connected their account for the function app, and all required parameters (if any) are provided in `params`. These function calls will show in the Function Calls log in [the Integry app](https://app.integry.io/platform/functions/calls-log).

Integry will not execute the function if the user has not connected an account, or the parameters passed are invalid. These function calls will not show in the Function Calls log.

```javascript
const params = {
  channel: "random",
  message: "hello world from the other side"
};
integry.invokeFunction("slack-post-message", params).then((result) => {
  console.log("Received response from Slack:", result);
}).catch((error) => {
  console.error("Failed to invoke function:", error);
});
```

#### Method parameters

<table><thead><tr><th width="140">Name</th><th width="83">Type</th><th width="346">Description</th><th width="120">Example</th><th>Required</th></tr></thead><tbody><tr><td><code>functionName</code></td><td>string</td><td>The name of the function to execute</td><td>slack-post-message</td><td>true</td></tr><tr><td><code>params</code></td><td>object</td><td>An object containing the function parameters.</td><td>{"limit":5}</td><td>true</td></tr><tr><td><code>connectedAccountId</code></td><td>string</td><td>The connected account to use for executing the action. Only use if the user has connected multiple accounts.</td><td>43654</td><td>false</td></tr></tbody></table>

Sample `params` object for `pipedrive-add-a-person` function call:

```json
{
    "name": "Sample contact"
}
```

The functions which fetch data from an app will often return pages of data and allow you to fetch further data by making subsequent calls. These functions use cursor-based pagination via the `next_page` parameter that is returned in the `result` (if there are more pages).

Sample `params` object for `pipedrive-get-all-persons` function call with `next_page`:

```json
{
    "limit": 5,
    "next_page": "eyJmaWVsZCI6ImlkIiwiZmllbGRWYWx1ZSI6Niwic29ydERpcmVjdGlvbiI6ImFzYyIsImlkIjo2fQ"
}
```

**Returns**

If Integry executes the function, this method returns a `result` object with following keys:

* `network_code`: HTTP response status code of the onwards API call made by Integry.
* `output`: HTTP response body of the onwards API call made by Integry.
* `next_page`: The cursor for the next page. It will only be present in responses of functions that support paginated calls. If there are no more pages, it will be empty.

If Integry does not execute the function, this method returns a `result` object with following keys:

* `error`: Summary of the error.
* `error_details[]`: Detailed errors for individual fields (if applicable).

Sample responses for `pipedrive-add-a-person` and `pipedrive-get-all-persons`:

{% tabs %}
{% tab title="Result 1" %}
{% code lineNumbers="true" %}
```json
// Function name: pipedrive-add-a-person
// Outcome: Person was created
{
    "network_code": "200",
    "output": {
        "success": true,
        "data": {
            "id": 27,
            "name": "Sample contact",
            "first_name": "Sample",
            "last_name": "contact",
            "add_time": "2024-11-11T17:18:18Z",
            "update_time": null,
            "visible_to": 3,
            "custom_fields": null,
            "owner_id": 22469411,
            "label_ids": [],
            "org_id": null,
            "is_deleted": false,
            "picture_id": null,
            "phones": [],
            "emails": []
        }
    }
}
```
{% endcode %}
{% endtab %}

{% tab title="Result 2" %}
```json
// Function name: pipedrive-add-a-person
// Outcome: Validation error
{
    "network_code": "400",
    "output": {
        "success": false,
        "error": "Validation failed: owner_id: User not found or not accessible.",
        "code": "ERR_SCHEMA_VALIDATION_FAILED"
    }
}
```
{% endtab %}

{% tab title="Result 3 (with next_page)" %}
```json
// Function name: pipedrive-get-all-persons
// Outcome: Data was fetched with a next_page cursor.
{
    "network_code": "200",
    "output": [
        {
            "id": 1,
            "name": "[Sample] Phyllis Yang",
            "first_name": "[Sample] Phyllis",
            "last_name": "Yang",
            "add_time": "2024-11-10T23:28:58Z",
            "update_time": "2024-11-11T00:52:38Z",
            "visible_to": 3,
            "custom_fields": null,
            "owner_id": 22469411,
            "label_ids": [
                14
            ],
            "org_id": 5,
            "is_deleted": false,
            "picture_id": null,
            "phones": [
                {
                    "label": "",
                    "value": "240-707-3884",
                    "primary": true
                }
            ],
            "emails": [
                {
                    "label": "work",
                    "value": "phyllis.yang@gmial.com",
                    "primary": true
                }
            ]
        },
        {
            "id": 2,
            "name": "[Sample] Tony Turner",
            "first_name": "[Sample] Tony",
            "last_name": "Turner",
            "add_time": "2024-11-10T23:28:58Z",
            "update_time": "2024-11-10T23:29:05Z",
            "visible_to": 3,
            "custom_fields": null,
            "owner_id": 22469411,
            "label_ids": [],
            "org_id": 1,
            "is_deleted": false,
            "picture_id": null,
            "phones": [
                {
                    "label": "",
                    "value": "218-348-8528",
                    "primary": true
                }
            ],
            "emails": [
                {
                    "label": "work",
                    "value": "tony.turner@moveer.com",
                    "primary": true
                }
            ]
        },
        {
            "id": 3,
            "name": "[Sample] Gloria Quinn",
            "first_name": "[Sample] Gloria",
            "last_name": "Quinn",
            "add_time": "2024-11-10T23:28:58Z",
            "update_time": "2024-11-10T23:29:05Z",
            "visible_to": 3,
            "custom_fields": null,
            "owner_id": 22469411,
            "label_ids": [],
            "org_id": 2,
            "is_deleted": false,
            "picture_id": null,
            "phones": [
                {
                    "label": "",
                    "value": "862-252-9773",
                    "primary": true
                }
            ],
            "emails": [
                {
                    "label": "work",
                    "value": "gloria.quinn@empowermmove.com",
                    "primary": true
                }
            ]
        },
        {
            "id": 4,
            "name": "[Sample] Benjamin Leon",
            "first_name": "[Sample] Benjamin",
            "last_name": "Leon",
            "add_time": "2024-11-10T23:28:58Z",
            "update_time": "2024-11-10T23:29:05Z",
            "visible_to": 3,
            "custom_fields": null,
            "owner_id": 22469411,
            "label_ids": [],
            "org_id": null,
            "is_deleted": false,
            "picture_id": null,
            "phones": [
                {
                    "label": "",
                    "value": "785-202-7824",
                    "primary": true
                }
            ],
            "emails": [
                {
                    "label": "work",
                    "value": "benjamin.leon@gmial.com",
                    "primary": true
                }
            ]
        },
        {
            "id": 5,
            "name": "[Sample] Otto Miller",
            "first_name": "[Sample] Otto",
            "last_name": "Miller",
            "add_time": "2024-11-10T23:28:58Z",
            "update_time": "2024-11-10T23:29:05Z",
            "visible_to": 3,
            "custom_fields": null,
            "owner_id": 22469411,
            "label_ids": [],
            "org_id": 3,
            "is_deleted": false,
            "picture_id": null,
            "phones": [
                {
                    "label": "",
                    "value": "601-906-7534",
                    "primary": true
                }
            ],
            "emails": [
                {
                    "label": "work",
                    "value": "otto.miller@itablee.eu",
                    "primary": true
                }
            ]
        }
    ],
    "next_page": "eyJmaWVsZCI6ImlkIiwiZmllbGRWYWx1ZSI6Niwic29ydERpcmVjdGlvbiI6ImFzYyIsImlkIjo2fQ"
}
```
{% endtab %}

{% tab title="Error 1" %}
```json
// Function name: pipedrive-add-a-person
// Outcome: Error -- app was not connected
{
    "error": "Could not call the function due to invalid input. Please see `error_details` for further information.",
    "error_details": [
        "User has not connected their Pipedrive account. To connect an account, please call following SDK method: `connect('pipedrive')`"
    ]
}
```
{% endtab %}

{% tab title="Error 2" %}
```json
// Function name: pipedrive-add-a-person
// Outcome: Error -- required parameter was missing
{
    "error": "Could not call the function due to invalid input. Please see `error_details` for further information.",
    "error_details": {
        "name": "This parameter is required and must not be null or empty"
    }
}
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
In rare cases where Integry is unable to determine if there are more pages, it will respond with a `next_page` cursor. Your subsequent call will return an empty `output[]` and `next_page` cursor since there are no more pages.
{% endhint %}

### Get a function

`getFunction(functionName)`

Gets the signature for a specific function to understand the parameters.

```javascript
integry.getFunction("slack-post-message").then((result) => {
  console.log("Function signature:", result);
}).catch((error) => {
  console.error("Failed to get function signature:", error);
});
```

#### Method parameters

<table><thead><tr><th width="140">Name</th><th width="83">Type</th><th width="346">Description</th><th width="120">Example</th><th>Required</th></tr></thead><tbody><tr><td><code>functionName</code></td><td>string</td><td>The name of the function to execute</td><td>slack-post-message</td><td>true</td></tr></tbody></table>

**Returns**

This method returns a `result` object with the function's signature.

```json
{
    "name": "slack-post-message",
    "description": "Post a message in a channel",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "The content of the message."
            },
            "channel": {
                "type": "string",
                "description": "The channel to send the message in. Call `slack-list-conversations` to get the available values."
            },
            "as_user": {
                "type": "boolean",
                "description": "(Legacy) Pass true to post the message as the authed user instead of as a bot. Defaults to false. Can only be used by classic apps."
            },
            "attachments": {
                "type": "string",
                "description": "A JSON-based array of structured attachments, presented as a URL-encoded string."
            },
            "blocks": {
                "type": "array",
                "description": "A JSON-based array of structured blocks, presented as a URL-encoded string.",
                "items": {
                    "type": "string"
                }
            },
            "icon_emoji": {
                "type": "string",
                "description": "Emoji to use as the icon for this message. Overrides icon_url."
            },
            "icon_url": {
                "type": "string",
                "description": "URL to an image to use as the icon for this message."
            },
            "link_names": {
                "type": "boolean",
                "description": "Find and link user groups. No longer supports linking individual users; use syntax shown in Mentioning Users instead."
            },
            "metadata": {
                "type": "string",
                "description": "JSON object with event_type and event_payload fields, presented as a URL-encoded string. Metadata you post to Slack is accessible to any app or user who is a member of that workspace."
            },
            "mrkdwn": {
                "type": "boolean",
                "description": "Disable Slack markup parsing by setting to false. Enabled by default."
            },
            "parse": {
                "type": "string",
                "description": "Change how messages are treated."
            },
            "reply_broadcast": {
                "type": "boolean",
                "description": "Used in conjunction with thread_ts and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to false."
            },
            "thread_ts": {
                "type": "string",
                "description": "Provide another message's ts value to make this message a reply. Avoid using a reply's ts value; use its parent instead."
            },
            "unfurl_links": {
                "type": "boolean",
                "description": "Pass true to enable unfurling of primarily text-based content."
            },
            "unfurl_media": {
                "type": "boolean",
                "description": "Pass false to disable unfurling of media content."
            },
            "username": {
                "type": "string",
                "description": "Set your bot's user name."
            }
        },
        "required": [
            "text",
            "channel"
        ]
    }
}
```

## Flows

### Show flows (Coming soon)

`showFlows(renderMode, containerID, layout, appName)`

Show flows in your workspace. You can filter by app. Coming soon!

### Show a flow (Coming soon)

`showFlow(flowID, renderMode, containerID, layout)`

Show a flow in your workspace. Coming soon!

### Create an integration (Coming soon)

`createIntegration(flowID, mappings)`

Create an integration of a flow in your workspace. Coming soon!

### Edit an integration (Coming soon)

`editIntegration(flowID)`

Edit an integration of a flow in your workspace. Coming soon!

### Trigger an integration (Coming soon)

`triggerIntegration(integrationID, payload)`

Trigger an integration of a flow in your workspace. Coming soon!
