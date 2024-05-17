import os
from os.path import join, dirname
from dotenv import load_dotenv

from aiotraq import AuthenticatedClient
from aiotraq.api.message import post_direct_message
from aiotraq.models.post_message_request import PostMessageRequest
from aiotraq_bot import TraqHttpBot
from aiotraq_bot.models.event import DirectMessageCreatedPayload


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

BOT_ACCESS_TOKEN = os.getenv("BOT_ACCESS_TOKEN")
BOT_VERIFICATION_TOKEN = os.getenv("BOT_VERIFICATION_TOKEN")
assert BOT_ACCESS_TOKEN is not None

# Create a client
client = AuthenticatedClient(base_url="https://q.trap.jp/api/v3", token=BOT_ACCESS_TOKEN)
bot = TraqHttpBot(verification_token=BOT_VERIFICATION_TOKEN)


# Register DIRECT_MESSAGE_CREATED event
@bot.event()
async def on_direct_message_created(payload: DirectMessageCreatedPayload) -> None:
    user_id = payload.message.user.id
    message = PostMessageRequest(
        content="Hello, World!",
    )
    with client as cl:
        # Send a message to the user "Hello, World!"
        message = await post_direct_message.asyncio(user_id=user_id, client=cl, body=message)


# Run the bot
bot.run(port=8080)
