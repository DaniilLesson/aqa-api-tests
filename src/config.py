import os


BASE_URL = os.getenv("BASE_URL", "https://reqres.in/api")


def get_timeout() -> float:
    raw = os.getenv("TIMEOUT_S", "10")
    try:
        v = float(raw)
        return v if v > 0 else 10.0
    except ValueError:
        return 10.0


TIMEOUT_S = get_timeout()
