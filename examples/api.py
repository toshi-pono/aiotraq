from aiotraq import AuthenticatedClient
from aiotraq.api.channel import get_channels
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_ACCESS_TOKEN = os.getenv("BOT_ACCESS_TOKEN")

client = AuthenticatedClient(base_url="https://q.trap.jp/api/v3", token=BOT_ACCESS_TOKEN)

with client as client:
    channels = get_channels.sync_detailed(client=client)
    print(channels.status_code)
    # print(channels.parsed)

