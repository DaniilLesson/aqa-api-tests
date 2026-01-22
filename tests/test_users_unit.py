import httpx
from src.clients.reqres_client import ApiClient


def test_get_user_unit_mocktransport():
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert request.url.path == "/users/2"
        return httpx.Response(200, json={"id": 2, "name": "John"})

    transport = httpx.MockTransport(handler)

    api = ApiClient(base_url="https://example.test", transport=transport)
    user = api.get_user(2)
    api.close()

    assert user.id == 2
    assert user.name == "John"

def test_get_user_unit(api_mock):
    user = api_mock.get_user(2)
    assert user.id == 2
