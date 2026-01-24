import httpx
from src.clients.reqres_client import ApiClient


def test_get_user_unit_mocktransport():
    # Unit-тест без интернета: проверяем работу ApiClient через MockTransport.

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert request.url.path == "/users/2"
        return httpx.Response(
            200,
            json={
                "data": {
                    "id": 2,
                    "email": "john@example.com",
                    "first_name": "John",
                    "last_name": "Doe",
                    "avatar": "https://example.com/avatar.png",
                }
                # Держим структуру как в reqres.in, чтобы unit-тест проверял контракт.
            },
        )

    # Создаём MockTransport, который вместо реального интернета вызывает handler
    transport = httpx.MockTransport(handler)
    with ApiClient(base_url="https://example.test", transport=transport) as api:
        user = api.get_user(2)

    assert user.id == 2
    assert user.first_name == "John"
    assert user.last_name == "Doe"


def test_get_user_unit(api_mock):
    user = api_mock.get_user(2)

    assert user.id == 2
    assert user.first_name == "John"
