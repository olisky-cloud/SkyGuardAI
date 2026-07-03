from fastapi import FastAPI

app = FastAPI()

# -------------------------
# BASIC STATUS
# -------------------------
@app.get("/status")
def status():
    return {
        "bot": "Atlas",
        "status": "online"
    }


# -------------------------
# SIMPLE WEATHER MOCK
# -------------------------
@app.get("/weather")
def weather():
    return {
        "temp": 20,
        "wind": 15,
        "rain": 10
    }
