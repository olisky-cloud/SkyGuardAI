import time

from config.config import INTERVAL
from modules.weather import get_weather
from modules.telegram import send_message
from modules.logger import log


def build_message(w):
    msg = f"""🌦 SkyGuard AI

🌡 Temperatur: {w['temp']} °C
💨 Wind: {w['wind']} km/h
🌧 Regenwahrscheinlichkeit: {w['rain']} %
"""

    if w["wind"] >= 40:
        msg += "\n\n🚨 Sturmwarnung!"
    elif w["wind"] >= 25:
        msg += "\n\n⚠️ Starker Wind."

    if w["rain"] >= 80:
        msg += "\n☔ Hohe Regenwahrscheinlichkeit."

    return msg


def run_once():
    w = get_weather()

    log(f"Wetter: {w}")

    msg = build_message(w)

    send_message(msg)

    log("Telegram-Nachricht gesendet.")


def main():
    print("================================")
    print("      SkyGuard AI v1.0")
    print("================================")
    print("Überwachung gestartet.\n")

    while True:
        try:
            run_once()
        except Exception as e:
            print("Fehler:", e)
            log(f"FEHLER: {e}")

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
