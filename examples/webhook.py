import os
from os.path import join, dirname
from dotenv import load_dotenv
from aiotraq import Client
from aiotraq.api.webhook import post_webhook
import hashlib
import hmac


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

WEBHOOK_ID = os.getenv("WEBHOOK_ID")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")


def main() -> None:
    client = Client(base_url="https://q.trap.jp/api/v3")

    with client as client:
        if WEBHOOK_ID is None or WEBHOOK_SECRET is None:
            print("WEBHOOK_ID or WEBHOOK_SECRET is not set.")
            return

        message = "Hello World!"
        # メッセージ本文をWebhookシークレットでHMAC-SHA1でハッシュ化した結果をhex形式で表した文字列
        # https://bot-console.trap.jp/docs/webhook/send
        secret = hmac.new(WEBHOOK_SECRET.encode(), message.encode(), hashlib.sha1).hexdigest()

        result = post_webhook.sync_detailed(
            client=client,
            webhook_id=WEBHOOK_ID,
            body=message,
            x_traq_signature=secret,
        )
        print(result)


if __name__ == "__main__":
    main()
