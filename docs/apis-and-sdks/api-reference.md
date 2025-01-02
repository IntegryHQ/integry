---
icon: gear
---

# API Reference

The Integry API is organized around [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts [JSON-encoded](http://www.json.org/) and [form-encoded](https://en.wikipedia.org/wiki/POST_\(HTTP\)#Use_for_submitting_web_forms) request bodies, returns [JSON-encoded](http://www.json.org/) responses, and uses standard HTTP response codes, authentication, and verbs.

## Setting Up

### Base URL

```
https://api.integry.io
```

### Client Libraries

{% tabs %}
{% tab title="Node.js" %}
```bash
npm install --save integry
```
{% endtab %}

{% tab title="Python" %}
```bash
pip install integry
```
{% endtab %}
{% endtabs %}

### Authentication

The Integry API requires an `App-Key` , `User-ID` and a hash of `App-Secret` and `User-ID` in the request headers to authenticate requests.&#x20;

You can view and copy your `App-Key` and `App-Secret` from [the Integry app](https://app.integry.io/wapp/settings/embed/).

`User-ID` is a unique string identifier for a user in your app. Function Calls and Integrations are associated to a user ID.

{% hint style="info" %}
If your app has workspaces/accounts and you want integrations to be shared across all users in a workspace/account, use the workspace/account ID as the user ID.
{% endhint %}

All API requests must be made over [HTTPS](http://en.wikipedia.org/wiki/HTTP_Secure). Calls made over plain HTTP will fail. API requests without authentication will also fail.

#### **Calculating the hash**

Calculate the hash server-side using HMAC SHA256.

{% tabs %}
{% tab title="Node.js" %}
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

#### Making an authenticated request

{% tabs %}
{% tab title="cURL" %}
{% code lineNumbers="true" %}
```bash
curl -X POST "https://api.integry.io/functions/slack-post-message/call/"
-H 'Content-Type: application/json'
-H 'App-Key: 002d4f23-778a-11e7-bf2a-42010a8002c7'
-H 'Hash: 08c123c88c6ee6b102710fcd00017c45250125e3a934d96750f4f70effece85a' 
-H 'User-ID: 123456'
-d '{"channel":"random",
     "text":"Hello, there!",
    }'
```
{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code lineNumbers="true" %}
```javascript
const userId = "USER_ID"; // Your user's ID
const appKey = "YOUR_INTEGRY_APP_KEY";
const appSecret = "YOUR_INTEGRY_APP_SECRET";

const Integry = require('integry');
const integry = Integry(
    appKey,
    appSecret
);

integry.functions.call("slack-post-message",{
     user_id: "123456",
     params: {
         "channel":"random",
         "text": "Hello, there!"
     }
});
```
{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code lineNumbers="true" %}
```python
from integry import Integry

user_id = "USER_ID" # Your user's ID
app_key = "YOUR_INTEGRY_APP_KEY"
app_secret = "YOUR_INTEGRY_APP_SECRET"

integry = Integry(
    app_key=app_key,
    app_secret=app_secret,
)

await integry.functions.call(
    "slack-post-message",
    {"channel": "random", "text": "Hello, there!"},
    user_id,
)
```
{% endcode %}
{% endtab %}
{% endtabs %}

## Apps

### List all apps

<mark style="color:purple;">`POST`</mark> `/apps/list`

List all apps available in Integry. If you need more, please reach out!

#### Sample Call&#x20;

{% tabs %}
{% tab title="cURL" %}
{% code lineNumbers="true" %}
```bash
curl -X POST "https://api.integry.io/apps/list/"
-H 'Content-Type: application/json'
-H 'App-Key: 002d4f23-778a-11e7-bf2a-42010a8002c7'
-H 'Hash: 08c123c88c6ee6b102710fcd00017c45250125e3a934d96750f4f70effece85a' 
-H 'User-ID: 123456'
-d '{}'
```
{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code lineNumbers="true" %}
```javascript
integry.apps.list({
    user_id: 123456
});
```
{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code lineNumbers="true" %}
```python
await integry.apps.list(user_id="123456")
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Parameters

<details>

<summary><code>_cursor</code> string</summary>

Paginate through apps by setting the `_cursor` parameter to the `_cursor` returned in a previous request's response. Leave empty to fetch the first page of apps. Default page size is 50.

</details>

<details>

<summary><code>connected_only</code> boolean</summary>

Include as a query param to only list apps that the user has connected.

</details>

**Sample Response**

{% tabs %}
{% tab title="Apps Found" %}
{% code title="200 OK" %}
```json
{
    "apps": [
        {
            "id": 410,
            "name": "pipedrive",
            "title": "Pipedrive",
            "icon_url": "https://storage.googleapis.com/app-services-prod--bucket/public/c07f082e-33d2-499f-b67a-d98722ab367b.png",
            "docs_url": "",
            "connected_accounts": [
                {
                    "id": 247714,
                    "display_name": "663----------8b1",
                    "modified_at": "2024-11-10T23:28:58Z"
                }
            ]
        },
        {
            "id": 24514,
            "name": "4me",
            "title": "4me",
            "icon_url": "https://storage.googleapis.com/app-services-prod--bucket/public/0d80bd3a-8207-426d-80e8-8aa75f5db662.png",
            "docs_url": "",
            "connected_accounts": []
        },
        {
            "id": 118,
            "name": "accelo",
            "title": "Accelo",
            "icon_url": "https://storage.googleapis.com/app-services-prod--bucket/public/e36d9d8c-8188-40e9-9fbf-9f4b5433e4ee.png",
            "docs_url": "",
            "connected_accounts": []
        }
    ],
    "_cursor": "E5JTNBMzklM0EzOS43NzA4MzclMkIwMCUzQTAw"
}
```
{% endcode %}
{% endtab %}

{% tab title="Error" %}
{% code title="400 Bad Request" %}
```json
{
    "detail": "Authentication credentials were not provided."
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Returns

Returns an `object[]` of `apps` that match the criteria, and an optional `_cursor` to paginate over the results.

### Get an app with the user's connected accounts

<mark style="color:purple;">`POST`</mark> `/apps/:app_name/get`

Get the details of an individual app and user's connected accounts with the app by passing `app_name` as a path variable.

#### Sample Call&#x20;

{% tabs %}
{% tab title="cURL" %}
{% code lineNumbers="true" %}
```bash
curl -X POST "https://api.integry.io/apps/slack/get/"
-H 'Content-Type: application/json'
-H 'App-Key: 002d4f23-778a-11e7-bf2a-42010a8002c7'
-H 'Hash: 08c123c88c6ee6b102710fcd00017c45250125e3a934d96750f4f70effece85a' 
-H 'User-ID: 123456'
```
{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code lineNumbers="true" %}
```javascript
integry.apps.get("slack",{
    user_id: 123456
});
```
{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code lineNumbers="true" %}
```python
await integry.apps.get("slack", user_id="123456")
```
{% endcode %}
{% endtab %}
{% endtabs %}

**Sample Response**

{% tabs %}
{% tab title="App Found" %}
{% code title="200 OK" %}
```json
{
    "id": 491,
    "name": "slack",
    "title": "Slack",
    "icon_url": "https://storage.googleapis.com/app-services-prod--bucket/public/c53aa5ce-1ced-48cb-98cc-8859eb8bf85d.png",
    "docs_url": "",
    "connected_accounts": []
}
```
{% endcode %}
{% endtab %}

{% tab title="App Not Found" %}
{% code title="404 Not Found" %}
```javascript
{
    "detail": "App not found"
}
```
{% endcode %}
{% endtab %}

{% tab title="Error" %}
{% code title="400 Bad Request" %}
```json
{
    "detail": "Authentication credentials were not provided."
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Returns

Returns the app object along with an `object[]` of `connected_accounts` of the user, if any.

## Functions

### List all functions

<mark style="color:purple;">`POST`</mark> `/functions/list`

List all functions available in Integry. If you need more, make a [passthrough request](../apps/passthrough-requests.md) or reach out!

#### Sample Call&#x20;

{% tabs %}
{% tab title="cURL" %}
{% code lineNumbers="true" %}
```bash
curl -X POST "https://api.integry.io/functions/list/?app=hubspot&type=ACTION"
-H 'Content-Type: application/json'
-H 'App-Key: 002d4f23-778a-11e7-bf2a-42010a8002c7'
-H 'Hash: 08c123c88c6ee6b102710fcd00017c45250125e3a934d96750f4f70effece85a' 
-H 'User-ID: 123456'
-d '{}'
```
{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code lineNumbers="true" %}
```javascript
integry.functions.list({
    user_id: 123456,
    app: "hubspot",
    type: "ACTION"
});
```
{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code lineNumbers="true" %}
```python
await integry.functions.list(app="hubspot", type="ACTION", user_id="123456")
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Parameters

<details>

<summary><code>app</code> string</summary>

Include as a query param to only list functions of a an app. Eg. `app=Hubspot`

</details>

<details>

<summary><code>type</code> string</summary>

Include as a query param to only list functions of a type. Allowed values: `QUERY`, `ACTION`, `PASSTHROUGH`

</details>

<details>

<summary><code>_cursor</code> string</summary>

Paginate through functions by setting the `_cursor` parameter to the `_cursor` returned in a previous request's response. Leave empty to fetch the first page of functions. Default page size is 50.

</details>

<details>

<summary><code>connected_only</code> boolean</summary>

Include as a query param to only list functions of apps that the user has connected.

</details>

<details>

<summary><code>include</code> string</summary>

Include as a query param to get info for rendering the function UI. Allowed values: meta

</details>

#### Sample Response

{% tabs %}
{% tab title="Functions list" %}
{% code title="200 OK" %}
```json
{
    "functions": [
        {
            "name": "hubspot-create-company",
            "description": "Create a company with the given properties. Call hubspot-list-properties to get the properties.",
            "parameters": {
                "type": "object",
                "properties": {
                    "properties": {
                        "type": "object",
                        "description": "Provide the properties as key, value pairs.. Call `hubspot-list-properties` to get the available values.",
                        "properties": {}
                    }
                },
                "required": []
            }
        },
        {
            "name": "hubspot-create-contact",
            "description": "Create a contact with the given properties. Call hubspot-list-properties to get the properties.",
            "parameters": {
                "type": "object",
                "properties": {
                    "properties": {
                        "type": "object",
                        "description": "Provide the properties as key, value pairs. Call `hubspot-list-properties` to get the available values.",
                        "properties": {}
                    }
                },
                "required": []
            }
        },
        {
            "name": "hubspot-create-deal",
            "description": "Create a deal with the given properties. Call hubspot-list-properties to get the properties.",
            "parameters": {
                "type": "object",
                "properties": {
                    "properties": {
                        "type": "object",
                        "description": "Provide the properties as key, value pairs.. Call `hubspot-list-properties` to get the available values.",
                        "properties": {}
                    }
                },
                "required": []
            }
        }
    ],
    "_cursor": null
}
```
{% endcode %}
{% endtab %}

{% tab title="No functions" %}
{% code title="200 OK" %}
```javascript
{
    "functions": [],
    "_cursor": null
}
```
{% endcode %}
{% endtab %}

{% tab title="Error" %}
{% code title="403 Forbidden" %}
```json
{
    "detail": "Authentication credentials were not provided."
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Returns

Returns an `object[]` of `functions` that match the criteria, and an optional `_cursor` to paginate over the results.

### Predict a function

<mark style="color:purple;">`POST`</mark> `/functions/predict`

Use Integry to find the most relevant function based on a prompt. For more details, see [Predict Function with Integry AI](https://integry.gitbook.io/integry-docs/getting-started/quickstart/quickstart#predict-the-function-with-integry-ai).

#### Sample Call

{% tabs %}
{% tab title="cURL" %}
{% code lineNumbers="true" %}
```bash
curl -X POST "https://api.integry.io/functions/predict/?predict_arguments=true"
-H 'Content-Type: application/json'
-H 'App-Key: 002d4f23-778a-11e7-bf2a-42010a8002c7'
-H 'Hash: 08c123c88c6ee6b102710fcd00017c45250125e3a934d96750f4f70effece85a' 
-H 'User-ID: 123456'
-d '{
      "prompt": "Send a message on Slack on random that contact just signed up! Include the contact's details.",
      "_variables": {
         "first_name":"John",
         "last_name":"Doe"
      }
 }'
```
{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code lineNumbers="true" %}
```javascript
integry.functions.predict({
    user_id: "123456",
    prompt: "Send a message on Slack on random that contact just signed up! Include the contact's details.",
    predict_arguments: true,
    include: "",
    variables: {
      "first_name": "John",
      "last_name": "Doe"
    }
});
```
{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code lineNumbers="true" %}
```python
await integry.functions.predict(
    prompt="Send a message on Slack on random that contact just signed up! Include the contact's details.",
    user_id=user_id,
    predict_arguments=True,
    variables={"first_name": "John", "last_name": "Doe"},
)
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Parameters

<details>

<summary><code>prompt</code> string  <mark style="color:red;">Required</mark></summary>

Prompt to use to predict function (and arguments).

</details>

<details>

<summary>_<code>variables</code> object</summary>

Variables to use for auto-mapping arguments.

</details>

<details>

<summary><code>predict_arguments</code> boolean</summary>

Uses the `prompt` and optionally `_variables` to predict the arguments of the predicted function. See [Predict Arguments with Integry AI](https://integry.gitbook.io/integry-docs/getting-started/quickstart/quickstart#predict-the-arguments-with-integry-ai).

</details>

<details>

<summary><code>include</code> string</summary>

Include as a query param to get info for rendering the function UI. Allowed values: meta

</details>

#### Sample Response

{% tabs %}
{% tab title="Function predicted" %}
{% code title="200 OK" %}
```json
{
    "functions": [
        {
            "name": "slack-post-message",
            "description": "Post a message in a channel",
            "parameters": {
                "type": "object",
                "properties": {
                    "channel": {
                        "type": "string",
                        "description": "The channel to send the message in. Call `slack-list-conversations` to get the available values."
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
                    "text": {
                        "type": "string",
                        "description": "The content of the message."
                    },
                    "as_user": {
                        "type": "boolean",
                        "description": "(Legacy) Pass true to post the message as the authed user instead of as a bot. Defaults to false. Can only be used by classic apps."
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
                    "channel",
                    "text"
                ]
            },
            "arguments": {
                "channel": "random",
                "text": "A new contact just signed up! Here are the details:\nFirst Name: {first_name}\nLast Name: {last_name}"
            }
        }
    ]
}
```
{% endcode %}
{% endtab %}

{% tab title="Could not predict" %}
{% code title="200 OK" %}
```java
{
    "functions": []
}
```
{% endcode %}
{% endtab %}

{% tab title="Error" %}
{% code title="400 Bad Request" %}
```json
{
    "prompt": "Must be a non-empty string"
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

### Get a function

<mark style="color:purple;">`POST`</mark> `/functions/:function_name/get`

Get the JSON schema of an individual function by passing function name as a path variable.

#### Sample Call&#x20;

{% tabs %}
{% tab title="cURL" %}
{% code lineNumbers="true" %}
```bash
curl -X POST "https://api.integry.io/functions/slack-post-message/get/"
-H 'Content-Type: application/json'
-H 'App-Key: 002d4f23-778a-11e7-bf2a-42010a8002c7'
-H 'Hash: 08c123c88c6ee6b102710fcd00017c45250125e3a934d96750f4f70effece85a' 
-H 'User-ID: 123456'
-d '{ "prompt": "prompt-goes-here", "_variables": {} }'
```
{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code lineNumbers="true" %}
```javascript
integry.functions.get("slack-post-message",{
    user_id: "123456",
    include: "",
    prompt: "prompt-goes-here",
    variables: {}
});
```
{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code lineNumbers="true" %}
```python
await integry.functions.get(
    "slack-post-message",
    prompt="prompt-goes-here",
    variables={},
    user_id="123456",
 )
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Parameters

<details>

<summary><code>prompt</code> string</summary>

Prompt to use to predict arguments.

</details>

<details>

<summary><code>_variables</code> object</summary>

Variables to use for auto-mapping arguments.

</details>

<details>

<summary><code>include</code> string</summary>

Include as a query param to get info for rendering the function UI. Allowed values: meta

</details>

#### Sample Response

{% tabs %}
{% tab title="Function found" %}
{% code title="200 OK" %}
```json
{
    "name": "slack-post-message",
    "description": "Post a message in a channel",
    "parameters": {
        "type": "object",
        "properties": {
            "channel": {
                "type": "string",
                "description": "The channel to send the message in. Call `slack-list-conversations` to get the available values."
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
            "text": {
                "type": "string",
                "description": "The content of the message."
            },
            "as_user": {
                "type": "boolean",
                "description": "(Legacy) Pass true to post the message as the authed user instead of as a bot. Defaults to false. Can only be used by classic apps."
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
            "channel",
            "text"
        ]
    }
}
```
{% endcode %}
{% endtab %}

{% tab title="Error" %}
{% code title="404 Not Found" %}
```json
{
    "detail": "Function not found"
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Returns

All supported function `parameters` are returned as keys, along with their `type` and `description` as key, value pairs. Required parameters are listed in the `required` array.

If you include a `prompt`, Integry AI will predict the arguments and list them in the `arguments` object.

If you include variables, Integry will auto-map them to the parameters and include reference tags (eg. `{first_name}`) in the values in the `arguments` object.

If you include both a `prompt` and `_variables`, Integry will predict the arguments using both the prompt and variables, adding tags where appropriate (eg. `"message": "{first_name} {last_name} just signed up!"`)&#x20;

### Call a function

<mark style="color:purple;">`POST`</mark> `/functions/:function_name/call`

Call a function by passing `function_name` as a path variable and the function parameters in the request body. Integry will automatically add the user's authentication credentials (eg. access token, API key) to the call.

Integry will execute the function if the user has already connected their account for the function app, and all required parameters (if any) are provided in the body. These function calls will show in the [Functions > Calls Log](https://app.integry.io/platform/functions/calls-log).

Integry will not execute the function if the user has not connected an account, or the parameters passed are invalid. These function calls will not show in the Function Calls log.

#### Sample Call

{% tabs %}
{% tab title="cURL" %}
{% code lineNumbers="true" %}
```bash
curl -X POST "https://api.integry.io/functions/slack-post-message/call/"
-H 'Content-Type: application/json'
-H 'App-Key: 002d4f23-778a-11e7-bf2a-42010a8002c7'
-H 'Hash: 08c123c88c6ee6b102710fcd00017c45250125e3a934d96750f4f70effece85a' 
-H 'User-ID: 123456'
-d '{
    "channel": "random",
    "text": "{first_name} {last_name} just signed up!",
    "_variables": {
        "first_name": "John",
        "last_name": "Doe"
     }
}'
```
{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code lineNumbers="true" %}
```javascript
integry.functions.call("slack-post-message", {
     user_id: "123456",
     connected_account_id: 1234,
     params: {
         channel: "random",
         text: "{first_name} {last_name} just signed up!"
     },
     variables: {
        "first_name": "John",
        "last_name": "Doe"
     }
});
```
{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code lineNumbers="true" %}
```python
await integry.functions.call("slack-post-message", {
     user_id: "123456",
     connected_account_id: 1234,
     arguments: {
         "channel": "random",
         "text": "{first_name} {last_name} just signed up!"
     },
     variables: {
        "first_name": "John",
        "last_name": "Doe"
     }
});
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Parameters

<details>

<summary><code>&#x3C;function_parameters></code> any data type  <mark style="color:red;">Required, if any</mark></summary>

In most cases, you simply need to pass the parameters of the function itself when calling a function. For instance, in the sample above, `channel` and `text` are required when calling `slack-post-message`.

If there are no required parameters, you don't have to pass anything.

</details>

<details>

<summary><code>_variables</code> object</summary>

Include if the values of any of the function parameters include variable reference tags.

</details>

<details>

<summary><code>_cursor</code> string, number or object </summary>

Include if the function returns paginated data. You will get the `_cursor` in the response of the first call if there are additional pages.

</details>

<details>

<summary><code>connected_account_id</code> number</summary>

Pass it as a query param if the user has connected multiple accounts of an app. For more, see [Connect an app](js-sdk-reference/#connect-an-app).

</details>

#### Sample Response

{% tabs %}
{% tab title="Function called" %}
{% code title="200 OK" %}
```javascript
{
    "network_code": "200",
    "output": {
        "ok": true,
        "channel": "C6F3LQ03A",
        "ts": "1734045658.057379",
        "message": {
            "user": "U02L42QCVGV",
            "type": "message",
            "ts": "1734045658.057379",
            "bot_id": "B0447TKCF1N",
            "app_id": "A6FQL4KQC",
            "text": "John Doe just signed up!",
            "team": "T6F74R6TB",
            "bot_profile": {
                "id": "B0447TKCF1N",
                "app_id": "A6FQL4KQC",
                "name": "Integry",
                "icons": {
                    "image_36": "https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-08-09/225182834294_8020ddc74d7822b48ea1_36.png",
                    "image_48": "https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-08-09/225182834294_8020ddc74d7822b48ea1_48.png",
                    "image_72": "https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-08-09/225182834294_8020ddc74d7822b48ea1_72.png"
                },
                "deleted": false,
                "updated": 1663866569,
                "team_id": "T6F74R6TB"
            },
            "blocks": [
                {
                    "type": "rich_text",
                    "block_id": "B92",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "John Doe just signed up!"
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }
}
```
{% endcode %}
{% endtab %}

{% tab title="Error" %}
{% code title="400 Bad Request" %}
```javascript
{
    "error": "Could not call the function due to invalid input. Please see `error_details` for further information.",
    "error_details": {
        "channel": "This parameter is required and must not be null or empty",
        "text": "This parameter is required and must not be null or empty"
    }
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### **Returns**

If Integry executes the function, it will respond with a `200 OK` with following keys in the response body:

* `network_code`: HTTP response status code of the onwards API call made by Integry.
* `output`: HTTP response body of the onwards API call made by Integry.
* `_cursor`: The cursor for the next page. It will only be present in responses of functions that support paginated calls. If there are no more pages, it will be `null`.

If Integry does not execute the function, it will respond with a `400 Bad Request` with following keys in the response body:

* `error`: Summary of the error.
* `error_details[]`: Detailed errors for individual fields (if applicable).

{% hint style="info" %}
In rare cases where Integry is unable to determine if there are more pages, it will respond with a `_cursor` as if there is more data to be fetched. However, your subsequent call will return an empty `output[]`  and `null` `_cursor`  which means there are no more pages.
{% endhint %}
