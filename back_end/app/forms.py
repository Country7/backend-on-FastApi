from typing import Optional  # Поддержка аннотации типов в Python
from pydantic import BaseModel # Pydantic проверяет данные и управляет настройками с помощью аннотаций типов Python


class UserCreateForm(BaseModel):
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    nickname: Optional[str] = None


class UserLoginForm(BaseModel):
  email: str
  password: str