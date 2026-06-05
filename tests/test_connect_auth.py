"""Tests de l'authentification."""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import httpx
import pytest

from henrri_connect.connect.synchro import SyncHenrriClient
from henrri_connect.connect.asynchro import AsyncHenrriClient
from henrri_connect.exc import HenrriAuthError
from henrri_connect.models import TokenResponse # pylint: disable=W0611


def test_sync_headers_and_auth_flow(monkeypatch):   # pylint: disable=W0613, C0116
    client: SyncHenrriClient = SyncHenrriClient.__new__(SyncHenrriClient)
    client._client_id = "cid"   # pylint: disable=W0212
    client._client_secret = "csecret"   # pylint: disable=W0212
    client._base_url = "https://api.test"   # pylint: disable=W0212
    client._access_token = None # pylint: disable=W0212
    client._refresh_token_str = None    # pylint: disable=W0212
    client._http = MagicMock(spec=httpx.Client) # pylint: disable=W0212

    # _headers should raise when no token and authenticated=True
    with pytest.raises(HenrriAuthError):
        client._headers(authenticated=True)  # type: ignore[attr-defined]  # pylint: disable=W0212

    # with token, Authorization header present
    client._access_token = "tok" # pylint: disable=W0212
    headers = client._headers(authenticated=True)  # type: ignore[attr-defined]  # pylint: disable=W0212
    assert headers["Authorization"] == "Bearer tok"

    # Test _request handles 401 by calling _do_refresh when refresh token present
    resp1 = MagicMock(spec=httpx.Response)
    resp1.status_code = 401
    resp1.is_success = False
    resp1.json.return_value = {}

    resp2 = MagicMock(spec=httpx.Response)
    resp2.status_code = 200
    resp2.is_success = True
    resp2.json.return_value = {
        "accessToken": "newtok",
        "refreshToken": "newrefresh",
        "expiresIn": 3600
    }

    client._http.request.side_effect = [resp1, resp2] # pylint: disable=W0212
    client._access_token = "old" # pylint: disable=W0212
    client._refresh_token_str = "r" # pylint: disable=W0212

    # replace _do_refresh to set new token
    def _do_refresh():
        client._access_token = "newtok" # pylint: disable=W0212
    client._do_refresh = _do_refresh # pylint: disable=W0212

    out = client._request("GET", "/v1/test", authenticated=True)  # type: ignore[attr-defined]  # pylint: disable=W0212
    assert out is resp2
    assert client._access_token == "newtok" # pylint: disable=W0212
    assert client._http.request.call_count == 2 # pylint: disable=W0212


@pytest.mark.asyncio
async def test_async_headers_and_refresh(monkeypatch):  # pylint: disable=W0613, C0116
    client: AsyncHenrriClient = AsyncHenrriClient.__new__(AsyncHenrriClient)
    client._client_id = "cid" # pylint: disable=W0212
    client._client_secret = "csecret" # pylint: disable=W0212
    client._base_url = "https://api.test" # pylint: disable=W0212
    client._access_token = None # pylint: disable=W0212
    client._refresh_token_str = None # pylint: disable=W0212
    client._http = AsyncMock(spec=httpx.AsyncClient) # pylint: disable=W0212

    with pytest.raises(HenrriAuthError):
        client._headers(authenticated=True)  # type: ignore[attr-defined]  # pylint: disable=W0212

    client._access_token = "tok" # pylint: disable=W0212
    headers = client._headers(authenticated=True)  # type: ignore[attr-defined]  # pylint: disable=W0212
    assert headers["Authorization"] == "Bearer tok"

    resp1 = MagicMock(spec=httpx.Response)
    resp1.status_code = 401
    resp1.is_success = False
    resp1.json.return_value = {}

    resp2 = MagicMock(spec=httpx.Response)
    resp2.status_code = 200
    resp2.is_success = True
    resp2.json.return_value = {
        "accessToken": "newtok",
        "refreshToken": "newrefresh",
        "expiresIn": 3600
    }

    # first call: resp1, second call: resp2
    client._http.request.side_effect = [resp1, resp2] # pylint: disable=W0212

    client._access_token = "old" # pylint: disable=W0212
    client._refresh_token_str = "r" # pylint: disable=W0212

    async def _do_refresh():
        client._access_token = "newtok" # pylint: disable=W0212
    client._do_refresh = _do_refresh # pylint: disable=W0212

    out = await client._request("GET", "/v1/test", authenticated=True)  # type: ignore[attr-defined]  # pylint: disable=W0212
    assert out is resp2
    assert client._access_token == "newtok" # pylint: disable=W0212
    assert client._http.request.call_count == 2 # pylint: disable=W0212
