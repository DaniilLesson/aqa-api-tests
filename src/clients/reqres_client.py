import allure
import httpx

from src.config import BASE_URL, TIMEOUT_S
from src.models.user import User


class ApiClient:
    def __init__(
        self,
        base_url: str = BASE_URL,
        timeout_s: float = TIMEOUT_S,
        transport: httpx.BaseTransport | None = None,
    ):
        self._client = httpx.Client(base_url=base_url, timeout=timeout_s, transport=transport)

    def close(self) -> None:
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    @allure.step("GET /users/{user_id}")
    def get_user_raw(self, user_id: int) -> httpx.Response:
        r = self._client.get(f"/users/{user_id}")

        allure.attach(
            f"status={r.status_code}\n\n{r.text[:2000]}",
            name="response",
            attachment_type=allure.attachment_type.TEXT,
        )
        return r

    @allure.step("Parse response to User model")
    def get_user(self, user_id: int) -> User:
        r = self.get_user_raw(user_id)
        r.raise_for_status()
        return User.model_validate(r.json())

