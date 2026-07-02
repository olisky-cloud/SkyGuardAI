import requests
import time
from datetime import datetime

TOKEN = "DEIN_TOKEN"
CHAT_ID = "DEINE_CHAT_ID"

LAT = 47.76
LON = 8.84


def get_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LON}"
        "&current=temperature_2m,wind_speed_10m"
        "&hourly=precipitation_probability"
    )

    data = requests.get(url).json()

    current = data["current"]
    hourly = data["hourly"]

    return {
        "temp": current["temperature_2m"],
        "wind": current["wind_speed_10m"],
        "rain": hourly["precipitation_probability"][0]
    }


def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})


def is_morning():
    now = datetime.now()
    return now.hour == 8 and now.minute == 0


last_sent = None

while True:
    if is_morning():
        if last_sent != "sent":
            w = get_weather()

            msg = f"""🌅 Guten Morgen – SkyGuard AI

🌤 Wetter für Singen:
🌡 {w['temp']} °C
💨 Wind: {w['wind']} km/h
🌧 Regen: {w['rain']} %

Schönen Start in den Tag!"""

            send(msg)
            last_sent = "sent"

    else:
        last_sent = None

    time.sleep(30)
