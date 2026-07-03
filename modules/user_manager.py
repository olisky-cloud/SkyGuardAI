import json

FILE = "data/users.json"


def load_users():
    with open(FILE, "r") as f:
        return json.load(f)


def get_user(user_id):
    data = load_users()
    return data["users"].get(user_id, None)


def check_access(user_id, feature):
    user = get_user(user_id)

    if not user:
        return False

    plan = user["plan"]

    # FREE LIMITS
    if plan == "free":
        if feature in ["weather", "status"]:
            return True
        return False

    # PRO FULL ACCESS
    if plan == "pro":
        return True

    return False
