from unittest.mock import patch, MagicMock, AsyncMock

import httpx
import pytest

from integry import Integry


def _make_response(json_data, headers=None, status_code=200):
    return httpx.Response(
        status_code=status_code,
        headers=headers or {},
        json=json_data,
        request=httpx.Request("POST", "https://api.integry.io/functions/foo/call/"),
    )


@pytest.mark.asyncio
async def test_call_returns_credits_and_session_id_from_headers():
    integry = Integry(app_key="k", app_secret="s")
    response = _make_response(
        {"network_code": 200, "output": {"ok": True}},
        headers={"X-Credits": "7", "X-Session-ID": "sess-xyz"},
    )

    with patch.object(integry, "post", AsyncMock(return_value=response)):
        result = await integry.functions.call("foo", {}, user_id="u")

    assert result.credits == 7
    assert result.session_id == "sess-xyz"


@pytest.mark.asyncio
async def test_call_headers_absent_returns_none():
    integry = Integry(app_key="k", app_secret="s")
    response = _make_response({"network_code": 200, "output": {}})

    with patch.object(integry, "post", AsyncMock(return_value=response)):
        result = await integry.functions.call("foo", {}, user_id="u")

    assert result.credits is None
    assert result.session_id is None


def test_call_sync_returns_credits_and_session_id_from_headers():
    integry = Integry(app_key="k", app_secret="s")
    response = _make_response(
        {"network_code": 200, "output": {"ok": True}},
        headers={"X-Credits": "3", "X-Session-ID": "sess-abc"},
    )

    with patch("integry.resources.functions.api.httpx.post", MagicMock(return_value=response)):
        result = integry.functions.call_sync("foo", {}, user_id="u")

    assert result.credits == 3
    assert result.session_id == "sess-abc"
