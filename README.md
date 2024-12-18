# Integry

Access [Integry REST API](https://docs.integry.ai/apis-and-sdks/api-reference) from JS/TS or Python programs.

# Get Started with Python

## 1. Installation

```bash
# install from PyPI
pip install integry
```

## 2. Usage with Agent Frameworks

### 1. LangChain/LangGraph

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

tool = slack_post_message.get_langchain_tool(StructuredTool.from_function, user_id)

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

### 2. CrewAI

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
    slack_post_message.get_langchain_tool(CrewStructuredTool.from_function, user_id)
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

### 3. AutoGen

```python
import os
from integry import Integry
from autogen import ConversableAgent, register_function

user_id = "your user's ID"

# Initialize the client
integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)

function = await integry.functions.get("slack-post-message", user_id)

llm_config = {"config_list": [{"model": "gpt-4o", "api_key": os.environ.get("OPENAI_API_KEY")}]}

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

function.register_with_autogen_agents(
    register_function,
    caller=assistant,
    executor=user_proxy,
    user_id=user_id,
)

chat_result = await user_proxy.a_initiate_chat(
    assistant,
    message="Say hello to my team on slack",
)
```

## 3. Prediction

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

# Get Started with NodeJS

## 1. Installation

```bash
# install from npm
npm install integry
```

## Usage

```bash
const integry = require('integry');

const sdk = new integry({ appKey: 'YOUR_INTEGRY_APP_KEY', appSecret: 'YOUR_INTEGRY_APP_SECRET' });
const functions = await sdk.functions.list({
    user_id: 'YOUR APPS USER ID'
});
console.log(functions);
```

## Run tests

```bash
npm install --save-dev jest ts-jest @types/jest typescript
npx ts-jest config:init
npx jest
```
