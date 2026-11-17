import unittest
from http import HTTPStatus

import httpx

from aiotraq import AuthenticatedClient, Client
from aiotraq.api.public import get_server_version
from aiotraq.errors import UnexpectedStatus


VERSION = {
    "revision": "test-revision",
    "version": "3.0.0",
    "flags": {"externalLogin": [], "signUpAllowed": False},
}


class ClientTests(unittest.TestCase):
    def test_sync_request_authentication_and_model(self):
        requests = []

        def respond(request):
            requests.append(request)
            return httpx.Response(200, json=VERSION)

        with AuthenticatedClient(
            base_url="https://example.invalid/api/v3",
            token="test-token",
            httpx_args={"transport": httpx.MockTransport(respond)},
        ) as client:
            result = get_server_version.sync_detailed(client=client)
        self.assertEqual(result.status_code, HTTPStatus.OK)
        self.assertEqual(result.parsed.version, "3.0.0")
        self.assertEqual(result.parsed.to_dict(), VERSION)
        self.assertEqual(requests[0].url.path, "/api/v3/version")
        self.assertEqual(requests[0].headers["Authorization"], "Bearer test-token")
        self.assertTrue(client.get_httpx_client().is_closed)

    def test_undocumented_error_is_raised_when_requested(self):
        with Client(
            base_url="https://example.invalid",
            raise_on_unexpected_status=True,
            httpx_args={"transport": httpx.MockTransport(lambda _: httpx.Response(503))},
        ) as client:
            with self.assertRaises(UnexpectedStatus):
                get_server_version.sync(client=client)


class AsyncClientTests(unittest.IsolatedAsyncioTestCase):
    async def test_async_request_and_cleanup(self):
        def respond(request):
            self.assertEqual(request.headers["Authorization"], "Bearer test-token")
            return httpx.Response(200, json=VERSION)

        async with AuthenticatedClient(
            base_url="https://example.invalid/api/v3",
            token="test-token",
            httpx_args={"transport": httpx.MockTransport(respond)},
        ) as client:
            result = await get_server_version.asyncio(client=client)
        self.assertEqual(result.revision, "test-revision")
        self.assertTrue(client.get_async_httpx_client().is_closed)
