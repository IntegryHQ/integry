import json
from typing import Any, Optional, Dict, List
from integry.resources.functions.types import Function


async def handle_litellm_tool_calls(
    response: Dict[str, Any],
    user_id: str,
    call_functions: List[Function],
    variables: Optional[Dict[str, Any]] = None,
) -> Optional[List[Dict[str, Any]]]:
    """
    Processes multiple tool calls from LiteLLM's response and executes the corresponding function.

    Args:
        response: The LLM response possibly containing tool calls.
        user_id: The user ID on whose behalf the Integry function will be called.
        call_functions: A list of functions that can be dynamically called.
        variables: Additional variables passed to the callable function.

    Returns:
        A list of results from executed tool functions, or None if no tool calls are found.
    """
    tool_calls = response.choices[0].message.tool_calls;

    if not tool_calls:
        return None

    results = []

    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        for call_function in call_functions:
            if call_function.name == function_name:
                result = await call_function._get_callable(user_id, variables)(**function_args)
                results.append(result)

    return results if results else None