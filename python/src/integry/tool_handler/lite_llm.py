import json
from typing import Any, Optional
from integry.resources.functions.types import Function


async def handle_litellm_tool_calls(
    response: dict[str, Any],
    user_id: str,
    call_functions: list[Function],
    variables: Optional[dict[str, Any]] = None,
) -> list[dict[str, Any]]:
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
    tool_calls = response.choices[0].message.tool_calls

    if not tool_calls:
        return []

    results = []

    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        matching_function = next(
            (func for func in call_functions if func.name == function_name), None
        )

        if matching_function:
            result = await matching_function._get_callable(user_id, variables)(
                **function_args
            )
            results.append(result)

    return results
