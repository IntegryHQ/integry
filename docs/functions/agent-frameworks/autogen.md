---
description: >-
  This guide will walk you through the process of setting up and using Integry
  and AutoGen to post a message on Slack.
---

# AutoGen

## 1. Install Integry

To work with Integry using python, you have to install using the latest version.

To check for the latest versions, you can visit the Integry Python package on the [Integry PyPI page](https://pypi.org/project/integry/#history) and install it using the following command:

```python
pip install integry==<version number>
```

For example, to install version 0.0.7:

```python
pip install integry==0.0.7
```

## 2. Initialize Integry & Agent

Install and Import the necessary Libraries

```python
pip install autogen
```

```python
import os
from integry import Integry
from autogen import ConversableAgent, register_function
```

`User-ID` is a unique string identifier for a user in your app. Function Calls and Integrations are associated to a user ID.

{% hint style="info" %}
If your app has workspaces/accounts and you want integrations to be shared across all users in a workspace/account, use the workspace/account ID as the user ID.
{% endhint %}

To get the user ID, visit the Team Management section in [settings](https://app.integry.io/wapp/settings/users/) and navigate to the **Team** section, where you'll find the **Name** and **Email** of the user. The **Email** serves as the **user ID** for making API calls.

```
user_id = "your user's ID"
```

For example:

```python
user_id = "nash@example.com"
```

Below code snippet initializes the **Integry** class to interact with the Integry API using the **App-Key** and **App-Secret**.&#x20;

You can view and copy your `App-Key` and `App-Secret` from [your workspace setting](https://app.integry.io/wapp/settings/embed/).

```python
integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)
```

The code creates two AI agents: one is "Assistant" that helps perform tasks, and another is "User" that listens for a **TERMINATE** message to stop. The assistant uses an API key for GPT-4 You can get the API Key from the [OpenAI Platform](https://platform.openai.com/api-keys), while the user agent has a rule to stop when it receives the "TERMINATE" message.

<pre class="language-python"><code class="lang-python"><strong>llm_config = {"config_list": [{"model": "gpt-4o", "api_key": os.environ.get("OPENAI_API_KEY")}]}
</strong>
assistant = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful integrations assistant. "
    "You can help users perform tasks in various apps. "
    "Return 'TERMINATE' when the task is done.",
    llm_config=llm_config,
)

user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None
    and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)
</code></pre>

## 3. Register an Integry Function as a Tool

The code retrieves a Slack post-message function from Integry, then registers it with the AI agents to enable the assistant to call the function.

<pre class="language-python"><code class="lang-python">function = await integry.functions.get("slack-post-message", user_id)
<strong>
</strong>function.register_with_autogen_agents(
    register_function,
    caller=assistant,
    executor=user_proxy,
    user_id=user_id,
)
</code></pre>

## 4. **Connect Your Slack Account (Required for First-Time Users)**

To allow the agent to send a message on Slack on your user's behalf, the user must connect their Slack account. To connect a Slack account against the provided user ID, execute the following snippet.

```python
slack = await integry.apps.get("slack", user_id)
print(slack.login_url)
```

This will print a URL which can be opened in a web browser to connect Slack.

## 5. Execute Agent

```python
chat_result = await user_proxy.a_initiate_chat(
    assistant,
    message="Say hello to my team on slack",
)
```
