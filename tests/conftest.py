import httpx
import pytest

from src.clients.reqres_client import ApiClient


@pytest.fixture
def api_mock():
    # Фикстура pytest, которая возвращает ApiClient с подменённым транспортом (MockTransport).

    def handler(request: httpx.Request) -> httpx.Response:

        if request.url.path == "/users/2":
            return httpx.Response(200, json={"id": 2, "name": "John"})
        

        if request.url.path == "/users/999":
            return httpx.Response(404, json={"detail": "not found"})
        

        if request.url.path == "/users/3":
            return httpx.Response(200, json={"id": "two"})
        

        return httpx.Response(404, json={"detail": "unknown route"})
    
    # Создаём MockTransport, который будет использовать handler вместо реального интернета
    transport = httpx.MockTransport(handler)

    # Создаём ApiClient с base_url "заглушкой" и нашим transport.
    with ApiClient(base_url="https://example.test", transport=transport) as api:

        yield api
