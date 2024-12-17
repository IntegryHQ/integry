# Integry Python API Library

[![PyPI version](https://img.shields.io/pypi/v/integry.svg)](https://pypi.org/project/integry/)

The Python API library allows access to [Integry REST API](https://docs.integry.ai/apis-and-sdks/api-reference) from Python programs.

# Installation

```bash
# install from PyPI
pip install integry
```

# Usage with Agent Frameworks

## 1. LangChain/LangGraph

```python
import os
from integry import Integry
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import StructuredTool
from langgraph.prebuilt import create_react_agent

user_id = "your user's ID"

# Initialize the client
integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)

slack_post_message = await integry.functions.get("slack-post-message", user_id)

llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.environ.get("OPENAI_API_KEY"),
)

tool = slack_post_message.as_langchain_tool(StructuredTool.from_function, user_id)

agent = create_react_agent(
    tools=[tool],
    model=llm,
)

await agent.ainvoke({
    "messages": [
        SystemMessage(content="You are a helpful assistant"),
        HumanMessage(content="Say hello to my team on slack"),
    ]
})

```

## 2. CrewAI

```python
import os
from integry import Integry
from crewai import Agent, Task, Crew, LLM
from crewai.tools.structured_tool import CrewStructuredTool

user_id = "your user's ID"

# Initialize the client
integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)

slack_post_message = await integry.functions.get("slack-post-message", user_id)

tools = [
    slack_post_message.as_langchain_tool(CrewStructuredTool.from_function, user_id)
]

llm = LLM(
    model="gpt-4o",
    temperature=0,
    base_url="https://api.openai.com/v1",
    api_key=os.environ.get("OPENAI_API_KEY"),
)

crewai_agent = Agent(
    role="Integration Assistant",
    goal="Help users achieve their goal by performing their required task in various apps",
    backstory="You are a virtual assistant with access to various apps and services. You are known for your ability to connect to any app and perform any task.",
    verbose=True,
    tools=tools,
    llm=llm,
)

task = Task(
    description="Say hello to my team on slack",
    agent=crewai_agent,
    expected_output="Result of the task",
)

crew = Crew(agents=[crewai_agent], tasks=[task])

result = crew.kickoff()
```

# Prediction
```python
import os
from integry import Integry

user_id = "your user's ID"

# Initialize the client
integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)

# Get the most relevant function
predictions = await integry.functions.predict(
    prompt="say hello to my team on Slack", user_id=user_id, predict_arguments=True
)

if predictions:
    function = predictions[0]
    # Call the function
    await function(user_id, function.arguments)
```

# Pagination
List methods are paginated and allow you to iterate over data without handling pagination manually.
```python
from integry import Integry

user_id = "your user's ID"

integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)

async for function in integry.functions.list(user_id):
    # do something with function
    print(function.name)
```

If you want to control pagination, you can fetch individual pages by using the `cursor` returned by the previous page.
```python
from integry import Integry

user_id = "your user's ID"

integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)

first_page = await integry.apps.list(user_id)

second_page = await integry.apps.list(user_id, cursor=first_page.cursor)
```
