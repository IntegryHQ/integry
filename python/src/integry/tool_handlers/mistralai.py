import json
from typing import Any, TypedDict, Optional
from integry.resources.functions.types import Function, FunctionCallOutput

FunctionCall = TypedDict("FunctionCall", {"name": str, "arguments": str})

ToolCall = TypedDict(
    "ToolCall", {"function": FunctionCall, "id": str, "type": Optional[str]}
)

Message = TypedDict(
    "Message",
    {"role": str, "content": Optional[str], "tool_calls": Optional[list[ToolCall]]},
)

Choice = TypedDict(
    "Choice",
    {"index": int, "message": Message, "finish_reason": str},
)

MistralResponse = TypedDict(
    "MistralResponse",
    {
        "id": str,
        "created": int,
        "model": str,
        "object": str,
        "choices": list[Choice],
    },
)


async def handle_mistralai_tool_calls(
    response: MistralResponse,
    user_id: str,
    call_functions: list[Function],
    variables: Optional[dict[str, Any]] = None,
) -> list[FunctionCallOutput]:
    """
    Processes multiple tool calls from Mistral's response and executes the corresponding functions.

    Args:
        response: The Mistral response possibly containing tool calls.
        user_id: The user ID on whose behalf the Integry function will be called.
        call_functions: A list of functions that can be called.
        variables: Additional variables passed to the callable function.

    Returns:
        A list of results from executed tool functions. The order of results matches the order of tool calls in the response.
    """
    choices = getattr(response, "choices", [])
    if not choices:
        return []

    first_choice = choices[0]
    message = getattr(first_choice, "message", {})

    tool_calls = getattr(message, "tool_calls", [])
    if not tool_calls:
        return []

    results: list[FunctionCallOutput] = []

    for tool_call in tool_calls:
        function_data = getattr(tool_call, "function", {})
        function_name = getattr(function_data, "name", "")
        function_args = getattr(function_data, "arguments", "{}")

        function_args = (
            json.loads(function_args)
            if isinstance(function_args, str)
            else function_args
        )

        matching_function = next(
            (func for func in call_functions if func.name == function_name), None
        )

        if matching_function:
            result: FunctionCallOutput = await matching_function(
                user_id, function_args, variables
            )
            results.append(result)

    return results
