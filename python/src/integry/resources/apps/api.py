from integry.resources.base import BaseResource, AsyncPaginator
from .types import App, AppsPage


class Apps(BaseResource):

    def list(self, user_id: str, cursor: str = "") -> AsyncPaginator[App, AppsPage]:
        """
        Lists all apps.

        Args:
            user_id: The ID of the user.
            cursor: Provide the cursor from last page to fetch the next page of apps.

        Returns:
            List of apps.
        """
        return AsyncPaginator(
            self,
            user_id,
            "",
            explicit_cursor=cursor,
            model=App,
            paginated_response_model=AppsPage,
        )

    async def get(self, app_name: str, user_id: str):
        """
        Gets an app by name.

        Args:
            app_name: The name of the app.
            user_id: The ID of the user.

        Returns:
            The app.
        """

        response = await self.http_client.post(
            f"{self.name}/{app_name}/get/",
            headers=self._get_signed_request_headers(user_id),
        )
        data = self._get_response_data_or_raise(response)

        return App(**data)

    async def is_connected(self, app_name: str, user_id: str) -> bool:
        """
        Returns whether user has connected an account of the app.

        Args:
            app_name: The name of the app.
            user_id: The ID of the user.

        Returns:
            Whether user has connected an account of the app.
        """

        response = await self.http_client.post(
            f"{self.name}/{app_name}/get/",
            headers=self._get_signed_request_headers(user_id),
        )

        data = self._get_response_data_or_raise(response)

        app = App(**data)
        return len(app.connected_accounts) > 0
