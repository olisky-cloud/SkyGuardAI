import requests

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=47.76"
    "&longitude=8.84"
    "&current=temperature_2m,wind_speed_10m,precipitation"
)

print("Verbinde mit Open-Meteo...")

response = requests.get(url, timeout=10)

print("Status:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(response.text)
