from typing import Optional, Type, Any
from pydantic import BaseModel, Field, create_model
from pydantic.fields import FieldInfo
from pydantic_core import PydanticUndefined


def get_pydantic_model_from_json_schema(json_schema: dict[str, Any]) -> Type[BaseModel]:
    """
    Generates a Pydantic model class using the provided JSON schema.

    Args:
        json_schema: The JSON schema to create the Pydantic model from.

    Returns:
        A subclass of Pydantic's BaseModel class to be used as argument schema in various agentic frameworks.
    """
    title = json_schema.get("title", "")
    fields = {}

    for key, schema in json_schema.get("properties", {}).items():
        updated_key, field_info = get_pydantic_field_from_json_schema(
            key, schema, json_schema.get("required", [])
        )
        fields[updated_key] = field_info

    return create_model(title, **fields)  # type: ignore


JSON_SCHEMA_TYPE_TO_NATIVE_TYPE_MAP: dict[str, Type[Any]] = {
    "boolean": bool,
    "number": float,
    "string": str,
    "array": list,
    "object": dict,
}


def get_pydantic_type_from_json_schema(
    json_schema: dict[str, Any],
) -> Type[Any]:
    _type = json_schema.get("type")
    if not isinstance(_type, str):
        raise ValueError(f"type must be a string, got: {_type}")

    native_type = JSON_SCHEMA_TYPE_TO_NATIVE_TYPE_MAP.get(_type)
    if native_type is None:
        raise ValueError(f"Unsupported type: {_type}")

    if _type == "array" and (items_schema := json_schema.get("items")):
        return list[get_pydantic_type_from_json_schema(items_schema)]

    if _type == "object":
        if not json_schema.get("properties"):
            # This occurs for custom fields parameters whose properties are only known
            # at runtime.
            return dict[str, Any]

        return get_pydantic_model_from_json_schema(json_schema)

    return native_type


def get_pydantic_field_from_json_schema(
    name: str,
    json_schema: dict[str, Any],
    required: list[str],
) -> tuple[str, tuple[Type[Any], FieldInfo]]:
    keywords = ["_cursor"]

    description = json_schema.get("description")
    default = json_schema.get("default", PydanticUndefined)

    alias = None
    if name in keywords:
        name = name.lstrip("_")
        # alias = name
    elif name.startswith("_"):
        # Pydantic does not allow fields to start with an underscore
        # TODO: Once Langchain fixes/adds support for aliases, use alias instead of raising exception
        raise ValueError(
            f"Parameters with names starting with an underscore are not supported: {name}"
        )
        alias = name
        name = name.lstrip("_")

    _type = get_pydantic_type_from_json_schema(
        json_schema,
    )

    if name not in required:
        default = None

    field_info = (
        _type,
        Field(
            description=description,
            default=default,
            alias=alias,
        ),
    )

    return (name, field_info)
