---
description: >-
  This guide explains how to use Integry with Smolagent to post a message on
  Slack.
---

# Smolagent

## 1. Install Required Libraries

First, you need to install the necessary packages:

{% hint style="info" %}
Integry requires Python version 3.12 or higher
{% endhint %}

* **Integry** enables seamless integration of structured tools and functions from over 300 apps
* **SmolAgents** integrates tools and automates workflows using large language models, enabling powerful agents in just a few lines of code.

```python
pip install integry smolagents
```

## 2. Initialize Integry & Agent

Import the necessary Libraries

```python
import os
from smolagents import tool, CodeAgent, HfApiModel
from integry import Integry
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

Now initializing the HuggingFace Instance. You can get the Access Token from the  [HuggingFace Platform](https://huggingface.co/settings/tokens)

```python
hugging_face_token = os.environ.get("HUGGING_FACE_TOKEN")
```

## 3. Register the Integry Function as a Tool

Perfect! Before you can use the functions available in Integry, you need to add the app to Integry. Slack, however, is pre-added to your Integry account, so there’s no need to add it manually.&#x20;

To enable the assistant to call the function, we register it with the SmolAgents framework. Now that everything is set up, we will send a message in Slack using the Integry slack-post-message function.

```python
slack_post_message = await integry.functions.get("slack-post-message", user_id)

slack_tool = slack_post_message.get_smolagent_tool(tool, user_id)

agent = CodeAgent(tools=[slack_tool], model=HfApiModel(token=hugging_face_token))
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
agent.run("Say hello to my team on slack.")
```

This will send the message to the slack channel. Here is reference image.

<figure><img src="../../.gitbook/assets/image (92).png" alt=""><figcaption></figcaption></figure>

The message has been sent successfully in slack #random channel. You can verify the successful message delivery by checking the highlighted content in the response below.

<pre><code>╭──────────────────────────────────────────────────────────────── New run ────────────────────────────────────────────────────────────────╮
│                                                                                                                                         │
│ Say hello to my team on slack in #alert channel.                                                                                        │
│                                                                                                                                         │
╰─ HfApiModel - Qwen/Qwen2.5-Coder-32B-Instruct ──────────────────────────────────────────────────────────────────────────────────────────╯
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 0 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ─ Executing this code: ────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  execute_function(channel="#alert", text="Hello to my team!")                                                                             
 ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
<strong><a data-footnote-ref href="#user-content-fn-1">Out: network_code=200 output={'ok': True, </a>'channel': 'C086GCY1J9E', 'ts': '1738671240.917739', 'message': {'user': 'U086GBQHLG0', 'type': 
</strong>'message', 'ts': '1738671240.917739', 'bot_id': 'B086E311JTB', 'app_id': 'A6FQL4KQC', 'text': 'Hello to my team!', 'team': 'T086682UW57',  
'bot_profile': {'id': 'B086E311JTB', 'app_id': 'A6FQL4KQC', 'name': 'Integry', 'icons': {'image_36':
'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-08-09/225182834294_8020ddc74d7822b48ea1_36.png', 'image_48':
'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-08-09/225182834294_8020ddc74d7822b48ea1_48.png', 'image_72':
'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-08-09/225182834294_8020ddc74d7822b48ea1_72.png'}, 'deleted': False,
'updated': 1734709233, 'team_id': 'T086682UW57'}, 'blocks': [{'type': 'rich_text', 'block_id': 'Bsr', 'elements': [{'type':
'rich_text_section', 'elements': [{'type': 'text', 'text': 'Hello to my team!'}]}]}]}}
[Step 0: Duration 3.79 seconds| Input tokens: 2,470 | Output tokens: 46]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ─ Executing this code: ────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
  final_answer("Message sent to #alert channel: Hello to my team!")                                                                        
 ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
Out - Final answer: Message sent to #alert channel: Hello to my team!
[Step 1: Duration 4.22 seconds| Input tokens: 5,551 | Output tokens: 101]
</code></pre>

[^1]: This success response show's that message has been sent successfully in slack channel.
