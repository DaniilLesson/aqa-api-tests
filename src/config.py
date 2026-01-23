import os


BASE_URL = os.getenv("BASE_URL", "https://reqres.in")  # Базовый URL для API.

def get_timeout() -> float:
    raw = os.getenv("TIMEOUT_S", "10")
    try:
        return float(raw)
    except ValueError:
        return 10.0

TIMEOUT_S = get_timeout()  # Итоговый таймаут для клиента (всегда число).
