---
description: >-
  This guide explains how to use Integry with Mistral AI to post a message on
  Slack.
---

# Mistral AI

1\. Install Required Libraries

First, you need to install the necessary packages:

{% hint style="info" %}
Integry requires Python version 3.12 or higher
{% endhint %}

* **Integry** enables seamless integration of structured tools and functions from over 300 apps
* **Mistral AI** offers state-of-the-art, open-weight models with full customization, enterprise-grade deployment, and seamless AI integration.

```python
pip install integry mistralai
```

## 2. Initialize Integry & Agent

Import the necessary Libraries

```python
from mistralai import Mistral
from integry import Integry
from integry import handle_mistralai_tool_calls
```

`user_id` is how you define users in your app or agent. By default, your email used during your Integry signup can act as a user\_id as well. Function Calls and Integrations are linked to this id.

For example:

```python
user_id = "joe@example.com" #replace with your email used during sign up
```

Below code snippet initializes the Integry class to interact with the Integry API using the App-Key and App-Secret.

You can view and copy your App-Key and App-Secret from the [Workspace Settings](https://app.integry.io/platform/workspace/security/).

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption><p>Workspace Settings</p></figcaption></figure>

To begin using Integry, you first set the App Key and App Secret as environment variables. Here is a quick way

```python
os.environ["INTEGRY_APP_KEY"] = "your_app_key_here"
os.environ["INTEGRY_APP_SECRET"] = "your_app_secret_here"
```

Initializing the Integry object

```python
integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)
```

Now retrieving the Mistral API Key from the enviroment. You can get the API Key from the [Mistral AI Console](https://console.mistral.ai/api-keys/)

```python
mistral_api_key = os.environ.get("MISTRAL_API_KEY")
```

Now that, we have the mistral api key, next step is to initialize the mistral client and the model we will be using to process and generate responses.&#x20;

```python
model = "mistral-large-latest"
client = Mistral(api_key=mistral_api_key)
```

## 3. Register the Integry Function as a Tool

Perfect! Before you can use the functions available in Integry, you need to add the app to Integry. Slack, however, is pre-added to your Integry account, so there’s no need to add it manually.

To enable the assistant to call the function, we register it with the Mistral AI agents. Now that everything is set up, we will send a message in Slack using the Integry slack-post-message function.

```python
slack_post_message = await integry.functions.get("slack-post-message", user_id)

messages = [{"role": "user", "content": "Say hello to my team on slack."}]

response = await client.chat.complete_async(
    model=model,
    messages=messages,
    tools=[slack_post_message.get_mistralai_tool()],
    tool_choice="auto"
)
```

## 4. **Connect Your Slack Account**

To allow the agent to send a message on Slack on your user's behalf, the user must connect their Slack account. To connect a Slack account against the provided user ID, execute the following snippet.

```python
slack = await integry.apps.get("slack", user_id)
print(slack.login_url)
```

This will print a URL which can be opened in a web browser to connect Slack.

## 5. Execute Agent

This will execute the agent and send a **Hello** message to the Slack channel.

```python
await handle_mistralai_tool_calls(response, user_id, [slack_post_message])
```

This will send the message to the slack channel. Here is reference image.

The message has been sent successfully in slack #random channel. You can verify the successful message delivery by checking the highlighted content in the response below.

<figure><img src="../../.gitbook/assets/image (93).png" alt=""><figcaption></figcaption></figure>

<pre class="language-python" data-overflow="wrap" data-full-width="true"><code class="lang-python">FunctionCallOutput(
    <a data-footnote-ref href="#user-content-fn-1">network_code=200,</a>
    output={
        'ok': True,
        'channel': 'C086GCY1J9E',
        'ts': '1742201773.841839',
        'message': {
            'user': 'U086GBQHLG0',
            'type': 'message',
            'ts': '1742201773.841839',
            'bot_id': 'B086E311JTB',
            'app_id': 'A6FQL4KQC',
            'text': 'Hello team!',
            'team': 'T086682UW57',
            'bot_profile': {
                'id': 'B086E311JTB',
                'app_id': 'A6FQL4KQC',
                'name': 'Integry',
                'icons': {
                    'image_36': 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/..._36.png',
                    'image_48': 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/..._48.png',
                    'image_72': 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/..._72.png'
                },
                'deleted': False,
                'updated': 1734709233,
                'team_id': 'T086682UW57'
            },
            'blocks': [
                {
                    'type': 'rich_text',
                    'block_id': 'e61a',
                    'elements': [
                        {
                            'type': 'rich_text_section',
                            'elements': [
                                {'type': 'text', 'text': 'Hello team!'}
                            ]
                        }
                    ]
                }
            ]
        }
    }
)

</code></pre>

[^1]: This success response show's that message has been sent successfully in slack channel.
