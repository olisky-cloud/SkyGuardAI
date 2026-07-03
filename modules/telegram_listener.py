import requests
import time
from config.config import TELEGRAM_TOKEN
from modules.commands import handle_command

URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

last_update_id = 0


def listen():
    global last_update_id

    print("📡 Telegram Listener gestartet")

    while True:
        try:
            r = requests.get(URL + "/getUpdates").json()

            for update in r.get("result", []):
                update_id = update["update_id"]

                if update_id <= last_update_id:
                    continue

                last_update_id = update_id

                message = update.get("message", {})
                text = message.get("text", "")
                chat_id = message.get("chat", {}).get("id")

                if text and chat_id:
                    response = handle_command(text)
                    send_message(chat_id, response)

            time.sleep(2)

        except Exception as e:
            print("Telegram Error:", e)
            time.sleep(5)


def send_message(chat_id, text):
    requests.get(URL + f"/sendMessage?chat_id={chat_id}&text={text}")
