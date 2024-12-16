import httpx

from integry.resources.functions.api import Functions
from integry.resources.apps.api import Apps


class Integry(httpx.AsyncClient):

    apps: Apps
    functions: Functions

    app_key: str
    app_secret: str

    def __init__(self, app_key: str, app_secret: str, *args, **kwargs):
        if not app_key:
            raise Exception("app_key must be provided when initializing Integry")

        if not app_secret:
            raise Exception("app_secret must be provided when initializing Integry")

        self.app_key = app_key
        self.app_secret = app_secret

        self.functions = Functions(self, app_key, app_secret, "functions")
        self.apps = Apps(self, app_key, app_secret, "apps")

        super().__init__(*args, **kwargs, base_url="https://api.integry.io", timeout=30)
