import asyncio
import os
from os.path import join, dirname
from aiotraq_bot.models.event import MessageCreatedPayload
from dotenv import load_dotenv
import numpy as np
import pandas as pd

from aiotraq_bot import TraqHttpBot
from aiotraq_bot.models import DirectMessageCreatedPayload
from aiotraq_message import TraqMessageManager, TraqMessage


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

BOT_ACCESS_TOKEN = os.getenv("BOT_ACCESS_TOKEN")
BOT_VERIFICATION_TOKEN = os.getenv("BOT_VERIFICATION_TOKEN")
assert BOT_ACCESS_TOKEN is not None

# Create Bot instance
bot = TraqHttpBot(verification_token=BOT_VERIFICATION_TOKEN)
response = TraqMessageManager(bot, BOT_ACCESS_TOKEN, "https://q.trap.jp/api/v3", "https://q.trap.jp")

df = pd.DataFrame(
    {
        "A": [x for x in range(30)],
        "B": [x for x in range(30)],
        "C": [x for x in range(30)],
        "D": [x for x in range(30)],
        "E": [x * 20 for x in range(30)],
    }
)


# Create a component
async def component(am: TraqMessage, payload: str) -> None:
    am.write("Hello, World!")
    am.write(payload)
    # Yellow Image
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    image[:, :] = [0, 255, 255]
    am.image(image)

    # DataFrame
    am.dataframe(df)

    with am.spinner():
        await asyncio.sleep(5)

    am.write(":done: Done!")


# Register DIRECT_MESSAGE_CREATED event
@bot.event()
async def on_direct_message_created(payload: DirectMessageCreatedPayload) -> None:
    user_id = payload.message.user.id
    message = payload.message.plainText

    await response(component, user_id=user_id, payload=message)


# Register MESSAGE_CREATED event
@bot.event()
async def on_message_created(payload: MessageCreatedPayload) -> None:
    channel_id = payload.message.channelId
    message = payload.message.plainText

    await response(component, channnel_id=channel_id, payload=message)


# Run the bot
if __name__ == "__main__":
    bot.run(port=8080)
