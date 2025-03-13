import json
from typing import Any, Optional
from pydantic import BaseModel
from integry.resources.functions.types import Function, FunctionCallOutput


class FunctionCall(BaseModel):
    name: str
    arguments: str


class ToolCall(BaseModel):
    function: FunctionCall
    id: str
    type: Optional[str] = None


class Message(BaseModel):
    role: str
    content: Optional[str] = None
    tool_calls: Optional[list[ToolCall]] = None


class Choice(BaseModel):
    index: int
    message: Message
    finish_reason: str


class MistralResponse(BaseModel):
    id: str
    created: int
    model: str
    object: str
    choices: list[Choice]


async def handle_mistralai_tool_calls(
    response: MistralResponse,
    user_id: str,
    functions_to_call: list[Function],
    variables: Optional[dict[str, Any]] = None,
) -> list[FunctionCallOutput]:
    """
    Processes multiple tool calls from Mistral's response and executes the corresponding functions.

    Args:
        response: The Mistral response possibly containing tool calls.
        user_id: The user ID on whose behalf the Integry function will be called.
        functions_to_call: A list of functions that can be called.
        variables: Additional variables passed to the callable function.

    Returns:
        A list of results from executed tool functions. The order of results matches the order of tool calls in the response.
    """
    choices = response.choices
    if not choices:
        return []

    tool_calls = choices[0].message.tool_calls
    if not tool_calls:
        return []

    results: list[Any] = []

    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        matching_function = next(
            (
                func
                for func in functions_to_call
                if getattr(func, "name", None) == function_name
            ),
            None,
        )

        if matching_function is not None:
            result = await matching_function(user_id, function_args, variables)
            results.append(result)

    return results
