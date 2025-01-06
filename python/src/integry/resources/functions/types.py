from pydantic import BaseModel, Field
from typing import (
    Any,
    Awaitable,
    Callable,
    Dict,
    List,
    Union,
    Literal,
    Optional,
    Annotated,
    TYPE_CHECKING,
    cast,
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

    def get_langchain_tool[
        T
    ](
        self,
        from_function: Callable[..., T],
        user_id: str,
        variables: Optional[dict[str, Any]] = None,
    ) -> T:
        """
        Returns a LangChain tool for the function.

        Args:
            from_function: This should be LangChain's `StructuredTool.from_function` method.
            user_id: The user ID of the user on whose behalf the function will be called.
            variables: The variables to use for mapping the arguments, if applicable.

        Returns:
            The LangChain tool.
        """
        argument_schema = get_pydantic_model_from_json_schema(
            json_schema=self.get_json_schema()["parameters"],
        )

        tool = from_function(
            coroutine=self._get_callable(user_id, variables),
            func=self._get_sync_callable(user_id, variables),
            name=self.name,
            description=self.description,
            args_schema=argument_schema,
        )
        return tool

    def get_llamaindex_tool[
        T
    ](
        self,
        tool_from_defaults: Callable[..., T],
        tools_metadata: Callable[..., T],
        user_id: str,
    ) -> T:
        """
        Returns a llamaIndex tool for the function..

        Args:
            tool_from_defaults: This should be llamaIndex `FunctionTool.from_defaults` method.
            tools_metadata: LlamaIndex function that generates metadata for the tool.
            user_id: The user ID for authentication.

        Returns:
            llamaindex tool
        """

        async def execute_function(**kwargs: Dict[str, Any]) -> FunctionCallOutput:
            callable_function = self._get_callable(user_id=user_id)
            result = await callable_function(**kwargs)
            return result

        function_schema = get_pydantic_model_from_json_schema(
            json_schema=self.get_json_schema()["parameters"],
        )

        metadata = tools_metadata(
            name=self.name,
            description=self.description,
            fn_schema=function_schema,
        )

        async_fn: Callable[[Dict[str, Any]], Awaitable[Any]] = (
            lambda **kwargs: execute_function(**kwargs)
        )

        return tool_from_defaults(
            async_fn=async_fn,
            tool_metadata=metadata,
        )

    def register_with_autogen_agents(
        self,
        register_function: Callable[..., None],
        caller: Any,
        executor: Any,
        user_id: str,
        variables: Optional[dict[str, Any]] = None,
    ):
        """
        Registers the function as a tool with AutoGen caller and executor agents.

        Args:
            register_function: This should be AutoGen's `register_function` function (`from autogen import register_function`).
            caller: The caller agent.
            executor: The executor agent.
            user_id: The ID of the user on whose behalf the function will be called.
            variables: The variables to use for mapping the arguments, if applicable.

        """
        argument_schema = get_pydantic_model_from_json_schema(
            json_schema=self.get_json_schema()["parameters"],
        )

        async def autogen_function(input: Annotated[argument_schema, f"Input to the {self.name}."]) -> FunctionCallOutput:  # type: ignore
            args = cast(BaseModel, input).model_dump(by_alias=True, exclude_unset=True)
            return await self._resource.call(
                self.name,
                args,
                user_id,
                variables,
            )

        register_function(
            autogen_function,
            caller=caller,
            executor=executor,
            name=self.name,
            description=self.description,
        )

    async def __call__(
        self,
        user_id: str,
        arguments: dict[str, Any],
        variables: Optional[dict[str, Any]] = None,
    ) -> FunctionCallOutput:
        return await self._resource.call(self.name, arguments, user_id, variables)

    def _get_callable(
        self, user_id: str, variables: Optional[dict[str, Any]] = None
    ) -> Callable[..., Awaitable[FunctionCallOutput]]:

        async def callable(**arguments: dict[str, Any]) -> FunctionCallOutput:
            return await self._resource.call(self.name, arguments, user_id, variables)

        return callable

    def _get_sync_callable(
        self, user_id: str, variables: Optional[dict[str, Any]] = None
    ):
        def sync_callable(**arguments: dict[str, Any]) -> FunctionCallOutput:
            return self._resource.call_sync(self.name, arguments, user_id, variables)

        return sync_callable


class FunctionsPage(BaseModel):
    functions: list[Function]
    cursor: str


IncludeOptions = list[Literal["meta"]]

FunctionType = Literal["ACTION", "QUERY"]
