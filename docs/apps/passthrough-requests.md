---
icon: syringe
---

# Passthrough Requests

We have Functions for the most commonly used endpoints of 200+ apps.

If you want to do anything else, you can call the **Passthrough Request** function of any app we support via [API endpoint](passthrough-requests.md#make-a-passthrough-request-via-api) or [SDK method](passthrough-requests.md#make-a-passthrough-request-via-sdk). Integry will automatically add the user's auth credentials to the request.

### Make a passthrough request via API

<mark style="color:green;">`POST`</mark> `/<app_name>-passthrough-request`

Integry will execute the function if the user has already connected their account for the function app, and the `method` and `URL` parameters are provided in the body. These function calls will show in the Function Calls log in [the Integry app](https://app.integry.io/platform/functions/calls-log).

Integry will not execute the function if the user has not connected an account, or the parameters passed are invalid. These function calls will not show in the Function Calls log.

#### **Body**

| Name   | Type   | Description    | Required |
| ------ | ------ | -------------- | -------- |
| method | string | Request method | true     |
| url    | string | Request URL    | true     |
| body   | object | Request body   | false    |

#### **Response**

If Integry executes the function, it will respond with a `200 OK` with following keys in the response body:

* `network_code`: HTTP response status code of the onwards API call made by Integry.
* `output`: HTTP response body of the onwards API call made by Integry.

If Integry does not execute the function, it will respond with a `400 Bad Request` with following keys in the response body:

* `error`: Summary of the error.
* `error_details[]`: Detailed errors for individual fields (if applicable).

{% tabs %}
{% tab title="200" %}
{% code lineNumbers="true" %}
```json
// Function name: slack-passthrough-request
// GET https://slack.com/api/conversations.list?limit=2

{
    "network_code": "200",
    "output": {
        "ok": true,
        "channels": [
            {
                "id": "C6F3LQ03A",
                "name": "random",
                "is_channel": true,
                "is_group": false,
                "is_im": false,
                "is_mpim": false,
                "is_private": false,
                "created": 1501486653,
                "is_archived": false,
                "is_general": false,
                "unlinked": 0,
                "name_normalized": "random",
                "is_shared": false,
                "is_org_shared": false,
                "is_pending_ext_shared": false,
                "pending_shared": [],
                "context_team_id": "T6F74R6TB",
                "updated": 1724807678577,
                "parent_conversation": null,
                "creator": "U6GKMKPE2",
                "is_ext_shared": false,
                "shared_team_ids": [
                    "T6F74R6TB"
                ],
                "pending_connected_team_ids": [],
                "is_member": true,
                "topic": {
                    "value": "Non-work banter and water cooler conversation",
                    "creator": "U6GKMKPE2",
                    "last_set": 1501486653
                },
                "purpose": {
                    "value": "A place for non-work-related flimflam, faffing, hodge-podge or jibber-jabber you'd prefer to keep out of more focused work-related channels.",
                    "creator": "U6GKMKPE2",
                    "last_set": 1501486653
                },
                "properties": {
                    "tabs": [
                        {
                            "id": "files",
                            "label": "",
                            "type": "files"
                        }
                    ]
                },
                "previous_names": [],
                "num_members": 7
            },
            {
                "id": "C6GKMKRUN",
                "name": "general",
                "is_channel": true,
                "is_group": false,
                "is_im": false,
                "is_mpim": false,
                "is_private": false,
                "created": 1501486653,
                "is_archived": false,
                "is_general": true,
                "unlinked": 0,
                "name_normalized": "general",
                "is_shared": false,
                "is_org_shared": false,
                "is_pending_ext_shared": false,
                "pending_shared": [],
                "context_team_id": "T6F74R6TB",
                "updated": 1731095674264,
                "parent_conversation": null,
                "creator": "U6GKMKPE2",
                "is_ext_shared": false,
                "shared_team_ids": [
                    "T6F74R6TB"
                ],
                "pending_connected_team_ids": [],
                "is_member": true,
                "topic": {
                    "value": "Channel for high priority, company-wide announcements and work-related matters. If you want to banter please head over to <#C02D3JZA45T|> if you want to discuss low priority items head over to <#G01L3PW2A01|integry-internal>",
                    "creator": "U6FQESQ02",
                    "last_set": 1632860908
                },
                "purpose": {
                    "value": "This channel is for team-wide communication and announcements. All team members are in this channel.",
                    "creator": "U6GKMKPE2",
                    "last_set": 1501486653
                },
                "properties": {
                    "tabs": [
                        {
                            "id": "files",
                            "label": "",
                            "type": "files"
                        }
                    ]
                },
                "previous_names": [],
                "num_members": 14
            }
        ],
        "response_metadata": {
            "next_cursor": "dGVhbTpDOFBLNUhOOTU="
        }
    }
}
```
{% endcode %}
{% endtab %}

{% tab title="400" %}
```json
// Function name: slack-passthrough-request
// Outcome: Error -- app was not connected
{
    "error": "Could not call the function due to invalid input. Please see `error_details` for further information.",
    "error_details": [
        "User has not connected their Slack account. To connect an account, please call following SDK method: `connectApp('slack')`"
    ]
}
```
{% endtab %}
{% endtabs %}

### Make a passthrough request via SDK

`invokeFunction(<app_name>-passthrough-request, params, connectedAccountId)`

Integry will execute the function if the user has already connected their account for the function app, and the `method` and `URL` parameters are provided in the `params` object. These function calls will show in the Function Calls log in [the Integry app](https://app.integry.io/platform/functions/calls-log).

Integry will not execute the function if the user has not connected an account, or the parameters passed are invalid. These function calls will not show in the Function Calls log.

```javascript
const params = {
  method: "GET",
  url: "https://slack.com/api/conversations.list?limit=2"
};
integry.invokeFunction("slack-passthrough-request", params).then((result) => {
  console.log("Received response from Slack:", result);
}).catch((error) => {
  console.error("Failed to invoke function:", error);
});
```

#### Method parameters

<table><thead><tr><th width="140">Name</th><th width="83">Type</th><th width="319">Description</th><th width="129">Example</th><th>Required</th></tr></thead><tbody><tr><td><code>functionName</code></td><td>string</td><td>The name of the function to execute</td><td>slack-post-message</td><td>true</td></tr><tr><td><code>params</code></td><td>object</td><td>An object containing the function parameters.</td><td><p>{"method":"",</p><p>"url":"",</p><p>"body":""}</p></td><td>true</td></tr><tr><td><code>connectedAccountId</code></td><td>string</td><td>The connected account to use for executing the action. Only use if the user has connected multiple accounts.</td><td>43654</td><td>false</td></tr></tbody></table>

#### **Returns**

If Integry executes the function, this method returns a `result` object with following keys:

* `network_code`: HTTP response status code of the onwards API call made by Integry.
* `output`: HTTP response body of the onwards API call made by Integry.

If Integry does not execute the function, this method returns a `result` object with following keys:

* `error`: Summary of the error.
* `error_details[]`: Detailed errors for individual fields (if applicable).

{% tabs %}
{% tab title="Result" %}
{% code lineNumbers="true" %}
```json
// Function name: pipedrive-passthrough-request
// POST https://api.pipedrive.com/api/v2/persons
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

{% tab title="Error" %}
```json
// Function name: pipedrive-passthrough-request
// POST https://api.pipedrive.com/api/v2/persons
{
    "error": "Could not call the function due to invalid input. Please see `error_details` for further information.",
    "error_details": [
        "User has not connected their Pipedrive account. To connect an account, please call following SDK method: `connect('pipedrive')`"
    ]
}
```
{% endtab %}
{% endtabs %}

### List all passthrough request functions

<mark style="color:green;">`GET`</mark> `/functions?type=passthrough`

List all passthrough request functions supported by Integry. See [`/functions`](https://integry.gitbook.io/integry-docs/apis-and-sdks/api-reference#list-all-functions) for more options.
