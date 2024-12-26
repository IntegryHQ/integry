---
description: Post a message on Slack using Integry and CrewAI
---

# CrewAI

## 1. Install Integry

```bash
pip install integry
```

## 2. Initialize Integry & LLM

```python
import os
from integry import Integry
from crewai import Agent, Task, Crew, LLM
from crewai.tools.structured_tool import CrewStructuredTool

user_id = "your user's ID"

integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)

llm = LLM(
    model="gpt-4o",
    temperature=0,
    base_url="https://api.openai.com/v1",
    api_key=os.environ.get("OPENAI_API_KEY"),
)
```

## 3. Initialize Agent with an Integry Function as a Tool

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

## 4. Connect your Slack account (skip if you already connected your Slack account)

To connect your Slack account, execute the following snippet. This will print a URL which you can open in your browser to connect your Slack account.

```python
slack = await integry.apps.get("slack", user_id)
print(slack.login_url)
```

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
