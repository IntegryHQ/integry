---
description: >-
  This guide will walk you through the process of setting up and using Integry
  and CrewAI to post a message on Slack.
---

# CrewAI

## 1. Install Required Libraries

First, you need to install the necessary packages:

{% hint style="info" %}
Integry requires Python version 3.12 or higher
{% endhint %}

* **Integry** is used to integrate structured tools and functions.
* **CrewAI** integrate tools and automate workflows using large language models.

```python
pip install integry crewai
```

## 2. Initialize Integry & Agent

Import the necessary Libraries

```python
import os
from integry import Integry
from crewai import Agent, Task, Crew, LLM
from crewai.tools.structured_tool import CrewStructuredTool
```

`User-ID` is a unique string identifier for a user in your app or agent. Function Calls and Integrations are associated to a user ID. It will be the email address you used during the signup process on Integry.

For example:

```python
user_id = "joe@example.com"
```

Below code snippet initializes the **Integry** class to interact with the Integry API using the **App-Key** and **App-Secret**.&#x20;

You can view and copy your `App-Key` and `App-Secret` from the [Workspace Settings](https://app.integry.io/wapp/settings/embed/).

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption><p>Workspace Setting</p></figcaption></figure>

```python
integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)
```

Now initializing the instance of the **ChatOpenAI** class to interact with OpenAI's GPT-4o model. You can get the API Key from the [OpenAI Platform](https://platform.openai.com/api-keys)

```python
llm = LLM(
    model="gpt-4o",
    temperature=0,
    base_url="https://api.openai.com/v1",
    api_key=os.environ.get("OPENAI_API_KEY"),
)
```

## 3. Initialize Agent with an Integry Function as a Tool

Perfect! Before you can use the functions available in Integry, you need to add the app to Integry. Slack, however, is pre-added to Integry by default, so there’s no need to add it manually.&#x20;

Now that we've set everything up, we will proceed to send a message in Slack using the **slack-post-message** function from [Integry](https://app.integry.io/platform/functions). You can copy the function ID from the dropdown.&#x20;

For example

In this case the function ID is <mark style="color:blue;">slack-post-message</mark>

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

After getting the function ID,  we then registers it with the Crew AI agents to enable the assistant to call the function.

```python
slack_post_message = await integry.functions.get("slack-post-message", user_id)

tools = [
    slack_post_message.get_langchain_tool(CrewStructuredTool.from_function, user_id)
]

crewai_agent = Agent(
    role="Integration Assistant",
    goal="Help users achieve their goal by performing their required task in various apps",
    backstory="You are a virtual assistant with access to various apps and services. You are known for your ability to connect to any app and perform any task.",
    verbose=True,
    tools=tools,
    llm=llm,
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

This will execute the agent and send a **Hello from crewai to the team** message in the Slack random channel.

```python
task = Task(
    description="Say hello from crewai to my team on slack in #random channel.",
    agent=crewai_agent,
    expected_output="Result of the task",
)

crew = Crew(agents=[crewai_agent], tasks=[task])

result = crew.kickoff()
```
