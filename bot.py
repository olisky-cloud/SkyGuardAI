import requests
import time

TOKEN = "8635923841:AAHN8IQgKhS8mMrgB9lseYYcXSknTj0K7Cg"
CHAT_ID = "8941361378"

LAT = 47.76
LON = 8.84

def get_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}"
        f"&longitude={LON}"
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


def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })


while True:
    w = get_weather()

    message = f"""🌦 SkyGuard AI – Singen

🌡 Temperatur: {w['temp']} °C
💨 Wind: {w['wind']} km/h
🌧 Regen: {w['rain']} %
"""

    # Warnlogik
    if w["wind"] > 40:
        message += "\n🚨 STURMWARNUNG!"
    elif w["wind"] > 25:
        message += "\n⚠️ Starker Wind möglich."

    if w["rain"] > 80:
        message += "\n☔ Hohe Regenwahrscheinlichkeit!"

    send_telegram(message)

    time.sleep(1800)  # 30 Minuten
