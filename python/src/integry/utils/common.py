import hashlib, hmac


def get_hash(app_secret: str, user_id: str):
    hash = hmac.new(
        bytearray(app_secret, "utf-8"),
        bytearray(user_id, "utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()
    return hash
