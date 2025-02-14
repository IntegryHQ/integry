import json
from typing import Any, Optional, Dict, List
from integry.resources.functions.types import Function

async def handle_litellm_tool_calls(
    response: dict[str, Any],
    user_id: str,
    call_functions: List[Function],
    variables: Optional[dict[str, Any]] = None,
) -> Optional[Dict[str, Any]]:
    """
    Processes multiple tool calls from LiteLLM's response and executes the corresponding function.

    Args:
        response (dict[str, Any]): The LLM response possibly containing tool calls.
        user_id (str): The user ID of the user on whose behalf the Integry function will be called.
        call_function (Callable[..., Any]): The function that should be called dynamically.
        variables (Optional[dict[str, Any]]): Additional variables passed to the callable function.

    Returns:
        Optional[Dict[str, Any]]: The result of the executed tool function, or None if no tool calls are found.
    """

    tool_calls = response.choices[0].message.tool_calls

    if tool_calls:
        for tool_call in tool_calls:
            function_args = json.loads(tool_call.function.arguments)

            for call_function in call_functions:
                return call_function._get_sync_callable(user_id, variables)(**function_args)

    return None
