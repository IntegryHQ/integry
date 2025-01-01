---
icon: forward
---

# Try Functions in 60 seconds

In this guide, we will use the [Integry Marketplace](../embedded-ui/embed-integry-apps-marketplace.md) and the [Integry Functions API](../apis-and-sdks/api-reference.md) to connect an app and call a function of that app.

Before you proceed, please [sign up](https://app.integry.io/accounts/register/v3/signup/?product=functions) for a free trial (if you haven't).

### Connect an app (as a user)

{% stepper %}
{% step %}
Go to **Apps** and click the **Access as a User** button in the Integry app.

You are accessing the marketplace as a user of your app. Later, once your users have connected apps (and setup integrations), you can impersonate them here if you need to debug and/or fix.
{% endstep %}

{% step %}
Click **Slack** and connect your account.

You can also connect a different app if you don't use Slack.
{% endstep %}
{% endstepper %}

### Copy the function call cURL

{% stepper %}
{% step %}
Go **Function Calls** and click **Public Functions**.&#x20;

You can also pick a different app if you don't use Slack.
{% endstep %}

{% step %}
Search for **Post Message** on **Slack**.

If you chose a different app, pick any function you're familiar with.
{% endstep %}

{% step %}
Click the copy button (to copy the cURL).

This will include your [authentication](../apis-and-sdks/api-reference.md#authentication) variables.
{% endstep %}
{% endstepper %}

### Call the function from a tool like Postman



{% stepper %}
{% step %}
[Setup Postman](https://learning.postman.com/docs/getting-started/first-steps/get-postman/) (if you haven't) and select **+** in the workbench to open a new [tab](https://learning.postman.com/docs/getting-started/basics/navigating-postman/#tabs).
{% endstep %}

{% step %}
Paste the cURL in the URL field. It should automatically fill in the URL, Headers and Body.
{% endstep %}

{% step %}
Click **Send**. You will see the response from Integry in the pane below.

```json
{
    "error": "Could not call the function due to invalid input. Please see `error_details` for further information.",
    "error_details": {
        "channel": "This parameter is required and must not be null or empty",
        "text": "This parameter is required and must not be null or empty"
    }
}
```
{% endstep %}

{% step %}
To fix that, toggle to the request **Body** tab, click Beautify to make it easy to read, fill in the `channel` and `text` parameters, and click **Send** again.
{% endstep %}
{% endstepper %}

Voila! If the response from Integry looks like the sample below, open Slack to see the message you just posted by calling an Integry Function. You can also [see the call you just made](../functions/viewing-function-calls.md) in the Function Calls tab in the Integry app.

```json
{
    "network_code": "200",
    "output": {
        "ok": true,
        "channel": "C6F3LQ03A",
        "ts": "1731965527.026429",
        "message": {
            "user": "U02L42QCVGV",
            "type": "message",
            "ts": "1731965527.026429",
            "bot_id": "B0447TKCF1N",
            "app_id": "A6FQL4KQC",
            "text": "Hello from Postman!",
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
                    "block_id": "dxA",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "Hello from Postman!"
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

### Next steps

Try fetching data using a function like `pipedrive-get-all-persons` . It supports paginated calls so the result will include a `next_page` cursor that you will include in the arguments in the next call.
