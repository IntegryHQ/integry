from integry.resources.base import BaseResource, AsyncPaginator
from .types import App, AppsPage


class Apps(BaseResource):

    def list(self, user_id: str, cursor: str = "") -> AsyncPaginator[App, AppsPage]:
        return AsyncPaginator(
            self,
            user_id,
            "",
            explicit_cursor=cursor,
            model=App,
            paginated_response_model=AppsPage,
        )

    async def get(self, app_name: str, user_id: str):
        response = await self.http_client.post(
            f"{self.name}/{app_name}/get/",
            headers=self._get_signed_request_headers(user_id),
        )
        data = self._get_response_data_or_raise(response)

        return App(**data)

    async def is_connected(self, app_name: str, user_id: str) -> bool:
        response = await self.http_client.post(
            f"{self.name}/{app_name}/get/",
            headers=self._get_signed_request_headers(user_id),
        )

        data = self._get_response_data_or_raise(response)

        app = App(**data)
        return len(app.connected_accounts) > 0
