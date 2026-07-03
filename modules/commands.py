from modules.weather import get_weather
from modules.updater import pull_update


def handle_command(text):
    text = text.lower().strip()

    if text == "/status":
        return "🤖 Atlas läuft stabil."

    if text == "/weather":
        w = get_weather()
        return f"""🌦 Wetter:
🌡 {w['temp']}°C
💨 {w['wind']} km/h
🌧 {w['rain']}%"""

    if text == "/update":
        pull_update()
        return "🔄 Update ausgeführt."

    if text == "/help":
        return """📲 Commands:
/status
/weather
/update
/help"""

    return "❓ Unbekannter Befehl. Tippe /help"
