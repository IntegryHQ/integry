from pydantic import BaseModel, Field
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Union,
    Literal,
    Optional,
    Annotated,
    TYPE_CHECKING,
)

from integry.utils.pydantic import get_pydantic_model_from_json_schema

if TYPE_CHECKING:
    from integry.resources.functions.api import Functions as FunctionsResource


class StringSchema(BaseModel):
    type: Literal["string"]


class NumberSchema(BaseModel):
    type: Literal["number"]


class BooleanSchema(BaseModel):
    type: Literal["boolean"]


class NullSchema(BaseModel):
    type: Literal["null"]


class ObjectSchema(BaseModel):
    type: Literal["object"]
    properties: Dict[str, "JSONSchemaType"] = Field(default_factory=dict)
    required: List[str] = []
    additionalProperties: Union["JSONSchemaType", bool] = True


class ArraySchema(BaseModel):
    type: Literal["array"]
    items: Union["JSONSchemaType", List["JSONSchemaType"], None] = None


JSONSchemaType = Annotated[
    StringSchema
    | NumberSchema
    | BooleanSchema
    | NullSchema
    | ObjectSchema
    | ArraySchema,
    Field(discriminator="type"),
]


class FunctionCallOutput(BaseModel):
    network_code: int
    output: Any


class PaginatedFunctionCallOutput(FunctionCallOutput):
    cursor: str = Field(alias="_cursor")


class Function(BaseModel):
    name: str
    description: str
    parameters: JSONSchemaType
    arguments: dict[str, Any] = Field(default_factory=dict)

    _json_schema: dict[str, Any]
    _resource: "FunctionsResource"

    def __init__(self, **data: Any):
        super().__init__(**data)

        self._resource = data.pop("_resource")

        self._json_schema = data

    def get_json_schema(self) -> dict[str, Any]:
        """
        Returns the JSON schema of the function which can be passed directly to an LLM.

        Returns:
            The JSON schema.
        """
        return self._json_schema

    def _get_callable(self, user_id: str):
        return FunctionCallable(self._resource, self.name, user_id)

    def as_langchain_tool[T](self, from_function: Callable[..., T], user_id: str) -> T:
        """
        Returns a LangChain tool for the function.

        Args:
            from_function: This should be LangChain's `StructuredTool.from_function` method.
            user_id: The user ID of the user on whose behalf the function will be called.

        Returns:
            The LangChain tool.
        """
        argument_schema = get_pydantic_model_from_json_schema(
            json_schema=self.get_json_schema()["parameters"],
        )

        tool = from_function(
            coroutine=self._get_callable(user_id),
            name=self.name,
            description=self.description,
            args_schema=argument_schema,
        )
        return tool

    async def __call__(
        self,
        user_id: str,
        arguments: dict[str, Any],
        variables: Optional[dict[str, Any]] = None,
    ) -> FunctionCallOutput:
        return await self._resource.call(self.name, arguments, user_id, variables)


class FunctionCallable:
    def __init__(
        self,
        resource: "FunctionsResource",
        name: str,
        user_id: str,
        variables: Optional[dict[str, Any]] = None,
    ):
        self._resource = resource
        self._name = name
        self._user_id = user_id
        self._variables = variables

    async def __call__(
        self,
        **arguments: dict[str, Any],
    ) -> FunctionCallOutput:
        return await self._resource.call(
            self._name, arguments, self._user_id, self._variables
        )


class FunctionsPage(BaseModel):
    functions: list[Function]
    cursor: str


IncludeOptions = list[Literal["meta"]]

FunctionType = Literal["ACTION", "QUERY"]
