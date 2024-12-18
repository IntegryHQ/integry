# AutoGen

## Post a message on Slack using Integry and LangChain/LangGraph

## 1. Install Integry

```bash
pip install integry
```

## 2. Initialize Agent

```python
import os
from integry import Integry
from autogen import ConversableAgent, register_function

user_id = "your user's ID"

integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)

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
```

## 3. Register an Integry Function as a Tool

```python
function = await integry.functions.get("slack-post-message", user_id)

function.register_with_autogen_agents(
    register_function,
    caller=assistant,
    executor=user_proxy,
    user_id=user_id,
)
```

## 4. Execute Agent

```python
chat_result = await user_proxy.a_initiate_chat(
    assistant,
    message="Say hello to my team on slack",
)
```
