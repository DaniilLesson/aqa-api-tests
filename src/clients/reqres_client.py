import allure
import httpx

from src.config import BASE_URL, TIMEOUT_S
from src.models.user import UserData, UserResponse


class ApiClient:
    def __init__(
        self,
        base_url: str = BASE_URL,
        timeout_s: float = TIMEOUT_S,
        transport: httpx.BaseTransport | None = None,
    ):
        self._client = httpx.Client(
            base_url=base_url,  # базовый адрес API
            timeout=timeout_s,  # таймаут на запросы (в секундах)
            transport=transport,  # позволяет подменять сетевой слой (MockTransport)
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    @allure.step("GET /users/{user_id}")
    def get_user_raw(self, user_id: int) -> httpx.Response:
        # Делаем запрос и возвращаем httpx.Response.
        r = self._client.get(f"/users/{user_id}")

        allure.attach(
            f"status={r.status_code}\n\n{r.text[:2000]}",
            name="response",
            attachment_type=allure.attachment_type.TEXT,
        )
        return r

    @allure.step("Parse response to User model")
    def get_user(self, user_id: int) -> UserData:
        """
        Делает запрос и возвращает Pydantic-модель UserData.

        1) получаем Response
        2) если статус 4xx/5xx — выбрасываем исключение (raise_for_status)
        3) парсим JSON и валидируем его через Pydantic
        """
        r = self.get_user_raw(user_id)
        # Если статус не 2xx, будет исключение httpx.HTTPStatusError
        # (в негативных тестах проверяем через pytest.raises).
        r.raise_for_status()

        # Валидация полного ответа по контракту, затем возвращаем data как доменную сущность.
        payload = UserResponse.model_validate(r.json())
        return payload.data
