import json
from typing import Any, Callable, Optional, Dict


def handle_litellm_tool_calls(
    response: dict[str, Any],
    user_id: str,
    call_function: Callable[..., Any],
    variables: Optional[dict[str, Any]] = None,
) -> Optional[Dict[str, Any]]:
    """
    Processes multiple tool calls from LiteLLM's response and executes the corresponding function.

    Args:
        response (dict[str, Any]): The response dictionary containing tool call information.
        user_id (str): The user ID for authentication.
        call_function (Callable[..., Any]): The function that should be called dynamically.
        variables (Optional[dict[str, Any]]): Additional variables passed to the callable function.

    Returns:
        Optional[Dict[str, Any]]: The result of the executed tool function, or None if no tool calls are found.
    """

    def callable_function(**kwargs: dict[str, Any]) -> dict[str, Any]:
        """
        Calls the provided function with the given arguments.

        Args:
            **kwargs (dict[str, Any]): The keyword arguments required by the function.

        Returns:
            dict[str, Any]: The result of executing the callable function.
        """
        callable_instance = call_function._get_sync_callable(user_id, variables)
        result = callable_instance(**kwargs)
        return result

    tool_calls = response.choices[0].message.tool_calls

    if tool_calls:
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            if function_name == "callable_function":
                return callable_function(**function_args)

    return None
