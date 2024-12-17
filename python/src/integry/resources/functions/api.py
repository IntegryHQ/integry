from typing import Any, Literal, Optional, List

import httpx

from integry.exceptions import FunctionCallError
from integry.resources.base import BaseResource, AsyncPaginator
from .types import (
    Function,
    FunctionCallOutput,
    FunctionsPage,
    IncludeOptions,
    FunctionType,
    PaginatedFunctionCallOutput,
)
from urllib.parse import urlencode


class Functions(BaseResource):

    def list(
        self,
        user_id: str,
        app: Optional[str] = None,
        connected_only: Optional[bool] = False,
        type: Optional[Literal["ACTION", "QUERY"]] = None,
        cursor: str = "",
        include: Optional[IncludeOptions] = None,
    ) -> AsyncPaginator[Function, FunctionsPage]:

        query_string = self._get_query_string(include, app, connected_only, type)
        return AsyncPaginator(
            self,
            user_id,
            query_string,
            explicit_cursor=cursor,
            model=Function,
            paginated_response_model=FunctionsPage,
        )

    async def predict(
        self,
        prompt: str,
        user_id: str,
        variables: Optional[dict[str, Any]] = None,
        predict_arguments: bool = False,
        connected_only: Optional[bool] = False,
        include: Optional[IncludeOptions] = None,
    ) -> List[Function]:
        query_string = self._get_query_string(
            include, None, connected_only, None, predict_arguments
        )

        body: dict = {"prompt": prompt}
        if variables:
            body["_variables"] = variables

        response = await self.http_client.post(
            f"functions/predict/{query_string}",
            headers=self._get_signed_request_headers(user_id),
            json=body,
        )
        data = self._get_response_data_or_raise(response)

        predicted_functions = data.get("functions", [])
        return [
            Function(**function, _resource=self) for function in predicted_functions
        ]

    async def get(
        self,
        function_name: str,
        user_id: str,
        prompt: str = "",
        variables: Optional[dict[str, Any]] = None,
        include: Optional[IncludeOptions] = None,
    ) -> Function:
        query_string = self._get_query_string(include, None, None, None)

        body = {}
        if prompt:
            body["prompt"] = prompt
        if variables:
            body["_variables"] = variables

        response = await self.http_client.post(
            f"functions/{function_name}/get/?{query_string}",
            headers=self._get_signed_request_headers(user_id),
            json=body,
        )
        data = self._get_response_data_or_raise(response)

        function = Function(**data, _resource=self)
        return function

    async def call(
        self,
        function_name: str,
        arguments: dict[str, Any],
        user_id: str,
        variables: Optional[dict[str, Any]] = None,
    ) -> FunctionCallOutput:
        """
        Calls a function with the given arguments and variables.

        Args:
            function_name: The name of the function to call.
            arguments: Values for the function's parameters.
            user_id: The user ID of the user on whose behalf the function will be called.
            variables: The variables to pass to the function, if any.

        Returns:
            The function's output.
        """

        if "cursor" in arguments:
            # LangChain doesn't support aliases in the arguments schema, so we
            # handle the cursor parameter.
            # TODO: Remove this once LangChain supports aliases in the arguments schema.
            arguments["_cursor"] = arguments["cursor"]

        response = await self.http_client.post(
            f"{self.name}/{function_name}/call/",
            headers=self._get_signed_request_headers(user_id),
            json={**arguments, "_variables": variables},
        )
        if response.status_code == 400:
            self._raise_function_call_exception(response)

        data = self._get_response_data_or_raise(response)

        if "_cursor" in data:
            return PaginatedFunctionCallOutput(**data)

        return FunctionCallOutput(**data)

    def call_sync(
        self,
        function_name: str,
        arguments: dict[str, Any],
        user_id: str,
        variables: Optional[dict[str, Any]] = None,
    ) -> FunctionCallOutput:
        """
        Calls a function synchronously with the given arguments and variables.

        Args:
            function_name: The name of the function to call.
            arguments: Values for the function's parameters.
            user_id: The user ID of the user on whose behalf the function will be called.
            variables: The variables to pass to the function, if any.

        Returns:
            The function's output.
        """

        if "cursor" in arguments:
            # LangChain doesn't support aliases in the arguments schema, so we
            # handle the cursor parameter.
            # TODO: Remove this once LangChain supports aliases in the arguments schema.
            arguments["_cursor"] = arguments["cursor"]

        response = httpx.post(
            f"{self.http_client.base_url}/{self.name}/{function_name}/call/",
            headers=self._get_signed_request_headers(user_id),
            json={**arguments, "_variables": variables},
        )
        if response.status_code == 400:
            self._raise_function_call_exception(response)

        data = self._get_response_data_or_raise(response)

        if "_cursor" in data:
            return PaginatedFunctionCallOutput(**data)

        return FunctionCallOutput(**data)

    def _raise_function_call_exception(self, response: Any):
        data = response.json()
        error_details = data.get("error_details")
        error_message = "Failed to call the function"
        errors = []

        if isinstance(error_details, dict):
            errors = [f"{key}: {value}" for key, value in error_details.items()]

        elif isinstance(error_details, list):
            errors = error_details

        raise FunctionCallError(error_message, errors=errors)

    @staticmethod
    def _get_query_string(
        include: Optional[IncludeOptions],
        app: str | None,
        connected_only: bool | None,
        type: FunctionType | None,
        predict_arguments: bool = False,
    ) -> str:
        query_params = {}
        if include:
            query_params["include"] = ",".join(include)
        if app:
            query_params["app"] = app
        if connected_only:
            query_params["connected_only"] = connected_only
        if type:
            query_params["type"] = type

        if predict_arguments:
            query_params["predict_arguments"] = "true" if predict_arguments else "false"

        query_string = urlencode(query_params, doseq=False)
        if query_string:
            query_string = f"?{query_string}"

        return query_string
