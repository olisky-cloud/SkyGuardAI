import time
import requests
from datetime import datetime
from threading import Thread

from config.config import TELEGRAM_TOKEN, CHAT_ID, INTERVAL


# -----------------------------
# SERVER
# -----------------------------
SERVER_URL = "http://127.0.0.1:8000"


def get_server_weather():
    try:
        r = requests.get(SERVER_URL + "/weather", timeout=3)
        return r.json()
    except:
        return {"temp": 0, "wind": 0, "rain": 0}


# -----------------------------
# TELEGRAM
# -----------------------------
URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"


def send_message(text):
    if not CHAT_ID:
        print("CHAT_ID fehlt")
        return
    requests.get(URL + f"/sendMessage?chat_id={CHAT_ID}&text={text}")


# -----------------------------
# COMMANDS
# -----------------------------
def handle_command(text):
    text = text.lower()

    if text == "/start":
        return "🤖 Atlas aktiv"

    if text == "/status":
        return "🟢 System läuft stabil"

    if text == "/weather":
        w = get_server_weather()
        return f"""🌦 Wetter

🌡 {w['temp']}°C
💨 {w['wind']} km/h
🌧 {w['rain']}%"""

    if text == "/help":
        return "/start /status /weather /help"

    return "❓ Unbekannt"


# -----------------------------
# TELEGRAM POLLING
# -----------------------------
last_update_id = 0


def telegram_loop():
    global last_update_id

    print("📡 Telegram aktiv")

    while True:
        try:
            r = requests.get(URL + "/getUpdates").json()

            for update in r.get("result", []):
                uid = update["update_id"]

                if uid <= last_update_id:
                    continue

                last_update_id = uid

                msg = update.get("message", {})
                text = msg.get("text", "")
                chat_id = msg.get("chat", {}).get("id")

                if text:
                    response = handle_command(text)
                    requests.get(URL + f"/sendMessage?chat_id={chat_id}&text={response}")

            time.sleep(2)

        except Exception as e:
            print("Error:", e)
            time.sleep(5)


# -----------------------------
# MAIN LOOP
# -----------------------------
def run_loop():
    while True:
        print("🤖 Atlas läuft... " + str(datetime.now()))
        time.sleep(INTERVAL)


# -----------------------------
# START
# -----------------------------
print("🚀 Atlas startet...")

Thread(target=telegram_loop, daemon=True).start()
run_loop()
