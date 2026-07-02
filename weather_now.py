import requests

LAT = 47.76
LON = 8.84

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

temp = current["temperature_2m"]
wind = current["wind_speed_10m"]

# nächste Regenwahrscheinlichkeit
rain_prob = hourly["precipitation_probability"][0]

print("🌦 SkyGuard AI Wetter Singen\n")

print(f"🌡 Temperatur: {temp} °C")
print(f"💨 Wind: {wind} km/h")
print(f"🌧 Regenwahrscheinlichkeit: {rain_prob} %")

print("\n--- Bewertung ---")

# Windlogik
if wind > 40:
    print("🚨 STURMWARNUNG!")
elif wind > 25:
    print("⚠️ Starker Wind möglich.")
else:
    print("✅ Wind normal.")

# Regenlogik
if rain_prob > 80:
    print("☔ Hohe Regenwahrscheinlichkeit!")
elif rain_prob > 40:
    print("🌦 Möglicher Regen später.")
else:
    print("🌤 Eher trocken.")
