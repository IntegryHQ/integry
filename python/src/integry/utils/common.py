import hashlib, hmac
from typing import (
    Any,
)


def get_hash(app_secret: str, user_id: str):
    hash = hmac.new(
        bytearray(app_secret, "utf-8"),
        bytearray(user_id, "utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()
    return hash


def generate_docstring_from_schema_for_smolagent(schema: dict[str, Any]) -> str:
    """
    Generates a dynamic docstring based on a given JSON schema.

    Args:
        schema (dict): JSON schema containing parameter definitions.

    Returns:
        Formatted docstring with parameter details.
    """
    description = schema.get("description", "No description provided.")

    docstring = f"{description}\n\n"
    docstring += "Args:\n"
    docstring += f"    kwargs: A dictionary containing the following keys:\n"

    parameters = schema.get("parameters", {})
    properties = parameters.get("properties", {})
    required_fields = parameters.get("required", [])

    for param, details in properties.items():
        param_type = details.get("type")
        param_description = details.get("description", "No description available.")
        is_required = "(required)" if param in required_fields else "(optional)"
        docstring += f"    {param} ({param_type}): {param_description} {is_required}\n"

    docstring += f"\nReturns:\n  dict: Response for the {schema.get('name', '')}.\n"
    return docstring
