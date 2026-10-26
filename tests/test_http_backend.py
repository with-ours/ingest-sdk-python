"""Also runnable without dev dependencies: python tests/test_http_backend.py."""

from __future__ import annotations

import json
import asyncio
import unittest
import importlib.util
from typing import Any

import httpx2 as httpx

from ours_privacy import OursPrivacy, APIStatusError, AsyncOursPrivacy, DefaultAioHttpClient, httpx as sdk_httpx


class HTTPBackendTests(unittest.TestCase):
    def test_selected_backend(self) -> None:
        self.assertIs(sdk_httpx, httpx)

    def test_sync_requests(self) -> None:
        requests: list[httpx.Request] = []

        def respond(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            if len(requests) == 1:
                return httpx.Response(429, headers={"retry-after-ms": "1"})
            return httpx.Response(200, json={"success": True})

        with OursPrivacy(
            http_client=httpx.Client(transport=httpx.MockTransport(respond)),
            timeout=httpx.Timeout(10, read=5),
        ) as client:
            self.assertTrue(client.track.event(token="test-token", event="test-event").success)
            self.assertEqual(len(requests), 2)
            self.assertEqual(json.loads(requests[-1].content)["event"], "test-event")
            self.assertEqual(requests[-1].extensions["timeout"]["read"], 5)
            raw = client.post("/raw", cast_to=httpx.Response)
            self.assertIsInstance(raw, httpx.Response)
            with client.track.with_streaming_response.event(token="test-token", event="test-event") as response:
                self.assertTrue(response.parse().success)

    def test_async_requests(self) -> None:
        async def run() -> None:
            def respond(_request: httpx.Request) -> httpx.Response:
                return httpx.Response(200, json={"success": True})

            async with AsyncOursPrivacy(
                http_client=httpx.AsyncClient(transport=httpx.MockTransport(respond)),
                timeout=httpx.Timeout(10),
            ) as client:
                self.assertTrue((await client.track.event(token="test-token", event="test-event")).success)
                raw = await client.post("/raw", cast_to=httpx.Response)
                self.assertIsInstance(raw, httpx.Response)
                async with client.track.with_streaming_response.event(
                    token="test-token", event="test-event"
                ) as response:
                    self.assertTrue((await response.parse()).success)

        asyncio.run(run())

    def test_optional_aiohttp_backend(self) -> None:
        if importlib.util.find_spec("httpx_aiohttp") is None:
            with self.assertRaisesRegex(RuntimeError, "aiohttp.*extra"):
                DefaultAioHttpClient()
            return

        async def run() -> None:
            requests: list[bytes] = []

            async def respond(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
                try:
                    headers = await reader.readuntil(b"\r\n\r\n")
                    length = next(
                        int(line.split(b":", 1)[1])
                        for line in headers.split(b"\r\n")
                        if line.lower().startswith(b"content-length:")
                    )
                    requests.append(await reader.readexactly(length))
                    # A normal chunked response exercises aiohttp's real response parser.
                    writer.write(
                        b"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n"
                        b"Transfer-Encoding: chunked\r\nConnection: close\r\n\r\n"
                        b'11\r\n{"success": true}\r\n0\r\n\r\n'
                    )
                    await writer.drain()
                finally:
                    writer.close()
                    await writer.wait_closed()

            server = await asyncio.start_server(respond, "127.0.0.1", 0)
            port = server.sockets[0].getsockname()[1]
            async with server:
                async with AsyncOursPrivacy(
                    base_url=f"http://127.0.0.1:{port}",
                    http_client=DefaultAioHttpClient(),
                ) as client:
                    self.assertTrue((await client.track.event(token="test-token", event="test-event")).success)
                    async with client.track.with_streaming_response.event(
                        token="test-token", event="test-event"
                    ) as response:
                        self.assertTrue((await response.parse()).success)
            self.assertEqual(len(requests), 2)
            self.assertEqual(json.loads(requests[0])["event"], "test-event")

        asyncio.run(run())

    def test_status_errors(self) -> None:
        def respond(_request: httpx.Request) -> httpx.Response:
            return httpx.Response(400, json={"message": "bad request"})

        with OursPrivacy(http_client=httpx.Client(transport=httpx.MockTransport(respond))) as client:
            with self.assertRaises(APIStatusError) as caught:
                client.post("/error", cast_to=dict[str, Any])
            self.assertIsInstance(caught.exception.response, httpx.Response)
            self.assertEqual(caught.exception.status_code, 400)


if __name__ == "__main__":
    unittest.main()
