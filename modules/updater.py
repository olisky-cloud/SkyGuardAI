import requests
import os
from config.version import VERSION

RAW_VERSION_URL = "https://raw.githubusercontent.com/olisky-cloud/SkyGuardAI/main/config/version.py"

def check_update():
    try:
        r = requests.get(RAW_VERSION_URL, timeout=10)
        remote_version = r.text.split('"')[1]

        if remote_version != VERSION:
            return True, remote_version

        return False, remote_version

    except Exception as e:
        return False, str(e)


def pull_update():
    os.system("git pull origin main")
