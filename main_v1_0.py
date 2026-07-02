import time

from config.config import INTERVAL
from modules.weather import get_weather
from modules.telegram import send_message


def build_message(w):
    msg = f"""🌦 SkyGuard AI

🌡 Temperatur: {w['temp']} °C
💨 Wind: {w['wind']} km/h
🌧 Regen: {w['rain']} %
"""

    if w["wind"] > 40:
        msg += "\n🚨 STURMWARNUNG!"
    elif w["wind"] > 25:
        msg += "\n⚠️ Starker Wind möglich."

    if w["rain"] > 80:
        msg += "\n☔ Hohe Regenwahrscheinlichkeit!"

    return msg


def run_once():
    w = get_weather()
    msg = build_message(w)
    send_message(msg)


print("🌦 SkyGuard AI gestartet")

while True:
    run_once()
    time.sleep(INTERVAL)
print("================================")
print("      SkyGuard AI startet")
print("================================")
print("")
print("Willkommen!")
print("Das Projekt wurde erfolgreich gestartet.")
