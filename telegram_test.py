import requests

TOKEN = "8925927498:AAFJaTgsG2ID5OIbZCPMWXIrYV5s60FD-Mw"
CHAT_ID = "8941361378"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

r = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "✅ Testnachricht von SkyGuard AI"
})

print(r.status_code)
print(r.text)
