import unittest
import os
from integry import Integry

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
        response = await self.integry.functions.list(user_id=self.user_id)

        self.assertIsInstance(response.functions, list, "Response should be a list")
        self.assertGreater(len(response.functions), 0, "Response should not be empty")

        
        for item in response.functions:
            self.assertTrue(hasattr(item, "name"), "Each item should have a 'name' field")
            self.assertTrue(hasattr(item, "description"), "Each item should have a 'description' field")

            self.assertIsInstance(item.name, str, "'name' should be a string")
            self.assertIsInstance(item.description, str, "'description' should be a string")

    async def test_predict_function(self):
        """Test if the predict function returns the correct response format"""
        response = await self.integry.functions.predict(
            prompt="Send a message on Slack on random that contact just signed up! Include the contact's details.",
            user_id=self.user_id,
            predict_arguments=True,
            variables={"first_name": "John", "last_name": "Doe"},
        )

        self.assertIsInstance(response, list, "Response should be a list")
        self.assertGreater(len(response), 0, "Response list should not be empty")

        for function in response:
            self.assertTrue(hasattr(function, "name"), "Function should have a 'name'")
            self.assertTrue(
                hasattr(function, "parameters"), "Function should have 'parameters'"
            )
            self.assertTrue(
                hasattr(function, "arguments"), "Function should have 'arguments'"
            )
            self.assertIsInstance(
                function.arguments, dict, "Function arguments should be a dictionary"
            )
            self.assertGreater(
                len(function.arguments), 0, "Function arguments should not be empty"
            )

    async def test_get_function(self):
        """Test if fetching function returns the expected response format"""
        response = await self.integry.functions.get(
                "slack-post-message",
                prompt="prompt-goes-here",
                variables={},
                user_id=self.user_id,
            )
        
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(response.name, "slack-post-message", "Function name should be 'slack-post-message'")
        self.assertEqual(response.description, "Post a message in a channel", "Description should match")
        self.assertTrue(hasattr(response, "parameters"), "Response should have 'parameters'")

        parameters = response.parameters.properties if hasattr(response.parameters, "properties") else {}

        required_fields = ["channel", "text"]
        for field in required_fields:
            with self.subTest(field=field):
                self.assertIn(field, parameters, f"Response should have '{field}' key")

    async def test_call_function(self):
        """Test if calling a function returns the correct response format"""

        slack_app = await self.integry.apps.get("slack", user_id=self.user_id)

        response = await self.integry.functions.call(
            "slack-post-message",
            {
                "connected_account_id": slack_app.connected_accounts[0].id,
                "channel": "random",
                "text": "{first_name} {last_name} just signed up!"
            },
            self.user_id,
            {
                "first_name": "John",
                "last_name": "Doe"
            }
        )
        
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(getattr(response, "network_code", None), 200, "Response network code should be 200")
        self.assertTrue(response.output.get("ok"), "Response output should have 'ok' set to True")
        self.assertIn("channel", response.output, "Response should contain 'channel'")
        self.assertIn("message", response.output, "Response should contain 'message'")
        self.assertIn("text", response.output.get("message", {}), "Message should contain 'text'")
        self.assertEqual(response.output["message"].get("text"), "John Doe just signed up!", "Message text should match expected output")

    async def test_call_function_sync(self):
        """Test if calling a function synchronously returns the correct response format"""
        slack_app = await self.integry.apps.get("slack", user_id=self.user_id)

        response = self.integry.functions.call_sync(
            "slack-post-message",
            {
                "connected_account_id": slack_app.connected_accounts[0].id,
                "channel": "random",
                "text": "{first_name} {last_name} just signed up!"
            },
            self.user_id,
            {
                "first_name": "John",
                "last_name": "Doe"
            }
        )
        
        self.assertIsNotNone(response, "Response should not be None")
        self.assertEqual(getattr(response, "network_code", None), 200, "Response network code should be 200")
        self.assertTrue(response.output.get("ok"), "Response output should have 'ok' set to True")
        self.assertIn("channel", response.output, "Response should contain 'channel'")
        self.assertIn("message", response.output, "Response should contain 'message'")
        self.assertIn("text", response.output.get("message", {}), "Message should contain 'text'")
        self.assertEqual(response.output["message"].get("text"), "John Doe just signed up!", "Message text should match expected output")

if __name__ == "__main__":
    unittest.main()