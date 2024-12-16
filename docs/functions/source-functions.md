---
icon: arrow-progress
---

# Source Functions

Source functions return object arrays that can be used to dynamically [populate dropdown options](source-functions.md#populate-dropdown-options), or [fetch custom fields](source-functions.md#fetch-custom-fields).

### Populate dropdown options

Functions like `slack-post-message` require the user to provide an ID value for the `channel` parameter. Source functions help populate such arguments.

For example, when you [show the Function UI](https://integry.gitbook.io/integry-docs/apis-and-sdks/js-sdk-reference#show-the-function-ui) to the user so they can select a `channel`, we call the source function `slack-list-conversations` (using the user's auth credentials) to populate the `channel` dynamic dropdown.

In fact, when you [predict the arguments with Integry AI](https://integry.gitbook.io/integry-docs/functions/quickstart-for-ai#predict-the-arguments-with-integry-ai), we call the same source function to get the list of channels so we can predict the most relevant option.

When you [get a function](https://integry.gitbook.io/integry-docs/apis-and-sdks/api-reference#get-a-function), the description of a field will mention if there is a source function available to list the options for that field.

See line 9 of this sample response for `GET /functions/slack-post-message`:

<pre class="language-json" data-overflow="wrap" data-line-numbers><code class="lang-json">{
    "name": "slack-post-message",
    "description": "Post a message in a channel",
    "parameters": {
        "type": "object",
        "properties": {
            "channel": {
                "type": "string",
    <a data-footnote-ref href="#user-content-fn-1">            "description": "The channel to send the message in. Call `slack-list-conversations` to get the available values."</a>
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
</code></pre>

### Fetch custom fields

Apps like Hubspot let the user completely customize objects to represent their business. Hence, functions like `hubspot-create-contact` don't have any typical standard parameters like email, name, etc. Instead, it requires an object parameter called `properties` in which all the fields of the contact to be created have to be passed. Source functions help populate such arguments.

When you [show the Function UI](https://integry.gitbook.io/integry-docs/apis-and-sdks/js-sdk-reference#show-the-function-ui) to the user so they can fill the Contact object fields, we call the source function `hubspot-list-properties` (with `objectType`: Contact) to fetch all the custom fields for the Contact object.

Similarly, when you [predict the arguments with Integry AI](https://integry.gitbook.io/integry-docs/functions/quickstart-for-ai#predict-the-arguments-with-integry-ai), we call the same source function to get the list of fields so we can predict the most relevant values for the fields.

When you [get a function](https://integry.gitbook.io/integry-docs/apis-and-sdks/api-reference#get-a-function), the description of an object field will mention if there is a source function available to list the fields for that object.

Sample response for `GET /functions/hubspot-create-contact`:

<pre class="language-json" data-overflow="wrap" data-line-numbers><code class="lang-json">{
    "name": "hubspot-create-contact",
    "description": "Create a contact with the given properties. Call hubspot-list-properties to get the properties.",
    "parameters": {
        "type": "object",
        "properties": {
            "properties": {
                "type": "object",
                <a data-footnote-ref href="#user-content-fn-2">"description": "Provide the properties as key, value pairs. Call `hubspot-list-properties` to get the available values.",</a>
                "properties": {}
            }
        },
        "required": []
    }
}
</code></pre>

### Call a source function

You can call a source function like any other function via the [API](https://integry.gitbook.io/integry-docs/apis-and-sdks/api-reference#call-a-function) or [SDK](https://integry.gitbook.io/integry-docs/apis-and-sdks/js-sdk-reference#call-a-function).

In fact, they can typically be called headlessly because they usually don't have any required parameters. You should cache the data to avoid repeated calls.

Good candidates to cache are channel list, user list, issue types, project names, etc. Ultimately, it depends on your use-case, but you can also implement a generic solution for supporting function data.

### List all source functions

You cannot list all source functions, per se, because they are context-dependent. Instead, you can list all query-type functions with `GET /functions?type=query.` To get all query-type functions for just one app, call `GET /functions?type=query&app=<app_name>`.

See [`/functions`](https://integry.gitbook.io/integry-docs/apis-and-sdks/api-reference#list-all-functions) for more options.

[^1]: Call this additional function to get data for this field



[^2]: Information on function call to get details
