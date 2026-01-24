from pydantic import BaseModel

class UserData(BaseModel):
    """Модель пользователя из блока data."""

    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    """Блок поддержки из ответа API."""

    url: str
    text: str


class UserResponse(BaseModel):
    # Структура ответа reqres.in для GET /users/{id}.
    data: UserData
    support: Support | None = None