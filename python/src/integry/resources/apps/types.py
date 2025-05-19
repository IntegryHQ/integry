from pydantic import BaseModel, PositiveInt
from typing import List
from datetime import datetime


class ConnectedAccount(BaseModel):
    id: PositiveInt
    display_name: str
    modified_at: datetime


class App(BaseModel):
    id: PositiveInt
    name: str
    title: str
    icon_url: str
    docs_url: str
    login_url: str
    allow_multiple_connected_accounts: bool
    connected_accounts: List[ConnectedAccount]


class AppsPage(BaseModel):
    apps: list[App]
    cursor: str
