import json
from typing import Any, TypedDict, Optional
from integry.resources.functions.types import Function, FunctionCallOutput

FunctionCall = TypedDict("FunctionCall", {"name": str, "arguments": str})

ToolCall = TypedDict("ToolCall", {"function": FunctionCall, "id": str, "type": str})

Message = TypedDict(
    "Message",
    {"role": str, "content": Optional[str], "tool_calls": Optional[list[ToolCall]]},
)

Choice = TypedDict(
    "Choice",
    {"index": int, "message": Message, "finish_reason": str},
)

LiteLLMResponse = TypedDict(
    "LiteLLMResponse",
    {
        "id": str,
        "created": int,
        "model": str,
        "object": str,
        "system_fingerprint": str,
        "choices": list[Choice],
    },
)


async def handle_litellm_tool_calls(
    response: LiteLLMResponse,
    user_id: str,
    call_functions: list[Function],
    variables: Optional[dict[str, Any]] = None,
) -> list[FunctionCallOutput]:
    """
    Processes multiple tool calls from LiteLLM's response and executes the corresponding functions.

    Args:
        response: The LLM response possibly containing tool calls.
        user_id: The user ID on whose behalf the Integry function will be called.
        call_functions: A list of functions that can be called.
        variables: Additional variables passed to the callable function.

    Returns:
        A list of results from executed tool functions. The order of results matches the order of tool calls in the response.
    """
    choices = response["choices"]
    if not choices:
        return []

    tool_calls = choices[0]["message"].get("tool_calls")

    if not tool_calls:
        return []

    results: list[FunctionCallOutput] = []

    for tool_call in tool_calls:
        function_name = tool_call["function"]["name"]
        function_args = json.loads(tool_call["function"]["arguments"])

        matching_function = next(
            (
                func
                for func in call_functions
                if getattr(func, "name", None) == function_name
            ),
            None,
        )

        if matching_function is not None:
            result: FunctionCallOutput = await matching_function(
                user_id, function_args, variables
            )
            results.append(result)

    return results
