import requests
import time

# =========================
# 🔧 KONFIGURATION
# =========================

TOKEN = "8635923841:AAHN8IQgKhS8mMrgB9lseYYcXSknTj0K7Cg"
CHAT_ID = "8941361378"

LAT = 47.76
LON = 8.84


# =========================
# 🌦️ WETTER ABRUF
# =========================

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


# =========================
# 🌿 ALLERGIE SYSTEM
# =========================

def allergy_risk(temp, wind, rain):
    score = 0

    if temp > 15:
        score += 1
    if temp > 25:
        score += 1

    if wind > 20:
        score += 1
    if wind > 40:
        score += 1

    if rain > 50:
        score -= 2
    elif rain > 20:
        score -= 1

    if score <= 0:
        return "🟢 Niedrig"
    elif score == 1:
        return "🟡 Mittel"
    else:
        return "🔴 Hoch"


# =========================
# 🧠 NACHRICHT ERSTELLEN
# =========================

def build_message(w):
    allergy = allergy_risk(w["temp"], w["wind"], w["rain"])

    msg = f"""🌦 SkyGuard AI – Singen

🌡 Temperatur: {w['temp']} °C
💨 Wind: {w['wind']} km/h
🌧 Regen: {w['rain']} %

🌿 Allergie-Risiko: {allergy}
"""

    if w["wind"] > 40:
        msg += "\n🚨 STURMWARNUNG!"
    elif w["wind"] > 25:
        msg += "\n⚠️ Starker Wind möglich."

    if w["rain"] > 80:
        msg += "\n☔ Hohe Regenwahrscheinlichkeit!"

    return msg


# =========================
# 📲 TELEGRAM SEND
# =========================

def send(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })


# =========================
# 🔁 EIN DURCHLAUF
# =========================

def run_once():
    w = get_weather()
    msg = build_message(w)
    send(msg)


# =========================
# 🚀 START
# =========================

print("🌦 SkyGuard AI gestartet")

while True:
    run_once()
    time.sleep(10)  # 30 Minuten
