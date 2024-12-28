---
description: >-
  This guide will walk you through the process of setting up and using Integry
  and CrewAI to post a message on Slack.
---

# CrewAI

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

## 2. Initialize Integry & LLM

Install and Import the necessary Libraries

```python
pip install crewai
```

```python
import os
from integry import Integry
from crewai import Agent, Task, Crew, LLM
from crewai.tools.structured_tool import CrewStructuredTool
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

Perfect! Now that we've set everything up, we will proceed to send a message in Slack using the Integry **slack-post-message** function.

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

## 4. **Connect Your Slack Account (Required for First-Time Users)**

To allow the agent to send a message on Slack on your user's behalf, the user must connect their Slack account. To connect a Slack account against the provided user ID, execute the following snippet.

```python
slack = await integry.apps.get("slack", user_id)
print(slack.login_url)
```

This will print a URL which can be opened in a web browser to connect Slack.

## 5. Execute Agent

```python
task = Task(
    description="Say hello to my team on slack",
    agent=crewai_agent,
    expected_output="Result of the task",
)

crew = Crew(agents=[crewai_agent], tasks=[task])

result = crew.kickoff()
```
