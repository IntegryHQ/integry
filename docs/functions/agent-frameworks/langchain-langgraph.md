---
description: >-
  This guide explains how to use Integry with LangChain/LangGraph to post a
  message on Slack.
---

# LangChain/LangGraph

We can utilize LangChain agents with `ChatAnthropicExperimental`, `ChatCohere`, `ChatFireworks`, `ChatMistralAI`, and `ChatOpenAI`. However, at present, creating agents using Langchain with `ChatGoogleGenerativeAI (Gemini)` is not supported.

## 1. Install Required Libraries

First, you need to install the necessary packages:

{% hint style="info" %}
Integry requires Python version 3.12 or higher
{% endhint %}

* **Integry** is used to integrate structured tools and functions.
* **LangChain** to interact with OpenAI models and integrate structured tools.
* **LangGraph** to create the agent and use the tools.
* **langchain\_openai** to interact with OpenAI’s GPT models.

```python
pip install integry langchain langgraph langchain_openai
```

## 2. Initialize Integry & LLM

Import the necessary Libraries

```python
import os
from integry import Integry
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import StructuredTool
from langgraph.prebuilt import create_react_agent
```

`User-ID` is a unique string identifier for a user in your app or agent. Function Calls and Integrations are associated to a user ID. It will be the email address you used during the signup process on Integry.

For example:

```python
user_id = "joe@example.com"
```

Below code snippet initializes the **Integry** class to interact with the Integry API using the **App-Key** and **App-Secret**.

You can view and copy your `App-Key` and `App-Secret` from the [Workspace Settings](https://app.integry.io/platform/workspace/security/).

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption><p>Workspace Setting</p></figcaption></figure>

```python
integry = Integry(
    app_key=os.environ.get("INTEGRY_APP_KEY"),
    app_secret=os.environ.get("INTEGRY_APP_SECRET"),
)
```

Now initializing the instance of the **ChatOpenAI** class to interact with OpenAI's GPT-4o model. You can get the API Key from the [OpenAI Platform](https://platform.openai.com/api-keys)

```python
llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.environ.get("OPENAI_API_KEY"),
)
```

## 3. Register the Integry Function as a Tool

Perfect! Before you can use the functions available in Integry, you need to add the app to Integry. Slack, however, is pre-added to Integry by default, so there’s no need to add it manually.

Now that we've set everything up, we will proceed to send a message in Slack using the Integry **slack-post-message** function. from [Integry](https://app.integry.io/platform/functions). You can copy the function ID from the dropdown.

For example

In this case the function ID is <mark style="color:blue;">slack-post-message</mark>

<figure><img src="../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

After getting the function ID, we then registers it with the Langchain agents to enable the assistant to call the function.

* **Create the LangChain Tool**: Convert the Integry function into a LangChain tool using `get_langchain_tool`.
* **Set Up the Agent**: Create an agent with LangGraph that uses the tool and LLM to post messages to Slack.

```python
slack_post_message = await integry.functions.get("slack-post-message", user_id)

tool = slack_post_message.get_langchain_tool(StructuredTool.from_function, user_id)

agent = create_react_agent(
    tools=[tool],
    model=llm,
)
```

<figure><img src="../../.gitbook/assets/download.png" alt=""><figcaption><p>Agent</p></figcaption></figure>

## 4. **Connect Your Slack Account**

To allow the agent to send a message on Slack on your user's behalf, the user must connect their Slack account. To connect a Slack account against the provided user ID, execute the following snippet.

```python
slack = await integry.apps.get("slack", user_id)
print(slack.login_url)
```

This will print a URL which can be opened in a web browser to connect Slack.

## 5. Execute Agent

This will execute the agent and send a **Hello** message to the Slack channel, if you want to be more specific to channel you can have a content like <mark style="color:blue;">Say hello to my team on Slack in the</mark> <mark style="color:blue;">**#random**</mark> <mark style="color:blue;">channel.</mark>

```python
await agent.ainvoke({
    "messages": [
        SystemMessage(content="You are a helpful assistant"),
        HumanMessage(content="Say hello to my team on slack"),
    ]
})
```

This will send the message to the slack channel. Here is reference image

<figure><img src="../../.gitbook/assets/image (88).png" alt=""><figcaption></figcaption></figure>

You can verify the successful message delivery by checking the highlighted content in the response, which indicates that the message was successfully sent.

**Sample Response**

<pre class="language-json" data-overflow="wrap" data-line-numbers><code class="lang-json">{
    "messages": [
        SystemMessage(
            content="You are a helpful assistant",
            additional_kwargs={},
            response_metadata={},
            id="4959b138-dae2-4a7e-b5b0-d211907be810",
        ),
        HumanMessage(
            content="Say hello to my team on slack in #alert channel",
            additional_kwargs={},
            response_metadata={},
            id="0b325592-1460-456e-b515-d392cbe07481",
        ),
        AIMessage(
            content="",
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "call_sKyJ5MgqxvFxZwquTP0aIAeB",
                        "function": {
                            "arguments": '{"channel":"#alert","text":"Hello Team!"}',
                            "name": "slack-post-message",
                        },
                        "type": "function",
                    }
                ],
                "refusal": None,
            },
            response_metadata={
                "token_usage": {
                    "completion_tokens": 24,
                    "prompt_tokens": 503,
                    "total_tokens": 527,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-4o-2024-08-06",
                "system_fingerprint": "fp_5f20662549",
                "finish_reason": "tool_calls",
                "logprobs": None,
            },
            id="run-a0acabb8-a818-422c-ba7d-44485ab37a39-0",
            tool_calls=[
                {
                    "name": "slack-post-message",
                    "args": {"channel": "#alert", "text": "Hello Team!"},
                    "id": "call_sKyJ5MgqxvFxZwquTP0aIAeB",
                    "type": "tool_call",
                }
            ],
            usage_metadata={
                "input_tokens": 503,
                "output_tokens": 24,
                "total_tokens": 527,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
<strong><a data-footnote-ref href="#user-content-fn-1">        </a>ToolMessage(
</strong><strong>            content="network_code=200 output={'ok': True, 'channel': 'C086GCY1J9E', 'ts': '1735231007.530469', 'message': {'user': 'U086GBQHLG0', 'type': 'message', 'ts': '1735231007.530469', 'bot_id': 'B086E311JTB', 'app_id': 'A6FQL4KQC', 'text': 'Hello Team!', 'team': 'T086682UW57', 'bot_profile': {'id': 'B086E311JTB', 'app_id': 'A6FQL4KQC', 'name': 'Integry', 'icons': {'image_36': 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-08-09/225182834294_8020ddc74d7822b48ea1_36.png', 'image_48': 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-08-09/225182834294_8020ddc74d7822b48ea1_48.png', 'image_72': 'https://slack-files2.s3-us-west-2.amazonaws.com/avatars/2017-08-09/225182834294_8020ddc74d7822b48ea1_72.png'}, 'deleted': False, 'updated': 1734709233, 'team_id': 'T086682UW57'}, 'blocks': [{'type': 'rich_text', 'block_id': 'ryD', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'Hello Team!'}]}]}]}}",
</strong>            name="slack-post-message",
            id="33c5541e-5b0a-4bb5-b342-8e13b683d2b9",
            tool_call_id="call_sKyJ5MgqxvFxZwquTP0aIAeB",
        ),
        AIMessage(
            content="I've said hello to your team in the #alert channel on Slack!",
            additional_kwargs={"refusal": None},
            response_metadata={
                "token_usage": {
                    "completion_tokens": 16,
                    "prompt_tokens": 912,
                    "total_tokens": 928,
                    "completion_tokens_details": {
                        "accepted_prediction_tokens": 0,
                        "audio_tokens": 0,
                        "reasoning_tokens": 0,
                        "rejected_prediction_tokens": 0,
                    },
                    "prompt_tokens_details": {"audio_tokens": 0, "cached_tokens": 0},
                },
                "model_name": "gpt-4o-2024-08-06",
                "system_fingerprint": "fp_d28bcae782",
                "finish_reason": "stop",
                "logprobs": None,
            },
            id="run-c5ce9372-0ea2-491b-93ce-48fab45926cc-0",
            usage_metadata={
                "input_tokens": 912,
                "output_tokens": 16,
                "total_tokens": 928,
                "input_token_details": {"audio": 0, "cache_read": 0},
                "output_token_details": {"audio": 0, "reasoning": 0},
            },
        ),
    ]
}

</code></pre>

[^1]: This success response show's that message has been sent successfully in slack channel.
