import unittest

import httpx

from aiotraq_bot import TraqHttpBot
from aiotraq_bot.bot import TraqHttpBotServer
from aiotraq_bot.models.event import PingPayload


class BotTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.events = []
        self.bot = TraqHttpBot("test-token")

        @self.bot.event()
        async def ping(payload: PingPayload, event, id):
            self.events.append((payload, event, id))

        server = TraqHttpBotServer("127.0.0.1", 8080, self.bot)
        self.client = httpx.AsyncClient(
            transport=httpx.ASGITransport(app=server.app), base_url="http://test"
        )
        self.headers = {
            "X-TRAQ-BOT-TOKEN": "test-token",
            "X-TRAQ-BOT-EVENT": "PING",
            "X-TRAQ-BOT-REQUEST-ID": "request-id",
        }

    async def asyncTearDown(self):
        await self.client.aclose()

    async def test_valid_event_is_parsed_and_dispatched(self):
        response = await self.client.post(
            "/", headers=self.headers, json={"eventTime": "2026-11-17T00:00:00Z"}
        )
        self.assertEqual(response.status_code, 204)
        payload, event, request_id = self.events[0]
        self.assertIsInstance(payload, PingPayload)
        self.assertEqual(payload.eventTime.year, 2026)
        self.assertEqual((event, request_id), ("PING", "request-id"))

    async def test_invalid_token_never_dispatches(self):
        self.headers["X-TRAQ-BOT-TOKEN"] = "wrong"
        response = await self.client.post("/", headers=self.headers, json={})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(self.events, [])

    async def test_invalid_payload_returns_bad_request(self):
        response = await self.client.post("/", headers=self.headers, json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.events, [])

    async def test_missing_event_header_returns_bad_request(self):
        del self.headers["X-TRAQ-BOT-EVENT"]
        response = await self.client.post("/", headers=self.headers, json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.events, [])
