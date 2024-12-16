from typing import AsyncIterator, Awaitable, Literal, Type, TypeVar
import httpx
from pydantic import BaseModel

from integry.exceptions import NotFound
from integry.utils.common import get_hash


class BaseResource:
    http_client: httpx.AsyncClient
    app_key: str
    app_secret: str
    name: Literal["functions"] | Literal["apps"]

    def __init__(
        self,
        client: httpx.AsyncClient,
        app_key: str,
        app_secret: str,
        resource: Literal["functions"] | Literal["apps"],
    ):
        self.http_client = client
        self.app_key = app_key
        self.app_secret = app_secret
        self.name = resource

    def _get_response_data_or_raise(self, response: httpx.Response):
        if response.status_code == 404:
            data = response.json()
            raise NotFound(data.get("detail"))

        if response.status_code != 200:
            raise Exception(response.content)

        return response.json()

    def _get_signed_request_headers(self, user_id: str):
        hash = get_hash(self.app_secret, user_id)
        return {"App-Key": self.app_key, "User-ID": user_id, "Hash": hash}


ResourceModel = TypeVar("ResourceModel", bound=BaseModel)
ResourcePage = TypeVar("ResourcePage", bound=BaseModel)


class AsyncPaginator(AsyncIterator[ResourceModel], Awaitable[ResourcePage]):
    _cursor_key = "_cursor"

    def __init__(
        self,
        resource: BaseResource,
        user_id: str,
        query_string: str,
        model: Type[ResourceModel],
        paginated_response_model: Type[ResourcePage],
        explicit_cursor: str = "",
    ):
        self._resource = resource
        self._user_id = user_id

        self._query_string = query_string
        self._data = []
        self._cursor = ""
        self._explicit_cursor = explicit_cursor

        self._model = model
        self._paginated_response_model = paginated_response_model

    def __aiter__(self):
        return self

    async def __anext__(self):
        if not self._data and self._cursor is not None:
            await self._populate_next_page()

        if not self._data:
            raise StopAsyncIteration

        return self._data.pop(0)

    def __await__(self):
        return self._get_data().__await__()

    async def _populate_next_page(self):
        self._data, self._cursor = await self._get_next_page(self._cursor)

    async def _get_data(self) -> ResourcePage:
        data, cursor = await self._get_next_page(self._explicit_cursor)

        if cursor is None:
            cursor = ""

        return self._paginated_response_model(
            cursor=cursor, **{self._resource.name: data}
        )

    async def _get_next_page(self, cursor) -> tuple[list[ResourceModel], str | None]:
        response = await self._resource.http_client.post(
            f"{self._resource.name}/list/{self._query_string}",
            headers=self._resource._get_signed_request_headers(self._user_id),
            json={self._cursor_key: cursor},
        )
        response_data = self._resource._get_response_data_or_raise(response)

        data = [
            self._model(**record, _resource=self._resource)
            for record in response_data.get(self._resource.name, [])
        ]
        next_cursor = response_data.get(self._cursor_key)
        return data, next_cursor
