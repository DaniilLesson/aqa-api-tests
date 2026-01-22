from pydantic import BaseModel


class User(BaseModel):
    #Модель пользователя (контракт данных).

    id: int         
    name: str       
