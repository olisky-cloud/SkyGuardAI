# 🌦 SkyGuard AI

**SkyGuard AI** ist ein Open-Source Wetterassistent für Android (Termux), der Wetterdaten in Echtzeit abruft und automatisch über Telegram sendet.

Entwickelt für 24/7 Betrieb auf Smartphones ohne PC.

---

## 🚀 Features

- 🌡 Echtzeit Wetterdaten (Open-Meteo API)
- 🌧 Regenwahrscheinlichkeit
- 💨 Windanalyse
- 🚨 Sturmwarnungen
- 📲 Telegram Benachrichtigungen
- 🔁 Automatischer 30-Minuten Zyklus
- 🧠 Modulare Struktur (leicht erweiterbar)

---

## 📱 Installation (Termux)

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/olisky-cloud/SkyGuardAI.git
cd SkyGuardAI
pip install -r requirements.txt
python main.py
