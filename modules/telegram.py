import requests
from config.config import TELEGRAM_TOKEN, CHAT_ID

URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"


def send_message(text):
    if not CHAT_ID:
        print("CHAT_ID fehlt")
        return

    requests.get(URL + f"/sendMessage?chat_id={CHAT_ID}&text={text}")

