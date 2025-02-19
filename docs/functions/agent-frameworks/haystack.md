---
description: >-
  This guide explains how to use Integry with Haystack to post a message on
  Slack.
---

# Haystack

## 1. Install Required Libraries

First, you need to install the necessary packages:

{% hint style="info" %}
Integry requires Python version 3.12 or higher
{% endhint %}

* **Integry** enables seamless integration of structured tools and functions from over 300 apps
* **Haystack** is AI orchestration framework to build customizable, production-ready LLM applications.

```python
pip install integry farm-haystack
```

## 2. Initialize Integry & Agent

Import the necessary Libraries

```python
import os
from integry import Integry
from haystack.components.generators.chat import OpenAIChatGenerator
from haystack.dataclasses import ChatMessage
from haystack.components.tools import ToolInvoker
from haystack.tools import Tool
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

Now retrieving the Open AI API Key from the enviroment. You can get the API Key from the [OpenAI Platform](https://platform.openai.com/api-keys)

```python
os.environ.get("OPENAI_API_KEY")
```

## 3. Register the Integry Function as a Tool

Perfect! Before you can use the functions available in Integry, you need to add the app to Integry. Slack, however, is pre-added to your Integry account, so there’s no need to add it manually.

To enable the assistant to call the function, we register it with the Haystack agents. Now that everything is set up, we will send a message in Slack using the Integry slack-post-message function.

```python
slack_post_message = await integry.functions.get("slack-post-message", user_id)

tool = slack_post_message.get_haystack_tool(Tool, user_id)

chat_generator = OpenAIChatGenerator(model="gpt-4o-mini", tools=[tool])

tool_invoker = ToolInvoker(tools=[tool])
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
user_message = ChatMessage.from_user("Say hello to my team on slack.")

replies = chat_generator.run(messages=[user_message])["replies"]

if replies[0].tool_calls:
    tool_messages = tool_invoker.run(messages=replies)["tool_messages"]
    print(f"tool messages: {tool_messages}")
```

This will send the message to the slack channel. Here is reference image.

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

The message has been sent successfully in slack #random channel. You can verify the successful message delivery by checking the highlighted content in the response below.

<pre data-overflow="wrap"><code>tool messages: [ChatMessage(_role=&#x3C;ChatRole.TOOL: 'tool'>, <a data-footnote-ref href="#user-content-fn-1">_content=[ToolCallResult(result='network_code=200 </a>output={\'ok\': True, \'channel\': \'C086GCY1J9E\', \'ts\': \'1739183566.488729\', \'message\': {\'user\': \'U086GBQHLG0\', \'type\': \'message\', \'ts\': \'1739183566.488729\', \'bot_id\': \'B086E311JTB\', \'app_id\': \'A6FQL4KQC\', \'text\': "Hello team! Hope you\'re all having a great day!", \'team\': \'T086682UW57\', \'bot_profile\': {\'id\': \'B086E311JTB\', \'app_id\': \'A6FQL4KQC\', \'name\': \'Integry\', \'icons\': {\'image_36\': \'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-08-09/225182834294_8020ddc74d7822b48ea1_36.png\', \'image_48\': \'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-08-09/225182834294_8020ddc74d7822b48ea1_48.png\', \'image_72\': \'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-08-09/225182834294_8020ddc74d7822b48ea1_72.png\'}, \'deleted\': False, \'updated\': 1734709233, \'team_id\': \'T086682UW57\'}, \'blocks\': [{\'type\': \'rich_text\', \'block_id\': \'WiFT\', \'elements\': [{\'type\': \'rich_text_section\', \'elements\': [{\'type\': \'text\', \'text\': "Hello team! Hope you\'re all having a great day!"}]}]}]}}', origin=ToolCall(tool_name='slack-post-message', arguments={'channel': '#random', 'text': "Hello team! Hope you're all having a great day!"}, id='call_oaaLsi9pxAoPUrH7cjH8Mp8t'), error=False)], _name=None, _meta={})]
</code></pre>

[^1]: This success response show's that message has been sent successfully in slack channel.
