# LangChain/LangGraph

## Post a message on Slack using Integry and LangChain/LangGraph

## 1. Install Integry

```bash
pip install integry
```

## 2. Initialize Integry & LLM

```python
import os
from integry import Integry
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import StructuredTool
from langgraph.prebuilt import create_react_agent

user_id = "your user's ID"

integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)

llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.environ.get("OPENAI_API_KEY"),
)
```

## 3. Register an Integry Function as a Tool

```python
slack_post_message = await integry.functions.get("slack-post-message", user_id)

tool = slack_post_message.get_langchain_tool(StructuredTool.from_function, user_id)

agent = create_react_agent(
    tools=[tool],
    model=llm,
)
```

## 4. Execute Agent

```python
await agent.ainvoke({
    "messages": [
        SystemMessage(content="You are a helpful assistant"),
        HumanMessage(content="Say hello to my team on slack"),
    ]
})
```
