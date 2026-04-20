import unittest
import os
from integry import Integry
from datetime import datetime

APP_KEY = os.getenv("INTEGRY_APP_KEY")
APP_SECRET = os.getenv("INTEGRY_APP_SECRET")
USER_ID = os.getenv("INTEGRY_USER_ID")

class TestIntegryFunctionAPI(unittest.IsolatedAsyncioTestCase):
    """Test suite for the Integry Function API"""

    async def asyncSetUp(self):
        """Initialize Integry client asynchronously"""
        self.integry = Integry(app_key=APP_KEY, app_secret=APP_SECRET)
        self.user_id = USER_ID

    async def test_list_apps(self):
        """Test if listing apps returns a valid response"""
        response = await self.integry.apps.list(user_id=self.user_id)

        self.assertIsInstance(response, object, "Response should be an object")
        self.assertTrue(
            hasattr(response, "apps"), "Response should have an 'apps' attribute"
        )
        self.assertIsInstance(response.apps, list, "'apps' should be a list")
        self.assertGreater(len(response.apps), 0, "'apps' list should not be empty")

        for app in response.apps:
            with self.subTest(app=app.name):
                self.assertTrue(hasattr(app, "id"), "App should have an 'id'")
                self.assertTrue(hasattr(app, "name"), "App should have a 'name'")
                self.assertTrue(hasattr(app, "title"), "App should have a 'title'")
                self.assertTrue(
                    hasattr(app, "icon_url"), "App should have an 'icon_url'"
                )
                self.assertTrue(
                    hasattr(app, "login_url"), "App should have a 'login_url'"
                )
                self.assertTrue(
                    hasattr(app, "connected_accounts"),
                    "App should have 'connected_accounts'",
                )

        for app in response.apps:
            for account in app.connected_accounts:
                with self.subTest(app=app.name, account=account.display_name):
                    self.assertTrue(
                        hasattr(account, "id"), "ConnectedAccount should have an 'id'"
                    )
                    self.assertTrue(
                        hasattr(account, "display_name"),
                        "ConnectedAccount should have a 'display_name'",
                    )
                    self.assertTrue(
                        hasattr(account, "modified_at"),
                        "ConnectedAccount should have 'modified_at'",
                    )
                    self.assertIsInstance(
                        account.modified_at,
                        datetime,
                        "'modified_at' should be a datetime object",
                    )

    async def test_get_app(self):
        """Test if getting the App returns the correct structure"""

        response = await self.integry.apps.get("slack", user_id=self.user_id)
        
        self.assertTrue(hasattr(response, "id"), "App should have an 'id'")
        self.assertTrue(hasattr(response, "name"), "App should have a 'name'")
        self.assertTrue(hasattr(response, "title"), "App should have a 'title'")
        self.assertTrue(hasattr(response, "icon_url"), "App should have an 'icon_url'")
        self.assertTrue(hasattr(response, "login_url"), "App should have a 'login_url'")
        self.assertTrue(hasattr(response, "connected_accounts"), "App should have 'connected_accounts'")
        
        self.assertIsInstance(response.connected_accounts, list, "'connected_accounts' should be a list")
        for account in response.connected_accounts:
            self.assertTrue(hasattr(account, "id"), "ConnectedAccount should have an 'id'")
            self.assertTrue(hasattr(account, "display_name"), "ConnectedAccount should have a 'display_name'")
            self.assertTrue(hasattr(account, "modified_at"), "ConnectedAccount should have 'modified_at'")
            self.assertIsInstance(account.modified_at, datetime, "'modified_at' should be a datetime object")

    async def test_is_connected(self):
        """Test if the app is connected successfully"""
        response = await self.integry.apps.is_connected(
            app_name="slack",
            user_id=self.user_id,
        )

        self.assertIsInstance(response, bool, "Response should be a boolean")
        self.assertTrue(response, "App should be connected")


if __name__ == "__main__":
    unittest.main()
