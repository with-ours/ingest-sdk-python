# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import logging
from typing import Any, List

import pytest

from ours_privacy import OursPrivacy, APIStatusError
from ours_privacy._base_client import httpx

SECRET = "SENTINEL_SECRET_DO_NOT_LOG"
FIELD = "token"
BODY = {"event": "still_visible", FIELD: SECRET, "nested": [{FIELD: SECRET}]}


def make_client(handler: Any) -> OursPrivacy:
    return OursPrivacy(
        base_url="http://127.0.0.1:4010",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
        max_retries=0,
    )


def test_debug_log_redacts_secrets_without_changing_the_request(caplog: pytest.LogCaptureFixture) -> None:
    sent: List[bytes] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request.content)
        return httpx.Response(200, json={"ok": True}, headers={"set-cookie": "session=" + SECRET})

    with caplog.at_level(logging.DEBUG, logger="ours_privacy"):
        make_client(handler).post(
            "/foo",
            cast_to=httpx.Response,
            body=BODY,
            options={"headers": {"Authorization": "Bearer " + SECRET}},
        )

    assert SECRET not in caplog.text
    assert "still_visible" in caplog.text
    assert "***" in caplog.text
    assert SECRET in sent[0].decode()


def test_status_error_message_redacts_echoed_secrets() -> None:
    def handler(_request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, json={FIELD: SECRET, "code": "still_visible"})

    with pytest.raises(APIStatusError) as caught:
        make_client(handler).post("/foo", cast_to=httpx.Response, body=BODY)

    assert SECRET not in str(caught.value)
    assert SECRET not in repr(caught.value)
    assert "still_visible" in str(caught.value)
