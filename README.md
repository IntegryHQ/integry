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
    app_key=os.environ.get("INTEGRY_APP_SECRET"),
    app_secret=os.environ.get("INTEGRY_APP_KEY"),
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

## 3. Prediction

```python
import os
from integry import Integry

user_id = "your user's ID"

# Initialize the client
integry = Integry(
    app_secret=os.environ.get("INTEGRY_APP_KEY"),
    app_key=os.environ.get("INTEGRY_APP_SECRET"),
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
