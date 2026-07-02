import requests
from config.config import LAT, LON

def get_weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={LAT}&longitude={LON}"
        "&current=temperature_2m,wind_speed_10m"
        "&hourly=precipitation_probability"
    )

    data = requests.get(url, timeout=10).json()

    current = data["current"]
    hourly = data["hourly"]

    return {
        "temp": current["temperature_2m"],
        "wind": current["wind_speed_10m"],
        "rain": hourly["precipitation_probability"][0]
    }
