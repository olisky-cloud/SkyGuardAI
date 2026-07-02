import requests
from config.config import TOKEN, CHAT_ID

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })
