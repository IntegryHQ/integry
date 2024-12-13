from pydantic import BaseModel, Field, PositiveInt
from typing import Any, Dict, List, Union, Literal, Optional, Annotated, TYPE_CHECKING

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
    _cursor: str


class Function(BaseModel):
    name: str
    description: str
    parameters: JSONSchemaType
    arguments: dict[str, Any] = Field(default_factory=dict)

    _resource: "FunctionsResource"

    def __init__(self, **data: Any):
        super().__init__(**data)
        if isinstance(data, dict):
            self._resource = data["_resource"]

    async def __call__(
        self,
        user_id: str,
        arguments: dict[str, Any],
        variables: Optional[dict[str, Any]] = None,
    ) -> FunctionCallOutput:
        return await self._resource.call(self.name, arguments, user_id, variables)


class FunctionsPage(BaseModel):
    functions: list[Function]
    cursor: str


IncludeOptions = list[Literal["meta"]]

FunctionType = Literal["ACTION", "QUERY"]
